import numpy as np
from matplotlib import pyplot as plt
import cv2
import os

# The function takes two dimension inputs for the filter image;
def highLaplacian(M, N):
    # Initializing the filter with ones; since the filter is a complex function,
    # it has two channels, representing the real and imaginary parts;
    # the data type is float32, since the pixels will take floating point values:
    filter = np.zeros((M, N, 2), dtype=np.float32)
    
    # Scanning through each pixel and calculating the negative of the sum of the
    # squares of the pixels, and assigning the value to the corresponding pixel
    # in the filter:
    for i in range(M):
        for j in range(N):
            filter[i][j] = -((i-M/2)**2 + (j-N/2)**2)

    return filter


path = "."+os.path.sep+"imagens"+os.path.sep+"desenho_amy_paint.bmp"

img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

m = img.shape[0]
n = img.shape[1]

ft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
ft_shifted = dft_shift = np.fft.fftshift(ft)

filter = highLaplacian(m, n)
filterMag = 20 * np.log(cv2.magnitude(filter[:, :, 0], filter[:, :, 1]))

applied = ft_shifted * filter
fshift_mask_mag = 20 * np.log(cv2.magnitude(applied[:, :, 0], applied[:, :, 1]))
f_ishift = np.fft.ifftshift(applied)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

imgplot = plt.imshow(img_back, cmap="gray")
plt.show()
cv2.imwrite("lap_output.png", filterMag)