import numpy as np
import cv2

#def readRawFile(name, row_size, column_size):
#    imgFile = open(name, 'rb')
#    img = np.fromfile(imgFile, dtype=np.uint8, count=row_size * column_size)
#    img = np.reshape(img, (-1, row_size))
#    imgFile.close()
#    return img

#img = readRawFile("ass-3/moon464x528.raw", 464, 528)
img = cv2.imread('moon.png', cv2.IMREAD_GRAYSCALE)  # Read input image as grayscale.

width = img.shape[0]  # The first index is the height (the names are swapped)
height = img.shape[1]

img_pad = np.pad(img, ((1, 1), (1, 1)), 'edge')

#w = np.array([1, 1.2, 1])
w = -1.2  # I think w in the formula is supposed to be a negative a scalar

t1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

edge_img = np.zeros((width, height))
edge_pad = np.pad(edge_img, ((1, 1), (1, 1)), 'constant')

for i in range(1, width - 1):
    for j in range(1, height - 1):

        #edge_pad[i, j] = abs(np.sum((img_pad[i:i + 3, j:j + 3] * t1) * w))
        # Edge is allowed to be negative.
        edge_pad[i, j] = np.sum(img_pad[i-1:i+2, j-1:j+2] * t1) * w

        #if edge_pad[i, j] < 0:
        #    edge_pad[i, j] = 0

# img tyep is uint8 and edge_pad is float64, the result is float64
out_img = img - edge_pad[1:edge_pad.shape[0] - 1, 1:edge_pad.shape[1] - 1]
out_img = np.clip(out_img, 0, 255).astype(np.uint8)  # Clip range to [0, 255] and cast to uint8

#out_img.astype('int8').tofile("ass-3/moon-1.raw")

cv2.imwrite('out_img.png', out_img)  # Save out_img as PNG image file

# Show the input and the output images for testing
cv2.imshow('img', img)
cv2.imshow('edge_pad', (edge_pad-edge_pad.min())/(edge_pad.max() - edge_pad.min()))
cv2.imshow('out_img', out_img)
cv2.waitKey()
cv2.destroyAllWindows()