# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from ui_login import Ui_widget
import main

class login_window(QtWidgets.QWidget,Ui_widget):
    def __init__(self):
        super(login_window,self).__init__()
        self.setupUi(self)
        self.btn_login_submit.clicked.connect(self.btn_login_fun)
        self.lineEdit_passwd.returnPressed.connect(self.btn_login_fun)
    def btn_login_fun(self):
        account=self.lineEdit_user.text()
        password=self.lineEdit_passwd.text()
        if account==password:
            Ui.show()
            window.hide()
        else:
            reply=QMessageBox.warning(self,"提示","密码错误请重新输入！",QMessageBox.Yes)
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=login_window()
    Ui=main.Ui_Main()
    window.show()
    sys.exit(app.exec_())