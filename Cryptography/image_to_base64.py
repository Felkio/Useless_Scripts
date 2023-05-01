import base64

def image_to_base64(image_path, output_path):
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read())
    with open(output_path, 'wb') as output_file:
        output_file.write(encoded_image)

# Convert an image to Base64
image_to_base64('garten.jpg', 'output_base64.txt')