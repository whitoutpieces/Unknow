#Interfaz Grafica Secundaria
# _*_ coding:utf-8 _*_
from Tkinter import *

import tkMessageBox


class secundario:
    def __init__(self):
        self.crear_ventana2()

    def crear_ventana2(self):
        self.vu = Toplevel()
        self.vu.geometry("600x350+400+200")
        self.vu.title("Alta de Detenido")

        #variables
        self.nombre=StringVar()
        self.apma=StringVar()
        self.appa=StringVar()
        self.edad=StringVar()
        self.clave =StringVar()
        self.sexo=StringVar
        self.value = StringVar()


        #Entradas y labels
        caja0 = Entry(self.vu, text=self.nombre).place(x=70, y=30)
        txt0 = Label(self.vu, text="Nombre").place(x=0, y=30)

        caja1 = Entry(self.vu, text=self.appa).place(x=70, y=60)
        txt1 = Label(self.vu, text="Ap Paterno").place(x=0, y=60)

        caja2 = Entry(self.vu, text=self.apma).place(x=70, y=90)
        txt2 = Label(self.vu, text="Ap Materno").place(x=0, y=90)

        caja3 = Entry(self.vu, text=self.edad).place(x=70, y=120)
        txt3 = Label(self.vu, text="Edad").place(x=0, y=120)

        caja4 = Entry(self.vu, text=self.clave).place(x=70, y=150)
        txt4 = Label(self.vu, text="Clave").place(x=0, y=150)

        self.check = Radiobutton(self.vu, text='Masculino', variable=self.sexo, value='Masculino').place(x=10, y=200)
        self.check = Radiobutton(self.vu , text='Femenino', variable=self.sexo, value='Femenino').place(x=120, y=200)

        CO=["Azul", "Verde", "Cafes", "Negros"]
        CP=[]
        txt5 = Label(self.vu, text="Color de Ojos: ").place(x=250, y=30)
        self.box = ttk.Combobox(self.vu, values=(CO) ,textvariable=self.value, state='readonly').place(x=350, y=30)



        # Botones
        botonalta = Button(self.vu, text="Guardar ", command='').place(x=10, y=280)
        botoneliminar = Button(self.vu, text="Eliminar ", command='').place(x=90, y=280)
        botonactualizar = Button(self.vu, text="Actualizar ", command='').place(x=160, y=280)
        botonsalir = Button(self.vu, text="salir ", command=self.vu.destroy).place(x=520, y=310)

        #
        # self.vu.mainloop()




