"Write a program to obtain Histogram of an image"

import numpy as np
import PIL.Image

def histogram(img):
    "Returns the histogram of the image. Each channel has an array stored in a dictionary"
    rawHist = np.array(img.histogram())
    # img.histogram builds a simple 256 sized array, each cell has the count of pixels
    # with the index as its value. While this is trivial to implement with a simple
    # for loop, the inbuilt function is much faster.
    # If there are multiple channels, the arrays are simply concatenated together
    hist = {}
    if len(rawHist) == 256:
        # Monochrome image
        hist['L'] = rawHist
    elif len(rawHist) == 768:
        hist['R'] = rawHist[000:256]
        hist['G'] = rawHist[256:512]
        hist['B'] = rawHist[512:768]

    return hist

def histogramImage(img):
    "Creates a histogram plot"
    hist = histogram(img)
    histMax = max([max(hist[key]) for key in hist])
    histImg = None

    if len(hist) == 1:
        array = [[255]*i + [0]*(histMax-i) for i in hist['L']]
        npArr = np.asarray(array).astype('uint8')
        histImg = PIL.Image.fromarray(npArr).transpose(PIL.Image.ROTATE_90)

    elif len(hist) == 3:
        Ra = [[255]*i + [0]*(histMax-i) for i in hist['R']]
        Ga = [[255]*i + [0]*(histMax-i) for i in hist['G']]
        Ba = [[255]*i + [0]*(histMax-i) for i in hist['B']]

        Rn = np.asarray(Ra).astype('uint8')
        Gn = np.asarray(Ga).astype('uint8')
        Bn = np.asarray(Ba).astype('uint8')

        Ri = PIL.Image.fromarray(Rn).transpose(PIL.Image.ROTATE_90)
        Gi = PIL.Image.fromarray(Gn).transpose(PIL.Image.ROTATE_90)
        Bi = PIL.Image.fromarray(Bn).transpose(PIL.Image.ROTATE_90)

        histImg = PIL.Image.merge('RGB', (Ri, Gi, Bi))

    return histImg
