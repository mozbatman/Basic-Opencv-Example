import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

small_img = cv2.pyrDown(img)
large_img = cv2.pyrUp(img)

cv2.imshow("orginal", img)
cv2.imshow("small", small_img)
cv2.imshow("large", large_img)

cv2.waitKey()
cv2.destroyAllWindows()