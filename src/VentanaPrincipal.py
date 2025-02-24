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

    #Define que hacer cuando se presiona, se pone el mouse encima, se saca el mouse o se da clic izquierdo en los botones
    def inBoton(self, event):
        event.widget.config(bg="#badeed") 

    def outBoton(self, event):
        event.widget.config(bg="#9ccce0")  
    
    def cambioImagen(self, evento):
        self.ImagenAplicacion = Image.open('./imagenes/Reservacion.png')

        # Dimensiones del Label
        ancho = int(self.labelInicio.winfo_width())
        alto = int(self.labelInicio.winfo_height())

        if ancho > 0 and alto > 0:  # Asegurar que tenga dimensiones válidas
            self.ImagenAplicacion = self.ImagenAplicacion.resize((ancho, alto), Image.Resampling.LANCZOS)
            self.ImagenTk = ImageTk.PhotoImage(self.ImagenAplicacion)  # Guardar referencia para evitar garbage collection

            self.labelInicio.configure(image=self.ImagenTk)
    

    def cargar_imagen(self):
        self.ImagenAplicacion = Image.open('./imagenes/Reservacion.png')

        # Dimensiones del Label
        ancho = int(self.labelInicio.winfo_width())
        alto = int(self.labelInicio.winfo_height())

        if ancho > 0 and alto > 0:  # Asegurar que tenga dimensiones válidas
            self.ImagenAplicacion = self.ImagenAplicacion.resize((ancho, alto), Image.Resampling.LANCZOS)
            self.ImagenTk = ImageTk.PhotoImage(self.ImagenAplicacion)  # Guardar referencia para evitar garbage collection

            self.labelInicio.configure(image=self.ImagenTk)
        #FIN ZONA DE Labels
        self.__class__.en_uso = True

        self.mainloop()

    #--------------------------------------------------------------------------------------------------------------
    #Se despliega un Message Box con la informacion basica de lo que hace la aplicacion.
    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Informacion", message = "SISTEMA DE RESERVA DE VUELOS",
        detail = "La aplicacion permite hacer reservaciones de un vuelo y un alojamiento en el lugar de destino, ademas de algunas opciones de administrador.")

    #--------------------------------------------------------------------------------------------------------------
    # Retorna a la Ventana de Inicio del programa.
    def salirVentana(self):
        from ventana_inicio import ventana_inicio
        self.destroy()
        ventana_inicio()
        
    

    #---------------------------------------------------------------------------------------------------------------------------------------
    # Muestra los vuelos disponibles por aerolinea, cada una en un frame que se actualiza por otro cada vez que se presiona el botón siguiente

    def mostrarVuelosPorAerolineas(self):
        self.label_proceso.config(text = "Vuelos disponibles por aerolínea")
        self.label_descripcion.config(text = "Aquí puede visualizar los vuelos que están disponibles por nuestrar aerolíneas")


        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones= Frame(self.frame,relief="groove",bd=2, bg="#bae7ec")
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH, expand=True)
        

        # Se ejecuta cada vez que se presiona el boton "siguiente", para reemplazar el label mostrado por pantalla
        def siguiente():

            self.contador_mostrarVuelosPorAerolineas +=1
            if self.contador_mostrarVuelosPorAerolineas == len(lista_labels):
                self.contador_mostrarVuelosPorAerolineas =0
            if self.contador_mostrarVuelosPorAerolineas==0:
                lista_labels[-1].pack_forget()
                boton_siguiente.pack_forget()
                lista_labels[self.contador_mostrarVuelosPorAerolineas].pack()
                boton_siguiente.place(rely = 0.85, relx= 0.4)
            else:
                lista_labels[self.contador_mostrarVuelosPorAerolineas-1].pack_forget()
                boton_siguiente.pack_forget()
                lista_labels[self.contador_mostrarVuelosPorAerolineas].pack()
                boton_siguiente.place(rely = 0.85, relx= 0.4)

        lista_labels=Admin.mostrarVuelosPorAerolineas(self.ventana_operaciones)
        lista_labels[0].pack()
        boton_siguiente = Button(self.ventana_operaciones,text= "Siguiente",font=("Cascadia Code", 10),command=siguiente, bg="#9ccce0", activebackground="#94c0d3",width=25)
        boton_siguiente.bind("<Enter>", self.inBoton) 
        boton_siguiente.bind("<Leave>", self.outBoton) 
        boton_siguiente.place(rely = 0.85, relx= 0.4)

    #-------------------------------------------------------------------------------------------------------------------------------------
    # Funcion auxiliar que permite mostrar una lista de vuelos disponibles por cada aerolinea hacia un destino seleccionado por el usuario
    # cada aerolinea en un frame que se actualiza por otro cada vez que se presiona el botón siguiente, y continuar con la compra de un
    # tiquete

    def buscarVuelos(self,formulario):
        try:
            hay_excepcion = formulario.aceptar()
        except ExcepcionStringNumero as owo:
            messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
            # self.generarTiquete()
            return
        if hay_excepcion:
            self.generarTiquete()
            return

        self.label_proceso.config(text = "Vuelos disponibles")
        self.label_descripcion.config(text = "Lista los vuelos disponibles de acuerdo a los parámetros ingresados")

        self.ventana_operaciones.pack_forget()

        hayFecha = False
        fecha = None
        destino = formulario.valor_entradas[0]
        lista_general = None

        if len(formulario.valor_entradas) == 2:
            hayFecha = True
            fecha = formulario.valor_entradas[1]

        self.ventana_operaciones= Frame(self.frame,relief="groove",bd=2, bg="#bae7ec")
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH, expand=True)

        if hayFecha:
            label = Label(self.ventana_operaciones, text = "Estos son los vuelos disponibles hacia: " + destino + " en la fecha " + fecha + " por nuestras aerolineas", bg="#bae7ec")
            label.pack()
            lista_general = Admin.consultarVuelosPorDestinoYFecha(destino, fecha, self.ventana_operaciones)
        else:
            label = Label(self.ventana_operaciones, text = "Estos son los vuelos disponibles hacia: " + destino + " por nuestras aerolineas", bg="#bae7ec")
            label.pack()
            lista_general = Admin.consultarVuelosPorDestino(destino, self.ventana_operaciones)
        if len(lista_general[0]) ==0:
            if hayFecha:
                messagebox.showinfo(title="Vuelos Disponibles",message= "Lo sentimos, no tenemos vuelos diponibles hacia " + destino+" en la fecha: " +fecha )
            else:
                messagebox.showinfo(title="Vuelos Disponibles",message= "Lo sentimos, no tenemos vuelos diponibles hacia " + destino )
            self.generarTiquete()
            return

        # Se ejecuta cada vez que se presiona el boton "siguiente", para reemplazar el label mostrado por pantalla

        def siguiente():
            self.contador_mostrarVuelosPorAerolineas +=1
            if self.contador_mostrarVuelosPorAerolineas == len(lista_labels):
                self.contador_mostrarVuelosPorAerolineas =0
            boton_siguiente.pack_forget()
            boton_continuar.pack_forget()
            lista_labels[self.contador_mostrarVuelosPorAerolineas-1].pack_forget()
            lista_labels[self.contador_mostrarVuelosPorAerolineas].pack()
            boton_siguiente.pack(ipady=10, pady=25)
            boton_continuar.pack(ipady=10, pady=20)

        lista_labels = lista_general[0]
        lista_labels[0].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Siguiente",font=("Cascadia Code", 10),command=siguiente, bg="#9ccce0", activebackground="#94c0d3",width=14)
        boton_siguiente.bind("<Enter>", self.inBoton) 
        boton_siguiente.bind("<Leave>", self.outBoton) 
        boton_siguiente.pack(ipady=10, pady=25)

        boton_continuar = Button(self.ventana_operaciones,text= "Continuar con la compra",font=("Cascadia Code", 10), command = lambda: self.comprarTiquete(lista_general[1]),bg="#9ccce0",activebackground="#94c0d3")
        boton_continuar.pack(ipady=10, pady=20)
        boton_continuar.bind("<Enter>", self.inBoton) 
        boton_continuar.bind("<Leave>", self.outBoton) 

        if len(lista_labels) == 0:
            messagebox.showinfo(title = "Buscar vuelos", message = "Lo sentimos, no tenemos vuelos hacia ese destino")
            return

    #-------------------------------------------------------------------------------------------------------------------------------------
    # Funcion auxiliar que permite continuar con la generacion de un tiquete de vuelo, pregunta por la aerolinea y vuelo que se
    # desea comprar, recoge las especificaciones de la silla y los datos del pasajero, para al final mostrar un resumen de la compra

    def comprarTiquete(self, nombres_aerolineas):

        self.label_proceso.config(text = "Compra del vuelo")
        self.label_descripcion.config(text = "Para efectuar la compra, seleccione la aerolínea con la que quiere viajar y el ID del vuelo que quiere comprar")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame,relief="groove",bd=2, bg="#bae7ec")
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH, expand=True)

        labelNombreAerolinea = Label(self.ventana_operaciones, text = "Seleccione la aerolinea con la que desea viajar", bg="#bae7ec")
        labelNombreAerolinea.pack(ipadx = 5, ipady = 5, padx = 3, pady= 3)

        # Es llamada cuando se selecciona una aerolinea en el combobox, y despliega un formulario que pregunta por el ID del vuelo a comprar

        def aerolineaSeleccionada(e):
            nombre = str(aerolineas.get())
            aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre)
            aerolineas.config(state = DISABLED)
            label_id_tiquete = Label(self.ventana_operaciones,text="Ingrese el ID del vuelo que desea comprar.",bg="#bae7ec")
            label_id_tiquete.pack()
            formulario = FieldFrame(self.ventana_operaciones,"Info",["_ID vuelo"],"valor",None,None,["int"])

            # Es llamada cuando se ingresa un ID, y continua con la toma de los datos del pasajero y de la silla. Al finalizar muestra por
            # pantalla un resumen de la compra desde el metodo modificarSilla

            def idVueloIngresado():
                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = Frame(self.frame,relief="groove",bd=2, bg="#bae7ec")
                self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH, expand=True)