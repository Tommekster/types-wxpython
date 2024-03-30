# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class BaseMaskedComboBox(ComboBox,MaskedEditMixin):
    """ Base class for generic masked edit comboboxes; allows auto-complete of values.
It is not meant to be instantiated directly, but rather serves as a base class
for any subsequent refinements.


  


        Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
    """
    def __init__(self, parent, id=-1, value = '', pos = wx.DefaultPosition, size = wx.DefaultSize, choices = [], style = wx.CB_DROPDOWN, validator = wx.DefaultValidator, name = "maskedComboBox", setupEventHandling = True, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *value = ''*, *pos = wx.DefaultPosition*, *size = wx.DefaultSize*, *choices = []*, *style = wx.CB\_DROPDOWN*, *validator = wx.DefaultValidator*, *name = "maskedComboBox"*, *setupEventHandling = True*, *\*\*kwargs*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window parent. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*string*) – value to be shown;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **choices** (*list*) – a list of valid choices;
* **style** (*integer*) – the window style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – this is mainly provided for data-transfer, as control does
its own validation;
* **name** (*string*) – the window name;
* **setupEventHandling** (*boolean*) – setup event handling by default.






            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Append(self, choice, clientData=None) -> None:
        """ 

`Append`(*self*, *choice*, *clientData=None*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Append "Permalink to this definition")
This base control function override is necessary so the control can keep
track of any additions to the list of choices, because [`ComboBox`](wx.lib.masked.combobox.ComboBox.html#wx.lib.masked.combobox.ComboBox "wx.lib.masked.combobox.ComboBox")
doesn’t have an accessor for the choice list. The code here is the same
as in the SetParameters() mixin function, but is done for the individual
value as appended, so the list can be built incrementally without speed
penalty.




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def AppendItems(self, choices) -> None:
        """ 

`AppendItems`(*self*, *choices*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.AppendItems "Permalink to this definition")
`AppendItems` is handled in terms
of `lib.masked.combobox.ComboBox.Append`, to avoid code replication.




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Clear "Permalink to this definition")
This base control function override is necessary so the derived control
can keep track of any additions to the list of choices, because
[`ComboBox`](wx.lib.masked.combobox.ComboBox.html#wx.lib.masked.combobox.ComboBox "wx.lib.masked.combobox.ComboBox") doesn’t have an accessor for the choice list.




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Cut "Permalink to this definition")
This function redefines the externally accessible `ComboBox.Cut`
to be a smart “erase” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def GetMark(self) -> None:
        """ 

`GetMark`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.GetMark "Permalink to this definition")
GetTextSelection() -> (from, to)


Gets the current selection span.




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def IsEmpty(*args, **kw) -> None:
        """ 

`IsEmpty`(*\*args*, *\*\*kw*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.IsEmpty "Permalink to this definition")
IsEmpty() -> bool


Returns true if the control is empty or false if it has some items.




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def OnWindowDestroy(self, event) -> None:
        """ 

`OnWindowDestroy`(*self*, *event*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.OnWindowDestroy "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Paste "Permalink to this definition")
This function redefines the externally accessible `ComboBox.Paste`
to be a smart “paste” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Refresh(self) -> None:
        """ 

`Refresh`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Refresh "Permalink to this definition")
This function redefines the externally accessible `ComboBox.Refresh`
to validate the contents of the masked control as it refreshes.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetFont(self, *args, **kwargs) -> None:
        """ 

`SetFont`(*self*, *\*args*, *\*\*kwargs*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.SetFont "Permalink to this definition")
Set the font, then recalculate control size, if appropriate.


see `ComboBox.SetFont` for valid arguments




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetSelection(self, index: int) -> None:
        """ 

`SetSelection`(*self*, *index*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.SetSelection "Permalink to this definition")
Necessary override for bookkeeping on choice selection, to keep current
value current.



Parameters
**index** (*integer*) – index to choice item to be set






            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def SetValue(self, value) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.SetValue "Permalink to this definition")
This function redefines the externally accessible `ComboBox.SetValue`
to be a smart “paste” of the text in question, so as not to corrupt the
masked control.



Note


This must be done in the class derived from the base wx control.





            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """

    def Undo(self) -> None:
        """ 

`Undo`(*self*)[¶](#wx.lib.masked.combobox.BaseMaskedComboBox.Undo "Permalink to this definition")
This function defines the undo operation for the control.
(The default undo is 1-deep.)




            Source: https://docs.wxpython.org/wx.lib.masked.combobox.BaseMaskedComboBox.html
        """



class ComboBox(BaseMaskedComboBox,MaskedEditAccessorsMixin):
    """ The “user-visible” masked combobox control, this class is
identical to the BaseMaskedComboBox class it’s derived from.
(This extra level of inheritance allows us to add the generic
set of masked edit parameters only to this class while allowing
other classes to derive from the “base” masked combobox control,
and provide a smaller set of valid accessor functions.)
See BaseMaskedComboBox for available methods.




        Source: https://docs.wxpython.org/wx.lib.masked.combobox.ComboBox.html
    """


class PreMaskedComboBox(BaseMaskedComboBox,MaskedEditAccessorsMixin):
    """ This class exists to support the use of XRC subclassing.


  


        Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.masked.combobox.PreMaskedComboBox.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window parent. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **value** (*string*) – value to be shown;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **choices** (*list*) – a list of valid choices;
* **style** (*integer*) – the window style;
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – this is mainly provided for data-transfer, as control does
its own validation;
* **name** (*string*) – the window name;
* **setupEventHandling** (*boolean*) – setup event handling by default.






            Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
        """

    def OnCreate(self, evt) -> None:
        """ 

`OnCreate`(*self*, *evt*)[¶](#wx.lib.masked.combobox.PreMaskedComboBox.OnCreate "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.combobox.PreMaskedComboBox.html
        """



