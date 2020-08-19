#           [-1 -1 -1]
# Kernel =  [-1  9 -1]
#           [-1 -1 -1]
#        

import cv2
import numpy as np

image = cv2.imread("../images/lena.png")
cv2.imshow("orn", image)


kernel = np.array([[-1, -1, -1],
                    [-1, 9, -1], 
                    [-1, -1, -1]])    


sharpened = cv2.filter2D(image, -1, kernel)

cv2.imshow("sharpening", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()