# Rotations Matrix

# T = [cos0 -sin0]
#     [sin0 cos0]

#     cv2.getRotationMatrix2D(rot_center_x, rot_center_y, angel, scale)

import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

height, width = img.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

rotate_image = cv2.warpAffine(img, rotation_matrix, (width, height))

rotate_image2 = cv2.transpose(img)


cv2.imshow("orginal", img)
cv2.imshow("rotate", rotate_image)
cv2.imshow("rotate-method-2", rotate_image2)
cv2.waitKey()
cv2.destroyAllWindows()