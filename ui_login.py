# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(289, 163)
        self.gridLayoutWidget = QtWidgets.QWidget(widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_user = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_user.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout.addWidget(self.lineEdit_user)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.Label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.gridLayout.addWidget(self.lineEdit_passwd, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 1, 1, 1)
        self.btn_login_submit = QtWidgets.QPushButton(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btn_login_submit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_login_submit.setFont(font)
        self.btn_login_submit.setMouseTracking(True)
        self.btn_login_submit.setAutoDefault(False)
        self.btn_login_submit.setDefault(True)
        self.btn_login_submit.setObjectName("btn_login_submit")
        self.gridLayout.addWidget(self.btn_login_submit, 4, 1, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "数学建模登录系统"))
        self.lineEdit_user.setText(_translate("widget", "admin"))
        self.Label.setText(_translate("widget", "用户名："))
        self.label_2.setText(_translate("widget", "密  码："))
        self.checkBox.setText(_translate("widget", "保存用户名和密码"))
        self.btn_login_submit.setText(_translate("widget", "登        录"))
