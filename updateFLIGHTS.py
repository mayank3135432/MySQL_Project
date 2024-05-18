from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys

import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/updateFLIGHTS.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_combobox()
        self.fill_details_on_combobox_selected()
        self.cb0.currentIndexChanged.connect(self.fill_details_on_combobox_selected)
        self.b1.clicked.connect(self.updatedb)
    def fill_combobox(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            cursor.execute("select * from FLIGHTS")
            result = cursor.fetchall()
            self.cb0.clear() #clear combobox
            if result:
                for FLIGHTS in result:
                    print(type(FLIGHTS))
                    self.cb0.addItem(str(FLIGHTS[0]))


            cursor.execute("select * from AIRLINE")
            result = cursor.fetchall()
            self.cb1.clear() #clear combobox
            if result:
                for AIRLINE in result:
                    print(type(AIRLINE))
                    self.cb1.addItem(str(AIRLINE[0]))

            cursor.execute("select * from AIRPORT") # source
            result = cursor.fetchall()
            self.cb2.clear() #clear combobox
            if result:
                for AIRPORT in result:
                    print(type(AIRPORT))
                    self.cb2.addItem(AIRPORT[0])

            cursor.execute("select * from AIRPORT") # destination
            result = cursor.fetchall()
            self.cb3.clear() #clear combobox
            if result:
                for AIRPORT in result:
                    print(type(AIRPORT))
                    self.cb3.addItem(str(AIRPORT[0]))


        except Exception as e:
            print(e)
            print("Error in fill combo box ")
    def fill_details_on_combobox_selected(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb0.currentText()
            cursor.execute("select * from FLIGHTS where FLIGHT_CODE='"+ em +"'")
            result = cursor.fetchall();
            if result:
                for FLIGHTS in result:
                    #self.cb1.setItemText(0,str(FLIGHTS[1]))
                    #self.cb2.setItemText(0,str(FLIGHTS[2]))
                    #self.cb3.setItemText(0,str(FLIGHTS[3]))
                    self.tb1.setText(str(FLIGHTS[4]))
                    self.tb2.setText(str(FLIGHTS[5]))
                    self.tb3.setText(str(FLIGHTS[6]))
        except Exception as e:
            print(e)
            print("Error in fill details on combo box select ")
    
    def updatedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            FLIGHT_CODE = self.cb0.currentText()
            AIRLINE_ID = self.cb1.currentText()
            SOURCE = self.cb2.currentText()
            DESTINATION = self.cb3.currentText()
            ARRIVAL = self.tb1.text()
            DEPARTURE = self.tb2.text()
            STATUS = self.tb3.text()
            cursor.execute("update FLIGHTS set AIRLINE_ID = '"+ AIRLINE_ID +"', SOURCE = '"+ SOURCE +"', DESTINATION = '"+ DESTINATION +"', ARRIVAL = '"+ ARRIVAL +"', DEPARTURE = '"+ DEPARTURE +"' , STATUS = '"+ STATUS +"' where FLIGHT_CODE = '"+ FLIGHT_CODE +"' ")
            result = cursor.fetchall();
            mydb.commit()
            QMessageBox.information(self, "Update Form", "Flight Details Updated Succsessfully")

        except Exception as e:
            print(e)
            print("Error in update db ")




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()