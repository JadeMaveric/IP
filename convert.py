"Wrapper library for converting between PIL image, wx.Bitmap and wx.Image"

import wx
from PIL import Image

def WxImageToPilImage( wx_image ):
    "Convert Wx Image to PIL Image"
    PilImage = Image.new('RGB', (wx_image.GetWidth(), wx_image.GetHeight()) )
    PilImage.frombytes( bytes(wx_image.GetData()) )
    return PilImage

def WxImageToWxBitmap( wx_image ):
    "Convert Wx Image to Wx Bitmap"
    return wx_image.ConvertToBitmap()


def PilImageToWxBitmap( pil_image ):
    "Convert PIL Image to Wx Bitmap"
    return WxImageToWxBitmap( PilImageToWxImage( pil_image ) )

def PilImageToWxImage( pil_image ):
    "Convert PIL Image to Wx Image"
    wxImage = wx.Image( pil_image.size[0], pil_image.size[1] )
    wxImage.SetData( pil_image.convert('RGB').tobytes() )
    return wxImage


def WxBitmapToPilImage( wx_bitmap ):
    "Convert Wx Bitmap to PIL Image"
    return WxImageToPilImage( WxBitmapToWxImage( wx_bitmap ) )

def WxBitmapToWxImage( wx_bitmap ):
    "Convert Wx Bitmap to Wx Image"
    return wx_bitmap.ConvertToImage()
