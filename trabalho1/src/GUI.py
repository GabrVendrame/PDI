import cv2 as cv
import os
from hue_inverter import invert_hue
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

def update_image():
    global input_image, output_image
    global hue_value, x_value
    global x_label, hue_label, image_label
    global hue_slider, x_slider
    new_hue_value = int(hue_slider.get())
    new_x_value = int(x_slider.get())

    hue_value = new_hue_value
    x_value = new_x_value
    output_image = invert_hue(input_image, hue_value, x_value)
    img = Image.fromarray(cv.cvtColor(output_image, cv.COLOR_BGR2RGB))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

def update_hue_label(value=None):
    global hue_label
    hue_label.config(text=f"Hue Value: {int(float(value))}")
    if (value):
        update_image()

def update_x_label(value=None):
    global x_label
    x_label.config(text=f"X Value: {int(float(value))}")
    if (value):
        update_image()

def select_file():

    global input_image
    filetypes = (
        ('Image Files', '*.png *.jpeg *.jpg *.jfif'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    input_image = cv.imread(filename)
    input_image = cv.resize(input_image, (450, 500))
    update_image()

def save_image():
    global output_image
    filetypes = (
        ('Image Files', '*.png *.jpeg *.jpg *.jfif'),
    )

    filename = fd.asksaveasfilename(
        title='Save Image',
        initialdir=os.getcwd(),
        filetypes=filetypes,
        defaultextension=".png",
    )

    if filename:
        cv.imwrite(filename, output_image)

root = tk.Tk()
root.title("Hue Adjustment")

input_image = cv.imread('trabalho1/images/matiz_angulos.png')
input_image = cv.resize(input_image, (450, 500))

hue_label = tk.Label(root, text= f"Hue Value: {0}")
hue_label.pack(expand=True)
hue_slider = ttk.Scale(root, from_=0, to=360, orient="horizontal", command=update_hue_label, length=360)
hue_slider.pack()

x_label = tk.Label(root, text=f"x Value: {0}")
x_label.pack()
x_slider = ttk.Scale(root, from_=0, to=180, orient="horizontal", command=update_x_label, length=360)
x_slider.pack()

img = Image.fromarray(cv.cvtColor(input_image, cv.COLOR_BGR2RGB))
img = ImageTk.PhotoImage(img, width=400, height=400)
image_label = tk.Label(root, image=img)
image_label.pack()

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file,
)

open_button.pack(expand=True)

save_button = ttk.Button(
    root,
    text='Save Image',
    command=save_image,
)

save_button.pack(expand=True)

update_image()

root.mainloop()