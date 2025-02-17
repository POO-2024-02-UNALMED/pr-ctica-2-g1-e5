# CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA
import random
import pickle
from tkinter import *
from excepciones.ErrorAsignacion import ExcepcionAgregarAlojamiento, ExcepcionIdTiquete, ExcepcionIdVuelo, ExcepcionModificarAlojamiento
from excepciones.ErrorAplicacion import ErrorAplicacion
from excepciones.ErrorFormato import ExcepcionEnteroFloat, ExcepcionEnteroString

from gestorAplicacion.hangar.Clase import Clase
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Aerolinea import Aerolinea
from gestorAplicacion.adminVuelos.Pasajero import Pasajero
from gestorAplicacion.adminVuelos.Tiquete import Tiquete
from gestorAplicacion.adminVuelos.Vuelo import Vuelo
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Avion import Avion
from gestorAplicacion.hangar.Avioneta import Avioneta
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Ubicacion import Ubicacion



class Admin(object):

    # DESERIALIZACION DE DATOS
    picklefile = open('./baseDeDatos/Aerolineas','rb')
    picklefile2 = open('./baseDeDatos/Alojamientos','rb')
    Aerolinea.setAerolineas(pickle.load(picklefile))
    Alojamiento.setAlojamientos(pickle.load(picklefile2))
    picklefile.close()
    picklefile2.close()

    #--------------------------------------------------------------------------------------------------------------------------------------
    # MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN DISPONIBLES
    @staticmethod
    def mostrarVuelosPorAerolineas(frame_operaciones):
        aerolineasDisponibles = Aerolinea.getAerolineas()
        return Admin.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles,frame_operaciones)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RETORNA LA LISTA DE ALOJAMIENTOS DISPONIBLES CON SU NOMBRE Y LOCACION
    @staticmethod
    def obtenerAlojamientos():
        lista_alojamientos= Alojamiento.getAlojamientos()
        valores =[]

        for alojamiento in lista_alojamientos:
            valores.append(alojamiento.getNombre()+"---"+alojamiento.getLocacion())

        return valores

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN VUELO COMO PARAMETRO Y SE ENCARGA DE GENERAR UN TIQUETE CON UN iD ALEATORIO, QUE ES RETORNADO AL FINAL DEL METODO
    @staticmethod
    def generarTiquete(vuelo):

        ID_tiquete = 100 + random.random() * 900 # DEVUELVE UN NUMERO ALEATORIO DE 3 CIFRAS
        try:
            while Aerolinea.BuscarTiquete(int(ID_tiquete)) is not None:
                ID_tiquete = 100 + random.random() * 900
        except ExcepcionIdTiquete:
            tiquete = Tiquete(int(ID_tiquete), vuelo.getPrecio(), vuelo)
        return tiquete


    #--------------------------------------------------------------------------------------------------------------------------------------
    # CREA UN PASAJERO Y SE LO ASIGNA AL TIQUETE, POSTERIORMENTE SE LE ASIGNA EL PRECIO AL TIQUETE
    @staticmethod
    def asignarTiquete(datos,tiquete):

        nombre = datos[0]
        edad = int(datos[1])
        pasaporte = datos[2]
        correo = datos[-1]

        #SE CREA EL OBJETO PASAJERO Y SE LE ASIGNA AL TIQUETE GENERADO EN EL METODO
        pasajero = Pasajero(pasaporte, nombre, tiquete, edad, correo)
        tiquete.setPasajero(pasajero)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # BUSCA UN TIQUETE CON EL ID PASADO Y SE VERIFICA SI EL TIQUETE TIENE YA UN ALOJAMIENTO SELECCIONADO, SEGUN ESTO SE RETORNA UN TIQUETE
    # NONE O 2
    @staticmethod
    def buscarTiqueteYAlojamiento(id,numero):
        tiqueteID = int(id)
        tiquete_solicitado = Aerolinea.BuscarTiquete(tiqueteID)

        if tiquete_solicitado == None:
            raise ExcepcionIdTiquete(tiqueteID) # SI NO EXISTE EL TIQUETE

        elif tiquete_solicitado.getAlojamiento() != None:
            if numero == 1:
                raise ExcepcionAgregarAlojamiento(tiqueteID) # SI EL TIQUETE YA TIENE UN ALOJAMIENTO ASOCIADO
            else:
                return tiquete_solicitado
        else:
            if numero == 1:
                return tiquete_solicitado # SI HAY ALOJAMIENTOS DISPONIBLES EN EL LUGAR DE DESTINO
            else:
                raise ExcepcionModificarAlojamiento(tiqueteID)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN TIQUETE Y UN NOMBRE DE ALOJAMIENTO, PARA OBTENER EL DESTINO DEL TIQUETE Y POSTERIORMENTE BUSCAR EL ALOJAMIENTO
    # SOLICITADO POR SU NOMBRE
    @staticmethod
    def solicitarAlojamiento(tiquete_solicitado,alojamiento_nombre):
        destino = tiquete_solicitado.getVuelo().getDestino()
        alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento_nombre)

        if alojamiento_solicitado == None:
            return alojamiento_solicitado #SI NO ENCUENTRA UN ALOJAMIENTO CON ESE NOMBRE

        elif  alojamiento_solicitado.getLocacion().lower() != destino.lower():
            alojamiento_solicitado = None #SI LA LOCACION DEL ALOJAMIENTO ES DISTINTA DEL DESTINO DEL TIQUETE
            return alojamiento_solicitado

        else:
            return alojamiento_solicitado

    #--------------------------------------------------------------------------------------------------------------------------------------
    # SE LE PASA UN TIQUETE, UN ALOJAMIENTO Y UN NUMERO DE DIAS, PARA SETEARLE EL ALOJAMIENTO AL TIQUETE Y POSTERIORMENTE ASIGNARLE SU
    # PRECIO EN BASE AL NUMERO DE DIAS QUE SE QUEDARA EN EL ALOJAMIENTO
    @staticmethod
    def agregarAlojamiento(tiquete_solicitado,alojamiento_solicitado,num_dias):
        tiquete_solicitado.setAlojamiento(alojamiento_solicitado)
        tiquete_solicitado.asignarPrecio(int(num_dias))

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN NUMERO QUE INDICA SI SE ESTA AGREGANDO LA SILLA POR PRIMERA VEZ O SE ESTA MODIFICANDO, UN TIQUETE Y UNA SILLA
    # PARA ASIGNARSELA AL TIQUETE
    @staticmethod
    def modificarSilla(numero, tiquete,silla):
        if numero ==1 :
            tiquete.setSilla(silla)
        else:
            tiquete.getSilla().setEstado(True) #SE DESOCUPA LA SILLA QUE SE TENIA ANTERIORMENTE
            tiquete.setSilla(silla)
        tiquete.asignarPrecio() #SE RECALCULA EL PRECIO EN BASE A LA NUEVA SILLA

    #--------------------------------------------------------------------------------------------------------------------------------------
    #ESTE METODO RECIBE UN LABEL Y RETORNA UN LABEL. SU OBJETIVO ES MOSTRAR LAS LISTAS DE PASAJAEROS ASOCIADOS A UN VUELO.
    #PARA ESTO ACCEDEMOS A TRAVES DEL ID DEL VUELO E INVOCAMOS EL METODO BUSCAR VUELO POR ID. AL FINAL NOS MOSTRARA SI EL VUELO TIENE PASAJEROS
    # ASOCIADOS O NO, Y LA INFORMACION ASOCIADA AL ID DEL TIQUETE DEL PASAJAERO, SU NOMBRE, SU PASARTE Y SU EMAIL.
    @staticmethod
    def isFloat(s):
        try:
            float(s)
            raise ExcepcionEnteroFloat(s)
        except ValueError:
            return
    @staticmethod
    def listarPasajeros(valor,label):
        aerolineas = Aerolinea.getAerolineas()
        if not valor.isdigit():
            Admin.isFloat(valor)
            raise ExcepcionEnteroString(valor)

        IDBusqueda = int(valor)

        tiquetes = []
        vuelo = None
        for i in aerolineas:
            if i.buscarVueloPorID(i.getVuelos(), IDBusqueda) != None:
                vuelo = i.buscarVueloPorID(i.getVuelos(), IDBusqueda)
                break
        if vuelo ==None:
            raise ExcepcionIdVuelo(IDBusqueda)

        tiquetes = vuelo.getTiquetes()
        label["text"]+="LISTA DE PASAJEROS PARA EL VUELO " + str(IDBusqueda)

        if len(tiquetes) == 0:
            label["text"]+="\nEl vuelo aun no tiene pasajeros asociados \n"
        else: