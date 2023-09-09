import cv2 as cv
import numpy as np

def save_image(image_path, changed_image):
    image_name = image_path.split('/')[-1]

    output_path = f'trabalho1/images/changed_{image_name}'

    cv.imwrite(output_path, changed_image)

def plot_images(original_image, changed_image):
    cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Original Image', 400, 400)
    cv.imshow('Original Image', original_image)

    cv.namedWindow('Changed Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Changed Image', 400, 400)
    cv.moveWindow('Changed Image', 510, 100)
    cv.imshow('Changed Image', changed_image)

    cv.waitKey(0)

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
    image_path = "trabalho1/images/matiz.png"
    # image_path = "trabalho1/images/matiz_angulos.png"
    # image_path = "trabalho1/images/mengao.png"
    # image_path = "trabalho1/images/anorlondo.png"
    # image_path = "trabalho1/images/divine-dragon.jpeg"
    # image_path = "trabalho1/images/erdtre.png"
    # image_path = "trabalho1/images/majula.png"
    original_image = cv.imread(image_path)
    m = int(input('Hue: '))
    x = int(input('X: '))

    changed_image = invert_hue(original_image, m, x)

    plot_images(original_image, changed_image)

    save_image(image_path, changed_image)

if __name__ == '__main__':
    main()