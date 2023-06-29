# Image interpolation Bilinear Interpolation

import cv2
import numpy as np

def bilinear_interpolation(image, scale_factor):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new dimensions based on the scale factor
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Create an empty image with the new dimensions
    interpolated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Perform bilinear interpolation
    for i in range(new_height):
        for j in range(new_width):
            # Calculate the corresponding position in the original image
            x = j / scale_factor
            y = i / scale_factor

            # Get the surrounding four pixels
            x1, y1 = int(x), int(y)
            x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

            # Calculate the fractional part
            dx = x - x1
            dy = y - y1

            # Perform bilinear interpolation
            interpolated_image[i, j] = (1 - dx) * (1 - dy) * image[y1, x1] + \
                                       dx * (1 - dy) * image[y1, x2] + \
                                       (1 - dx) * dy * image[y2, x1] + \
                                       dx * dy * image[y2, x2]

    return interpolated_image

# Load the original image
original_image = cv2.imread("images1.jpg")

# Set the scale factor for interpolation
scale_factor = 2

# Perform bilinear interpolation
interpolated_image = bilinear_interpolation(original_image, scale_factor)

# Display the original and interpolated images
cv2.imshow("Original Image", original_image)
cv2.imshow("Interpolated Image (Bilinear)", interpolated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
