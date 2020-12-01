"""implement optimal thresholding to find the threshold for segmentation.
Output should be binary image. Also display the threshold obtained."""
import numpy as np
import PIL.Image
from expt2 import gray

def optimalThreshold(img):
    "Returns the optimal threshold value"
    grayImg = gray(img)
    npImg = np.asarray(grayImg)
    numPixels = npImg.size
    sumPixels = np.sum(npImg)

    t_0 = sumPixels / numPixels
    t_k = 0
    while abs(t_k-t_0) > 0.0001:
        t_0 = t_k or t_0
        o_1 = npImg[npImg < t_0]
        o_2 = npImg[npImg >= t_0]

        t_1 = len(o_1) and (np.sum(o_1) / len(o_1))
        t_2 = len(o_2) and (np.sum(o_2) / len(o_2))
        t_k = (t_1 + t_2) / 2

    return t_0

def makeMono(img, threshold):
    "Returns a monocoloured (binary) image based on the given threshold"
    grayImg = gray(img)
    npImg = np.asarray(grayImg)
    imgArr = npImg.reshape(npImg.size)

    threshImg = [0 if pixel < threshold else 255 for pixel in imgArr]
    threshImg = np.array(threshImg).astype('uint8').reshape(npImg.shape)
    threshImg = PIL.Image.fromarray(threshImg)

    return threshImg

def makeOptimalMono(img):
    "Calls makeMono() with the optimal threshold value"
    threshold = optimalThreshold(img)
    threshImg = makeMono(img, threshold)
    return threshImg
