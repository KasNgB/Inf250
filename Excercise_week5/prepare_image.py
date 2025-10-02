from skimage import io, filters, color

def load_image(path):
    img_matrice = io.imread(path)
    return img_matrice

def convert_greyscale(image):
    if len(image.shape) == 3 and image.shape[-1] == 3:
        greyscale_image = color.rgb2gray(image)
        return greyscale_image
    if len(image.shape) == 3 and image.shape[-1] == 4:
        greyscale_image =  color.rgb2gray(color.rgba2rgb(image))
        return greyscale_image
    if len(image.shape) == 2:
        return image
    else:
        raise Exception("Invalid image shape")

def convert_binary(image):
    threshold = filters.threshold_otsu(image)
    binary = image <  threshold
    return binary 

