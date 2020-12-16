"Apply grayscale erosion to the image"

# import numpy as np
import PIL.Image
import PIL.ImageFilter
from expt2 import gray

def grayScaleErosion(img):
    "Returns the grayscale eroded version of the image"
    grayImg = gray(img)
    eroImg = grayImg.filter(PIL.ImageFilter.MinFilter(3))
    return eroImg
    # "The numpy stuff works, but is incredibly slow"
    # "using MinFilter is a much faster `approximation`"
    # npImg = np.asarray(grayImg)
    # kernel = [
    #     [0,1,0],
    #     [1,1,1],
    #     [0,1,0]
    # ]

    # width = npImg.shape[1] - 2
    # height = npImg.shape[0] - 2
    # eroNpImg = np.zeros((height, width))
    # for x,y in np.ndindex((height, width)):
    #     value = float('inf')
    #     for ox, oy in np.ndindex((3,3)):
    #         value = min(value, npImg[x+ox][y+oy] - kernel[ox][oy])
    #     eroNpImg[x][y] = value

    # eroImg = PIL.Image.fromarray(eroNpImg.astype('uint8'))
    # return eroImg
