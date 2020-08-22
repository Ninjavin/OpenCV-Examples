from cv2 import cv2

img = cv2.imread("reddit-alien-png-3.png")
img2 = cv2.imread("1772746.jpg")

# print(img.shape)    # Returns a tuple of number of rows, columns, channels
# print(img.size)     # Returns total number of pixels
# print(img.dtype)    # Returns Image Datatype

# b, g, r = cv2.split(img)
# img = cv2.merge((b, g, r))

# eye = img[0:60, 150:210]
# img[273:333, 100:160] = eye

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .2, img2, .8, 0)

cv2.imshow('Reddit', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()