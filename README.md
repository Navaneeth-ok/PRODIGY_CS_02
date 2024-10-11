# Image Encryption and Decryption with XOR
This project demonstrates basic image encryption and decryption using XOR bitwise operations on each pixel channel. The project uses Python and OpenCV to manipulate images.

## Features
- Encryption: The image is encrypted using a key provided by the user. The encryption is performed by applying an XOR operation on each pixel’s color channels.
- Decryption: The encrypted image can be decrypted using the same XOR key. This reverses the encryption since XOR is a symmetric operation.
  
## Requirements
- Python 3.x
- OpenCV library (opencv-python)
- NumPy library (numpy)

## How It Works
- The script reads an image from the specified path.
- It uses a key (a list of numbers) to perform XOR operations on each pixel of the image.
- The encrypted image is saved to a new file.
- The same process is repeated for decryption, using the same key to retrieve the original image.
  
## Example Process
- Input Image: You specify the path to an image file (e.g., Mohanlal_Viswanathan_BNC.jpg).
- Encryption: The image is encrypted using the XOR operation with the given key, and the encrypted image is saved (e.g., encrypted_image.png).
- Decryption: The encrypted image is decrypted using the same key, and the decrypted image is saved (e.g., decrypted_image.png).

## Key Points
- The key is essential for both encryption and decryption. It must match the number of color channels in the image (usually 3 for RGB images).
- If the same key is used for both encryption and decryption, the original image can be recovered exactly.
