from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

import mysql.connector as con
ui,_=loadUiType('/home/ateium/SQL_PROJECT/savePASSENGER.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.b1.clicked.connect(self.savedb)
        self.fill_combobox();
        self.cb1.currentIndexChanged.connect(self.fill_details_on_combobox_selected)
        

    def fill_combobox(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            cursor.execute("select * from FLIGHTS")
            result = cursor.fetchall();
            self.cb1.clear() #clear combobox
            if result:
                for FLIGHTS in result:
                    self.cb1.addItem(str(FLIGHTS[0]))

        except Exception as e:
            print(e)
            print("Error in fill combo box ")

    def fill_details_on_combobox_selected(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            
            cursor.execute("SELECT FLIGHTS.FLIGHT_CODE, AIRLINE.AL_NAME FROM FLIGHTS JOIN AIRLINE ON FLIGHTS.AIRLINE_ID = AIRLINE.AIRLINE_ID where FLIGHTS.FLIGHT_CODE= "+ em +";")
            result = cursor.fetchall()
            if result:
                for X in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb5.setText(str(X[1]))
            cursor.execute("select SOURCE from FLIGHTS where FLIGHTS.FLIGHT_CODE = "+ em +";")
            result = cursor.fetchall()
            if result:
                for X in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb6.setText(str(X[0]))
            
            cursor.execute("select DESTINATION from FLIGHTS where FLIGHTS.FLIGHT_CODE = "+ em +";")
            result = cursor.fetchall()
            if result:
                for X in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb7.setText(str(X[0]))

            cursor.execute("select DEPARTURE from FLIGHTS where FLIGHTS.FLIGHT_CODE = "+ em +";")
            result = cursor.fetchall()
            if result:
                for X in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb8.setText(str(X[0]))
            
            cursor.execute("select ARRIVAL from FLIGHTS where FLIGHTS.FLIGHT_CODE = "+ em +";")
            result = cursor.fetchall()
            if result:
                for X in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb9.setText(str(X[0]))
        except Exception as e:
            print(e)
            print("Error in fill details on combo box selected ")
    

    def savedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            FLIGHT_CODE = self.cb1.currentText()
            SEAT_NO = self.tb1.text()
            BOOK_DATE = self.tb2.text()
            PNAME = self.tb3.text()
            PHONE_NO = self.tb4.text()
            print(type(self.cb1), self.cb1.currentText()) # for debugging
            cursor.execute("insert into PASSENGER(FLIGHT_CODE, SEAT_NO, BOOK_DATE, PNAME, PHONE_NO)  values('"+ FLIGHT_CODE +"', '"+ SEAT_NO +"' ,'"+ BOOK_DATE +"','"+ PNAME +"','"+ PHONE_NO +"')");
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