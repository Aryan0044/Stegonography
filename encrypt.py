import cv2

image = cv2.imread("mypic.jpg")
message = input("Enter your Message: ")
password = input("Enter encryption Password: ")

with open("password.txt", "w") as p:
    p.write(password)

message += "\0"
msg_bytes = message.encode("utf-8")

if len(msg_bytes) > image.size:
    print("Message lenght limit exceeding")
    exit()

index = 0
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(3):
            if index < len(msg_bytes):
                image[i, j, k] = msg_bytes[index]
                index += 1
            else:
                break
        else:
            continue
        break

cv2.imwrite("encryptedImage.png", image)
print("Encryption Successfull!\nSaved as 'encryptedImage.png'.")
