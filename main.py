"Driver for image processing experiments"
import os
import wx
from PIL import Image

import expt2
import expt3
import expt5
import expt7
import expt8
import expt9
import expt10
import expt11
import expt12

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


class PreviewFrame(wx.Frame):
    "Temporary preview window"
    def __init__(self, parent, title, images):
        wx.Frame.__init__(self,parent, title=title)
        self.control = ImagePanel(self, wx.ID_ANY)
        self.images = images
        self.index = 0

        self.control.display(self.images[0])
        self.control.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.control.SetFocus()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText(
            f'[{self.index+1}/{len(self.images)}] Use left/right arrow keys to cycle between images'
        )

        self.Show(True)

    def OnKeyDown(self, event):
        "Handle keypresses for left/right arrow keys"
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_LEFT:
            self.index -= 1 if self.index > 0 else 0
            self.control.display(self.images[self.index])
        elif keycode == wx.WXK_RIGHT:
            self.index += 1 if self.index < len(self.images)-1 else 0
            self.control.display(self.images[self.index])
        else:
            event.Skip()
        self.statusbar.SetStatusText(
            f'[{self.index+1}/{len(self.images)}] Use left/right arrow keys to cycle between images'
        )

class MyFrame(wx.Frame):
    "App window"
    def __init__(self, parent,  title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = ImagePanel(self, wx.ID_ANY)
        self.statusbar = self.CreateStatusBar()
        self.dirname = ""
        self.filename = ""

        # Add a menubar, cause every app needs one
        menuBar = wx.MenuBar()
        self.SetMenuBar(menuBar)

        # File Menu (Expt 1)
        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open an image file")
        menuSaveAs = filemenu.Append(wx.ID_SAVE, "Save As", "Save an image")
        menuReset = filemenu.Append(wx.ID_RESET, "Reset", "Reset open image")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Image Processing Experiments")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")

        menuBar.Append(filemenu, "File")

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnReset, menuReset)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Expt 2 menu
        expt2menu = wx.Menu()

        menuGray = expt2menu.Append(wx.ID_ANY, "Gray", "Convert image to grayscale")
        menuBar.Append(expt2menu, "Expt2")

        self.Bind(wx.EVT_MENU, self.OnGray, menuGray)
        self.Show()

        # Expt 3 menu
        expt3menu = wx.Menu()

        menuNegative = expt3menu.Append(wx.ID_ANY, "Negative", "Convert image to its negative")
        menuBar.Append(expt3menu, "Expt3")

        self.Bind(wx.EVT_MENU, self.OnNegative, menuNegative)
        self.Show()

        # Expt 5 menu
        expt5menu = wx.Menu()
        bitplanemenu = wx.Menu()

        previewPlanes = expt5menu.Append(wx.ID_ANY, "Preview all", "Show all bitplanes together")
        bitPlanes = [
            bitplanemenu.Append(wx.ID_ANY, f'Bit {p}', f'Isolate bit plane {p}') for p in range(8)
        ]

        expt5menu.AppendMenu(wx.ID_ANY, "Bit Planes", bitplanemenu, "Display/preview bitplanes")
        menuBar.Append(expt5menu, "Expt5")

        self.Bind(wx.EVT_MENU, self.OnBitPlanePreview, previewPlanes)
        for p in range(8):
            self.Bind(wx.EVT_MENU, self.OnBitPlane(p), bitPlanes[p])
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

        # Expt 9 menu
        expt9menu = wx.Menu()

        menuHist = expt9menu.Append(wx.ID_ANY, "Histogram", "Open the histogram in a preview pane")

        menuBar.Append(expt9menu, "Expt9")

        self.Bind(wx.EVT_MENU, self.OnHistogram, menuHist)
        self.Show(True)

        # Expt 10 menu
        expt10menu = wx.Menu()

        menuHistEq = expt10menu.Append(wx.ID_ANY, "Histogram EQ", "Equalise the image")

        menuBar.Append(expt10menu, "Expt10")

        self.Bind(wx.EVT_MENU, self.OnHistogramEq, menuHistEq)

        # Expt 11 menu
        expt11menu = wx.Menu()

        menuMakeOptimalMono = \
        expt11menu.Append(wx.ID_ANY, "Make Optimal Mono", "Make binary img using optimal threshold")

        menuBar.Append(expt11menu, "Expt11")

        self.Bind(wx.EVT_MENU, self.OnMakeOptimalMono, menuMakeOptimalMono)

        # Expt 12 menu
        expt12menu = wx.Menu()

        menuGrayScaleErosion = \
        expt12menu.Append(wx.ID_ANY, "Gray Scale Erosion", "Convert image to grayscale & apply GSE")

        menuBar.Append(expt12menu, "Expt 12")

        self.Bind(wx.EVT_MENU, self.OnGrayScaleErosion, menuGrayScaleErosion)

    # FILE MENU
    def OnOpen(self, _event):
        "File dialog box"
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "",
            wildcard="ALL files (*.*)|*.*|JPEG files (*.jpg)|*.jpg|PNG files (*.png)|*.png",
            style=wx.FD_OPEN
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            imagePath = os.path.join(self.dirname, self.filename)
            pilImage = Image.open(imagePath).convert("RGB") # Always use 3x8bit images
            self.control.display(pilImage)
            self.control.original = pilImage
        dlg.Destroy()

    def OnSaveAs(self, _event):
        "Save as dialog box"
        dlg = wx.FileDialog(self, "Save image", self.dirname,
            wildcard="ALL files (*.*)|*.*|JPEG files (*.jpg)|*.jpg|PNG files (*.png)|*.png",
            style=wx.FD_SAVE
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            imagePath = os.path.join(self.dirname, self.filename)
            pilImage = self.control.image
            pilImage.save(imagePath)

    def OnReset(self, _event):
        "Resets the current image"
        OriginalImage = self.control.original
        self.control.display(OriginalImage)
        self.statusbar.SetStatusText('')

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

    # EXPT 3 MENU
    def OnNegative(self, _event):
        "Convert current image to its negative"
        PilImage = self.control.image
        NegativePilImage = expt3.negative(PilImage)
        self.control.display(NegativePilImage)

    # EXPT 5 MENU
    def OnBitPlanePreview(self, _event):
        "Preview all bitplanes in a new windows"
        PilImg = self.control.image
        bitplanes = expt5.allBitplanes(PilImg)
        preview = PreviewFrame(self, "Bit Plane Previews", bitplanes)
        preview.Show()

    def OnBitPlane(self, plane):
        "Construct a bitplane handler for the specified bitplane"
        root = self # The main window
        def _onBitPlane(_self):
            "Slice the current image to the specified bitplane"
            PilImage = root.control.image
            BitplaneImage = expt5.bitplane(PilImage, plane)
            root.control.display(BitplaneImage)
        return _onBitPlane

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
        "Grab current image, apply laplacian, display"
        PilImage = self.control.image
        EdgePilImage = expt8.laplacian(PilImage)
        self.control.display(EdgePilImage)

    # EXPT 9 MENU
    def OnHistogram(self, _event):
        "Grab current image, calculate histogram, show in preview window"
        PilImage = self.control.image
        hist = expt9.histogramImage(PilImage)
        hist = hist.resize((400,300))

        if hist.mode == 'RGB':
            R,G,B = hist.split()
            preview = PreviewFrame(self, "Histogram Preview", (hist,R,G,B))
            preview.Show()
        else:
            preview = PreviewFrame(self, "Histogram Preview", [hist])
            preview.Show()

    # EXPT 10 MENU
    def OnHistogramEq(self, _event):
        "Grab current image, perform histogram EQ and display"
        PilImage = self.control.image
        HistEqImage = expt10.histogramEq(PilImage)
        self.control.display(HistEqImage)

    # EXPT 11 MENU
    def OnMakeOptimalMono(self, _event):
        "Grab current image, replace with optimal binary image"
        PilImage = self.control.image
        OptimalMonoImg = expt11.makeOptimalMono(PilImage)
        self.control.display(OptimalMonoImg)

        OptimalThreshold = expt11.optimalThreshold(PilImage)
        self.statusbar.SetStatusText(f'Optimal Threshold: {OptimalThreshold}')

    # EXPT 12 MENU
    def OnGrayScaleErosion(self, _event):
        "Grab current image, replace with gray scale eroded image"
        PilImage = self.control.image
        ErodedImg = expt12.grayScaleErosion(PilImage)
        self.control.display(ErodedImg)


app = wx.App(False)
frame = MyFrame(None, 'IP Expts')
app.MainLoop()
