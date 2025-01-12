import numpy as np
from PIL import Image
import math

# Define image dimensions
width, height = 800, 800

# Create an empty array for the image
pattern = np.zeros((height, width, 3), dtype=np.uint8)

# Generate pattern using sine waves
for x in range(width):
    for y in range(height):
        # Create wave patterns for RGB channels
        r = int(127.5 * (1 + math.sin(2 * math.pi * x / 200 + 2 * math.pi * y / 300)))
        g = int(127.5 * (1 + math.sin(2 * math.pi * y / 250 + 2 * math.pi * x / 400)))
        b = int(127.5 * (1 + math.sin(2 * math.pi * (x + y) / 350)))
        pattern[y, x] = (r, g, b)

# Convert the array into an image
image = Image.fromarray(pattern)

# Save and show the image
image.save("complex_pattern.png")
print("Complex pattern image saved as 'complex_pattern.png'")
