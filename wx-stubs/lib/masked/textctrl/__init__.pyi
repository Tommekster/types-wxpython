# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class BaseMaskedTextCtrl(TextCtrl,MaskedEditMixin):
    """ This is the primary derivation from MaskedEditMixin. It provides
a general masked text control that can be configured with different
masks.


However, this is done with an extra level of inheritance, so that
“general” classes like masked.TextCtrl can have all possible attributes,
while derived classes, like masked.TimeCtrl and masked.NumCtrl
can prevent exposure of those optional attributes of their base
class that do not make sense for their derivation. Therefore,
we define:



```
BaseMaskedTextCtrl(TextCtrl, MaskedEditMixin)

```


and:



```
masked.TextCtrl(BaseMaskedTextCtrl, MaskedEditAccessorsMixin).

```


This allows us to then derive:



```
masked.NumCtrl( BaseMaskedTextCtrl )

```


and not have to expose all the same accessor functions for the
derived control when they don’t all make sense for it.


In practice, BaseMaskedTextCtrl should never be instantiated directly,
but should only be used in derived classes.


  


        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.TE_PROCESS_TAB, validator=wx.DefaultValidator, name = 'maskedTextCtrl', setupEventHandling = True, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = ''*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *style = wx.TE\_PROCESS\_TAB*, *validator=wx.DefaultValidator*, *name = 'maskedTextCtrl'*, *setupEventHandling = True*, *\*\*kwargs*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.__init__ "Permalink to this definition")
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






            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def ChangeValue(self, value: str) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.ChangeValue "Permalink to this definition")
Provided to accommodate similar functionality added to base
control in wxPython 2.7.1.1.



Parameters
**value** (*string*) – new value for control, this will not fire an event






            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.Clear "Permalink to this definition")
Blanks the current control value by replacing it with the default value.




            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.Cut "Permalink to this definition")
This function redefines the externally accessible `TextCtrl.Cut`
to be a smart “erase” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def IsEmpty(*args, **kw) -> None:
        """ 

`IsEmpty`(*\*args*, *\*\*kw*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.IsEmpty "Permalink to this definition")
IsEmpty() -> bool


Returns true if the control is currently empty.




            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def IsModified(self) -> None:
        """ 

`IsModified`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.IsModified "Permalink to this definition")
This function overrides the raw `TextCtrl.IsModified` method,
because the masked edit mixin uses SetValue to change the value, which
doesn’t modify the state of this attribute. So, the derived control
keeps track on each keystroke to see if the value changes, and if so,
it’s been modified.




            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def ModifyValue(self, value, use_change_value=False) -> None:
        """ 

`ModifyValue`(*self*, *value*, *use\_change\_value=False*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.ModifyValue "Permalink to this definition")
This factored function of common code does the bulk of the work for
SetValue and ChangeValue.



Parameters
* **value** (*string*) – new value for control
* **use\_change\_value** (*boolean*) – if `True` uses `ChangeValue`






            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.Paste "Permalink to this definition")
This function redefines the externally accessible `TextCtrl.Paste`
to be a smart “paste” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Refresh(self) -> None:
        """ 

`Refresh`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.Refresh "Permalink to this definition")
This function redefines the externally accessible `TextCtrl.Refresh`
to validate the contents of the masked control as it refreshes.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def SetFont(self, *args, **kwargs) -> None:
        """ 

`SetFont`(*self*, *\*args*, *\*\*kwargs*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.SetFont "Permalink to this definition")
Set the font, then recalculate control size, if appropriate.


see `TextCtrl.SetFont` for valid arguments




            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def SetValue(self, value) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.SetValue "Permalink to this definition")
This function redefines the externally accessible `TextCtrl.SetValue`
to be a smart “paste” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """

    def Undo(self) -> None:
        """ 

`Undo`(*self*)[¶](#wx.lib.masked.textctrl.BaseMaskedTextCtrl.Undo "Permalink to this definition")
This function defines the undo operation for the control.
(The default undo is 1-deep.)




            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.BaseMaskedTextCtrl.html
        """



class PreMaskedTextCtrl(BaseMaskedTextCtrl,MaskedEditAccessorsMixin):
    """ This class exists to support the use of XRC subclassing.


  


        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.masked.textctrl.PreMaskedTextCtrl.__init__ "Permalink to this definition")
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






            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
        """

    def OnCreate(self, evt) -> None:
        """ 

`OnCreate`(*self*, *evt*)[¶](#wx.lib.masked.textctrl.PreMaskedTextCtrl.OnCreate "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.textctrl.PreMaskedTextCtrl.html
        """



class TextCtrl(BaseMaskedTextCtrl,MaskedEditAccessorsMixin):
    """ The “user-visible” masked text control; it is identical to the
BaseMaskedTextCtrl class it’s derived from.
(This extra level of inheritance allows us to add the generic
set of masked edit parameters only to this class while allowing
other classes to derive from the “base” masked text control,
and provide a smaller set of valid accessor functions.)
See BaseMaskedTextCtrl for available methods.




        Source: https://docs.wxpython.org/wx.lib.masked.textctrl.TextCtrl.html
    """


