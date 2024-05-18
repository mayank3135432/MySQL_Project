from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

import sys

import mysql.connector as con

ui,_=loadUiType('/home/ateium/SQL_PROJECT/saveAIRLINE.ui')


class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.b1.clicked.connect(self.savedb)


    def savedb(self):
        try:
            mydb = con.connect(host="localhost",user="root", password="admin",db="AIRPORT")
            cursor = mydb.cursor()
            NAME = self.tb1.text()
            cursor.execute("insert into AIRLINE(AL_NAME) values('"+ NAME +"')");
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