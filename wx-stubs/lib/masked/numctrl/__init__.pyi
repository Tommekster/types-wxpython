# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class NumCtrl(BaseMaskedTextCtrl,NumCtrlAccessorsMixin):
    """ Masked edit control supporting “native” numeric values, ie. .SetValue(3), for
example, and supporting a variety of formatting options, including automatic
rounding specifiable precision, grouping and decimal place characters, etc.


  


        Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
    """
    def __init__(self, parent, id=-1, value = 0, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = "masked.num", **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = 0*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = wx.TE\_PROCESS\_TAB*, *validator = wx.DefaultValidator*, *name = "masked.num"*, *\*\*kwargs*)[¶](#wx.lib.masked.numctrl.NumCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window parent. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*integer*) – value to be shown;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the window style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – this is mainly provided for data-transfer, as control does
its own validation;
* **name** (*string*) – the window name;






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def ChangeValue(self, value: int) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.ChangeValue "Permalink to this definition")
Sets the value of the control to the value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.


This method does not fire a change event.



Parameters
**value** (*integer*) – new value






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAllowNegative(self) -> None:
        """ 

`GetAllowNegative`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetAllowNegative "Permalink to this definition")
(For regularization of property accessors)




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAllowNone(self) -> None:
        """ 

`GetAllowNone`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetAllowNone "Permalink to this definition")
(For regularization of property accessors)




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetAutoSize(self) -> None:
        """ 

`GetAutoSize`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetAutoSize "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetBounds(self) -> None:
        """ 

`GetBounds`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetBounds "Permalink to this definition")
This function returns a two-tuple (min,max), indicating the
current bounds of the control. Each value can be None if
that bound is not set.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetDecimalChar(self) -> None:
        """ 

`GetDecimalChar`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetDecimalChar "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetFraction(self, candidate=None) -> None:
        """ 

`GetFraction`(*self*, *candidate=None*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetFraction "Permalink to this definition")
Returns the fractional portion of the value as a float. If there is no
fractional portion, the value returned will be 0.0.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetFractionWidth(self) -> None:
        """ 

`GetFractionWidth`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetFractionWidth "Permalink to this definition")
Get the fraction width.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetGroupChar(self) -> None:
        """ 

`GetGroupChar`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetGroupChar "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetGroupDigits(self) -> None:
        """ 

`GetGroupDigits`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetGroupDigits "Permalink to this definition")
(For regularization of property accessors)




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetIntegerWidth(self) -> None:
        """ 

`GetIntegerWidth`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetIntegerWidth "Permalink to this definition")
Get the integer width.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetLimited(self) -> None:
        """ 

`GetLimited`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetLimited "Permalink to this definition")
(For regularization of property accessors)




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetLimitOnFieldChange(self) -> None:
        """ 

`GetLimitOnFieldChange`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetLimitOnFieldChange "Permalink to this definition")
(For regularization of property accessors)




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetMax(self) -> None:
        """ 

`GetMax`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetMax "Permalink to this definition")
Gets the maximum value of the control. It will return the current
maximum integer, or None if not specified.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetMin(self) -> None:
        """ 

`GetMin`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetMin "Permalink to this definition")
Gets the lower bound value of the control. It will return
None if not specified.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetSelectOnEntry(self) -> None:
        """ 

`GetSelectOnEntry`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetSelectOnEntry "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.GetValue "Permalink to this definition")
Returns the current numeric value of the control.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsGroupingAllowed(self) -> None:
        """ 

`IsGroupingAllowed`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsGroupingAllowed "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsInBounds(self, value: Optional[Any]=None) -> None:
        """ 

`IsInBounds`(*self*, *value=None*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsInBounds "Permalink to this definition")
Returns `True` if no value is specified and the current value
of the control falls within the current bounds. This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.



Parameters
**value** – value to check






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsLimited(self) -> None:
        """ 

`IsLimited`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsLimited "Permalink to this definition")
Returns `True` if the control is currently limiting the
value to fall within the current bounds.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsLimitedOnFieldChange(self) -> None:
        """ 

`IsLimitedOnFieldChange`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsLimitedOnFieldChange "Permalink to this definition")
Returns `True` if the control is currently limiting the
value to fall within the current bounds.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsNegativeAllowed(self) -> None:
        """ 

`IsNegativeAllowed`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsNegativeAllowed "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def IsNoneAllowed(self) -> None:
        """ 

`IsNoneAllowed`(*self*)[¶](#wx.lib.masked.numctrl.NumCtrl.IsNoneAllowed "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def OnTextChange(self, event) -> None:
        """ 

`OnTextChange`(*self*, *event*)[¶](#wx.lib.masked.numctrl.NumCtrl.OnTextChange "Permalink to this definition")
Handles an event indicating that the text control’s value
has changed, and issue EVT\_NUM event.



Note


Using `TextCtrl.SetValue` to change the control’s contents from
within a EVT\_CHAR handler can cause double text events. So we check
for actual changes to the text before passing the events on.





            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAllowNegative(self, value) -> None:
        """ 

`SetAllowNegative`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetAllowNegative "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAllowNone(self, allow_none: bool) -> None:
        """ 

`SetAllowNone`(*self*, *allow\_none*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetAllowNone "Permalink to this definition")
Change the behavior of the validation code, allowing control
to have a value of None or not, as appropriate. If the value
of the control is currently None, and allow\_none is False, the
value of the control will be set to the minimum value of the
control, or 0 if no lower bound is set.



Parameters
**allow\_none** (*boolean*) – `True` if None is allowed






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetAutoSize(self, value) -> None:
        """ 

`SetAutoSize`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetAutoSize "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ 

`SetBounds`(*self*, *min=None*, *max=None*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetBounds "Permalink to this definition")
This function is a convenience function for setting the min and max
values at the same time. The function only applies the maximum bound
if setting the minimum bound is successful, and returns `True` only if both operations succeed.



Note


leaving out an argument will remove the corresponding bound.




Parameters
* **min** (*integer* *or* *None*) – Minimum value for the control
* **max** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetDecimalChar(self, value) -> None:
        """ 

`SetDecimalChar`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetDecimalChar "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetFractionWidth(self, value: int) -> None:
        """ 

`SetFractionWidth`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetFractionWidth "Permalink to this definition")
Set the fraction width of the control



Parameters
**value** (*integer*) – the width value






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetGroupChar(self, value) -> None:
        """ 

`SetGroupChar`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetGroupChar "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetGroupDigits(self, value) -> None:
        """ 

`SetGroupDigits`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetGroupDigits "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetIntegerWidth(self, value: int) -> None:
        """ 

`SetIntegerWidth`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetIntegerWidth "Permalink to this definition")
Set the integer width of the control



Parameters
**value** (*integer*) – the width value






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetLimited(self, limited: bool) -> None:
        """ 

`SetLimited`(*self*, *limited*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetLimited "Permalink to this definition")
If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the control’s value currently exceeds the bounds, it will then
be limited accordingly.


If called with a value of False, this function will disable value
limiting, but coloring of out-of-bounds values will still take
place if bounds have been set for the control.



Parameters
**limited** (*boolean*) – define value limiting






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetLimitOnFieldChange(self, limit: bool) -> None:
        """ 

`SetLimitOnFieldChange`(*self*, *limit*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetLimitOnFieldChange "Permalink to this definition")
If called with a value of True, this function will cause the control
to prevent navigation out of the current field if its value is out-of-bounds,
and limit the value to fall within the bounds currently specified if the
control loses focus.


If called with a value of False, this function will disable value
limiting, but coloring of out-of-bounds values will still take
place if bounds have been set for the control.



Parameters
**limit** (*boolean*) – define value limiting






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ 

`SetMax`(*self*, *max=None*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetMax "Permalink to this definition")
Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns `False` and the maximum will not change from its
current setting. On success, the function returns True.


If successful and the current value is greater than the new upper
bound, if the control is limited the value will be automatically
adjusted to this maximum value; if not limited, the value in the
control will be colored as invalid.


If max > the max value allowed by the width of the control,
the function will return False, and the max will not be set.



Parameters
**max** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ 

`SetMin`(*self*, *min=None*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetMin "Permalink to this definition")
Sets the minimum value of the control. If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns `False` and the minimum will not change from
its current setting. On success, the function returns True.


If successful and the current value is lower than the new lower
bound, if the control is limited, the value will be automatically
adjusted to the new minimum value; if not limited, the value in the
control will be colored as invalid.


If min > the max value allowed by the width of the control,
the function will return False, and the min will not be set.



Parameters
**min** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetParameters(self, **kwargs) -> None:
        """ 

`SetParameters`(*self*, *\*\*kwargs*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetParameters "Permalink to this definition")
This function is used to initialize and reconfigure the control.
See `TimeCtrl` module overview for available
parameters.




            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetSelectOnEntry(self, value) -> None:
        """ 

`SetSelectOnEntry`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetSelectOnEntry "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """

    def SetValue(self, value: int) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.masked.numctrl.NumCtrl.SetValue "Permalink to this definition")
Sets the value of the control to the value specified.
The resulting actual value of the control may be altered to
conform with the bounds set on the control if limited,
or colored if not limited but the value is out-of-bounds.
A ValueError exception will be raised if an invalid value
is specified.



Parameters
**value** (*integer*) – new value






            Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrl.html
        """



class NumCtrlAccessorsMixin:
    """ Defines masked.NumCtrl’s list of attributes having their own
Get/Set functions, ignoring those that make no sense for
a numeric control.




        Source: https://docs.wxpython.org/wx.lib.masked.numctrl.NumCtrlAccessorsMixin.html
    """


