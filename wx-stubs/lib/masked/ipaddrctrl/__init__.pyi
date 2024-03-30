# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class IpAddrCtrl(BaseMaskedTextCtrl,IpAddrCtrlAccessorsMixin):
    """ This class is a particular type of MaskedTextCtrl that accepts
and understands the semantics of IP addresses, reformats input
as you move from field to field, and accepts ‘.’ as a navigation
character, so that typing an IP address can be done naturally.


  


        Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator = wx.DefaultValidator, name = 'IpAddrCtrl', setupEventHandling = True, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = ''*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = wx.TE\_PROCESS\_TAB*, *validator = wx.DefaultValidator*, *name = 'IpAddrCtrl'*, *setupEventHandling = True*, *\*\*kwargs*)[¶](#wx.lib.masked.ipaddrctrl.IpAddrCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window parent. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*string*) – value to be shown;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the window style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – this is mainly provided for data-transfer, as control does
its own validation;
* **name** (*string*) – the window name;
* **setupEventHandling** (*boolean*) – setup event handling by default.






            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def GetAddress(self) -> None:
        """ 

`GetAddress`(*self*)[¶](#wx.lib.masked.ipaddrctrl.IpAddrCtrl.GetAddress "Permalink to this definition")
Returns the control value, with any spaces removed.




            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def OnDot(self, event) -> None:
        """ 

`OnDot`(*self*, *event*)[¶](#wx.lib.masked.ipaddrctrl.IpAddrCtrl.OnDot "Permalink to this definition")
Defines what action to take when the ‘.’ character is typed in the
control. By default, the current field is right-justified, and the
cursor is placed in the next field.




            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """

    def SetValue(self, value: str) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.masked.ipaddrctrl.IpAddrCtrl.SetValue "Permalink to this definition")
Takes a string value, validates it for a valid IP address,
splits it into an array of 4 fields, justifies it
appropriately, and inserts it into the control.
Invalid values will raise a ValueError exception.



Parameters
**value** (*string*) – the IP address in the form ‘000.000.000.000’






            Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrl.html
        """



class IpAddrCtrlAccessorsMixin:
    """ Defines IpAddrCtrl’s list of attributes having their own
Get/Set functions, exposing only those that make sense for
an IP address control.




        Source: https://docs.wxpython.org/wx.lib.masked.ipaddrctrl.IpAddrCtrlAccessorsMixin.html
    """


