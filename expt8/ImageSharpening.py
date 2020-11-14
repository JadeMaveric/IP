import os
import wx

class MyFrame(wx.Frame):

    def __init__(self, parent,  title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        self.dirname = ""
        self.filename = ""

        # Setting up the menu
        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", " Open an image file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", " Add stuff ")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)


    def OnOpen(self, _event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            textFile = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(textFile.read())
            textFile.close()
        dlg.Destroy()

    def OnAbout(self, _event):
        # A message dialog with an OK button.
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, _event):
        self.Close(True)


app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()
