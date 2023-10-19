# High-Boost Filter

This project aims to implement and test the high-boost filtering method for enhancing the sharpness of digital images. The method involves receiving images with reduced sharpness and returning another image with enhanced sharpness as per the high-boost filtering technique. The low-pass filtering in this project is performed in the spatial domain through convolution. The implementation is done in Python 3.10.12, utilizing the Numpy library. Additionally, the OpenCV library is used for image loading, saving, and display.

## Prerequisites

Before using this application, ensure that you have the following dependencies installed:

- Numpy library
- OpenCV library

You can install those dependencies by running the following command:

  ```bash
  pip install numpy
  ```
  ```bash
  pip install opencv-python
  ```

## Usage

### How to use highBoostFilter.py

1. Clone the repository to your local machine:

  ```bash
  git clone https://github.com/GabrVendrame/PDI.git
  ```

2. Run the script `highBoostFilter.py`:

  ```bash
  python3 highBoostFilter.py
  ```

The application will apply the high boost filter, returning the sharpened image.

- To specify the image you want to apply the filter you should change the script in the codeline similar to this:

  ```python
  image_path = f"{image_dir}/(name_of_image).(extension)"
  ```

ONLY `(name_of_image)` and `(extension)` must be changed. The `(name_of_image)` is the name of the image you want to sharp and `(extension)` is any type of image files like `(.png, .jpeg, .jpg, .jfif, .tif)`

## Implementation Details

The high-boost sharpening is achieved through spatial domain convolution using a low-pass filter. The Numpy library is employed for efficient array operations, and OpenCV is used for image I/O operations.

## Contribution

Feel free to explore and enhance the code for further experimentation and understanding.