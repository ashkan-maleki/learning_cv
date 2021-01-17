import cv2
import numpy as np


input = cv2.imread("./images/input.jpg")
cv2.imshow('Orginal', input)
cv2.waitKey(1000)

gray_image = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()


img = cv2.imread('./images/input.jpg',0)

cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()

