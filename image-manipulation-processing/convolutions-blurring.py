import cv2
import numpy as np


img = cv2.imread("../images/lena.png")
cv2.imshow("org", img)
cv2.waitKey(0)


kernel_3x3 = np.ones((3, 3), np.float32) / 9 

blurred = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow("blur", blurred)
cv2.waitKey(0)

kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(img, -1, kernel_7x7)
cv2.imshow("blur2", blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()

# ORDER BLUR FUNC

blur = cv2.blur(img,(3,3))
cv2.imshow("blur", blur)
cv2.waitKey(0)

gaussian = cv2.GaussianBlur(img,(7,7), 0)
cv2.imshow("gausse", gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img,5)
cv2.imshow("median", median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()


dst = cv2.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 71)
cv2.imshow("dst", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()