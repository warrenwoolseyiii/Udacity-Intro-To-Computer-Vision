import numpy as np
import cv2
import copy


def showimageblocking(images):
    thelist = enumerate(images)
    for (index, element) in thelist:
        name = str(index)
        cv2.imshow(name, element)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def validatesize(size, threshold):
    rtn = False
    if size > threshold:
        rtn = True
    return rtn


# Load color images
img1 = cv2.imread('input/jelly_beans.tiff', cv2.IMREAD_COLOR)
img2 = cv2.imread('input/peppers.tiff', cv2.IMREAD_COLOR)

# 1a
# Save the images to output
cv2.imwrite('output/ps0-1-a-1.png', img1)
cv2.imwrite('output/ps0-1-a-2.png', img2)

# 2a
# Swap red and blue pixels
b, g, r = cv2.split(img1)
img1_rb_swapp = cv2.merge((r, g, b))
cv2.imwrite('output/ps0-2-a-1.png', img1_rb_swapp)

# 2b
# Leave only the green pixels
img1_g = copy.copy(img1)
img1_g[:, :, 0] = 0
img1_g[:, :, 2] = 0
cv2.imwrite('output/ps0-2-b-1.png', img1_g)

# 2c
# Leave only the red pixels
img1_r = copy.copy(img1)
img1_r[:, :, 0] = 0
img1_r[:, :, 1] = 0
cv2.imwrite('output/ps0-2-c-1.png', img1_r)

# 3a
# Leave only the red pixels for image 2
img2_r = copy.copy(img2)
img2_r[:, :, 0] = 0
img2_r[:, :, 1] = 0

# Get the image shape and validate its large enough
row1, col1, chan1 = img1_r.shape
row2, col2, chan2 = img2_r.shape
if not validatesize(row1, 100) or not validatesize(col1, 100):
    print 'image 1 is not large enough: ', row1, ' ', col1
elif not validatesize(row2, 100) or not validatesize(col2, 100):
    print 'image 2 is not large enough: ', row2, ' ', col2
else:
    # Get the cetner 100 x 100 square of img1_r
    center_row1 = row1/2
    center_col1 = col1/2
    center1 = img1_r[center_row1-50:center_row1 +
                     50, center_col1-50:center_col1+50]
    # Transplant the center square into img2_r
    center_row2 = row2/2
    center_col2 = col2/2
    transplant2_r = copy.copy(img2_r)
    transplant2_r[center_row2-50:center_row2+50,
                  center_col2-50:center_col2+50] = center1[:, :]
    cv2.imwrite('output/ps0-3-a-1.png', transplant2_r)

# 4a
# Get the min and max pixel values for img1_g
min = img1_g[..., 1].min()
max = img1_g[..., 1].max()

# Get the mean and standard deviation values for img1_g
stddev = np.std(img1_g[..., 1])
mn = np.mean(img1_g[..., 1])

# Print the results
print '### img1_g ###'
print 'min: ', min
print 'max: ', max
print 'mean: ', mn
print 'standard deviation: ', stddev

# 4b
# Perform a bunch of arithmetic on the image
modified1_g = copy.copy(img1_g)
modified1_g[..., 1] -= int(mn)
modified1_g[..., 1] /= int(stddev)
modified1_g[..., 1] *= 10
modified1_g[..., 1] += int(mn)
cv2.imwrite('output/ps0-4-b-1.png', modified1_g)

# 4c
# Shift img1_g two pixels to the left
# Create a transformation matrix
rows, cols, chan = img1_g.shape
m = np.float32([[1, 0, -2], [0, 1, 0]])
# Apply the matrix to the source image 
img1_g_lshift2 = cv2.warpAffine(img1_g, m, (cols, rows))
cv2.imwrite('output/ps0-4-c-1.png', img1_g_lshift2)

# 4d
diff = img1_g - img1_g_lshift2
cv2.imwrite('output/ps0-4-d-1.png', diff)