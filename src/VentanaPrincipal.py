from tkinter import messagebox
from tkinter.ttk import Combobox
from excepciones.ErrorAplicacion import *
from excepciones.ErrorAsignacion import *
from excepciones.ErrorFormato  import *
from tkinter import *
from FieldFrame import *
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Aerolinea import Aerolinea
from tkinter import Tk
from PIL import Image, ImageTk
class VentanaSecundaria(Tk):

    en_uso = False #Permite saber si hay una ventanaSecundaria abierta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana secundaria")
        self.option_add('*tearOff', FALSE)
        self.title("Sistema de reserva de vuelos")
        self.geometry("850x560")
        self.minsize(850,560)
        self.iconbitmap('./imagenes/icono.ico')
        self.ventanaInicio = None
        self.focus()
        self.contador_mostrarVuelosPorAerolineas = 0

        self.option_add("*Label.font", ("Cascadia Code", 10))


        #ZONA DE Frames
        self.frame = Frame(self,relief="groove",bd=2, bg="#bae7ec")
        self.frame.pack(ipadx=50, padx=15,ipady=20,pady=15,expand=True,fill=BOTH)
        self.frame_proceso = Frame(self.frame,bg="#137a9b")
        self.frame_proceso.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
        self.frame_proceso.config(relief = "ridge")
        self.frame_proceso.config(bd=2)
        self.frame_descripcion = Frame(self.frame ,relief="ridge",bg="#0979b0")
        self.frame_descripcion.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)
        self.frame_descripcion.config(bd=2)
        self.ventana_operaciones = Frame(self.frame,relief="groove",bd=2,bg="#bae7ec")
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH,expand = True)
        #FIN ZONA DE FRAME

        #ZONA DE Menus
        self.menubar = Menu(self)
        self.option_add("*Menu.font", ("Cascadia Code", 8))

        self.menuArchivo = Menu(self.menubar,bg="#f0f0f0", fg="black", activebackground="#2171ea", activeforeground="#f9f9f9")
        self.menuArchivo.add_command(label = "Aplicacion", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)
