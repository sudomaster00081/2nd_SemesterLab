#Read an RGB image and Display its Channels


#>>> pip install pillow

from PIL import Image

# Load the image
image = Image.open('images1.png')

# Convert the image to RGB format
image = image.convert('RGB')

# Split the image into its channels
r, g, b = image.split()

# Display each channel
r.show(title='Red channel')
g.show(title='Green channel')
b.show(title='Blue channel')

