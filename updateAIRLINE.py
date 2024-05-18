from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys

import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/updateAIRLINE.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_combobox()
        self.fill_details_on_combobox_selected()
        self.cb1.currentIndexChanged.connect(self.fill_details_on_combobox_selected)
        self.b1.clicked.connect(self.updatedb)
    def fill_combobox(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            cursor.execute("select * from AIRLINE")
            result = cursor.fetchall();
            self.cb1.clear() #clear combobox
            if result:
                for AIRLINE in result:
                    self.cb1.addItem(str(AIRLINE[0]))
        except Exception as e:
            print(e)
            print("Error in fill combo box ")
    def fill_details_on_combobox_selected(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            cursor.execute("select * from AIRLINE where AIRLINE_ID = '"+ em +"'")
            result = cursor.fetchall();
            if result:
                for AIRLINE in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb1.setText(str(AIRLINE[1]))
        except Exception as e:
            print(e)
            print("Error in fill details ")
    
    def updatedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            country = self.tb1.text()
            cursor.execute("update AIRLINE set AL_NAME = '"+ country +"' where AIRLINE_ID = '"+ em +"'")
            result = cursor.fetchall();
            mydb.commit()
            QMessageBox.information(self, "Update Form", "Airport Details Updated Succsessfully")

        except Exception as e:
            print(e)
            print("Error in fill updatedb ")




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()