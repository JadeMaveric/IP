import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import numpy as np

def select_image():
    global image0, image1

    path = tk.filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = Image.fromarray(gray)
        gray = ImageTk.PhotoImage(gray)
        image1.configure(image=gray)
        image1.image = gray

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image0.configure(image=image)
        image0.image = image



root = tk.Tk()

button = tk.Button(root, text="Load Image", command=select_image)
button.grid(column=0, row=0)

label0 = tk.Label(root, text="Original")
label0.grid(column=0, row=1)
image0 = tk.Label(root, image=None)
image0.grid(column=0, row=2)

label1 = tk.Label(root, text="Grayscale")
label1.grid(column=1, row=1)
image1 = tk.Label(root, image=None)
image1.grid(column=1, row=2)

root.mainloop()