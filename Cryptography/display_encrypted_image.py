import numpy as np
import matplotlib.pyplot as plt

encrypted_image_path = 'encrypte_immagine.jpg'

with open(encrypted_image_path, 'rb') as f:
    encrypted_data = f.read()

# Convert encrypted data to a NumPy array
encrypted_array = np.frombuffer(encrypted_data, dtype=np.uint8)

# Calculate the dimensions for the reshaped array (width and height should be close to the original image dimensions)
width = int(np.sqrt(len(encrypted_array)))
height = len(encrypted_array) // width

# Reshape the array to create an image
encrypted_image = encrypted_array[:width * height].reshape(height, width)

# Display the encrypted image
plt.imshow(encrypted_image, cmap='gray')
plt.show()