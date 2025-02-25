# CLASE AERONAVE
# AUTORES: JHONEYKER DELGADO, EMMANUEL VALENCIA, SIMON GUARIN, CAMILO MIRANDA Y JACOBO LEAL.
from abc import ABC, abstractmethod


class Aeronave(ABC):

    # CONTRUCTOR
    def __init__(self, nombre, aerolinea=0):
        self.Gasto_gasolina = 10000
        self._descompuesto = False
        self._SILLAS_ECONOMICAS = []
        self._SILLAS_EJECUTIVAS = []
        self._nombre = nombre
        if aerolinea==0:
            self._aerolinea = None
        else:
            self._aerolinea = aerolinea

    # GET AND SET
    def getAerolinea(self):
        return self._aerolinea

    def setAerolinea(self, aerolinea):
        self._aerolinea = aerolinea

    def getSILLASECONOMICAS(self):
        return self._SILLAS_ECONOMICAS

    def setSILLASECONOMICAS(self, sILLAS_ECONOMICAS):
        self._SILLAS_ECONOMICAS = sILLAS_ECONOMICAS

    def getSILLASEJECUTIVAS(self):
        return self._SILLAS_EJECUTIVAS

    def setSILLASEJECUTIVAS(self, sILLAS_EJECUTIVAS):
        self._SILLAS_EJECUTIVAS = sILLAS_EJECUTIVAS

    def getGastoGasolina(self):
        return self.Gasto_gasolina

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # METODOS

    def isDescompuesto(self):
        return self._descompuesto

    def setDescompuesto(self, descompuesto):
        self._descompuesto = descompuesto

    def __str__(self):
        return self._nombre

    # BUSCAR SILLAS POR UBICACION Y TIPO
    #	EN ESTE METODO SE RECIBE UNA UBICACION(UBICACION) Y UN TIPO(STRING), LOS CUALES UTILIZA PARA BUSCAR DENTRO DE
    #	LAS LISTAS DE LA AERONAVE QUE LO LLAMA UNA SILLA CON LA UBICACION Y TIPO QUE SE INGRESAN.
    def buscarSillaPorUbicacionyTipo(self, ubicacion, tipo):
        from gestorAplicacion.hangar.Silla import Silla
        if tipo.lower() == "ECONOMICA".lower():
            for i in self._SILLAS_ECONOMICAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        elif tipo.lower() == "EJECUTIVA".lower():
            for i in self._SILLAS_EJECUTIVAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        return None
    #	ESTE METODO RECORRAN LOS ARREGLOS DE SILLAS EJECUTIVOS Y ECONOMICAS DE CADA AVION Y AVIONETA
    #	PARA VERIFICAR LA CANTIDAD DE SILLAS QUE ESTAN OCUPADAS Y RETORNAR DICHA CANTIDAD

    def Calcular_Sillas_Ocupadas(self):
        from gestorAplicacion.hangar.Silla import Silla
        contador=0
        for i in self._SILLAS_ECONOMICAS:
            if i.isEstado()== False:
                contador+=1
        for i in self._SILLAS_EJECUTIVAS:
            if i.isEstado()== False:
                contador+=1
        return "Esta es la cantidad de silla ocupadas: "+contador

    # ESTE METODO RECORRE LOS ARREGLOS DE SILLAS EJECUTIVAS Y ECONOMICAS DE LA AERONAVE QUE LO INVOQUE PARA VERIFICAR LA
	# CANTIDAD DE SILLAS QUE ESTAN OCUPADAS Y SI ESTAN TODAS OCUPADAS DEVUELVE TRUE QUE SIMBOLIZA QUE EL VUELO ESTA LLENO.
    def cambiarEstado(self):
        from gestorAplicacion.hangar.Silla import Silla
        contador=0
        for i in self._SILLAS_ECONOMICAS:
            if i.isEstado()== False:
                contador+=1
        for i in self._SILLAS_EJECUTIVAS:
            if i.isEstado()== False:
                contador+=1
        return contador==len(self.getSILLASECONOMICAS())+len(self.getSILLASEJECUTIVAS())

    # ESTE METODO RECIBE UNA AERONAVE Y UN IDENTIFICADOR, SI ESTE ES 1 QUIERE DECIR QUE ES UN AVION POR LO QUE
	# CREARA TODOS LOS OBJETOS SILLAS SEGUN LA CAPACIDAD DEL AVION Y DEPENDIENDO DE LA CLASE Y EL NUMERO DARA LA UBICACION
	# Y SI ES DISTINTO DE UNO QUIERE DECIR QUE CORRESPONDE A UNA AVIONETA Y HARA LO MISMO QUE PARA EL AVION SOLO QUE SEGUN
	# LA CAPACIDAD DE LA AVIONETA.
    def asignarParamatrosSilla(self,aeronave,identificador):
        from gestorAplicacion.hangar.Silla import Silla
        from gestorAplicacion.hangar.Clase import Clase
        from gestorAplicacion.hangar.Ubicacion import Ubicacion
        from gestorAplicacion.hangar.Avion import Avion
        from gestorAplicacion.hangar.Avioneta import Avioneta
        if identificador==1:
            # LA VARIABLE UBICACION VA CAMBIANDO SU VALOR SEGUN LOS SIGUIENTES PROCESOS, SE
            # USA PARA LA ASIGNACION DEL ATRIBUTO UBICACION DE LAS SILLAS.
            ubicacion = None

            # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS EJECUTIVAS QUE
            # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
            # NOTA: LAS SILLAS DE TIPO EJECUTIVA SE REPARTEN EN GRUPOS DE 4 EN FILA
            # SEPARADAS POR UN PASILLO.(POR TANTO NO HAY UBICACION CENTRAL)
            for numPosicion in range(0,Avion.getNumSillasEjecutivas()):
                if numPosicion%4 == 0 or numPosicion % 4 == 3:
                    ubicacion = Ubicacion.VENTANA
                else:
                    ubicacion = Ubicacion.PASILLO

                aeronave.getSILLASEJECUTIVAS().append( Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

            # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS ECONOMICAS QUE
            # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
            # NOTA: LAS SILLAS DE TIPO ECONOMICA SE REPARTEN EN GRUPOS DE 6 EN FILA
            # SEPARADAS POR UN PASILLO
            for numPosicion in range(0, Avion.getNumSillasEconomicas()):
                if numPosicion % 6 == 0 or numPosicion% 6 == 5:
                    ubicacion = Ubicacion.VENTANA
                elif numPosicion % 6 == 1 or numPosicion % 6 == 4:
                    ubicacion = Ubicacion.CENTRAL
                elif numPosicion % 6 == 2 or numPosicion % 6 == 3:
                    ubicacion = Ubicacion.PASILLO
                aeronave.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))
        else:
            # LA VARIABLE UBICACION VA CAMBIANDO SU VALOR SEGUN LOS SIGUIENTES PROCESOS, SE
            # USA PARA LA ASIGNACION DEL ATRIBUTO UBICACION DE LAS SILLAS.
            ubicacion = None

            # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS EJECUTIVAS QUE
            # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
            # NOTA: LAS SILLAS DE TIPO EJECUTIVA SE REPARTEN EN GRUPOS DE 4 EN FILA
            # SEPARADAS POR UN PASILLO.(POR TANTO NO HAY UBICACION CENTRAL)
            for numPosicion in range(0,Avioneta.getNumSillasEjecutivas()):
                if numPosicion%4 == 0 or numPosicion % 4 == 3:
                    ubicacion = Ubicacion.VENTANA
                else:
                    ubicacion = Ubicacion.PASILLO

                aeronave.getSILLASEJECUTIVAS().append( Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

            # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS ECONOMICAS QUE
            # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
            # NOTA: LAS SILLAS DE TIPO ECONOMICA SE REPARTEN EN GRUPOS DE 6 EN FILA
            # SEPARADAS POR UN PASILLO
            for numPosicion in range(0, Avioneta.getNumSillasEconomicas()):
                if numPosicion % 6 == 0 or numPosicion% 6 == 5:
                    ubicacion = Ubicacion.VENTANA
                elif numPosicion % 6 == 1 or numPosicion % 6 == 4:
                    ubicacion = Ubicacion.CENTRAL
                elif numPosicion % 6 == 2 or numPosicion % 6 == 3:
                    ubicacion = Ubicacion.PASILLO
                aeronave.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))


    #	METODO ABSTRACTO: ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
    #	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO
    @abstractmethod
    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        return distancia_en_km*self.GASTO_GASOLINA*0.05