# Name: Markus Gunadi, Issa Mohamed
# Date: 10/27/21
# Class: CS 111
# Prof: Aaron Bauer 

import matplotlib.pyplot as plt

# beach_portrait_gray.png is an RGB image, so image is a 3D array with 3 values at each pixel location
# the slice is to remove an unnecessary alpha channel, if present
image = plt.imread("beach_portrait.png")[:, :, :3]


def blur(img, radius):
    radius = int(radius)
    # Checks and balances for common errors:
    if (radius < 0):
        print("radius is a negative number.")
        return img
    new_img = img.copy()
    # Calculating the perimeter of image:
    img_height = len(img) - 1
    img_width = len(img[0]) - 1
    for row in range(len(image)):
        # Finding the single pixel:
        for column in range(len(image[row])):
            rgb_pixel = image[row][column]
            # Calculating the perimeter and edge cases of the image:
            start_width = column - radius
            if (start_width < 0):
                start_width = 0
            end_width = column + radius 
            if (end_width > img_width):
                end_width = img_width
            start_height = row - radius
            if (start_height < 0):
                start_height = 0
            end_height =  row + radius
            if (end_height > img_height):
                end_height = img_height
            splice_img_array = img[start_height:end_height,start_width: end_width]
            # finding mean average of each color in each pixel:
            red_pixel_mean_value = splice_img_array[:, :, 0].mean()
            green_pixel_mean_value = splice_img_array[:, :, 1].mean()
            blue_pixel_mean_value = splice_img_array[:, :, 2].mean()
            mean_pixel_array = [red_pixel_mean_value, green_pixel_mean_value, blue_pixel_mean_value]
            new_img[row][column] = mean_pixel_array
    return new_img
            






            
                
    # YOUR CODE HERE TO PRODUCE AND RETURN A NEW array THAT IS A BLURRED VERSION OF img
    

plt.imsave("beach_portrait_blur.png", blur(image, 3))