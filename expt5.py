"Expt 5: Implement Bit plane slicing as explained. Include all 8 plane outputs."

def bitplane(img, plane):
    "Returns the specified bitplane of the image"
    assert 0 <= plane <= 7
    planeImg = img.point(lambda i: i & 2**plane or (255 if plane < 6 else 0))
    return planeImg

def allBitplanes(img):
    "Returns all the bitplanes of the image"
    bitplanes = [img.point(lambda i: i & 2**p or (255 if p < 6 else 0)) for p in range(8)]
    return bitplanes
