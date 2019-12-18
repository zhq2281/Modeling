# -*- coding: utf-8 -*-

'''
2019/12/13 16:59
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from dialog_plot import MainDialogImgBW
from dialog_cv   import cv_win
from dialog_cv_add import cv_add_win

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5


from ui_main import Ui_MainWindow

class Ui_Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Ui_Main,self).__init__()
        self.setupUi(self)
      #  self.pushButton.clicked.connect(MainDialogImgBW)
        self.actionplot_Lne.triggered.connect(MainDialogImgBW)
        self.actionOpenCV.triggered.connect(cv_win)
        self.actionOpenCv_add.triggered.connect(cv_add_win)

        self.setStyleSheet("#MainWindow{background-image:url(./pic/back.jpg);}")  # mainwindow background pic



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=Ui_Main()
    main=MainDialogImgBW()
    # main.show()
    # window.show()
    sys.exit(app.exec_())