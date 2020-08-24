import cv2
import numpy as np

image = cv2.imread('../images/bunchofshapes.jpg')
cv2.imshow('0 - Original Image', image)
cv2.waitKey(0)

blank_image = np.zeros((image.shape[0], image.shape[1], 3))
orginal_image = image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0)


contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print ("Number of contours found = ", len(contours))


cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)
cv2.waitKey(0)

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', image)
cv2.waitKey(0)


cv2.destroyAllWindows()

####################################################################

def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas


orginal_image = image
print ("Contor Areas before sorting") 
print (get_contour_areas(contours))

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print ("Contor Areas after sorting") 
print (get_contour_areas(sorted_contours))

for c in sorted_contours:
    cv2.drawContours(orginal_image, [c], -1, (255,0,0), 3)
    cv2.waitKey(0)
    cv2.imshow('Contours by area', orginal_image)

cv2.waitKey(0)
cv2.destroyAllWindows()







