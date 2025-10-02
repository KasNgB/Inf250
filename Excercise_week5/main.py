import matplotlib.pyplot as plt
import numpy as np
import prepare_image
import dilate_image
import footprints 
import erode_image
import open_image
import countour_image

def main():
    # images_to_save = []

    img_path = 'car.jpg'
    img = prepare_image.load_image(img_path)
    greyscale_img = prepare_image.convert_greyscale(img)
    binary_img = prepare_image.convert_binary(greyscale_img)
    binary_img = (binary_img > 0).astype(np.uint8) * 255
    # images_to_save.append(binary_img)

    # square_fp = footprints.square_footprint(3)
    # circle_fp = footprints.circle_footprint(3)
    # footprints_list = [square_fp, circle_fp]

    # opening_image = [open_image.opening_image(binary_img, fp) for fp in footprints_list]
    countoured_image = countour_image.countoured_image(binary_img)
    # images_to_save.extend(opening_image)

    file_names = ['countoured.png']
    
    plt.imsave(f"results/{file_names[0]}", countoured_image, cmap='gray')
    # index = 0
    # for img in images_to_save:
    #     plt.imsave(f'results/{file_names[index]}',img, cmap='gray')
    #     index += 1




main()
