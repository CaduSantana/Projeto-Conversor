import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
from PyQt5.QtGui import QKeySequence, QPixmap, QMovie
from PyQt5.QtWidgets import QAction, QDialog, QApplication, QMainWindow, QFileDialog
import numpy as np
from PIL import ImageQt
from PIL import Image, ImageOps
import cv2
import image_processing as pdi
import color_conversion as color
import histogram_equalization as histeq
import power_law_tranformation as gamma
import laplacian_filter2 as laplacian
import sobel
import median_filter as md
import average_filter as av
import threshold as td

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"menu.ui", self) 
        # self.movie = QMovie("."+os.path.sep+"icons"+os.path.sep+"paint.gif")
        # self.label_2.setMovie(self.movie)
        # self.movie.start()          
        global numpyimage
        numpyimage = 0
        self.pushButton.clicked.connect(self.gotoaula2a)
        self.pushButton_6.clicked.connect(self.gototrabalhopratico)
        self.pushButton_7.clicked.connect(self.gotoaula5a)   

    def gotoaula2a(self):
        aula2a = Aula2aScreen()
        widget.addWidget(aula2a)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)
    
    def gototrabalhopratico(self):
        tbpratico = TrabalhoPraticoScreen()
        widget.addWidget(tbpratico)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)  

    def gotoaula5a(self):
        aula5a = Aula5aScreen()
        widget.addWidget(aula5a)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula9(self):
        aula9 = Aula9Screen()
        widget.addWidget(aula9)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

class  Aula2aScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(600)
        widget.setFixedWidth(1090)
        super(Aula2aScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula2a.ui", self)
        self.flag = False
        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Save.triggered.connect(self.save_file)
        self.action_Save.setShortcut(QKeySequence("Ctrl+S"))

        self.actionReturn_Menu.triggered.connect(self.gotomenu)
        self.actionReturn_Menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q"))

        self.action_Grayscale_Conversion.triggered.connect(self.color_to_grayscale)
        self.action_Grayscale_Conversion.setShortcut(QKeySequence("Ctrl+G"))

        self.action_Negative.triggered.connect(self.negative_)
        self.action_Negative.setShortcut(QKeySequence("Ctrl+N"))

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 2A", "."+os.path.sep+"imagens"+os.path.sep+"aula2a", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            img = Image.open(filename[0])
            numpyimage = np.asarray(img)
            self.label.setPixmap(QPixmap(filename[0]))

    def save_file(self):
        if(self.flag):
            file = QFileDialog.getSaveFileName(None,"Aula 2A", "."+os.path.sep+"Saves", "Images (*.bmp)")
            if(file[0] != ''):
                image = ImageQt.fromqpixmap(self.label_4.pixmap())
                image.save(file[0])

    def color_to_grayscale(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None
        grayscale = pdi.rgb2gray(numpyimage)
        PIL_image = Image.fromarray(np.uint8(grayscale)).convert('RGB')
        PIL_image.save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        self.flag = True

    def negative_(self):
        if(np.all(numpyimage == 0)):
            return None        
        img = pdi.inverse(numpyimage) 
        Image.fromarray(img).save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        self.flag = True

class TrabalhoPraticoScreen(QMainWindow):
    def __init__(self):
        super(TrabalhoPraticoScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"trab_pratico.ui", self)
        self.action_Return_menuTB.triggered.connect(self.gotomenu)        
        self.action_Return_menuTB.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q"))   

        #self.pushButton.clicked.connect(self.convert_color)    

        self.pushButton_3.clicked.connect(self.RGB2HSL) 
        self.pushButton_2.clicked.connect(self.HSL2RGB)  

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)


    def lenght_number(self, number):
        number = abs(int(number))
        if number < 2:
            return 1
        count = 0
        value = 1
        while value <= number:
            value *= 10
            count += 1
        return count


    def RGB2HSL(self):
        H,S,L = self.read_HSL()
        R, G, B = self.read_RGB()     
        if(R.isnumeric() and G.isnumeric() and B.isnumeric()):
            f1 = self.lenght_number(R) 
            f2 = self.lenght_number(G) 
            f3 = self.lenght_number(B) 
            if( (f1>=1 and f1<=3) and (f2>=1 and f2<=3) and (f3>=1 and f3<=3) ):
                self.setRGB_button(R,G,B)
                R,G,B = int(R, base=10),int(G, base=10),int(B, base=10)
                H, S, L = color.RGB_to_HSL(R,G,B)
                self.setHSL(H,S,L)

    def HSL2RGB(self):
        R,G,B = self.read_RGB()
        H, S, L = self.read_HSL()        
        if(H.isnumeric() and S.isnumeric() and L.isnumeric()):
            f1 = self.lenght_number(H) 
            f2 = self.lenght_number(S) 
            f3 = self.lenght_number(L) 
            if( (f1>=1 and f1<=3) and (f2>=1 and f2<=3) and (f3>=1 and f3<=3) ):
                H, S, L = int(H, base=10), int(S, base=10), int(L, base=10)
                R, G, B = color.HSL_to_RGB(H, S, L)
                self.setRGB(R,G,B)
                self.setRGB_button(R,G,B)

    def read_RGB(self):
        R = self.textEdit.toPlainText()
        G = self.textEdit_2.toPlainText()
        B = self.textEdit_3.toPlainText()
        return R, G, B

    def read_HSL(self):
        H = self.textEdit_6.toPlainText()
        S = self.textEdit_4.toPlainText()
        L = self.textEdit_5.toPlainText()
        return H, S, L        

    def setRGB_button(self,R,G,B):
        self.pushButton.setStyleSheet('background-color: rgb('+str(R)+','+str(G)+','+str(B)+');')

    def setRGB(self,R,G,B):
        R, G, B = str(R), str(G), str(B)
        self.textEdit.setPlainText(R)
        self.textEdit_2.setPlainText(G)
        self.textEdit_3.setPlainText(B)

    def setHSL(self,H,S,L):
        H, S, L = str(H), str(S), str(L)
        self.textEdit_6.setPlainText(H)
        self.textEdit_4.setPlainText(S)
        self.textEdit_5.setPlainText(L)

class Aula5aScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(500)
        widget.setFixedWidth(900)
        super(Aula5aScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a.ui", self)
        # self.movie = QMovie("."+os.path.sep+"icons"+os.path.sep+"waiting_2.gif")
        # self.label_2.setMovie(self.movie)
        # self.movie.start()

        # self.movie2 = QMovie("."+os.path.sep+"icons"+os.path.sep+"message_2.gif")
        # self.label_3.setMovie(self.movie2)
        # self.movie2.start()

        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H"))        

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L"))

        self.action_s_c_r.triggered.connect(self.gotoaula5a_gamma)        
        self.action_s_c_r.setShortcut(QKeySequence("Ctrl+G"))    

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel)        
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q"))        

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)            

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)  

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

class Aula5HistogramScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(500)
        widget.setFixedWidth(900)
        super(Aula5HistogramScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_histrogram.ui", self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q"))   

        self.action_open.triggered.connect(self.open_file)
        self.action_open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_S_c_r.triggered.connect(self.gotoaula5a_gamma)        
        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))   

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L")) 

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel)        
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.pushButton.clicked.connect(self.histo_eq)         

        self.action_Equalized_Image.triggered.connect(self.save_eqimage) 
        self.action_Equalized_Histogram.triggered.connect(self.save_eqhist) 
        self.action_Unequalized_Histogram.triggered.connect(self.save_unhist) 

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)            

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Histogram", "."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"img", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]

    def save_eqimage(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_4.pixmap())
            self.save_file(image)

    def save_unhist(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_2.pixmap())
            self.save_file(image)

    def save_eqhist(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_3.pixmap())
            self.save_file(image)

    def save_file(self, image):
        file = QFileDialog.getSaveFileName(None,"Aula 5 - Histogram", "."+os.path.sep+"Saves", "Images (*.bmp)")
        if(file[0] != ''):
            #image = ImageQt.fromqpixmap(self.label_4.pixmap())
            image.save(file[0])

    def histo_eq(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None
        grayscale = cv2.imread(self.path)
        cv2.imwrite("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"grayscale.png", grayscale)
        self.label.setPixmap(QPixmap("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"grayscale.png"))
        pdi.delete_image("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"grayscale.png")
        #PIL_image = Image.fromarray(np.uint8(grayscale)).convert('RGB')
        class_hist = histeq.HistogramEqualization(grayscale)
        a = class_hist.original_histogram(grayscale)
        class_hist.plot_unequalized_histogram(a,'Unequalized Histogram','Frequency (Number of Pixels)','Intensity (Grey Level)')
        # self.label_2.setPixmap(QPixmap("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"result"+os.path.sep+"unequalized.png"))
        hist_eq = class_hist.histogram_equalization()
        build_image = class_hist.build_image(hist_eq)
        cv2.imwrite("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"result"+os.path.sep+"histogram_equalization.png", build_image)
        self.label_2.setPixmap(QPixmap("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"result"+os.path.sep+"histogram_equalization.png"))
        hist_eq_4_plot = class_hist.histogram_equalization_for_plot(build_image)
        class_hist.plot_equalized_histogram(hist_eq_4_plot,'Equalized Histogram','Frequency (Number of Pixels)','Intensity (Grey Level)')        
        # self.label_2.setPixmap(QPixmap("."+os.path.sep+"imagens"+os.path.sep+"histogram_equalization"+os.path.sep+"result"+os.path.sep+"equalized.png"))
        self.flag = True

class Aula5GammaScreen(QMainWindow):
    def __init__(self):
        super(Aula5GammaScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_gamma.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L")) 

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel)        
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Save.triggered.connect(self.save_file)
        self.action_Save.setShortcut(QKeySequence("Ctrl+S"))

        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))

        self.pushButton.clicked.connect(self.gamma_transformation) 
        
    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)    

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Power Law (Gamma) Transformation", "."+os.path.sep+"imagens"+os.path.sep+"gamma_transformation", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]           

    def save_file(self):
        if(self.flag):
            file = QFileDialog.getSaveFileName(None,"Aula 5 - Power Law (Gamma) Transformation", "."+os.path.sep+"Saves", "Images (*.bmp)")
            if(file[0] != ''):
                image = ImageQt.fromqpixmap(self.label_4.pixmap())
                image.save(file[0])

    def gamma_transformation(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None
        img = ImageQt.fromqpixmap(self.label.pixmap()) 
        c = float(self.textEdit.toPlainText())
        gam = float(self.textEdit_2.toPlainText())
        result = gamma.power_law_tranformation(numpyimage,c,gam)
        Image.fromarray(result).save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")        
        #self.label_2.setPixmap(QPixmap(result))
        self.flag = True

class Aula5LaplacianScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(850)
        widget.setFixedWidth(1350)
        super(Aula5LaplacianScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_laplacian.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.action_S_c_r.triggered.connect(self.gotoaula5a_gamma)        
        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))  

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel)        
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L"))

        self.pushButton.clicked.connect(self.run_laplacian) 

        self.action_Image_A.triggered.connect(self.save_imageA) 
        self.action_Image_B.triggered.connect(self.save_imageB)
        self.action_Image_C.triggered.connect(self.save_imageC)
        self.action_Image_D.triggered.connect(self.save_imageD)

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self) 

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)   

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)  

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Laplacian", "."+os.path.sep+"imagens"+os.path.sep+"laplacian_filter"+os.path.sep+"img", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0] 

    def save_imageA(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_4.pixmap())
            self.save_file(image)

    def save_imageB(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_8.pixmap())
            self.save_file(image)

    def save_imageC(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_7.pixmap())
            self.save_file(image)

    def save_imageD(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_9.pixmap())
            self.save_file(image)

    def save_file(self, image):
        file = QFileDialog.getSaveFileName(None,"Aula 5 - Laplacian", "."+os.path.sep+"Saves", "Images (*.bmp)")
        if(file[0] != ''):
            image.save(file[0])

    def run_laplacian(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None
        img = cv2.imread(self.path,0)     
        LP = laplacian.Laplacian(img) 
        #A
        a = LP.laplace_a()
        Image.fromarray(a).save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")          
        #B
        b = LP.laplace_b()
        Image.fromarray(b).save("tempimg.bmp")
        self.label_8.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        #C
        c = LP.laplace_c()
        Image.fromarray(c).save("tempimg.bmp")
        self.label_7.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")    
        #D
        d = LP.laplace_d()
        Image.fromarray(d).save("tempimg.bmp")
        self.label_9.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp") 
        self.flag = True

class Aula5SobelScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(510)
        widget.setFixedWidth(830)
        super(Aula5SobelScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_sobel.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L")) 

        self.action_S_c_r.triggered.connect(self.gotoaula5a_gamma)        
        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))  

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Save.triggered.connect(self.save_file)
        self.action_Save.setShortcut(QKeySequence("Ctrl+S"))

        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.pushButton.clicked.connect(self.run_sobel) 

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)    

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Sobel", "."+os.path.sep+"imagens"+os.path.sep+"sobel", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]  

    def save_file(self):
        if(self.flag):
            file = QFileDialog.getSaveFileName(None,"Aula 5 - Sobel", "."+os.path.sep+"Saves", "Images (*.bmp)")
            if(file[0] != ''):
                image = ImageQt.fromqpixmap(self.label_4.pixmap())
                image.save(file[0])

    def run_sobel(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None
        img = cv2.cvtColor(cv2.imread(self.path), cv2.COLOR_BGR2GRAY)
        img = sobel.sobel_operator(img) 
        Image.fromarray(img).save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")   
        self.flag = True        

class Aula5AandScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(460)
        widget.setFixedWidth(830)        
        super(Aula5AandScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_median_and_average.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L")) 

        self.action_S_c_r.triggered.connect(self.gotoaula5a_gamma)        
        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))  

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel) 
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Threshold.triggered.connect(self.gotoaula5a_Threshold)        
        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.action_Average_and_Median_Filter.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Averaging_filter.triggered.connect(self.save_av)
        self.action_Median_filter.triggered.connect(self.save_md)  

        self.pushButton.clicked.connect(self.run_AandM) 

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self) 

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)  

    def gotoaula5a_Threshold(self):
        Threshold = Aula5ThreshholdScreen()
        widget.addWidget(Threshold)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Averaging and Median Filters", "."+os.path.sep+"imagens"+os.path.sep+"median_and_average", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]   

    def save_av(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_4.pixmap())
            self.save_file(image)

    def save_md(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_7.pixmap())
            self.save_file(image)

    def save_file(self, image):
        file = QFileDialog.getSaveFileName(None,"Aula 5 - Averaging and Median Filters", "."+os.path.sep+"Saves", "Images (*.bmp)")
        if(file[0] != ''):
            #image = ImageQt.fromqpixmap(self.label_4.pixmap())
            image.save(file[0])

    def run_AandM(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None  
        img = cv2.imread(self.path, 0)                   
        #img = Image.open(self.path).convert("L")
        #median filter
        arr = np.array(img)
        removed_noise = md.median_filter(arr, 3) 
        cv2.imwrite("tempimg.bmp", removed_noise)
        self.label_7.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        #averaging filter
        img_new = av.averaging_filter(img)
        cv2.imwrite("tempimg.bmp", img_new)
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        self.flag = True     


class Aula5ThreshholdScreen(QMainWindow):
    def __init__(self):
        widget.setFixedHeight(510)
        widget.setFixedWidth(660)
        super(Aula5ThreshholdScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula5a_threshold.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Histogram_Equalization.triggered.connect(self.gotoaula5a_histogram)        
        self.action_Histogram_Equalization.setShortcut(QKeySequence("Ctrl+H")) 

        self.action_Laplacian_Filter.triggered.connect(self.gotoaula5a_laplacian)        
        self.action_Laplacian_Filter.setShortcut(QKeySequence("Ctrl+L")) 

        self.action_Sobel_Filter.triggered.connect(self.gotoaula5a_sobel)        
        self.action_Sobel_Filter.setShortcut(QKeySequence("Ctrl+B")) 

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula5a_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_S_c_r.triggered.connect(self.gotoaula5a_gamma) 
        self.action_S_c_r.setShortcut(QKeySequence("Ctrl+G"))

        self.action_Save.triggered.connect(self.save_file)
        self.action_Save.setShortcut(QKeySequence("Ctrl+S"))

        self.action_Threshold.setShortcut(QKeySequence("Ctrl+T")) 

        self.pushButton.clicked.connect(self.run_threshold) 
        
    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)    

    def gotoaula5a_histogram(self):
        histogram = Aula5HistogramScreen()
        widget.addWidget(histogram)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_laplacian(self):
        laplacian = Aula5LaplacianScreen()
        widget.addWidget(laplacian)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self)

    def gotoaula5a_sobel(self):
        sobel = Aula5SobelScreen()
        widget.addWidget(sobel)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_gamma(self):
        gamma = Aula5GammaScreen()
        widget.addWidget(gamma)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def gotoaula5a_AandM(self):
        AandM = Aula5AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 5 - Threshold", "."+os.path.sep+"imagens"+os.path.sep+"gamma_transformation", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]  

    def save_file(self):
        if(self.flag):
            file = QFileDialog.getSaveFileName(None,"Aula 5 - Threshold", "."+os.path.sep+"Saves", "Images (*.bmp)")
            if(file[0] != ''):
                image = ImageQt.fromqpixmap(self.label_4.pixmap())
                image.save(file[0])

    def run_threshold(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None  
        img = Image.open(self.path).convert('L')
        t = float(self.textEdit.toPlainText())
        result = td.threshold(t, img)
        result.save("tempimg.bmp")
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")    
        self.flag = True   

class Aula9Screen(QMainWindow):
    def __init__(self):
        super(Aula9Screen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula9.ui", self)
        self.movie = QMovie("."+os.path.sep+"icons"+os.path.sep+"waiting_2.gif")
        self.label_2.setMovie(self.movie)
        self.movie.start()

        self.movie2 = QMovie("."+os.path.sep+"icons"+os.path.sep+"message_2.gif")
        self.label_3.setMovie(self.movie2)
        self.movie2.start()

        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Averaging_and_Median_Filters.triggered.connect(self.gotoaula9_AandM)        
        self.action_Averaging_and_Median_Filters.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q"))        

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self)         

    def gotoaula9_AandM(self):
        AandM = Aula9AandScreen()
        widget.addWidget(AandM)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        widget.removeWidget(self) 

class Aula9AandScreen(QMainWindow):
    def __init__(self):
        super(Aula9AandScreen, self).__init__()
        loadUi("."+os.path.sep+"GUI"+os.path.sep+"aula9_median_and_average.ui",self)
        self.flag = False
        self.action_Return_menu.triggered.connect(self.gotomenu)        
        self.action_Return_menu.setShortcut(QKeySequence("Ctrl+R"))

        self.action_Exit.triggered.connect(lambda: sys.exit())
        self.action_Exit.setShortcut(QKeySequence("Ctrl+Q")) 

        self.action_Open.triggered.connect(self.open_file)
        self.action_Open.setShortcut(QKeySequence("Ctrl+O"))

        self.action_Average_and_Median_Filter.setShortcut(QKeySequence("Ctrl+A")) 

        self.action_Averaging_filter.triggered.connect(self.save_av)
        self.action_Median_filter.triggered.connect(self.save_md)  

        self.pushButton.clicked.connect(self.run_AandM) 

    def gotomenu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.removeWidget(self) 

    def open_file(self):
        global numpyimage
        #filename = QtWidgets.QFileDialog.getOpenFileName()[0] 
        filename= QFileDialog.getOpenFileName(None,"Aula 9 - Averaging and Median Filters", "."+os.path.sep+"imagens"+os.path.sep+"median_and_average", "Images ( *.bmp , *.png , *.jpg , *.jpeg , *.tif)")
        if(filename[0] != ''):
            self.img = Image.open(filename[0])
            numpyimage = np.asarray(self.img)
            self.label.setPixmap(QPixmap(filename[0]))
            self.path = filename[0]   

    def save_av(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_4.pixmap())
            self.save_file(image)

    def save_md(self):
        if(self.flag):
            image = ImageQt.fromqpixmap(self.label_7.pixmap())
            self.save_file(image)

    def save_file(self, image):
        file = QFileDialog.getSaveFileName(None,"Aula 9 - Averaging and Median Filters", "."+os.path.sep+"Saves", "Images (*.bmp)")
        if(file[0] != ''):
            #image = ImageQt.fromqpixmap(self.label_4.pixmap())
            image.save(file[0])

    def run_AandM(self):
        if(np.all(numpyimage == 0)):
            self.flag = False
            return None  
        img = cv2.imread(self.path, 0)                   
        #img = Image.open(self.path).convert("L")
        #median filter
        arr = np.array(img)
        removed_noise = md.median_filter(arr, 3) 
        cv2.imwrite("tempimg.bmp", removed_noise)
        self.label_7.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        #averaging filter
        img_new = av.averaging_filter(img)
        cv2.imwrite("tempimg.bmp", img_new)
        self.label_4.setPixmap(QPixmap("tempimg.bmp"))
        pdi.delete_image("tempimg.bmp")
        self.flag = True 

#main
app = QApplication(sys.argv)
menu = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(menu)
# widget.setFixedHeight(680)
# widget.setFixedWidth(1350)
widget.setFixedHeight(300)
widget.setFixedWidth(600)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
