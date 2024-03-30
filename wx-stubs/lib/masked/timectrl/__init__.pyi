# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class TimeCtrl(BaseMaskedTextCtrl):
    """ Masked control providing several time formats and manipulation of time values.


  


        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
    """
    def __init__(self, parent, id=-1, value = '00:00:00', pos = wx.DefaultPosition, size = wx.DefaultSize, fmt24hr=False, spinButton = None, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = "time", **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = '00:00:00'*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *fmt24hr=False*, *spinButton = None*, *style = wx.TE\_PROCESS\_TAB*, *validator = wx.DefaultValidator*, *name = "time"*, *\*\*kwargs*)[¶](#wx.lib.masked.timectrl.TimeCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window parent. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*string*) – value to be shown;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **fmt24hr** (*boolean*) – `True` to use 24 hour format (sometimes called military format;
* **spinButton** ([*SpinButton*](wx.SpinButton.html#wx.SpinButton "wx.SpinButton")) – an instance of `SpinButton` or
None;
* **style** (*integer*) – the window style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – this is mainly provided for data-transfer, as control does
its own validation;
* **name** (*string*) – the window name;






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def BindSpinButton(self, sb: SpinButton) -> None:
        """ 

`BindSpinButton`(*self*, *sb*)[¶](#wx.lib.masked.timectrl.TimeCtrl.BindSpinButton "Permalink to this definition")
This function binds an externally created spin button to the control,
so that up/down events from the button automatically change the control.



Parameters
**sb** ([*SpinButton*](wx.SpinButton.html#wx.SpinButton "wx.SpinButton")) – an instance of `SpinButton`






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def ChangeValue(self, value: Any) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.lib.masked.timectrl.TimeCtrl.ChangeValue "Permalink to this definition")
Validating ChangeValue function for time values:
This function will do dynamic type checking on the value argument,
and convert `DateTime`, mxDateTime, or 12/24 format time string
into the appropriate format string for the control.


No change event is fired by this method.



Parameters
**value** – the time value






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetBounds(self, as_string = False) -> None:
        """ 

`GetBounds`(*self*, *as\_string = False*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetBounds "Permalink to this definition")
This function returns a two-tuple (min,max), indicating the
current bounds of the control. Each value can be None if
that bound is not set.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetFormat(self) -> None:
        """ 

`GetFormat`(*self*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetFormat "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMax(self, as_string = False) -> None:
        """ 

`GetMax`(*self*, *as\_string = False*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetMax "Permalink to this definition")
Gets the minimum value of the control.
If None, it will return None. Otherwise it will return
the current minimum bound on the control, as a `DateTime`
by default, or as a string if as\_string argument is True.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMin(self, as_string = False) -> None:
        """ 

`GetMin`(*self*, *as\_string = False*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetMin "Permalink to this definition")
Gets the minimum value of the control.
If None, it will return None. Otherwise it will return
the current minimum bound on the control, as a `DateTime`
by default, or as a string if as\_string argument is True.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetMxDateTime(self, value=None) -> None:
        """ 

`GetMxDateTime`(*self*, *value=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetMxDateTime "Permalink to this definition")
Returns the value of the control as an mx.DateTime, with the date
portion set to January 1, 1970.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetValue(self, as_wxDateTime = False, as_mxDateTime = False, as_wxTimeSpan = False, as_mxDateTimeDelta = False) -> Optional[Any]:
        """ 

`GetValue`(*self*, *as\_wxDateTime = False*, *as\_mxDateTime = False*, *as\_wxTimeSpan = False*, *as\_mxDateTimeDelta = False*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetValue "Permalink to this definition")
This function returns the value of the display as a string by default,
but supports return as a `DateTime`, mx.DateTime, `TimeSpan`,
or mx.DateTimeDelta, if requested.
(Evaluated in the order above– first one wins!)



Parameters
* **as\_wxDateTime** (*boolean*) – return value as `DateTime`;
* **as\_mxDateTime** (*boolean*) – return value as mxDateTime;
* **as\_wxTimeSpan** (*boolean*) – return value as `TimeSpan`;
* **as\_mxDateTimeDelta** (*boolean*) – return value as mxDateTimeDelta;






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def GetWxDateTime(self, value=None) -> None:
        """ 

`GetWxDateTime`(*self*, *value=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.GetWxDateTime "Permalink to this definition")
This function is the conversion engine for TimeCtrl; it takes
one of the following types:


* time string
* `DateTime`
* `TimeSpan`
* mxDateTime
* mxDateTimeDelta


and converts it to a `DateTime` that always has Jan 1, 1970 as
its date portion, so that range comparisons around values can work using
`DateTime` built-in comparison function. If a value is not
provided to convert, the string value of the control will be used.
If the value is not one of the accepted types, a ValueError will be
raised.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsInBounds(self, value=None) -> None:
        """ 

`IsInBounds`(*self*, *value=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.IsInBounds "Permalink to this definition")
Returns `True` if no value is specified and the current value
of the control falls within the current bounds. As the clock
is a “circle”, both minimum and maximum bounds must be set for
a value to ever be considered “out of bounds”. This function can
also be called with a value to see if that value would fall within
the current bounds of the given control.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsLimited(self) -> None:
        """ 

`IsLimited`(*self*)[¶](#wx.lib.masked.timectrl.TimeCtrl.IsLimited "Permalink to this definition")
Returns `True` if the control is currently limiting the
value to fall within any current bounds. *Note:* can
be set even if there are no current bounds.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def IsValid(self, value: Any) -> None:
        """ 

`IsValid`(*self*, *value*)[¶](#wx.lib.masked.timectrl.TimeCtrl.IsValid "Permalink to this definition")
Can be used to determine if a given value would be a legal and
in-bounds value for the control.



Parameters
**value** – value to check






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetBounds(self, min=None, max=None) -> None:
        """ 

`SetBounds`(*self*, *min=None*, *max=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetBounds "Permalink to this definition")
This function is a convenience function for setting the min and max
values at the same time. The function only applies the maximum bound
if setting the minimum bound is successful, and returns `True` only if both operations succeed.



Note


Leaving out an argument will remove the corresponding bound.




Parameters
* **min** (*integer* *or* *None*) – Minimum value for the control
* **max** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetFormat(self, format) -> None:
        """ 

`SetFormat`(*self*, *format*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetFormat "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetInsertionPoint(self, pos) -> None:
        """ 

`SetInsertionPoint`(*self*, *pos*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetInsertionPoint "Permalink to this definition")
This override records the specified position and associated cell before
calling base class’ function. This is necessary to handle the optional
spin button, because the insertion point is lost when the focus shifts
to the spin button.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetLimited(self, limited: bool) -> None:
        """ 

`SetLimited`(*self*, *limited*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetLimited "Permalink to this definition")
If called with a value of True, this function will cause the control
to limit the value to fall within the bounds currently specified.
If the control’s value currently exceeds the bounds, it will then
be limited accordingly.


If called with a value of 0, this function will disable value
limiting, but coloring of out-of-bounds values will still take
place if bounds have been set for the control.



Parameters
**limited** (*boolean*) – define value limiting






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMax(self, max: Optional[int]=None) -> None:
        """ 

`SetMax`(*self*, *max=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetMax "Permalink to this definition")
Sets the maximum value of the control. If a value of None
is provided, then the control will have no explicit maximum value.
If the value specified is less than the current minimum value, then
the function returns `False` and the maximum will not change from its
current setting. On success, the function returns True.


If successful and the current value is greater than the new upper
bound, if the control is limited the value will be automatically
adjusted to this maximum value; if not limited, the value in the
control will be colored as invalid.



Parameters
**max** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMin(self, min: Optional[int]=None) -> None:
        """ 

`SetMin`(*self*, *min=None*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetMin "Permalink to this definition")
Sets the minimum value of the control. If a value of None
is provided, then the control will have no explicit minimum value.
If the value specified is greater than the current maximum value,
then the function returns 0 and the minimum will not change from
its current setting. On success, the function returns 1.


If successful and the current value is lower than the new lower
bound, if the control is limited, the value will be automatically
adjusted to the new minimum value; if not limited, the value in the
control will be colored as invalid.



Parameters
**min** (*integer* *or* *None*) – Minimum value for the control






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetMxDateTime(self, mxdt) -> None:
        """ 

`SetMxDateTime`(*self*, *mxdt*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetMxDateTime "Permalink to this definition")
Because SetValue can take an mx.DateTime, (if DateTime is importable),
this is now just an alias.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetParameters(self, **kwargs) -> None:
        """ 

`SetParameters`(*self*, *\*\*kwargs*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetParameters "Permalink to this definition")
Function providing access to the parameters governing TimeCtrl display
and bounds.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetSelection(self, sel_start, sel_to) -> None:
        """ 

`SetSelection`(*self*, *sel\_start*, *sel\_to*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetSelection "Permalink to this definition")
SetSelection([from\_](#id5), [to\_](#id7))


Selects the text starting at the first position up to (but not
including) the character at the last position.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetValue(self, value: Any) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetValue "Permalink to this definition")
Validating SetValue function for time values:
This function will do dynamic type checking on the value argument,
and convert `DateTime`, mxDateTime, or 12/24 format time string
into the appropriate format string for the control.



Parameters
**value** – the time value






            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """

    def SetWxDateTime(self, wxdt) -> None:
        """ 

`SetWxDateTime`(*self*, *wxdt*)[¶](#wx.lib.masked.timectrl.TimeCtrl.SetWxDateTime "Permalink to this definition")
Because SetValue can take a `DateTime`, this is now just an alias.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrl.html
        """



class TimeCtrlAccessorsMixin:
    """ Defines TimeCtrl’s list of attributes having their own Get/Set functions,
ignoring those in the base class that make no sense for a time control.




        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeCtrlAccessorsMixin.html
    """


class TimeUpdatedEvent(PyCommandEvent):
    """ Used to fire an EVT\_TIMEUPDATE event whenever the value in a TimeCtrl changes.


  


        Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
    """
    def __init__(self, id, value ='12:00:00 AM') -> None:
        """ 

`__init__`(*self*, *id*, *value ='12:00:00 AM'*)[¶](#wx.lib.masked.timectrl.TimeUpdatedEvent.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.masked.timectrl.TimeUpdatedEvent.GetValue "Permalink to this definition")
Retrieve the value of the time control at the time this event was generated




            Source: https://docs.wxpython.org/wx.lib.masked.timectrl.TimeUpdatedEvent.html
        """



