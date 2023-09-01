import cv2
import numpy as np

def plot_image(image):
    width = 600
    height = 600
    cv2.namedWindow('Imagem Alterada', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Imagem Alterada', width, height)
    cv2.imshow('Imagem Alterada', image)
    cv2.waitKey(0)

def invert_hue(image, m, x):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

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

    changed_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return changed_image

def main():
    image = cv2.imread('matiz.png')
    m = int(input('Valor da matiz: '))
    x = int(input('X: '))

    changed_image = invert_hue(image, m, x)

    plot_image(changed_image)

if __name__ == '__main__':
    main()