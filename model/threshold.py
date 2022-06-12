from PIL import Image
import sys, os
import cv2

def threshold(t, image):
    intensity_array = []
    for w in range(0,image.size[1]):
        for h in range(0,image.size[0]):
            intensity = image.getpixel((h,w))
            if (intensity <= t):
                x = 0
            else:
                x = 255
            intensity_array.append(x)
    image.putdata(intensity_array)
    return image 

"""
path = "."+os.path.sep+"imagens"+os.path.sep+"lena.bmp"
img = Image.open(path).convert('L')
#img = cv2.imread(path, 0)
image = threshold(44, img)
image.show()
"""