from skimage import measure
import numpy as np
import prepare_image
import matplotlib.pyplot as plt

def countoured_image(image):
    img = prepare_image.load_image('car.jpg')
    greyscale = prepare_image.convert_greyscale(img)
    binary = prepare_image.convert_binary(greyscale)
    countours =  measure.find_contours(binary, level = 0.5)

    plt.imshow(binary, cmap='gray')

    for countour in countours:
       plt.plot(countour[:, 1], countour[:, 0], linewidth=2)


    plt.axis('image')
    plt.gca().invert_yaxis()
    plt.show()

countoured_image('car.jpg')

