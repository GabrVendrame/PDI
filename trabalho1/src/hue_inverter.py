import numpy as np
from skimage import color
from skimage.io import imsave, imread
from skimage.util import img_as_ubyte
import matplotlib.pyplot as plt

def plot_image(changed_image, name):
    # Save the image with the new name
    file_name = 'trabalho1/images/color_inverted_' + name
    imsave(file_name, img_as_ubyte(changed_image))

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].set_title("Original Image")
    axes[0].imshow(image)
    axes[0].axis('off')

    axes[1].set_title("Inverted Hue Image")
    axes[1].imshow(changed_image)
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()

def invert_hue(image, m, x):
    if image.shape[2] == 4:
        # If the image has an alpha channel, remove it
        image = image[:, :, :3]

    hsv_image = color.rgb2hsv(image)

    lower_interval = (np.mod((m - x), 360)) / 360
    upper_interval = (np.mod((m + x), 360)) / 360

    image_hue = hsv_image[:, :, 0]

    lower = lower_interval <= image_hue
    upper = upper_interval >= image_hue

    if lower_interval > upper_interval:
        image_mask = np.logical_or(upper, lower)
    else:
        image_mask = np.logical_and(upper, lower)

    image_hue[image_mask] = np.mod((image_hue[image_mask] + 0.5), 1)

    hsv_image[:, :, 0] = image_hue

    changed_image = color.hsv2rgb(hsv_image)

    return changed_image

def main():
    global image
    image_name = input('Image name: ')
    image = imread('trabalho1/images/' + image_name)
    m = int(input('Hue: '))
    x = int(input('X: '))

    changed_image = invert_hue(image, m % 360, x)

    plot_image(changed_image, image_name)

if __name__ == '__main__':
    main()