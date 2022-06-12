from PyQt5 import uic, QtWidgets, QtGui
from PIL import ImageQt
from PIL import Image
import numpy as np
import os


def delete_image(img):
    os.remove(os.path.join(os.getcwd(), img))


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def QPixmapToArray(pixmap):
    # Get the size of the current pixmap
    size = pixmap.size()
    h = size.width()
    w = size.height()

    # Get the QImage Item and convert it to a byte string
    qimg = pixmap.toImage()
    byte_str = qimg.bits().tobytes()

    # Using the np.frombuffer function to convert the byte string into an np array
    img = np.frombuffer(byte_str, dtype=np.uint8).reshape((w, h, 4))

    return img


def build_image(data, height, width):
    img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
    for x in range(width):
        for y in range(height):
            img.setPixel(x, y, QtGui.QColor(*data[x][y]).rgb())

    pix = QtGui.QPixmap.fromImage(img)
    return pix


def negative(img):
    # Read pixels and apply negative transformation
    for i in range(0, img.size[0]-1):
        for j in range(0, img.size[1]-1):
            # Get pixel value at (x,y) position of the image
            pixelColorVals = img.getpixel((i, j))
            # Invert color
            redPixel = 255 - pixelColorVals[0]  # Negate red pixel
            greenPixel = 255 - pixelColorVals[1]  # Negate green pixel
            bluePixel = 255 - pixelColorVals[2]  # Negate blue pixel
            # Modify the image with the inverted pixel values
            img.putpixel((i, j), (redPixel, greenPixel, bluePixel))
    return img        

def inverse(img):
    im = np.array(img)
    inv_im = 255 - im
    return inv_im
    
    