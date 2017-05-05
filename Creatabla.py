import sys
import pypyodbc
from PyQt5.QtWidgets import *#QApplication, QMainWindow,QDialog,QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import time
import random
from  tkinter import *

from PyQt5.QtCore import pyqtSlot


class Elim(QDialog):
    def __init__(self):
       # lista=[["Dt1234","Jose","Gomez","Ramirez","19","el Parian","Perturbar el orden publico","18/04/17","06:39","Desempleado","Jorge ","Masculino","Chepe",]
        #    ,["Dt1235","Diego","Ramos","Rosas","21","el pasaje","Perturbar el orden publico","18/03/17","06:39","Desempleado","Jorge ","Masculino","go diego",],
         #      ["Dt1235", "Diego", "Ramos", "Rosas", "21", "el pasaje", "Perturbar el orden publico", "18/03/17","06:39", "Desempleado", "Jorge ", "Masculino", "go diego",]]
        QMainWindow.__init__(self)
        uic.loadUi('TABLA.ui',self)
        self.tableWidget.setRowCount(4)

        """        for c in range(3):
            for i in range (13):
                self.tableWidget.setItem(c, i, QTableWidgetItem(lista[c][i]))#"hola"+str(c)+str(i)))
        """
        ###############################
        connection = pypyodbc.connect(
            'Driver={SQL Server};Server=LAPTOP-M7FQT57H;Database=Detenidosp;uid=sa;pwd=1234' )
        # Creating Cursor
        cursor = connection.cursor()

        # SQL Query
        SQLCommand = ("select * from infractor")
        # Processing Query
        cursor.execute(SQLCommand)
        i = 0

        rowsbd = 100
        fielddb = 13

        self.tableWidget.setRowCount(8)
        self.tableWidget.clearContents()

        for rows in cursor.fetchall():
            print("------------Employee %d-----------------" % i)
            f = 0
            for field in rows:
                print(str(field))
                #if f==5:
                if f==8 :
                    numale=random.randint(10000,99999)
                    self.tableWidget.setItem(i, f, QTableWidgetItem('43710'+str(numale)))


                else:

                    self.tableWidget.setItem(i, f, QTableWidgetItem(str(field)))
                f += 1
            print("---------------------------------------")
            print('')
            i = i + 1

        connection.close()






class ven:
    def __init__(self):
        ven = Tk()
        Button(ven, text="TAbLa", command=self.boton).pack()
        ven.mainloop()


    def boton(self):
        app = QApplication(sys.argv)
        # Crear un objeto de la clase
        _ventana = Elim()
        _ventana.show()
        # Mostra la ventana
        # _ventana.show()
        # Ejecutar la aplicaci
        app.exec_()
