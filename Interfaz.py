#Interfaz Grafica Principal
# _*_ coding:utf-8 _*_
from tkinter import *
from pypyodbc import *
from tkinter import  messagebox
#import tkMessageBox

from venDelito import *
from Creatabla import *
from Permisos import *
class trabajo:
    def __init__(self):
        self.crear_ventana()

    def alta_det(self):
        from Capturista import captura
        captura()

    def usua(self):
        from Root import root
        root()

    def salir(self):
        self.ventana2.destroy()
        self.ventana.deiconify()
        self.usuario.set('')
        self.password.set('')

    def tabla(self):
        print ("sa")
        app = QApplication(sys.argv)
        # Crear un objeto de la clase
        _ventana = Elim()
        _ventana.show()
        # Mostra la ventana
        # _ventana.show()
        # Ejecutar la aplicaci
        app.exec_()
    def delito(self):

        app = QApplication(sys.argv)
        # Crear un objeto de la clase
        _ventana = Delito()
        _ventana.show()
        # Mostra la ventana
        # _ventana.show()
        # Ejecutar la aplicaci
        app.exec_()

    def crear_ventana2(self):
        # Creacion de la ventana

        self. ventana2 =Toplevel()
        self.ventana2.geometry("1366x768")

        self.ventana2.title("Principal")
        #fondo = PhotoImage(file="C:\Users\Rodrigo Miku\Pictures\p\Proy\Portada.ppm")
        #label = Label(self.ventana2, image=fondo).place(x=1, y=1)

        # Cajas, Labels y Variables
        menubar = Menu(self.ventana2)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Lectura de Detenidos  ', command=self.tabla)##################################todo@@@@@@@@@
        #filemenu.add_command(label='Consulta   ', command='')
        filemenu.add_separator()
        menubar.add_cascade(label='Consulta', menu=filemenu)
        ###########################         Imagen De Fondo
        name = "FondoP.png"
        photo = PhotoImage(file=name)
        photo_label = Label(self.ventana2, image=photo).pack()

        ###########################

        if self.level[self.lel] == "0":
            filemenu1 = Menu(menubar, tearoff=0)
            menubar.add_cascade(label='Control de Usuarios ', menu=filemenu1)
            filemenu1.add_command(label='Alta de Usuarios ', command=self.usua)
            up=UsuaP()
            filemenu1.add_command(label='Permisos de Usuarios ', command=up.crear_ventana3)

        if self.level[self.lel]=="1" or self.level[self.lel] == "0" :
            filemenu2 = Menu(menubar, tearoff=0)
            menubar.add_cascade(label='Detenidos ', menu=filemenu2)
            filemenu2.add_command(label='Alta de Detenidos  ', command=self.alta_det)
            filemenu2.add_command(label='Delitos  ', command=self.delito)###############################TODO@@@@@@@@@@

        filemenu4 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Salir', menu=filemenu4)
        filemenu4.add_command(label='Cerrar Sesion  ', command=self.salir)

        self.ventana2.config(menu=menubar)
        self.ventana2.mainloop()

        # Boton para salir del programa

#6 7 8 9 11
    def login(self):
        usua=self.usuario.get()
        password=self.password.get()
        lim=len(self.Lusuarios)
        for i in range(lim):
            if usua==self.Lusuarios[i] and password==self.Lpass[i]:
                    messagebox.showinfo(title="Welcome ", message="Bienvenido "+ usua )
                    self.lel=i
                    self.ventana.withdraw()
                    self.crear_ventana2()
                    susua='sa'
                    spassword='1234'
                    print( 'Driver={SQL Server};' \
                          'Server=localhost;' \
                          'Database=Detenidosp;uid=' + str(usua) + \
                          ';pwd=' + str(password))
                    try:
                        # creating connection Object which will contain SQL Server Connection
                        connection = pypyodbc.connect('Driver={SQL Server};'
                                                      'Server=localhost;'
                                                      'Database=Detenidosp'
                                                      ';uid=' + str(susua) +
                                                      ';pwd=' + str(spassword))

                        print("Connection Successfully Established")

                        # closing connection
                        connection.close()


                    except:
                        print("error")
                    break



            else:
                if i == lim-1:
                    messagebox.showerror(title="Advertencia", message="Usuario o Password Incorrecto")





    def crear_ventana(self):
        #Creacion de la ventana

        self.Lusuarios=['Admin',"Capturista","Lector"]
        self.Lpass=['123','1234','12345']
        self.level=['0','1','2']
        self.ventana=Tk()
        self.ventana.geometry("200x250")
        self.ventana.title("Login")
        ###########################         Imagen De Fondo
        name="Inicio.png"
        photo=PhotoImage(file=name)
        photo_label=Label(self.ventana,image=photo).pack()

        ###########################
        #Cajas, Labels y Variables

        self.usuario=StringVar()
        self.password=StringVar()

        label_usua = Label(self.ventana, text="Usuario").place(x=20, y=40)
        caja_usua = Entry(self.ventana, text=self.usuario).place(x=20, y=60)

        label_pass = Label(self.ventana, text="Password").place(x=20, y=110)
        caja_usua = Entry(self.ventana, show="*", text=self.password).place(x=20, y=130)

        botonlogin = Button(self.ventana, text="Entrar ", command=self.login).place(x=150, y=190)


        #Boton para salir del programa
        boton1 = Button(self.ventana, text="salir ", command=self.ventana.destroy).place(x=350, y=390)

        # Llama a la ventana
        self.ventana.mainloop()

t=trabajo()