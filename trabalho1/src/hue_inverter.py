import cv2 as cv
import numpy as np

def plot_image(image, name):
    cv.imwrite('trabalho1/images/color_inverted_' + name, image)

def invert_hue(image, m, x):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    lower_interval = np.mod((m - x) / 2, 180)
    upper_interval = np.mod((m + x) / 2, 180)

    image_hue = hsv_image[:, :, 0]

    lower = lower_interval <= image_hue
    upper = upper_interval >= image_hue

    image_hue = image_hue.astype(np.uint16)


    if lower_interval > upper_interval:
        image_mask = np.logical_or(upper, lower)
    else:
        image_mask = np.logical_and(upper, lower)

    image_hue[image_mask] = np.mod((image_hue[image_mask] + 90), 180).astype(np.uint8)

    hsv_image[:, :, 0] = image_hue

    changed_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    return changed_image

def main():
    image_name = input('Image name: ')
    image = cv.imread('trabalho1/images/' + image_name)
    m = int(input('Hue: '))
    x = int(input('X: '))

    changed_image = invert_hue(image, m, x)

    plot_image(changed_image, image_name)

if __name__ == '__main__':
    main()
