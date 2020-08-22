from cv2 import cv2
from matplotlib import pyplot as plt

img = cv2.imread("sudoku-original.jpg", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

titles = ['image', 'mask']
images = [img, mask]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()