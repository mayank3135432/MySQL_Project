from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import os
import sys

import mysql.connector as con
ui,_=loadUiType('/home/ateium/SQL_PROJECT/Admin_Login.ui')

class MainApp(QWidget,ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.b1.clicked.connect(self.login)


    def login(self):
        try:
            
            if self.tb1.text() == 'admin' and self.tb2.text() == 'admin':
                os.system(f'python /home/ateium/SQL_PROJECT/table.py &')
            else:
                QMessageBox.information(self,"LOGIN","Wrong Password")
        except Exception as e:
            print(e)
            print('ERROR IN MAINAPP')
    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()