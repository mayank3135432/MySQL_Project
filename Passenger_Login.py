from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import os
import sys

import mysql.connector as con
ui,_=loadUiType('/home/ateium/SQL_PROJECT/Passenger_Login.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(lambda : os.system(f'python /home/ateium/SQL_PROJECT/savePASSENGER.py &'))
        self.b3.clicked.connect(self.show_table)


    def login(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            cursor.execute("select PNAME from PASSENGER")
            result = cursor.fetchall()
            print(result,type(result), self.tb1.text())
            if self.tb1.text() in list(map(lambda X:X[0], result)):
                self.show_table()
            else:
                QMessageBox.information(self,"LOGIN","Name Not Found")
        except Exception as e:
            print(e)
            print('ERROR IN MAINAPP')
    def show_table(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            cursor.execute("select * from PASSENGER where PNAME = '"+ self.tb1.text() +"' ")
            colnames = cursor.column_names
            result = cursor.fetchall()
            r = 0
            c = 0
            for row_number, row_data in enumerate(result):
                r += 1
                c = 0
                for column_number, data in enumerate(row_data):
                    c += 1
            self.tableReport.clear()
            self.tableReport.setColumnCount(c)
            for row_number, row_data in enumerate(result):
                self.tableReport.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableReport.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.tableReport.setHorizontalHeaderLabels(colnames)
        except con.Error as e:
            print(e)
            print('DATABASE ERROR')
    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()