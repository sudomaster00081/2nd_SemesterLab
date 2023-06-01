#Read Two RGB images and Perform Subtraction Operation on Them

import cv2
import numpy as np

# Load the images
image1 = cv2.imread('images1.jpg')
image2 = cv2.imread('images3.jpg')

# Check if the images have the same size
if image1.shape == image2.shape:
    # Perform the addition of the images
    added_image = cv2.subtract(image1, image2)
    # Display the result
    cv2.imshow('Added Image', added_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Images have different sizes. Addition cannot be performed.")
