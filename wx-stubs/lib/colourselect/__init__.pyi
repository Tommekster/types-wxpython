# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class ColourSelect(GenBitmapButton):
    """ A subclass of [`wx.lib.buttons.GenBitmapButton`](wx.lib.buttons.GenBitmapButton.html#wx.lib.buttons.GenBitmapButton "wx.lib.buttons.GenBitmapButton") that,
when clicked, will display a colour selection dialog.


  


        Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
    """
    def __init__(self, parent, id=wx.ID_ANY, label="", colour=wx.BLACK, pos=wx.DefaultPosition, size=wx.DefaultSize, callback=None, style=0) -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *label=""*, *colour=wx.BLACK*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *callback=None*, *style=0*)[¶](#wx.lib.colourselect.ColourSelect.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **label** (*string*) – the button text label;
* **wx.Colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance, which will be the default initial
colour for this button;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **callback** (*PyObject*) – a callable method/function that will be called every time
the user chooses a new colour;
* **style** (*integer*) – the button style.






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetColour(self) -> 'Colour':
        """ 

`GetColour`(*self*)[¶](#wx.lib.colourselect.ColourSelect.GetColour "Permalink to this definition")
Returns the current colour set for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").



Return type
[`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetCustomColours(self) -> 'CustomColourData':
        """ 

`GetCustomColours`(*self*)[¶](#wx.lib.colourselect.ColourSelect.GetCustomColours "Permalink to this definition")
Returns the current set of custom colour values to be shown in the
colour dialog, if supported.



Return type
[`CustomColourData`](wx.lib.colourselect.CustomColourData.html#wx.lib.colourselect.CustomColourData "wx.lib.colourselect.CustomColourData")






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetLabel(self) -> str:
        """ 

`GetLabel`(*self*)[¶](#wx.lib.colourselect.ColourSelect.GetLabel "Permalink to this definition")
Returns the current text label for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").



Return type
string






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def GetValue(self) -> 'Colour':
        """ 

`GetValue`(*self*)[¶](#wx.lib.colourselect.ColourSelect.GetValue "Permalink to this definition")
Returns the current colour set for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").
Same as [`GetColour`](#wx.lib.colourselect.ColourSelect.GetColour "wx.lib.colourselect.ColourSelect.GetColour").



Return type
[`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def MakeBitmap(self) -> None:
        """ 

`MakeBitmap`(*self*)[¶](#wx.lib.colourselect.ColourSelect.MakeBitmap "Permalink to this definition")
Creates a bitmap representation of the current selected colour.




            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def OnChange(self) -> None:
        """ 

`OnChange`(*self*)[¶](#wx.lib.colourselect.ColourSelect.OnChange "Permalink to this definition")
Fires the `EVT_COLOURSELECT` event, as the user has changed the current colour.




            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def OnClick(self, event: 'CommandEvent') -> None:
        """ 

`OnClick`(*self*, *event*)[¶](#wx.lib.colourselect.ColourSelect.OnClick "Permalink to this definition")
Handles the `wx.EVT_BUTTON` event for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").



Parameters
**event** – a [`wx.CommandEvent`](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetBitmap(self, bmp: 'Bitmap') -> None:
        """ 

`SetBitmap`(*self*, *bmp*)[¶](#wx.lib.colourselect.ColourSelect.SetBitmap "Permalink to this definition")
Sets the bitmap representation of the current selected colour to the button.



Parameters
**bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new bitmap.






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.lib.colourselect.ColourSelect.SetColour "Permalink to this definition")
Sets the current colour for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").



Parameters
**colour** (tuple or string or [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")) – the new colour for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetCustomColours(self, colours: CustomColourData) -> None:
        """ 

`SetCustomColours`(*self*, *colours*)[¶](#wx.lib.colourselect.ColourSelect.SetCustomColours "Permalink to this definition")
Sets the list of custom colour values to be shown in colour dialog, if
supported.



Parameters
**colours** – An instance of [`CustomColourData`](wx.lib.colourselect.CustomColourData.html#wx.lib.colourselect.CustomColourData "wx.lib.colourselect.CustomColourData") or a 16




element list of `None` or [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") values.




            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.lib.colourselect.ColourSelect.SetLabel "Permalink to this definition")
Sets the new text label for `wx.ColourSelect`.



Parameters
**label** (*string*) – the new text label for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    def SetValue(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetValue`(*self*, *colour*)[¶](#wx.lib.colourselect.ColourSelect.SetValue "Permalink to this definition")
Sets the current colour for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect"). Same as
[`SetColour`](#wx.lib.colourselect.ColourSelect.SetColour "wx.lib.colourselect.ColourSelect.SetColour").



Parameters
**colour** (tuple or string or [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")) – the new colour for [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").






            Source: https://docs.wxpython.org/wx.lib.colourselect.ColourSelect.html
        """

    Colour: Any  # `Colour`[¶](#wx.lib.colourselect.ColourSelect.Colour "Permalink to this definition")Returns the current colour set for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").Return type[`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")
    CustomColours: Any  # `CustomColours`[¶](#wx.lib.colourselect.ColourSelect.CustomColours "Permalink to this definition")Returns the current set of custom colour values to be shown in thecolour dialog, if supported.Return type[`CustomColourData`](wx.lib.colourselect.CustomColourData.html#wx.lib.colourselect.CustomColourData "wx.lib.colourselect.CustomColourData")
    Label: Any  # `Label`[¶](#wx.lib.colourselect.ColourSelect.Label "Permalink to this definition")Returns the current text label for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").Return typestring
    Value: Any  # `Value`[¶](#wx.lib.colourselect.ColourSelect.Value "Permalink to this definition")Returns the current colour set for the [`ColourSelect`](#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect").Same as [`GetColour`](#wx.lib.colourselect.ColourSelect.GetColour "wx.lib.colourselect.ColourSelect.GetColour").Return type[`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")



EVT_BUTTON: int

class CustomColourData:
    """ A simple container for tracking custom colours to be shown in the colour
dialog, and which facilitates reuse of this collection across multiple
instances or multiple invocations of the [`ColourSelect`](wx.lib.colourselect.ColourSelect.html#wx.lib.colourselect.ColourSelect "wx.lib.colourselect.ColourSelect") button.


  


        Source: https://docs.wxpython.org/wx.lib.colourselect.CustomColourData.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.colourselect.CustomColourData.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.colourselect.CustomColourData.html
        """

    Colours: Any  # `Colours`[¶](#wx.lib.colourselect.CustomColourData.Colours "Permalink to this definition")See [`Colours`](#wx.lib.colourselect.CustomColourData.Colours "wx.lib.colourselect.CustomColourData.Colours") , [`Colours`](#wx.lib.colourselect.CustomColourData.Colours "wx.lib.colourselect.CustomColourData.Colours")



