import numpy as np
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def xor_encrypt_file(input_file_path, output_file_path, key):
    # Get the file extension
    file_extension = os.path.splitext(input_file_path)[1]

    # Check if the input file is an image
    if file_extension.lower() in ['.png', '.jpg', '.jpeg', '.bmp']:
        # Open the image and get the data as a NumPy array
        image = Image.open(input_file_path)
        input_data = np.array(image, dtype=np.uint8)
    else:
        # Read the input file as bytes
        with open(input_file_path, 'rb') as file:
            input_data = np.fromfile(file, dtype=np.uint8)

    # Create the key array
    key_array = np.frombuffer(key.encode(), dtype=np.uint8)

    # Create the key matrix with the appropriate shape
    if input_data.ndim == 3:  # Check if it's a color image
        key_matrix_reshaped = np.tile(key_array, (input_data.shape[0], input_data.shape[1], (input_data.shape[2] + len(key_array) - 1) // len(key_array)))[:, :, :input_data.shape[2]]
    else:
        key_matrix_reshaped = np.tile(key_array, (input_data.shape[0], (input_data.shape[1] + len(key_array) - 1) // len(key_array)))[:, :input_data.shape[1]]

    # Encrypt the input data using XOR with the key matrix
    encrypted_data = np.bitwise_xor(input_data, key_matrix_reshaped)

    # Save the encrypted data as an image or a file
    if file_extension.lower() in ['.png', '.jpg', '.jpeg', '.bmp']:
        encrypted_image = Image.fromarray(encrypted_data)
        encrypted_image.save(output_file_path)
    else:
        with open(output_file_path, 'wb') as file:
            encrypted_data.tofile(file)

def browse_input_file():
    # Open the file dialog and set the input file path
    input_file_path = filedialog.askopenfilename()
    input_path_var.set(input_file_path)

def browse_output_file():
    # Open the file dialog and set the output file path
    output_file_path = filedialog.asksaveasfilename()
    output_path_var.set(output_file_path)

def generate_key():
    # Generate a random encryption key
    key = os.urandom(16).hex()
    key_var.set(key)

def encrypt_file():
    # Get the input and output file paths and the key
    input_file_path = input_path_var.get()
    output_file_path = output_path_var.get()
    key = key_var.get()

    # Check if all the fields are filled in
    if not input_file_path or not output_file_path or not key:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Encrypt the input file and save the result
    xor_encrypt_file(input_file_path, output_file_path, key)
    messagebox.showinfo("Success", "File encrypted successfully.")

# Create the main window
root = tk.Tk()
root.title("XOR Image Encryption")

input_path_var = tk.StringVar()
output_path_var = tk.StringVar()
key_var = tk.StringVar()

# Create the input file widgets
input_label = tk.Label(root, text="Input file:")
input_label.grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(root, textvariable=input_path_var, width=40)
input_entry.grid(row=0, column=1)
input_browse_button = tk.Button(root, text="Browse...", command=browse_input_file)
input_browse_button.grid(row=0, column=2)

# Create the output file widgets
output_label = tk.Label(root, text="Output file:")
output_label.grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(root, textvariable=output_path_var, width=40)
output_entry.grid(row=1, column=1)
output_browse_button = tk.Button(root, text="Browse...", command=browse_output_file)
output_browse_button.grid(row=1, column=2)

# Create the encryption key widgets
key_label = tk.Label(root, text="Encryption key:")
key_label.grid(row=2, column=0, sticky="e")
key_entry = tk.Entry(root, textvariable=key_var, width=40)
key_entry.grid(row=2, column=1)
key_generate_button = tk.Button(root, text="Generate key", command=generate_key)
key_generate_button.grid(row=2, column=2)

# Create the encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_file, width=10)
encrypt_button.grid(row=3, column=1, pady=10)

# Run the main loop
root.mainloop()
