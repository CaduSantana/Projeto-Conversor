import numpy as np
import os 
import cv2
import matplotlib.pyplot as plt

class HistogramEqualization:
    def __init__(self,image):
        self.img = image
        self.a = np.zeros((256,),dtype=np.float16)
        self.b = np.zeros((256,),dtype=np.float16)
        self.height = image.shape[0]
        self.width = image.shape[1]
        #self.height, self.width= image.shape

    def original_histogram(self,img):
        for i in range(self.width):
            for j in range(self.height):
                g = img[j,i]
                self.a[g] = self.a[g]+1
        return self.a

    def histogram_equalization(self):
        #performing histogram equalization
        tmp = 1.0/(self.height*self.width)
        self.b = np.zeros((256,),dtype=np.float16)

        for i in range(256):
            for j in range(i+1):
                self.b[i] += self.a[j] * tmp;
            self.b[i] = round(self.b[i] * 255);

        # b now contains the equalized histogram
        self.b=self.b.astype(np.uint8)
        return self.b

    def build_image(self,b):
        #Re-map values from equalized histogram into the image
        for i in range(self.width):
            for j in range(self.height):
                g = self.img[j,i]
                self.img[j,i]= b[g]

        return self.img

    def histogram_equalization_for_plot(self,img):
        eq_hist = np.zeros(256)
        for i in range(self.width):
            for j in range(self.height):
                eq_hist[(img[i,j])] = eq_hist[(img[i,j])] + 1
        return eq_hist

    def plot_unequalized_histogram(self, hist,title,y_label,x_label):
        plt.figure(figsize=(4.9, 4))
        plt.bar(list(range(len(hist))), hist, color='blue') 
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.show()

    def plot_equalized_histogram(self, hist,title,y_label,x_label):
        plt.figure(figsize=(4.9, 4))
        plt.bar(list(range(len(hist))), hist, color='blue') 
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        plt.show()


"""
path = "."+os.path.sep+"imagens"+os.path.sep+"lena_grayscale.bmp"
img = cv2.imread(path,0)

classe = HistogramEqualization(img)
a = classe.original_histogram(img)
print(a)
classe.plot_unequalized_histogram(a,'Unequalized Histogram','Frequency (Number of Pixels)','Intensity (Grey Level)')
hist_eq = classe.histogram_equalization()
build_image = classe.build_image(hist_eq)
hist_eq_4_plot = classe.histogram_equalization_for_plot(build_image)
classe.plot_equalized_histogram(hist_eq_4_plot,'Equalized Histogram','Frequency (Number of Pixels)','Intensity (Grey Level)')
"""

"""

path = "."+os.path.sep+"imagens"+os.path.sep+"lena_grayscale.bmp"
img = cv2.imread(path,0)

#To display image before equalization
cv2.imshow('image',img)
cv2.waitKey(0)


a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

#finding histogram
for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1

print(a)   

plt.figure(figsize=(4.9, 4))
plt.bar(list(range(len(a))), a, color='blue') 
plt.title('Unequalized Histogram')
plt.ylabel('Frequency (Number of Pixels)')
plt.xlabel('Intensity (Grey Level)')
plt.savefig("."+os.path.sep+"imagens"+os.path.sep+"unequalized.png")

#performing histogram equalization
tmp = 1.0/(height*width)
b = np.zeros((256,),dtype=np.float16)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp;
    b[i] = round(b[i] * 255);

# b now contains the equalized histogram
b=b.astype(np.uint8)

print(b)

"""
#plt.figure(figsize=(3, 3))
#plt.bar(list(range(len(b))), b, color='green') 
#plt.title('Cumulative function')
#plt.ylabel('Frequency (Number of Pixels)')
#plt.xlabel('Intensity (Grey Level)')
#plt.show()
"""

#Re-map values from equalized histogram into the image
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]


################################################
eq_hist = np.zeros(256)
for i in range(width):
    for j in range(height):
        eq_hist[(img[i,j])] = eq_hist[(img[i,j])] + 1
        
plt.figure(figsize=(4.9, 4))
plt.bar(list(range(len(eq_hist))), eq_hist, color='blue') 
plt.title('Equalized Histogram')
plt.ylabel('Frequency (Number of Pixels)')
plt.xlabel('Intensity (Grey Level)')
plt.savefig("."+os.path.sep+"imagens"+os.path.sep+"equalized.png")
########################################################
cv2.imshow('image',img)
cv2.imwrite("histogrma_equalizado.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""