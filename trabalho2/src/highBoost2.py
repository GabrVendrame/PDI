import cv2
import os
import numpy as np


def unsharp_masking(image_path, output_path, alpha=1.5, sigma=1.0):
    # Step 1: Load the original image
    original_image = cv2.imread(image_path)

    # Step 2: Make a copy of the original image to avoid modifying it
    image_copy = original_image.copy().astype(np.float32)

    # Step 3: Blur the copied image
    blurred_image = cv2.GaussianBlur(image_copy, (5, 5), 3)

    # Step 4: Subtract the blurred image from the copied image to create the mask
    mask = image_copy - blurred_image

    # Step 5: Add the mask to the original image to get the sharpened image
    sharpened_image = original_image + 1 * mask

    # Clip the values to ensure they are in the valid range (0-255)
    sharpened_image = np.clip(sharpened_image, 0, 255).astype(np.uint8)

    # Convert mask back to uint8 for display
    mask = np.clip(mask, -255, 255) # Ensure values are in valid range for conversion
    mask += 255 # Shift values to positive range
    mask /= 2 # Scale values back down to between 0 and 255
    mask = mask.astype(np.uint8)

    # Step 6: Display and save the sharpened image
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.imshow('blurred_image', blurred_image.astype(np.uint8))
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(output_path, sharpened_image)


if __name__ == "__main__":
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images")
    image_path = f"{image_dir}/Fig0340.tif"
    #original_image = cv2.imread(image_path)
    output_image_path = 'output_image.jpg'  # Replace with the desired output image path
    #cv2.imshow('Original Image', original_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    unsharp_masking(image_path, output_image_path, alpha=4.5, sigma=1.0)
