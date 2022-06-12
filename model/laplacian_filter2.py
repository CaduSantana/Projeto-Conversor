import cv2
import numpy as np
import os


class Laplacian:
    def __init__(self,image):
        self.img = image
        self.height = image.shape[0]
        self.width = image.shape[1]

    def convolution(self,laplace):
        #Image Peripheral Fill 0
        padding = np.zeros((self.height+2, self.width+2), np.uint8)
        padding[1:-1, 1:-1] = self.img
        result_image = np.zeros((self.height, self.width), np.uint8)
        for i in range(0, self.height):  # The 5*5 matrix is ​​operated 3 times from left to right and 3 times from top to bottom
            for j in range(0, self.width):
                window = padding[i:i+3, j:j+3]
                result_image[i, j] = np.abs(np.sum(laplace*window)) #Matrix inner product
        return result_image

    def laplace_a(self):
        laplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]) #positive (a)
        result_image = self.convolution(laplace)
        return  result_image

    def laplace_b(self):
        laplace = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) #includes the diagonal neighbors (b)
        result_image = self.convolution(laplace)
        return  result_image

    def laplace_c(self):
        laplace = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]) # negative (c)
        result_image = self.convolution(laplace)
        return  result_image

    def laplace_d(self):
        laplace = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]) #(d)
        result_image = self.convolution(laplace)
        return  result_image

################################################################################################
"""
path = "."+os.path.sep+"imagens"+os.path.sep+"lena.bmp"

img1 = cv2.imread(path,0)#, 0)
teste = Laplacian(img1)
#teste.laplace_a()
#teste.laplace_b()
#teste.laplace_c()
#teste.laplace_d()
"""
###########################################################################################
"""
import cv2
import numpy as np
import os


path = "."+os.path.sep+"imagens"+os.path.sep+"lena.bmp"
img1 = cv2.imread(path,0)#, 0)
high = img1.shape[0]
wide = img1.shape[1]
#Laplace operator
#laplace = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) #includes the diagonal neighbors (b)
#laplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]) #positive (a)
#laplace = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]) # negative (c)
laplace = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]) #(d)
#Image Peripheral Fill 0
padding = np.zeros((high+2, wide+2), np.uint8)
padding[1:-1, 1:-1] = img1
cv2.imshow("image", padding)
#Create result image
result_image = np.zeros((high, wide), np.uint8)
# Convolution operation
for i in range(0, high):  # The 5*5 matrix is ​​operated 3 times from left to right and 3 times from top to bottom
    for j in range(0, wide):
        window = padding[i:i+3, j:j+3]
        result_image[i, j] = np.abs(np.sum(laplace*window)) #Matrix inner product
cv2.imshow("result", result_image)
cv2.waitKey(0)
"""
