import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('geometric_shapes_small.pgm')
corner_img = np.zeros(img.shape)

t = 10.0 # Float-Variable um Integer-Overflow zu vermeiden

for row in range(3, img.shape[0]-3):
    for col in range(3, img.shape[1]-3):
        iscorner = False
        
        # TODO: Add corner checks here
        p = img[row,col]
        
        if iscorner:
            corner_img[row,col] = 255

plt.subplot(121)
plt.imshow(img, cmap='gray', interpolation='none')
plt.subplot(122)
plt.imshow(corner_img, cmap='gray', interpolation='none')
plt.show()

