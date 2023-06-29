# Image interpolation Bicubic interpolation

import cv2
import numpy as np

def bicubic_interpolation(image, scale_factor):
    # Get the original image dimensions
    height, width = image.shape[:2]

    # Calculate the new dimensions based on the scale factor
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Create an empty image with the new dimensions
    interpolated_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Perform bicubic interpolation
    for i in range(new_height):
        for j in range(new_width):
            # Calculate the corresponding position in the original image
            x = j / scale_factor
            y = i / scale_factor

            # Get the surrounding 16 pixels
            x1 = int(x) - 1
            y1 = int(y) - 1

            # Calculate the fractional part
            dx = x - int(x)
            dy = y - int(y)

            # Perform bicubic interpolation
            interpolated_value = 0
            for m in range(4):
                for n in range(4):
                    x_index = min(max(x1 + n, 0), width - 1)
                    y_index = min(max(y1 + m, 0), height - 1)
                    weight = bicubic_kernel(dx - n + 1) * bicubic_kernel(dy - m + 1)
                    interpolated_value += weight * image[y_index, x_index]

            interpolated_image[i, j] = np.clip(interpolated_value, 0, 255)

    # Resize the interpolated image to the target dimensions
    interpolated_image = cv2.resize(interpolated_image, (width, height))

    return interpolated_image

def bicubic_kernel(x):
    # Bicubic interpolation kernel function
    a = -0.5
    abs_x = abs(x)
    if abs_x < 1:
        return (a + 2) * (abs_x ** 3) - (a + 3) * (abs_x ** 2) + 1
    elif abs_x < 2:
        return a * (abs_x ** 3) - 5 * a * (abs_x ** 2) + 8 * a * abs_x - 4 * a
    else:
        return 0

# Load the original image
original_image = cv2.imread("images1.jpg")

# Set the scale factor for interpolation
scale_factor = 3

# Perform bicubic interpolation
interpolated_image = bicubic_interpolation(original_image, scale_factor)

# Display the original and interpolated images
cv2.imshow("Original Image", original_image)
cv2.imshow("Interpolated Image (Bicubic)", interpolated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
