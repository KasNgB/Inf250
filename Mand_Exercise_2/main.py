from skimage import io, filters, color, morphology
import matplotlib.pyplot as plt

def read_img(filepath):
    img = io.imread(filepath)
    return img

def prepare_img(image):
    if len(image.shape) == 3 and image.shape[-1] == 3:
        greyscale_image = color.rgb2gray(image)
    elif len(image.shape) == 3 and image.shape[-1] == 4:
        greyscale_image =  color.rgb2gray(color.rgba2rgb(image))
    elif len(image.shape) == 2:
        greyscale_image = image    

    blurred_greyscale = filters.gaussian(greyscale_image)
    threshold = filters.threshold_yen(blurred_greyscale)
    binary_pic = greyscale_image < threshold
    cleaned = morphology.remove_small_holes(binary_pic, area_threshold=20000)
    
    return cleaned

def set_footprint(value):
    footprint = morphology.disk(value)
    return footprint
   
def opening(binary_img, footprint):
    opened_img = morphology.opening(binary_img, footprint)
    return opened_img

def closing(binary_img, footprint):
    closed_img = morphology.closing(binary_img, footprint)
    return closed_img


pic = read_img("sort.JPG")
prepared = prepare_img(pic)
footprint = set_footprint(13)
open = closing(prepared, footprint)
finished_pic = opening(open, footprint)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(finished_pic, cmap="gray")
axes[0].set_title("finished")

axes[1].imshow(prepared, cmap="gray")
axes[1].set_title("binary")

plt.show()
