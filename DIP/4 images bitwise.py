#Read Two RGB images and Perform Bitwise Operations on Them

import cv2 as cv
import numpy as np

img1 = cv.imread(r"images1.jpg")
img2 = cv.imread(r"images3.jpg")

res_and = cv.bitwise_and(img1, img2)
res_or = cv.bitwise_or(img1, img2)
res_xor = cv.bitwise_xor(img1, img2)
res_not = cv.bitwise_not(img1, img2)

cv.imshow("AND", res_and)
cv.imshow("OR", res_or)
cv.imshow("XOR", res_xor)
cv.imshow("not", res_not)

cv.waitKey(0)