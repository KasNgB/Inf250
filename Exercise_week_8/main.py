from skimage import io, color, feature
import matplotlib.pyplot as plt
import numpy as np

def read_img(filepath):
    img = io.imread(filepath)
    return img

def greyscaled(img):
    if len(img.shape) == 3 and img.shape[-1] == 3:
        greyscale_img = color.rgb2gray(img)
    elif len(img.shape) == 3 and img.shape[-1] == 4:
        greyscale_img =  color.rgb2gray(color.rgba2rgb(img))
    elif len(img.shape) == 2:
        greyscale_img = img    
    return greyscale_img


def get_area(img, x_start, x_end, y_start, y_end):
    sliced_img = img[y_start:y_end, x_start:x_end]
    return sliced_img

def get_histogram(img):
    hist, bins = np.histogram(img.flatten(), bins=256, range=[0, 1])
    return hist, bins

def glcm_analysis(img, choice):
    analysis = feature.graycoprops(img, prop=f'{choice}')
    return analysis 


image = read_img("leaf.jpg")
greyscaled_img = greyscaled(image)
sliced1 = get_area(greyscaled_img, 200, 250, 200, 250)
sliced2 = get_area(greyscaled_img, 100, 150, 25, 75)
sliced3 = get_area(greyscaled_img, 0, 50, 100, 150)
hist1, bins1 = get_histogram(sliced1)
hist2, bins2 = get_histogram(sliced2)
hist3, bins3 = get_histogram(sliced3)


fig, axs = plt.subplots(2, 3, figsize=(12, 6))

# Row 0: images
axs[0, 0].imshow(sliced1, cmap="gray")
axs[0, 0].set_title("Patch 1")
axs[0, 0].axis('off')

axs[0, 1].imshow(sliced2, cmap="gray")
axs[0, 1].set_title("Patch 2")
axs[0, 1].axis('off')

axs[0, 2].imshow(sliced3, cmap="gray")
axs[0, 2].set_title("Patch 3")
axs[0, 2].axis('off')

# Row 1: histograms
axs[1, 0].bar(bins1[:-1], hist1, width=(bins1[1]-bins1[0]), color='gray')
axs[1, 0].set_title("Histogram 1")
axs[1, 0].set_xlabel("Intensity")
axs[1, 0].set_ylabel("Pixel count")

axs[1, 1].bar(bins2[:-1], hist2, width=(bins2[1]-bins2[0]), color='gray')
axs[1, 1].set_title("Histogram 2")
axs[1, 1].set_xlabel("Intensity")
axs[1, 1].set_ylabel("Pixel count")

axs[1, 2].bar(bins3[:-1], hist3, width=(bins3[1]-bins3[0]), color='gray')
axs[1, 2].set_title("Histogram 3")
axs[1, 2].set_xlabel("Intensity")
axs[1, 2].set_ylabel("Pixel count")

plt.tight_layout()
plt.show()
