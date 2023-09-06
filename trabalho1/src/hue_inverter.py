import cv2 as cv
import numpy as np

def plot_images(image, name):
    global original_image
    cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Original Image', 400, 400)
    cv.imshow('Original Image', original_image)

    cv.namedWindow('Changed Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Changed Image', 400, 400)
    cv.imshow('Changed Image', image)

    cv.waitKey(0)

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
    global original_image
    image_name = "trabalho1/images/matiz.png"
    # image_name = "trabalho1/images/matiz_angulos.png"
    # image_name = "trabalho1/images/mengao.png"
    original_image = cv.imread(image_name)
    m = float(input('Hue: '))
    x = float(input('X: '))

    changed_image = invert_hue(original_image, m, x)

    plot_images(changed_image, image_name)

if __name__ == '__main__':
    main()
