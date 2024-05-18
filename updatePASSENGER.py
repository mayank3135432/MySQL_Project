from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys

import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/updatePASSENGER.ui')

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
            cursor.execute("select * from PASSENGER")
            result = cursor.fetchall()
            self.cb0.clear() #clear combobox
            if result:
                for PASSENGER in result:
                    print('pass ',type(PASSENGER))
                    self.cb0.addItem(str(PASSENGER[0]))


            cursor.execute("select * from FLIGHTS")
            result = cursor.fetchall()
            self.cb1.clear() #clear combobox
            if result:
                for FLGHTS in result:
                    print('flight ',type(FLGHTS))
                    self.cb1.addItem(str(FLGHTS[0]))

        except Exception as e:
            print(e)
            print("Error in fill combo box ")
    def fill_details_on_combobox_selected(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb0.currentText()
            cursor.execute("select * from PASSENGER where PID='"+ em +"'")
            result = cursor.fetchall();
            if result:
                for PASSENGER in result:
                    #self.cb1.setItemText(0,str(PASSENGER[1]))
                    self.tb1.setText(str(PASSENGER[2]))
                    self.tb2.setText(str(PASSENGER[3]))
                    self.tb3.setText(str(PASSENGER[4]))
                    self.tb4.setText(str(PASSENGER[5]))
        except Exception as e:
            print(e)
            print("Error in fill details on combo box select ")
    
    def updatedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            PID = self.cb0.currentText()
            FLIGHT_CODE = self.cb1.currentText()
            SEAT_NO = self.tb1.text()
            BOOK_DATE = self.tb2.text()
            PNAME = self.tb3.text()
            PHONE_NO = self.tb4.text()
            cursor.execute("update PASSENGER set FLIGHT_CODE = '"+ FLIGHT_CODE +"', SEAT_NO = '"+ SEAT_NO +"', BOOK_DATE = '"+ BOOK_DATE +"', PNAME = '"+ PNAME +"', PHONE_NO = '"+ PHONE_NO +"' where PID = '"+ PID +"'  ")
            result = cursor.fetchall();
            mydb.commit()
            QMessageBox.information(self, "Update Form", "PASSENGER Details Updated Succsessfully")
            
            mydb.commit()
            QMessageBox.information(self, "Update Form", "Details Updated Succsessfully")

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