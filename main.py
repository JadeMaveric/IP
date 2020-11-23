"Driver for image processing experiments"
import os
import wx
from PIL import Image

import expt2
import expt3
import expt7
import expt8

import convert

class ImagePanel(wx.Panel):
    "Image plane"
    def __init__(self, parent, ID):
        wx.Panel.__init__(self, parent, ID)
        self.image = None
        self.bitmap = None
        self.original = None
        wx.EVT_PAINT(self, self.OnPaint)

    def display(self, pil_image):
        "Display an image"
        self.image = pil_image
        self.bitmap = convert.PilImageToWxBitmap(pil_image)
        self.Refresh(True)

    def OnPaint(self, _event):
        "@override Called whenever frame is painted"
        dc = wx.PaintDC(self)
        if self.bitmap:
            dc.DrawBitmap(self.bitmap, 0,0)
        elif self.image:
            self.bitmap = convert.PilImageToWxBitmap(self.image)
            dc.DrawBitmap(self.bitmap, 0,0)


class MyFrame(wx.Frame):
    "App window"
    def __init__(self, parent,  title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = ImagePanel(self, wx.ID_ANY)
        self.CreateStatusBar()
        self.dirname = ""
        self.filename = ""

        # Add a menubar, cause every app needs one
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)

        # Setting up the file menu
        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open an image file")
        menuReset = filemenu.Append(wx.ID_RESET, "Reset", "Reset open image")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Image Processing Experiments")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")

        menuBar.Append(filemenu, "File")

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnReset, menuReset)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Expt 2 menu
        expt2menu = wx.Menu()

        menuGray = expt2menu.Append(wx.ID_ANY, "Gray", "Convert image to grayscale")
        menuBar.Append(expt2menu, "Expt2")

        self.Bind(wx.EVT_MENU, self.OnGray, menuGray)
        self.Show()

        # Expt 2 menu
        expt3menu = wx.Menu()

        menuNegative = expt3menu.Append(wx.ID_ANY, "Negative", "Convert image to its negative")
        menuBar.Append(expt3menu, "Expt3")

        self.Bind(wx.EVT_MENU, self.OnNegative, menuNegative)
        self.Show()


        # Expt 7 menu
        expt7menu = wx.Menu()

        menuBox = expt7menu.Append(wx.ID_ANY, "Box", "Apply the Box operator")
        menuMedian = expt7menu.Append(wx.ID_ANY, "Median", "Apply the Median operator")
        menuWeightedAvg = expt7menu.Append(wx.ID_ANY, "Weighted Avg", "Apply a weighted avg filter")

        menuBar.Append(expt7menu, "Expt7")

        self.Bind(wx.EVT_MENU, self.OnBox, menuBox)
        self.Bind(wx.EVT_MENU, self.OnMedian, menuMedian)
        self.Bind(wx.EVT_MENU, self.OnWeightedAvg, menuWeightedAvg)
        self.Show(True)

        # Expt 8 menu
        expt8menu = wx.Menu()

        menuSobel = expt8menu.Append(wx.ID_ANY, "Sobel", "Apply the Sobel operator")
        menuPrewitt = expt8menu.Append(wx.ID_ANY, "Prewitt", "Apply the Prewitt operator")
        menuLaplacian = expt8menu.Append(wx.ID_ANY, "Laplacian", "Apply the Laplacian operator")

        menuBar.Append(expt8menu, "Expt8")

        self.Bind(wx.EVT_MENU, self.OnSobel, menuSobel)
        self.Bind(wx.EVT_MENU, self.OnPrewitt, menuPrewitt)
        self.Bind(wx.EVT_MENU, self.OnLaplacian, menuLaplacian)
        self.Show(True)

    # FILE MENU
    def OnOpen(self, _event):
        "File dialog box"
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            imagePath = os.path.join(self.dirname, self.filename)
            pilImage = Image.open(imagePath).convert("RGB") # Always use 3x8bit images
            self.control.display(pilImage)
            self.control.original = pilImage
        dlg.Destroy()

    def OnReset(self, _event):
        "Resets the current image"
        OriginalImage = self.control.original
        self.control.display(OriginalImage)

    def OnAbout(self, _event):
        "A message dialog with an OK button."
        dlg = wx.MessageDialog(self, "IP Experiments, 7th semester, GEC", "About IP Expts", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, _event):
        "Safely kill application"
        self.Close(True)

    # EXPT 2 MENU
    def OnGray(self, _event):
        "Convert current image to grayscale"
        PilImage = self.control.image
        GrayPilImage = expt2.gray(PilImage)
        self.control.display(GrayPilImage)

    # EXPT 2 MENU
    def OnNegative(self, _event):
        "Convert current image to its negative"
        PilImage = self.control.image
        NegativePilImage = expt3.negative(PilImage)
        self.control.display(NegativePilImage)

    # EXPT 7 MENU
    def OnBox(self, _event):
        "Grab the current image, apply Box operator, display"
        PilImage = self.control.image
        EdgePilImage = expt7.box(PilImage)
        self.control.display(EdgePilImage)

    def OnMedian(self, _event):
        "Grab current image, apply Median, display"
        PilImage = self.control.image
        EdgePilImage = expt7.median(PilImage)
        self.control.display(EdgePilImage)

    def OnWeightedAvg(self, _event):
        "Grab curent image, apply weighted average, display"
        PilImage = self.control.image
        EdgePilImage = expt7.weightedAvg(PilImage)
        self.control.display(EdgePilImage)

    # EXPT 8 MENU
    def OnSobel(self, _event):
        "Grab the current image, apply sobel operator, display"
        PilImage = self.control.image
        EdgePilImage = expt8.sobel(PilImage)
        self.control.display(EdgePilImage)

    def OnPrewitt(self, _event):
        "Grab current image, apply prewitt, display"
        PilImage = self.control.image
        EdgePilImage = expt8.sobel(PilImage)
        self.control.display(EdgePilImage)

    def OnLaplacian(self, _event):
        "Grab curent image, apply laplacian, display"
        PilImage = self.control.image
        EdgePilImage = expt8.laplacian(PilImage)
        self.control.display(EdgePilImage)


app = wx.App(False)
frame = MyFrame(None, 'IP Expts')
app.MainLoop()
