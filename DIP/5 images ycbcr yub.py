#Read an RGB image Convert it into Ycbcr and yuv images and show them by channel

import cv2
import numpy as np

# Load the RGB image
image = cv2.imread('images3.jpg')

# Convert RGB image to YCbCr
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Convert RGB image to YUV
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# Split YCbCr channels
y_channel, cb_channel, cr_channel = cv2.split(ycbcr_image)

# Split YUV channels
y_channel_uv, u_channel, v_channel = cv2.split(yuv_image)

# Display the channels
cv2.imshow('Y Channel (YCbCr)', y_channel)
cv2.imshow('Cb Channel (YCbCr)', cb_channel)
cv2.imshow('Cr Channel (YCbCr)', cr_channel)

cv2.imshow('Y Channel (YUV)', y_channel_uv)
cv2.imshow('U Channel (YUV)', u_channel)
cv2.imshow('V Channel (YUV)', v_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
