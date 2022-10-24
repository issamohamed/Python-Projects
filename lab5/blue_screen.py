# Name: Markus Gunadi, Issa Mohamed
# Date: 10/27/21
# Class: CS 111
# Prof: Aaron Bauer 

import matplotlib.pyplot as plt

# oz_bluescreen and meadow are a RGB images, so image and background are 3D arrays
# and have 3 values at every pixel location
# the slice is to remove an unnecessary alpha channel, if present
image = plt.imread("oz_bluescreen.png")[:, :, :3]
background = plt.imread("meadow.png")[:, :, :3]


# YOUR CODE HERE TO MODIFY image TO PUT THE WIZARD AND HIS BALLOON IN THE MEADOW
# Finding the single pixel:
for row in range(len(image)):
    for column in range(len(image[row])):
        rgb_pixel = image[row][column]
        # Equation:
        if rgb_pixel[2] > (rgb_pixel[1] + rgb_pixel[0]):
            # Reassigning the blue-heavy pixels
            image[row][column] = background[row][column]






# save the modified image to a new file called oz_meadow.png
plt.imsave("oz_meadow.png", image)