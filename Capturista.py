#Interfaz Grafica Secundaria
# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter.ttk

from  tkinter import messagebox
import tkinter.ttk
from pypyodbc import *
import pypyodbc
from Verasgos import *
import random

class captura:
    def __init__(self):
        self.crear_ventana3()

    def crear_ventana3(self):
        self.vu = Toplevel()
        self.vu.geometry("800x450+400+200")
        self.vu.title("Alta de Detenido")
        ###########################         Imagen De Fondo
        name = "FondoS.png"
        photo = PhotoImage(file=name)
        photo_label = Label(self.vu, image=photo).pack()

        ###########################
        #variables
        self.nombre=StringVar()
        self.apma=StringVar()
        self.appa=StringVar()
        self.edad=StringVar()
        self.alias =StringVar()
        self.sexo=StringVar
        self.telefono = StringVar()
        self.ocupa = StringVar()


        #Entradas y labels
        caja0 = Entry(self.vu, text=self.nombre).place(x=70, y=30)
        txt0 = Label(self.vu, text="Nombre").place(x=0, y=30)

        caja1 = Entry(self.vu, text=self.appa).place(x=310, y=30)
        txt1 = Label(self.vu, text="Ap Paterno").place(x=240, y=30)

        caja2 = Entry(self.vu, text=self.apma).place(x=550, y=30)
        txt2 = Label(self.vu, text="Ap Materno").place(x=480, y=30)

        #caja3 = Entry(self.vu, text=self.edad).place(x=0, y=60)
        spin= Spinbox(self.vu, from_=15, to=60).place(x=40, y=70)
        txt3 = Label(self.vu, text="Edad").place(x=0, y=70)

        caja4 = Entry(self.vu, text=self.alias).place(x=490, y=70)
        txt4 = Label(self.vu, text="Alias").place(x=440, y=70)

        txsex= Label(self.vu, text="Genero").place(x=200, y=70)
        self.check = Radiobutton(self.vu, text='Masculino', variable=self.sexo, value='Masculino').place(x=260, y=70)
        self.check = Radiobutton(self.vu , text='Femenino', variable=self.sexo, value='Femenino').place(x=340, y=70)

        caja5= Entry(self.vu, text=self.telefono).place(x=70, y=120)
        txt5 = Label(self.vu, text="Telefono").place(x=0, y=120)

        caja6= Entry(self.vu, text=self.ocupa).place(x=310, y=120)
        txt6 = Label(self.vu, text="Ocupacion").place(x=240, y=120)

        #caja6= Entry(self.vu, text='').place(x=310, y=220)
        #txt6 = Label(self.vu, text="Imagen").place(x=340, y=220)

        CO=["Azul", "Verde", "Cafes", "Negros"]
        CP=["Azul", "Verde", "Cafes", "Negros"]
        #txt5 = Label(self.vu, text="Color de Ojos: ").place(x=250, y=30)
        #self.box = ttk.Combobox(self.vu, values=(CO) ,textvariable='', state='readonly').place(x=350, y=500)
        #self.box2 = ttk.Combobox(self.vu, values=(CP), textvariable='', state='readonly').place(x=450, y=500)



        # Botones
        botonalta = Button(self.vu, text="Guardar ", command=self.guardard).place(x=10, y=280)
        botoneliminar = Button(self.vu, text="Actualizar ", command='').place(x=70, y=280)
        botonactualizar = Button(self.vu, text="Siguiente ", command=self.venrasgos).place(x=150, y=280)
        botonsalir = Button(self.vu, text="salir ", command=self.vu.destroy).place(x=520, y=410)

        #
        # self.vu.mainloop()

        ##################################################################
        #################################################################
        ###############################################################
        ##############################################################
        self.vu.mainloop()
    def guardard(self):
        connection = pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-M7FQT57H;Database=Detenidosp;uid=sa;pwd=1234')
        # Creating Cursor
        cursor = connection.cursor()
        #############Database Parameters##########

        ##########################################

        # SQL Query


        SQLCommand = (
            "INSERT INTO infractor(id,nombre,apeidom,apeidop,edad,lugararresto,motivoarresto,fecha,horaentrada,ocupacion,quienaloarresto,sexo,alias) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)")
        idale = random.randint(100, 999)
        id = "SEGT-"
        lugardearresto='Tlaltenango'
        motivodearresto='Lucrar'
        fecha='2017/02/03'
        hora='10:30'
        quienloarresto='Jose'
        Values = [(id + str(idale)),
                  str(self.nombre.get()),
                  str(self.apma.get()),
                  str(self.appa.get()),
                  str(19),#str(self.edad.get()),
                  lugardearresto,
                  motivodearresto,
                  "29/03/2017",
                  "09:13",
                  str(self.ocupa.get()),
                  quienloarresto,
                  'Masculino',#str(self.sexo.get()),
                  str(self.alias.get()),

                  ]
        #########################

        #####################333#
        # Processing Query
        cursor.execute(SQLCommand, Values)
        # Commiting any pending transaction to the database.
        connection.commit()
        # closing connection
        connection.close()
        print("Data Successfully Inserted")

    def venrasgos(self):
        ven=Rasgos()



