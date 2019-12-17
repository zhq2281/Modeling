# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_dialog_cv_add.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ptn_open = QtWidgets.QPushButton(Dialog)
        self.ptn_open.setObjectName("ptn_open")
        self.horizontalLayout_2.addWidget(self.ptn_open)
        self.ptn_huidu = QtWidgets.QPushButton(Dialog)
        self.ptn_huidu.setObjectName("ptn_huidu")
        self.horizontalLayout_2.addWidget(self.ptn_huidu)
        self.ptn_erzhi = QtWidgets.QPushButton(Dialog)
        self.ptn_erzhi.setObjectName("ptn_erzhi")
        self.horizontalLayout_2.addWidget(self.ptn_erzhi)
        self.ptn_mohu = QtWidgets.QPushButton(Dialog)
        self.ptn_mohu.setObjectName("ptn_mohu")
        self.horizontalLayout_2.addWidget(self.ptn_mohu)
        self.ptn_exit = QtWidgets.QPushButton(Dialog)
        self.ptn_exit.setObjectName("ptn_exit")
        self.horizontalLayout_2.addWidget(self.ptn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图像处理"))
        self.label_2.setText(_translate("Dialog", "原始图像"))
        self.label.setText(_translate("Dialog", "处理后图像"))
        self.ptn_open.setText(_translate("Dialog", "打开"))
        self.ptn_huidu.setText(_translate("Dialog", "灰度"))
        self.ptn_erzhi.setText(_translate("Dialog", "二值"))
        self.ptn_mohu.setText(_translate("Dialog", "模糊"))
        self.ptn_exit.setText(_translate("Dialog", "退出"))
