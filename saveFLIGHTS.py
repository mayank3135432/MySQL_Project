from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

import mysql.connector as con
ui,_=loadUiType('/home/ateium/SQL_PROJECT/saveFLIGHTS.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.b1.clicked.connect(self.savedb)
        self.fill_combobox();

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

            cursor.execute("select * from AIRPORT")
            result = cursor.fetchall();
            self.cb2.clear() #clear combobox
            if result:
                for AIRPORT in result:
                    self.cb2.addItem(str(AIRPORT[0]))

            cursor.execute("select * from AIRPORT")
            result = cursor.fetchall();
            self.cb3.clear() #clear combobox
            if result:
                for AIRPORT in result:
                    self.cb3.addItem(str(AIRPORT[0]))

        except Exception as e:
            print(e)
            print("Error in fill combo box ")


    def savedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            AIRLINE_ID = self.cb1.currentText()
            SOURCE = self.cb2.currentText()
            DESTINATION = self.cb3.currentText()
            ARRIVAL = self.tb1.text()
            DEPARTURE = self.tb2.text()
            STATUS = self.tb3.text()
            print(type(self.cb1), self.cb1.currentText()) # for debugging
            cursor.execute("insert into FLIGHTS(AIRLINE_ID, SOURCE, DESTINATION, ARRIVAL, DEPARTURE, STATUS)  values('"+ AIRLINE_ID +"', '"+ SOURCE +"' ,'"+ DESTINATION +"','"+ ARRIVAL +"','"+ DEPARTURE +"','"+ STATUS +"')");
            mydb.commit()
            QMessageBox.information(self,"DB Insert","Details saved successfully")
        except Exception as e:
            print(e)
            QMessageBox.information(self,"DB Insert","Error in save db")

    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()