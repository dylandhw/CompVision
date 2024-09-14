'''
steps to read & display an image using openCV
1. read an image using imread() function.
2. create a GUI window and display image using imshow() function.
3. use function waitkey(0) to hold the image window on the screen by the specified 
number of seconds, o means till the user closes it, it will hold GUI window on the 
screen.
4. delete image window from the memory after displaying using destroyAllWindows() 
function.

for flag, 0 reads it in grayscale
'''


import cv2

minion = "C:\\Users\\dylan\\f1Tenth\\f1tenth\\open_cv_practice\\images\\minion.jpg"


image = cv2.imread(minion, 0)
image2 = cv2.imread(minion, cv2.IMREAD_COLOR)

cv2.imshow("window name", image)
cv2.imshow("window name 2", image2)


cv2.waitKey(0)


cv2.destroyAllWindows()
