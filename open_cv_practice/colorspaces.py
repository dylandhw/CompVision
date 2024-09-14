'''
color spaces are a way to represent the color channels present in the image that gives
the image that particular hue. 

some popular color spaces:
RGB
CMYK
HSV
'''
import cv2
RGB = "C:\\Users\dylan\\f1Tenth\\f1tenth\\open_cv_practice\\images\\RGB.png"

image = cv2.imread(RGB)
B, G, R = cv2.split(image) # split will return an array with the three channels 

cv2.imshow("original", image)

cv2.imshow("blue", B) 
cv2.imshow("Green", G) 
cv2.imshow("red", R) 

cv2.waitKey(0) 
  
cv2.destroyAllWindows() 

# when viewing the opened windows, imagine it is as if you dragged a stained glass shard
# over the image