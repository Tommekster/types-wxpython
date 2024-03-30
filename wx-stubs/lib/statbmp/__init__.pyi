# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class GenStaticBitmap(Control):
    """ [`GenStaticBitmap`](#wx.lib.statbmp.GenStaticBitmap "wx.lib.statbmp.GenStaticBitmap") is a generic implementation of [`wx.StaticBitmap`](wx.StaticBitmap.html#wx.StaticBitmap "wx.StaticBitmap").


  


        Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
    """
    def __init__(self, parent, ID, bitmap, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, name = "genstatbmp") -> None:
        """ 

`__init__`(*self*, *parent*, *ID*, *bitmap*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = 0*, *name = "genstatbmp"*)[¶](#wx.lib.statbmp.GenStaticBitmap.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([`wx.Window`](wx.Window.html#wx.Window "wx.Window")) – parent window, must not be `None`;
* **ID** (*integer*) – window identifier. A value of -1 indicates a default value;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the static bitmap used in the control;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying [`wx.Control`](wx.Control.html#wx.Control "wx.Control") style;
* **name** (*string*) – the widget name.






            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def AcceptsFocus(self) -> None:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.lib.statbmp.GenStaticBitmap.AcceptsFocus "Permalink to this definition")
Can this window be given focus by mouse click?



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.statbmp.GenStaticBitmap.DoGetBestSize "Permalink to this definition")
Overridden base class virtual. Determines the best size of
the control based on the label size and the current font.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.lib.statbmp.GenStaticBitmap.GetBitmap "Permalink to this definition")
Returns the bitmap currently used in the control.



Return type
[wx.Bitmap](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")





See also


[`SetBitmap`](#wx.lib.statbmp.GenStaticBitmap.SetBitmap "wx.lib.statbmp.GenStaticBitmap.SetBitmap")





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def GetDefaultAttributes(self) -> None:
        """ 

`GetDefaultAttributes`(*self*)[¶](#wx.lib.statbmp.GenStaticBitmap.GetDefaultAttributes "Permalink to this definition")
Overridden base class virtual. By default we should use
the same font/colour attributes as the native `StaticBitmap`.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.statbmp.GenStaticBitmap.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`GenStaticBitmap`](#wx.lib.statbmp.GenStaticBitmap "wx.lib.statbmp.GenStaticBitmap").



Parameters
**event** – a [`wx.EraseEvent`](wx.EraseEvent.html#wx.EraseEvent "wx.EraseEvent") event to be processed.





Note


This is intentionally empty to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.statbmp.GenStaticBitmap.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` for [`GenStaticBitmap`](#wx.lib.statbmp.GenStaticBitmap "wx.lib.statbmp.GenStaticBitmap").



Parameters
**event** – a [`wx.PaintEvent`](wx.PaintEvent.html#wx.PaintEvent "wx.PaintEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def SetBitmap(self, bitmap: 'Bitmap') -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.lib.statbmp.GenStaticBitmap.SetBitmap "Permalink to this definition")
Sets the bitmap label.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new bitmap.





See also


[`GetBitmap`](#wx.lib.statbmp.GenStaticBitmap.GetBitmap "wx.lib.statbmp.GenStaticBitmap.GetBitmap")





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """

    def ShouldInheritColours(self) -> None:
        """ 

`ShouldInheritColours`(*self*)[¶](#wx.lib.statbmp.GenStaticBitmap.ShouldInheritColours "Permalink to this definition")
Overridden base class virtual. If the parent has non-default
colours then we want this control to inherit them.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.statbmp.GenStaticBitmap.html
        """



EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

