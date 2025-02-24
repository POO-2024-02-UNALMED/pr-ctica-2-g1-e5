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

        self.menuProcesos = Menu(self.menubar,bg="#f0f0f0", fg="black", activebackground="#2171ea", activeforeground="#f9f9f9")
        self.menuProcesos.add_command(label = "Ver vuelos disponibles por Aerolineas",command= self.mostrarVuelosPorAerolineas)
        self.menuProcesos.add_command(label = "Comprar tiquete para un vuelo por destino y fecha", command = self.generarTiquete)
        self.menuProcesos.add_command(label = "Agregar alojamiento en el destino del vuelo", command = self.agregarAlojamientoTiquete )
        self.menuProcesos.add_command(label = "Modificar tiquete comprado", command = self.modificarTiquete)

        self.menuAdmin = Menu(self.menuProcesos, bg="#f0f0f0", fg="black", activebackground="#2171ea", activeforeground="#f9f9f9", tearoff=0)
        self.menuProcesos.add_cascade(menu = self.menuAdmin,label = "Ver opciones de administrador")
        self.menuAdmin.add_command(label= "Listar pasajeros",command=self.listarPasajeros)
        self.menuAdmin.add_command(label= "Agregar vuelo",command=self.agregarVuelo)
        self.menuAdmin.add_command(label= "Cancelar vuelo",command=self.cancelarVuelo)
        self.menuAdmin.add_command(label= "Retirar avion",command=self.retirarAvion)
        self.menuAdmin.add_command(label= "Agregar alojamiento",command=self.agregarAlojamiento)
        self.menuAdmin.add_command(label= "Eliminar Alojamiento",command=self.eliminarAlojamiento)
        self.menuAdmin.add_command(label= "Agregar Aerolinea",command=self.agregarAerolinea)
        self.menuAdmin.add_command(label= "Eliminar Aerolinea",command=self.eliminarAerolinea)
        self.menuAdmin.add_command(label= "Agregar Aerolinea con vuelos",command=self.agAerolinea)

        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Acerca de", command = self.ayuda)

        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProcesos)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar
        #FIN ZONAS DE MENUS


        #ZONA DE LABELS
        self.label_proceso = Label(self.frame_proceso,text= "TURBINA TOURS AND RESORT", font = ("Cascadia Code", 17,"bold"),height=2,bg="#137a9b")
        self.label_proceso.pack(ipadx = 2, ipady =2, padx = 5, pady= 5)

        self.label_descripcion = Label(self.frame_descripcion, text = "Sistema para la venta de tiquetes y alojamientos, y modificación por parte de un administrador", font = ("Cascadia Code", 9), bg="#0979b0")
        self.label_descripcion.pack(ipadx = 2, ipady = 2, padx = 5, pady= 5)

        self.labelTexto = Label(self.ventana_operaciones, text = "Puedes hacerlo con las acciones dispuestas en el menu <Procesos y consultas>", font = ("Cascadia Code", 10),bg="#bae7ec")
        self.labelInicio = Label(self.ventana_operaciones)
        self.labelInicio.place(relheight=0.55, relwidth=0.5,relx=0.25, rely=0.25)
        self.labelTexto.place(relheight=0.2, relwidth=0.8, relx=0.1)
        self.ventana_operaciones.after(100, self.cargar_imagen)
        self.labelInicio.bind("<Configure>", self.cambioImagen)