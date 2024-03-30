# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class FontSelect(GenButton):
    """ A generic button, and base class for the other generic buttons.


  


        Source: https://docs.wxpython.org/wx.lib.analogclock.lib_setup.fontselect.FontSelect.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *size=(75*, *21)*, *value=None*)[¶](#wx.lib.analogclock.lib_setup.fontselect.FontSelect.__init__ "Permalink to this definition")
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





            Source: https://docs.wxpython.org/wx.lib.analogclock.lib_setup.fontselect.FontSelect.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.analogclock.lib_setup.fontselect.FontSelect.GetValue "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.analogclock.lib_setup.fontselect.FontSelect.html
        """

    def OnClick(self, event) -> None:
        """ 

`OnClick`(*self*, *event*)[¶](#wx.lib.analogclock.lib_setup.fontselect.FontSelect.OnClick "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.analogclock.lib_setup.fontselect.FontSelect.html
        """

    def SetValue(self, value) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.analogclock.lib_setup.fontselect.FontSelect.SetValue "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.analogclock.lib_setup.fontselect.FontSelect.html
        """



