import cv2
import numpy as np

image = cv2.imread("../images/lena.png")
height, width = image.shape[:2]

M = np.ones(image.shape, dtype="uint8") * 75 

added = cv2.add(image, M)
substracted = cv2.subtract(image, M)

cv2.imshow("orginal", image)
cv2.waitKey(0)
cv2.imshow("added", added)
cv2.waitKey(0)
cv2.imshow("sub", substracted)
cv2.waitKey(0)
cv2.destroyAllWindows()