import cv2
import numpy as np

square = np.ones((300,300), np.uint8)
cv2.rectangle(square,(50,50), (250,250), 255, -1)
cv2.imshow("square", square)
cv2.waitKey(0)


ellipse = np.ones((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("ellipse", ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

And = cv2.bitwise_and(square, ellipse)
cv2.imshow("AND", And)
cv2.waitKey(0)

Or = cv2.bitwise_or(square, ellipse)
cv2.imshow("or", Or)
cv2.waitKey(0)

Xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("Xor", Xor)
cv2.waitKey(0)

bitwise_not = cv2.bitwise_not(square)
cv2.imshow("bitwise not", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()