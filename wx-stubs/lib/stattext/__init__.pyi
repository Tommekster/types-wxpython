# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class GenStaticText(Control):
    """ [`GenStaticText`](#wx.lib.stattext.GenStaticText "wx.lib.stattext.GenStaticText") is a generic implementation of [`wx.StaticText`](wx.StaticText.html#wx.StaticText "wx.StaticText").


  


        Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
    """
    def __init__(self, parent, ID=-1, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="genstattext") -> None:
        """ 

`__init__`(*self*, *parent*, *ID=-1*, *label=""*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *name="genstattext"*)[¶](#wx.lib.stattext.GenStaticText.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([`wx.Window`](wx.Window.html#wx.Window "wx.Window")) – parent window, must not be `None`;
* **ID** (*integer*) – window identifier. A value of -1 indicates a default value;
* **label** (*string*) – the static text label (i.e., its text label);
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying [`wx.Control`](wx.Control.html#wx.Control "wx.Control") style;
* **name** (*string*) – the widget name.






            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def AcceptsFocus(self) -> None:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.lib.stattext.GenStaticText.AcceptsFocus "Permalink to this definition")
Can this window be given focus by mouse click?



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def Disable(self) -> None:
        """ 

`Disable`(*self*)[¶](#wx.lib.stattext.GenStaticText.Disable "Permalink to this definition")
Disables the control.



Returns
`True` if the window has been disabled, `False` if it had been
already disabled before the call to this function.





Note


This is functionally equivalent of calling [`Enable`](wx.Window.html#wx.Window.Enable "wx.Window.Enable")
with a `False` flag.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.stattext.GenStaticText.DoGetBestSize "Permalink to this definition")
Overridden base class virtual. Determines the best size of
the control based on the label size and the current font.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.stattext.GenStaticText.Enable "Permalink to this definition")
Enable or disable the widget for user input.



Parameters
**enable** (*bool*) – If `True`, enables the window for input. If
`False`, disables the window.



Returns
`True` if the window has been enabled or disabled,
`False` if nothing was done, i.e. if the window had already been
in the specified state.





Note


Note that when a parent window is disabled, all of its
children are disabled as well and they are re-enabled again when
the parent is.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def GetDefaultAttributes(self) -> None:
        """ 

`GetDefaultAttributes`(*self*)[¶](#wx.lib.stattext.GenStaticText.GetDefaultAttributes "Permalink to this definition")
Overridden base class virtual. By default we should use
the same font/colour attributes as the native [`wx.StaticText`](wx.StaticText.html#wx.StaticText "wx.StaticText").



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.stattext.GenStaticText.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`GenStaticText`](#wx.lib.stattext.GenStaticText "wx.lib.stattext.GenStaticText").



Parameters
**event** – a [`wx.EraseEvent`](wx.EraseEvent.html#wx.EraseEvent "wx.EraseEvent") event to be processed.





Note


This is intentionally empty to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.stattext.GenStaticText.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` for [`GenStaticText`](#wx.lib.stattext.GenStaticText "wx.lib.stattext.GenStaticText").



Parameters
**event** – a [`wx.PaintEvent`](wx.PaintEvent.html#wx.PaintEvent "wx.PaintEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.stattext.GenStaticText.SetFont "Permalink to this definition")
Sets the static text font and updates the control’s size to exactly
fit the label unless the control has `wx.ST_NO_AUTORESIZE` flag.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – a valid font instance, which will be the new font used
to display the text.






            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.lib.stattext.GenStaticText.SetLabel "Permalink to this definition")
Sets the static text label and updates the control’s size to exactly
fit the label unless the control has `wx.ST_NO_AUTORESIZE` flag.



Parameters
**label** (*string*) – the static text label (i.e., its text label).






            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """

    def ShouldInheritColours(self) -> None:
        """ 

`ShouldInheritColours`(*self*)[¶](#wx.lib.stattext.GenStaticText.ShouldInheritColours "Permalink to this definition")
Overridden base class virtual. If the parent has non-default
colours then we want this control to inherit them.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.stattext.GenStaticText.html
        """



EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

ST_NO_AUTORESIZE: int

