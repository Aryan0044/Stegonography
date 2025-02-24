# SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY

This project offers a straightforward implementation of **image-based steganography**, allowing users to embed secret messages within an image and later retrieve them using a decryption script. The encryption and decryption processes modify the pixel values of an image to encode message bytes securely.

## Key Features

- Conceal a confidential message within an image through pixel manipulation.
- Protect the hidden message using a password.
- Retrieve the embedded message only when the correct password is provided.
- Lightweight and efficient implementation using Python and OpenCV.
- Ensures data privacy without significantly altering the visual quality of the image.

## Prerequisites

Before running the scripts, ensure you have the necessary dependencies installed:

```sh
pip install opencv-python
```

## How to Use

### 1. Hiding a Secret Message

To embed a secret message within an image, run the encryption script:

```sh
python encrypt.py
```

#### Process:

1. The script prompts for the image file (e.g., `mypic.jpg`).
2. Enter the secret message to be hidden.
3. Provide a password for added security.
4. The encrypted image is generated and saved as `encryptedImage.png`.
5. The password is securely stored in `key.txt`.

### 2. Extracting the Hidden Message

To retrieve the concealed message, execute the decryption script:

```sh
python decrypt.py
```

#### Process:

1. The script reads `encryptedImage.png`.
2. Enter the correct password.
3. If the password matches, the hidden message is displayed.
4. If the password is incorrect, access is denied.

## File Structure

- **encrypt.py** - Script for embedding a secret message into an image.
- **decrypt.py** - Script for extracting the secret message from the image.
- **encryptedImage.png** - The modified image containing the hidden message.
- **password.txt** - Stores the password required for decryption.
- **mypic.jpg** - The original image used for encryption.

## Example Usage

### Encrypting a Message:

```sh
Enter your Message: This is a hidden message.
Enter encryption Password: 12345
Encryption Successful.
Saved as 'encryptedImage.png'.
```

### Decrypting a Message:

```sh
Enter password: 12345
Secret Message is: This is a hidden message.
```

## Important Notes

- The encryption algorithm alters pixel values to store message bytes.
- The length of the hidden message should not exceed the available pixel capacity in the image.
- A NULL (`\0`) byte is used as an end marker to determine the message termination.
- The encryption method ensures minimal distortion to maintain image integrity.
- Recommended for securely transmitting sensitive information without attracting attention.

## License

This project is open-source and released under the MIT License.

## Author

**Aryan Namdev**


