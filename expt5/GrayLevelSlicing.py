import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import numpy as np


def select_image():
    # grab a reference to the image panels
    global panelA, grayImage

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
        # First initialise it if its not ready
        if panelA is None:
            panelA = tk.Label(image=gray)
            panelA.image = gray
            panelA.grid(column=0, row=6)

        else:
            panelA.configure(image=gray)
            panelA.image = gray

def apply_filter():
    global grayImage, panelB, sliderA, sliderB, sliderC, keepBG

    if grayImage is None:
        return

    a = sliderA.get()
    b = sliderB.get()
    c = sliderC.get()
    image = grayImage.copy()

    for x,y in np.ndindex(image.shape):
        pixel = image[x,y]
        if a <= pixel <= b:
            image[x,y] = c
        elif bool(keepBG.get()):
            image[x,y] = 0 #Erase background by turning it black

    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    if panelB is None:
        panelB = tk.Label(image=image)
        panelB.image = image
        panelB.grid(column=1, row=6)
    else:
        panelB.configure(image=image)
        panelB.image = image

# --- MAIN TKINTER STUFF ---

root = tk.Tk()
panelA = None
panelB = None
grayImage = None

keepBG = tk.IntVar()


buttonA = tk.Button(root, text="Select an image", command=select_image)
buttonB = tk.Button(root, text="Apply filter", command=apply_filter)
buttonA.grid(column=1, row=0)
buttonB.grid(column=2, row=0)


labelA = tk.Label(root, text="min")
labelB = tk.Label(root, text="max")
labelC = tk.Label(root, text="replace")
labelA.grid(column=0, row=1)
labelB.grid(column=0, row=2)
labelC.grid(column=0, row=3)

labelD = tk.Label(root, text="Original")
labelE = tk.Label(root, text="Filtered")
labelD.grid(column=0, row=5)
labelE.grid(column=1, row=5)


sliderA = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
sliderB = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
sliderC = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL)
sliderA.grid(column=1, row=1)
sliderB.grid(column=1, row=2)
sliderC.grid(column=1, row=3)

checkbtn =tk.Checkbutton(root, text="Remove background", variable=keepBG)
checkbtn.grid(column=1, row=4)

root.mainloop()