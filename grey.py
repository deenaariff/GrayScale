# Deen Aariff

from scipy import misc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import sys as sys


image = misc.imread(sys.argv[1])

# the tuple shape (row, columns, <rgb vector>)
print image.shape

# Intialize a new array of zeroes with the same shape
grey = np.zeros((image.shape[0],image.shape[1]));
grey2 = np.zeros((image.shape[0],image.shape[1]));

# 'Human' Average - adapted for human eyes
def average1(pixel):
    return (0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])/3

# Raw Average 
def average2(pixel):
    return np.average(pixel);

# Map averages of pixels to the grey image
for r in range(len(image)): 
    for c in range(len(image[r])): 
        # Use human average
        grey[r][c] = average1(image[r][c]);

plt.imshow(grey, cmap = matplotlib.cm.Greys_r) 
plt.show()
