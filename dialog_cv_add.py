import sys
import cv2
import numpy as np
from ui_dialog_cv_add import Ui_Dialog

from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog,QGridLayout,QLabel,QPushButton

class cv_add_win(QDialog,Ui_Dialog):
    def __init__(self):
        super(cv_add_win,self).__init__()
        self.setupUi(self)
        self.captured = np.ndarray(())
        self.ptn_open.clicked.connect(self.btnReadImage_Clicked)
        self.ptn_huidu.clicked.connect(self.btnGray_Clicked)
        self.ptn_erzhi.clicked.connect(self.btnThreshold_Clicked)
        self.ptn_mohu.clicked.connect(self.btnMohu_Clicked)
        self.ptn_exit.clicked.connect(self.close)


    def btnReadImage_Clicked(self):
        # 打开文件选取对话框
        filename,  _ = QFileDialog.getOpenFileName(self,"Open Image","Image","*.png *.jpg *.bmp")
        if filename is "":
            return
        else:
            self.captured = cv2.imread(str(filename))
            # OpenCV图像以BGR通道存储，显示时需要从BGR转到RGB
            self.captured = cv2.cvtColor(self.captured, cv2.COLOR_BGR2RGB)
            self.captured2 = self.captured

        if self.captured.size==1:
            return
        self.refreshShow()
    def refreshShow(self):
        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        QImg = QImage(self.captured.data, cols, rows,
                      bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label_2.size()))

    def btnGray_Clicked(self):
        self.captured = cv2.cvtColor(self.captured, cv2.COLOR_RGB2GRAY)

        rows, columns = self.captured.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.captured.data, columns, rows,
                      bytesPerLine, QImage.Format_Indexed8)
        self.label.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label.size()))
    def btnThreshold_Clicked(self):
        _, self.captured=cv2.threshold(
            self.captured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rows, cloumns=self.captured.shape
        bytePerLine=cloumns
        QImg=QImage(self.captured.data, cloumns, rows,
                    bytePerLine, QImage.Format_Indexed8)
        self.label.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label.size()))
    def btnMohu_Clicked(self):


        # 对图像做模糊处理，窗口设定为5*5
        height, width, channel = self.captured2.shape
        bytesPerline = 3 * width
        QImg = QImage(self.captured2.data, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # 将QImage显示出来
        self.label_2.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_2.size()))

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=cv_add_win()
    window.show()
    sys.exit(app.exec())