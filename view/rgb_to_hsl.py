# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\rgb_to_hsl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import colorsys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_RGB_to_HSL(object):
    def setupUi(self, Dialog_RGB_to_HSL):
        Dialog_RGB_to_HSL.setObjectName("Dialog_RGB_to_HSL")
        Dialog_RGB_to_HSL.resize(202, 128)
        self.label = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label.setGeometry(QtCore.QRect(20, 20, 21, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 16, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 16, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 40, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 60, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label_4.setGeometry(QtCore.QRect(130, 40, 16, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 40, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label_5.setGeometry(QtCore.QRect(130, 60, 16, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 20, 31, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Dialog_RGB_to_HSL)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(130, 20, 21, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog_RGB_to_HSL)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 60, 31, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Dialog_RGB_to_HSL)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog_RGB_to_HSL)
        self.groupBox.setGeometry(QtCore.QRect(80, 20, 41, 51))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.mode = 0
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        
        self.radioButton.toggled.connect(self.rgb2hsl)
        self.radioButton_2.toggled.connect(self.hsl2rgb)
        self.pushButton.clicked.connect(self.conversor)

        self.retranslateUi(Dialog_RGB_to_HSL)

        QtCore.QMetaObject.connectSlotsByName(Dialog_RGB_to_HSL)

    def retranslateUi(self, Dialog_RGB_to_HSL):
        _translate = QtCore.QCoreApplication.translate
        Dialog_RGB_to_HSL.setWindowTitle(_translate("Dialog_RGB_to_HSL", "Dialog"))
        self.label.setText(_translate("Dialog_RGB_to_HSL", "R:"))
        self.label_2.setText(_translate("Dialog_RGB_to_HSL", "G:"))
        self.label_3.setText(_translate("Dialog_RGB_to_HSL", "B:"))
        self.label_4.setText(_translate("Dialog_RGB_to_HSL", "S:"))
        self.label_5.setText(_translate("Dialog_RGB_to_HSL", "V:"))
        self.label_6.setText(_translate("Dialog_RGB_to_HSL", "H:"))
        self.pushButton.setText(_translate("Dialog_RGB_to_HSL", "Converter"))
        self.radioButton.setText(_translate("Dialog_RGB_to_HSL", "→"))
        self.radioButton_2.setText(_translate("Dialog_RGB_to_HSL", "←"))

    def convert_RGB_to_HSV(self, r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0 # Divida tudo por 255
        mx = max(r, g, b) # Encontre os máximos e os mínimos das cores
        mn = min(r, g, b)
        luminance = (mx + mn) / 2.0
        if mx == mn:
            hue = 0
            saturation = 0
        if luminance <= 0.5:
            saturation = (mx - mn) / (mx + mn)
        else:
            saturation = (mx - mn) / (2.0 - mx - mn)
        if mx == r:
            hue = (g - b) / (mx - mn)
        elif mx == g:
            hue = 2.0 + (b - r) / (mx - mn)
        else:
            hue = 4.0 + (r - g) / (mx - mn)
        hue *= 60.0
        if hue < 0:
            hue += 360
        return((math.floor(hue *  (2 / 3)), math.floor(saturation*240), math.floor(luminance * 240)))
    
    def convert_HSL_to_RGB(self, h, s, l):
        h, s, l = h/360, s/100.0, l / 100.0
        if s == 0:
            l = l * 255
            return(l, l, l)
        # h = h / 360.0
        # s = s / 255.0
        if l < 0.5:
            q = l * (1 + s)
        if l >= 0.5:
            q = (l + s) - (l * s)
        p = 2 * l - q
        h = h / 360.0
        r = h + 1.0 / 3.0
        g = h
        b = h - 1.0 / 3.0
        if r*6 < 0:
            r = r + 1
        if r*2 > 1:
            r = q
        if r*3 < 2:
            r = p + (q - p) * (2.0 / 3.0 - r) * 6.0
        if g*6 < 0:
            g = g + 1
        if g*2 > 1:
            g = q
        if g*3 < 2:
            g = p + (q - p) * (2.0 / 3.0 - g) * 6.0
        if b*6 < 0:
            b = b + 1
        if b*2 > 1:
            b = q
        if b*3 < 2:
            b = p + (q - p) * (2.0 / 3.0 - b) * 6.0
        return(math.floor(r * 255), math.floor(g * 255), math.floor(b * 255))

    def hue2rgb(self, n, h, s, l):
        k = (n + h / 3.0) % 12
        return math.floor((l - (s * min(l, 1 - l)) * max(-1, min({k - 3, 9 - k, 1}))) * 255)

    def conversor(self):
        if self.mode == 0:
            r = float(self.lineEdit.text())
            g = float(self.lineEdit_2.text())
            b = float(self.lineEdit_3.text())
            print(r, g, b)
            h, s, l = self.convert_RGB_to_HSV(r/100, g/100, b/100)
            print(h, s, l)
            self.lineEdit_4.setText(str(s))
            self.lineEdit_5.setText(str(h))
            self.lineEdit_6.setText(str(l))
        else:
            h = float(self.lineEdit_4.text())
            s = float(self.lineEdit_5.text())
            l = float(self.lineEdit_6.text())
            print(h, s, l)
            r, g, b = self.convert_HSL_to_RGB(s, h, l)
            print(r, g, b)
            self.lineEdit.setText(str(r))
            self.lineEdit_2.setText(str(g))
            self.lineEdit_3.setText(str(b))

    def rgb2hsl(self):
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.mode = 0

    def hsl2rgb(self):
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.mode = 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_RGB_to_HSL = QtWidgets.QDialog()
    ui = Ui_Dialog_RGB_to_HSL()
    ui.setupUi(Dialog_RGB_to_HSL)
    Dialog_RGB_to_HSL.show()
    sys.exit(app.exec_())
