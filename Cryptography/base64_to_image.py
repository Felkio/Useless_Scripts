import base64

def base64_to_image(base64_path, output_path):
    with open(base64_path, 'rb') as base64_file:
        decoded_image = base64.b64decode(base64_file.read())
    with open(output_path, 'wb') as output_file:
        output_file.write(decoded_image)

# Convert Base64 back to an image
base64_to_image('output_base64.txt', 'decoded_image.jpg')
