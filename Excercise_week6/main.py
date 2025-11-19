from skimage import io, color
import matplotlib.pyplot as plt

def read_img(filepath):
    image = io.imread(filepath)
    return image

def convert_lab(img):
    converted_img = color.rgb2lab(img)
    return converted_img

def split_channels(image):
    inp = input("""
                1: Red/L
                2: Blue/A
                3: Green/B
                """)
    if inp == "1":
        channel = image[:,:,0]
    elif inp == "2":
        channel = image[:,:,1]
    elif inp == "3":
        channel = image[:,:,2]
    else:
        raise Exception("Choose from the options")
    return channel

def convert_HSV(img):
    converted_img = color.rgb2hsv(img)
    return converted_img

def edit_HSV(image):
    cp_image = image.copy()
    cp_image[:, :, 2] = 1
    return cp_image

img = read_img("bush.png")
converted = convert_HSV(img)
edited_HSV = edit_HSV(converted)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].imshow(converted)
axs[0].set_title("Original Image")
axs[0].axis('off')

# Display edited image
axs[1].imshow(edited_HSV)
axs[1].set_title("Edited Image")
axs[1].axis('off')

plt.show()
