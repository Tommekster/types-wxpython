# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class IntCtrl(TextCtrl):
    """ This class provides a control that takes and returns integers as
value, and provides bounds support and optional value limiting.


  


        Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
    """
    def __init__(self, parent, id=-1, value = 0, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0, validator = wx.DefaultValidator, name = "integer", min=None, max=None, limited = 0, allow_none = 0, allow_long = 0, default_color = wx.NullColour, oob_color = wx.RED) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = 0*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = 0*, *validator = wx.DefaultValidator*, *name = "integer"*, *min=None*, *max=None*, *limited = 0*, *allow\_none = 0*, *allow\_long = 0*, *default\_color = wx.NullColour*, *oob\_color = wx.RED*)[¶](#wx.lib.intctrl.IntCtrl.__init__ "Permalink to this definition")
Default constructor



Parameters
* **parent** – parent window
* **id** (*int*) – window identifier. A value of -1 indicates a
default value
* **value** – If no initial value is set, the default will be zero,
or the minimum value, if specified. If an illegal string is
specified, a ValueError will result. (You can always later set the
initial value with ChangeValue() after instantiation of the control.)
* **pos** (*tuple*) – the control position. A value of (-1, -1) indicates
a default position, chosen by either the windowing system or
wxPython, depending on platform
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a
default size, chosen by either the windowing system or wxPython,
depending on platform
* **style** (*int*) – the underlying `TextCtrl` style
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Normally None, IntCtrl uses its own
validator to do value validation and input control. However, a
validator derived from `IntValidator` can be
supplied to override the data transfer methods for the
`IntValidator` class.
* **min** (*int*) – The minimum value that the control should allow. This
can be adjusted with SetMin(). If the control is not limited, any
value below this bound will be colored with the current out-of-bounds
color. If min < -sys.maxsize-1 and the control is configured to not
allow long values, the minimum bound will still be set to the long
value, but the implicit bound will be -sys.maxsize-1.
* **max** (*int*) – The maximum value that the control should allow. This
can be adjusted with SetMax(). If the control is not limited, any
value above this bound will be colored with the current out-of-bounds
color. if max > sys.maxsize and the control is configured to not
allow long values, the maximum bound will still be set to the long
value, but the implicit bound will be sys.maxsize.
* **limited** (*bool*) – Boolean indicating whether the control
prevents values from exceeding the currently set minimum and maximum
values (bounds). If `False` and bounds are set, out-of-bounds values
will be colored with the current out-of-bounds color.
* **allow\_none** (*bool*) – Boolean indicating whether or not the
control is allowed to be empty, representing a value of None for the
control.
* **allow\_long** (*bool*) – Boolean indicating whether or not the
control is allowed to hold and return a long as well as an int.
* **default\_color** (*Color*) – Color value used for in-bounds values
of the control.
* **oob\_color** (*Color*) – Color value used for out-of-bounds values
of the control when the bounds are set but the control is not limited.






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def ChangeValue(self, value: int) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.lib.intctrl.IntCtrl.ChangeValue "Permalink to this definition")
Change the value without sending an EVT\_TEXT event.



Parameters
**value** (*int*) – The value to be set






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.lib.intctrl.IntCtrl.Cut "Permalink to this definition")
Override the `TextCtrl.Cut` function, with our own
that does validation. Will result in a value of 0
if entire contents of control are removed.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetBounds(self) -> None:
        """ 

`GetBounds`(*self*)[¶](#wx.lib.intctrl.IntCtrl.GetBounds "Permalink to this definition")
This function returns a two-tuple (min,max), indicating the
current bounds of the control. Each value can be None if
that bound is not set.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetColors(self) -> None:
        """ 

`GetColors`(*self*)[¶](#wx.lib.intctrl.IntCtrl.GetColors "Permalink to this definition")
Returns a tuple of (default\_color, oob\_color), indicating
the current color settings for the control.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetMax(self) -> None:
        """ 

`GetMax`(*self*)[¶](#wx.lib.intctrl.IntCtrl.GetMax "Permalink to this definition")
Gets the maximum value of the control. It will return the current
maximum integer, or None if not specified.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetMin(self) -> None:
        """ 

`GetMin`(*self*)[¶](#wx.lib.intctrl.IntCtrl.GetMin "Permalink to this definition")
Gets the minimum value of the control. It will return the current
minimum integer, or None if not specified.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def GetValue(self) -> Optional[int]:
        """ 

`GetValue`(*self*)[¶](#wx.lib.intctrl.IntCtrl.GetValue "Permalink to this definition")
Returns the current integer (long) value of the control.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsInBounds(self, value: Optional[int]=None) -> None:
        """ 

`IsInBounds`(*self*, *value=None*)[¶](#wx.lib.intctrl.IntCtrl.IsInBounds "Permalink to this definition")
Returns `True` if no value is specified and the current value
of the control falls within the current bounds. This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.



Parameters
**value** (*int*) – value to check or None






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsLimited(self) -> None:
        """ 

`IsLimited`(*self*)[¶](#wx.lib.intctrl.IntCtrl.IsLimited "Permalink to this definition")
Returns `True` if the control is currently limiting the
value to fall within the current bounds.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsLongAllowed(self) -> None:
        """ 

`IsLongAllowed`(*self*)[¶](#wx.lib.intctrl.IntCtrl.IsLongAllowed "Permalink to this definition")
Is a long value allowed.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def IsNoneAllowed(self) -> None:
        """ 

`IsNoneAllowed`(*self*)[¶](#wx.lib.intctrl.IntCtrl.IsNoneAllowed "Permalink to this definition")
Is a None value allowed.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def OnText(self, event) -> None:
        """ 

`OnText`(*self*, *event*)[¶](#wx.lib.intctrl.IntCtrl.OnText "Permalink to this definition")
Handles an event indicating that the text control’s value
has changed, and issue EVT\_INT event.
NOTE: using wx.TextCtrl.SetValue() to change the control’s
contents from within a wx.EVT\_CHAR handler can cause double
text events. So we check for actual changes to the text
before passing the events on.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.lib.intctrl.IntCtrl.Paste "Permalink to this definition")
Override the `TextCtrl.Paste` function, with our own
that does validation. Will raise ValueError if not a
valid integerizable value.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ 

`SetBounds`(*self*, *min=None*, *max=None*)[¶](#wx.lib.intctrl.IntCtrl.SetBounds "Permalink to this definition")
This function is a convenience function for setting the min and max
values at the same time. The function only applies the maximum bound
if setting the minimum bound is successful, and returns `True` only if both operations succeed.
..note:



```
Leaving out an argument will remove the corresponding bound.

```



Parameters
* **min** (*int*) – The value to be set as minimum
* **max** (*int*) – The value to be set as maximum






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetColors(self, default_color=wx.BLACK, oob_color=wx.RED) -> None:
        """ 

`SetColors`(*self*, *default\_color=wx.BLACK*, *oob\_color=wx.RED*)[¶](#wx.lib.intctrl.IntCtrl.SetColors "Permalink to this definition")
Tells the control what colors to use for normal and out-of-bounds
values. If the value currently exceeds the bounds, it will be
recolored accordingly.



Parameters
* **default\_color** (*Color*) – default color to be used
* **oob\_color** (*Color*) – out of bound color to be used






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetLimited(self, limited: bool) -> None:
        """ 

`SetLimited`(*self*, *limited*)[¶](#wx.lib.intctrl.IntCtrl.SetLimited "Permalink to this definition")
If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the control’s value currently exceeds the bounds, it will then
be limited accordingly.


If called with a value of 0, this function will disable value
limiting, but coloring of out-of-bounds values will still take
place if bounds have been set for the control.



Parameters
**limited** (*bool*) – If `True` set to control to be limited.






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetLongAllowed(self, allow_long: bool) -> None:
        """ 

`SetLongAllowed`(*self*, *allow\_long*)[¶](#wx.lib.intctrl.IntCtrl.SetLongAllowed "Permalink to this definition")
Change the behavior of the validation code, allowing control
to have a long value or not, as appropriate. If the value
of the control is currently long, and allow\_long is 0, the
value of the control will be adjusted to fall within the
size of an integer type, at either the sys.maxsize or -sys.maxsize-1,
for positive and negative values, respectively.



Parameters
**allow\_long** (*bool*) – If `True` allow long values for control






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ 

`SetMax`(*self*, *max=None*)[¶](#wx.lib.intctrl.IntCtrl.SetMax "Permalink to this definition")
Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns 0 and the maximum will not change from its
current setting. On success, the function returns 1.


If successful and the current value is greater than the new upper
bound, if the control is limited the value will be automatically
adjusted to this maximum value; if not limited, the value in the
control will be colored with the current out-of-bounds color.


If max > sys.maxsize and the control is configured to not allow longs,
the function will return 0, and the max will not be set.



Parameters
**max** (*int*) – The value to be set as maximum






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ 

`SetMin`(*self*, *min=None*)[¶](#wx.lib.intctrl.IntCtrl.SetMin "Permalink to this definition")
Sets the minimum value of the control. If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns 0 and the minimum will not change from
its current setting. On success, the function returns 1.


If successful and the current value is lower than the new lower
bound, if the control is limited, the value will be automatically
adjusted to the new minimum value; if not limited, the value in the
control will be colored with the current out-of-bounds color.


If min > -sys.maxsize-1 and the control is configured to not allow longs,
the function will return 0, and the min will not be set.



Parameters
**min** (*int*) – The value to be set as minimum






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetNoneAllowed(self, allow_none: bool) -> None:
        """ 

`SetNoneAllowed`(*self*, *allow\_none*)[¶](#wx.lib.intctrl.IntCtrl.SetNoneAllowed "Permalink to this definition")
Change the behavior of the validation code, allowing control
to have a value of None or not, as appropriate. If the value
of the control is currently None, and allow\_none is 0, the
value of the control will be set to the minimum value of the
control, or 0 if no lower bound is set.



Parameters
**allow\_none** (*bool*) – If `True` a None value is allowed






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    def SetValue(self, value: Optional[int]) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.intctrl.IntCtrl.SetValue "Permalink to this definition")
Sets the value of the control to the integer value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.



Parameters
**value** (*int*) – The value to be set






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntCtrl.html
        """

    Limited: Any  # `Limited`[¶](#wx.lib.intctrl.IntCtrl.Limited "Permalink to this definition")Returns True if the control is currently limiting thevalue to fall within the current bounds.
    LongAllowed: Any  # `LongAllowed`[¶](#wx.lib.intctrl.IntCtrl.LongAllowed "Permalink to this definition")Is a long value allowed.
    Max: Any  # `Max`[¶](#wx.lib.intctrl.IntCtrl.Max "Permalink to this definition")Gets the maximum value of the control. It will return the currentmaximum integer, or None if not specified.
    Min: Any  # `Min`[¶](#wx.lib.intctrl.IntCtrl.Min "Permalink to this definition")Gets the minimum value of the control. It will return the currentminimum integer, or None if not specified.
    NoneAllowed: Any  # `NoneAllowed`[¶](#wx.lib.intctrl.IntCtrl.NoneAllowed "Permalink to this definition")Is a None value allowed.
    Value: Any  # `Value`[¶](#wx.lib.intctrl.IntCtrl.Value "Permalink to this definition")Returns the current integer (long) value of the control.



class IntUpdatedEvent(PyCommandEvent):
    """ Event sent from the `IntCtrl` when control is updated.


  


        Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
    """
    def __init__(self, id, value = 0, object=None) -> None:
        """ 

`__init__`(*self*, *id*, *value = 0*, *object=None*)[¶](#wx.lib.intctrl.IntUpdatedEvent.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **id** (*int*) – the object id
* **value** (*int*) – the value
* **object** – the object of the event






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.intctrl.IntUpdatedEvent.GetValue "Permalink to this definition")
Retrieve the value of the control at the time
this event was generated.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntUpdatedEvent.html
        """



class IntValidator(Validator):
    """ Validator class used with `IntCtrl` handles all validation of
input prior to changing the value of the underlying `TextCtrl`.


  


        Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.intctrl.IntValidator.__init__ "Permalink to this definition")
Standard constructor




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.intctrl.IntValidator.Clone "Permalink to this definition")
Standard cloner



..note::Every validator must implement the Clone() method.






            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def OnChar(self, event) -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.lib.intctrl.IntValidator.OnChar "Permalink to this definition")
Validates keystrokes to make sure the resulting value will a legal
value. Erasing the value causes it to be set to 0, with the value
selected, so it can be replaced. Similarly, replacing the value
with a ‘-‘ sign causes the value to become -1, with the value
selected. Leading zeros are removed if introduced by selection,
and are prevented from being inserted.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def TransferFromWindow(self) -> None:
        """ 

`TransferFromWindow`(*self*)[¶](#wx.lib.intctrl.IntValidator.TransferFromWindow "Permalink to this definition")
Transfer data from window to validator.


The default implementation returns False, indicating that an error
occurred. We simply return True, to indicate to e.g. `Dialog`
that all is well.


If data comes e.g. from a database then you need to override this.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def TransferToWindow(self) -> None:
        """ 

`TransferToWindow`(*self*)[¶](#wx.lib.intctrl.IntValidator.TransferToWindow "Permalink to this definition")
Transfer data from validator to window.


The default implementation returns False, indicating that an error
occurred. We simply return True, to indicate to e.g. `Dialog`
that all is well.


If data comes e.g. from a database then you need to override this.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """

    def Validate(self, window) -> None:
        """ 

`Validate`(*self*, *window*)[¶](#wx.lib.intctrl.IntValidator.Validate "Permalink to this definition")
Because each operation on the control is vetted as it’s made,
the value of the control is always valid.




            Source: https://docs.wxpython.org/wx.lib.intctrl.IntValidator.html
        """



EVT_INT: int

WXK_CTRL_V: int

WXK_CTRL_X: int

