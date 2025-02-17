from VentanaPrincipal import VentanaSecundaria
from tkinter import *
from Admin import Admin
from PIL import Image, ImageTk
class ventana_inicio(Tk):
    ventana=None
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # CONFIGURACION PARAMETROS PRINCIPALES DE LA VENTANA
        self.geometry("850x560")
        self.minsize(850,560)
        self.title("TURBINA TOURS AND RESORT")
        self.option_add("*tearOff", False)
        self.iconbitmap('./imagenes/icono.ico')
        # CONFIGURACION VR--TEXTO HDV DESARROLLADORES
        self.varHDV = StringVar()
        self.varHDV.set("Desarrolladores")

        # CONFIGURACION ZONA DE MENU
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion",command=self.desno)
        self.menuInicio.add_command(label="Salir",command=self.salir)
        self["menu"] = self.menubar

        #CONFIGURACION ZONA FRAMES

        self.P1 = Frame(self, bg="#000000")
        self.P1.place(relwidth=0.50, relheight=1)
        self.P3 = Frame(self.P1)
        self.P3.place(relwidth=0.985, relheight=0.285, relx=0.007, rely=0.009)
        self.saludo = Label(self.P3, text="BIENVENIDO A TURBINA TOURS AND RESORT\n""HAZ CLICK EN LA IMAGEN PARA INGRESAR AL SISTEMA\n""⇣", font=("Segoe UI", 12), bg="#13bcb7")
        self.P4 = Frame(self.P1, bg="pink")
        self.P4.place(relwidth=0.985, relheight=0.685, relx=0.007, rely=0.305)
        self.contenedorImagen = Label(self.P4)
        self.contenedorImagen.config()
        self.ImagenAplicacion = Image.open('./imagenes/--x3.png')
        a, al=self.P4.winfo_width(),self.P4.winfo_height()
        self.ImagenAplicacion = self.ImagenAplicacion.resize((a, al), Image.Resampling.LANCZOS)
        self.contenedorImagen["image"] = ImageTk.PhotoImage(self.ImagenAplicacion)
        self.P2 = Frame(self, bg="black")
        self.P2.place(relwidth=0.50, relheight=1, relx=0.50)
        self.P5 = Frame(self.P2, bg="Gray")
        self.P5.place(relwidth=0.985, relheight=0.285, relx=0.007, rely=0.009)
        self.textoHDV = Label(self.P5, textvariable=self.varHDV, font = ("Segoe UI", 8))
        self.textoHDV.bind('<ButtonPress-1>', self.cambioHDV)
        self.textoHDV.place(relheight=0.53, relwidth=0.53,relx=0.24, rely=0.23)
        self.P6 = Frame(self.P2,bg="Gray")
        self.P6.place(relwidth=0.985, relheight=0.685, relx=0.007, rely=0.305)
        self.saludo.place(relwidth=1, relheight=1)
        self.W1 = Frame(self.P6, bg="Gray", bd=2)
        self.W1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
        self.W2 = Frame(self.P6, bg="Gray", bd=2)
        self.W2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
        self.W3 = Frame(self.P6, bg="Gray", bd=2)
        self.W3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
        self.W4 = Frame(self.P6, bg="Gray", bd=2)
        self.W4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

        #CONTADORES CAMBIO DE CASOS METODOS
        self.acumulador = 0
        self.numClicksHDV = 0

        # LISTA MENEJO IMAGENES DESARROLLADORES
        self.direcciones = ['./imagenes/jh1.png', './imagenes/jh2.png', './imagenes/jh3.png', './imagenes/jh4.png','./imagenes/--c1.png', './imagenes/--c2.png', './imagenes/--c3.png', './imagenes/--c4.png','./imagenes/--m1.png', './imagenes/--m2.png', './imagenes/--m3.png', './imagenes/--m4.png','./imagenes/--q1.png', './imagenes/--q2.png', './imagenes/--q3.png', './imagenes/--q4.png','./imagenes/--z1.png','./imagenes/--z2.png','./imagenes/--z3.png','./imagenes/--z4.png','./imagenes/--yu.png','./imagenes/h.png']
        self.cambio_posiciones = []

        # LISTA MANEJO DE IMAGENES DEL SISTEMA
        self.lineas = ['./imagenes/--x2.png', './imagenes/--x3.png', './imagenes/--x1.png','./imagenes/--x4.png', './imagenes/--x5.png']
        self.chang_posiciones = []

        #RECORRIDO SOBRE LA LISTA direcciones PARA OBTENER LAS IMAGENES SEGUN LA REFERENIA DEL DESARROLLADOR
        for i in self.direcciones:
            nuevo_ancho = self.W4.winfo_width()
            nuevo_alto = self.W4.winfo_height()
            imagen = Image.open(i)
            imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
            imagen = ImageTk.PhotoImage(imagen_redimensionada)
            self.cambio_posiciones.append(imagen)

        for widget in [self.W1, self.W2, self.W3, self.W4]:
             widget.grid_rowconfigure(0, weight=1)  # Centrado vertical
             widget.grid_columnconfigure(0, weight=1)  # Centrado horizontal

        self.im_desa_pos1 = Label(self.W1)
        self.im_desa_pos2 = Label(self.W2)
        self.im_desa_pos3 = Label(self.W3)
        self.im_desa_pos4 = Label(self.W4)
        self.im_desa_pos1["image"] = self.cambio_posiciones[-1]
        self.im_desa_pos1.grid(row=0, column=0,sticky="nsew")
        self.im_desa_pos2["image"] = self.cambio_posiciones[-2]
        self.im_desa_pos2.grid(row=0, column=0,sticky="nsew")
        self.im_desa_pos3["image"] = self.cambio_posiciones[-2]
        self.im_desa_pos3.grid(row=0, column=0,sticky="nsew")
        self.im_desa_pos4["image"] = self.cambio_posiciones[-1]
        self.im_desa_pos4.grid(row=0, column=0,sticky="nsew")
        self.contador = 0
        
        #RECORRIDO SOBRE LA LISTA lineas PARA ABRIR DETERMINADA IMAGEN SEGUN LA REFERENCIA DEL EVENTO PARA CAMBIO DE IMAGEN
        for i in self.lineas:
            imagen = Image.open(i)
            imagen_redimensionada = imagen.resize((425, 380), Image.Resampling.LANCZOS)
            imagen = ImageTk.PhotoImage(imagen_redimensionada)
            self.chang_posiciones.append(imagen)
        # CONFIGURACION BOTON APERTURA DE LA VENTANA PRINCIPAL Y CAMBIO DE IMAGEN
        self.nueva_ventana = Button(self.P4, image=self.chang_posiciones[0],command=self.abrirVentanaSecundaria)
        self.nueva_ventana.pack(fill=BOTH, expand=True)
        self.nueva_ventana.bind('<Enter>', self.cambio)
        self.P4.bind("<Configure>", self.actualizar_imagen)
        
        self.mainloop()
    
    def actualiza_imagen(self, event=0):
        n1,n2,n3,n4 = self.W1.winfo_width(),self.W2.winfo_width(),self.W3.winfo_width(),self.W4.winfo_width()
        a1,a2,a3,a4 = self.W1.winfo_height(),self.W2.winfo_height(),self.W3.winfo_height(),self.W4.winfo_height()
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        if self.contador == 1:
            y1 = self.contador - 1
            y2 = self.contador
            y3 = self.contador + 1
            y4 = self.contador + 2
        elif self.contador == 2:
            y1 = self.contador + 2
            y2 = self.contador + 3
            y3 = self.contador + 4
            y4 = self.contador + 5
        elif self.contador == 3:
            y1 = self.contador + 5
            y2 = self.contador + 6
            y3 = self.contador + 7
            y4 = self.contador + 8
        elif self.contador == 4:
            y1 = self.contador + 8
            y2 = self.contador + 9
            y3 = self.contador + 10
            y4 = self.contador + 11
        elif self.contador == 0:
            y1 = self.contador -1
            y2 = self.contador -2 
            y3 = self.contador -2
            y4 = self.contador -1
        elif self.contador == 5:
            y1 = self.contador + 11
            y2 = self.contador + 12
            y3 = self.contador + 13
            y4 = self.contador + 14
        imagen_redimensionada1 = Image.open(self.direcciones[y1]).resize((n1, a1), Image.Resampling.LANCZOS)
        imagen_redimensionada2 = Image.open(self.direcciones[y2]).resize((n2, a2), Image.Resampling.LANCZOS)
        imagen_redimensionada3 = Image.open(self.direcciones[y3]).resize((n3, a3), Image.Resampling.LANCZOS)
        imagen_redimensionada4 = Image.open(self.direcciones[y4]).resize((n4, a4), Image.Resampling.LANCZOS)
        self.nueva_imagen1 = ImageTk.PhotoImage(imagen_redimensionada1)
        self.nueva_imagen2 = ImageTk.PhotoImage(imagen_redimensionada2)
        self.nueva_imagen3 = ImageTk.PhotoImage(imagen_redimensionada3)
        self.nueva_imagen4 = ImageTk.PhotoImage(imagen_redimensionada4)
        self.im_desa_pos1.config(image=self.nueva_imagen1)
        self.im_desa_pos2.config(image=self.nueva_imagen2)
        self.im_desa_pos3.config(image=self.nueva_imagen3)
        self.im_desa_pos4.config(image=self.nueva_imagen4)

    def actualizar_imagen(self,event=0):
        nuevo_ancho = self.P4.winfo_width()
        nuevo_alto = self.P4.winfo_height()
        imagen_redimensionada = Image.open(self.lineas[self.acumulador]).resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
        nueva_imagen = ImageTk.PhotoImage(imagen_redimensionada)
        self.nueva_ventana.config(image=nueva_imagen)
        self.nueva_ventana.image = nueva_imagen
        self.actualiza_imagen()
        
    #GENERA LA SALIDA DEL TEXTO DE EN LA DESCRIPCION
    def desno(self):
        from tkinter import messagebox
        descripcion = messagebox.showinfo(title = "Informacion", message = "SISTEMA DE RESERVA DE VUELOS",
        detail = "Nuestra app permite reservar vuelos y alojamientos fácilmente, con herramientas para una gestión eficiente como administrador")

    #GENERA LA SALIDA DE LA VENTANA DE INICIO DANDO CULMINADO EL FUNCIONAMIENTO DE LA APLICACION
    def salir(self):
        Admin.salirDelSistema()
        self.destroy()

    #OCASIONA LA APERTURA DE LA VENTANAPRINCIAL
    def abrirVentanaSecundaria(self):
        self.destroy()
        VentanaSecundaria()
        #return self.destroy()

    #SUSCITA EL CAMBIO DE INFORMACIÓN DE LA HOJA DE VIDA E IMAGENES DE LOS DESARROLLADORES
    def cambioHDV(self,b):
        self.numClicksHDV += 1
        if self.numClicksHDV == 1:
            self.varHDV.set("Nombre: Jhoneyker Delgado Urbina \n""Edad : 17 años \n""Programa: Ingeniería de sistemas\n")
            self.evento()
        elif self.numClicksHDV == 2:
            self.varHDV.set("Nombre: Emmanuel Valencia Lopera \n""Edad: 18 años \n" "Programa: Ingeniería de sistemas\n")
            self.evento()
        elif self.numClicksHDV == 3:
            self.varHDV.set("Nombre: Simon Guarin Cortes  \n""Edad : 18 años \n""Programa: Ingeniería de sistemas\n")
            self.evento()
        elif self.numClicksHDV == 4:
            self.varHDV.set("Nombre: Jesus Camilo Miranda Aguirre \n""Edad : 20 años \n""Programa: Ingeniería de sistemas\n")
            self.evento()
        elif self.numClicksHDV == 5:
            self.varHDV.set("Nombre: Andres Jacobo Leal Aguirre \n""Edad : 18 años \n""Programa: Ingeniería de sistemas\n")
            self.evento()
            self.numClicksHDV =0

    #PROVOCA LA APERTURA DE LAS IMAGENES DE CADA DESARROLLADOR SEGUN SU IDENTIFICADOR POSICIONAL
    def evento(self):
        y1 = 0
        y2 = 0
        y3 = 0
        y4 = 0
        self.contador += 1
        if self.contador == 1:
            y1 = self.contador - 1
            y2 = self.contador
            y3 = self.contador + 1
            y4 = self.contador + 2
        elif self.contador == 2:
            y1 = self.contador + 2
            y2 = self.contador + 3
            y3 = self.contador + 4
            y4 = self.contador + 5
        elif self.contador == 3:
            y1 = self.contador + 5
            y2 = self.contador + 6
            y3 = self.contador + 7
            y4 = self.contador + 8
        elif self.contador == 4:
            y1 = self.contador + 8
            y2 = self.contador + 9
            y3 = self.contador + 10
            y4 = self.contador + 11
        elif self.contador == 5:
            y1 = self.contador + 11
            y2 = self.contador + 12
            y3 = self.contador + 13
            y4 = self.contador + 14
        self.im_desa_pos1.config(image=self.cambio_posiciones[y1])
        self.im_desa_pos2.config(image=self.cambio_posiciones[y2])
        self.im_desa_pos3.config(image=self.cambio_posiciones[y3])
        self.im_desa_pos4.config(image=self.cambio_posiciones[y4])
        if self.contador>5:
            self.contador=1
        self.actualiza_imagen()

    # OCASIONA EL CAMBIO EN LA POSICION DE LAS IMAGENES DEL SISTEMA
    def cambio(self,a):
        self.acumulador += 1
        if self.acumulador == 5:
            self.acumulador = 0
        self.nueva_ventana.config(image=self.chang_posiciones[self.acumulador])

if __name__ == "__main__":
    ventana_inicios = ventana_inicio()