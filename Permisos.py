#Interfaz Grafica Secundaria
# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter.ttk as ttk


#import tkMessageBox


class UsuaP:
    def __init__(self):
        #self.crear_ventana3()
        print ('hola')
    def crear_ventana3(self):
        self.vu = Toplevel()
        self.vu.geometry("400x250+400+200")
        self.vu.title("Permisos Usuaro")
        ###########################         Imagen De Fondo
        name = "FondoS.png"
        photo = PhotoImage(file=name)
        photo_label = Label(self.vu, image=photo).pack()

        ###########################
        #variables
        self.nombre=StringVar()
        self.conta=StringVar()
        self.permiso=StringVar()



        #Entradas y labels
        CO = ["Comandaante", "Official", "SubDirector"]
        self.box = ttk.Combobox(self.vu, values=(CO), textvariable='').place(x=80, y=30)
        #caja0 = Entry(self.vu, text=self.nombre).place(x=70, y=30)
        txt0 = Label(self.vu, text="Nombre").place(x=0, y=30)

        caja1 = Entry(self.vu, text=self.conta).place(x=80, y=70)
        txt1 = Label(self.vu, text="Contrasena").place(x=0, y=70)

        CP = ["Capturista", "Lector"]
        self.box2 = ttk.Combobox(self.vu, values=(CP), textvariable='', state='readonly').place(x=80, y=110)
        #caja2 = Entry(self.vu, text=self.permiso).place(x=70, y=110)
        txt2 = Label(self.vu, text="Nivel de usuario").place(x=0, y=110)


        # Botones
        botonalta = Button(self.vu, text="Guardar ", command='').place(x=10, y=180)
        botoneliminar = Button(self.vu, text="Actualizar ", command='').place(x=90, y=180)
        botonsalir = Button(self.vu, text="salir ", command=self.vu.destroy).place(x=520, y=410)

        #
        self.vu.mainloop()

