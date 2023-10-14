import cv2 as cv
import numpy as np
import os

def save_image(image_path, changed_image):
    image_name = image_path.split('/')[-1]
    
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images")

    output_path = f'{out}/changed_{image_name}'

    cv.imwrite(output_path, changed_image)

def plot_images(original_image, changed_image):
    cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Original Image', 300, 300)
    cv.imshow('Original Image', original_image)

    cv.namedWindow('Changed Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Changed Image', 300, 300)
    cv.moveWindow('Changed Image', 510, 100)
    cv.imshow('Changed Image', changed_image)

def filter(image, alpha):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # kernel = np.array([[1, 4, 7, 4, 1],
    #                    [4, 16, 26, 16, 4],
    #                    [7, 26, 41, 26, 7],
    #                    [4, 16, 26, 16, 4],
    #                    [1, 4, 7, 4, 1]]) / 273
    
    kernel = np.array([[1, 2, 3, 2, 1], 
                       [2, 6, 8, 6, 2], 
                       [3, 8, 10, 8, 3], 
                       [2, 6, 8, 6, 2], 
                       [1, 2, 3, 2, 1]]) / 98
    
    blur_image = cv.filter2D(gray_image, -1, kernel)

    

    mask = gray_image - blur_image

    changed_image = gray_image + alpha * mask

    changed_image = np.clip(changed_image, 0, 255).astype(np.uint8)

    return changed_image

def main():
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images")
    image_path = f"{image_dir}/Fig0340.tif"
    original_image = cv.imread(image_path)
    a = 3
    
    changed_image = filter(original_image, a)

    plot_images(original_image, changed_image)

    save_image(image_path, changed_image)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()