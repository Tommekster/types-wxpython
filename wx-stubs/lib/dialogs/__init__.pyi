# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class MultiMessageDialog(Dialog):
    """ A dialog like [`wx.MessageDialog`](wx.MessageDialog.html#wx.MessageDialog "wx.MessageDialog"), but with an optional 2nd message string
that is shown in a scrolled window, and also allows passing in the icon to
be shown instead of the stock error, question, etc. icons. The btnLabels
can be used if you’d like to change the stock labels on the buttons, it’s
a dictionary mapping stock IDs to label strings.


  


        Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
    """
    def __init__(self, parent, message, caption = "Message Box", msg2="", style = wx.OK | wx.CANCEL, pos = wx.DefaultPosition, icon=None, btnLabels=None) -> None:
        """ 

`__init__`(*self*, *parent*, *message*, *caption = "Message Box"*, *msg2=""*, *style = wx.OK | wx.CANCEL*, *pos = wx.DefaultPosition*, *icon=None*, *btnLabels=None*)[¶](#wx.lib.dialogs.MultiMessageDialog.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
        """

    def OnButton(self, evt) -> None:
        """ 

`OnButton`(*self*, *evt*)[¶](#wx.lib.dialogs.MultiMessageDialog.OnButton "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.dialogs.MultiMessageDialog.html
        """



class MultipleChoiceDialog(Dialog):
    """ Dialog()
Dialog(parent, id=ID\_ANY, title=””, pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_DIALOG\_STYLE, name=DialogNameStr)


A dialog box is a window with a title bar and sometimes a system menu,
which can be moved around the screen.


  


        Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *msg*, *title*, *lst*, *pos = wx.DefaultPosition*, *size = (200*, *200)*, *style = wx.DEFAULT\_DIALOG\_STYLE*)[¶](#wx.lib.dialogs.MultipleChoiceDialog.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.dialogs.MultipleChoiceDialog.GetValue "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """

    def GetValueString(self) -> None:
        """ 

`GetValueString`(*self*)[¶](#wx.lib.dialogs.MultipleChoiceDialog.GetValueString "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.dialogs.MultipleChoiceDialog.html
        """



class ScrolledMessageDialog(Dialog):
    """ Dialog()
Dialog(parent, id=ID\_ANY, title=””, pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_DIALOG\_STYLE, name=DialogNameStr)


A dialog box is a window with a title bar and sometimes a system menu,
which can be moved around the screen.


  


        Source: https://docs.wxpython.org/wx.lib.dialogs.ScrolledMessageDialog.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *msg*, *caption*, *pos=wx.DefaultPosition*, *size=(500*, *300)*, *style=wx.DEFAULT\_DIALOG\_STYLE*)[¶](#wx.lib.dialogs.ScrolledMessageDialog.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.dialogs.ScrolledMessageDialog.html
        """



