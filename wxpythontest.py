
import wx

class TestFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(TestFrame, self).__init__(*args, **kw)


app = wx.App()
frame = wx.Frame(None, title = "hello world.")
frame.Show()
app.MainLoop()





