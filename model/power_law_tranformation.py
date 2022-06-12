import numpy as np
#import os
#import cv2

def power_law_tranformation(img,c,gamma):
    gamma_corrected = np.array((c*((img/255)**gamma)), dtype = 'uint8')
    return gamma_corrected

"""
path = "."+os.path.sep+"imagens"+os.path.sep+"lena.bmp"

img = cv2.imread(path)

result = power_law_tranformation(img,1,1.5) #(c between 0 and 255) and (gamma>1 => darker and gamma<1 => lighter)

cv2.imshow("result", result)
cv2.waitKey(0)

"""