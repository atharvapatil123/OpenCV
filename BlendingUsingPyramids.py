# Blending means mixing
import cv2
import numpy as np

apple = cv2.imread('data\\apple.jpg')
orange = cv2.imread('data\orange.jpg')
print(apple.shape)
print(orange.shape)

# apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
apple_orange = np.vstack((apple[:256, :], orange[256:, :]))
#hstack method does the blendng for us and :256 is upto 256 and 256: is from 256, also : is for all x 


# To blend the line as well, we using pyramid tech.

# 1.) Load the two images
# 2.) Find Gaussian pyramids for both the images
# 3.) From Gaussian pyramids, find their Laplacian pyramids
# 4.) Now join the left half of apple and right half of orange in each levels of Laplacian pyramids
# 5.) Finally, from this joint image pyramids, reconstruct the original image

# Step 2.)
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Step 3.)
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    gausssian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gausssian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gausssian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gausssian_expanded)
    lp_orange.append(laplacian)


# Step 4.)
apple_orange_pyramid = []
n=0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    # laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    # laplacian = np.hstack((orange_lap[:, 0:int(cols/2)], apple_lap[:, int(cols/2):]))
    # laplacian = np.vstack((apple_lap[0:int(rows/2), :], orange_lap[int(rows/2):, :]))
    laplacian = np.vstack((orange_lap[0:int(rows/2), :], apple_lap[int(rows/2):, :]))
    apple_orange_pyramid.append(laplacian)

# Step 5.)
apple_orange_reconstuct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstuct = cv2.pyrUp(apple_orange_reconstuct)
    apple_orange_reconstuct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstuct)



cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("apple_orange",apple_orange)
cv2.imshow("apple_orange_reconstruct",apple_orange_reconstuct)
cv2.waitKey(0)
cv2.destroyAllWindows()



