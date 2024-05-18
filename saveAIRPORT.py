from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

import sys

import mysql.connector as con


ui,_=loadUiType('/home/ateium/SQL_PROJECT/saveAIRPORT.ui')


class MainApp(QWidget,ui):

    def __init__(self):

        QWidget.__init__(self)

        self.setupUi(self)

        self.b1.clicked.connect(self.savedb)


    def savedb(self):

        try:

            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")

            cursor = mydb.cursor()

            AP_NAME = self.tb1.text()

            COUNTRY = self.tb2.text()

            CITY_NAME = self.tb3.text()

            qry = "insert into AIRPORT values(%s,%s,%s)"

            value = (AP_NAME, COUNTRY, CITY_NAME)

            cursor.execute(qry,value)

            mydb.commit()

            QMessageBox.information(self,"DB Insert","Contacts saved successfully")

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