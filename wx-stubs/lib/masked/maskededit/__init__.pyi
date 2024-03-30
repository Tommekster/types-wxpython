# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class MaskedEditMixin:
    """ This class allows us to abstract the masked edit functionality that could
be associated with any text entry control. (eg. wx.TextCtrl, wx.ComboBox, etc.)
It forms the basis for all of the lib.masked controls.


  


        Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
    """
    def __init__(self, name = 'MaskedEdit', **kwargs) -> None:
        """ 

`__init__`(*self*, *name = 'MaskedEdit'*, *\*\*kwargs*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.__init__ "Permalink to this definition")
This is the “constructor” for setting up the mixin variable parameters for the composite class.




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def ClearValue(self) -> None:
        """ 

`ClearValue`(*self*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.ClearValue "Permalink to this definition")
Blanks the current control value by replacing it with the default value.




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def ClearValueAlt(self) -> None:
        """ 

`ClearValueAlt`(*self*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.ClearValueAlt "Permalink to this definition")
Blanks the current control value by replacing it with the default value.
Using ChangeValue, so not to fire a change event




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetCtrlParameter(self, paramname) -> None:
        """ 

`GetCtrlParameter`(*self*, *paramname*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.GetCtrlParameter "Permalink to this definition")
Routine for retrieving the value of any given parameter




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetFieldParameter(self, field_index, paramname) -> None:
        """ 

`GetFieldParameter`(*self*, *field\_index*, *paramname*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.GetFieldParameter "Permalink to this definition")
Routine provided for getting a parameter of an individual field.




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetMaskParameter(self, paramname) -> None:
        """ 

`GetMaskParameter`(*self*, *paramname*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.GetMaskParameter "Permalink to this definition")
old name for the GetCtrlParameters function (DEPRECATED)




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def GetPlainValue(self, candidate=None) -> None:
        """ 

`GetPlainValue`(*self*, *candidate=None*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.GetPlainValue "Permalink to this definition")
Returns control’s value stripped of the template text.
plainvalue = MaskedEditMixin.GetPlainValue()




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsDefault(self, value=None) -> None:
        """ 

`IsDefault`(*self*, *value=None*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.IsDefault "Permalink to this definition")
Returns `True` if the value specified (or the value of the control if not specified)
is equal to the default value.




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsEmpty(self, value=None) -> None:
        """ 

`IsEmpty`(*self*, *value=None*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.IsEmpty "Permalink to this definition")
Returns `True` if control is equal to an empty value.
(Empty means all editable positions in the template == fillChar.)




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def IsValid(self, value=None) -> None:
        """ 

`IsValid`(*self*, *value=None*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.IsValid "Permalink to this definition")
Indicates whether the value specified (or the current value of the control
if not specified) is considered valid.




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetBackgroundColour(self, colour) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.SetBackgroundColour "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetCtrlParameters(self, **kwargs) -> None:
        """ 

`SetCtrlParameters`(*self*, *\*\*kwargs*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.SetCtrlParameters "Permalink to this definition")
This public function can be used to set individual or multiple masked edit
parameters after construction. (See maskededit module overview for the list
of valid parameters.)




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetFieldParameters(self, field_index, **kwargs) -> None:
        """ 

`SetFieldParameters`(*self*, *field\_index*, *\*\*kwargs*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.SetFieldParameters "Permalink to this definition")
Routine provided to modify the parameters of a given field.
Because changes to fields can affect the overall control,
direct access to the fields is prevented, and the control
is always “reconfigured” after setting a field parameter.
(See maskededit module overview for the list of valid field-level
parameters.)




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetForegroundColour(self, colour) -> None:
        """ 

`SetForegroundColour`(*self*, *colour*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.SetForegroundColour "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """

    def SetMaskParameters(self, **kwargs) -> None:
        """ 

`SetMaskParameters`(*self*, *\*\*kwargs*)[¶](#wx.lib.masked.maskededit.MaskedEditMixin.SetMaskParameters "Permalink to this definition")
old name for the SetCtrlParameters function (DEPRECATED)




            Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditMixin.html
        """



class MaskedEditAccessorsMixin:
    """ To avoid a ton of boiler-plate, and to automate the getter/setter generation
for each valid control parameter so we never forget to add the functions when
adding parameters, this class programmatically adds the masked edit mixin
parameters to itself.
(This makes it easier for Designers like Boa to deal with masked controls.)


To further complicate matters, this is done with an extra level of inheritance,
so that “general” classes like masked.TextCtrl can have all possible attributes,
while derived classes, like masked.TimeCtrl and masked.NumCtrl can prevent
exposure of those optional attributes of their base class that do not make
sense for their derivation.



Therefore, we define:BaseMaskedTextCtrl(TextCtrl, MaskedEditMixin)



andmasked.TextCtrl(BaseMaskedTextCtrl, MaskedEditAccessorsMixin).



This allows us to then derive:masked.NumCtrl( BaseMaskedTextCtrl )




and not have to expose all the same accessor functions for the
derived control when they don’t all make sense for it.




        Source: https://docs.wxpython.org/wx.lib.masked.maskededit.MaskedEditAccessorsMixin.html
    """


