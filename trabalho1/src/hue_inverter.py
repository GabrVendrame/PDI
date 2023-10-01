import cv2 as cv
import numpy as np

def save_image(image_path, changed_image):
    image_name = image_path.split('/')[-1]

    output_path = f'images/changed_{image_name}'

    cv.imwrite(output_path, changed_image)

def plot_images(original_image, changed_image):
    cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Original Image', 300, 300)
    cv.imshow('Original Image', original_image)

    cv.namedWindow('Changed Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Changed Image', 300, 300)
    cv.moveWindow('Changed Image', 510, 100)
    cv.imshow('Changed Image', changed_image)

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
    x = -1
    # image_path = "images/matiz.png"
    # image_path = "images/anorlondo.png"
    # image_path = "images/divine-dragon.jpeg"
    # image_path = "images/duck.jpeg"
    # image_path = "images/erdtree.png"
    # image_path = "images/eye-of-sauron.jpg"
    image_path = "images/mengao.png"
    original_image = cv.imread(image_path)
    m = int(input('Hue: '))
    while x < 0 or x > 180:
        x = int(input('X: '))
        if x > 180 or x < 0: print("Values must be between [0, 180]")

    changed_image = invert_hue(original_image, m, x)

    plot_images(original_image, changed_image)

    save_image(image_path, changed_image)

    cv.waitKey(0)

if __name__ == '__main__':
    main()