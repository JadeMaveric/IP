import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import numpy as np

def select_image():
    # grab a reference to the image panel
    global imageO, image1, image2, image3, grayImage

    #open a file selection dialog and allow the user to select an input image
    path = tk.filedialog.askopenfilename()

    #ensure a filepath was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale
        image = cv2.imread(path)
        _gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        grayImage = _gray

        # Calculate Neighbours
        print("Calculating Neighbours")
        h,w = _gray.shape
        n = np.zeros(h*w*3*3)
        n = n.reshape((h,w,3,3))
        for x,y in np.ndindex(_gray.shape):
            for i,j in np.ndindex((3,3)):
                _x,_y = x+i-1, y+j-1
                if 0<=_x<h and 0<=_y<w:
                    n[x,y,i,j] = _gray[_x,_y]

        # Original Image
        print("Processing Original Image")
        gray = Image.fromarray(_gray)
        gray = ImageTk.PhotoImage(gray)
        imageO.configure(image=gray)
        imageO.image = gray

        # Average Filter
        print("Processing Box Filter")
        box = _gray.copy()
        for x,y in np.ndindex(box.shape):
            p = np.sum(n[x,y]) / 9
            box[x,y] = p
        box = Image.fromarray(box)
        box = ImageTk.PhotoImage(box)
        image1.configure(image=box)
        image1.image = box

        # Median Filter
        print("Processing Median Filter")
        med = _gray.copy()
        for x,y in np.ndindex(med.shape):
            p = np.median(n[x,y])
            med[x,y] = p
        med = Image.fromarray(med)
        med = ImageTk.PhotoImage(med)
        image2.configure(image=med)
        image2.image = med

        # Weighted Average
        print("Processing Weighted Average Filter")
        wavg = _gray.copy()
        k = np.array([1,2,1,2,4,2,1,2,1], dtype=int).reshape((3,3))
        for x,y in np.ndindex(wavg.shape):
            p = n[x,y]*k
            wavg[x,y] = np.sum(p)/np.sum(k)
        wavg = Image.fromarray(wavg)
        wavg = ImageTk.PhotoImage(wavg)
        image3.configure(image=wavg)
        image3.image = wavg


# --- MAIN TKINTER STUFF ---

root = tk.Tk()

grayImage = []

button_load = tk.Button(root, text="Load Image", command=select_image)
button_load.grid(column=1, row=0, sticky="sw")

labelO = tk.Label(root, text="Original")
labelO.grid(column=1, row=1)
imageO = tk.Label(root, image=None, padx=10)
imageO.grid(column=1, row=2)

label1 = tk.Label(root, text="Average/Box")
label1.grid(column=2, row=1)
image1 = tk.Label(root, image=None)
image1.grid(column=2, row=2)

label2 = tk.Label(root, text="Median")
label2.grid(column=1, row=3)
image2 = tk.Label(root, image=None)
image2.grid(column=1, row=4)

label3 = tk.Label(root, text="Weighted Avg")
label3.grid(column=2, row=3)
image3 = tk.Label(root, image=None)
image3.grid(column=2, row=4)

root.mainloop()
