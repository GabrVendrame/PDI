import cv2 as cv
import numpy as np
import os

def save_image(image_path, changed_image):
    image_name = image_path.split('/')[-1]
    
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images")

    output_path = f'{out}/sharpened_{image_name}'

    cv.imwrite(output_path, changed_image)

def plot_images(original_image, changed_image):
    cv.imshow('Original Image', original_image)

    cv.imshow('Changed Image', changed_image)

def high_boost(image, k):
    gray_image = image.copy().astype(np.float32)

    # faz convolucao com filtro gaussiano 5x5 e desvio padrao 3
    low_filter = cv.GaussianBlur(gray_image, (5, 5), 3)

    sharpness_mask = gray_image - low_filter

    # normalizando valores na mascara
    sharpness_mask = np.clip(sharpness_mask, 0, 255)

    changed_image = image + k * sharpness_mask

    changed_image = np.clip(changed_image, 0, 255).astype(np.uint8)

    # ajustando mascara para melhor visualizacao
    sharpness_mask += 255
    sharpness_mask /= 2

    cv.imshow('Blurred Image', low_filter.astype(np.uint8))
    cv.imshow('Mask', sharpness_mask.astype(np.uint8))

    return changed_image

def main():
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images")
    image_path = f"{image_dir}/Fig0340.tif"
    original_image = cv.imread(image_path)
    k = 4.5
    
    changed_image = high_boost(original_image, k)

    plot_images(original_image, changed_image)

    save_image(image_path, changed_image)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()