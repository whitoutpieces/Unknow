from tkinter import *
import tkinter.ttk as ttk
class Rasgos:
    def __init__(self):
        venrasgos=Toplevel()
        venrasgos.geometry('550x650')

        ###########################         Imagen De Fondo
        name = "FondoS.png"
        photo = PhotoImage(file=name)
        photo_label = Label(venrasgos, image=photo).pack()

        ###########################

        ojos=['azules','cafes','verdes','negros']
        colorojo=StringVar()
        Label(venrasgos,text='color de ojos').place(x=10,y=10)
        boxojos=ttk.Combobox(venrasgos,values=(ojos),textvariable=colorojo,state='readonly').place(x=100,y=10)

        piel = ['blanco','beige','moreno claro','moreno oscuro','negro']
        colorpiel = StringVar()
        Label(venrasgos, text='color de piel').place(x=250, y=10)
        boxpiel = ttk.Combobox(venrasgos, values=(piel), textvariable=colorpiel, state='readonly').place(x=350, y=10)


        cabello = ['negro','casta#o','rubio','pelirrojo']
        colorcabello = StringVar()
        Label(venrasgos, text='color de cabello').place(x=10, y=50)
        boxcabello= ttk.Combobox(venrasgos, values=(cabello), textvariable=colorcabello, state='readonly').place(x=100, y=50)


        Label(venrasgos, text='peso(en kilogramos)').place(x=250, y=50)
        spinpeso=Spinbox(venrasgos,from_=50,to=300).place(x=370, y=50)


        Label(venrasgos, text='altura(en centimetros)').place(x=10, y=100)
        spinaltura= Spinbox(venrasgos, from_=0, to=250).place(x=130, y=100)

        ceja = ['marilyn', 'clara', 'marlene', 'audrey','brooke']
        cejas = StringVar()
        Label(venrasgos, text='tipo de cejas').place(x=250, y=100)
        boxcejas = ttk.Combobox(venrasgos, values=(ceja), textvariable=cejas, state='readonly').place(x=350,y=100)

        boca = ['caida','carnuda','fina','larga']
        tipoboca= StringVar()
        Label(venrasgos, text='tipo de boca').place(x=10, y=150)
        boxcabello = ttk.Combobox(venrasgos, values=(boca), textvariable=tipoboca, state='readonly').place(x=100,y=150)

        nariz = ['concava','recta','convexa']
        tiponariz= StringVar()
        Label(venrasgos, text='tipo de nariz').place(x=10, y=150)
        boxcabello = ttk.Combobox(venrasgos, values=(nariz), textvariable=tiponariz, state='readonly').place(x=100, y=150)

        frente = ['ancha','estrecha','recta','curvada','forma de m','aguda']
        tipofrente = StringVar()
        Label(venrasgos, text='tipo de frente').place(x=250, y=150)
        boxcabello = ttk.Combobox(venrasgos, values=(frente), textvariable=tipofrente, state='readonly').place(x=350,
                                                                                                             y=150)
        menton = ['cuadrado', 'reducido', 'sobresaliente','redondeado']
        tipomenton = StringVar()
        Label(venrasgos, text='tipo de menton').place(x=10, y=200)
        boxcabello = ttk.Combobox(venrasgos, values=(menton), textvariable=tipomenton, state='readonly').place(x=100,
                                                                                                             y=200)
        complexion = ['ectomorfo', 'endomorfo', 'mesomorfo']
        tipocomplexion = StringVar()
        Label(venrasgos, text='tipo de complexion').place(x=250, y=200)
        boxcabello = ttk.Combobox(venrasgos, values=(complexion), textvariable=tipocomplexion, state='readonly').place(x=370,
                                                                                                             y=200)

        venrasgos.mainloop()

