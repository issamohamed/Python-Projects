# Name: Markus Gunadi, Issa Mohamed
# Date: 10/27/21
# Class: CS 111
# Prof: Aaron Bauer 

import matplotlib.pyplot as plt

# beach_portrait.png is an RGB image, so image is a 3D array with 3 values at each pixel location
# the slice is to remove an unnecessary alpha channel, if present
image = plt.imread("beach_portrait.png")[:, :, :3]


# YOUR CODE HERE TO COVERT image TO GRAYSCALE

# Finding the single pixel:
for row in range(len(image)):
    for column in range(len(image[row])):
        rgb_pixel = image[row][column] 
        # Finding RG pixel average:
        RG_pixel_average = ((rgb_pixel[0] + rgb_pixel[1]) / 2)
        # Reassigning red and green pixel to average of both colors:
        rgb_pixel[0] = RG_pixel_average
        rgb_pixel[1] = RG_pixel_average



# save the data in gray_image as a grayscale image to a file called beach_portrait_gray.png
# plt.gray()
plt.imsave("beach_portrait_red_green.png", image)
