import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')
print(image.shape)

B, G, R = image[10, 50]
print(B, G, R)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray_img.shape)
print(gray_img[10, 50])
print(gray_img[0, 0])


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
B, G, R = hsv_image[10, 50]
print(B, G, R)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey(1500)
cv2.destroyAllWindows()


# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

print(B.shape)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(1500)
cv2.destroyAllWindows()

# Let's re-make the original image,
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged)

cv2.waitKey(1500)
cv2.destroyAllWindows()

zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(1500)
cv2.destroyAllWindows()

print(image.shape[:2])