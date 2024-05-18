from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys

import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/updateEMPLOYEE.ui')

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
            cursor.execute("select * from EMPLOYEE")
            result = cursor.fetchall()
            self.cb1.clear() #clear combobox
            if result:
                for EMPLOYEE in result:
                    print(type(EMPLOYEE))
                    self.cb1.addItem(str(EMPLOYEE[0]))

            cursor.execute("select * from AIRPORT")
            result = cursor.fetchall()
            self.cb2.clear() #clear combobox
            if result:
                for stuff in result:
                    print(type(stuff))
                    self.cb2.addItem(stuff[0])
        except Exception as e:
            print(e)
            print("Error in fill combo box ")
    def fill_details_on_combobox_selected(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            cursor.execute("select * from EMPLOYEE where EMP_ID='"+ em +"'")
            result = cursor.fetchall();
            if result:
                for EMPLOYEE in result:
                    #self.tb1.setText(str(AIRPORT[0]))
                    self.tb2.setText(str(EMPLOYEE[1]))
                    self.tb3.setText(str(EMPLOYEE[2]))
                    self.tb4.setText(str(EMPLOYEE[3]))
                    self.tb5.setText(str(EMPLOYEE[4]))
                    self.tb6.setText(str(EMPLOYEE[5]))
                    #self.cb2.setItemText(0,str(EMPLOYEE[6]))
        except Exception as e:
            print(e)
            print("Error in fill details on combo box select ")
    
    def updatedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            em = self.cb1.currentText()
            name = self.tb2.text()
            jobtype = self.tb3.text()
            salary = self.tb4.text()
            DOB = self.tb5.text()
            PHONE_NO = self.tb6.text()
            apname = self.cb2.currentText()
            cursor.execute("update EMPLOYEE set EMP_ID = '"+ em +"', ENAME = '"+ name +"', JOBTYPE = '"+ jobtype +"', SALARY = '"+ salary +"', DOB = '"+ DOB +"', PHONE_NO = '"+ PHONE_NO +"' , AP_NAME = '"+ apname +"' where EMP_ID = '"+ em +"'");
            result = cursor.fetchall();
            mydb.commit()
            QMessageBox.information(self, "Update Form", "Employee Details Updated Succsessfully")

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