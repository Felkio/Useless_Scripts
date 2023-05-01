from PIL import Image
import numpy as np

def xor_encrypt_image(image_path, key):
    image = Image.open(image_path).convert('L')
    image_array = np.array(image, dtype=np.uint8)

    key_array = np.frombuffer(key.encode(), dtype=np.uint8)
    key_matrix = np.tile(key_array, (image_array.shape[0], (image_array.shape[1] + len(key_array) - 1) // len(key_array)))[:, :image_array.shape[1]]

    encrypted_image_array = np.bitwise_xor(image_array, key_matrix)
    encrypted_image = Image.fromarray(encrypted_image_array)

    return encrypted_image

input_image_path = "cattura.png"
output_image_path = "encrypted_xor.png"
key = "my_fixed_key"

encrypted_image = xor_encrypt_image(input_image_path, key)
encrypted_image.save(output_image_path)
encrypted_image.show()
