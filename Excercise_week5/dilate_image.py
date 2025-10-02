from skimage import morphology

def dilate_image(image, footprint):
    dilated_image = morphology.binary_dilation(image, footprint)
    return dilated_image
