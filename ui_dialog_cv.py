# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_cv.ui'
#
# Created by: PyQt5 UI code generator 5.13.0123
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(745, 600)
        Dialog.setMaximumSize(QtCore.QSize(1024, 768))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(1024, 768))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ptn_open = QtWidgets.QPushButton(Dialog)
        self.ptn_open.setObjectName("ptn_open")
        self.horizontalLayout_2.addWidget(self.ptn_open)
        self.ptn_save = QtWidgets.QPushButton(Dialog)
        self.ptn_save.setObjectName("ptn_save")
        self.horizontalLayout_2.addWidget(self.ptn_save)
        self.ptn_process = QtWidgets.QPushButton(Dialog)
        self.ptn_process.setObjectName("ptn_process")
        self.horizontalLayout_2.addWidget(self.ptn_process)
        self.ptn_quit = QtWidgets.QPushButton(Dialog)
        self.ptn_quit.setObjectName("ptn_quit")
        self.horizontalLayout_2.addWidget(self.ptn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图片处理"))
        self.label.setText(_translate("Dialog", "请打开要处理的图片"))
        self.ptn_open.setText(_translate("Dialog", "Open"))
        self.ptn_save.setText(_translate("Dialog", "Save"))
        self.ptn_process.setText(_translate("Dialog", "Process"))
        self.ptn_quit.setText(_translate("Dialog", "Quit"))
