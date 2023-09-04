import sys
import numpy as np
from skimage import io
from skimage.transform import resize
from skimage.color import rgba2rgb
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel, QSlider, QLineEdit, QFileDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from hue_inverter import invert_hue

class ImageProcessorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hue Inverter")
        self.setGeometry(100, 100, 600, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        button_layout = QHBoxLayout()

        self.open_button = QPushButton("Open Image")
        self.open_button.setFixedSize(100, 35)
        self.open_button.clicked.connect(self.open_image)
        button_layout.addWidget(self.open_button, alignment=Qt.AlignLeft)

        self.save_button = QPushButton("Save Image")
        self.save_button.setFixedSize(100, 35)
        self.save_button.clicked.connect(self.save_image)
        button_layout.addWidget(self.save_button, alignment=Qt.AlignRight)

        self.layout.addLayout(button_layout)

        self.result_container = QFrame()  # Container for image display
        self.result_container.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.result_container.setLineWidth(1)
        self.layout.addWidget(self.result_container)

        self.result_layout = QVBoxLayout()  # Layout for image display
        self.result_container.setLayout(self.result_layout)
        self.result_container.setFixedHeight(500)

        self.result_label = QLabel()
        self.result_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)  # Center-align the image

        # Create horizontal layouts for "hue" and "x" components
        hue_layout = QHBoxLayout()
        self.hue_label = QLabel("Matiz:")
        self.hue_slider = QSlider(Qt.Horizontal)
        self.hue_entry = QLineEdit()
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(360)
        self.hue_entry.setFixedWidth(35)
        self.hue_slider.setFixedWidth(120)
        self.hue_slider.setFixedHeight(35)
        self.hue_slider.setEnabled(False)
        self.hue_entry.setEnabled(False)
        hue_layout.addWidget(self.hue_label, alignment=Qt.AlignCenter)
        hue_layout.addWidget(self.hue_slider, alignment=Qt.AlignLeft)
        hue_layout.addWidget(self.hue_entry, alignment=Qt.AlignLeft)
        hue_layout.setAlignment(Qt.AlignCenter)

        x_layout = QHBoxLayout()
        self.x_label = QLabel("X:")
        self.x_slider = QSlider(Qt.Horizontal)
        self.x_entry = QLineEdit()
        self.x_slider.setMinimum(0)
        self.x_slider.setMaximum(360)
        self.x_entry.setFixedWidth(35)
        self.x_slider.setFixedWidth(120)
        self.x_slider.setFixedHeight(35)
        self.x_slider.setEnabled(False)
        self.x_entry.setEnabled(False)
        x_layout.addWidget(self.x_label, alignment=Qt.AlignCenter)
        x_layout.addWidget(self.x_slider, alignment=Qt.AlignLeft)
        x_layout.addWidget(self.x_entry, alignment=Qt.AlignLeft)
        x_layout.setAlignment(Qt.AlignCenter)

        self.layout.addStretch(0)
        self.layout.addLayout(hue_layout)
        self.layout.addLayout(x_layout)

        self.central_widget.setLayout(self.layout)

        self.image = None
        self.changed_image = None

        self.hue_slider.valueChanged.connect(self.update_image)
        self.x_slider.valueChanged.connect(self.update_image)
        self.hue_entry.textChanged.connect(self.update_image)
        self.x_entry.textChanged.connect(self.update_image)

        # Connect slider value changes to update text input fields
        self.hue_slider.valueChanged.connect(self.update_hue_entry)
        self.x_slider.valueChanged.connect(self.update_x_entry)

        self.hue_entry.textChanged.connect(self.update_hue_slider)
        self.x_entry.textChanged.connect(self.update_x_slider)

    def open_image(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self,
                                "Open Image",
                                "trabalho1/images",
                                "Image files (*.jpg *.jpeg *.png *.tif *.tiff *.heif *.heic)")

        if file_path:
            self.image = io.imread(file_path)
            
            # Check if the image is RGBA and convert it to RGB
            if self.image.shape[-1] == 4:
                self.image = rgba2rgb(self.image)
            
            self.image = resize(self.image, (450, 450))
            self.display_image(self.image) 

            # Enable sliders if the image is loaded
            self.hue_slider.setEnabled(True)
            self.x_slider.setEnabled(True)

            # Enable text input fields if the image is loaded
            self.hue_entry.setEnabled(True)
            self.x_entry.setEnabled(True)

            self.update_image()

    def save_image(self):
        if self.changed_image is not None:
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName(self,
                                    "Save Image",
                                    "./images/untitled.png",
                                    "Image files (*.jpg *.jpeg *.png *.tif *.tiff *.heif *.heic)")

            if file_path:
                io.imsave(file_path, self.changed_image)

    def update_image(self):
        if self.image is not None:
            m = self.hue_slider.value()
            x = self.x_slider.value()
            self.hue_entry.setText(str(m))
            self.x_entry.setText(str(x))

            if x == 0:
                self.changed_image = self.image.copy()
            else:
                self.changed_image = invert_hue(self.image.copy(), m, x)
            self.display_image(self.changed_image)

    def update_hue_entry(self, value):
        self.hue_entry.setText(str(value))
        self.update_image()

    def update_x_entry(self, value):
        self.x_entry.setText(str(value))
        self.update_image()

    def update_hue_slider(self, value):
        value = int(value) % 360
        self.hue_slider.setValue(value)
        self.update_image()
    
    def update_x_slider(self, value):
        value = int(value) % 360
        self.x_slider.setValue(value)
        self.update_image()

    def display_image(self, image):
        if image is not None:
            image = (image*255).astype(np.uint8)
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.result_label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    window = ImageProcessorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()