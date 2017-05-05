#Interfaz Grafica del usuario root
# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter.ttk as ttk

from tkinter import messagebox


class root:
    def __init__(self):
        self.crear_ventana_root()



    def crear_ventana_root(self):
        #Creacion de la venroot
        self.venroot=Toplevel()
        self.venroot.geometry("220x250")
        self.venroot.title("Login")
        ###########################         Imagen De Fondo
        name = "FondoS.png"
        photo = PhotoImage(file=name)
        photo_label = Label(self.venroot, image=photo).pack()

        ###########################
        #Cajas, Labels y Variables

        self.usuario=StringVar()
        self.password=StringVar()

        label_usua = Label(self.venroot, text="Usuario").place(x=10, y=10)
        caja_usua = Entry(self.venroot, text=self.usuario).place(x=10, y=30)

        label_pass = Label(self.venroot, text="Password").place(x=10, y=80)
        caja_usua = Entry(self.venroot, text=self.password).place(x=10, y=100)

        CA=["Capturista", "Lectura"]
        txt5 = Label(self.venroot, text="Nivel de Usuario ").place(x=10, y=170)
        self.box = ttk.Combobox(self.venroot, values=(CA) ,textvariable='', state='readonly').place(x=10, y=190)


        #Boton para salir del programa
        boton1 = Button(self.venroot, text="Guardar ", command=self.venroot.destroy).place(x=50, y=220)

        # Llama a la venroot
        self.venroot.mainloop()