import wx

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 255,166 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter ??", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.response = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.response, 0, wx.ALL, 5 )

        self.mybutton = wx.Button( self, wx.ID_ANY, u"Press Me", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.mybutton, 0, wx.ALL, 5 )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.result = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.result, 1, wx.ALL|wx.EXPAND, 5 )


        gSizer1.Add( bSizer1, 1, wx.EXPAND, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.mybutton.Bind( wx.EVT_BUTTON, self.showres )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def showres( self, event ):
        resp = self.response.GetValue()
        if resp =='A':
            self.result.SetValue('Hello you are John')
        elif resp =='B':
            self.result.SetValue('Hello you are brain')
        else:
            self.result.SetValue('ID not matched')

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()

