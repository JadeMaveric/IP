"Find the negative of an image"

def negative(img):
    "Returns the negative of an image"
    neg = img.point(lambda i: 255 - i)
    return neg
