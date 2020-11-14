import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import numpy as np


def stretch_contrast():
    global s1, s2, grayImage, colorImage, image1, image3

    if len(grayImage):
        r1 = grayImage.min()
        r2 = grayImage.max()
        a = s1.get()
        b = s2.get()

        gray = grayImage.copy()

        for x,y in np.ndindex((grayImage.shape)):
            r = gray[x,y]
            p = (b-a)*(r-r1)//(r2-r1)
            p += a
            gray[x,y] = p

        stretched = Image.fromarray(gray)
        stretched = ImageTk.PhotoImage(stretched)
        image1.configure(image=stretched)
        image1.image = stretched

    if len(colorImage):
        ci = colorImage

        r_plane = np.array([ci[x,y,0] for x,y in np.ndindex(ci.shape[:2])], dtype=int)
        g_plane = np.array([ci[x,y,1] for x,y in np.ndindex(ci.shape[:2])], dtype=int)
        b_plane = np.array([ci[x,y,2] for x,y in np.ndindex(ci.shape[:2])], dtype=int)

        r_min, r_max = r_plane.min(), r_plane.max()
        g_min, g_max = g_plane.min(), g_plane.max()
        b_min, b_max = b_plane.min(), b_plane.max()
        bounds = [(r_min, r_max), (g_min, g_max), (b_min, b_max)]
        color = colorImage.copy()

        for x,y,c in np.ndindex((color.shape)):
            r1 = bounds[c][0]
            r2 = bounds[c][1]
            r  = color[x,y,c]
            p  = (b-a)*(r-r1)//(r2-r1)
            p += a
            color[x,y,c] = p

        stretched_c = Image.fromarray(color)
        stretched_c = ImageTk.PhotoImage(stretched_c)
        image3.configure(image=stretched_c)
        image3.image = stretched_c

def select_image():
    # grab a reference to the image panel
    global imageO, image2, grayImage, colorImage

    #open a file selection dialog and allow the user to select an input image
    path =tk.filedialog.askopenfilename()

    #ensure a filepath was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        grayImage = gray
        gray = Image.fromarray(gray)
        gray = ImageTk.PhotoImage(gray)
        imageO.configure(image=gray)
        imageO.image = gray

        colorImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image2.configure(image=image)
        image2.image = image

        # Calculate and display the constrast streched version
        stretch_contrast()

# --- MAIN TKINTER STUFF ---

root = tk.Tk()
grayImage = []
colorImage = []

button_load = tk.Button(root, text="Load Image", command=select_image)
button_load.grid(column=2, row=4, sticky="sw")

labelO = tk.Label(root, text="Original")
labelO.grid(column=1, row=1)
imageO = tk.Label(root, image=None, padx=10)
imageO.grid(column=1, row=2)

label1 = tk.Label(root, text="Stretched")
label1.grid(column=2, row=1)
image1 = tk.Label(root, image=None)
image1.grid(column=2, row=2)

label2 = tk.Label(root, text="Coloured")
label2.grid(column=0, row=2)
image2 = tk.Label(root, image=None)
image2.grid(column=1, row=3)

label3 = tk.Label(root, text="Grayscale")
label3.grid(column=0, row=3)
image3 = tk.Label(root, image=None)
image3.grid(column=2, row=3)


label_s1 = tk.Label(root, text="s1")
label_s2 = tk.Label(root, text="s2")
label_s1.grid(column=0, row=4)
label_s2.grid(column=0, row=5)

s1 = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
s2 = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
s1.grid(column=1, row=4)
s2.grid(column=1, row=5)
s2.set(255)

button_apply = tk.Button(root, text="Apply", command=stretch_contrast)
button_apply.grid(column=2, row=5, sticky="sw")

root.mainloop()
