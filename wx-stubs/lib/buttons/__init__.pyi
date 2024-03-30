# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class __ThemedMixin:
    """ Uses the native renderer to draw the bezel, also handle mouse-overs.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
    """
    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 

`DrawBezel`(*self*, *dc*, *x1*, *y1*, *x2*, *y2*)[¶](#wx.lib.buttons.__ThemedMixin.DrawBezel "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """

    def InitOtherEvents(self) -> None:
        """ 

`InitOtherEvents`(*self*)[¶](#wx.lib.buttons.__ThemedMixin.InitOtherEvents "Permalink to this definition")
Initializes other events needed for themed buttons.




            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """

    def OnMouse(self, event: 'MouseEvent') -> None:
        """ 

`OnMouse`(*self*, *event*)[¶](#wx.lib.buttons.__ThemedMixin.OnMouse "Permalink to this definition")
Handles the `wx.EVT_ENTER_WINDOW` and `wx.EVT_LEAVE_WINDOW` events for
[`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as a themed button.



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ThemedMixin.html
        """



EVT_ENTER_WINDOW: int

EVT_LEAVE_WINDOW: int

class __ToggleMixin:
    """ A mixin that allows to transform [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") in the corresponding
toggle button.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
    """
    def GetToggle(self) -> None:
        """ 

`GetToggle`(*self*)[¶](#wx.lib.buttons.__ToggleMixin.GetToggle "Permalink to this definition")
Returns the toggled state of a button.



Returns
`True` is the button is toggled, `False` if it is not toggled.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.buttons.__ToggleMixin.OnKeyDown "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as toggle button.



Parameters
**event** – a [`wx.KeyEvent`](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.buttons.__ToggleMixin.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as toggle button.



Parameters
**event** – a [`wx.KeyEvent`](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.buttons.__ToggleMixin.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as toggle button.



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.buttons.__ToggleMixin.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as toggle button.



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.buttons.__ToggleMixin.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") when used as toggle button.



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """

    def SetToggle(self, flag: bool) -> None:
        """ 

`SetToggle`(*self*, *flag*)[¶](#wx.lib.buttons.__ToggleMixin.SetToggle "Permalink to this definition")
Sets the button as toggled/not toggled.



Parameters
**flag** (*bool*) – `True` to set the button as toggled, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.buttons.__ToggleMixin.html
        """



EVT_KEY_DOWN: int

EVT_KEY_UP: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MOTION: int

class GenButton(Control):
    """ A generic button, and base class for the other generic buttons.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
    """
    def __init__(self, parent, id=-1, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *label=''*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = 0*, *validator = wx.DefaultValidator*, *name = "genbutton"*)[¶](#wx.lib.buttons.GenButton.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **label** (*string*) – the button text label;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default
position, chosen by either the windowing system or wxPython, depending on
platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the button style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – the validator associated with the button;
* **name** (*string*) – the button name.





See also


[`wx.Button`](wx.Button.html#wx.Button "wx.Button") for a list of valid window styles.





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def AcceptsFocus(self) -> None:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.lib.buttons.GenButton.AcceptsFocus "Permalink to this definition")
Can this window be given focus by mouse click?



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.buttons.GenButton.DoGetBestSize "Permalink to this definition")
Overridden base class virtual. Determines the best size of the
button based on the label and bezel size.



Returns
An instance of [`wx.Size`](wx.Size.html#wx.Size "wx.Size").





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawBezel(self, dc, x1, y1, x2, y2) -> None:
        """ 

`DrawBezel`(*self*, *dc*, *x1*, *y1*, *x2*, *y2*)[¶](#wx.lib.buttons.GenButton.DrawBezel "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawFocusIndicator(self, dc, w, h) -> None:
        """ 

`DrawFocusIndicator`(*self*, *dc*, *w*, *h*)[¶](#wx.lib.buttons.GenButton.DrawFocusIndicator "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *width*, *height*, *dx=0*, *dy=0*)[¶](#wx.lib.buttons.GenButton.DrawLabel "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.buttons.GenButton.Enable "Permalink to this definition")
Enables/disables the button.



Parameters
**enable** (*bool*) – `True` to enable the button, `False` to disable it.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetBackgroundBrush(self, dc: 'DC') -> None:
        """ 

`GetBackgroundBrush`(*self*, *dc*)[¶](#wx.lib.buttons.GenButton.GetBackgroundBrush "Permalink to this definition")
Returns the current [`wx.Brush`](wx.Brush.html#wx.Brush "wx.Brush") to be used to draw the button background.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – the device context used to draw the button background.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetBezelWidth(self) -> int:
        """ 

`GetBezelWidth`(*self*)[¶](#wx.lib.buttons.GenButton.GetBezelWidth "Permalink to this definition")
Returns the width of the 3D effect, in pixels.



Return type
integer






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetDefaultAttributes(self) -> None:
        """ 

`GetDefaultAttributes`(*self*)[¶](#wx.lib.buttons.GenButton.GetDefaultAttributes "Permalink to this definition")
Overridden base class virtual. By default we should use
the same font/colour attributes as the native [`wx.Button`](wx.Button.html#wx.Button "wx.Button").



Returns
an instance of [`wx.VisualAttributes`](wx.VisualAttributes.html#wx.VisualAttributes "wx.VisualAttributes").





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def GetUseFocusIndicator(self) -> bool:
        """ 

`GetUseFocusIndicator`(*self*)[¶](#wx.lib.buttons.GenButton.GetUseFocusIndicator "Permalink to this definition")
Returns the focus indicator flag, specifying if a focus indicator
(dotted line) is being used.



Return type
bool






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def InitColours(self) -> None:
        """ 

`InitColours`(*self*)[¶](#wx.lib.buttons.GenButton.InitColours "Permalink to this definition")
Calculate a new set of highlight and shadow colours based on
the background colour. Works okay if the colour is dark…




            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def InitOtherEvents(self) -> None:
        """ 

`InitOtherEvents`(*self*)[¶](#wx.lib.buttons.GenButton.InitOtherEvents "Permalink to this definition")
Override this method in a subclass to initialize any other events that
need to be bound. Added so [`__init__`](#wx.lib.buttons.GenButton.__init__ "wx.lib.buttons.GenButton.__init__") doesn’t need to be
overridden, which is complicated with multiple inheritance.




            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def Notify(self) -> None:
        """ 

`Notify`(*self*)[¶](#wx.lib.buttons.GenButton.Notify "Permalink to this definition")
Actually sends a `wx.EVT_BUTTON` event to the listener (if any).




            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnGainFocus(self, event: 'FocusEvent') -> None:
        """ 

`OnGainFocus`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnGainFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.FocusEvent`](wx.FocusEvent.html#wx.FocusEvent "wx.FocusEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnKeyDown(self, event: 'KeyEvent') -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnKeyDown "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.KeyEvent`](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnKeyUp(self, event: 'KeyEvent') -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.KeyEvent`](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLoseCapture(self, event: 'MouseCaptureLostEvent') -> None:
        """ 

`OnLoseCapture`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnLoseCapture "Permalink to this definition")
Handles the `wx.EVT_MOUSE_CAPTURE_LOST` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.MouseCaptureLostEvent`](wx.MouseCaptureLostEvent.html#wx.MouseCaptureLostEvent "wx.MouseCaptureLostEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnLoseFocus(self, event: 'FocusEvent') -> None:
        """ 

`OnLoseFocus`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnLoseFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.FocusEvent`](wx.FocusEvent.html#wx.FocusEvent "wx.FocusEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnMotion(self, event: 'MouseEvent') -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.MouseEvent`](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.PaintEvent`](wx.PaintEvent.html#wx.PaintEvent "wx.PaintEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.buttons.GenButton.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.lib.buttons.GenButton.SetBackgroundColour "Permalink to this definition")
Sets the [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") background colour.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetBezelWidth(self, width: int) -> None:
        """ 

`SetBezelWidth`(*self*, *width*)[¶](#wx.lib.buttons.GenButton.SetBezelWidth "Permalink to this definition")
Sets the width of the 3D effect.



Parameters
**width** (*integer*) – the 3D border width, in pixels.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetDefault(self) -> None:
        """ 

`SetDefault`(*self*)[¶](#wx.lib.buttons.GenButton.SetDefault "Permalink to this definition")
This sets the [`GenButton`](#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton") to be the default item for
the panel or dialog box.



Note


Under Windows, only dialog box buttons respond to this function.
As normal under Windows and Motif, pressing return causes the
default button to be depressed when the return key is pressed. See
also [`wx.Window.SetFocus`](wx.Window.html#wx.Window.SetFocus "wx.Window.SetFocus") which sets the keyboard focus for
windows and text panel items, and
[`wx.TopLevelWindow.SetDefaultItem`](wx.TopLevelWindow.html#wx.TopLevelWindow.SetDefaultItem "wx.TopLevelWindow.SetDefaultItem").




Note


Note that under Motif, calling this function immediately after
creation of a button and before the creation of other buttons will
cause misalignment of the row of buttons, since default buttons are
larger. To get around this, call `wx.SetDefault` after you
have created a row of buttons: wxPython will then set the size of
all buttons currently on the panel to the same size.





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetForegroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetForegroundColour`(*self*, *colour*)[¶](#wx.lib.buttons.GenButton.SetForegroundColour "Permalink to this definition")
Sets the `wx.GenButton` foreground colour.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetInitialSize(self, size: Optional[Union[tuple[int, int], 'Size']]=None) -> None:
        """ 

`SetInitialSize`(*self*, *size=None*)[¶](#wx.lib.buttons.GenButton.SetInitialSize "Permalink to this definition")
Given the current font and bezel width settings, calculate
and set a good size.



Parameters
**size** – an instance of [`wx.Size`](wx.Size.html#wx.Size "wx.Size") or `None`,
in which case the wxPython
`wx.DefaultSize` is used instead.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def SetUseFocusIndicator(self, flag: bool) -> None:
        """ 

`SetUseFocusIndicator`(*self*, *flag*)[¶](#wx.lib.buttons.GenButton.SetUseFocusIndicator "Permalink to this definition")
Specifies if a focus indicator (dotted line) should be used.



Parameters
**flag** (*bool*) – `True` to draw a focus ring, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """

    def ShouldInheritColours(self) -> None:
        """ 

`ShouldInheritColours`(*self*)[¶](#wx.lib.buttons.GenButton.ShouldInheritColours "Permalink to this definition")
Overridden base class virtual. Buttons usually don’t inherit
the parent’s colours.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.buttons.GenButton.html
        """



EVT_BUTTON: int

EVT_SET_FOCUS: int

EVT_MOUSE_CAPTURE_LOST: int

EVT_KILL_FOCUS: int

EVT_PAINT: int

EVT_SIZE: int

DefaultSize: int

class GenBitmapButton(GenButton):
    """ A generic bitmap button.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *bitmap=wx.NullBitmap*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = 0*, *validator = wx.DefaultValidator*, *name = "genbutton"*)[¶](#wx.lib.buttons.GenBitmapButton.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the button bitmap;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the button style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – the validator associated to the button;
* **name** (*string*) – the button name.





See also


[`wx.Button`](wx.Button.html#wx.Button "wx.Button") for a list of valid window styles.





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *width*, *height*, *dx=0*, *dy=0*)[¶](#wx.lib.buttons.GenBitmapButton.DrawLabel "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapDisabled(self) -> 'Bitmap':
        """ 

`GetBitmapDisabled`(*self*)[¶](#wx.lib.buttons.GenBitmapButton.GetBitmapDisabled "Permalink to this definition")
Returns the bitmap for the button’s disabled state, which may be invalid.



Return type
[`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")





See also


[`SetBitmapDisabled`](#wx.lib.buttons.GenBitmapButton.SetBitmapDisabled "wx.lib.buttons.GenBitmapButton.SetBitmapDisabled")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapFocus(self) -> 'Bitmap':
        """ 

`GetBitmapFocus`(*self*)[¶](#wx.lib.buttons.GenBitmapButton.GetBitmapFocus "Permalink to this definition")
Returns the bitmap for the button’s focused state, which may be invalid.



Return type
[`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")





See also


[`SetBitmapFocus`](#wx.lib.buttons.GenBitmapButton.SetBitmapFocus "wx.lib.buttons.GenBitmapButton.SetBitmapFocus")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapLabel(self) -> 'Bitmap':
        """ 

`GetBitmapLabel`(*self*)[¶](#wx.lib.buttons.GenBitmapButton.GetBitmapLabel "Permalink to this definition")
Returns the bitmap for the button’s normal state.



Return type
[`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")





See also


[`SetBitmapLabel`](#wx.lib.buttons.GenBitmapButton.SetBitmapLabel "wx.lib.buttons.GenBitmapButton.SetBitmapLabel")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def GetBitmapSelected(self) -> 'Bitmap':
        """ 

`GetBitmapSelected`(*self*)[¶](#wx.lib.buttons.GenBitmapButton.GetBitmapSelected "Permalink to this definition")
Returns the bitmap for the button’s pressed state, which may be invalid.



Return type
[`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")





See also


[`SetBitmapSelected`](#wx.lib.buttons.GenBitmapButton.SetBitmapSelected "wx.lib.buttons.GenBitmapButton.SetBitmapSelected")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapDisabled(self, bitmap: 'Bitmap') -> None:
        """ 

`SetBitmapDisabled`(*self*, *bitmap*)[¶](#wx.lib.buttons.GenBitmapButton.SetBitmapDisabled "Permalink to this definition")
Sets the bitmap for the disabled button appearance.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for the disabled button appearance.





See also


[`GetBitmapDisabled`](#wx.lib.buttons.GenBitmapButton.GetBitmapDisabled "wx.lib.buttons.GenBitmapButton.GetBitmapDisabled"), [`SetBitmapLabel`](#wx.lib.buttons.GenBitmapButton.SetBitmapLabel "wx.lib.buttons.GenBitmapButton.SetBitmapLabel"),
[`SetBitmapSelected`](#wx.lib.buttons.GenBitmapButton.SetBitmapSelected "wx.lib.buttons.GenBitmapButton.SetBitmapSelected"), [`SetBitmapFocus`](#wx.lib.buttons.GenBitmapButton.SetBitmapFocus "wx.lib.buttons.GenBitmapButton.SetBitmapFocus")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapFocus(self, bitmap: 'Bitmap') -> None:
        """ 

`SetBitmapFocus`(*self*, *bitmap*)[¶](#wx.lib.buttons.GenBitmapButton.SetBitmapFocus "Permalink to this definition")
Sets the bitmap for the focused button appearance.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for the focused button appearance.





See also


[`GetBitmapFocus`](#wx.lib.buttons.GenBitmapButton.GetBitmapFocus "wx.lib.buttons.GenBitmapButton.GetBitmapFocus"), [`SetBitmapLabel`](#wx.lib.buttons.GenBitmapButton.SetBitmapLabel "wx.lib.buttons.GenBitmapButton.SetBitmapLabel"),
[`SetBitmapSelected`](#wx.lib.buttons.GenBitmapButton.SetBitmapSelected "wx.lib.buttons.GenBitmapButton.SetBitmapSelected"), [`SetBitmapDisabled`](#wx.lib.buttons.GenBitmapButton.SetBitmapDisabled "wx.lib.buttons.GenBitmapButton.SetBitmapDisabled")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapLabel(self, bitmap: 'Bitmap', createOthers=True) -> None:
        """ 

`SetBitmapLabel`(*self*, *bitmap*, *createOthers=True*)[¶](#wx.lib.buttons.GenBitmapButton.SetBitmapLabel "Permalink to this definition")
Set the bitmap to display normally.
This is the only one that is required.


If *createOthers* is `True`, then the other bitmaps will be generated
on the fly. Currently, only the disabled bitmap is generated.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for the normal button appearance.





Note


This is the bitmap used for the unselected state, and for all other
states if no other bitmaps are provided.





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """

    def SetBitmapSelected(self, bitmap: 'Bitmap') -> None:
        """ 

`SetBitmapSelected`(*self*, *bitmap*)[¶](#wx.lib.buttons.GenBitmapButton.SetBitmapSelected "Permalink to this definition")
Sets the bitmap for the selected (depressed) button appearance.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for the selected (depressed) button appearance.





See also


[`GetBitmapSelected`](#wx.lib.buttons.GenBitmapButton.GetBitmapSelected "wx.lib.buttons.GenBitmapButton.GetBitmapSelected"), [`SetBitmapLabel`](#wx.lib.buttons.GenBitmapButton.SetBitmapLabel "wx.lib.buttons.GenBitmapButton.SetBitmapLabel"),
[`SetBitmapDisabled`](#wx.lib.buttons.GenBitmapButton.SetBitmapDisabled "wx.lib.buttons.GenBitmapButton.SetBitmapDisabled"), [`SetBitmapFocus`](#wx.lib.buttons.GenBitmapButton.SetBitmapFocus "wx.lib.buttons.GenBitmapButton.SetBitmapFocus")





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapButton.html
        """



class GenBitmapTextButton(GenBitmapButton):
    """ A generic bitmapped button with text label.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
    """
    def __init__(self, parent, id=-1, bitmap=wx.NullBitmap, label='', pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "genbutton") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *bitmap=wx.NullBitmap*, *label=''*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = 0*, *validator = wx.DefaultValidator*, *name = "genbutton"*)[¶](#wx.lib.buttons.GenBitmapTextButton.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the button bitmap;
* **label** (*string*) – the button text label;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the button style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – the validator associated to the button;
* **name** (*string*) – the button name.





See also


[`wx.Button`](wx.Button.html#wx.Button "wx.Button") for a list of valid window styles.





            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
        """

    def DrawLabel(self, dc, width, height, dx=0, dy=0) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *width*, *height*, *dx=0*, *dy=0*)[¶](#wx.lib.buttons.GenBitmapTextButton.DrawLabel "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextButton.html
        """



class GenBitmapTextToggleButton(__ToggleMixin,GenBitmapTextButton):
    """ A generic toggle bitmap button with text label.




        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapTextToggleButton.html
    """


class GenBitmapToggleButton(__ToggleMixin,GenBitmapButton):
    """ A generic toggle bitmap button.




        Source: https://docs.wxpython.org/wx.lib.buttons.GenBitmapToggleButton.html
    """


class GenButtonEvent(CommandEvent):
    """ Event sent from the generic buttons when the button is activated.


  


        Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
    """
    def __init__(self, eventType, id) -> None:
        """ 

`__init__`(*self*, *eventType*, *id*)[¶](#wx.lib.buttons.GenButtonEvent.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **eventType** (*integer*) – the event type;
* **id** (*integer*) – the event identifier.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def GetButtonObj(self) -> None:
        """ 

`GetButtonObj`(*self*)[¶](#wx.lib.buttons.GenButtonEvent.GetButtonObj "Permalink to this definition")
Returns the object associated with this event.



Returns
An instance of [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def GetIsDown(self) -> bool:
        """ 

`GetIsDown`(*self*)[¶](#wx.lib.buttons.GenButtonEvent.GetIsDown "Permalink to this definition")
Returns the button toggle status as `True` if the button is down, `False`
otherwise.



Return type
bool






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def SetButtonObj(self, btn: GenButton) -> None:
        """ 

`SetButtonObj`(*self*, *btn*)[¶](#wx.lib.buttons.GenButtonEvent.SetButtonObj "Permalink to this definition")
Sets the event object for the event.



Parameters
**btn** – the button object, an instance of [`GenButton`](wx.lib.buttons.GenButton.html#wx.lib.buttons.GenButton "wx.lib.buttons.GenButton").






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """

    def SetIsDown(self, isDown: bool) -> None:
        """ 

`SetIsDown`(*self*, *isDown*)[¶](#wx.lib.buttons.GenButtonEvent.SetIsDown "Permalink to this definition")
Set the button toggle status as ‘down’ or ‘up’.



Parameters
**isDown** (*bool*) – `True` if the button is clicked, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.buttons.GenButtonEvent.html
        """



class GenToggleButton(__ToggleMixin,GenButton):
    """ A generic toggle button.




        Source: https://docs.wxpython.org/wx.lib.buttons.GenToggleButton.html
    """


class ThemedGenBitmapButton(__ThemedMixin,GenBitmapButton):
    """ A themed generic bitmap button.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapButton.html
    """


class ThemedGenBitmapTextButton(__ThemedMixin,GenBitmapTextButton):
    """ A themed generic bitmapped button with text label.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapTextButton.html
    """


class ThemedGenBitmapTextToggleButton(__ThemedMixin,GenBitmapTextToggleButton):
    """ A themed generic toggle bitmap button with text label.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapTextToggleButton.html
    """


class ThemedGenBitmapToggleButton(__ThemedMixin,GenBitmapToggleButton):
    """ A themed generic toggle bitmap button.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenBitmapToggleButton.html
    """


class ThemedGenButton(__ThemedMixin,GenButton):
    """ A themed generic button.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenButton.html
    """


class ThemedGenToggleButton(__ThemedMixin,GenToggleButton):
    """ A themed generic toggle button.




        Source: https://docs.wxpython.org/wx.lib.buttons.ThemedGenToggleButton.html
    """


