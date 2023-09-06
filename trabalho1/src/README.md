# Hue Inverter Image

The "Hue Inverter Image" is a Python application built using PyQt5, OpenCV (cv2), and NumPy. This application allows you to open, manipulate, and save images with a focus on changing the hue of an image.

## Prerequisites

Before using this application, ensure that you have the following dependencies installed:

- OpenCV (cv2)
- tkinter
- NumPy
- PIL (pillow)

You can install the required dependencies using pip:

  ```bash
  pip install opencv-python numpy pillow
  ```

## Usage

### How to use GUI.py and hue_inverter.py

1. Clone the repository to your local machine:

  ```bash
  git clone https://github.com/GabrVendrame/PDI.git
  ```

2. Run the script `GUI.py` using the following command, to use the aplication with GUI:

  ```bash
  python3 GUI.py
  ```

The application window will open, and you can use it to perform the following tasks:

- Open Image: Click the "Open Image" button to load an image for processing. You can select image files in various formats `(.png, .jpeg, .jpg, .jfif)` using the file dialog.

- Adjust Hue and X: You can adjust the "Matiz" (Hue) and "X" sliders to change the hue of the loaded image. The "Matiz" slider controls the primary hue, and the "X" slider controls the range of hues affected by the inversion. You can also manually input values in the corresponding text fields.

- Save Image: After modifying the image, click the "Save Image" button to save the processed image. You can specify the file name, location, and format `(.png, .jpeg, .jpg, .jfif)` using the file dialog.

3. If you don't want to use the application without GUI, you can use the standalone script `hue_inverter.py` for a simplified command-line version of the hue inversion process:

  ```bash
  python3 hue_inverter.py
  ```

- This script allows you to input the Hue value you wanted to change, and X value, which specifies the range of colors, and it will create a color-inverted image using the provided parameters. Both images (original and modified) will be displayed after the values are inputed.
To change the image you want to modify, remove the comment in the line specifying the image you want change, then comment the line of the current image. For new images inserted in the images folder you must add a line in the code, like this:

  ```python
  image_path = "trabalho1/images/(name_of_image).(extension)"
  ```

Change `(name_of_image)` with the name of the image you want to use and `(extension)` is the type of image, that must be one of the following types: `(.png, .jpeg, .jpg, .jfif)`

<!-- ### How to use plot_hue.ipynb -->

## Features

- Load images in various formats.
- Adjust hue and the range of hues for inversion.
- Real-time preview of image changes.
- Save the processed image in different formats.

You can further customize and extend this application to meet your specific image processing needs.
