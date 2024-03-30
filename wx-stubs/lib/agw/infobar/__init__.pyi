# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class AutoWrapStaticText(GenStaticText):
    """ A simple class derived from `lib.stattext` that implements auto-wrapping
behaviour depending on the parent size.



New in version 0.9.5.



  


        Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
    """
    def __init__(self, parent, label) -> None:
        """ 

`__init__`(*self*, *parent*, *label*)[¶](#wx.lib.agw.infobar.AutoWrapStaticText.__init__ "Permalink to this definition")
Defsult class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – a subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window"), must not be `None`;
* **label** (*string*) – the [`AutoWrapStaticText`](#wx.lib.agw.infobar.AutoWrapStaticText "wx.lib.agw.infobar.AutoWrapStaticText") text label.






            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.infobar.AutoWrapStaticText.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AutoWrapStaticText`](#wx.lib.agw.infobar.AutoWrapStaticText "wx.lib.agw.infobar.AutoWrapStaticText").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def SetLabel(self, label, wrapped=False) -> None:
        """ 

`SetLabel`(*self*, *label*, *wrapped=False*)[¶](#wx.lib.agw.infobar.AutoWrapStaticText.SetLabel "Permalink to this definition")
Sets the [`AutoWrapStaticText`](#wx.lib.agw.infobar.AutoWrapStaticText "wx.lib.agw.infobar.AutoWrapStaticText") label.


All “&” characters in the label are special and indicate that the following character is
a mnemonic for this control and can be used to activate it from the keyboard (typically
by using `Alt` key in combination with it). To insert a literal ampersand character, you
need to double it, i.e. use “&&”. If this behaviour is undesirable, use `SetLabelText` instead.



Parameters
* **label** (*string*) – the new [`AutoWrapStaticText`](#wx.lib.agw.infobar.AutoWrapStaticText "wx.lib.agw.infobar.AutoWrapStaticText") text label;
* **wrapped** (*bool*) – `True` if this method was called by the developer using [`SetLabel`](#wx.lib.agw.infobar.AutoWrapStaticText.SetLabel "wx.lib.agw.infobar.AutoWrapStaticText.SetLabel"),
`False` if it comes from the [`OnSize`](#wx.lib.agw.infobar.AutoWrapStaticText.OnSize "wx.lib.agw.infobar.AutoWrapStaticText.OnSize") event handler.





Note


Reimplemented from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """

    def Wrap(self, width: int) -> None:
        """ 

`Wrap`(*self*, *width*)[¶](#wx.lib.agw.infobar.AutoWrapStaticText.Wrap "Permalink to this definition")
This functions wraps the controls label so that each of its lines becomes at
most *width* pixels wide if possible (the lines are broken at words boundaries
so it might not be the case if words are too long).


If *width* is negative, no wrapping is done.



Parameters
**width** (*integer*) – the maximum available width for the text, in pixels.





Note


Note that this *width* is not necessarily the total width of the control,
since a few pixels for the border (depending on the controls border style) may be added.





            Source: https://docs.wxpython.org/wx.lib.agw.infobar.AutoWrapStaticText.html
        """



EVT_SIZE: int

