import cv2

image = cv2.imread("encryptedImage.png")

try:
    with open("password.txt", "r") as p:
        correct_password = p.read().strip()
except FileNotFoundError:
    print("Password Missing!")
    exit()

password = input("Enter password: ")
if password != correct_password:
    print("Access denied!")
    exit()

msg_bytes = bytearray()
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(3):
            byte = image[i, j, k]
            if byte == 0:
                break
            msg_bytes.append(byte)
        else:
            continue
        break
    else:
        continue
    break

msg = msg_bytes.decode("utf-8")
print("Secret Message is: ", msg)


