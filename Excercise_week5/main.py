import matplotlib.pyplot as plt
import prepare_image
import dilate_image

def main():
    images_to_save = []

    img_path = 'car.jpg'
    img = prepare_image.load_image(img_path)
    greyscale_img = prepare_image.convert_greyscale(img)
    binary_img = prepare_image.convert_binary(greyscale_img)
    images_to_save.append(binary_img)

    square_footprint = dilate_image.square_footprint(3)
    circle_footprint = dilate_image.circle_footprint(3)
    footprints = [square_footprint, circle_footprint]   
    
    dilated_images = [dilate_image.dilate_image(binary_img, fp) for fp in footprints]
    images_to_save.extend(dilated_images)

    file_names = ['binary.png', 'dilated_square.png', 'dilated_circle.png']

    index = 0
    for img in images_to_save:
        plt.imsave(f'results/{file_names[index]}',img, cmap='gray')
        index += 1




main()
