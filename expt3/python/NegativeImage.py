import cv2
import numpy as np


def select_image():
    global image0, image1

    path = tk.filedialog.askopenfilename()

    if len(path) > 0:
        img = cv2.imread(path)
        neg = np.zeros(img.shape, dtype=img.dtype)
        neg += 255
        neg -= img
        #neg = img.copy()

        #height, width, _ = neg.shape
        #for x,y in np.ndindex((height,width)):
        #    pixel = neg[x,y]
        #    pixel[0] = 255 - pixel[0]
        #    pixel[1] = 255 - pixel[1]
        #    pixel[2] = 255 - pixel[2]
        #    neg[x,y] = pixel

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        image0.configure(image=img)
        image0.image = img

        neg = cv2.cvtColor(neg, cv2.COLOR_BGR2RGB)
        neg = Image.fromarray(neg)
        neg = ImageTk.PhotoImage(neg)
        image1.configure(image=neg)
        image1.image = neg



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