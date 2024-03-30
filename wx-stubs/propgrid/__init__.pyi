# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import CommandEvent, Window, Size, VisualAttributes, Dialog, Validator, EvtHandler, Object, Colour, BitmapBundle, _Font, Font, ClientData, Bitmap, Panel, _ToolBar, ToolBar, TextCtrl, _StatusBar, Rect, Point, StatusBar, DateTime, LongLong_t, ObjectRefData

class PropertyGridEvent(CommandEvent):
    """ **Possible constructors**:



```
PropertyGridEvent(commandType=0, id=0)

PropertyGridEvent(event)

```


A property grid event holds information about events associated with
PropertyGrid objects.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, commandType=0, id=0)*


Constructor.



Parameters
* **commandType** (*wx.EventType*) –
* **id** (*int*) –






---

  



**\_\_init\_\_** *(self, event)*


Copy constructor.



Parameters
**event** ([*wx.propgrid.PropertyGridEvent*](#wx.propgrid.PropertyGridEvent "wx.propgrid.PropertyGridEvent")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def CanVeto(self) -> bool:
        """ 

`CanVeto`(*self*)[¶](#wx.propgrid.PropertyGridEvent.CanVeto "Permalink to this definition")
Returns `True` if you can veto the action that the event is signaling.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetColumn(self) -> int:
        """ 

`GetColumn`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetColumn "Permalink to this definition")
Returns the column index associated with this event.


For the column dragging events, it is the column to the left of the splitter being dragged



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetMainParent(self) -> 'PGProperty':
        """ 

`GetMainParent`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetMainParent "Permalink to this definition")
Returns highest level non-category, non-root parent of property for which event occurred.


Useful when you have nested properties with children.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


If immediate parent is root or category, this will return the property itself.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetProperty(self) -> 'PGProperty':
        """ 

`GetProperty`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetProperty "Permalink to this definition")
Returns property associated with this event.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


You should assume that this property can always be `None`. For instance, `wxEVT_PG_SELECTED` is emitted not only when a new property is selected, but also when selection is cleared by user activity.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetPropertyName(self) -> str:
        """ 

`GetPropertyName`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetPropertyName "Permalink to this definition")
Returns name of the associated property.



Return type
`string`





Note


Property name is stored in event, so it remains accessible even after the associated property or the property grid has been deleted.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetPropertyValue(self) -> 'PGVariant':
        """ 

`GetPropertyValue`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetPropertyValue "Permalink to this definition")
Returns value of the associated property.


Works for all event types, but for `wxEVT_PG_CHANGING` this member function returns the value that is pending, so you can call [`Veto`](#wx.propgrid.PropertyGridEvent.Veto "wx.propgrid.PropertyGridEvent.Veto") if the value is not satisfactory.



Return type
*PGVariant*





Note


Property value is stored in event, so it remains accessible even after the associated property or the property grid has been deleted.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetValidationFailureBehavior(self) -> 'byte':
        """ 

`GetValidationFailureBehavior`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetValidationFailureBehavior "Permalink to this definition")
Returns current validation failure flags.



Return type
*wx.byte*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def GetValue(self) -> 'PGVariant':
        """ 

`GetValue`(*self*)[¶](#wx.propgrid.PropertyGridEvent.GetValue "Permalink to this definition")
Returns value of the associated property.



Return type
*PGVariant*





See also


[`GetPropertyValue`](#wx.propgrid.PropertyGridEvent.GetPropertyValue "wx.propgrid.PropertyGridEvent.GetPropertyValue")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetCanVeto(self, canVeto: bool) -> None:
        """ 

`SetCanVeto`(*self*, *canVeto*)[¶](#wx.propgrid.PropertyGridEvent.SetCanVeto "Permalink to this definition")
Set if event can be vetoed.



Parameters
**canVeto** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetProperty(self, p: 'propgrid.PGProperty') -> None:
        """ 

`SetProperty`(*self*, *p*)[¶](#wx.propgrid.PropertyGridEvent.SetProperty "Permalink to this definition")
Changes the property associated with this event.



Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetValidationFailureBehavior(self, flags: 'byte') -> None:
        """ 

`SetValidationFailureBehavior`(*self*, *flags*)[¶](#wx.propgrid.PropertyGridEvent.SetValidationFailureBehavior "Permalink to this definition")
Set override validation failure behaviour.


Only effective if [`Veto`](#wx.propgrid.PropertyGridEvent.Veto "wx.propgrid.PropertyGridEvent.Veto") was also called, and only allowed if event type is `wxEVT_PG_CHANGING` .



Parameters
**flags** (*wx.byte*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def SetValidationFailureMessage(self, message: str) -> None:
        """ 

`SetValidationFailureMessage`(*self*, *message*)[¶](#wx.propgrid.PropertyGridEvent.SetValidationFailureMessage "Permalink to this definition")
Sets custom failure message for this time only.


Only applies if `PG_VFB_SHOW_MESSAGE` is set in validation failure flags.



Parameters
**message** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def Veto(self, veto: bool=True) -> None:
        """ 

`Veto`(*self*, *veto=True*)[¶](#wx.propgrid.PropertyGridEvent.Veto "Permalink to this definition")
Call this from your event handler to veto action that the event is signaling.


You can only veto a shutdown if [`wx.propgrid.PropertyGridEvent.CanVeto`](#wx.propgrid.PropertyGridEvent.CanVeto "wx.propgrid.PropertyGridEvent.CanVeto") returns `True`.



Parameters
**veto** (*bool*) – 





Note


Currently only `wxEVT_PG_CHANGING` supports vetoing.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    def WasVetoed(self) -> bool:
        """ 

`WasVetoed`(*self*)[¶](#wx.propgrid.PropertyGridEvent.WasVetoed "Permalink to this definition")
Returns `True` if event was vetoed.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridEvent.html
        """

    Column: int  # `Column`[¶](#wx.propgrid.PropertyGridEvent.Column "Permalink to this definition")See [`GetColumn`](#wx.propgrid.PropertyGridEvent.GetColumn "wx.propgrid.PropertyGridEvent.GetColumn")
    MainParent: 'PGProperty'  # `MainParent`[¶](#wx.propgrid.PropertyGridEvent.MainParent "Permalink to this definition")See [`GetMainParent`](#wx.propgrid.PropertyGridEvent.GetMainParent "wx.propgrid.PropertyGridEvent.GetMainParent")
    Property: 'PGProperty'  # `Property`[¶](#wx.propgrid.PropertyGridEvent.Property "Permalink to this definition")See [`GetProperty`](#wx.propgrid.PropertyGridEvent.GetProperty "wx.propgrid.PropertyGridEvent.GetProperty") and [`SetProperty`](#wx.propgrid.PropertyGridEvent.SetProperty "wx.propgrid.PropertyGridEvent.SetProperty")
    PropertyName: str  # `PropertyName`[¶](#wx.propgrid.PropertyGridEvent.PropertyName "Permalink to this definition")See [`GetPropertyName`](#wx.propgrid.PropertyGridEvent.GetPropertyName "wx.propgrid.PropertyGridEvent.GetPropertyName")
    PropertyValue: 'PGVariant'  # `PropertyValue`[¶](#wx.propgrid.PropertyGridEvent.PropertyValue "Permalink to this definition")See [`GetPropertyValue`](#wx.propgrid.PropertyGridEvent.GetPropertyValue "wx.propgrid.PropertyGridEvent.GetPropertyValue")
    ValidationFailureBehavior: 'byte'  # `ValidationFailureBehavior`[¶](#wx.propgrid.PropertyGridEvent.ValidationFailureBehavior "Permalink to this definition")See [`GetValidationFailureBehavior`](#wx.propgrid.PropertyGridEvent.GetValidationFailureBehavior "wx.propgrid.PropertyGridEvent.GetValidationFailureBehavior") and [`SetValidationFailureBehavior`](#wx.propgrid.PropertyGridEvent.SetValidationFailureBehavior "wx.propgrid.PropertyGridEvent.SetValidationFailureBehavior")
    Value: 'PGVariant'  # `Value`[¶](#wx.propgrid.PropertyGridEvent.Value "Permalink to this definition")See [`GetValue`](#wx.propgrid.PropertyGridEvent.GetValue "wx.propgrid.PropertyGridEvent.GetValue")



EVT_PG_SELECTED : int  # Respond to  wxEVT_PG_SELECTED   event, generated when a property selection has been changed, either by user action or by indirect program function. For instance, collapsing a parent property programmatically causes any selected child property to become unselected, and may therefore cause this event to be generated.

EVT_PG_CHANGED: int  # Respond to  wxEVT_PG_CHANGED   event, generated when property value has been changed by the user.

EVT_PG_CHANGING: int  # Respond to  wxEVT_PG_CHANGING   event, generated when property value is about to be changed by user. Use  wx.propgrid.PropertyGridEvent.GetValue   to take a peek at the pending value, and wx.propgrid.PropertyGridEvent.Veto   to prevent change from taking place, if necessary.

EVT_PG_HIGHLIGHTED: int  # Respond to  wxEVT_PG_HIGHLIGHTED   event, which occurs when mouse moves over a property. Event’s property is None if hovered area does not belong to any property.

EVT_PG_RIGHT_CLICK: int  # Respond to  wxEVT_PG_RIGHT_CLICK   event, which occurs when property is clicked on with right mouse button.

EVT_PG_DOUBLE_CLICK: int  # Respond to  wxEVT_PG_DOUBLE_CLICK   event, which occurs when property is double-clicked on with left mouse button.

EVT_PG_ITEM_COLLAPSED: int  # Respond to  wxEVT_PG_ITEM_COLLAPSED   event, generated when user collapses a property or category.

EVT_PG_ITEM_EXPANDED: int  # Respond to  wxEVT_PG_ITEM_EXPANDED   event, generated when user expands a property or category.

EVT_PG_LABEL_EDIT_BEGIN: int  # Respond to  wxEVT_PG_LABEL_EDIT_BEGIN   event, generated when user is about to begin editing a property label. You can veto this event to prevent the action.

EVT_PG_LABEL_EDIT_ENDING: int  # Respond to  wxEVT_PG_LABEL_EDIT_ENDING   event, generated when user is about to end editing of a property label. You can veto this event to prevent the action.

EVT_PG_COL_BEGIN_DRAG: int  # Respond to  wxEVT_PG_COL_BEGIN_DRAG   event, generated when user starts resizing a column - can be vetoed.

EVT_PG_COL_DRAGGING: int  # Respond to  wxEVT_PG_COL_DRAGGING , event, generated when a column resize by user is in progress. This event is also generated when user double-clicks the splitter in order to recenter it.

EVT_PG_COL_END_DRAG: int  # Respond to  wxEVT_PG_COL_END_DRAG   event, generated after column resize by user has finished. ^^

class PGMultiButton(Window):
    """ **Possible constructors**:



```
PGMultiButton(pg, sz)

```


This class can be used to have multiple buttons in a property editor.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
    """
    def __init__(self, pg, sz) -> None:
        """ 

`__init__`(*self*, *pg*, *sz*)[¶](#wx.propgrid.PGMultiButton.__init__ "Permalink to this definition")
Constructor.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def Add(self, *args, **kw) -> None:
        """ 

`Add`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGMultiButton.Add "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Add** *(self, label, id=-2)*


Adds new button, with given label.



Parameters
* **label** (*string*) –
* **id** (*int*) –






---

  



**Add** *(self, bitmap, id=-2)*


Adds new bitmap button.



Parameters
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **id** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def AddBitmapButton(self, bitmap, id=-2) -> None:
        """ 

`AddBitmapButton`(*self*, *bitmap*, *id=-2*)[¶](#wx.propgrid.PGMultiButton.AddBitmapButton "Permalink to this definition")
A simple wrapper around the PGMultiButton.Add method, for backwards compatibility.




            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def AddButton(self, label, id=-2) -> None:
        """ 

`AddButton`(*self*, *label*, *id=-2*)[¶](#wx.propgrid.PGMultiButton.AddButton "Permalink to this definition")
A simple wrapper around the PGMultiButton.Add method, for backwards compatibility.




            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def Finalize(self, propGrid, pos) -> None:
        """ 

`Finalize`(*self*, *propGrid*, *pos*)[¶](#wx.propgrid.PGMultiButton.Finalize "Permalink to this definition")
Call this in CreateControls() of your custom editor class after all buttons have been added.



Parameters
* **propGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) given in CreateControls().
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –  [wx.Point](wx.Point.html#wx-point) given in CreateControls().






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetButton(self, i: int) -> 'Window':
        """ 

`GetButton`(*self*, *i*)[¶](#wx.propgrid.PGMultiButton.GetButton "Permalink to this definition")
Returns pointer to one of the buttons.



Parameters
**i** (*int*) – 



Return type
*Window*






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetButtonId(self, i: int) -> int:
        """ 

`GetButtonId`(*self*, *i*)[¶](#wx.propgrid.PGMultiButton.GetButtonId "Permalink to this definition")
Returns Id of one of the buttons.


This is utility function to be used in event handlers.



Parameters
**i** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.propgrid.PGMultiButton.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.propgrid.PGMultiButton.GetCount "Permalink to this definition")
Returns number of buttons.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    def GetPrimarySize(self) -> 'Size':
        """ 

`GetPrimarySize`(*self*)[¶](#wx.propgrid.PGMultiButton.GetPrimarySize "Permalink to this definition")
Returns size of primary editor control, as appropriately reduced by number of buttons present.



Return type
`Size`






            Source: https://docs.wxpython.org/wx.propgrid.PGMultiButton.html
        """

    Count: int  # `Count`[¶](#wx.propgrid.PGMultiButton.Count "Permalink to this definition")See [`GetCount`](#wx.propgrid.PGMultiButton.GetCount "wx.propgrid.PGMultiButton.GetCount")
    PrimarySize: 'Size'  # `PrimarySize`[¶](#wx.propgrid.PGMultiButton.PrimarySize "Permalink to this definition")See [`GetPrimarySize`](#wx.propgrid.PGMultiButton.GetPrimarySize "wx.propgrid.PGMultiButton.GetPrimarySize")



class PGArrayEditorDialog(Dialog):
    """ **Possible constructors**:



```
PGArrayEditorDialog()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayGet(self, index: int) -> str:
        """ 

`ArrayGet`(*self*, *index*)[¶](#wx.propgrid.PGArrayEditorDialog.ArrayGet "Permalink to this definition")

Parameters
**index** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayGetCount(self) -> int:
        """ 

`ArrayGetCount`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.ArrayGetCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayInsert(self, str, index) -> bool:
        """ 

`ArrayInsert`(*self*, *str*, *index*)[¶](#wx.propgrid.PGArrayEditorDialog.ArrayInsert "Permalink to this definition")

Parameters
* **str** (*string*) –
* **index** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArrayRemoveAt(self, index: int) -> None:
        """ 

`ArrayRemoveAt`(*self*, *index*)[¶](#wx.propgrid.PGArrayEditorDialog.ArrayRemoveAt "Permalink to this definition")

Parameters
**index** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArraySet(self, index, str) -> bool:
        """ 

`ArraySet`(*self*, *index*, *str*)[¶](#wx.propgrid.PGArrayEditorDialog.ArraySet "Permalink to this definition")

Parameters
* **index** (*int*) –
* **str** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def ArraySwap(self, first, second) -> None:
        """ 

`ArraySwap`(*self*, *first*, *second*)[¶](#wx.propgrid.PGArrayEditorDialog.ArraySwap "Permalink to this definition")

Parameters
* **first** (*int*) –
* **second** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def Create(self, parent, message, caption, style=AEDIALOG_STYLE, pos=DefaultPosition, sz=DefaultSize) -> bool:
        """ 

`Create`(*self*, *parent*, *message*, *caption*, *style=AEDIALOG\_STYLE*, *pos=DefaultPosition*, *sz=DefaultSize*)[¶](#wx.propgrid.PGArrayEditorDialog.Create "Permalink to this definition")

Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **message** (*string*) –
* **caption** (*string*) –
* **style** (*long*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def EnableCustomNewAction(self) -> None:
        """ 

`EnableCustomNewAction`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.EnableCustomNewAction "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.propgrid.PGArrayEditorDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetDialogValue(self) -> 'PGVariant':
        """ 

`GetDialogValue`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.GetDialogValue "Permalink to this definition")
Return value modified by dialog.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetSelection(self) -> int:
        """ 

`GetSelection`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.GetSelection "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def GetTextCtrlValidator(self) -> 'Validator':
        """ 

`GetTextCtrlValidator`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.GetTextCtrlValidator "Permalink to this definition")
Override to return  [wx.Validator](wx.Validator.html#wx-validator) to be used with the  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) in dialog.


Note that the validator is used in the standard way, ie. it immediately prevents user from entering invalid input.



Return type
`Validator`





Note


Dialog frees the validator.





            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.Init "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def IsModified(self) -> bool:
        """ 

`IsModified`(*self*)[¶](#wx.propgrid.PGArrayEditorDialog.IsModified "Permalink to this definition")
Returns `True` if array was actually modified.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def OnCustomNewAction(self, resString: str) -> bool:
        """ 

`OnCustomNewAction`(*self*, *resString*)[¶](#wx.propgrid.PGArrayEditorDialog.OnCustomNewAction "Permalink to this definition")

Parameters
**resString** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def SetDialogValue(self, value: PGVariant) -> None:
        """ 

`SetDialogValue`(*self*, *value*)[¶](#wx.propgrid.PGArrayEditorDialog.SetDialogValue "Permalink to this definition")
Set value modified by dialog.



Parameters
**value** (*PGVariant*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    def SetNewButtonText(self, text: str) -> None:
        """ 

`SetNewButtonText`(*self*, *text*)[¶](#wx.propgrid.PGArrayEditorDialog.SetNewButtonText "Permalink to this definition")
Sets tooltip text for button allowing the user to enter new string.



Parameters
**text** (*string*) – 





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.propgrid.PGArrayEditorDialog.html
        """

    DialogValue: 'PGVariant'  # `DialogValue`[¶](#wx.propgrid.PGArrayEditorDialog.DialogValue "Permalink to this definition")See [`GetDialogValue`](#wx.propgrid.PGArrayEditorDialog.GetDialogValue "wx.propgrid.PGArrayEditorDialog.GetDialogValue") and [`SetDialogValue`](#wx.propgrid.PGArrayEditorDialog.SetDialogValue "wx.propgrid.PGArrayEditorDialog.SetDialogValue")
    Selection: int  # `Selection`[¶](#wx.propgrid.PGArrayEditorDialog.Selection "Permalink to this definition")See [`GetSelection`](#wx.propgrid.PGArrayEditorDialog.GetSelection "wx.propgrid.PGArrayEditorDialog.GetSelection")
    TextCtrlValidator: 'Validator'  # `TextCtrlValidator`[¶](#wx.propgrid.PGArrayEditorDialog.TextCtrlValidator "Permalink to this definition")See [`GetTextCtrlValidator`](#wx.propgrid.PGArrayEditorDialog.GetTextCtrlValidator "wx.propgrid.PGArrayEditorDialog.GetTextCtrlValidator")



class PropertyGridPage(EvtHandler,PropertyGridInterface,PropertyGridPageState):
    """ **Possible constructors**:



```
PropertyGridPage()

```


Holder of property grid page information.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PropertyGridPage.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PropertyGridPage.Clear "Permalink to this definition")
Deletes all properties on page.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def FitColumns(self) -> 'Size':
        """ 

`FitColumns`(*self*)[¶](#wx.propgrid.PropertyGridPage.FitColumns "Permalink to this definition")
Reduces column sizes to minimum possible that contents are still visibly (naturally some margin space will be applied as well).


Note that you can also get calculated column widths by calling [`GetColumnWidth`](wx.propgrid.PropertyGridPageState.html#wx.propgrid.PropertyGridPageState.GetColumnWidth "wx.propgrid.PropertyGridPageState.GetColumnWidth") immediately after this function returns.



Return type
*Size*



Returns
Returns minimum size for the page to still display everything.





Note


This function only works properly if size of containing grid was already fairly large.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetIndex(self) -> int:
        """ 

`GetIndex`(*self*)[¶](#wx.propgrid.PropertyGridPage.GetIndex "Permalink to this definition")
Returns page index in manager;.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetRoot(self) -> 'PGProperty':
        """ 

`GetRoot`(*self*)[¶](#wx.propgrid.PropertyGridPage.GetRoot "Permalink to this definition")
Returns “root property”.


It does not have name, etc. and it is not visible. It is only useful for accessing its children.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetSplitterPosition(self, col: int=0) -> int:
        """ 

`GetSplitterPosition`(*self*, *col=0*)[¶](#wx.propgrid.PropertyGridPage.GetSplitterPosition "Permalink to this definition")
Returns x-coordinate position of splitter on a page.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetStatePtr(self) -> 'PropertyGridPageState':
        """ 

`GetStatePtr`(*self*)[¶](#wx.propgrid.PropertyGridPage.GetStatePtr "Permalink to this definition")
Returns pointer to contained property grid state.



Return type
 [wx.propgrid.PropertyGridPageState](wx.propgrid.PropertyGridPageState.html#wx-propgrid-propertygridpagestate)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def GetToolId(self) -> int:
        """ 

`GetToolId`(*self*)[¶](#wx.propgrid.PropertyGridPage.GetToolId "Permalink to this definition")
Returns id of the tool bar item that represents this page on  [wx.propgrid.PropertyGridManager](wx.propgrid.PropertyGridManager.html#wx-propgrid-propertygridmanager)’s  [wx.ToolBar](wx.ToolBar.html#wx-toolbar).



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.propgrid.PropertyGridPage.Init "Permalink to this definition")
Do any member initialization in this method.



Note


* Called every time the page is added into a manager.
* You can add properties to the page here.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def IsHandlingAllEvents(self) -> bool:
        """ 

`IsHandlingAllEvents`(*self*)[¶](#wx.propgrid.PropertyGridPage.IsHandlingAllEvents "Permalink to this definition")
Return `False` here to indicate unhandled events should be propagated to manager’s parent, as normal.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def OnShow(self) -> None:
        """ 

`OnShow`(*self*)[¶](#wx.propgrid.PropertyGridPage.OnShow "Permalink to this definition")
Called every time page is about to be shown.


Useful, for instance, creating properties just-in-time.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ 

`RefreshProperty`(*self*, *p*)[¶](#wx.propgrid.PropertyGridPage.RefreshProperty "Permalink to this definition")
Refreshes given property on page.



Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    def SetSplitterPosition(self, splitterPos, col=0) -> None:
        """ 

`SetSplitterPosition`(*self*, *splitterPos*, *col=0*)[¶](#wx.propgrid.PropertyGridPage.SetSplitterPosition "Permalink to this definition")
Sets splitter position on page.



Parameters
* **splitterPos** (*int*) –
* **col** (*int*) –





Note


Splitter position cannot exceed grid size, and therefore setting it during form creation may fail as initial grid size is often smaller than desired splitter position, especially when sizers are being used.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPage.html
        """

    Index: int  # `Index`[¶](#wx.propgrid.PropertyGridPage.Index "Permalink to this definition")See [`GetIndex`](#wx.propgrid.PropertyGridPage.GetIndex "wx.propgrid.PropertyGridPage.GetIndex")
    Root: 'PGProperty'  # `Root`[¶](#wx.propgrid.PropertyGridPage.Root "Permalink to this definition")See [`GetRoot`](#wx.propgrid.PropertyGridPage.GetRoot "wx.propgrid.PropertyGridPage.GetRoot")
    SplitterPosition: int  # `SplitterPosition`[¶](#wx.propgrid.PropertyGridPage.SplitterPosition "Permalink to this definition")See [`GetSplitterPosition`](#wx.propgrid.PropertyGridPage.GetSplitterPosition "wx.propgrid.PropertyGridPage.GetSplitterPosition") and [`SetSplitterPosition`](#wx.propgrid.PropertyGridPage.SetSplitterPosition "wx.propgrid.PropertyGridPage.SetSplitterPosition")
    StatePtr: 'PropertyGridPageState'  # `StatePtr`[¶](#wx.propgrid.PropertyGridPage.StatePtr "Permalink to this definition")See [`GetStatePtr`](#wx.propgrid.PropertyGridPage.GetStatePtr "wx.propgrid.PropertyGridPage.GetStatePtr")
    ToolId: int  # `ToolId`[¶](#wx.propgrid.PropertyGridPage.ToolId "Permalink to this definition")See [`GetToolId`](#wx.propgrid.PropertyGridPage.GetToolId "wx.propgrid.PropertyGridPage.GetToolId")



class ColourPropertyValue(Object):
    """ **Possible constructors**:



```
ColourPropertyValue()

ColourPropertyValue(v)

ColourPropertyValue(colour)

ColourPropertyValue(type)

ColourPropertyValue(type, colour)

```


Because text, background and other colours tend to differ between
platforms, SystemColourProperty must be able to select between
system colour and, when necessary, to pick a custom one.


  


        Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.ColourPropertyValue.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, v)*



Parameters
**v** ([*wx.propgrid.ColourPropertyValue*](#wx.propgrid.ColourPropertyValue "wx.propgrid.ColourPropertyValue")) – 






---

  



**\_\_init\_\_** *(self, colour)*



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






---

  



**\_\_init\_\_** *(self, type)*



Parameters
**type** (*wx.int*) – 






---

  



**\_\_init\_\_** *(self, type, colour)*



Parameters
* **type** (*wx.int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
        """

    def Init(self, type, colour) -> None:
        """ 

`Init`(*self*, *type*, *colour*)[¶](#wx.propgrid.ColourPropertyValue.Init "Permalink to this definition")

Parameters
* **type** (*wx.int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.propgrid.ColourPropertyValue.html
        """

    m_colour: Any  # `m_colour`[¶](#wx.propgrid.ColourPropertyValue.m_colour "Permalink to this definition")A public C++ attribute of type [`Colour`](wx.Colour.html#wx.Colour "wx.Colour") . Resulting colour.
    m_type: Any  # `m_type`[¶](#wx.propgrid.ColourPropertyValue.m_type "Permalink to this definition")A public C++ attribute of type *int* . An integer value relating to the colour, and which exact meaning depends on the property with which it is used.



class PGCell(Object):
    """ **Possible constructors**:



```
PGCell()

PGCell(other)

PGCell(text, bitmap=BitmapBundle(), fgCol=NullColour, bgCol=NullColour)

```


Base class for PropertyGrid cell information.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGCell.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, other)*



Parameters
**other** ([*wx.propgrid.PGCell*](#wx.propgrid.PGCell "wx.propgrid.PGCell")) – 






---

  



**\_\_init\_\_** *(self, text, bitmap=BitmapBundle(), fgCol=NullColour, bgCol=NullColour)*



Parameters
* **text** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **fgCol** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **bgCol** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetBgCol(self) -> 'Colour':
        """ 

`GetBgCol`(*self*)[¶](#wx.propgrid.PGCell.GetBgCol "Permalink to this definition")

Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetBitmap(self) -> 'BitmapBundle':
        """ 

`GetBitmap`(*self*)[¶](#wx.propgrid.PGCell.GetBitmap "Permalink to this definition")

Return type
*BitmapBundle*






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetData(self) -> 'PGCellData':
        """ 

`GetData`(*self*)[¶](#wx.propgrid.PGCell.GetData "Permalink to this definition")

Return type
 [wx.propgrid.PGCellData](wx.propgrid.PGCellData.html#wx-propgrid-pgcelldata)






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetFgCol(self) -> 'Colour':
        """ 

`GetFgCol`(*self*)[¶](#wx.propgrid.PGCell.GetFgCol "Permalink to this definition")

Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.propgrid.PGCell.GetFont "Permalink to this definition")
Returns font of the cell.


If no specific font is set for this cell, then the font will be invalid.



Return type
[`Font`](#wx.propgrid.PGCell.Font "wx.propgrid.PGCell.Font")






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.propgrid.PGCell.GetText "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def HasText(self) -> bool:
        """ 

`HasText`(*self*)[¶](#wx.propgrid.PGCell.HasText "Permalink to this definition")
Returns `True` if this cell has custom text stored within.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def MergeFrom(self, srcCell: 'propgrid.PGCell') -> None:
        """ 

`MergeFrom`(*self*, *srcCell*)[¶](#wx.propgrid.PGCell.MergeFrom "Permalink to this definition")
Merges valid data from srcCell into this.



Parameters
**srcCell** ([*wx.propgrid.PGCell*](#wx.propgrid.PGCell "wx.propgrid.PGCell")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetBgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetBgCol`(*self*, *col*)[¶](#wx.propgrid.PGCell.SetBgCol "Permalink to this definition")

Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.propgrid.PGCell.SetBitmap "Permalink to this definition")

Parameters
**bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetEmptyData(self) -> None:
        """ 

`SetEmptyData`(*self*)[¶](#wx.propgrid.PGCell.SetEmptyData "Permalink to this definition")
Sets empty but valid data to this cell object.




            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetFgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetFgCol`(*self*, *col*)[¶](#wx.propgrid.PGCell.SetFgCol "Permalink to this definition")

Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.propgrid.PGCell.SetFont "Permalink to this definition")
Sets font of the cell.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 





Note


Because  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) does not support rows of different height, it makes little sense to change size of the font. Therefore it is recommended to use return value of `wx.propgrid.PropertyGrid.GetFont` or [`wx.propgrid.PropertyGrid.GetCaptionFont`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.GetCaptionFont "wx.propgrid.PropertyGrid.GetCaptionFont") as a basis for the font that, after modifications, is passed to this member function.





            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.propgrid.PGCell.SetText "Permalink to this definition")

Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCell.html
        """

    BgCol: 'Colour'  # `BgCol`[¶](#wx.propgrid.PGCell.BgCol "Permalink to this definition")See [`GetBgCol`](#wx.propgrid.PGCell.GetBgCol "wx.propgrid.PGCell.GetBgCol") and [`SetBgCol`](#wx.propgrid.PGCell.SetBgCol "wx.propgrid.PGCell.SetBgCol")
    Bitmap: 'BitmapBundle'  # `Bitmap`[¶](#wx.propgrid.PGCell.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.propgrid.PGCell.GetBitmap "wx.propgrid.PGCell.GetBitmap") and [`SetBitmap`](#wx.propgrid.PGCell.SetBitmap "wx.propgrid.PGCell.SetBitmap")
    Data: 'PGCellData'  # `Data`[¶](#wx.propgrid.PGCell.Data "Permalink to this definition")See [`GetData`](#wx.propgrid.PGCell.GetData "wx.propgrid.PGCell.GetData")
    FgCol: 'Colour'  # `FgCol`[¶](#wx.propgrid.PGCell.FgCol "Permalink to this definition")See [`GetFgCol`](#wx.propgrid.PGCell.GetFgCol "wx.propgrid.PGCell.GetFgCol") and [`SetFgCol`](#wx.propgrid.PGCell.SetFgCol "wx.propgrid.PGCell.SetFgCol")
    Font: '_Font'  # `Font`[¶](#wx.propgrid.PGCell.Font "Permalink to this definition")See [`GetFont`](#wx.propgrid.PGCell.GetFont "wx.propgrid.PGCell.GetFont") and [`SetFont`](#wx.propgrid.PGCell.SetFont "wx.propgrid.PGCell.SetFont")
    Text: str  # `Text`[¶](#wx.propgrid.PGCell.Text "Permalink to this definition")See [`GetText`](#wx.propgrid.PGCell.GetText "wx.propgrid.PGCell.GetText") and [`SetText`](#wx.propgrid.PGCell.SetText "wx.propgrid.PGCell.SetText")



class PGEditor(Object):
    """ **Possible constructors**:



```
PGEditor()

```


Base class for custom PropertyGrid editors.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGEditor.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def CanContainCustomImage(self) -> bool:
        """ 

`CanContainCustomImage`(*self*)[¶](#wx.propgrid.PGEditor.CanContainCustomImage "Permalink to this definition")
Returns `True` if control itself can contain the custom image.


Default implementation returns `False`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def DeleteItem(self, ctrl, index) -> None:
        """ 

`DeleteItem`(*self*, *ctrl*, *index*)[¶](#wx.propgrid.PGEditor.DeleteItem "Permalink to this definition")
Deletes item from existing control.


Default implementation does nothing.



Parameters
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **index** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def DrawValue(self, dc, rect, property, text) -> None:
        """ 

`DrawValue`(*self*, *dc*, *rect*, *property*, *text*)[¶](#wx.propgrid.PGEditor.DrawValue "Permalink to this definition")
Draws value for given property.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def GetValueFromControl(self, property, ctrl) -> tuple:
        """ 

`GetValueFromControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGEditor.GetValueFromControl "Permalink to this definition")
Returns value from control, via parameter *variant*.


Usually ends up calling property’s StringToValue() or IntToValue(). Returns `True` if value was different.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*tuple*



Returns
( *bool*, *variant* )






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def InsertItem(self, ctrl, label, index) -> int:
        """ 

`InsertItem`(*self*, *ctrl*, *label*, *index*)[¶](#wx.propgrid.PGEditor.InsertItem "Permalink to this definition")
Inserts item to existing control.


Index -1 means end of list. Default implementation does nothing. Returns index of item added.



Parameters
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **label** (*string*) –
* **index** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ 

`OnFocus`(*self*, *property*, *wnd*)[¶](#wx.propgrid.PGEditor.OnFocus "Permalink to this definition")
Extra processing when control gains focus.


For example,  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) based controls should select all text.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlAppearance(self, pg, property, ctrl, appearance, oldAppearance, unspecified) -> None:
        """ 

`SetControlAppearance`(*self*, *pg*, *property*, *ctrl*, *appearance*, *oldAppearance*, *unspecified*)[¶](#wx.propgrid.PGEditor.SetControlAppearance "Permalink to this definition")
Called by property grid to set new appearance for the control.


Default implementation sets foreground colour, background colour, font, plus text for  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboCtrl](wx.ComboCtrl.html#wx-comboctrl).



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid to which the edited property belongs.
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Edited property to which the editor control belongs.
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Editor control.
* **appearance** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) – New appearance to be applied.
* **oldAppearance** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) – Previously applied appearance. Used to detect which control attributes need to be changed (e.g. so we only change background colour if really needed).
* **unspecified** (*bool*) – If `True` tells this function that the new appearance represents an unspecified property value.






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ 

`SetControlIntValue`(*self*, *property*, *ctrl*, *value*)[¶](#wx.propgrid.PGEditor.SetControlIntValue "Permalink to this definition")
Sets control’s value specifically from int (applies to choice etc.).



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **value** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ 

`SetControlStringValue`(*self*, *property*, *ctrl*, *txt*)[¶](#wx.propgrid.PGEditor.SetControlStringValue "Permalink to this definition")
Sets control’s value specifically from string.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **txt** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ 

`SetValueToUnspecified`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGEditor.SetValueToUnspecified "Permalink to this definition")
Sets value in control to unspecified.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ 

`UpdateControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGEditor.UpdateControl "Permalink to this definition")
Loads value from property to the control.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGEditor.GetName "wx.propgrid.PGEditor.GetName")
    m_clientData: Any  # `m_clientData`[¶](#wx.propgrid.PGEditor.m_clientData "Permalink to this definition")A public C++ attribute of type [``](#id5)[``](#id7).



class PGEditorDialogAdapter(Object):
    """ **Possible constructors**:



```
PGEditorDialogAdapter()

```


Derive a class from this to adapt an existing editor dialog or
function to be used when editor button of a property is pushed.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGEditorDialogAdapter.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def DoShowDialog(self, propGrid, property) -> bool:
        """ 

`DoShowDialog`(*self*, *propGrid*, *property*)[¶](#wx.propgrid.PGEditorDialogAdapter.DoShowDialog "Permalink to this definition")

Parameters
* **propGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def GetValue(self) -> 'PGVariant':
        """ 

`GetValue`(*self*)[¶](#wx.propgrid.PGEditorDialogAdapter.GetValue "Permalink to this definition")
This method is typically only used if deriving class from existing adapter with value conversion purposes.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def SetValue(self, value: PGVariant) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.propgrid.PGEditorDialogAdapter.SetValue "Permalink to this definition")

Parameters
**value** (*PGVariant*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    def ShowDialog(self, propGrid, property) -> bool:
        """ 

`ShowDialog`(*self*, *propGrid*, *property*)[¶](#wx.propgrid.PGEditorDialogAdapter.ShowDialog "Permalink to this definition")

Parameters
* **propGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGEditorDialogAdapter.html
        """

    Value: 'PGVariant'  # `Value`[¶](#wx.propgrid.PGEditorDialogAdapter.Value "Permalink to this definition")See [`GetValue`](#wx.propgrid.PGEditorDialogAdapter.GetValue "wx.propgrid.PGEditorDialogAdapter.GetValue") and [`SetValue`](#wx.propgrid.PGEditorDialogAdapter.SetValue "wx.propgrid.PGEditorDialogAdapter.SetValue")
    m_clientData: Any  # `m_clientData`[¶](#wx.propgrid.PGEditorDialogAdapter.m_clientData "Permalink to this definition")A public C++ attribute of type [``](#id5)[``](#id7).



class PGProperty(Object):
    """ **Possible constructors**:



```
PGProperty()

PGProperty(label, name)

```


PGProperty is base class for all PropertyGrid properties and as
such it is not intended to be instantiated directly.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
    """
    def AdaptListToValue(self, list, value) -> None:
        """ 

`AdaptListToValue`(*self*, *list*, *value*)[¶](#wx.propgrid.PGProperty.AdaptListToValue "Permalink to this definition")
Adapts list variant into proper value using consecutive [`ChildChanged`](#wx.propgrid.PGProperty.ChildChanged "wx.propgrid.PGProperty.ChildChanged") calls.



Parameters
* **list** (*PGVariant*) –
* **value** (*PGVariant*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AddChoice(self, label, value=PG_INVALID_VALUE) -> int:
        """ 

`AddChoice`(*self*, *label*, *value=PG\_INVALID\_VALUE*)[¶](#wx.propgrid.PGProperty.AddChoice "Permalink to this definition")
Append a new choice to property’s list of choices.



Parameters
* **label** (*string*) – Label for added choice.
* **value** (*int*) – Value for new choice. Do not specify if you wish this to equal choice index.



Return type
*int*



Returns
Index to added choice.






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AddPrivateChild(self, prop: 'propgrid.PGProperty') -> None:
        """ 

`AddPrivateChild`(*self*, *prop*)[¶](#wx.propgrid.PGProperty.AddPrivateChild "Permalink to this definition")
Adds a private child property.


If you use this instead of [`wx.propgrid.PropertyGridInterface.Insert`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.Insert "wx.propgrid.PropertyGridInterface.Insert") or [`wx.propgrid.PropertyGridInterface.AppendIn`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.AppendIn "wx.propgrid.PropertyGridInterface.AppendIn") , then property’s parental type will automatically be set up to `PG_PROP_AGGREGATE`. In other words, all properties of this property will become private.



Parameters
**prop** ([*wx.propgrid.PGProperty*](#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AppendChild(self, childProperty: 'propgrid.PGProperty') -> 'PGProperty':
        """ 

`AppendChild`(*self*, *childProperty*)[¶](#wx.propgrid.PGProperty.AppendChild "Permalink to this definition")
Use this member function to add independent (i.e.


regular) children to a property.



Parameters
**childProperty** ([*wx.propgrid.PGProperty*](#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)



Returns
Appended childProperty.





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) is not automatically refreshed by this function.




See also


[`InsertChild`](#wx.propgrid.PGProperty.InsertChild "wx.propgrid.PGProperty.InsertChild") , [`AddPrivateChild`](#wx.propgrid.PGProperty.AddPrivateChild "wx.propgrid.PGProperty.AddPrivateChild")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AreAllChildrenSpecified(self, pendingList: Optional[PGVariant]=None) -> bool:
        """ 

`AreAllChildrenSpecified`(*self*, *pendingList=None*)[¶](#wx.propgrid.PGProperty.AreAllChildrenSpecified "Permalink to this definition")
Determines, recursively, if all children are not unspecified.



Parameters
**pendingList** (*PGVariant*) – Assumes members in this *Variant* list as pending replacement values.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def AreChildrenComponents(self) -> bool:
        """ 

`AreChildrenComponents`(*self*)[¶](#wx.propgrid.PGProperty.AreChildrenComponents "Permalink to this definition")
Returns `True` if children of this property are component values (for instance, points size, face name, and is\_underlined are component values of a font).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ChangeFlag(self, flag, set) -> None:
        """ 

`ChangeFlag`(*self*, *flag*, *set*)[¶](#wx.propgrid.PGProperty.ChangeFlag "Permalink to this definition")
Sets or clears given property flag.


Mainly for internal use.



Parameters
* **flag** ([*PGPropertyFlags*](wx.propgrid.PGPropertyFlags.enumeration.html "PGPropertyFlags")) –
* **set** (*bool*) –





Note


Setting a property flag never has any side-effect, and is intended almost exclusively for internal use. So, for example, if you want to disable a property, call



```
Enable(False)

```


instead of setting `PG_PROP_DISABLED` flag.




See also


[`HasFlag`](#wx.propgrid.PGProperty.HasFlag "wx.propgrid.PGProperty.HasFlag") , GetFlags()





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'PGVariant':
        """ 

`ChildChanged`(*self*, *thisValue*, *childIndex*, *childValue*)[¶](#wx.propgrid.PGProperty.ChildChanged "Permalink to this definition")
Called after value of a child property has been altered.


Must return new value of the whole property (after any alterations warranted by child’s new value).


Note that this function is usually called at the time that value of this property, or given child property, is still pending for change, and as such, result of [`GetValue`](#wx.propgrid.PGProperty.GetValue "wx.propgrid.PGProperty.GetValue") or m\_value should not be relied on.


Sample pseudo-code implementation:



```
# TBW

```



Parameters
* **thisValue** (*PGVariant*) – Value of this property. Changed value should be returned (in previous versions of  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) it was only necessary to write value back to this argument).
* **childIndex** (*int*) – Index of child changed (you can use Item(childIndex) to get child property).
* **childValue** (*PGVariant*) – (Pending) value of the child property.



Return type
*PGVariant*



Returns
Modified value of the whole property.






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DeleteChildren(self) -> None:
        """ 

`DeleteChildren`(*self*)[¶](#wx.propgrid.PGProperty.DeleteChildren "Permalink to this definition")
Deletes children of the property.




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DeleteChoice(self, index: int) -> None:
        """ 

`DeleteChoice`(*self*, *index*)[¶](#wx.propgrid.PGProperty.DeleteChoice "Permalink to this definition")
Removes entry from property’s  [wx.propgrid.PGChoices](wx.propgrid.PGChoices.html#wx-propgrid-pgchoices) and editor control (if it is active).


If selected item is deleted, then the value is set to unspecified.



Parameters
**index** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetAttribute(self, name: str) -> 'PGVariant':
        """ 

`DoGetAttribute`(*self*, *name*)[¶](#wx.propgrid.PGProperty.DoGetAttribute "Permalink to this definition")
Returns value of an attribute.


Override if custom handling of attributes is needed.


Default implementation simply return `None` variant.



Parameters
**name** (*string*) – 



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetEditorClass(self) -> 'PGEditor':
        """ 

`DoGetEditorClass`(*self*)[¶](#wx.propgrid.PGProperty.DoGetEditorClass "Permalink to this definition")
Returns pointer to an instance of used editor.



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.PGProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.PGProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](wx.propgrid.DirProperty.html#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoGetValue(self) -> 'PGVariant':
        """ 

`DoGetValue`(*self*)[¶](#wx.propgrid.PGProperty.DoGetValue "Permalink to this definition")
Override this to return something else than m\_value as the value.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.PGProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.propgrid.PGProperty.Enable "Permalink to this definition")
Enables or disables the property.


Disabled property usually appears as having grey text.



Parameters
**enable** (*bool*) – If `False`, property is disabled instead.





See also


[`wx.propgrid.PropertyGridInterface.EnableProperty`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.EnableProperty "wx.propgrid.PropertyGridInterface.EnableProperty")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def EnableCommonValue(self, enable: bool=True) -> None:
        """ 

`EnableCommonValue`(*self*, *enable=True*)[¶](#wx.propgrid.PGProperty.EnableCommonValue "Permalink to this definition")
Call to enable or disable usage of common value (integer value that can be selected for properties instead of their normal values) for this property.


Common values are disabled by the default for all properties.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GenerateComposedValue(self) -> str:
        """ 

`GenerateComposedValue`(*self*)[¶](#wx.propgrid.PGProperty.GenerateComposedValue "Permalink to this definition")
Composes text from values of child properties.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttribute(self, *args, **kw) -> 'PGVariant':
        """ 

`GetAttribute`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGProperty.GetAttribute "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetAttribute** *(self, name)*


Returns property attribute value, null variant if not found.



Parameters
**name** (*string*) – 



Return type
*PGVariant*





Note


For built-in attribute returns null variant if extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set.





---

  



**GetAttribute** *(self, name, defVal)*


Returns named attribute, as string, if found.


Otherwise *defVal* is returned.



Parameters
* **name** (*string*) –
* **defVal** (*string*) –



Return type
`string`





Note


For built-in attribute returns *defVal* if extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set.





---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributeAsDouble(self, name, defVal) -> float:
        """ 

`GetAttributeAsDouble`(*self*, *name*, *defVal*)[¶](#wx.propgrid.PGProperty.GetAttributeAsDouble "Permalink to this definition")
Returns named attribute, as double, if found.


Otherwise *defVal* is returned.



Parameters
* **name** (*string*) –
* **defVal** (*float*) –



Return type
*float*





Note


For built-in attribute returns *defVal* if extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributeAsLong(self, name, defVal) -> int:
        """ 

`GetAttributeAsLong`(*self*, *name*, *defVal*)[¶](#wx.propgrid.PGProperty.GetAttributeAsLong "Permalink to this definition")
Returns named attribute, as long, if found.


Otherwise *defVal* is returned.



Parameters
* **name** (*string*) –
* **defVal** (*long*) –



Return type
*long*





Note


For built-in attribute returns *defVal* if extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributes(self) -> Any:
        """ 

`GetAttributes`(*self*)[¶](#wx.propgrid.PGProperty.GetAttributes "Permalink to this definition")
Returns map-like storage of property’s attributes.



Return type
*PyObject*





Note


If extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set, then builtin-attributes are not included in the storage.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetAttributesAsList(self) -> 'PGVariant':
        """ 

`GetAttributesAsList`(*self*)[¶](#wx.propgrid.PGProperty.GetAttributesAsList "Permalink to this definition")
Returns attributes as list *Variant* .



Return type
*PGVariant*





Note


If extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set, then builtin-attributes are not included in the list.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetBaseName(self) -> str:
        """ 

`GetBaseName`(*self*)[¶](#wx.propgrid.PGProperty.GetBaseName "Permalink to this definition")
Returns property’s base name (i.e.


parent’s name is not added in any case).



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCell(self, column: int) -> 'PGCell':
        """ 

`GetCell`(*self*, *column*)[¶](#wx.propgrid.PGProperty.GetCell "Permalink to this definition")
Returns  [wx.propgrid.PGCell](wx.propgrid.PGCell.html#wx-propgrid-pgcell) of given column, creating one if necessary.



Parameters
**column** (*int*) – 



Return type
 [wx.propgrid.PGCell](wx.propgrid.PGCell.html#wx-propgrid-pgcell)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCellRenderer(self, column: int) -> 'PGCellRenderer':
        """ 

`GetCellRenderer`(*self*, *column*)[¶](#wx.propgrid.PGProperty.GetCellRenderer "Permalink to this definition")
Returns used  [wx.propgrid.PGCellRenderer](wx.propgrid.PGCellRenderer.html#wx-propgrid-pgcellrenderer) instance for given property column (label=0, value=1).


Default implementation returns editor’s renderer for all columns.



Parameters
**column** (*int*) – 



Return type
 [wx.propgrid.PGCellRenderer](wx.propgrid.PGCellRenderer.html#wx-propgrid-pgcellrenderer)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChildCount(self) -> int:
        """ 

`GetChildCount`(*self*)[¶](#wx.propgrid.PGProperty.GetChildCount "Permalink to this definition")
Returns number of child properties.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChildrenHeight(self, lh, iMax=-1) -> int:
        """ 

`GetChildrenHeight`(*self*, *lh*, *iMax=-1*)[¶](#wx.propgrid.PGProperty.GetChildrenHeight "Permalink to this definition")
Returns height of children, recursively, and by taking expanded/collapsed status into account.



Parameters
* **lh** (*int*) – Line height. Pass result of [`GetGrid`](#wx.propgrid.PGProperty.GetGrid "wx.propgrid.PGProperty.GetGrid") .GetRowHeight() here.
* **iMax** (*int*) – Only used (internally) when finding property y-positions.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ 

`GetChoiceSelection`(*self*)[¶](#wx.propgrid.PGProperty.GetChoiceSelection "Permalink to this definition")
Returns which choice is currently selected.


Only applies to properties which have choices.


Needs to reimplemented in derived class if property value does not map directly to a choice. Integer as index, bool, and string usually do.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetChoices(self) -> 'PGChoices':
        """ 

`GetChoices`(*self*)[¶](#wx.propgrid.PGProperty.GetChoices "Permalink to this definition")
Returns read-only reference to property’s list of choices.



Return type
 [wx.propgrid.PGChoices](wx.propgrid.PGChoices.html#wx-propgrid-pgchoices)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetClientData(self) -> 'ClientData':
        """ 

`GetClientData`(*self*)[¶](#wx.propgrid.PGProperty.GetClientData "Permalink to this definition")
Gets managed client object of a property.



Return type
*ClientData*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetClientObject(self, n) -> None:
        """ 

`GetClientObject`(*self*, *n*)[¶](#wx.propgrid.PGProperty.GetClientObject "Permalink to this definition")
Alias for [`GetClientData`](#wx.propgrid.PGProperty.GetClientData "wx.propgrid.PGProperty.GetClientData")




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetColumnEditor(self, column: int) -> 'PGEditor':
        """ 

`GetColumnEditor`(*self*, *column*)[¶](#wx.propgrid.PGProperty.GetColumnEditor "Permalink to this definition")
Returns editor used for given column.


`None` for no editor.



Parameters
**column** (*int*) – 



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetCommonValue(self) -> int:
        """ 

`GetCommonValue`(*self*)[¶](#wx.propgrid.PGProperty.GetCommonValue "Permalink to this definition")
Returns common value selected for this property.


-1 for none.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDefaultValue(self) -> 'PGVariant':
        """ 

`GetDefaultValue`(*self*)[¶](#wx.propgrid.PGProperty.GetDefaultValue "Permalink to this definition")
Returns property’s default value.


If property’s value type is not a built-in one, and “DefaultValue” attribute is not defined, then this function usually returns Null variant.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDepth(self) -> int:
        """ 

`GetDepth`(*self*)[¶](#wx.propgrid.PGProperty.GetDepth "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDisplayedCommonValueCount(self) -> int:
        """ 

`GetDisplayedCommonValueCount`(*self*)[¶](#wx.propgrid.PGProperty.GetDisplayedCommonValueCount "Permalink to this definition")
Return number of displayed common values for this property.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetDisplayedString(self) -> str:
        """ 

`GetDisplayedString`(*self*)[¶](#wx.propgrid.PGProperty.GetDisplayedString "Permalink to this definition")
Returns property’s displayed text.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetEditorClass(self) -> 'PGEditor':
        """ 

`GetEditorClass`(*self*)[¶](#wx.propgrid.PGProperty.GetEditorClass "Permalink to this definition")
Returns  [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor) that will be used and created when property becomes selected.


Returns more accurate value than [`DoGetEditorClass`](#wx.propgrid.PGProperty.DoGetEditorClass "wx.propgrid.PGProperty.DoGetEditorClass") .



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetEditorDialog(self) -> 'PGEditorDialogAdapter':
        """ 

`GetEditorDialog`(*self*)[¶](#wx.propgrid.PGProperty.GetEditorDialog "Permalink to this definition")
Returns instance of a new  [wx.propgrid.PGEditorDialogAdapter](wx.propgrid.PGEditorDialogAdapter.html#wx-propgrid-pgeditordialogadapter) instance, which is used when user presses the (optional) button next to the editor control;.


Default implementation returns `None` (i.e. no action is generated when button is pressed).



Return type
 [wx.propgrid.PGEditorDialogAdapter](wx.propgrid.PGEditorDialogAdapter.html#wx-propgrid-pgeditordialogadapter)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetFlagsAsString(self, flagsMask: FlagType) -> str:
        """ 

`GetFlagsAsString`(*self*, *flagsMask*)[¶](#wx.propgrid.PGProperty.GetFlagsAsString "Permalink to this definition")
Gets flags as a’|’ delimited string.


Note that flag names are not prepended with ‘wx``PG\_PROP\_``’.



Parameters
**flagsMask** (*FlagType*) – String will only be made to include flags combined by this parameter.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetGrid(self) -> 'PropertyGrid':
        """ 

`GetGrid`(*self*)[¶](#wx.propgrid.PGProperty.GetGrid "Permalink to this definition")
Returns property grid where property lies.



Return type
 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetGridIfDisplayed(self) -> 'PropertyGrid':
        """ 

`GetGridIfDisplayed`(*self*)[¶](#wx.propgrid.PGProperty.GetGridIfDisplayed "Permalink to this definition")
Returns owner  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), but only if one is currently on a page displaying this property.



Return type
 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetHelpString(self) -> str:
        """ 

`GetHelpString`(*self*)[¶](#wx.propgrid.PGProperty.GetHelpString "Permalink to this definition")
Returns property’s help or description text.



Return type
`string`





See also


[`SetHelpString`](#wx.propgrid.PGProperty.SetHelpString "wx.propgrid.PGProperty.SetHelpString")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetHintText(self) -> str:
        """ 

`GetHintText`(*self*)[¶](#wx.propgrid.PGProperty.GetHintText "Permalink to this definition")
Returns property’s hint text (shown in empty value cell).



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetImageOffset(self, imageWidth: int) -> int:
        """ 

`GetImageOffset`(*self*, *imageWidth*)[¶](#wx.propgrid.PGProperty.GetImageOffset "Permalink to this definition")
Converts image width into full image offset, with margins.



Parameters
**imageWidth** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetIndexInParent(self) -> int:
        """ 

`GetIndexInParent`(*self*)[¶](#wx.propgrid.PGProperty.GetIndexInParent "Permalink to this definition")
Returns position in parent’s array.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetItemAtY(self, y: int) -> 'PGProperty':
        """ 

`GetItemAtY`(*self*, *y*)[¶](#wx.propgrid.PGProperty.GetItemAtY "Permalink to this definition")
Returns property at given virtual y coordinate.



Parameters
**y** (*int*) – 



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetLabel(self) -> str:
        """ 

`GetLabel`(*self*)[¶](#wx.propgrid.PGProperty.GetLabel "Permalink to this definition")
Returns property’s label.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetLastVisibleSubItem(self) -> 'PGProperty':
        """ 

`GetLastVisibleSubItem`(*self*)[¶](#wx.propgrid.PGProperty.GetLastVisibleSubItem "Permalink to this definition")
Returns last visible child property, recursively.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetMainParent(self) -> 'PGProperty':
        """ 

`GetMainParent`(*self*)[¶](#wx.propgrid.PGProperty.GetMainParent "Permalink to this definition")
Returns highest level non-category, non-root parent.


Useful when you have nested properties with children.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)





Note


If immediate parent is root or category, this will return the property itself.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetMaxLength(self) -> int:
        """ 

`GetMaxLength`(*self*)[¶](#wx.propgrid.PGProperty.GetMaxLength "Permalink to this definition")
Returns maximum allowed length of the text the user can enter in the property text editor.



Return type
*int*





Note


0 is returned if length is not explicitly limited and the text can be as long as it is supported by the underlying native text control widget.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGProperty.GetName "Permalink to this definition")
Returns property’s name with all (non-category, non-root) parents.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetOrCreateCell(self, column: int) -> 'PGCell':
        """ 

`GetOrCreateCell`(*self*, *column*)[¶](#wx.propgrid.PGProperty.GetOrCreateCell "Permalink to this definition")
Returns  [wx.propgrid.PGCell](wx.propgrid.PGCell.html#wx-propgrid-pgcell) of given column, creating one if necessary.



Parameters
**column** (*int*) – 



Return type
 [wx.propgrid.PGCell](wx.propgrid.PGCell.html#wx-propgrid-pgcell)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetParent(self) -> 'PGProperty':
        """ 

`GetParent`(*self*)[¶](#wx.propgrid.PGProperty.GetParent "Permalink to this definition")
Return parent of property.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetPropertyByName(self, name: str) -> 'PGProperty':
        """ 

`GetPropertyByName`(*self*, *name*)[¶](#wx.propgrid.PGProperty.GetPropertyByName "Permalink to this definition")
Returns (direct) child property with given name (or `None` if not found).



Parameters
**name** (*string*) – Name of the child property to look for.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValidator(self) -> 'Validator':
        """ 

`GetValidator`(*self*)[¶](#wx.propgrid.PGProperty.GetValidator "Permalink to this definition")
Gets assignable version of property’s validator.



Return type
*Validator*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValue(self) -> 'PGVariant':
        """ 

`GetValue`(*self*)[¶](#wx.propgrid.PGProperty.GetValue "Permalink to this definition")
Returns property’s value.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueAsString(self, argFlags: int=0) -> str:
        """ 

`GetValueAsString`(*self*, *argFlags=0*)[¶](#wx.propgrid.PGProperty.GetValueAsString "Permalink to this definition")
Returns text representation of property’s value.



Parameters
**argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


In older versions, this function used to be overridden to convert property’s value into a string representation. This function is now handled by [`ValueToString`](#wx.propgrid.PGProperty.ValueToString "wx.propgrid.PGProperty.ValueToString") , and overriding this function now will result in run-time assertion failure.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueImage(self) -> 'Bitmap':
        """ 

`GetValueImage`(*self*)[¶](#wx.propgrid.PGProperty.GetValueImage "Permalink to this definition")
Returns bitmap that appears next to value text.


Only returns not `None` bitmap if one was set with [`SetValueImage`](#wx.propgrid.PGProperty.SetValueImage "wx.propgrid.PGProperty.SetValueImage") .



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetValueType(self) -> str:
        """ 

`GetValueType`(*self*)[¶](#wx.propgrid.PGProperty.GetValueType "Permalink to this definition")
Returns value type used by this property.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def GetY(self) -> int:
        """ 

`GetY`(*self*)[¶](#wx.propgrid.PGProperty.GetY "Permalink to this definition")
Returns coordinate to the top y of the property.


Note that the position of scrollbars is not taken into account.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasFlag(self, flag: PGPropertyFlags) -> bool:
        """ 

`HasFlag`(*self*, *flag*)[¶](#wx.propgrid.PGProperty.HasFlag "Permalink to this definition")
Returns `True` if property has given flag set.



Parameters
**flag** ([*PGPropertyFlags*](wx.propgrid.PGPropertyFlags.enumeration.html "PGPropertyFlags")) – 



Return type
*bool*





See also


propgrid\_propflags





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasFlagsExact(self, flags: FlagType) -> bool:
        """ 

`HasFlagsExact`(*self*, *flags*)[¶](#wx.propgrid.PGProperty.HasFlagsExact "Permalink to this definition")
Returns `True` if property has all given flags set.



Parameters
**flags** (*FlagType*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def HasVisibleChildren(self) -> bool:
        """ 

`HasVisibleChildren`(*self*)[¶](#wx.propgrid.PGProperty.HasVisibleChildren "Permalink to this definition")
Returns `True` if property has even one visible child.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Hide(self, hide, flags=PG_RECURSE) -> bool:
        """ 

`Hide`(*self*, *hide*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PGProperty.Hide "Permalink to this definition")
Hides or reveals the property.



Parameters
* **hide** (*bool*) – `True` for hide, `False` for reveal.
* **flags** (*int*) – By default changes are applied recursively. Set this parameter to `PG_DONT_RECURSE` to prevent this.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Index(self, p: 'propgrid.PGProperty') -> int:
        """ 

`Index`(*self*, *p*)[¶](#wx.propgrid.PGProperty.Index "Permalink to this definition")
Returns index of given child property.


`wx.NOT_FOUND` if given property is not child of this.



Parameters
**p** ([*wx.propgrid.PGProperty*](#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def InsertChild(self, index, childProperty) -> 'PGProperty':
        """ 

`InsertChild`(*self*, *index*, *childProperty*)[¶](#wx.propgrid.PGProperty.InsertChild "Permalink to this definition")
Use this member function to add independent (i.e.


regular) children to a property.



Parameters
* **index** (*int*) –
* **childProperty** ([*wx.propgrid.PGProperty*](#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)



Returns
Inserted childProperty.





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) is not automatically refreshed by this function.




See also


[`AppendChild`](#wx.propgrid.PGProperty.AppendChild "wx.propgrid.PGProperty.AppendChild") , [`AddPrivateChild`](#wx.propgrid.PGProperty.AddPrivateChild "wx.propgrid.PGProperty.AddPrivateChild")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def InsertChoice(self, label, index, value=PG_INVALID_VALUE) -> int:
        """ 

`InsertChoice`(*self*, *label*, *index*, *value=PG\_INVALID\_VALUE*)[¶](#wx.propgrid.PGProperty.InsertChoice "Permalink to this definition")
Inserts a new choice to property’s list of choices.



Parameters
* **label** (*string*) – Text for new choice
* **index** (*int*) – Insertion position. Use `wx.NOT_FOUND` to append.
* **value** (*int*) – Value for new choice. Do not specify if you wish this to equal choice index.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.PGProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsCategory(self) -> bool:
        """ 

`IsCategory`(*self*)[¶](#wx.propgrid.PGProperty.IsCategory "Permalink to this definition")
Returns `True` if this property is actually a  [wx.propgrid.PropertyCategory](wx.propgrid.PropertyCategory.html#wx-propgrid-propertycategory).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsEnabled(self) -> bool:
        """ 

`IsEnabled`(*self*)[¶](#wx.propgrid.PGProperty.IsEnabled "Permalink to this definition")
Returns `True` if property is enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsExpanded(self) -> bool:
        """ 

`IsExpanded`(*self*)[¶](#wx.propgrid.PGProperty.IsExpanded "Permalink to this definition")
Returns `True` if property has visible children.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsRoot(self) -> bool:
        """ 

`IsRoot`(*self*)[¶](#wx.propgrid.PGProperty.IsRoot "Permalink to this definition")
Returns `True` if this property is actually a RootProperty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsSomeParent(self, candidateParent: 'propgrid.PGProperty') -> bool:
        """ 

`IsSomeParent`(*self*, *candidateParent*)[¶](#wx.propgrid.PGProperty.IsSomeParent "Permalink to this definition")
Returns `True` if candidateParent is some parent of this property.


Use, for example, to detect if item is inside collapsed section.



Parameters
**candidateParent** ([*wx.propgrid.PGProperty*](#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsSubProperty(self) -> bool:
        """ 

`IsSubProperty`(*self*)[¶](#wx.propgrid.PGProperty.IsSubProperty "Permalink to this definition")
Returns `True` if this is a sub-property.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsTextEditable(self) -> bool:
        """ 

`IsTextEditable`(*self*)[¶](#wx.propgrid.PGProperty.IsTextEditable "Permalink to this definition")
Returns `True` if property has editable  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) when selected.



Return type
*bool*





Note


Although disabled properties do not displayed editor, they still return `True` here as being disabled is considered a temporary condition (unlike being read-only or having limited editing enabled).





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsValueUnspecified(self) -> bool:
        """ 

`IsValueUnspecified`(*self*)[¶](#wx.propgrid.PGProperty.IsValueUnspecified "Permalink to this definition")
Returns `True` if property’s value is considered unspecified.


This usually means that value is Null variant.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def IsVisible(self) -> bool:
        """ 

`IsVisible`(*self*)[¶](#wx.propgrid.PGProperty.IsVisible "Permalink to this definition")
Returns `True` if all parents expanded.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Item(self, i: int) -> 'PGProperty':
        """ 

`Item`(*self*, *i*)[¶](#wx.propgrid.PGProperty.Item "Permalink to this definition")
Returns child property at index *i*.



Parameters
**i** (*int*) – 



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def Last(self) -> 'PGProperty':
        """ 

`Last`(*self*)[¶](#wx.propgrid.PGProperty.Last "Permalink to this definition")
Returns last sub-property.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ 

`OnCustomPaint`(*self*, *dc*, *rect*, *paintdata*)[¶](#wx.propgrid.PGProperty.OnCustomPaint "Permalink to this definition")
Override to paint an image in front of the property value text or drop-down list item (but only if [`wx.propgrid.PGProperty.OnMeasureImage`](#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") is overridden as well).


If property’s [`OnMeasureImage`](#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") returns size that has height != 0 but less than row height ( < 0 has special meanings),  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) calls this method to draw a custom image in a limited area in front of the editor control or value text/graphics, and if control has drop-down list, then the image is drawn there as well (even in the case [`OnMeasureImage`](#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") returned higher height than row height).


`NOTE`: Following applies when [`OnMeasureImage`](#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") returns a “flexible” height ( using `PG_FLEXIBLE_SIZE(W,H)` macro), which implies variable height items: If (rect.x+rect.width) is < 0, then this is a measure item call, which means that dc is invalid and only thing that should be done is to set paintdata.m\_drawnHeight to the height of the image of item at index paintdata.m\_choiceItem. This call may be done even as often as once every drop-down popup show.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for custom graphics. Includes surrounding rectangle, if any. If x+width is < 0, then this is a measure item call (see above).
* **paintdata** ([*wx.propgrid.PGPaintData*](wx.propgrid.PGPaintData.html#wx.propgrid.PGPaintData "wx.propgrid.PGPaintData")) –  [wx.propgrid.PGPaintData](wx.propgrid.PGPaintData.html#wx-propgrid-pgpaintdata) structure with much useful data about painted item.





Note


* You can actually exceed rect width, but if you do so then paintdata.m\_drawnWidth must be set to the full width drawn in pixels.
* Due to technical reasons, rect’s height will be default even if custom height was reported during measure call.
* Brush is guaranteed to be default background colour. It has been already used to clear the background of area being painted. It can be modified.
* Pen is guaranteed to be 1-wide ‘black’ (or whatever is the proper colour) pen for drawing framing rectangle. It can be changed as well.




See also


[`ValueToString`](#wx.propgrid.PGProperty.ValueToString "wx.propgrid.PGProperty.ValueToString")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnEvent(self, propgrid, wnd_primary, event) -> None:
        """ 

`OnEvent`(*self*, *propgrid*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGProperty.OnEvent "Permalink to this definition")
Events received by editor widgets are processed here.


Note that editor class usually processes most events. Some, such as button press events of TextCtrlAndButton class, can be handled here. Also, if custom handling for regular events is desired, then that can also be done (for example,  [wx.propgrid.SystemColourProperty](wx.propgrid.SystemColourProperty.html#wx-propgrid-systemcolourproperty) custom handles `wxEVT_CHOICE` to display colour picker dialog when ‘custom’ selection is made).


If the event causes value to be changed, [`SetValueInEvent`](#wx.propgrid.PGProperty.SetValueInEvent "wx.propgrid.PGProperty.SetValueInEvent") should be called to set the new value.


The parameter *event* is the associated  [wx.Event](wx.Event.html#wx-event).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –




return `True` if any changes in value should be reported.



Return type
*bool*





Note


* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnMeasureImage(self, item: int=-1) -> 'Size':
        """ 

`OnMeasureImage`(*self*, *item=-1*)[¶](#wx.propgrid.PGProperty.OnMeasureImage "Permalink to this definition")
Returns size of the custom painted image in front of property.


This method must be overridden to return non-default value if OnCustomPaint is to be called.



Parameters
**item** (*int*) – Normally -1, but can be an index to the property’s list of items.



Return type
*Size*





Note


* Default behaviour is to return  [wx.Size](wx.Size.html#wx-size), which means no image.
* Default image width or height is indicated with dimension -1.
* You can also return `PG_DEFAULT_IMAGE_SIZE` which equals DefaultSize.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.PGProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.PGProperty.OnSetValue "wx.propgrid.PGProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.PGProperty.OnSetValue "wx.propgrid.PGProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def OnValidationFailure(self, pendingValue: PGVariant) -> None:
        """ 

`OnValidationFailure`(*self*, *pendingValue*)[¶](#wx.propgrid.PGProperty.OnValidationFailure "Permalink to this definition")
Called whenever validation has failed with given pending value.



Parameters
**pendingValue** (*PGVariant*) – 





Note


If you implement this in your custom property class, please remember to call the base implementation as well, since they may use it to revert property into pre-change state.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RecreateEditor(self) -> bool:
        """ 

`RecreateEditor`(*self*)[¶](#wx.propgrid.PGProperty.RecreateEditor "Permalink to this definition")
If property’s editor is created this forces its recreation.


Useful in SetAttribute etc. Returns `True` if actually did anything.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RefreshChildren(self) -> None:
        """ 

`RefreshChildren`(*self*)[¶](#wx.propgrid.PGProperty.RefreshChildren "Permalink to this definition")
Refresh values of child properties.


Automatically called after value is set.




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def RefreshEditor(self) -> None:
        """ 

`RefreshEditor`(*self*)[¶](#wx.propgrid.PGProperty.RefreshEditor "Permalink to this definition")
If property’s editor is active, then update it’s value.




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAttribute(self, name, value) -> None:
        """ 

`SetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.PGProperty.SetAttribute "Permalink to this definition")
Sets an attribute for this property.



Parameters
* **name** (*string*) – Text identifier of attribute. See PropertyGrid Property Attribute Identifiers.
* **value** (*PGVariant*) – Value of attribute.





Note


Setting attribute’s value to Null variant will simply remove it from property’s set of attributes.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAttributes(self, attributes) -> None:
        """ 

`SetAttributes`(*self*, *attributes*)[¶](#wx.propgrid.PGProperty.SetAttributes "Permalink to this definition")
Set the property’s attributes from a Python dictionary.




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetAutoUnspecified(self, enable: bool=True) -> None:
        """ 

`SetAutoUnspecified`(*self*, *enable=True*)[¶](#wx.propgrid.PGProperty.SetAutoUnspecified "Permalink to this definition")
Set if user can change the property’s value to unspecified by modifying the value of the editor control (usually by clearing it).


Currently, this can work with following properties:  [wx.propgrid.IntProperty](wx.propgrid.IntProperty.html#wx-propgrid-intproperty),  [wx.propgrid.UIntProperty](wx.propgrid.UIntProperty.html#wx-propgrid-uintproperty),  [wx.propgrid.FloatProperty](wx.propgrid.FloatProperty.html#wx-propgrid-floatproperty),  [wx.propgrid.EditEnumProperty](wx.propgrid.EditEnumProperty.html#wx-propgrid-editenumproperty).



Parameters
**enable** (*bool*) – Whether to enable or disable this behaviour (it is disabled by default).






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetBackgroundColour(self, colour, flags=PG_RECURSE) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PGProperty.SetBackgroundColour "Permalink to this definition")
Sets property’s background colour.



Parameters
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – Background colour to use.
* **flags** (*int*) – Default is `PG_RECURSE` which causes colour to be set recursively. Omit this flag to only set colour for the property in question and not any of its children.





Note


Unlike [`wx.propgrid.PropertyGridInterface.SetPropertyBackgroundColour`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetPropertyBackgroundColour "wx.propgrid.PropertyGridInterface.SetPropertyBackgroundColour") , this does not automatically update the display.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetCell(self, column, cell) -> None:
        """ 

`SetCell`(*self*, *column*, *cell*)[¶](#wx.propgrid.PGProperty.SetCell "Permalink to this definition")
Sets cell information for given column.



Parameters
* **column** (*int*) –
* **cell** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetChoiceSelection(self, newValue: int) -> None:
        """ 

`SetChoiceSelection`(*self*, *newValue*)[¶](#wx.propgrid.PGProperty.SetChoiceSelection "Permalink to this definition")
Sets selected choice and changes property value.


Tries to retain value type, although currently if it is not string, then it is forced to integer.



Parameters
**newValue** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetChoices(self, choices: 'propgrid.PGChoices') -> bool:
        """ 

`SetChoices`(*self*, *choices*)[¶](#wx.propgrid.PGProperty.SetChoices "Permalink to this definition")
Sets new set of choices for the property.



Parameters
**choices** ([*wx.propgrid.PGChoices*](wx.propgrid.PGChoices.html#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) – 



Return type
*bool*





Note


This operation deselects the property and clears its value.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetClientData(self, data: ClientData) -> None:
        """ 

`SetClientData`(*self*, *data*)[¶](#wx.propgrid.PGProperty.SetClientData "Permalink to this definition")
Sets client object of a property.



Parameters
**data** (*ClientData*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetClientObject(self, n, data) -> None:
        """ 

`SetClientObject`(*self*, *n*, *data*)[¶](#wx.propgrid.PGProperty.SetClientObject "Permalink to this definition")
Alias for [`SetClientData`](#wx.propgrid.PGProperty.SetClientData "wx.propgrid.PGProperty.SetClientData")




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetCommonValue(self, commonValue: int) -> None:
        """ 

`SetCommonValue`(*self*, *commonValue*)[¶](#wx.propgrid.PGProperty.SetCommonValue "Permalink to this definition")
Sets common value selected for this property.


-1 for none.



Parameters
**commonValue** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetDefaultColours(self, flags: int=PG_RECURSE) -> None:
        """ 

`SetDefaultColours`(*self*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PGProperty.SetDefaultColours "Permalink to this definition")
Sets property’s default text and background colours.



Parameters
**flags** (*int*) – Default is `PG_RECURSE` which causes colours to be set recursively. Omit this flag to only set colours for the property in question and not any of its children.





New in version 4.1/wxWidgets-3.1.0.




Note


Unlike [`wx.propgrid.PropertyGridInterface.SetPropertyColoursToDefault`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetPropertyColoursToDefault "wx.propgrid.PropertyGridInterface.SetPropertyColoursToDefault") , this does not automatically update the display.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetDefaultValue(self, value: PGVariant) -> None:
        """ 

`SetDefaultValue`(*self*, *value*)[¶](#wx.propgrid.PGProperty.SetDefaultValue "Permalink to this definition")
Set default value of a property.


Synonymous to



```
theProperty.SetAttribute("DefaultValue", value)

```



Parameters
**value** (*PGVariant*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetEditor(self, *args, **kw) -> None:
        """ 

`SetEditor`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGProperty.SetEditor "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetEditor** *(self, editor)*


Sets editor for a property.



Parameters
**editor** ([*wx.propgrid.PGEditor*](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor "wx.propgrid.PGEditor")) – For builtin editors, use PGEditor\_X, where X is builtin editor’s name (TextCtrl, Choice, etc. see  [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor) documentation for full list).




[`wx.propgrid.PropertyGrid.RegisterEditorClass`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.RegisterEditorClass "wx.propgrid.PropertyGrid.RegisterEditorClass") .




---

  



**SetEditor** *(self, editorName)*


Sets editor for a property, by editor name.



Parameters
**editorName** (*string*) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetExpanded(self, expanded: bool) -> None:
        """ 

`SetExpanded`(*self*, *expanded*)[¶](#wx.propgrid.PGProperty.SetExpanded "Permalink to this definition")

Parameters
**expanded** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetFlagRecursively(self, flag, set) -> None:
        """ 

`SetFlagRecursively`(*self*, *flag*, *set*)[¶](#wx.propgrid.PGProperty.SetFlagRecursively "Permalink to this definition")
Sets or clears given property flag, recursively.


This function is primarily intended for internal use.



Parameters
* **flag** ([*PGPropertyFlags*](wx.propgrid.PGPropertyFlags.enumeration.html "PGPropertyFlags")) –
* **set** (*bool*) –





See also


[`ChangeFlag`](#wx.propgrid.PGProperty.ChangeFlag "wx.propgrid.PGProperty.ChangeFlag")





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetFlagsFromString(self, str: str) -> None:
        """ 

`SetFlagsFromString`(*self*, *str*)[¶](#wx.propgrid.PGProperty.SetFlagsFromString "Permalink to this definition")
Sets flags from a ‘|’ delimited string.


Note that flag names are not prepended with ‘wx``PG\_PROP\_``’.



Parameters
**str** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetHelpString(self, helpString: str) -> None:
        """ 

`SetHelpString`(*self*, *helpString*)[¶](#wx.propgrid.PGProperty.SetHelpString "Permalink to this definition")
Sets property’s help string, which is shown, for example, in  [wx.propgrid.PropertyGridManager](wx.propgrid.PropertyGridManager.html#wx-propgrid-propertygridmanager)’s description text box.



Parameters
**helpString** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.propgrid.PGProperty.SetLabel "Permalink to this definition")
Sets property’s label.



Parameters
**label** (*string*) – 





Note


* Properties under same parent may have same labels. However, property names must still remain unique.
* Unlike [`wx.propgrid.PropertyGridInterface.SetPropertyLabel`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetPropertyLabel "wx.propgrid.PropertyGridInterface.SetPropertyLabel") , this does not automatically update the display.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetMaxLength(self, maxLen: int) -> bool:
        """ 

`SetMaxLength`(*self*, *maxLen*)[¶](#wx.propgrid.PGProperty.SetMaxLength "Permalink to this definition")
Set maximum length of the text the user can enter in the text editor.


If it is 0, the length is not limited and the text can be as long as it is supported by the underlying native text control widget.



Parameters
**maxLen** (*int*) – 



Return type
*bool*



Returns
Returns `True` if maximum length was set.






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetModifiedStatus(self, modified: bool) -> None:
        """ 

`SetModifiedStatus`(*self*, *modified*)[¶](#wx.propgrid.PGProperty.SetModifiedStatus "Permalink to this definition")
Sets property’s “is it modified?” flag.


Affects children recursively.



Parameters
**modified** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetName(self, newName: str) -> None:
        """ 

`SetName`(*self*, *newName*)[¶](#wx.propgrid.PGProperty.SetName "Permalink to this definition")
Sets new (base) name for property.



Parameters
**newName** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetParentalType(self, flag: int) -> None:
        """ 

`SetParentalType`(*self*, *flag*)[¶](#wx.propgrid.PGProperty.SetParentalType "Permalink to this definition")
Changes what sort of parent this property is for its children.



Parameters
**flag** (*int*) – Use one of the following values: `PG_PROP_MISC_PARENT` (for generic parents), `PG_PROP_CATEGORY` (for categories), or `PG_PROP_AGGREGATE` (for derived property classes with private children).





Note


You generally do not need to call this function.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetTextColour(self, colour, flags=PG_RECURSE) -> None:
        """ 

`SetTextColour`(*self*, *colour*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PGProperty.SetTextColour "Permalink to this definition")
Sets property’s text colour.



Parameters
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – Text colour to use.
* **flags** (*int*) – Default is `PG_RECURSE` which causes colour to be set recursively. Omit this flag to only set colour for the property in question and not any of its children.





Note


Unlike [`wx.propgrid.PropertyGridInterface.SetPropertyTextColour`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetPropertyTextColour "wx.propgrid.PropertyGridInterface.SetPropertyTextColour") , this does not automatically update the display.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValidator(self, validator: 'Validator') -> None:
        """ 

`SetValidator`(*self*, *validator*)[¶](#wx.propgrid.PGProperty.SetValidator "Permalink to this definition")
Sets  [wx.Validator](wx.Validator.html#wx-validator) for a property.



Parameters
**validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValue(self, value, pList=None, flags=PG_SETVAL_REFRESH_EDITOR) -> None:
        """ 

`SetValue`(*self*, *value*, *pList=None*, *flags=PG\_SETVAL\_REFRESH\_EDITOR*)[¶](#wx.propgrid.PGProperty.SetValue "Permalink to this definition")
Call this to set value of the property.


Unlike methods in  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), this does not automatically update the display.


If you need to change property value in event, based on user input, use [`SetValueInEvent`](#wx.propgrid.PGProperty.SetValueInEvent "wx.propgrid.PGProperty.SetValueInEvent") instead.



Parameters
* **value** (*PGVariant*) – The value to set.
* **pList** (*PGVariant*) – Pointer to list variant that contains child values. Used to indicate which children should be marked as modified. Usually you just use `None`.
* **flags** (*int*) – `PG_SETVAL_REFRESH_EDITOR` is set by default, to refresh editor and redraw properties.





Note


Use [`wx.propgrid.PropertyGrid.ChangePropertyValue`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.ChangePropertyValue "wx.propgrid.PropertyGrid.ChangePropertyValue") instead if you need to run through validation process and send property change event.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueFromInt(self, value, flags=0) -> bool:
        """ 

`SetValueFromInt`(*self*, *value*, *flags=0*)[¶](#wx.propgrid.PGProperty.SetValueFromInt "Permalink to this definition")
Converts integer to a value, and if successful, calls [`SetValue`](#wx.propgrid.PGProperty.SetValue "wx.propgrid.PGProperty.SetValue") on it.


Default behaviour is to do nothing.



Parameters
* **value** (*long*) – Int to get the value from.
* **flags** (*int*) – If has `PG_FULL_VALUE`, then the value given is an actual value and not an index.



Return type
*bool*



Returns
`True` if value was changed.






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueFromString(self, text, flags=PG_PROGRAMMATIC_VALUE) -> bool:
        """ 

`SetValueFromString`(*self*, *text*, *flags=PG\_PROGRAMMATIC\_VALUE*)[¶](#wx.propgrid.PGProperty.SetValueFromString "Permalink to this definition")
Converts string to a value, and if successful, calls [`SetValue`](#wx.propgrid.PGProperty.SetValue "wx.propgrid.PGProperty.SetValue") on it.


Default behaviour is to do nothing.



Parameters
* **text** (*string*) – String to get the value from.
* **flags** (*int*) – If `PG_FULL_VALUE` is set, the function sets complete, storable value instead of displayable one (they may be different). `PG_PROGRAMMATIC_VALUE` flag is used to indicate that value is being set programmatically (i.e. operation is not caused by user input). If `PG_REPORT_ERROR` is set, a special action should be performed if string couldn’t have been successfully converted to the valid value (e.g. a special value can be set in this case).



Return type
*bool*



Returns
`True` if value was changed.






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueImage(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetValueImage`(*self*, *bmp*)[¶](#wx.propgrid.PGProperty.SetValueImage "Permalink to this definition")
Set  [wx.Bitmap](wx.Bitmap.html#wx-bitmap) taken from  [wx.BitmapBundle](wx.BitmapBundle.html#wx-bitmapbundle) in front of the value.


This bitmap may be ignored by custom cell renderers.



Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueInEvent(self, value: PGVariant) -> None:
        """ 

`SetValueInEvent`(*self*, *value*)[¶](#wx.propgrid.PGProperty.SetValueInEvent "Permalink to this definition")
Call this function in [`OnEvent`](#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") , OnButtonClick() etc.


to change the property value based on user input.



Parameters
**value** (*PGVariant*) – 





Note


This method is since it doesn’t actually modify value, but posts given variant as pending value, stored in  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid).





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetValueToUnspecified(self) -> None:
        """ 

`SetValueToUnspecified`(*self*)[¶](#wx.propgrid.PGProperty.SetValueToUnspecified "Permalink to this definition")
Sets property’s value to unspecified (i.e.


Null variant).




            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def SetWasModified(self, set: bool=True) -> None:
        """ 

`SetWasModified`(*self*, *set=True*)[¶](#wx.propgrid.PGProperty.SetWasModified "Permalink to this definition")
Call with `False` in [`OnSetValue`](#wx.propgrid.PGProperty.OnSetValue "wx.propgrid.PGProperty.OnSetValue") to cancel value changes after all (i.e.


cancel `True` returned by [`StringToValue`](#wx.propgrid.PGProperty.StringToValue "wx.propgrid.PGProperty.StringToValue") or [`IntToValue`](#wx.propgrid.PGProperty.IntToValue "wx.propgrid.PGProperty.IntToValue") ).



Parameters
**set** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.PGProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.PGProperty.ValueToString "wx.propgrid.PGProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def UpdateParentValues(self) -> 'PGProperty':
        """ 

`UpdateParentValues`(*self*)[¶](#wx.propgrid.PGProperty.UpdateParentValues "Permalink to this definition")
Updates composed values of parent non-category properties, recursively.


Returns topmost property updated.



Return type
 [wx.propgrid.PGProperty](#wx-propgrid-pgproperty)





Note


Must not call [`SetValue`](#wx.propgrid.PGProperty.SetValue "wx.propgrid.PGProperty.SetValue") (as can be called in it).





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def UsesAutoUnspecified(self) -> bool:
        """ 

`UsesAutoUnspecified`(*self*)[¶](#wx.propgrid.PGProperty.UsesAutoUnspecified "Permalink to this definition")
Returns `True` if containing grid uses `PG_EX_AUTO_UNSPECIFIED_VALUES`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ 

`ValidateValue`(*self*, *value*, *validationInfo*)[¶](#wx.propgrid.PGProperty.ValidateValue "Permalink to this definition")
Implement this function in derived class to check the value.


Return `True` if it is ok. Returning `False` prevents property change events from occurring.



Parameters
* **value** (*PGVariant*) –
* **validationInfo** ([*wx.propgrid.PGValidationInfo*](wx.propgrid.PGValidationInfo.html#wx.propgrid.PGValidationInfo "wx.propgrid.PGValidationInfo")) –



Return type
*bool*





Note


* Default implementation always returns `True`.





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.PGProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


It is protected because  [wx.propgrid.PGProperty](#wx-propgrid-pgproperty) is only a base class for other property classes.




---

  



**\_\_init\_\_** *(self, label, name)*


Constructor.


It is protected because  [wx.propgrid.PGProperty](#wx-propgrid-pgproperty) is only a base class for other property classes. Non-abstract property classes should have constructor of this style:



```
class MyProperty(wx.propgrid.PGProperty):
    def __init__(self, label, name, value):
        wx.propgrid.PGProperty.__init__(self, label, name)
        self.SetValue(value)

```



Parameters
* **label** (*string*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGProperty.html
        """

    m_clientData: Any  # `m_clientData`[¶](#wx.propgrid.PGProperty.m_clientData "Permalink to this definition")A public C++ attribute of type [``](#id5)[``](#id7). This member is public so scripting language bindings wrapper code can access it freely.
    m_value: Any  # `m_value`[¶](#wx.propgrid.PGProperty.m_value "Permalink to this definition")See [`GetValue`](#wx.propgrid.PGProperty.GetValue "wx.propgrid.PGProperty.GetValue") and [`SetValue`](#wx.propgrid.PGProperty.SetValue "wx.propgrid.PGProperty.SetValue")



NOT_FOUND: int

class PropertyGridManager(Panel,PropertyGridInterface):
    """ **Possible constructors**:



```
PropertyGridManager()

PropertyGridManager(parent, id=ID_ANY, pos=DefaultPosition,
                    size=DefaultSize, style=PGMAN_DEFAULT_STYLE,
                    name=PropertyGridManagerNameStr)

```


PropertyGridManager is an efficient multi-page version of
PropertyGrid, which can optionally have toolbar for mode and page
selection, a help text box, and a header.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridManager.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Two step constructor.


Call Create when this constructor is called to build up the  [wx.propgrid.PropertyGridManager](#wx-propgrid-propertygridmanager).




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=PGMAN\_DEFAULT\_STYLE, name=PropertyGridManagerNameStr)*


The default constructor.


The styles to be used are styles valid for the  [wx.Window](wx.Window.html#wx-window).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –





See also


PropertyGrid Window Styles





---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def AddPage(*args, **kwargs) -> 'PropertyGridPage':
        """ 

`AddPage`(*self*, *label=""*, *bmp=BitmapBundle()*, *pageObj=None*)[¶](#wx.propgrid.PropertyGridManager.AddPage "Permalink to this definition")
Creates new property page.


Note that the first page is not created automatically.



Parameters
* **label** (*string*) – A label for the page. This may be shown as a toolbar tooltip etc.
* **bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – Bitmap bundle for toolbar image. If the bundle is empty, then a built-in default bitmap bundle is used.
* **pageObj** ([*wx.propgrid.PropertyGridPage*](wx.propgrid.PropertyGridPage.html#wx.propgrid.PropertyGridPage "wx.propgrid.PropertyGridPage")) –  [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage) instance. Manager will take ownership of this object. `None` indicates that a default page instance should be created.



Return type
 [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage)



Returns
Returns pointer to created property grid page.





Note


If toolbar is used, it is highly recommended that the pages are added when the toolbar is not turned off using window style flag switching. Otherwise toolbar buttons might not be added properly.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PropertyGridManager.Clear "Permalink to this definition")
Deletes all properties and all pages.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def ClearPage(self, page: int) -> None:
        """ 

`ClearPage`(*self*, *page*)[¶](#wx.propgrid.PropertyGridManager.ClearPage "Permalink to this definition")
Deletes all properties on given page.



Parameters
**page** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def CommitChangesFromEditor(self, flags: 'int'=0) -> bool:
        """ 

`CommitChangesFromEditor`(*self*, *flags=0*)[¶](#wx.propgrid.PropertyGridManager.CommitChangesFromEditor "Permalink to this definition")
Forces updating the value of property from the editor control.



Parameters
**flags** (*wx.int*) – 



Return type
*bool*



Returns
Returns `True` if value was actually updated.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=PGMAN_DEFAULT_STYLE, name=PropertyGridManagerNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=PGMAN\_DEFAULT\_STYLE*, *name=PropertyGridManagerNameStr*)[¶](#wx.propgrid.PropertyGridManager.Create "Permalink to this definition")
Two step creation.


Whenever the control is created without any parameters, use Create to actually create it. Don’t access the control’s public methods before this is called.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*





See also


PropertyGrid Window Styles





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def CreatePropertyGrid(self) -> 'PropertyGrid':
        """ 

`CreatePropertyGrid`(*self*)[¶](#wx.propgrid.PropertyGridManager.CreatePropertyGrid "Permalink to this definition")
Creates property grid for the manager.


Reimplement in derived class to use subclassed  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid). However, if you do this then you must also use the two-step construction (i.e. default constructor and [`Create`](#wx.propgrid.PropertyGridManager.Create "wx.propgrid.PropertyGridManager.Create") instead of constructor with arguments) when creating the manager.



Return type
 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ 

`EnableCategories`(*self*, *enable*)[¶](#wx.propgrid.PropertyGridManager.EnableCategories "Permalink to this definition")
Enables or disables (shows/hides) categories according to parameter enable.



Parameters
**enable** (*bool*) – 



Return type
*bool*





Note


Calling this may not properly update toolbar buttons.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def EnsureVisible(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`EnsureVisible`(*self*, *id*)[¶](#wx.propgrid.PropertyGridManager.EnsureVisible "Permalink to this definition")
Selects page, scrolls and/or expands items to ensure that the given item is visible.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*



Returns
Returns `True` if something was actually done.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.propgrid.PropertyGridManager.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetColumnCount(self, page: int=-1) -> int:
        """ 

`GetColumnCount`(*self*, *page=-1*)[¶](#wx.propgrid.PropertyGridManager.GetColumnCount "Permalink to this definition")
Returns number of columns on given page.


By the default, returns number of columns on current page.



Parameters
**page** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetCurrentPage(self) -> 'PropertyGridPage':
        """ 

`GetCurrentPage`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetCurrentPage "Permalink to this definition")
Returns currently selected page.



Return type
 [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetDescBoxHeight(self) -> int:
        """ 

`GetDescBoxHeight`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetDescBoxHeight "Permalink to this definition")
Returns height of the description text box.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetGrid(self) -> 'PropertyGrid':
        """ 

`GetGrid`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetGrid "Permalink to this definition")
Returns pointer to the contained  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid).


This does not change after  [wx.propgrid.PropertyGridManager](#wx-propgrid-propertygridmanager) has been created, so you can safely obtain pointer once and use it for the entire lifetime of the manager instance.



Return type
 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPage(self, *args, **kw) -> 'PropertyGridPage':
        """ 

`GetPage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridManager.GetPage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetPage** *(self, ind)*


Returns page object for given page index.



Parameters
**ind** (*int*) – 



Return type
 [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage)






---

  



**GetPage** *(self, name)*


Returns page object for given page name.



Parameters
**name** (*string*) – 



Return type
 [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageByName(self, name: str) -> int:
        """ 

`GetPageByName`(*self*, *name*)[¶](#wx.propgrid.PropertyGridManager.GetPageByName "Permalink to this definition")
Returns index for a page name.


If no match is found, `wx.NOT_FOUND` is returned.



Parameters
**name** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageByState(self, pstate: 'propgrid.PropertyGridPageState') -> int:
        """ 

`GetPageByState`(*self*, *pstate*)[¶](#wx.propgrid.PropertyGridManager.GetPageByState "Permalink to this definition")
Returns index for a relevant propertygrid state.


If no match is found, `wx.NOT_FOUND` is returned.



Parameters
**pstate** ([*wx.propgrid.PropertyGridPageState*](wx.propgrid.PropertyGridPageState.html#wx.propgrid.PropertyGridPageState "wx.propgrid.PropertyGridPageState")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageCount(self) -> int:
        """ 

`GetPageCount`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetPageCount "Permalink to this definition")
Returns number of managed pages.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageName(self, index: int) -> str:
        """ 

`GetPageName`(*self*, *index*)[¶](#wx.propgrid.PropertyGridManager.GetPageName "Permalink to this definition")
Returns name of given page.



Parameters
**index** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetPageRoot(self, index: int) -> 'PGProperty':
        """ 

`GetPageRoot`(*self*, *index*)[¶](#wx.propgrid.PropertyGridManager.GetPageRoot "Permalink to this definition")
Returns “root property” of the given page.


It does not have name, etc. and it is not visible. It is only useful for accessing its children.



Parameters
**index** (*int*) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelectedPage(self) -> int:
        """ 

`GetSelectedPage`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetSelectedPage "Permalink to this definition")
Returns index to currently selected page.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelectedProperty(self) -> 'PGProperty':
        """ 

`GetSelectedProperty`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetSelectedProperty "Permalink to this definition")
Alias for [`GetSelection`](#wx.propgrid.PropertyGridManager.GetSelection "wx.propgrid.PropertyGridManager.GetSelection") .



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetSelection(self) -> 'PGProperty':
        """ 

`GetSelection`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetSelection "Permalink to this definition")
Shortcut for [`GetGrid`](#wx.propgrid.PropertyGridManager.GetGrid "wx.propgrid.PropertyGridManager.GetGrid") . [`GetSelection`](#wx.propgrid.PropertyGridManager.GetSelection "wx.propgrid.PropertyGridManager.GetSelection") .



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetToolBar(self) -> 'ToolBar':
        """ 

`GetToolBar`(*self*)[¶](#wx.propgrid.PropertyGridManager.GetToolBar "Permalink to this definition")
Returns a pointer to the toolbar currently associated with the  [wx.propgrid.PropertyGridManager](#wx-propgrid-propertygridmanager) (if any).



Return type
[`ToolBar`](#wx.propgrid.PropertyGridManager.ToolBar "wx.propgrid.PropertyGridManager.ToolBar")






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def GetVIterator(self, flags: int) -> 'PGVIterator':
        """ 

`GetVIterator`(*self*, *flags*)[¶](#wx.propgrid.PropertyGridManager.GetVIterator "Permalink to this definition")
Similar to [`GetIterator`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.GetIterator "wx.propgrid.PropertyGridInterface.GetIterator") , but instead returns  [wx.propgrid.PGVIterator](wx.propgrid.PGVIterator.html#wx-propgrid-pgviterator) instance, which can be useful for forward-iterating through arbitrary property containers.



Parameters
**flags** (*int*) – 



Return type
 [wx.propgrid.PGVIterator](wx.propgrid.PGVIterator.html#wx-propgrid-pgviterator)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def InsertPage(*args, **kwargs) -> 'PropertyGridPage':
        """ 

`InsertPage`(*self*, *index*, *label*, *bmp=BitmapBundle()*, *pageObj=None*)[¶](#wx.propgrid.PropertyGridManager.InsertPage "Permalink to this definition")
Creates new property page.


Note that the first page is not created automatically.



Parameters
* **index** (*int*) – Add to this position. -1 will add as the last item.
* **label** (*string*) – A label for the page. This may be shown as a toolbar tooltip etc.
* **bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – Bitmap bundle for toolbar image. If the bundle is empty, then a built-in default bitmap bundle is used.
* **pageObj** ([*wx.propgrid.PropertyGridPage*](wx.propgrid.PropertyGridPage.html#wx.propgrid.PropertyGridPage "wx.propgrid.PropertyGridPage")) –  [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage) instance. Manager will take ownership of this object. If `None`, default page object is constructed.



Return type
 [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage)



Returns
Returns pointer to created page.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsAnyModified(self) -> bool:
        """ 

`IsAnyModified`(*self*)[¶](#wx.propgrid.PropertyGridManager.IsAnyModified "Permalink to this definition")
Returns `True` if any property on any page has been modified by the user.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsPageModified(self, index: int) -> bool:
        """ 

`IsPageModified`(*self*, *index*)[¶](#wx.propgrid.PropertyGridManager.IsPageModified "Permalink to this definition")
Returns `True` if any property on given page has been modified by the user.



Parameters
**index** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def IsPropertySelected(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertySelected`(*self*, *id*)[¶](#wx.propgrid.PropertyGridManager.IsPropertySelected "Permalink to this definition")
Returns `True` if property is selected.


Since selection is page based, this function checks every page in the manager.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def RemovePage(self, page: int) -> bool:
        """ 

`RemovePage`(*self*, *page*)[¶](#wx.propgrid.PropertyGridManager.RemovePage "Permalink to this definition")
Removes a page.



Parameters
**page** (*int*) – 



Return type
*bool*



Returns
Returns `False` if it was not possible to remove page in question.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SelectPage(self, *args, **kw) -> None:
        """ 

`SelectPage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridManager.SelectPage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SelectPage** *(self, index)*


Select and displays a given page.



Parameters
**index** (*int*) – Index of page being selected. Can be -1 to select nothing.






---

  



**SelectPage** *(self, label)*


Select and displays a given page (by label).



Parameters
**label** (*string*) – 






---

  



**SelectPage** *(self, page)*


Select and displays a given page.



Parameters
**page** ([*wx.propgrid.PropertyGridPage*](wx.propgrid.PropertyGridPage.html#wx.propgrid.PropertyGridPage "wx.propgrid.PropertyGridPage")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SelectProperty(self, id, focus=False) -> bool:
        """ 

`SelectProperty`(*self*, *id*, *focus=False*)[¶](#wx.propgrid.PropertyGridManager.SelectProperty "Permalink to this definition")
Select a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **focus** (*bool*) –



Return type
*bool*





See also


[`wx.propgrid.PropertyGrid.SelectProperty`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.SelectProperty "wx.propgrid.PropertyGrid.SelectProperty") , [`wx.propgrid.PropertyGridInterface.ClearSelection`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.ClearSelection "wx.propgrid.PropertyGridInterface.ClearSelection")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetColumnCount(self, colCount, page=-1) -> None:
        """ 

`SetColumnCount`(*self*, *colCount*, *page=-1*)[¶](#wx.propgrid.PropertyGridManager.SetColumnCount "Permalink to this definition")
Sets number of columns on given page (default is current page).



Parameters
* **colCount** (*int*) –
* **page** (*int*) –





Note


If you use header, then you should always use this member function to set the column count, instead of ones present in  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) or  [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage).





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetColumnTitle(self, idx, title) -> None:
        """ 

`SetColumnTitle`(*self*, *idx*, *title*)[¶](#wx.propgrid.PropertyGridManager.SetColumnTitle "Permalink to this definition")
Sets a column title.


Default title for column 0 is “Property”, and “Value” for column 1.



Parameters
* **idx** (*int*) –
* **title** (*string*) –





Note


If header is not shown yet, then calling this member function will make it visible.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetDescBoxHeight(self, ht, refresh=True) -> None:
        """ 

`SetDescBoxHeight`(*self*, *ht*, *refresh=True*)[¶](#wx.propgrid.PropertyGridManager.SetDescBoxHeight "Permalink to this definition")
Sets y coordinate of the description box splitter.



Parameters
* **ht** (*int*) –
* **refresh** (*bool*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetDescription(self, label, content) -> None:
        """ 

`SetDescription`(*self*, *label*, *content*)[¶](#wx.propgrid.PropertyGridManager.SetDescription "Permalink to this definition")
Sets label and text in description box.



Parameters
* **label** (*string*) –
* **content** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetPageSplitterLeft(self, page, subProps=False) -> None:
        """ 

`SetPageSplitterLeft`(*self*, *page*, *subProps=False*)[¶](#wx.propgrid.PropertyGridManager.SetPageSplitterLeft "Permalink to this definition")
Moves splitter as left as possible on an individual page, while still allowing all labels to be shown in full.



Parameters
* **page** (*int*) –
* **subProps** (*bool*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetPageSplitterPosition(self, page, pos, column=0) -> None:
        """ 

`SetPageSplitterPosition`(*self*, *page*, *pos*, *column=0*)[¶](#wx.propgrid.PropertyGridManager.SetPageSplitterPosition "Permalink to this definition")
Sets splitter position on individual page.



Parameters
* **page** (*int*) –
* **pos** (*int*) –
* **column** (*int*) –





Note


If you use header, then you should always use this member function to set the splitter position, instead of ones present in  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) or  [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage).





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetSplitterLeft(self, subProps=False, allPages=True) -> None:
        """ 

`SetSplitterLeft`(*self*, *subProps=False*, *allPages=True*)[¶](#wx.propgrid.PropertyGridManager.SetSplitterLeft "Permalink to this definition")
Moves splitter as left as possible, while still allowing all labels to be shown in full.



Parameters
* **subProps** (*bool*) – If `False`, will still allow sub-properties (i.e. properties which parent is not root or category) to be cropped.
* **allPages** (*bool*) – If `True`, takes labels on all pages into account.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def SetSplitterPosition(self, pos, column=0) -> None:
        """ 

`SetSplitterPosition`(*self*, *pos*, *column=0*)[¶](#wx.propgrid.PropertyGridManager.SetSplitterPosition "Permalink to this definition")
Sets splitter position for all pages.


If you use header, then you should always use this member function to set the splitter position, instead of ones present in  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) or  [wx.propgrid.PropertyGridPage](wx.propgrid.PropertyGridPage.html#wx-propgrid-propertygridpage).



Parameters
* **pos** (*int*) –
* **column** (*int*) –





Note


Splitter position cannot exceed grid size, and therefore setting it during form creation may fail as initial grid size is often smaller than desired splitter position, especially when sizers are being used.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    def ShowHeader(self, show: bool=True) -> None:
        """ 

`ShowHeader`(*self*, *show=True*)[¶](#wx.propgrid.PropertyGridManager.ShowHeader "Permalink to this definition")
Show or hide the property grid header control.


It is hidden by the default.



Parameters
**show** (*bool*) – 





Note


Grid may look better if you use `PG_NO_INTERNAL_BORDER` window style when showing a header.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridManager.html
        """

    ColumnCount: int  # `ColumnCount`[¶](#wx.propgrid.PropertyGridManager.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.propgrid.PropertyGridManager.GetColumnCount "wx.propgrid.PropertyGridManager.GetColumnCount") and [`SetColumnCount`](#wx.propgrid.PropertyGridManager.SetColumnCount "wx.propgrid.PropertyGridManager.SetColumnCount")
    CurrentPage: 'PropertyGridPage'  # `CurrentPage`[¶](#wx.propgrid.PropertyGridManager.CurrentPage "Permalink to this definition")See [`GetCurrentPage`](#wx.propgrid.PropertyGridManager.GetCurrentPage "wx.propgrid.PropertyGridManager.GetCurrentPage")
    DescBoxHeight: int  # `DescBoxHeight`[¶](#wx.propgrid.PropertyGridManager.DescBoxHeight "Permalink to this definition")See [`GetDescBoxHeight`](#wx.propgrid.PropertyGridManager.GetDescBoxHeight "wx.propgrid.PropertyGridManager.GetDescBoxHeight") and [`SetDescBoxHeight`](#wx.propgrid.PropertyGridManager.SetDescBoxHeight "wx.propgrid.PropertyGridManager.SetDescBoxHeight")
    Grid: 'PropertyGrid'  # `Grid`[¶](#wx.propgrid.PropertyGridManager.Grid "Permalink to this definition")See [`GetGrid`](#wx.propgrid.PropertyGridManager.GetGrid "wx.propgrid.PropertyGridManager.GetGrid")
    PageCount: int  # `PageCount`[¶](#wx.propgrid.PropertyGridManager.PageCount "Permalink to this definition")See [`GetPageCount`](#wx.propgrid.PropertyGridManager.GetPageCount "wx.propgrid.PropertyGridManager.GetPageCount")
    SelectedPage: int  # `SelectedPage`[¶](#wx.propgrid.PropertyGridManager.SelectedPage "Permalink to this definition")See [`GetSelectedPage`](#wx.propgrid.PropertyGridManager.GetSelectedPage "wx.propgrid.PropertyGridManager.GetSelectedPage")
    SelectedProperty: 'PGProperty'  # `SelectedProperty`[¶](#wx.propgrid.PropertyGridManager.SelectedProperty "Permalink to this definition")See [`GetSelectedProperty`](#wx.propgrid.PropertyGridManager.GetSelectedProperty "wx.propgrid.PropertyGridManager.GetSelectedProperty")
    Selection: 'PGProperty'  # `Selection`[¶](#wx.propgrid.PropertyGridManager.Selection "Permalink to this definition")See [`GetSelection`](#wx.propgrid.PropertyGridManager.GetSelection "wx.propgrid.PropertyGridManager.GetSelection")
    ToolBar: '_ToolBar'  # `ToolBar`[¶](#wx.propgrid.PropertyGridManager.ToolBar "Permalink to this definition")See [`GetToolBar`](#wx.propgrid.PropertyGridManager.GetToolBar "wx.propgrid.PropertyGridManager.GetToolBar")



class PropertyGrid(Scrolled,PropertyGridInterface):
    """ **Possible constructors**:



```
PropertyGrid()

PropertyGrid(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
             style=PG_DEFAULT_STYLE, name=PropertyGridNameStr)

```


PropertyGrid is a specialized grid for editing properties - in other
words name = value pairs.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGrid.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Two step constructor.


Call [`Create`](#wx.propgrid.PropertyGrid.Create "wx.propgrid.PropertyGrid.Create") when this constructor is called to build up the  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid)




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=PG\_DEFAULT\_STYLE, name=PropertyGridNameStr)*


Constructor.


The styles to be used are styles valid for the  [wx.Window](wx.Window.html#wx-window).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –





See also


PropertyGrid Window Styles.





---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AddActionTrigger(self, action, keycode, modifiers=0) -> None:
        """ 

`AddActionTrigger`(*self*, *action*, *keycode*, *modifiers=0*)[¶](#wx.propgrid.PropertyGrid.AddActionTrigger "Permalink to this definition")
Adds given key combination to trigger given action.


Here is a sample code to make Enter key press move focus to the next property.



```
propGrid.AddActionTrigger(wx.propgrid.PG_ACTION_NEXT_PROPERTY,
                          wx.WXK_RETURN)
propGrid.DedicateKey(wx.WXK_RETURN)

```



Parameters
* **action** (*int*) – Which action to trigger. See PropertyGrid Action Identifiers.
* **keycode** (*int*) – Which keycode triggers the action.
* **modifiers** (*int*) – Which key event modifiers, in addition to keycode, are needed to trigger the action.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AddToSelection(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`AddToSelection`(*self*, *id*)[¶](#wx.propgrid.PropertyGrid.AddToSelection "Permalink to this definition")
Adds given property into selection.


If `PG_EX_MULTIPLE_SELECTION` extra style is not used, then this has same effect as calling [`SelectProperty`](#wx.propgrid.PropertyGrid.SelectProperty "wx.propgrid.PropertyGrid.SelectProperty") .



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*





Note


Multiple selection is not supported for categories. This means that if you have properties selected, you cannot add category to selection, and also if you have category selected, you cannot add other properties to selection. This member function will fail silently in these cases, even returning `True`.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def AdjustScrollbars(self) -> None:
        """ 

`AdjustScrollbars`(*self*)[¶](#wx.propgrid.PropertyGrid.AdjustScrollbars "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def AutoGetTranslation(enable: bool) -> None:
        """ 

*static* `AutoGetTranslation`(*enable*)[¶](#wx.propgrid.PropertyGrid.AutoGetTranslation "Permalink to this definition")
This static function enables or disables automatic use of [`wx.GetTranslation`](wx.functions.html#wx.GetTranslation "wx.GetTranslation") for following strings:  [wx.propgrid.EnumProperty](wx.propgrid.EnumProperty.html#wx-propgrid-enumproperty) list labels,  [wx.propgrid.FlagsProperty](wx.propgrid.FlagsProperty.html#wx-propgrid-flagsproperty) child property labels.


Default is `False`.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def BeginLabelEdit(self, colIndex: int=0) -> None:
        """ 

`BeginLabelEdit`(*self*, *colIndex=0*)[¶](#wx.propgrid.PropertyGrid.BeginLabelEdit "Permalink to this definition")
Creates label editor  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) for given column, for property that is currently selected.


When multiple selection is enabled, this applies to whatever property [`GetSelection`](#wx.propgrid.PropertyGrid.GetSelection "wx.propgrid.PropertyGrid.GetSelection") returns.



Parameters
**colIndex** (*int*) – Which column’s label to edit. Note that you should not use value 1, which is reserved for property value column.





See also


[`EndLabelEdit`](#wx.propgrid.PropertyGrid.EndLabelEdit "wx.propgrid.PropertyGrid.EndLabelEdit") , [`MakeColumnEditable`](#wx.propgrid.PropertyGrid.MakeColumnEditable "wx.propgrid.PropertyGrid.MakeColumnEditable")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CalcScrolledPosition(self, *args, **kw) -> 'Point':
        """ 

`CalcScrolledPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGrid.CalcScrolledPosition "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CalcScrolledPosition** *(self, x, y)*


Translates the logical coordinates to the device ones.


For example, if a window is scrolled 10 pixels to the bottom, the device coordinates of the origin are (0, 0) (as always), but the logical coordinates are (0, 10) and so the call to CalcScrolledPosition(0, 10, xx, yy) will return 0 in yy.




---

  



**CalcScrolledPosition** *(self, pt)*



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
 [wx.Point](wx.Point.html#wx-point)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CalcUnscrolledPosition(self, *args, **kw) -> 'Point':
        """ 

`CalcUnscrolledPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGrid.CalcUnscrolledPosition "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CalcUnscrolledPosition** *(self, x, y)*


Translates the device coordinates to the logical ones.


For example, if a window is scrolled 10 pixels to the bottom, the device coordinates of the origin are (0, 0) (as always), but the logical coordinates are (0, 10) and so the call to CalcUnscrolledPosition(0, 0, xx, yy) will return 10 in yy.




---

  



**CalcUnscrolledPosition** *(self, pt)*



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
 [wx.Point](wx.Point.html#wx-point)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CenterSplitter(self, enableAutoResizing: bool=False) -> None:
        """ 

`CenterSplitter`(*self*, *enableAutoResizing=False*)[¶](#wx.propgrid.PropertyGrid.CenterSplitter "Permalink to this definition")
Centers the splitter.



Parameters
**enableAutoResizing** (*bool*) – If `True`, automatic column resizing is enabled (only applicable if window style `PG_SPLITTER_AUTO_CENTER` is used).






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ChangePropertyValue(self, id, newValue) -> bool:
        """ 

`ChangePropertyValue`(*self*, *id*, *newValue*)[¶](#wx.propgrid.PropertyGrid.ChangePropertyValue "Permalink to this definition")
Changes value of a property, as if from an editor.


Use this instead of [`SetPropertyValue`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetPropertyValue "wx.propgrid.PropertyGridInterface.SetPropertyValue") if you need the value to run through validation process, and also send `wxEVT_PG_CHANGED` .



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **newValue** (*PGVariant*) –



Return type
*bool*



Returns
Returns `True` if value was successfully changed.





Note


Since this function sends `wxEVT_PG_CHANGED` , it should not be called from `EVT_PG_CHANGED` handler.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PropertyGrid.Clear "Permalink to this definition")
Deletes all properties.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ClearActionTriggers(self, action: int) -> None:
        """ 

`ClearActionTriggers`(*self*, *action*)[¶](#wx.propgrid.PropertyGrid.ClearActionTriggers "Permalink to this definition")
Clears action triggers for given action.



Parameters
**action** (*int*) – Which action to trigger. PropertyGrid Action Identifiers.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def CommitChangesFromEditor(self, flags: 'int'=0) -> bool:
        """ 

`CommitChangesFromEditor`(*self*, *flags=0*)[¶](#wx.propgrid.PropertyGrid.CommitChangesFromEditor "Permalink to this definition")
Forces updating the value of property from the editor control.


Note that `wxEVT_PG_CHANGING` and `wxEVT_PG_CHANGED` are dispatched using ProcessEvent, meaning your event handlers will be called immediately.



Parameters
**flags** (*wx.int*) – 



Return type
*bool*



Returns
Returns `True` if anything was changed.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=PG_DEFAULT_STYLE, name=PropertyGridNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=PG\_DEFAULT\_STYLE*, *name=PropertyGridNameStr*)[¶](#wx.propgrid.PropertyGrid.Create "Permalink to this definition")
Two step creation.


Whenever the control is created without any parameters, use Create to actually create it. Don’t access the control’s public methods before this is called



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*





See also


PropertyGrid Window Styles.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DedicateKey(self, keycode: int) -> None:
        """ 

`DedicateKey`(*self*, *keycode*)[¶](#wx.propgrid.PropertyGrid.DedicateKey "Permalink to this definition")
Dedicates a specific keycode to  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid).


This means that such key presses will not be redirected to editor controls.


Using this function allows, for example, navigation between properties using arrow keys even when the focus is in the editor control.



Parameters
**keycode** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DisableKeyboardScrolling(self) -> None:
        """ 

`DisableKeyboardScrolling`(*self*)[¶](#wx.propgrid.PropertyGrid.DisableKeyboardScrolling "Permalink to this definition")
Disable use of keyboard keys for scrolling.


By default cursor movement keys (including Home, End, Page Up and Down) are used to scroll the window appropriately. If the derived class uses these keys for something else, e.g. changing the currently selected item, this function can be used to disable this behaviour as it’s not only not necessary then but can actually be actively harmful if another object forwards a keyboard event corresponding to one of the above keys to us using ProcessWindowEvent() because the event will always be processed which can be undesirable.



New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoHidePropertyError(self, property: 'propgrid.PGProperty') -> None:
        """ 

`DoHidePropertyError`(*self*, *property*)[¶](#wx.propgrid.PropertyGrid.DoHidePropertyError "Permalink to this definition")
Override in derived class to hide an error displayed by [`DoShowPropertyError`](#wx.propgrid.PropertyGrid.DoShowPropertyError "wx.propgrid.PropertyGrid.DoShowPropertyError") .



Parameters
**property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 





See also


[`DoShowPropertyError`](#wx.propgrid.PropertyGrid.DoShowPropertyError "wx.propgrid.PropertyGrid.DoShowPropertyError")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoOnValidationFailure(self, property, invalidValue) -> bool:
        """ 

`DoOnValidationFailure`(*self*, *property*, *invalidValue*)[¶](#wx.propgrid.PropertyGrid.DoOnValidationFailure "Permalink to this definition")
Override to customize property validation failure behaviour.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property with entered an invalid value
* **invalidValue** (*PGVariant*) – Value which failed in validation.



Return type
*bool*



Returns
Return `True` if user is allowed to change to another property even if current has invalid value.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoOnValidationFailureReset(self, property: 'propgrid.PGProperty') -> None:
        """ 

`DoOnValidationFailureReset`(*self*, *property*)[¶](#wx.propgrid.PropertyGrid.DoOnValidationFailureReset "Permalink to this definition")
Override to customize resetting of property validation failure status.



Parameters
**property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 





Note


Property is guaranteed to have flag `PG_PROP_INVALID_VALUE` set.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoPrepareDC(self, dc: 'DC') -> None:
        """ 

`DoPrepareDC`(*self*, *dc*)[¶](#wx.propgrid.PropertyGrid.DoPrepareDC "Permalink to this definition")
Call this function to prepare the device context for drawing a scrolled image.


It sets the device origin according to the current scroll position. [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") is called automatically within the default `wxEVT_PAINT` event handler, so your [`OnDraw`](#wx.propgrid.PropertyGrid.OnDraw "wx.propgrid.PropertyGrid.OnDraw") override will be passed an already ‘pre-scrolled’ device context. However, if you wish to draw from outside of [`OnDraw`](#wx.propgrid.PropertyGrid.OnDraw "wx.propgrid.PropertyGrid.OnDraw") (e.g. from your own `wxEVT_PAINT` handler), you must call this function yourself.


For example:



```
def OnEvent(self, event):

    dc = wx.ClientDC(self)
    self.DoPrepareDC(dc)

    dc.SetPen(wx.BLACK_PEN)

    x, y = event.GetPosition()

    if (xpos > -1 and ypos > -1 and event.Dragging()):
        dc.DrawLine(xpos, ypos, x, y)

    xpos = x
    ypos = y

```


Notice that the function sets the origin by moving it relatively to the current origin position, so you shouldn’t change the origin before calling [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") or, if you do, reset it to (0, 0) later. If you call [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") immediately after device context creation, as in the example above, this problem doesn’t arise, of course, so it is customary to do it like this.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def DoRegisterEditorClass(editor, name, noDefCheck=False) -> 'PGEditor':
        """ 

*static* `DoRegisterEditorClass`(*editor*, *name*, *noDefCheck=False*)[¶](#wx.propgrid.PropertyGrid.DoRegisterEditorClass "Permalink to this definition")
Registers a new editor class.



Parameters
* **editor** ([*wx.propgrid.PGEditor*](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor "wx.propgrid.PGEditor")) –
* **name** (*string*) –
* **noDefCheck** (*bool*) –



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)



Returns
Returns pointer to the editor class instance that should be used.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DoShowPropertyError(self, property, msg) -> None:
        """ 

`DoShowPropertyError`(*self*, *property*, *msg*)[¶](#wx.propgrid.PropertyGrid.DoShowPropertyError "Permalink to this definition")
Override in derived class to display error messages in custom manner (these message usually only result from validation failure).



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **msg** (*string*) –





Note


If you implement this, then you also need to implement [`DoHidePropertyError`](#wx.propgrid.PropertyGrid.DoHidePropertyError "wx.propgrid.PropertyGrid.DoHidePropertyError") - possibly to do nothing, if error does not need hiding (e.g. it was logged or shown in a message box).




See also


[`DoHidePropertyError`](#wx.propgrid.PropertyGrid.DoHidePropertyError "wx.propgrid.PropertyGrid.DoHidePropertyError")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def DrawItemAndValueRelated(self, p: 'propgrid.PGProperty') -> None:
        """ 

`DrawItemAndValueRelated`(*self*, *p*)[¶](#wx.propgrid.PropertyGrid.DrawItemAndValueRelated "Permalink to this definition")
Draws item, children, and consecutive parents as long as category is not met.



Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EditorsValueWasModified(self) -> None:
        """ 

`EditorsValueWasModified`(*self*)[¶](#wx.propgrid.PropertyGrid.EditorsValueWasModified "Permalink to this definition")
Call when editor widget’s contents is modified.


For example, this is called when changes text in  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) (used in  [wx.propgrid.StringProperty](wx.propgrid.StringProperty.html#wx-propgrid-stringproperty) and  [wx.propgrid.IntProperty](wx.propgrid.IntProperty.html#wx-propgrid-intproperty)).



Note


This function should only be called by custom properties.




See also


[`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EditorsValueWasNotModified(self) -> None:
        """ 

`EditorsValueWasNotModified`(*self*)[¶](#wx.propgrid.PropertyGrid.EditorsValueWasNotModified "Permalink to this definition")
Reverse of [`EditorsValueWasModified`](#wx.propgrid.PropertyGrid.EditorsValueWasModified "wx.propgrid.PropertyGrid.EditorsValueWasModified") .



Note


This function should only be called by custom properties.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ 

`EnableCategories`(*self*, *enable*)[¶](#wx.propgrid.PropertyGrid.EnableCategories "Permalink to this definition")
Enables or disables (shows/hides) categories according to parameter enable.



Parameters
**enable** (*bool*) – 



Return type
*bool*





Note


This functions deselects selected property, if any. Validation failure option `PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnableScrolling(self, xScrolling, yScrolling) -> None:
        """ 

`EnableScrolling`(*self*, *xScrolling*, *yScrolling*)[¶](#wx.propgrid.PropertyGrid.EnableScrolling "Permalink to this definition")
Enable or disable use of [`wx.Window.ScrollWindow`](wx.Window.html#wx.Window.ScrollWindow "wx.Window.ScrollWindow") for scrolling.


By default, when a scrolled window is logically scrolled, [`wx.Window.ScrollWindow`](wx.Window.html#wx.Window.ScrollWindow "wx.Window.ScrollWindow") is called on the underlying window which scrolls the window contents and only invalidates the part of the window newly brought into view. If `False` is passed as an argument, then this “physical scrolling” is disabled and the window is entirely invalidated whenever it is scrolled by calling [`wx.Window.Refresh`](wx.Window.html#wx.Window.Refresh "wx.Window.Refresh") .


It should be rarely necessary to disable physical scrolling, so this method shouldn’t be called in normal circumstances.



Parameters
* **xScrolling** (*bool*) – If `True`, enables physical scrolling in the x direction.
* **yScrolling** (*bool*) – If `True`, enables physical scrolling in the y direction.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EndLabelEdit(self, commit: bool=True) -> None:
        """ 

`EndLabelEdit`(*self*, *commit=True*)[¶](#wx.propgrid.PropertyGrid.EndLabelEdit "Permalink to this definition")
Destroys label editor  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl), if any.



Parameters
**commit** (*bool*) – Use `True` (default) to store edited label text in property cell data.





See also


[`BeginLabelEdit`](#wx.propgrid.PropertyGrid.BeginLabelEdit "wx.propgrid.PropertyGrid.BeginLabelEdit") , [`MakeColumnEditable`](#wx.propgrid.PropertyGrid.MakeColumnEditable "wx.propgrid.PropertyGrid.MakeColumnEditable")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def EnsureVisible(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`EnsureVisible`(*self*, *id*)[¶](#wx.propgrid.PropertyGrid.EnsureVisible "Permalink to this definition")
Scrolls and/or expands items to ensure that the given item is visible.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*



Returns
Returns `True` if something was actually done.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def FitColumns(self) -> 'Size':
        """ 

`FitColumns`(*self*)[¶](#wx.propgrid.PropertyGrid.FitColumns "Permalink to this definition")
Reduces column sizes to minimum possible, while still retaining fully visible grid contents (labels, images).



Return type
`Size`



Returns
Minimum size for the grid to still display everything.





Note


Does not work well with `PG_SPLITTER_AUTO_CENTER` window style.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionBackgroundColour(self) -> 'Colour':
        """ 

`GetCaptionBackgroundColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCaptionBackgroundColour "Permalink to this definition")
Returns current category caption background colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionFont(self) -> 'Font':
        """ 

`GetCaptionFont`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCaptionFont "Permalink to this definition")
Returns current category caption font.



Return type
`Font`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCaptionForegroundColour(self) -> 'Colour':
        """ 

`GetCaptionForegroundColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCaptionForegroundColour "Permalink to this definition")
Returns current category caption text colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellBackgroundColour(self) -> 'Colour':
        """ 

`GetCellBackgroundColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCellBackgroundColour "Permalink to this definition")
Returns current cell background colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellDisabledTextColour(self) -> 'Colour':
        """ 

`GetCellDisabledTextColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCellDisabledTextColour "Permalink to this definition")
Returns current cell text colour when disabled.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetCellTextColour(self) -> 'Colour':
        """ 

`GetCellTextColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetCellTextColour "Permalink to this definition")
Returns current cell text colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.propgrid.PropertyGrid.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetColumnCount(self) -> int:
        """ 

`GetColumnCount`(*self*)[¶](#wx.propgrid.PropertyGrid.GetColumnCount "Permalink to this definition")
Returns number of columns currently on grid.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetEditorTextCtrl(self) -> 'TextCtrl':
        """ 

`GetEditorTextCtrl`(*self*)[¶](#wx.propgrid.PropertyGrid.GetEditorTextCtrl "Permalink to this definition")
Returns  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) active in currently selected property, if any.


Takes  [wx.adv.OwnerDrawnComboBox](wx.adv.OwnerDrawnComboBox.html#wx-adv-ownerdrawncombobox) into account.



Return type
*TextCtrl*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetEmptySpaceColour(self) -> 'Colour':
        """ 

`GetEmptySpaceColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetEmptySpaceColour "Permalink to this definition")
Returns colour of empty space below properties.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetFontHeight(self) -> int:
        """ 

`GetFontHeight`(*self*)[¶](#wx.propgrid.PropertyGrid.GetFontHeight "Permalink to this definition")
Returns height of highest characters of used font.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetGrid(self) -> 'PropertyGrid':
        """ 

`GetGrid`(*self*)[¶](#wx.propgrid.PropertyGrid.GetGrid "Permalink to this definition")
Returns pointer to itself.


Dummy function that enables same kind of code to use  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid) and  [wx.propgrid.PropertyGridManager](wx.propgrid.PropertyGridManager.html#wx-propgrid-propertygridmanager).



Return type
 [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetImageRect(self, property, item) -> 'Rect':
        """ 

`GetImageRect`(*self*, *property*, *item*)[¶](#wx.propgrid.PropertyGrid.GetImageRect "Permalink to this definition")
Returns rectangle of custom paint image.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Return image rectangle for this property.
* **item** (*int*) – Which choice of property to use (each choice may have different image).



Return type
`Rect`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetImageSize(self, property=None, item=-1) -> 'Size':
        """ 

`GetImageSize`(*self*, *property=None*, *item=-1*)[¶](#wx.propgrid.PropertyGrid.GetImageSize "Permalink to this definition")
Returns size of the custom paint image in front of property.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Return image rectangle for this property. If this argument is `None`, then preferred size is returned.
* **item** (*int*) – Which choice of property to use (each choice may have different image).



Return type
`Size`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLabelEditor(self) -> 'TextCtrl':
        """ 

`GetLabelEditor`(*self*)[¶](#wx.propgrid.PropertyGrid.GetLabelEditor "Permalink to this definition")
Returns currently active label editor, `None` if none.



Return type
*TextCtrl*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLastItem(self, flags: int=PG_ITERATE_DEFAULT) -> 'PGProperty':
        """ 

`GetLastItem`(*self*, *flags=PG\_ITERATE\_DEFAULT*)[¶](#wx.propgrid.PropertyGrid.GetLastItem "Permalink to this definition")
Returns last item which could be iterated using given flags.



Parameters
**flags** (*int*) – See PropertyGridIterator Flags.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetLineColour(self) -> 'Colour':
        """ 

`GetLineColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetLineColour "Permalink to this definition")
Returns colour of lines between cells.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetMarginColour(self) -> 'Colour':
        """ 

`GetMarginColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetMarginColour "Permalink to this definition")
Returns background colour of margin.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetMarginWidth(self) -> int:
        """ 

`GetMarginWidth`(*self*)[¶](#wx.propgrid.PropertyGrid.GetMarginWidth "Permalink to this definition")
Returns margin width.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetPanel(self) -> 'Window':
        """ 

`GetPanel`(*self*)[¶](#wx.propgrid.PropertyGrid.GetPanel "Permalink to this definition")
Returns  [wx.Window](wx.Window.html#wx-window) that the properties are painted on, and which should be used as the parent for editor controls.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetRoot(self) -> 'PGProperty':
        """ 

`GetRoot`(*self*)[¶](#wx.propgrid.PropertyGrid.GetRoot "Permalink to this definition")
Returns “root property”.


It does not have name, etc. and it is not visible. It is only useful for accessing its children.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetRowHeight(self) -> int:
        """ 

`GetRowHeight`(*self*)[¶](#wx.propgrid.PropertyGrid.GetRowHeight "Permalink to this definition")
Returns height of a single grid row (in pixels).



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScaleX(self) -> float:
        """ 

`GetScaleX`(*self*)[¶](#wx.propgrid.PropertyGrid.GetScaleX "Permalink to this definition")

Return type
*float*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScaleY(self) -> float:
        """ 

`GetScaleY`(*self*)[¶](#wx.propgrid.PropertyGrid.GetScaleY "Permalink to this definition")

Return type
*float*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollLines(self, orient: int) -> int:
        """ 

`GetScrollLines`(*self*, *orient*)[¶](#wx.propgrid.PropertyGrid.GetScrollLines "Permalink to this definition")

Parameters
**orient** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollPageSize(self, orient: int) -> int:
        """ 

`GetScrollPageSize`(*self*, *orient*)[¶](#wx.propgrid.PropertyGrid.GetScrollPageSize "Permalink to this definition")

Parameters
**orient** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetScrollPixelsPerUnit(self) -> tuple:
        """ 

`GetScrollPixelsPerUnit`(*self*)[¶](#wx.propgrid.PropertyGrid.GetScrollPixelsPerUnit "Permalink to this definition")
Get the number of pixels per scroll unit (line), in each direction, as set by [`SetScrollbars`](#wx.propgrid.PropertyGrid.SetScrollbars "wx.propgrid.PropertyGrid.SetScrollbars") .


A value of zero indicates no scrolling in that direction.



Return type
*tuple*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectedProperty(self) -> 'PGProperty':
        """ 

`GetSelectedProperty`(*self*)[¶](#wx.propgrid.PropertyGrid.GetSelectedProperty "Permalink to this definition")
Returns currently selected property.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelection(self) -> 'PGProperty':
        """ 

`GetSelection`(*self*)[¶](#wx.propgrid.PropertyGrid.GetSelection "Permalink to this definition")
Returns currently selected property.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectionBackgroundColour(self) -> 'Colour':
        """ 

`GetSelectionBackgroundColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetSelectionBackgroundColour "Permalink to this definition")
Returns current selection background colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSelectionForegroundColour(self) -> 'Colour':
        """ 

`GetSelectionForegroundColour`(*self*)[¶](#wx.propgrid.PropertyGrid.GetSelectionForegroundColour "Permalink to this definition")
Returns current selection text colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSizeAvailableForScrollTarget(self, size: Union[tuple[int, int], 'Size']) -> 'Size':
        """ 

`GetSizeAvailableForScrollTarget`(*self*, *size*)[¶](#wx.propgrid.PropertyGrid.GetSizeAvailableForScrollTarget "Permalink to this definition")
Function which must be overridden to implement the size available for the scroll target for the given size of the main window.


This method must be overridden if [`SetTargetWindow`](#wx.propgrid.PropertyGrid.SetTargetWindow "wx.propgrid.PropertyGrid.SetTargetWindow") is used (it is never called otherwise). The implementation should decrease the *size* to account for the size of the non-scrollable parts of the main window and return only the size available for the scrollable window itself. E.g. in the example given in [`SetTargetWindow`](#wx.propgrid.PropertyGrid.SetTargetWindow "wx.propgrid.PropertyGrid.SetTargetWindow") documentation the function would subtract the height of the header window from the vertical component of *size*.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
 [wx.Size](wx.Size.html#wx-size)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetSplitterPosition(self, splitterIndex: int=0) -> int:
        """ 

`GetSplitterPosition`(*self*, *splitterIndex=0*)[¶](#wx.propgrid.PropertyGrid.GetSplitterPosition "Permalink to this definition")
Returns current splitter x position.



Parameters
**splitterIndex** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetStatusBar(self) -> 'StatusBar':
        """ 

`GetStatusBar`(*self*)[¶](#wx.propgrid.PropertyGrid.GetStatusBar "Permalink to this definition")
Return  [wx.StatusBar](wx.StatusBar.html#wx-statusbar) that is used by this  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid).


You can reimplement this member function in derived class to override the default behaviour of using the top-level  [wx.Frame](wx.Frame.html#wx-frame)’s status bar, if any.



Return type
[`StatusBar`](#wx.propgrid.PropertyGrid.StatusBar "wx.propgrid.PropertyGrid.StatusBar")






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetTargetRect(self) -> 'Rect':
        """ 

`GetTargetRect`(*self*)[¶](#wx.propgrid.PropertyGrid.GetTargetRect "Permalink to this definition")

Return type
 [wx.Rect](wx.Rect.html#wx-rect)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetTargetWindow(self) -> 'Window':
        """ 

`GetTargetWindow`(*self*)[¶](#wx.propgrid.PropertyGrid.GetTargetWindow "Permalink to this definition")

Return type
 [wx.Window](wx.Window.html#wx-window)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUncommittedPropertyValue(self) -> 'PGVariant':
        """ 

`GetUncommittedPropertyValue`(*self*)[¶](#wx.propgrid.PropertyGrid.GetUncommittedPropertyValue "Permalink to this definition")
Returns most up-to-date value of selected property.


This will return value different from [`GetSelectedProperty`](#wx.propgrid.PropertyGrid.GetSelectedProperty "wx.propgrid.PropertyGrid.GetSelectedProperty") .GetValue() only when text editor is activate and string edited by user represents valid, uncommitted property value.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUnspecifiedValueAppearance(self) -> 'PGCell':
        """ 

`GetUnspecifiedValueAppearance`(*self*)[¶](#wx.propgrid.PropertyGrid.GetUnspecifiedValueAppearance "Permalink to this definition")
Returns current appearance of unspecified value cells.



Return type
 [wx.propgrid.PGCell](wx.propgrid.PGCell.html#wx-propgrid-pgcell)





See also


[`SetUnspecifiedValueAppearance`](#wx.propgrid.PropertyGrid.SetUnspecifiedValueAppearance "wx.propgrid.PropertyGrid.SetUnspecifiedValueAppearance")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetUnspecifiedValueText(self, argFlags: int=0) -> str:
        """ 

`GetUnspecifiedValueText`(*self*, *argFlags=0*)[¶](#wx.propgrid.PropertyGrid.GetUnspecifiedValueText "Permalink to this definition")
Returns (visual) text representation of the unspecified property value.



Parameters
**argFlags** (*int*) – For internal use only.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetVerticalSpacing(self) -> int:
        """ 

`GetVerticalSpacing`(*self*)[¶](#wx.propgrid.PropertyGrid.GetVerticalSpacing "Permalink to this definition")
Returns current vertical spacing.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def GetViewStart(self) -> tuple:
        """ 

`GetViewStart`(*self*)[¶](#wx.propgrid.PropertyGrid.GetViewStart "Permalink to this definition")
Get the position at which the visible portion of the window starts.



Return type
*tuple*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> 'PropertyGridHitTestResult':
        """ 

`HitTest`(*self*, *pt*)[¶](#wx.propgrid.PropertyGrid.HitTest "Permalink to this definition")
Returns information about arbitrary position in the grid.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Coordinates in the virtual grid space. You may need to use [`wx.Scrolled.CalcScrolledPosition`](wx.Scrolled.html#wx.Scrolled.CalcScrolledPosition "wx.Scrolled.CalcScrolledPosition") for translating  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid) client coordinates into something this member function can use.



Return type
 [wx.propgrid.PropertyGridHitTestResult](wx.propgrid.PropertyGridHitTestResult.html#wx-propgrid-propertygridhittestresult)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsAnyModified(self) -> bool:
        """ 

`IsAnyModified`(*self*)[¶](#wx.propgrid.PropertyGrid.IsAnyModified "Permalink to this definition")
Returns `True` if any property has been modified by the user.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsAutoScrolling(self) -> bool:
        """ 

`IsAutoScrolling`(*self*)[¶](#wx.propgrid.PropertyGrid.IsAutoScrolling "Permalink to this definition")
Are we generating the autoscroll events?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsEditorFocused(self) -> bool:
        """ 

`IsEditorFocused`(*self*)[¶](#wx.propgrid.PropertyGrid.IsEditorFocused "Permalink to this definition")
Returns `True` if a property editor control has focus.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsEditorsValueModified(self) -> bool:
        """ 

`IsEditorsValueModified`(*self*)[¶](#wx.propgrid.PropertyGrid.IsEditorsValueModified "Permalink to this definition")
Returns `True` if editor’s value was marked modified.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsFrozen(self) -> bool:
        """ 

`IsFrozen`(*self*)[¶](#wx.propgrid.PropertyGrid.IsFrozen "Permalink to this definition")
Returns `True` if updating is frozen (i.e.


`Freeze` called but not yet `Thaw` ).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def IsRetained(self) -> bool:
        """ 

`IsRetained`(*self*)[¶](#wx.propgrid.PropertyGrid.IsRetained "Permalink to this definition")
Motif only: `True` if the window has a backing bitmap.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def MakeColumnEditable(self, column, editable=True) -> None:
        """ 

`MakeColumnEditable`(*self*, *column*, *editable=True*)[¶](#wx.propgrid.PropertyGrid.MakeColumnEditable "Permalink to this definition")
Makes given column editable by user.



Parameters
* **column** (*int*) – The index of the column to make editable.
* **editable** (*bool*) – Using `False` here will disable column from being editable.




*column* must not be equal to 1, as the second column is always editable and can be made read-only only on cell-by-cell basis using:



```
property.ChangeFlag(wx.propgrid.PG_PROP_READONLY, True)

```



See also


[`BeginLabelEdit`](#wx.propgrid.PropertyGrid.BeginLabelEdit "wx.propgrid.PropertyGrid.BeginLabelEdit") , [`EndLabelEdit`](#wx.propgrid.PropertyGrid.EndLabelEdit "wx.propgrid.PropertyGrid.EndLabelEdit")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def OnDraw(self, dc: 'DC') -> None:
        """ 

`OnDraw`(*self*, *dc*)[¶](#wx.propgrid.PropertyGrid.OnDraw "Permalink to this definition")
Called by the default paint event handler to allow the application to define painting behaviour without having to worry about calling [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") .


Instead of overriding this function you may also just process the paint event in the derived class as usual, but then you will have to call [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") yourself.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def OnTLPChanging(self, newTLP: 'Window') -> None:
        """ 

`OnTLPChanging`(*self*, *newTLP*)[¶](#wx.propgrid.PropertyGrid.OnTLPChanging "Permalink to this definition")
It is recommended that you call this function any time your code causes  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid)’s top-level parent to change.


 [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid)’s OnIdle() handler should be able to detect most changes, but it is not perfect.



Parameters
**newTLP** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – New top-level parent that is about to be set. Old top-level parent window should still exist as the current one.





Note


This function is automatically called from  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid):: `Reparent` and `wx.propgrid.PropertyGridManager.Reparent` . You only need to use it if you reparent  [wx.propgrid.PropertyGrid](#wx-propgrid-propertygrid) indirectly.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def PrepareDC(self, dc: 'DC') -> None:
        """ 

`PrepareDC`(*self*, *dc*)[¶](#wx.propgrid.PropertyGrid.PrepareDC "Permalink to this definition")
This function is for backwards compatibility only and simply calls [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") now.


Notice that it is not called by the default paint event handle ( [`DoPrepareDC`](#wx.propgrid.PropertyGrid.DoPrepareDC "wx.propgrid.PropertyGrid.DoPrepareDC") is), so overriding this method in your derived class is useless.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RefreshEditor(self) -> None:
        """ 

`RefreshEditor`(*self*)[¶](#wx.propgrid.PropertyGrid.RefreshEditor "Permalink to this definition")
Refreshes any active editor control.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ 

`RefreshProperty`(*self*, *p*)[¶](#wx.propgrid.PropertyGrid.RefreshProperty "Permalink to this definition")
Redraws given property.



Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    @staticmethod
    def RegisterEditorClass(editor, noDefCheck=False) -> 'PGEditor':
        """ 

*static* `RegisterEditorClass`(*editor*, *noDefCheck=False*)[¶](#wx.propgrid.PropertyGrid.RegisterEditorClass "Permalink to this definition")
Forwards to DoRegisterEditorClass with empty name.



Parameters
* **editor** ([*wx.propgrid.PGEditor*](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor "wx.propgrid.PGEditor")) –
* **noDefCheck** (*bool*) –



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def RemoveFromSelection(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`RemoveFromSelection`(*self*, *id*)[¶](#wx.propgrid.PropertyGrid.RemoveFromSelection "Permalink to this definition")
Removes given property from selection.


If property is not selected, an assertion failure will occur.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ResetColours(self) -> None:
        """ 

`ResetColours`(*self*)[¶](#wx.propgrid.PropertyGrid.ResetColours "Permalink to this definition")
Resets all colours to the original system values.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ResetColumnSizes(self, enableAutoResizing: bool=False) -> None:
        """ 

`ResetColumnSizes`(*self*, *enableAutoResizing=False*)[¶](#wx.propgrid.PropertyGrid.ResetColumnSizes "Permalink to this definition")
Resets column sizes and splitter positions, based on proportions.



Parameters
**enableAutoResizing** (*bool*) – If `True`, automatic column resizing is enabled (only applicable if window style `PG_SPLITTER_AUTO_CENTER` is used).





See also


[`wx.propgrid.PropertyGridInterface.SetColumnProportion`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.SetColumnProportion "wx.propgrid.PropertyGridInterface.SetColumnProportion")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def Scroll(self, *args, **kw) -> None:
        """ 

`Scroll`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGrid.Scroll "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Scroll** *(self, x, y)*


Scrolls a window so the view start is at the given point.



Parameters
* **x** (*int*) – The x position to scroll to, in scroll units.
* **y** (*int*) – The y position to scroll to, in scroll units.





Note


The positions are in scroll units, not pixels, so to convert to pixels you will have to multiply by the number of pixels per scroll increment. If either parameter is `wx.DefaultCoord` (-1), that position will be ignored (no change in that direction).




See also


[`SetScrollbars`](#wx.propgrid.PropertyGrid.SetScrollbars "wx.propgrid.PropertyGrid.SetScrollbars") , [`GetScrollPixelsPerUnit`](#wx.propgrid.PropertyGrid.GetScrollPixelsPerUnit "wx.propgrid.PropertyGrid.GetScrollPixelsPerUnit")





---

  



**Scroll** *(self, pt)*


This is an overload of [`Scroll`](#wx.propgrid.PropertyGrid.Scroll "wx.propgrid.PropertyGrid.Scroll") ; see that function for more info.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SelectProperty(self, id, focus=False) -> bool:
        """ 

`SelectProperty`(*self*, *id*, *focus=False*)[¶](#wx.propgrid.PropertyGrid.SelectProperty "Permalink to this definition")
Selects a property.


Editor widget is automatically created, but not focused unless focus is `True`.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property to select (name or pointer).
* **focus** (*bool*) – If `True`, move keyboard focus to the created editor right away.



Return type
*bool*



Returns
returns `True` if selection finished successfully. Usually only fails if current value in editor is not valid.





Note


In wxWidgets 2.9 and later, this function no longer sends `wxEVT_PG_SELECTED` .




Note


This clears any previous selection.




See also


[`wx.propgrid.PropertyGridInterface.ClearSelection`](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface.ClearSelection "wx.propgrid.PropertyGridInterface.ClearSelection")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SendAutoScrollEvents(self, event: 'ScrollWinEvent') -> bool:
        """ 

`SendAutoScrollEvents`(*self*, *event*)[¶](#wx.propgrid.PropertyGrid.SendAutoScrollEvents "Permalink to this definition")
This method can be overridden in a derived class to forbid sending the auto scroll events - note that unlike [`StopAutoScrolling`](#wx.propgrid.PropertyGrid.StopAutoScrolling "wx.propgrid.PropertyGrid.StopAutoScrolling") it doesn’t stop the timer, so it will be called repeatedly and will typically return different values depending on the current mouse position.


The base class version just returns `True`.



Parameters
**event** ([*wx.ScrollWinEvent*](wx.ScrollWinEvent.html#wx.ScrollWinEvent "wx.ScrollWinEvent")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCaptionBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetCaptionBackgroundColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetCaptionBackgroundColour "Permalink to this definition")
Sets category caption background colour.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCaptionTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetCaptionTextColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetCaptionTextColour "Permalink to this definition")
Sets category caption text colour.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetCellBackgroundColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetCellBackgroundColour "Permalink to this definition")
Sets default cell background colour - applies to property cells.


Note that appearance of editor widgets may not be affected.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellDisabledTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetCellDisabledTextColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetCellDisabledTextColour "Permalink to this definition")
Sets cell text colour for disabled properties.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCellTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetCellTextColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetCellTextColour "Permalink to this definition")
Sets default cell text colour - applies to property name and value text.


Note that appearance of editor widgets may not be affected.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetColumnCount(self, colCount: int) -> None:
        """ 

`SetColumnCount`(*self*, *colCount*)[¶](#wx.propgrid.PropertyGrid.SetColumnCount "Permalink to this definition")
Set number of columns (2 or more).



Parameters
**colCount** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetCurrentCategory(self, id: 'propgrid.PGPropArgCls') -> None:
        """ 

`SetCurrentCategory`(*self*, *id*)[¶](#wx.propgrid.PropertyGrid.SetCurrentCategory "Permalink to this definition")
Sets the ‘current’ category - Append will add non-category properties under it.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetEmptySpaceColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetEmptySpaceColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetEmptySpaceColour "Permalink to this definition")
Sets colour of empty space below properties.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetLineColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetLineColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetLineColour "Permalink to this definition")
Sets colour of lines between cells.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetMarginColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetMarginColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetMarginColour "Permalink to this definition")
Sets background colour of margin.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScale(self, xs, ys) -> None:
        """ 

`SetScale`(*self*, *xs*, *ys*)[¶](#wx.propgrid.PropertyGrid.SetScale "Permalink to this definition")

Parameters
* **xs** (*float*) –
* **ys** (*float*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollPageSize(self, orient, pageSize) -> None:
        """ 

`SetScrollPageSize`(*self*, *orient*, *pageSize*)[¶](#wx.propgrid.PropertyGrid.SetScrollPageSize "Permalink to this definition")

Parameters
* **orient** (*int*) –
* **pageSize** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollRate(self, xstep, ystep) -> None:
        """ 

`SetScrollRate`(*self*, *xstep*, *ystep*)[¶](#wx.propgrid.PropertyGrid.SetScrollRate "Permalink to this definition")
Set the horizontal and vertical scrolling increment only.


See the pixelsPerUnit parameter in [`SetScrollbars`](#wx.propgrid.PropertyGrid.SetScrollbars "wx.propgrid.PropertyGrid.SetScrollbars") .



Parameters
* **xstep** (*int*) –
* **ystep** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetScrollbars(self, pixelsPerUnitX, pixelsPerUnitY, noUnitsX, noUnitsY, xPos=0, yPos=0, noRefresh=False) -> None:
        """ 

`SetScrollbars`(*self*, *pixelsPerUnitX*, *pixelsPerUnitY*, *noUnitsX*, *noUnitsY*, *xPos=0*, *yPos=0*, *noRefresh=False*)[¶](#wx.propgrid.PropertyGrid.SetScrollbars "Permalink to this definition")
Sets up vertical and/or horizontal scrollbars.


The first pair of parameters give the number of pixels per ‘scroll step’, i.e. amount moved when the up or down scroll arrows are pressed. The second pair gives the length of scrollbar in scroll steps, which sets the size of the virtual window.


*xPos* and *yPos* optionally specify a position to scroll to immediately.


For example, the following gives a window horizontal and vertical scrollbars with 20 pixels per scroll step, and a size of 50 steps (1000 pixels) in each direction:



```
window.SetScrollbars(20, 20, 50, 50)

```


 [wx.Scrolled](wx.Scrolled.html#wx-scrolled) manages the page size itself, using the current client window size as the page size.


Note that for more sophisticated scrolling applications, for example where scroll steps may be variable according to the position in the document, it will be necessary to derive a new class from  [wx.Window](wx.Window.html#wx-window), overriding OnSize() and adjusting the scrollbars appropriately.



Parameters
* **pixelsPerUnitX** (*int*) – Pixels per scroll unit in the horizontal direction.
* **pixelsPerUnitY** (*int*) – Pixels per scroll unit in the vertical direction.
* **noUnitsX** (*int*) – Number of units in the horizontal direction.
* **noUnitsY** (*int*) – Number of units in the vertical direction.
* **xPos** (*int*) – Position to initialize the scrollbars in the horizontal direction, in scroll units.
* **yPos** (*int*) – Position to initialize the scrollbars in the vertical direction, in scroll units.
* **noRefresh** (*bool*) – Will not refresh window if `True`.





See also


[`wx.Window.SetVirtualSize`](wx.Window.html#wx.Window.SetVirtualSize "wx.Window.SetVirtualSize")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelection(self, newSelection: ArrayPGProperty) -> None:
        """ 

`SetSelection`(*self*, *newSelection*)[¶](#wx.propgrid.PropertyGrid.SetSelection "Permalink to this definition")
Set entire new selection from given list of properties.



Parameters
**newSelection** (*ArrayPGProperty*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelectionBackgroundColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetSelectionBackgroundColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetSelectionBackgroundColour "Permalink to this definition")
Sets selection background colour - applies to selected property name background.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSelectionTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetSelectionTextColour`(*self*, *col*)[¶](#wx.propgrid.PropertyGrid.SetSelectionTextColour "Permalink to this definition")
Sets selection foreground colour - applies to selected property name text.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSplitterLeft(self, privateChildrenToo: bool=False) -> None:
        """ 

`SetSplitterLeft`(*self*, *privateChildrenToo=False*)[¶](#wx.propgrid.PropertyGrid.SetSplitterLeft "Permalink to this definition")
Moves splitter as left as possible, while still allowing all labels to be shown in full.



Parameters
**privateChildrenToo** (*bool*) – If `False`, will still allow private children to be cropped.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetSplitterPosition(self, newxpos, col=0) -> None:
        """ 

`SetSplitterPosition`(*self*, *newxpos*, *col=0*)[¶](#wx.propgrid.PropertyGrid.SetSplitterPosition "Permalink to this definition")
Sets x coordinate of the splitter.



Parameters
* **newxpos** (*int*) –
* **col** (*int*) –





Note


Splitter position cannot exceed grid size, and therefore setting it during form creation may fail as initial grid size is often smaller than desired splitter position, especially when sizers are being used.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetTargetRect(self, rect: 'Rect') -> None:
        """ 

`SetTargetRect`(*self*, *rect*)[¶](#wx.propgrid.PropertyGrid.SetTargetRect "Permalink to this definition")

Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetTargetWindow(self, window: 'Window') -> None:
        """ 

`SetTargetWindow`(*self*, *window*)[¶](#wx.propgrid.PropertyGrid.SetTargetWindow "Permalink to this definition")
Call this function to tell  [wx.Scrolled](wx.Scrolled.html#wx-scrolled) to perform the actual scrolling on a different window (and not on itself).


This method is useful when only a part of the window should be scrolled. A typical example is a control consisting of a fixed header and the scrollable contents window: the scrollbars are attached to the main window itself, hence it, and not the contents window must be derived from  [wx.Scrolled](wx.Scrolled.html#wx-scrolled), but only the contents window scrolls when the scrollbars are used. To implement such setup, you need to call this method with the contents window as argument.


Notice that if this method is used, [`GetSizeAvailableForScrollTarget`](#wx.propgrid.PropertyGrid.GetSizeAvailableForScrollTarget "wx.propgrid.PropertyGrid.GetSizeAvailableForScrollTarget") method must be overridden.



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetUnspecifiedValueAppearance(self, cell: 'propgrid.PGCell') -> None:
        """ 

`SetUnspecifiedValueAppearance`(*self*, *cell*)[¶](#wx.propgrid.PropertyGrid.SetUnspecifiedValueAppearance "Permalink to this definition")
Sets appearance of value cells representing an unspecified property value.


Default appearance is blank.



Parameters
**cell** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) – 





Note


If you set the unspecified value to have any textual representation, then that will override “InlineHelp” attribute.




See also


[`wx.propgrid.PGProperty.SetValueToUnspecified`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetValueToUnspecified "wx.propgrid.PGProperty.SetValueToUnspecified") , [`wx.propgrid.PGProperty.IsValueUnspecified`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.IsValueUnspecified "wx.propgrid.PGProperty.IsValueUnspecified")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetVerticalSpacing(self, vspacing: int) -> None:
        """ 

`SetVerticalSpacing`(*self*, *vspacing*)[¶](#wx.propgrid.PropertyGrid.SetVerticalSpacing "Permalink to this definition")
Sets vertical spacing.


Can be 1, 2, or 3 - a value relative to font height. Value of 2 should be default on most platforms.



Parameters
**vspacing** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetVirtualWidth(self, width: int) -> None:
        """ 

`SetVirtualWidth`(*self*, *width*)[¶](#wx.propgrid.PropertyGrid.SetVirtualWidth "Permalink to this definition")
Set virtual width for this particular page.


Width -1 indicates that the virtual width should be disabled.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def SetupTextCtrlValue(self, text: str) -> None:
        """ 

`SetupTextCtrlValue`(*self*, *text*)[¶](#wx.propgrid.PropertyGrid.SetupTextCtrlValue "Permalink to this definition")
Must be called in [`wx.propgrid.PGEditor.CreateControls`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.CreateControls "wx.propgrid.PGEditor.CreateControls") if primary editor window is  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl), just before textctrl is created.



Parameters
**text** (*string*) – Initial text value of created  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl).






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShouldScrollToChildOnFocus(self, child: 'Window') -> bool:
        """ 

`ShouldScrollToChildOnFocus`(*self*, *child*)[¶](#wx.propgrid.PropertyGrid.ShouldScrollToChildOnFocus "Permalink to this definition")
This method can be overridden in a derived class to prevent scrolling the child window into view automatically when it gets focus.


The default behaviour is to scroll this window to show its currently focused child automatically, to ensure that the user can interact with it. This is usually helpful, but can be undesirable for some windows, in which case this method can be overridden to return `False` for them to prevent any scrolling from taking place when such windows get focus.



Parameters
**child** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShowPropertyError(self, id, msg) -> None:
        """ 

`ShowPropertyError`(*self*, *id*, *msg*)[¶](#wx.propgrid.PropertyGrid.ShowPropertyError "Permalink to this definition")
Shows a brief error message that is related to a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **msg** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ShowScrollbars(self, horz, vert) -> None:
        """ 

`ShowScrollbars`(*self*, *horz*, *vert*)[¶](#wx.propgrid.PropertyGrid.ShowScrollbars "Permalink to this definition")
Set the scrollbar visibility.


By default the scrollbar in the corresponding direction is only shown if it is needed, i.e. if the virtual size of the scrolled window in this direction is greater than the current physical window size. Using this function the scrollbar visibility can be changed to be:


* `wx.SHOW_SB_ALWAYS`: To always show the scrollbar, even if it is not needed currently (wx``wx.ALWAYS\_SHOW\_SB`` style can be used during the window creation to achieve the same effect but it applies in both directions).
* `wx.SHOW_SB_NEVER`: To never show the scrollbar at all. In this case the program should presumably provide some other way for the user to scroll the window.
* `wx.SHOW_SB_DEFAULT`: To restore the default behaviour described above.


Note that the window must be created before calling this method.



Parameters
* **horz** ([*ScrollbarVisibility*](wx.ScrollbarVisibility.enumeration.html "ScrollbarVisibility")) – The desired visibility for the horizontal scrollbar.
* **vert** ([*ScrollbarVisibility*](wx.ScrollbarVisibility.enumeration.html "ScrollbarVisibility")) – The desired visibility for the vertical scrollbar.





New in version 2.9.0.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def StopAutoScrolling(self) -> None:
        """ 

`StopAutoScrolling`(*self*)[¶](#wx.propgrid.PropertyGrid.StopAutoScrolling "Permalink to this definition")
Stop generating the scroll events when mouse is held outside the window.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def UnfocusEditor(self) -> bool:
        """ 

`UnfocusEditor`(*self*)[¶](#wx.propgrid.PropertyGrid.UnfocusEditor "Permalink to this definition")
Unfocuses or closes editor if one was open, but does not deselect property.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def ValueChangeInEvent(self, variant: PGVariant) -> None:
        """ 

`ValueChangeInEvent`(*self*, *variant*)[¶](#wx.propgrid.PropertyGrid.ValueChangeInEvent "Permalink to this definition")
Call this from [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") to cause property value to be changed after the function returns (with `True` as return value).


[`ValueChangeInEvent`](#wx.propgrid.PropertyGrid.ValueChangeInEvent "wx.propgrid.PropertyGrid.ValueChangeInEvent") must be used if you wish the application to be able to use wxEVT\_PG\_CHANGING to potentially veto the given value.



Parameters
**variant** (*PGVariant*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    def WasValueChangedInEvent(self) -> bool:
        """ 

`WasValueChangedInEvent`(*self*)[¶](#wx.propgrid.PropertyGrid.WasValueChangedInEvent "Permalink to this definition")
You can use this member function, for instance, to detect in [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") if [`wx.propgrid.PGProperty.SetValueInEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetValueInEvent "wx.propgrid.PGProperty.SetValueInEvent") was already called in [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") .


It really only detects if was value was changed using [`wx.propgrid.PGProperty.SetValueInEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetValueInEvent "wx.propgrid.PGProperty.SetValueInEvent") , which is usually used when a ‘picker’ dialog is displayed. If value was written by “normal means” in [`wx.propgrid.PGProperty.StringToValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.StringToValue "wx.propgrid.PGProperty.StringToValue") or IntToValue(), then this function will return `False` (on the other hand, [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") is not even called in those cases).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGrid.html
        """

    CaptionBackgroundColour: 'Colour'  # `CaptionBackgroundColour`[¶](#wx.propgrid.PropertyGrid.CaptionBackgroundColour "Permalink to this definition")See [`GetCaptionBackgroundColour`](#wx.propgrid.PropertyGrid.GetCaptionBackgroundColour "wx.propgrid.PropertyGrid.GetCaptionBackgroundColour") and [`SetCaptionBackgroundColour`](#wx.propgrid.PropertyGrid.SetCaptionBackgroundColour "wx.propgrid.PropertyGrid.SetCaptionBackgroundColour")
    CaptionFont: 'Font'  # `CaptionFont`[¶](#wx.propgrid.PropertyGrid.CaptionFont "Permalink to this definition")See [`GetCaptionFont`](#wx.propgrid.PropertyGrid.GetCaptionFont "wx.propgrid.PropertyGrid.GetCaptionFont")
    CaptionForegroundColour: 'Colour'  # `CaptionForegroundColour`[¶](#wx.propgrid.PropertyGrid.CaptionForegroundColour "Permalink to this definition")See [`GetCaptionForegroundColour`](#wx.propgrid.PropertyGrid.GetCaptionForegroundColour "wx.propgrid.PropertyGrid.GetCaptionForegroundColour")
    CellBackgroundColour: 'Colour'  # `CellBackgroundColour`[¶](#wx.propgrid.PropertyGrid.CellBackgroundColour "Permalink to this definition")See [`GetCellBackgroundColour`](#wx.propgrid.PropertyGrid.GetCellBackgroundColour "wx.propgrid.PropertyGrid.GetCellBackgroundColour") and [`SetCellBackgroundColour`](#wx.propgrid.PropertyGrid.SetCellBackgroundColour "wx.propgrid.PropertyGrid.SetCellBackgroundColour")
    CellDisabledTextColour: 'Colour'  # `CellDisabledTextColour`[¶](#wx.propgrid.PropertyGrid.CellDisabledTextColour "Permalink to this definition")See [`GetCellDisabledTextColour`](#wx.propgrid.PropertyGrid.GetCellDisabledTextColour "wx.propgrid.PropertyGrid.GetCellDisabledTextColour") and [`SetCellDisabledTextColour`](#wx.propgrid.PropertyGrid.SetCellDisabledTextColour "wx.propgrid.PropertyGrid.SetCellDisabledTextColour")
    CellTextColour: 'Colour'  # `CellTextColour`[¶](#wx.propgrid.PropertyGrid.CellTextColour "Permalink to this definition")See [`GetCellTextColour`](#wx.propgrid.PropertyGrid.GetCellTextColour "wx.propgrid.PropertyGrid.GetCellTextColour") and [`SetCellTextColour`](#wx.propgrid.PropertyGrid.SetCellTextColour "wx.propgrid.PropertyGrid.SetCellTextColour")
    ColumnCount: int  # `ColumnCount`[¶](#wx.propgrid.PropertyGrid.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.propgrid.PropertyGrid.GetColumnCount "wx.propgrid.PropertyGrid.GetColumnCount") and [`SetColumnCount`](#wx.propgrid.PropertyGrid.SetColumnCount "wx.propgrid.PropertyGrid.SetColumnCount")
    EditorTextCtrl: 'TextCtrl'  # `EditorTextCtrl`[¶](#wx.propgrid.PropertyGrid.EditorTextCtrl "Permalink to this definition")See [`GetEditorTextCtrl`](#wx.propgrid.PropertyGrid.GetEditorTextCtrl "wx.propgrid.PropertyGrid.GetEditorTextCtrl")
    EmptySpaceColour: 'Colour'  # `EmptySpaceColour`[¶](#wx.propgrid.PropertyGrid.EmptySpaceColour "Permalink to this definition")See [`GetEmptySpaceColour`](#wx.propgrid.PropertyGrid.GetEmptySpaceColour "wx.propgrid.PropertyGrid.GetEmptySpaceColour") and [`SetEmptySpaceColour`](#wx.propgrid.PropertyGrid.SetEmptySpaceColour "wx.propgrid.PropertyGrid.SetEmptySpaceColour")
    FontHeight: int  # `FontHeight`[¶](#wx.propgrid.PropertyGrid.FontHeight "Permalink to this definition")See [`GetFontHeight`](#wx.propgrid.PropertyGrid.GetFontHeight "wx.propgrid.PropertyGrid.GetFontHeight")
    Grid: 'PropertyGrid'  # `Grid`[¶](#wx.propgrid.PropertyGrid.Grid "Permalink to this definition")See [`GetGrid`](#wx.propgrid.PropertyGrid.GetGrid "wx.propgrid.PropertyGrid.GetGrid")
    ImageSize: 'Size'  # `ImageSize`[¶](#wx.propgrid.PropertyGrid.ImageSize "Permalink to this definition")See [`GetImageSize`](#wx.propgrid.PropertyGrid.GetImageSize "wx.propgrid.PropertyGrid.GetImageSize")
    LabelEditor: 'TextCtrl'  # `LabelEditor`[¶](#wx.propgrid.PropertyGrid.LabelEditor "Permalink to this definition")See [`GetLabelEditor`](#wx.propgrid.PropertyGrid.GetLabelEditor "wx.propgrid.PropertyGrid.GetLabelEditor")
    LastItem: 'PGProperty'  # `LastItem`[¶](#wx.propgrid.PropertyGrid.LastItem "Permalink to this definition")See [`GetLastItem`](#wx.propgrid.PropertyGrid.GetLastItem "wx.propgrid.PropertyGrid.GetLastItem")
    LineColour: 'Colour'  # `LineColour`[¶](#wx.propgrid.PropertyGrid.LineColour "Permalink to this definition")See [`GetLineColour`](#wx.propgrid.PropertyGrid.GetLineColour "wx.propgrid.PropertyGrid.GetLineColour") and [`SetLineColour`](#wx.propgrid.PropertyGrid.SetLineColour "wx.propgrid.PropertyGrid.SetLineColour")
    MarginColour: 'Colour'  # `MarginColour`[¶](#wx.propgrid.PropertyGrid.MarginColour "Permalink to this definition")See [`GetMarginColour`](#wx.propgrid.PropertyGrid.GetMarginColour "wx.propgrid.PropertyGrid.GetMarginColour") and [`SetMarginColour`](#wx.propgrid.PropertyGrid.SetMarginColour "wx.propgrid.PropertyGrid.SetMarginColour")
    MarginWidth: int  # `MarginWidth`[¶](#wx.propgrid.PropertyGrid.MarginWidth "Permalink to this definition")See [`GetMarginWidth`](#wx.propgrid.PropertyGrid.GetMarginWidth "wx.propgrid.PropertyGrid.GetMarginWidth")
    Panel: 'Window'  # `Panel`[¶](#wx.propgrid.PropertyGrid.Panel "Permalink to this definition")See [`GetPanel`](#wx.propgrid.PropertyGrid.GetPanel "wx.propgrid.PropertyGrid.GetPanel")
    Root: 'PGProperty'  # `Root`[¶](#wx.propgrid.PropertyGrid.Root "Permalink to this definition")See [`GetRoot`](#wx.propgrid.PropertyGrid.GetRoot "wx.propgrid.PropertyGrid.GetRoot")
    RowHeight: int  # `RowHeight`[¶](#wx.propgrid.PropertyGrid.RowHeight "Permalink to this definition")See [`GetRowHeight`](#wx.propgrid.PropertyGrid.GetRowHeight "wx.propgrid.PropertyGrid.GetRowHeight")
    ScaleX: float  # `ScaleX`[¶](#wx.propgrid.PropertyGrid.ScaleX "Permalink to this definition")See [`GetScaleX`](#wx.propgrid.PropertyGrid.GetScaleX "wx.propgrid.PropertyGrid.GetScaleX")
    ScaleY: float  # `ScaleY`[¶](#wx.propgrid.PropertyGrid.ScaleY "Permalink to this definition")See [`GetScaleY`](#wx.propgrid.PropertyGrid.GetScaleY "wx.propgrid.PropertyGrid.GetScaleY")
    SelectedProperty: 'PGProperty'  # `SelectedProperty`[¶](#wx.propgrid.PropertyGrid.SelectedProperty "Permalink to this definition")See [`GetSelectedProperty`](#wx.propgrid.PropertyGrid.GetSelectedProperty "wx.propgrid.PropertyGrid.GetSelectedProperty")
    Selection: 'PGProperty'  # `Selection`[¶](#wx.propgrid.PropertyGrid.Selection "Permalink to this definition")See [`GetSelection`](#wx.propgrid.PropertyGrid.GetSelection "wx.propgrid.PropertyGrid.GetSelection") and [`SetSelection`](#wx.propgrid.PropertyGrid.SetSelection "wx.propgrid.PropertyGrid.SetSelection")
    SelectionBackgroundColour: 'Colour'  # `SelectionBackgroundColour`[¶](#wx.propgrid.PropertyGrid.SelectionBackgroundColour "Permalink to this definition")See [`GetSelectionBackgroundColour`](#wx.propgrid.PropertyGrid.GetSelectionBackgroundColour "wx.propgrid.PropertyGrid.GetSelectionBackgroundColour") and [`SetSelectionBackgroundColour`](#wx.propgrid.PropertyGrid.SetSelectionBackgroundColour "wx.propgrid.PropertyGrid.SetSelectionBackgroundColour")
    SelectionForegroundColour: 'Colour'  # `SelectionForegroundColour`[¶](#wx.propgrid.PropertyGrid.SelectionForegroundColour "Permalink to this definition")See [`GetSelectionForegroundColour`](#wx.propgrid.PropertyGrid.GetSelectionForegroundColour "wx.propgrid.PropertyGrid.GetSelectionForegroundColour")
    SplitterPosition: int  # `SplitterPosition`[¶](#wx.propgrid.PropertyGrid.SplitterPosition "Permalink to this definition")See [`GetSplitterPosition`](#wx.propgrid.PropertyGrid.GetSplitterPosition "wx.propgrid.PropertyGrid.GetSplitterPosition") and [`SetSplitterPosition`](#wx.propgrid.PropertyGrid.SetSplitterPosition "wx.propgrid.PropertyGrid.SetSplitterPosition")
    StatusBar: '_StatusBar'  # `StatusBar`[¶](#wx.propgrid.PropertyGrid.StatusBar "Permalink to this definition")See [`GetStatusBar`](#wx.propgrid.PropertyGrid.GetStatusBar "wx.propgrid.PropertyGrid.GetStatusBar")
    TargetRect: 'Rect'  # `TargetRect`[¶](#wx.propgrid.PropertyGrid.TargetRect "Permalink to this definition")See [`GetTargetRect`](#wx.propgrid.PropertyGrid.GetTargetRect "wx.propgrid.PropertyGrid.GetTargetRect") and [`SetTargetRect`](#wx.propgrid.PropertyGrid.SetTargetRect "wx.propgrid.PropertyGrid.SetTargetRect")
    TargetWindow: 'Window'  # `TargetWindow`[¶](#wx.propgrid.PropertyGrid.TargetWindow "Permalink to this definition")See [`GetTargetWindow`](#wx.propgrid.PropertyGrid.GetTargetWindow "wx.propgrid.PropertyGrid.GetTargetWindow") and [`SetTargetWindow`](#wx.propgrid.PropertyGrid.SetTargetWindow "wx.propgrid.PropertyGrid.SetTargetWindow")
    UncommittedPropertyValue: 'PGVariant'  # `UncommittedPropertyValue`[¶](#wx.propgrid.PropertyGrid.UncommittedPropertyValue "Permalink to this definition")See [`GetUncommittedPropertyValue`](#wx.propgrid.PropertyGrid.GetUncommittedPropertyValue "wx.propgrid.PropertyGrid.GetUncommittedPropertyValue")
    UnspecifiedValueAppearance: 'PGCell'  # `UnspecifiedValueAppearance`[¶](#wx.propgrid.PropertyGrid.UnspecifiedValueAppearance "Permalink to this definition")See [`GetUnspecifiedValueAppearance`](#wx.propgrid.PropertyGrid.GetUnspecifiedValueAppearance "wx.propgrid.PropertyGrid.GetUnspecifiedValueAppearance") and [`SetUnspecifiedValueAppearance`](#wx.propgrid.PropertyGrid.SetUnspecifiedValueAppearance "wx.propgrid.PropertyGrid.SetUnspecifiedValueAppearance")
    UnspecifiedValueText: str  # `UnspecifiedValueText`[¶](#wx.propgrid.PropertyGrid.UnspecifiedValueText "Permalink to this definition")See [`GetUnspecifiedValueText`](#wx.propgrid.PropertyGrid.GetUnspecifiedValueText "wx.propgrid.PropertyGrid.GetUnspecifiedValueText")
    VerticalSpacing: int  # `VerticalSpacing`[¶](#wx.propgrid.PropertyGrid.VerticalSpacing "Permalink to this definition")See [`GetVerticalSpacing`](#wx.propgrid.PropertyGrid.GetVerticalSpacing "wx.propgrid.PropertyGrid.GetVerticalSpacing") and [`SetVerticalSpacing`](#wx.propgrid.PropertyGrid.SetVerticalSpacing "wx.propgrid.PropertyGrid.SetVerticalSpacing")



SHOW_SB_ALWAYS: int

SHOW_SB_NEVER: int

SHOW_SB_DEFAULT: int

class PGWindowList:
    """ **Possible constructors**:



```
PGWindowList(primary, secondary=None)

```


Contains a list of editor windows returned by CreateControls.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
    """
    def __init__(self, primary, secondary=None) -> None:
        """ 

`__init__`(*self*, *primary*, *secondary=None*)[¶](#wx.propgrid.PGWindowList.__init__ "Permalink to this definition")

Parameters
* **primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **secondary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def GetPrimary(self) -> 'Window':
        """ 

`GetPrimary`(*self*)[¶](#wx.propgrid.PGWindowList.GetPrimary "Permalink to this definition")
Gets window of primary editor.



Return type
*Window*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def GetSecondary(self) -> 'Window':
        """ 

`GetSecondary`(*self*)[¶](#wx.propgrid.PGWindowList.GetSecondary "Permalink to this definition")
Gets window of secondary editor.



Return type
*Window*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    def SetSecondary(self, secondary: 'Window') -> None:
        """ 

`SetSecondary`(*self*, *secondary*)[¶](#wx.propgrid.PGWindowList.SetSecondary "Permalink to this definition")

Parameters
**secondary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGWindowList.html
        """

    Primary: 'Window'  # `Primary`[¶](#wx.propgrid.PGWindowList.Primary "Permalink to this definition")See [`GetPrimary`](#wx.propgrid.PGWindowList.GetPrimary "wx.propgrid.PGWindowList.GetPrimary")
    Secondary: 'Window'  # `Secondary`[¶](#wx.propgrid.PGWindowList.Secondary "Permalink to this definition")See [`GetSecondary`](#wx.propgrid.PGWindowList.GetSecondary "wx.propgrid.PGWindowList.GetSecondary") and [`SetSecondary`](#wx.propgrid.PGWindowList.SetSecondary "wx.propgrid.PGWindowList.SetSecondary")



class PGArrayStringEditorDialog(PGArrayEditorDialog):
    """ **Possible constructors**:



```
PGArrayStringEditorDialog()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGArrayStringEditorDialog.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayGet(self, index: int) -> str:
        """ 

`ArrayGet`(*self*, *index*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArrayGet "Permalink to this definition")

Parameters
**index** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayGetCount(self) -> int:
        """ 

`ArrayGetCount`(*self*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArrayGetCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayInsert(self, str, index) -> bool:
        """ 

`ArrayInsert`(*self*, *str*, *index*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArrayInsert "Permalink to this definition")

Parameters
* **str** (*string*) –
* **index** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArrayRemoveAt(self, index: int) -> None:
        """ 

`ArrayRemoveAt`(*self*, *index*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArrayRemoveAt "Permalink to this definition")

Parameters
**index** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArraySet(self, index, str) -> bool:
        """ 

`ArraySet`(*self*, *index*, *str*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArraySet "Permalink to this definition")

Parameters
* **index** (*int*) –
* **str** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def ArraySwap(self, first, second) -> None:
        """ 

`ArraySwap`(*self*, *first*, *second*)[¶](#wx.propgrid.PGArrayStringEditorDialog.ArraySwap "Permalink to this definition")

Parameters
* **first** (*int*) –
* **second** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.propgrid.PGArrayStringEditorDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def GetDialogValue(self) -> 'PGVariant':
        """ 

`GetDialogValue`(*self*)[¶](#wx.propgrid.PGArrayStringEditorDialog.GetDialogValue "Permalink to this definition")
Return value modified by dialog.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.propgrid.PGArrayStringEditorDialog.Init "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def OnCustomNewAction(self, resString: str) -> bool:
        """ 

`OnCustomNewAction`(*self*, *resString*)[¶](#wx.propgrid.PGArrayStringEditorDialog.OnCustomNewAction "Permalink to this definition")

Parameters
**resString** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def SetCustomButton(self, custBtText, pcc) -> None:
        """ 

`SetCustomButton`(*self*, *custBtText*, *pcc*)[¶](#wx.propgrid.PGArrayStringEditorDialog.SetCustomButton "Permalink to this definition")

Parameters
* **custBtText** (*string*) –
* **pcc** (*wx.propgrid.list of stringsProperty*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    def SetDialogValue(self, value: PGVariant) -> None:
        """ 

`SetDialogValue`(*self*, *value*)[¶](#wx.propgrid.PGArrayStringEditorDialog.SetDialogValue "Permalink to this definition")
Set value modified by dialog.



Parameters
**value** (*PGVariant*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGArrayStringEditorDialog.html
        """

    DialogValue: 'PGVariant'  # `DialogValue`[¶](#wx.propgrid.PGArrayStringEditorDialog.DialogValue "Permalink to this definition")See [`GetDialogValue`](#wx.propgrid.PGArrayStringEditorDialog.GetDialogValue "wx.propgrid.PGArrayStringEditorDialog.GetDialogValue") and [`SetDialogValue`](#wx.propgrid.PGArrayStringEditorDialog.SetDialogValue "wx.propgrid.PGArrayStringEditorDialog.SetDialogValue")



class PropertyGridInterface:
    """ Most of the shared property manipulation interface shared by
PropertyGrid, PropertyGridPage, and PropertyGridManager is
defined in this class.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
    """
    def Append(self, property: 'propgrid.PGProperty') -> 'PGProperty':
        """ 

`Append`(*self*, *property*)[¶](#wx.propgrid.PropertyGridInterface.Append "Permalink to this definition")
Appends property to the list.


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) assumes ownership of the object. Becomes child of most recently added category.



Parameters
**property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


* [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) takes the ownership of the property pointer.
* If appending a category with name identical to a category already in the  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), then newly created category is deleted, and most recently added category (under which properties are appended) is set to the one with same name. This allows easier adding of items to same categories in multiple passes.
* Does not automatically redraw the control, so you may need to call Refresh() when calling this function after control has been shown for the first time.
* This functions deselects selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def AppendIn(self, id, newProperty) -> 'PGProperty':
        """ 

`AppendIn`(*self*, *id*, *newProperty*)[¶](#wx.propgrid.PropertyGridInterface.AppendIn "Permalink to this definition")
Same as [`Append`](#wx.propgrid.PropertyGridInterface.Append "wx.propgrid.PropertyGridInterface.Append") , but appends under given parent property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer to parent property.
* **newProperty** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property to be added.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def AutoFill(self, obj, parent=None) -> None:
        """ 

`AutoFill`(*self*, *obj*, *parent=None*)[¶](#wx.propgrid.PropertyGridInterface.AutoFill "Permalink to this definition")
“Clears properties and re-fills to match members and values of
the given object or dictionary obj.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def BeginAddChildren(self, id: 'propgrid.PGPropArgCls') -> None:
        """ 

`BeginAddChildren`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.BeginAddChildren "Permalink to this definition")
In order to add new items into a property with private children (for instance,  [wx.propgrid.FlagsProperty](wx.propgrid.FlagsProperty.html#wx-propgrid-flagsproperty)), you need to call this method.


After populating has been finished, you need to call [`EndAddChildren`](#wx.propgrid.PropertyGridInterface.EndAddChildren "wx.propgrid.PropertyGridInterface.EndAddChildren") .



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 





See also


[`EndAddChildren`](#wx.propgrid.PropertyGridInterface.EndAddChildren "wx.propgrid.PropertyGridInterface.EndAddChildren")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ChangePropertyValue(self, id, newValue) -> bool:
        """ 

`ChangePropertyValue`(*self*, *id*, *newValue*)[¶](#wx.propgrid.PropertyGridInterface.ChangePropertyValue "Permalink to this definition")
Changes value of a property, as if by user.


Use this instead of [`SetPropertyValue`](#wx.propgrid.PropertyGridInterface.SetPropertyValue "wx.propgrid.PropertyGridInterface.SetPropertyValue") if you need the value to run through validation process, and also send `wxEVT_PG_CHANGED` .



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **newValue** (*PGVariant*) –



Return type
*bool*



Returns
Returns `True` if value was successfully changed.





Note


Since this function sends `wxEVT_PG_CHANGED` , it should not be called from `EVT_PG_CHANGED` handler.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PropertyGridInterface.Clear "Permalink to this definition")
Deletes all properties.



Note


This functions deselects selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ClearModifiedStatus(self) -> None:
        """ 

`ClearModifiedStatus`(*self*)[¶](#wx.propgrid.PropertyGridInterface.ClearModifiedStatus "Permalink to this definition")
Resets modified status of all properties.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ClearSelection(self, validation: bool=False) -> bool:
        """ 

`ClearSelection`(*self*, *validation=False*)[¶](#wx.propgrid.PropertyGridInterface.ClearSelection "Permalink to this definition")
Clears current selection, if any.



Parameters
**validation** (*bool*) – If set to `False`, deselecting the property will always work, even if its editor had invalid value in it.



Return type
*bool*



Returns
Returns `True` if successful or if there was no selection. May fail if validation was enabled and active editor had invalid value.





Note


In wxWidgets 2.9 and later, this function no longer sends `PG_EVT_SELECTED` .




See also


[`wx.propgrid.PropertyGrid.SelectProperty`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.SelectProperty "wx.propgrid.PropertyGrid.SelectProperty")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Collapse(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`Collapse`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.Collapse "Permalink to this definition")
Collapses given category or property with children.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*



Returns
Returns `True` if actually collapsed.





Note


This function may deselect selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def CollapseAll(self) -> bool:
        """ 

`CollapseAll`(*self*)[¶](#wx.propgrid.PropertyGridInterface.CollapseAll "Permalink to this definition")
Collapses all items that can be collapsed.



Return type
*bool*



Returns
Return `False` if failed (may fail if editor value cannot be validated).





Note


This functions clears selection. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DeleteProperty(self, id: 'propgrid.PGPropArgCls') -> None:
        """ 

`DeleteProperty`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.DeleteProperty "Permalink to this definition")
Removes and deletes a property and any children.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Pointer or name of a property.




This functions deselects selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.



Note


If you delete a property in a  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) event handler, the actual deletion is postponed until the next idle event.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DisableProperty(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`DisableProperty`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.DisableProperty "Permalink to this definition")
Disables a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*





Note


Property is refreshed with new settings.




See also


[`EnableProperty`](#wx.propgrid.PropertyGridInterface.EnableProperty "wx.propgrid.PropertyGridInterface.EnableProperty") , [`wx.propgrid.PGProperty.Enable`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.Enable "wx.propgrid.PGProperty.Enable")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DoDefaultTypeMappings(self) -> None:
        """ 

`DoDefaultTypeMappings`(*self*)[¶](#wx.propgrid.PropertyGridInterface.DoDefaultTypeMappings "Permalink to this definition")
Add built-in properties to the map.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def DoDefaultValueTypeMappings(self) -> None:
        """ 

`DoDefaultValueTypeMappings`(*self*)[¶](#wx.propgrid.PropertyGridInterface.DoDefaultValueTypeMappings "Permalink to this definition")
Map pg value type ids to getter methods.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EditorValidate(self) -> bool:
        """ 

`EditorValidate`(*self*)[¶](#wx.propgrid.PropertyGridInterface.EditorValidate "Permalink to this definition")
Returns `True` if all property grid data changes have been committed.


Usually only returns `False` if value in active editor has been invalidated by a  [wx.Validator](wx.Validator.html#wx-validator).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EnableProperty(self, id, enable=True) -> bool:
        """ 

`EnableProperty`(*self*, *id*, *enable=True*)[¶](#wx.propgrid.PropertyGridInterface.EnableProperty "Permalink to this definition")
Enables or disables property.


Disabled property usually appears as having grey text.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer to a property.
* **enable** (*bool*) – If `False`, property is disabled instead.



Return type
*bool*





Note


Property is refreshed with new settings.




See also


[`wx.propgrid.PGProperty.Enable`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.Enable "wx.propgrid.PGProperty.Enable")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def EndAddChildren(self, id: 'propgrid.PGPropArgCls') -> None:
        """ 

`EndAddChildren`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.EndAddChildren "Permalink to this definition")
Called after population of property with fixed children has finished.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 





See also


[`BeginAddChildren`](#wx.propgrid.PropertyGridInterface.BeginAddChildren "wx.propgrid.PropertyGridInterface.BeginAddChildren")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Expand(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`Expand`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.Expand "Permalink to this definition")
Expands given category or property with children.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*



Returns
Returns `True` if actually expanded.





Note


This function may deselect selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ExpandAll(self, expand: bool=True) -> bool:
        """ 

`ExpandAll`(*self*, *expand=True*)[¶](#wx.propgrid.PropertyGridInterface.ExpandAll "Permalink to this definition")
Expands all items that can be expanded.



Parameters
**expand** (*bool*) – 



Return type
*bool*





Note


This functions clears selection. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetColumnProportion(self, column: int) -> int:
        """ 

`GetColumnProportion`(*self*, *column*)[¶](#wx.propgrid.PropertyGridInterface.GetColumnProportion "Permalink to this definition")
Returns auto-resize proportion of the given column.



Parameters
**column** (*int*) – 



Return type
*int*





See also


[`SetColumnProportion`](#wx.propgrid.PropertyGridInterface.SetColumnProportion "wx.propgrid.PropertyGridInterface.SetColumnProportion")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def GetEditorByName(editorName: str) -> 'PGEditor':
        """ 

*static* `GetEditorByName`(*editorName*)[¶](#wx.propgrid.PropertyGridInterface.GetEditorByName "Permalink to this definition")
Returns editor pointer of editor with given name.



Parameters
**editorName** (*string*) – 



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetFirst(self, flags: int=PG_ITERATE_ALL) -> 'PGProperty':
        """ 

`GetFirst`(*self*, *flags=PG\_ITERATE\_ALL*)[¶](#wx.propgrid.PropertyGridInterface.GetFirst "Permalink to this definition")
Returns id of first item that matches given criteria.



Parameters
**flags** (*int*) – See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags).



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetFirstChild(self, id: 'propgrid.PGPropArgCls') -> 'PGProperty':
        """ 

`GetFirstChild`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetFirstChild "Permalink to this definition")
Returns id of first child of given property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


Does not return private children!





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetIterator(self, *args, **kw) -> 'PropertyGridIterator':
        """ 

`GetIterator`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridInterface.GetIterator "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetIterator** *(self, flags=PG\_ITERATE\_DEFAULT, firstProp=None)*


Returns iterator class instance.



Parameters
* **flags** (*int*) – See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags). Value `wx.propgrid.PG_ITERATE_DEFAULT` causes iteration over everything except private child properties.
* **firstProp** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property to start iteration from. If `None`, then first child of root is used.



Return type
 [wx.propgrid.PropertyGridIterator](wx.propgrid.PropertyGridIterator.html#wx-propgrid-propertygriditerator)






---

  



**GetIterator** *(self, flags, startPos)*


Returns iterator class instance.



Parameters
* **flags** (*int*) – See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags). Value `wx.propgrid.PG_ITERATE_DEFAULT` causes iteration over everything except private child properties.
* **startPos** (*int*) – Either `wx.TOP` or `wx.BOTTOM`. `wx.TOP` will indicate that iterations start from the first property from the top, and `wx.BOTTOM` means that the iteration will instead begin from bottommost valid item.



Return type
 [wx.propgrid.PropertyGridIterator](wx.propgrid.PropertyGridIterator.html#wx-propgrid-propertygriditerator)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertiesWithFlag(self, targetArr, flags, inverse=False, iterFlags=PG_ITERATE_PROPERTIES|PG_ITERATE_HIDDEN|PG_ITERATE_CATEGORIES) -> None:
        """ 

`GetPropertiesWithFlag`(*self*, *targetArr*, *flags*, *inverse=False*, *iterFlags=PG\_ITERATE\_PROPERTIES|PG\_ITERATE\_HIDDEN|PG\_ITERATE\_CATEGORIES*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertiesWithFlag "Permalink to this definition")
Adds to *targetArr* pointers to properties that have given *flags* set.


However, if *inverse* is set to `True`, then only properties without given flags are stored.



Parameters
* **targetArr** (*ArrayPGProperty*) – Array of pointers to properties in which found properties are stored.
* **flags** (*PGProperty.FlagType*) – Property flags to use.
* **inverse** (*bool*) – If `False`, properties that have given flags are stored, otherwise there are stored only properties without given flags.
* **iterFlags** (*int*) – Iterator flags to use. Default is everything expect private children. See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags).






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetProperty(self, name: str) -> 'PGProperty':
        """ 

`GetProperty`(*self*, *name*)[¶](#wx.propgrid.PropertyGridInterface.GetProperty "Permalink to this definition")
Returns pointer to a property with given name (case-sensitive).


If there is no property with such name, `None` pointer is returned.



Parameters
**name** (*string*) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


Properties which have non-category, non-root parent cannot be accessed globally by their name. Instead, use “<property>.<subproperty>” instead of “<subproperty>”.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyAttribute(self, id, attrName) -> 'PGVariant':
        """ 

`GetPropertyAttribute`(*self*, *id*, *attrName*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyAttribute "Permalink to this definition")
Returns value of given attribute.


If none found, returns NullVariant.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **attrName** (*string*) –



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyAttributes(self, id: 'propgrid.PGPropArgCls') -> 'PGAttributeStorage':
        """ 

`GetPropertyAttributes`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyAttributes "Permalink to this definition")
Returns map-like storage of property’s attributes.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
 [wx.propgrid.PGAttributeStorage](wx.propgrid.PGAttributeStorage.html#wx-propgrid-pgattributestorage)





Note


Note that if extra style `PG_EX_WRITEONLY_BUILTIN_ATTRIBUTES` is set, then builtin-attributes are not included in the storage.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyBackgroundColour(self, id: 'propgrid.PGPropArgCls') -> 'Colour':
        """ 

`GetPropertyBackgroundColour`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyBackgroundColour "Permalink to this definition")
Returns background colour of first cell of a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByLabel(self, label: str) -> 'PGProperty':
        """ 

`GetPropertyByLabel`(*self*, *label*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyByLabel "Permalink to this definition")
Returns first property which label matches given string.


`None` if none found. Note that this operation is very slow when compared to [`GetPropertyByName`](#wx.propgrid.PropertyGridInterface.GetPropertyByName "wx.propgrid.PropertyGridInterface.GetPropertyByName") .



Parameters
**label** (*string*) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByName(self, *args, **kw) -> 'PGProperty':
        """ 

`GetPropertyByName`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyByName "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetPropertyByName** *(self, name)*


Returns pointer to a property with given name (case-sensitive).


If there is no property with such name, `None` pointer is returned.



Parameters
**name** (*string*) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


Properties which have non-category, non-root parent cannot be accessed globally by their name. Instead, use “<property>.<subproperty>” instead of “<subproperty>”.





---

  



**GetPropertyByName** *(self, name, subname)*


Returns child property *subname* of property *name*.


Same as calling GetPropertyByName(“name.subname”), albeit slightly faster.



Parameters
* **name** (*string*) –
* **subname** (*string*) –



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyByNameA(self, name: str) -> 'PGProperty':
        """ 

`GetPropertyByNameA`(*self*, *name*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyByNameA "Permalink to this definition")
[`GetPropertyByName`](#wx.propgrid.PropertyGridInterface.GetPropertyByName "wx.propgrid.PropertyGridInterface.GetPropertyByName") with assertion error message.



Parameters
**name** (*string*) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyCategory(self, id: 'propgrid.PGPropArgCls') -> 'PropertyCategory':
        """ 

`GetPropertyCategory`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyCategory "Permalink to this definition")
Returns pointer of property’s nearest parent category.


If no category found, returns `None`.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
 [wx.propgrid.PropertyCategory](wx.propgrid.PropertyCategory.html#wx-propgrid-propertycategory)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyClientData(self, p) -> None:
        """ 

`GetPropertyClientData`(*self*, *p*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyClientData "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyEditor(self, id: 'propgrid.PGPropArgCls') -> 'PGEditor':
        """ 

`GetPropertyEditor`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyEditor "Permalink to this definition")
Returns property’s editor.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
 [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyHelpString(self, id: 'propgrid.PGPropArgCls') -> str:
        """ 

`GetPropertyHelpString`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyHelpString "Permalink to this definition")
Returns help string associated with a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyImage(self, id: 'propgrid.PGPropArgCls') -> 'Bitmap':
        """ 

`GetPropertyImage`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyImage "Permalink to this definition")
Returns property’s custom value image (`None` of none).



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyLabel(self, id: 'propgrid.PGPropArgCls') -> str:
        """ 

`GetPropertyLabel`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyLabel "Permalink to this definition")
Returns label of a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyName(self, property: 'propgrid.PGProperty') -> str:
        """ 

`GetPropertyName`(*self*, *property*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyName "Permalink to this definition")
Returns property’s name, by which it is globally accessible.



Parameters
**property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyParent(self, id: 'propgrid.PGPropArgCls') -> 'PGProperty':
        """ 

`GetPropertyParent`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyParent "Permalink to this definition")
Returns parent item of a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyTextColour(self, id: 'propgrid.PGPropArgCls') -> 'Colour':
        """ 

`GetPropertyTextColour`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyTextColour "Permalink to this definition")
Returns text colour of first cell of a property.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValidator(self, id: 'propgrid.PGPropArgCls') -> 'Validator':
        """ 

`GetPropertyValidator`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValidator "Permalink to this definition")
Returns validator of a property as a reference, which you can pass to any number of SetPropertyValidator.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*Validator*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValue(self, id: 'propgrid.PGPropArgCls') -> 'PGVariant':
        """ 

`GetPropertyValue`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValue "Permalink to this definition")
Returns property’s value as *Variant* .


If property value is unspecified, NullVariant is returned.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsArrayInt(self, id: 'propgrid.PGPropArgCls') -> int:
        """ 

`GetPropertyValueAsArrayInt`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsArrayInt "Permalink to this definition")
Return’s property’s value as ArrayInt.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsArrayString(self, id: 'propgrid.PGPropArgCls') -> list[str]:
        """ 

`GetPropertyValueAsArrayString`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsArrayString "Permalink to this definition")
Returns property’s value as list of strings .



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsBool(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`GetPropertyValueAsBool`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsBool "Permalink to this definition")
Returns property’s value as bool.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsDateTime(self, id: 'propgrid.PGPropArgCls') -> 'DateTime':
        """ 

`GetPropertyValueAsDateTime`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsDateTime "Permalink to this definition")
Return’s property’s value as  [wx.DateTime](wx.DateTime.html#wx-datetime).



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsDouble(self, id: 'propgrid.PGPropArgCls') -> float:
        """ 

`GetPropertyValueAsDouble`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsDouble "Permalink to this definition")
Returns property’s value as double-precision floating point number.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*float*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsInt(self, id: 'propgrid.PGPropArgCls') -> int:
        """ 

`GetPropertyValueAsInt`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsInt "Permalink to this definition")
Returns property’s value as integer.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsLong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ 

`GetPropertyValueAsLong`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsLong "Permalink to this definition")
Returns property’s value as integer.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsLongLong(self, id: 'propgrid.PGPropArgCls') -> 'LongLong_t':
        """ 

`GetPropertyValueAsLongLong`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsLongLong "Permalink to this definition")
Returns property’s value as native signed 64-bit integer.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*LongLong\_t*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsString(self, id: 'propgrid.PGPropArgCls') -> str:
        """ 

`GetPropertyValueAsString`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsString "Permalink to this definition")
Returns property’s value as *String* .


If property does not use string value type, then its value is converted using [`wx.propgrid.PGProperty.GetValueAsString`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GetValueAsString "wx.propgrid.PGProperty.GetValueAsString") .



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsULong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ 

`GetPropertyValueAsULong`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsULong "Permalink to this definition")
Returns property’s value as integer.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValueAsULongLong(self, id: 'propgrid.PGPropArgCls') -> int:
        """ 

`GetPropertyValueAsULongLong`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValueAsULongLong "Permalink to this definition")
Returns property’s value as native 64-bit integer.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*ULongLong\_t*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPropertyValues(self, dict_=None, as_strings=False, inc_attributes=False, flags=PG_ITERATE_PROPERTIES) -> None:
        """ 

`GetPropertyValues`(*self*, *dict\_=None*, *as\_strings=False*, *inc\_attributes=False*, *flags=PG\_ITERATE\_PROPERTIES*)[¶](#wx.propgrid.PropertyGridInterface.GetPropertyValues "Permalink to this definition")
Returns all property values in the grid.



Parameters
* **dict\_** – A diftionary to fill with the property values.
If not given, then a new one is created. The [dict\_](#id5) can be an
object as well, in which case it’s \_\_dict\_\_ is used.
* **as\_strings** – if True, then string representations of values
are fetched instead of native types. Useful for config and such.
* **inc\_attributes** – if True, then property attributes are added
in the form of `"@<propname>@<attr>"`.
* **flags** – Flags to pass to the iterator. See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags).



Returns
A dictionary with values. It is always a dictionary,
so if [dict\_](#id7) was an object with \_\_dict\_\_ attribute, then that
attribute is returned.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPyIterator(self, flags=PG_ITERATE_DEFAULT, firstProperty=None) -> None:
        """ 

`GetPyIterator`(*self*, *flags=PG\_ITERATE\_DEFAULT*, *firstProperty=None*)[¶](#wx.propgrid.PropertyGridInterface.GetPyIterator "Permalink to this definition")
Returns a pythonic property iterator for a single *PropertyGrid*
or page in *PropertyGridManager* . Arguments are same as for
[`GetIterator`](#wx.propgrid.PropertyGridInterface.GetIterator "wx.propgrid.PropertyGridInterface.GetIterator") .


The following example demonstrates iterating absolutely all items in
a single grid:



```
iterator = propGrid.GetPyIterator(wx.propgrid.PG_ITERATE_ALL)
for prop in iterator:
        print(prop)

```



See also


[`wx.propgrid.PropertyGridInterface.Properties`](#wx.propgrid.PropertyGridInterface.Properties "wx.propgrid.PropertyGridInterface.Properties")
[`wx.propgrid.PropertyGridInterface.Items`](#wx.propgrid.PropertyGridInterface.Items "wx.propgrid.PropertyGridInterface.Items")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetPyVIterator(self, flags=PG_ITERATE_DEFAULT) -> None:
        """ 

`GetPyVIterator`(*self*, *flags=PG\_ITERATE\_DEFAULT*)[¶](#wx.propgrid.PropertyGridInterface.GetPyVIterator "Permalink to this definition")
Similar to [`GetVIterator`](#wx.propgrid.PropertyGridInterface.GetVIterator "wx.propgrid.PropertyGridInterface.GetVIterator") but returns a pythonic iterator.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetSelectedProperties(self) -> 'ArrayPGProperty':
        """ 

`GetSelectedProperties`(*self*)[¶](#wx.propgrid.PropertyGridInterface.GetSelectedProperties "Permalink to this definition")
Returns list of currently selected properties.



Return type
*ArrayPGProperty*





Note


ArrayPGProperty should be compatible with *std.vector* API.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetSelection(self) -> 'PGProperty':
        """ 

`GetSelection`(*self*)[¶](#wx.propgrid.PropertyGridInterface.GetSelection "Permalink to this definition")
Returns currently selected property.


`None` if none.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


When `wx.propgrid.PG_EX_MULTIPLE_SELECTION` extra style is used, this member function returns the focused property, that is the one which can have active editor.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def GetVIterator(self, flags: int) -> 'PGVIterator':
        """ 

`GetVIterator`(*self*, *flags*)[¶](#wx.propgrid.PropertyGridInterface.GetVIterator "Permalink to this definition")
Similar to [`GetIterator`](#wx.propgrid.PropertyGridInterface.GetIterator "wx.propgrid.PropertyGridInterface.GetIterator") , but instead returns  [wx.propgrid.PGVIterator](wx.propgrid.PGVIterator.html#wx-propgrid-pgviterator) instance, which can be useful for forward-iterating through arbitrary property containers.



Parameters
**flags** (*int*) – See  [wx.propgrid.PG\_ITERATOR\_FLAGS](wx.propgrid.PG_ITERATOR_FLAGS.enumeration.html#wx-propgrid-pg-iterator-flags).



Return type
 [wx.propgrid.PGVIterator](wx.propgrid.PGVIterator.html#wx-propgrid-pgviterator)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def HideProperty(self, id, hide=True, flags=PG_RECURSE) -> bool:
        """ 

`HideProperty`(*self*, *id*, *hide=True*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PropertyGridInterface.HideProperty "Permalink to this definition")
Hides or reveals a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer to a property.
* **hide** (*bool*) – If `True`, hides property, otherwise reveals it.
* **flags** (*int*) – By default changes are applied recursively. Set this parameter `wx.propgrid.PG_DONT_RECURSE` to prevent this.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def InitAllTypeHandlers() -> None:
        """ 

*static* `InitAllTypeHandlers`()[¶](#wx.propgrid.PropertyGridInterface.InitAllTypeHandlers "Permalink to this definition")
Initializes *all* property types.


Causes references to most object files in the library, so calling this may cause significant increase in executable size when linking with static library.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Insert(self, *args, **kw) -> 'PGProperty':
        """ 

`Insert`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridInterface.Insert "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Insert** *(self, priorThis, newProperty)*


Inserts property to the property container.



Parameters
* **priorThis** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – New property is inserted just prior to this. Available only in the first variant. There are two versions of this function to allow this parameter to be either an id or name to a property.
* **newProperty** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Pointer to the inserted property.  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will take ownership of this object.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)




* [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) takes the ownership of the property pointer.
* While Append may be faster way to add items, make note that when both types of data storage (categoric and non-categoric) are active, Insert becomes even more slow. This is especially `True` if current mode is non-categoric.
* This functions deselects selected property, if any. Validation failure option `wx.propgrid.PG_VFB_STAY_IN_PROPERTY` is not respected, i.e. selection is cleared even if editor had invalid value.


Example of use:



```
# append category
my_cat_id = thePropGrid.Append(wx.propgrid.PropertyCategory("My Category"))

...

# insert into category - using second variant
my_item_id1 = thePropGrid.Insert(my_cat_id, 0, wx.propgrid.StringProperty("My String 1"))

# insert before to first item - using first variant
my_item_id2 = thePropGrid.Insert(my_item_id, wx.propgrid.StringProperty("My String 2"))

```



Returns
Returns newProperty.






---

  



**Insert** *(self, parent, index, newProperty)*


Inserts property to the property container.


See the other overload for more details.



Parameters
* **parent** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – New property is inserted under this category. Available only in the second variant. There are two versions of this function to allow this parameter to be either an id or name to a property.
* **index** (*int*) – Index under category. Available only in the second variant. If index is < 0, property is appended in category.
* **newProperty** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Pointer to the inserted property.  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will take ownership of this object.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)



Returns
Returns newProperty.






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyCategory(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyCategory`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyCategory "Permalink to this definition")
Returns `True` if property is a category.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyEnabled(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyEnabled`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyEnabled "Permalink to this definition")
Returns `True` if property is enabled.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyExpanded(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyExpanded`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyExpanded "Permalink to this definition")
Returns `True` if given property is expanded.


Naturally, always returns `False` for properties that cannot be expanded.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyModified(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyModified`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyModified "Permalink to this definition")
Returns `True` if property has been modified after value set or modify flag clear by software.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertySelected(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertySelected`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertySelected "Permalink to this definition")
Returns `True` if property is selected.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyShown(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyShown`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyShown "Permalink to this definition")
Returns `True` if property is shown (i.e.


[`HideProperty`](#wx.propgrid.PropertyGridInterface.HideProperty "wx.propgrid.PropertyGridInterface.HideProperty") with `True` not called for it).



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def IsPropertyValueUnspecified(self, id: 'propgrid.PGPropArgCls') -> bool:
        """ 

`IsPropertyValueUnspecified`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.IsPropertyValueUnspecified "Permalink to this definition")
Returns `True` if property value is set to unspecified.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def LimitPropertyEditing(self, id, limit=True) -> None:
        """ 

`LimitPropertyEditing`(*self*, *id*, *limit=True*)[¶](#wx.propgrid.PropertyGridInterface.LimitPropertyEditing "Permalink to this definition")
Disables (*limit* = `True`) or enables (*limit* = `False`)  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) editor of a property, if it is not the sole mean to edit the value.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **limit** (*bool*) –





Note


Property is refreshed with new settings.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def MapType(self, class_, factory: Any) -> None:
        """ 

`MapType`(*self*, *class\_*, *factory*)[¶](#wx.propgrid.PropertyGridInterface.MapType "Permalink to this definition")
Registers Python type/class to property mapping.



Parameters
**factory** – Property builder function/class.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RefreshGrid(self, state: Optional['propgrid.PropertyGridPageState']=None) -> None:
        """ 

`RefreshGrid`(*self*, *state=None*)[¶](#wx.propgrid.PropertyGridInterface.RefreshGrid "Permalink to this definition")
If state is shown in its grid, refresh it now.



Parameters
**state** ([*wx.propgrid.PropertyGridPageState*](wx.propgrid.PropertyGridPageState.html#wx.propgrid.PropertyGridPageState "wx.propgrid.PropertyGridPageState")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RefreshProperty(self, p: 'propgrid.PGProperty') -> None:
        """ 

`RefreshProperty`(*self*, *p*)[¶](#wx.propgrid.PropertyGridInterface.RefreshProperty "Permalink to this definition")

Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 





Note


This function reselects the property and may cause excess flicker, so to just call Refresh() on a rect of single property, call DrawItem() instead.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def RegisterAdditionalEditors() -> None:
        """ 

*static* `RegisterAdditionalEditors`()[¶](#wx.propgrid.PropertyGridInterface.RegisterAdditionalEditors "Permalink to this definition")
Initializes additional property editors (SpinCtrl etc.).


Causes references to most object files in the library, so calling this may cause significant increase in executable size when linking with static library.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RegisterEditor(self, editor, editorName=None) -> None:
        """ 

`RegisterEditor`(*self*, *editor*, *editorName=None*)[¶](#wx.propgrid.PropertyGridInterface.RegisterEditor "Permalink to this definition")
Register a new editor, either an instance or a class.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RemoveProperty(self, id: 'propgrid.PGPropArgCls') -> 'PGProperty':
        """ 

`RemoveProperty`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.RemoveProperty "Permalink to this definition")
Removes a property.


Does not delete the property object, but instead returns it.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Pointer or name of a property.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





Note


Removed property cannot have any children.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def ReplaceProperty(self, id, property) -> 'PGProperty':
        """ 

`ReplaceProperty`(*self*, *id*, *property*)[¶](#wx.propgrid.PropertyGridInterface.ReplaceProperty "Permalink to this definition")
Replaces property with id with newly created one.


For example, this code replaces existing property named “Flags” with one that will have different set of items:



```
pg.ReplaceProperty("Flags",
    wx.propgrid.FlagsProperty("Flags", wx.propgrid.PG_LABEL, newItems))

```



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)





See also


[`Insert`](#wx.propgrid.PropertyGridInterface.Insert "wx.propgrid.PropertyGridInterface.Insert")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def RestoreEditableState(self, src, restoreStates=AllStates) -> bool:
        """ 

`RestoreEditableState`(*self*, *src*, *restoreStates=AllStates*)[¶](#wx.propgrid.PropertyGridInterface.RestoreEditableState "Permalink to this definition")
Restores user-editable state.


See also [`wx.propgrid.PropertyGridInterface.SaveEditableState`](#wx.propgrid.PropertyGridInterface.SaveEditableState "wx.propgrid.PropertyGridInterface.SaveEditableState") .



Parameters
* **src** (*string*) – String generated by SaveEditableState.
* **restoreStates** (*int*) – Which parts to restore from source string. See [list of editable state flags](#wx-propgrid-propertygridinterface).



Return type
*bool*



Returns
Returns `False` if there was problem reading the string.





Note


If some parts of state (such as scrolled or splitter position) fail to restore correctly, please make sure that you call this function after  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) size has been set (this may sometimes be tricky when sizers are used).





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SaveEditableState(self, includedStates: int=AllStates) -> str:
        """ 

`SaveEditableState`(*self*, *includedStates=AllStates*)[¶](#wx.propgrid.PropertyGridInterface.SaveEditableState "Permalink to this definition")
Used to acquire user-editable state (selected property, expanded properties, scrolled position, splitter positions).



Parameters
**includedStates** (*int*) – Which parts of state to include. See [list of editable state flags](#wx-propgrid-propertygridinterface).



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    @staticmethod
    def SetBoolChoices(trueChoice, falseChoice) -> None:
        """ 

*static* `SetBoolChoices`(*trueChoice*, *falseChoice*)[¶](#wx.propgrid.PropertyGridInterface.SetBoolChoices "Permalink to this definition")
Sets strings listed in the choice dropdown of a  [wx.propgrid.BoolProperty](wx.propgrid.BoolProperty.html#wx-propgrid-boolproperty).


Defaults are “True” and “False”, so changing them to, say, “Yes” and “No” may be useful in some less technical applications.



Parameters
* **trueChoice** (*string*) –
* **falseChoice** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetColumnProportion(self, column, proportion) -> bool:
        """ 

`SetColumnProportion`(*self*, *column*, *proportion*)[¶](#wx.propgrid.PropertyGridInterface.SetColumnProportion "Permalink to this definition")
Set proportion of an auto-stretchable column.


`wx.propgrid.PG_SPLITTER_AUTO_CENTER` window style needs to be used to indicate that columns are auto- resizable.



Parameters
* **column** (*int*) –
* **proportion** (*int*) –



Return type
*bool*



Returns
Returns `False` on failure.





Note


You should call this for individual pages of  [wx.propgrid.PropertyGridManager](wx.propgrid.PropertyGridManager.html#wx-propgrid-propertygridmanager) (if used).




See also


[`GetColumnProportion`](#wx.propgrid.PropertyGridInterface.GetColumnProportion "wx.propgrid.PropertyGridInterface.GetColumnProportion")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropVal(self, id, value) -> None:
        """ 

`SetPropVal`(*self*, *id*, *value*)[¶](#wx.propgrid.PropertyGridInterface.SetPropVal "Permalink to this definition")
Sets value (*Variant* &) of a property.


Same as SetPropertyValue, but accepts reference.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*PGVariant*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyAttribute(self, id, attrName, value, argFlags=0) -> None:
        """ 

`SetPropertyAttribute`(*self*, *id*, *attrName*, *value*, *argFlags=0*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyAttribute "Permalink to this definition")
Sets an attribute for this property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer to a property.
* **attrName** (*string*) – Text identifier of attribute. See PropertyGrid Property Attribute Identifiers.
* **value** (*PGVariant*) – Value of attribute.
* **argFlags** (*long*) – Optional. Use `wx.propgrid.PG_RECURSE` to set the attribute to child properties recursively.





Note


* Setting attribute’s value to NullVariant will simply remove it from property’s set of attributes.
* Property is refreshed with new settings.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyAttributeAll(self, attrName, value) -> None:
        """ 

`SetPropertyAttributeAll`(*self*, *attrName*, *value*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyAttributeAll "Permalink to this definition")
Sets property attribute for all applicable properties.


Be sure to use this method only after all properties have been added to the grid.



Parameters
* **attrName** (*string*) –
* **value** (*PGVariant*) –





Note


Properties are refreshed with new settings.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyBackgroundColour(self, id, colour, flags=PG_RECURSE) -> None:
        """ 

`SetPropertyBackgroundColour`(*self*, *id*, *colour*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyBackgroundColour "Permalink to this definition")
Sets background colour of given property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer.
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – New background colour.
* **flags** (*int*) – Default is `wx.propgrid.PG_RECURSE` which causes colour to be set recursively. Omit this flag to only set colour for the property in question and not any of its children.





Note


* If category is tried to set recursively, only its children are affected.
* Property is redrawn with new colour.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyCell(*args, **kwargs) -> None:
        """ 

`SetPropertyCell`(*self*, *id*, *column*, *text=""*, *bitmap=BitmapBundle()*, *fgCol=NullColour*, *bgCol=NullColour*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyCell "Permalink to this definition")
Sets text, bitmap, and colours for given column’s cell.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **column** (*int*) –
* **text** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **fgCol** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **bgCol** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





Note


* You can set label cell by using column 0.
* You can use `wx.propgrid.PG_LABEL` as text to use default text for column.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyClientData(self, p, data) -> None:
        """ 

`SetPropertyClientData`(*self*, *p*, *data*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyClientData "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyColoursToDefault(self, id, flags=PG_DONT_RECURSE) -> None:
        """ 

`SetPropertyColoursToDefault`(*self*, *id*, *flags=PG\_DONT\_RECURSE*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyColoursToDefault "Permalink to this definition")
Resets text and background colours of given property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer.
* **flags** (*int*) – Default is `wx.propgrid.PG_DONT_RECURSE` which causes colour to be reset only for the property in question (for backward compatibility).





Note


* If category is tried to set recursively, only its children are affected.
* Property is redrawn with new colours.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyEditor(self, *args, **kw) -> None:
        """ 

`SetPropertyEditor`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyEditor "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetPropertyEditor** *(self, id, editor)*


Sets editor for a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer to a property.
* **editor** ([*wx.propgrid.PGEditor*](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor "wx.propgrid.PGEditor")) – For builtin editors, use PGEditor\_X, where X is builtin editor’s name (TextCtrl, Choice, etc. see  [wx.propgrid.PGEditor](wx.propgrid.PGEditor.html#wx-propgrid-pgeditor) documentation for full list).




[`wx.propgrid.PropertyGrid.RegisterEditorClass`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.RegisterEditorClass "wx.propgrid.PropertyGrid.RegisterEditorClass") .




---

  



**SetPropertyEditor** *(self, id, editorName)*


Sets editor control of a property.


As editor argument, use editor name string, such as “TextCtrl” or “Choice”.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **editorName** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyHelpString(self, id, helpString) -> None:
        """ 

`SetPropertyHelpString`(*self*, *id*, *helpString*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyHelpString "Permalink to this definition")
Associates the help string with property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **helpString** (*string*) –





Note


By default, text is shown either in the manager’s “description” text box or in the status bar. If extra window style `wx.propgrid.PG_EX_HELP_AS_TOOLTIPS` is used, then the text will appear as a tooltip.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyImage(self, id, bmp) -> None:
        """ 

`SetPropertyImage`(*self*, *id*, *bmp*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyImage "Permalink to this definition")
Set  [wx.Bitmap](wx.Bitmap.html#wx-bitmap) taken from  [wx.BitmapBundle](wx.BitmapBundle.html#wx-bitmapbundle) in front of the value.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –





Note


Bitmap will be scaled to a size returned by [`wx.propgrid.PropertyGrid.GetImageSize`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid.GetImageSize "wx.propgrid.PropertyGrid.GetImageSize") ;





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyLabel(self, id, newproplabel) -> None:
        """ 

`SetPropertyLabel`(*self*, *id*, *newproplabel*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyLabel "Permalink to this definition")
Sets label of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **newproplabel** (*string*) –





Note


* Properties under same parent may have same labels. However, property names must still remain unique.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyMaxLength(self, id, maxLen) -> bool:
        """ 

`SetPropertyMaxLength`(*self*, *id*, *maxLen*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyMaxLength "Permalink to this definition")
Sets maximum length of text in property text editor.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer.
* **maxLen** (*int*) – Maximum number of characters of the text the user can enter in the text editor. If it is 0, the length is not limited and the text can be as long as it is supported by the underlying native text control widget.



Return type
*bool*



Returns
Returns `True` if maximum length was set.





See also


[`wx.propgrid.PGProperty.SetMaxLength`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetMaxLength "wx.propgrid.PGProperty.SetMaxLength") .





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyName(self, id, newName) -> None:
        """ 

`SetPropertyName`(*self*, *id*, *newName*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyName "Permalink to this definition")
Sets name of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer of property which name to change.
* **newName** (*string*) – New name for property.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyReadOnly(self, id, set=True, flags=PG_RECURSE) -> None:
        """ 

`SetPropertyReadOnly`(*self*, *id*, *set=True*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyReadOnly "Permalink to this definition")
Sets property (and, recursively, its children) to have read-only value.


In other words, user cannot change the value in the editor, but they can still copy it.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer.
* **set** (*bool*) – Use `True` to enable read-only, `False` to disable it.
* **flags** (*int*) – By default changes are applied recursively. Set this parameter to `wx.propgrid.PG_DONT_RECURSE` to prevent this.





Note


* This is mainly for use with textctrl editor. Only some other editors fully support it.
* Property is refreshed with new settings.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyTextColour(self, id, colour, flags=PG_RECURSE) -> None:
        """ 

`SetPropertyTextColour`(*self*, *id*, *colour*, *flags=PG\_RECURSE*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyTextColour "Permalink to this definition")
Sets text colour of given property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Property name or pointer.
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – New text colour.
* **flags** (*int*) – Default is `wx.propgrid.PG_RECURSE` which causes colour to be set recursively. Omit this flag to only set colour for the property in question and not any of its children.





Note


* If category is tried to set recursively, only its children are affected.
* Property is redrawn with new colour.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValidator(self, id, validator) -> None:
        """ 

`SetPropertyValidator`(*self*, *id*, *validator*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyValidator "Permalink to this definition")
Sets validator of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValue(self, *args, **kw) -> None:
        """ 

`SetPropertyValue`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyValue "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetPropertyValue** *(self, id, value)*


Sets value (floating point) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*float*) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (bool) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*bool*) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (string) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*string*) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (list of strings ) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*list of strings*) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value ( [wx.DateTime](wx.DateTime.html#wx-datetime)) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (:ref:[`](#id1)wx.Object`&) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (wxArrayInt&) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*list of integers*) –






---

  



**SetPropertyValue** *(self, id, value)*


Sets value (*Variant* ) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*PGVariant*) –





Note


Use [`ChangePropertyValue`](#wx.propgrid.PropertyGridInterface.ChangePropertyValue "wx.propgrid.PropertyGridInterface.ChangePropertyValue") instead if you need to run through validation process and send property change event.





---

  



**SetPropertyValue** *(self, id, value)*


Sets value (long integer) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValueString(self, id, value) -> None:
        """ 

`SetPropertyValueString`(*self*, *id*, *value*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyValueString "Permalink to this definition")
Sets value (*String* ) of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) –
* **value** (*string*) –





Note


This method uses [`wx.propgrid.PGProperty.SetValueFromString`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetValueFromString "wx.propgrid.PGProperty.SetValueFromString") , which all properties should implement. This means that there should not be a type error, and instead the string is converted to property’s actual value type.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValueUnspecified(self, id: 'propgrid.PGPropArgCls') -> None:
        """ 

`SetPropertyValueUnspecified`(*self*, *id*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyValueUnspecified "Permalink to this definition")
Sets property’s value to unspecified.


If it has children (it may be category), then the same thing is done to them.



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetPropertyValues(self, dict_, autofill=False) -> None:
        """ 

`SetPropertyValues`(*self*, *dict\_*, *autofill=False*)[¶](#wx.propgrid.PropertyGridInterface.SetPropertyValues "Permalink to this definition")
Sets property values from a dictionary.



Parameters
* **dict\_** – the source of the property values to set, which can be
either a dictionary or an object with a \_\_dict\_\_ attribute.
* **autofill** – If `True`, keys with not relevant properties are
auto-created. For more info, see [:method:`AutoFill`](#id3).





Note


Keys starting with underscore are ignored.
Attributes can be set with entries named like “@<propname>@<attr>”.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SetValidationFailureBehavior(self, vfbFlags: int) -> None:
        """ 

`SetValidationFailureBehavior`(*self*, *vfbFlags*)[¶](#wx.propgrid.PropertyGridInterface.SetValidationFailureBehavior "Permalink to this definition")
Adjusts how  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) behaves when invalid value is entered in a property.



Parameters
**vfbFlags** (*int*) – See PropertyGrid Validation Failure behaviour Flags for possible values.






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def Sort(self, flags: int=0) -> None:
        """ 

`Sort`(*self*, *flags=0*)[¶](#wx.propgrid.PropertyGridInterface.Sort "Permalink to this definition")
Sorts all properties recursively.



Parameters
**flags** (*int*) – This can contain any of the following options: `wx.propgrid.PG_SORT_TOP_LEVEL_ONLY`: Only sort categories and their immediate children. Sorting done by `wx.propgrid.PG_AUTO_SORT` option uses this.





See also


[`SortChildren`](#wx.propgrid.PropertyGridInterface.SortChildren "wx.propgrid.PropertyGridInterface.SortChildren") , `wx.propgrid.PropertyGrid.SetSortFunction`





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def SortChildren(self, id, flags=0) -> None:
        """ 

`SortChildren`(*self*, *id*, *flags=0*)[¶](#wx.propgrid.PropertyGridInterface.SortChildren "Permalink to this definition")
Sorts children of a property.



Parameters
* **id** ([*wx.propgrid.PGPropArgCls*](wx.propgrid.PGPropArgCls.html#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – Name or pointer to a property.
* **flags** (*int*) – This can contain any of the following options: `wx.propgrid.PG_RECURSE`: Sorts recursively.





See also


[`Sort`](#wx.propgrid.PropertyGridInterface.Sort "wx.propgrid.PropertyGridInterface.Sort") , `wx.propgrid.PropertyGrid.SetSortFunction`





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _AutoFillMany(self, cat, dict_) -> None:
        """ 

`_AutoFillMany`(*self*, *cat*, *dict\_*)[¶](#wx.propgrid.PropertyGridInterface._AutoFillMany "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _AutoFillOne(self, cat, k, v) -> None:
        """ 

`_AutoFillOne`(*self*, *cat*, *k*, *v*)[¶](#wx.propgrid.PropertyGridInterface._AutoFillOne "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _Items(self) -> None:
        """ 

`_Items`(*self*)[¶](#wx.propgrid.PropertyGridInterface._Items "Permalink to this definition")
This attribute is a pythonic iterator over all items in this
*PropertyGrid* property container, excluding only private child
properties. Usage is simple:



```
for prop in propGrid.Items:
        print(prop)

```



See also


[`wx.propgrid.PropertyGridInterface.Properties`](#wx.propgrid.PropertyGridInterface.Properties "wx.propgrid.PropertyGridInterface.Properties")
[`wx.propgrid.PropertyGridInterface.GetPyVIterator`](#wx.propgrid.PropertyGridInterface.GetPyVIterator "wx.propgrid.PropertyGridInterface.GetPyVIterator")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    def _Properties(self) -> None:
        """ 

`_Properties`(*self*)[¶](#wx.propgrid.PropertyGridInterface._Properties "Permalink to this definition")
This attribute is a pythonic iterator over all properties in
this *PropertyGrid* property container. It will only skip
categories and private child properties. Usage is simple:



```
for prop in propGrid.Properties:
        print(prop)

```



See also


[`wx.propgrid.PropertyGridInterface.Items`](#wx.propgrid.PropertyGridInterface.Items "wx.propgrid.PropertyGridInterface.Items")
[`wx.propgrid.PropertyGridInterface.GetPyIterator`](#wx.propgrid.PropertyGridInterface.GetPyIterator "wx.propgrid.PropertyGridInterface.GetPyIterator")





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridInterface.html
        """

    Items: Any  # `Items`[¶](#wx.propgrid.PropertyGridInterface.Items "Permalink to this definition")See [`_Items`](#wx.propgrid.PropertyGridInterface._Items "wx.propgrid.PropertyGridInterface._Items")
    Properties: Any  # `Properties`[¶](#wx.propgrid.PropertyGridInterface.Properties "Permalink to this definition")See [`_Properties`](#wx.propgrid.PropertyGridInterface._Properties "wx.propgrid.PropertyGridInterface._Properties")



PG_VFB_STAY_IN_PROPERTY: int

PG_ITERATE_DEFAULT: int

TOP: int

BOTTOM: int

PG_EX_MULTIPLE_SELECTION: int

PG_DONT_RECURSE: int

PG_SPLITTER_AUTO_CENTER: int

PG_RECURSE: int

PG_LABEL: int

PG_EX_HELP_AS_TOOLTIPS: int

PG_SORT_TOP_LEVEL_ONLY: int

PG_AUTO_SORT: int

class PropertyGridPageState:
    """ **Possible constructors**:



```
PropertyGridPageState()

```


Contains low-level property page information (properties, column
widths, etc.) of a single PropertyGrid or single PropertyGridPage.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PropertyGridPageState.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def CheckColumnWidths(self, widthChange: int=0) -> None:
        """ 

`CheckColumnWidths`(*self*, *widthChange=0*)[¶](#wx.propgrid.PropertyGridPageState.CheckColumnWidths "Permalink to this definition")
Makes sure all columns have minimum width.



Parameters
**widthChange** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoDelete(self, item, doDelete=True) -> None:
        """ 

`DoDelete`(*self*, *item*, *doDelete=True*)[¶](#wx.propgrid.PropertyGridPageState.DoDelete "Permalink to this definition")
Override this member function to add custom behaviour on property deletion.



Parameters
* **item** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **doDelete** (*bool*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoInsert(self, parent, index, property) -> 'PGProperty':
        """ 

`DoInsert`(*self*, *parent*, *index*, *property*)[¶](#wx.propgrid.PropertyGridPageState.DoInsert "Permalink to this definition")
Override this member function to add custom behaviour on property insertion.



Parameters
* **parent** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **index** (*int*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def DoSetSplitterPosition(self, pos, splitterColumn=0, flags=0) -> None:
        """ 

`DoSetSplitterPosition`(*self*, *pos*, *splitterColumn=0*, *flags=0*)[¶](#wx.propgrid.PropertyGridPageState.DoSetSplitterPosition "Permalink to this definition")
This needs to be overridden in grid used the manager so that splitter changes can be propagated to other pages.



Parameters
* **pos** (*int*) –
* **splitterColumn** (*int*) –
* **flags** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def EnableCategories(self, enable: bool) -> bool:
        """ 

`EnableCategories`(*self*, *enable*)[¶](#wx.propgrid.PropertyGridPageState.EnableCategories "Permalink to this definition")

Parameters
**enable** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def EnsureVirtualHeight(self) -> None:
        """ 

`EnsureVirtualHeight`(*self*)[¶](#wx.propgrid.PropertyGridPageState.EnsureVirtualHeight "Permalink to this definition")
Make sure virtual height is up-to-date.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetActualVirtualHeight(self) -> int:
        """ 

`GetActualVirtualHeight`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetActualVirtualHeight "Permalink to this definition")
Returns actual height of contained visible properties.



Return type
*int*





Note


Mostly used for internal diagnostic purposes.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnCount(self) -> int:
        """ 

`GetColumnCount`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetColumnCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnFullWidth(self, p, col) -> int:
        """ 

`GetColumnFullWidth`(*self*, *p*, *col*)[¶](#wx.propgrid.PropertyGridPageState.GetColumnFullWidth "Permalink to this definition")

Parameters
* **p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **col** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnMinWidth(self, column: int) -> int:
        """ 

`GetColumnMinWidth`(*self*, *column*)[¶](#wx.propgrid.PropertyGridPageState.GetColumnMinWidth "Permalink to this definition")

Parameters
**column** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetColumnWidth(self, column: int) -> int:
        """ 

`GetColumnWidth`(*self*, *column*)[¶](#wx.propgrid.PropertyGridPageState.GetColumnWidth "Permalink to this definition")

Parameters
**column** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetGrid(self) -> 'PropertyGrid':
        """ 

`GetGrid`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetGrid "Permalink to this definition")

Return type
 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetLastItem(self, flags: int=PG_ITERATE_DEFAULT) -> 'PGProperty':
        """ 

`GetLastItem`(*self*, *flags=PG\_ITERATE\_DEFAULT*)[¶](#wx.propgrid.PropertyGridPageState.GetLastItem "Permalink to this definition")
Returns last item which could be iterated using given flags.



Parameters
**flags** (*int*) – PropertyGridIterator Flags



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetPropertyCategory(self, p: 'propgrid.PGProperty') -> 'PropertyCategory':
        """ 

`GetPropertyCategory`(*self*, *p*)[¶](#wx.propgrid.PropertyGridPageState.GetPropertyCategory "Permalink to this definition")

Parameters
**p** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 



Return type
 [wx.propgrid.PropertyCategory](wx.propgrid.PropertyCategory.html#wx-propgrid-propertycategory)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetSelection(self) -> 'PGProperty':
        """ 

`GetSelection`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetSelection "Permalink to this definition")
Returns currently selected property.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetVirtualHeight(self) -> int:
        """ 

`GetVirtualHeight`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetVirtualHeight "Permalink to this definition")
Returns (precalculated) height of contained visible properties.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def GetVirtualWidth(self) -> int:
        """ 

`GetVirtualWidth`(*self*)[¶](#wx.propgrid.PropertyGridPageState.GetVirtualWidth "Permalink to this definition")
Returns combined width of margin and all the columns.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> 'PropertyGridHitTestResult':
        """ 

`HitTest`(*self*, *pt*)[¶](#wx.propgrid.PropertyGridPageState.HitTest "Permalink to this definition")
Returns information about arbitrary position in the grid.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Logical coordinates in the virtual grid space. Use [`wx.Scrolled.CalcUnscrolledPosition`](wx.Scrolled.html#wx.Scrolled.CalcUnscrolledPosition "wx.Scrolled.CalcUnscrolledPosition") if you need to translate a scrolled position into a logical one.



Return type
 [wx.propgrid.PropertyGridHitTestResult](wx.propgrid.PropertyGridHitTestResult.html#wx-propgrid-propertygridhittestresult)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def IsDisplayed(self) -> bool:
        """ 

`IsDisplayed`(*self*)[¶](#wx.propgrid.PropertyGridPageState.IsDisplayed "Permalink to this definition")
Returns `True` if page is visibly displayed.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def IsInNonCatMode(self) -> bool:
        """ 

`IsInNonCatMode`(*self*)[¶](#wx.propgrid.PropertyGridPageState.IsInNonCatMode "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    def VirtualHeightChanged(self) -> None:
        """ 

`VirtualHeightChanged`(*self*)[¶](#wx.propgrid.PropertyGridPageState.VirtualHeightChanged "Permalink to this definition")
Called after virtual height needs to be recalculated.




            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridPageState.html
        """

    ActualVirtualHeight: int  # `ActualVirtualHeight`[¶](#wx.propgrid.PropertyGridPageState.ActualVirtualHeight "Permalink to this definition")See [`GetActualVirtualHeight`](#wx.propgrid.PropertyGridPageState.GetActualVirtualHeight "wx.propgrid.PropertyGridPageState.GetActualVirtualHeight")
    ColumnCount: int  # `ColumnCount`[¶](#wx.propgrid.PropertyGridPageState.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.propgrid.PropertyGridPageState.GetColumnCount "wx.propgrid.PropertyGridPageState.GetColumnCount")
    Grid: 'PropertyGrid'  # `Grid`[¶](#wx.propgrid.PropertyGridPageState.Grid "Permalink to this definition")See [`GetGrid`](#wx.propgrid.PropertyGridPageState.GetGrid "wx.propgrid.PropertyGridPageState.GetGrid")
    LastItem: 'PGProperty'  # `LastItem`[¶](#wx.propgrid.PropertyGridPageState.LastItem "Permalink to this definition")See [`GetLastItem`](#wx.propgrid.PropertyGridPageState.GetLastItem "wx.propgrid.PropertyGridPageState.GetLastItem")
    Selection: 'PGProperty'  # `Selection`[¶](#wx.propgrid.PropertyGridPageState.Selection "Permalink to this definition")See [`GetSelection`](#wx.propgrid.PropertyGridPageState.GetSelection "wx.propgrid.PropertyGridPageState.GetSelection")
    VirtualHeight: int  # `VirtualHeight`[¶](#wx.propgrid.PropertyGridPageState.VirtualHeight "Permalink to this definition")See [`GetVirtualHeight`](#wx.propgrid.PropertyGridPageState.GetVirtualHeight "wx.propgrid.PropertyGridPageState.GetVirtualHeight")
    VirtualWidth: int  # `VirtualWidth`[¶](#wx.propgrid.PropertyGridPageState.VirtualWidth "Permalink to this definition")See [`GetVirtualWidth`](#wx.propgrid.PropertyGridPageState.GetVirtualWidth "wx.propgrid.PropertyGridPageState.GetVirtualWidth")



class SystemColourProperty(EnumProperty):
    """ **Possible constructors**:



```
SystemColourProperty(label=PG_LABEL, name=PG_LABEL,
                     value=ColourPropertyValue())

```


Has dropdown list of wxWidgets system colours.


  


        Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=ColourPropertyValue()*)[¶](#wx.propgrid.SystemColourProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** ([*wx.propgrid.ColourPropertyValue*](wx.propgrid.ColourPropertyValue.html#wx.propgrid.ColourPropertyValue "wx.propgrid.ColourPropertyValue")) –






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def ColourToString(self, col, index, argFlags=0) -> str:
        """ 

`ColourToString`(*self*, *col*, *index*, *argFlags=0*)[¶](#wx.propgrid.SystemColourProperty.ColourToString "Permalink to this definition")
Override in derived class to customize how colours are printed as strings.



Parameters
* **col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **index** (*int*) –
* **argFlags** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.SystemColourProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetColour(self, index: int) -> 'Colour':
        """ 

`GetColour`(*self*, *index*)[¶](#wx.propgrid.SystemColourProperty.GetColour "Permalink to this definition")
Default is to use *SystemSettings.GetColour(index).*


Override to use custom colour tables etc.



Parameters
**index** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetCustomColourIndex(self) -> int:
        """ 

`GetCustomColourIndex`(*self*)[¶](#wx.propgrid.SystemColourProperty.GetCustomColourIndex "Permalink to this definition")
Returns index of entry that triggers colour picker dialog (default is last).



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def GetVal(self, pVariant: Optional[PGVariant]=None) -> 'ColourPropertyValue':
        """ 

`GetVal`(*self*, *pVariant=None*)[¶](#wx.propgrid.SystemColourProperty.GetVal "Permalink to this definition")

Parameters
**pVariant** (*PGVariant*) – 



Return type
 [wx.propgrid.ColourPropertyValue](wx.propgrid.ColourPropertyValue.html#wx-propgrid-colourpropertyvalue)






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.SystemColourProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ 

`OnCustomPaint`(*self*, *dc*, *rect*, *paintdata*)[¶](#wx.propgrid.SystemColourProperty.OnCustomPaint "Permalink to this definition")
Override to paint an image in front of the property value text or drop-down list item (but only if [`wx.propgrid.PGProperty.OnMeasureImage`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") is overridden as well).


If property’s [`OnMeasureImage`](#wx.propgrid.SystemColourProperty.OnMeasureImage "wx.propgrid.SystemColourProperty.OnMeasureImage") returns size that has height != 0 but less than row height ( < 0 has special meanings),  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) calls this method to draw a custom image in a limited area in front of the editor control or value text/graphics, and if control has drop-down list, then the image is drawn there as well (even in the case [`OnMeasureImage`](#wx.propgrid.SystemColourProperty.OnMeasureImage "wx.propgrid.SystemColourProperty.OnMeasureImage") returned higher height than row height).


`NOTE`: Following applies when [`OnMeasureImage`](#wx.propgrid.SystemColourProperty.OnMeasureImage "wx.propgrid.SystemColourProperty.OnMeasureImage") returns a “flexible” height ( using `PG_FLEXIBLE_SIZE(W,H)` macro), which implies variable height items: If (rect.x+rect.width) is < 0, then this is a measure item call, which means that dc is invalid and only thing that should be done is to set paintdata.m\_drawnHeight to the height of the image of item at index paintdata.m\_choiceItem. This call may be done even as often as once every drop-down popup show.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for custom graphics. Includes surrounding rectangle, if any. If x+width is < 0, then this is a measure item call (see above).
* **paintdata** ([*wx.propgrid.PGPaintData*](wx.propgrid.PGPaintData.html#wx.propgrid.PGPaintData "wx.propgrid.PGPaintData")) –  [wx.propgrid.PGPaintData](wx.propgrid.PGPaintData.html#wx-propgrid-pgpaintdata) structure with much useful data about painted item.





Note


* You can actually exceed rect width, but if you do so then paintdata.m\_drawnWidth must be set to the full width drawn in pixels.
* Due to technical reasons, rect’s height will be default even if custom height was reported during measure call.
* Brush is guaranteed to be default background colour. It has been already used to clear the background of area being painted. It can be modified.
* Pen is guaranteed to be 1-wide ‘black’ (or whatever is the proper colour) pen for drawing framing rectangle. It can be changed as well.




See also


[`ValueToString`](#wx.propgrid.SystemColourProperty.ValueToString "wx.propgrid.SystemColourProperty.ValueToString")





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnEvent(self, propgrid, wnd_primary, event) -> None:
        """ 

`OnEvent`(*self*, *propgrid*, *wnd\_primary*, *event*)[¶](#wx.propgrid.SystemColourProperty.OnEvent "Permalink to this definition")
Events received by editor widgets are processed here.


Note that editor class usually processes most events. Some, such as button press events of TextCtrlAndButton class, can be handled here. Also, if custom handling for regular events is desired, then that can also be done (for example,  [wx.propgrid.SystemColourProperty](#wx-propgrid-systemcolourproperty) custom handles `wxEVT_CHOICE` to display colour picker dialog when ‘custom’ selection is made).


If the event causes value to be changed, `SetValueInEvent` should be called to set the new value.


The parameter *event* is the associated  [wx.Event](wx.Event.html#wx-event).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –




return `True` if any changes in value should be reported.



Return type
*bool*





Note


* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ 

`OnMeasureImage`(*self*, *item*)[¶](#wx.propgrid.SystemColourProperty.OnMeasureImage "Permalink to this definition")
Returns size of the custom painted image in front of property.


This method must be overridden to return non-default value if OnCustomPaint is to be called.



Parameters
**item** (*int*) – Normally -1, but can be an index to the property’s list of items.



Return type
*Size*





Note


* Default behaviour is to return  [wx.Size](wx.Size.html#wx-size), which means no image.
* Default image width or height is indicated with dimension -1.
* You can also return `PG_DEFAULT_IMAGE_SIZE` which equals DefaultSize.





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.SystemColourProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.SystemColourProperty.OnSetValue "wx.propgrid.SystemColourProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.SystemColourProperty.OnSetValue "wx.propgrid.SystemColourProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def QueryColourFromUser(self, variant: PGVariant) -> bool:
        """ 

`QueryColourFromUser`(*self*, *variant*)[¶](#wx.propgrid.SystemColourProperty.QueryColourFromUser "Permalink to this definition")

Parameters
**variant** (*PGVariant*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.SystemColourProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.SystemColourProperty.ValueToString "wx.propgrid.SystemColourProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.SystemColourProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.SystemColourProperty.html
        """

    CustomColourIndex: int  # `CustomColourIndex`[¶](#wx.propgrid.SystemColourProperty.CustomColourIndex "Permalink to this definition")See [`GetCustomColourIndex`](#wx.propgrid.SystemColourProperty.GetCustomColourIndex "wx.propgrid.SystemColourProperty.GetCustomColourIndex")
    Val: 'ColourPropertyValue'  # `Val`[¶](#wx.propgrid.SystemColourProperty.Val "Permalink to this definition")See [`GetVal`](#wx.propgrid.SystemColourProperty.GetVal "wx.propgrid.SystemColourProperty.GetVal")



class PGChoiceEntry(PGCell):
    """ **Possible constructors**:



```
PGChoiceEntry()

PGChoiceEntry(other)

PGChoiceEntry(label, value=PG_INVALID_VALUE)

```


Data of a single PGChoices choice.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGChoiceEntry.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, other)*



Parameters
**other** ([*wx.propgrid.PGChoiceEntry*](#wx.propgrid.PGChoiceEntry "wx.propgrid.PGChoiceEntry")) – 






---

  



**\_\_init\_\_** *(self, label, value=PG\_INVALID\_VALUE)*



Parameters
* **label** (*string*) –
* **value** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    def GetValue(self) -> int:
        """ 

`GetValue`(*self*)[¶](#wx.propgrid.PGChoiceEntry.GetValue "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    def SetValue(self, value: int) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.propgrid.PGChoiceEntry.SetValue "Permalink to this definition")

Parameters
**value** (*int*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEntry.html
        """

    Value: int  # `Value`[¶](#wx.propgrid.PGChoiceEntry.Value "Permalink to this definition")See [`GetValue`](#wx.propgrid.PGChoiceEntry.GetValue "wx.propgrid.PGChoiceEntry.GetValue") and [`SetValue`](#wx.propgrid.PGChoiceEntry.SetValue "wx.propgrid.PGChoiceEntry.SetValue")



class PGCellData(ObjectRefData):
    """ **Possible constructors**:



```
PGCellData()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGCellData.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetBgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetBgCol`(*self*, *col*)[¶](#wx.propgrid.PGCellData.SetBgCol "Permalink to this definition")

Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetBitmap(self, bitmap: 'BitmapBundle') -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.propgrid.PGCellData.SetBitmap "Permalink to this definition")

Parameters
**bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetFgCol(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetFgCol`(*self*, *col*)[¶](#wx.propgrid.PGCellData.SetFgCol "Permalink to this definition")

Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.propgrid.PGCellData.SetFont "Permalink to this definition")

Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.propgrid.PGCellData.SetText "Permalink to this definition")

Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGCellData.html
        """



class PGCheckBoxEditor(PGEditor):
    """ **Possible constructors**:



```
PGCheckBoxEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGCheckBoxEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGCheckBoxEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def DrawValue(self, dc, rect, property, text) -> None:
        """ 

`DrawValue`(*self*, *dc*, *rect*, *property*, *text*)[¶](#wx.propgrid.PGCheckBoxEditor.DrawValue "Permalink to this definition")
Draws value for given property.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGCheckBoxEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ 

`GetValueFromControl`(*self*, *variant*, *property*, *ctrl*)[¶](#wx.propgrid.PGCheckBoxEditor.GetValueFromControl "Permalink to this definition")
Returns value from control, via parameter *variant*.


Usually ends up calling property’s StringToValue() or IntToValue(). Returns `True` if value was different.



Parameters
* **variant** (*PGVariant*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGCheckBoxEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ 

`SetControlIntValue`(*self*, *property*, *ctrl*, *value*)[¶](#wx.propgrid.PGCheckBoxEditor.SetControlIntValue "Permalink to this definition")
Sets control’s value specifically from int (applies to choice etc.).



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **value** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ 

`SetValueToUnspecified`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGCheckBoxEditor.SetValueToUnspecified "Permalink to this definition")
Sets value in control to unspecified.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ 

`UpdateControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGCheckBoxEditor.UpdateControl "Permalink to this definition")
Loads value from property to the control.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCheckBoxEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGCheckBoxEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGCheckBoxEditor.GetName "wx.propgrid.PGCheckBoxEditor.GetName")



class PGChoiceEditor(PGEditor):
    """ **Possible constructors**:



```
PGChoiceEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGChoiceEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CanContainCustomImage(self) -> bool:
        """ 

`CanContainCustomImage`(*self*)[¶](#wx.propgrid.PGChoiceEditor.CanContainCustomImage "Permalink to this definition")
Returns `True` if control itself can contain the custom image.


Default implementation returns `False`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGChoiceEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def CreateControlsBase(self, propgrid, property, pos, sz, extraStyle) -> 'Window':
        """ 

`CreateControlsBase`(*self*, *propgrid*, *property*, *pos*, *sz*, *extraStyle*)[¶](#wx.propgrid.PGChoiceEditor.CreateControlsBase "Permalink to this definition")

Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **extraStyle** (*long*) –



Return type
*Window*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def DeleteItem(self, ctrl, index) -> None:
        """ 

`DeleteItem`(*self*, *ctrl*, *index*)[¶](#wx.propgrid.PGChoiceEditor.DeleteItem "Permalink to this definition")
Deletes item from existing control.


Default implementation does nothing.



Parameters
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **index** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGChoiceEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ 

`GetValueFromControl`(*self*, *variant*, *property*, *ctrl*)[¶](#wx.propgrid.PGChoiceEditor.GetValueFromControl "Permalink to this definition")
Returns value from control, via parameter *variant*.


Usually ends up calling property’s StringToValue() or IntToValue(). Returns `True` if value was different.



Parameters
* **variant** (*PGVariant*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def InsertItem(self, ctrl, label, index) -> int:
        """ 

`InsertItem`(*self*, *ctrl*, *label*, *index*)[¶](#wx.propgrid.PGChoiceEditor.InsertItem "Permalink to this definition")
Inserts item to existing control.


Index -1 means end of list. Default implementation does nothing. Returns index of item added.



Parameters
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **label** (*string*) –
* **index** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGChoiceEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetControlIntValue(self, property, ctrl, value) -> None:
        """ 

`SetControlIntValue`(*self*, *property*, *ctrl*, *value*)[¶](#wx.propgrid.PGChoiceEditor.SetControlIntValue "Permalink to this definition")
Sets control’s value specifically from int (applies to choice etc.).



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **value** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ 

`SetControlStringValue`(*self*, *property*, *ctrl*, *txt*)[¶](#wx.propgrid.PGChoiceEditor.SetControlStringValue "Permalink to this definition")
Sets control’s value specifically from string.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **txt** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def SetValueToUnspecified(self, property, ctrl) -> None:
        """ 

`SetValueToUnspecified`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGChoiceEditor.SetValueToUnspecified "Permalink to this definition")
Sets value in control to unspecified.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ 

`UpdateControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGChoiceEditor.UpdateControl "Permalink to this definition")
Loads value from property to the control.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGChoiceEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGChoiceEditor.GetName "wx.propgrid.PGChoiceEditor.GetName")



class PGTextCtrlEditor(PGEditor):
    """ **Possible constructors**:



```
PGTextCtrlEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGTextCtrlEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGTextCtrlEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGTextCtrlEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    @staticmethod
    def GetTextCtrlValueFromControl(variant, property, ctrl) -> bool:
        """ 

*static* `GetTextCtrlValueFromControl`(*variant*, *property*, *ctrl*)[¶](#wx.propgrid.PGTextCtrlEditor.GetTextCtrlValueFromControl "Permalink to this definition")

Parameters
* **variant** (*PGVariant*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ 

`GetValueFromControl`(*self*, *variant*, *property*, *ctrl*)[¶](#wx.propgrid.PGTextCtrlEditor.GetValueFromControl "Permalink to this definition")
Returns value from control, via parameter *variant*.


Usually ends up calling property’s StringToValue() or IntToValue(). Returns `True` if value was different.



Parameters
* **variant** (*PGVariant*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGTextCtrlEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ 

`OnFocus`(*self*, *property*, *wnd*)[¶](#wx.propgrid.PGTextCtrlEditor.OnFocus "Permalink to this definition")
Extra processing when control gains focus.


For example,  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) based controls should select all text.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    @staticmethod
    def OnTextCtrlEvent(propgrid, property, ctrl, event) -> bool:
        """ 

*static* `OnTextCtrlEvent`(*propgrid*, *property*, *ctrl*, *event*)[¶](#wx.propgrid.PGTextCtrlEditor.OnTextCtrlEvent "Permalink to this definition")

Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def SetControlStringValue(self, property, ctrl, txt) -> None:
        """ 

`SetControlStringValue`(*self*, *property*, *ctrl*, *txt*)[¶](#wx.propgrid.PGTextCtrlEditor.SetControlStringValue "Permalink to this definition")
Sets control’s value specifically from string.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **txt** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ 

`UpdateControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGTextCtrlEditor.UpdateControl "Permalink to this definition")
Loads value from property to the control.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGTextCtrlEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGTextCtrlEditor.GetName "wx.propgrid.PGTextCtrlEditor.GetName")



class ArrayStringProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
ArrayStringProperty(label=PG_LABEL, name=PG_LABEL, value=[])

```


Property that manages a list of strings.


  


        Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=[]) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=[]*)[¶](#wx.propgrid.ArrayStringProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*list of strings*) –






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    @staticmethod
    def ArrayStringToString(src, delimiter, flags) -> str:
        """ 

*static* `ArrayStringToString`(*src*, *delimiter*, *flags*)[¶](#wx.propgrid.ArrayStringProperty.ArrayStringToString "Permalink to this definition")
Generates string based on the contents of list of strings *src*.



Parameters
* **src** (*list of strings*) –
* **delimiter** ([*wx.UniChar*](wx.UniChar.html#wx.UniChar "wx.UniChar")) –
* **flags** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def ConvertArrayToString(self, arr, delimiter) -> str:
        """ 

`ConvertArrayToString`(*self*, *arr*, *delimiter*)[¶](#wx.propgrid.ArrayStringProperty.ConvertArrayToString "Permalink to this definition")
Implement in derived class for custom array-to-string conversion.



Parameters
* **arr** (*list of strings*) –
* **delimiter** ([*wx.UniChar*](wx.UniChar.html#wx.UniChar "wx.UniChar")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def CreateEditorDialog(self) -> 'PGArrayEditorDialog':
        """ 

`CreateEditorDialog`(*self*)[¶](#wx.propgrid.ArrayStringProperty.CreateEditorDialog "Permalink to this definition")
Creates  [wx.propgrid.PGArrayEditorDialog](wx.propgrid.PGArrayEditorDialog.html#wx-propgrid-pgarrayeditordialog) for string editing.



Return type
 [wx.propgrid.PGArrayEditorDialog](wx.propgrid.PGArrayEditorDialog.html#wx-propgrid-pgarrayeditordialog)






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.ArrayStringProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.ArrayStringProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def GenerateValueAsString(self) -> None:
        """ 

`GenerateValueAsString`(*self*)[¶](#wx.propgrid.ArrayStringProperty.GenerateValueAsString "Permalink to this definition")
Previously this was to be implemented in derived class for array-to- string conversion.


Now you should implement ConvertValueToString() instead.




            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def OnCustomStringEdit(self, parent, value) -> bool:
        """ 

`OnCustomStringEdit`(*self*, *parent*, *value*)[¶](#wx.propgrid.ArrayStringProperty.OnCustomStringEdit "Permalink to this definition")
Shows string editor dialog to edit the individual item.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned if that was the case.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **value** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.ArrayStringProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.ArrayStringProperty.OnSetValue "wx.propgrid.ArrayStringProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.ArrayStringProperty.OnSetValue "wx.propgrid.ArrayStringProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.ArrayStringProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.ArrayStringProperty.ValueToString "wx.propgrid.ArrayStringProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.ArrayStringProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.ArrayStringProperty.html
        """



class BoolProperty(PGProperty):
    """ **Possible constructors**:



```
BoolProperty(label=PG_LABEL, name=PG_LABEL, value=False)

```


Basic property with boolean value.


  


        Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=False) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=False*)[¶](#wx.propgrid.BoolProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*bool*) –






            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.BoolProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.BoolProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.BoolProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.BoolProperty.ValueToString "wx.propgrid.BoolProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.BoolProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.BoolProperty.html
        """



class ColourProperty(SystemColourProperty):
    """ **Possible constructors**:



```
ColourProperty(label=PG_LABEL, name=PG_LABEL, value=WHITE)

```


Allows to select a colour from the list or with colour dialog.


  


        Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=WHITE) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=WHITE*)[¶](#wx.propgrid.ColourProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """

    def GetColour(self, index: int) -> 'Colour':
        """ 

`GetColour`(*self*, *index*)[¶](#wx.propgrid.ColourProperty.GetColour "Permalink to this definition")
Default is to use *SystemSettings.GetColour(index).*


Override to use custom colour tables etc.



Parameters
**index** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.ColourProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.ColourProperty.html
        """



class CursorProperty(EnumProperty):
    """ **Possible constructors**:



```
CursorProperty(label=PG_LABEL, name=PG_LABEL, value=0)

```


Property representing Cursor.


  


        Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=0) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=0*)[¶](#wx.propgrid.CursorProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ 

`OnCustomPaint`(*self*, *dc*, *rect*, *paintdata*)[¶](#wx.propgrid.CursorProperty.OnCustomPaint "Permalink to this definition")
Override to paint an image in front of the property value text or drop-down list item (but only if [`wx.propgrid.PGProperty.OnMeasureImage`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") is overridden as well).


If property’s [`OnMeasureImage`](#wx.propgrid.CursorProperty.OnMeasureImage "wx.propgrid.CursorProperty.OnMeasureImage") returns size that has height != 0 but less than row height ( < 0 has special meanings),  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) calls this method to draw a custom image in a limited area in front of the editor control or value text/graphics, and if control has drop-down list, then the image is drawn there as well (even in the case [`OnMeasureImage`](#wx.propgrid.CursorProperty.OnMeasureImage "wx.propgrid.CursorProperty.OnMeasureImage") returned higher height than row height).


`NOTE`: Following applies when [`OnMeasureImage`](#wx.propgrid.CursorProperty.OnMeasureImage "wx.propgrid.CursorProperty.OnMeasureImage") returns a “flexible” height ( using `PG_FLEXIBLE_SIZE(W,H)` macro), which implies variable height items: If (rect.x+rect.width) is < 0, then this is a measure item call, which means that dc is invalid and only thing that should be done is to set paintdata.m\_drawnHeight to the height of the image of item at index paintdata.m\_choiceItem. This call may be done even as often as once every drop-down popup show.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for custom graphics. Includes surrounding rectangle, if any. If x+width is < 0, then this is a measure item call (see above).
* **paintdata** ([*wx.propgrid.PGPaintData*](wx.propgrid.PGPaintData.html#wx.propgrid.PGPaintData "wx.propgrid.PGPaintData")) –  [wx.propgrid.PGPaintData](wx.propgrid.PGPaintData.html#wx-propgrid-pgpaintdata) structure with much useful data about painted item.





Note


* You can actually exceed rect width, but if you do so then paintdata.m\_drawnWidth must be set to the full width drawn in pixels.
* Due to technical reasons, rect’s height will be default even if custom height was reported during measure call.
* Brush is guaranteed to be default background colour. It has been already used to clear the background of area being painted. It can be modified.
* Pen is guaranteed to be 1-wide ‘black’ (or whatever is the proper colour) pen for drawing framing rectangle. It can be changed as well.




See also


[`ValueToString`](wx.propgrid.EnumProperty.html#wx.propgrid.EnumProperty.ValueToString "wx.propgrid.EnumProperty.ValueToString")





            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ 

`OnMeasureImage`(*self*, *item*)[¶](#wx.propgrid.CursorProperty.OnMeasureImage "Permalink to this definition")
Returns size of the custom painted image in front of property.


This method must be overridden to return non-default value if OnCustomPaint is to be called.



Parameters
**item** (*int*) – Normally -1, but can be an index to the property’s list of items.



Return type
*Size*





Note


* Default behaviour is to return  [wx.Size](wx.Size.html#wx-size), which means no image.
* Default image width or height is indicated with dimension -1.
* You can also return `PG_DEFAULT_IMAGE_SIZE` which equals DefaultSize.





            Source: https://docs.wxpython.org/wx.propgrid.CursorProperty.html
        """



class DateProperty(PGProperty):
    """ **Possible constructors**:



```
DateProperty(label=PG_LABEL, name=PG_LABEL, value=DateTime())

```


Property representing DateTime.


  


        Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=DateTime()*)[¶](#wx.propgrid.DateProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) –






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.DateProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetDatePickerStyle(self) -> int:
        """ 

`GetDatePickerStyle`(*self*)[¶](#wx.propgrid.DateProperty.GetDatePickerStyle "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetDateValue(self) -> 'DateTime':
        """ 

`GetDateValue`(*self*)[¶](#wx.propgrid.DateProperty.GetDateValue "Permalink to this definition")

Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def GetFormat(self) -> str:
        """ 

`GetFormat`(*self*)[¶](#wx.propgrid.DateProperty.GetFormat "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.DateProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.DateProperty.OnSetValue "wx.propgrid.DateProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.DateProperty.OnSetValue "wx.propgrid.DateProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def SetDateValue(self, dt: 'DateTime') -> None:
        """ 

`SetDateValue`(*self*, *dt*)[¶](#wx.propgrid.DateProperty.SetDateValue "Permalink to this definition")

Parameters
**dt** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def SetFormat(self, format: str) -> None:
        """ 

`SetFormat`(*self*, *format*)[¶](#wx.propgrid.DateProperty.SetFormat "Permalink to this definition")

Parameters
**format** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.DateProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.DateProperty.ValueToString "wx.propgrid.DateProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.DateProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.DateProperty.html
        """

    DatePickerStyle: int  # `DatePickerStyle`[¶](#wx.propgrid.DateProperty.DatePickerStyle "Permalink to this definition")See [`GetDatePickerStyle`](#wx.propgrid.DateProperty.GetDatePickerStyle "wx.propgrid.DateProperty.GetDatePickerStyle")
    DateValue: 'DateTime'  # `DateValue`[¶](#wx.propgrid.DateProperty.DateValue "Permalink to this definition")See [`GetDateValue`](#wx.propgrid.DateProperty.GetDateValue "wx.propgrid.DateProperty.GetDateValue") and [`SetDateValue`](#wx.propgrid.DateProperty.SetDateValue "wx.propgrid.DateProperty.SetDateValue")
    Format: str  # `Format`[¶](#wx.propgrid.DateProperty.Format "Permalink to this definition")See [`GetFormat`](#wx.propgrid.DateProperty.GetFormat "wx.propgrid.DateProperty.GetFormat") and [`SetFormat`](#wx.propgrid.DateProperty.SetFormat "wx.propgrid.DateProperty.SetFormat")



class DirProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
DirProperty(label=PG_LABEL, name=PG_LABEL, value="")

```


Like LongStringProperty, but the button triggers directory selector
instead.


  


        Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=""*)[¶](#wx.propgrid.DirProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.DirProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.DirProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.DirProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.DirProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.DirProperty.ValueToString "wx.propgrid.DirProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.DirProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.DirProperty.html
        """



class EditEnumProperty(EnumProperty):
    """ **Possible constructors**:



```
EditEnumProperty(label=PG_LABEL, name=PG_LABEL, labels=[], values=[],
                 value="")

EditEnumProperty(label, name, choices, value="")

```


EnumProperty with string value and writable combo box editor.


  


        Source: https://docs.wxpython.org/wx.propgrid.EditEnumProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.EditEnumProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, labels=[], values=[], value=””)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **labels** (*list of strings*) –
* **values** (*list of integers*) –
* **value** (*string*) –






---

  



**\_\_init\_\_** *(self, label, name, choices, value=””)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **choices** ([*wx.propgrid.PGChoices*](wx.propgrid.PGChoices.html#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) –
* **value** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.EditEnumProperty.html
        """



class EnumProperty(PGProperty):
    """ **Possible constructors**:



```
EnumProperty(label, name, choices, value=0)

EnumProperty(label=PG_LABEL, name=PG_LABEL, labels=[], values=[],
             value=0)

```


You can derive custom properties with choices from this class.


  


        Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.EnumProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label, name, choices, value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **choices** ([*wx.propgrid.PGChoices*](wx.propgrid.PGChoices.html#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) –
* **value** (*int*) –






---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, labels=[], values=[], value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **labels** (*list of strings*) –
* **values** (*list of integers*) –
* **value** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ 

`GetChoiceSelection`(*self*)[¶](#wx.propgrid.EnumProperty.GetChoiceSelection "Permalink to this definition")
Returns which choice is currently selected.


Only applies to properties which have choices.


Needs to reimplemented in derived class if property value does not map directly to a choice. Integer as index, bool, and string usually do.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetIndexForValue(self, value: int) -> int:
        """ 

`GetIndexForValue`(*self*, *value*)[¶](#wx.propgrid.EnumProperty.GetIndexForValue "Permalink to this definition")

Parameters
**value** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def GetItemCount(self) -> int:
        """ 

`GetItemCount`(*self*)[¶](#wx.propgrid.EnumProperty.GetItemCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.EnumProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.EnumProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.EnumProperty.OnSetValue "wx.propgrid.EnumProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.EnumProperty.OnSetValue "wx.propgrid.EnumProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.EnumProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.EnumProperty.ValueToString "wx.propgrid.EnumProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ 

`ValidateValue`(*self*, *value*, *validationInfo*)[¶](#wx.propgrid.EnumProperty.ValidateValue "Permalink to this definition")
Implement this function in derived class to check the value.


Return `True` if it is ok. Returning `False` prevents property change events from occurring.



Parameters
* **value** (*PGVariant*) –
* **validationInfo** ([*wx.propgrid.PGValidationInfo*](wx.propgrid.PGValidationInfo.html#wx.propgrid.PGValidationInfo "wx.propgrid.PGValidationInfo")) –



Return type
*bool*





Note


* Default implementation always returns `True`.





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.EnumProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.EnumProperty.html
        """

    ChoiceSelection: int  # `ChoiceSelection`[¶](#wx.propgrid.EnumProperty.ChoiceSelection "Permalink to this definition")See [`GetChoiceSelection`](#wx.propgrid.EnumProperty.GetChoiceSelection "wx.propgrid.EnumProperty.GetChoiceSelection")
    ItemCount: int  # `ItemCount`[¶](#wx.propgrid.EnumProperty.ItemCount "Permalink to this definition")See [`GetItemCount`](#wx.propgrid.EnumProperty.GetItemCount "wx.propgrid.EnumProperty.GetItemCount")



class FileProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
FileProperty(label=PG_LABEL, name=PG_LABEL, value="")

```


Like LongStringProperty, but the button triggers file selector
instead.


  


        Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=""*)[¶](#wx.propgrid.FileProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.FileProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.FileProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.FileProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](wx.propgrid.DirProperty.html#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.FileProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ 

*static* `GetClassValidator`()[¶](#wx.propgrid.FileProperty.GetClassValidator "Permalink to this definition")

Return type
*Validator*






            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def GetFileName(self) -> str:
        """ 

`GetFileName`(*self*)[¶](#wx.propgrid.FileProperty.GetFileName "Permalink to this definition")
Returns filename to file represented by current value.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.FileProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.FileProperty.OnSetValue "wx.propgrid.FileProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.FileProperty.OnSetValue "wx.propgrid.FileProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.FileProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.FileProperty.ValueToString "wx.propgrid.FileProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.FileProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.FileProperty.html
        """

    FileName: str  # `FileName`[¶](#wx.propgrid.FileProperty.FileName "Permalink to this definition")See [`GetFileName`](#wx.propgrid.FileProperty.GetFileName "wx.propgrid.FileProperty.GetFileName")



class FlagsProperty(PGProperty):
    """ **Possible constructors**:



```
FlagsProperty(label, name, choices, value=0)

FlagsProperty(label=PG_LABEL, name=PG_LABEL, labels=[], values=[],
              value=0)

```


Represents a bit set that fits in a long integer.


  


        Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.FlagsProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label, name, choices, value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **choices** ([*wx.propgrid.PGChoices*](wx.propgrid.PGChoices.html#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) –
* **value** (*long*) –






---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, labels=[], values=[], value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **labels** (*list of strings*) –
* **values** (*list of integers*) –
* **value** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'PGVariant':
        """ 

`ChildChanged`(*self*, *thisValue*, *childIndex*, *childValue*)[¶](#wx.propgrid.FlagsProperty.ChildChanged "Permalink to this definition")
Called after value of a child property has been altered.


Must return new value of the whole property (after any alterations warranted by child’s new value).


Note that this function is usually called at the time that value of this property, or given child property, is still pending for change, and as such, result of [`GetValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GetValue "wx.propgrid.PGProperty.GetValue") or m\_value should not be relied on.


Sample pseudo-code implementation:



```
# TBW

```



Parameters
* **thisValue** (*PGVariant*) – Value of this property. Changed value should be returned (in previous versions of  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) it was only necessary to write value back to this argument).
* **childIndex** (*int*) – Index of child changed (you can use Item(childIndex) to get child property).
* **childValue** (*PGVariant*) – (Pending) value of the child property.



Return type
*PGVariant*



Returns
Modified value of the whole property.






            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.FlagsProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetChoiceSelection(self) -> int:
        """ 

`GetChoiceSelection`(*self*)[¶](#wx.propgrid.FlagsProperty.GetChoiceSelection "Permalink to this definition")
Returns which choice is currently selected.


Only applies to properties which have choices.


Needs to reimplemented in derived class if property value does not map directly to a choice. Integer as index, bool, and string usually do.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetItemCount(self) -> int:
        """ 

`GetItemCount`(*self*)[¶](#wx.propgrid.FlagsProperty.GetItemCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def GetLabel(self, ind: int) -> str:
        """ 

`GetLabel`(*self*, *ind*)[¶](#wx.propgrid.FlagsProperty.GetLabel "Permalink to this definition")

Parameters
**ind** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.FlagsProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.FlagsProperty.OnSetValue "wx.propgrid.FlagsProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.FlagsProperty.OnSetValue "wx.propgrid.FlagsProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def RefreshChildren(self) -> None:
        """ 

`RefreshChildren`(*self*)[¶](#wx.propgrid.FlagsProperty.RefreshChildren "Permalink to this definition")
Refresh values of child properties.


Automatically called after value is set.




            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def StringToValue(self, text, argFlags) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags*)[¶](#wx.propgrid.FlagsProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.FlagsProperty.ValueToString "wx.propgrid.FlagsProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.FlagsProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.FlagsProperty.html
        """

    ChoiceSelection: int  # `ChoiceSelection`[¶](#wx.propgrid.FlagsProperty.ChoiceSelection "Permalink to this definition")See [`GetChoiceSelection`](#wx.propgrid.FlagsProperty.GetChoiceSelection "wx.propgrid.FlagsProperty.GetChoiceSelection")
    ItemCount: int  # `ItemCount`[¶](#wx.propgrid.FlagsProperty.ItemCount "Permalink to this definition")See [`GetItemCount`](#wx.propgrid.FlagsProperty.GetItemCount "wx.propgrid.FlagsProperty.GetItemCount")



class FloatProperty(NumericProperty):
    """ **Possible constructors**:



```
FloatProperty(label=PG_LABEL, name=PG_LABEL, value=0.0)

```


Basic property with double-precision floating point value.


  


        Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value=0.0) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=0.0*)[¶](#wx.propgrid.FloatProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*float*) –






            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'PGVariant':
        """ 

`AddSpinStepValue`(*self*, *stepScale*)[¶](#wx.propgrid.FloatProperty.AddSpinStepValue "Permalink to this definition")
Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.


Current value range and wrapping (if enabled) are taken into account. This member has to be implemented in derived properties.



Parameters
**stepScale** (*long*) – SpinCtrl editor step is first multiplied by this factor and next added to the current value.



Return type
*PGVariant*



Returns
Value which property would have after adding SpinCtrl editor step.





Note


Current property value is not changed.





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.FloatProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.FloatProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](wx.propgrid.DirProperty.html#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.FloatProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ 

*static* `GetClassValidator`()[¶](#wx.propgrid.FloatProperty.GetClassValidator "Permalink to this definition")

Return type
*Validator*






            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.FloatProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.FloatProperty.ValueToString "wx.propgrid.FloatProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ 

`ValidateValue`(*self*, *value*, *validationInfo*)[¶](#wx.propgrid.FloatProperty.ValidateValue "Permalink to this definition")
Implement this function in derived class to check the value.


Return `True` if it is ok. Returning `False` prevents property change events from occurring.



Parameters
* **value** (*PGVariant*) –
* **validationInfo** ([*wx.propgrid.PGValidationInfo*](wx.propgrid.PGValidationInfo.html#wx.propgrid.PGValidationInfo "wx.propgrid.PGValidationInfo")) –



Return type
*bool*





Note


* Default implementation always returns `True`.





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.FloatProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.FloatProperty.html
        """



class FontProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
FontProperty(label=PG_LABEL, name=PG_LABEL, value=Font())

```


Property representing Font.


  


        Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=Font()*)[¶](#wx.propgrid.FontProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def ChildChanged(self, thisValue, childIndex, childValue) -> 'PGVariant':
        """ 

`ChildChanged`(*self*, *thisValue*, *childIndex*, *childValue*)[¶](#wx.propgrid.FontProperty.ChildChanged "Permalink to this definition")
Called after value of a child property has been altered.


Must return new value of the whole property (after any alterations warranted by child’s new value).


Note that this function is usually called at the time that value of this property, or given child property, is still pending for change, and as such, result of `GetValue` or m\_value should not be relied on.


Sample pseudo-code implementation:



```
# TBW

```



Parameters
* **thisValue** (*PGVariant*) – Value of this property. Changed value should be returned (in previous versions of  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) it was only necessary to write value back to this argument).
* **childIndex** (*int*) – Index of child changed (you can use Item(childIndex) to get child property).
* **childValue** (*PGVariant*) – (Pending) value of the child property.



Return type
*PGVariant*



Returns
Modified value of the whole property.






            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.FontProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.FontProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.FontProperty.OnSetValue "wx.propgrid.FontProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.FontProperty.OnSetValue "wx.propgrid.FontProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def RefreshChildren(self) -> None:
        """ 

`RefreshChildren`(*self*)[¶](#wx.propgrid.FontProperty.RefreshChildren "Permalink to this definition")
Refresh values of child properties.


Automatically called after value is set.




            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.FontProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.FontProperty.html
        """



class ImageFileProperty(FileProperty):
    """ **Possible constructors**:



```
ImageFileProperty(label=PG_LABEL, name=PG_LABEL, value="")

```


Property representing image file(name).


  


        Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=""*)[¶](#wx.propgrid.ImageFileProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnCustomPaint(self, dc, rect, paintdata) -> None:
        """ 

`OnCustomPaint`(*self*, *dc*, *rect*, *paintdata*)[¶](#wx.propgrid.ImageFileProperty.OnCustomPaint "Permalink to this definition")
Override to paint an image in front of the property value text or drop-down list item (but only if [`wx.propgrid.PGProperty.OnMeasureImage`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnMeasureImage "wx.propgrid.PGProperty.OnMeasureImage") is overridden as well).


If property’s [`OnMeasureImage`](#wx.propgrid.ImageFileProperty.OnMeasureImage "wx.propgrid.ImageFileProperty.OnMeasureImage") returns size that has height != 0 but less than row height ( < 0 has special meanings),  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) calls this method to draw a custom image in a limited area in front of the editor control or value text/graphics, and if control has drop-down list, then the image is drawn there as well (even in the case [`OnMeasureImage`](#wx.propgrid.ImageFileProperty.OnMeasureImage "wx.propgrid.ImageFileProperty.OnMeasureImage") returned higher height than row height).


`NOTE`: Following applies when [`OnMeasureImage`](#wx.propgrid.ImageFileProperty.OnMeasureImage "wx.propgrid.ImageFileProperty.OnMeasureImage") returns a “flexible” height ( using `PG_FLEXIBLE_SIZE(W,H)` macro), which implies variable height items: If (rect.x+rect.width) is < 0, then this is a measure item call, which means that dc is invalid and only thing that should be done is to set paintdata.m\_drawnHeight to the height of the image of item at index paintdata.m\_choiceItem. This call may be done even as often as once every drop-down popup show.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for custom graphics. Includes surrounding rectangle, if any. If x+width is < 0, then this is a measure item call (see above).
* **paintdata** ([*wx.propgrid.PGPaintData*](wx.propgrid.PGPaintData.html#wx.propgrid.PGPaintData "wx.propgrid.PGPaintData")) –  [wx.propgrid.PGPaintData](wx.propgrid.PGPaintData.html#wx-propgrid-pgpaintdata) structure with much useful data about painted item.





Note


* You can actually exceed rect width, but if you do so then paintdata.m\_drawnWidth must be set to the full width drawn in pixels.
* Due to technical reasons, rect’s height will be default even if custom height was reported during measure call.
* Brush is guaranteed to be default background colour. It has been already used to clear the background of area being painted. It can be modified.
* Pen is guaranteed to be 1-wide ‘black’ (or whatever is the proper colour) pen for drawing framing rectangle. It can be changed as well.




See also


[`ValueToString`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.ValueToString "wx.propgrid.FileProperty.ValueToString")





            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnMeasureImage(self, item: int) -> 'Size':
        """ 

`OnMeasureImage`(*self*, *item*)[¶](#wx.propgrid.ImageFileProperty.OnMeasureImage "Permalink to this definition")
Returns size of the custom painted image in front of property.


This method must be overridden to return non-default value if OnCustomPaint is to be called.



Parameters
**item** (*int*) – Normally -1, but can be an index to the property’s list of items.



Return type
*Size*





Note


* Default behaviour is to return  [wx.Size](wx.Size.html#wx-size), which means no image.
* Default image width or height is indicated with dimension -1.
* You can also return `PG_DEFAULT_IMAGE_SIZE` which equals DefaultSize.





            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.ImageFileProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.ImageFileProperty.OnSetValue "wx.propgrid.ImageFileProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.ImageFileProperty.OnSetValue "wx.propgrid.ImageFileProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.ImageFileProperty.html
        """



class IntProperty(NumericProperty):
    """ **Possible constructors**:



```
IntProperty(label=PG_LABEL, name=PG_LABEL, value=0)

IntProperty(label, name, value)

```


Basic property with integer value.


  


        Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.IntProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*long*) –






---

  



**\_\_init\_\_** *(self, label, name, value)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'PGVariant':
        """ 

`AddSpinStepValue`(*self*, *stepScale*)[¶](#wx.propgrid.IntProperty.AddSpinStepValue "Permalink to this definition")
Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.


Current value range and wrapping (if enabled) are taken into account. This member has to be implemented in derived properties.



Parameters
**stepScale** (*long*) – SpinCtrl editor step is first multiplied by this factor and next added to the current value.



Return type
*PGVariant*



Returns
Value which property would have after adding SpinCtrl editor step.





Note


Current property value is not changed.





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.IntProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.IntProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](wx.propgrid.DirProperty.html#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    @staticmethod
    def GetClassValidator() -> 'Validator':
        """ 

*static* `GetClassValidator`()[¶](#wx.propgrid.IntProperty.GetClassValidator "Permalink to this definition")

Return type
*Validator*






            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.IntProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.IntProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.IntProperty.ValueToString "wx.propgrid.IntProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ 

`ValidateValue`(*self*, *value*, *validationInfo*)[¶](#wx.propgrid.IntProperty.ValidateValue "Permalink to this definition")
Implement this function in derived class to check the value.


Return `True` if it is ok. Returning `False` prevents property change events from occurring.



Parameters
* **value** (*PGVariant*) –
* **validationInfo** ([*wx.propgrid.PGValidationInfo*](wx.propgrid.PGValidationInfo.html#wx.propgrid.PGValidationInfo "wx.propgrid.PGValidationInfo")) –



Return type
*bool*





Note


* Default implementation always returns `True`.





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.IntProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.IntProperty.html
        """



class LongStringProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
LongStringProperty(label=PG_LABEL, name=PG_LABEL, value="")

```


Like StringProperty, but has a button that triggers a small text
editor dialog.


  


        Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=""*)[¶](#wx.propgrid.LongStringProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.LongStringProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.LongStringProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.LongStringProperty.ValueToString "wx.propgrid.LongStringProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.LongStringProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.LongStringProperty.html
        """



class MultiChoiceProperty(EditorDialogProperty):
    """ **Possible constructors**:



```
MultiChoiceProperty(label, name=PG_LABEL, choices=[], value=[])

MultiChoiceProperty(label, name, choices, value=[])

MultiChoiceProperty(label=PG_LABEL, name=PG_LABEL, value=[])

```


Property that manages a value resulting from MultiChoiceDialog.


  


        Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.MultiChoiceProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label, name=PG\_LABEL, choices=[], value=[])*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **choices** (*list of strings*) –
* **value** (*list of strings*) –






---

  



**\_\_init\_\_** *(self, label, name, choices, value=[])*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **choices** ([*wx.propgrid.PGChoices*](wx.propgrid.PGChoices.html#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) –
* **value** (*list of strings*) –






---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, value=[])*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*list of strings*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def DisplayEditorDialog(self, pg, value) -> tuple:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.MultiChoiceProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*tuple*



Returns
( *bool*, *value* )






            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def GetValueAsArrayInt(self) -> int:
        """ 

`GetValueAsArrayInt`(*self*)[¶](#wx.propgrid.MultiChoiceProperty.GetValueAsArrayInt "Permalink to this definition")

Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.MultiChoiceProperty.OnSetValue "Permalink to this definition")
This virtual function is called after m\_value has been set.



Note


* If m\_value was set to Null variant (i.e. unspecified value), [`OnSetValue`](#wx.propgrid.MultiChoiceProperty.OnSetValue "wx.propgrid.MultiChoiceProperty.OnSetValue") will not be called.
* m\_value may be of any variant type. Typically properties internally support only one variant type, and as such [`OnSetValue`](#wx.propgrid.MultiChoiceProperty.OnSetValue "wx.propgrid.MultiChoiceProperty.OnSetValue") provides a good opportunity to convert supported values into internal type.
* Default implementation does nothing.





            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.MultiChoiceProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.MultiChoiceProperty.ValueToString "wx.propgrid.MultiChoiceProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.MultiChoiceProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.MultiChoiceProperty.html
        """

    ValueAsArrayInt: int  # `ValueAsArrayInt`[¶](#wx.propgrid.MultiChoiceProperty.ValueAsArrayInt "Permalink to this definition")See [`GetValueAsArrayInt`](#wx.propgrid.MultiChoiceProperty.GetValueAsArrayInt "wx.propgrid.MultiChoiceProperty.GetValueAsArrayInt")



class PropertyCategory(PGProperty):
    """ **Possible constructors**:



```
PropertyCategory()

PropertyCategory(label, name=PG_LABEL)

```


Category (caption) property.


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyCategory.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor is only used in special cases.




---

  



**\_\_init\_\_** *(self, label, name=PG\_LABEL)*



Parameters
* **label** (*string*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def GetTextExtent(self, wnd, font) -> int:
        """ 

`GetTextExtent`(*self*, *wnd*, *font*)[¶](#wx.propgrid.PropertyCategory.GetTextExtent "Permalink to this definition")

Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def GetValueAsString(self, argFlags: int=0) -> str:
        """ 

`GetValueAsString`(*self*, *argFlags=0*)[¶](#wx.propgrid.PropertyCategory.GetValueAsString "Permalink to this definition")
Returns text representation of property’s value.



Parameters
**argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


In older versions, this function used to be overridden to convert property’s value into a string representation. This function is now handled by [`ValueToString`](#wx.propgrid.PropertyCategory.ValueToString "wx.propgrid.PropertyCategory.ValueToString") , and overriding this function now will result in run-time assertion failure.





            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    def ValueToString(self, value, argFlags) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags*)[¶](#wx.propgrid.PropertyCategory.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.PropertyCategory.html
        """

    ValueAsString: str  # `ValueAsString`[¶](#wx.propgrid.PropertyCategory.ValueAsString "Permalink to this definition")See [`GetValueAsString`](#wx.propgrid.PropertyCategory.GetValueAsString "wx.propgrid.PropertyCategory.GetValueAsString")



class StringProperty(PGProperty):
    """ **Possible constructors**:



```
StringProperty(label=PG_LABEL, name=PG_LABEL, value="")

```


Basic property with string value.


  


        Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
    """
    def __init__(self, label=PG_LABEL, name=PG_LABEL, value="") -> None:
        """ 

`__init__`(*self*, *label=PG\_LABEL*, *name=PG\_LABEL*, *value=""*)[¶](#wx.propgrid.StringProperty.__init__ "Permalink to this definition")

Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.StringProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def OnSetValue(self) -> None:
        """ 

`OnSetValue`(*self*)[¶](#wx.propgrid.StringProperty.OnSetValue "Permalink to this definition")
This is updated so “<composed>” special value can be handled.




            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.StringProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.StringProperty.ValueToString "wx.propgrid.StringProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.StringProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls [`GenerateComposedValue`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.GenerateComposedValue "wx.propgrid.PGProperty.GenerateComposedValue") .





            Source: https://docs.wxpython.org/wx.propgrid.StringProperty.html
        """



class UIntProperty(NumericProperty):
    """ **Possible constructors**:



```
UIntProperty(label=PG_LABEL, name=PG_LABEL, value=0)

UIntProperty(label, name, value)

```


Basic property with integer value.


  


        Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.UIntProperty.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, label=PG\_LABEL, name=PG\_LABEL, value=0)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*long*) –






---

  



**\_\_init\_\_** *(self, label, name, value)*



Parameters
* **label** (*string*) –
* **name** (*string*) –
* **value** (*ULongLong*) –






---

  





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def AddSpinStepValue(self, stepScale: int) -> 'PGVariant':
        """ 

`AddSpinStepValue`(*self*, *stepScale*)[¶](#wx.propgrid.UIntProperty.AddSpinStepValue "Permalink to this definition")
Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.


Current value range and wrapping (if enabled) are taken into account. This member has to be implemented in derived properties.



Parameters
**stepScale** (*long*) – SpinCtrl editor step is first multiplied by this factor and next added to the current value.



Return type
*PGVariant*



Returns
Value which property would have after adding SpinCtrl editor step.





Note


Current property value is not changed.





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def DoGetValidator(self) -> 'Validator':
        """ 

`DoGetValidator`(*self*)[¶](#wx.propgrid.UIntProperty.DoGetValidator "Permalink to this definition")
Returns pointer to the  [wx.Validator](wx.Validator.html#wx-validator) that should be used with the editor of this property (`None` for no validator).


Setting validator explicitly via SetPropertyValidator will override this.


In most situations, code like this should work well (macros are used to maintain one actual validator instance, so on the second call the function exits within the first macro):



```
class MyPropertyClass(wx.propgrid.UIntProperty):
    ...
    def DoGetValidator(self):
        validator = MyValidator(...)

        ... prepare validator...

        return validator

```



Return type
*Validator*





Note


You can get common filename validator by returning [`wx.propgrid.FileProperty.GetClassValidator`](wx.propgrid.FileProperty.html#wx.propgrid.FileProperty.GetClassValidator "wx.propgrid.FileProperty.GetClassValidator") .  [wx.propgrid.DirProperty](wx.propgrid.DirProperty.html#wx-propgrid-dirproperty), for example, uses it.





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.UIntProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def IntToValue(self, number, argFlags=0) -> tuple:
        """ 

`IntToValue`(*self*, *number*, *argFlags=0*)[¶](#wx.propgrid.UIntProperty.IntToValue "Permalink to this definition")
Converts integer (possibly a choice selection) into *Variant* value appropriate for this property.



Parameters
* **number** (*int*) – Integer to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one.



Return type
*tuple*



Returns
( *bool*, *variant* )





Note


* If property is not supposed to use choice or spinctrl or other editor with int-based value, it is not necessary to implement this method.
* Default implementation simply assign given int to m\_value.
* If property uses choice control, and displays a dialog on some choice items, then it is preferred to display that dialog in IntToValue instead of OnEvent.
* You might want to take into account that m\_value is Mull variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def StringToValue(self, text, argFlags=0) -> tuple:
        """ 

`StringToValue`(*self*, *text*, *argFlags=0*)[¶](#wx.propgrid.UIntProperty.StringToValue "Permalink to this definition")
Converts text into *Variant* value appropriate for this property.



Parameters
* **text** (*string*) – Text to be translated into variant.
* **argFlags** (*int*) – If `PG_FULL_VALUE` is set, returns complete, storable value instead of displayable one (they may be different). If `PG_COMPOSITE_FRAGMENT` is set, text is interpreted as a part of composite property string value (as generated by [`ValueToString`](#wx.propgrid.UIntProperty.ValueToString "wx.propgrid.UIntProperty.ValueToString") called with this same flag).



Return type
*tuple*




You might want to take into account that m\_value is Null variant if property value is unspecified (which is usually only case if you explicitly enabled that sort behaviour).



Returns
( *bool*, *variant* )





Note


Default implementation converts semicolon delimited tokens into child values. Only works for properties with children.





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def ValidateValue(self, value, validationInfo) -> bool:
        """ 

`ValidateValue`(*self*, *value*, *validationInfo*)[¶](#wx.propgrid.UIntProperty.ValidateValue "Permalink to this definition")
Implement this function in derived class to check the value.


Return `True` if it is ok. Returning `False` prevents property change events from occurring.



Parameters
* **value** (*PGVariant*) –
* **validationInfo** ([*wx.propgrid.PGValidationInfo*](wx.propgrid.PGValidationInfo.html#wx.propgrid.PGValidationInfo "wx.propgrid.PGValidationInfo")) –



Return type
*bool*





Note


* Default implementation always returns `True`.





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """

    def ValueToString(self, value, argFlags=0) -> str:
        """ 

`ValueToString`(*self*, *value*, *argFlags=0*)[¶](#wx.propgrid.UIntProperty.ValueToString "Permalink to this definition")
Converts property value into a text representation.



Parameters
* **value** (*PGVariant*) – Value to be converted.
* **argFlags** (*int*) – If 0 (default value), then displayed string is returned. If `PG_FULL_VALUE` is set, returns complete, storable string value instead of displayable. If `PG_EDITABLE_VALUE` is set, returns string value that must be editable in textctrl. If `PG_COMPOSITE_FRAGMENT` is set, returns text that is appropriate to display as a part of string property’s composite text representation.



Return type
`string`





Note


Default implementation calls `GenerateComposedValue` .





            Source: https://docs.wxpython.org/wx.propgrid.UIntProperty.html
        """



class NumericProperty(PGProperty):
    """ **Possible constructors**:



```
NumericProperty(label, name)

```


This is an abstract class which serves as a base class for numeric
properties, like IntProperty, UIntProperty, FloatProperty.


  


        Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
    """
    def AddSpinStepValue(self, stepScale: int) -> 'PGVariant':
        """ 

`AddSpinStepValue`(*self*, *stepScale*)[¶](#wx.propgrid.NumericProperty.AddSpinStepValue "Permalink to this definition")
Returns what would be the new value of the property after adding SpinCtrl editor step to the current value.


Current value range and wrapping (if enabled) are taken into account. This member has to be implemented in derived properties.



Parameters
**stepScale** (*long*) – SpinCtrl editor step is first multiplied by this factor and next added to the current value.



Return type
*PGVariant*



Returns
Value which property would have after adding SpinCtrl editor step.





Note


Current property value is not changed.





            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.NumericProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def UseSpinMotion(self) -> bool:
        """ 

`UseSpinMotion`(*self*)[¶](#wx.propgrid.NumericProperty.UseSpinMotion "Permalink to this definition")
Return `True` if value can be changed with SpinCtrl editor by moving the mouse.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """

    def __init__(self, label, name) -> None:
        """ 

`__init__`(*self*, *label*, *name*)[¶](#wx.propgrid.NumericProperty.__init__ "Permalink to this definition")
Constructor is protected because  [wx.propgrid.NumericProperty](#wx-propgrid-numericproperty) is only a base class for other numeric property classes.



Parameters
* **label** (*string*) –
* **name** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.NumericProperty.html
        """



class EditorDialogProperty(PGProperty):
    """ **Possible constructors**:



```
EditorDialogProperty(label, name)

```


This is an abstract class which serves as a base class for the
properties having a button triggering an editor dialog, like e.g.


  


        Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
    """
    def DisplayEditorDialog(self, pg, value) -> bool:
        """ 

`DisplayEditorDialog`(*self*, *pg*, *value*)[¶](#wx.propgrid.EditorDialogProperty.DisplayEditorDialog "Permalink to this definition")
Shows editor dialog.


Value to be edited should be read from *value*, and if dialog is not cancelled, it should be stored back and `True` should be returned.



Parameters
* **pg** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **value** (*PGVariant*) – Value to be edited.



Return type
*bool*



Returns
Returns `True` if editor dialog was not cancelled and *value* was updated.






            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def DoSetAttribute(self, name, value) -> bool:
        """ 

`DoSetAttribute`(*self*, *name*, *value*)[¶](#wx.propgrid.EditorDialogProperty.DoSetAttribute "Permalink to this definition")
Reimplement this member function to add special handling for attributes of this property.



Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –



Return type
*bool*



Returns
Return `False` to have the attribute automatically stored in m\_attributes. Default implementation simply does that and nothing else.





Note


To actually set property attribute values from the application, use [`wx.propgrid.PGProperty.SetAttribute`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.SetAttribute "wx.propgrid.PGProperty.SetAttribute") instead.





            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def GetEditorDialog(self) -> 'PGEditorDialogAdapter':
        """ 

`GetEditorDialog`(*self*)[¶](#wx.propgrid.EditorDialogProperty.GetEditorDialog "Permalink to this definition")
Returns instance of a new  [wx.propgrid.PGEditorDialogAdapter](wx.propgrid.PGEditorDialogAdapter.html#wx-propgrid-pgeditordialogadapter) instance, which is used when user presses the (optional) button next to the editor control;.


Default implementation returns `None` (i.e. no action is generated when button is pressed).



Return type
 [wx.propgrid.PGEditorDialogAdapter](wx.propgrid.PGEditorDialogAdapter.html#wx-propgrid-pgeditordialogadapter)






            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    def __init__(self, label, name) -> None:
        """ 

`__init__`(*self*, *label*, *name*)[¶](#wx.propgrid.EditorDialogProperty.__init__ "Permalink to this definition")
Constructor is protected because  [wx.propgrid.EditorDialogProperty](#wx-propgrid-editordialogproperty) is only the base class for other property classes.



Parameters
* **label** (*string*) –
* **name** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.EditorDialogProperty.html
        """

    EditorDialog: 'PGEditorDialogAdapter'  # `EditorDialog`[¶](#wx.propgrid.EditorDialogProperty.EditorDialog "Permalink to this definition")See [`GetEditorDialog`](#wx.propgrid.EditorDialogProperty.GetEditorDialog "wx.propgrid.EditorDialogProperty.GetEditorDialog")



class PGChoices:
    """ **Possible constructors**:



```
PGChoices()

PGChoices(a)

PGChoices(labels, values=[])

PGChoices(data)

```


Helper class for managing choices of PropertyGrid properties.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGChoices.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, a)*


Copy constructor, uses reference counting.


To create a real copy, use [`Copy`](#wx.propgrid.PGChoices.Copy "wx.propgrid.PGChoices.Copy") member function instead.



Parameters
**a** ([*wx.propgrid.PGChoices*](#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) – 






---

  



**\_\_init\_\_** *(self, labels, values=[])*


Constructor.



Parameters
* **labels** (*list of strings*) – Labels for choices.
* **values** (*list of integers*) – Values for choices. If empty, indexes are used. Otherwise must have at least the same size as *labels*.






---

  



**\_\_init\_\_** *(self, data)*


Simple interface constructor.



Parameters
**data** ([*wx.propgrid.PGChoicesData*](wx.propgrid.PGChoicesData.html#wx.propgrid.PGChoicesData "wx.propgrid.PGChoicesData")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Add(self, *args, **kw) -> None:
        """ 

`Add`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGChoices.Add "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Add** *(self, arr, arrint)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **arr** (*list of strings*) –
* **arrint** (*list of integers*) –






---

  



**Add** *(self, label, value=PG\_INVALID\_VALUE)*


Adds a single choice item.



Parameters
* **label** (*string*) – Label for added choice.
* **value** (*int*) – Value for added choice. If unspecified, index is used.



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






---

  



**Add** *(self, label, bitmap, value=PG\_INVALID\_VALUE)*


Adds a single item, with bitmap.



Parameters
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **value** (*int*) –



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






---

  



**Add** *(self, entry)*


Adds a single item with full entry information.



Parameters
**entry** ([*wx.propgrid.PGChoiceEntry*](wx.propgrid.PGChoiceEntry.html#wx.propgrid.PGChoiceEntry "wx.propgrid.PGChoiceEntry")) – 



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AddAsSorted(self, label, value=PG_INVALID_VALUE) -> 'PGChoiceEntry':
        """ 

`AddAsSorted`(*self*, *label*, *value=PG\_INVALID\_VALUE*)[¶](#wx.propgrid.PGChoices.AddAsSorted "Permalink to this definition")
Adds a single item, sorted.



Parameters
* **label** (*string*) –
* **value** (*int*) –



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AllocExclusive(self) -> None:
        """ 

`AllocExclusive`(*self*)[¶](#wx.propgrid.PGChoices.AllocExclusive "Permalink to this definition")
Creates exclusive copy of current choices.




            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Assign(self, a: 'propgrid.PGChoices') -> None:
        """ 

`Assign`(*self*, *a*)[¶](#wx.propgrid.PGChoices.Assign "Permalink to this definition")
Assigns choices data, using reference counting.


To create a real copy, use [`Copy`](#wx.propgrid.PGChoices.Copy "wx.propgrid.PGChoices.Copy") member function instead.



Parameters
**a** ([*wx.propgrid.PGChoices*](#wx.propgrid.PGChoices "wx.propgrid.PGChoices")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def AssignData(self, data: 'propgrid.PGChoicesData') -> None:
        """ 

`AssignData`(*self*, *data*)[¶](#wx.propgrid.PGChoices.AssignData "Permalink to this definition")
Assigns data from another set of choices.



Parameters
**data** ([*wx.propgrid.PGChoicesData*](wx.propgrid.PGChoicesData.html#wx.propgrid.PGChoicesData "wx.propgrid.PGChoicesData")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PGChoices.Clear "Permalink to this definition")
Deletes all items.




            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Copy(self) -> 'PGChoices':
        """ 

`Copy`(*self*)[¶](#wx.propgrid.PGChoices.Copy "Permalink to this definition")
Returns a real copy of the choices.



Return type
 [wx.propgrid.PGChoices](#wx-propgrid-pgchoices)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def EnsureData(self) -> None:
        """ 

`EnsureData`(*self*)[¶](#wx.propgrid.PGChoices.EnsureData "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def ExtractData(self) -> 'PGChoicesData':
        """ 

`ExtractData`(*self*)[¶](#wx.propgrid.PGChoices.ExtractData "Permalink to this definition")
Changes ownership of data to you.



Return type
 [wx.propgrid.PGChoicesData](wx.propgrid.PGChoicesData.html#wx-propgrid-pgchoicesdata)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.propgrid.PGChoices.GetCount "Permalink to this definition")
Returns number of items.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetData(self) -> 'PGChoicesData':
        """ 

`GetData`(*self*)[¶](#wx.propgrid.PGChoices.GetData "Permalink to this definition")
Returns data, increases refcount.



Return type
 [wx.propgrid.PGChoicesData](wx.propgrid.PGChoicesData.html#wx-propgrid-pgchoicesdata)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetDataPtr(self) -> 'PGChoicesData':
        """ 

`GetDataPtr`(*self*)[¶](#wx.propgrid.PGChoices.GetDataPtr "Permalink to this definition")
Returns plain data ptr - no refcounting stuff is done.



Return type
 [wx.propgrid.PGChoicesData](wx.propgrid.PGChoicesData.html#wx-propgrid-pgchoicesdata)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetId(self) -> int:
        """ 

`GetId`(*self*)[¶](#wx.propgrid.PGChoices.GetId "Permalink to this definition")
Gets an number identifying this list.



Return type
*wx.IntPtr*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetIndicesForStrings(self, strings, unmatched=None) -> int:
        """ 

`GetIndicesForStrings`(*self*, *strings*, *unmatched=None*)[¶](#wx.propgrid.PGChoices.GetIndicesForStrings "Permalink to this definition")
Returns array of indices matching given strings.


Unmatching strings are added to ‘unmatched’, if not `None`.



Parameters
* **strings** (*list of strings*) –
* **unmatched** (*list of strings*) –



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetLabel(self, ind: int) -> str:
        """ 

`GetLabel`(*self*, *ind*)[¶](#wx.propgrid.PGChoices.GetLabel "Permalink to this definition")
Returns label of item.



Parameters
**ind** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetLabels(self) -> list[str]:
        """ 

`GetLabels`(*self*)[¶](#wx.propgrid.PGChoices.GetLabels "Permalink to this definition")
Returns array of choice labels.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetValue(self, ind: int) -> int:
        """ 

`GetValue`(*self*, *ind*)[¶](#wx.propgrid.PGChoices.GetValue "Permalink to this definition")
Returns value of item.



Parameters
**ind** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def GetValuesForStrings(self, strings: list[str]) -> int:
        """ 

`GetValuesForStrings`(*self*, *strings*)[¶](#wx.propgrid.PGChoices.GetValuesForStrings "Permalink to this definition")
Returns array of values matching the given strings.


Unmatching strings result in `PG_INVALID_VALUE` entry in array.



Parameters
**strings** (*list of strings*) – 



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Index(self, *args, **kw) -> int:
        """ 

`Index`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGChoices.Index "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Index** *(self, label)*


Returns index of item with given label.



Parameters
**label** (*string*) – 



Return type
*int*






---

  



**Index** *(self, val)*


Returns index of item with given value.



Parameters
**val** (*int*) – 



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Insert(self, *args, **kw) -> 'PGChoiceEntry':
        """ 

`Insert`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGChoices.Insert "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Insert** *(self, label, index, value=PG\_INVALID\_VALUE)*


Inserts a single item.



Parameters
* **label** (*string*) –
* **index** (*int*) –
* **value** (*int*) –



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






---

  



**Insert** *(self, entry, index)*


Inserts a single item with full entry information.



Parameters
* **entry** ([*wx.propgrid.PGChoiceEntry*](wx.propgrid.PGChoiceEntry.html#wx.propgrid.PGChoiceEntry "wx.propgrid.PGChoiceEntry")) –
* **index** (*int*) –



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.propgrid.PGChoices.IsOk "Permalink to this definition")
Returns `False` if this is a constant empty set of choices, which should not be modified.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Item(self, i: int) -> 'PGChoiceEntry':
        """ 

`Item`(*self*, *i*)[¶](#wx.propgrid.PGChoices.Item "Permalink to this definition")
Returns item at given index.



Parameters
**i** (*int*) – 



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def RemoveAt(self, nIndex, count=1) -> None:
        """ 

`RemoveAt`(*self*, *nIndex*, *count=1*)[¶](#wx.propgrid.PGChoices.RemoveAt "Permalink to this definition")
Removes count items starting at position nIndex.



Parameters
* **nIndex** (*int*) –
* **count** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def Set(self, labels, values=[]) -> None:
        """ 

`Set`(*self*, *labels*, *values=[]*)[¶](#wx.propgrid.PGChoices.Set "Permalink to this definition")
This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **labels** (*list of strings*) –
* **values** (*list of integers*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def __getitem__(self, index) -> None:
        """ 

`__getitem__`(*self*, *index*)[¶](#wx.propgrid.PGChoices.__getitem__ "Permalink to this definition")
Returns a reference to a :class:PGChoiceEntry using Python list syntax.




            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    def __len__(self) -> None:
        """ 

`__len__`(*self*)[¶](#wx.propgrid.PGChoices.__len__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoices.html
        """

    Count: int  # `Count`[¶](#wx.propgrid.PGChoices.Count "Permalink to this definition")See [`GetCount`](#wx.propgrid.PGChoices.GetCount "wx.propgrid.PGChoices.GetCount")
    Data: 'PGChoicesData'  # `Data`[¶](#wx.propgrid.PGChoices.Data "Permalink to this definition")See [`GetData`](#wx.propgrid.PGChoices.GetData "wx.propgrid.PGChoices.GetData")
    DataPtr: 'PGChoicesData'  # `DataPtr`[¶](#wx.propgrid.PGChoices.DataPtr "Permalink to this definition")See [`GetDataPtr`](#wx.propgrid.PGChoices.GetDataPtr "wx.propgrid.PGChoices.GetDataPtr")
    Id: int  # `Id`[¶](#wx.propgrid.PGChoices.Id "Permalink to this definition")See [`GetId`](#wx.propgrid.PGChoices.GetId "wx.propgrid.PGChoices.GetId")
    Labels: list[str]  # `Labels`[¶](#wx.propgrid.PGChoices.Labels "Permalink to this definition")See [`GetLabels`](#wx.propgrid.PGChoices.GetLabels "wx.propgrid.PGChoices.GetLabels")



class PGCellRenderer(ObjectRefData):
    """ **Possible constructors**:



```
PGCellRenderer()

```


Base class for PropertyGrid cell renderers.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGCellRenderer.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawCaptionSelectionRect(self, dc, x, y, w, h) -> None:
        """ 

`DrawCaptionSelectionRect`(*self*, *dc*, *x*, *y*, *w*, *h*)[¶](#wx.propgrid.PGCellRenderer.DrawCaptionSelectionRect "Permalink to this definition")
Paints property category selection rectangle.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **x** (*int*) –
* **y** (*int*) –
* **w** (*int*) –
* **h** (*int*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawEditorValue(self, dc, rect, xOffset, text, property, editor) -> None:
        """ 

`DrawEditorValue`(*self*, *dc*, *rect*, *xOffset*, *text*, *property*, *editor*)[¶](#wx.propgrid.PGCellRenderer.DrawEditorValue "Permalink to this definition")
Utility to draw editor’s value, or vertically aligned text if editor is `None`.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **xOffset** (*int*) –
* **text** (*string*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **editor** ([*wx.propgrid.PGEditor*](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor "wx.propgrid.PGEditor")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def DrawText(self, dc, rect, imageWidth, text) -> None:
        """ 

`DrawText`(*self*, *dc*, *rect*, *imageWidth*, *text*)[¶](#wx.propgrid.PGCellRenderer.DrawText "Permalink to this definition")
Utility to draw vertically centered text.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **imageWidth** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def GetImageSize(self, property, column, item) -> 'Size':
        """ 

`GetImageSize`(*self*, *property*, *column*, *item*)[¶](#wx.propgrid.PGCellRenderer.GetImageSize "Permalink to this definition")
Returns size of the image in front of the editable area.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **column** (*int*) –
* **item** (*int*) –



Return type
*Size*





Note


If property is `None`, then this call is for a custom value. In that case the item is index to  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)’s custom values.





            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def PostDrawCell(self, dc, propGrid, cell, flags) -> None:
        """ 

`PostDrawCell`(*self*, *dc*, *propGrid*, *cell*, *flags*)[¶](#wx.propgrid.PGCellRenderer.PostDrawCell "Permalink to this definition")
Utility to be called after drawing is done, to revert whatever changes [`PreDrawCell`](#wx.propgrid.PGCellRenderer.PreDrawCell "wx.propgrid.PGCellRenderer.PreDrawCell") did.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) which was used to paint on.
* **propGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid to which the cell belongs.
* **cell** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) – Cell information.
* **flags** (*int*) – Same as those passed to [`PreDrawCell`](#wx.propgrid.PGCellRenderer.PreDrawCell "wx.propgrid.PGCellRenderer.PreDrawCell") . See [list of render flags](#wx-propgrid-pgcellrenderer).






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def PreDrawCell(self, dc, rect, propGrid, cell, flags) -> int:
        """ 

`PreDrawCell`(*self*, *dc*, *rect*, *propGrid*, *cell*, *flags*)[¶](#wx.propgrid.PGCellRenderer.PreDrawCell "Permalink to this definition")
Utility to render cell bitmap and set text colour plus bg brush colour.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for drawing.
* **propGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid to which the cell belongs.
* **cell** ([*wx.propgrid.PGCell*](wx.propgrid.PGCell.html#wx.propgrid.PGCell "wx.propgrid.PGCell")) – Cell information.
* **flags** (*int*) – See [list of render flags](#wx-propgrid-pgcellrenderer).



Return type
*int*



Returns
Returns image width, which, for instance, can be passed to [`DrawText`](#wx.propgrid.PGCellRenderer.DrawText "wx.propgrid.PGCellRenderer.DrawText") .






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """

    def Render(self, dc, rect, propertyGrid, property, column, item, flags) -> bool:
        """ 

`Render`(*self*, *dc*, *rect*, *propertyGrid*, *property*, *column*, *item*, *flags*)[¶](#wx.propgrid.PGCellRenderer.Render "Permalink to this definition")
Returns `True` if rendered something in the foreground (text or bitmap).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for drawing.
* **propertyGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property to be rendered.
* **column** (*int*) – Property cell column.
* **item** (*int*) – Index of chosen item if combo popup is drawn, -1 otherwise.
* **flags** (*int*) – See [list of render flags](#wx-propgrid-pgcellrenderer).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGCellRenderer.html
        """



PGPropertyFlags: TypeAlias = int  # Enumeration

PG_PROP_MODIFIED: int

PG_PROP_DISABLED: int

PG_PROP_HIDDEN: int

PG_PROP_CUSTOMIMAGE: int

PG_PROP_NOEDITOR: int

PG_PROP_COLLAPSED: int

PG_PROP_INVALID_VALUE: int

PG_PROP_WAS_MODIFIED: int

PG_PROP_AGGREGATE: int

PG_PROP_CHILDREN_ARE_COPIES: int

PG_PROP_PROPERTY: int

PG_PROP_CATEGORY: int

PG_PROP_MISC_PARENT: int

PG_PROP_READONLY: int

PG_PROP_COMPOSED_VALUE: int

PG_PROP_USES_COMMON_VALUE: int

PG_PROP_AUTO_UNSPECIFIED: int

PG_PROP_CLASS_SPECIFIC_1: int

PG_PROP_CLASS_SPECIFIC_2: int

PG_PROP_BEING_DELETED: int

class PGPaintData:
    """ Contains information related to property’s OnCustomPaint.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGPaintData.html
    """
    m_choiceItem: Any  # `m_choiceItem`[¶](#wx.propgrid.PGPaintData.m_choiceItem "Permalink to this definition")A public C++ attribute of type `int`. Normally -1, otherwise index to drop-down list item that has to be drawn.
    m_drawnHeight: Any  # `m_drawnHeight`[¶](#wx.propgrid.PGPaintData.m_drawnHeight "Permalink to this definition")A public C++ attribute of type `int`. In a measure item call, set this to the height of item at m\_choiceItem index.
    m_drawnWidth: Any  # `m_drawnWidth`[¶](#wx.propgrid.PGPaintData.m_drawnWidth "Permalink to this definition")A public C++ attribute of type `int`. Set to drawn width in OnCustomPaint (optional).
    m_parent: Any  # `m_parent`[¶](#wx.propgrid.PGPaintData.m_parent "Permalink to this definition")A public C++ attribute of type [`PropertyGrid`](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid") .  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)



class PGValidationInfo:
    """ Used to convey validation information to and from functions that
actually perform validation.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
    """
    def GetFailureBehavior(self) -> 'byte':
        """ 

`GetFailureBehavior`(*self*)[¶](#wx.propgrid.PGValidationInfo.GetFailureBehavior "Permalink to this definition")

Return type
*wx.byte*



Returns
Returns failure behaviour which is a combination of PropertyGrid Validation Failure behaviour Flags.






            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def GetFailureMessage(self) -> str:
        """ 

`GetFailureMessage`(*self*)[¶](#wx.propgrid.PGValidationInfo.GetFailureMessage "Permalink to this definition")
Returns current failure message.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def GetValue(self) -> 'PGVariant':
        """ 

`GetValue`(*self*)[¶](#wx.propgrid.PGValidationInfo.GetValue "Permalink to this definition")
Returns reference to pending value.



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def SetFailureBehavior(self, failureBehavior: 'byte') -> None:
        """ 

`SetFailureBehavior`(*self*, *failureBehavior*)[¶](#wx.propgrid.PGValidationInfo.SetFailureBehavior "Permalink to this definition")
Set validation failure behaviour.



Parameters
**failureBehavior** (*wx.byte*) – Mixture of PropertyGrid Validation Failure behaviour Flags.






            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    def SetFailureMessage(self, message: str) -> None:
        """ 

`SetFailureMessage`(*self*, *message*)[¶](#wx.propgrid.PGValidationInfo.SetFailureMessage "Permalink to this definition")
Set current failure message.



Parameters
**message** (*string*) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGValidationInfo.html
        """

    FailureBehavior: 'byte'  # `FailureBehavior`[¶](#wx.propgrid.PGValidationInfo.FailureBehavior "Permalink to this definition")See [`GetFailureBehavior`](#wx.propgrid.PGValidationInfo.GetFailureBehavior "wx.propgrid.PGValidationInfo.GetFailureBehavior") and [`SetFailureBehavior`](#wx.propgrid.PGValidationInfo.SetFailureBehavior "wx.propgrid.PGValidationInfo.SetFailureBehavior")
    FailureMessage: str  # `FailureMessage`[¶](#wx.propgrid.PGValidationInfo.FailureMessage "Permalink to this definition")See [`GetFailureMessage`](#wx.propgrid.PGValidationInfo.GetFailureMessage "wx.propgrid.PGValidationInfo.GetFailureMessage") and [`SetFailureMessage`](#wx.propgrid.PGValidationInfo.SetFailureMessage "wx.propgrid.PGValidationInfo.SetFailureMessage")
    Value: 'PGVariant'  # `Value`[¶](#wx.propgrid.PGValidationInfo.Value "Permalink to this definition")See [`GetValue`](#wx.propgrid.PGValidationInfo.GetValue "wx.propgrid.PGValidationInfo.GetValue")



class PGVIterator:
    """ **Possible constructors**:



```
PGVIterator()

PGVIterator(it)

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGVIterator.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, it)*



Parameters
**it** ([*wx.propgrid.PGVIterator*](#wx.propgrid.PGVIterator "wx.propgrid.PGVIterator")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def AtEnd(self) -> bool:
        """ 

`AtEnd`(*self*)[¶](#wx.propgrid.PGVIterator.AtEnd "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def GetProperty(self) -> 'PGProperty':
        """ 

`GetProperty`(*self*)[¶](#wx.propgrid.PGVIterator.GetProperty "Permalink to this definition")

Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def Next(self) -> None:
        """ 

`Next`(*self*)[¶](#wx.propgrid.PGVIterator.Next "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    def UnRef(self) -> None:
        """ 

`UnRef`(*self*)[¶](#wx.propgrid.PGVIterator.UnRef "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGVIterator.html
        """

    Property: 'PGProperty'  # `Property`[¶](#wx.propgrid.PGVIterator.Property "Permalink to this definition")See [`GetProperty`](#wx.propgrid.PGVIterator.GetProperty "wx.propgrid.PGVIterator.GetProperty")



class PGPropArgCls:
    """ **Possible constructors**:



```
PGPropArgCls(property)

PGPropArgCls(str)

PGPropArgCls(id)

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGPropArgCls.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, property)*



Parameters
**property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – 






---

  



**\_\_init\_\_** *(self, str)*


Creates a PGPropArgCls from a string.




---

  



**\_\_init\_\_** *(self, id)*



Parameters
**id** ([*wx.propgrid.PGPropArgCls*](#wx.propgrid.PGPropArgCls "wx.propgrid.PGPropArgCls")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGPropArgCls.GetName "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetPtr(self, *args, **kw) -> 'PGProperty':
        """ 

`GetPtr`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PGPropArgCls.GetPtr "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetPtr** *(self)*



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






---

  



**GetPtr** *(self, iface)*



Parameters
**iface** ([*wx.propgrid.PropertyGridInterface*](wx.propgrid.PropertyGridInterface.html#wx.propgrid.PropertyGridInterface "wx.propgrid.PropertyGridInterface")) – 



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def GetPtr0(self) -> 'PGProperty':
        """ 

`GetPtr0`(*self*)[¶](#wx.propgrid.PGPropArgCls.GetPtr0 "Permalink to this definition")

Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    def HasName(self) -> bool:
        """ 

`HasName`(*self*)[¶](#wx.propgrid.PGPropArgCls.HasName "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGPropArgCls.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGPropArgCls.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGPropArgCls.GetName "wx.propgrid.PGPropArgCls.GetName")
    Ptr: 'PGProperty'  # `Ptr`[¶](#wx.propgrid.PGPropArgCls.Ptr "Permalink to this definition")See [`GetPtr`](#wx.propgrid.PGPropArgCls.GetPtr "wx.propgrid.PGPropArgCls.GetPtr")
    Ptr0: 'PGProperty'  # `Ptr0`[¶](#wx.propgrid.PGPropArgCls.Ptr0 "Permalink to this definition")See [`GetPtr0`](#wx.propgrid.PGPropArgCls.GetPtr0 "wx.propgrid.PGPropArgCls.GetPtr0")



class PropertyGridHitTestResult:
    """ **Possible constructors**:



```
PropertyGridHitTestResult()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PropertyGridHitTestResult.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetColumn(self) -> int:
        """ 

`GetColumn`(*self*)[¶](#wx.propgrid.PropertyGridHitTestResult.GetColumn "Permalink to this definition")
Returns column hit.


-1 for margin.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetProperty(self) -> 'PGProperty':
        """ 

`GetProperty`(*self*)[¶](#wx.propgrid.PropertyGridHitTestResult.GetProperty "Permalink to this definition")
Returns property hit.


`None` if empty space below properties was hit instead.



Return type
 [wx.propgrid.PGProperty](wx.propgrid.PGProperty.html#wx-propgrid-pgproperty)






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetSplitter(self) -> int:
        """ 

`GetSplitter`(*self*)[¶](#wx.propgrid.PropertyGridHitTestResult.GetSplitter "Permalink to this definition")
Returns index of splitter hit, -1 for none.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    def GetSplitterHitOffset(self) -> int:
        """ 

`GetSplitterHitOffset`(*self*)[¶](#wx.propgrid.PropertyGridHitTestResult.GetSplitterHitOffset "Permalink to this definition")
If splitter hit, then this member function returns offset to the exact splitter position.



Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridHitTestResult.html
        """

    Column: int  # `Column`[¶](#wx.propgrid.PropertyGridHitTestResult.Column "Permalink to this definition")See [`GetColumn`](#wx.propgrid.PropertyGridHitTestResult.GetColumn "wx.propgrid.PropertyGridHitTestResult.GetColumn")
    Property: 'PGProperty'  # `Property`[¶](#wx.propgrid.PropertyGridHitTestResult.Property "Permalink to this definition")See [`GetProperty`](#wx.propgrid.PropertyGridHitTestResult.GetProperty "wx.propgrid.PropertyGridHitTestResult.GetProperty")
    Splitter: int  # `Splitter`[¶](#wx.propgrid.PropertyGridHitTestResult.Splitter "Permalink to this definition")See [`GetSplitter`](#wx.propgrid.PropertyGridHitTestResult.GetSplitter "wx.propgrid.PropertyGridHitTestResult.GetSplitter")
    SplitterHitOffset: int  # `SplitterHitOffset`[¶](#wx.propgrid.PropertyGridHitTestResult.SplitterHitOffset "Permalink to this definition")See [`GetSplitterHitOffset`](#wx.propgrid.PropertyGridHitTestResult.GetSplitterHitOffset "wx.propgrid.PropertyGridHitTestResult.GetSplitterHitOffset")



PG_ITERATE_PROPERTIES: int

PG_ITERATE_HIDDEN: int

PG_ITERATE_FIXED_CHILDREN: int

PG_ITERATE_CATEGORIES: int

PG_ITERATE_ALL_PARENTS: int

PG_ITERATE_ALL_PARENTS_RECURSIVELY: int

PG_ITERATOR_FLAGS_ALL: int

PG_ITERATOR_MASK_OP_ITEM: int

PG_ITERATOR_MASK_OP_PARENT: int

PG_ITERATE_VISIBLE: int

PG_ITERATE_ALL: int

PG_ITERATE_NORMAL: int

class PropertyGridIterator(PropertyGridIteratorBase):
    """ **Possible constructors**:



```
PropertyGridIterator()

PropertyGridIterator(state, flags=PG_ITERATE_DEFAULT, property=None,
                     dir=1)

PropertyGridIterator(state, flags, startPos, dir=0)

PropertyGridIterator(it)

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PropertyGridIterator.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.propgrid.PropertyGridIterator.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, state, flags=PG\_ITERATE\_DEFAULT, property=None, dir=1)*



Parameters
* **state** ([*wx.propgrid.PropertyGridPageState*](wx.propgrid.PropertyGridPageState.html#wx.propgrid.PropertyGridPageState "wx.propgrid.PropertyGridPageState")) –
* **flags** (*int*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **dir** (*int*) –






---

  



**\_\_init\_\_** *(self, state, flags, startPos, dir=0)*



Parameters
* **state** ([*wx.propgrid.PropertyGridPageState*](wx.propgrid.PropertyGridPageState.html#wx.propgrid.PropertyGridPageState "wx.propgrid.PropertyGridPageState")) –
* **flags** (*int*) –
* **startPos** (*int*) –
* **dir** (*int*) –






---

  



**\_\_init\_\_** *(self, it)*



Parameters
**it** ([*wx.propgrid.PropertyGridIterator*](#wx.propgrid.PropertyGridIterator "wx.propgrid.PropertyGridIterator")) – 






---

  





            Source: https://docs.wxpython.org/wx.propgrid.PropertyGridIterator.html
        """



class PGAttributeStorage:
    """ **Possible constructors**:



```
PGAttributeStorage()

```


PGAttributeStorage is somewhat optimized storage for key=variant
pairs (i.e.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGAttributeStorage.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def FindValue(self, name: str) -> 'PGVariant':
        """ 

`FindValue`(*self*, *name*)[¶](#wx.propgrid.PGAttributeStorage.FindValue "Permalink to this definition")

Parameters
**name** (*string*) – 



Return type
*PGVariant*






            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.propgrid.PGAttributeStorage.GetCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    def Set(self, name, value) -> None:
        """ 

`Set`(*self*, *name*, *value*)[¶](#wx.propgrid.PGAttributeStorage.Set "Permalink to this definition")

Parameters
* **name** (*string*) –
* **value** (*PGVariant*) –






            Source: https://docs.wxpython.org/wx.propgrid.PGAttributeStorage.html
        """

    Count: int  # `Count`[¶](#wx.propgrid.PGAttributeStorage.Count "Permalink to this definition")See [`GetCount`](#wx.propgrid.PGAttributeStorage.GetCount "wx.propgrid.PGAttributeStorage.GetCount")



class PGChoiceAndButtonEditor(PGChoiceEditor):
    """ **Possible constructors**:



```
PGChoiceAndButtonEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGChoiceAndButtonEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGChoiceAndButtonEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGChoiceAndButtonEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGChoiceAndButtonEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGChoiceAndButtonEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGChoiceAndButtonEditor.GetName "wx.propgrid.PGChoiceAndButtonEditor.GetName")



class PGComboBoxEditor(PGChoiceEditor):
    """ **Possible constructors**:



```
PGComboBoxEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGComboBoxEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGComboBoxEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGComboBoxEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def GetValueFromControl(self, variant, property, ctrl) -> bool:
        """ 

`GetValueFromControl`(*self*, *variant*, *property*, *ctrl*)[¶](#wx.propgrid.PGComboBoxEditor.GetValueFromControl "Permalink to this definition")
Returns value from control, via parameter *variant*.


Usually ends up calling property’s StringToValue() or IntToValue(). Returns `True` if value was different.



Parameters
* **variant** (*PGVariant*) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGComboBoxEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def OnFocus(self, property, wnd) -> None:
        """ 

`OnFocus`(*self*, *property*, *wnd*)[¶](#wx.propgrid.PGComboBoxEditor.OnFocus "Permalink to this definition")
Extra processing when control gains focus.


For example,  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) based controls should select all text.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    def UpdateControl(self, property, ctrl) -> None:
        """ 

`UpdateControl`(*self*, *property*, *ctrl*)[¶](#wx.propgrid.PGComboBoxEditor.UpdateControl "Permalink to this definition")
Loads value from property to the control.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **ctrl** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.propgrid.PGComboBoxEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGComboBoxEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGComboBoxEditor.GetName "wx.propgrid.PGComboBoxEditor.GetName")



class PGSpinCtrlEditor(PGTextCtrlEditor):
    """ 
  


        Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
    """
    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGSpinCtrlEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGSpinCtrlEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    def OnEvent(self, propgrid, property, wnd_primary, event) -> bool:
        """ 

`OnEvent`(*self*, *propgrid*, *property*, *wnd\_primary*, *event*)[¶](#wx.propgrid.PGSpinCtrlEditor.OnEvent "Permalink to this definition")
Handles events.


Returns `True` if value in control was modified (see [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") for more information).



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **wnd\_primary** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –



Return type
*bool*





Note


 [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) will automatically unfocus the editor when `wxEVT_TEXT_ENTER` is received and when it results in property value being modified. This happens regardless of editor type (i.e. behaviour is same for any  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) and  [wx.ComboBox](wx.ComboBox.html#wx-combobox) based editor).





            Source: https://docs.wxpython.org/wx.propgrid.PGSpinCtrlEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGSpinCtrlEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGSpinCtrlEditor.GetName "wx.propgrid.PGSpinCtrlEditor.GetName")



class PGTextCtrlAndButtonEditor(PGTextCtrlEditor):
    """ **Possible constructors**:



```
PGTextCtrlAndButtonEditor()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGTextCtrlAndButtonEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    def CreateControls(self, propgrid, property, pos, size) -> 'PGWindowList':
        """ 

`CreateControls`(*self*, *propgrid*, *property*, *pos*, *size*)[¶](#wx.propgrid.PGTextCtrlAndButtonEditor.CreateControls "Permalink to this definition")
Instantiates editor controls.



Parameters
* **propgrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) –  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid) to which the property belongs (use as parent for control).
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property for which this method is called.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position, inside  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid), to create control(s) to.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size for control(s).



Return type
 [wx.propgrid.PGWindowList](wx.propgrid.PGWindowList.html#wx-propgrid-pgwindowlist)





Note


* It is not necessary to call [`wx.EvtHandler.Bind`](wx.EvtHandler.html#wx.EvtHandler.Bind "wx.EvtHandler.Bind") for interesting editor events. All events from controls are automatically forwarded to [`wx.propgrid.PGEditor.OnEvent`](wx.propgrid.PGEditor.html#wx.propgrid.PGEditor.OnEvent "wx.propgrid.PGEditor.OnEvent") and [`wx.propgrid.PGProperty.OnEvent`](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty.OnEvent "wx.propgrid.PGProperty.OnEvent") .





            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.propgrid.PGTextCtrlAndButtonEditor.GetName "Permalink to this definition")
Returns pointer to the name of the editor.


For example, PGEditor\_TextCtrl has name “TextCtrl”. If you don’t need to access your custom editor by string name, then you do not need to implement this function.



Return type
`string`






            Source: https://docs.wxpython.org/wx.propgrid.PGTextCtrlAndButtonEditor.html
        """

    Name: str  # `Name`[¶](#wx.propgrid.PGTextCtrlAndButtonEditor.Name "Permalink to this definition")See [`GetName`](#wx.propgrid.PGTextCtrlAndButtonEditor.GetName "wx.propgrid.PGTextCtrlAndButtonEditor.GetName")



class PGChoicesData(ObjectRefData):
    """ **Possible constructors**:



```
PGChoicesData()

```


  


        Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.propgrid.PGChoicesData.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.propgrid.PGChoicesData.Clear "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def CopyDataFrom(self, data: 'propgrid.PGChoicesData') -> None:
        """ 

`CopyDataFrom`(*self*, *data*)[¶](#wx.propgrid.PGChoicesData.CopyDataFrom "Permalink to this definition")

Parameters
**data** ([*wx.propgrid.PGChoicesData*](#wx.propgrid.PGChoicesData "wx.propgrid.PGChoicesData")) – 






            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.propgrid.PGChoicesData.GetCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Insert(self, index, item) -> 'PGChoiceEntry':
        """ 

`Insert`(*self*, *index*, *item*)[¶](#wx.propgrid.PGChoicesData.Insert "Permalink to this definition")

Parameters
* **index** (*int*) –
* **item** ([*wx.propgrid.PGChoiceEntry*](wx.propgrid.PGChoiceEntry.html#wx.propgrid.PGChoiceEntry "wx.propgrid.PGChoiceEntry")) –



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    def Item(self, i: int) -> 'PGChoiceEntry':
        """ 

`Item`(*self*, *i*)[¶](#wx.propgrid.PGChoicesData.Item "Permalink to this definition")

Parameters
**i** (*int*) – 



Return type
 [wx.propgrid.PGChoiceEntry](wx.propgrid.PGChoiceEntry.html#wx-propgrid-pgchoiceentry)






            Source: https://docs.wxpython.org/wx.propgrid.PGChoicesData.html
        """

    Count: int  # `Count`[¶](#wx.propgrid.PGChoicesData.Count "Permalink to this definition")See [`GetCount`](#wx.propgrid.PGChoicesData.GetCount "wx.propgrid.PGChoicesData.GetCount")



class PGDefaultRenderer(PGCellRenderer):
    """ Default cell renderer, that can handles the common scenarios.


  


        Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
    """
    def GetImageSize(self, property, column, item) -> 'Size':
        """ 

`GetImageSize`(*self*, *property*, *column*, *item*)[¶](#wx.propgrid.PGDefaultRenderer.GetImageSize "Permalink to this definition")
Returns size of the image in front of the editable area.



Parameters
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) –
* **column** (*int*) –
* **item** (*int*) –



Return type
*Size*





Note


If property is `None`, then this call is for a custom value. In that case the item is index to  [wx.propgrid.PropertyGrid](wx.propgrid.PropertyGrid.html#wx-propgrid-propertygrid)’s custom values.





            Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
        """

    def Render(self, dc, rect, propertyGrid, property, column, item, flags) -> bool:
        """ 

`Render`(*self*, *dc*, *rect*, *propertyGrid*, *property*, *column*, *item*, *flags*)[¶](#wx.propgrid.PGDefaultRenderer.Render "Permalink to this definition")
Returns `True` if rendered something in the foreground (text or bitmap.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –  [wx.DC](wx.DC.html#wx-dc) to paint on.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Box reserved for drawing.
* **propertyGrid** ([*wx.propgrid.PropertyGrid*](wx.propgrid.PropertyGrid.html#wx.propgrid.PropertyGrid "wx.propgrid.PropertyGrid")) – Property grid in which property is displayed.
* **property** ([*wx.propgrid.PGProperty*](wx.propgrid.PGProperty.html#wx.propgrid.PGProperty "wx.propgrid.PGProperty")) – Property to be rendered.
* **column** (*int*) – Property cell column.
* **item** (*int*) – Index of chosen item if combo popup is drawn, -1 otherwise.
* **flags** (*int*) – See [list of render flags](wx.propgrid.PGCellRenderer.html#wx-propgrid-pgcellrenderer).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.propgrid.PGDefaultRenderer.html
        """



PGVariant: TypeAlias = Any

byte: TypeAlias = bytes

ArrayPGProperty: TypeAlias = list['PGProperty']

FlagType: TypeAlias = int  # Enumeration

