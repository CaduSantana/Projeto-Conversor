# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from colorsys import rgb_to_hls
import PIL
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPainter, QImage, QPen
from PyQt5.QtCore import QSize, QRect, QBuffer, QPoint
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QSizePolicy, QAction, QWidget, QPushButton, QLabel, QFrame, QMenu, QMenuBar, QStatusBar
from PyQt5.Qt import qRed, qGreen, qBlue, qRgb
from PIL import Image
import numpy as np
import windowrgb, rgb_to_hsl, testeDesenho, io, winsound, inspect
from math import floor
import matplotlib.pyplot as plt
import skimage.color
import skimage.io


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(360, 460, 75, 23))
        self.button1.setObjectName("button1")
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(10, 10, 381, 331))
        self.foto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foto.setText("")
        self.foto.setObjectName("foto")
        # aligns content of label to center
        # self.foto.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_2 = QtWidgets.QLabel(self.centralwidget)
        self.foto_2.setGeometry(QtCore.QRect(410, 10, 371, 331))
        self.foto_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foto_2.setText("")
        self.foto_2.setObjectName("foto_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuOperacoes = QtWidgets.QMenu(self.menubar)
        self.menuOperacoes.setObjectName("menuOpera_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_como.setObjectName("actionSalvar_como")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionSeparador_RGB = QtWidgets.QAction(MainWindow)
        self.actionSeparador_RGB.setObjectName("actionSeparador_RGB")
        self.actionDesenhar = QtWidgets.QAction(MainWindow)
        self.actionDesenhar.setObjectName("actionDesenhar")
        self.actionInverter_cores = QtWidgets.QAction(MainWindow)
        self.actionInverter_cores.setObjectName("actionInverter_cores")
        self.actionConverter_de_RGB_para_HSL = QtWidgets.QAction(MainWindow)
        self.actionConverter_de_RGB_para_HSL.setObjectName("actionConverter_de_RGB_para_HSL")
        self.actionEqualizar_Histograma = QtWidgets.QAction(MainWindow)
        self.actionEqualizar_Histograma.setObjectName("actionEqualizar_Histograma")
        self.actionDCT = QtWidgets.QAction(MainWindow)
        self.actionDCT.setObjectName("actionDCT")
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionSalvar_como)
        self.menuAjuda.addAction(self.actionSobre)
        self.menuOperacoes.addAction(self.actionSeparador_RGB)
        self.menuOperacoes.addAction(self.actionInverter_cores)
        self.menuOperacoes.addAction(self.actionDesenhar)
        self.menuOperacoes.addAction(self.actionConverter_de_RGB_para_HSL)
        self.menuOperacoes.addAction(self.actionEqualizar_Histograma)
        self.menuOperacoes.addAction(self.actionDCT)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuOperacoes.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.actionAbrir.triggered.connect(self.abrir)
        self.actionSobre.triggered.connect(self.sobre)
        self.actionSeparador_RGB.triggered.connect(self.rgb)
        self.actionInverter_cores.triggered.connect(self.inverterCor)
        self.actionDesenhar.triggered.connect(self.desenhar)
        self.actionConverter_de_RGB_para_HSL.triggered.connect(self.insertColorValues)
        self.actionEqualizar_Histograma.triggered.connect(self.histogram)
        # self.actionDCT.triggered.connect(self.discrete_cosine_transform)

        # self.convert_HSV_to_RGB(111, 140, 120)

        self.button1.clicked.connect(self.converterCorParaCinza)
        # self.button1.clicked.connect(self.inverterCor)
        # self.button1.clicked.connect(self.apenasVermelho)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "(0,0) R: 0, G: 0, B: 0"))
        self.button1.setText(_translate("MainWindow", "←"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.menuOperacoes.setTitle(_translate("MainWindow", "Operações"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_como.setText(_translate("MainWindow", "Salvar como..."))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionSeparador_RGB.setText(_translate("MainWindow", "Separador RGB"))
        self.actionInverter_cores.setText(_translate("MainWindow", "Inverter cores"))
        self.actionDesenhar.setText(_translate("MainWindow", "Desenhar"))
        self.actionConverter_de_RGB_para_HSL.setText(_translate("MainWindow", "Conversor RGB/HSL"))
        self.actionEqualizar_Histograma.setText(_translate("MainWindow", "Equalizar histograma"))
        self.actionDCT.setText(_translate("MainWindow", "DCT"))
        

    def abrir(self):
        dlg = QFileDialog()  # cria um dialogo para selecionar o arquivo
        # seleciona qualquer tipo de arquivo
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Imagens (*.png *.jpg *.jpeg)") # filtra os arquivos
        # filenames = list # cria uma lista para armazenar os nomes dos arquivos

        filename = dlg.getOpenFileName()  # abre o dialogo e armazena o nome do arquivo
        # coloca o conteudo do arquivo na textbox
        myPixmap = QtGui.QPixmap(filename[0])
        self.foto.setPixmap(myPixmap.scaled(self.foto.size(), QtCore.Qt.KeepAspectRatio))
        # self.foto.setAlignment(QtCore.Qt.AlignCenter) # TODO Fix this

        # self.foto.setScaledContents(True)  # ajusta o tamanho da imagem

        # pil_image = self.convert_qimage_to_pil(self.foto.pixmap().toImage())
        # im = pil_image.convert('RGB')
        # dados = im.tobytes("raw", "RGB")
        # qim = QtGui.QImage(dados, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)       

        # self.foto.setPixmap(QtGui.QPixmap.fromImage(qim))
        self.foto.mouseMoveEvent = self.mouseMoveEvent
        self.foto.setMouseTracking(True)


    #converts QImage to PIL Image
    def convert_qimage_to_pil(self, qimage):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        qimage.save(buffer, "PNG")
        pil_image = PIL.Image.open(io.BytesIO(buffer.data()))
        # pil_image.show()

        return pil_image

    def converterCorParaCinza(self):
        # converts the image to grayscale bitwise using bits(). each pixel is a 3 by 1 vector. the first element is the red value, the second is the green value, and the third is the blue value. the value is between 0 and 255. the value of each element is multiplied by the corresponding weight. the sum of the three values is the final value for that pixel.
        # luminancia = (r + g + b) / 3

        image = self.foto.pixmap().toImage()
        # arrayptr = image.bits()
        for x in range(image.width()):
            for y in range(image.height()):
                pixel = image.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                # luminancia = (r + g + b) / 3
                luminancia = r*0.299 + g*0.587 + b*0.114
                image.setPixel(x, y, qRgb(round(luminancia), round(luminancia), round(luminancia)))
        self.foto_2.setPixmap(QtGui.QPixmap(image.scaled(self.foto_2.size(), QtCore.Qt.KeepAspectRatio)))
        # self.foto_2.setScaledContents(True)

    def inverterCor(self):
        image = self.foto.pixmap().toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                pixel = image.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                image.setPixel(x, y, qRgb(255-r, 255-g, 255-b))
        self.foto_2.setPixmap(QtGui.QPixmap(image.scaled(self.foto_2.size(), QtCore.Qt.KeepAspectRatio)))
        # self.foto_2.setScaledContents(True)

    # def apenasVermelho(self):
    #     image = self.foto.pixmap().toImage()
    #     for x in range(image.width()):
    #         for y in range(image.height()):
    #             pixel = image.pixel(x, y)
    #             r = qRed(pixel)
    #             g = qGreen(pixel)
    #             b = qBlue(pixel)
    #             image.setPixel(x, y, qRgb(r, 0, 0))
    #     self.foto_2.setPixmap(QtGui.QPixmap(image))
    #     self.foto_2.setScaledContents(True)

    def rgb(self):
        self.Form = QtWidgets.QWidget()
        rgbWindow = windowrgb.Ui_Form()
        rgbWindow.setupUi(self.Form)

        imageR = self.foto.pixmap().toImage()
        for x in range(imageR.width()):
            for y in range(imageR.height()):
                pixel = imageR.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                imageR.setPixel(x, y, qRgb(r, 0, 0))
        rgbWindow.foto.setPixmap(QtGui.QPixmap(imageR.scaled(rgbWindow.foto.size(), QtCore.Qt.KeepAspectRatio)))
        # rgbWindow.foto.setScaledContents(True)
        
        imageG = self.foto.pixmap().toImage()
        for x in range(imageG.width()):
            for y in range(imageG.height()):
                pixel = imageG.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                imageG.setPixel(x, y, qRgb(0, g, 0))
        rgbWindow.foto_2.setPixmap(QtGui.QPixmap(imageG.scaled(rgbWindow.foto_2.size(), QtCore.Qt.KeepAspectRatio)))
        # rgbWindow.foto_2.setScaledContents(True)
        
        imageB = self.foto.pixmap().toImage()
        for x in range(imageB.width()):
            for y in range(imageB.height()):
                pixel = imageB.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                imageB.setPixel(x, y, qRgb(0, 0, b))
        rgbWindow.foto_3.setPixmap(QtGui.QPixmap(imageB.scaled(rgbWindow.foto_3.size(), QtCore.Qt.KeepAspectRatio)))
        # rgbWindow.foto_3.setScaledContents(True)
    
        self.Form.show()
    
    def desenhar(self):
        duration = 1000  # milliseconds
        freq = 440  # Hz
        self.foto.mousePressEvent = self.mouseClickEvent
        winsound.Beep(freq, duration)


    # the following function logs the current xy coordinates of the mouse when the user hovers on the image label and prints it on the status bar
    def mouseMoveEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        ibagem = self.foto.pixmap().toImage()
        # ibagem.save("teste.png")
        pixel = ibagem.pixel(x, y)
        r = qRed(pixel)
        g = qGreen(pixel)
        b = qBlue(pixel)

        self.statusbar.showMessage(
            "({},{}) R: {}, G: {}, B: {}".format(x, y, r, g, b))

    def mouseClickEvent(self, event):
        x, y = event.pos().x(), event.pos().y()
        ibagem = self.foto.pixmap().toImage()
        ibagem.setPixel(x, y, qRgb(255, 0, 0))
        print("foi")
        self.foto.setPixmap(QtGui.QPixmap(ibagem.scaled(self.foto.size(), QtCore.Qt.KeepAspectRatio)))
    
    def insertColorValues(self):
        conversor = rgb_to_hsl.Ui_Dialog_RGB_to_HSL()
        MainWindow.addWidget(conversor)
        MainWindow.setCurrentIndex(MainWindow.currentIndex()+1) 
        MainWindow.removeWidget(self)

    def equalize_image_histogram(self):
        image = self.foto_2.pixmap().toImage()
        image_histogram = image.copy()
        image_histogram.fill(QtCore.Qt.black)
        for x in range(image.width()):
            for y in range(image.height()):
                pixel = image.pixel(x, y)
                r = qRed(pixel)
                g = qGreen(pixel)
                b = qBlue(pixel)
                image_histogram.setPixel(x, y, qRgb(r, g, b))
        image_histogram.save("teste.png")
        self.foto_2.setPixmap(QtGui.QPixmap(image_histogram.scaled(self.foto_2.size(), QtCore.Qt.KeepAspectRatio)))
        self.histogram()
        # self.foto_2.setScaledContents(True)

    def histogram(self):
        self.foto_2.pixmap().toImage().save("temp.png")
        ibagem = skimage.io.imread(fname="temp.png")
        # image_histogram = ibagem.copy()
        histogram, bin_edges = np.histogram(ibagem, bins=256, range=(0, 1))
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.ylabel("pixel count")
        plt.xlim([0.0, 1.0])  # <- named arguments do not work here

        plt.plot(bin_edges[0:-1], histogram)  # <- or here
        plt.show()


    # def discrete_cosine_transform(self):
    #     # This function aplies DCT on a given image
    #     # The image is converted to a matrix and then the DCT is applied
    #     # The result is converted back to a image and then it is shown on the screen
        
    #     ibagem = open('city.jpg', 'rb')
    #     image = Image.open(ibagem)
    #     image = image.convert('RGB')
    #     image = np.array(image)

    #     c = np.array.reshape(128,128)

    #     for i in range(image.width-1): # Iterate over the rows
    #         for x in range(image.width()):
    #             for y in range(image.height()):
    #                 pixel = image.pixel(x, y)
    #                 r = qRed(pixel)
    #                 g = qGreen(pixel)
    #                 b = qBlue(pixel)
    #                 c[x][y] = np.cos((2 * x + 1) * (y + 0.5) * np.pi / (2 * image.width()))
    #     imabe = Image.fromarray(c)
    #     imabe.show()


        
    def sobre(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sobre")
        msg.setText("Projeto de conversão de imagens.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("Desenvolvido por Carlos Santana.")
        # msg.setDetailedText("Detalhes.")

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())   