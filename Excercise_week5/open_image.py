from skimage import morphology

def opening_image(image, footprint):
    opening_image = morphology.binary_opening(image, footprint)
    return opening_image
