from skimage import io, feature, filters
import matplotlib.pyplot as plt

def edge_detection(image_path):
    print("""
          Edge Detecton options:
            1. Canny Edge edge_detection
            2. Sobel Edge edge_detection
            3. Prewitt Edge edge_detection
          """)

    save_path = 'results/'
    inp = input("Choose an option (1-3): ")
    if inp not in ['1', '2', '3']:
        raise ValueError("Invalid option. Please choose a number between 1 and 3.")

    image = io.imread(image_path, as_gray=True)
    
    if inp == '1':
        edges = feature.canny(image)
        plt.imshow(edges)
        plt.savefig(f'{save_path}Canny_Edge_Detection.png')

    if inp == '2':
        edges = filters.sobel(image)
        plt.imshow(edges)
        plt.savefig(f'{save_path}Sobel_Edge_Detection.png')

    if inp == '3':
        edges = filters.prewitt(image)
        plt.imshow(edges)
        plt.savefig(f'{save_path}Prewitt_Edge_Detection.png')


def image_sharpening(image_path):
    print("""
          Image Sharpening options:
            1. Unsharp Masking
            2. Laplacian Filter
          """)

    save_path = 'results/'
    inp = input("Choose an option (1-2): ")
    if inp not in ['1', '2']:
        raise ValueError("Invalid option. Please choose a number between 1 and 2.")

    image = io.imread(image_path, as_gray=False)
    plt.imshow(image, cmap='gray') 
    plt.savefig(f'{save_path}Original_Image.png')
    if inp == '1':
        blurred = filters.gaussian(image, sigma=1)
        sharpened = image + (image - blurred)
        plt.imshow(sharpened, cmap='gray')
        plt.savefig(f'{save_path}Unsharp_Masking.png')

    if inp == '2':
        laplacian = filters.laplace(image)
        # sharpened = image - laplacian
        plt.imshow(laplacian)
        plt.savefig(f'{save_path}Laplacian_Filter.png')

image_sharpening('AthenIR.png')













