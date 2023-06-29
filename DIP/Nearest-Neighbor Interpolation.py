# Image interpolation Nearest-Neighbor Interpolation


import cv2
import numpy as np

def nearest_neighbor_interpolation(image, scale_factor):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new dimensions based on the scale factor
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Create an empty image with the new dimensions
    interpolated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Perform nearest-neighbor interpolation
    for i in range(new_height):
        for j in range(new_width):
            # Calculate the corresponding position in the original image
            x = int(j / scale_factor)
            y = int(i / scale_factor)

            # Assign the value of the nearest pixel to the corresponding position in the interpolated image
            interpolated_image[i, j] = image[y, x]

    return interpolated_image

# Load the original image
original_image = cv2.imread("images1.jpg")

# Set the scale factor for interpolation
scale_factor = 2

# Perform nearest-neighbor interpolation
interpolated_image = nearest_neighbor_interpolation(original_image, scale_factor)

# Display the original and interpolated images
cv2.imshow("Original Image", original_image)
cv2.imshow("Interpolated Image (Nearest-Neighbor)", interpolated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
