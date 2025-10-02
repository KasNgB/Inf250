from skimage import morphology

def eroded_image(image, footprint):
    eroded_image = morphology.binary_erosion(image, footprint)
    return eroded_image
