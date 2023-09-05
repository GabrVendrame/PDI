# Hue Inverter Image

The "Hue Inverter Image" is a Python application built using PyQt5, OpenCV (cv2), and NumPy. This application allows you to open, manipulate, and save images with a focus on changing the hue of an image.

## Prerequisites

Before using this application, ensure that you have the following dependencies installed:

- Python 3.x
- PyQt5
- OpenCV (cv2)
- NumPy

You can install the required dependencies using pip:

  ```bash
  pip install PyQt5 opencv-python-headless numpy
  ```

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GabrVendrame/PDI.git
   ```

2. Run the script `GUI.py` using the following command, to use the aplication with GUI:

  ```bash
  python3 GUI.py
  ```

The application window will open, and you can use it to perform the following tasks:

- Open Image: Click the "Open Image" button to load an image for processing. You can select image files in various formats (JPEG, PNG, TIFF, HEIF/HEIC) using the file dialog.

- Adjust Hue and X: You can adjust the "Matiz" (Hue) and "X" sliders to change the hue of the loaded image. The "Matiz" slider controls the primary hue, and the "X" slider controls the range of hues affected by the inversion. You can also manually input values in the corresponding text fields.

- Save Image: After modifying the image, click the "Save Image" button to save the processed image. You can specify the file name, location, and format (JPEG, PNG, TIFF, HEIF/HEIC) using the file dialog.

3. If you don't want to use the application without GUI, you can use the standalone script `hue_inverter.py` for a simplified command-line version of the hue inversion process:

  ```bash
  python3 hue_inverter.py
  ```

- This script allows you to input the image name (must be with the extension included), Hue value, and X value, and it will create a color-inverted image using the provided parameters.

## Features

- Load images in various formats.
- Adjust hue and the range of hues for inversion.
- Real-time preview of image changes.
- Save the processed image in different formats.

You can further customize and extend this application to meet your specific image processing needs.
