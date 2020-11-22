"Expt7: Image smoothening using Box, Median and Weighted Average"
import PIL.ImageFilter

def box(img):
    "Accepts an image, applies the box filter and returns the result"

    # Define the kernels
    boxKernel = PIL.ImageFilter.Kernel((3,3), (1,1,1,1,1,1,1,1,1), 9, 0)
    boxImg = img.filter(boxKernel) # Apply the kernels
    return boxImg

def median(img):
    "Accepts an image, applies the median filter and returns the result"

    medianKernel = PIL.ImageFilter.MedianFilter(3)
    medianImg = img.filter(medianKernel)
    return medianImg

def weightedAvg(img):
    "Accpets an image, applies the wieghted average filter and returns the result"

    wavgKernel = PIL.ImageFilter.Kernel((3,3), (1,2,1,2,4,2,1,2,1), 16, 0)
    wavgImage = img.filter(wavgKernel)
    return wavgImage
