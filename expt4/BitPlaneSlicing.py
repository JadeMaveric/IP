import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import numpy as np


def select_image():
    # grab a reference to the image panels
    global imageO, bit_planes

    #open a file selection dialog and allow the user to select an input image
    path =tk.filedialog.askopenfilename()

    #ensure a filepath was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Save a reference to the gray image
        grayImage = gray

        # convert the image to PIL format
        gray = Image.fromarray(gray)

        # ... and then to ImageTk format
        gray = ImageTk.PhotoImage(gray)


        # Display the image on the panel
        imageO.configure(image=gray)
        imageO.image = gray

        # Split the images
        for bit, label in enumerate(bit_planes):
            mask = 2**(bit+1)
            image = grayImage.copy()

            for x,y in np.ndindex(image.shape):
                pixel = image[x,y]
                image[x,y] = pixel & mask

            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            label.configure(image=image)
            label.image = image

# --- MAIN TKINTER STUFF ---

root = tk.Tk()

button = tk.Button(root, text="Load Image", command=select_image)
button.grid(column=1, row=0)

labelO = tk.Label(root, text="Original")
labelO.grid(column=0, row=0)
imageO = tk.Label(root, image=None)
imageO.grid(column=0, row=1)


image_labels = []
bit_num=0

for row in (2,4):
    for col in (0,1,2,3):
        label = tk.Label(root, text="Bit"+str(bit_num))
        label.grid(column=col, row=row)
        bit_num += 1
        image_labels.append(label)

bit_planes = []
bit_num = 0
for row in (3,5):
    for col in (0,1,2,3):
        label = tk.Label(root, image=None)
        label.grid(column=col, row=row)
        bit_num +=1
        bit_planes.append(label)


root.mainloop()
