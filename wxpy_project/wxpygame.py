import wxcommon
import wx

import sys
sys.path.append('/Users/zhangxian/program/python/python test/pygame/')
#from pygame import pygameInterface
import alphabet


# Next, create an application object.

class MainFrame(wx.Frame):
    #scoreText = 0
    #scoreValue = {}
    def __init__(self, parent, title):
        wx.Frame.__init__(self, None, title= title, size = (600, 700))

        self.pnl = wx.Panel(self)

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ABOUT)
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_EXIT, u"exit", u"exit")

        helpMenu = wx.Menu()
        helpMenu.Append(wx.ID_ABOUT)
        helpMenu.AppendSeparator()
        helpMenu.Append(wx.ID_EXIT, u"exit", u"exit")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        #frm.Show()
        startButton = wx.Button(self.pnl, label = "start game", pos = (60, 60))
        #startButton = wx.Button(pnl, label = "start game")

        self.Bind(wx.EVT_BUTTON, self.ShowBox, startButton)

        scoreButton = wx.Button(self.pnl, label = "score", pos = (60, 90))
        #startButton = wx.Button(pnl, label = "start game")

        self.Bind(wx.EVT_BUTTON, self.UpdateScoreValue, scoreButton)

        self.scoreText = wx.TextCtrl(self.pnl,value = "score is: ", pos = (60, 120),\
            size = (150, 100),style = wx.TE_MULTILINE | wx.HSCROLL)

        self.scoreValue = {'right': 0, 'wrong':0}
        #self.Bind(wx.EVT_CLOSE, self.UpdateScoreValue)
    
    def ShowBox(self, e):
        #wx.MessageBox("start alphabet game!!!!")
        alphabet.StartAlphabetGame(self.scoreValue)
        if self.scoreValue['right'] > 0:
            self.UpdateScoreValueTest()
        else:
            self.UpdateScoreValueTest()
    
    def UpdateScoreValueTest():
        scoreInfo = "right is : " + str(self.scoreValue['right'])
        scoreInfo = "wrong is : " + str(self.scoreValue['wrong'])
        #self.scoreText.value = ''
        #self.scoreText = wx.TextCtrl(self.pnl,value = scoreInfo)
        self.scoreText.WriteText("\n right score is : " + str(self.scoreValue['right']))
        self.scoreText.WriteText("\n wrong score is : " + str(self.scoreValue['wrong']))
        #self.scoreText.flush()

    def UpdateScoreValue(self, e):
        scoreInfo = "right is : " + str(self.scoreValue['right'])
        scoreInfo = "wrong is : " + str(self.scoreValue['wrong'])
        #self.scoreText.value = ''
        #self.scoreText = wx.TextCtrl(self.pnl,value = scoreInfo)
        self.scoreText.WriteText("\n right input is : " + str(self.scoreValue['right']))
        self.scoreText.WriteText("\n wrong input is : " + str(self.scoreValue['wrong']))
        scores = (self.scoreValue['right']*100)//(self.scoreValue['right'] + self.scoreValue['wrong'])
        self.scoreText.WriteText("\n score is : " + str(scores))
        self.scoreText.flush()


app = wx.App()  
frm = MainFrame(None, "hell world.")
# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()


