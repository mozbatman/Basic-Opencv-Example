# Translation Matrix

# T = [1 0 Tx]
#     [0 1 Ty]

#     Tx = x ekseninde kaydırılacak konumu
#     Ty = y ekseninde kaydırılacak konumu

#     cv2.warpAffine

import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

height, width = img.shape[:2]

quarter_width, quarter_height = height/4, width / 4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

trans = cv2.warpAffine(img, T, (width, height))


cv2.imshow("orginal", img)
cv2.imshow("trans", trans)
cv2.waitKey()
cv2.destroyAllWindows()
