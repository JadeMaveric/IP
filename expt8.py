"Expt8: Image sharpening using Laplacian, sobel and prewitt"
import numpy as np
import PIL.Image
import PIL.ImageFilter

def sobel(img):
    "Accepts an image, applies the sobel filter and returns the result"

    # Define the kernels
    horizontal = PIL.ImageFilter.Kernel((3,3), (-1,0,1,-2,0,2,-1,0,1), 1, 0)
    vertical = PIL.ImageFilter.Kernel((3,3), (-1,-2,-1,0,0,0,1,2,1), 1, 0)

    # Apply the kernels
    horizontalGrad = img.filter(horizontal)
    verticalGrad = img.filter(vertical)

    # Edge magnitude
    npHorz = np.asarray(horizontalGrad).astype('float')
    npVert = np.asarray(verticalGrad).astype('float')
    npEdge = np.sqrt( npHorz*npHorz + npVert*npVert )

    edgeGrad = PIL.Image.fromarray(npEdge.astype('uint8'))

    return edgeGrad

def prewitt(img):
    "Accepts an image, applies the prewitt filter and returns the result"

    horizontal = PIL.ImageFilter.Kernel((3,3), (-1,0,1,-1,0,1,-1,0,1), 1, 0)
    vertical = PIL.ImageFilter.Kernel((3,3), (-1,-1,-1,0,0,0,1,1,1), 1, 0)

    horizontalGrad = img.filter(horizontal)
    verticalGrad = img.filter(vertical)

    npHorz = np.asarray(horizontalGrad).astype('float')
    npVert = np.asarray(verticalGrad).astype('float')
    npEdge = np.sqrt( npHorz*npHorz + npVert*npVert )

    edgeGrad = PIL.Image.fromarray(npEdge.astype('uint8'))

    return edgeGrad

def laplacian(img):
    "Accpets an image, applies the laplacian filter and returns the result"

    laplace = PIL.ImageFilter.Kernel((3,3), (-1,-1,-1,-1,8,-1,-1,-1,-1), 1, 0)

    edgedImage = img.filter(laplace)
    
    return edgedImage
