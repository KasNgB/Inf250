from skimage import morphology, measure
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import prepare_image

img = prepare_image.load_image('figures.png')
greyscale_img = prepare_image.convert_greyscale(img)
binary_img = prepare_image.convert_binary(greyscale_img)

def set_footprint(value):
    footprint = morphology.footprint_rectangle((value, value))
    return footprint

def opening(binary_img, footprint):
    opened_img = morphology.opening(binary_img, footprint)
    return opened_img

def closing(binary_img, footprint):
    closed_img = morphology.closing(binary_img, footprint)
    return closed_img

def label_objects(binary_img, connectivity=2):
    labeled_img = measure.label(binary_img, connectivity)
    return labeled_img

def prop_info(labeled_img):
    info = measure.regionprops(labeled_img)
    return info



footprint = set_footprint(15)
opened = opening(binary_img, footprint)
finished_pic = closing(opened, footprint)
labeled_img = label_objects(finished_pic)
object_info = prop_info(labeled_img)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(finished_pic, cmap='gray')

for region in object_info:
    minr, minc, maxr, maxc = region.bbox
    width = maxc - minc
    height = maxr - minr

    # Determine shape based on eccentricity
    if region.eccentricity < 0.5:
        shape = "Circle"
        edge_color = "green"
    else:
        shape = "Rectangle"
        edge_color = "red"

    # Draw rectangle around object
    rect = patches.Rectangle((minc, minr), width, height, 
                             linewidth=2, edgecolor=edge_color, facecolor='none')
    ax.add_patch(rect)

    # Add label text
    ax.text(minc, minr-5, f"{shape}", color=edge_color, fontsize=10, weight='bold')

plt.title("Objects with Bounding Boxes")
plt.axis('off')
plt.show()




