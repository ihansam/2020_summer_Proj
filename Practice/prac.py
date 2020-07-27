import cv2
img = cv2.imread('pracpic.jpg', cv2.IMREAD_UNCHANGED)
""" 
cv2.imshow("Resized image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print('Resized Dimensions : ', img.shape)

dim = (48, 27)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
