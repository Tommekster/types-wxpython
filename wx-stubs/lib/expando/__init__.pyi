# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class ExpandoTextCtrl(TextCtrl):
    """ The ExpandoTextCtrl is a multi-line wx.TextCtrl that will
adjust its height on the fly as needed to accommodate the number of
lines needed to display the current content of the control. It is
assumed that the width of the control will be a fixed value and
that only the height will be adjusted automatically. If the
control is used in a sizer then the width should be set as part of
the initial or min size of the control.


When the control resizes itself it will attempt to also make
necessary adjustments in the sizer hierarchy it is a member of (if
any) but if that is not suffiecient then the programmer can catch
the EVT\_ETC\_LAYOUT\_NEEDED event in the container and make any
other layout adjustments that may be needed.


  


        Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
    """
    def __init__(self, parent, id=-1, value="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name="expando") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value=""*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *validator=wx.DefaultValidator*, *name="expando"*)[¶](#wx.lib.expando.ExpandoTextCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([`wx.Window`](wx.Window.html#wx.Window "wx.Window")) – parent window, must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*string*) – the control text label;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying [`wx.Control`](wx.Control.html#wx.Control "wx.Control") style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – the window validator;
* **name** (*string*) – the widget name.






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def AppendText(self, text: str) -> None:
        """ 

`AppendText`(*self*, *text*)[¶](#wx.lib.expando.ExpandoTextCtrl.AppendText "Permalink to this definition")
Appends the text to the end of the text control.



Parameters
**text** (*string*) – text to write to the text control.





See also


[`WriteText`](#wx.lib.expando.ExpandoTextCtrl.WriteText "wx.lib.expando.ExpandoTextCtrl.WriteText")





            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def GetMaxHeight(self) -> int:
        """ 

`GetMaxHeight`(*self*)[¶](#wx.lib.expando.ExpandoTextCtrl.GetMaxHeight "Permalink to this definition")
Returns the maximum height that the control will expand to on its own.



Return type
int






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def OnSize(self, evt) -> None:
        """ 

`OnSize`(*self*, *evt*)[¶](#wx.lib.expando.ExpandoTextCtrl.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`ExpandoTextCtrl`](#wx.lib.expando.ExpandoTextCtrl "wx.lib.expando.ExpandoTextCtrl").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def OnTextChanged(self, evt) -> None:
        """ 

`OnTextChanged`(*self*, *evt*)[¶](#wx.lib.expando.ExpandoTextCtrl.OnTextChanged "Permalink to this definition")
Handles the `wx.EVT_TEXT` event for [`ExpandoTextCtrl`](#wx.lib.expando.ExpandoTextCtrl "wx.lib.expando.ExpandoTextCtrl").



Parameters
**event** – a `CommandEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.expando.ExpandoTextCtrl.SetFont "Permalink to this definition")
Sets the font for the [`ExpandoTextCtrl`](#wx.lib.expando.ExpandoTextCtrl "wx.lib.expando.ExpandoTextCtrl").



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – font to associate with the [`ExpandoTextCtrl`](#wx.lib.expando.ExpandoTextCtrl "wx.lib.expando.ExpandoTextCtrl"), pass
`NullFont` to reset to the default font.



Return type
bool



Returns
`True` if the font was really changed, `False` if it was already
set to this font and nothing was done.






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def SetMaxHeight(self, h: int) -> None:
        """ 

`SetMaxHeight`(*self*, *h*)[¶](#wx.lib.expando.ExpandoTextCtrl.SetMaxHeight "Permalink to this definition")
Sets the maximum height that the control will expand to on its
own, and adjusts it down if needed.



Parameters
**h** (*integer*) – the maximum control height, in pixels.






            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """

    def WriteText(self, text: str) -> None:
        """ 

`WriteText`(*self*, *text*)[¶](#wx.lib.expando.ExpandoTextCtrl.WriteText "Permalink to this definition")
Writes the text into the text control at the current insertion position.



Parameters
**text** (*string*) – text to write to the text control.





Note


Newlines in the text string are the only control characters allowed, and they
will cause appropriate line breaks. See [`AppendText`](#wx.lib.expando.ExpandoTextCtrl.AppendText "wx.lib.expando.ExpandoTextCtrl.AppendText") for more convenient
ways of writing to the window. After the write operation, the insertion point
will be at the end of the inserted text, so subsequent write operations will
be appended. To append text after the user may have interacted with the control,
call `TextCtrl.SetInsertionPointEnd` before writing.





            Source: https://docs.wxpython.org/wx.lib.expando.ExpandoTextCtrl.html
        """



EVT_SIZE: int

EVT_TEXT: int

