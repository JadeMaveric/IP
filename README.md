# Image Processing
A collection image processing algorithms implemented in Python (numpy, pillow)
I had to implement these are part of my practical work. The GUI is build using wx-python

## Requirements
* Pillow - A popular image processing library
* Numpy - For when Pillow doesn't offer options, or I need to do something myself
* WxPython - The GUI, WxWidgets needs to be installed on the system

## Project Organisation
All the `expt*.py` files contain modular functions that accept a pillow image, process it and return the pillow image. These can used anywhere.  
`main.py` contains the driver code that builds the GUI and uses the `expt*.py` modules to process images.  
`convert.py` contains helpful uitlity fuctions to convert between WxBitmaps, WxImages and PillowImages
