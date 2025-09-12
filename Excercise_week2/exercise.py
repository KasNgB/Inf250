import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('airfield.tif')


io.imshow(img)
io.show()

plt.hist(img.ravel(), bins=256, color='black', alpha=0.7)
plt.show()

edited_brightness = img + 50

io.imshow(edited_brightness)
io.show()

plt.hist(edited_brightness.ravel(), bins=256, color='black', alpha=0.7)
plt.show()


edited_contrast = img * 2

io.imshow(edited_contrast)
io.show()

plt.hist(edited_contrast.ravel(), bins=256, color='black', alpha=0.7)
plt.show()
