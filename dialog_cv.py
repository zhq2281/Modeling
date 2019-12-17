# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
from ui_dialog_cv import Ui_Dialog

from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog,QGridLayout,QLabel,QPushButton

class cv_win(QDialog,Ui_Dialog):
    def __init__(self):
        super(cv_win,self).__init__()
        self.setupUi(self)
        self.img=np.ndarray(())

        self.ptn_open.clicked.connect(self.openslot)
        self.ptn_save.clicked.connect(self.saveslot)
        self.ptn_process.clicked.connect(self.processslot)
        self.ptn_quit.clicked.connect(self.close)
        self.exec_()

    def openslot(self):
        filename,tmp=QFileDialog.getOpenFileName(self,"Open Image","Image","*.png *.jpg *.bmp")
        if filename is "":
            return
        self.img=cv2.imread(filename,-1)
        # self.size=(int(cv_win.width(self)*0.8),int(cv_win.height(self)*0.8))
        # self.shrink=cv2.resize(self.img,self.size,interpolation=cv2.INTER_AREA)
        if self.img.size==1:
            return
        self.refreshShow()

    def saveslot(self):
        filename,tmp=QFileDialog.getSaveFileName(self,"Save Image","Image","*.png *.jpg *.bmp")
        if filename is "":
            return
        if self.img.size==1:
            return
        cv2.imwrite(filename,self.img)

    def processslot(self):
        if self.img.size == 1:
            return
        # 对图像做模糊处理，窗口设定为5*5
        self.img = cv2.blur(self.img, (5, 5))
        self.refreshShow()

    def refreshShow(self):
        # 提取图像的通道和尺寸，用于将OpenCV下的image转换成Qimage
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label.setPixmap(QPixmap.fromImage(self.qImg))

if __name__ == "__main__":
    a=QApplication(sys.argv)
    w=cv_win()
    w.show()
    sys.exit(a.exec_())