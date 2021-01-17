import cv2
import numpy as np

input = cv2.imread('./images/input.jpg')
cv2.imshow('hello world', input)
cv2.waitKey(500)
cv2.destroyAllWindows()

print(input.shape)

print(f'Height of image: {input.shape[0]}px')
print(f'Width of image: {input.shape[1]}px')

cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)

