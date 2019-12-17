# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 23))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionplot_Lne = QtWidgets.QAction(MainWindow)
        self.actionplot_Lne.setObjectName("actionplot_Lne")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionOpenCV = QtWidgets.QAction(MainWindow)
        self.actionOpenCV.setObjectName("actionOpenCV")
        self.menu.addAction(self.actionopen)
        self.menu_2.addAction(self.actionplot_Lne)
        self.menu_2.addAction(self.actionOpenCV)
        self.menu_3.addAction(self.actionabout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数学建模设计系统V1.0"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "建模"))
        self.menu_3.setTitle(_translate("MainWindow", "说明"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionplot_Lne.setText(_translate("MainWindow", "plot Line"))
        self.actionabout.setText(_translate("MainWindow", "about "))
        self.actionOpenCV.setText(_translate("MainWindow", "OpenCV"))
