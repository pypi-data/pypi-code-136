"""
This is a minimal wxPython SplashScreen
"""

from os.path import dirname, join
import wx
from   wx.adv import SplashScreen as SplashScreen,SPLASH_CENTRE_ON_SCREEN,SPLASH_TIMEOUT

class WolfLauncher(SplashScreen):
    """
    Wolf Splashcreen
    """    
    def __init__(self, parent=None):

        mybitmap = wx.Bitmap(name=join(dirname(__file__),".\\WolfPython.png"), type=wx.BITMAP_TYPE_PNG)
        mask = wx.Mask(mybitmap, wx.Colour(255,0,204))
        mybitmap.SetMask(mask)
        splash = SPLASH_CENTRE_ON_SCREEN | SPLASH_TIMEOUT
        duration = 3000 # milliseconds

        # Call the constructor with the above arguments
        # in exactly the following order.
        super(WolfLauncher, self).__init__(bitmap=mybitmap,
                                            splashStyle=splash,
                                            milliseconds=duration,
                                            parent=None,
                                            id=-1,
                                            pos=wx.DefaultPosition,
                                            size=wx.DefaultSize,
                                            style=wx.STAY_ON_TOP |
                                                    wx.BORDER_NONE)

        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.CenterOnScreen(wx.BOTH)
        self.Show()
        

    def OnExit(self, event):
        # The program will freeze without this line.
        event.Skip()  # Make sure the default handler runs too...
        self.Hide()
