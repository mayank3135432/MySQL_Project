from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys
import os
import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/table.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.select_table()
        self.show_table()
        self.fillanothercombobox()
        self.cb1.currentIndexChanged.connect(self.show_table)
        self.cb1.currentIndexChanged.connect(self.fillanothercombobox)
        self.b1.clicked.connect(self.deletedb)
        self.b2.clicked.connect(lambda : os.system(f'python /home/ateium/SQL_PROJECT/save{self.cb1.currentText()}.py &'))
        self.b4.clicked.connect(lambda : os.system(f'python /home/ateium/SQL_PROJECT/update{self.cb1.currentText()}.py &'))
        self.b3.clicked.connect(self.show_table)
    
    b4_is_visible = 1

    def select_table(self):
        mydb = con.connect(host="localhost",user="root",password="admin",db="AIRPORT")
        cursor = mydb.cursor()
        cursor.execute("show tables")
        result = cursor.fetchall()
        self.cb1.clear()
        if result:
            for tables in result:
                self.cb1.addItem(str(tables[0]))

    def fillanothercombobox(self):
        try:
            mydb = con.connect(host="localhost",user="root",password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            mystr = self.cb1.currentText()
            print(mystr)
            cursor.execute("select * from "+ mystr +"")
            result = cursor.fetchall()
            self.cb2.clear()
            self.colnames = cursor.column_names
            print(type(self.colnames),self.colnames)
            if result:
                if mystr != 'CONTAINS':
                    self.cb3.clear()
                    self.cb3.hide()
                    self.b4.show()
                    for tables in result:
                        self.cb2.addItem(str(tables[0]))
                else:
                    self.cb3.show()
                    self.b4.hide()
                    for tables in result:
                        self.cb2.addItem(str(tables[0]))
                        self.cb3.addItem(str(tables[1]))
        except Exception as e:
            print(e)
            print("Error in fill another combo box ")


    
    def deletedb(self):
        try:
            mydb = con.connect(host="localhost",user="root",password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            pk = self.cb2.currentText()
            if str(em) == 'CONTAINS':
                pk3 = self.cb3.currentText()
                cursor.execute("delete from "+ em +" where "+ self.colnames[0] +" = '"+ pk +"' and "+ self.colnames[1] +" = '"+ pk3 +"'")
            else:
                cursor.execute("delete from "+ em +" where "+ self.colnames[0] +" = '"+ pk +"' ")
                
            mydb.commit()
            # self.select_table()
            QMessageBox.information(self,"Delete Form","Contact Details Deleted successfully !")

        except Exception as e:
            print(e)
            print("Error in deletedb ")


    def show_table(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            tablename = self.cb1.currentText()
            cursor.execute("select * from "+ tablename +" ")
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
    app.exec()

if __name__ == '__main__':
    main()