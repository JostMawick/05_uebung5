import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('geometric_shapes_small.pgm')
corner_img = np.zeros(img.shape)

t = 100.0 # Float-Variable um Integer-Overflow zu vermeiden

for row in range(3, img.shape[0]-3):
    for col in range(3, img.shape[1]-3):
        iscorner = False
        
        # TODO: Add corner checks here
        p = img[row, col]
        p1 = img[row - 3, col]
        p9 = img[row + 3, col]

        if (p - t < p1 < p + t) and (p - t < p9 < p + t):
            continue

        p5 = img[row, col + 3]
        p13 = img[row, col - 3]
        i=0
        if p1 > p + t or p1 < p - t:
            i=i+1
        if p9 > p + t or p9 < p - t:
            i=i+1
        if p5 > p + t or p5 < p - t:
            i=i+1
        if p13 > p + t or p13 < p - t:
            i=i+1  

        if i >= 3:
            iscorner = True

        if iscorner:
            corner_img[row,col] = 255

plt.subplot(121)
plt.imshow(img, cmap='gray', interpolation='none')
plt.subplot(122)
plt.imshow(corner_img, cmap='gray', interpolation='none')
plt.show()
