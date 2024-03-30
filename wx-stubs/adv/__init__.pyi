# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Button, VisualAttributes, Panel, BitmapButton, _ListCtrl, ListCtrl, ComboCtrl, ItemContainer, Coord, ComboBox, Size, Bitmap, CommandEvent, DateTime, Rect, Window, Control, Colour, Dialog, BookCtrlBase, Sizer, _Bitmap, Event, _Rect, _Size, EvtHandler, Menu, Frame, HelpControllerBase, Object, Point, NotifyEvent, Image, WeekDay, _Font, Font, ObjectRefData

class CommandLinkButton(Button):
    """ **Possible constructors**:



```
CommandLinkButton()

CommandLinkButton(parent, id=ID_ANY, mainLabel="", note="",
                  pos=DefaultPosition, size=DefaultSize, style=0,
                  validator=DefaultValidator, name=ButtonNameStr)

```


Objects of this class are similar in appearance to the normal
Buttons but are similar to the links in a web page in functionality.


  


        Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.CommandLinkButton.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


Use [`Create`](#wx.adv.CommandLinkButton.Create "wx.adv.CommandLinkButton.Create") to really create the control.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, mainLabel=””, note=””, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr)*


Constructor really creating a command Link button.


The button will be decorated with stock icons under GTK+ 2.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Button identifier. A value of `wx.ID_ANY` indicates a default value.
* **mainLabel** (*string*) – First line of text on the button, typically the label of an action that will be made when the button is pressed.
* **note** (*string*) – Second line of text describing the action performed when the button is pressed.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Button position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Button size. If the default size is specified then the button is sized appropriately for the text.
* **style** (*long*) – Window style. See  [wx.Button](wx.Button.html#wx-button) class description.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Window validator.
* **name** (*string*) – Window name.





See also


[`Create`](#wx.adv.CommandLinkButton.Create "wx.adv.CommandLinkButton.Create") ,  [wx.Validator](wx.Validator.html#wx-validator)





---

  





            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def Create(self, parent, id=ID_ANY, mainLabel="", note="", pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ButtonNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *mainLabel=""*, *note=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *validator=DefaultValidator*, *name=ButtonNameStr*)[¶](#wx.adv.CommandLinkButton.Create "Permalink to this definition")
Button creation function for two-step creation.


For more details, see  [wx.adv.CommandLinkButton](#wx-adv-commandlinkbutton).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **mainLabel** (*string*) –
* **note** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.CommandLinkButton.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetLabel(self) -> str:
        """ 

`GetLabel`(*self*)[¶](#wx.adv.CommandLinkButton.GetLabel "Permalink to this definition")
Returns the string label for the button.



Return type
`string`



Returns
A string with the main label and note concatenated together with a newline separating them.





See also


[`SetLabel`](#wx.adv.CommandLinkButton.SetLabel "wx.adv.CommandLinkButton.SetLabel")





            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetMainLabel(self) -> str:
        """ 

`GetMainLabel`(*self*)[¶](#wx.adv.CommandLinkButton.GetMainLabel "Permalink to this definition")
Returns the current main label.



Return type
`string`



Returns
Main label currently displayed.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def GetNote(self) -> str:
        """ 

`GetNote`(*self*)[¶](#wx.adv.CommandLinkButton.GetNote "Permalink to this definition")
Returns the currently used note.



Return type
`string`



Returns
Note currently displayed.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.adv.CommandLinkButton.SetLabel "Permalink to this definition")
Sets the string label and note for the button.



Parameters
**label** (*string*) – The label and note to set, with the two separated by the first newline or none to set a blank note.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetMainLabel(self, mainLabel: str) -> None:
        """ 

`SetMainLabel`(*self*, *mainLabel*)[¶](#wx.adv.CommandLinkButton.SetMainLabel "Permalink to this definition")
Changes the main label.



Parameters
**mainLabel** (*string*) – New main label to use.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetMainLabelAndNote(self, mainLabel, note) -> None:
        """ 

`SetMainLabelAndNote`(*self*, *mainLabel*, *note*)[¶](#wx.adv.CommandLinkButton.SetMainLabelAndNote "Permalink to this definition")
Sets a new main label and note for the button.


Neither of the arguments can be empty, if you need to change just the label or just the note, use [`SetMainLabel`](#wx.adv.CommandLinkButton.SetMainLabel "wx.adv.CommandLinkButton.SetMainLabel") or [`SetNote`](#wx.adv.CommandLinkButton.SetNote "wx.adv.CommandLinkButton.SetNote") instead of this function.



Parameters
* **mainLabel** (*string*) – New main label to use.
* **note** (*string*) – New note to use.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    def SetNote(self, note: str) -> None:
        """ 

`SetNote`(*self*, *note*)[¶](#wx.adv.CommandLinkButton.SetNote "Permalink to this definition")
Changes the note.



Parameters
**note** (*string*) – New note to use.






            Source: https://docs.wxpython.org/wx.adv.CommandLinkButton.html
        """

    Label: str  # `Label`[¶](#wx.adv.CommandLinkButton.Label "Permalink to this definition")See [`GetLabel`](#wx.adv.CommandLinkButton.GetLabel "wx.adv.CommandLinkButton.GetLabel") and [`SetLabel`](#wx.adv.CommandLinkButton.SetLabel "wx.adv.CommandLinkButton.SetLabel")
    MainLabel: str  # `MainLabel`[¶](#wx.adv.CommandLinkButton.MainLabel "Permalink to this definition")See [`GetMainLabel`](#wx.adv.CommandLinkButton.GetMainLabel "wx.adv.CommandLinkButton.GetMainLabel") and [`SetMainLabel`](#wx.adv.CommandLinkButton.SetMainLabel "wx.adv.CommandLinkButton.SetMainLabel")
    Note: str  # `Note`[¶](#wx.adv.CommandLinkButton.Note "Permalink to this definition")See [`GetNote`](#wx.adv.CommandLinkButton.GetNote "wx.adv.CommandLinkButton.GetNote") and [`SetNote`](#wx.adv.CommandLinkButton.SetNote "wx.adv.CommandLinkButton.SetNote")



ID_ANY: int

class EditableListBox(Panel):
    """ **Possible constructors**:



```
EditableListBox()

EditableListBox(parent, id=ID_ANY, label="", pos=DefaultPosition,
                size=DefaultSize, style=EL_DEFAULT_STYLE, name=EditableListBoxNameStr)

```


An editable listbox is composite control that lets the user easily
enter, delete and reorder a list of strings.


  


        Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.EditableListBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, label=””, pos=DefaultPosition, size=DefaultSize, style=EL\_DEFAULT\_STYLE, name=EditableListBoxNameStr)*


Constructor, creating and showing a list box.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Window identifier. The value `wx.ID_ANY` indicates a default value.
* **label** (*string*) – The text shown just before the list control.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position. If `wx.DefaultPosition` is specified then a default position is chosen.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. If `wx.DefaultSize` is specified then the window is sized appropriately.
* **style** (*long*) – Window style. See  [wx.adv.EditableListBox](#wx-adv-editablelistbox).
* **name** (*string*) – Window name.





See also


[`Create`](#wx.adv.EditableListBox.Create "wx.adv.EditableListBox.Create")





---

  





            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def Create(self, parent, id=ID_ANY, label="", pos=DefaultPosition, size=DefaultSize, style=EL_DEFAULT_STYLE, name=EditableListBoxNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *label=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=EL\_DEFAULT\_STYLE*, *name=EditableListBoxNameStr*)[¶](#wx.adv.EditableListBox.Create "Permalink to this definition")
Creates the editable listbox for two-step construction.


See  [wx.adv.EditableListBox](#wx-adv-editablelistbox) for further details.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **label** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.EditableListBox.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetDelButton(self) -> 'BitmapButton':
        """ 

`GetDelButton`(*self*)[¶](#wx.adv.EditableListBox.GetDelButton "Permalink to this definition")
Returns a reference to the delete button used in the EditableListBox.



Return type
*BitmapButton*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetDownButton(self) -> 'BitmapButton':
        """ 

`GetDownButton`(*self*)[¶](#wx.adv.EditableListBox.GetDownButton "Permalink to this definition")
Returns a reference to the down button used in the EditableListBox.



Return type
*BitmapButton*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetEditButton(self) -> 'BitmapButton':
        """ 

`GetEditButton`(*self*)[¶](#wx.adv.EditableListBox.GetEditButton "Permalink to this definition")
Returns a reference to the edit button used in the EditableListBox.



Return type
*BitmapButton*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetListCtrl(self) -> 'ListCtrl':
        """ 

`GetListCtrl`(*self*)[¶](#wx.adv.EditableListBox.GetListCtrl "Permalink to this definition")
Returns a reference to the listctrl used in the EditableListBox.



Return type
[`ListCtrl`](#wx.adv.EditableListBox.ListCtrl "wx.adv.EditableListBox.ListCtrl")






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetNewButton(self) -> 'BitmapButton':
        """ 

`GetNewButton`(*self*)[¶](#wx.adv.EditableListBox.GetNewButton "Permalink to this definition")
Returns a reference to the new button used in the EditableListBox.



Return type
*BitmapButton*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetStrings(self) -> list[str]:
        """ 

`GetStrings`(*self*)[¶](#wx.adv.EditableListBox.GetStrings "Permalink to this definition")
Returns a list of the current contents of the control.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def GetUpButton(self) -> 'BitmapButton':
        """ 

`GetUpButton`(*self*)[¶](#wx.adv.EditableListBox.GetUpButton "Permalink to this definition")
Returns a reference to the up button used in the EditableListBox.



Return type
*BitmapButton*






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    def SetStrings(self, strings: list[str]) -> None:
        """ 

`SetStrings`(*self*, *strings*)[¶](#wx.adv.EditableListBox.SetStrings "Permalink to this definition")
Replaces current contents with given strings.



Parameters
**strings** (*list of strings*) – 






            Source: https://docs.wxpython.org/wx.adv.EditableListBox.html
        """

    DelButton: 'BitmapButton'  # `DelButton`[¶](#wx.adv.EditableListBox.DelButton "Permalink to this definition")See [`GetDelButton`](#wx.adv.EditableListBox.GetDelButton "wx.adv.EditableListBox.GetDelButton")
    DownButton: 'BitmapButton'  # `DownButton`[¶](#wx.adv.EditableListBox.DownButton "Permalink to this definition")See [`GetDownButton`](#wx.adv.EditableListBox.GetDownButton "wx.adv.EditableListBox.GetDownButton")
    EditButton: 'BitmapButton'  # `EditButton`[¶](#wx.adv.EditableListBox.EditButton "Permalink to this definition")See [`GetEditButton`](#wx.adv.EditableListBox.GetEditButton "wx.adv.EditableListBox.GetEditButton")
    ListCtrl: '_ListCtrl'  # `ListCtrl`[¶](#wx.adv.EditableListBox.ListCtrl "Permalink to this definition")See [`GetListCtrl`](#wx.adv.EditableListBox.GetListCtrl "wx.adv.EditableListBox.GetListCtrl")
    NewButton: 'BitmapButton'  # `NewButton`[¶](#wx.adv.EditableListBox.NewButton "Permalink to this definition")See [`GetNewButton`](#wx.adv.EditableListBox.GetNewButton "wx.adv.EditableListBox.GetNewButton")
    Strings: list[str]  # `Strings`[¶](#wx.adv.EditableListBox.Strings "Permalink to this definition")See [`GetStrings`](#wx.adv.EditableListBox.GetStrings "wx.adv.EditableListBox.GetStrings") and [`SetStrings`](#wx.adv.EditableListBox.SetStrings "wx.adv.EditableListBox.SetStrings")
    UpButton: 'BitmapButton'  # `UpButton`[¶](#wx.adv.EditableListBox.UpButton "Permalink to this definition")See [`GetUpButton`](#wx.adv.EditableListBox.GetUpButton "wx.adv.EditableListBox.GetUpButton")



EL_ALLOW_NEW: int  # Allows the user to enter new strings.

EL_ALLOW_EDIT: int  # Allows the user to edit existing strings.

EL_ALLOW_DELETE: int  # Allows the user to delete existing strings.

EL_NO_REORDER: int  # Does not allow the user to reorder the strings.

EL_DEFAULT_STYLE: int  # Default style: EL_ALLOW_NEW|wxEL_ALLOW_EDIT|wxEL_ALLOW_DELETE. ^^

class OwnerDrawnComboBox(ComboCtrl,ItemContainer):
    """ **Possible constructors**:



```
OwnerDrawnComboBox()

OwnerDrawnComboBox(parent, id=ID_ANY, value="", pos=DefaultPosition,
                   size=DefaultSize, choices=[], style=0, validator=DefaultValidator,
                   name="comboBox")

```


OwnerDrawnComboBox is a combobox with owner-drawn list items.


  


        Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.OwnerDrawnComboBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, value=””, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=”comboBox”)*


Constructor, creating and showing a owner-drawn combobox.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Window identifier. The value `ID_ANY` indicates a default value.
* **value** (*string*) – Initial selection string. An empty string indicates no selection.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. If `wx.DefaultSize` is specified then the window is sized appropriately.
* **choices** (*list of strings*) – An array of strings with which to initialise the control.
* **style** (*long*) – Window style. See  [wx.adv.OwnerDrawnComboBox](#wx-adv-ownerdrawncombobox).
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Window validator.
* **name** (*string*) – Window name.





See also


[`Create`](#wx.adv.OwnerDrawnComboBox.Create "wx.adv.OwnerDrawnComboBox.Create") ,  [wx.Validator](wx.Validator.html#wx-validator)





---

  





            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=ComboBoxNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *value=""*, *pos=DefaultPosition*, *size=DefaultSize*, *choices=[]*, *style=0*, *validator=DefaultValidator*, *name=ComboBoxNameStr*)[¶](#wx.adv.OwnerDrawnComboBox.Create "Permalink to this definition")
Creates the combobox for two-step construction.


See  [wx.adv.OwnerDrawnComboBox](#wx-adv-ownerdrawncombobox) for further details.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **value** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **choices** (*list of strings*) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –



Return type
*bool*





Note


Derived classes should call or replace this function.





            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.OwnerDrawnComboBox.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def GetWidestItem(self) -> int:
        """ 

`GetWidestItem`(*self*)[¶](#wx.adv.OwnerDrawnComboBox.GetWidestItem "Permalink to this definition")
Returns index to the widest item in the list.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def GetWidestItemWidth(self) -> int:
        """ 

`GetWidestItemWidth`(*self*)[¶](#wx.adv.OwnerDrawnComboBox.GetWidestItemWidth "Permalink to this definition")
Returns width of the widest item in the list.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def IsListEmpty(self) -> bool:
        """ 

`IsListEmpty`(*self*)[¶](#wx.adv.OwnerDrawnComboBox.IsListEmpty "Permalink to this definition")
Returns `True` if the list of combobox choices is empty.


Use this method instead of (not available in this class) `IsEmpty` to test if the list of items is empty.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def IsTextEmpty(self) -> bool:
        """ 

`IsTextEmpty`(*self*)[¶](#wx.adv.OwnerDrawnComboBox.IsTextEmpty "Permalink to this definition")
Returns `True` if the text of the combobox is empty.


Use this method instead of (not available in this class) `IsEmpty` to test if the text currently entered into the combobox is empty.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnDrawBackground(self, dc, rect, item, flags) -> None:
        """ 

`OnDrawBackground`(*self*, *dc*, *rect*, *item*, *flags*)[¶](#wx.adv.OwnerDrawnComboBox.OnDrawBackground "Permalink to this definition")
This method is used to draw the items background and, maybe, a border around it.


The base class version implements a reasonable default behaviour which consists in drawing the selected item with the standard background colour and drawing a border around the item if it is either selected or current.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **item** (*int*) –
* **flags** (*int*) –





Note


flags has the same meaning as with [`OnDrawItem`](#wx.adv.OwnerDrawnComboBox.OnDrawItem "wx.adv.OwnerDrawnComboBox.OnDrawItem") .





            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnDrawItem(self, dc, rect, item, flags) -> None:
        """ 

`OnDrawItem`(*self*, *dc*, *rect*, *item*, *flags*)[¶](#wx.adv.OwnerDrawnComboBox.OnDrawItem "Permalink to this definition")
The derived class may implement this function to actually draw the item with the given index on the provided DC.


If function is not implemented, the item text is simply drawn, as if the control was a normal combobox.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to use for drawing
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The bounding rectangle for the item being drawn (DC clipping region is set to this rectangle before calling this function)
* **item** (*int*) – The index of the item to be drawn
* **flags** (*int*) – A combination of the  [wx.adv.OwnerDrawnComboBoxPaintingFlags](wx.adv.OwnerDrawnComboBoxPaintingFlags.enumeration.html#wx-adv-ownerdrawncomboboxpaintingflags) enumeration values.






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnMeasureItem(self, item: int) -> 'Coord':
        """ 

`OnMeasureItem`(*self*, *item*)[¶](#wx.adv.OwnerDrawnComboBox.OnMeasureItem "Permalink to this definition")
The derived class may implement this method to return the height of the specified item (in pixels).


The default implementation returns text height, as if this control was a normal combobox.



Parameters
**item** (*int*) – 



Return type
*wx.Coord*






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    def OnMeasureItemWidth(self, item: int) -> 'Coord':
        """ 

`OnMeasureItemWidth`(*self*, *item*)[¶](#wx.adv.OwnerDrawnComboBox.OnMeasureItemWidth "Permalink to this definition")
The derived class may implement this method to return the width of the specified item (in pixels).


If -1 is returned, then the item text width is used.


The default implementation returns -1.



Parameters
**item** (*int*) – 



Return type
*wx.Coord*






            Source: https://docs.wxpython.org/wx.adv.OwnerDrawnComboBox.html
        """

    WidestItem: int  # `WidestItem`[¶](#wx.adv.OwnerDrawnComboBox.WidestItem "Permalink to this definition")See [`GetWidestItem`](#wx.adv.OwnerDrawnComboBox.GetWidestItem "wx.adv.OwnerDrawnComboBox.GetWidestItem")
    WidestItemWidth: int  # `WidestItemWidth`[¶](#wx.adv.OwnerDrawnComboBox.WidestItemWidth "Permalink to this definition")See [`GetWidestItemWidth`](#wx.adv.OwnerDrawnComboBox.GetWidestItemWidth "wx.adv.OwnerDrawnComboBox.GetWidestItemWidth")



ODCB_DCLICK_CYCLES: int  # Double-clicking cycles item if wx.CB_READONLY is also used. Synonymous with wx.CC_SPECIAL_DCLICK.

ODCB_STD_CONTROL_PAINT: int  # Control itself is not custom painted using OnDrawItem. Even if this style is not used, writable   wx.adv.OwnerDrawnComboBox  is never custom painted unless SetCustomPaintWidth  is called. ^^

EVT_COMBOBOX: int  # Process a wxEVT_COMBOBOX event, when an item on the list is selected. Note that calling GetValue  returns the new value of selection. ^^

CB_READONLY: int

CC_SPECIAL_DCLICK: int

class BitmapComboBox(ComboBox):
    """ **Possible constructors**:



```
BitmapComboBox()

BitmapComboBox(parent, id=ID_ANY, value="", pos=DefaultPosition,
               size=DefaultSize, choices=[], style=0, validator=DefaultValidator,
               name=BitmapComboBoxNameStr)

```


A combobox that displays bitmap in front of the list items.


  


        Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.BitmapComboBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, value=””, pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=BitmapComboBoxNameStr)*


Constructor, creating and showing a combobox.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Window identifier. The value `wx.ID_ANY` indicates a default value.
* **value** (*string*) – Initial selection string. An empty string indicates no selection.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size.
* **choices** (*list of strings*) – A list of strings with which to initialise the control.
* **style** (*long*) – The window style, see `CB_` flags.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Validator which can be used for additional data checks.
* **name** (*string*) – Control name.





See also


[`Create`](#wx.adv.BitmapComboBox.Create "wx.adv.BitmapComboBox.Create") ,  [wx.Validator](wx.Validator.html#wx-validator)





---

  





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Append(self, *args, **kw) -> int:
        """ 

`Append`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.BitmapComboBox.Append "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Append** *(self, item, bitmap=NullBitmap)*


Adds the item to the end of the combo box.



Parameters
* **item** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –



Return type
*int*






---

  



**Append** *(self, item, bitmap, clientData)*


Adds the item to the end of the combo box, associating the given typed client data pointer *clientData* with the item.



Parameters
* **item** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **clientData** (*ClientData*) –



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Create(self, parent, id=ID_ANY, value="", pos=DefaultPosition, size=DefaultSize, choices=[], style=0, validator=DefaultValidator, name=BitmapComboBoxNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *value=""*, *pos=DefaultPosition*, *size=DefaultSize*, *choices=[]*, *style=0*, *validator=DefaultValidator*, *name=BitmapComboBoxNameStr*)[¶](#wx.adv.BitmapComboBox.Create "Permalink to this definition")
Creates the combobox for two-step construction.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **value** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **choices** (*list of strings*) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Dismiss(self) -> None:
        """ 

`Dismiss`(*self*)[¶](#wx.adv.BitmapComboBox.Dismiss "Permalink to this definition")
Hides the list box portion of the combo box.


Currently this method is implemented in wxMSW, wxGTK and OSX/Cocoa.


Notice that calling this function will generate a `wxEVT_COMBOBOX_CLOSEUP` event except under wxOSX where generation of this event is not supported at all.



New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def FindString(self, string, caseSensitive=False) -> int:
        """ 

`FindString`(*self*, *string*, *caseSensitive=False*)[¶](#wx.adv.BitmapComboBox.FindString "Permalink to this definition")
Finds an item whose label matches the given string.



Parameters
* **string** (*string*) – String to find.
* **caseSensitive** (*bool*) – Whether search is case sensitive (default is not).



Return type
*int*



Returns
The zero-based position of the item, or `wx.NOT_FOUND` if the string was not found.






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetBitmapSize(self) -> 'Size':
        """ 

`GetBitmapSize`(*self*)[¶](#wx.adv.BitmapComboBox.GetBitmapSize "Permalink to this definition")
Returns the size of the bitmaps used in the combo box.


If the combo box is empty, then `wx.DefaultSize` is returned.



Return type
`Size`






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.BitmapComboBox.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.adv.BitmapComboBox.GetCount "Permalink to this definition")
Returns the number of items in the control.



Return type
*int*





See also


[`IsEmpty`](wx.TextEntry.html#wx.TextEntry.IsEmpty "wx.TextEntry.IsEmpty")





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetInsertionPoint(self) -> int:
        """ 

`GetInsertionPoint`(*self*)[¶](#wx.adv.BitmapComboBox.GetInsertionPoint "Permalink to this definition")
Same as [`wx.TextEntry.GetInsertionPoint`](wx.TextEntry.html#wx.TextEntry.GetInsertionPoint "wx.TextEntry.GetInsertionPoint") .



Return type
*long*





Note


Under wxMSW, this function always returns 0 if the combobox doesn’t have the focus.





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetItemBitmap(self, n: int) -> 'Bitmap':
        """ 

`GetItemBitmap`(*self*, *n*)[¶](#wx.adv.BitmapComboBox.GetItemBitmap "Permalink to this definition")
Returns the bitmap of the item with the given index.



Parameters
**n** (*int*) – 



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetSelection(self) -> int:
        """ 

`GetSelection`(*self*)[¶](#wx.adv.BitmapComboBox.GetSelection "Permalink to this definition")
Returns the index of the selected item or `NOT_FOUND` if no item is selected.



Return type
*int*



Returns
The position of the current selection.





See also


[`SetSelection`](#wx.adv.BitmapComboBox.SetSelection "wx.adv.BitmapComboBox.SetSelection") , [`GetStringSelection`](wx.TextEntry.html#wx.TextEntry.GetStringSelection "wx.TextEntry.GetStringSelection")





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetTextSelection(self) -> tuple:
        """ 

`GetTextSelection`(*self*)[¶](#wx.adv.BitmapComboBox.GetTextSelection "Permalink to this definition")
Gets the current selection span.


If the returned values are equal, there was no selection. Please note that the indices returned may be used with the other  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) methods but don’t necessarily represent the correct indices into the string returned by [`GetValue`](wx.TextEntry.html#wx.TextEntry.GetValue "wx.TextEntry.GetValue") for multiline controls under Windows (at least,) you should use [`GetStringSelection`](wx.TextEntry.html#wx.TextEntry.GetStringSelection "wx.TextEntry.GetStringSelection") to get the selected text.



Return type
*tuple*






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def GetString(self, n: int) -> str:
        """ 

`GetString`(*self*, *n*)[¶](#wx.adv.BitmapComboBox.GetString "Permalink to this definition")
Returns the label of the item with the given index.


The index must be valid, i.e. less than the value returned by [`GetCount`](#wx.adv.BitmapComboBox.GetCount "wx.adv.BitmapComboBox.GetCount") , otherwise an assert is triggered. Notably, this function can’t be called if the control is empty.



Parameters
**n** (*int*) – The zero-based index.



Return type
`string`



Returns
The label of the item.






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Insert(self, *args, **kw) -> int:
        """ 

`Insert`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.BitmapComboBox.Insert "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Insert** *(self, item, bitmap, pos)*


Inserts the item into the list before *pos*.


Not valid for `CB_SORT` style, use [`Append`](#wx.adv.BitmapComboBox.Append "wx.adv.BitmapComboBox.Append") instead.



Parameters
* **item** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **pos** (*int*) –



Return type
*int*






---

  



**Insert** *(self, item, bitmap, pos, clientData)*


Inserts the item into the list before pos, associating the given typed client data pointer with the item.


Not valid for `CB_SORT` style, use [`Append`](#wx.adv.BitmapComboBox.Append "wx.adv.BitmapComboBox.Append") instead.



Parameters
* **item** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **pos** (*int*) –
* **clientData** (*ClientData*) –



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def IsListEmpty(self) -> bool:
        """ 

`IsListEmpty`(*self*)[¶](#wx.adv.BitmapComboBox.IsListEmpty "Permalink to this definition")
Returns `True` if the list of combobox choices is empty.


Use this method instead of (not available in this class) [`IsEmpty`](wx.TextEntry.html#wx.TextEntry.IsEmpty "wx.TextEntry.IsEmpty") to test if the list of items is empty.



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def IsTextEmpty(self) -> bool:
        """ 

`IsTextEmpty`(*self*)[¶](#wx.adv.BitmapComboBox.IsTextEmpty "Permalink to this definition")
Returns `True` if the text of the combobox is empty.


Use this method instead of (not available in this class) [`IsEmpty`](wx.TextEntry.html#wx.TextEntry.IsEmpty "wx.TextEntry.IsEmpty") to test if the text currently entered into the combobox is empty.



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def Popup(self) -> None:
        """ 

`Popup`(*self*)[¶](#wx.adv.BitmapComboBox.Popup "Permalink to this definition")
Shows the list box portion of the combo box.


Currently this method is implemented in wxMSW, wxGTK and OSX/Cocoa.


Notice that calling this function will generate a `wxEVT_COMBOBOX_DROPDOWN` event except under wxOSX where generation of this event is not supported at all.



New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetItemBitmap(self, n, bitmap) -> None:
        """ 

`SetItemBitmap`(*self*, *n*, *bitmap*)[¶](#wx.adv.BitmapComboBox.SetItemBitmap "Permalink to this definition")
Sets the bitmap for the given item.



Parameters
* **n** (*int*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetSelection(self, *args, **kw) -> None:
        """ 

`SetSelection`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.BitmapComboBox.SetSelection "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetSelection** *(self, from\_, to\_)*


Same as [`wx.TextEntry.SetSelection`](wx.TextEntry.html#wx.TextEntry.SetSelection "wx.TextEntry.SetSelection") .



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –






---

  



**SetSelection** *(self, n)*


Sets the selection to the given item *n* or removes the selection entirely if *n* == `NOT_FOUND` .


Note that this does not cause any command events to be emitted nor does it deselect any other items in the controls which support multiple selections.



Parameters
**n** (*int*) – The string position to select, starting from zero.





See also


[`SetString`](#wx.adv.BitmapComboBox.SetString "wx.adv.BitmapComboBox.SetString") , `SetStringSelection`





---

  





            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetString(self, n, text) -> None:
        """ 

`SetString`(*self*, *n*, *text*)[¶](#wx.adv.BitmapComboBox.SetString "Permalink to this definition")
Changes the text of the specified combobox item.


Notice that if the item is the currently selected one, i.e. if its text is displayed in the text part of the combobox, then the text is also replaced with the new *text*.



Parameters
* **n** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetTextSelection(self, from_, to_) -> None:
        """ 

`SetTextSelection`(*self*, *from\_*, *to\_*)[¶](#wx.adv.BitmapComboBox.SetTextSelection "Permalink to this definition")
Same as [`wx.TextEntry.SetSelection`](wx.TextEntry.html#wx.TextEntry.SetSelection "wx.TextEntry.SetSelection") .



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    def SetValue(self, text: str) -> None:
        """ 

`SetValue`(*self*, *text*)[¶](#wx.adv.BitmapComboBox.SetValue "Permalink to this definition")
Sets the text for the combobox text field.


For normal, editable comboboxes with a text entry field calling this method will generate a `wxEVT_TEXT` event, consistently with [`wx.TextEntry.SetValue`](wx.TextEntry.html#wx.TextEntry.SetValue "wx.TextEntry.SetValue") behaviour, use [`wx.TextEntry.ChangeValue`](wx.TextEntry.html#wx.TextEntry.ChangeValue "wx.TextEntry.ChangeValue") if this is undesirable.


For controls with `CB_READONLY` style the method behaves somewhat differently: the string must be in the combobox choices list (the check for this is case-insensitive) and `wxEVT_TEXT` is *not* generated in this case.



Parameters
**text** (*string*) – The text to set.






            Source: https://docs.wxpython.org/wx.adv.BitmapComboBox.html
        """

    BitmapSize: 'Size'  # `BitmapSize`[¶](#wx.adv.BitmapComboBox.BitmapSize "Permalink to this definition")See [`GetBitmapSize`](#wx.adv.BitmapComboBox.GetBitmapSize "wx.adv.BitmapComboBox.GetBitmapSize")
    Count: int  # `Count`[¶](#wx.adv.BitmapComboBox.Count "Permalink to this definition")See [`GetCount`](#wx.adv.BitmapComboBox.GetCount "wx.adv.BitmapComboBox.GetCount")
    InsertionPoint: int  # `InsertionPoint`[¶](#wx.adv.BitmapComboBox.InsertionPoint "Permalink to this definition")See [`GetInsertionPoint`](#wx.adv.BitmapComboBox.GetInsertionPoint "wx.adv.BitmapComboBox.GetInsertionPoint")
    Selection: int  # `Selection`[¶](#wx.adv.BitmapComboBox.Selection "Permalink to this definition")See [`GetSelection`](#wx.adv.BitmapComboBox.GetSelection "wx.adv.BitmapComboBox.GetSelection") and [`SetSelection`](#wx.adv.BitmapComboBox.SetSelection "wx.adv.BitmapComboBox.SetSelection")



CB_SORT: int  # Sorts the entries in the list alphabetically.

TE_PROCESS_ENTER: int  # The control will generate the event wxEVT_TEXT_ENTER (otherwise pressing Enter key is either processed internally by the control or used for navigation between dialog controls). Windows only. ^^

EVT_TEXT: int  # Process a  wxEVT_TEXT   event, when the combobox text changes.

EVT_TEXT_ENTER: int  # Process a  wxEVT_TEXT_ENTER   event, when RETURN is pressed in the combobox. ^^

NOT_FOUND: int

class DateEvent(CommandEvent):
    """ **Possible constructors**:



```
DateEvent()

DateEvent(win, dt, type)

```


This event class holds information about a date change and is used
together with DatePickerCtrl.


  


        Source: https://docs.wxpython.org/wx.adv.DateEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.DateEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, win, dt, type)*



Parameters
* **win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **type** (*wx.EventType*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def GetDate(self) -> 'DateTime':
        """ 

`GetDate`(*self*)[¶](#wx.adv.DateEvent.GetDate "Permalink to this definition")
Returns the date.



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def PyGetDate(self) -> None:
        """ 

`PyGetDate`(*self*)[¶](#wx.adv.DateEvent.PyGetDate "Permalink to this definition")
Return the date as a Python datetime.date object.




            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    def SetDate(self, date: 'DateTime') -> None:
        """ 

`SetDate`(*self*, *date*)[¶](#wx.adv.DateEvent.SetDate "Permalink to this definition")
Sets the date carried by the event, normally only used by the library internally.



Parameters
**date** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 






            Source: https://docs.wxpython.org/wx.adv.DateEvent.html
        """

    Date: 'DateTime'  # `Date`[¶](#wx.adv.DateEvent.Date "Permalink to this definition")See [`GetDate`](#wx.adv.DateEvent.GetDate "wx.adv.DateEvent.GetDate") and [`SetDate`](#wx.adv.DateEvent.SetDate "wx.adv.DateEvent.SetDate")



class HyperlinkEvent(CommandEvent):
    """ **Possible constructors**:



```
HyperlinkEvent(generator, id, url)

```


This event class is used for the events generated by HyperlinkCtrl.


  


        Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
    """
    def __init__(self, generator, id, url) -> None:
        """ 

`__init__`(*self*, *generator*, *id*, *url*)[¶](#wx.adv.HyperlinkEvent.__init__ "Permalink to this definition")
The constructor is not normally used by the user code.



Parameters
* **generator** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **id** (*int*) –
* **url** (*string*) –






            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    def GetURL(self) -> str:
        """ 

`GetURL`(*self*)[¶](#wx.adv.HyperlinkEvent.GetURL "Permalink to this definition")
Returns the URL of the hyperlink where the user has just clicked.



Return type
`string`






            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    def SetURL(self, url: str) -> None:
        """ 

`SetURL`(*self*, *url*)[¶](#wx.adv.HyperlinkEvent.SetURL "Permalink to this definition")
Sets the URL associated with the event.



Parameters
**url** (*string*) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkEvent.html
        """

    URL: str  # `URL`[¶](#wx.adv.HyperlinkEvent.URL "Permalink to this definition")See [`GetURL`](#wx.adv.HyperlinkEvent.GetURL "wx.adv.HyperlinkEvent.GetURL") and [`SetURL`](#wx.adv.HyperlinkEvent.SetURL "wx.adv.HyperlinkEvent.SetURL")



EVT_HYPERLINK: int  # User clicked on a hyperlink. ^^

class SashEvent(CommandEvent):
    """ **Possible constructors**:



```
SashEvent(id=0, edge=SASH_NONE)

```


A sash event is sent when the sash of a SashWindow has been dragged
by the user.


  


        Source: https://docs.wxpython.org/wx.adv.SashEvent.html
    """
    def __init__(self, id=0, edge=SASH_NONE) -> None:
        """ 

`__init__`(*self*, *id=0*, *edge=SASH\_NONE*)[¶](#wx.adv.SashEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **id** (*int*) –
* **edge** ([*SashEdgePosition*](wx.adv.SashEdgePosition.enumeration.html "SashEdgePosition")) –






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetDragRect(self) -> 'Rect':
        """ 

`GetDragRect`(*self*)[¶](#wx.adv.SashEvent.GetDragRect "Permalink to this definition")
Returns the rectangle representing the new size the window would be if the resize was applied.


It is up to the application to set the window size if required.



Return type
*Rect*






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetDragStatus(self) -> 'SashDragStatus':
        """ 

`GetDragStatus`(*self*)[¶](#wx.adv.SashEvent.GetDragStatus "Permalink to this definition")
Returns the status of the sash: one of `wx.adv.SASH_STATUS_OK`, `wx.adv.SASH_STATUS_OUT_OF_RANGE`.


If the drag caused the notional bounding box of the window to flip over, for example, the drag will be out of rage.



Return type
 [wx.adv.SashDragStatus](wx.adv.SashDragStatus.enumeration.html#wx-adv-sashdragstatus)






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def GetEdge(self) -> 'SashEdgePosition':
        """ 

`GetEdge`(*self*)[¶](#wx.adv.SashEvent.GetEdge "Permalink to this definition")
Returns the dragged edge.


The return value is one of `wx.adv.SASH_TOP`, `wx.adv.SASH_RIGHT`, `wx.adv.SASH_BOTTOM`, `wx.adv.SASH_LEFT`.



Return type
 [wx.adv.SashEdgePosition](wx.adv.SashEdgePosition.enumeration.html#wx-adv-sashedgeposition)






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetDragRect(self, rect: 'Rect') -> None:
        """ 

`SetDragRect`(*self*, *rect*)[¶](#wx.adv.SashEvent.SetDragRect "Permalink to this definition")

Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetDragStatus(self, status: SashDragStatus) -> None:
        """ 

`SetDragStatus`(*self*, *status*)[¶](#wx.adv.SashEvent.SetDragStatus "Permalink to this definition")

Parameters
**status** ([*SashDragStatus*](wx.adv.SashDragStatus.enumeration.html "SashDragStatus")) – 






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    def SetEdge(self, edge: SashEdgePosition) -> None:
        """ 

`SetEdge`(*self*, *edge*)[¶](#wx.adv.SashEvent.SetEdge "Permalink to this definition")

Parameters
**edge** ([*SashEdgePosition*](wx.adv.SashEdgePosition.enumeration.html "SashEdgePosition")) – 






            Source: https://docs.wxpython.org/wx.adv.SashEvent.html
        """

    DragRect: 'Rect'  # `DragRect`[¶](#wx.adv.SashEvent.DragRect "Permalink to this definition")See [`GetDragRect`](#wx.adv.SashEvent.GetDragRect "wx.adv.SashEvent.GetDragRect") and [`SetDragRect`](#wx.adv.SashEvent.SetDragRect "wx.adv.SashEvent.SetDragRect")
    DragStatus: 'SashDragStatus'  # `DragStatus`[¶](#wx.adv.SashEvent.DragStatus "Permalink to this definition")See [`GetDragStatus`](#wx.adv.SashEvent.GetDragStatus "wx.adv.SashEvent.GetDragStatus") and [`SetDragStatus`](#wx.adv.SashEvent.SetDragStatus "wx.adv.SashEvent.SetDragStatus")
    Edge: 'SashEdgePosition'  # `Edge`[¶](#wx.adv.SashEvent.Edge "Permalink to this definition")See [`GetEdge`](#wx.adv.SashEvent.GetEdge "wx.adv.SashEvent.GetEdge") and [`SetEdge`](#wx.adv.SashEvent.SetEdge "wx.adv.SashEvent.SetEdge")



EVT_SASH_DRAGGED: int  # Process a  wxEVT_SASH_DRAGGED   event, when the user has finished dragging a sash.

EVT_SASH_DRAGGED_RANGE: int  # Process a  wxEVT_SASH_DRAGGED_RANGE   event, when the user has finished dragging a sash. The event handler is called when windows with ids in the given range have their sashes dragged. ^^

OK: int

SASH_STATUS_OK: int

SASH_STATUS_OUT_OF_RANGE: int

SASH_TOP: int

SASH_RIGHT: int

SASH_BOTTOM: int

SASH_LEFT: int

class BannerWindow(Window):
    """ **Possible constructors**:



```
BannerWindow()

BannerWindow(parent, winid=ID_ANY, dir=LEFT, pos=DefaultPosition,
             size=DefaultSize, style=0, name=BannerWindowNameStr)

```


A simple banner window showing either a bitmap or text.


  


        Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.BannerWindow.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor, use [`Create`](#wx.adv.BannerWindow.Create "wx.adv.BannerWindow.Create") later.


This constructor is only used for two-step creation, if possible, prefer using the constructor below directly instead of using this one and calling [`Create`](#wx.adv.BannerWindow.Create "wx.adv.BannerWindow.Create") later.




---

  



**\_\_init\_\_** *(self, parent, winid=ID\_ANY, dir=LEFT, pos=DefaultPosition, size=DefaultSize, style=0, name=BannerWindowNameStr)*


Full constructor provided for consistency with the other classes only.


Prefer to use the shorter constructor documented above. You should rarely, if ever, need to use non-default values for any other parameters: as the banner window doesn’t generate any events, its identifier is not particularly useful; its position and size will be almost always managed by the containing sizer and it doesn’t have any specific styles. So only the parent and the banner direction need to be specified.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **winid** (*wx.WindowID*) –
* **dir** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def Create(self, parent, winid=ID_ANY, dir=LEFT, pos=DefaultPosition, size=DefaultSize, style=0, name=BannerWindowNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *winid=ID\_ANY*, *dir=LEFT*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *name=BannerWindowNameStr*)[¶](#wx.adv.BannerWindow.Create "Permalink to this definition")
Really create the banner window for the objects created using the default constructor.


It’s an error to call [`Create`](#wx.adv.BannerWindow.Create "wx.adv.BannerWindow.Create") for the objects created using non-default constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **winid** (*wx.WindowID*) –
* **dir** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.BannerWindow.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetBitmap`(*self*, *bmp*)[¶](#wx.adv.BannerWindow.SetBitmap "Permalink to this definition")
Provide the bitmap to use as background.


Notice that ideally the bitmap should be big enough to always cover the entire banner, e.g. for a horizontal banner with `wx.TOP` style its width should be bigger than any reasonable window size. Otherwise the bitmap is extended to cover the entire window area with a solid colour taken from the bitmap pixel on the edge in which direction the extension occurs so all bitmap pixels on this edge (top for `wx.LEFT`, right for `wx.TOP` and `wx.BOTTOM` and bottom for `wx.RIGHT`) should have the same colour to avoid jarring discontinuity.


If, on the other hand, the bitmap is bigger than the window size, then it is truncated. For `wx.LEFT` orientation the bitmap is truncated from the top, for `wx.TOP` and `wx.BOTTOM` – from the right and for `wx.RIGHT` – from the bottom, so put the most important part of the bitmap information in the opposite direction where it will never be truncated.


If no valid background bitmap is specified, the banner draws gradient background but if a valid bitmap is given here, the gradient is not draw and the start and end colours specified for it are ignored.



Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – Bitmap to use as background. May be invalid to indicate that no background bitmap should be used.






            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetGradient(self, start, end) -> None:
        """ 

`SetGradient`(*self*, *start*, *end*)[¶](#wx.adv.BannerWindow.SetGradient "Permalink to this definition")
Set the colours between which the gradient runs.


The gradient colours are ignored if [`SetBitmap`](#wx.adv.BannerWindow.SetBitmap "wx.adv.BannerWindow.SetBitmap") is used.



Parameters
* **start** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **end** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """

    def SetText(self, title, message) -> None:
        """ 

`SetText`(*self*, *title*, *message*)[¶](#wx.adv.BannerWindow.SetText "Permalink to this definition")
Set the text to display.


This is mutually exclusive with [`SetBitmap`](#wx.adv.BannerWindow.SetBitmap "wx.adv.BannerWindow.SetBitmap") .


Title is rendered in bold and should be single line, message can have multiple lines but is not wrapped automatically, include explicit line breaks in the string if you want to have multiple lines.



Parameters
* **title** (*string*) –
* **message** (*string*) –






            Source: https://docs.wxpython.org/wx.adv.BannerWindow.html
        """



TOP: int

LEFT: int

BOTTOM: int

RIGHT: int

class SashWindow(Window):
    """ **Possible constructors**:



```
SashWindow()

SashWindow(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
           style=CLIP_CHILDREN|SW_3D, name="sashWindow")

```


SashWindow allows any of its edges to have a sash which can be
dragged to resize the window.


  


        Source: https://docs.wxpython.org/wx.adv.SashWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.SashWindow.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=CLIP\_CHILDREN|SW\_3D, name=”sashWindow”)*


Constructs a sash window, which can be a child of a frame, dialog or any other non-control window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Pointer to a parent window.
* **id** (*wx.WindowID*) – Window identifier. If -1, will automatically create an identifier.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position. DefaultPosition is (-1, -1) which indicates that SashWindows should generate a default position for the window. If using the  [wx.adv.SashWindow](#wx-adv-sashwindow) class directly, supply an actual position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. DefaultSize is (-1, -1) which indicates that SashWindows should generate a default size for the window.
* **style** (*long*) – Window style. For window styles, please see  [wx.adv.SashWindow](#wx-adv-sashwindow).
* **name** (*string*) – Window name.






---

  





            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.SashWindow.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetDefaultBorderSize(self) -> int:
        """ 

`GetDefaultBorderSize`(*self*)[¶](#wx.adv.SashWindow.GetDefaultBorderSize "Permalink to this definition")
Gets the default sash border size.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetEdgeMargin(self, edge: SashEdgePosition) -> int:
        """ 

`GetEdgeMargin`(*self*, *edge*)[¶](#wx.adv.SashWindow.GetEdgeMargin "Permalink to this definition")
Get border size.



Parameters
**edge** ([*SashEdgePosition*](wx.adv.SashEdgePosition.enumeration.html "SashEdgePosition")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetExtraBorderSize(self) -> int:
        """ 

`GetExtraBorderSize`(*self*)[¶](#wx.adv.SashWindow.GetExtraBorderSize "Permalink to this definition")
Gets the addition border size between child and sash window.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMaximumSizeX(self) -> int:
        """ 

`GetMaximumSizeX`(*self*)[¶](#wx.adv.SashWindow.GetMaximumSizeX "Permalink to this definition")
Gets the maximum window size in the x direction.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMaximumSizeY(self) -> int:
        """ 

`GetMaximumSizeY`(*self*)[¶](#wx.adv.SashWindow.GetMaximumSizeY "Permalink to this definition")
Gets the maximum window size in the y direction.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMinimumSizeX(self) -> int:
        """ 

`GetMinimumSizeX`(*self*)[¶](#wx.adv.SashWindow.GetMinimumSizeX "Permalink to this definition")
Gets the minimum window size in the x direction.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetMinimumSizeY(self) -> int:
        """ 

`GetMinimumSizeY`(*self*)[¶](#wx.adv.SashWindow.GetMinimumSizeY "Permalink to this definition")
Gets the minimum window size in the y direction.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def GetSashVisible(self, edge: SashEdgePosition) -> bool:
        """ 

`GetSashVisible`(*self*, *edge*)[¶](#wx.adv.SashWindow.GetSashVisible "Permalink to this definition")
Returns `True` if a sash is visible on the given edge, `False` otherwise.



Parameters
**edge** ([*SashEdgePosition*](wx.adv.SashEdgePosition.enumeration.html "SashEdgePosition")) – Edge. One of `wx.adv.SASH_TOP`, `wx.adv.SASH_RIGHT`, `wx.adv.SASH_BOTTOM`, `wx.adv.SASH_LEFT`.



Return type
*bool*





See also


[`SetSashVisible`](#wx.adv.SashWindow.SetSashVisible "wx.adv.SashWindow.SetSashVisible")





            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SashHitTest(self, x, y, tolerance=2) -> 'SashEdgePosition':
        """ 

`SashHitTest`(*self*, *x*, *y*, *tolerance=2*)[¶](#wx.adv.SashWindow.SashHitTest "Permalink to this definition")
Tests for x, y over sash.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **tolerance** (*int*) –



Return type
 [wx.adv.SashEdgePosition](wx.adv.SashEdgePosition.enumeration.html#wx-adv-sashedgeposition)






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetDefaultBorderSize(self, width: int) -> None:
        """ 

`SetDefaultBorderSize`(*self*, *width*)[¶](#wx.adv.SashWindow.SetDefaultBorderSize "Permalink to this definition")
Sets the default sash border size.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetExtraBorderSize(self, width: int) -> None:
        """ 

`SetExtraBorderSize`(*self*, *width*)[¶](#wx.adv.SashWindow.SetExtraBorderSize "Permalink to this definition")
Sets the additional border size between child and sash window.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMaximumSizeX(self, min: int) -> None:
        """ 

`SetMaximumSizeX`(*self*, *min*)[¶](#wx.adv.SashWindow.SetMaximumSizeX "Permalink to this definition")
Sets the maximum window size in the x direction.



Parameters
**min** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMaximumSizeY(self, min: int) -> None:
        """ 

`SetMaximumSizeY`(*self*, *min*)[¶](#wx.adv.SashWindow.SetMaximumSizeY "Permalink to this definition")
Sets the maximum window size in the y direction.



Parameters
**min** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMinimumSizeX(self, min: int) -> None:
        """ 

`SetMinimumSizeX`(*self*, *min*)[¶](#wx.adv.SashWindow.SetMinimumSizeX "Permalink to this definition")
Sets the minimum window size in the x direction.



Parameters
**min** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetMinimumSizeY(self, min: int) -> None:
        """ 

`SetMinimumSizeY`(*self*, *min*)[¶](#wx.adv.SashWindow.SetMinimumSizeY "Permalink to this definition")
Sets the minimum window size in the y direction.



Parameters
**min** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SetSashVisible(self, edge, visible) -> None:
        """ 

`SetSashVisible`(*self*, *edge*, *visible*)[¶](#wx.adv.SashWindow.SetSashVisible "Permalink to this definition")
Call this function to make a sash visible or invisible on a particular edge.



Parameters
* **edge** ([*SashEdgePosition*](wx.adv.SashEdgePosition.enumeration.html "SashEdgePosition")) – Edge to change. One of `wx.adv.SASH_TOP`, `wx.adv.SASH_RIGHT`, `wx.adv.SASH_BOTTOM`, `wx.adv.SASH_LEFT`.
* **visible** (*bool*) – `True` to make the sash visible, `False` to make it invisible.





See also


[`GetSashVisible`](#wx.adv.SashWindow.GetSashVisible "wx.adv.SashWindow.GetSashVisible")





            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    def SizeWindows(self) -> None:
        """ 

`SizeWindows`(*self*)[¶](#wx.adv.SashWindow.SizeWindows "Permalink to this definition")
Resizes subwindows.




            Source: https://docs.wxpython.org/wx.adv.SashWindow.html
        """

    DefaultBorderSize: int  # `DefaultBorderSize`[¶](#wx.adv.SashWindow.DefaultBorderSize "Permalink to this definition")See [`GetDefaultBorderSize`](#wx.adv.SashWindow.GetDefaultBorderSize "wx.adv.SashWindow.GetDefaultBorderSize") and [`SetDefaultBorderSize`](#wx.adv.SashWindow.SetDefaultBorderSize "wx.adv.SashWindow.SetDefaultBorderSize")
    ExtraBorderSize: int  # `ExtraBorderSize`[¶](#wx.adv.SashWindow.ExtraBorderSize "Permalink to this definition")See [`GetExtraBorderSize`](#wx.adv.SashWindow.GetExtraBorderSize "wx.adv.SashWindow.GetExtraBorderSize") and [`SetExtraBorderSize`](#wx.adv.SashWindow.SetExtraBorderSize "wx.adv.SashWindow.SetExtraBorderSize")
    MaximumSizeX: int  # `MaximumSizeX`[¶](#wx.adv.SashWindow.MaximumSizeX "Permalink to this definition")See [`GetMaximumSizeX`](#wx.adv.SashWindow.GetMaximumSizeX "wx.adv.SashWindow.GetMaximumSizeX") and [`SetMaximumSizeX`](#wx.adv.SashWindow.SetMaximumSizeX "wx.adv.SashWindow.SetMaximumSizeX")
    MaximumSizeY: int  # `MaximumSizeY`[¶](#wx.adv.SashWindow.MaximumSizeY "Permalink to this definition")See [`GetMaximumSizeY`](#wx.adv.SashWindow.GetMaximumSizeY "wx.adv.SashWindow.GetMaximumSizeY") and [`SetMaximumSizeY`](#wx.adv.SashWindow.SetMaximumSizeY "wx.adv.SashWindow.SetMaximumSizeY")
    MinimumSizeX: int  # `MinimumSizeX`[¶](#wx.adv.SashWindow.MinimumSizeX "Permalink to this definition")See [`GetMinimumSizeX`](#wx.adv.SashWindow.GetMinimumSizeX "wx.adv.SashWindow.GetMinimumSizeX") and [`SetMinimumSizeX`](#wx.adv.SashWindow.SetMinimumSizeX "wx.adv.SashWindow.SetMinimumSizeX")
    MinimumSizeY: int  # `MinimumSizeY`[¶](#wx.adv.SashWindow.MinimumSizeY "Permalink to this definition")See [`GetMinimumSizeY`](#wx.adv.SashWindow.GetMinimumSizeY "wx.adv.SashWindow.GetMinimumSizeY") and [`SetMinimumSizeY`](#wx.adv.SashWindow.SetMinimumSizeY "wx.adv.SashWindow.SetMinimumSizeY")



SW_3D: int  # Draws a 3D effect sash and border.

SW_3DSASH: int  # Draws a 3D effect sash.

SW_3DBORDER: int  # Draws a 3D effect border.

SW_BORDER: int  # Draws a thin black border. ^^

class AnimationCtrl(Control):
    """ **Possible constructors**:



```
AnimationCtrl(parent, id=ID_ANY, anim=NullAnimation,
              pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE,
              name=AnimationCtrlNameStr)

```


This is a static control which displays an animation.


  


        Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> None:
        """ 

`__init__`(*self*, *parent*, *id=ID\_ANY*, *anim=NullAnimation*, *pos=DefaultPosition*, *size=DefaultSize*, *style=AC\_DEFAULT\_STYLE*, *name=AnimationCtrlNameStr*)[¶](#wx.adv.AnimationCtrl.__init__ "Permalink to this definition")
Initializes the object and calls [`Create`](#wx.adv.AnimationCtrl.Create "wx.adv.AnimationCtrl.Create") with all the parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Create(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *anim=NullAnimation*, *pos=DefaultPosition*, *size=DefaultSize*, *style=AC\_DEFAULT\_STYLE*, *name=AnimationCtrlNameStr*)[¶](#wx.adv.AnimationCtrl.Create "Permalink to this definition")
Creates the control with the given *anim* animation.


After control creation you must explicitly call [`Play`](#wx.adv.AnimationCtrl.Play "wx.adv.AnimationCtrl.Play") to start to play the animation. Until that function won’t be called, the first frame of the animation is displayed.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window, must be not `None`.
* **id** (*wx.WindowID*) – The identifier for the control.
* **anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) – The initial animation shown in the control.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size.
* **style** (*long*) – The window style, see `AC_` flags.
* **name** (*string*) – Control name.



Return type
*bool*



Returns
`True` if the control was successfully created or `False` if creation failed.






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def CreateAnimation(self) -> 'Animation':
        """ 

`CreateAnimation`(*self*)[¶](#wx.adv.AnimationCtrl.CreateAnimation "Permalink to this definition")
Create a new animation object compatible with this control.


A  [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation) object created using this function is always compatible with controls of this type, see [`wx.adv.Animation.IsCompatibleWith`](wx.adv.Animation.html#wx.adv.Animation.IsCompatibleWith "wx.adv.Animation.IsCompatibleWith") .



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)





New in version 4.1/wxWidgets-3.1.4.




See also


[`CreateCompatibleAnimation`](#wx.adv.AnimationCtrl.CreateCompatibleAnimation "wx.adv.AnimationCtrl.CreateCompatibleAnimation")





            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    @staticmethod
    def CreateCompatibleAnimation() -> 'Animation':
        """ 

*static* `CreateCompatibleAnimation`()[¶](#wx.adv.AnimationCtrl.CreateCompatibleAnimation "Permalink to this definition")
Create a new animation object compatible with this control.


This method does the same thing as [`CreateAnimation`](#wx.adv.AnimationCtrl.CreateAnimation "wx.adv.AnimationCtrl.CreateAnimation") but is static, i.e. can be called without creating any  [wx.adv.AnimationCtrl](#wx-adv-animationctrl) objects.



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def GetAnimation(self) -> 'Animation':
        """ 

`GetAnimation`(*self*)[¶](#wx.adv.AnimationCtrl.GetAnimation "Permalink to this definition")
Returns the animation associated with this control.



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.AnimationCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def GetInactiveBitmap(self) -> 'Bitmap':
        """ 

`GetInactiveBitmap`(*self*)[¶](#wx.adv.AnimationCtrl.GetInactiveBitmap "Permalink to this definition")
Returns the inactive bitmap shown in this control when the; see [`SetInactiveBitmap`](#wx.adv.AnimationCtrl.SetInactiveBitmap "wx.adv.AnimationCtrl.SetInactiveBitmap") for more info.



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def IsPlaying(self) -> bool:
        """ 

`IsPlaying`(*self*)[¶](#wx.adv.AnimationCtrl.IsPlaying "Permalink to this definition")
Returns `True` if the animation is being played.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Load(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ 

`Load`(*self*, *file*, *animType=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.AnimationCtrl.Load "Permalink to this definition")
Loads the animation from the given stream and calls [`SetAnimation`](#wx.adv.AnimationCtrl.SetAnimation "wx.adv.AnimationCtrl.SetAnimation") .


See [`wx.adv.Animation.Load`](wx.adv.Animation.html#wx.adv.Animation.Load "wx.adv.Animation.Load") for more info.



Parameters
* **file** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **animType** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def LoadFile(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ 

`LoadFile`(*self*, *file*, *animType=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.AnimationCtrl.LoadFile "Permalink to this definition")
Loads the animation from the given file and calls [`SetAnimation`](#wx.adv.AnimationCtrl.SetAnimation "wx.adv.AnimationCtrl.SetAnimation") .


See [`wx.adv.Animation.LoadFile`](wx.adv.Animation.html#wx.adv.Animation.LoadFile "wx.adv.Animation.LoadFile") for more info.



Parameters
* **file** (*string*) –
* **animType** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Play(self) -> bool:
        """ 

`Play`(*self*)[¶](#wx.adv.AnimationCtrl.Play "Permalink to this definition")
Starts playing the animation.


The animation is always played in loop mode (unless the last frame of the animation has an infinite delay time) and always start from the first frame even if you `stopped` it while some other frame was displayed.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def SetAnimation(self, anim: 'adv.Animation') -> None:
        """ 

`SetAnimation`(*self*, *anim*)[¶](#wx.adv.AnimationCtrl.SetAnimation "Permalink to this definition")
Sets the animation to play in this control.


If the previous animation is being played, it’s [`Stop`](#wx.adv.AnimationCtrl.Stop "wx.adv.AnimationCtrl.Stop") stopped. Until [`Play`](#wx.adv.AnimationCtrl.Play "wx.adv.AnimationCtrl.Play") isn’t called, a static image, the first frame of the given animation or the background colour will be shown (see [`SetInactiveBitmap`](#wx.adv.AnimationCtrl.SetInactiveBitmap "wx.adv.AnimationCtrl.SetInactiveBitmap") for more info).



Parameters
**anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) – 






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def SetInactiveBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetInactiveBitmap`(*self*, *bmp*)[¶](#wx.adv.AnimationCtrl.SetInactiveBitmap "Permalink to this definition")
Sets the bitmap to show on the control when it’s not playing an animation.


If you set as inactive bitmap `wx.NullBitmap` (which is the default), then the first frame of the animation is instead shown when the control is inactive; in this case, if there’s no valid animation associated with the control (see [`SetAnimation`](#wx.adv.AnimationCtrl.SetAnimation "wx.adv.AnimationCtrl.SetAnimation") ), then the background colour of the window is shown.


If the control is not playing the animation, the given bitmap will be immediately shown, otherwise it will be shown as soon as [`Stop`](#wx.adv.AnimationCtrl.Stop "wx.adv.AnimationCtrl.Stop") is called.


Note that the inactive bitmap, if smaller than the control’s size, will be centered in the control; if bigger, it will be stretched to fit it.



Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    def Stop(self) -> None:
        """ 

`Stop`(*self*)[¶](#wx.adv.AnimationCtrl.Stop "Permalink to this definition")
Stops playing the animation.


The control will show the first frame of the animation, a custom static image or the window’s background colour as specified by the last [`SetInactiveBitmap`](#wx.adv.AnimationCtrl.SetInactiveBitmap "wx.adv.AnimationCtrl.SetInactiveBitmap") call.




            Source: https://docs.wxpython.org/wx.adv.AnimationCtrl.html
        """

    Animation: 'Animation'  # `Animation`[¶](#wx.adv.AnimationCtrl.Animation "Permalink to this definition")See [`GetAnimation`](#wx.adv.AnimationCtrl.GetAnimation "wx.adv.AnimationCtrl.GetAnimation") and [`SetAnimation`](#wx.adv.AnimationCtrl.SetAnimation "wx.adv.AnimationCtrl.SetAnimation")
    InactiveBitmap: 'Bitmap'  # `InactiveBitmap`[¶](#wx.adv.AnimationCtrl.InactiveBitmap "Permalink to this definition")See [`GetInactiveBitmap`](#wx.adv.AnimationCtrl.GetInactiveBitmap "wx.adv.AnimationCtrl.GetInactiveBitmap") and [`SetInactiveBitmap`](#wx.adv.AnimationCtrl.SetInactiveBitmap "wx.adv.AnimationCtrl.SetInactiveBitmap")



AC_DEFAULT_STYLE: int  # The default style: wx.BORDER_NONE.

AC_NO_AUTORESIZE: int  # By default, the control will adjust its size to exactly fit to the size of the animation when SetAnimation is called. If this style flag is given, the control will not change its size ^^

BORDER_NONE: int

class CalendarCtrl(Control):
    """ **Possible constructors**:



```
CalendarCtrl()

CalendarCtrl(parent, id=ID_ANY, date=DefaultDateTime,
             pos=DefaultPosition, size=DefaultSize, style=CAL_SHOW_HOLIDAYS,
             name=CalendarNameStr)

```


The calendar control allows the user to pick a date.


  


        Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.CalendarCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, date=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=CAL\_SHOW\_HOLIDAYS, name=CalendarNameStr)*


Does the same as [`Create`](#wx.adv.CalendarCtrl.Create "wx.adv.CalendarCtrl.Create") method.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **date** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def Create(self, parent, id=ID_ANY, date=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=CAL_SHOW_HOLIDAYS, name=CalendarNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *date=DefaultDateTime*, *pos=DefaultPosition*, *size=DefaultSize*, *style=CAL\_SHOW\_HOLIDAYS*, *name=CalendarNameStr*)[¶](#wx.adv.CalendarCtrl.Create "Permalink to this definition")
Creates the control.


See `Window.__init__` for the meaning of the parameters and the control overview for the possible styles.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **date** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def EnableHolidayDisplay(self, display: bool=True) -> None:
        """ 

`EnableHolidayDisplay`(*self*, *display=True*)[¶](#wx.adv.CalendarCtrl.EnableHolidayDisplay "Permalink to this definition")
This function should be used instead of changing `CAL_SHOW_HOLIDAYS` style bit directly.


It enables or disables the special highlighting of the holidays.



Parameters
**display** (*bool*) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def EnableMonthChange(self, enable: bool=True) -> bool:
        """ 

`EnableMonthChange`(*self*, *enable=True*)[¶](#wx.adv.CalendarCtrl.EnableMonthChange "Permalink to this definition")
This function should be used instead of changing `CAL_NO_MONTH_CHANGE` style bit.


It allows or disallows the user to change the month interactively. Note that if the month cannot be changed, the year cannot be changed either.



Parameters
**enable** (*bool*) – 



Return type
*bool*



Returns
`True` if the value of this option really changed or `False` if it was already set to the requested value.






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetAttr(self, day: int) -> 'CalendarDateAttr':
        """ 

`GetAttr`(*self*, *day*)[¶](#wx.adv.CalendarCtrl.GetAttr "Permalink to this definition")
Returns the attribute for the given date (should be in the range 1…31).


The returned pointer may be `None`. Only in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl).



Parameters
**day** (*int*) – 



Return type
 [wx.adv.CalendarDateAttr](wx.adv.CalendarDateAttr.html#wx-adv-calendardateattr)






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.CalendarCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetDate(self) -> 'DateTime':
        """ 

`GetDate`(*self*)[¶](#wx.adv.CalendarCtrl.GetDate "Permalink to this definition")
Gets the currently selected date.



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetDateRange(self) -> tuple:
        """ 

`GetDateRange`(*self*)[¶](#wx.adv.CalendarCtrl.GetDateRange "Permalink to this definition")
Returns the limits currently being used.



Return type
*tuple*



Returns
( *bool*, *lowerdate*, *upperdate* )





See also


[`SetDateRange`](#wx.adv.CalendarCtrl.SetDateRange "wx.adv.CalendarCtrl.SetDateRange")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHeaderColourBg(self) -> 'Colour':
        """ 

`GetHeaderColourBg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHeaderColourBg "Permalink to this definition")
Gets the background colour of the header part of the calendar window.


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and always returns `NullColour` in the native versions.



Return type
*Colour*





See also


[`SetHeaderColours`](#wx.adv.CalendarCtrl.SetHeaderColours "wx.adv.CalendarCtrl.SetHeaderColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHeaderColourFg(self) -> 'Colour':
        """ 

`GetHeaderColourFg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHeaderColourFg "Permalink to this definition")
Gets the foreground colour of the header part of the calendar window.


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and always returns `NullColour` in the native versions.



Return type
*Colour*





See also


[`SetHeaderColours`](#wx.adv.CalendarCtrl.SetHeaderColours "wx.adv.CalendarCtrl.SetHeaderColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHighlightColourBg(self) -> 'Colour':
        """ 

`GetHighlightColourBg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHighlightColourBg "Permalink to this definition")
Gets the background highlight colour.


Only in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl).


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and always returns `NullColour` in the native versions.



Return type
*Colour*





See also


[`SetHighlightColours`](#wx.adv.CalendarCtrl.SetHighlightColours "wx.adv.CalendarCtrl.SetHighlightColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHighlightColourFg(self) -> 'Colour':
        """ 

`GetHighlightColourFg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHighlightColourFg "Permalink to this definition")
Gets the foreground highlight colour.


Only in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl).


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and always returns `NullColour` in the native versions.



Return type
*Colour*





See also


[`SetHighlightColours`](#wx.adv.CalendarCtrl.SetHighlightColours "wx.adv.CalendarCtrl.SetHighlightColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHolidayColourBg(self) -> 'Colour':
        """ 

`GetHolidayColourBg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHolidayColourBg "Permalink to this definition")
Return the background colour currently used for holiday highlighting.


Only useful with generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) as native versions currently don’t support holidays display at all and always return `NullColour` .



Return type
*Colour*





See also


[`SetHolidayColours`](#wx.adv.CalendarCtrl.SetHolidayColours "wx.adv.CalendarCtrl.SetHolidayColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def GetHolidayColourFg(self) -> 'Colour':
        """ 

`GetHolidayColourFg`(*self*)[¶](#wx.adv.CalendarCtrl.GetHolidayColourFg "Permalink to this definition")
Return the foreground colour currently used for holiday highlighting.


Only useful with generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) as native versions currently don’t support holidays display at all and always return `NullColour` .



Return type
*Colour*





See also


[`SetHolidayColours`](#wx.adv.CalendarCtrl.SetHolidayColours "wx.adv.CalendarCtrl.SetHolidayColours")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def HitTest(self, pos: Union[tuple[int, int], 'Point']) -> tuple:
        """ 

`HitTest`(*self*, *pos*)[¶](#wx.adv.CalendarCtrl.HitTest "Permalink to this definition")
Returns one of CalendarHitTestResult constants and fills either *date* or *wd* pointer with the corresponding value depending on the hit test code.


Not implemented in wxGTK currently.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*tuple*



Returns
(  [wx.adv.CalendarHitTestResult](wx.adv.CalendarHitTestResult.enumeration.html#wx-adv-calendarhittestresult), *date*, *wd* )






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def Mark(self, day, mark) -> None:
        """ 

`Mark`(*self*, *day*, *mark*)[¶](#wx.adv.CalendarCtrl.Mark "Permalink to this definition")
Mark or unmark the day.


This day of month will be marked in every month. In generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl),



Parameters
* **day** (*int*) –
* **mark** (*bool*) –






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def PyGetDate(self) -> None:
        """ 

`PyGetDate`(*self*)[¶](#wx.adv.CalendarCtrl.PyGetDate "Permalink to this definition")
Return the date as a Python datetime.date object.




            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def ResetAttr(self, day: int) -> None:
        """ 

`ResetAttr`(*self*, *day*)[¶](#wx.adv.CalendarCtrl.ResetAttr "Permalink to this definition")
Clears any attributes associated with the given day (in the range 1…31).


Only in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl).



Parameters
**day** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetAttr(self, day, attr) -> None:
        """ 

`SetAttr`(*self*, *day*, *attr*)[¶](#wx.adv.CalendarCtrl.SetAttr "Permalink to this definition")
Associates the attribute with the specified date (in the range 1…31).


If the pointer is `None`, the items attribute is cleared. Only in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl).



Parameters
* **day** (*int*) –
* **attr** ([*wx.adv.CalendarDateAttr*](wx.adv.CalendarDateAttr.html#wx.adv.CalendarDateAttr "wx.adv.CalendarDateAttr")) –






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetDate(self, date: 'DateTime') -> bool:
        """ 

`SetDate`(*self*, *date*)[¶](#wx.adv.CalendarCtrl.SetDate "Permalink to this definition")
Sets the current date.


The *date* parameter must be valid and in the currently valid range as set by [`SetDateRange`](#wx.adv.CalendarCtrl.SetDateRange "wx.adv.CalendarCtrl.SetDateRange") , otherwise the current date is not changed and the function returns `False` and, additionally, triggers an assertion failure if the date is invalid.



Parameters
**date** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetDateRange(self, lowerdate=DefaultDateTime, upperdate=DefaultDateTime) -> bool:
        """ 

`SetDateRange`(*self*, *lowerdate=DefaultDateTime*, *upperdate=DefaultDateTime*)[¶](#wx.adv.CalendarCtrl.SetDateRange "Permalink to this definition")
Restrict the dates that can be selected in the control to the specified range.


If either date is set, the corresponding limit will be enforced and `True` returned. If none are set, the existing restrictions are removed and `False` is returned.



Parameters
* **lowerdate** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – The low limit for the dates shown by the control or `wx.DefaultDateTime` .
* **upperdate** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – The high limit for the dates shown by the control or `wx.DefaultDateTime` .



Return type
*bool*



Returns
`True` if either limit is valid, `False` otherwise





See also


[`GetDateRange`](#wx.adv.CalendarCtrl.GetDateRange "wx.adv.CalendarCtrl.GetDateRange")





            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHeaderColours(self, colFg, colBg) -> None:
        """ 

`SetHeaderColours`(*self*, *colFg*, *colBg*)[¶](#wx.adv.CalendarCtrl.SetHeaderColours "Permalink to this definition")
Set the colours used for painting the weekdays at the top of the control.


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and does nothing in the native versions.



Parameters
* **colFg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHighlightColours(self, colFg, colBg) -> None:
        """ 

`SetHighlightColours`(*self*, *colFg*, *colBg*)[¶](#wx.adv.CalendarCtrl.SetHighlightColours "Permalink to this definition")
Set the colours to be used for highlighting the currently selected date.


This method is currently only implemented in generic  [wx.adv.CalendarCtrl](#wx-adv-calendarctrl) and does nothing in the native versions.



Parameters
* **colFg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHoliday(self, day: int) -> None:
        """ 

`SetHoliday`(*self*, *day*)[¶](#wx.adv.CalendarCtrl.SetHoliday "Permalink to this definition")
Marks the specified day as being a holiday in the current month.


This method is only implemented in the generic version of the control and does nothing in the native ones.



Parameters
**day** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetHolidayColours(self, colFg, colBg) -> None:
        """ 

`SetHolidayColours`(*self*, *colFg*, *colBg*)[¶](#wx.adv.CalendarCtrl.SetHolidayColours "Permalink to this definition")
Sets the colours to be used for the holidays highlighting.


This method is only implemented in the generic version of the control and does nothing in the native ones. It should also only be called if the window style includes `CAL_SHOW_HOLIDAYS` flag or [`EnableHolidayDisplay`](#wx.adv.CalendarCtrl.EnableHolidayDisplay "wx.adv.CalendarCtrl.EnableHolidayDisplay") had been called.



Parameters
* **colFg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBg** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.adv.CalendarCtrl.html
        """

    def SetUpperDateLimit(self, date: 'DateTime') -> None:
        """ 
        """

    def SetLowerDateLimit(self, date: 'DateTime') -> None:
        """ 
        """

    Date: 'DateTime'  # `Date`[¶](#wx.adv.CalendarCtrl.Date "Permalink to this definition")See [`GetDate`](#wx.adv.CalendarCtrl.GetDate "wx.adv.CalendarCtrl.GetDate") and [`SetDate`](#wx.adv.CalendarCtrl.SetDate "wx.adv.CalendarCtrl.SetDate")
    DateRange: tuple  # `DateRange`[¶](#wx.adv.CalendarCtrl.DateRange "Permalink to this definition")See [`GetDateRange`](#wx.adv.CalendarCtrl.GetDateRange "wx.adv.CalendarCtrl.GetDateRange") and [`SetDateRange`](#wx.adv.CalendarCtrl.SetDateRange "wx.adv.CalendarCtrl.SetDateRange")
    HeaderColourBg: 'Colour'  # `HeaderColourBg`[¶](#wx.adv.CalendarCtrl.HeaderColourBg "Permalink to this definition")See [`GetHeaderColourBg`](#wx.adv.CalendarCtrl.GetHeaderColourBg "wx.adv.CalendarCtrl.GetHeaderColourBg")
    HeaderColourFg: 'Colour'  # `HeaderColourFg`[¶](#wx.adv.CalendarCtrl.HeaderColourFg "Permalink to this definition")See [`GetHeaderColourFg`](#wx.adv.CalendarCtrl.GetHeaderColourFg "wx.adv.CalendarCtrl.GetHeaderColourFg")
    HighlightColourBg: 'Colour'  # `HighlightColourBg`[¶](#wx.adv.CalendarCtrl.HighlightColourBg "Permalink to this definition")See [`GetHighlightColourBg`](#wx.adv.CalendarCtrl.GetHighlightColourBg "wx.adv.CalendarCtrl.GetHighlightColourBg")
    HighlightColourFg: 'Colour'  # `HighlightColourFg`[¶](#wx.adv.CalendarCtrl.HighlightColourFg "Permalink to this definition")See [`GetHighlightColourFg`](#wx.adv.CalendarCtrl.GetHighlightColourFg "wx.adv.CalendarCtrl.GetHighlightColourFg")
    HolidayColourBg: 'Colour'  # `HolidayColourBg`[¶](#wx.adv.CalendarCtrl.HolidayColourBg "Permalink to this definition")See [`GetHolidayColourBg`](#wx.adv.CalendarCtrl.GetHolidayColourBg "wx.adv.CalendarCtrl.GetHolidayColourBg")
    HolidayColourFg: 'Colour'  # `HolidayColourFg`[¶](#wx.adv.CalendarCtrl.HolidayColourFg "Permalink to this definition")See [`GetHolidayColourFg`](#wx.adv.CalendarCtrl.GetHolidayColourFg "wx.adv.CalendarCtrl.GetHolidayColourFg")



CAL_SUNDAY_FIRST: int  # Show Sunday as the first day in the week (not in wxGTK)

CAL_MONDAY_FIRST: int  # Show Monday as the first day in the week (not in wxGTK)

CAL_SHOW_HOLIDAYS: int  # Highlight holidays in the calendar (only generic)

CAL_NO_YEAR_CHANGE: int  # Disable the year changing (deprecated, only generic)

CAL_NO_MONTH_CHANGE: int  # Disable the month (and, implicitly, the year) changing

CAL_SHOW_SURROUNDING_WEEKS: int  # Show the neighbouring weeks in the previous and next months (only generic, always on for the native controls)

CAL_SEQUENTIAL_MONTH_SELECTION: int  # Use alternative, more compact, style for the month and year selection controls. (only generic)

CAL_SHOW_WEEK_NUMBERS: int  # Show week numbers on the left side of the calendar. (not in generic) ^^

EVT_CALENDAR: int  # A day was double clicked in the calendar.

EVT_CALENDAR_SEL_CHANGED: int  # The selected date changed.

EVT_CALENDAR_PAGE_CHANGED: int  # The selected month (and/or year) changed.

EVT_CALENDAR_WEEKDAY_CLICKED: int  # User clicked on the week day header (only generic).

EVT_CALENDAR_WEEK_CLICKED: int  # User clicked on the week of the year number (only generic). ^^

class DatePickerCtrl(Control):
    """ **Possible constructors**:



```
DatePickerCtrl()

DatePickerCtrl(parent, id=ID_ANY, dt=DefaultDateTime,
               pos=DefaultPosition, size=DefaultSize, style=DP_DEFAULT|DP_SHOWCENTURY,
               validator=DefaultValidator, name="datectrl")

```


This control allows the user to select a date.


  


        Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.DatePickerCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=DP\_DEFAULT|DP\_SHOWCENTURY, validator=DefaultValidator, name=”datectrl”)*


Initializes the object and calls [`Create`](#wx.adv.DatePickerCtrl.Create "wx.adv.DatePickerCtrl.Create") with all the parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def Create(self, parent, id=ID_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=DP_DEFAULT|DP_SHOWCENTURY, validator=DefaultValidator, name="datectrl") -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *dt=DefaultDateTime*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DP\_DEFAULT|DP\_SHOWCENTURY*, *validator=DefaultValidator*, *name="datectrl"*)[¶](#wx.adv.DatePickerCtrl.Create "Permalink to this definition")
Create the control window.


This method should only be used for objects created using default constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window, must not be not `None`.
* **id** (*wx.WindowID*) – The identifier for the control.
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – The initial value of the control, if an invalid date (such as the default value) is used, the control is set to today.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size. If left at default value, the control chooses its own best size by using the height approximately equal to a text control and width large enough to show the date string fully.
* **style** (*long*) – The window style, see the description of the styles in the class documentation.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Validator which can be used for additional data checks.
* **name** (*string*) – Control name.



Return type
*bool*



Returns
`True` if the control was successfully created or `False` if creation failed.






            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.DatePickerCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def GetRange(self) -> tuple:
        """ 

`GetRange`(*self*)[¶](#wx.adv.DatePickerCtrl.GetRange "Permalink to this definition")
If the control had been previously limited to a range of dates using [`SetRange`](#wx.adv.DatePickerCtrl.SetRange "wx.adv.DatePickerCtrl.SetRange") , returns the lower and upper bounds of this range.


If no range is set (or only one of the bounds is set), *dt1* and/or *dt2* are set to be invalid.


Notice that when using a native MSW implementation of this control the lower range is always set, even if [`SetRange`](#wx.adv.DatePickerCtrl.SetRange "wx.adv.DatePickerCtrl.SetRange") hadn’t been called explicitly, as the native control only supports dates later than year 1601.



Return type
*tuple*



Returns
( *bool*, *dt1*, *dt2* )






            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def GetValue(self) -> 'DateTime':
        """ 

`GetValue`(*self*)[¶](#wx.adv.DatePickerCtrl.GetValue "Permalink to this definition")
Returns the currently entered date.


For a control with `DP_ALLOWNONE` style the returned value may be invalid if no date is entered, otherwise it is always valid.



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetNullText(self, text: str) -> None:
        """ 

`SetNullText`(*self*, *text*)[¶](#wx.adv.DatePickerCtrl.SetNullText "Permalink to this definition")
Set the text to show when there is no valid value.


For the controls with `DP_ALLOWNONE` style, set the string displayed when the control doesn’t have any valid value. Currently this is only actually used under MSW, where it can be used to override the previous value which is still displayed by the control in this case, and ignored elsewhere.


Notably, *text* can be empty to completely hide the date if no valid date is specified.



Parameters
**text** (*string*) – 





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetRange(self, dt1, dt2) -> None:
        """ 

`SetRange`(*self*, *dt1*, *dt2*)[¶](#wx.adv.DatePickerCtrl.SetRange "Permalink to this definition")
Sets the valid range for the date selection.


If *dt1* is valid, it becomes the earliest date (inclusive) accepted by the control. If *dt2* is valid, it becomes the latest possible date.


Notice that if the current value is not inside the new range, it will be adjusted to lie inside it, i.e. calling this method can change the control value, however no events are generated by it.



Parameters
* **dt1** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **dt2** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –





Note


If the current value of the control is outside of the newly set range bounds, the behaviour is undefined.





            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    def SetValue(self, dt: 'DateTime') -> None:
        """ 

`SetValue`(*self*, *dt*)[¶](#wx.adv.DatePickerCtrl.SetValue "Permalink to this definition")
Changes the current value of the control.


The date should be valid unless the control was created with `DP_ALLOWNONE` style and included in the currently selected range, if any.


Calling this method does not result in a date change event.



Parameters
**dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 






            Source: https://docs.wxpython.org/wx.adv.DatePickerCtrl.html
        """

    Value: 'DateTime'  # `Value`[¶](#wx.adv.DatePickerCtrl.Value "Permalink to this definition")See [`GetValue`](#wx.adv.DatePickerCtrl.GetValue "wx.adv.DatePickerCtrl.GetValue") and [`SetValue`](#wx.adv.DatePickerCtrl.SetValue "wx.adv.DatePickerCtrl.SetValue")



DP_SPIN: int  # Creates a control without a month calendar drop down but with spin-control-like arrows to change individual date components. This style is not supported by the generic version.

DP_DROPDOWN: int  # Creates a control with a month calendar drop-down part from which the user can select a date. This style is not supported in OSX/Cocoa native version.

DP_DEFAULT: int  # Creates a control with the style that is best supported for the current platform (currently wx.adv.DP_SPIN under Windows and OSX/Cocoa and wx.adv.DP_DROPDOWN elsewhere).

DP_ALLOWNONE: int  # With this style, the control allows the user to not enter any valid date at all. Without it - the default - the control always has some valid date. This style is not supported in OSX/Cocoa native version.

DP_SHOWCENTURY: int  # Forces display of the century in the default date format. Without this style the century could be displayed, or not, depending on the default date representation in the system. This style is not supported in OSX/Cocoa native version currently. ^^

EVT_DATE_CHANGED: int  # Process a wxEVT_DATE_CHANGED event, which fires when the user changes the current selection in the control. ^^

class HyperlinkCtrl(Control):
    """ **Possible constructors**:



```
HyperlinkCtrl()

HyperlinkCtrl(parent, id=ID_ANY, label="", url="", pos=DefaultPosition,
              size=DefaultSize, style=HL_DEFAULT_STYLE, name=HyperlinkCtrlNameStr)

```


This class shows a static text element which links to an URL.


  


        Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.HyperlinkCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, label=””, url=””, pos=DefaultPosition, size=DefaultSize, style=HL\_DEFAULT\_STYLE, name=HyperlinkCtrlNameStr)*


Constructor.


See [`Create`](#wx.adv.HyperlinkCtrl.Create "wx.adv.HyperlinkCtrl.Create") for more info.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **label** (*string*) –
* **url** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def Create(self, parent, id=ID_ANY, label="", url="", pos=DefaultPosition, size=DefaultSize, style=HL_DEFAULT_STYLE, name=HyperlinkCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *label=""*, *url=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=HL\_DEFAULT\_STYLE*, *name=HyperlinkCtrlNameStr*)[¶](#wx.adv.HyperlinkCtrl.Create "Permalink to this definition")
Creates the hyperlink control.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Window identifier. A value of `wx.ID_ANY` indicates a default value.
* **label** (*string*) – The label of the hyperlink.
* **url** (*string*) – The URL associated with the given label.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. If the DefaultSize is specified then the window is sized appropriately.
* **style** (*long*) – Window style. See  [wx.adv.HyperlinkCtrl](#wx-adv-hyperlinkctrl).
* **name** (*string*) – Window name.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.HyperlinkCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetHoverColour(self) -> 'Colour':
        """ 

`GetHoverColour`(*self*)[¶](#wx.adv.HyperlinkCtrl.GetHoverColour "Permalink to this definition")
Returns the colour used to print the label of the hyperlink when the mouse is over the control.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetNormalColour(self) -> 'Colour':
        """ 

`GetNormalColour`(*self*)[¶](#wx.adv.HyperlinkCtrl.GetNormalColour "Permalink to this definition")
Returns the colour used to print the label when the link has never been clicked before (i.e. the link has not been *visited*) and the mouse is not over the control.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetURL(self) -> str:
        """ 

`GetURL`(*self*)[¶](#wx.adv.HyperlinkCtrl.GetURL "Permalink to this definition")
Returns the URL associated with the hyperlink.



Return type
`string`






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetVisited(self) -> bool:
        """ 

`GetVisited`(*self*)[¶](#wx.adv.HyperlinkCtrl.GetVisited "Permalink to this definition")
Returns `True` if the hyperlink has already been clicked by the user at least one time.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def GetVisitedColour(self) -> 'Colour':
        """ 

`GetVisitedColour`(*self*)[¶](#wx.adv.HyperlinkCtrl.GetVisitedColour "Permalink to this definition")
Returns the colour used to print the label when the mouse is not over the control and the link has already been clicked before (i.e. the link has been *visited*).



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetHoverColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHoverColour`(*self*, *colour*)[¶](#wx.adv.HyperlinkCtrl.SetHoverColour "Permalink to this definition")
Sets the colour used to print the label of the hyperlink when the mouse is over the control.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetNormalColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetNormalColour`(*self*, *colour*)[¶](#wx.adv.HyperlinkCtrl.SetNormalColour "Permalink to this definition")
Sets the colour used to print the label when the link has never been clicked before (i.e. the link has not been *visited*) and the mouse is not over the control.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetURL(self, url: str) -> None:
        """ 

`SetURL`(*self*, *url*)[¶](#wx.adv.HyperlinkCtrl.SetURL "Permalink to this definition")
Sets the URL associated with the hyperlink.



Parameters
**url** (*string*) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ 

`SetVisited`(*self*, *visited=True*)[¶](#wx.adv.HyperlinkCtrl.SetVisited "Permalink to this definition")
Marks the hyperlink as visited (see [`wx.adv.HyperlinkCtrl.SetVisitedColour`](#wx.adv.HyperlinkCtrl.SetVisitedColour "wx.adv.HyperlinkCtrl.SetVisitedColour") ).



Parameters
**visited** (*bool*) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    def SetVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetVisitedColour`(*self*, *colour*)[¶](#wx.adv.HyperlinkCtrl.SetVisitedColour "Permalink to this definition")
Sets the colour used to print the label when the mouse is not over the control and the link has already been clicked before (i.e. the link has been *visited*).



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.HyperlinkCtrl.html
        """

    HoverColour: 'Colour'  # `HoverColour`[¶](#wx.adv.HyperlinkCtrl.HoverColour "Permalink to this definition")See [`GetHoverColour`](#wx.adv.HyperlinkCtrl.GetHoverColour "wx.adv.HyperlinkCtrl.GetHoverColour") and [`SetHoverColour`](#wx.adv.HyperlinkCtrl.SetHoverColour "wx.adv.HyperlinkCtrl.SetHoverColour")
    NormalColour: 'Colour'  # `NormalColour`[¶](#wx.adv.HyperlinkCtrl.NormalColour "Permalink to this definition")See [`GetNormalColour`](#wx.adv.HyperlinkCtrl.GetNormalColour "wx.adv.HyperlinkCtrl.GetNormalColour") and [`SetNormalColour`](#wx.adv.HyperlinkCtrl.SetNormalColour "wx.adv.HyperlinkCtrl.SetNormalColour")
    URL: str  # `URL`[¶](#wx.adv.HyperlinkCtrl.URL "Permalink to this definition")See [`GetURL`](#wx.adv.HyperlinkCtrl.GetURL "wx.adv.HyperlinkCtrl.GetURL") and [`SetURL`](#wx.adv.HyperlinkCtrl.SetURL "wx.adv.HyperlinkCtrl.SetURL")
    Visited: bool  # `Visited`[¶](#wx.adv.HyperlinkCtrl.Visited "Permalink to this definition")See [`GetVisited`](#wx.adv.HyperlinkCtrl.GetVisited "wx.adv.HyperlinkCtrl.GetVisited") and [`SetVisited`](#wx.adv.HyperlinkCtrl.SetVisited "wx.adv.HyperlinkCtrl.SetVisited")
    VisitedColour: 'Colour'  # `VisitedColour`[¶](#wx.adv.HyperlinkCtrl.VisitedColour "Permalink to this definition")See [`GetVisitedColour`](#wx.adv.HyperlinkCtrl.GetVisitedColour "wx.adv.HyperlinkCtrl.GetVisitedColour") and [`SetVisitedColour`](#wx.adv.HyperlinkCtrl.SetVisitedColour "wx.adv.HyperlinkCtrl.SetVisitedColour")



HL_ALIGN_LEFT: int  # Align the text to the left.

HL_ALIGN_RIGHT: int  # Align the text to the right. This style is not supported under Windows.

HL_ALIGN_CENTRE: int  # Center the text (horizontally). This style is not supported under Windows.

HL_CONTEXTMENU: int  # Pop up a context menu when the hyperlink is right-clicked. The context menu contains a “Copy URL” menu item which is automatically handled by the hyperlink and which just copies in the clipboard the URL (not the label) of the control.

HL_DEFAULT_STYLE: int  # The default style for   wx.adv.HyperlinkCtrl: BORDER_NONE|wxHL_CONTEXTMENU|wxHL_ALIGN_CENTRE. ^^

class TimePickerCtrl(Control):
    """ **Possible constructors**:



```
TimePickerCtrl()

TimePickerCtrl(parent, id=ID_ANY, dt=DefaultDateTime,
               pos=DefaultPosition, size=DefaultSize, style=TP_DEFAULT,
               validator=DefaultValidator, name=TimePickerCtrlNameStr)

```


This control allows the user to enter time.


  


        Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.TimePickerCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=TP\_DEFAULT, validator=DefaultValidator, name=TimePickerCtrlNameStr)*


Initializes the object and calls [`Create`](#wx.adv.TimePickerCtrl.Create "wx.adv.TimePickerCtrl.Create") with all the parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def Create(self, parent, id=ID_ANY, dt=DefaultDateTime, pos=DefaultPosition, size=DefaultSize, style=TP_DEFAULT, validator=DefaultValidator, name=TimePickerCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *dt=DefaultDateTime*, *pos=DefaultPosition*, *size=DefaultSize*, *style=TP\_DEFAULT*, *validator=DefaultValidator*, *name=TimePickerCtrlNameStr*)[¶](#wx.adv.TimePickerCtrl.Create "Permalink to this definition")
Create the control window.


This method should only be used for objects created using default constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window, must not be not `None`.
* **id** (*wx.WindowID*) – The identifier for the control.
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – The initial value of the control, if an invalid date (such as the default value) is used, the control is set to current time.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size. If left at default value, the control chooses its own best size by using the height approximately equal to a text control and width large enough to show the time fully.
* **style** (*long*) – The window style, should be left at 0 as there are no special styles for this control in this version.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Validator which can be used for additional checks.
* **name** (*string*) – Control name.



Return type
*bool*



Returns
`True` if the control was successfully created or `False` if creation failed.






            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.TimePickerCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def GetTime(self) -> tuple:
        """ 

`GetTime`(*self*)[¶](#wx.adv.TimePickerCtrl.GetTime "Permalink to this definition")
Returns the currently entered time as hours, minutes and seconds.


All the arguments must be not `None`, `False` is returned otherwise and none of them is modified.



Return type
*tuple*



Returns
( *hour*, *min*, *sec* )





New in version 2.9.4.




See also


[`SetTime`](#wx.adv.TimePickerCtrl.SetTime "wx.adv.TimePickerCtrl.SetTime")





            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def GetValue(self) -> 'DateTime':
        """ 

`GetValue`(*self*)[¶](#wx.adv.TimePickerCtrl.GetValue "Permalink to this definition")
Returns the currently entered time.


The date part of the returned  [wx.DateTime](wx.DateTime.html#wx-datetime) object is always set to today and should be ignored, only the time part is relevant.



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def SetTime(self, hour, min, sec) -> bool:
        """ 

`SetTime`(*self*, *hour*, *min*, *sec*)[¶](#wx.adv.TimePickerCtrl.SetTime "Permalink to this definition")
Changes the current time of the control.


Calling this method does not result in a time change event.



Parameters
* **hour** (*int*) – The new hour value in 0..23 interval.
* **min** (*int*) – The new minute value in 0..59 interval.
* **sec** (*int*) – The new second value in 0..59 interval.



Return type
*bool*



Returns
`True` if the time was changed or `False` on failure, e.g. if the time components were invalid.





New in version 2.9.4.




See also


[`GetTime`](#wx.adv.TimePickerCtrl.GetTime "wx.adv.TimePickerCtrl.GetTime")





            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    def SetValue(self, dt: 'DateTime') -> None:
        """ 

`SetValue`(*self*, *dt*)[¶](#wx.adv.TimePickerCtrl.SetValue "Permalink to this definition")
Changes the current value of the control.


The date part of *dt* is ignored, only the time part is displayed in the control. The *dt* object must however be valid.


In particular, notice that it is a bad idea to use default  [wx.DateTime](wx.DateTime.html#wx-datetime) constructor from hour, minute and second values as it uses the today date for the date part, which means that some values can be invalid if today happens to be the day of `DST` change. For example, when switching to summer time, the time 2:00 typically doesn’t exist as the clocks jump directly to 3:00. To avoid this problem, use a fixed date on which `DST` is known not to change (e.g. Jan 1, 2012) for the date part of the argument or use [`SetTime`](#wx.adv.TimePickerCtrl.SetTime "wx.adv.TimePickerCtrl.SetTime") .


Calling this method does not result in a time change event.



Parameters
**dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 






            Source: https://docs.wxpython.org/wx.adv.TimePickerCtrl.html
        """

    Value: 'DateTime'  # `Value`[¶](#wx.adv.TimePickerCtrl.Value "Permalink to this definition")See [`GetValue`](#wx.adv.TimePickerCtrl.GetValue "wx.adv.TimePickerCtrl.GetValue") and [`SetValue`](#wx.adv.TimePickerCtrl.SetValue "wx.adv.TimePickerCtrl.SetValue")



EVT_TIME_CHANGED: int  # Process a wxEVT_TIME_CHANGED event, which fires when the user changes the current selection in the control. ^^

class PropertySheetDialog(Dialog):
    """ **Possible constructors**:



```
PropertySheetDialog()

PropertySheetDialog(parent, id=ID_ANY, title="", pos=DefaultPosition,
                    size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr)

```


This class represents a property sheet dialog: a tabbed dialog for
showing settings.


  


        Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.PropertySheetDialog.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


Call Create if using this form of constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, title=””, pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_DIALOG\_STYLE, name=DialogNameStr)*


Constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def AddBookCtrl(self, sizer: 'Sizer') -> None:
        """ 

`AddBookCtrl`(*self*, *sizer*)[¶](#wx.adv.PropertySheetDialog.AddBookCtrl "Permalink to this definition")
Override this if you wish to add the book control in a way different from the standard way (for example, using different spacing).



Parameters
**sizer** ([*wx.Sizer*](wx.Sizer.html#wx.Sizer "wx.Sizer")) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def Create(self, parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_DIALOG_STYLE, name=DialogNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *title=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DEFAULT\_DIALOG\_STYLE*, *name=DialogNameStr*)[¶](#wx.adv.PropertySheetDialog.Create "Permalink to this definition")
Call this from your own Create function, before adding buttons and pages.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def CreateBookCtrl(self) -> 'BookCtrlBase':
        """ 

`CreateBookCtrl`(*self*)[¶](#wx.adv.PropertySheetDialog.CreateBookCtrl "Permalink to this definition")
Override this if you wish to create a different kind of book control; by default, the value passed to [`SetSheetStyle`](#wx.adv.PropertySheetDialog.SetSheetStyle "wx.adv.PropertySheetDialog.SetSheetStyle") is used to determine the control.


The default behaviour is to create a notebook except on Smartphone, where a choicebook is used.



Return type
*BookCtrlBase*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def CreateButtons(self, flags: int=OK|CANCEL) -> None:
        """ 

`CreateButtons`(*self*, *flags=OK|CANCEL*)[¶](#wx.adv.PropertySheetDialog.CreateButtons "Permalink to this definition")
Call this to create the buttons for the dialog.


This calls [`wx.Dialog.CreateButtonSizer`](wx.Dialog.html#wx.Dialog.CreateButtonSizer "wx.Dialog.CreateButtonSizer") , and the flags are the same.



Parameters
**flags** (*int*) – 





Note


On PocketPC, no buttons are created.





            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetBookCtrl(self) -> 'BookCtrlBase':
        """ 

`GetBookCtrl`(*self*)[¶](#wx.adv.PropertySheetDialog.GetBookCtrl "Permalink to this definition")
Returns the book control that will contain your settings pages.



Return type
*BookCtrlBase*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.PropertySheetDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetContentWindow(self) -> 'Window':
        """ 

`GetContentWindow`(*self*)[¶](#wx.adv.PropertySheetDialog.GetContentWindow "Permalink to this definition")
Override this to return a window containing the main content of the dialog.


This is particularly useful when the dialog implements pages, such as  [wx.adv.PropertySheetDialog](#wx-adv-propertysheetdialog), and allows the [layout adaptation code](dialog_overview.html#layout-adaptation-code) to know that only the pages need to be made scrollable.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetInnerSizer(self) -> 'Sizer':
        """ 

`GetInnerSizer`(*self*)[¶](#wx.adv.PropertySheetDialog.GetInnerSizer "Permalink to this definition")
Returns the inner sizer that contains the book control and button sizer.



Return type
`Sizer`






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetInnerBorder(self) -> int:
        """ 

`GetSheetInnerBorder`(*self*)[¶](#wx.adv.PropertySheetDialog.GetSheetInnerBorder "Permalink to this definition")
Returns the border around the book control only.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetOuterBorder(self) -> int:
        """ 

`GetSheetOuterBorder`(*self*)[¶](#wx.adv.PropertySheetDialog.GetSheetOuterBorder "Permalink to this definition")
Returns the border around the whole dialog.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def GetSheetStyle(self) -> int:
        """ 

`GetSheetStyle`(*self*)[¶](#wx.adv.PropertySheetDialog.GetSheetStyle "Permalink to this definition")
Returns the sheet style.


See [`SetSheetStyle`](#wx.adv.PropertySheetDialog.SetSheetStyle "wx.adv.PropertySheetDialog.SetSheetStyle") for allowed values.



Return type
*long*






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def LayoutDialog(self, centreFlags: int=BOTH) -> None:
        """ 

`LayoutDialog`(*self*, *centreFlags=BOTH*)[¶](#wx.adv.PropertySheetDialog.LayoutDialog "Permalink to this definition")
Call this to lay out the dialog.



Parameters
**centreFlags** (*int*) – 





Note


On PocketPC, this does nothing, since the dialog will be shown full-screen, and the layout will be done when the dialog receives a size event.





            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetBookCtrl(self, bookCtrl: 'BookCtrlBase') -> None:
        """ 

`SetBookCtrl`(*self*, *bookCtrl*)[¶](#wx.adv.PropertySheetDialog.SetBookCtrl "Permalink to this definition")
Sets the book control used for the dialog.


You will normally not need to use this.



Parameters
**bookCtrl** ([*wx.BookCtrlBase*](wx.BookCtrlBase.html#wx.BookCtrlBase "wx.BookCtrlBase")) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetInnerSizer(self, sizer: 'Sizer') -> None:
        """ 

`SetInnerSizer`(*self*, *sizer*)[¶](#wx.adv.PropertySheetDialog.SetInnerSizer "Permalink to this definition")
Set the inner sizer that contains the book control and button sizer.



Parameters
**sizer** ([*wx.Sizer*](wx.Sizer.html#wx.Sizer "wx.Sizer")) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetInnerBorder(self, border: int) -> None:
        """ 

`SetSheetInnerBorder`(*self*, *border*)[¶](#wx.adv.PropertySheetDialog.SetSheetInnerBorder "Permalink to this definition")
Set the border around the book control only.



Parameters
**border** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetOuterBorder(self, border: int) -> None:
        """ 

`SetSheetOuterBorder`(*self*, *border*)[¶](#wx.adv.PropertySheetDialog.SetSheetOuterBorder "Permalink to this definition")
Set the border around the whole dialog.



Parameters
**border** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    def SetSheetStyle(self, style: int) -> None:
        """ 

`SetSheetStyle`(*self*, *style*)[¶](#wx.adv.PropertySheetDialog.SetSheetStyle "Permalink to this definition")
You can customize the look and feel of the dialog by setting the sheet style.


It is a bit list of the  [wx.adv.PropertySheetDialogFlags](wx.adv.PropertySheetDialogFlags.enumeration.html#wx-adv-propertysheetdialogflags) values.



Parameters
**style** (*long*) – 






            Source: https://docs.wxpython.org/wx.adv.PropertySheetDialog.html
        """

    BookCtrl: 'BookCtrlBase'  # `BookCtrl`[¶](#wx.adv.PropertySheetDialog.BookCtrl "Permalink to this definition")See [`GetBookCtrl`](#wx.adv.PropertySheetDialog.GetBookCtrl "wx.adv.PropertySheetDialog.GetBookCtrl") and [`SetBookCtrl`](#wx.adv.PropertySheetDialog.SetBookCtrl "wx.adv.PropertySheetDialog.SetBookCtrl")
    ContentWindow: 'Window'  # `ContentWindow`[¶](#wx.adv.PropertySheetDialog.ContentWindow "Permalink to this definition")See [`GetContentWindow`](#wx.adv.PropertySheetDialog.GetContentWindow "wx.adv.PropertySheetDialog.GetContentWindow")
    InnerSizer: 'Sizer'  # `InnerSizer`[¶](#wx.adv.PropertySheetDialog.InnerSizer "Permalink to this definition")See [`GetInnerSizer`](#wx.adv.PropertySheetDialog.GetInnerSizer "wx.adv.PropertySheetDialog.GetInnerSizer") and [`SetInnerSizer`](#wx.adv.PropertySheetDialog.SetInnerSizer "wx.adv.PropertySheetDialog.SetInnerSizer")
    SheetInnerBorder: int  # `SheetInnerBorder`[¶](#wx.adv.PropertySheetDialog.SheetInnerBorder "Permalink to this definition")See [`GetSheetInnerBorder`](#wx.adv.PropertySheetDialog.GetSheetInnerBorder "wx.adv.PropertySheetDialog.GetSheetInnerBorder") and [`SetSheetInnerBorder`](#wx.adv.PropertySheetDialog.SetSheetInnerBorder "wx.adv.PropertySheetDialog.SetSheetInnerBorder")
    SheetOuterBorder: int  # `SheetOuterBorder`[¶](#wx.adv.PropertySheetDialog.SheetOuterBorder "Permalink to this definition")See [`GetSheetOuterBorder`](#wx.adv.PropertySheetDialog.GetSheetOuterBorder "wx.adv.PropertySheetDialog.GetSheetOuterBorder") and [`SetSheetOuterBorder`](#wx.adv.PropertySheetDialog.SetSheetOuterBorder "wx.adv.PropertySheetDialog.SetSheetOuterBorder")
    SheetStyle: int  # `SheetStyle`[¶](#wx.adv.PropertySheetDialog.SheetStyle "Permalink to this definition")See [`GetSheetStyle`](#wx.adv.PropertySheetDialog.GetSheetStyle "wx.adv.PropertySheetDialog.GetSheetStyle") and [`SetSheetStyle`](#wx.adv.PropertySheetDialog.SetSheetStyle "wx.adv.PropertySheetDialog.SetSheetStyle")



class Wizard(Dialog):
    """ **Possible constructors**:



```
Wizard()

Wizard(parent, id=ID_ANY, title="", bitmap=BitmapBundle(),
       pos=DefaultPosition, style=DEFAULT_DIALOG_STYLE)

```


Wizard is the central class for implementing ‘wizard-like’ dialogs.


  


        Source: https://docs.wxpython.org/wx.adv.Wizard.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.Wizard.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


Use this if you wish to derive from  [wx.adv.Wizard](#wx-adv-wizard) and then call [`Create`](#wx.adv.Wizard.Create "wx.adv.Wizard.Create") , for example if you wish to set an extra style with [`wx.Window.SetExtraStyle`](wx.Window.html#wx.Window.SetExtraStyle "wx.Window.SetExtraStyle") between the two calls.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, title=””, bitmap=BitmapBundle(), pos=DefaultPosition, style=DEFAULT\_DIALOG\_STYLE)*


Constructor which really creates the wizard – if you use this constructor, you shouldn’t call [`Create`](#wx.adv.Wizard.Create "wx.adv.Wizard.Create") .


Notice that unlike almost all other wxWidgets classes, there is no *size* parameter in the  [wx.adv.Wizard](#wx-adv-wizard) constructor because the wizard will have a predefined default size by default. If you want to change this, you should use the [`GetPageAreaSizer`](#wx.adv.Wizard.GetPageAreaSizer "wx.adv.Wizard.GetPageAreaSizer") function.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The parent window, may be `None`.
* **id** (*int*) – The id of the dialog, will usually be just `wx.ID_ANY`.
* **title** (*string*) – The title of the dialog.
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – The default bitmap used in the left side of the wizard. See also [`GetBitmap`](#wx.adv.Wizard.GetBitmap "wx.adv.Wizard.GetBitmap") .
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The position of the dialog, it will be centered on the screen by default.
* **style** (*long*) – Window style is passed to  [wx.Dialog](wx.Dialog.html#wx-dialog).






---

  





            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *title=""*, *bitmap=BitmapBundle()*, *pos=DefaultPosition*, *style=DEFAULT\_DIALOG\_STYLE*)[¶](#wx.adv.Wizard.Create "Permalink to this definition")
Creates the wizard dialog.


Must be called if the default constructor had been used to create the object.


Notice that unlike almost all other wxWidgets classes, there is no *size* parameter in the  [wx.adv.Wizard](#wx-adv-wizard) constructor because the wizard will have a predefined default size by default. If you want to change this, you should use the [`GetPageAreaSizer`](#wx.adv.Wizard.GetPageAreaSizer "wx.adv.Wizard.GetPageAreaSizer") function.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The parent window, may be `None`.
* **id** (*int*) – The id of the dialog, will usually be just -1.
* **title** (*string*) – The title of the dialog.
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – The default bitmap used in the left side of the wizard. See also [`GetBitmap`](#wx.adv.Wizard.GetBitmap "wx.adv.Wizard.GetBitmap") .
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The position of the dialog, it will be centered on the screen by default.
* **style** (*long*) – Window style is passed to  [wx.Dialog](wx.Dialog.html#wx-dialog).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def FitToPage(self, firstPage: 'adv.WizardPage') -> None:
        """ 

`FitToPage`(*self*, *firstPage*)[¶](#wx.adv.Wizard.FitToPage "Permalink to this definition")
This method is obsolete, use [`GetPageAreaSizer`](#wx.adv.Wizard.GetPageAreaSizer "wx.adv.Wizard.GetPageAreaSizer") instead.


Sets the page size to be big enough for all the pages accessible via the given *firstPage*, i.e. this page, its next page and so on.


This method may be called more than once and it will only change the page size if the size required by the new page is bigger than the previously set one. This is useful if the decision about which pages to show is taken during run-time, as in this case, the wizard won’t be able to get to all pages starting from a single one and you should call `Fit` separately for the others.



Parameters
**firstPage** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.adv.Wizard.GetBitmap "Permalink to this definition")
Returns the bitmap used for the wizard.



Return type
[`Bitmap`](#wx.adv.Wizard.Bitmap "wx.adv.Wizard.Bitmap")






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmapBackgroundColour(self) -> 'Colour':
        """ 

`GetBitmapBackgroundColour`(*self*)[¶](#wx.adv.Wizard.GetBitmapBackgroundColour "Permalink to this definition")
Returns the colour that should be used to fill the area not taken up by the wizard or page bitmap, if a non-zero bitmap placement flag has been set.


See also [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement") .



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetBitmapPlacement(self) -> int:
        """ 

`GetBitmapPlacement`(*self*)[¶](#wx.adv.Wizard.GetBitmapPlacement "Permalink to this definition")
Returns the flags indicating how the wizard or page bitmap should be expanded and positioned to fit the page height.


By default, placement is 0 (no expansion is done).


See also [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement") for the possible values.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.Wizard.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetCurrentPage(self) -> 'WizardPage':
        """ 

`GetCurrentPage`(*self*)[¶](#wx.adv.Wizard.GetCurrentPage "Permalink to this definition")
Get the current page while the wizard is running.


`None` is returned if [`RunWizard`](#wx.adv.Wizard.RunWizard "wx.adv.Wizard.RunWizard") is not being executed now.



Return type
 [wx.adv.WizardPage](wx.adv.WizardPage.html#wx-adv-wizardpage)






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetMinimumBitmapWidth(self) -> int:
        """ 

`GetMinimumBitmapWidth`(*self*)[¶](#wx.adv.Wizard.GetMinimumBitmapWidth "Permalink to this definition")
Returns the minimum width for the bitmap that will be constructed to contain the actual wizard or page bitmap if a non-zero bitmap placement flag has been set.


See also [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement") .



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetPageAreaSizer(self) -> 'Sizer':
        """ 

`GetPageAreaSizer`(*self*)[¶](#wx.adv.Wizard.GetPageAreaSizer "Permalink to this definition")
Returns pointer to page area sizer.


The wizard is laid out using sizers and the page area sizer is the place-holder for the pages. All pages are resized before being shown to match the wizard page area.


Page area sizer has a minimal size that is the maximum of several values. First, all pages (or other objects) added to the sizer. Second, all pages reachable by repeatedly applying [`wx.adv.WizardPage.GetNext`](wx.adv.WizardPage.html#wx.adv.WizardPage.GetNext "wx.adv.WizardPage.GetNext") to any page inserted into the sizer.


Third, the minimal size specified using [`SetPageSize`](#wx.adv.Wizard.SetPageSize "wx.adv.Wizard.SetPageSize") and [`FitToPage`](#wx.adv.Wizard.FitToPage "wx.adv.Wizard.FitToPage") . Fourth, the total wizard height may be increased to accommodate the bitmap height. Fifth and finally, wizards are never smaller than some built-in minimal size to avoid wizards that are too small.


The caller can use [`wx.Sizer.SetMinSize`](wx.Sizer.html#wx.Sizer.SetMinSize "wx.Sizer.SetMinSize") to enlarge it beyond the minimal size. If `RESIZE_BORDER` was passed to constructor, user can resize wizard and consequently the page area (but not make it smaller than the minimal size).


It is recommended to add the first page to the page area sizer. For simple wizards, this will enlarge the wizard to fit the biggest page.


For non-linear wizards, the first page of every separate chain should be added. Caller-specified size can be accomplished using [`wx.Sizer.SetMinSize`](wx.Sizer.html#wx.Sizer.SetMinSize "wx.Sizer.SetMinSize") . Adding pages to the page area sizer affects the default border width around page area that can be altered with [`SetBorder`](#wx.adv.Wizard.SetBorder "wx.adv.Wizard.SetBorder") .



Return type
`Sizer`






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def GetPageSize(self) -> 'Size':
        """ 

`GetPageSize`(*self*)[¶](#wx.adv.Wizard.GetPageSize "Permalink to this definition")
Returns the size available for the pages.



Return type
`Size`






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def HasNextPage(self, page: 'adv.WizardPage') -> bool:
        """ 

`HasNextPage`(*self*, *page*)[¶](#wx.adv.Wizard.HasNextPage "Permalink to this definition")
Return `True` if this page is not the last one in the wizard.


The base class version implements this by calling `page->GetNext` but this could be undesirable if, for example, the pages are created on demand only.



Parameters
**page** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 



Return type
*bool*





See also


[`HasPrevPage`](#wx.adv.Wizard.HasPrevPage "wx.adv.Wizard.HasPrevPage")





            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def HasPrevPage(self, page: 'adv.WizardPage') -> bool:
        """ 

`HasPrevPage`(*self*, *page*)[¶](#wx.adv.Wizard.HasPrevPage "Permalink to this definition")
Returns `True` if this page is not the first one in the wizard.


The base class version implements this by calling `page->GetPrev` but this could be undesirable if, for example, the pages are created on demand only.



Parameters
**page** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 



Return type
*bool*





See also


[`HasNextPage`](#wx.adv.Wizard.HasNextPage "wx.adv.Wizard.HasNextPage")





            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def IsRunning(self) -> bool:
        """ 

`IsRunning`(*self*)[¶](#wx.adv.Wizard.IsRunning "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def RunWizard(self, firstPage: 'adv.WizardPage') -> bool:
        """ 

`RunWizard`(*self*, *firstPage*)[¶](#wx.adv.Wizard.RunWizard "Permalink to this definition")
Executes the wizard starting from the given page, returning `True` if it was successfully finished or `False` if user cancelled it.


The *firstPage* cannot be `None`.



Parameters
**firstPage** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.adv.Wizard.SetBitmap "Permalink to this definition")
Sets the bitmap used for the wizard.



Parameters
**bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmapBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBitmapBackgroundColour`(*self*, *colour*)[¶](#wx.adv.Wizard.SetBitmapBackgroundColour "Permalink to this definition")
Sets the colour that should be used to fill the area not taken up by the wizard or page bitmap, if a non-zero bitmap placement flag has been set.


See also [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement") .



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBitmapPlacement(self, placement: int) -> None:
        """ 

`SetBitmapPlacement`(*self*, *placement*)[¶](#wx.adv.Wizard.SetBitmapPlacement "Permalink to this definition")
Sets the flags indicating how the wizard or page bitmap should be expanded and positioned to fit the page height.


By default, placement is 0 (no expansion is done). *placement* is a bitlist with the following possible values:


* `wx.adv.WIZARD_VALIGN_TOP`: Aligns the bitmap at the top.
* `wx.adv.WIZARD_VALIGN_CENTRE`: Centres the bitmap vertically.
* `wx.adv.WIZARD_VALIGN_BOTTOM`: Aligns the bitmap at the bottom.
* `wx.adv.WIZARD_HALIGN_LEFT`: Left-aligns the bitmap.
* `wx.adv.WIZARD_HALIGN_CENTRE`: Centres the bitmap horizontally.
* `wx.adv.WIZARD_HALIGN_RIGHT`: Right-aligns the bitmap.
* `wx.adv.WIZARD_TILE`: The bitmap will be tiled to fit available space.


See also [`SetMinimumBitmapWidth`](#wx.adv.Wizard.SetMinimumBitmapWidth "wx.adv.Wizard.SetMinimumBitmapWidth") .



Parameters
**placement** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetBorder(self, border: int) -> None:
        """ 

`SetBorder`(*self*, *border*)[¶](#wx.adv.Wizard.SetBorder "Permalink to this definition")
Sets width of border around page area.


Default is zero. For backward compatibility, if there are no pages in [`GetPageAreaSizer`](#wx.adv.Wizard.GetPageAreaSizer "wx.adv.Wizard.GetPageAreaSizer") , the default is 5 pixels.


If there is a five point border around all controls in a page and the border around page area is left as zero, a five point white space along all dialog borders will be added to the control border in order to space page controls ten points from the dialog border and non-page controls.



Parameters
**border** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetMinimumBitmapWidth(self, width: int) -> None:
        """ 

`SetMinimumBitmapWidth`(*self*, *width*)[¶](#wx.adv.Wizard.SetMinimumBitmapWidth "Permalink to this definition")
Sets the minimum width for the bitmap that will be constructed to contain the actual wizard or page bitmap if a non-zero bitmap placement flag has been set.


If this is not set when using bitmap placement, the initial layout may be incorrect.


See also [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement") .



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def SetPageSize(self, sizePage: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetPageSize`(*self*, *sizePage*)[¶](#wx.adv.Wizard.SetPageSize "Permalink to this definition")
Sets the minimal size to be made available for the wizard pages.


The wizard will take into account the size of the bitmap (if any) itself. Also, the wizard will never be smaller than the default size.


The recommended way to use this function is to lay out all wizard pages using the sizers (even though the wizard is not resizable) and then use [`wx.Sizer.CalcMin`](wx.Sizer.html#wx.Sizer.CalcMin "wx.Sizer.CalcMin") in a loop to calculate the maximum of minimal sizes of the pages and pass it to [`SetPageSize`](#wx.adv.Wizard.SetPageSize "wx.adv.Wizard.SetPageSize") .



Parameters
**sizePage** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    def ShowPage(self, page, goingForward=True) -> bool:
        """ 

`ShowPage`(*self*, *page*, *goingForward=True*)[¶](#wx.adv.Wizard.ShowPage "Permalink to this definition")
Show the given wizard page.



> Calls TransferDataFromWindow on the current page first, and
> returns `False` without changing the page if it returned `False`.
> Returns True/False to indicate if the page was actually
> changed.



Parameters
* **page** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –
* **goingForward** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Wizard.html
        """

    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.adv.Wizard.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.adv.Wizard.GetBitmap "wx.adv.Wizard.GetBitmap") and [`SetBitmap`](#wx.adv.Wizard.SetBitmap "wx.adv.Wizard.SetBitmap")
    BitmapBackgroundColour: 'Colour'  # `BitmapBackgroundColour`[¶](#wx.adv.Wizard.BitmapBackgroundColour "Permalink to this definition")See [`GetBitmapBackgroundColour`](#wx.adv.Wizard.GetBitmapBackgroundColour "wx.adv.Wizard.GetBitmapBackgroundColour") and [`SetBitmapBackgroundColour`](#wx.adv.Wizard.SetBitmapBackgroundColour "wx.adv.Wizard.SetBitmapBackgroundColour")
    BitmapPlacement: int  # `BitmapPlacement`[¶](#wx.adv.Wizard.BitmapPlacement "Permalink to this definition")See [`GetBitmapPlacement`](#wx.adv.Wizard.GetBitmapPlacement "wx.adv.Wizard.GetBitmapPlacement") and [`SetBitmapPlacement`](#wx.adv.Wizard.SetBitmapPlacement "wx.adv.Wizard.SetBitmapPlacement")
    CurrentPage: 'WizardPage'  # `CurrentPage`[¶](#wx.adv.Wizard.CurrentPage "Permalink to this definition")See [`GetCurrentPage`](#wx.adv.Wizard.GetCurrentPage "wx.adv.Wizard.GetCurrentPage")
    MinimumBitmapWidth: int  # `MinimumBitmapWidth`[¶](#wx.adv.Wizard.MinimumBitmapWidth "Permalink to this definition")See [`GetMinimumBitmapWidth`](#wx.adv.Wizard.GetMinimumBitmapWidth "wx.adv.Wizard.GetMinimumBitmapWidth") and [`SetMinimumBitmapWidth`](#wx.adv.Wizard.SetMinimumBitmapWidth "wx.adv.Wizard.SetMinimumBitmapWidth")
    PageAreaSizer: 'Sizer'  # `PageAreaSizer`[¶](#wx.adv.Wizard.PageAreaSizer "Permalink to this definition")See [`GetPageAreaSizer`](#wx.adv.Wizard.GetPageAreaSizer "wx.adv.Wizard.GetPageAreaSizer")
    PageSize: 'Size'  # `PageSize`[¶](#wx.adv.Wizard.PageSize "Permalink to this definition")See [`GetPageSize`](#wx.adv.Wizard.GetPageSize "wx.adv.Wizard.GetPageSize") and [`SetPageSize`](#wx.adv.Wizard.SetPageSize "wx.adv.Wizard.SetPageSize")



EVT_WIZARD_PAGE_CHANGED: int  # The page has just been changed (this event cannot be vetoed).

EVT_WIZARD_PAGE_CHANGING: int  # The page is being changed (this event can be vetoed).

EVT_WIZARD_BEFORE_PAGE_CHANGED: int  # Called after Next is clicked but before GetNext is called. Unlike EVT_WIZARD_CHANGING, the handler for this function can change state that might affect the return value of GetNext. This event can be vetoed.

EVT_WIZARD_PAGE_SHOWN: int  # The page was shown and laid out (this event cannot be vetoed).

EVT_WIZARD_CANCEL: int  # The user attempted to cancel the wizard (this event may also be vetoed).

EVT_WIZARD_HELP: int  # The wizard help button was pressed.

EVT_WIZARD_FINISHED: int  # The wizard finished button was pressed. ^^

WIZARD_EX_HELPBUTTON: int

ID_HELP: int

WIZARD_VALIGN_TOP: int

WIZARD_VALIGN_CENTRE: int

WIZARD_VALIGN_BOTTOM: int

WIZARD_HALIGN_LEFT: int

WIZARD_HALIGN_CENTRE: int

WIZARD_HALIGN_RIGHT: int

WIZARD_TILE: int

class CalculateLayoutEvent(Event):
    """ **Possible constructors**:



```
CalculateLayoutEvent(id=0)

```


This event is sent by LayoutAlgorithm to calculate the amount of the
remaining client area that the window should occupy.


  


        Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
    """
    def __init__(self, id: int=0) -> None:
        """ 

`__init__`(*self*, *id=0*)[¶](#wx.adv.CalculateLayoutEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
**id** (*wx.WindowID*) – 






            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.adv.CalculateLayoutEvent.GetFlags "Permalink to this definition")
Returns the flags associated with this event.


Not currently used.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def GetRect(self) -> 'Rect':
        """ 

`GetRect`(*self*)[¶](#wx.adv.CalculateLayoutEvent.GetRect "Permalink to this definition")
Before the event handler is entered, returns the remaining parent client area that the window could occupy.


When the event handler returns, this should contain the remaining parent client rectangle, after the event handler has subtracted the area that its window occupies.



Return type
[`Rect`](#wx.adv.CalculateLayoutEvent.Rect "wx.adv.CalculateLayoutEvent.Rect")






            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.adv.CalculateLayoutEvent.SetFlags "Permalink to this definition")
Sets the flags associated with this event.


Not currently used.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    def SetRect(self, rect: 'Rect') -> None:
        """ 

`SetRect`(*self*, *rect*)[¶](#wx.adv.CalculateLayoutEvent.SetRect "Permalink to this definition")
Call this to specify the new remaining parent client area, after the space occupied by the window has been subtracted.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.adv.CalculateLayoutEvent.html
        """

    Flags: int  # `Flags`[¶](#wx.adv.CalculateLayoutEvent.Flags "Permalink to this definition")See [`GetFlags`](#wx.adv.CalculateLayoutEvent.GetFlags "wx.adv.CalculateLayoutEvent.GetFlags") and [`SetFlags`](#wx.adv.CalculateLayoutEvent.SetFlags "wx.adv.CalculateLayoutEvent.SetFlags")
    Rect: '_Rect'  # `Rect`[¶](#wx.adv.CalculateLayoutEvent.Rect "Permalink to this definition")See [`GetRect`](#wx.adv.CalculateLayoutEvent.GetRect "wx.adv.CalculateLayoutEvent.GetRect") and [`SetRect`](#wx.adv.CalculateLayoutEvent.SetRect "wx.adv.CalculateLayoutEvent.SetRect")



EVT_CALCULATE_LAYOUT: int  # Process a  wxEVT_CALCULATE_LAYOUT   event, which asks the window to take a ‘bite’ out of a rectangle provided by the algorithm. ^^

class QueryLayoutInfoEvent(Event):
    """ **Possible constructors**:



```
QueryLayoutInfoEvent(id=0)

```


This event is sent when LayoutAlgorithm wishes to get the size,
orientation and alignment of a window.


  


        Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
    """
    def __init__(self, id: int=0) -> None:
        """ 

`__init__`(*self*, *id=0*)[¶](#wx.adv.QueryLayoutInfoEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
**id** (*wx.WindowID*) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetAlignment(self) -> int:
        """ 

`GetAlignment`(*self*)[¶](#wx.adv.QueryLayoutInfoEvent.GetAlignment "Permalink to this definition")
Specifies the alignment of the window (which side of the remaining parent client area the window sticks to).


One of `wx.adv.LAYOUT_TOP`, `wx.adv.LAYOUT_LEFT`, `wx.adv.LAYOUT_RIGHT`, `wx.adv.LAYOUT_BOTTOM`.



Return type
 [wx.adv.LayoutAlignment](wx.adv.LayoutAlignment.enumeration.html#wx-adv-layoutalignment)






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.adv.QueryLayoutInfoEvent.GetFlags "Permalink to this definition")
Returns the flags associated with this event.


Not currently used.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetOrientation(self) -> 'LayoutOrientation':
        """ 

`GetOrientation`(*self*)[¶](#wx.adv.QueryLayoutInfoEvent.GetOrientation "Permalink to this definition")
Returns the orientation that the event handler specified to the event object.


May be one of `wx.adv.LAYOUT_HORIZONTAL`, `wx.adv.LAYOUT_VERTICAL`.



Return type
 [wx.adv.LayoutOrientation](wx.adv.LayoutOrientation.enumeration.html#wx-adv-layoutorientation)






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetRequestedLength(self) -> int:
        """ 

`GetRequestedLength`(*self*)[¶](#wx.adv.QueryLayoutInfoEvent.GetRequestedLength "Permalink to this definition")
Returns the requested length of the window in the direction of the window orientation.


This information is not yet used.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def GetSize(self) -> 'Size':
        """ 

`GetSize`(*self*)[¶](#wx.adv.QueryLayoutInfoEvent.GetSize "Permalink to this definition")
Returns the size that the event handler specified to the event object as being the requested size of the window.



Return type
[`Size`](#wx.adv.QueryLayoutInfoEvent.Size "wx.adv.QueryLayoutInfoEvent.Size")






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetAlignment(self, alignment: int) -> None:
        """ 

`SetAlignment`(*self*, *alignment*)[¶](#wx.adv.QueryLayoutInfoEvent.SetAlignment "Permalink to this definition")
Call this to specify the alignment of the window (which side of the remaining parent client area the window sticks to).


May be one of `wx.adv.LAYOUT_TOP`, `wx.adv.LAYOUT_LEFT`, `wx.adv.LAYOUT_RIGHT`, `wx.adv.LAYOUT_BOTTOM`.



Parameters
**alignment** ([*LayoutAlignment*](wx.adv.LayoutAlignment.enumeration.html "LayoutAlignment")) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.adv.QueryLayoutInfoEvent.SetFlags "Permalink to this definition")
Sets the flags associated with this event.


Not currently used.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetOrientation(self, orientation: LayoutOrientation) -> None:
        """ 

`SetOrientation`(*self*, *orientation*)[¶](#wx.adv.QueryLayoutInfoEvent.SetOrientation "Permalink to this definition")
Call this to specify the orientation of the window.


May be one of `wx.adv.LAYOUT_HORIZONTAL`, `wx.adv.LAYOUT_VERTICAL`.



Parameters
**orientation** ([*LayoutOrientation*](wx.adv.LayoutOrientation.enumeration.html "LayoutOrientation")) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetRequestedLength(self, length: int) -> None:
        """ 

`SetRequestedLength`(*self*, *length*)[¶](#wx.adv.QueryLayoutInfoEvent.SetRequestedLength "Permalink to this definition")
Sets the requested length of the window in the direction of the window orientation.


This information is not yet used.



Parameters
**length** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    def SetSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetSize`(*self*, *size*)[¶](#wx.adv.QueryLayoutInfoEvent.SetSize "Permalink to this definition")
Call this to let the calling code know what the size of the window is.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.adv.QueryLayoutInfoEvent.html
        """

    Alignment: int  # `Alignment`[¶](#wx.adv.QueryLayoutInfoEvent.Alignment "Permalink to this definition")See [`GetAlignment`](#wx.adv.QueryLayoutInfoEvent.GetAlignment "wx.adv.QueryLayoutInfoEvent.GetAlignment") and [`SetAlignment`](#wx.adv.QueryLayoutInfoEvent.SetAlignment "wx.adv.QueryLayoutInfoEvent.SetAlignment")
    Flags: int  # `Flags`[¶](#wx.adv.QueryLayoutInfoEvent.Flags "Permalink to this definition")See [`GetFlags`](#wx.adv.QueryLayoutInfoEvent.GetFlags "wx.adv.QueryLayoutInfoEvent.GetFlags") and [`SetFlags`](#wx.adv.QueryLayoutInfoEvent.SetFlags "wx.adv.QueryLayoutInfoEvent.SetFlags")
    Orientation: 'LayoutOrientation'  # `Orientation`[¶](#wx.adv.QueryLayoutInfoEvent.Orientation "Permalink to this definition")See [`GetOrientation`](#wx.adv.QueryLayoutInfoEvent.GetOrientation "wx.adv.QueryLayoutInfoEvent.GetOrientation") and [`SetOrientation`](#wx.adv.QueryLayoutInfoEvent.SetOrientation "wx.adv.QueryLayoutInfoEvent.SetOrientation")
    RequestedLength: int  # `RequestedLength`[¶](#wx.adv.QueryLayoutInfoEvent.RequestedLength "Permalink to this definition")See [`GetRequestedLength`](#wx.adv.QueryLayoutInfoEvent.GetRequestedLength "wx.adv.QueryLayoutInfoEvent.GetRequestedLength") and [`SetRequestedLength`](#wx.adv.QueryLayoutInfoEvent.SetRequestedLength "wx.adv.QueryLayoutInfoEvent.SetRequestedLength")
    Size: '_Size'  # `Size`[¶](#wx.adv.QueryLayoutInfoEvent.Size "Permalink to this definition")See [`GetSize`](#wx.adv.QueryLayoutInfoEvent.GetSize "wx.adv.QueryLayoutInfoEvent.GetSize") and [`SetSize`](#wx.adv.QueryLayoutInfoEvent.SetSize "wx.adv.QueryLayoutInfoEvent.SetSize")



EVT_QUERY_LAYOUT_INFO: int  # Process a  wxEVT_QUERY_LAYOUT_INFO   event, to get size, orientation and alignment from a window. ^^

LAYOUT_TOP: int

LAYOUT_LEFT: int

LAYOUT_RIGHT: int

LAYOUT_BOTTOM: int

LAYOUT_HORIZONTAL: int

LAYOUT_VERTICAL: int

class TaskBarIconEvent(Event):
    """ **Possible constructors**:



```
TaskBarIconEvent(evtType, tbIcon)

```


The event class used by TaskBarIcon.


  


        Source: https://docs.wxpython.org/wx.adv.TaskBarIconEvent.html
    """
    def __init__(self, evtType, tbIcon) -> None:
        """ 

`__init__`(*self*, *evtType*, *tbIcon*)[¶](#wx.adv.TaskBarIconEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **evtType** (*wx.EventType*) –
* **tbIcon** ([*wx.adv.TaskBarIcon*](wx.adv.TaskBarIcon.html#wx.adv.TaskBarIcon "wx.adv.TaskBarIcon")) –






            Source: https://docs.wxpython.org/wx.adv.TaskBarIconEvent.html
        """



class NotificationMessage(EvtHandler):
    """ **Possible constructors**:



```
NotificationMessage()

NotificationMessage(title, message="", parent=None,
                    flags=ICON_INFORMATION)

```


This class allows showing the user a message non intrusively.


  


        Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.NotificationMessage.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor, use [`SetParent`](#wx.adv.NotificationMessage.SetParent "wx.adv.NotificationMessage.SetParent") , [`SetTitle`](#wx.adv.NotificationMessage.SetTitle "wx.adv.NotificationMessage.SetTitle") and [`SetMessage`](#wx.adv.NotificationMessage.SetMessage "wx.adv.NotificationMessage.SetMessage") to initialize the object before showing it.




---

  



**\_\_init\_\_** *(self, title, message=””, parent=None, flags=ICON\_INFORMATION)*


Create a notification object with the given attributes.


See [`SetTitle`](#wx.adv.NotificationMessage.SetTitle "wx.adv.NotificationMessage.SetTitle") , [`SetMessage`](#wx.adv.NotificationMessage.SetMessage "wx.adv.NotificationMessage.SetMessage") , [`SetParent`](#wx.adv.NotificationMessage.SetParent "wx.adv.NotificationMessage.SetParent") and [`SetFlags`](#wx.adv.NotificationMessage.SetFlags "wx.adv.NotificationMessage.SetFlags") for the description of the corresponding parameters.



Parameters
* **title** (*string*) –
* **message** (*string*) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **flags** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def AddAction(self, actionid, label="") -> bool:
        """ 

`AddAction`(*self*, *actionid*, *label=""*)[¶](#wx.adv.NotificationMessage.AddAction "Permalink to this definition")
Add an action to the notification.


If supported by the implementation this are usually buttons in the notification selectable by the user.



Parameters
* **actionid** (*wx.WindowID*) –
* **label** (*string*) –



Return type
*bool*



Returns
`False` if the current implementation or OS version does not support actions in notifications.





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def Close(self) -> bool:
        """ 

`Close`(*self*)[¶](#wx.adv.NotificationMessage.Close "Permalink to this definition")
Hides the notification.


Returns `True` if it was hidden or `False` if it couldn’t be done (e.g. on some systems automatically hidden notifications can’t be hidden manually).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    @staticmethod
    def MSWUseToasts(shortcutPath="", appId="") -> bool:
        """ 

*static* `MSWUseToasts`(*shortcutPath=""*, *appId=""*)[¶](#wx.adv.NotificationMessage.MSWUseToasts "Permalink to this definition")
Enables toast notifications available since Windows 8 and suppresses the additional icon in the notification area on Windows 10.


Toast notifications **require** a shortcut to the application in the start menu. The start menu shortcut needs to contain an Application User Model `ID`. It is recommended that the applications setup creates the shortcut and the application specifies the setup created shortcut in `shortcutPath` . A call to this method will verify (and if necessary modify) the shortcut before enabling toast notifications.



Parameters
* **shortcutPath** (*string*) – Path to a shortcut file referencing the applications executable. If the string is empty the applications display name will be used. If not fully qualified, it will be used as a path relative to the users start menu directory. The file extension .lnk is optional.
* **appId** (*string*) – The applications [Application User Model ID](https://msdn.microsoft.com/en-us/library/windows/desktop/dd378459(vs.85).aspx). If empty it will be extracted from the shortcut. If the shortcut does not contain an id an id will be automatically created from the applications vendor and app name.



Return type
*bool*



Returns
`False` if toast notifications could not be enabled.





New in version 4.1/wxWidgets-3.1.0.




Availability


Only available for MSW.




See also


[`wx.AppConsole.SetAppName`](wx.AppConsole.html#wx.AppConsole.SetAppName "wx.AppConsole.SetAppName") , [`wx.AppConsole.SetVendorName`](wx.AppConsole.html#wx.AppConsole.SetVendorName "wx.AppConsole.SetVendorName")





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.adv.NotificationMessage.SetFlags "Permalink to this definition")
This parameter can be currently used to specify the icon to show in the notification.


Valid values are `ICON_INFORMATION` , `ICON_WARNING` and `ICON_ERROR` (notice that `ICON_QUESTION` is not allowed here). Some implementations of this class may not support the icons.



Parameters
**flags** (*int*) – 





See also


[`SetIcon`](#wx.adv.NotificationMessage.SetIcon "wx.adv.NotificationMessage.SetIcon")





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ 

`SetIcon`(*self*, *icon*)[¶](#wx.adv.NotificationMessage.SetIcon "Permalink to this definition")
Specify a custom icon to be displayed in the notification.


Some implementations of this class may not support custom icons.



Parameters
**icon** ([*wx.Icon*](wx.Icon.html#wx.Icon "wx.Icon")) – 





New in version 4.1/wxWidgets-3.1.0.




See also


[`SetFlags`](#wx.adv.NotificationMessage.SetFlags "wx.adv.NotificationMessage.SetFlags")





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetMessage(self, message: str) -> None:
        """ 

`SetMessage`(*self*, *message*)[¶](#wx.adv.NotificationMessage.SetMessage "Permalink to this definition")
Set the main text of the notification.


This should be a more detailed description than the title but still limited to reasonable length (not more than 256 characters).



Parameters
**message** (*string*) – 






            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetParent(self, parent: 'Window') -> None:
        """ 

`SetParent`(*self*, *parent*)[¶](#wx.adv.NotificationMessage.SetParent "Permalink to this definition")
Set the parent for this notification: the notification will be associated with the top level parent of this window or, if this method is not called, with the main application window by default.



Parameters
**parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def SetTitle(self, title: str) -> None:
        """ 

`SetTitle`(*self*, *title*)[¶](#wx.adv.NotificationMessage.SetTitle "Permalink to this definition")
Set the title, it must be a concise string (not more than 64 characters), use [`SetMessage`](#wx.adv.NotificationMessage.SetMessage "wx.adv.NotificationMessage.SetMessage") to give the user more details.



Parameters
**title** (*string*) – 






            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    def Show(self, timeout: int=Timeout_Auto) -> bool:
        """ 

`Show`(*self*, *timeout=Timeout\_Auto*)[¶](#wx.adv.NotificationMessage.Show "Permalink to this definition")
Show the notification to the user and hides it after *timeout* seconds are elapsed.


Special values `Timeout_Auto` and `Timeout_Never` can be used here, notice that you shouldn’t rely on *timeout* being exactly respected because the current platform may only support default timeout value and also because the user may be able to close the notification.



Parameters
**timeout** (*int*) – 



Return type
*bool*



Returns
`False` if an error occurred.





Note


When using native notifications in wxGTK, the timeout is ignored for the notifications with `ICON_WARNING` or `ICON_ERROR` flags, they always remain shown unless they’re explicitly hidden by the user, i.e. behave as if Timeout\_Auto were given.





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """

    @staticmethod
    def UseTaskBarIcon(icon: 'adv.TaskBarIcon') -> 'TaskBarIcon':
        """ 

*static* `UseTaskBarIcon`(*icon*)[¶](#wx.adv.NotificationMessage.UseTaskBarIcon "Permalink to this definition")
If the application already uses a  [wx.adv.TaskBarIcon](wx.adv.TaskBarIcon.html#wx-adv-taskbaricon), it should be connected to notifications by using this method.


This has no effect if toast notifications are used.



Parameters
**icon** ([*wx.adv.TaskBarIcon*](wx.adv.TaskBarIcon.html#wx.adv.TaskBarIcon "wx.adv.TaskBarIcon")) – 



Return type
 [wx.adv.TaskBarIcon](wx.adv.TaskBarIcon.html#wx-adv-taskbaricon)



Returns
the task bar icon which was used previously (may be `NULL` )





Availability


Only available for MSW.





            Source: https://docs.wxpython.org/wx.adv.NotificationMessage.html
        """



EVT_NOTIFICATION_MESSAGE_CLICK: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_CLICK   event, when a notification is clicked.

EVT_NOTIFICATION_MESSAGE_DISMISSED: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_DISMISSED   event, when a notification is dismissed by the user or times out.

EVT_NOTIFICATION_MESSAGE_ACTION: int  # Process a  wxEVT_NOTIFICATION_MESSAGE_ACTION   event, when the user selects on of the actions added by  AddAction  ^^

class TaskBarIcon(EvtHandler):
    """ **Possible constructors**:



```
TaskBarIcon(iconType=TBI_DEFAULT_TYPE)

```


This class represents a taskbar icon.


  


        Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
    """
    def __init__(self, iconType: TaskBarIconType=TBI_DEFAULT_TYPE) -> None:
        """ 

`__init__`(*self*, *iconType=TBI\_DEFAULT\_TYPE*)[¶](#wx.adv.TaskBarIcon.__init__ "Permalink to this definition")
Default constructor.


The iconType is only applicable on OSX/Cocoa.



Parameters
**iconType** ([*TaskBarIconType*](wx.adv.TaskBarIconType.enumeration.html "TaskBarIconType")) – 






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def CreatePopupMenu(self) -> 'Menu':
        """ 

`CreatePopupMenu`(*self*)[¶](#wx.adv.TaskBarIcon.CreatePopupMenu "Permalink to this definition")
Called by the library when the user requests popup menu if [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") is not overridden.


Override this function in order to provide popup menu associated with the icon if you don’t want to override [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") , i.e. if you prefer creating a new menu every time instead of reusing the same menu.


If [`CreatePopupMenu`](#wx.adv.TaskBarIcon.CreatePopupMenu "wx.adv.TaskBarIcon.CreatePopupMenu") returns `None` (this happens by default), no menu is shown, otherwise the menu is displayed and then deleted by the library as soon as the user dismisses it. If you don’t want the menu to be destroyed when it is dismissed, override [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") instead.



Return type
*Menu*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def Destroy(self) -> None:
        """ 

`Destroy`(*self*)[¶](#wx.adv.TaskBarIcon.Destroy "Permalink to this definition")
This method is similar to [`wx.Window.Destroy`](wx.Window.html#wx.Window.Destroy "wx.Window.Destroy") and can be used to schedule the task bar icon object for the delayed destruction: it will be deleted during the next event loop iteration, which allows the task bar icon to process any pending events for it before being destroyed.




            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def GetPopupMenu(self) -> 'Menu':
        """ 

`GetPopupMenu`(*self*)[¶](#wx.adv.TaskBarIcon.GetPopupMenu "Permalink to this definition")
Called by the library when the user requests popup menu.


On Windows and Unix platforms this happens when the user right-clicks the icon, so overriding this method is the simplest way to implement the standard behaviour of showing a menu when the taskbar icon is clicked.


If [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") returns `None` (this happens by default), [`CreatePopupMenu`](#wx.adv.TaskBarIcon.CreatePopupMenu "wx.adv.TaskBarIcon.CreatePopupMenu") is called next and its menu is used (if not `None`). Otherwise the menu returned by [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") is shown and, contrary to [`CreatePopupMenu`](#wx.adv.TaskBarIcon.CreatePopupMenu "wx.adv.TaskBarIcon.CreatePopupMenu") , not destroyed when the user dismisses it, allowing to reuse the same menu pointer multiple times.



Return type
*Menu*





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    @staticmethod
    def IsAvailable() -> bool:
        """ 

*static* `IsAvailable`()[¶](#wx.adv.TaskBarIcon.IsAvailable "Permalink to this definition")
Returns `True` if system tray is available in the desktop environment the app runs under.


On Windows and macOS, the tray is always available and this function simply returns `True`.


On Unix, X11 environment may or may not provide the tray, depending on user’s desktop environment. Most modern desktops support the tray via the System Tray Protocol by freedesktop.org (<http://freedesktop.org/wiki/Specifications/systemtray-spec>).



Return type
*bool*





New in version 2.9.0.




Note


Tray availability may change during application’s lifetime under X11 and so applications shouldn’t cache the result.




Note


 [wx.adv.TaskBarIcon](#wx-adv-taskbaricon) supports older GNOME 1.2 and KDE 1/2 methods of adding icons to tray, but they are unreliable and this method doesn’t detect them.





            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def IsIconInstalled(self) -> bool:
        """ 

`IsIconInstalled`(*self*)[¶](#wx.adv.TaskBarIcon.IsIconInstalled "Permalink to this definition")
Returns `True` if [`SetIcon`](#wx.adv.TaskBarIcon.SetIcon "wx.adv.TaskBarIcon.SetIcon") was called with no subsequent [`RemoveIcon`](#wx.adv.TaskBarIcon.RemoveIcon "wx.adv.TaskBarIcon.RemoveIcon") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.adv.TaskBarIcon.IsOk "Permalink to this definition")
Returns `True` if the object initialized successfully.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ 

`PopupMenu`(*self*, *menu*)[¶](#wx.adv.TaskBarIcon.PopupMenu "Permalink to this definition")
Pops up a menu at the current mouse position.


The events can be handled by a class derived from  [wx.adv.TaskBarIcon](#wx-adv-taskbaricon).



Parameters
**menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) – 



Return type
*bool*





Note


It is recommended to override the [`CreatePopupMenu`](#wx.adv.TaskBarIcon.CreatePopupMenu "wx.adv.TaskBarIcon.CreatePopupMenu") or [`GetPopupMenu`](#wx.adv.TaskBarIcon.GetPopupMenu "wx.adv.TaskBarIcon.GetPopupMenu") callback instead of calling this method from event handler, because some ports (e.g. Cocoa) may not implement [`PopupMenu`](#wx.adv.TaskBarIcon.PopupMenu "wx.adv.TaskBarIcon.PopupMenu") and mouse click events at all.





            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def RemoveIcon(self) -> bool:
        """ 

`RemoveIcon`(*self*)[¶](#wx.adv.TaskBarIcon.RemoveIcon "Permalink to this definition")
Removes the icon previously set with [`SetIcon`](#wx.adv.TaskBarIcon.SetIcon "wx.adv.TaskBarIcon.SetIcon") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def SetIcon(self, icon, tooltip="") -> bool:
        """ 

`SetIcon`(*self*, *icon*, *tooltip=""*)[¶](#wx.adv.TaskBarIcon.SetIcon "Permalink to this definition")
Sets the icon, and optional tooltip text.



Parameters
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **tooltip** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """

    def ShowBalloon(self, title, text, msec=0, flags=0) -> bool:
        """ 

`ShowBalloon`(*self*, *title*, *text*, *msec=0*, *flags=0*)[¶](#wx.adv.TaskBarIcon.ShowBalloon "Permalink to this definition")

> Show a balloon notification (the icon must have been already
> initialized using SetIcon). Only implemented for Windows.
> 
> 
> The `title` and `text` parameters are limited to 63 and 255
> characters respectively, `msec` is the timeout, in milliseconds,
> before the balloon disappears (will be clamped down to the allowed
> 10-30s range by Windows if it’s outside it) and `flags` can
> include ICON\_ERROR/INFO/WARNING to show a corresponding icon.
> 
> 
> Returns `True` if balloon was shown, `False` on error (incorrect
> parameters or function unsupported by OS).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.TaskBarIcon.html
        """



EVT_TASKBAR_MOVE: int  # Process a  wxEVT_TASKBAR_MOVE   event.

EVT_TASKBAR_LEFT_DOWN: int  # Process a  wxEVT_TASKBAR_LEFT_DOWN   event.

EVT_TASKBAR_LEFT_UP: int  # Process a  wxEVT_TASKBAR_LEFT_UP   event.

EVT_TASKBAR_RIGHT_DOWN: int  # Process a  wxEVT_TASKBAR_RIGHT_DOWN   event.

EVT_TASKBAR_RIGHT_UP: int  # Process a  wxEVT_TASKBAR_RIGHT_UP   event.

EVT_TASKBAR_LEFT_DCLICK: int  # Process a  wxEVT_TASKBAR_LEFT_DCLICK   event.

EVT_TASKBAR_RIGHT_DCLICK: int  # Process a  wxEVT_TASKBAR_RIGHT_DCLICK   event.

EVT_TASKBAR_CLICK: int  # This is a synonym for either EVT_TASKBAR_RIGHT_DOWN or wx.UP depending on the platform, use this event macro to catch the event which should result in the menu being displayed on the current platform. ^^

UP: int

class SplashScreen(Frame):
    """ **Possible constructors**:



```
SplashScreen(bitmap, splashStyle, milliseconds, parent, id=ID_ANY,
             pos=DefaultPosition, size=DefaultSize,
             style=BORDER_SIMPLE|FRAME_NO_TASKBAR|STAY_ON_TOP)

```


SplashScreen shows a window with a thin border, displaying a bitmap
describing your application.


  


        Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
    """
    def __init__(self, bitmap, splashStyle, milliseconds, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=BORDER_SIMPLE|FRAME_NO_TASKBAR|STAY_ON_TOP) -> None:
        """ 

`__init__`(*self*, *bitmap*, *splashStyle*, *milliseconds*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=BORDER\_SIMPLE|FRAME\_NO\_TASKBAR|STAY\_ON\_TOP*)[¶](#wx.adv.SplashScreen.__init__ "Permalink to this definition")
Construct the splash screen passing a bitmap, a style, a timeout, a window id, optional position and size, and a window style.


*splashStyle* is a bitlist of some of the following:


* `wx.adv.SPLASH_CENTRE_ON_PARENT`
* `wx.adv.SPLASH_CENTRE_ON_SCREEN`
* `wx.adv.SPLASH_NO_CENTRE`
* `wx.adv.SPLASH_TIMEOUT`
* `wx.adv.SPLASH_NO_TIMEOUT`


*milliseconds* is the timeout in milliseconds.



Parameters
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **splashStyle** (*long*) –
* **milliseconds** (*int*) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.adv.SplashScreen.GetBitmap "Permalink to this definition")
Get the spash screen’s bitmap



Return type
[`Bitmap`](#wx.adv.SplashScreen.Bitmap "wx.adv.SplashScreen.Bitmap")






            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.SplashScreen.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetSplashStyle(self) -> int:
        """ 

`GetSplashStyle`(*self*)[¶](#wx.adv.SplashScreen.GetSplashStyle "Permalink to this definition")
Returns the splash style (see  [wx.adv.SplashScreen](#wx-adv-splashscreen) for details).



Return type
*long*






            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def GetTimeout(self) -> int:
        """ 

`GetTimeout`(*self*)[¶](#wx.adv.SplashScreen.GetTimeout "Permalink to this definition")
Returns the timeout in milliseconds.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    def SetBitmap(self, bitmap) -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.adv.SplashScreen.SetBitmap "Permalink to this definition")
Set a new bitmap for the splash screen.




            Source: https://docs.wxpython.org/wx.adv.SplashScreen.html
        """

    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.adv.SplashScreen.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.adv.SplashScreen.GetBitmap "wx.adv.SplashScreen.GetBitmap") and [`SetBitmap`](#wx.adv.SplashScreen.SetBitmap "wx.adv.SplashScreen.SetBitmap")
    SplashStyle: int  # `SplashStyle`[¶](#wx.adv.SplashScreen.SplashStyle "Permalink to this definition")See [`GetSplashStyle`](#wx.adv.SplashScreen.GetSplashStyle "wx.adv.SplashScreen.GetSplashStyle")
    Timeout: int  # `Timeout`[¶](#wx.adv.SplashScreen.Timeout "Permalink to this definition")See [`GetTimeout`](#wx.adv.SplashScreen.GetTimeout "wx.adv.SplashScreen.GetTimeout")



SPLASH_CENTRE_ON_PARENT: int

SPLASH_CENTRE_ON_SCREEN: int

SPLASH_NO_CENTRE: int

SPLASH_TIMEOUT: int

SPLASH_NO_TIMEOUT: int

class ExtHelpController(HelpControllerBase):
    """ **Possible constructors**:



```
ExtHelpController(parentWindow=None)

```


This class implements help via an external browser.


  


        Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
    """
    def __init__(self, parentWindow: Optional['Window']=None) -> None:
        """ 

`__init__`(*self*, *parentWindow=None*)[¶](#wx.adv.ExtHelpController.__init__ "Permalink to this definition")

Parameters
**parentWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayBlock(self, blockNo: int) -> bool:
        """ 

`DisplayBlock`(*self*, *blockNo*)[¶](#wx.adv.ExtHelpController.DisplayBlock "Permalink to this definition")
Display help for URL (using DisplayHelp) or keyword (using KeywordSearch)



Parameters
**blockNo** (*long*) – 



Return type
*bool*



Returns
`True` on success






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayContents(self) -> bool:
        """ 

`DisplayContents`(*self*)[¶](#wx.adv.ExtHelpController.DisplayContents "Permalink to this definition")
Display list of all help entries.



Return type
*bool*



Returns
`True` on success






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplayHelp(self, relativeURL: str) -> bool:
        """ 

`DisplayHelp`(*self*, *relativeURL*)[¶](#wx.adv.ExtHelpController.DisplayHelp "Permalink to this definition")
Call the browser using a relative URL.



Parameters
**relativeURL** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def DisplaySection(self, *args, **kw) -> bool:
        """ 

`DisplaySection`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.ExtHelpController.DisplaySection "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**DisplaySection** *(self, sectionNo)*


Display help for id sectionNo.



Parameters
**sectionNo** (*int*) – 



Return type
*bool*



Returns
`True` on success






---

  



**DisplaySection** *(self, section)*


Display help for id sectionNo – identical with [`DisplaySection`](#wx.adv.ExtHelpController.DisplaySection "wx.adv.ExtHelpController.DisplaySection") .



Parameters
**section** (*string*) – 



Return type
*bool*



Returns
`True` on success






---

  





            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def GetFrameParameters(self, size=None, pos=None, newFrameEachTime=None) -> 'Frame':
        """ 

`GetFrameParameters`(*self*, *size=None*, *pos=None*, *newFrameEachTime=None*)[¶](#wx.adv.ExtHelpController.GetFrameParameters "Permalink to this definition")
Obtains the latest settings used by the help frame and the help frame.



Parameters
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **newFrameEachTime** (*bool*) –



Return type
*Frame*






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def Initialize(self, dir: str) -> bool:
        """ 

`Initialize`(*self*, *dir*)[¶](#wx.adv.ExtHelpController.Initialize "Permalink to this definition")
This must be called to tell the controller where to find the documentation.


If a locale is set, look in file/localename, i.e. If passed “/usr/local/myapp/help” and the current  [wx.Locale](wx.Locale.html#wx-locale) is set to be “de”, then look in “/usr/local/myapp/help/de/” first and fall back to “/usr/local/myapp/help” if that doesn’t exist.



Parameters
**dir** (*string*) – directory name where to fine the help files



Return type
*bool*



Returns
`True` on success






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def KeywordSearch(self, k, mode=HELP_SEARCH_ALL) -> bool:
        """ 

`KeywordSearch`(*self*, *k*, *mode=HELP\_SEARCH\_ALL*)[¶](#wx.adv.ExtHelpController.KeywordSearch "Permalink to this definition")
Search comment/documentation fields in map file and present a list to chose from.



Parameters
* **k** (*string*) – string to search for, empty string will list all entries
* **mode** ([*HelpSearchMode*](wx.HelpSearchMode.enumeration.html "HelpSearchMode")) – optional parameter allows the search the index (wx``wx.HELP\_SEARCH\_INDEX``) but this currently only supported by the  [wx.html.HtmlHelpController](wx.html.HtmlHelpController.html#wx-html-htmlhelpcontroller).



Return type
*bool*



Returns
`True` on success






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def LoadFile(self, file: str="") -> bool:
        """ 

`LoadFile`(*self*, *file=""*)[¶](#wx.adv.ExtHelpController.LoadFile "Permalink to this definition")
If file is “”, reloads file given in Initialize.



Parameters
**file** (*string*) – Name of help directory.



Return type
*bool*



Returns
`True` on success






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def OnQuit(self) -> None:
        """ 

`OnQuit`(*self*)[¶](#wx.adv.ExtHelpController.OnQuit "Permalink to this definition")
Does nothing.




            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def Quit(self) -> bool:
        """ 

`Quit`(*self*)[¶](#wx.adv.ExtHelpController.Quit "Permalink to this definition")
Does nothing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def SetFrameParameters(self, titleFormat, size, pos=DefaultPosition, newFrameEachTime=False) -> None:
        """ 

`SetFrameParameters`(*self*, *titleFormat*, *size*, *pos=DefaultPosition*, *newFrameEachTime=False*)[¶](#wx.adv.ExtHelpController.SetFrameParameters "Permalink to this definition")
Allows one to override the default settings for the help frame.



Parameters
* **titleFormat** (*string*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **newFrameEachTime** (*bool*) –






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    def SetViewer(self, viewer="", flags=HELP_NETSCAPE) -> None:
        """ 

`SetViewer`(*self*, *viewer=""*, *flags=HELP\_NETSCAPE*)[¶](#wx.adv.ExtHelpController.SetViewer "Permalink to this definition")
Tell it which browser to use.


The Netscape support will check whether Netscape is already running (by looking at the .netscape/lock file in the user’s home directory) and tell it to load the page into the existing window.



Parameters
* **viewer** (*string*) – The command to call a browser/html viewer.
* **flags** (*long*) – Set this to `wx.HELP_NETSCAPE` if the browser is some variant of Netscape.






            Source: https://docs.wxpython.org/wx.adv.ExtHelpController.html
        """

    FrameParameters: 'Frame'  # `FrameParameters`[¶](#wx.adv.ExtHelpController.FrameParameters "Permalink to this definition")See [`GetFrameParameters`](#wx.adv.ExtHelpController.GetFrameParameters "wx.adv.ExtHelpController.GetFrameParameters")



HELP_NETSCAPE: int

class Joystick(Object):
    """ **Possible constructors**:



```
Joystick(joystick=JOYSTICK1)

```


Joystick allows an application to control one or more joysticks.


  


        Source: https://docs.wxpython.org/wx.adv.Joystick.html
    """
    def __init__(self, joystick: int=JOYSTICK1) -> None:
        """ 

`__init__`(*self*, *joystick=JOYSTICK1*)[¶](#wx.adv.Joystick.__init__ "Permalink to this definition")
Constructor.


*joystick* may be one of `wx.JOYSTICK1`, `wx.JOYSTICK2`, indicating the joystick controller of interest.



Parameters
**joystick** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetButtonState(self, *args, **kw) -> int:
        """ 

`GetButtonState`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.Joystick.GetButtonState "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetButtonState** *(self)*


Returns the state of the joystick buttons.


Every button is mapped to a single bit in the returned integer, with the first button being mapped to the least significant bit, and so on.


A bitlist of JOY\_BUTTONn identifiers, where n is 1, 2, 3 or 4 is available for historical reasons.



Return type
*int*






---

  



**GetButtonState** *(self, id)*


Returns the state of the specified joystick button.



Parameters
**id** (*int*) – The button id to report, from 0 to [`GetNumberButtons`](#wx.adv.Joystick.GetNumberButtons "wx.adv.Joystick.GetNumberButtons") - 1



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetManufacturerId(self) -> int:
        """ 

`GetManufacturerId`(*self*)[¶](#wx.adv.Joystick.GetManufacturerId "Permalink to this definition")
Returns the manufacturer id.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMaxAxes(self) -> int:
        """ 

`GetMaxAxes`(*self*)[¶](#wx.adv.Joystick.GetMaxAxes "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMaxButtons(self) -> int:
        """ 

`GetMaxButtons`(*self*)[¶](#wx.adv.Joystick.GetMaxButtons "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetMovementThreshold(self) -> int:
        """ 

`GetMovementThreshold`(*self*)[¶](#wx.adv.Joystick.GetMovementThreshold "Permalink to this definition")
Returns the movement threshold, the number of steps outside which the joystick is deemed to have moved.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetNumberAxes(self) -> int:
        """ 

`GetNumberAxes`(*self*)[¶](#wx.adv.Joystick.GetNumberAxes "Permalink to this definition")
Returns the number of axes for this joystick.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetNumberButtons(self) -> int:
        """ 

`GetNumberButtons`(*self*)[¶](#wx.adv.Joystick.GetNumberButtons "Permalink to this definition")
Returns the number of buttons for this joystick.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    @staticmethod
    def GetNumberJoysticks() -> int:
        """ 

*static* `GetNumberJoysticks`()[¶](#wx.adv.Joystick.GetNumberJoysticks "Permalink to this definition")
Returns the number of joysticks currently attached to the computer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPOVCTSPosition(self) -> int:
        """ 

`GetPOVCTSPosition`(*self*)[¶](#wx.adv.Joystick.GetPOVCTSPosition "Permalink to this definition")
Returns the point-of-view position, expressed in continuous, one-hundredth of a degree units.


Returns -1 on error.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPOVPosition(self) -> int:
        """ 

`GetPOVPosition`(*self*)[¶](#wx.adv.Joystick.GetPOVPosition "Permalink to this definition")
Returns the point-of-view position, expressed in continuous, one-hundredth of a degree units, but limited to return 0, 9000, 18000 or 27000.


Returns -1 on error.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPollingMax(self) -> int:
        """ 

`GetPollingMax`(*self*)[¶](#wx.adv.Joystick.GetPollingMax "Permalink to this definition")
Returns the maximum polling frequency.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPollingMin(self) -> int:
        """ 

`GetPollingMin`(*self*)[¶](#wx.adv.Joystick.GetPollingMin "Permalink to this definition")
Returns the minimum polling frequency.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetPosition(self, *args, **kw) -> 'Point':
        """ 

`GetPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.Joystick.GetPosition "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetPosition** *(self)*


Returns the x, y position of the joystick.



Return type
*Point*






---

  



**GetPosition** *(self, axis)*


Returns the position of the specified joystick axis.



Parameters
**axis** (*int*) – The joystick axis to report, from 0 to [`GetNumberAxes`](#wx.adv.Joystick.GetNumberAxes "wx.adv.Joystick.GetNumberAxes") - 1.



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetProductId(self) -> int:
        """ 

`GetProductId`(*self*)[¶](#wx.adv.Joystick.GetProductId "Permalink to this definition")
Returns the product id for the joystick.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetProductName(self) -> str:
        """ 

`GetProductName`(*self*)[¶](#wx.adv.Joystick.GetProductName "Permalink to this definition")
Returns the product name for the joystick.



Return type
`string`






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderMax(self) -> int:
        """ 

`GetRudderMax`(*self*)[¶](#wx.adv.Joystick.GetRudderMax "Permalink to this definition")
Returns the maximum rudder position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderMin(self) -> int:
        """ 

`GetRudderMin`(*self*)[¶](#wx.adv.Joystick.GetRudderMin "Permalink to this definition")
Returns the minimum rudder position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetRudderPosition(self) -> int:
        """ 

`GetRudderPosition`(*self*)[¶](#wx.adv.Joystick.GetRudderPosition "Permalink to this definition")
Returns the rudder position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUMax(self) -> int:
        """ 

`GetUMax`(*self*)[¶](#wx.adv.Joystick.GetUMax "Permalink to this definition")
Returns the maximum U position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUMin(self) -> int:
        """ 

`GetUMin`(*self*)[¶](#wx.adv.Joystick.GetUMin "Permalink to this definition")
Returns the minimum U position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetUPosition(self) -> int:
        """ 

`GetUPosition`(*self*)[¶](#wx.adv.Joystick.GetUPosition "Permalink to this definition")
Gets the position of the fifth axis of the joystick, if it exists.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVMax(self) -> int:
        """ 

`GetVMax`(*self*)[¶](#wx.adv.Joystick.GetVMax "Permalink to this definition")
Returns the maximum V position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVMin(self) -> int:
        """ 

`GetVMin`(*self*)[¶](#wx.adv.Joystick.GetVMin "Permalink to this definition")
Returns the minimum V position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetVPosition(self) -> int:
        """ 

`GetVPosition`(*self*)[¶](#wx.adv.Joystick.GetVPosition "Permalink to this definition")
Gets the position of the sixth axis of the joystick, if it exists.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetXMax(self) -> int:
        """ 

`GetXMax`(*self*)[¶](#wx.adv.Joystick.GetXMax "Permalink to this definition")
Returns the maximum x position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetXMin(self) -> int:
        """ 

`GetXMin`(*self*)[¶](#wx.adv.Joystick.GetXMin "Permalink to this definition")
Returns the minimum x position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetYMax(self) -> int:
        """ 

`GetYMax`(*self*)[¶](#wx.adv.Joystick.GetYMax "Permalink to this definition")
Returns the maximum y position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetYMin(self) -> int:
        """ 

`GetYMin`(*self*)[¶](#wx.adv.Joystick.GetYMin "Permalink to this definition")
Returns the minimum y position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZMax(self) -> int:
        """ 

`GetZMax`(*self*)[¶](#wx.adv.Joystick.GetZMax "Permalink to this definition")
Returns the maximum z position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZMin(self) -> int:
        """ 

`GetZMin`(*self*)[¶](#wx.adv.Joystick.GetZMin "Permalink to this definition")
Returns the minimum z position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def GetZPosition(self) -> int:
        """ 

`GetZPosition`(*self*)[¶](#wx.adv.Joystick.GetZPosition "Permalink to this definition")
Returns the z position of the joystick.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOV(self) -> bool:
        """ 

`HasPOV`(*self*)[¶](#wx.adv.Joystick.HasPOV "Permalink to this definition")
Returns `True` if the joystick has a point of view control.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOV4Dir(self) -> bool:
        """ 

`HasPOV4Dir`(*self*)[¶](#wx.adv.Joystick.HasPOV4Dir "Permalink to this definition")
Returns `True` if the joystick point-of-view supports discrete values (centered, forward, backward, left, and right).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasPOVCTS(self) -> bool:
        """ 

`HasPOVCTS`(*self*)[¶](#wx.adv.Joystick.HasPOVCTS "Permalink to this definition")
Returns `True` if the joystick point-of-view supports continuous degree bearings.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasRudder(self) -> bool:
        """ 

`HasRudder`(*self*)[¶](#wx.adv.Joystick.HasRudder "Permalink to this definition")
Returns `True` if there is a rudder attached to the computer.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasU(self) -> bool:
        """ 

`HasU`(*self*)[¶](#wx.adv.Joystick.HasU "Permalink to this definition")
Returns `True` if the joystick has a U axis.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasV(self) -> bool:
        """ 

`HasV`(*self*)[¶](#wx.adv.Joystick.HasV "Permalink to this definition")
Returns `True` if the joystick has a V axis.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def HasZ(self) -> bool:
        """ 

`HasZ`(*self*)[¶](#wx.adv.Joystick.HasZ "Permalink to this definition")
Returns `True` if the joystick has a Z axis.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.adv.Joystick.IsOk "Permalink to this definition")
Returns `True` if the joystick is functioning.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def ReleaseCapture(self) -> bool:
        """ 

`ReleaseCapture`(*self*)[¶](#wx.adv.Joystick.ReleaseCapture "Permalink to this definition")
Releases the capture set by **SetCapture**.



Return type
*bool*



Returns
`True` if the capture release succeeded.





See also


[`SetCapture`](#wx.adv.Joystick.SetCapture "wx.adv.Joystick.SetCapture") ,  [wx.JoystickEvent](wx.JoystickEvent.html#wx-joystickevent)





            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def SetCapture(self, win, pollingFreq=0) -> bool:
        """ 

`SetCapture`(*self*, *win*, *pollingFreq=0*)[¶](#wx.adv.Joystick.SetCapture "Permalink to this definition")
Sets the capture to direct joystick events to *win*.



Parameters
* **win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window that will receive joystick events.
* **pollingFreq** (*int*) – If zero, movement events are sent when above the threshold. If greater than zero, events are received every *pollingFreq* milliseconds.



Return type
*bool*



Returns
`True` if the capture succeeded.





See also


[`ReleaseCapture`](#wx.adv.Joystick.ReleaseCapture "wx.adv.Joystick.ReleaseCapture") ,  [wx.JoystickEvent](wx.JoystickEvent.html#wx-joystickevent)





            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    def SetMovementThreshold(self, threshold: int) -> None:
        """ 

`SetMovementThreshold`(*self*, *threshold*)[¶](#wx.adv.Joystick.SetMovementThreshold "Permalink to this definition")
Sets the movement threshold, the number of steps outside which the joystick is deemed to have moved.



Parameters
**threshold** (*int*) – 






            Source: https://docs.wxpython.org/wx.adv.Joystick.html
        """

    ButtonState: int  # `ButtonState`[¶](#wx.adv.Joystick.ButtonState "Permalink to this definition")See [`GetButtonState`](#wx.adv.Joystick.GetButtonState "wx.adv.Joystick.GetButtonState")
    ManufacturerId: int  # `ManufacturerId`[¶](#wx.adv.Joystick.ManufacturerId "Permalink to this definition")See [`GetManufacturerId`](#wx.adv.Joystick.GetManufacturerId "wx.adv.Joystick.GetManufacturerId")
    MaxAxes: int  # `MaxAxes`[¶](#wx.adv.Joystick.MaxAxes "Permalink to this definition")See [`GetMaxAxes`](#wx.adv.Joystick.GetMaxAxes "wx.adv.Joystick.GetMaxAxes")
    MaxButtons: int  # `MaxButtons`[¶](#wx.adv.Joystick.MaxButtons "Permalink to this definition")See [`GetMaxButtons`](#wx.adv.Joystick.GetMaxButtons "wx.adv.Joystick.GetMaxButtons")
    MovementThreshold: int  # `MovementThreshold`[¶](#wx.adv.Joystick.MovementThreshold "Permalink to this definition")See [`GetMovementThreshold`](#wx.adv.Joystick.GetMovementThreshold "wx.adv.Joystick.GetMovementThreshold") and [`SetMovementThreshold`](#wx.adv.Joystick.SetMovementThreshold "wx.adv.Joystick.SetMovementThreshold")
    NumberAxes: int  # `NumberAxes`[¶](#wx.adv.Joystick.NumberAxes "Permalink to this definition")See [`GetNumberAxes`](#wx.adv.Joystick.GetNumberAxes "wx.adv.Joystick.GetNumberAxes")
    NumberButtons: int  # `NumberButtons`[¶](#wx.adv.Joystick.NumberButtons "Permalink to this definition")See [`GetNumberButtons`](#wx.adv.Joystick.GetNumberButtons "wx.adv.Joystick.GetNumberButtons")
    POVCTSPosition: int  # `POVCTSPosition`[¶](#wx.adv.Joystick.POVCTSPosition "Permalink to this definition")See [`GetPOVCTSPosition`](#wx.adv.Joystick.GetPOVCTSPosition "wx.adv.Joystick.GetPOVCTSPosition")
    POVPosition: int  # `POVPosition`[¶](#wx.adv.Joystick.POVPosition "Permalink to this definition")See [`GetPOVPosition`](#wx.adv.Joystick.GetPOVPosition "wx.adv.Joystick.GetPOVPosition")
    PollingMax: int  # `PollingMax`[¶](#wx.adv.Joystick.PollingMax "Permalink to this definition")See [`GetPollingMax`](#wx.adv.Joystick.GetPollingMax "wx.adv.Joystick.GetPollingMax")
    PollingMin: int  # `PollingMin`[¶](#wx.adv.Joystick.PollingMin "Permalink to this definition")See [`GetPollingMin`](#wx.adv.Joystick.GetPollingMin "wx.adv.Joystick.GetPollingMin")
    Position: 'Point'  # `Position`[¶](#wx.adv.Joystick.Position "Permalink to this definition")See [`GetPosition`](#wx.adv.Joystick.GetPosition "wx.adv.Joystick.GetPosition")
    ProductId: int  # `ProductId`[¶](#wx.adv.Joystick.ProductId "Permalink to this definition")See [`GetProductId`](#wx.adv.Joystick.GetProductId "wx.adv.Joystick.GetProductId")
    ProductName: str  # `ProductName`[¶](#wx.adv.Joystick.ProductName "Permalink to this definition")See [`GetProductName`](#wx.adv.Joystick.GetProductName "wx.adv.Joystick.GetProductName")
    RudderMax: int  # `RudderMax`[¶](#wx.adv.Joystick.RudderMax "Permalink to this definition")See [`GetRudderMax`](#wx.adv.Joystick.GetRudderMax "wx.adv.Joystick.GetRudderMax")
    RudderMin: int  # `RudderMin`[¶](#wx.adv.Joystick.RudderMin "Permalink to this definition")See [`GetRudderMin`](#wx.adv.Joystick.GetRudderMin "wx.adv.Joystick.GetRudderMin")
    RudderPosition: int  # `RudderPosition`[¶](#wx.adv.Joystick.RudderPosition "Permalink to this definition")See [`GetRudderPosition`](#wx.adv.Joystick.GetRudderPosition "wx.adv.Joystick.GetRudderPosition")
    UMax: int  # `UMax`[¶](#wx.adv.Joystick.UMax "Permalink to this definition")See [`GetUMax`](#wx.adv.Joystick.GetUMax "wx.adv.Joystick.GetUMax")
    UMin: int  # `UMin`[¶](#wx.adv.Joystick.UMin "Permalink to this definition")See [`GetUMin`](#wx.adv.Joystick.GetUMin "wx.adv.Joystick.GetUMin")
    UPosition: int  # `UPosition`[¶](#wx.adv.Joystick.UPosition "Permalink to this definition")See [`GetUPosition`](#wx.adv.Joystick.GetUPosition "wx.adv.Joystick.GetUPosition")
    VMax: int  # `VMax`[¶](#wx.adv.Joystick.VMax "Permalink to this definition")See [`GetVMax`](#wx.adv.Joystick.GetVMax "wx.adv.Joystick.GetVMax")
    VMin: int  # `VMin`[¶](#wx.adv.Joystick.VMin "Permalink to this definition")See [`GetVMin`](#wx.adv.Joystick.GetVMin "wx.adv.Joystick.GetVMin")
    VPosition: int  # `VPosition`[¶](#wx.adv.Joystick.VPosition "Permalink to this definition")See [`GetVPosition`](#wx.adv.Joystick.GetVPosition "wx.adv.Joystick.GetVPosition")
    XMax: int  # `XMax`[¶](#wx.adv.Joystick.XMax "Permalink to this definition")See [`GetXMax`](#wx.adv.Joystick.GetXMax "wx.adv.Joystick.GetXMax")
    XMin: int  # `XMin`[¶](#wx.adv.Joystick.XMin "Permalink to this definition")See [`GetXMin`](#wx.adv.Joystick.GetXMin "wx.adv.Joystick.GetXMin")
    YMax: int  # `YMax`[¶](#wx.adv.Joystick.YMax "Permalink to this definition")See [`GetYMax`](#wx.adv.Joystick.GetYMax "wx.adv.Joystick.GetYMax")
    YMin: int  # `YMin`[¶](#wx.adv.Joystick.YMin "Permalink to this definition")See [`GetYMin`](#wx.adv.Joystick.GetYMin "wx.adv.Joystick.GetYMin")
    ZMax: int  # `ZMax`[¶](#wx.adv.Joystick.ZMax "Permalink to this definition")See [`GetZMax`](#wx.adv.Joystick.GetZMax "wx.adv.Joystick.GetZMax")
    ZMin: int  # `ZMin`[¶](#wx.adv.Joystick.ZMin "Permalink to this definition")See [`GetZMin`](#wx.adv.Joystick.GetZMin "wx.adv.Joystick.GetZMin")
    ZPosition: int  # `ZPosition`[¶](#wx.adv.Joystick.ZPosition "Permalink to this definition")See [`GetZPosition`](#wx.adv.Joystick.GetZPosition "wx.adv.Joystick.GetZPosition")



JOYSTICK1: int

JOYSTICK2: int

class WizardEvent(NotifyEvent):
    """ **Possible constructors**:



```
WizardEvent(type=wxEVT_NULL, id=ID_ANY, direction=True, page=0)

```


WizardEvent class represents an event generated by the Wizard:
this event is first sent to the page itself and, if not processed
there, goes up the window hierarchy as usual.


  


        Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
    """
    def __init__(self, type=wxEVT_NULL, id=ID_ANY, direction=True, page=0) -> None:
        """ 

`__init__`(*self*, *type=wxEVT\_NULL*, *id=ID\_ANY*, *direction=True*, *page=0*)[¶](#wx.adv.WizardEvent.__init__ "Permalink to this definition")
Constructor.


It is not normally used by the user code as the objects of this type are constructed by  [wx.adv.Wizard](wx.adv.Wizard.html#wx-adv-wizard).



Parameters
* **type** (*wx.EventType*) –
* **id** (*int*) –
* **direction** (*bool*) –
* **page** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –






            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    def GetDirection(self) -> bool:
        """ 

`GetDirection`(*self*)[¶](#wx.adv.WizardEvent.GetDirection "Permalink to this definition")
Return the direction in which the page is changing: for `EVT_WIZARD_PAGE_CHANGING` , return `True` if we’re going forward or `False` otherwise and for `EVT_WIZARD_PAGE_CHANGED` return `True` if we came from the previous page and `False` if we returned from the next one.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    def GetPage(self) -> 'WizardPage':
        """ 

`GetPage`(*self*)[¶](#wx.adv.WizardEvent.GetPage "Permalink to this definition")
Returns the  [wx.adv.WizardPage](wx.adv.WizardPage.html#wx-adv-wizardpage) which was active when this event was generated.



Return type
 [wx.adv.WizardPage](wx.adv.WizardPage.html#wx-adv-wizardpage)






            Source: https://docs.wxpython.org/wx.adv.WizardEvent.html
        """

    Direction: bool  # `Direction`[¶](#wx.adv.WizardEvent.Direction "Permalink to this definition")See [`GetDirection`](#wx.adv.WizardEvent.GetDirection "wx.adv.WizardEvent.GetDirection")
    Page: 'WizardPage'  # `Page`[¶](#wx.adv.WizardEvent.Page "Permalink to this definition")See [`GetPage`](#wx.adv.WizardEvent.GetPage "wx.adv.WizardEvent.GetPage")



class Animation(Object):
    """ **Possible constructors**:



```
Animation()

Animation(name, type=ANIMATION_TYPE_ANY)

Animation(other)

```


The Animation class handles the interface between the animation
control and the details of the animation image or data.


  


        Source: https://docs.wxpython.org/wx.adv.Animation.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.Animation.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Constructs a new empty animation object.


Call [`Load`](#wx.adv.Animation.Load "wx.adv.Animation.Load") to initialize it.



See also


[`wx.adv.AnimationCtrl.CreateAnimation`](wx.adv.AnimationCtrl.html#wx.adv.AnimationCtrl.CreateAnimation "wx.adv.AnimationCtrl.CreateAnimation")





---

  



**\_\_init\_\_** *(self, name, type=ANIMATION\_TYPE\_ANY)*


Constructs a new animation object and load the animation data from the given filename.



Parameters
* **name** (*string*) – A filename.
* **type** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) – One of the  [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype) values; `wx.adv.ANIMATION_TYPE_ANY` means that the function should try to autodetect the filetype.





See also


[`wx.adv.AnimationCtrl.CreateAnimation`](wx.adv.AnimationCtrl.html#wx.adv.AnimationCtrl.CreateAnimation "wx.adv.AnimationCtrl.CreateAnimation")





---

  



**\_\_init\_\_** *(self, other)*


Copy constructor.



Parameters
**other** ([*wx.adv.Animation*](#wx.adv.Animation "wx.adv.Animation")) – 






---

  





            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def AddHandler(handler: 'adv.AnimationDecoder') -> None:
        """ 

*static* `AddHandler`(*handler*)[¶](#wx.adv.Animation.AddHandler "Permalink to this definition")
Add a new decoder to the list of animation decoders.



Parameters
**handler** ([*wx.adv.AnimationDecoder*](wx.adv.AnimationDecoder.html#wx.adv.AnimationDecoder "wx.adv.AnimationDecoder")) – 






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def CleanUpHandlers() -> None:
        """ 

*static* `CleanUpHandlers`()[¶](#wx.adv.Animation.CleanUpHandlers "Permalink to this definition")
Clear out the animation decoder list.


This is called automatically at program shutdown.




            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def FindHandler(animType: AnimationType) -> 'AnimationDecoder':
        """ 

*static* `FindHandler`(*animType*)[¶](#wx.adv.Animation.FindHandler "Permalink to this definition")
Search for an animation decoder by type.



Parameters
**animType** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) – 



Return type
 [wx.adv.AnimationDecoder](wx.adv.AnimationDecoder.html#wx-adv-animationdecoder)






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetDelay(self, frame: int) -> int:
        """ 

`GetDelay`(*self*, *frame*)[¶](#wx.adv.Animation.GetDelay "Permalink to this definition")
Returns the delay for the i-th frame in milliseconds.


If `-1` is returned the frame is to be displayed forever.



Parameters
**frame** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetFrame(self, frame: int) -> 'Image':
        """ 

`GetFrame`(*self*, *frame*)[¶](#wx.adv.Animation.GetFrame "Permalink to this definition")
Returns the i-th frame as a  [wx.Image](wx.Image.html#wx-image).


This method is not implemented in the native wxGTK implementation of this class and always returns an invalid image there.



Parameters
**frame** (*int*) – 



Return type
*Image*






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetFrameCount(self) -> int:
        """ 

`GetFrameCount`(*self*)[¶](#wx.adv.Animation.GetFrameCount "Permalink to this definition")
Returns the number of frames for this animation.


This method is not implemented in the native wxGTK implementation of this class and always returns 0 there.



Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def GetHandlers() -> list['adv.AnimationHandler']:
        """ 

*static* `GetHandlers`()[¶](#wx.adv.Animation.GetHandlers "Permalink to this definition")
Returns the list of animation decoders used by the generic animation and  [wx.adv.GenericAnimationCtrl](wx.adv.GenericAnimationCtrl.html#wx-adv-genericanimationctrl).



Return type
*AnimationDecoderList*






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def GetSize(self) -> 'Size':
        """ 

`GetSize`(*self*)[¶](#wx.adv.Animation.GetSize "Permalink to this definition")
Returns the size of the animation.



Return type
[`Size`](#wx.adv.Animation.Size "wx.adv.Animation.Size")






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def InitStandardHandlers() -> None:
        """ 

*static* `InitStandardHandlers`()[¶](#wx.adv.Animation.InitStandardHandlers "Permalink to this definition")
Load the stock animation decoders (currently `GIF` and `ANI`) into the list of decoders.


This is called automatically at program startup.




            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    @staticmethod
    def InsertHandler(handler: 'adv.AnimationDecoder') -> None:
        """ 

*static* `InsertHandler`(*handler*)[¶](#wx.adv.Animation.InsertHandler "Permalink to this definition")
Insert a new decoder to the front of the list of animation decoders.



Parameters
**handler** ([*wx.adv.AnimationDecoder*](wx.adv.AnimationDecoder.html#wx.adv.AnimationDecoder "wx.adv.AnimationDecoder")) – 






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def IsCompatibleWith(self, ci: 'ClassInfo') -> bool:
        """ 

`IsCompatibleWith`(*self*, *ci*)[¶](#wx.adv.Animation.IsCompatibleWith "Permalink to this definition")
Returns `True` if animation can be used with controls of the given type.


This function checks if this animation object can be used with  [wx.adv.AnimationCtrl](wx.adv.AnimationCtrl.html#wx-adv-animationctrl) of particular type. This will be always the case for the platforms where only a single  [wx.adv.AnimationCtrl](wx.adv.AnimationCtrl.html#wx-adv-animationctrl) implementation is available, but not necessarily under e.g. wxGTK where both native (but limited) GTK implementation and generic implementation can be used.



Parameters
**ci** ([*wx.ClassInfo*](wx.ClassInfo.html#wx.ClassInfo "wx.ClassInfo")) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.adv.Animation.IsOk "Permalink to this definition")
Returns `True` if animation data is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def Load(self, stream, type=ANIMATION_TYPE_ANY) -> bool:
        """ 

`Load`(*self*, *stream*, *type=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.Animation.Load "Permalink to this definition")
Loads an animation from the given stream.



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – The stream to use to load the animation. Under wxGTK may be any kind of stream; under other platforms this must be a seekable stream.
* **type** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) – One of the  [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype) enumeration values.



Return type
*bool*



Returns
`True` if the operation succeeded, `False` otherwise.






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    def LoadFile(self, name, type=ANIMATION_TYPE_ANY) -> bool:
        """ 

`LoadFile`(*self*, *name*, *type=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.Animation.LoadFile "Permalink to this definition")
Loads an animation from a file.



Parameters
* **name** (*string*) – A filename.
* **type** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) – One of the  [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype) values; `wx.adv.ANIMATION_TYPE_ANY` means that the function should try to autodetect the filetype.



Return type
*bool*



Returns
`True` if the operation succeeded, `False` otherwise.






            Source: https://docs.wxpython.org/wx.adv.Animation.html
        """

    FrameCount: int  # `FrameCount`[¶](#wx.adv.Animation.FrameCount "Permalink to this definition")See [`GetFrameCount`](#wx.adv.Animation.GetFrameCount "wx.adv.Animation.GetFrameCount")
    Size: '_Size'  # `Size`[¶](#wx.adv.Animation.Size "Permalink to this definition")See [`GetSize`](#wx.adv.Animation.GetSize "wx.adv.Animation.GetSize")



ANIMATION_TYPE_ANY: int

class LayoutAlgorithm(Object):
    """ **Possible constructors**:



```
LayoutAlgorithm()

```


LayoutAlgorithm implements layout of subwindows in MDI or SDI
frames.


  


        Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.adv.LayoutAlgorithm.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutFrame(self, frame, mainWindow=None) -> bool:
        """ 

`LayoutFrame`(*self*, *frame*, *mainWindow=None*)[¶](#wx.adv.LayoutAlgorithm.LayoutFrame "Permalink to this definition")
Lays out the children of a normal frame.


*mainWindow* is set to occupy the remaining space. This function simply calls [`LayoutWindow`](#wx.adv.LayoutAlgorithm.LayoutWindow "wx.adv.LayoutAlgorithm.LayoutWindow") .



Parameters
* **frame** ([*wx.Frame*](wx.Frame.html#wx.Frame "wx.Frame")) –
* **mainWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutMDIFrame(self, frame, rect=None) -> bool:
        """ 

`LayoutMDIFrame`(*self*, *frame*, *rect=None*)[¶](#wx.adv.LayoutAlgorithm.LayoutMDIFrame "Permalink to this definition")
Lays out the children of an MDI parent frame.


If *rect* is not `None`, the given rectangle will be used as a starting point instead of the frame’s client area. The MDI client window is set to occupy the remaining space.



Parameters
* **frame** ([*wx.MDIParentFrame*](wx.MDIParentFrame.html#wx.MDIParentFrame "wx.MDIParentFrame")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """

    def LayoutWindow(self, parent, mainWindow=None) -> bool:
        """ 

`LayoutWindow`(*self*, *parent*, *mainWindow=None*)[¶](#wx.adv.LayoutAlgorithm.LayoutWindow "Permalink to this definition")
Lays out the children of a normal frame or other window.


*mainWindow* is set to occupy the remaining space. If this is not specified, then the last window that responds to a calculate layout event in query mode will get the remaining space (that is, a non-query OnCalculateLayout event will not be sent to this window and the window will be set to the remaining size).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **mainWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.LayoutAlgorithm.html
        """



class Sound(Object):
    """ **Possible constructors**:



```
Sound()

Sound(fileName)

```


This class represents a short sound (loaded from Windows `WAV` file),
that can be stored in memory and played.


  


        Source: https://docs.wxpython.org/wx.adv.Sound.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.Sound.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, fileName)*


Constructs a wave object from a file or, under Windows, from a Windows resource.


Call [`IsOk`](#wx.adv.Sound.IsOk "wx.adv.Sound.IsOk") to determine whether this succeeded.



Parameters
**fileName** (*string*) – The filename or Windows resource.






---

  





            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def Create(self, fileName: str) -> bool:
        """ 

`Create`(*self*, *fileName*)[¶](#wx.adv.Sound.Create "Permalink to this definition")
Constructs a wave object from a file or resource.



Parameters
**fileName** (*string*) – The filename or Windows resource.



Return type
*bool*



Returns
`True` if the call was successful, `False` otherwise.






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def CreateFromData(self, data) -> bool:
        """ 

`CreateFromData`(*self*, *data*)[¶](#wx.adv.Sound.CreateFromData "Permalink to this definition")
Create a sound object from data in a memory buffer in `WAV` format.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.adv.Sound.IsOk "Permalink to this definition")
Returns `True` if the object contains a successfully loaded file or resource, `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def Play(self, flags: Any=SOUND_ASYNC) -> bool:
        """ 

`Play`(*self*, *flags=SOUND\_ASYNC*)[¶](#wx.adv.Sound.Play "Permalink to this definition")
Plays the sound file.


If another sound is playing, it will be interrupted.


Returns `True` on success, `False` otherwise. Note that in general it is possible to delete the object which is being asynchronously played any time after calling this function and the sound would continue playing, however this currently doesn’t work under Windows for sound objects loaded from memory data.


The possible values for *flags* are:


* `wx.adv.SOUND_SYNC`: `Play` will block and wait until the sound is replayed.
* `wx.adv.SOUND_ASYNC`: Sound is played asynchronously, `Play` returns immediately.
* SOUND\_ASYNC|wxSOUND\_LOOP: Sound is played asynchronously and loops until another sound is played, [`Stop`](#wx.adv.Sound.Stop "wx.adv.Sound.Stop") is called or the program terminates.


The static form is shorthand for this code:



```
wx.adv.Sound(filename).Play(flags)

```



Parameters
**flags** – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    @staticmethod
    def PlaySound(filename, flags=SOUND_ASYNC) -> bool:
        """ 

*static* `PlaySound`(*filename*, *flags=SOUND\_ASYNC*)[¶](#wx.adv.Sound.PlaySound "Permalink to this definition")
Plays the sound file.


If another sound is playing, it will be interrupted.


Returns `True` on success, `False` otherwise. Note that in general it is possible to delete the object which is being asynchronously played any time after calling this function and the sound would continue playing, however this currently doesn’t work under Windows for sound objects loaded from memory data.


The possible values for *flags* are:


* `wx.adv.SOUND_SYNC`: `Play` will block and wait until the sound is replayed.
* `wx.adv.SOUND_ASYNC`: Sound is played asynchronously, `Play` returns immediately.
* SOUND\_ASYNC|wxSOUND\_LOOP: Sound is played asynchronously and loops until another sound is played, [`Stop`](#wx.adv.Sound.Stop "wx.adv.Sound.Stop") is called or the program terminates.


The static form is shorthand for this code:



```
wx.adv.Sound(filename).Play(flags)

```



Parameters
* **filename** (*string*) –
* **flags** –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    @staticmethod
    def Stop() -> None:
        """ 

*static* `Stop`()[¶](#wx.adv.Sound.Stop "Permalink to this definition")
If a sound is played, this function stops it.




            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.adv.Sound.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.adv.Sound.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.Sound.html
        """



SOUND_SYNC: int

SOUND_ASYNC: int

class WizardPage(Panel):
    """ **Possible constructors**:



```
WizardPage()

WizardPage(parent, bitmap=BitmapBundle())

```


WizardPage is one of the screens in Wizard: it must know what are
the following and preceding pages (which may be `None` for the
first/last page).


  


        Source: https://docs.wxpython.org/wx.adv.WizardPage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.WizardPage.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, bitmap=BitmapBundle())*


Constructor accepts an optional bitmap which will be used for this page instead of the default one for this wizard (note that all bitmaps used should be of the same size).


Notice that no other parameters are needed because the wizard will resize and reposition the page anyhow.



Parameters
* **parent** ([*wx.adv.Wizard*](wx.adv.Wizard.html#wx.adv.Wizard "wx.adv.Wizard")) – The parent wizard
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – The page-specific bitmap if different from the global one






---

  





            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *parent*, *bitmap=BitmapBundle()*)[¶](#wx.adv.WizardPage.Create "Permalink to this definition")
Creates the wizard page.


Must be called if the default constructor had been used to create the object.



Parameters
* **parent** ([*wx.adv.Wizard*](wx.adv.Wizard.html#wx.adv.Wizard "wx.adv.Wizard")) – The parent wizard
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – The page-specific bitmap if different from the global one



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.adv.WizardPage.GetBitmap "Permalink to this definition")
This method is called by  [wx.adv.Wizard](wx.adv.Wizard.html#wx-adv-wizard) to get the bitmap to display alongside the page.


By default, `m_bitmap` member variable which was set in the  [wx.adv.WizardPage](#wx-adv-wizardpage) constructor.


If the bitmap was not explicitly set (i.e. if `wx.NullBitmap` is returned), the default bitmap for the wizard should be used.


The only cases when you would want to override this function is if the page bitmap depends dynamically on the user choices, i.e. almost never.



Return type
[`Bitmap`](#wx.adv.WizardPage.Bitmap "wx.adv.WizardPage.Bitmap")






            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.WizardPage.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetNext(self) -> 'WizardPage':
        """ 

`GetNext`(*self*)[¶](#wx.adv.WizardPage.GetNext "Permalink to this definition")
Get the page which should be shown when the user chooses the `"Next"` button: if `None` is returned, this button will be disabled.


The last page of the wizard will usually return `None` from here, but the others will not.



Return type
 [wx.adv.WizardPage](#wx-adv-wizardpage)





See also


[`GetPrev`](#wx.adv.WizardPage.GetPrev "wx.adv.WizardPage.GetPrev")





            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    def GetPrev(self) -> 'WizardPage':
        """ 

`GetPrev`(*self*)[¶](#wx.adv.WizardPage.GetPrev "Permalink to this definition")
Get the page which should be shown when the user chooses the `"Back"` button: if `None` is returned, this button will be disabled.


The first page of the wizard will usually return `None` from here, but the others will not.



Return type
 [wx.adv.WizardPage](#wx-adv-wizardpage)





See also


[`GetNext`](#wx.adv.WizardPage.GetNext "wx.adv.WizardPage.GetNext")





            Source: https://docs.wxpython.org/wx.adv.WizardPage.html
        """

    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.adv.WizardPage.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.adv.WizardPage.GetBitmap "wx.adv.WizardPage.GetBitmap")
    Next: 'WizardPage'  # `Next`[¶](#wx.adv.WizardPage.Next "Permalink to this definition")See [`GetNext`](#wx.adv.WizardPage.GetNext "wx.adv.WizardPage.GetNext")
    Prev: 'WizardPage'  # `Prev`[¶](#wx.adv.WizardPage.Prev "Permalink to this definition")See [`GetPrev`](#wx.adv.WizardPage.GetPrev "wx.adv.WizardPage.GetPrev")



OwnerDrawnComboBoxPaintingFlags: TypeAlias = int  # Enumeration

ODCB_PAINTING_CONTROL: int

ODCB_PAINTING_SELECTED: int

class CalendarEvent(DateEvent):
    """ **Possible constructors**:



```
CalendarEvent()

CalendarEvent(win, dt, type)

```


The CalendarEvent class is used together with CalendarCtrl.


  


        Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.CalendarEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, win, dt, type)*



Parameters
* **win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –
* **type** (*wx.EventType*) –






---

  





            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    def GetWeekDay(self) -> 'WeekDay':
        """ 

`GetWeekDay`(*self*)[¶](#wx.adv.CalendarEvent.GetWeekDay "Permalink to this definition")
Returns the week day on which the user clicked in `EVT_CALENDAR_WEEKDAY_CLICKED` handler.


It doesn’t make sense to call this function in other handlers.



Return type
 [wx.DateTime.WeekDay](wx.DateTime.WeekDay.enumeration.html#wx-datetime-weekday)






            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    def SetWeekDay(self, day: DateTime.WeekDay) -> None:
        """ 

`SetWeekDay`(*self*, *day*)[¶](#wx.adv.CalendarEvent.SetWeekDay "Permalink to this definition")
Sets the week day carried by the event, normally only used by the library internally.



Parameters
**day** (*DateTime.WeekDay*) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarEvent.html
        """

    WeekDay: 'WeekDay'  # `WeekDay`[¶](#wx.adv.CalendarEvent.WeekDay "Permalink to this definition")See [`GetWeekDay`](#wx.adv.CalendarEvent.GetWeekDay "wx.adv.CalendarEvent.GetWeekDay") and [`SetWeekDay`](#wx.adv.CalendarEvent.SetWeekDay "wx.adv.CalendarEvent.SetWeekDay")



SashEdgePosition: TypeAlias = int  # Enumeration

SASH_NONE: int

SashDragStatus: TypeAlias = int  # Enumeration

class SashLayoutWindow(SashWindow):
    """ **Possible constructors**:



```
SashLayoutWindow()

SashLayoutWindow(parent, id=ID_ANY, pos=DefaultPosition,
                 size=DefaultSize, style=CLIP_CHILDREN|SW_3D, name="layoutWindow")

```


SashLayoutWindow responds to OnCalculateLayout events generated by
LayoutAlgorithm.


  


        Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.SashLayoutWindow.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=CLIP\_CHILDREN|SW\_3D, name=”layoutWindow”)*


Constructs a sash layout window, which can be a child of a frame, dialog or any other non-control window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Pointer to a parent window.
* **id** (*wx.WindowID*) – Window identifier. If -1, will automatically create an identifier.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position. DefaultPosition is (-1, -1) which indicates that SashLayoutWindows should generate a default position for the window. If using the  [wx.adv.SashLayoutWindow](#wx-adv-sashlayoutwindow) class directly, supply an actual position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. DefaultSize is (-1, -1) which indicates that SashLayoutWindows should generate a default size for the window.
* **style** (*long*) – Window style. For window styles, please see  [wx.adv.SashLayoutWindow](#wx-adv-sashlayoutwindow).
* **name** (*string*) – Window name.






---

  





            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=CLIP_CHILDREN|SW_3D, name="layoutWindow") -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=CLIP\_CHILDREN|SW\_3D*, *name="layoutWindow"*)[¶](#wx.adv.SashLayoutWindow.Create "Permalink to this definition")
Initializes a sash layout window, which can be a child of a frame, dialog or any other non-control window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Pointer to a parent window.
* **id** (*wx.WindowID*) – Window identifier. If -1, will automatically create an identifier.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position. DefaultPosition is (-1, -1) which indicates that SashLayoutWindows should generate a default position for the window. If using the  [wx.adv.SashLayoutWindow](#wx-adv-sashlayoutwindow) class directly, supply an actual position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. DefaultSize is (-1, -1) which indicates that SashLayoutWindows should generate a default size for the window.
* **style** (*long*) – Window style. For window styles, please see  [wx.adv.SashLayoutWindow](#wx-adv-sashlayoutwindow).
* **name** (*string*) – Window name.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def GetAlignment(self) -> int:
        """ 

`GetAlignment`(*self*)[¶](#wx.adv.SashLayoutWindow.GetAlignment "Permalink to this definition")
Returns the alignment of the window: one of `wx.adv.LAYOUT_TOP`, `wx.adv.LAYOUT_LEFT`, `wx.adv.LAYOUT_RIGHT`, `wx.adv.LAYOUT_BOTTOM`.



Return type
 [wx.adv.LayoutAlignment](wx.adv.LayoutAlignment.enumeration.html#wx-adv-layoutalignment)






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.SashLayoutWindow.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def GetOrientation(self) -> 'LayoutOrientation':
        """ 

`GetOrientation`(*self*)[¶](#wx.adv.SashLayoutWindow.GetOrientation "Permalink to this definition")
Returns the orientation of the window: one of `wx.adv.LAYOUT_HORIZONTAL`, `wx.adv.LAYOUT_VERTICAL`.



Return type
 [wx.adv.LayoutOrientation](wx.adv.LayoutOrientation.enumeration.html#wx-adv-layoutorientation)






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def OnCalculateLayout(self, event: 'adv.CalculateLayoutEvent') -> None:
        """ 

`OnCalculateLayout`(*self*, *event*)[¶](#wx.adv.SashLayoutWindow.OnCalculateLayout "Permalink to this definition")
The default handler for the event that is generated by  [wx.adv.LayoutAlgorithm](wx.adv.LayoutAlgorithm.html#wx-adv-layoutalgorithm).


The implementation of this function calls [`wx.adv.CalculateLayoutEvent.SetRect`](wx.adv.CalculateLayoutEvent.html#wx.adv.CalculateLayoutEvent.SetRect "wx.adv.CalculateLayoutEvent.SetRect") to shrink the provided size according to how much space this window takes up. For further details, see  [wx.adv.LayoutAlgorithm](wx.adv.LayoutAlgorithm.html#wx-adv-layoutalgorithm) and  [wx.adv.CalculateLayoutEvent](wx.adv.CalculateLayoutEvent.html#wx-adv-calculatelayoutevent).



Parameters
**event** ([*wx.adv.CalculateLayoutEvent*](wx.adv.CalculateLayoutEvent.html#wx.adv.CalculateLayoutEvent "wx.adv.CalculateLayoutEvent")) – 






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def OnQueryLayoutInfo(self, event: 'adv.QueryLayoutInfoEvent') -> None:
        """ 

`OnQueryLayoutInfo`(*self*, *event*)[¶](#wx.adv.SashLayoutWindow.OnQueryLayoutInfo "Permalink to this definition")
The default handler for the event that is generated by OnCalculateLayout to get size, alignment and orientation information for the window.


The implementation of this function uses member variables as set by accessors called by the application.


For further details, see  [wx.adv.LayoutAlgorithm](wx.adv.LayoutAlgorithm.html#wx-adv-layoutalgorithm) and  [wx.adv.QueryLayoutInfoEvent](wx.adv.QueryLayoutInfoEvent.html#wx-adv-querylayoutinfoevent).



Parameters
**event** ([*wx.adv.QueryLayoutInfoEvent*](wx.adv.QueryLayoutInfoEvent.html#wx.adv.QueryLayoutInfoEvent "wx.adv.QueryLayoutInfoEvent")) – 






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetAlignment(self, alignment: int) -> None:
        """ 

`SetAlignment`(*self*, *alignment*)[¶](#wx.adv.SashLayoutWindow.SetAlignment "Permalink to this definition")
Sets the alignment of the window (which edge of the available parent client area the window is attached to).


*alignment* is one of `wx.adv.LAYOUT_TOP`, `wx.adv.LAYOUT_LEFT`, `wx.adv.LAYOUT_RIGHT`, `wx.adv.LAYOUT_BOTTOM`.



Parameters
**alignment** ([*LayoutAlignment*](wx.adv.LayoutAlignment.enumeration.html "LayoutAlignment")) – 






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetDefaultSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetDefaultSize`(*self*, *size*)[¶](#wx.adv.SashLayoutWindow.SetDefaultSize "Permalink to this definition")
Sets the default dimensions of the window.


The dimension other than the orientation will be fixed to this value, and the orientation dimension will be ignored and the window stretched to fit the available space.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    def SetOrientation(self, orientation: LayoutOrientation) -> None:
        """ 

`SetOrientation`(*self*, *orientation*)[¶](#wx.adv.SashLayoutWindow.SetOrientation "Permalink to this definition")
Sets the orientation of the window (the direction the window will stretch in, to fill the available parent client area).


*orientation* is one of `wx.adv.LAYOUT_HORIZONTAL`, `wx.adv.LAYOUT_VERTICAL`.



Parameters
**orientation** ([*LayoutOrientation*](wx.adv.LayoutOrientation.enumeration.html "LayoutOrientation")) – 






            Source: https://docs.wxpython.org/wx.adv.SashLayoutWindow.html
        """

    Alignment: int  # `Alignment`[¶](#wx.adv.SashLayoutWindow.Alignment "Permalink to this definition")See [`GetAlignment`](#wx.adv.SashLayoutWindow.GetAlignment "wx.adv.SashLayoutWindow.GetAlignment") and [`SetAlignment`](#wx.adv.SashLayoutWindow.SetAlignment "wx.adv.SashLayoutWindow.SetAlignment")
    Orientation: 'LayoutOrientation'  # `Orientation`[¶](#wx.adv.SashLayoutWindow.Orientation "Permalink to this definition")See [`GetOrientation`](#wx.adv.SashLayoutWindow.GetOrientation "wx.adv.SashLayoutWindow.GetOrientation") and [`SetOrientation`](#wx.adv.SashLayoutWindow.SetOrientation "wx.adv.SashLayoutWindow.SetOrientation")



class GenericAnimationCtrl(AnimationCtrl):
    """ **Possible constructors**:



```
GenericAnimationCtrl(parent, id=ID_ANY, anim=NullAnimation,
                     pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE,
                     name=AnimationCtrlNameStr)

```


Generic implementation of AnimationCtrl interface.


  


        Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> None:
        """ 

`__init__`(*self*, *parent*, *id=ID\_ANY*, *anim=NullAnimation*, *pos=DefaultPosition*, *size=DefaultSize*, *style=AC\_DEFAULT\_STYLE*, *name=AnimationCtrlNameStr*)[¶](#wx.adv.GenericAnimationCtrl.__init__ "Permalink to this definition")
Initializes the object and calls [`Create`](#wx.adv.GenericAnimationCtrl.Create "wx.adv.GenericAnimationCtrl.Create") with all the parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Create(self, parent, id=ID_ANY, anim=NullAnimation, pos=DefaultPosition, size=DefaultSize, style=AC_DEFAULT_STYLE, name=AnimationCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *anim=NullAnimation*, *pos=DefaultPosition*, *size=DefaultSize*, *style=AC\_DEFAULT\_STYLE*, *name=AnimationCtrlNameStr*)[¶](#wx.adv.GenericAnimationCtrl.Create "Permalink to this definition")
Creates the control with the given *anim* animation.


After control creation you must explicitly call [`Play`](#wx.adv.GenericAnimationCtrl.Play "wx.adv.GenericAnimationCtrl.Play") to start to play the animation. Until that function won’t be called, the first frame of the animation is displayed.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window, must be not `None`.
* **id** (*wx.WindowID*) – The identifier for the control.
* **anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) – The initial animation shown in the control.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size.
* **style** (*long*) – The window style, see `AC_` flags.
* **name** (*string*) – Control name.



Return type
*bool*



Returns
`True` if the control was successfully created or `False` if creation failed.






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def CreateAnimation(self) -> 'Animation':
        """ 

`CreateAnimation`(*self*)[¶](#wx.adv.GenericAnimationCtrl.CreateAnimation "Permalink to this definition")
Create a new animation object compatible with this control.


A  [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation) object created using this function is always compatible with controls of this type, see [`wx.adv.Animation.IsCompatibleWith`](wx.adv.Animation.html#wx.adv.Animation.IsCompatibleWith "wx.adv.Animation.IsCompatibleWith") .



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)





New in version 4.1/wxWidgets-3.1.4.




See also


[`CreateCompatibleAnimation`](#wx.adv.GenericAnimationCtrl.CreateCompatibleAnimation "wx.adv.GenericAnimationCtrl.CreateCompatibleAnimation")





            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    @staticmethod
    def CreateCompatibleAnimation() -> 'Animation':
        """ 

*static* `CreateCompatibleAnimation`()[¶](#wx.adv.GenericAnimationCtrl.CreateCompatibleAnimation "Permalink to this definition")
Create a new animation object compatible with this control.


This method does the same thing as [`CreateAnimation`](#wx.adv.GenericAnimationCtrl.CreateAnimation "wx.adv.GenericAnimationCtrl.CreateAnimation") but is static, i.e. can be called without creating any  [wx.adv.AnimationCtrl](wx.adv.AnimationCtrl.html#wx-adv-animationctrl) objects.



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def DrawCurrentFrame(self, dc: 'DC') -> None:
        """ 

`DrawCurrentFrame`(*self*, *dc*)[¶](#wx.adv.GenericAnimationCtrl.DrawCurrentFrame "Permalink to this definition")
Draw the current frame of the animation into given DC.


This is fast as current frame is always cached.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetAnimation(self) -> 'Animation':
        """ 

`GetAnimation`(*self*)[¶](#wx.adv.GenericAnimationCtrl.GetAnimation "Permalink to this definition")
Returns the animation associated with this control.



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetBackingStore(self) -> 'Bitmap':
        """ 

`GetBackingStore`(*self*)[¶](#wx.adv.GenericAnimationCtrl.GetBackingStore "Permalink to this definition")
Returns a  [wx.Bitmap](wx.Bitmap.html#wx-bitmap) with the current frame drawn in it.



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.GenericAnimationCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def GetInactiveBitmap(self) -> 'Bitmap':
        """ 

`GetInactiveBitmap`(*self*)[¶](#wx.adv.GenericAnimationCtrl.GetInactiveBitmap "Permalink to this definition")
Returns the inactive bitmap shown in this control when the; see [`SetInactiveBitmap`](#wx.adv.GenericAnimationCtrl.SetInactiveBitmap "wx.adv.GenericAnimationCtrl.SetInactiveBitmap") for more info.



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def IsPlaying(self) -> bool:
        """ 

`IsPlaying`(*self*)[¶](#wx.adv.GenericAnimationCtrl.IsPlaying "Permalink to this definition")
Returns `True` if the animation is being played.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def IsUsingWindowBackgroundColour(self) -> bool:
        """ 

`IsUsingWindowBackgroundColour`(*self*)[¶](#wx.adv.GenericAnimationCtrl.IsUsingWindowBackgroundColour "Permalink to this definition")
Returns `true` if the window’s background colour is being used.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Load(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ 

`Load`(*self*, *file*, *animType=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.GenericAnimationCtrl.Load "Permalink to this definition")
Loads the animation from the given stream and calls [`SetAnimation`](#wx.adv.GenericAnimationCtrl.SetAnimation "wx.adv.GenericAnimationCtrl.SetAnimation") .


See [`wx.adv.Animation.Load`](wx.adv.Animation.html#wx.adv.Animation.Load "wx.adv.Animation.Load") for more info.



Parameters
* **file** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **animType** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def LoadFile(self, file, animType=ANIMATION_TYPE_ANY) -> bool:
        """ 

`LoadFile`(*self*, *file*, *animType=ANIMATION\_TYPE\_ANY*)[¶](#wx.adv.GenericAnimationCtrl.LoadFile "Permalink to this definition")
Loads the animation from the given file and calls [`SetAnimation`](#wx.adv.GenericAnimationCtrl.SetAnimation "wx.adv.GenericAnimationCtrl.SetAnimation") .


See [`wx.adv.Animation.LoadFile`](wx.adv.Animation.html#wx.adv.Animation.LoadFile "wx.adv.Animation.LoadFile") for more info.



Parameters
* **file** (*string*) –
* **animType** ([*AnimationType*](wx.adv.AnimationType.enumeration.html "AnimationType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Play(self, *args, **kw) -> bool:
        """ 

`Play`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.GenericAnimationCtrl.Play "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Play** *(self, looped)*


This overload of [`Play`](#wx.adv.GenericAnimationCtrl.Play "wx.adv.GenericAnimationCtrl.Play") lets you specify if the animation must loop or not.



Parameters
**looped** (*bool*) – 



Return type
*bool*






---

  



**Play** *(self)*


Starts playing the animation.


The animation is always played in loop mode (unless the last frame of the animation has an infinite delay time) and always start from the first frame even if you `stopped` it while some other frame was displayed.



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetAnimation(self, anim: 'adv.Animation') -> None:
        """ 

`SetAnimation`(*self*, *anim*)[¶](#wx.adv.GenericAnimationCtrl.SetAnimation "Permalink to this definition")
Sets the animation to play in this control.


If the previous animation is being played, it’s [`Stop`](#wx.adv.GenericAnimationCtrl.Stop "wx.adv.GenericAnimationCtrl.Stop") stopped. Until [`Play`](#wx.adv.GenericAnimationCtrl.Play "wx.adv.GenericAnimationCtrl.Play") isn’t called, a static image, the first frame of the given animation or the background colour will be shown (see [`SetInactiveBitmap`](#wx.adv.GenericAnimationCtrl.SetInactiveBitmap "wx.adv.GenericAnimationCtrl.SetInactiveBitmap") for more info).



Parameters
**anim** ([*wx.adv.Animation*](wx.adv.Animation.html#wx.adv.Animation "wx.adv.Animation")) – 






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetInactiveBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetInactiveBitmap`(*self*, *bmp*)[¶](#wx.adv.GenericAnimationCtrl.SetInactiveBitmap "Permalink to this definition")
Sets the bitmap to show on the control when it’s not playing an animation.


If you set as inactive bitmap `wx.NullBitmap` (which is the default), then the first frame of the animation is instead shown when the control is inactive; in this case, if there’s no valid animation associated with the control (see [`SetAnimation`](#wx.adv.GenericAnimationCtrl.SetAnimation "wx.adv.GenericAnimationCtrl.SetAnimation") ), then the background colour of the window is shown.


If the control is not playing the animation, the given bitmap will be immediately shown, otherwise it will be shown as soon as [`Stop`](#wx.adv.GenericAnimationCtrl.Stop "wx.adv.GenericAnimationCtrl.Stop") is called.


Note that the inactive bitmap, if smaller than the control’s size, will be centered in the control; if bigger, it will be stretched to fit it.



Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def SetUseWindowBackgroundColour(self, useWinBackground: bool=True) -> None:
        """ 

`SetUseWindowBackgroundColour`(*self*, *useWinBackground=True*)[¶](#wx.adv.GenericAnimationCtrl.SetUseWindowBackgroundColour "Permalink to this definition")
Specify whether the animation’s background colour is to be shown (the default), or whether the window background should show through.



Parameters
**useWinBackground** (*bool*) – 






            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    def Stop(self) -> None:
        """ 

`Stop`(*self*)[¶](#wx.adv.GenericAnimationCtrl.Stop "Permalink to this definition")
Stops playing the animation.


The control will show the first frame of the animation, a custom static image or the window’s background colour as specified by the last [`SetInactiveBitmap`](#wx.adv.GenericAnimationCtrl.SetInactiveBitmap "wx.adv.GenericAnimationCtrl.SetInactiveBitmap") call.




            Source: https://docs.wxpython.org/wx.adv.GenericAnimationCtrl.html
        """

    Animation: 'Animation'  # `Animation`[¶](#wx.adv.GenericAnimationCtrl.Animation "Permalink to this definition")See [`GetAnimation`](#wx.adv.GenericAnimationCtrl.GetAnimation "wx.adv.GenericAnimationCtrl.GetAnimation") and [`SetAnimation`](#wx.adv.GenericAnimationCtrl.SetAnimation "wx.adv.GenericAnimationCtrl.SetAnimation")
    BackingStore: 'Bitmap'  # `BackingStore`[¶](#wx.adv.GenericAnimationCtrl.BackingStore "Permalink to this definition")See [`GetBackingStore`](#wx.adv.GenericAnimationCtrl.GetBackingStore "wx.adv.GenericAnimationCtrl.GetBackingStore")
    InactiveBitmap: 'Bitmap'  # `InactiveBitmap`[¶](#wx.adv.GenericAnimationCtrl.InactiveBitmap "Permalink to this definition")See [`GetInactiveBitmap`](#wx.adv.GenericAnimationCtrl.GetInactiveBitmap "wx.adv.GenericAnimationCtrl.GetInactiveBitmap") and [`SetInactiveBitmap`](#wx.adv.GenericAnimationCtrl.SetInactiveBitmap "wx.adv.GenericAnimationCtrl.SetInactiveBitmap")



AnimationType: TypeAlias = int  # Enumeration

ANIMATION_TYPE_INVALID: int

ANIMATION_TYPE_GIF: int

ANIMATION_TYPE_ANI: int

class CalendarDateAttr:
    """ **Possible constructors**:



```
CalendarDateAttr(colText=NullColour, colBack=NullColour,
                 colBorder=NullColour, font=NullFont, border=CAL_BORDER_NONE)

CalendarDateAttr(border, colBorder=NullColour)

```


CalendarDateAttr is a custom attributes for a calendar date.


  


        Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.CalendarDateAttr.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, colText=NullColour, colBack=NullColour, colBorder=NullColour, font=NullFont, border=CAL\_BORDER\_NONE)*


Constructor for specifying all  [wx.adv.CalendarDateAttr](#wx-adv-calendardateattr) properties.



Parameters
* **colText** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBack** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBorder** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –
* **border** ([*CalendarDateBorder*](wx.adv.CalendarDateBorder.enumeration.html "CalendarDateBorder")) –






---

  



**\_\_init\_\_** *(self, border, colBorder=NullColour)*


Constructor using default properties except the given border.



Parameters
* **border** ([*CalendarDateBorder*](wx.adv.CalendarDateBorder.enumeration.html "CalendarDateBorder")) –
* **colBorder** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






---

  





            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.adv.CalendarDateAttr.GetBackgroundColour "Permalink to this definition")
Returns the background colour set for the calendar date.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBorder(self) -> 'CalendarDateBorder':
        """ 

`GetBorder`(*self*)[¶](#wx.adv.CalendarDateAttr.GetBorder "Permalink to this definition")
Returns the border set for the calendar date.



Return type
 [wx.adv.CalendarDateBorder](wx.adv.CalendarDateBorder.enumeration.html#wx-adv-calendardateborder)






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetBorderColour(self) -> 'Colour':
        """ 

`GetBorderColour`(*self*)[¶](#wx.adv.CalendarDateAttr.GetBorderColour "Permalink to this definition")
Returns the border colour set for the calendar date.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.adv.CalendarDateAttr.GetFont "Permalink to this definition")
Returns the font set for the calendar date.



Return type
[`Font`](#wx.adv.CalendarDateAttr.Font "wx.adv.CalendarDateAttr.Font")






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    @staticmethod
    def GetMark() -> 'CalendarDateAttr':
        """ 

*static* `GetMark`()[¶](#wx.adv.CalendarDateAttr.GetMark "Permalink to this definition")
Used (internally) by the generic [`wx.adv.CalendarCtrl.Mark`](wx.adv.CalendarCtrl.html#wx.adv.CalendarCtrl.Mark "wx.adv.CalendarCtrl.Mark") .



Return type
 [wx.adv.CalendarDateAttr](#wx-adv-calendardateattr)






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def GetTextColour(self) -> 'Colour':
        """ 

`GetTextColour`(*self*)[¶](#wx.adv.CalendarDateAttr.GetTextColour "Permalink to this definition")
Returns the text colour set for the calendar date.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBackgroundColour(self) -> bool:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.adv.CalendarDateAttr.HasBackgroundColour "Permalink to this definition")
Returns `True` if a non-default text background colour is set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBorder(self) -> bool:
        """ 

`HasBorder`(*self*)[¶](#wx.adv.CalendarDateAttr.HasBorder "Permalink to this definition")
Returns `True` if a non-default (i.e. any) border is set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasBorderColour(self) -> bool:
        """ 

`HasBorderColour`(*self*)[¶](#wx.adv.CalendarDateAttr.HasBorderColour "Permalink to this definition")
Returns `True` if a non-default border colour is set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasFont(self) -> bool:
        """ 

`HasFont`(*self*)[¶](#wx.adv.CalendarDateAttr.HasFont "Permalink to this definition")
Returns `True` if a non-default font is set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def HasTextColour(self) -> bool:
        """ 

`HasTextColour`(*self*)[¶](#wx.adv.CalendarDateAttr.HasTextColour "Permalink to this definition")
Returns `True` if a non-default text foreground colour is set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def IsHoliday(self) -> bool:
        """ 

`IsHoliday`(*self*)[¶](#wx.adv.CalendarDateAttr.IsHoliday "Permalink to this definition")
Returns `True` if this calendar day is displayed as a holiday.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colBack*)[¶](#wx.adv.CalendarDateAttr.SetBackgroundColour "Permalink to this definition")
Sets the text background colour to use.



Parameters
**colBack** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBorder(self, border: CalendarDateBorder) -> None:
        """ 

`SetBorder`(*self*, *border*)[¶](#wx.adv.CalendarDateAttr.SetBorder "Permalink to this definition")
Sets the border to use.



Parameters
**border** ([*CalendarDateBorder*](wx.adv.CalendarDateBorder.enumeration.html "CalendarDateBorder")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetBorderColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetBorderColour`(*self*, *col*)[¶](#wx.adv.CalendarDateAttr.SetBorderColour "Permalink to this definition")
Sets the border colour to use.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.adv.CalendarDateAttr.SetFont "Permalink to this definition")
Sets the font to use.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetHoliday(self, holiday: bool) -> None:
        """ 

`SetHoliday`(*self*, *holiday*)[¶](#wx.adv.CalendarDateAttr.SetHoliday "Permalink to this definition")
If *holiday* is `True`, this calendar day will be displayed as a holiday.



Parameters
**holiday** (*bool*) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    @staticmethod
    def SetMark(m: 'adv.CalendarDateAttr') -> None:
        """ 

*static* `SetMark`(*m*)[¶](#wx.adv.CalendarDateAttr.SetMark "Permalink to this definition")
Set the attributes that will be used to Mark() days on the generic  [wx.adv.CalendarCtrl](wx.adv.CalendarCtrl.html#wx-adv-calendarctrl).



Parameters
**m** ([*wx.adv.CalendarDateAttr*](#wx.adv.CalendarDateAttr "wx.adv.CalendarDateAttr")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colText*)[¶](#wx.adv.CalendarDateAttr.SetTextColour "Permalink to this definition")
Sets the text (foreground) colour to use.



Parameters
**colText** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.adv.CalendarDateAttr.html
        """

    BackgroundColour: 'Colour'  # `BackgroundColour`[¶](#wx.adv.CalendarDateAttr.BackgroundColour "Permalink to this definition")See [`GetBackgroundColour`](#wx.adv.CalendarDateAttr.GetBackgroundColour "wx.adv.CalendarDateAttr.GetBackgroundColour") and [`SetBackgroundColour`](#wx.adv.CalendarDateAttr.SetBackgroundColour "wx.adv.CalendarDateAttr.SetBackgroundColour")
    Border: 'CalendarDateBorder'  # `Border`[¶](#wx.adv.CalendarDateAttr.Border "Permalink to this definition")See [`GetBorder`](#wx.adv.CalendarDateAttr.GetBorder "wx.adv.CalendarDateAttr.GetBorder") and [`SetBorder`](#wx.adv.CalendarDateAttr.SetBorder "wx.adv.CalendarDateAttr.SetBorder")
    BorderColour: 'Colour'  # `BorderColour`[¶](#wx.adv.CalendarDateAttr.BorderColour "Permalink to this definition")See [`GetBorderColour`](#wx.adv.CalendarDateAttr.GetBorderColour "wx.adv.CalendarDateAttr.GetBorderColour") and [`SetBorderColour`](#wx.adv.CalendarDateAttr.SetBorderColour "wx.adv.CalendarDateAttr.SetBorderColour")
    Font: '_Font'  # `Font`[¶](#wx.adv.CalendarDateAttr.Font "Permalink to this definition")See [`GetFont`](#wx.adv.CalendarDateAttr.GetFont "wx.adv.CalendarDateAttr.GetFont") and [`SetFont`](#wx.adv.CalendarDateAttr.SetFont "wx.adv.CalendarDateAttr.SetFont")
    TextColour: 'Colour'  # `TextColour`[¶](#wx.adv.CalendarDateAttr.TextColour "Permalink to this definition")See [`GetTextColour`](#wx.adv.CalendarDateAttr.GetTextColour "wx.adv.CalendarDateAttr.GetTextColour") and [`SetTextColour`](#wx.adv.CalendarDateAttr.SetTextColour "wx.adv.CalendarDateAttr.SetTextColour")



CalendarHitTestResult: TypeAlias = int  # Enumeration

CAL_HITTEST_NOWHERE: int

CAL_HITTEST_HEADER: int

CAL_HITTEST_DAY: int

CAL_HITTEST_INCMONTH: int

CAL_HITTEST_DECMONTH: int

CAL_HITTEST_SURROUNDING_WEEK: int

CAL_HITTEST_WEEK: int

PropertySheetDialogFlags: TypeAlias = int  # Enumeration

PROPSHEET_DEFAULT: int

PROPSHEET_NOTEBOOK: int

PROPSHEET_TOOLBOOK: int

PROPSHEET_CHOICEBOOK: int

PROPSHEET_LISTBOOK: int

PROPSHEET_BUTTONTOOLBOOK: int

PROPSHEET_TREEBOOK: int

PROPSHEET_SHRINKTOFIT: int

LayoutAlignment: TypeAlias = int  # Enumeration

LAYOUT_NONE: int

LayoutOrientation: TypeAlias = int  # Enumeration

TaskBarIconType: TypeAlias = int  # Enumeration

TBI_DOCK: int

TBI_CUSTOM_STATUSITEM: int

TBI_DEFAULT_TYPE: int

class AnimationDecoder(ObjectRefData):
    """ **Possible constructors**:



```
AnimationDecoder()

```


AnimationDecoder is used by Animation for loading frames and other
information for the animation from the animation image file.


  


        Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.adv.AnimationDecoder.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def CanRead(self, stream: 'InputStream') -> bool:
        """ 

`CanRead`(*self*, *stream*)[¶](#wx.adv.AnimationDecoder.CanRead "Permalink to this definition")
Returns `True` if this decoder supports loading from the given stream.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def Clone(self) -> 'AnimationDecoder':
        """ 

`Clone`(*self*)[¶](#wx.adv.AnimationDecoder.Clone "Permalink to this definition")
Create a copy of this decoder.



Return type
 [wx.adv.AnimationDecoder](#wx-adv-animationdecoder)






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ 

`ConvertToImage`(*self*, *frame*, *image*)[¶](#wx.adv.AnimationDecoder.ConvertToImage "Permalink to this definition")
Convert given frame to  [wx.Image](wx.Image.html#wx-image).



Parameters
* **frame** (*int*) –
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ 

`DoCanRead`(*self*, *stream*)[¶](#wx.adv.AnimationDecoder.DoCanRead "Permalink to this definition")
Checks the signature of the data in the given stream and returns `True` if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since [`CanRead`](#wx.adv.AnimationDecoder.CanRead "wx.adv.AnimationDecoder.CanRead") will do it.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetAnimationSize(self) -> 'Size':
        """ 

`GetAnimationSize`(*self*)[¶](#wx.adv.AnimationDecoder.GetAnimationSize "Permalink to this definition")

Return type
*Size*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.adv.AnimationDecoder.GetBackgroundColour "Permalink to this definition")

Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ 

`GetDelay`(*self*, *frame*)[¶](#wx.adv.AnimationDecoder.GetDelay "Permalink to this definition")
Return the number of milliseconds this frame should be displayed.


If -1 is returned then the frame must be displayed forever.



Parameters
**frame** (*int*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'AnimationDisposal':
        """ 

`GetDisposalMethod`(*self*, *frame*)[¶](#wx.adv.AnimationDecoder.GetDisposalMethod "Permalink to this definition")
What should be done after displaying this frame.



Parameters
**frame** (*int*) – 



Return type
 [wx.adv.AnimationDisposal](wx.adv.AnimationDisposal.enumeration.html#wx-adv-animationdisposal)






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFrameCount(self) -> int:
        """ 

`GetFrameCount`(*self*)[¶](#wx.adv.AnimationDecoder.GetFrameCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ 

`GetFramePosition`(*self*, *frame*)[¶](#wx.adv.AnimationDecoder.GetFramePosition "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ 

`GetFrameSize`(*self*, *frame*)[¶](#wx.adv.AnimationDecoder.GetFrameSize "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Size*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ 

`GetTransparentColour`(*self*, *frame*)[¶](#wx.adv.AnimationDecoder.GetTransparentColour "Permalink to this definition")
The transparent colour for this frame, if any, or `NullColour` .



Parameters
**frame** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def GetType(self) -> 'AnimationType':
        """ 

`GetType`(*self*)[¶](#wx.adv.AnimationDecoder.GetType "Permalink to this definition")
Return the animation type this decoder implements.



Return type
 [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype)






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ 

`Load`(*self*, *stream*)[¶](#wx.adv.AnimationDecoder.Load "Permalink to this definition")
Load the animation image frames from the given stream.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.AnimationDecoder.html
        """

    AnimationSize: 'Size'  # `AnimationSize`[¶](#wx.adv.AnimationDecoder.AnimationSize "Permalink to this definition")See [`GetAnimationSize`](#wx.adv.AnimationDecoder.GetAnimationSize "wx.adv.AnimationDecoder.GetAnimationSize")
    BackgroundColour: 'Colour'  # `BackgroundColour`[¶](#wx.adv.AnimationDecoder.BackgroundColour "Permalink to this definition")See [`GetBackgroundColour`](#wx.adv.AnimationDecoder.GetBackgroundColour "wx.adv.AnimationDecoder.GetBackgroundColour")
    FrameCount: int  # `FrameCount`[¶](#wx.adv.AnimationDecoder.FrameCount "Permalink to this definition")See [`GetFrameCount`](#wx.adv.AnimationDecoder.GetFrameCount "wx.adv.AnimationDecoder.GetFrameCount")
    Type: 'AnimationType'  # `Type`[¶](#wx.adv.AnimationDecoder.Type "Permalink to this definition")See [`GetType`](#wx.adv.AnimationDecoder.GetType "wx.adv.AnimationDecoder.GetType")



class WizardPageSimple(WizardPage):
    """ **Possible constructors**:



```
WizardPageSimple()

WizardPageSimple(parent, prev=None, next=None, bitmap=BitmapBundle())

```


WizardPageSimple is the simplest possible WizardPage
implementation: it just returns the pointers given to its constructor
from *WizardPage.GetNext()* and *WizardPage.GetPrev()* functions.


  


        Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.WizardPageSimple.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, prev=None, next=None, bitmap=BitmapBundle())*


Constructor takes the previous and next pages.


They may be modified later by [`SetPrev`](#wx.adv.WizardPageSimple.SetPrev "wx.adv.WizardPageSimple.SetPrev") or [`SetNext`](#wx.adv.WizardPageSimple.SetNext "wx.adv.WizardPageSimple.SetNext") .



Parameters
* **parent** ([*wx.adv.Wizard*](wx.adv.Wizard.html#wx.adv.Wizard "wx.adv.Wizard")) –
* **prev** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –
* **next** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






---

  





            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def Chain(self, *args, **kw) -> 'WizardPageSimple':
        """ 

`Chain`(*self*, *\*args*, *\*\*kw*)[¶](#wx.adv.WizardPageSimple.Chain "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Chain** *(self, next)*


A helper chaining this page with the next one.


Notice that this method returns a reference to the next page, so the calls to it can, in turn, be chained:



```
page3 = wx.RadioboxPage(wizard)
page4 = wx.ValidationPage(wizard)

wx.adv.WizardPageSimple.Chain(page3, page4)

```


This makes this method the simplest way to define the order of changes in fully static wizards, i.e. in those where the order doesn’t depend on the choices made by the user in the wizard pages during run-time.



Parameters
**next** ([*wx.adv.WizardPageSimple*](#wx.adv.WizardPageSimple "wx.adv.WizardPageSimple")) – A not `None` pointer to the next page.



Return type
 [wx.adv.WizardPageSimple](#wx-adv-wizardpagesimple)



Returns
Reference to *next* on which [`Chain`](#wx.adv.WizardPageSimple.Chain "wx.adv.WizardPageSimple.Chain") can be called again.





New in version 2.9.5.





---

  



**Chain** *(first, second)*


A convenience function to make the pages follow each other.


Example:



```
# FirstPage is an instance of wx.adv.WizardPageSimple
firstPage = FirstPage(self)
firstPage.Chain(SecondPage).Chain(ThirdPage).Chain(LastPage)

```



Parameters
* **first** ([*wx.adv.WizardPageSimple*](#wx.adv.WizardPageSimple "wx.adv.WizardPageSimple")) –
* **second** ([*wx.adv.WizardPageSimple*](#wx.adv.WizardPageSimple "wx.adv.WizardPageSimple")) –






---

  





            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *parent=None*, *prev=None*, *next=None*, *bitmap=BitmapBundle()*)[¶](#wx.adv.WizardPageSimple.Create "Permalink to this definition")
Creates the wizard page.


Must be called if the default constructor had been used to create the object.



Parameters
* **parent** ([*wx.adv.Wizard*](wx.adv.Wizard.html#wx.adv.Wizard "wx.adv.Wizard")) –
* **prev** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –
* **next** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.adv.WizardPageSimple.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def SetNext(self, next: 'adv.WizardPage') -> None:
        """ 

`SetNext`(*self*, *next*)[¶](#wx.adv.WizardPageSimple.SetNext "Permalink to this definition")
Sets the next page.



Parameters
**next** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 






            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """

    def SetPrev(self, prev: 'adv.WizardPage') -> None:
        """ 

`SetPrev`(*self*, *prev*)[¶](#wx.adv.WizardPageSimple.SetPrev "Permalink to this definition")
Sets the previous page.



Parameters
**prev** ([*wx.adv.WizardPage*](wx.adv.WizardPage.html#wx.adv.WizardPage "wx.adv.WizardPage")) – 






            Source: https://docs.wxpython.org/wx.adv.WizardPageSimple.html
        """



CalendarDateBorder: TypeAlias = int  # Enumeration

CAL_BORDER_NONE: int

CAL_BORDER_SQUARE: int

CAL_BORDER_ROUND: int

class ANIDecoder(AnimationDecoder):
    """ **Possible constructors**:



```
ANIDecoder()

```


An animation decoder supporting animated cursor (.ani) files.


  


        Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.adv.ANIDecoder.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def Clone(self) -> 'AnimationDecoder':
        """ 

`Clone`(*self*)[¶](#wx.adv.ANIDecoder.Clone "Permalink to this definition")
Create a copy of this decoder.



Return type
 [wx.adv.AnimationDecoder](wx.adv.AnimationDecoder.html#wx-adv-animationdecoder)






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ 

`ConvertToImage`(*self*, *frame*, *image*)[¶](#wx.adv.ANIDecoder.ConvertToImage "Permalink to this definition")
Convert given frame to  [wx.Image](wx.Image.html#wx-image).



Parameters
* **frame** (*int*) –
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ 

`DoCanRead`(*self*, *stream*)[¶](#wx.adv.ANIDecoder.DoCanRead "Permalink to this definition")
Checks the signature of the data in the given stream and returns `True` if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since [`CanRead`](wx.adv.AnimationDecoder.html#wx.adv.AnimationDecoder.CanRead "wx.adv.AnimationDecoder.CanRead") will do it.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ 

`GetDelay`(*self*, *frame*)[¶](#wx.adv.ANIDecoder.GetDelay "Permalink to this definition")
Return the number of milliseconds this frame should be displayed.


If -1 is returned then the frame must be displayed forever.



Parameters
**frame** (*int*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'AnimationDisposal':
        """ 

`GetDisposalMethod`(*self*, *frame*)[¶](#wx.adv.ANIDecoder.GetDisposalMethod "Permalink to this definition")
What should be done after displaying this frame.



Parameters
**frame** (*int*) – 



Return type
 [wx.adv.AnimationDisposal](wx.adv.AnimationDisposal.enumeration.html#wx-adv-animationdisposal)






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ 

`GetFramePosition`(*self*, *frame*)[¶](#wx.adv.ANIDecoder.GetFramePosition "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ 

`GetFrameSize`(*self*, *frame*)[¶](#wx.adv.ANIDecoder.GetFrameSize "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Size*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ 

`GetTransparentColour`(*self*, *frame*)[¶](#wx.adv.ANIDecoder.GetTransparentColour "Permalink to this definition")
The transparent colour for this frame, if any, or `NullColour` .



Parameters
**frame** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def GetType(self) -> 'AnimationType':
        """ 

`GetType`(*self*)[¶](#wx.adv.ANIDecoder.GetType "Permalink to this definition")
Return the animation type this decoder implements.



Return type
 [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype)






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ 

`Load`(*self*, *stream*)[¶](#wx.adv.ANIDecoder.Load "Permalink to this definition")
Load the animation image frames from the given stream.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.ANIDecoder.html
        """

    Type: 'AnimationType'  # `Type`[¶](#wx.adv.ANIDecoder.Type "Permalink to this definition")See [`GetType`](#wx.adv.ANIDecoder.GetType "wx.adv.ANIDecoder.GetType")



class GIFDecoder(AnimationDecoder):
    """ **Possible constructors**:



```
GIFDecoder()

```


An animation decoder supporting animated `GIF` files.


  


        Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.adv.GIFDecoder.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def Clone(self) -> 'AnimationDecoder':
        """ 

`Clone`(*self*)[¶](#wx.adv.GIFDecoder.Clone "Permalink to this definition")
Create a copy of this decoder.



Return type
 [wx.adv.AnimationDecoder](wx.adv.AnimationDecoder.html#wx-adv-animationdecoder)






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def ConvertToImage(self, frame, image) -> bool:
        """ 

`ConvertToImage`(*self*, *frame*, *image*)[¶](#wx.adv.GIFDecoder.ConvertToImage "Permalink to this definition")
Convert given frame to  [wx.Image](wx.Image.html#wx-image).



Parameters
* **frame** (*int*) –
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def DoCanRead(self, stream: 'InputStream') -> bool:
        """ 

`DoCanRead`(*self*, *stream*)[¶](#wx.adv.GIFDecoder.DoCanRead "Permalink to this definition")
Checks the signature of the data in the given stream and returns `True` if it appears to be a valid animation format recognized by the animation decoder; this function should modify the stream current position without taking care of restoring it since [`CanRead`](wx.adv.AnimationDecoder.html#wx.adv.AnimationDecoder.CanRead "wx.adv.AnimationDecoder.CanRead") will do it.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetDelay(self, frame: int) -> int:
        """ 

`GetDelay`(*self*, *frame*)[¶](#wx.adv.GIFDecoder.GetDelay "Permalink to this definition")
Return the number of milliseconds this frame should be displayed.


If -1 is returned then the frame must be displayed forever.



Parameters
**frame** (*int*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetDisposalMethod(self, frame: int) -> 'AnimationDisposal':
        """ 

`GetDisposalMethod`(*self*, *frame*)[¶](#wx.adv.GIFDecoder.GetDisposalMethod "Permalink to this definition")
What should be done after displaying this frame.



Parameters
**frame** (*int*) – 



Return type
 [wx.adv.AnimationDisposal](wx.adv.AnimationDisposal.enumeration.html#wx-adv-animationdisposal)






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetFramePosition(self, frame: int) -> 'Point':
        """ 

`GetFramePosition`(*self*, *frame*)[¶](#wx.adv.GIFDecoder.GetFramePosition "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetFrameSize(self, frame: int) -> 'Size':
        """ 

`GetFrameSize`(*self*, *frame*)[¶](#wx.adv.GIFDecoder.GetFrameSize "Permalink to this definition")

Parameters
**frame** (*int*) – 



Return type
*Size*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetTransparentColour(self, frame: int) -> 'Colour':
        """ 

`GetTransparentColour`(*self*, *frame*)[¶](#wx.adv.GIFDecoder.GetTransparentColour "Permalink to this definition")
The transparent colour for this frame, if any, or `NullColour` .



Parameters
**frame** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def GetType(self) -> 'AnimationType':
        """ 

`GetType`(*self*)[¶](#wx.adv.GIFDecoder.GetType "Permalink to this definition")
Return the animation type this decoder implements.



Return type
 [wx.adv.AnimationType](wx.adv.AnimationType.enumeration.html#wx-adv-animationtype)






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    def Load(self, stream: 'InputStream') -> bool:
        """ 

`Load`(*self*, *stream*)[¶](#wx.adv.GIFDecoder.Load "Permalink to this definition")
Load the animation image frames from the given stream.



Parameters
**stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.adv.GIFDecoder.html
        """

    Type: 'AnimationType'  # `Type`[¶](#wx.adv.GIFDecoder.Type "Permalink to this definition")See [`GetType`](#wx.adv.GIFDecoder.GetType "wx.adv.GIFDecoder.GetType")



AnimationDisposal: TypeAlias = int  # Enumeration

ANIM_UNSPECIFIED: int

ANIM_DONOTREMOVE: int

ANIM_TOBACKGROUND: int

ANIM_TOPREVIOUS: int

EVT_CALENDAR_DAY: int

