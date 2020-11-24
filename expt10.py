"Given an input image, perform histogram equalization."

import numpy as np
import PIL.Image
from expt9 import histogram

def histogramEq(img):
    "Returns a histogram equalised image"
    source = img.split()
    equalisedSource = []
    for channel in source:
        hist = histogram(channel)['L']
        pdf = np.cumsum(hist)
        cdf = pdf / pdf[-1]
        greyLevel = np.round(cdf*255).astype('uint8')
        tempImage = channel.point(lambda i: greyLevel[i])
        equalisedSource.append(tempImage)

    if len(equalisedSource) == 1:
        return equalisedSource[0]
    elif len(equalisedSource) == 3:
        return PIL.Image.merge("RGB", equalisedSource)
    else:
        raise ValueError(f'Invalid dimensions for equalised image {len(equalisedSource)}')
