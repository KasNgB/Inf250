from skimage import io, filters, color, morphology, segmentation, measure
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
import numpy as np
import time

start = time.time()


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
   
def opening(image, footprint):
    opened_img = morphology.opening(image, footprint)
    return opened_img

def closing(image, footprint):
    closed_img = morphology.closing(image, footprint)
    return closed_img

def apply_watershed(image):
    distance = ndi.distance_transform_edt(image)
    coords = peak_local_max(distance, footprint = np.ones((3, 3)), labels=image, min_distance=100)
    mask = np.zeros(distance.shape, dtype=bool)
    mask[tuple(coords.T)] = True
    markers, _= ndi.label(mask)
    labels = segmentation.watershed(-distance, markers, mask=image)
    return labels

def prop_info(labeled_img):
    info = measure.regionprops(labeled_img)
    return info

def cropped_image(image, x_crop, y_crop):
    cropped = image[y_crop:image.shape[0]-y_crop, x_crop:image.shape[1]-x_crop]
    return cropped


pic = read_img("sort.JPG")
cropped_original = cropped_image(pic, 500,  300)
prepared = prepare_img(pic)
cropped_img = cropped_image(prepared, 500,  300)
# footprint = set_footprint(5)
# close = closing(cropped_img, footprint) Makes program much slower, have not experienced any advantages to using this
# opened_img = opening(close, footprint)
watershed = apply_watershed(cropped_img)
object_info = prop_info(watershed)

relevant_objects = []
for region in object_info:
    if region.area > 20000: 
        relevant_objects.append(region)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(cropped_original)

for region in relevant_objects:
    minr, minc, maxr, maxc = region.bbox
    width = maxc - minc
    height = maxr - minr

    # Determine shape based on eccentricity
    if region.eccentricity < 0.5:
        shape = "Nonstop"
        edge_color = "green"
    else:
        shape = "M&M"
        edge_color = "red"

    # Draw rectangle around object
    rect = patches.Rectangle((minc, minr), width, height, 
                             linewidth=2, edgecolor=edge_color, facecolor='none')
    ax.add_patch(rect)

    # Add label text
    ax.text(minc, minr-5, f"{shape}", color=edge_color, fontsize=10, weight='bold')

plt.title("Objects with Bounding Boxes")
plt.axis('off')

end = time.time()
print(end-start)
plt.show()

