from skimage import morphology

def square_footprint(size):
    footprint = morphology.footprint_rectangle((size, size))
    return footprint 

def circle_footprint(radius):
    footprint = morphology.disk(radius)
    return footprint
