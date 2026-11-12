import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('geometric_shapes_small.pgm')
img_shifted = plt.imread('geometric_shapes_small_shifted.pgm')
t = 50.0 # Float-Variable um Integer-Overflow zu vermeiden

def detect_and_describe(img):
    corner_img = np.zeros(img.shape)
    descriptor_img = np.zeros(img.shape)

    for row in range(3, img.shape[0]-3):
        for col in range(3, img.shape[1]-3):
            iscorner = False

            p = img[row, col]
            p1 = img[row - 3, col]
            p9 = img[row + 3, col]

            if (p - t < p1 < p + t) and (p - t < p9 < p + t):
                continue

            p2 = img[row - 3, col + 1]
            p3 = img[row - 2, col + 2]
            p4 = img[row - 1, col + 3]
            p5 = img[row, col + 3]
            p6 = img[row + 1, col + 3]
            p7 = img[row + 2, col + 2]
            p8 = img[row + 3, col + 1]
            p10 = img[row + 3, col - 1]
            p11 = img[row + 2, col - 2]
            p12 = img[row + 1, col - 3]
            p13 = img[row, col - 3]
            p14 = img[row - 1, col - 3]
            p15 = img[row - 2, col - 2]
            p16 = img[row - 3, col - 1]
            i = 0
            if p1 > p + t or p1 < p - t:
                i = i + 1
            if p9 > p + t or p9 < p - t:
                i = i + 1
            if p5 > p + t or p5 < p - t:
                i = i + 1
            if p13 > p + t or p13 < p - t:
                i = i + 1

            if i >= 3:
                iscorner = True

            if iscorner:
                corner_img[row, col] = 255

                descriptor = 0
                if p1 > p9:
                    descriptor += 128
                if p2 > p10:
                    descriptor += 64
                if p3 > p11:
                    descriptor += 32
                if p4 > p12:
                    descriptor += 16
                if p5 > p13:
                    descriptor += 8
                if p6 > p14:
                    descriptor += 4
                if p7 > p15:
                    descriptor += 2
                if p8 > p16:
                    descriptor += 1

                descriptor_img[row, col] = descriptor

    return corner_img, descriptor_img

print("Descriptor example")
print("11111000")
corner_img, descriptor_img = detect_and_describe(img)
corner_img_shifted, descriptor_img_shifted = detect_and_describe(img_shifted)

base_corner_descriptor = descriptor_img[34, 32]
for row in range(3, img_shifted.shape[0]-3):
        for col in range(3, img_shifted.shape[1]-3):
            if img_shifted[row,col] == 255:
                shiftet_corner_descriptor = descriptor_img_shifted[row, col]



plt.subplot(231)
plt.imshow(img, cmap='gray', interpolation='none')

plt.subplot(232)
plt.imshow(corner_img, cmap='gray', interpolation='none')

plt.subplot(233)
plt.imshow(descriptor_img, cmap='gray', interpolation='none')

plt.subplot(234)
plt.imshow(img_shifted, cmap='gray', interpolation='none')

plt.subplot(235)
plt.imshow(corner_img_shifted, cmap='gray', interpolation='none')

plt.subplot(236)
plt.imshow(descriptor_img_shifted, cmap='gray', interpolation='none')

plt.show()
