# Interpolation = enterpolasyon, farklı bir bilgi veri noktası aralığı içinde yeni veri noktaları oluşturma yöntemidir.

# cv2.INTER_AREA - küçültmek veya örneklemek için iyi
# cv2.INTER_NEAREST - en hızlı
# cv2.INTER_LINEAR - yakınlaştırmak veya örneklemek için iyi (default)
# cv2.INTER_CUBIC - daha iyi 
# cv2.INTER_LANCZOS4 - en iyi

# cv2.resize(image, dsize(output image size), x scale, y scale, interpolation)

import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

image_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow('scaling-linear interpolation', image_scaled)
cv2.waitKey()

image_scaled = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('scaling-cubic interpolation', image_scaled)
cv2.waitKey()

image_scaled = cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA)
cv2.imshow('scaling-skewed interpolation', image_scaled)
cv2.waitKey()
cv2.destroyAllWindows()

