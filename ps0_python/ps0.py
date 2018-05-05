import numpy as np
import cv2
import copy


def showimageblocking(images):
    thelist = enumerate(images)
    for (index,element) in thelist:
        name = str(index)
        cv2.imshow(name,element)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Load color images
img1 = cv2.imread('input/jelly_beans.tiff', cv2.IMREAD_COLOR)
img2 = cv2.imread('input/peppers.tiff', cv2.IMREAD_COLOR)

### 1a
# Save the images to output
cv2.imwrite('output/ps0-1-a-1.png', img1)
cv2.imwrite('output/ps0-1-a-2.png', img2)

### 2a
# Swap red and blue pixels
b, g, r = cv2.split(img1)
img1_rb_swapp = cv2.merge((r, g, b))
cv2.imwrite('output/ps0-2-a-1.png', img1_rb_swapp)

### 2b
# Leave only the green pixels
img1_g = copy.copy(img1)
img1_g[:,:,0] = 0
img1_g[:,:,2] = 0
cv2.imwrite('output/ps0-2-b-1.png', img1_g)

### 2c
# Leave only the red pixels
img1_r = copy.copy(img1)
img1_r[:,:,0] = 0
img1_r[:,:,1] = 0
cv2.imwrite('output/ps0-2-c-1.png', img1_r)
