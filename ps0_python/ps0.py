import numpy as np
import cv2

# Load color images
img1 = cv2.imread('input/jelly_beans.tiff',cv2.IMREAD_COLOR)
img2 = cv2.imread('input/peppers.tiff',cv2.IMREAD_COLOR)

# Display the color images
cv2.imshow('jelly beans',img1)
cv2.imshow('peppers',img2)

# Save the images to output
cv2.imwrite('output/ps0-1-a-1.png',img1)
cv2.imwrite('output/ps0-1-a-2.png',img2)

# Wait to exit
cv2.waitKey(0)
cv2.destroyAllWindows()