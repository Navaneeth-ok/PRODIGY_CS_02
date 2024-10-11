import cv2
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Read the input image
    image = cv2.imread(input_path)

    if image is None:
        print("Error: Could not read the image.")
        return

    # Get the pixel data
    height, width, channels = image.shape
    encrypted_data = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            # XOR each color channel with the key
            for c in range(channels):
                encrypted_data[i][j][c] = image[i][j][c] ^ key[c]

    # Save the encrypted image
    cv2.imwrite(output_path, encrypted_data)
    print(f"Encrypted image saved as: {output_path}")
    print("Encryption successful!")  

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # Reuse the encrypt function
    print("Decryption successful!") 

input_image = "Mohanlal_Viswanathan_BNC.jpg"  # Path to the input image
encrypted_image_path = "encrypted_image.png"  # Path for the encrypted image
decrypted_image_path = "decrypted_image.png"  # Path for the decrypted image

# Example key for XOR operation (length should match the number of channels)
key = [123, 234, 145]  

# Encrypt the image
encrypt_image(input_image, encrypted_image_path, key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, key)
