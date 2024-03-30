# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import CommandEvent, _DragResult, DragResult, Control, TextEntry, Colour, TextAttr, Point, VisualAttributes, VersionInfo, MemoryBuffer, Font

class StyledTextEvent(CommandEvent):
    """ **Possible constructors**:



```
StyledTextEvent(commandType=0, id=0)

StyledTextEvent(event)

```


The type of events sent from StyledTextCtrl.


  


        Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.stc.StyledTextEvent.__init__ "Permalink to this definition")
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
**event** ([*wx.stc.StyledTextEvent*](#wx.stc.StyledTextEvent "wx.stc.StyledTextEvent")) – 






---

  





            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetAlt(self) -> bool:
        """ 

`GetAlt`(*self*)[¶](#wx.stc.StyledTextEvent.GetAlt "Permalink to this definition")
Returns `True` if the Alt key is pressed.


This method is valid for the following event types:


* `wxEVT_STC_DOUBLECLICK`
* `wxEVT_STC_MARGINCLICK`
* `wxEVT_STC_HOTSPOT_CLICK`
* `wxEVT_STC_HOTSPOT_DCLICK`
* `wxEVT_STC_HOTSPOT_RELEASE_CLICK`
* `wxEVT_STC_INDICATOR_CLICK`
* `wxEVT_STC_INDICATOR_RELEASE`
* `wxEVT_STC_MARGIN_RIGHT_CLICK`



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetAnnotationsLinesAdded(self) -> int:
        """ 

`GetAnnotationsLinesAdded`(*self*)[¶](#wx.stc.StyledTextEvent.GetAnnotationsLinesAdded "Permalink to this definition")
Returns the number of lines that have been added to or removed from an annotation.


This method is valid for `wxEVT_STC_MODIFIED` events when the result of [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") includes `STC_MOD_CHANGEANNOTATION`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetControl(self) -> bool:
        """ 

`GetControl`(*self*)[¶](#wx.stc.StyledTextEvent.GetControl "Permalink to this definition")
Returns `True` if the Control key is pressed.


This method is valid for the following event types:


* `wxEVT_STC_DOUBLECLICK`
* `wxEVT_STC_MARGINCLICK`
* `wxEVT_STC_HOTSPOT_CLICK`
* `wxEVT_STC_HOTSPOT_DCLICK`
* `wxEVT_STC_HOTSPOT_RELEASE_CLICK`
* `wxEVT_STC_INDICATOR_CLICK`
* `wxEVT_STC_INDICATOR_RELEASE`
* `wxEVT_STC_MARGIN_RIGHT_CLICK`



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragFlags(self) -> int:
        """ 

`GetDragFlags`(*self*)[¶](#wx.stc.StyledTextEvent.GetDragFlags "Permalink to this definition")
Returns flags for the drag operation associated with this event.


This method is valid for `wxEVT_STC_START_DRAG` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragResult(self) -> 'DragResult':
        """ 

`GetDragResult`(*self*)[¶](#wx.stc.StyledTextEvent.GetDragResult "Permalink to this definition")
Returns drag result for this event.


This method is valid for `wxEVT_STC_DRAG_OVER` and `wxEVT_STC_DO_DROP` events.



Return type
 [wx.DragResult](wx.DragResult.enumeration.html#wx-dragresult)






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetDragText(self) -> str:
        """ 

`GetDragText`(*self*)[¶](#wx.stc.StyledTextEvent.GetDragText "Permalink to this definition")

Return type
`string`





Deprecated


Use [`GetString`](wx.CommandEvent.html#wx.CommandEvent.GetString "wx.CommandEvent.GetString") instead.





            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetFoldLevelNow(self) -> int:
        """ 

`GetFoldLevelNow`(*self*)[¶](#wx.stc.StyledTextEvent.GetFoldLevelNow "Permalink to this definition")
Returns the current fold level for the line.


This method is valid for `wxEVT_STC_MODIFIED` events when the result of [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") includes `STC_MOD_CHANGEFOLD`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetFoldLevelPrev(self) -> int:
        """ 

`GetFoldLevelPrev`(*self*)[¶](#wx.stc.StyledTextEvent.GetFoldLevelPrev "Permalink to this definition")
Returns previous fold level for the line.


This method is valid for `wxEVT_STC_MODIFIED` events when the result of [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") includes `STC_MOD_CHANGEFOLD`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetKey(self) -> int:
        """ 

`GetKey`(*self*)[¶](#wx.stc.StyledTextEvent.GetKey "Permalink to this definition")
Returns the key code of the key that generated this event.


This method is valid for the following event types:


* `wxEVT_STC_CHARADDED`
* `wxEVT_STC_USERLISTSELECTION`
* `wxEVT_STC_AUTOCOMP_SELECTION`
* `wxEVT_STC_AUTOCOMP_COMPLETED`



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLParam(self) -> int:
        """ 

`GetLParam`(*self*)[¶](#wx.stc.StyledTextEvent.GetLParam "Permalink to this definition")
Returns the value of the LParam field for this event.


This method is valid for `wxEVT_STC_MACRORECORD` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLength(self) -> int:
        """ 

`GetLength`(*self*)[¶](#wx.stc.StyledTextEvent.GetLength "Permalink to this definition")
Returns the length (number of characters) of this event.


This method is valid for `wxEVT_STC_MODIFIED` and `wxEVT_STC_NEEDSHOWN` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLine(self) -> int:
        """ 

`GetLine`(*self*)[¶](#wx.stc.StyledTextEvent.GetLine "Permalink to this definition")
Returns zero-based line number for this event.


This method is valid for `wxEVT_STC_DOUBLECLICK` and `wxEVT_STC_MODIFIED` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetLinesAdded(self) -> int:
        """ 

`GetLinesAdded`(*self*)[¶](#wx.stc.StyledTextEvent.GetLinesAdded "Permalink to this definition")
Returns the number of lines added or deleted with this event.


This method is valid for `wxEVT_STC_MODIFIED` events when the result of [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") includes `STC_MOD_INSERTTEXT ``   or ``STC_MOD_DELETETEXT`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetListCompletionMethod(self) -> int:
        """ 

`GetListCompletionMethod`(*self*)[¶](#wx.stc.StyledTextEvent.GetListCompletionMethod "Permalink to this definition")
Returns a value describing the action that closed the list.


The returned value will be one of the following constants:







| `STC_AC_FILLUP` | A fillup character caused the completion. |
| --- | --- |
| `STC_AC_DOUBLECLICK` | A double-click caused the completion. |
| `STC_AC_TAB` | The tab key caused the completion. |
| `STC_AC_NEWLINE` | The enter key caused the completion. |
| `STC_AC_COMMAND` | The [`wx.stc.StyledTextCtrl.AutoCompComplete`](wx.stc.StyledTextCtrl.html#wx.stc.StyledTextCtrl.AutoCompComplete "wx.stc.StyledTextCtrl.AutoCompComplete") method was called. |



  


This method is valid for `wxEVT_STC_USERLISTSELECTION` , `wxEVT_STC_AUTOCOMP_SELECTION` , and `wxEVT_STC_AUTOCOMP_COMPLETED` events.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetListType(self) -> int:
        """ 

`GetListType`(*self*)[¶](#wx.stc.StyledTextEvent.GetListType "Permalink to this definition")
Returns the list type for this event.


The list type is an integer passed to a list when it is created with the [`wx.stc.StyledTextCtrl.UserListShow`](wx.stc.StyledTextCtrl.html#wx.stc.StyledTextCtrl.UserListShow "wx.stc.StyledTextCtrl.UserListShow") method and can be used to distinguish lists if more than one is used.


This method is valid for `wxEVT_STC_AUTOCOMP_SELECTION_CHANGE` and `wxEVT_STC_USERLISTSELECTION` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetMargin(self) -> int:
        """ 

`GetMargin`(*self*)[¶](#wx.stc.StyledTextEvent.GetMargin "Permalink to this definition")
Returns the zero-based index of the margin that generated this event.


This method is valid for `wxEVT_STC_MARGINCLICK` and `wxEVT_STC_MARGIN_RIGHT_CLICK` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetMessage(self) -> int:
        """ 

`GetMessage`(*self*)[¶](#wx.stc.StyledTextEvent.GetMessage "Permalink to this definition")
Returns a message number while a macro is being recorded.


Many of the  [wx.stc.StyledTextCtrl](wx.stc.StyledTextCtrl.html#wx-stc-styledtextctrl) methods such as `InsertText` and `Paste` have an event number associated with them. This method returns that number while a macro is being recorded so that the macro can be played back later.


This method is valid for `wxEVT_STC_MACRORECORD` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetModificationType(self) -> int:
        """ 

`GetModificationType`(*self*)[¶](#wx.stc.StyledTextEvent.GetModificationType "Permalink to this definition")
Returns the modification type for this event.


The modification type is a bit list that describes the change that generated this event. It may contain one or more of the following values:


* [``](#id1)STC\_MOD\_INSERTTEXT ``
* [``](#id3)STC\_MOD\_DELETETEXT ``
* [``](#id5)STC\_MOD\_CHANGESTYLE ``
* [``](#id7)STC\_MOD\_CHANGEFOLD ``
* [``](#id9)STC\_PERFORMED\_USER ``
* [``](#id11)STC\_PERFORMED\_UNDO ``
* [``](#id13)STC\_PERFORMED\_REDO ``
* [``](#id15)STC\_MULTISTEPUNDOREDO ``
* [``](#id17)STC\_LASTSTEPINUNDOREDO ``
* [``](#id19)STC\_MOD\_CHANGEMARKER ``
* [``](#id21)STC\_MOD\_BEFOREINSERT ``
* [``](#id23)STC\_MOD\_BEFOREDELETE ``
* [``](#id25)STC\_MULTILINEUNDOREDO ``
* [``](#id27)STC\_STARTACTION ``
* [``](#id29)STC\_MOD\_CHANGEINDICATOR ``
* [``](#id31)STC\_MOD\_CHANGELINESTATE ``
* [``](#id33)STC\_MOD\_CHANGEMARGIN ``
* [``](#id35)STC\_MOD\_CHANGEANNOTATION ``
* [``](#id37)STC\_MOD\_CONTAINER ``
* [``](#id39)STC\_MOD\_LEXERSTATE ``
* [``](#id41)STC\_MOD\_INSERTCHECK ``
* [``](#id43)STC\_MOD\_CHANGETABSTOPS ``


This method is valid for `wxEVT_STC_MODIFIED` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetModifiers(self) -> int:
        """ 

`GetModifiers`(*self*)[¶](#wx.stc.StyledTextEvent.GetModifiers "Permalink to this definition")
Returns the modifiers of the key press or mouse click for this event.


The returned value is a bit list that may contain one or more of the following values:


* [``](#id45)STC\_KEYMOD\_SHIFT ``
* [``](#id47)STC\_KEYMOD\_CTRL ``
* [``](#id49)STC\_KEYMOD\_ALT ``
* [``](#id51)STC\_KEYMOD\_SUPER ``
* [``](#id53)STC\_KEYMOD\_META ``


In addition, the value can be checked for equality with [``](#id55)STC\_KEYMOD\_NORM `` to test if no modifiers are present.


This method is valid for the following event types:


* `wxEVT_STC_DOUBLECLICK`
* `wxEVT_STC_MARGINCLICK`
* `wxEVT_STC_HOTSPOT_CLICK`
* `wxEVT_STC_HOTSPOT_DCLICK`
* `wxEVT_STC_HOTSPOT_RELEASE_CLICK`
* `wxEVT_STC_INDICATOR_CLICK`
* `wxEVT_STC_INDICATOR_RELEASE`
* `wxEVT_STC_MARGIN_RIGHT_CLICK`



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetPosition(self) -> int:
        """ 

`GetPosition`(*self*)[¶](#wx.stc.StyledTextEvent.GetPosition "Permalink to this definition")
Returns the zero-based text position associated this event.


This method is valid for the following event types:


* `wxEVT_STC_STYLENEEDED`
* `wxEVT_STC_DOUBLECLICK`
* `wxEVT_STC_MODIFIED`
* `wxEVT_STC_MARGINCLICK`
* `wxEVT_STC_NEEDSHOWN`
* `wxEVT_STC_USERLISTSELECTION`
* `wxEVT_STC_DWELLSTART`
* `wxEVT_STC_DWELLEND`
* `wxEVT_STC_HOTSPOT_CLICK`
* `wxEVT_STC_HOTSPOT_DCLICK`
* `wxEVT_STC_HOTSPOT_RELEASE_CLICK`
* `wxEVT_STC_INDICATOR_CLICK`
* `wxEVT_STC_INDICATOR_RELEASE`
* `wxEVT_STC_CALLTIP_CLICK`
* `wxEVT_STC_AUTOCOMP_SELECTION`
* `wxEVT_STC_AUTOCOMP_SELECTION_CHANGE`
* `wxEVT_STC_AUTOCOMP_COMPLETED`
* `wxEVT_STC_MARGIN_RIGHT_CLICK`



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetShift(self) -> bool:
        """ 

`GetShift`(*self*)[¶](#wx.stc.StyledTextEvent.GetShift "Permalink to this definition")
Returns `True` if the Shift key is pressed.


This method is valid for the following event types:


* `wxEVT_STC_DOUBLECLICK`
* `wxEVT_STC_MARGINCLICK`
* `wxEVT_STC_HOTSPOT_CLICK`
* `wxEVT_STC_HOTSPOT_DCLICK`
* `wxEVT_STC_HOTSPOT_RELEASE_CLICK`
* `wxEVT_STC_INDICATOR_CLICK`
* `wxEVT_STC_INDICATOR_RELEASE`
* `wxEVT_STC_MARGIN_RIGHT_CLICK`



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.stc.StyledTextEvent.GetText "Permalink to this definition")

Return type
`string`





Deprecated


Use [`GetString`](wx.CommandEvent.html#wx.CommandEvent.GetString "wx.CommandEvent.GetString") instead.





            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetToken(self) -> int:
        """ 

`GetToken`(*self*)[¶](#wx.stc.StyledTextEvent.GetToken "Permalink to this definition")
Returns the token value for this event.


The token is an integer value that can be set with a call to the [`wx.stc.StyledTextCtrl.AddUndoAction`](wx.stc.StyledTextCtrl.html#wx.stc.StyledTextCtrl.AddUndoAction "wx.stc.StyledTextCtrl.AddUndoAction") method.


This method is valid for `wxEVT_STC_MODIFIED` events when the result of [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") includes `STC_MOD_CONTAINER`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetUpdated(self) -> int:
        """ 

`GetUpdated`(*self*)[¶](#wx.stc.StyledTextEvent.GetUpdated "Permalink to this definition")
Returns the value of the updated field for this event.


The value of this field is a bit list that describes the change that generated this event. It may contain one or more of the following values:


* [``](#id57)STC\_UPDATE\_CONTENT ``
* [``](#id59)STC\_UPDATE\_SELECTION ``
* [``](#id61)STC\_UPDATE\_V\_SCROLL ``
* [``](#id63)STC\_UPDATE\_H\_SCROLL ``


This method is valid for `wxEVT_STC_UPDATEUI` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetWParam(self) -> int:
        """ 

`GetWParam`(*self*)[¶](#wx.stc.StyledTextEvent.GetWParam "Permalink to this definition")
Returns value of the WParam field for this event.


This method is valid for `wxEVT_STC_MACRORECORD` events.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetX(self) -> int:
        """ 

`GetX`(*self*)[¶](#wx.stc.StyledTextEvent.GetX "Permalink to this definition")
Returns the X coordinate of the mouse for this event.


This method is valid for the following event types:


* `wxEVT_STC_DWELLSTART`
* `wxEVT_STC_DWELLEND`
* `wxEVT_STC_START_DRAG`
* `wxEVT_STC_DRAG_OVER`
* `wxEVT_STC_DO_DROP`



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def GetY(self) -> int:
        """ 

`GetY`(*self*)[¶](#wx.stc.StyledTextEvent.GetY "Permalink to this definition")
Returns the Y coordinate of the mouse for this event.


This method is valid for the following event types:


* `wxEVT_STC_DWELLSTART`
* `wxEVT_STC_DWELLEND`
* `wxEVT_STC_START_DRAG`
* `wxEVT_STC_DRAG_OVER`
* `wxEVT_STC_DO_DROP`



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetAnnotationLinesAdded(self, val: int) -> None:
        """ 

`SetAnnotationLinesAdded`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetAnnotationLinesAdded "Permalink to this definition")
Sets the annotation lines added value for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragFlags(self, flags: int) -> None:
        """ 

`SetDragFlags`(*self*, *flags*)[¶](#wx.stc.StyledTextEvent.SetDragFlags "Permalink to this definition")
Sets the drag flags for this event.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragResult(self, val: DragResult) -> None:
        """ 

`SetDragResult`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetDragResult "Permalink to this definition")
Sets the drag result for this event.



Parameters
**val** ([*DragResult*](wx.DragResult.enumeration.html "DragResult")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetDragText(self, val: str) -> None:
        """ 

`SetDragText`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetDragText "Permalink to this definition")
Sets the drag text for this event.



Parameters
**val** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetFoldLevelNow(self, val: int) -> None:
        """ 

`SetFoldLevelNow`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetFoldLevelNow "Permalink to this definition")
Sets the current fold level for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetFoldLevelPrev(self, val: int) -> None:
        """ 

`SetFoldLevelPrev`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetFoldLevelPrev "Permalink to this definition")
Sets the previous fold level for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetKey(self, k: int) -> None:
        """ 

`SetKey`(*self*, *k*)[¶](#wx.stc.StyledTextEvent.SetKey "Permalink to this definition")
Sets the key code for this event.



Parameters
**k** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLParam(self, val: int) -> None:
        """ 

`SetLParam`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetLParam "Permalink to this definition")
Sets value of the LParam field for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLength(self, len: int) -> None:
        """ 

`SetLength`(*self*, *len*)[¶](#wx.stc.StyledTextEvent.SetLength "Permalink to this definition")
Sets the length value for this event.



Parameters
**len** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLine(self, val: int) -> None:
        """ 

`SetLine`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetLine "Permalink to this definition")
Sets line number for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetLinesAdded(self, num: int) -> None:
        """ 

`SetLinesAdded`(*self*, *num*)[¶](#wx.stc.StyledTextEvent.SetLinesAdded "Permalink to this definition")
Sets the number of lines added for this event.



Parameters
**num** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetListCompletionMethod(self, val: int) -> None:
        """ 

`SetListCompletionMethod`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetListCompletionMethod "Permalink to this definition")
Sets the list completion method for this event.



Parameters
**val** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetListType(self, val: int) -> None:
        """ 

`SetListType`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetListType "Permalink to this definition")
Sets the list type for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetMargin(self, val: int) -> None:
        """ 

`SetMargin`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetMargin "Permalink to this definition")
Sets margin number for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetMessage(self, val: int) -> None:
        """ 

`SetMessage`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetMessage "Permalink to this definition")
Sets message number for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetModificationType(self, t: int) -> None:
        """ 

`SetModificationType`(*self*, *t*)[¶](#wx.stc.StyledTextEvent.SetModificationType "Permalink to this definition")
Sets the modification type for this event.



Parameters
**t** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetModifiers(self, m: int) -> None:
        """ 

`SetModifiers`(*self*, *m*)[¶](#wx.stc.StyledTextEvent.SetModifiers "Permalink to this definition")
Sets the value of the modifiers field for this event.



Parameters
**m** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetPosition(self, pos: int) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.stc.StyledTextEvent.SetPosition "Permalink to this definition")
Sets file position for this event.



Parameters
**pos** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetText(self, t: str) -> None:
        """ 

`SetText`(*self*, *t*)[¶](#wx.stc.StyledTextEvent.SetText "Permalink to this definition")
Sets the text for this event.



Parameters
**t** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetToken(self, val: int) -> None:
        """ 

`SetToken`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetToken "Permalink to this definition")
Sets the token for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetUpdated(self, val: int) -> None:
        """ 

`SetUpdated`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetUpdated "Permalink to this definition")
Sets the value of the updated field for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetWParam(self, val: int) -> None:
        """ 

`SetWParam`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetWParam "Permalink to this definition")
Sets the value of the WParam field for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetX(self, val: int) -> None:
        """ 

`SetX`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetX "Permalink to this definition")
Sets the X value for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    def SetY(self, val: int) -> None:
        """ 

`SetY`(*self*, *val*)[¶](#wx.stc.StyledTextEvent.SetY "Permalink to this definition")
Sets the Y value for this event.



Parameters
**val** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextEvent.html
        """

    Alt: bool  # `Alt`[¶](#wx.stc.StyledTextEvent.Alt "Permalink to this definition")See [`GetAlt`](#wx.stc.StyledTextEvent.GetAlt "wx.stc.StyledTextEvent.GetAlt")
    AnnotationsLinesAdded: int  # `AnnotationsLinesAdded`[¶](#wx.stc.StyledTextEvent.AnnotationsLinesAdded "Permalink to this definition")See [`GetAnnotationsLinesAdded`](#wx.stc.StyledTextEvent.GetAnnotationsLinesAdded "wx.stc.StyledTextEvent.GetAnnotationsLinesAdded")
    Control: bool  # `Control`[¶](#wx.stc.StyledTextEvent.Control "Permalink to this definition")See [`GetControl`](#wx.stc.StyledTextEvent.GetControl "wx.stc.StyledTextEvent.GetControl")
    DragFlags: int  # `DragFlags`[¶](#wx.stc.StyledTextEvent.DragFlags "Permalink to this definition")See [`GetDragFlags`](#wx.stc.StyledTextEvent.GetDragFlags "wx.stc.StyledTextEvent.GetDragFlags") and [`SetDragFlags`](#wx.stc.StyledTextEvent.SetDragFlags "wx.stc.StyledTextEvent.SetDragFlags")
    DragResult: '_DragResult'  # `DragResult`[¶](#wx.stc.StyledTextEvent.DragResult "Permalink to this definition")See [`GetDragResult`](#wx.stc.StyledTextEvent.GetDragResult "wx.stc.StyledTextEvent.GetDragResult") and [`SetDragResult`](#wx.stc.StyledTextEvent.SetDragResult "wx.stc.StyledTextEvent.SetDragResult")
    DragText: str  # `DragText`[¶](#wx.stc.StyledTextEvent.DragText "Permalink to this definition")See [`GetDragText`](#wx.stc.StyledTextEvent.GetDragText "wx.stc.StyledTextEvent.GetDragText") and [`SetDragText`](#wx.stc.StyledTextEvent.SetDragText "wx.stc.StyledTextEvent.SetDragText")
    FoldLevelNow: int  # `FoldLevelNow`[¶](#wx.stc.StyledTextEvent.FoldLevelNow "Permalink to this definition")See [`GetFoldLevelNow`](#wx.stc.StyledTextEvent.GetFoldLevelNow "wx.stc.StyledTextEvent.GetFoldLevelNow") and [`SetFoldLevelNow`](#wx.stc.StyledTextEvent.SetFoldLevelNow "wx.stc.StyledTextEvent.SetFoldLevelNow")
    FoldLevelPrev: int  # `FoldLevelPrev`[¶](#wx.stc.StyledTextEvent.FoldLevelPrev "Permalink to this definition")See [`GetFoldLevelPrev`](#wx.stc.StyledTextEvent.GetFoldLevelPrev "wx.stc.StyledTextEvent.GetFoldLevelPrev") and [`SetFoldLevelPrev`](#wx.stc.StyledTextEvent.SetFoldLevelPrev "wx.stc.StyledTextEvent.SetFoldLevelPrev")
    Key: int  # `Key`[¶](#wx.stc.StyledTextEvent.Key "Permalink to this definition")See [`GetKey`](#wx.stc.StyledTextEvent.GetKey "wx.stc.StyledTextEvent.GetKey") and [`SetKey`](#wx.stc.StyledTextEvent.SetKey "wx.stc.StyledTextEvent.SetKey")
    LParam: int  # `LParam`[¶](#wx.stc.StyledTextEvent.LParam "Permalink to this definition")See [`GetLParam`](#wx.stc.StyledTextEvent.GetLParam "wx.stc.StyledTextEvent.GetLParam") and [`SetLParam`](#wx.stc.StyledTextEvent.SetLParam "wx.stc.StyledTextEvent.SetLParam")
    Length: int  # `Length`[¶](#wx.stc.StyledTextEvent.Length "Permalink to this definition")See [`GetLength`](#wx.stc.StyledTextEvent.GetLength "wx.stc.StyledTextEvent.GetLength") and [`SetLength`](#wx.stc.StyledTextEvent.SetLength "wx.stc.StyledTextEvent.SetLength")
    Line: int  # `Line`[¶](#wx.stc.StyledTextEvent.Line "Permalink to this definition")See [`GetLine`](#wx.stc.StyledTextEvent.GetLine "wx.stc.StyledTextEvent.GetLine") and [`SetLine`](#wx.stc.StyledTextEvent.SetLine "wx.stc.StyledTextEvent.SetLine")
    LinesAdded: int  # `LinesAdded`[¶](#wx.stc.StyledTextEvent.LinesAdded "Permalink to this definition")See [`GetLinesAdded`](#wx.stc.StyledTextEvent.GetLinesAdded "wx.stc.StyledTextEvent.GetLinesAdded") and [`SetLinesAdded`](#wx.stc.StyledTextEvent.SetLinesAdded "wx.stc.StyledTextEvent.SetLinesAdded")
    ListCompletionMethod: int  # `ListCompletionMethod`[¶](#wx.stc.StyledTextEvent.ListCompletionMethod "Permalink to this definition")See [`GetListCompletionMethod`](#wx.stc.StyledTextEvent.GetListCompletionMethod "wx.stc.StyledTextEvent.GetListCompletionMethod") and [`SetListCompletionMethod`](#wx.stc.StyledTextEvent.SetListCompletionMethod "wx.stc.StyledTextEvent.SetListCompletionMethod")
    ListType: int  # `ListType`[¶](#wx.stc.StyledTextEvent.ListType "Permalink to this definition")See [`GetListType`](#wx.stc.StyledTextEvent.GetListType "wx.stc.StyledTextEvent.GetListType") and [`SetListType`](#wx.stc.StyledTextEvent.SetListType "wx.stc.StyledTextEvent.SetListType")
    Margin: int  # `Margin`[¶](#wx.stc.StyledTextEvent.Margin "Permalink to this definition")See [`GetMargin`](#wx.stc.StyledTextEvent.GetMargin "wx.stc.StyledTextEvent.GetMargin") and [`SetMargin`](#wx.stc.StyledTextEvent.SetMargin "wx.stc.StyledTextEvent.SetMargin")
    Message: int  # `Message`[¶](#wx.stc.StyledTextEvent.Message "Permalink to this definition")See [`GetMessage`](#wx.stc.StyledTextEvent.GetMessage "wx.stc.StyledTextEvent.GetMessage") and [`SetMessage`](#wx.stc.StyledTextEvent.SetMessage "wx.stc.StyledTextEvent.SetMessage")
    ModificationType: int  # `ModificationType`[¶](#wx.stc.StyledTextEvent.ModificationType "Permalink to this definition")See [`GetModificationType`](#wx.stc.StyledTextEvent.GetModificationType "wx.stc.StyledTextEvent.GetModificationType") and [`SetModificationType`](#wx.stc.StyledTextEvent.SetModificationType "wx.stc.StyledTextEvent.SetModificationType")
    Modifiers: int  # `Modifiers`[¶](#wx.stc.StyledTextEvent.Modifiers "Permalink to this definition")See [`GetModifiers`](#wx.stc.StyledTextEvent.GetModifiers "wx.stc.StyledTextEvent.GetModifiers") and [`SetModifiers`](#wx.stc.StyledTextEvent.SetModifiers "wx.stc.StyledTextEvent.SetModifiers")
    Position: int  # `Position`[¶](#wx.stc.StyledTextEvent.Position "Permalink to this definition")See [`GetPosition`](#wx.stc.StyledTextEvent.GetPosition "wx.stc.StyledTextEvent.GetPosition") and [`SetPosition`](#wx.stc.StyledTextEvent.SetPosition "wx.stc.StyledTextEvent.SetPosition")
    Shift: bool  # `Shift`[¶](#wx.stc.StyledTextEvent.Shift "Permalink to this definition")See [`GetShift`](#wx.stc.StyledTextEvent.GetShift "wx.stc.StyledTextEvent.GetShift")
    Text: str  # `Text`[¶](#wx.stc.StyledTextEvent.Text "Permalink to this definition")See [`GetText`](#wx.stc.StyledTextEvent.GetText "wx.stc.StyledTextEvent.GetText") and [`SetText`](#wx.stc.StyledTextEvent.SetText "wx.stc.StyledTextEvent.SetText")
    Token: int  # `Token`[¶](#wx.stc.StyledTextEvent.Token "Permalink to this definition")See [`GetToken`](#wx.stc.StyledTextEvent.GetToken "wx.stc.StyledTextEvent.GetToken") and [`SetToken`](#wx.stc.StyledTextEvent.SetToken "wx.stc.StyledTextEvent.SetToken")
    Updated: int  # `Updated`[¶](#wx.stc.StyledTextEvent.Updated "Permalink to this definition")See [`GetUpdated`](#wx.stc.StyledTextEvent.GetUpdated "wx.stc.StyledTextEvent.GetUpdated") and [`SetUpdated`](#wx.stc.StyledTextEvent.SetUpdated "wx.stc.StyledTextEvent.SetUpdated")
    WParam: int  # `WParam`[¶](#wx.stc.StyledTextEvent.WParam "Permalink to this definition")See [`GetWParam`](#wx.stc.StyledTextEvent.GetWParam "wx.stc.StyledTextEvent.GetWParam") and [`SetWParam`](#wx.stc.StyledTextEvent.SetWParam "wx.stc.StyledTextEvent.SetWParam")
    X: int  # `X`[¶](#wx.stc.StyledTextEvent.X "Permalink to this definition")See [`GetX`](#wx.stc.StyledTextEvent.GetX "wx.stc.StyledTextEvent.GetX") and [`SetX`](#wx.stc.StyledTextEvent.SetX "wx.stc.StyledTextEvent.SetX")
    Y: int  # `Y`[¶](#wx.stc.StyledTextEvent.Y "Permalink to this definition")See [`GetY`](#wx.stc.StyledTextEvent.GetY "wx.stc.StyledTextEvent.GetY") and [`SetY`](#wx.stc.StyledTextEvent.SetY "wx.stc.StyledTextEvent.SetY")



EVT_STC_AUTOCOMP_CANCELLED: int  # Process a  wxEVT_STC_AUTOCOMP_CANCELLED   event.

EVT_STC_AUTOCOMP_CHAR_DELETED: int  # Process a  wxEVT_STC_AUTOCOMP_CHAR_DELETED   event.

EVT_STC_AUTOCOMP_COMPLETED: int  # Process a  wxEVT_STC_AUTOCOMP_COMPLETED   event.

EVT_STC_AUTOCOMP_SELECTION: int  # Process a  wxEVT_STC_AUTOCOMP_SELECTION   event.

EVT_STC_AUTOCOMP_SELECTION_CHANGE: int  # Process a  wxEVT_STC_AUTOCOMP_SELECTION_CHANGE   event.

EVT_STC_CALLTIP_CLICK: int  # Process a  wxEVT_STC_CALLTIP_CLICK   event.

EVT_STC_CHANGE: int  # Process a  wxEVT_STC_CHANGE   event.

EVT_STC_CHARADDED: int  # Process a  wxEVT_STC_CHARADDED   event.

EVT_STC_CLIPBOARD_COPY: int  # Process a  wxEVT_STC_CLIPBOARD_COPY   event.

EVT_STC_CLIPBOARD_PASTE: int  # Process a  wxEVT_STC_CLIPBOARD_PASTE   event.

EVT_STC_DO_DROP: int  # Process a  wxEVT_STC_DO_DROP   event.

EVT_STC_DOUBLECLICK: int  # Process a  wxEVT_STC_DOUBLECLICK   event.

EVT_STC_DRAG_OVER: int  # Process a  wxEVT_STC_DRAG_OVER   event.

EVT_STC_DWELLEND: int  # Process a  wxEVT_STC_DWELLEND   event.

EVT_STC_DWELLSTART: int  # Process a  wxEVT_STC_DWELLSTART   event.

EVT_STC_HOTSPOT_CLICK: int  # Process a  wxEVT_STC_HOTSPOT_CLICK   event.

EVT_STC_HOTSPOT_DCLICK: int  # Process a  wxEVT_STC_HOTSPOT_DCLICK   event.

EVT_STC_HOTSPOT_RELEASE_CLICK: int  # Process a  wxEVT_STC_HOTSPOT_RELEASE_CLICK   event.

EVT_STC_INDICATOR_CLICK: int  # Process a  wxEVT_STC_INDICATOR_CLICK   event.

EVT_STC_INDICATOR_RELEASE: int  # Process a  wxEVT_STC_INDICATOR_RELEASE   event.

EVT_STC_MACRORECORD: int  # Process a  wxEVT_STC_MACRORECORD   event.

EVT_STC_MARGIN_RIGHT_CLICK: int  # Process a  wxEVT_STC_MARGIN_RIGHT_CLICK   event.

EVT_STC_MARGINCLICK: int  # Process a  wxEVT_STC_MARGINCLICK   event.

EVT_STC_MODIFIED: int  # Process a  wxEVT_STC_MODIFIED   event.

EVT_STC_NEEDSHOWN: int  # Process a  wxEVT_STC_NEEDSHOWN   event.

EVT_STC_PAINTED: int  # Process a  wxEVT_STC_PAINTED   event.

EVT_STC_ROMODIFYATTEMPT: int  # Process a  wxEVT_STC_ROMODIFYATTEMPT   event.

EVT_STC_SAVEPOINTLEFT: int  # Process a  wxEVT_STC_SAVEPOINTLEFT   event.

EVT_STC_SAVEPOINTREACHED: int  # Process a  wxEVT_STC_SAVEPOINTREACHED   event.

EVT_STC_START_DRAG: int  # Process a  wxEVT_STC_START_DRAG   event.

EVT_STC_STYLENEEDED: int  # Process a  wxEVT_STC_STYLENEEDED   event.

EVT_STC_UPDATEUI: int  # Process a  wxEVT_STC_UPDATEUI   event.

EVT_STC_USERLISTSELECTION: int  # Process a  wxEVT_STC_USERLISTSELECTION   event.

EVT_STC_ZOOM: int  # Process a  wxEVT_STC_ZOOM   event. ^^

class StyledTextCtrl(Control,TextEntry):
    """ **Possible constructors**:



```
StyledTextCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
               style=0, name=STCNameStr)

StyledTextCtrl()

```


A wxWidgets implementation of the Scintilla source code editing
component.


  


        Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.stc.StyledTextCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=STCNameStr)*


Ctor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddRefDocument(self, docPointer: Any) -> None:
        """ 

`AddRefDocument`(*self*, *docPointer*)[¶](#wx.stc.StyledTextCtrl.AddRefDocument "Permalink to this definition")
Extend life of document.



Parameters
**docPointer** – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddSelection(self, caret, anchor) -> int:
        """ 

`AddSelection`(*self*, *caret*, *anchor*)[¶](#wx.stc.StyledTextCtrl.AddSelection "Permalink to this definition")
Add a selection.



Parameters
* **caret** (*int*) –
* **anchor** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddStyledText(self, data: MemoryBuffer) -> None:
        """ 

`AddStyledText`(*self*, *data*)[¶](#wx.stc.StyledTextCtrl.AddStyledText "Permalink to this definition")
Add array of cells to document.



Parameters
**data** (*MemoryBuffer*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddTabStop(self, line, x) -> None:
        """ 

`AddTabStop`(*self*, *line*, *x*)[¶](#wx.stc.StyledTextCtrl.AddTabStop "Permalink to this definition")
Add an explicit tab stop for a line.



Parameters
* **line** (*int*) –
* **x** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddText(self, text: str) -> None:
        """ 

`AddText`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.AddText "Permalink to this definition")
Add text to the document at current position.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddTextRaw(self, text, length=-1) -> None:
        """ 

`AddTextRaw`(*self*, *text*, *length=-1*)[¶](#wx.stc.StyledTextCtrl.AddTextRaw "Permalink to this definition")
Add text to the document at current position.



Parameters
* **text** (*int*) –
* **length** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AddUndoAction(self, token, flags) -> None:
        """ 

`AddUndoAction`(*self*, *token*, *flags*)[¶](#wx.stc.StyledTextCtrl.AddUndoAction "Permalink to this definition")
Add a container action to the undo stack.


The flags argument can be either 0 or `wx.stc.STC_UNDO_MAY_COALESCE`.



Parameters
* **token** (*int*) –
* **flags** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Allocate(self, bytes: int) -> None:
        """ 

`Allocate`(*self*, *bytes*)[¶](#wx.stc.StyledTextCtrl.Allocate "Permalink to this definition")
Enlarge the document to a particular size of text bytes.



Parameters
**bytes** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AllocateExtendedStyles(self, numberStyles: int) -> int:
        """ 

`AllocateExtendedStyles`(*self*, *numberStyles*)[¶](#wx.stc.StyledTextCtrl.AllocateExtendedStyles "Permalink to this definition")
Allocate some extended (>255) style numbers and return the start of the range.



Parameters
**numberStyles** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AllocateSubStyles(self, styleBase, numberStyles) -> int:
        """ 

`AllocateSubStyles`(*self*, *styleBase*, *numberStyles*)[¶](#wx.stc.StyledTextCtrl.AllocateSubStyles "Permalink to this definition")
Allocate a set of sub styles for a particular base style, returning start of range.



Parameters
* **styleBase** (*int*) –
* **numberStyles** (*int*) –



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationClearAll(self) -> None:
        """ 

`AnnotationClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.AnnotationClearAll "Permalink to this definition")
Clear the annotations from all lines.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationClearLine(self, line: int) -> None:
        """ 

`AnnotationClearLine`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.AnnotationClearLine "Permalink to this definition")
Clear annotations from the given line.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetLines(self, line: int) -> int:
        """ 

`AnnotationGetLines`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetLines "Permalink to this definition")
Get the number of annotation lines for a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyle(self, line: int) -> int:
        """ 

`AnnotationGetStyle`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetStyle "Permalink to this definition")
Get the style number for the annotations for a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyleOffset(self) -> int:
        """ 

`AnnotationGetStyleOffset`(*self*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetStyleOffset "Permalink to this definition")
Get the start of the range of style numbers used for annotations.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetStyles(self, line: int) -> str:
        """ 

`AnnotationGetStyles`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetStyles "Permalink to this definition")
Get the annotation styles for a line.



Parameters
**line** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetText(self, line: int) -> str:
        """ 

`AnnotationGetText`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetText "Permalink to this definition")
Get the annotation text for a line.



Parameters
**line** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationGetVisible(self) -> int:
        """ 

`AnnotationGetVisible`(*self*)[¶](#wx.stc.StyledTextCtrl.AnnotationGetVisible "Permalink to this definition")
Get the visibility for the annotations for a view.


The return value will be one of the [``](#id1)STC\_ANNOTATION\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyle(self, line, style) -> None:
        """ 

`AnnotationSetStyle`(*self*, *line*, *style*)[¶](#wx.stc.StyledTextCtrl.AnnotationSetStyle "Permalink to this definition")
Set the style number for the annotations for a line.



Parameters
* **line** (*int*) –
* **style** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyleOffset(self, style: int) -> None:
        """ 

`AnnotationSetStyleOffset`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.AnnotationSetStyleOffset "Permalink to this definition")
Get the start of the range of style numbers used for annotations.



Parameters
**style** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetStyles(self, line, styles) -> None:
        """ 

`AnnotationSetStyles`(*self*, *line*, *styles*)[¶](#wx.stc.StyledTextCtrl.AnnotationSetStyles "Permalink to this definition")
Set the annotation styles for a line.



Parameters
* **line** (*int*) –
* **styles** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetText(self, line, text) -> None:
        """ 

`AnnotationSetText`(*self*, *line*, *text*)[¶](#wx.stc.StyledTextCtrl.AnnotationSetText "Permalink to this definition")
Set the annotation text for a line.



Parameters
* **line** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AnnotationSetVisible(self, visible: int) -> None:
        """ 

`AnnotationSetVisible`(*self*, *visible*)[¶](#wx.stc.StyledTextCtrl.AnnotationSetVisible "Permalink to this definition")
Set the visibility for the annotations for a view.


The input should be one of the [``](#id3)STC\_ANNOTATION\_\* `` constants.



Parameters
**visible** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AppendText(self, text: str) -> None:
        """ 

`AppendText`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.AppendText "Permalink to this definition")
Append a string to the end of the document without changing the selection.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AppendTextRaw(self, text, length=-1) -> None:
        """ 

`AppendTextRaw`(*self*, *text*, *length=-1*)[¶](#wx.stc.StyledTextCtrl.AppendTextRaw "Permalink to this definition")
Append a string to the end of the document without changing the selection.



Parameters
* **text** (*int*) –
* **length** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompActive(self) -> bool:
        """ 

`AutoCompActive`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompActive "Permalink to this definition")
Is there an auto-completion list visible?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompCancel(self) -> None:
        """ 

`AutoCompCancel`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompCancel "Permalink to this definition")
Remove the auto-completion list from the screen.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompComplete(self) -> None:
        """ 

`AutoCompComplete`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompComplete "Permalink to this definition")
User has selected an item so remove the list and insert the selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetAutoHide(self) -> bool:
        """ 

`AutoCompGetAutoHide`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetAutoHide "Permalink to this definition")
Retrieve whether or not autocompletion is hidden automatically when nothing matches.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCancelAtStart(self) -> bool:
        """ 

`AutoCompGetCancelAtStart`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetCancelAtStart "Permalink to this definition")
Retrieve whether auto-completion cancelled by backspacing before start.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCaseInsensitiveBehaviour(self) -> int:
        """ 

`AutoCompGetCaseInsensitiveBehaviour`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetCaseInsensitiveBehaviour "Permalink to this definition")
Get auto-completion case insensitive behaviour.


The return value will be one of the [``](#id5)STC\_CASEINSENSITIVEBEHAVIOUR\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetChooseSingle(self) -> bool:
        """ 

`AutoCompGetChooseSingle`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetChooseSingle "Permalink to this definition")
Retrieve whether a single item auto-completion list automatically choose the item.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCurrent(self) -> int:
        """ 

`AutoCompGetCurrent`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetCurrent "Permalink to this definition")
Get currently selected item position in the auto-completion list.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetCurrentText(self) -> str:
        """ 

`AutoCompGetCurrentText`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetCurrentText "Permalink to this definition")
Get currently selected item text in the auto-completion list.



Return type
`string`





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetDropRestOfWord(self) -> bool:
        """ 

`AutoCompGetDropRestOfWord`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetDropRestOfWord "Permalink to this definition")
Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetIgnoreCase(self) -> bool:
        """ 

`AutoCompGetIgnoreCase`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetIgnoreCase "Permalink to this definition")
Retrieve state of ignore case flag.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMaxHeight(self) -> int:
        """ 

`AutoCompGetMaxHeight`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetMaxHeight "Permalink to this definition")
Set the maximum height, in rows, of auto-completion and user lists.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMaxWidth(self) -> int:
        """ 

`AutoCompGetMaxWidth`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetMaxWidth "Permalink to this definition")
Get the maximum width, in characters, of auto-completion and user lists.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetMulti(self) -> int:
        """ 

`AutoCompGetMulti`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetMulti "Permalink to this definition")
Retrieve the effect of autocompleting when there are multiple selections.


The return value will be one of the [``](#id7)STC\_MULTIAUTOC\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetOrder(self) -> int:
        """ 

`AutoCompGetOrder`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetOrder "Permalink to this definition")
Get the way autocompletion lists are ordered.


The return value will be one of the [``](#id9)STC\_ORDER\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetSeparator(self) -> int:
        """ 

`AutoCompGetSeparator`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetSeparator "Permalink to this definition")
Retrieve the auto-completion list separator character.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompGetTypeSeparator(self) -> int:
        """ 

`AutoCompGetTypeSeparator`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompGetTypeSeparator "Permalink to this definition")
Retrieve the auto-completion list type-separator character.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompPosStart(self) -> int:
        """ 

`AutoCompPosStart`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompPosStart "Permalink to this definition")
Retrieve the position of the caret when the auto-completion list was displayed.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSelect(self, select: str) -> None:
        """ 

`AutoCompSelect`(*self*, *select*)[¶](#wx.stc.StyledTextCtrl.AutoCompSelect "Permalink to this definition")
Select the item in the auto-completion list that starts with a string.



Parameters
**select** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetAutoHide(self, autoHide: bool) -> None:
        """ 

`AutoCompSetAutoHide`(*self*, *autoHide*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetAutoHide "Permalink to this definition")
Set whether or not autocompletion is hidden automatically when nothing matches.



Parameters
**autoHide** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetCancelAtStart(self, cancel: bool) -> None:
        """ 

`AutoCompSetCancelAtStart`(*self*, *cancel*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetCancelAtStart "Permalink to this definition")
Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created.



Parameters
**cancel** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetCaseInsensitiveBehaviour(self, behaviour: int) -> None:
        """ 

`AutoCompSetCaseInsensitiveBehaviour`(*self*, *behaviour*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetCaseInsensitiveBehaviour "Permalink to this definition")
Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference.


The input should be one of the [``](#id11)STC\_CASEINSENSITIVEBEHAVIOUR\_\* `` constants.



Parameters
**behaviour** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetChooseSingle(self, chooseSingle: bool) -> None:
        """ 

`AutoCompSetChooseSingle`(*self*, *chooseSingle*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetChooseSingle "Permalink to this definition")
Should a single item auto-completion list automatically choose the item.



Parameters
**chooseSingle** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetDropRestOfWord(self, dropRestOfWord: bool) -> None:
        """ 

`AutoCompSetDropRestOfWord`(*self*, *dropRestOfWord*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetDropRestOfWord "Permalink to this definition")
Set whether or not autocompletion deletes any word characters after the inserted text upon completion.



Parameters
**dropRestOfWord** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetFillUps(self, characterSet: str) -> None:
        """ 

`AutoCompSetFillUps`(*self*, *characterSet*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetFillUps "Permalink to this definition")
Define a set of characters that when typed will cause the autocompletion to choose the selected item.



Parameters
**characterSet** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetIgnoreCase(self, ignoreCase: bool) -> None:
        """ 

`AutoCompSetIgnoreCase`(*self*, *ignoreCase*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetIgnoreCase "Permalink to this definition")
Set whether case is significant when performing auto-completion searches.



Parameters
**ignoreCase** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMaxHeight(self, rowCount: int) -> None:
        """ 

`AutoCompSetMaxHeight`(*self*, *rowCount*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetMaxHeight "Permalink to this definition")
Set the maximum height, in rows, of auto-completion and user lists.


The default is 5 rows.



Parameters
**rowCount** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMaxWidth(self, characterCount: int) -> None:
        """ 

`AutoCompSetMaxWidth`(*self*, *characterCount*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetMaxWidth "Permalink to this definition")
Set the maximum width, in characters, of auto-completion and user lists.


Set to 0 to autosize to fit longest item, which is the default.



Parameters
**characterCount** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetMulti(self, multi: int) -> None:
        """ 

`AutoCompSetMulti`(*self*, *multi*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetMulti "Permalink to this definition")
Change the effect of autocompleting when there are multiple selections.


The input should be one of the [``](#id13)STC\_MULTIAUTOC\_\* `` constants.



Parameters
**multi** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetOrder(self, order: int) -> None:
        """ 

`AutoCompSetOrder`(*self*, *order*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetOrder "Permalink to this definition")
Set the way autocompletion lists are ordered.


The input should be one of the [``](#id15)STC\_ORDER\_\* `` constants.



Parameters
**order** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetSeparator(self, separatorCharacter: int) -> None:
        """ 

`AutoCompSetSeparator`(*self*, *separatorCharacter*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetSeparator "Permalink to this definition")
Change the separator character in the string setting up an auto-completion list.


Default is space but can be changed if items contain space.



Parameters
**separatorCharacter** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompSetTypeSeparator(self, separatorCharacter: int) -> None:
        """ 

`AutoCompSetTypeSeparator`(*self*, *separatorCharacter*)[¶](#wx.stc.StyledTextCtrl.AutoCompSetTypeSeparator "Permalink to this definition")
Change the type-separator character in the string setting up an auto-completion list.


Default is ‘?’ but can be changed if items contain ‘?’.



Parameters
**separatorCharacter** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompShow(self, lengthEntered, itemList) -> None:
        """ 

`AutoCompShow`(*self*, *lengthEntered*, *itemList*)[¶](#wx.stc.StyledTextCtrl.AutoCompShow "Permalink to this definition")
Display an auto-completion list.


The lengthEntered parameter indicates how many characters before the caret should be used to provide context.



Parameters
* **lengthEntered** (*int*) –
* **itemList** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompStops(self, characterSet: str) -> None:
        """ 

`AutoCompStops`(*self*, *characterSet*)[¶](#wx.stc.StyledTextCtrl.AutoCompStops "Permalink to this definition")
Define a set of character that when typed cancel the auto-completion list.



Parameters
**characterSet** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoComplete(self, *args, **kw) -> bool:
        """ 

`AutoComplete`(*self*, *\*args*, *\*\*kw*)[¶](#wx.stc.StyledTextCtrl.AutoComplete "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AutoComplete** *(self, choices)*


Call this function to enable auto-completion of the text typed in a single-line text control using the given *choices*.



Parameters
**choices** (*list of strings*) – 



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.0.




See also


[`AutoCompleteFileNames`](#wx.stc.StyledTextCtrl.AutoCompleteFileNames "wx.stc.StyledTextCtrl.AutoCompleteFileNames")





---

  



**AutoComplete** *(self, completer)*


Enable auto-completion using the provided completer object.


This method should be used instead of [`AutoComplete`](#wx.stc.StyledTextCtrl.AutoComplete "wx.stc.StyledTextCtrl.AutoComplete") overload taking the array of possible completions if the total number of strings is too big as it allows returning the completions dynamically, depending on the text already entered by user and so is more efficient.


The specified *completer* object will be used to retrieve the list of possible completions for the already entered text and will be deleted by  [wx.TextEntry](wx.TextEntry.html#wx-textentry) itself when it’s not needed any longer.


Notice that you need to include */textcompleter.h* in order to define your class inheriting from  [wx.TextCompleter](wx.TextCompleter.html#wx-textcompleter).



Parameters
**completer** ([*wx.TextCompleter*](wx.TextCompleter.html#wx.TextCompleter "wx.TextCompleter")) – The object to be used for generating completions if not `None`. If it is `None`, auto-completion is disabled. The  [wx.TextEntry](wx.TextEntry.html#wx-textentry) object takes ownership of this pointer and will delete it in any case (i.e. even if this method returns `False`).



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.2.




See also


 [wx.TextCompleter](wx.TextCompleter.html#wx-textcompleter)





---

  





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompleteDirectories(self) -> bool:
        """ 

`AutoCompleteDirectories`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompleteDirectories "Permalink to this definition")
Call this function to enable auto-completion of the text using the file system directories.


Unlike [`AutoCompleteFileNames`](#wx.stc.StyledTextCtrl.AutoCompleteFileNames "wx.stc.StyledTextCtrl.AutoCompleteFileNames") which completes both file names and directories, this function only completes the directory names.


Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.3.




See also


[`AutoComplete`](#wx.stc.StyledTextCtrl.AutoComplete "wx.stc.StyledTextCtrl.AutoComplete")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def AutoCompleteFileNames(self) -> bool:
        """ 

`AutoCompleteFileNames`(*self*)[¶](#wx.stc.StyledTextCtrl.AutoCompleteFileNames "Permalink to this definition")
Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.


Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.0.




See also


[`AutoComplete`](#wx.stc.StyledTextCtrl.AutoComplete "wx.stc.StyledTextCtrl.AutoComplete")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BackTab(self) -> None:
        """ 

`BackTab`(*self*)[¶](#wx.stc.StyledTextCtrl.BackTab "Permalink to this definition")
Dedent the selected lines.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BeginUndoAction(self) -> None:
        """ 

`BeginUndoAction`(*self*)[¶](#wx.stc.StyledTextCtrl.BeginUndoAction "Permalink to this definition")
Start a sequence of actions that is undone and redone as a unit.


May be nested.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceBadLight(self, pos: int) -> None:
        """ 

`BraceBadLight`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.BraceBadLight "Permalink to this definition")
Highlight the character at a position indicating there is no matching brace.



Parameters
**pos** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceBadLightIndicator(self, useSetting, indicator) -> None:
        """ 

`BraceBadLightIndicator`(*self*, *useSetting*, *indicator*)[¶](#wx.stc.StyledTextCtrl.BraceBadLightIndicator "Permalink to this definition")
Use specified indicator to highlight non matching brace instead of changing its style.



Parameters
* **useSetting** (*bool*) –
* **indicator** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceHighlight(self, posA, posB) -> None:
        """ 

`BraceHighlight`(*self*, *posA*, *posB*)[¶](#wx.stc.StyledTextCtrl.BraceHighlight "Permalink to this definition")
Highlight the characters at two positions.



Parameters
* **posA** (*int*) –
* **posB** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceHighlightIndicator(self, useSetting, indicator) -> None:
        """ 

`BraceHighlightIndicator`(*self*, *useSetting*, *indicator*)[¶](#wx.stc.StyledTextCtrl.BraceHighlightIndicator "Permalink to this definition")
Use specified indicator to highlight matching braces instead of changing their style.



Parameters
* **useSetting** (*bool*) –
* **indicator** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def BraceMatch(self, pos, maxReStyle=0) -> int:
        """ 

`BraceMatch`(*self*, *pos*, *maxReStyle=0*)[¶](#wx.stc.StyledTextCtrl.BraceMatch "Permalink to this definition")
Find the position of a matching brace or `wx.stc.STC_INVALID_POSITION` if no match.


The maxReStyle must be 0 for now. It may be defined in a future release.



Parameters
* **pos** (*int*) –
* **maxReStyle** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipActive(self) -> bool:
        """ 

`CallTipActive`(*self*)[¶](#wx.stc.StyledTextCtrl.CallTipActive "Permalink to this definition")
Is there an active call tip?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipCancel(self) -> None:
        """ 

`CallTipCancel`(*self*)[¶](#wx.stc.StyledTextCtrl.CallTipCancel "Permalink to this definition")
Remove the call tip from the screen.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipPosAtStart(self) -> int:
        """ 

`CallTipPosAtStart`(*self*)[¶](#wx.stc.StyledTextCtrl.CallTipPosAtStart "Permalink to this definition")
Retrieve the position where the caret was before displaying the call tip.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetBackground(self, back: Union[int, str, 'Colour']) -> None:
        """ 

`CallTipSetBackground`(*self*, *back*)[¶](#wx.stc.StyledTextCtrl.CallTipSetBackground "Permalink to this definition")
Set the background colour for the call tip.



Parameters
**back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetForeground(self, fore: Union[int, str, 'Colour']) -> None:
        """ 

`CallTipSetForeground`(*self*, *fore*)[¶](#wx.stc.StyledTextCtrl.CallTipSetForeground "Permalink to this definition")
Set the foreground colour for the call tip.



Parameters
**fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetForegroundHighlight(self, fore: Union[int, str, 'Colour']) -> None:
        """ 

`CallTipSetForegroundHighlight`(*self*, *fore*)[¶](#wx.stc.StyledTextCtrl.CallTipSetForegroundHighlight "Permalink to this definition")
Set the foreground colour for the highlighted part of the call tip.



Parameters
**fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetHighlight(self, highlightStart, highlightEnd) -> None:
        """ 

`CallTipSetHighlight`(*self*, *highlightStart*, *highlightEnd*)[¶](#wx.stc.StyledTextCtrl.CallTipSetHighlight "Permalink to this definition")
Highlight a segment of the definition.



Parameters
* **highlightStart** (*int*) –
* **highlightEnd** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetPosAtStart(self, posStart: int) -> None:
        """ 

`CallTipSetPosAtStart`(*self*, *posStart*)[¶](#wx.stc.StyledTextCtrl.CallTipSetPosAtStart "Permalink to this definition")
Set the start position in order to change when backspacing removes the calltip.



Parameters
**posStart** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipSetPosition(self, above: bool) -> None:
        """ 

`CallTipSetPosition`(*self*, *above*)[¶](#wx.stc.StyledTextCtrl.CallTipSetPosition "Permalink to this definition")
Set position of calltip, above or below text.



Parameters
**above** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipShow(self, pos, definition) -> None:
        """ 

`CallTipShow`(*self*, *pos*, *definition*)[¶](#wx.stc.StyledTextCtrl.CallTipShow "Permalink to this definition")
Show a call tip containing a definition near position pos.



Parameters
* **pos** (*int*) –
* **definition** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CallTipUseStyle(self, tabSize: int) -> None:
        """ 

`CallTipUseStyle`(*self*, *tabSize*)[¶](#wx.stc.StyledTextCtrl.CallTipUseStyle "Permalink to this definition")
Enable use of `wx.stc.STC_STYLE_CALLTIP` and set call tip tab size in pixels.



Parameters
**tabSize** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanCopy(self) -> bool:
        """ 

`CanCopy`(*self*)[¶](#wx.stc.StyledTextCtrl.CanCopy "Permalink to this definition")
Returns `True` if the selection can be copied to the clipboard.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanCut(self) -> bool:
        """ 

`CanCut`(*self*)[¶](#wx.stc.StyledTextCtrl.CanCut "Permalink to this definition")
Returns `True` if the selection can be cut to the clipboard.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanPaste(self) -> bool:
        """ 

`CanPaste`(*self*)[¶](#wx.stc.StyledTextCtrl.CanPaste "Permalink to this definition")
Will a paste succeed?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanRedo(self) -> bool:
        """ 

`CanRedo`(*self*)[¶](#wx.stc.StyledTextCtrl.CanRedo "Permalink to this definition")
Are there any redoable actions in the undo history?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CanUndo(self) -> bool:
        """ 

`CanUndo`(*self*)[¶](#wx.stc.StyledTextCtrl.CanUndo "Permalink to this definition")
Are there any undoable actions in the undo history?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Cancel(self) -> None:
        """ 

`Cancel`(*self*)[¶](#wx.stc.StyledTextCtrl.Cancel "Permalink to this definition")
Cancel any modes such as call tip or auto-completion list display.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeInsertion(self, length, text) -> None:
        """ 

`ChangeInsertion`(*self*, *length*, *text*)[¶](#wx.stc.StyledTextCtrl.ChangeInsertion "Permalink to this definition")
Change the text that is being inserted in response to `wx.stc.STC_MOD_INSERTCHECK`.



Parameters
* **length** (*int*) –
* **text** (*string*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeLexerState(self, start, end) -> int:
        """ 

`ChangeLexerState`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.ChangeLexerState "Permalink to this definition")
Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw.



Parameters
* **start** (*int*) –
* **end** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChangeValue(self, value: str) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.stc.StyledTextCtrl.ChangeValue "Permalink to this definition")
Sets the new text control value.


It also marks the control as not-modified which means that IsModified() would return `False` immediately after the call to [`ChangeValue`](#wx.stc.StyledTextCtrl.ChangeValue "wx.stc.StyledTextCtrl.ChangeValue") .


The insertion point is set to the start of the control (i.e. position 0) by this function.


This functions does not generate the `wxEVT_TEXT` event but otherwise is identical to [`SetValue`](#wx.stc.StyledTextCtrl.SetValue "wx.stc.StyledTextCtrl.SetValue") .


See [User Generated Events vs Programmatically Generated Events](events_overview.html#user-generated-events-vs-programmatically-generated-events) for more information.



Parameters
**value** (*string*) – The new value to set. It may contain newline characters if the text control is multi-line.





New in version 2.7.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeft(self) -> None:
        """ 

`CharLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.CharLeft "Permalink to this definition")
Move caret left one character.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeftExtend(self) -> None:
        """ 

`CharLeftExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.CharLeftExtend "Permalink to this definition")
Move caret left one character extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharLeftRectExtend(self) -> None:
        """ 

`CharLeftRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.CharLeftRectExtend "Permalink to this definition")
Move caret left one character, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharPositionFromPoint(self, x, y) -> int:
        """ 

`CharPositionFromPoint`(*self*, *x*, *y*)[¶](#wx.stc.StyledTextCtrl.CharPositionFromPoint "Permalink to this definition")
Find the position of a character from a point within the window.



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharPositionFromPointClose(self, x, y) -> int:
        """ 

`CharPositionFromPointClose`(*self*, *x*, *y*)[¶](#wx.stc.StyledTextCtrl.CharPositionFromPointClose "Permalink to this definition")
Find the position of a character from a point within the window.


Return `wx.stc.STC_INVALID_POSITION` if not close to text.



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRight(self) -> None:
        """ 

`CharRight`(*self*)[¶](#wx.stc.StyledTextCtrl.CharRight "Permalink to this definition")
Move caret right one character.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRightExtend(self) -> None:
        """ 

`CharRightExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.CharRightExtend "Permalink to this definition")
Move caret right one character extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CharRightRectExtend(self) -> None:
        """ 

`CharRightRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.CharRightRectExtend "Permalink to this definition")
Move caret right one character, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ChooseCaretX(self) -> None:
        """ 

`ChooseCaretX`(*self*)[¶](#wx.stc.StyledTextCtrl.ChooseCaretX "Permalink to this definition")
Set the last x chosen value to be the caret x position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.stc.StyledTextCtrl.Clear "Permalink to this definition")
Clear the selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearAll(self) -> None:
        """ 

`ClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.ClearAll "Permalink to this definition")
Delete all text in the document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearDocumentStyle(self) -> None:
        """ 

`ClearDocumentStyle`(*self*)[¶](#wx.stc.StyledTextCtrl.ClearDocumentStyle "Permalink to this definition")
Set all style bytes to 0, remove all folding information.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearRegisteredImages(self) -> None:
        """ 

`ClearRegisteredImages`(*self*)[¶](#wx.stc.StyledTextCtrl.ClearRegisteredImages "Permalink to this definition")
Clear all the registered images.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearRepresentation(self, encodedCharacter: str) -> None:
        """ 

`ClearRepresentation`(*self*, *encodedCharacter*)[¶](#wx.stc.StyledTextCtrl.ClearRepresentation "Permalink to this definition")
Remove a character representation.



Parameters
**encodedCharacter** (*string*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearSelections(self) -> None:
        """ 

`ClearSelections`(*self*)[¶](#wx.stc.StyledTextCtrl.ClearSelections "Permalink to this definition")
Clear selections to a single empty stream selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ClearTabStops(self, line: int) -> None:
        """ 

`ClearTabStops`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.ClearTabStops "Permalink to this definition")
Clear explicit tabstops on a line.



Parameters
**line** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyAssign(self, key, modifiers, cmd) -> None:
        """ 

`CmdKeyAssign`(*self*, *key*, *modifiers*, *cmd*)[¶](#wx.stc.StyledTextCtrl.CmdKeyAssign "Permalink to this definition")
When key+modifier combination keyDefinition is pressed perform sciCommand.


The second argument should be a bit list containing one or more of the [``](#id17)STC\_KEYMOD\_\* `` constants and the third argument should be one of the [``](#id19)STC\_CMD\_\* `` constants.



Parameters
* **key** (*int*) –
* **modifiers** (*int*) –
* **cmd** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyClear(self, key, modifiers) -> None:
        """ 

`CmdKeyClear`(*self*, *key*, *modifiers*)[¶](#wx.stc.StyledTextCtrl.CmdKeyClear "Permalink to this definition")
When key+modifier combination keyDefinition is pressed do nothing.


The second argument should be a bit list containing one or more of the [``](#id21)STC\_KEYMOD\_\* `` constants.



Parameters
* **key** (*int*) –
* **modifiers** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyClearAll(self) -> None:
        """ 

`CmdKeyClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.CmdKeyClearAll "Permalink to this definition")
Drop all key mappings.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CmdKeyExecute(self, cmd: int) -> None:
        """ 

`CmdKeyExecute`(*self*, *cmd*)[¶](#wx.stc.StyledTextCtrl.CmdKeyExecute "Permalink to this definition")
Perform one of the operations defined by the `STC_CMD_` constants.



Parameters
**cmd** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Colourise(self, start, end) -> None:
        """ 

`Colourise`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.Colourise "Permalink to this definition")
Colourise a segment of the document using the current lexing language.



Parameters
* **start** (*int*) –
* **end** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ContractedFoldNext(self, lineStart: int) -> int:
        """ 

`ContractedFoldNext`(*self*, *lineStart*)[¶](#wx.stc.StyledTextCtrl.ContractedFoldNext "Permalink to this definition")
Find the next line at or after lineStart that is a contracted fold header line.


Return -1 when no more lines.



Parameters
**lineStart** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ConvertEOLs(self, eolMode: int) -> None:
        """ 

`ConvertEOLs`(*self*, *eolMode*)[¶](#wx.stc.StyledTextCtrl.ConvertEOLs "Permalink to this definition")
Convert all line endings in the document to one mode.



Parameters
**eolMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Copy(self) -> None:
        """ 

`Copy`(*self*)[¶](#wx.stc.StyledTextCtrl.Copy "Permalink to this definition")
Copy the selection to the clipboard.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyAllowLine(self) -> None:
        """ 

`CopyAllowLine`(*self*)[¶](#wx.stc.StyledTextCtrl.CopyAllowLine "Permalink to this definition")
Copy the selection, if selection empty copy the line with the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyRange(self, start, end) -> None:
        """ 

`CopyRange`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.CopyRange "Permalink to this definition")
Copy a range of text to the clipboard.


Positions are clipped into the document.



Parameters
* **start** (*int*) –
* **end** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CopyText(self, length, text) -> None:
        """ 

`CopyText`(*self*, *length*, *text*)[¶](#wx.stc.StyledTextCtrl.CopyText "Permalink to this definition")
Copy argument text to the clipboard.



Parameters
* **length** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CountCharacters(self, start, end) -> int:
        """ 

`CountCharacters`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.CountCharacters "Permalink to this definition")
Count characters between two positions.



Parameters
* **start** (*int*) –
* **end** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=STCNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *name=STCNameStr*)[¶](#wx.stc.StyledTextCtrl.Create "Permalink to this definition")
Create the UI elements for a `STC` that was created with the default constructor.


(For 2-phase create.)



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CreateDocument(self) -> None:
        """ 

`CreateDocument`(*self*)[¶](#wx.stc.StyledTextCtrl.CreateDocument "Permalink to this definition")
Create a new document object.


Starts with reference count of 1 and not selected into editor.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def CreateLoader(self, bytes: int) -> None:
        """ 

`CreateLoader`(*self*, *bytes*)[¶](#wx.stc.StyledTextCtrl.CreateLoader "Permalink to this definition")
Create an ILoader.



Parameters
**bytes** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.stc.StyledTextCtrl.Cut "Permalink to this definition")
Cut the selection to the clipboard.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelLineLeft(self) -> None:
        """ 

`DelLineLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.DelLineLeft "Permalink to this definition")
Delete back from the current position to the start of the line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelLineRight(self) -> None:
        """ 

`DelLineRight`(*self*)[¶](#wx.stc.StyledTextCtrl.DelLineRight "Permalink to this definition")
Delete forwards from the current position to the end of the line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordLeft(self) -> None:
        """ 

`DelWordLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.DelWordLeft "Permalink to this definition")
Delete the word to the left of the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordRight(self) -> None:
        """ 

`DelWordRight`(*self*)[¶](#wx.stc.StyledTextCtrl.DelWordRight "Permalink to this definition")
Delete the word to the right of the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DelWordRightEnd(self) -> None:
        """ 

`DelWordRightEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.DelWordRightEnd "Permalink to this definition")
Delete the word to the right of the caret, but not the trailing non-word characters.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteBack(self) -> None:
        """ 

`DeleteBack`(*self*)[¶](#wx.stc.StyledTextCtrl.DeleteBack "Permalink to this definition")
Delete the selection or if no selection, the character before the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteBackNotLine(self) -> None:
        """ 

`DeleteBackNotLine`(*self*)[¶](#wx.stc.StyledTextCtrl.DeleteBackNotLine "Permalink to this definition")
Delete the selection or if no selection, the character before the caret.


Will not delete the character before at the start of a line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DeleteRange(self, start, lengthDelete) -> None:
        """ 

`DeleteRange`(*self*, *start*, *lengthDelete*)[¶](#wx.stc.StyledTextCtrl.DeleteRange "Permalink to this definition")
Delete a range of text in the document.



Parameters
* **start** (*int*) –
* **lengthDelete** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DescribeKeyWordSets(self) -> str:
        """ 

`DescribeKeyWordSets`(*self*)[¶](#wx.stc.StyledTextCtrl.DescribeKeyWordSets "Permalink to this definition")
Retrieve a ‘\n’ separated list of descriptions of the keyword sets understood by the current lexer.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DescribeProperty(self, name: str) -> str:
        """ 

`DescribeProperty`(*self*, *name*)[¶](#wx.stc.StyledTextCtrl.DescribeProperty "Permalink to this definition")
Describe a property.



Parameters
**name** (*string*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DiscardEdits(self) -> None:
        """ 

`DiscardEdits`(*self*)[¶](#wx.stc.StyledTextCtrl.DiscardEdits "Permalink to this definition")
Resets the internal modified flag as if the current changes had been saved.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DistanceToSecondaryStyles(self) -> int:
        """ 

`DistanceToSecondaryStyles`(*self*)[¶](#wx.stc.StyledTextCtrl.DistanceToSecondaryStyles "Permalink to this definition")
Where styles are duplicated by a feature such as active/inactive code return the distance between the two types.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragEnter(self, x, y, defaultRes) -> 'DragResult':
        """ 

`DoDragEnter`(*self*, *x*, *y*, *defaultRes*)[¶](#wx.stc.StyledTextCtrl.DoDragEnter "Permalink to this definition")
Allow for simulating a DnD DragEnter.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **defaultRes** ([*DragResult*](wx.DragResult.enumeration.html "DragResult")) –



Return type
 [wx.DragResult](wx.DragResult.enumeration.html#wx-dragresult)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragLeave(self) -> None:
        """ 

`DoDragLeave`(*self*)[¶](#wx.stc.StyledTextCtrl.DoDragLeave "Permalink to this definition")
Allow for simulating a DnD DragLeave.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDragOver(self, x, y, defaultRes) -> 'DragResult':
        """ 

`DoDragOver`(*self*, *x*, *y*, *defaultRes*)[¶](#wx.stc.StyledTextCtrl.DoDragOver "Permalink to this definition")
Allow for simulating a DnD DragOver.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **defaultRes** ([*DragResult*](wx.DragResult.enumeration.html "DragResult")) –



Return type
 [wx.DragResult](wx.DragResult.enumeration.html#wx-dragresult)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DoDropText(self, x, y, data) -> bool:
        """ 

`DoDropText`(*self*, *x*, *y*, *data*)[¶](#wx.stc.StyledTextCtrl.DoDropText "Permalink to this definition")
Allow for simulating a DnD DropText.



Parameters
* **x** (*long*) –
* **y** (*long*) –
* **data** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocLineFromVisible(self, displayLine: int) -> int:
        """ 

`DocLineFromVisible`(*self*, *displayLine*)[¶](#wx.stc.StyledTextCtrl.DocLineFromVisible "Permalink to this definition")
Find the document line of a display line taking hidden lines into account.



Parameters
**displayLine** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentEnd(self) -> None:
        """ 

`DocumentEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.DocumentEnd "Permalink to this definition")
Move caret to last position in document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentEndExtend(self) -> None:
        """ 

`DocumentEndExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.DocumentEndExtend "Permalink to this definition")
Move caret to last position in document extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentStart(self) -> None:
        """ 

`DocumentStart`(*self*)[¶](#wx.stc.StyledTextCtrl.DocumentStart "Permalink to this definition")
Move caret to first position in document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DocumentStartExtend(self) -> None:
        """ 

`DocumentStartExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.DocumentStartExtend "Permalink to this definition")
Move caret to first position in document extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def DropSelectionN(self, selection: int) -> None:
        """ 

`DropSelectionN`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.DropSelectionN "Permalink to this definition")
Drop one selection.



Parameters
**selection** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EditToggleOvertype(self) -> None:
        """ 

`EditToggleOvertype`(*self*)[¶](#wx.stc.StyledTextCtrl.EditToggleOvertype "Permalink to this definition")
Switch from insert to overtype mode or the reverse.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EmptyUndoBuffer(self) -> None:
        """ 

`EmptyUndoBuffer`(*self*)[¶](#wx.stc.StyledTextCtrl.EmptyUndoBuffer "Permalink to this definition")
Delete the undo history.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EndUndoAction(self) -> None:
        """ 

`EndUndoAction`(*self*)[¶](#wx.stc.StyledTextCtrl.EndUndoAction "Permalink to this definition")
End a sequence of actions that is undone and redone as a unit.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureCaretVisible(self) -> None:
        """ 

`EnsureCaretVisible`(*self*)[¶](#wx.stc.StyledTextCtrl.EnsureCaretVisible "Permalink to this definition")
Ensure the caret is visible.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureVisible(self, line: int) -> None:
        """ 

`EnsureVisible`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.EnsureVisible "Permalink to this definition")
Ensure a particular line is visible by expanding any header line hiding it.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def EnsureVisibleEnforcePolicy(self, line: int) -> None:
        """ 

`EnsureVisibleEnforcePolicy`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.EnsureVisibleEnforcePolicy "Permalink to this definition")
Ensure a particular line is visible by expanding any header line hiding it.


Use the currently set visibility policy to determine which range to display.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ExpandChildren(self, line, level) -> None:
        """ 

`ExpandChildren`(*self*, *line*, *level*)[¶](#wx.stc.StyledTextCtrl.ExpandChildren "Permalink to this definition")
Expand a fold header and all children.


Use the level argument instead of the line’s current level.



Parameters
* **line** (*int*) –
* **level** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FindColumn(self, line, column) -> int:
        """ 

`FindColumn`(*self*, *line*, *column*)[¶](#wx.stc.StyledTextCtrl.FindColumn "Permalink to this definition")
Find the position of a column on a line taking into account tabs and multi-byte characters.


If beyond end of line, return line end position.



Parameters
* **line** (*int*) –
* **column** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FindText(self, minPos, maxPos, text, flags=0) -> tuple:
        """ 

`FindText`(*self*, *minPos*, *maxPos*, *text*, *flags=0*)[¶](#wx.stc.StyledTextCtrl.FindText "Permalink to this definition")
Find some text in the document.



Parameters
* **minPos** (*int*) – The position (starting from zero) in the document at which to begin the search
* **maxPos** (*int*) – The last position (starting from zero) in the document to which the search will be restricted.
* **text** (*string*) – The text to search for.
* **flags** (*int*) – (Optional) The search flags. This should be a bit list containing one or more of the [``](#id23)STC\_FIND\_\* `` constants.



Return type
*tuple*



Returns
( *int*, *findEnd* )





Note


A backwards search can be performed by setting minPos to be greater than maxPos.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldAll(self, action: int) -> None:
        """ 

`FoldAll`(*self*, *action*)[¶](#wx.stc.StyledTextCtrl.FoldAll "Permalink to this definition")
Expand or contract all fold headers.


The input should be one of the [``](#id25)STC\_FOLDACTION\_\* `` constants.



Parameters
**action** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldChildren(self, line, action) -> None:
        """ 

`FoldChildren`(*self*, *line*, *action*)[¶](#wx.stc.StyledTextCtrl.FoldChildren "Permalink to this definition")
Expand or contract a fold header and its children.


The second argument should be one of the [``](#id27)STC\_FOLDACTION\_\* `` constants.



Parameters
* **line** (*int*) –
* **action** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldDisplayTextSetStyle(self, style: int) -> None:
        """ 

`FoldDisplayTextSetStyle`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.FoldDisplayTextSetStyle "Permalink to this definition")
Set the style of fold display text.


The input should be one of the [``](#id29)STC\_FOLDDISPLAYTEXT\_\* `` constants.



Parameters
**style** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FoldLine(self, line, action) -> None:
        """ 

`FoldLine`(*self*, *line*, *action*)[¶](#wx.stc.StyledTextCtrl.FoldLine "Permalink to this definition")
Expand or contract a fold header.


The second argument should be one of the [``](#id31)STC\_FOLDACTION\_\* `` constants.



Parameters
* **line** (*int*) –
* **action** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ForceUpper(self) -> None:
        """ 

`ForceUpper`(*self*)[¶](#wx.stc.StyledTextCtrl.ForceUpper "Permalink to this definition")
Convert all text entered into the control to upper case.


Call this method to ensure that all text entered into the control is converted on the fly to upper case. If the control is not empty, its existing contents is also converted to upper case.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FormFeed(self) -> None:
        """ 

`FormFeed`(*self*)[¶](#wx.stc.StyledTextCtrl.FormFeed "Permalink to this definition")
Insert a Form Feed character.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FormatRange(self, doDraw, startPos, endPos, draw, target, renderRect, pageRect) -> int:
        """ 

`FormatRange`(*self*, *doDraw*, *startPos*, *endPos*, *draw*, *target*, *renderRect*, *pageRect*)[¶](#wx.stc.StyledTextCtrl.FormatRange "Permalink to this definition")
On Windows, will draw the document into a display context such as a printer.



Parameters
* **doDraw** (*bool*) –
* **startPos** (*int*) –
* **endPos** (*int*) –
* **draw** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **target** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **renderRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pageRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def FreeSubStyles(self) -> None:
        """ 

`FreeSubStyles`(*self*)[¶](#wx.stc.StyledTextCtrl.FreeSubStyles "Permalink to this definition")
Free allocated sub styles.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretForeground(self) -> 'Colour':
        """ 

`GetAdditionalCaretForeground`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAdditionalCaretForeground "Permalink to this definition")
Get the foreground colour of additional carets.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretsBlink(self) -> bool:
        """ 

`GetAdditionalCaretsBlink`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAdditionalCaretsBlink "Permalink to this definition")
Whether additional carets will blink.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalCaretsVisible(self) -> bool:
        """ 

`GetAdditionalCaretsVisible`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAdditionalCaretsVisible "Permalink to this definition")
Whether additional carets are visible.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalSelAlpha(self) -> int:
        """ 

`GetAdditionalSelAlpha`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAdditionalSelAlpha "Permalink to this definition")
Get the alpha of the selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAdditionalSelectionTyping(self) -> bool:
        """ 

`GetAdditionalSelectionTyping`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAdditionalSelectionTyping "Permalink to this definition")
Whether typing can be performed into multiple selections.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAllLinesVisible(self) -> bool:
        """ 

`GetAllLinesVisible`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAllLinesVisible "Permalink to this definition")
Are all lines visible?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAnchor(self) -> int:
        """ 

`GetAnchor`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAnchor "Permalink to this definition")
Returns the position of the opposite end of the selection to the caret.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetAutomaticFold(self) -> int:
        """ 

`GetAutomaticFold`(*self*)[¶](#wx.stc.StyledTextCtrl.GetAutomaticFold "Permalink to this definition")
Get automatic folding behaviours.


The return value will be a bit list containing one or more of the [``](#id33)STC\_AUTOMATICFOLD\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetBackSpaceUnIndents(self) -> bool:
        """ 

`GetBackSpaceUnIndents`(*self*)[¶](#wx.stc.StyledTextCtrl.GetBackSpaceUnIndents "Permalink to this definition")
Does a backspace pressed when caret is within indentation unindent?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetBufferedDraw(self) -> bool:
        """ 

`GetBufferedDraw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetBufferedDraw "Permalink to this definition")
Is drawing done first into a buffer or direct to the screen?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretForeground(self) -> 'Colour':
        """ 

`GetCaretForeground`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretForeground "Permalink to this definition")
Get the foreground colour of the caret.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineBackAlpha(self) -> int:
        """ 

`GetCaretLineBackAlpha`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretLineBackAlpha "Permalink to this definition")
Get the background alpha of the caret line.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineBackground(self) -> 'Colour':
        """ 

`GetCaretLineBackground`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretLineBackground "Permalink to this definition")
Get the colour of the background of the line containing the caret.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineVisible(self) -> bool:
        """ 

`GetCaretLineVisible`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretLineVisible "Permalink to this definition")
Is the background of the line containing the caret in a different colour?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretLineVisibleAlways(self) -> bool:
        """ 

`GetCaretLineVisibleAlways`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretLineVisibleAlways "Permalink to this definition")
Is the caret line always visible?



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretPeriod(self) -> int:
        """ 

`GetCaretPeriod`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretPeriod "Permalink to this definition")
Get the time in milliseconds that the caret is on and off.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretSticky(self) -> int:
        """ 

`GetCaretSticky`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretSticky "Permalink to this definition")
Can the caret preferred x position only be changed by explicit movement commands?


The return value will be one of the [``](#id35)STC\_CARETSTICKY\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretStyle(self) -> int:
        """ 

`GetCaretStyle`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretStyle "Permalink to this definition")
Returns the current style of the caret.


The return value will be one of the [``](#id37)STC\_CARETSTYLE\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCaretWidth(self) -> int:
        """ 

`GetCaretWidth`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCaretWidth "Permalink to this definition")
Returns the width of the insert mode caret.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCharAt(self, pos: int) -> int:
        """ 

`GetCharAt`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.GetCharAt "Permalink to this definition")
Returns the character byte at the position.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCharacterPointer(self) -> Any:
        """ 

`GetCharacterPointer`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCharacterPointer "Permalink to this definition")

> Compact the document buffer and return a read-only memoryview
> object of the characters in the document.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.stc.StyledTextCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
 [wx.VisualAttributes](wx.VisualAttributes.html#wx-visualattributes)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCodePage(self) -> int:
        """ 

`GetCodePage`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCodePage "Permalink to this definition")
Get the code page used to interpret the bytes of the document as characters.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetColumn(self, pos: int) -> int:
        """ 

`GetColumn`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.GetColumn "Permalink to this definition")
Retrieve the column number of a position, taking tab width into account.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetControlCharSymbol(self) -> int:
        """ 

`GetControlCharSymbol`(*self*)[¶](#wx.stc.StyledTextCtrl.GetControlCharSymbol "Permalink to this definition")
Get the way control characters are displayed.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurLine(self) -> tuple:
        """ 

`GetCurLine`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCurLine "Permalink to this definition")
Retrieve the text of the line containing the caret.


linePos can optionally be passed in to receive the index of the caret on the line.



Return type
*tuple*



Returns
( *String* , *linePos* )






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurLineRaw(self) -> tuple:
        """ 

`GetCurLineRaw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCurLineRaw "Permalink to this definition")
Retrieve the text of the line containing the caret.


Returns the index of the caret on the line.



Return type
*tuple*



Returns
( *CharBuffer* , *linePos* )






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurrentLine(self) -> int:
        """ 

`GetCurrentLine`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCurrentLine "Permalink to this definition")
Returns the line number of the line with the caret.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetCurrentPos(self) -> int:
        """ 

`GetCurrentPos`(*self*)[¶](#wx.stc.StyledTextCtrl.GetCurrentPos "Permalink to this definition")
Returns the position of the caret.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDefaultStyle(self) -> 'TextAttr':
        """ 

`GetDefaultStyle`(*self*)[¶](#wx.stc.StyledTextCtrl.GetDefaultStyle "Permalink to this definition")
Returns the style currently used for the new text.



Return type
 [wx.TextAttr](wx.TextAttr.html#wx-textattr)





See also


[`SetDefaultStyle`](#wx.stc.StyledTextCtrl.SetDefaultStyle "wx.stc.StyledTextCtrl.SetDefaultStyle")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDirectFunction(self) -> None:
        """ 

`GetDirectFunction`(*self*)[¶](#wx.stc.StyledTextCtrl.GetDirectFunction "Permalink to this definition")
Retrieve a pointer to a function that processes messages for this Scintilla.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDirectPointer(self) -> None:
        """ 

`GetDirectPointer`(*self*)[¶](#wx.stc.StyledTextCtrl.GetDirectPointer "Permalink to this definition")
Retrieve a pointer value to use as the first argument when calling the function returned by GetDirectFunction.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetDocPointer(self) -> None:
        """ 

`GetDocPointer`(*self*)[¶](#wx.stc.StyledTextCtrl.GetDocPointer "Permalink to this definition")
Retrieve a pointer to the document object.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEOLMode(self) -> int:
        """ 

`GetEOLMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEOLMode "Permalink to this definition")
Retrieve the current end of line mode - one of `wx.stc.STC_EOL_CRLF`, `wx.stc.STC_EOL_CR`, or `wx.stc.STC_EOL_LF`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeColour(self) -> 'Colour':
        """ 

`GetEdgeColour`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEdgeColour "Permalink to this definition")
Retrieve the colour used in edge indication.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeColumn(self) -> int:
        """ 

`GetEdgeColumn`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEdgeColumn "Permalink to this definition")
Retrieve the column number which text should be kept within.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEdgeMode(self) -> int:
        """ 

`GetEdgeMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEdgeMode "Permalink to this definition")
Retrieve the edge highlight mode.


The return value will be one of the [``](#id39)STC\_EDGE\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEndAtLastLine(self) -> bool:
        """ 

`GetEndAtLastLine`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEndAtLastLine "Permalink to this definition")
Retrieve whether the maximum scroll position has the last line at the bottom of the view.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetEndStyled(self) -> int:
        """ 

`GetEndStyled`(*self*)[¶](#wx.stc.StyledTextCtrl.GetEndStyled "Permalink to this definition")
Retrieve the position of the last correctly styled character.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetExtraAscent(self) -> int:
        """ 

`GetExtraAscent`(*self*)[¶](#wx.stc.StyledTextCtrl.GetExtraAscent "Permalink to this definition")
Get extra ascent for each line.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetExtraDescent(self) -> int:
        """ 

`GetExtraDescent`(*self*)[¶](#wx.stc.StyledTextCtrl.GetExtraDescent "Permalink to this definition")
Get extra descent for each line.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFirstVisibleLine(self) -> int:
        """ 

`GetFirstVisibleLine`(*self*)[¶](#wx.stc.StyledTextCtrl.GetFirstVisibleLine "Permalink to this definition")
Retrieve the display line at the top of the display.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldExpanded(self, line: int) -> bool:
        """ 

`GetFoldExpanded`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetFoldExpanded "Permalink to this definition")
Is a header line expanded?



Parameters
**line** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldLevel(self, line: int) -> int:
        """ 

`GetFoldLevel`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetFoldLevel "Permalink to this definition")
Retrieve the fold level of a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFoldParent(self, line: int) -> int:
        """ 

`GetFoldParent`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetFoldParent "Permalink to this definition")
Find the parent line of a child line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetFontQuality(self) -> int:
        """ 

`GetFontQuality`(*self*)[¶](#wx.stc.StyledTextCtrl.GetFontQuality "Permalink to this definition")
Retrieve the quality level for text.


The return value will be one of the [``](#id41)STC\_EFF\_QUALITY\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetGapPosition(self) -> int:
        """ 

`GetGapPosition`(*self*)[¶](#wx.stc.StyledTextCtrl.GetGapPosition "Permalink to this definition")
Return a position which, to avoid performance costs, should not be within the range of a call to GetRangePointer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHighlightGuide(self) -> int:
        """ 

`GetHighlightGuide`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHighlightGuide "Permalink to this definition")
Get the highlighted indentation guide column.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHint(self) -> str:
        """ 

`GetHint`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHint "Permalink to this definition")
Returns the current hint string.


See [`SetHint`](#wx.stc.StyledTextCtrl.SetHint "wx.stc.StyledTextCtrl.SetHint") for more information about hints.



Return type
`string`





New in version 2.9.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveBackground(self) -> 'Colour':
        """ 

`GetHotspotActiveBackground`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHotspotActiveBackground "Permalink to this definition")
Get the back colour for active hotspots.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveForeground(self) -> 'Colour':
        """ 

`GetHotspotActiveForeground`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHotspotActiveForeground "Permalink to this definition")
Get the fore colour for active hotspots.



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotActiveUnderline(self) -> bool:
        """ 

`GetHotspotActiveUnderline`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHotspotActiveUnderline "Permalink to this definition")
Get whether underlining for active hotspots.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetHotspotSingleLine(self) -> bool:
        """ 

`GetHotspotSingleLine`(*self*)[¶](#wx.stc.StyledTextCtrl.GetHotspotSingleLine "Permalink to this definition")
Get the HotspotSingleLine property.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIMEInteraction(self) -> int:
        """ 

`GetIMEInteraction`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIMEInteraction "Permalink to this definition")
Is the `IME` displayed in a window or inline?


The return value will be one of the [``](#id43)STC\_IME\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIdentifier(self) -> int:
        """ 

`GetIdentifier`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIdentifier "Permalink to this definition")
Get the identifier.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIdleStyling(self) -> int:
        """ 

`GetIdleStyling`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIdleStyling "Permalink to this definition")
Retrieve the limits to idle styling.


The return value will be one of the [``](#id45)STC\_IDLESTYLING\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndent(self) -> int:
        """ 

`GetIndent`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIndent "Permalink to this definition")
Retrieve indentation size.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndentationGuides(self) -> int:
        """ 

`GetIndentationGuides`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIndentationGuides "Permalink to this definition")
Are the indentation guides visible?


The return value will be one of the [``](#id47)STC\_IV\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndicatorCurrent(self) -> int:
        """ 

`GetIndicatorCurrent`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIndicatorCurrent "Permalink to this definition")
Get the current indicator.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetIndicatorValue(self) -> int:
        """ 

`GetIndicatorValue`(*self*)[¶](#wx.stc.StyledTextCtrl.GetIndicatorValue "Permalink to this definition")
Get the current indicator value.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetInsertionPoint(self) -> int:
        """ 

`GetInsertionPoint`(*self*)[¶](#wx.stc.StyledTextCtrl.GetInsertionPoint "Permalink to this definition")
Returns the insertion point, or cursor, position.


This is defined as the zero based index of the character position to the right of the insertion point. For example, if the insertion point is at the end of the single-line text control, it is equal to [`GetLastPosition`](#wx.stc.StyledTextCtrl.GetLastPosition "wx.stc.StyledTextCtrl.GetLastPosition") .


Notice that insertion position is, in general, different from the index of the character the cursor position at in the string returned by [`GetValue`](#wx.stc.StyledTextCtrl.GetValue "wx.stc.StyledTextCtrl.GetValue") . While this is always the case for the single line controls, multi-line controls can use two characters `"\\r\\n"` as line separator (this is notably the case under MSW) meaning that indices in the control and its string value are offset by 1 for every line.


Hence to correctly get the character at the current cursor position, taking into account that there can be none if the cursor is at the end of the string, you could do the following:



```
def GetCurrentChar(self, text_ctrl):

    pos = text_ctrl.GetInsertionPoint()
    if pos == text_ctrl.GetLastPosition():
        return ''

    return text_ctrl.GetRange(pos, pos + 1)

```



Return type
*long*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastChild(self, line, level) -> int:
        """ 

`GetLastChild`(*self*, *line*, *level*)[¶](#wx.stc.StyledTextCtrl.GetLastChild "Permalink to this definition")
Find the last child line of a header line.



Parameters
* **line** (*int*) –
* **level** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastKeydownProcessed(self) -> bool:
        """ 

`GetLastKeydownProcessed`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLastKeydownProcessed "Permalink to this definition")
Can be used to prevent the `EVT_CHAR` handler from adding the char.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLastPosition(self) -> int:
        """ 

`GetLastPosition`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLastPosition "Permalink to this definition")
Returns the zero based index of the last position in the text control, which is equal to the number of characters in the control.



Return type
*long*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLayoutCache(self) -> int:
        """ 

`GetLayoutCache`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLayoutCache "Permalink to this definition")
Retrieve the degree of caching of layout information.


The return value will be one of the [``](#id49)STC\_CACHE\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLength(self) -> int:
        """ 

`GetLength`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLength "Permalink to this definition")
Returns the number of bytes in the document.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLexer(self) -> int:
        """ 

`GetLexer`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLexer "Permalink to this definition")
Retrieve the lexing language of the document.


The return value will be one of the [``](#id51)STC\_LEX\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLexerLanguage(self) -> str:
        """ 

`GetLexerLanguage`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLexerLanguage "Permalink to this definition")
Retrieve the lexing language of the document.



Return type
`string`





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    @staticmethod
    def GetLibraryVersionInfo() -> 'VersionInfo':
        """ 

*static* `GetLibraryVersionInfo`()[¶](#wx.stc.StyledTextCtrl.GetLibraryVersionInfo "Permalink to this definition")
Returns the version of the Scintilla library used by this control.



Return type
 [wx.VersionInfo](wx.VersionInfo.html#wx-versioninfo)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLine(self, line: int) -> str:
        """ 

`GetLine`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLine "Permalink to this definition")
Retrieve the contents of a line.



Parameters
**line** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineCount(self) -> int:
        """ 

`GetLineCount`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLineCount "Permalink to this definition")
Returns the number of lines in the document.


There is always at least one.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndPosition(self, line: int) -> int:
        """ 

`GetLineEndPosition`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineEndPosition "Permalink to this definition")
Get the position after the last visible characters on a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesActive(self) -> int:
        """ 

`GetLineEndTypesActive`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLineEndTypesActive "Permalink to this definition")
Get the line end types currently recognised.


May be a subset of the allowed types due to lexer limitation.


The return value will be one of the [``](#id53)STC\_LINE\_END\_TYPE\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesAllowed(self) -> int:
        """ 

`GetLineEndTypesAllowed`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLineEndTypesAllowed "Permalink to this definition")
Get the line end types currently allowed.


The return value will be one of the [``](#id55)STC\_LINE\_END\_TYPE\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineEndTypesSupported(self) -> int:
        """ 

`GetLineEndTypesSupported`(*self*)[¶](#wx.stc.StyledTextCtrl.GetLineEndTypesSupported "Permalink to this definition")
Bit set of LineEndType enumertion for which line ends beyond the standard `LF`, `CR`, and `CRLF` are supported by the lexer.


The return value will be a bit list containing one or more of the [``](#id57)STC\_LINE\_END\_TYPE\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineIndentPosition(self, line: int) -> int:
        """ 

`GetLineIndentPosition`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineIndentPosition "Permalink to this definition")
Retrieve the position before the first non indentation character on a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineIndentation(self, line: int) -> int:
        """ 

`GetLineIndentation`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineIndentation "Permalink to this definition")
Retrieve the number of columns that a line is indented.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineLength(self, lineNo: int) -> int:
        """ 

`GetLineLength`(*self*, *lineNo*)[¶](#wx.stc.StyledTextCtrl.GetLineLength "Permalink to this definition")
Gets the length of the specified line, not including any trailing newline character(s).



Parameters
**lineNo** (*long*) – Line number (starting from zero).



Return type
*int*



Returns
The length of the line, or -1 if *lineNo* was invalid.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineRaw(self, line: int) -> 'CharBuffer':
        """ 

`GetLineRaw`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineRaw "Permalink to this definition")
Retrieve the contents of a line.



Parameters
**line** (*int*) – 



Return type
*CharBuffer*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineSelEndPosition(self, line: int) -> int:
        """ 

`GetLineSelEndPosition`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineSelEndPosition "Permalink to this definition")
Retrieve the position of the end of the selection at the given line (wx``wx.stc.STC\_INVALID\_POSITION`` if no selection on this line).



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineSelStartPosition(self, line: int) -> int:
        """ 

`GetLineSelStartPosition`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineSelStartPosition "Permalink to this definition")
Retrieve the position of the start of the selection at the given line (wx``wx.stc.STC\_INVALID\_POSITION`` if no selection on this line).



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineState(self, line: int) -> int:
        """ 

`GetLineState`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineState "Permalink to this definition")
Retrieve the extra styling information for a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineText(self, lineNo: int) -> str:
        """ 

`GetLineText`(*self*, *lineNo*)[¶](#wx.stc.StyledTextCtrl.GetLineText "Permalink to this definition")
Returns the contents of a given line in the text control, not including any trailing newline character(s).



Parameters
**lineNo** (*long*) – The line number, starting from zero.



Return type
`string`



Returns
The contents of the line.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetLineVisible(self, line: int) -> bool:
        """ 

`GetLineVisible`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GetLineVisible "Permalink to this definition")
Is a line visible?



Parameters
**line** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMainSelection(self) -> int:
        """ 

`GetMainSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMainSelection "Permalink to this definition")
Which selection is the main selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginBackground(self, margin: int) -> 'Colour':
        """ 

`GetMarginBackground`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginBackground "Permalink to this definition")
Retrieve the background colour of a margin.



Parameters
**margin** (*int*) – 



Return type
 [wx.Colour](wx.Colour.html#wx-colour)





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginCount(self) -> int:
        """ 

`GetMarginCount`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMarginCount "Permalink to this definition")
How many margins are there?.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginCursor(self, margin: int) -> int:
        """ 

`GetMarginCursor`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginCursor "Permalink to this definition")
Retrieve the cursor shown in a margin.


The return value will be one of the [``](#id59)STC\_CURSOR\* `` constants.



Parameters
**margin** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginLeft(self) -> int:
        """ 

`GetMarginLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMarginLeft "Permalink to this definition")
Returns the size in pixels of the left margin.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginMask(self, margin: int) -> int:
        """ 

`GetMarginMask`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginMask "Permalink to this definition")
Retrieve the marker mask of a margin.



Parameters
**margin** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginOptions(self) -> int:
        """ 

`GetMarginOptions`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMarginOptions "Permalink to this definition")
Get the margin options.


The return value will be one of the [``](#id61)STC\_MARGINOPTION\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginRight(self) -> int:
        """ 

`GetMarginRight`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMarginRight "Permalink to this definition")
Returns the size in pixels of the right margin.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginSensitive(self, margin: int) -> bool:
        """ 

`GetMarginSensitive`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginSensitive "Permalink to this definition")
Retrieve the mouse click sensitivity of a margin.



Parameters
**margin** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginType(self, margin: int) -> int:
        """ 

`GetMarginType`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginType "Permalink to this definition")
Retrieve the type of a margin.


The return value will be one of the [``](#id63)STC\_MARGIN\_\* `` constants.



Parameters
**margin** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarginWidth(self, margin: int) -> int:
        """ 

`GetMarginWidth`(*self*, *margin*)[¶](#wx.stc.StyledTextCtrl.GetMarginWidth "Permalink to this definition")
Retrieve the width of a margin in pixels.



Parameters
**margin** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMargins(self) -> 'Point':
        """ 

`GetMargins`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMargins "Permalink to this definition")
Returns the margins used by the control.


The `x` field of the returned point is the horizontal margin and the `y` field is the vertical one.



Return type
 [wx.Point](wx.Point.html#wx-point)





New in version 2.9.1.




Note


If given margin cannot be accurately determined, its value will be set to -1. On some platforms you cannot obtain valid margin values until you have called [`SetMargins`](#wx.stc.StyledTextCtrl.SetMargins "wx.stc.StyledTextCtrl.SetMargins") .




See also


[`SetMargins`](#wx.stc.StyledTextCtrl.SetMargins "wx.stc.StyledTextCtrl.SetMargins")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMarkerSymbolDefined(self, markerNumber: int) -> int:
        """ 

`GetMarkerSymbolDefined`(*self*, *markerNumber*)[¶](#wx.stc.StyledTextCtrl.GetMarkerSymbolDefined "Permalink to this definition")
Which symbol was defined for markerNumber with MarkerDefine.


The return value will be one of the [``](#id65)STC\_MARK\_\* `` constants.



Parameters
**markerNumber** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMaxLineState(self) -> int:
        """ 

`GetMaxLineState`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMaxLineState "Permalink to this definition")
Retrieve the last line number that has line state.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetModEventMask(self) -> int:
        """ 

`GetModEventMask`(*self*)[¶](#wx.stc.StyledTextCtrl.GetModEventMask "Permalink to this definition")
Get which document modification events are sent to the container.


The return value will `wx.stc.STC_MODEVENTMASKALL` if all changes generate events. Otherwise it will be a bit list containing one or more of the `STC_MOD_* ``   constants, the ``STC_PERFORMED_* ``   constants, ``wx.stc.STC_STARTACTION`, `wx.stc.STC_MULTILINEUNDOREDO`, `wx.stc.STC_MULTISTEPUNDOREDO`, and `wx.stc.STC_LASTSTEPINUNDOREDO`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetModify(self) -> bool:
        """ 

`GetModify`(*self*)[¶](#wx.stc.StyledTextCtrl.GetModify "Permalink to this definition")
Is the document different from when it was last saved?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseDownCaptures(self) -> bool:
        """ 

`GetMouseDownCaptures`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMouseDownCaptures "Permalink to this definition")
Get whether mouse gets captured.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseDwellTime(self) -> int:
        """ 

`GetMouseDwellTime`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMouseDwellTime "Permalink to this definition")
Retrieve the time the mouse must sit still to generate a mouse dwell event.


The return value will be a time in milliseconds or `wx.stc.STC_TIME_FOREVER`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseSelectionRectangularSwitch(self) -> bool:
        """ 

`GetMouseSelectionRectangularSwitch`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMouseSelectionRectangularSwitch "Permalink to this definition")
Whether switching to rectangular mode while selecting with the mouse is allowed.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMouseWheelCaptures(self) -> bool:
        """ 

`GetMouseWheelCaptures`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMouseWheelCaptures "Permalink to this definition")
Get whether mouse wheel can be active outside the window.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMultiPaste(self) -> int:
        """ 

`GetMultiPaste`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMultiPaste "Permalink to this definition")
Retrieve the effect of pasting when there are multiple selections.


The return value will be one of the [``](#id67)STC\_MULTIPASTE\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetMultipleSelection(self) -> bool:
        """ 

`GetMultipleSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.GetMultipleSelection "Permalink to this definition")
Whether multiple selections can be made.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetNextTabStop(self, line, x) -> int:
        """ 

`GetNextTabStop`(*self*, *line*, *x*)[¶](#wx.stc.StyledTextCtrl.GetNextTabStop "Permalink to this definition")
Find the next explicit tab stop position on a line after a position.



Parameters
* **line** (*int*) –
* **x** (*int*) –



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetNumberOfLines(self) -> int:
        """ 

`GetNumberOfLines`(*self*)[¶](#wx.stc.StyledTextCtrl.GetNumberOfLines "Permalink to this definition")
Returns the number of lines in the text control buffer.


The returned number is the number of logical lines, i.e. just the count of the number of newline characters in the control + 1, for wxGTK and OSX/Cocoa ports while it is the number of physical lines, i.e. the count of lines actually shown in the control, in wxMSW. Because of this discrepancy, it is not recommended to use this function.



Return type
*int*





Note


Note that even empty text controls have one line (where the insertion point is), so [`GetNumberOfLines`](#wx.stc.StyledTextCtrl.GetNumberOfLines "wx.stc.StyledTextCtrl.GetNumberOfLines") never returns 0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetOvertype(self) -> bool:
        """ 

`GetOvertype`(*self*)[¶](#wx.stc.StyledTextCtrl.GetOvertype "Permalink to this definition")
Returns `True` if overtype mode is active otherwise `False` is returned.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPasteConvertEndings(self) -> bool:
        """ 

`GetPasteConvertEndings`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPasteConvertEndings "Permalink to this definition")
Get convert-on-paste setting.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPhasesDraw(self) -> int:
        """ 

`GetPhasesDraw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPhasesDraw "Permalink to this definition")
How many phases is drawing done in?


The return value will be one of the [``](#id69)STC\_PHASES\_\* `` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPositionCacheSize(self) -> int:
        """ 

`GetPositionCacheSize`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPositionCacheSize "Permalink to this definition")
How many entries are allocated to the position cache?



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrimaryStyleFromStyle(self, style: int) -> int:
        """ 

`GetPrimaryStyleFromStyle`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.GetPrimaryStyleFromStyle "Permalink to this definition")
For a secondary style, return the primary style, else return the argument.



Parameters
**style** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintColourMode(self) -> int:
        """ 

`GetPrintColourMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPrintColourMode "Permalink to this definition")
Returns the print colour mode.


The return value will be one of the [``](#id71)STC\_PRINT\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintMagnification(self) -> int:
        """ 

`GetPrintMagnification`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPrintMagnification "Permalink to this definition")
Returns the print magnification.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPrintWrapMode(self) -> int:
        """ 

`GetPrintWrapMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPrintWrapMode "Permalink to this definition")
Is printing line wrapped?


The return value will be one of the [``](#id73)STC\_WRAP\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetProperty(self, key: str) -> str:
        """ 

`GetProperty`(*self*, *key*)[¶](#wx.stc.StyledTextCtrl.GetProperty "Permalink to this definition")
Retrieve a “property” value previously set with SetProperty.



Parameters
**key** (*string*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPropertyExpanded(self, key: str) -> str:
        """ 

`GetPropertyExpanded`(*self*, *key*)[¶](#wx.stc.StyledTextCtrl.GetPropertyExpanded "Permalink to this definition")
Retrieve a “property” value previously set with SetProperty, with “$()” variable replacement on returned buffer.



Parameters
**key** (*string*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPropertyInt(self, key, defaultValue=0) -> int:
        """ 

`GetPropertyInt`(*self*, *key*, *defaultValue=0*)[¶](#wx.stc.StyledTextCtrl.GetPropertyInt "Permalink to this definition")
Retrieve a “property” value previously set with SetProperty, interpreted as an int `AFTER` any “$()” variable replacement.



Parameters
* **key** (*string*) –
* **defaultValue** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetPunctuationChars(self) -> str:
        """ 

`GetPunctuationChars`(*self*)[¶](#wx.stc.StyledTextCtrl.GetPunctuationChars "Permalink to this definition")
Get the set of characters making up punctuation characters.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRange(self, from_, to_) -> str:
        """ 

`GetRange`(*self*, *from\_*, *to\_*)[¶](#wx.stc.StyledTextCtrl.GetRange "Permalink to this definition")
Returns the string containing the text starting in the positions *from* and up to *to* in the control.


The positions must have been returned by another  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) method. Please note that the positions in a multiline  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) do **not** correspond to the indices in the string returned by [`GetValue`](#wx.stc.StyledTextCtrl.GetValue "wx.stc.StyledTextCtrl.GetValue") because of the different new line representations ( `CR` or `CR` `LF`) and so this method should be used to obtain the correct results instead of extracting parts of the entire value. It may also be more efficient, especially if the control contains a lot of data.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRangePointer(self, position, rangeLength) -> Any:
        """ 

`GetRangePointer`(*self*, *position*, *rangeLength*)[¶](#wx.stc.StyledTextCtrl.GetRangePointer "Permalink to this definition")

> Return a read-only pointer to a range of characters in the
> document. May move the gap so that the range is contiguous,
> but will only move up to rangeLength bytes.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetReadOnly(self) -> bool:
        """ 

`GetReadOnly`(*self*)[¶](#wx.stc.StyledTextCtrl.GetReadOnly "Permalink to this definition")
In read-only mode?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionAnchor(self) -> int:
        """ 

`GetRectangularSelectionAnchor`(*self*)[¶](#wx.stc.StyledTextCtrl.GetRectangularSelectionAnchor "Permalink to this definition")
Return the anchor position of the rectangular selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionAnchorVirtualSpace(self) -> int:
        """ 

`GetRectangularSelectionAnchorVirtualSpace`(*self*)[¶](#wx.stc.StyledTextCtrl.GetRectangularSelectionAnchorVirtualSpace "Permalink to this definition")
Return the virtual space of the anchor of the rectangular selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionCaret(self) -> int:
        """ 

`GetRectangularSelectionCaret`(*self*)[¶](#wx.stc.StyledTextCtrl.GetRectangularSelectionCaret "Permalink to this definition")
Return the caret position of the rectangular selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionCaretVirtualSpace(self) -> int:
        """ 

`GetRectangularSelectionCaretVirtualSpace`(*self*)[¶](#wx.stc.StyledTextCtrl.GetRectangularSelectionCaretVirtualSpace "Permalink to this definition")
Return the virtual space of the caret of the rectangular selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRectangularSelectionModifier(self) -> int:
        """ 

`GetRectangularSelectionModifier`(*self*)[¶](#wx.stc.StyledTextCtrl.GetRectangularSelectionModifier "Permalink to this definition")
Get the modifier key used for rectangular selection.


The return value will be a bit list containing one or more of the [``](#id75)STC\_KEYMOD\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetRepresentation(self, encodedCharacter: str) -> str:
        """ 

`GetRepresentation`(*self*, *encodedCharacter*)[¶](#wx.stc.StyledTextCtrl.GetRepresentation "Permalink to this definition")
Set the way a character is drawn.



Parameters
**encodedCharacter** (*string*) – 



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSTCCursor(self) -> int:
        """ 

`GetSTCCursor`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSTCCursor "Permalink to this definition")
Get cursor type.


The return value will be one of the [``](#id77)STC\_CURSOR\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSTCFocus(self) -> bool:
        """ 

`GetSTCFocus`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSTCFocus "Permalink to this definition")
Get internal focus flag.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetScrollWidth(self) -> int:
        """ 

`GetScrollWidth`(*self*)[¶](#wx.stc.StyledTextCtrl.GetScrollWidth "Permalink to this definition")
Retrieve the document width assumed for scrolling.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetScrollWidthTracking(self) -> bool:
        """ 

`GetScrollWidthTracking`(*self*)[¶](#wx.stc.StyledTextCtrl.GetScrollWidthTracking "Permalink to this definition")
Retrieve whether the scroll width tracks wide lines.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSearchFlags(self) -> int:
        """ 

`GetSearchFlags`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSearchFlags "Permalink to this definition")
Get the search flags used by SearchInTarget.


The return value will be a bit list containing one or more of the [``](#id79)STC\_FIND\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelAlpha(self) -> int:
        """ 

`GetSelAlpha`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelAlpha "Permalink to this definition")
Get the alpha of the selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelEOLFilled(self) -> bool:
        """ 

`GetSelEOLFilled`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelEOLFilled "Permalink to this definition")
Is the selection end of line filled?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectedText(self) -> str:
        """ 

`GetSelectedText`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectedText "Permalink to this definition")
Retrieve the selected text.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectedTextRaw(self) -> 'CharBuffer':
        """ 

`GetSelectedTextRaw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectedTextRaw "Permalink to this definition")
Retrieve the selected text.



Return type
*CharBuffer*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelection(self) -> tuple:
        """ 

`GetSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelection "Permalink to this definition")
Gets the current selection span.


If the returned values are equal, there was no selection. Please note that the indices returned may be used with the other  [wx.TextCtrl](wx.TextCtrl.html#wx-textctrl) methods but don’t necessarily represent the correct indices into the string returned by [`GetValue`](#wx.stc.StyledTextCtrl.GetValue "wx.stc.StyledTextCtrl.GetValue") for multiline controls under Windows (at least,) you should use [`GetStringSelection`](#wx.stc.StyledTextCtrl.GetStringSelection "wx.stc.StyledTextCtrl.GetStringSelection") to get the selected text.


The returned first position.


The returned last position.



Return type
*tuple*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionEmpty(self) -> bool:
        """ 

`GetSelectionEmpty`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectionEmpty "Permalink to this definition")
Is every selected range empty?



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionEnd(self) -> int:
        """ 

`GetSelectionEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectionEnd "Permalink to this definition")
Returns the position at the end of the selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionMode(self) -> int:
        """ 

`GetSelectionMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectionMode "Permalink to this definition")
Get the mode of the current selection.


The return value will be one of the [``](#id81)STC\_SEL\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNAnchor(self, selection: int) -> int:
        """ 

`GetSelectionNAnchor`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNAnchor "Permalink to this definition")
Return the anchor position of the nth selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNAnchorVirtualSpace(self, selection: int) -> int:
        """ 

`GetSelectionNAnchorVirtualSpace`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNAnchorVirtualSpace "Permalink to this definition")
Return the virtual space of the anchor of the nth selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNCaret(self, selection: int) -> int:
        """ 

`GetSelectionNCaret`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNCaret "Permalink to this definition")
Return the caret position of the nth selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNCaretVirtualSpace(self, selection: int) -> int:
        """ 

`GetSelectionNCaretVirtualSpace`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNCaretVirtualSpace "Permalink to this definition")
Return the virtual space of the caret of the nth selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNEnd(self, selection: int) -> int:
        """ 

`GetSelectionNEnd`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNEnd "Permalink to this definition")
Returns the position at the end of the selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionNStart(self, selection: int) -> int:
        """ 

`GetSelectionNStart`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.GetSelectionNStart "Permalink to this definition")
Returns the position at the start of the selection.



Parameters
**selection** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelectionStart(self) -> int:
        """ 

`GetSelectionStart`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelectionStart "Permalink to this definition")
Returns the position at the start of the selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSelections(self) -> int:
        """ 

`GetSelections`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSelections "Permalink to this definition")
How many selections are there?



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStatus(self) -> int:
        """ 

`GetStatus`(*self*)[¶](#wx.stc.StyledTextCtrl.GetStatus "Permalink to this definition")
Get error status.


The return value will be one of the [``](#id83)STC\_STATUS\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStringSelection(self) -> str:
        """ 

`GetStringSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.GetStringSelection "Permalink to this definition")
Gets the text currently selected in the control.


If there is no selection, the returned string is empty.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyle(self, position, style) -> bool:
        """ 

`GetStyle`(*self*, *position*, *style*)[¶](#wx.stc.StyledTextCtrl.GetStyle "Permalink to this definition")
This method is inherited from TextAreaBase but is not implemented in  [wx.stc.StyledTextCtrl](#wx-stc-styledtextctrl).



Parameters
* **position** (*long*) –
* **style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleAt(self, pos: int) -> int:
        """ 

`GetStyleAt`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.GetStyleAt "Permalink to this definition")
Returns the style byte at the position.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleBits(self) -> int:
        """ 

`GetStyleBits`(*self*)[¶](#wx.stc.StyledTextCtrl.GetStyleBits "Permalink to this definition")
Retrieve number of bits in style bytes used to hold the lexical state.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleBitsNeeded(self) -> int:
        """ 

`GetStyleBitsNeeded`(*self*)[¶](#wx.stc.StyledTextCtrl.GetStyleBitsNeeded "Permalink to this definition")
Retrieve the number of bits the current lexer needs for styling.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyleFromSubStyle(self, subStyle: int) -> int:
        """ 

`GetStyleFromSubStyle`(*self*, *subStyle*)[¶](#wx.stc.StyledTextCtrl.GetStyleFromSubStyle "Permalink to this definition")
For a sub style, return the base style, else return the argument.



Parameters
**subStyle** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetStyledText(self, startPos, endPos) -> 'MemoryBuffer':
        """ 

`GetStyledText`(*self*, *startPos*, *endPos*)[¶](#wx.stc.StyledTextCtrl.GetStyledText "Permalink to this definition")
Retrieve a buffer of cells.



Parameters
* **startPos** (*int*) –
* **endPos** (*int*) –



Return type
*MemoryBuffer*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStyleBases(self) -> str:
        """ 

`GetSubStyleBases`(*self*)[¶](#wx.stc.StyledTextCtrl.GetSubStyleBases "Permalink to this definition")
Get the set of base styles that can be extended with sub styles.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStylesLength(self, styleBase: int) -> int:
        """ 

`GetSubStylesLength`(*self*, *styleBase*)[¶](#wx.stc.StyledTextCtrl.GetSubStylesLength "Permalink to this definition")
The number of sub styles associated with a base style.



Parameters
**styleBase** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetSubStylesStart(self, styleBase: int) -> int:
        """ 

`GetSubStylesStart`(*self*, *styleBase*)[¶](#wx.stc.StyledTextCtrl.GetSubStylesStart "Permalink to this definition")
The starting style number for the sub styles associated with a base style.



Parameters
**styleBase** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabDrawMode(self) -> int:
        """ 

`GetTabDrawMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTabDrawMode "Permalink to this definition")
Retrieve the current tab draw mode.


Returns one of `STC_TD_` constants.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabIndents(self) -> bool:
        """ 

`GetTabIndents`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTabIndents "Permalink to this definition")
Does a tab pressed when caret is within indentation indent?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTabWidth(self) -> int:
        """ 

`GetTabWidth`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTabWidth "Permalink to this definition")
Retrieve the visible size of a tab.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTag(self, tagNumber: int) -> str:
        """ 

`GetTag`(*self*, *tagNumber*)[¶](#wx.stc.StyledTextCtrl.GetTag "Permalink to this definition")
Retrieve the value of a tag from a regular expression search.



Parameters
**tagNumber** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetEnd(self) -> int:
        """ 

`GetTargetEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTargetEnd "Permalink to this definition")
Get the position that ends the target.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetStart(self) -> int:
        """ 

`GetTargetStart`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTargetStart "Permalink to this definition")
Get the position that starts the target.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetText(self) -> str:
        """ 

`GetTargetText`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTargetText "Permalink to this definition")
Retrieve the text in the target.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTargetTextRaw(self) -> 'CharBuffer':
        """ 

`GetTargetTextRaw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTargetTextRaw "Permalink to this definition")
Retrieve the target text.



Return type
*CharBuffer*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTechnology(self) -> int:
        """ 

`GetTechnology`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTechnology "Permalink to this definition")
Get the tech.


The return value will be one of the [``](#id85)STC\_TECHNOLOGY\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.stc.StyledTextCtrl.GetText "Permalink to this definition")
Retrieve all the text in the document.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextLength(self) -> int:
        """ 

`GetTextLength`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTextLength "Permalink to this definition")
Retrieve the number of characters in the document.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRange(self, startPos, endPos) -> str:
        """ 

`GetTextRange`(*self*, *startPos*, *endPos*)[¶](#wx.stc.StyledTextCtrl.GetTextRange "Permalink to this definition")
Retrieve a range of text.



Parameters
* **startPos** (*int*) –
* **endPos** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRangeRaw(self, startPos, endPos) -> 'CharBuffer':
        """ 

`GetTextRangeRaw`(*self*, *startPos*, *endPos*)[¶](#wx.stc.StyledTextCtrl.GetTextRangeRaw "Permalink to this definition")
Retrieve a range of text.



Parameters
* **startPos** (*int*) –
* **endPos** (*int*) –



Return type
*CharBuffer*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTextRaw(self) -> 'CharBuffer':
        """ 

`GetTextRaw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTextRaw "Permalink to this definition")
Retrieve all the text in the document.



Return type
*CharBuffer*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetTwoPhaseDraw(self) -> bool:
        """ 

`GetTwoPhaseDraw`(*self*)[¶](#wx.stc.StyledTextCtrl.GetTwoPhaseDraw "Permalink to this definition")
Is drawing done in two phases with backgrounds drawn before foregrounds?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUndoCollection(self) -> bool:
        """ 

`GetUndoCollection`(*self*)[¶](#wx.stc.StyledTextCtrl.GetUndoCollection "Permalink to this definition")
Is undo history being collected?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseAntiAliasing(self) -> bool:
        """ 

`GetUseAntiAliasing`(*self*)[¶](#wx.stc.StyledTextCtrl.GetUseAntiAliasing "Permalink to this definition")
Returns the current UseAntiAliasing setting.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseHorizontalScrollBar(self) -> bool:
        """ 

`GetUseHorizontalScrollBar`(*self*)[¶](#wx.stc.StyledTextCtrl.GetUseHorizontalScrollBar "Permalink to this definition")
Is the horizontal scroll bar visible?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseTabs(self) -> bool:
        """ 

`GetUseTabs`(*self*)[¶](#wx.stc.StyledTextCtrl.GetUseTabs "Permalink to this definition")
Retrieve whether tabs will be used in indentation.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetUseVerticalScrollBar(self) -> bool:
        """ 

`GetUseVerticalScrollBar`(*self*)[¶](#wx.stc.StyledTextCtrl.GetUseVerticalScrollBar "Permalink to this definition")
Is the vertical scroll bar visible?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetValue(self) -> str:
        """ 

`GetValue`(*self*)[¶](#wx.stc.StyledTextCtrl.GetValue "Permalink to this definition")
Gets the contents of the control.


Notice that for a multiline text control, the lines will be separated by (Unix-style) `\n` characters, even under Windows where they are separated by a `\r\n` sequence in the native control.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetViewEOL(self) -> bool:
        """ 

`GetViewEOL`(*self*)[¶](#wx.stc.StyledTextCtrl.GetViewEOL "Permalink to this definition")
Are the end of line characters visible?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetViewWhiteSpace(self) -> int:
        """ 

`GetViewWhiteSpace`(*self*)[¶](#wx.stc.StyledTextCtrl.GetViewWhiteSpace "Permalink to this definition")
Are white space characters currently visible? Returns one of `STC_WS_` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetVirtualSpaceOptions(self) -> int:
        """ 

`GetVirtualSpaceOptions`(*self*)[¶](#wx.stc.StyledTextCtrl.GetVirtualSpaceOptions "Permalink to this definition")
Return options for virtual space behaviour.


The return value will be one of the [``](#id87)STC\_VS\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWhitespaceChars(self) -> str:
        """ 

`GetWhitespaceChars`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWhitespaceChars "Permalink to this definition")
Get the set of characters making up whitespace for when moving or selecting by word.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWhitespaceSize(self) -> int:
        """ 

`GetWhitespaceSize`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWhitespaceSize "Permalink to this definition")
Get the size of the dots used to mark space characters.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWordChars(self) -> str:
        """ 

`GetWordChars`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWordChars "Permalink to this definition")
Get the set of characters making up words for when moving or selecting by word.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapIndentMode(self) -> int:
        """ 

`GetWrapIndentMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWrapIndentMode "Permalink to this definition")
Retrieve how wrapped sublines are placed.


Default is `wx.stc.STC_WRAPINDENT_FIXED`.


The return value will be one of the [``](#id89)STC\_WRAPINDENT\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapMode(self) -> int:
        """ 

`GetWrapMode`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWrapMode "Permalink to this definition")
Retrieve whether text is word wrapped.


The return value will be one of the [``](#id91)STC\_WRAP\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapStartIndent(self) -> int:
        """ 

`GetWrapStartIndent`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWrapStartIndent "Permalink to this definition")
Retrieve the start indent for wrapped lines.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapVisualFlags(self) -> int:
        """ 

`GetWrapVisualFlags`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWrapVisualFlags "Permalink to this definition")
Retrieve the display mode of visual flags for wrapped lines.


The return value will be a bit list containing one or more of the [``](#id93)STC\_WRAPVISUALFLAG\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetWrapVisualFlagsLocation(self) -> int:
        """ 

`GetWrapVisualFlagsLocation`(*self*)[¶](#wx.stc.StyledTextCtrl.GetWrapVisualFlagsLocation "Permalink to this definition")
Retrieve the location of visual flags for wrapped lines.


The return value will be a bit list containing one or more of the [``](#id95)STC\_WRAPVISUALFLAGLOC\_\* `` constants.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetXOffset(self) -> int:
        """ 

`GetXOffset`(*self*)[¶](#wx.stc.StyledTextCtrl.GetXOffset "Permalink to this definition")
Get the xOffset (ie, horizontal scroll position).



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GetZoom(self) -> int:
        """ 

`GetZoom`(*self*)[¶](#wx.stc.StyledTextCtrl.GetZoom "Permalink to this definition")
Retrieve the zoom level.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GotoLine(self, line: int) -> None:
        """ 

`GotoLine`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.GotoLine "Permalink to this definition")
Set caret to start of a line and ensure it is visible.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def GotoPos(self, caret: int) -> None:
        """ 

`GotoPos`(*self*, *caret*)[¶](#wx.stc.StyledTextCtrl.GotoPos "Permalink to this definition")
Set caret to a position and ensure it is visible.



Parameters
**caret** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HideLines(self, lineStart, lineEnd) -> None:
        """ 

`HideLines`(*self*, *lineStart*, *lineEnd*)[¶](#wx.stc.StyledTextCtrl.HideLines "Permalink to this definition")
Make a range of lines invisible.



Parameters
* **lineStart** (*int*) –
* **lineEnd** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HideSelection(self, hide: bool) -> None:
        """ 

`HideSelection`(*self*, *hide*)[¶](#wx.stc.StyledTextCtrl.HideSelection "Permalink to this definition")
Draw the selection in normal style or with selection highlighted.



Parameters
**hide** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HitTestPos(self, pt) -> None:
        """ 

`HitTestPos`(*self*, *pt*)[¶](#wx.stc.StyledTextCtrl.HitTestPos "Permalink to this definition")
Finds the position of the character at the specified point.


If the return code is not `TE_HT_UNKNOWN` the row and column of the character closest to this position are returned, otherwise the output parameters are not modified.


Please note that this function is currently only implemented in Univ, wxMSW and wxGTK2 ports and always returns `TE_HT_UNKNOWN` in the other ports.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HitTest(self, pt) -> None:
        """ 

`HitTest`(*self*, *pt*)[¶](#wx.stc.StyledTextCtrl.HitTest "Permalink to this definition")
Finds the row and column of the character at the specified point.


If the return code is not `TE_HT_UNKNOWN` the row and column of the character closest to this position are returned, otherwise the output parameters are not modified.


Please note that this function is currently only implemented in Univ, wxMSW and wxGTK2 ports and always returns `TE_HT_UNKNOWN` in the other ports.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Home(self) -> None:
        """ 

`Home`(*self*)[¶](#wx.stc.StyledTextCtrl.Home "Permalink to this definition")
Move caret to first position on line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeDisplay(self) -> None:
        """ 

`HomeDisplay`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeDisplay "Permalink to this definition")
Move caret to first position on display line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeDisplayExtend(self) -> None:
        """ 

`HomeDisplayExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeDisplayExtend "Permalink to this definition")
Move caret to first position on display line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeExtend(self) -> None:
        """ 

`HomeExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeExtend "Permalink to this definition")
Move caret to first position on line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeRectExtend(self) -> None:
        """ 

`HomeRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeRectExtend "Permalink to this definition")
Move caret to first position on line, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeWrap(self) -> None:
        """ 

`HomeWrap`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeWrap "Permalink to this definition")
Like Home but when word-wrap is enabled goes first to start of display line HomeDisplay, then to start of document line Home.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def HomeWrapExtend(self) -> None:
        """ 

`HomeWrapExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.HomeWrapExtend "Permalink to this definition")
Like HomeExtend but when word-wrap is enabled extends first to start of display line HomeDisplayExtend, then to start of document line HomeExtend.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorAllOnFor(self, pos: int) -> int:
        """ 

`IndicatorAllOnFor`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.IndicatorAllOnFor "Permalink to this definition")
Are any indicators present at pos?



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorClearRange(self, start, lengthClear) -> None:
        """ 

`IndicatorClearRange`(*self*, *start*, *lengthClear*)[¶](#wx.stc.StyledTextCtrl.IndicatorClearRange "Permalink to this definition")
Turn an indicator off over a range.



Parameters
* **start** (*int*) –
* **lengthClear** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorEnd(self, indicator, pos) -> int:
        """ 

`IndicatorEnd`(*self*, *indicator*, *pos*)[¶](#wx.stc.StyledTextCtrl.IndicatorEnd "Permalink to this definition")
Where does a particular indicator end?



Parameters
* **indicator** (*int*) –
* **pos** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorFillRange(self, start, lengthFill) -> None:
        """ 

`IndicatorFillRange`(*self*, *start*, *lengthFill*)[¶](#wx.stc.StyledTextCtrl.IndicatorFillRange "Permalink to this definition")
Turn an indicator on over a range.



Parameters
* **start** (*int*) –
* **lengthFill** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetAlpha(self, indicator: int) -> int:
        """ 

`IndicatorGetAlpha`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetAlpha "Permalink to this definition")
Get the alpha fill colour of the given indicator.



Parameters
**indicator** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetFlags(self, indicator: int) -> int:
        """ 

`IndicatorGetFlags`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetFlags "Permalink to this definition")
Retrieve the attributes of an indicator.


The return value will be a bit list containing one or more of the [``](#id97)STC\_INDICFLAG\_\* `` constants.



Parameters
**indicator** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetForeground(self, indicator: int) -> 'Colour':
        """ 

`IndicatorGetForeground`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetForeground "Permalink to this definition")
Retrieve the foreground colour of an indicator.



Parameters
**indicator** (*int*) – 



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetHoverForeground(self, indicator: int) -> 'Colour':
        """ 

`IndicatorGetHoverForeground`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetHoverForeground "Permalink to this definition")
Retrieve the foreground hover colour of an indicator.



Parameters
**indicator** (*int*) – 



Return type
 [wx.Colour](wx.Colour.html#wx-colour)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetHoverStyle(self, indicator: int) -> int:
        """ 

`IndicatorGetHoverStyle`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetHoverStyle "Permalink to this definition")
Retrieve the hover style of an indicator.



Parameters
**indicator** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetOutlineAlpha(self, indicator: int) -> int:
        """ 

`IndicatorGetOutlineAlpha`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetOutlineAlpha "Permalink to this definition")
Get the alpha outline colour of the given indicator.



Parameters
**indicator** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetStyle(self, indicator: int) -> int:
        """ 

`IndicatorGetStyle`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetStyle "Permalink to this definition")
Retrieve the style of an indicator.


The return value will be one of the [``](#id99)STC\_INDIC\_\* `` constants.



Parameters
**indicator** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorGetUnder(self, indicator: int) -> bool:
        """ 

`IndicatorGetUnder`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.IndicatorGetUnder "Permalink to this definition")
Retrieve whether indicator drawn under or over text.



Parameters
**indicator** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetAlpha(self, indicator, alpha) -> None:
        """ 

`IndicatorSetAlpha`(*self*, *indicator*, *alpha*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetAlpha "Permalink to this definition")
Set the alpha fill colour of the given indicator.



Parameters
* **indicator** (*int*) –
* **alpha** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetFlags(self, indicator, flags) -> None:
        """ 

`IndicatorSetFlags`(*self*, *indicator*, *flags*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetFlags "Permalink to this definition")
Set the attributes of an indicator.


The second argument should be a bit list containing one or more of the [``](#id101)STC\_INDICFLAG\_\* `` constants.



Parameters
* **indicator** (*int*) –
* **flags** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetForeground(self, indicator, fore) -> None:
        """ 

`IndicatorSetForeground`(*self*, *indicator*, *fore*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetForeground "Permalink to this definition")
Set the foreground colour of an indicator.



Parameters
* **indicator** (*int*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetHoverForeground(self, indicator, fore) -> None:
        """ 

`IndicatorSetHoverForeground`(*self*, *indicator*, *fore*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetHoverForeground "Permalink to this definition")
Set the foreground hover colour of an indicator.



Parameters
* **indicator** (*int*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetHoverStyle(self, indicator, indicatorStyle) -> None:
        """ 

`IndicatorSetHoverStyle`(*self*, *indicator*, *indicatorStyle*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetHoverStyle "Permalink to this definition")
Set a hover indicator to plain, squiggle or `TT`.



Parameters
* **indicator** (*int*) –
* **indicatorStyle** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetOutlineAlpha(self, indicator, alpha) -> None:
        """ 

`IndicatorSetOutlineAlpha`(*self*, *indicator*, *alpha*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetOutlineAlpha "Permalink to this definition")
Set the alpha outline colour of the given indicator.



Parameters
* **indicator** (*int*) –
* **alpha** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetStyle(self, indicator, indicatorStyle) -> None:
        """ 

`IndicatorSetStyle`(*self*, *indicator*, *indicatorStyle*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetStyle "Permalink to this definition")
Set an indicator to plain, squiggle or `TT`.


The second argument should be one of the [``](#id103)STC\_INDIC\_\* `` constants.



Parameters
* **indicator** (*int*) –
* **indicatorStyle** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorSetUnder(self, indicator, under) -> None:
        """ 

`IndicatorSetUnder`(*self*, *indicator*, *under*)[¶](#wx.stc.StyledTextCtrl.IndicatorSetUnder "Permalink to this definition")
Set an indicator to draw under text or over(default).



Parameters
* **indicator** (*int*) –
* **under** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorStart(self, indicator, pos) -> int:
        """ 

`IndicatorStart`(*self*, *indicator*, *pos*)[¶](#wx.stc.StyledTextCtrl.IndicatorStart "Permalink to this definition")
Where does a particular indicator start?



Parameters
* **indicator** (*int*) –
* **pos** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IndicatorValueAt(self, indicator, pos) -> int:
        """ 

`IndicatorValueAt`(*self*, *indicator*, *pos*)[¶](#wx.stc.StyledTextCtrl.IndicatorValueAt "Permalink to this definition")
What value does a particular indicator have at a position?



Parameters
* **indicator** (*int*) –
* **pos** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def InsertText(self, pos, text) -> None:
        """ 

`InsertText`(*self*, *pos*, *text*)[¶](#wx.stc.StyledTextCtrl.InsertText "Permalink to this definition")
Insert string at a position.



Parameters
* **pos** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def InsertTextRaw(self, pos, text) -> None:
        """ 

`InsertTextRaw`(*self*, *pos*, *text*)[¶](#wx.stc.StyledTextCtrl.InsertTextRaw "Permalink to this definition")
Insert string at a position.



Parameters
* **pos** (*int*) –
* **text** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsEditable(self) -> bool:
        """ 

`IsEditable`(*self*)[¶](#wx.stc.StyledTextCtrl.IsEditable "Permalink to this definition")
Returns `True` if the controls contents may be edited by user (note that it always can be changed by the program).


In other words, this functions returns `True` if the control hasn’t been put in read-only mode by a previous call to [`SetEditable`](#wx.stc.StyledTextCtrl.SetEditable "wx.stc.StyledTextCtrl.SetEditable") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.stc.StyledTextCtrl.IsEmpty "Permalink to this definition")
Returns `True` if the control is currently empty.


This is the same as [`GetValue`](#wx.stc.StyledTextCtrl.GetValue "wx.stc.StyledTextCtrl.GetValue") .empty() but can be much more efficient for the multiline controls containing big amounts of text.



Return type
*bool*





New in version 2.7.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsModified(self) -> bool:
        """ 

`IsModified`(*self*)[¶](#wx.stc.StyledTextCtrl.IsModified "Permalink to this definition")
Returns `True` if the text has been modified by user.


Note that calling [`SetValue`](#wx.stc.StyledTextCtrl.SetValue "wx.stc.StyledTextCtrl.SetValue") doesn’t make the control modified.



Return type
*bool*





See also


[`MarkDirty`](#wx.stc.StyledTextCtrl.MarkDirty "wx.stc.StyledTextCtrl.MarkDirty")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def IsRangeWord(self, start, end) -> bool:
        """ 

`IsRangeWord`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.IsRangeWord "Permalink to this definition")
Is the range start..end considered a word?



Parameters
* **start** (*int*) –
* **end** (*int*) –



Return type
*bool*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineCopy(self) -> None:
        """ 

`LineCopy`(*self*)[¶](#wx.stc.StyledTextCtrl.LineCopy "Permalink to this definition")
Copy the line containing the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineCut(self) -> None:
        """ 

`LineCut`(*self*)[¶](#wx.stc.StyledTextCtrl.LineCut "Permalink to this definition")
Cut the line containing the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDelete(self) -> None:
        """ 

`LineDelete`(*self*)[¶](#wx.stc.StyledTextCtrl.LineDelete "Permalink to this definition")
Delete the line containing the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDown(self) -> None:
        """ 

`LineDown`(*self*)[¶](#wx.stc.StyledTextCtrl.LineDown "Permalink to this definition")
Move caret down one line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDownExtend(self) -> None:
        """ 

`LineDownExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineDownExtend "Permalink to this definition")
Move caret down one line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDownRectExtend(self) -> None:
        """ 

`LineDownRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineDownRectExtend "Permalink to this definition")
Move caret down one line, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineDuplicate(self) -> None:
        """ 

`LineDuplicate`(*self*)[¶](#wx.stc.StyledTextCtrl.LineDuplicate "Permalink to this definition")
Duplicate the current line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEnd(self) -> None:
        """ 

`LineEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEnd "Permalink to this definition")
Move caret to last position on line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndDisplay(self) -> None:
        """ 

`LineEndDisplay`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndDisplay "Permalink to this definition")
Move caret to last position on display line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndDisplayExtend(self) -> None:
        """ 

`LineEndDisplayExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndDisplayExtend "Permalink to this definition")
Move caret to last position on display line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndExtend(self) -> None:
        """ 

`LineEndExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndExtend "Permalink to this definition")
Move caret to last position on line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndRectExtend(self) -> None:
        """ 

`LineEndRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndRectExtend "Permalink to this definition")
Move caret to last position on line, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndWrap(self) -> None:
        """ 

`LineEndWrap`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndWrap "Permalink to this definition")
Like LineEnd but when word-wrap is enabled goes first to end of display line LineEndDisplay, then to start of document line LineEnd.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineEndWrapExtend(self) -> None:
        """ 

`LineEndWrapExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineEndWrapExtend "Permalink to this definition")
Like LineEndExtend but when word-wrap is enabled extends first to end of display line LineEndDisplayExtend, then to start of document line LineEndExtend.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineFromPosition(self, pos: int) -> int:
        """ 

`LineFromPosition`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.LineFromPosition "Permalink to this definition")
Retrieve the line containing a position.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineLength(self, line: int) -> int:
        """ 

`LineLength`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.LineLength "Permalink to this definition")
How many characters are on a line, including end of line characters?



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScroll(self, columns, lines) -> None:
        """ 

`LineScroll`(*self*, *columns*, *lines*)[¶](#wx.stc.StyledTextCtrl.LineScroll "Permalink to this definition")
Scroll horizontally and vertically.



Parameters
* **columns** (*int*) –
* **lines** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScrollDown(self) -> None:
        """ 

`LineScrollDown`(*self*)[¶](#wx.stc.StyledTextCtrl.LineScrollDown "Permalink to this definition")
Scroll the document down, keeping the caret visible.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineScrollUp(self) -> None:
        """ 

`LineScrollUp`(*self*)[¶](#wx.stc.StyledTextCtrl.LineScrollUp "Permalink to this definition")
Scroll the document up, keeping the caret visible.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineTranspose(self) -> None:
        """ 

`LineTranspose`(*self*)[¶](#wx.stc.StyledTextCtrl.LineTranspose "Permalink to this definition")
Switch the current line with the previous.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUp(self) -> None:
        """ 

`LineUp`(*self*)[¶](#wx.stc.StyledTextCtrl.LineUp "Permalink to this definition")
Move caret up one line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUpExtend(self) -> None:
        """ 

`LineUpExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineUpExtend "Permalink to this definition")
Move caret up one line extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LineUpRectExtend(self) -> None:
        """ 

`LineUpRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.LineUpRectExtend "Permalink to this definition")
Move caret up one line, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesJoin(self) -> None:
        """ 

`LinesJoin`(*self*)[¶](#wx.stc.StyledTextCtrl.LinesJoin "Permalink to this definition")
Join the lines in the target.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesOnScreen(self) -> int:
        """ 

`LinesOnScreen`(*self*)[¶](#wx.stc.StyledTextCtrl.LinesOnScreen "Permalink to this definition")
Retrieves the number of lines completely visible.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LinesSplit(self, pixelWidth: int) -> None:
        """ 

`LinesSplit`(*self*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.LinesSplit "Permalink to this definition")
Split the lines in the target into lines that are less wide than pixelWidth where possible.



Parameters
**pixelWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LoadFile(self, filename: str) -> bool:
        """ 

`LoadFile`(*self*, *filename*)[¶](#wx.stc.StyledTextCtrl.LoadFile "Permalink to this definition")
Load the contents of filename into the editor.



Parameters
**filename** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LoadLexerLibrary(self, path: str) -> None:
        """ 

`LoadLexerLibrary`(*self*, *path*)[¶](#wx.stc.StyledTextCtrl.LoadLexerLibrary "Permalink to this definition")
Load a lexer library (dll / so).



Parameters
**path** (*string*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def LowerCase(self) -> None:
        """ 

`LowerCase`(*self*)[¶](#wx.stc.StyledTextCtrl.LowerCase "Permalink to this definition")
Transform the selection to lower case.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyle(self, line: int) -> int:
        """ 

`MarginGetStyle`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.MarginGetStyle "Permalink to this definition")
Get the style number for the text margin for a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyleOffset(self) -> int:
        """ 

`MarginGetStyleOffset`(*self*)[¶](#wx.stc.StyledTextCtrl.MarginGetStyleOffset "Permalink to this definition")
Get the start of the range of style numbers used for margin text.



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetStyles(self, line: int) -> str:
        """ 

`MarginGetStyles`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.MarginGetStyles "Permalink to this definition")
Get the styles in the text margin for a line.



Parameters
**line** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginGetText(self, line: int) -> str:
        """ 

`MarginGetText`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.MarginGetText "Permalink to this definition")
Get the text in the text margin for a line.



Parameters
**line** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyle(self, line, style) -> None:
        """ 

`MarginSetStyle`(*self*, *line*, *style*)[¶](#wx.stc.StyledTextCtrl.MarginSetStyle "Permalink to this definition")
Set the style number for the text margin for a line.



Parameters
* **line** (*int*) –
* **style** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyleOffset(self, style: int) -> None:
        """ 

`MarginSetStyleOffset`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.MarginSetStyleOffset "Permalink to this definition")
Get the start of the range of style numbers used for margin text.



Parameters
**style** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetStyles(self, line, styles) -> None:
        """ 

`MarginSetStyles`(*self*, *line*, *styles*)[¶](#wx.stc.StyledTextCtrl.MarginSetStyles "Permalink to this definition")
Set the style in the text margin for a line.



Parameters
* **line** (*int*) –
* **styles** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginSetText(self, line, text) -> None:
        """ 

`MarginSetText`(*self*, *line*, *text*)[¶](#wx.stc.StyledTextCtrl.MarginSetText "Permalink to this definition")
Set the text in the text margin for a line.



Parameters
* **line** (*int*) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarginTextClearAll(self) -> None:
        """ 

`MarginTextClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.MarginTextClearAll "Permalink to this definition")
Clear the margin text on all lines.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkDirty(self) -> None:
        """ 

`MarkDirty`(*self*)[¶](#wx.stc.StyledTextCtrl.MarkDirty "Permalink to this definition")
Mark text as modified (dirty).



See also


[`IsModified`](#wx.stc.StyledTextCtrl.IsModified "wx.stc.StyledTextCtrl.IsModified")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerAdd(self, line, markerNumber) -> int:
        """ 

`MarkerAdd`(*self*, *line*, *markerNumber*)[¶](#wx.stc.StyledTextCtrl.MarkerAdd "Permalink to this definition")
Add a marker to a line, returning an `ID` which can be used to find or delete the marker.



Parameters
* **line** (*int*) –
* **markerNumber** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerAddSet(self, line, markerSet) -> None:
        """ 

`MarkerAddSet`(*self*, *line*, *markerSet*)[¶](#wx.stc.StyledTextCtrl.MarkerAddSet "Permalink to this definition")
Add a set of markers to a line.



Parameters
* **line** (*int*) –
* **markerSet** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefine(self, markerNumber, markerSymbol, foreground=NullColour, background=NullColour) -> None:
        """ 

`MarkerDefine`(*self*, *markerNumber*, *markerSymbol*, *foreground=NullColour*, *background=NullColour*)[¶](#wx.stc.StyledTextCtrl.MarkerDefine "Permalink to this definition")
Set the symbol used for a particular marker number, and optionally the fore and background colours.


The second argument should be one of the [``](#id105)STC\_MARK\_\* `` constants.



Parameters
* **markerNumber** (*int*) –
* **markerSymbol** (*int*) –
* **foreground** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **background** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefineBitmap(self, markerNumber, bmp) -> None:
        """ 

`MarkerDefineBitmap`(*self*, *markerNumber*, *bmp*)[¶](#wx.stc.StyledTextCtrl.MarkerDefineBitmap "Permalink to this definition")
Define a marker with a  [wx.Bitmap](wx.Bitmap.html#wx-bitmap).



Parameters
* **markerNumber** (*int*) –
* **bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDefineRGBAImage(self, markerNumber, pixels) -> None:
        """ 

`MarkerDefineRGBAImage`(*self*, *markerNumber*, *pixels*)[¶](#wx.stc.StyledTextCtrl.MarkerDefineRGBAImage "Permalink to this definition")
Define a marker from `RGBA` data.


It has the width and height from RGBAImageSetWidth/Height. You must
ensure that the buffer is at least widthheight4 bytes long.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDelete(self, line, markerNumber) -> None:
        """ 

`MarkerDelete`(*self*, *line*, *markerNumber*)[¶](#wx.stc.StyledTextCtrl.MarkerDelete "Permalink to this definition")
Delete a marker from a line.



Parameters
* **line** (*int*) –
* **markerNumber** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDeleteAll(self, markerNumber: int) -> None:
        """ 

`MarkerDeleteAll`(*self*, *markerNumber*)[¶](#wx.stc.StyledTextCtrl.MarkerDeleteAll "Permalink to this definition")
Delete all markers with a particular number from all lines.



Parameters
**markerNumber** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerDeleteHandle(self, markerHandle: int) -> None:
        """ 

`MarkerDeleteHandle`(*self*, *markerHandle*)[¶](#wx.stc.StyledTextCtrl.MarkerDeleteHandle "Permalink to this definition")
Delete a marker.



Parameters
**markerHandle** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerEnableHighlight(self, enabled: bool) -> None:
        """ 

`MarkerEnableHighlight`(*self*, *enabled*)[¶](#wx.stc.StyledTextCtrl.MarkerEnableHighlight "Permalink to this definition")
Enable/disable highlight for current folding block (smallest one that contains the caret)



Parameters
**enabled** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerGet(self, line: int) -> int:
        """ 

`MarkerGet`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.MarkerGet "Permalink to this definition")
Get a bit mask of all the markers set on a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerLineFromHandle(self, markerHandle: int) -> int:
        """ 

`MarkerLineFromHandle`(*self*, *markerHandle*)[¶](#wx.stc.StyledTextCtrl.MarkerLineFromHandle "Permalink to this definition")
Retrieve the line number at which a particular marker is located.



Parameters
**markerHandle** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerNext(self, lineStart, markerMask) -> int:
        """ 

`MarkerNext`(*self*, *lineStart*, *markerMask*)[¶](#wx.stc.StyledTextCtrl.MarkerNext "Permalink to this definition")
Find the next line at or after lineStart that includes a marker in mask.


Return -1 when no more lines.



Parameters
* **lineStart** (*int*) –
* **markerMask** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerPrevious(self, lineStart, markerMask) -> int:
        """ 

`MarkerPrevious`(*self*, *lineStart*, *markerMask*)[¶](#wx.stc.StyledTextCtrl.MarkerPrevious "Permalink to this definition")
Find the previous line before lineStart that includes a marker in mask.



Parameters
* **lineStart** (*int*) –
* **markerMask** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetAlpha(self, markerNumber, alpha) -> None:
        """ 

`MarkerSetAlpha`(*self*, *markerNumber*, *alpha*)[¶](#wx.stc.StyledTextCtrl.MarkerSetAlpha "Permalink to this definition")
Set the alpha used for a marker that is drawn in the text area, not the margin.



Parameters
* **markerNumber** (*int*) –
* **alpha** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetBackground(self, markerNumber, back) -> None:
        """ 

`MarkerSetBackground`(*self*, *markerNumber*, *back*)[¶](#wx.stc.StyledTextCtrl.MarkerSetBackground "Permalink to this definition")
Set the background colour used for a particular marker number.



Parameters
* **markerNumber** (*int*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetBackgroundSelected(self, markerNumber, back) -> None:
        """ 

`MarkerSetBackgroundSelected`(*self*, *markerNumber*, *back*)[¶](#wx.stc.StyledTextCtrl.MarkerSetBackgroundSelected "Permalink to this definition")
Set the background colour used for a particular marker number when its folding block is selected.



Parameters
* **markerNumber** (*int*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MarkerSetForeground(self, markerNumber, fore) -> None:
        """ 

`MarkerSetForeground`(*self*, *markerNumber*, *fore*)[¶](#wx.stc.StyledTextCtrl.MarkerSetForeground "Permalink to this definition")
Set the foreground colour used for a particular marker number.



Parameters
* **markerNumber** (*int*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveCaretInsideView(self) -> None:
        """ 

`MoveCaretInsideView`(*self*)[¶](#wx.stc.StyledTextCtrl.MoveCaretInsideView "Permalink to this definition")
Move the caret inside current view if it’s not there already.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveSelectedLinesDown(self) -> None:
        """ 

`MoveSelectedLinesDown`(*self*)[¶](#wx.stc.StyledTextCtrl.MoveSelectedLinesDown "Permalink to this definition")
Move the selected lines down one line, shifting the line below before the selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MoveSelectedLinesUp(self) -> None:
        """ 

`MoveSelectedLinesUp`(*self*)[¶](#wx.stc.StyledTextCtrl.MoveSelectedLinesUp "Permalink to this definition")
Move the selected lines up one line, shifting the line above after the selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultiEdgeAddLine(self, column, edgeColour) -> None:
        """ 

`MultiEdgeAddLine`(*self*, *column*, *edgeColour*)[¶](#wx.stc.StyledTextCtrl.MultiEdgeAddLine "Permalink to this definition")
Add a new vertical edge to the view.



Parameters
* **column** (*int*) –
* **edgeColour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultiEdgeClearAll(self) -> None:
        """ 

`MultiEdgeClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.MultiEdgeClearAll "Permalink to this definition")
Clear all vertical edges.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultipleSelectAddEach(self) -> None:
        """ 

`MultipleSelectAddEach`(*self*)[¶](#wx.stc.StyledTextCtrl.MultipleSelectAddEach "Permalink to this definition")
Add each occurrence of the main selection in the target to the set of selections.


If the current selection is empty then select word around caret.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def MultipleSelectAddNext(self) -> None:
        """ 

`MultipleSelectAddNext`(*self*)[¶](#wx.stc.StyledTextCtrl.MultipleSelectAddNext "Permalink to this definition")
Add the next occurrence of the main selection to the set of selections as main.


If the current selection is empty then select word around caret.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def NewLine(self) -> None:
        """ 

`NewLine`(*self*)[¶](#wx.stc.StyledTextCtrl.NewLine "Permalink to this definition")
Insert a new line, may use a `CRLF`, `CR` or `LF` depending on `EOL` mode.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDown(self) -> None:
        """ 

`PageDown`(*self*)[¶](#wx.stc.StyledTextCtrl.PageDown "Permalink to this definition")
Move caret one page down.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDownExtend(self) -> None:
        """ 

`PageDownExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.PageDownExtend "Permalink to this definition")
Move caret one page down extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageDownRectExtend(self) -> None:
        """ 

`PageDownRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.PageDownRectExtend "Permalink to this definition")
Move caret one page down, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUp(self) -> None:
        """ 

`PageUp`(*self*)[¶](#wx.stc.StyledTextCtrl.PageUp "Permalink to this definition")
Move caret one page up.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUpExtend(self) -> None:
        """ 

`PageUpExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.PageUpExtend "Permalink to this definition")
Move caret one page up extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PageUpRectExtend(self) -> None:
        """ 

`PageUpRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.PageUpRectExtend "Permalink to this definition")
Move caret one page up, extending rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaDown(self) -> None:
        """ 

`ParaDown`(*self*)[¶](#wx.stc.StyledTextCtrl.ParaDown "Permalink to this definition")
Move caret down one paragraph (delimited by empty lines).




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaDownExtend(self) -> None:
        """ 

`ParaDownExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.ParaDownExtend "Permalink to this definition")
Extend selection down one paragraph (delimited by empty lines).




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaUp(self) -> None:
        """ 

`ParaUp`(*self*)[¶](#wx.stc.StyledTextCtrl.ParaUp "Permalink to this definition")
Move caret up one paragraph (delimited by empty lines).




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ParaUpExtend(self) -> None:
        """ 

`ParaUpExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.ParaUpExtend "Permalink to this definition")
Extend selection up one paragraph (delimited by empty lines).




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.stc.StyledTextCtrl.Paste "Permalink to this definition")
Paste the contents of the clipboard into the document replacing the selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PointFromPosition(self, pos: int) -> 'Point':
        """ 

`PointFromPosition`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.PointFromPosition "Permalink to this definition")
Retrieve the point in the window where a position is displayed.



Parameters
**pos** (*int*) – 



Return type
 [wx.Point](wx.Point.html#wx-point)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionAfter(self, pos: int) -> int:
        """ 

`PositionAfter`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.PositionAfter "Permalink to this definition")
Given a valid document position, return the next position taking code page into account.


Maximum value returned is the last position in the document.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionBefore(self, pos: int) -> int:
        """ 

`PositionBefore`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.PositionBefore "Permalink to this definition")
Given a valid document position, return the previous position taking code page into account.


Returns 0 if passed 0.



Parameters
**pos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromLine(self, line: int) -> int:
        """ 

`PositionFromLine`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.PositionFromLine "Permalink to this definition")
Retrieve the position at the start of a line.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromPoint(self, pt: Union[tuple[int, int], 'Point']) -> int:
        """ 

`PositionFromPoint`(*self*, *pt*)[¶](#wx.stc.StyledTextCtrl.PositionFromPoint "Permalink to this definition")
Find the position from a point within the window.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionFromPointClose(self, x, y) -> int:
        """ 

`PositionFromPointClose`(*self*, *x*, *y*)[¶](#wx.stc.StyledTextCtrl.PositionFromPointClose "Permalink to this definition")
Find the position from a point within the window but return `wx.stc.STC_INVALID_POSITION` if not close to text.



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionRelative(self, pos, relative) -> int:
        """ 

`PositionRelative`(*self*, *pos*, *relative*)[¶](#wx.stc.StyledTextCtrl.PositionRelative "Permalink to this definition")
Given a valid document position, return a position that differs in a number of characters.


Returned value is always between 0 and last position in document.



Parameters
* **pos** (*int*) –
* **relative** (*int*) –



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionToCoords(self, pos: int) -> 'Point':
        """ 

`PositionToCoords`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.PositionToCoords "Permalink to this definition")
Converts given text position to client coordinates in pixels.


This function allows finding where is the character at the given position displayed in the text control.



Parameters
**pos** (*long*) – Text position in 0 to [`GetLastPosition`](#wx.stc.StyledTextCtrl.GetLastPosition "wx.stc.StyledTextCtrl.GetLastPosition") range (inclusive).



Return type
 [wx.Point](wx.Point.html#wx-point)



Returns
On success returns a  [wx.Point](wx.Point.html#wx-point) which contains client coordinates for the given position in pixels, otherwise returns `wx.DefaultPosition` .





New in version 2.9.3.




Availability


Only available for MSW, GTK . Additionally, wxGTK only implements this method for multiline controls and `wx.DefaultPosition` is always returned for the single line ones.




See also


[`XYToPosition`](#wx.stc.StyledTextCtrl.XYToPosition "wx.stc.StyledTextCtrl.XYToPosition") , [`PositionToXY`](#wx.stc.StyledTextCtrl.PositionToXY "wx.stc.StyledTextCtrl.PositionToXY")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PositionToXY(self, pos: int) -> tuple:
        """ 

`PositionToXY`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.PositionToXY "Permalink to this definition")
Converts given position to a zero-based column, line number pair.



Parameters
**pos** (*long*) – Position.



Return type
*tuple*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PrivateLexerCall(self, operation, pointer) -> None:
        """ 

`PrivateLexerCall`(*self*, *operation*, *pointer*)[¶](#wx.stc.StyledTextCtrl.PrivateLexerCall "Permalink to this definition")
For private communication between an application and a known lexer.



Parameters
* **operation** (*int*) –
* **pointer** –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PropertyNames(self) -> str:
        """ 

`PropertyNames`(*self*)[¶](#wx.stc.StyledTextCtrl.PropertyNames "Permalink to this definition")
Retrieve a ‘\n’ separated list of properties understood by the current lexer.



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def PropertyType(self, name: str) -> int:
        """ 

`PropertyType`(*self*, *name*)[¶](#wx.stc.StyledTextCtrl.PropertyType "Permalink to this definition")
Retrieve the type of a property.


The return value will be one of the [``](#id107)STC\_TYPE\_\* `` constants.



Parameters
**name** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetHeight(self, height: int) -> None:
        """ 

`RGBAImageSetHeight`(*self*, *height*)[¶](#wx.stc.StyledTextCtrl.RGBAImageSetHeight "Permalink to this definition")
Set the height for future `RGBA` image data.



Parameters
**height** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetScale(self, scalePercent: int) -> None:
        """ 

`RGBAImageSetScale`(*self*, *scalePercent*)[¶](#wx.stc.StyledTextCtrl.RGBAImageSetScale "Permalink to this definition")
Set the scale factor in percent for future `RGBA` image data.



Parameters
**scalePercent** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RGBAImageSetWidth(self, width: int) -> None:
        """ 

`RGBAImageSetWidth`(*self*, *width*)[¶](#wx.stc.StyledTextCtrl.RGBAImageSetWidth "Permalink to this definition")
Set the width for future `RGBA` image data.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Redo(self) -> None:
        """ 

`Redo`(*self*)[¶](#wx.stc.StyledTextCtrl.Redo "Permalink to this definition")
Redoes the next action on the undo history.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RegisterImage(self, type, bmp) -> None:
        """ 

`RegisterImage`(*self*, *type*, *bmp*)[¶](#wx.stc.StyledTextCtrl.RegisterImage "Permalink to this definition")
Register an image for use in autocompletion lists.



Parameters
* **type** (*int*) –
* **bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RegisterRGBAImage(self, type, pixels) -> None:
        """ 

`RegisterRGBAImage`(*self*, *type*, *pixels*)[¶](#wx.stc.StyledTextCtrl.RegisterRGBAImage "Permalink to this definition")
Register an `RGBA` image for use in autocompletion lists.


It has the width and height from RGBAImageSetWidth/Height. You must
ensure that the buffer is at least widthheight4 bytes long.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReleaseAllExtendedStyles(self) -> None:
        """ 

`ReleaseAllExtendedStyles`(*self*)[¶](#wx.stc.StyledTextCtrl.ReleaseAllExtendedStyles "Permalink to this definition")
Release all extended (>255) style numbers.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReleaseDocument(self, docPointer: Any) -> None:
        """ 

`ReleaseDocument`(*self*, *docPointer*)[¶](#wx.stc.StyledTextCtrl.ReleaseDocument "Permalink to this definition")
Release a reference to the document, deleting document if it fades to black.



Parameters
**docPointer** – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Remove(self, from_, to_) -> None:
        """ 

`Remove`(*self*, *from\_*, *to\_*)[¶](#wx.stc.StyledTextCtrl.Remove "Permalink to this definition")
Removes the text starting at the first given position up to (but not including) the character at the last position.


This function puts the current insertion point position at *to* as a side effect.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –




The first position.


The last position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Replace(self, from_, to_, value) -> None:
        """ 

`Replace`(*self*, *from\_*, *to\_*, *value*)[¶](#wx.stc.StyledTextCtrl.Replace "Permalink to this definition")
Replaces the text starting at the first position up to (but not including) the character at the last position with the given text.


This function puts the current insertion point position at *to* as a side effect.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –
* **value** (*string*) – The value to replace the existing text with.




The first position.


The last position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceSelection(self, text: str) -> None:
        """ 

`ReplaceSelection`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.ReplaceSelection "Permalink to this definition")
Replace the selected text with the argument text.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceSelectionRaw(self, text: int) -> None:
        """ 

`ReplaceSelectionRaw`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.ReplaceSelectionRaw "Permalink to this definition")
Replace the current selection with text.


If there is no current selection, text is inserted at the current caret position.



Parameters
**text** (*int*) – The null terminated string used for the replacement.





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTarget(self, text: str) -> int:
        """ 

`ReplaceTarget`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.ReplaceTarget "Permalink to this definition")
Replace the target text with the argument text.


Text is counted so it can contain NULs. Returns the length of the replacement text.



Parameters
**text** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRE(self, text: str) -> int:
        """ 

`ReplaceTargetRE`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.ReplaceTargetRE "Permalink to this definition")
Replace the target text with the argument text after \d processing.


Text is counted so it can contain NULs. Looks for \d where d is between 1 and 9 and replaces these with the strings matched in the last search operation which were surrounded by \( and \). Returns the length of the replacement text including any change caused by processing the \d patterns.



Parameters
**text** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRERaw(self, text, length=-1) -> int:
        """ 

`ReplaceTargetRERaw`(*self*, *text*, *length=-1*)[¶](#wx.stc.StyledTextCtrl.ReplaceTargetRERaw "Permalink to this definition")
Replace the current target with text using regular expressions.


The replacement string will be formed from text with any occurrences ‘\1’ through ‘\9’ replaced by tagged matches from the most recent regular expression search. In addition, any occurrences of ‘\0’ will be replaced with all the matched text from the most recent search. After replacement, the target range refers to the replacement text.



Parameters
* **text** (*int*) –
* **length** (*int*) –



Return type
*int*



Returns
The return value is the length of the replacement string.





New in version 4.1/wxWidgets-3.1.3.




Note


If length=-1, text must be null terminated.




See also


[`SearchInTarget`](#wx.stc.StyledTextCtrl.SearchInTarget "wx.stc.StyledTextCtrl.SearchInTarget")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ReplaceTargetRaw(self, text, length=-1) -> int:
        """ 

`ReplaceTargetRaw`(*self*, *text*, *length=-1*)[¶](#wx.stc.StyledTextCtrl.ReplaceTargetRaw "Permalink to this definition")
Replace the current target with text.



Parameters
* **text** (*int*) –
* **length** (*int*) –



Return type
*int*



Returns
The return value is the length of the replacement string.





New in version 4.1/wxWidgets-3.1.3.




Note


If length=-1, text must be null terminated.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def RotateSelection(self) -> None:
        """ 

`RotateSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.RotateSelection "Permalink to this definition")
Set the main selection to the next selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SaveFile(self, filename: str) -> bool:
        """ 

`SaveFile`(*self*, *filename*)[¶](#wx.stc.StyledTextCtrl.SaveFile "Permalink to this definition")
Write the contents of the editor to filename.



Parameters
**filename** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollRange(self, secondary, primary) -> None:
        """ 

`ScrollRange`(*self*, *secondary*, *primary*)[¶](#wx.stc.StyledTextCtrl.ScrollRange "Permalink to this definition")
Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position.


This may be used to make a search match visible.



Parameters
* **secondary** (*int*) –
* **primary** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToColumn(self, column: int) -> None:
        """ 

`ScrollToColumn`(*self*, *column*)[¶](#wx.stc.StyledTextCtrl.ScrollToColumn "Permalink to this definition")
Scroll enough to make the given column visible.



Parameters
**column** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToEnd(self) -> None:
        """ 

`ScrollToEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.ScrollToEnd "Permalink to this definition")
Scroll to end of document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToLine(self, line: int) -> None:
        """ 

`ScrollToLine`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.ScrollToLine "Permalink to this definition")
Scroll enough to make the given line visible.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ScrollToStart(self) -> None:
        """ 

`ScrollToStart`(*self*)[¶](#wx.stc.StyledTextCtrl.ScrollToStart "Permalink to this definition")
Scroll to start of document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchAnchor(self) -> None:
        """ 

`SearchAnchor`(*self*)[¶](#wx.stc.StyledTextCtrl.SearchAnchor "Permalink to this definition")
Sets the current caret position to be the search anchor.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchInTarget(self, text: str) -> int:
        """ 

`SearchInTarget`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.SearchInTarget "Permalink to this definition")
Search for a counted string in the target and set the target to the found range.


Text is counted so it can contain NULs. Returns length of range or -1 for failure in which case target is not moved.



Parameters
**text** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchNext(self, searchFlags, text) -> int:
        """ 

`SearchNext`(*self*, *searchFlags*, *text*)[¶](#wx.stc.StyledTextCtrl.SearchNext "Permalink to this definition")
Find some text starting at the search anchor.


Does not ensure the selection is visible.



Parameters
* **searchFlags** (*int*) –
* **text** (*string*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SearchPrev(self, searchFlags, text) -> int:
        """ 

`SearchPrev`(*self*, *searchFlags*, *text*)[¶](#wx.stc.StyledTextCtrl.SearchPrev "Permalink to this definition")
Find some text starting at the search anchor and moving backwards.


Does not ensure the selection is visible.



Parameters
* **searchFlags** (*int*) –
* **text** (*string*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.stc.StyledTextCtrl.SelectAll "Permalink to this definition")
Select all the text in the document.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectNone(self) -> None:
        """ 

`SelectNone`(*self*)[¶](#wx.stc.StyledTextCtrl.SelectNone "Permalink to this definition")
Deselects selected text in the control.



New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectionDuplicate(self) -> None:
        """ 

`SelectionDuplicate`(*self*)[¶](#wx.stc.StyledTextCtrl.SelectionDuplicate "Permalink to this definition")
Duplicate the selection.


If selection empty duplicate the line containing the caret.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SelectionIsRectangle(self) -> bool:
        """ 

`SelectionIsRectangle`(*self*)[¶](#wx.stc.StyledTextCtrl.SelectionIsRectangle "Permalink to this definition")
Is the selection rectangular? The alternative is the more common stream selection.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SendMsg(self, msg, wp=0, lp=0) -> int:
        """ 

`SendMsg`(*self*, *msg*, *wp=0*, *lp=0*)[¶](#wx.stc.StyledTextCtrl.SendMsg "Permalink to this definition")
Scintilla API call.



Parameters
* **msg** (*int*) –
* **wp** (*wx.UIntPtr*) –
* **lp** (*wx.IntPtr*) –



Return type
*wx.IntPtr*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretForeground(self, fore: Union[int, str, 'Colour']) -> None:
        """ 

`SetAdditionalCaretForeground`(*self*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalCaretForeground "Permalink to this definition")
Set the foreground colour of additional carets.



Parameters
**fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretsBlink(self, additionalCaretsBlink: bool) -> None:
        """ 

`SetAdditionalCaretsBlink`(*self*, *additionalCaretsBlink*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalCaretsBlink "Permalink to this definition")
Set whether additional carets will blink.



Parameters
**additionalCaretsBlink** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalCaretsVisible(self, additionalCaretsVisible: bool) -> None:
        """ 

`SetAdditionalCaretsVisible`(*self*, *additionalCaretsVisible*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalCaretsVisible "Permalink to this definition")
Set whether additional carets are visible.



Parameters
**additionalCaretsVisible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelAlpha(self, alpha: int) -> None:
        """ 

`SetAdditionalSelAlpha`(*self*, *alpha*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalSelAlpha "Permalink to this definition")
Set the alpha of the selection.



Parameters
**alpha** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelBackground(self, back: Union[int, str, 'Colour']) -> None:
        """ 

`SetAdditionalSelBackground`(*self*, *back*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalSelBackground "Permalink to this definition")
Set the background colour of additional selections.


Must have previously called SetSelBack with non-zero first argument for this to have an effect.



Parameters
**back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelForeground(self, fore: Union[int, str, 'Colour']) -> None:
        """ 

`SetAdditionalSelForeground`(*self*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalSelForeground "Permalink to this definition")
Set the foreground colour of additional selections.


Must have previously called SetSelFore with non-zero first argument for this to have an effect.



Parameters
**fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAdditionalSelectionTyping(self, additionalSelectionTyping: bool) -> None:
        """ 

`SetAdditionalSelectionTyping`(*self*, *additionalSelectionTyping*)[¶](#wx.stc.StyledTextCtrl.SetAdditionalSelectionTyping "Permalink to this definition")
Set whether typing can be performed into multiple selections.



Parameters
**additionalSelectionTyping** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAnchor(self, anchor: int) -> None:
        """ 

`SetAnchor`(*self*, *anchor*)[¶](#wx.stc.StyledTextCtrl.SetAnchor "Permalink to this definition")
Set the selection anchor to a position.


The anchor is the opposite end of the selection from the caret.



Parameters
**anchor** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetAutomaticFold(self, automaticFold: int) -> None:
        """ 

`SetAutomaticFold`(*self*, *automaticFold*)[¶](#wx.stc.StyledTextCtrl.SetAutomaticFold "Permalink to this definition")
Set automatic folding behaviours.


The input should be a bit list containing one or more of the [``](#id109)STC\_AUTOMATICFOLD\_\* `` constants.



Parameters
**automaticFold** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetBackSpaceUnIndents(self, bsUnIndents: bool) -> None:
        """ 

`SetBackSpaceUnIndents`(*self*, *bsUnIndents*)[¶](#wx.stc.StyledTextCtrl.SetBackSpaceUnIndents "Permalink to this definition")
Sets whether a backspace pressed when caret is within indentation unindents.



Parameters
**bsUnIndents** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetBufferedDraw(self, buffered: bool) -> None:
        """ 

`SetBufferedDraw`(*self*, *buffered*)[¶](#wx.stc.StyledTextCtrl.SetBufferedDraw "Permalink to this definition")
If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker.



Parameters
**buffered** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretForeground(self, fore: Union[int, str, 'Colour']) -> None:
        """ 

`SetCaretForeground`(*self*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetCaretForeground "Permalink to this definition")
Set the foreground colour of the caret.



Parameters
**fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineBackAlpha(self, alpha: int) -> None:
        """ 

`SetCaretLineBackAlpha`(*self*, *alpha*)[¶](#wx.stc.StyledTextCtrl.SetCaretLineBackAlpha "Permalink to this definition")
Set background alpha of the caret line.



Parameters
**alpha** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineBackground(self, back: Union[int, str, 'Colour']) -> None:
        """ 

`SetCaretLineBackground`(*self*, *back*)[¶](#wx.stc.StyledTextCtrl.SetCaretLineBackground "Permalink to this definition")
Set the colour of the background of the line containing the caret.



Parameters
**back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineVisible(self, show: bool) -> None:
        """ 

`SetCaretLineVisible`(*self*, *show*)[¶](#wx.stc.StyledTextCtrl.SetCaretLineVisible "Permalink to this definition")
Display the background of the line containing the caret in a different colour.



Parameters
**show** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretLineVisibleAlways(self, alwaysVisible: bool) -> None:
        """ 

`SetCaretLineVisibleAlways`(*self*, *alwaysVisible*)[¶](#wx.stc.StyledTextCtrl.SetCaretLineVisibleAlways "Permalink to this definition")
Sets the caret line to always visible.



Parameters
**alwaysVisible** (*bool*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretPeriod(self, periodMilliseconds: int) -> None:
        """ 

`SetCaretPeriod`(*self*, *periodMilliseconds*)[¶](#wx.stc.StyledTextCtrl.SetCaretPeriod "Permalink to this definition")
Get the time in milliseconds that the caret is on and off.


0 = steady on.



Parameters
**periodMilliseconds** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretSticky(self, useCaretStickyBehaviour: int) -> None:
        """ 

`SetCaretSticky`(*self*, *useCaretStickyBehaviour*)[¶](#wx.stc.StyledTextCtrl.SetCaretSticky "Permalink to this definition")
Stop the caret preferred x position changing when the user types.


The input should be one of the [``](#id111)STC\_CARETSTICKY\_\* `` constants.



Parameters
**useCaretStickyBehaviour** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretStyle(self, caretStyle: int) -> None:
        """ 

`SetCaretStyle`(*self*, *caretStyle*)[¶](#wx.stc.StyledTextCtrl.SetCaretStyle "Permalink to this definition")
Set the style of the caret to be drawn.


The input should be one of the [``](#id113)STC\_CARETSTYLE\_\* `` constants.



Parameters
**caretStyle** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCaretWidth(self, pixelWidth: int) -> None:
        """ 

`SetCaretWidth`(*self*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.SetCaretWidth "Permalink to this definition")
Set the width of the insert mode caret.



Parameters
**pixelWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCharsDefault(self) -> None:
        """ 

`SetCharsDefault`(*self*)[¶](#wx.stc.StyledTextCtrl.SetCharsDefault "Permalink to this definition")
Reset the set of characters for whitespace and word characters to the defaults.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCodePage(self, codePage: int) -> None:
        """ 

`SetCodePage`(*self*, *codePage*)[¶](#wx.stc.StyledTextCtrl.SetCodePage "Permalink to this definition")
Set the code page used to interpret the bytes of the document as characters.



Parameters
**codePage** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetControlCharSymbol(self, symbol: int) -> None:
        """ 

`SetControlCharSymbol`(*self*, *symbol*)[¶](#wx.stc.StyledTextCtrl.SetControlCharSymbol "Permalink to this definition")
Change the way control characters are displayed: If symbol is < 32, keep the drawn way, else, use the given character.



Parameters
**symbol** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetCurrentPos(self, caret: int) -> None:
        """ 

`SetCurrentPos`(*self*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetCurrentPos "Permalink to this definition")
Sets the position of the caret.



Parameters
**caret** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetDefaultStyle(self, style: 'TextAttr') -> bool:
        """ 

`SetDefaultStyle`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.SetDefaultStyle "Permalink to this definition")
This method is inherited from TextAreaBase but is not implemented in  [wx.stc.StyledTextCtrl](#wx-stc-styledtextctrl).



Parameters
**style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetDocPointer(self, docPointer: Any) -> None:
        """ 

`SetDocPointer`(*self*, *docPointer*)[¶](#wx.stc.StyledTextCtrl.SetDocPointer "Permalink to this definition")
Change the document object used.



Parameters
**docPointer** – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEOLMode(self, eolMode: int) -> None:
        """ 

`SetEOLMode`(*self*, *eolMode*)[¶](#wx.stc.StyledTextCtrl.SetEOLMode "Permalink to this definition")
Set the current end of line mode.


The input should be one of the [``](#id115)STC\_EOL\_\* `` constants.



Parameters
**eolMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeColour(self, edgeColour: Union[int, str, 'Colour']) -> None:
        """ 

`SetEdgeColour`(*self*, *edgeColour*)[¶](#wx.stc.StyledTextCtrl.SetEdgeColour "Permalink to this definition")
Change the colour used in edge indication.



Parameters
**edgeColour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeColumn(self, column: int) -> None:
        """ 

`SetEdgeColumn`(*self*, *column*)[¶](#wx.stc.StyledTextCtrl.SetEdgeColumn "Permalink to this definition")
Set the column number of the edge.


If text goes past the edge then it is highlighted.



Parameters
**column** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEdgeMode(self, edgeMode: int) -> None:
        """ 

`SetEdgeMode`(*self*, *edgeMode*)[¶](#wx.stc.StyledTextCtrl.SetEdgeMode "Permalink to this definition")
The edge may be displayed by a line (wxSTC\_EDGE\_LINE/wxSTC\_EDGE\_MULTILINE) or by highlighting text that goes beyond it (wx``wx.stc.STC\_EDGE\_BACKGROUND``) or not displayed at all (wx``wx.stc.STC\_EDGE\_NONE``).


The input should be one of the [``](#id117)STC\_EDGE\_\* `` constants.



Parameters
**edgeMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEditable(self, editable: bool) -> None:
        """ 

`SetEditable`(*self*, *editable*)[¶](#wx.stc.StyledTextCtrl.SetEditable "Permalink to this definition")
Makes the text item editable or read-only, overriding the `wx.TE_READONLY` flag.



Parameters
**editable** (*bool*) – If `True`, the control is editable. If `False`, the control is read-only.





See also


[`IsEditable`](#wx.stc.StyledTextCtrl.IsEditable "wx.stc.StyledTextCtrl.IsEditable")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEmptySelection(self, caret: int) -> None:
        """ 

`SetEmptySelection`(*self*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetEmptySelection "Permalink to this definition")
Set caret to a position, while removing any existing selection.



Parameters
**caret** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetEndAtLastLine(self, endAtLastLine: bool) -> None:
        """ 

`SetEndAtLastLine`(*self*, *endAtLastLine*)[¶](#wx.stc.StyledTextCtrl.SetEndAtLastLine "Permalink to this definition")
Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default).


Setting this to `False` allows scrolling one page below the last line.



Parameters
**endAtLastLine** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetExtraAscent(self, extraAscent: int) -> None:
        """ 

`SetExtraAscent`(*self*, *extraAscent*)[¶](#wx.stc.StyledTextCtrl.SetExtraAscent "Permalink to this definition")
Set extra ascent for each line.



Parameters
**extraAscent** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetExtraDescent(self, extraDescent: int) -> None:
        """ 

`SetExtraDescent`(*self*, *extraDescent*)[¶](#wx.stc.StyledTextCtrl.SetExtraDescent "Permalink to this definition")
Set extra descent for each line.



Parameters
**extraDescent** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFirstVisibleLine(self, displayLine: int) -> None:
        """ 

`SetFirstVisibleLine`(*self*, *displayLine*)[¶](#wx.stc.StyledTextCtrl.SetFirstVisibleLine "Permalink to this definition")
Scroll so that a display line is at the top of the display.



Parameters
**displayLine** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldExpanded(self, line, expanded) -> None:
        """ 

`SetFoldExpanded`(*self*, *line*, *expanded*)[¶](#wx.stc.StyledTextCtrl.SetFoldExpanded "Permalink to this definition")
Show the children of a header line.



Parameters
* **line** (*int*) –
* **expanded** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldFlags(self, flags: int) -> None:
        """ 

`SetFoldFlags`(*self*, *flags*)[¶](#wx.stc.StyledTextCtrl.SetFoldFlags "Permalink to this definition")
Set some style options for folding.


The second argument should be a bit list containing one or more of the [``](#id119)STC\_FOLDFLAG\_\* `` constants.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldLevel(self, line, level) -> None:
        """ 

`SetFoldLevel`(*self*, *line*, *level*)[¶](#wx.stc.StyledTextCtrl.SetFoldLevel "Permalink to this definition")
Set the fold level of a line.


This encodes an integer level along with flags indicating whether the line is a header and whether it is effectively white space.



Parameters
* **line** (*int*) –
* **level** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldMarginColour(self, useSetting, back) -> None:
        """ 

`SetFoldMarginColour`(*self*, *useSetting*, *back*)[¶](#wx.stc.StyledTextCtrl.SetFoldMarginColour "Permalink to this definition")
Set one of the colours used as a chequerboard pattern in the fold margin.



Parameters
* **useSetting** (*bool*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFoldMarginHiColour(self, useSetting, fore) -> None:
        """ 

`SetFoldMarginHiColour`(*self*, *useSetting*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetFoldMarginHiColour "Permalink to this definition")
Set the other colour used as a chequerboard pattern in the fold margin.



Parameters
* **useSetting** (*bool*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetFontQuality(self, fontQuality: int) -> None:
        """ 

`SetFontQuality`(*self*, *fontQuality*)[¶](#wx.stc.StyledTextCtrl.SetFontQuality "Permalink to this definition")
Choose the quality level for text.


The input should be one of the [``](#id121)STC\_EFF\_QUALITY\_\* `` constants.



Parameters
**fontQuality** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.




Note


This method only has any effect with the wxMSW port and when technology has been set to `wx.stc.STC_TECHNOLOGY_DIRECTWRITE`.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHScrollBar(self, bar: 'ScrollBar') -> None:
        """ 

`SetHScrollBar`(*self*, *bar*)[¶](#wx.stc.StyledTextCtrl.SetHScrollBar "Permalink to this definition")
Set the horizontal scrollbar to use instead of the one that’s built-in.



Parameters
**bar** ([*wx.ScrollBar*](wx.ScrollBar.html#wx.ScrollBar "wx.ScrollBar")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHighlightGuide(self, column: int) -> None:
        """ 

`SetHighlightGuide`(*self*, *column*)[¶](#wx.stc.StyledTextCtrl.SetHighlightGuide "Permalink to this definition")
Set the highlighted indentation guide column.


0 = no highlighted guide.



Parameters
**column** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHint(self, hint: str) -> bool:
        """ 

`SetHint`(*self*, *hint*)[¶](#wx.stc.StyledTextCtrl.SetHint "Permalink to this definition")
Sets a hint shown in an empty unfocused text control.


The hints are usually used to indicate to the user what is supposed to be entered into the given entry field, e.g. a common use of them is to show an explanation of what can be entered in a  [wx.SearchCtrl](wx.SearchCtrl.html#wx-searchctrl).


The hint is shown (usually greyed out) for an empty control until it gets focus and is shown again if the control loses it and remains empty. It won’t be shown once the control has a non-empty value, although it will be shown again if the control contents is cleared. Because of this, it generally only makes sense to use hints with the controls which are initially empty.


Notice that hints are known as *cue banners* under MSW or *placeholder strings* under macOS.


For the platforms without native hints support, the implementation has several known limitations. Notably, the hint display will not be properly updated if you change  [wx.TextEntry](wx.TextEntry.html#wx-textentry) contents programmatically when the hint is displayed using methods other than [`SetValue`](#wx.stc.StyledTextCtrl.SetValue "wx.stc.StyledTextCtrl.SetValue") or [`ChangeValue`](#wx.stc.StyledTextCtrl.ChangeValue "wx.stc.StyledTextCtrl.ChangeValue") or others which use them internally (e.g. [`Clear`](#wx.stc.StyledTextCtrl.Clear "wx.stc.StyledTextCtrl.Clear") ). In other words, currently you should avoid calling methods such as [`WriteText`](#wx.stc.StyledTextCtrl.WriteText "wx.stc.StyledTextCtrl.WriteText") or [`Replace`](#wx.stc.StyledTextCtrl.Replace "wx.stc.StyledTextCtrl.Replace") when using hints and the text control is empty. If you bind to the control’s focus and wxEVT\_TEXT events, you must call [`wx.Event.Skip`](wx.Event.html#wx.Event.Skip "wx.Event.Skip") on them so that the generic implementation works correctly.


Another limitation is that hints are ignored for the controls with `TE_PASSWORD` style.



Parameters
**hint** (*string*) – 



Return type
*bool*





New in version 2.9.0.




Note


Currently implemented natively on Windows (Vista and later only), macOS and GTK+ (3.2 and later).




Note


Hints can be used for single line text controls under all platforms, but only MSW and GTK+ 2 support them for multi-line text controls, they are ignored for them under the other platforms.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveBackground(self, useSetting, back) -> None:
        """ 

`SetHotspotActiveBackground`(*self*, *useSetting*, *back*)[¶](#wx.stc.StyledTextCtrl.SetHotspotActiveBackground "Permalink to this definition")
Set a back colour for active hotspots.



Parameters
* **useSetting** (*bool*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveForeground(self, useSetting, fore) -> None:
        """ 

`SetHotspotActiveForeground`(*self*, *useSetting*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetHotspotActiveForeground "Permalink to this definition")
Set a fore colour for active hotspots.



Parameters
* **useSetting** (*bool*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotActiveUnderline(self, underline: bool) -> None:
        """ 

`SetHotspotActiveUnderline`(*self*, *underline*)[¶](#wx.stc.StyledTextCtrl.SetHotspotActiveUnderline "Permalink to this definition")
Enable / Disable underlining active hotspots.



Parameters
**underline** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetHotspotSingleLine(self, singleLine: bool) -> None:
        """ 

`SetHotspotSingleLine`(*self*, *singleLine*)[¶](#wx.stc.StyledTextCtrl.SetHotspotSingleLine "Permalink to this definition")
Limit hotspots to single line so hotspots on two lines don’t merge.



Parameters
**singleLine** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIMEInteraction(self, imeInteraction: int) -> None:
        """ 

`SetIMEInteraction`(*self*, *imeInteraction*)[¶](#wx.stc.StyledTextCtrl.SetIMEInteraction "Permalink to this definition")
Choose to display the `IME` in a winow or inline.


The input should be one of the [``](#id123)STC\_IME\_\* `` constants.



Parameters
**imeInteraction** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdentifier(self, identifier: int) -> None:
        """ 

`SetIdentifier`(*self*, *identifier*)[¶](#wx.stc.StyledTextCtrl.SetIdentifier "Permalink to this definition")
Set the identifier reported as idFrom in notification messages.



Parameters
**identifier** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdentifiers(self, style, identifiers) -> None:
        """ 

`SetIdentifiers`(*self*, *style*, *identifiers*)[¶](#wx.stc.StyledTextCtrl.SetIdentifiers "Permalink to this definition")
Set the identifiers that are shown in a particular style.



Parameters
* **style** (*int*) –
* **identifiers** (*string*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIdleStyling(self, idleStyling: int) -> None:
        """ 

`SetIdleStyling`(*self*, *idleStyling*)[¶](#wx.stc.StyledTextCtrl.SetIdleStyling "Permalink to this definition")
Sets limits to idle styling.


The input should be one of the [``](#id125)STC\_IDLESTYLING\_\* `` constants.



Parameters
**idleStyling** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndent(self, indentSize: int) -> None:
        """ 

`SetIndent`(*self*, *indentSize*)[¶](#wx.stc.StyledTextCtrl.SetIndent "Permalink to this definition")
Set the number of spaces used for one level of indentation.



Parameters
**indentSize** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndentationGuides(self, indentView: int) -> None:
        """ 

`SetIndentationGuides`(*self*, *indentView*)[¶](#wx.stc.StyledTextCtrl.SetIndentationGuides "Permalink to this definition")
Show or hide indentation guides.


The input should be one of the [``](#id127)STC\_IV\_\* `` constants.



Parameters
**indentView** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndicatorCurrent(self, indicator: int) -> None:
        """ 

`SetIndicatorCurrent`(*self*, *indicator*)[¶](#wx.stc.StyledTextCtrl.SetIndicatorCurrent "Permalink to this definition")
Set the indicator used for IndicatorFillRange and IndicatorClearRange.



Parameters
**indicator** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetIndicatorValue(self, value: int) -> None:
        """ 

`SetIndicatorValue`(*self*, *value*)[¶](#wx.stc.StyledTextCtrl.SetIndicatorValue "Permalink to this definition")
Set the value used for IndicatorFillRange.



Parameters
**value** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetInsertionPoint(self, pos: int) -> None:
        """ 

`SetInsertionPoint`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.SetInsertionPoint "Permalink to this definition")
Sets the insertion point at the given position.



Parameters
**pos** (*long*) – Position to set, in the range from 0 to [`GetLastPosition`](#wx.stc.StyledTextCtrl.GetLastPosition "wx.stc.StyledTextCtrl.GetLastPosition") inclusive.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetInsertionPointEnd(self) -> None:
        """ 

`SetInsertionPointEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.SetInsertionPointEnd "Permalink to this definition")
Sets the insertion point at the end of the text control.


This is equivalent to calling [`wx.TextCtrl.SetInsertionPoint`](wx.TextEntry.html#wx.TextEntry.SetInsertionPoint "wx.TextEntry.SetInsertionPoint") with [`wx.TextCtrl.GetLastPosition`](wx.TextEntry.html#wx.TextEntry.GetLastPosition "wx.TextEntry.GetLastPosition") argument.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetKeyWords(self, keyWordSet, keyWords) -> None:
        """ 

`SetKeyWords`(*self*, *keyWordSet*, *keyWords*)[¶](#wx.stc.StyledTextCtrl.SetKeyWords "Permalink to this definition")
Set up the key words used by the lexer.



Parameters
* **keyWordSet** (*int*) –
* **keyWords** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLastKeydownProcessed(self, val: bool) -> None:
        """ 

`SetLastKeydownProcessed`(*self*, *val*)[¶](#wx.stc.StyledTextCtrl.SetLastKeydownProcessed "Permalink to this definition")
Returns the line number of the line with the caret.



Parameters
**val** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLayoutCache(self, cacheMode: int) -> None:
        """ 

`SetLayoutCache`(*self*, *cacheMode*)[¶](#wx.stc.StyledTextCtrl.SetLayoutCache "Permalink to this definition")
Sets the degree of caching of layout information.


The input should be one of the [``](#id129)STC\_CACHE\_\* `` constants.



Parameters
**cacheMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLexer(self, lexer: int) -> None:
        """ 

`SetLexer`(*self*, *lexer*)[¶](#wx.stc.StyledTextCtrl.SetLexer "Permalink to this definition")
Set the lexing language of the document.


The input should be one of the [``](#id131)STC\_LEX\_\* `` constants.



Parameters
**lexer** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLexerLanguage(self, language: str) -> None:
        """ 

`SetLexerLanguage`(*self*, *language*)[¶](#wx.stc.StyledTextCtrl.SetLexerLanguage "Permalink to this definition")
Set the lexing language of the document based on string name.



Parameters
**language** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineEndTypesAllowed(self, lineEndBitSet: int) -> None:
        """ 

`SetLineEndTypesAllowed`(*self*, *lineEndBitSet*)[¶](#wx.stc.StyledTextCtrl.SetLineEndTypesAllowed "Permalink to this definition")
Set the line end types that the application wants to use.


May not be used if incompatible with lexer or encoding.


The input should be one of the [``](#id133)STC\_LINE\_END\_TYPE\_\* `` constants.



Parameters
**lineEndBitSet** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineIndentation(self, line, indentation) -> None:
        """ 

`SetLineIndentation`(*self*, *line*, *indentation*)[¶](#wx.stc.StyledTextCtrl.SetLineIndentation "Permalink to this definition")
Change the indentation of a line to a number of columns.



Parameters
* **line** (*int*) –
* **indentation** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetLineState(self, line, state) -> None:
        """ 

`SetLineState`(*self*, *line*, *state*)[¶](#wx.stc.StyledTextCtrl.SetLineState "Permalink to this definition")
Used to hold extra styling information for each line.



Parameters
* **line** (*int*) –
* **state** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMainSelection(self, selection: int) -> None:
        """ 

`SetMainSelection`(*self*, *selection*)[¶](#wx.stc.StyledTextCtrl.SetMainSelection "Permalink to this definition")
Set the main selection.



Parameters
**selection** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginBackground(self, margin, back) -> None:
        """ 

`SetMarginBackground`(*self*, *margin*, *back*)[¶](#wx.stc.StyledTextCtrl.SetMarginBackground "Permalink to this definition")
Set the background colour of a margin.


Only visible for `wx.stc.STC_MARGIN_COLOUR`.



Parameters
* **margin** (*int*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginCount(self, margins: int) -> None:
        """ 

`SetMarginCount`(*self*, *margins*)[¶](#wx.stc.StyledTextCtrl.SetMarginCount "Permalink to this definition")
Allocate a non-standard number of margins.



Parameters
**margins** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginCursor(self, margin, cursor) -> None:
        """ 

`SetMarginCursor`(*self*, *margin*, *cursor*)[¶](#wx.stc.StyledTextCtrl.SetMarginCursor "Permalink to this definition")
Set the cursor shown when the mouse is inside a margin.


The second argument should be one of the [``](#id135)STC\_CURSOR\* `` constants.



Parameters
* **margin** (*int*) –
* **cursor** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginLeft(self, pixelWidth: int) -> None:
        """ 

`SetMarginLeft`(*self*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.SetMarginLeft "Permalink to this definition")
Sets the size in pixels of the left margin.



Parameters
**pixelWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginMask(self, margin, mask) -> None:
        """ 

`SetMarginMask`(*self*, *margin*, *mask*)[¶](#wx.stc.StyledTextCtrl.SetMarginMask "Permalink to this definition")
Set a mask that determines which markers are displayed in a margin.



Parameters
* **margin** (*int*) –
* **mask** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginOptions(self, marginOptions: int) -> None:
        """ 

`SetMarginOptions`(*self*, *marginOptions*)[¶](#wx.stc.StyledTextCtrl.SetMarginOptions "Permalink to this definition")
Set the margin options.


The input should be one of the [``](#id137)STC\_MARGINOPTION\_\* `` constants.



Parameters
**marginOptions** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginRight(self, pixelWidth: int) -> None:
        """ 

`SetMarginRight`(*self*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.SetMarginRight "Permalink to this definition")
Sets the size in pixels of the right margin.



Parameters
**pixelWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginSensitive(self, margin, sensitive) -> None:
        """ 

`SetMarginSensitive`(*self*, *margin*, *sensitive*)[¶](#wx.stc.StyledTextCtrl.SetMarginSensitive "Permalink to this definition")
Make a margin sensitive or insensitive to mouse clicks.



Parameters
* **margin** (*int*) –
* **sensitive** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginType(self, margin, marginType) -> None:
        """ 

`SetMarginType`(*self*, *margin*, *marginType*)[¶](#wx.stc.StyledTextCtrl.SetMarginType "Permalink to this definition")
Set a margin to be either numeric or symbolic.


The second argument should be one of the [``](#id139)STC\_MARGIN\_\* `` constants.



Parameters
* **margin** (*int*) –
* **marginType** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMarginWidth(self, margin, pixelWidth) -> None:
        """ 

`SetMarginWidth`(*self*, *margin*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.SetMarginWidth "Permalink to this definition")
Set the width of a margin to a width expressed in pixels.



Parameters
* **margin** (*int*) –
* **pixelWidth** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMargins(self, left, right) -> None:
        """ 

`SetMargins`(*self*, *left*, *right*)[¶](#wx.stc.StyledTextCtrl.SetMargins "Permalink to this definition")
Set the left and right margin in the edit area, measured in pixels.



Parameters
* **left** (*int*) –
* **right** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMaxLength(self, len: int) -> None:
        """ 

`SetMaxLength`(*self*, *len*)[¶](#wx.stc.StyledTextCtrl.SetMaxLength "Permalink to this definition")
This function sets the maximum number of characters the user can enter into the control.


In other words, it allows limiting the text value length to *len* not counting the terminating `NUL` character.


If *len* is 0, the previously set max length limit, if any, is discarded and the user may enter as much text as the underlying native text control widget supports (typically at least 32Kb). If the user tries to enter more characters into the text control when it already is filled up to the maximal length, a `wxEVT_TEXT_MAXLEN` event is sent to notify the program about it (giving it the possibility to show an explanatory message, for example) and the extra input is discarded.


Note that in wxGTK this function may only be used with single line text controls.



Parameters
**len** (*long*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetModEventMask(self, eventMask: int) -> None:
        """ 

`SetModEventMask`(*self*, *eventMask*)[¶](#wx.stc.StyledTextCtrl.SetModEventMask "Permalink to this definition")
Set which document modification events are sent to the container.


The input should be a bit list containing one or more of the `STC_MOD_* ``   constants, the ``STC_PERFORMED_* ``   constants, ``wx.stc.STC_STARTACTION`, `wx.stc.STC_MULTILINEUNDOREDO`, `wx.stc.STC_MULTISTEPUNDOREDO`, and `wx.stc.STC_LASTSTEPINUNDOREDO`. The input can also be `wx.stc.STC_MODEVENTMASKALL` to indicate that all changes should generate events.



Parameters
**eventMask** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetModified(self, modified: bool) -> None:
        """ 

`SetModified`(*self*, *modified*)[¶](#wx.stc.StyledTextCtrl.SetModified "Permalink to this definition")
Marks the control as being modified by the user or not.



Parameters
**modified** (*bool*) – 





See also


[`MarkDirty`](#wx.stc.StyledTextCtrl.MarkDirty "wx.stc.StyledTextCtrl.MarkDirty") , [`DiscardEdits`](#wx.stc.StyledTextCtrl.DiscardEdits "wx.stc.StyledTextCtrl.DiscardEdits")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseDownCaptures(self, captures: bool) -> None:
        """ 

`SetMouseDownCaptures`(*self*, *captures*)[¶](#wx.stc.StyledTextCtrl.SetMouseDownCaptures "Permalink to this definition")
Set whether the mouse is captured when its button is pressed.



Parameters
**captures** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseDwellTime(self, periodMilliseconds: int) -> None:
        """ 

`SetMouseDwellTime`(*self*, *periodMilliseconds*)[¶](#wx.stc.StyledTextCtrl.SetMouseDwellTime "Permalink to this definition")
Sets the time the mouse must sit still to generate a mouse dwell event.


The input should be a time in milliseconds or `wx.stc.STC_TIME_FOREVER`.



Parameters
**periodMilliseconds** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseSelectionRectangularSwitch(self, mouseSelectionRectangularSwitch: bool) -> None:
        """ 

`SetMouseSelectionRectangularSwitch`(*self*, *mouseSelectionRectangularSwitch*)[¶](#wx.stc.StyledTextCtrl.SetMouseSelectionRectangularSwitch "Permalink to this definition")
Set whether switching to rectangular mode while selecting with the mouse is allowed.



Parameters
**mouseSelectionRectangularSwitch** (*bool*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMouseWheelCaptures(self, captures: bool) -> None:
        """ 

`SetMouseWheelCaptures`(*self*, *captures*)[¶](#wx.stc.StyledTextCtrl.SetMouseWheelCaptures "Permalink to this definition")
Set whether the mouse wheel can be active outside the window.



Parameters
**captures** (*bool*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMultiPaste(self, multiPaste: int) -> None:
        """ 

`SetMultiPaste`(*self*, *multiPaste*)[¶](#wx.stc.StyledTextCtrl.SetMultiPaste "Permalink to this definition")
Change the effect of pasting when there are multiple selections.


The input should be one of the [``](#id141)STC\_MULTIPASTE\_\* `` constants.



Parameters
**multiPaste** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetMultipleSelection(self, multipleSelection: bool) -> None:
        """ 

`SetMultipleSelection`(*self*, *multipleSelection*)[¶](#wx.stc.StyledTextCtrl.SetMultipleSelection "Permalink to this definition")
Set whether multiple selections can be made.



Parameters
**multipleSelection** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetOvertype(self, overType: bool) -> None:
        """ 

`SetOvertype`(*self*, *overType*)[¶](#wx.stc.StyledTextCtrl.SetOvertype "Permalink to this definition")
Set to overtype (`True`) or insert mode.



Parameters
**overType** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPasteConvertEndings(self, convert: bool) -> None:
        """ 

`SetPasteConvertEndings`(*self*, *convert*)[¶](#wx.stc.StyledTextCtrl.SetPasteConvertEndings "Permalink to this definition")
Enable/Disable convert-on-paste for line endings.



Parameters
**convert** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPhasesDraw(self, phases: int) -> None:
        """ 

`SetPhasesDraw`(*self*, *phases*)[¶](#wx.stc.StyledTextCtrl.SetPhasesDraw "Permalink to this definition")
In one phase draw, text is drawn in a series of rectangular blocks with no overlap.


In two phase draw, text is drawn in a series of lines allowing runs to overlap horizontally. In multiple phase draw, each element is drawn over the whole drawing area, allowing text to overlap from one line to the next.


The input should be one of the [``](#id143)STC\_PHASES\_\* `` constants.



Parameters
**phases** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPositionCacheSize(self, size: int) -> None:
        """ 

`SetPositionCacheSize`(*self*, *size*)[¶](#wx.stc.StyledTextCtrl.SetPositionCacheSize "Permalink to this definition")
Set number of entries in position cache.



Parameters
**size** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintColourMode(self, mode: int) -> None:
        """ 

`SetPrintColourMode`(*self*, *mode*)[¶](#wx.stc.StyledTextCtrl.SetPrintColourMode "Permalink to this definition")
Modify colours when printing for clearer printed text.


The input should be one of the [``](#id145)STC\_PRINT\_\* `` constants.



Parameters
**mode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintMagnification(self, magnification: int) -> None:
        """ 

`SetPrintMagnification`(*self*, *magnification*)[¶](#wx.stc.StyledTextCtrl.SetPrintMagnification "Permalink to this definition")
Sets the print magnification added to the point size of each style for printing.



Parameters
**magnification** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPrintWrapMode(self, wrapMode: int) -> None:
        """ 

`SetPrintWrapMode`(*self*, *wrapMode*)[¶](#wx.stc.StyledTextCtrl.SetPrintWrapMode "Permalink to this definition")
Set printing to line wrapped (wx``wx.stc.STC\_WRAP\_WORD``) or not line wrapped (wx``wx.stc.STC\_WRAP\_NONE``).



Parameters
**wrapMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetProperty(self, key, value) -> None:
        """ 

`SetProperty`(*self*, *key*, *value*)[¶](#wx.stc.StyledTextCtrl.SetProperty "Permalink to this definition")
Set up a value that may be used by a lexer for some optional feature.



Parameters
* **key** (*string*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetPunctuationChars(self, characters: str) -> None:
        """ 

`SetPunctuationChars`(*self*, *characters*)[¶](#wx.stc.StyledTextCtrl.SetPunctuationChars "Permalink to this definition")
Set the set of characters making up punctuation characters Should be called after SetWordChars.



Parameters
**characters** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetReadOnly(self, readOnly: bool) -> None:
        """ 

`SetReadOnly`(*self*, *readOnly*)[¶](#wx.stc.StyledTextCtrl.SetReadOnly "Permalink to this definition")
Set to read only or read write.



Parameters
**readOnly** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionAnchor(self, anchor: int) -> None:
        """ 

`SetRectangularSelectionAnchor`(*self*, *anchor*)[¶](#wx.stc.StyledTextCtrl.SetRectangularSelectionAnchor "Permalink to this definition")
Set the anchor position of the rectangular selection.



Parameters
**anchor** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionAnchorVirtualSpace(self, space: int) -> None:
        """ 

`SetRectangularSelectionAnchorVirtualSpace`(*self*, *space*)[¶](#wx.stc.StyledTextCtrl.SetRectangularSelectionAnchorVirtualSpace "Permalink to this definition")
Set the virtual space of the anchor of the rectangular selection.



Parameters
**space** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionCaret(self, caret: int) -> None:
        """ 

`SetRectangularSelectionCaret`(*self*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetRectangularSelectionCaret "Permalink to this definition")
Set the caret position of the rectangular selection.



Parameters
**caret** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionCaretVirtualSpace(self, space: int) -> None:
        """ 

`SetRectangularSelectionCaretVirtualSpace`(*self*, *space*)[¶](#wx.stc.StyledTextCtrl.SetRectangularSelectionCaretVirtualSpace "Permalink to this definition")
Set the virtual space of the caret of the rectangular selection.



Parameters
**space** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRectangularSelectionModifier(self, modifier: int) -> None:
        """ 

`SetRectangularSelectionModifier`(*self*, *modifier*)[¶](#wx.stc.StyledTextCtrl.SetRectangularSelectionModifier "Permalink to this definition")
On GTK+, allow selecting the modifier key to use for mouse-based rectangular selection.


Often the window manager requires Alt+Mouse Drag for moving windows. Valid values are `wx.stc.STC_KEYMOD_CTRL` (default), `wx.stc.STC_KEYMOD_ALT`, or `wx.stc.STC_KEYMOD_SUPER`.



Parameters
**modifier** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetRepresentation(self, encodedCharacter, representation) -> None:
        """ 

`SetRepresentation`(*self*, *encodedCharacter*, *representation*)[¶](#wx.stc.StyledTextCtrl.SetRepresentation "Permalink to this definition")
Set the way a character is drawn.



Parameters
* **encodedCharacter** (*string*) –
* **representation** (*string*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSTCCursor(self, cursorType: int) -> None:
        """ 

`SetSTCCursor`(*self*, *cursorType*)[¶](#wx.stc.StyledTextCtrl.SetSTCCursor "Permalink to this definition")
Sets the cursor to one of the `STC_CURSOR` values.



Parameters
**cursorType** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSTCFocus(self, focus: bool) -> None:
        """ 

`SetSTCFocus`(*self*, *focus*)[¶](#wx.stc.StyledTextCtrl.SetSTCFocus "Permalink to this definition")
Change internal focus flag.



Parameters
**focus** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSavePoint(self) -> None:
        """ 

`SetSavePoint`(*self*)[¶](#wx.stc.StyledTextCtrl.SetSavePoint "Permalink to this definition")
Remember the current position in the undo history as the position at which the document was saved.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetScrollWidth(self, pixelWidth: int) -> None:
        """ 

`SetScrollWidth`(*self*, *pixelWidth*)[¶](#wx.stc.StyledTextCtrl.SetScrollWidth "Permalink to this definition")
Sets the document width assumed for scrolling.



Parameters
**pixelWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetScrollWidthTracking(self, tracking: bool) -> None:
        """ 

`SetScrollWidthTracking`(*self*, *tracking*)[¶](#wx.stc.StyledTextCtrl.SetScrollWidthTracking "Permalink to this definition")
Sets whether the maximum width line displayed is used to set scroll width.



Parameters
**tracking** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSearchFlags(self, searchFlags: int) -> None:
        """ 

`SetSearchFlags`(*self*, *searchFlags*)[¶](#wx.stc.StyledTextCtrl.SetSearchFlags "Permalink to this definition")
Set the search flags used by SearchInTarget.


The input should be a bit list containing one or more of the [``](#id147)STC\_FIND\_\* `` constants.



Parameters
**searchFlags** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelAlpha(self, alpha: int) -> None:
        """ 

`SetSelAlpha`(*self*, *alpha*)[¶](#wx.stc.StyledTextCtrl.SetSelAlpha "Permalink to this definition")
Set the alpha of the selection.



Parameters
**alpha** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelBackground(self, useSetting, back) -> None:
        """ 

`SetSelBackground`(*self*, *useSetting*, *back*)[¶](#wx.stc.StyledTextCtrl.SetSelBackground "Permalink to this definition")
Set the background colour of the main and additional selections and whether to use this setting.



Parameters
* **useSetting** (*bool*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelEOLFilled(self, filled: bool) -> None:
        """ 

`SetSelEOLFilled`(*self*, *filled*)[¶](#wx.stc.StyledTextCtrl.SetSelEOLFilled "Permalink to this definition")
Set the selection to have its end of line filled or not.



Parameters
**filled** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelForeground(self, useSetting, fore) -> None:
        """ 

`SetSelForeground`(*self*, *useSetting*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetSelForeground "Permalink to this definition")
Set the foreground colour of the main and additional selections and whether to use this setting.



Parameters
* **useSetting** (*bool*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelection(self, from_, to_) -> None:
        """ 

`SetSelection`(*self*, *from\_*, *to\_*)[¶](#wx.stc.StyledTextCtrl.SetSelection "Permalink to this definition")
Selects the text starting at the first position up to (but not including) the character at the last position.


If both parameters are equal to -1 all text in the control is selected.


Notice that the insertion point will be moved to *from* by this function.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –




The first position.


The last position.



See also


[`SelectAll`](#wx.stc.StyledTextCtrl.SelectAll "wx.stc.StyledTextCtrl.SelectAll")





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionEnd(self, caret: int) -> None:
        """ 

`SetSelectionEnd`(*self*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetSelectionEnd "Permalink to this definition")
Sets the position that ends the selection - this becomes the caret.



Parameters
**caret** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionMode(self, selectionMode: int) -> None:
        """ 

`SetSelectionMode`(*self*, *selectionMode*)[¶](#wx.stc.StyledTextCtrl.SetSelectionMode "Permalink to this definition")
Set the selection mode to stream (wx``wx.stc.STC\_SEL\_STREAM``) or rectangular (wxSTC\_SEL\_RECTANGLE/wxSTC\_SEL\_THIN) or by lines (wx``wx.stc.STC\_SEL\_LINES``).



Parameters
**selectionMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNAnchor(self, selection, anchor) -> None:
        """ 

`SetSelectionNAnchor`(*self*, *selection*, *anchor*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNAnchor "Permalink to this definition")
Set the anchor position of the nth selection.



Parameters
* **selection** (*int*) –
* **anchor** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNAnchorVirtualSpace(self, selection, space) -> None:
        """ 

`SetSelectionNAnchorVirtualSpace`(*self*, *selection*, *space*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNAnchorVirtualSpace "Permalink to this definition")
Set the virtual space of the anchor of the nth selection.



Parameters
* **selection** (*int*) –
* **space** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNCaret(self, selection, caret) -> None:
        """ 

`SetSelectionNCaret`(*self*, *selection*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNCaret "Permalink to this definition")
Set the caret position of the nth selection.



Parameters
* **selection** (*int*) –
* **caret** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNCaretVirtualSpace(self, selection, space) -> None:
        """ 

`SetSelectionNCaretVirtualSpace`(*self*, *selection*, *space*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNCaretVirtualSpace "Permalink to this definition")
Set the virtual space of the caret of the nth selection.



Parameters
* **selection** (*int*) –
* **space** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNEnd(self, selection, caret) -> None:
        """ 

`SetSelectionNEnd`(*self*, *selection*, *caret*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNEnd "Permalink to this definition")
Sets the position that ends the selection - this becomes the currentPosition.



Parameters
* **selection** (*int*) –
* **caret** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionNStart(self, selection, anchor) -> None:
        """ 

`SetSelectionNStart`(*self*, *selection*, *anchor*)[¶](#wx.stc.StyledTextCtrl.SetSelectionNStart "Permalink to this definition")
Sets the position that starts the selection - this becomes the anchor.



Parameters
* **selection** (*int*) –
* **anchor** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetSelectionStart(self, anchor: int) -> None:
        """ 

`SetSelectionStart`(*self*, *anchor*)[¶](#wx.stc.StyledTextCtrl.SetSelectionStart "Permalink to this definition")
Sets the position that starts the selection - this becomes the anchor.



Parameters
**anchor** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStatus(self, status: int) -> None:
        """ 

`SetStatus`(*self*, *status*)[¶](#wx.stc.StyledTextCtrl.SetStatus "Permalink to this definition")
Change error status - 0 = `wx.OK`.


The input should be one of the [``](#id149)STC\_STATUS\_\* `` constants.



Parameters
**status** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyle(self, start, end, style) -> bool:
        """ 

`SetStyle`(*self*, *start*, *end*, *style*)[¶](#wx.stc.StyledTextCtrl.SetStyle "Permalink to this definition")
This method is inherited from TextAreaBase but is not implemented in  [wx.stc.StyledTextCtrl](#wx-stc-styledtextctrl).



Parameters
* **start** (*long*) –
* **end** (*long*) –
* **style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyleBits(self, bits: int) -> None:
        """ 

`SetStyleBits`(*self*, *bits*)[¶](#wx.stc.StyledTextCtrl.SetStyleBits "Permalink to this definition")
Divide each styling byte into lexical class bits (default: 5) and indicator bits (default: 3).


If a lexer requires more than 32 lexical states, then this is used to expand the possible states.



Parameters
**bits** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyleBytes(self, length, styleBytes) -> None:
        """ 

`SetStyleBytes`(*self*, *length*, *styleBytes*)[¶](#wx.stc.StyledTextCtrl.SetStyleBytes "Permalink to this definition")
Set the styles for a segment of the document.



Parameters
* **length** (*int*) –
* **styleBytes** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetStyling(self, length, style) -> None:
        """ 

`SetStyling`(*self*, *length*, *style*)[¶](#wx.stc.StyledTextCtrl.SetStyling "Permalink to this definition")
Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment.



Parameters
* **length** (*int*) –
* **style** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabDrawMode(self, tabDrawMode: int) -> None:
        """ 

`SetTabDrawMode`(*self*, *tabDrawMode*)[¶](#wx.stc.StyledTextCtrl.SetTabDrawMode "Permalink to this definition")
Set how tabs are drawn when visible.


The input should be one of the [``](#id151)STC\_TD\_\* `` constants.



Parameters
**tabDrawMode** (*int*) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabIndents(self, tabIndents: bool) -> None:
        """ 

`SetTabIndents`(*self*, *tabIndents*)[¶](#wx.stc.StyledTextCtrl.SetTabIndents "Permalink to this definition")
Sets whether a tab pressed when caret is within indentation indents.



Parameters
**tabIndents** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTabWidth(self, tabWidth: int) -> None:
        """ 

`SetTabWidth`(*self*, *tabWidth*)[¶](#wx.stc.StyledTextCtrl.SetTabWidth "Permalink to this definition")
Change the visible size of a tab to be a multiple of the width of a space character.



Parameters
**tabWidth** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetEnd(self, end: int) -> None:
        """ 

`SetTargetEnd`(*self*, *end*)[¶](#wx.stc.StyledTextCtrl.SetTargetEnd "Permalink to this definition")
Sets the position that ends the target which is used for updating the document without affecting the scroll position.



Parameters
**end** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetRange(self, start, end) -> None:
        """ 

`SetTargetRange`(*self*, *start*, *end*)[¶](#wx.stc.StyledTextCtrl.SetTargetRange "Permalink to this definition")
Sets both the start and end of the target in one call.



Parameters
* **start** (*int*) –
* **end** (*int*) –





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTargetStart(self, start: int) -> None:
        """ 

`SetTargetStart`(*self*, *start*)[¶](#wx.stc.StyledTextCtrl.SetTargetStart "Permalink to this definition")
Sets the position that starts the target which is used for updating the document without affecting the scroll position.



Parameters
**start** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTechnology(self, technology: int) -> None:
        """ 

`SetTechnology`(*self*, *technology*)[¶](#wx.stc.StyledTextCtrl.SetTechnology "Permalink to this definition")
Set the technology used.



Parameters
**technology** (*int*) – 





Note


For the wxMSW port, the input can be either `wx.stc.STC_TECHNOLOGY_DEFAULT` or `wx.stc.STC_TECHNOLOGY_DIRECTWRITE`. With other ports, this method has no effect.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.SetText "Permalink to this definition")
Replace the contents of the document with the argument text.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTextRaw(self, text: int) -> None:
        """ 

`SetTextRaw`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.SetTextRaw "Permalink to this definition")
Replace the contents of the document with the argument text.



Parameters
**text** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetTwoPhaseDraw(self, twoPhase: bool) -> None:
        """ 

`SetTwoPhaseDraw`(*self*, *twoPhase*)[¶](#wx.stc.StyledTextCtrl.SetTwoPhaseDraw "Permalink to this definition")
In twoPhaseDraw mode, drawing is performed in two phases, first the background and then the foreground.


This avoids chopping off characters that overlap the next run.



Parameters
**twoPhase** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUndoCollection(self, collectUndo: bool) -> None:
        """ 

`SetUndoCollection`(*self*, *collectUndo*)[¶](#wx.stc.StyledTextCtrl.SetUndoCollection "Permalink to this definition")
Choose between collecting actions into the undo history and discarding them.



Parameters
**collectUndo** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseAntiAliasing(self, useAA: bool) -> None:
        """ 

`SetUseAntiAliasing`(*self*, *useAA*)[¶](#wx.stc.StyledTextCtrl.SetUseAntiAliasing "Permalink to this definition")
Specify whether anti-aliased fonts should be used.


This will have no effect on some platforms, but on some (wxMac for example) can greatly improve performance.



Parameters
**useAA** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseHorizontalScrollBar(self, visible: bool) -> None:
        """ 

`SetUseHorizontalScrollBar`(*self*, *visible*)[¶](#wx.stc.StyledTextCtrl.SetUseHorizontalScrollBar "Permalink to this definition")
Show or hide the horizontal scroll bar.



Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseTabs(self, useTabs: bool) -> None:
        """ 

`SetUseTabs`(*self*, *useTabs*)[¶](#wx.stc.StyledTextCtrl.SetUseTabs "Permalink to this definition")
Indentation will only use space characters if useTabs is `False`, otherwise it will use a combination of tabs and spaces.



Parameters
**useTabs** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetUseVerticalScrollBar(self, visible: bool) -> None:
        """ 

`SetUseVerticalScrollBar`(*self*, *visible*)[¶](#wx.stc.StyledTextCtrl.SetUseVerticalScrollBar "Permalink to this definition")
Show or hide the vertical scroll bar.



Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVScrollBar(self, bar: 'ScrollBar') -> None:
        """ 

`SetVScrollBar`(*self*, *bar*)[¶](#wx.stc.StyledTextCtrl.SetVScrollBar "Permalink to this definition")
Set the vertical scrollbar to use instead of the one that’s built-in.



Parameters
**bar** ([*wx.ScrollBar*](wx.ScrollBar.html#wx.ScrollBar "wx.ScrollBar")) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetValue(self, value: str) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.stc.StyledTextCtrl.SetValue "Permalink to this definition")
Sets the new text control value.


It also marks the control as not-modified which means that IsModified() would return `False` immediately after the call to [`SetValue`](#wx.stc.StyledTextCtrl.SetValue "wx.stc.StyledTextCtrl.SetValue") .


The insertion point is set to the start of the control (i.e. position 0) by this function unless the control value doesn’t change at all, in which case the insertion point is left at its original position.


Note that, unlike most other functions changing the controls values, this function generates a `wxEVT_TEXT` event. To avoid this you can use [`ChangeValue`](#wx.stc.StyledTextCtrl.ChangeValue "wx.stc.StyledTextCtrl.ChangeValue") instead.



Parameters
**value** (*string*) – The new value to set. It may contain newline characters if the text control is multi-line.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetViewEOL(self, visible: bool) -> None:
        """ 

`SetViewEOL`(*self*, *visible*)[¶](#wx.stc.StyledTextCtrl.SetViewEOL "Permalink to this definition")
Make the end of line characters visible or invisible.



Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetViewWhiteSpace(self, viewWS: int) -> None:
        """ 

`SetViewWhiteSpace`(*self*, *viewWS*)[¶](#wx.stc.StyledTextCtrl.SetViewWhiteSpace "Permalink to this definition")
Make white space characters invisible, always visible or visible outside indentation.


The input should be one of the [``](#id153)STC\_WS\_\* `` constants.



Parameters
**viewWS** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVirtualSpaceOptions(self, virtualSpaceOptions: int) -> None:
        """ 

`SetVirtualSpaceOptions`(*self*, *virtualSpaceOptions*)[¶](#wx.stc.StyledTextCtrl.SetVirtualSpaceOptions "Permalink to this definition")
Set options for virtual space behaviour.


The input should be one of the [``](#id155)STC\_VS\_\* `` constants.



Parameters
**virtualSpaceOptions** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetVisiblePolicy(self, visiblePolicy, visibleSlop) -> None:
        """ 

`SetVisiblePolicy`(*self*, *visiblePolicy*, *visibleSlop*)[¶](#wx.stc.StyledTextCtrl.SetVisiblePolicy "Permalink to this definition")
Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc.


The first argument should be a bit list containing one or more of the [``](#id157)STC\_VISIBLE\_\* `` constants.



Parameters
* **visiblePolicy** (*int*) –
* **visibleSlop** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceBackground(self, useSetting, back) -> None:
        """ 

`SetWhitespaceBackground`(*self*, *useSetting*, *back*)[¶](#wx.stc.StyledTextCtrl.SetWhitespaceBackground "Permalink to this definition")
Set the background colour of all whitespace and whether to use this setting.



Parameters
* **useSetting** (*bool*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceChars(self, characters: str) -> None:
        """ 

`SetWhitespaceChars`(*self*, *characters*)[¶](#wx.stc.StyledTextCtrl.SetWhitespaceChars "Permalink to this definition")
Set the set of characters making up whitespace for when moving or selecting by word.


Should be called after SetWordChars.



Parameters
**characters** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceForeground(self, useSetting, fore) -> None:
        """ 

`SetWhitespaceForeground`(*self*, *useSetting*, *fore*)[¶](#wx.stc.StyledTextCtrl.SetWhitespaceForeground "Permalink to this definition")
Set the foreground colour of all whitespace and whether to use this setting.



Parameters
* **useSetting** (*bool*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWhitespaceSize(self, size: int) -> None:
        """ 

`SetWhitespaceSize`(*self*, *size*)[¶](#wx.stc.StyledTextCtrl.SetWhitespaceSize "Permalink to this definition")
Set the size of the dots used to mark space characters.



Parameters
**size** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWordChars(self, characters: str) -> None:
        """ 

`SetWordChars`(*self*, *characters*)[¶](#wx.stc.StyledTextCtrl.SetWordChars "Permalink to this definition")
Set the set of characters making up words for when moving or selecting by word.


First sets defaults like SetCharsDefault.



Parameters
**characters** (*string*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapIndentMode(self, wrapIndentMode: int) -> None:
        """ 

`SetWrapIndentMode`(*self*, *wrapIndentMode*)[¶](#wx.stc.StyledTextCtrl.SetWrapIndentMode "Permalink to this definition")
Sets how wrapped sublines are placed.


Default is `wx.stc.STC_WRAPINDENT_FIXED`.


The input should be one of the [``](#id159)STC\_WRAPINDENT\_\* `` constants.



Parameters
**wrapIndentMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapMode(self, wrapMode: int) -> None:
        """ 

`SetWrapMode`(*self*, *wrapMode*)[¶](#wx.stc.StyledTextCtrl.SetWrapMode "Permalink to this definition")
Sets whether text is word wrapped.


The input should be one of the [``](#id161)STC\_WRAP\_\* `` constants.



Parameters
**wrapMode** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapStartIndent(self, indent: int) -> None:
        """ 

`SetWrapStartIndent`(*self*, *indent*)[¶](#wx.stc.StyledTextCtrl.SetWrapStartIndent "Permalink to this definition")
Set the start indent for wrapped lines.



Parameters
**indent** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapVisualFlags(self, wrapVisualFlags: int) -> None:
        """ 

`SetWrapVisualFlags`(*self*, *wrapVisualFlags*)[¶](#wx.stc.StyledTextCtrl.SetWrapVisualFlags "Permalink to this definition")
Set the display mode of visual flags for wrapped lines.


The input should be a bit list containing one or more of the [``](#id163)STC\_WRAPVISUALFLAG\_\* `` constants.



Parameters
**wrapVisualFlags** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetWrapVisualFlagsLocation(self, wrapVisualFlagsLocation: int) -> None:
        """ 

`SetWrapVisualFlagsLocation`(*self*, *wrapVisualFlagsLocation*)[¶](#wx.stc.StyledTextCtrl.SetWrapVisualFlagsLocation "Permalink to this definition")
Set the location of visual flags for wrapped lines.


The input should be a bit list containing one or more of the [``](#id165)STC\_WRAPVISUALFLAGLOC\_\* `` constants.



Parameters
**wrapVisualFlagsLocation** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetXCaretPolicy(self, caretPolicy, caretSlop) -> None:
        """ 

`SetXCaretPolicy`(*self*, *caretPolicy*, *caretSlop*)[¶](#wx.stc.StyledTextCtrl.SetXCaretPolicy "Permalink to this definition")
Set the way the caret is kept visible when going sideways.


The exclusion zone is given in pixels.


The first argument should be a bit list containing one or more of the [``](#id167)STC\_CARET\_\* `` constants.



Parameters
* **caretPolicy** (*int*) –
* **caretSlop** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetXOffset(self, xOffset: int) -> None:
        """ 

`SetXOffset`(*self*, *xOffset*)[¶](#wx.stc.StyledTextCtrl.SetXOffset "Permalink to this definition")
Set the xOffset (ie, horizontal scroll position).



Parameters
**xOffset** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetYCaretPolicy(self, caretPolicy, caretSlop) -> None:
        """ 

`SetYCaretPolicy`(*self*, *caretPolicy*, *caretSlop*)[¶](#wx.stc.StyledTextCtrl.SetYCaretPolicy "Permalink to this definition")
Set the way the line the caret is on is kept visible.


The exclusion zone is given in lines.


The first argument should be a bit list containing one or more of the [``](#id169)STC\_CARET\_\* `` constants.



Parameters
* **caretPolicy** (*int*) –
* **caretSlop** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SetZoom(self, zoomInPoints: int) -> None:
        """ 

`SetZoom`(*self*, *zoomInPoints*)[¶](#wx.stc.StyledTextCtrl.SetZoom "Permalink to this definition")
Set the zoom level.


This number of points is added to the size of all fonts. It may be positive to magnify or negative to reduce.



Parameters
**zoomInPoints** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ShowLines(self, lineStart, lineEnd) -> None:
        """ 

`ShowLines`(*self*, *lineStart*, *lineEnd*)[¶](#wx.stc.StyledTextCtrl.ShowLines "Permalink to this definition")
Make a range of lines visible.



Parameters
* **lineStart** (*int*) –
* **lineEnd** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ShowPosition(self, pos: int) -> None:
        """ 

`ShowPosition`(*self*, *pos*)[¶](#wx.stc.StyledTextCtrl.ShowPosition "Permalink to this definition")
Makes the line containing the given position visible.



Parameters
**pos** (*long*) – The position that should be visible.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StartRecord(self) -> None:
        """ 

`StartRecord`(*self*)[¶](#wx.stc.StyledTextCtrl.StartRecord "Permalink to this definition")
Start notifying the container of all key presses and commands.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StartStyling(self, start: int) -> None:
        """ 

`StartStyling`(*self*, *start*)[¶](#wx.stc.StyledTextCtrl.StartStyling "Permalink to this definition")
Set the current styling position to start.



Parameters
**start** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StopRecord(self) -> None:
        """ 

`StopRecord`(*self*)[¶](#wx.stc.StyledTextCtrl.StopRecord "Permalink to this definition")
Stop notifying the container of all key presses and commands.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageDown(self) -> None:
        """ 

`StutteredPageDown`(*self*)[¶](#wx.stc.StyledTextCtrl.StutteredPageDown "Permalink to this definition")
Move caret to bottom of page, or one page down if already at bottom of page.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageDownExtend(self) -> None:
        """ 

`StutteredPageDownExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.StutteredPageDownExtend "Permalink to this definition")
Move caret to bottom of page, or one page down if already at bottom of page, extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageUp(self) -> None:
        """ 

`StutteredPageUp`(*self*)[¶](#wx.stc.StyledTextCtrl.StutteredPageUp "Permalink to this definition")
Move caret to top of page, or one page up if already at top of page.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StutteredPageUpExtend(self) -> None:
        """ 

`StutteredPageUpExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.StutteredPageUpExtend "Permalink to this definition")
Move caret to top of page, or one page up if already at top of page, extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleClearAll(self) -> None:
        """ 

`StyleClearAll`(*self*)[¶](#wx.stc.StyledTextCtrl.StyleClearAll "Permalink to this definition")
Clear all the styles and make equivalent to the global default style.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetBackground(self, style: int) -> 'Colour':
        """ 

`StyleGetBackground`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetBackground "Permalink to this definition")
Get the background colour of a style.



Parameters
**style** (*int*) – 



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetBold(self, style: int) -> bool:
        """ 

`StyleGetBold`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetBold "Permalink to this definition")
Get is a style bold or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetCase(self, style: int) -> int:
        """ 

`StyleGetCase`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetCase "Permalink to this definition")
Get is a style mixed case, or to force upper or lower case.


The return value will be one of the [``](#id171)STC\_CASE\_\* `` constants.



Parameters
**style** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetChangeable(self, style: int) -> bool:
        """ 

`StyleGetChangeable`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetChangeable "Permalink to this definition")
Get is a style changeable or not (read only).


Experimental feature, currently buggy.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetCharacterSet(self, style: int) -> int:
        """ 

`StyleGetCharacterSet`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetCharacterSet "Permalink to this definition")
Get the character get of the font in a style.



Parameters
**style** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetEOLFilled(self, style: int) -> bool:
        """ 

`StyleGetEOLFilled`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetEOLFilled "Permalink to this definition")
Get is a style to have its end of line filled or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetFaceName(self, style: int) -> str:
        """ 

`StyleGetFaceName`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetFaceName "Permalink to this definition")
Get the font facename of a style.



Parameters
**style** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetFont(self, style: int) -> 'Font':
        """ 

`StyleGetFont`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetFont "Permalink to this definition")
Get the font of a style.



Parameters
**style** (*int*) – 



Return type
 [wx.Font](wx.Font.html#wx-font)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetForeground(self, style: int) -> 'Colour':
        """ 

`StyleGetForeground`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetForeground "Permalink to this definition")
Get the foreground colour of a style.



Parameters
**style** (*int*) – 



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetHotSpot(self, style: int) -> bool:
        """ 

`StyleGetHotSpot`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetHotSpot "Permalink to this definition")
Get is a style a hotspot or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetItalic(self, style: int) -> bool:
        """ 

`StyleGetItalic`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetItalic "Permalink to this definition")
Get is a style italic or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetSize(self, style: int) -> int:
        """ 

`StyleGetSize`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetSize "Permalink to this definition")
Get the size of characters of a style.



Parameters
**style** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetSizeFractional(self, style: int) -> int:
        """ 

`StyleGetSizeFractional`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetSizeFractional "Permalink to this definition")
Get the size of characters of a style in points multiplied by 100.



Parameters
**style** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetUnderline(self, style: int) -> bool:
        """ 

`StyleGetUnderline`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetUnderline "Permalink to this definition")
Get is a style underlined or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetVisible(self, style: int) -> bool:
        """ 

`StyleGetVisible`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetVisible "Permalink to this definition")
Get is a style visible or not.



Parameters
**style** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleGetWeight(self, style: int) -> int:
        """ 

`StyleGetWeight`(*self*, *style*)[¶](#wx.stc.StyledTextCtrl.StyleGetWeight "Permalink to this definition")
Get the weight of characters of a style.


The return value will be an integer that is possibly one of the [``](#id173)STC\_WEIGHT\_\* `` constants.



Parameters
**style** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleResetDefault(self) -> None:
        """ 

`StyleResetDefault`(*self*)[¶](#wx.stc.StyledTextCtrl.StyleResetDefault "Permalink to this definition")
Reset the default style to its state at startup.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetBackground(self, style, back) -> None:
        """ 

`StyleSetBackground`(*self*, *style*, *back*)[¶](#wx.stc.StyledTextCtrl.StyleSetBackground "Permalink to this definition")
Set the background colour of a style.



Parameters
* **style** (*int*) –
* **back** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetBold(self, style, bold) -> None:
        """ 

`StyleSetBold`(*self*, *style*, *bold*)[¶](#wx.stc.StyledTextCtrl.StyleSetBold "Permalink to this definition")
Set a style to be bold or not.



Parameters
* **style** (*int*) –
* **bold** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetCase(self, style, caseVisible) -> None:
        """ 

`StyleSetCase`(*self*, *style*, *caseVisible*)[¶](#wx.stc.StyledTextCtrl.StyleSetCase "Permalink to this definition")
Set a style to be mixed case, or to force upper or lower case.


The second argument should be one of the [``](#id175)STC\_CASE\_\* `` constants.



Parameters
* **style** (*int*) –
* **caseVisible** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetChangeable(self, style, changeable) -> None:
        """ 

`StyleSetChangeable`(*self*, *style*, *changeable*)[¶](#wx.stc.StyledTextCtrl.StyleSetChangeable "Permalink to this definition")
Set a style to be changeable or not (read only).


Experimental feature, currently buggy.



Parameters
* **style** (*int*) –
* **changeable** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetCharacterSet(self, style, characterSet) -> None:
        """ 

`StyleSetCharacterSet`(*self*, *style*, *characterSet*)[¶](#wx.stc.StyledTextCtrl.StyleSetCharacterSet "Permalink to this definition")
Set the character set of the font in a style.


Converts the Scintilla character set values to a FontEncoding.



Parameters
* **style** (*int*) –
* **characterSet** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetEOLFilled(self, style, eolFilled) -> None:
        """ 

`StyleSetEOLFilled`(*self*, *style*, *eolFilled*)[¶](#wx.stc.StyledTextCtrl.StyleSetEOLFilled "Permalink to this definition")
Set a style to have its end of line filled or not.



Parameters
* **style** (*int*) –
* **eolFilled** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFaceName(self, style, fontName) -> None:
        """ 

`StyleSetFaceName`(*self*, *style*, *fontName*)[¶](#wx.stc.StyledTextCtrl.StyleSetFaceName "Permalink to this definition")
Set the font of a style.



Parameters
* **style** (*int*) –
* **fontName** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFont(self, styleNum, font) -> None:
        """ 

`StyleSetFont`(*self*, *styleNum*, *font*)[¶](#wx.stc.StyledTextCtrl.StyleSetFont "Permalink to this definition")
Set style size, face, bold, italic, and underline attributes from a  [wx.Font](wx.Font.html#wx-font)’s attributes.



Parameters
* **styleNum** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFontAttr(self, styleNum, size, faceName, bold, italic, underline, encoding=FONTENCODING_DEFAULT) -> None:
        """ 

`StyleSetFontAttr`(*self*, *styleNum*, *size*, *faceName*, *bold*, *italic*, *underline*, *encoding=FONTENCODING\_DEFAULT*)[¶](#wx.stc.StyledTextCtrl.StyleSetFontAttr "Permalink to this definition")
Set all font style attributes at once.



Parameters
* **styleNum** (*int*) –
* **size** (*int*) –
* **faceName** (*string*) –
* **bold** (*bool*) –
* **italic** (*bool*) –
* **underline** (*bool*) –
* **encoding** ([*FontEncoding*](wx.FontEncoding.enumeration.html "FontEncoding")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetFontEncoding(self, style, encoding) -> None:
        """ 

`StyleSetFontEncoding`(*self*, *style*, *encoding*)[¶](#wx.stc.StyledTextCtrl.StyleSetFontEncoding "Permalink to this definition")
Set the font encoding to be used by a style.



Parameters
* **style** (*int*) –
* **encoding** ([*FontEncoding*](wx.FontEncoding.enumeration.html "FontEncoding")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetForeground(self, style, fore) -> None:
        """ 

`StyleSetForeground`(*self*, *style*, *fore*)[¶](#wx.stc.StyledTextCtrl.StyleSetForeground "Permalink to this definition")
Set the foreground colour of a style.



Parameters
* **style** (*int*) –
* **fore** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetHotSpot(self, style, hotspot) -> None:
        """ 

`StyleSetHotSpot`(*self*, *style*, *hotspot*)[¶](#wx.stc.StyledTextCtrl.StyleSetHotSpot "Permalink to this definition")
Set a style to be a hotspot or not.



Parameters
* **style** (*int*) –
* **hotspot** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetItalic(self, style, italic) -> None:
        """ 

`StyleSetItalic`(*self*, *style*, *italic*)[¶](#wx.stc.StyledTextCtrl.StyleSetItalic "Permalink to this definition")
Set a style to be italic or not.



Parameters
* **style** (*int*) –
* **italic** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSize(self, style, sizePoints) -> None:
        """ 

`StyleSetSize`(*self*, *style*, *sizePoints*)[¶](#wx.stc.StyledTextCtrl.StyleSetSize "Permalink to this definition")
Set the size of characters of a style.



Parameters
* **style** (*int*) –
* **sizePoints** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSizeFractional(self, style, sizeHundredthPoints) -> None:
        """ 

`StyleSetSizeFractional`(*self*, *style*, *sizeHundredthPoints*)[¶](#wx.stc.StyledTextCtrl.StyleSetSizeFractional "Permalink to this definition")
Set the size of characters of a style.


Size is in points multiplied by 100.



Parameters
* **style** (*int*) –
* **sizeHundredthPoints** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetSpec(self, styleNum, spec) -> None:
        """ 

`StyleSetSpec`(*self*, *styleNum*, *spec*)[¶](#wx.stc.StyledTextCtrl.StyleSetSpec "Permalink to this definition")
Extract style settings from a spec-string which is composed of one or more of the following comma separated elements:


bold turns on bold italic turns on italics fore:[name or #``RRGGBB]`` sets the foreground colour back:[name or #``RRGGBB]`` sets the background colour face:[facename] sets the font face name to use size:[num] sets the font size in points eol turns on eol filling underline turns on underlining



Parameters
* **styleNum** (*int*) –
* **spec** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetUnderline(self, style, underline) -> None:
        """ 

`StyleSetUnderline`(*self*, *style*, *underline*)[¶](#wx.stc.StyledTextCtrl.StyleSetUnderline "Permalink to this definition")
Set a style to be underlined or not.



Parameters
* **style** (*int*) –
* **underline** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetVisible(self, style, visible) -> None:
        """ 

`StyleSetVisible`(*self*, *style*, *visible*)[¶](#wx.stc.StyledTextCtrl.StyleSetVisible "Permalink to this definition")
Set a style to be visible or not.



Parameters
* **style** (*int*) –
* **visible** (*bool*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def StyleSetWeight(self, style, weight) -> None:
        """ 

`StyleSetWeight`(*self*, *style*, *weight*)[¶](#wx.stc.StyledTextCtrl.StyleSetWeight "Permalink to this definition")
Set the weight of characters of a style.


The second argument can be an integer or one of the [``](#id177)STC\_WEIGHT\_\* `` constants.



Parameters
* **style** (*int*) –
* **weight** (*int*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def SwapMainAnchorCaret(self) -> None:
        """ 

`SwapMainAnchorCaret`(*self*)[¶](#wx.stc.StyledTextCtrl.SwapMainAnchorCaret "Permalink to this definition")
Swap that caret and anchor of the main selection.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Tab(self) -> None:
        """ 

`Tab`(*self*)[¶](#wx.stc.StyledTextCtrl.Tab "Permalink to this definition")
If selection is empty or all on one line replace the selection with a tab character.


If more than one line selected, indent the lines.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TargetFromSelection(self) -> None:
        """ 

`TargetFromSelection`(*self*)[¶](#wx.stc.StyledTextCtrl.TargetFromSelection "Permalink to this definition")
Make the target range start and end be the same as the selection range start and end.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TargetWholeDocument(self) -> None:
        """ 

`TargetWholeDocument`(*self*)[¶](#wx.stc.StyledTextCtrl.TargetWholeDocument "Permalink to this definition")
Sets the target to the whole document.



New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TextHeight(self, line: int) -> int:
        """ 

`TextHeight`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.TextHeight "Permalink to this definition")
Retrieve the height of a particular line of text in pixels.



Parameters
**line** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def TextWidth(self, style, text) -> int:
        """ 

`TextWidth`(*self*, *style*, *text*)[¶](#wx.stc.StyledTextCtrl.TextWidth "Permalink to this definition")
Measure the pixel width of some text in a particular style.


Does not handle tab or control characters.



Parameters
* **style** (*int*) –
* **text** (*string*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleCaretSticky(self) -> None:
        """ 

`ToggleCaretSticky`(*self*)[¶](#wx.stc.StyledTextCtrl.ToggleCaretSticky "Permalink to this definition")
Switch between sticky and non-sticky: meant to be bound to a key.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleFold(self, line: int) -> None:
        """ 

`ToggleFold`(*self*, *line*)[¶](#wx.stc.StyledTextCtrl.ToggleFold "Permalink to this definition")
Switch a header line between expanded and contracted.



Parameters
**line** (*int*) – 






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ToggleFoldShowText(self, line, text) -> None:
        """ 

`ToggleFoldShowText`(*self*, *line*, *text*)[¶](#wx.stc.StyledTextCtrl.ToggleFoldShowText "Permalink to this definition")
Switch a header line between expanded and contracted and show some text after the line.



Parameters
* **line** (*int*) –
* **text** (*string*) –





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def Undo(self) -> None:
        """ 

`Undo`(*self*)[¶](#wx.stc.StyledTextCtrl.Undo "Permalink to this definition")
Undo one action in the undo history.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UpperCase(self) -> None:
        """ 

`UpperCase`(*self*)[¶](#wx.stc.StyledTextCtrl.UpperCase "Permalink to this definition")
Transform the selection to upper case.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UsePopUp(self, popUpMode: int) -> None:
        """ 

`UsePopUp`(*self*, *popUpMode*)[¶](#wx.stc.StyledTextCtrl.UsePopUp "Permalink to this definition")
Set whether a pop up menu is displayed automatically when the user presses the wrong mouse button on certain areas.


The input should be one of the [``](#id179)STC\_POPUP\_\* `` constants.



Parameters
**popUpMode** (*int*) – 





Note


When  [wx.ContextMenuEvent](wx.ContextMenuEvent.html#wx-contextmenuevent) is used to create a custom popup menu, this function should be called with `wx.stc.STC_POPUP_NEVER`. Otherwise the default menu will be shown instead of the custom one.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def UserListShow(self, listType, itemList) -> None:
        """ 

`UserListShow`(*self*, *listType*, *itemList*)[¶](#wx.stc.StyledTextCtrl.UserListShow "Permalink to this definition")
Display a list of strings and send notification when user chooses one.



Parameters
* **listType** (*int*) –
* **itemList** (*string*) –






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHome(self) -> None:
        """ 

`VCHome`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHome "Permalink to this definition")
Move caret to before first visible character on line.


If already there move to first character on line.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeDisplay(self) -> None:
        """ 

`VCHomeDisplay`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeDisplay "Permalink to this definition")
Move caret to before first visible character on display line.


If already there move to first character on display line.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeDisplayExtend(self) -> None:
        """ 

`VCHomeDisplayExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeDisplayExtend "Permalink to this definition")
Like VCHomeDisplay but extending selection to new caret position.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeExtend(self) -> None:
        """ 

`VCHomeExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeExtend "Permalink to this definition")
Like VCHome but extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeRectExtend(self) -> None:
        """ 

`VCHomeRectExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeRectExtend "Permalink to this definition")
Move caret to before first visible character on line.


If already there move to first character on line. In either case, extend rectangular selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeWrap(self) -> None:
        """ 

`VCHomeWrap`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeWrap "Permalink to this definition")
Like VCHome but when word-wrap is enabled goes first to start of display line VCHomeDisplay, then behaves like VCHome.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VCHomeWrapExtend(self) -> None:
        """ 

`VCHomeWrapExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.VCHomeWrapExtend "Permalink to this definition")
Like VCHomeExtend but when word-wrap is enabled extends first to start of display line VCHomeDisplayExtend, then behaves like VCHomeExtend.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VerticalCentreCaret(self) -> None:
        """ 

`VerticalCentreCaret`(*self*)[¶](#wx.stc.StyledTextCtrl.VerticalCentreCaret "Permalink to this definition")
Centre current line in window.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def VisibleFromDocLine(self, docLine: int) -> int:
        """ 

`VisibleFromDocLine`(*self*, *docLine*)[¶](#wx.stc.StyledTextCtrl.VisibleFromDocLine "Permalink to this definition")
Find the display line of a document line taking hidden lines into account.



Parameters
**docLine** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordEndPosition(self, pos, onlyWordCharacters) -> int:
        """ 

`WordEndPosition`(*self*, *pos*, *onlyWordCharacters*)[¶](#wx.stc.StyledTextCtrl.WordEndPosition "Permalink to this definition")
Get position of end of word.



Parameters
* **pos** (*int*) –
* **onlyWordCharacters** (*bool*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeft(self) -> None:
        """ 

`WordLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.WordLeft "Permalink to this definition")
Move caret left one word.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftEnd(self) -> None:
        """ 

`WordLeftEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.WordLeftEnd "Permalink to this definition")
Move caret left one word, position cursor at end of word.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftEndExtend(self) -> None:
        """ 

`WordLeftEndExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordLeftEndExtend "Permalink to this definition")
Move caret left one word, position cursor at end of word, extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordLeftExtend(self) -> None:
        """ 

`WordLeftExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordLeftExtend "Permalink to this definition")
Move caret left one word extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartLeft(self) -> None:
        """ 

`WordPartLeft`(*self*)[¶](#wx.stc.StyledTextCtrl.WordPartLeft "Permalink to this definition")
Move to the previous change in capitalisation.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartLeftExtend(self) -> None:
        """ 

`WordPartLeftExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordPartLeftExtend "Permalink to this definition")
Move to the previous change in capitalisation extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartRight(self) -> None:
        """ 

`WordPartRight`(*self*)[¶](#wx.stc.StyledTextCtrl.WordPartRight "Permalink to this definition")
Move to the change next in capitalisation.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordPartRightExtend(self) -> None:
        """ 

`WordPartRightExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordPartRightExtend "Permalink to this definition")
Move to the next change in capitalisation extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRight(self) -> None:
        """ 

`WordRight`(*self*)[¶](#wx.stc.StyledTextCtrl.WordRight "Permalink to this definition")
Move caret right one word.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightEnd(self) -> None:
        """ 

`WordRightEnd`(*self*)[¶](#wx.stc.StyledTextCtrl.WordRightEnd "Permalink to this definition")
Move caret right one word, position cursor at end of word.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightEndExtend(self) -> None:
        """ 

`WordRightEndExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordRightEndExtend "Permalink to this definition")
Move caret right one word, position cursor at end of word, extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordRightExtend(self) -> None:
        """ 

`WordRightExtend`(*self*)[¶](#wx.stc.StyledTextCtrl.WordRightExtend "Permalink to this definition")
Move caret right one word extending selection to new caret position.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WordStartPosition(self, pos, onlyWordCharacters) -> int:
        """ 

`WordStartPosition`(*self*, *pos*, *onlyWordCharacters*)[¶](#wx.stc.StyledTextCtrl.WordStartPosition "Permalink to this definition")
Get position of start of word.



Parameters
* **pos** (*int*) –
* **onlyWordCharacters** (*bool*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WrapCount(self, docLine: int) -> int:
        """ 

`WrapCount`(*self*, *docLine*)[¶](#wx.stc.StyledTextCtrl.WrapCount "Permalink to this definition")
The number of display lines needed to wrap a document line.



Parameters
**docLine** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def WriteText(self, text: str) -> None:
        """ 

`WriteText`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.WriteText "Permalink to this definition")
Writes the text into the text control at the current insertion position.



Parameters
**text** (*string*) – Text to write to the text control.





Note


Newlines in the text string are the only control characters allowed, and they will cause appropriate line breaks. See operator<<() and [`AppendText`](#wx.stc.StyledTextCtrl.AppendText "wx.stc.StyledTextCtrl.AppendText") for more convenient ways of writing to the window. After the write operation, the insertion point will be at the end of the inserted text, so subsequent write operations will be appended. To append text after the user may have interacted with the control, call [`wx.TextCtrl.SetInsertionPointEnd`](wx.TextEntry.html#wx.TextEntry.SetInsertionPointEnd "wx.TextEntry.SetInsertionPointEnd") before writing.





            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def XYToPosition(self, x, y) -> int:
        """ 

`XYToPosition`(*self*, *x*, *y*)[¶](#wx.stc.StyledTextCtrl.XYToPosition "Permalink to this definition")
Converts the given zero based column and line number to a position.



Parameters
* **x** (*long*) – The column number.
* **y** (*long*) – The line number.



Return type
*long*



Returns
The position value, or -1 if x or y was invalid.






            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ZoomIn(self) -> None:
        """ 

`ZoomIn`(*self*)[¶](#wx.stc.StyledTextCtrl.ZoomIn "Permalink to this definition")
Magnify the displayed text by increasing the sizes by 1 point.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def ZoomOut(self) -> None:
        """ 

`ZoomOut`(*self*)[¶](#wx.stc.StyledTextCtrl.ZoomOut "Permalink to this definition")
Make the displayed text smaller by decreasing the sizes by 1 point.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def flush(self) -> None:
        """ 

`flush`(*self*)[¶](#wx.stc.StyledTextCtrl.flush "Permalink to this definition")
`NOP`, for file-like compatibility.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    def write(self, text) -> None:
        """ 

`write`(*self*, *text*)[¶](#wx.stc.StyledTextCtrl.write "Permalink to this definition")
Append text to the textctrl, for file-like compatibility.




            Source: https://docs.wxpython.org/wx.stc.StyledTextCtrl.html
        """

    AdditionalCaretForeground: 'Colour'  # `AdditionalCaretForeground`[¶](#wx.stc.StyledTextCtrl.AdditionalCaretForeground "Permalink to this definition")See [`GetAdditionalCaretForeground`](#wx.stc.StyledTextCtrl.GetAdditionalCaretForeground "wx.stc.StyledTextCtrl.GetAdditionalCaretForeground") and [`SetAdditionalCaretForeground`](#wx.stc.StyledTextCtrl.SetAdditionalCaretForeground "wx.stc.StyledTextCtrl.SetAdditionalCaretForeground")
    AdditionalCaretsBlink: bool  # `AdditionalCaretsBlink`[¶](#wx.stc.StyledTextCtrl.AdditionalCaretsBlink "Permalink to this definition")See [`GetAdditionalCaretsBlink`](#wx.stc.StyledTextCtrl.GetAdditionalCaretsBlink "wx.stc.StyledTextCtrl.GetAdditionalCaretsBlink") and [`SetAdditionalCaretsBlink`](#wx.stc.StyledTextCtrl.SetAdditionalCaretsBlink "wx.stc.StyledTextCtrl.SetAdditionalCaretsBlink")
    AdditionalCaretsVisible: bool  # `AdditionalCaretsVisible`[¶](#wx.stc.StyledTextCtrl.AdditionalCaretsVisible "Permalink to this definition")See [`GetAdditionalCaretsVisible`](#wx.stc.StyledTextCtrl.GetAdditionalCaretsVisible "wx.stc.StyledTextCtrl.GetAdditionalCaretsVisible") and [`SetAdditionalCaretsVisible`](#wx.stc.StyledTextCtrl.SetAdditionalCaretsVisible "wx.stc.StyledTextCtrl.SetAdditionalCaretsVisible")
    AdditionalSelAlpha: int  # `AdditionalSelAlpha`[¶](#wx.stc.StyledTextCtrl.AdditionalSelAlpha "Permalink to this definition")See [`GetAdditionalSelAlpha`](#wx.stc.StyledTextCtrl.GetAdditionalSelAlpha "wx.stc.StyledTextCtrl.GetAdditionalSelAlpha") and [`SetAdditionalSelAlpha`](#wx.stc.StyledTextCtrl.SetAdditionalSelAlpha "wx.stc.StyledTextCtrl.SetAdditionalSelAlpha")
    AdditionalSelectionTyping: bool  # `AdditionalSelectionTyping`[¶](#wx.stc.StyledTextCtrl.AdditionalSelectionTyping "Permalink to this definition")See [`GetAdditionalSelectionTyping`](#wx.stc.StyledTextCtrl.GetAdditionalSelectionTyping "wx.stc.StyledTextCtrl.GetAdditionalSelectionTyping") and [`SetAdditionalSelectionTyping`](#wx.stc.StyledTextCtrl.SetAdditionalSelectionTyping "wx.stc.StyledTextCtrl.SetAdditionalSelectionTyping")
    AllLinesVisible: bool  # `AllLinesVisible`[¶](#wx.stc.StyledTextCtrl.AllLinesVisible "Permalink to this definition")See [`GetAllLinesVisible`](#wx.stc.StyledTextCtrl.GetAllLinesVisible "wx.stc.StyledTextCtrl.GetAllLinesVisible")
    Anchor: int  # `Anchor`[¶](#wx.stc.StyledTextCtrl.Anchor "Permalink to this definition")See [`GetAnchor`](#wx.stc.StyledTextCtrl.GetAnchor "wx.stc.StyledTextCtrl.GetAnchor") and [`SetAnchor`](#wx.stc.StyledTextCtrl.SetAnchor "wx.stc.StyledTextCtrl.SetAnchor")
    AutomaticFold: int  # `AutomaticFold`[¶](#wx.stc.StyledTextCtrl.AutomaticFold "Permalink to this definition")See [`GetAutomaticFold`](#wx.stc.StyledTextCtrl.GetAutomaticFold "wx.stc.StyledTextCtrl.GetAutomaticFold") and [`SetAutomaticFold`](#wx.stc.StyledTextCtrl.SetAutomaticFold "wx.stc.StyledTextCtrl.SetAutomaticFold")
    BackSpaceUnIndents: bool  # `BackSpaceUnIndents`[¶](#wx.stc.StyledTextCtrl.BackSpaceUnIndents "Permalink to this definition")See [`GetBackSpaceUnIndents`](#wx.stc.StyledTextCtrl.GetBackSpaceUnIndents "wx.stc.StyledTextCtrl.GetBackSpaceUnIndents") and [`SetBackSpaceUnIndents`](#wx.stc.StyledTextCtrl.SetBackSpaceUnIndents "wx.stc.StyledTextCtrl.SetBackSpaceUnIndents")
    BufferedDraw: bool  # `BufferedDraw`[¶](#wx.stc.StyledTextCtrl.BufferedDraw "Permalink to this definition")See [`GetBufferedDraw`](#wx.stc.StyledTextCtrl.GetBufferedDraw "wx.stc.StyledTextCtrl.GetBufferedDraw") and [`SetBufferedDraw`](#wx.stc.StyledTextCtrl.SetBufferedDraw "wx.stc.StyledTextCtrl.SetBufferedDraw")
    CaretForeground: 'Colour'  # `CaretForeground`[¶](#wx.stc.StyledTextCtrl.CaretForeground "Permalink to this definition")See [`GetCaretForeground`](#wx.stc.StyledTextCtrl.GetCaretForeground "wx.stc.StyledTextCtrl.GetCaretForeground") and [`SetCaretForeground`](#wx.stc.StyledTextCtrl.SetCaretForeground "wx.stc.StyledTextCtrl.SetCaretForeground")
    CaretLineBackAlpha: int  # `CaretLineBackAlpha`[¶](#wx.stc.StyledTextCtrl.CaretLineBackAlpha "Permalink to this definition")See [`GetCaretLineBackAlpha`](#wx.stc.StyledTextCtrl.GetCaretLineBackAlpha "wx.stc.StyledTextCtrl.GetCaretLineBackAlpha") and [`SetCaretLineBackAlpha`](#wx.stc.StyledTextCtrl.SetCaretLineBackAlpha "wx.stc.StyledTextCtrl.SetCaretLineBackAlpha")
    CaretLineBackground: 'Colour'  # `CaretLineBackground`[¶](#wx.stc.StyledTextCtrl.CaretLineBackground "Permalink to this definition")See [`GetCaretLineBackground`](#wx.stc.StyledTextCtrl.GetCaretLineBackground "wx.stc.StyledTextCtrl.GetCaretLineBackground") and [`SetCaretLineBackground`](#wx.stc.StyledTextCtrl.SetCaretLineBackground "wx.stc.StyledTextCtrl.SetCaretLineBackground")
    CaretLineVisible: bool  # `CaretLineVisible`[¶](#wx.stc.StyledTextCtrl.CaretLineVisible "Permalink to this definition")See [`GetCaretLineVisible`](#wx.stc.StyledTextCtrl.GetCaretLineVisible "wx.stc.StyledTextCtrl.GetCaretLineVisible") and [`SetCaretLineVisible`](#wx.stc.StyledTextCtrl.SetCaretLineVisible "wx.stc.StyledTextCtrl.SetCaretLineVisible")
    CaretLineVisibleAlways: bool  # `CaretLineVisibleAlways`[¶](#wx.stc.StyledTextCtrl.CaretLineVisibleAlways "Permalink to this definition")See [`GetCaretLineVisibleAlways`](#wx.stc.StyledTextCtrl.GetCaretLineVisibleAlways "wx.stc.StyledTextCtrl.GetCaretLineVisibleAlways") and [`SetCaretLineVisibleAlways`](#wx.stc.StyledTextCtrl.SetCaretLineVisibleAlways "wx.stc.StyledTextCtrl.SetCaretLineVisibleAlways")
    CaretPeriod: int  # `CaretPeriod`[¶](#wx.stc.StyledTextCtrl.CaretPeriod "Permalink to this definition")See [`GetCaretPeriod`](#wx.stc.StyledTextCtrl.GetCaretPeriod "wx.stc.StyledTextCtrl.GetCaretPeriod") and [`SetCaretPeriod`](#wx.stc.StyledTextCtrl.SetCaretPeriod "wx.stc.StyledTextCtrl.SetCaretPeriod")
    CaretSticky: int  # `CaretSticky`[¶](#wx.stc.StyledTextCtrl.CaretSticky "Permalink to this definition")See [`GetCaretSticky`](#wx.stc.StyledTextCtrl.GetCaretSticky "wx.stc.StyledTextCtrl.GetCaretSticky") and [`SetCaretSticky`](#wx.stc.StyledTextCtrl.SetCaretSticky "wx.stc.StyledTextCtrl.SetCaretSticky")
    CaretStyle: int  # `CaretStyle`[¶](#wx.stc.StyledTextCtrl.CaretStyle "Permalink to this definition")See [`GetCaretStyle`](#wx.stc.StyledTextCtrl.GetCaretStyle "wx.stc.StyledTextCtrl.GetCaretStyle") and [`SetCaretStyle`](#wx.stc.StyledTextCtrl.SetCaretStyle "wx.stc.StyledTextCtrl.SetCaretStyle")
    CaretWidth: int  # `CaretWidth`[¶](#wx.stc.StyledTextCtrl.CaretWidth "Permalink to this definition")See [`GetCaretWidth`](#wx.stc.StyledTextCtrl.GetCaretWidth "wx.stc.StyledTextCtrl.GetCaretWidth") and [`SetCaretWidth`](#wx.stc.StyledTextCtrl.SetCaretWidth "wx.stc.StyledTextCtrl.SetCaretWidth")
    CharacterPointer: Any  # `CharacterPointer`[¶](#wx.stc.StyledTextCtrl.CharacterPointer "Permalink to this definition")See [`GetCharacterPointer`](#wx.stc.StyledTextCtrl.GetCharacterPointer "wx.stc.StyledTextCtrl.GetCharacterPointer")
    CodePage: int  # `CodePage`[¶](#wx.stc.StyledTextCtrl.CodePage "Permalink to this definition")See [`GetCodePage`](#wx.stc.StyledTextCtrl.GetCodePage "wx.stc.StyledTextCtrl.GetCodePage") and [`SetCodePage`](#wx.stc.StyledTextCtrl.SetCodePage "wx.stc.StyledTextCtrl.SetCodePage")
    ControlCharSymbol: int  # `ControlCharSymbol`[¶](#wx.stc.StyledTextCtrl.ControlCharSymbol "Permalink to this definition")See [`GetControlCharSymbol`](#wx.stc.StyledTextCtrl.GetControlCharSymbol "wx.stc.StyledTextCtrl.GetControlCharSymbol") and [`SetControlCharSymbol`](#wx.stc.StyledTextCtrl.SetControlCharSymbol "wx.stc.StyledTextCtrl.SetControlCharSymbol")
    CurLine: tuple  # `CurLine`[¶](#wx.stc.StyledTextCtrl.CurLine "Permalink to this definition")See [`GetCurLine`](#wx.stc.StyledTextCtrl.GetCurLine "wx.stc.StyledTextCtrl.GetCurLine")
    CurLineRaw: tuple  # `CurLineRaw`[¶](#wx.stc.StyledTextCtrl.CurLineRaw "Permalink to this definition")See [`GetCurLineRaw`](#wx.stc.StyledTextCtrl.GetCurLineRaw "wx.stc.StyledTextCtrl.GetCurLineRaw")
    CurrentLine: int  # `CurrentLine`[¶](#wx.stc.StyledTextCtrl.CurrentLine "Permalink to this definition")See [`GetCurrentLine`](#wx.stc.StyledTextCtrl.GetCurrentLine "wx.stc.StyledTextCtrl.GetCurrentLine")
    CurrentPos: int  # `CurrentPos`[¶](#wx.stc.StyledTextCtrl.CurrentPos "Permalink to this definition")See [`GetCurrentPos`](#wx.stc.StyledTextCtrl.GetCurrentPos "wx.stc.StyledTextCtrl.GetCurrentPos") and [`SetCurrentPos`](#wx.stc.StyledTextCtrl.SetCurrentPos "wx.stc.StyledTextCtrl.SetCurrentPos")
    DefaultStyle: 'TextAttr'  # `DefaultStyle`[¶](#wx.stc.StyledTextCtrl.DefaultStyle "Permalink to this definition")See [`GetDefaultStyle`](#wx.stc.StyledTextCtrl.GetDefaultStyle "wx.stc.StyledTextCtrl.GetDefaultStyle") and [`SetDefaultStyle`](#wx.stc.StyledTextCtrl.SetDefaultStyle "wx.stc.StyledTextCtrl.SetDefaultStyle")
    DirectFunction: None  # `DirectFunction`[¶](#wx.stc.StyledTextCtrl.DirectFunction "Permalink to this definition")See [`GetDirectFunction`](#wx.stc.StyledTextCtrl.GetDirectFunction "wx.stc.StyledTextCtrl.GetDirectFunction")
    DirectPointer: None  # `DirectPointer`[¶](#wx.stc.StyledTextCtrl.DirectPointer "Permalink to this definition")See [`GetDirectPointer`](#wx.stc.StyledTextCtrl.GetDirectPointer "wx.stc.StyledTextCtrl.GetDirectPointer")
    DocPointer: None  # `DocPointer`[¶](#wx.stc.StyledTextCtrl.DocPointer "Permalink to this definition")See [`GetDocPointer`](#wx.stc.StyledTextCtrl.GetDocPointer "wx.stc.StyledTextCtrl.GetDocPointer") and [`SetDocPointer`](#wx.stc.StyledTextCtrl.SetDocPointer "wx.stc.StyledTextCtrl.SetDocPointer")
    EOLMode: int  # `EOLMode`[¶](#wx.stc.StyledTextCtrl.EOLMode "Permalink to this definition")See [`GetEOLMode`](#wx.stc.StyledTextCtrl.GetEOLMode "wx.stc.StyledTextCtrl.GetEOLMode") and [`SetEOLMode`](#wx.stc.StyledTextCtrl.SetEOLMode "wx.stc.StyledTextCtrl.SetEOLMode")
    EdgeColour: 'Colour'  # `EdgeColour`[¶](#wx.stc.StyledTextCtrl.EdgeColour "Permalink to this definition")See [`GetEdgeColour`](#wx.stc.StyledTextCtrl.GetEdgeColour "wx.stc.StyledTextCtrl.GetEdgeColour") and [`SetEdgeColour`](#wx.stc.StyledTextCtrl.SetEdgeColour "wx.stc.StyledTextCtrl.SetEdgeColour")
    EdgeColumn: int  # `EdgeColumn`[¶](#wx.stc.StyledTextCtrl.EdgeColumn "Permalink to this definition")See [`GetEdgeColumn`](#wx.stc.StyledTextCtrl.GetEdgeColumn "wx.stc.StyledTextCtrl.GetEdgeColumn") and [`SetEdgeColumn`](#wx.stc.StyledTextCtrl.SetEdgeColumn "wx.stc.StyledTextCtrl.SetEdgeColumn")
    EdgeMode: int  # `EdgeMode`[¶](#wx.stc.StyledTextCtrl.EdgeMode "Permalink to this definition")See [`GetEdgeMode`](#wx.stc.StyledTextCtrl.GetEdgeMode "wx.stc.StyledTextCtrl.GetEdgeMode") and [`SetEdgeMode`](#wx.stc.StyledTextCtrl.SetEdgeMode "wx.stc.StyledTextCtrl.SetEdgeMode")
    EndAtLastLine: bool  # `EndAtLastLine`[¶](#wx.stc.StyledTextCtrl.EndAtLastLine "Permalink to this definition")See [`GetEndAtLastLine`](#wx.stc.StyledTextCtrl.GetEndAtLastLine "wx.stc.StyledTextCtrl.GetEndAtLastLine") and [`SetEndAtLastLine`](#wx.stc.StyledTextCtrl.SetEndAtLastLine "wx.stc.StyledTextCtrl.SetEndAtLastLine")
    EndStyled: int  # `EndStyled`[¶](#wx.stc.StyledTextCtrl.EndStyled "Permalink to this definition")See [`GetEndStyled`](#wx.stc.StyledTextCtrl.GetEndStyled "wx.stc.StyledTextCtrl.GetEndStyled")
    ExtraAscent: int  # `ExtraAscent`[¶](#wx.stc.StyledTextCtrl.ExtraAscent "Permalink to this definition")See [`GetExtraAscent`](#wx.stc.StyledTextCtrl.GetExtraAscent "wx.stc.StyledTextCtrl.GetExtraAscent") and [`SetExtraAscent`](#wx.stc.StyledTextCtrl.SetExtraAscent "wx.stc.StyledTextCtrl.SetExtraAscent")
    ExtraDescent: int  # `ExtraDescent`[¶](#wx.stc.StyledTextCtrl.ExtraDescent "Permalink to this definition")See [`GetExtraDescent`](#wx.stc.StyledTextCtrl.GetExtraDescent "wx.stc.StyledTextCtrl.GetExtraDescent") and [`SetExtraDescent`](#wx.stc.StyledTextCtrl.SetExtraDescent "wx.stc.StyledTextCtrl.SetExtraDescent")
    FirstVisibleLine: int  # `FirstVisibleLine`[¶](#wx.stc.StyledTextCtrl.FirstVisibleLine "Permalink to this definition")See [`GetFirstVisibleLine`](#wx.stc.StyledTextCtrl.GetFirstVisibleLine "wx.stc.StyledTextCtrl.GetFirstVisibleLine") and [`SetFirstVisibleLine`](#wx.stc.StyledTextCtrl.SetFirstVisibleLine "wx.stc.StyledTextCtrl.SetFirstVisibleLine")
    FontQuality: int  # `FontQuality`[¶](#wx.stc.StyledTextCtrl.FontQuality "Permalink to this definition")See [`GetFontQuality`](#wx.stc.StyledTextCtrl.GetFontQuality "wx.stc.StyledTextCtrl.GetFontQuality") and [`SetFontQuality`](#wx.stc.StyledTextCtrl.SetFontQuality "wx.stc.StyledTextCtrl.SetFontQuality")
    GapPosition: int  # `GapPosition`[¶](#wx.stc.StyledTextCtrl.GapPosition "Permalink to this definition")See [`GetGapPosition`](#wx.stc.StyledTextCtrl.GetGapPosition "wx.stc.StyledTextCtrl.GetGapPosition")
    HighlightGuide: int  # `HighlightGuide`[¶](#wx.stc.StyledTextCtrl.HighlightGuide "Permalink to this definition")See [`GetHighlightGuide`](#wx.stc.StyledTextCtrl.GetHighlightGuide "wx.stc.StyledTextCtrl.GetHighlightGuide") and [`SetHighlightGuide`](#wx.stc.StyledTextCtrl.SetHighlightGuide "wx.stc.StyledTextCtrl.SetHighlightGuide")
    Hint: str  # `Hint`[¶](#wx.stc.StyledTextCtrl.Hint "Permalink to this definition")See [`GetHint`](#wx.stc.StyledTextCtrl.GetHint "wx.stc.StyledTextCtrl.GetHint") and [`SetHint`](#wx.stc.StyledTextCtrl.SetHint "wx.stc.StyledTextCtrl.SetHint")
    HotspotActiveBackground: 'Colour'  # `HotspotActiveBackground`[¶](#wx.stc.StyledTextCtrl.HotspotActiveBackground "Permalink to this definition")See [`GetHotspotActiveBackground`](#wx.stc.StyledTextCtrl.GetHotspotActiveBackground "wx.stc.StyledTextCtrl.GetHotspotActiveBackground")
    HotspotActiveForeground: 'Colour'  # `HotspotActiveForeground`[¶](#wx.stc.StyledTextCtrl.HotspotActiveForeground "Permalink to this definition")See [`GetHotspotActiveForeground`](#wx.stc.StyledTextCtrl.GetHotspotActiveForeground "wx.stc.StyledTextCtrl.GetHotspotActiveForeground")
    HotspotActiveUnderline: bool  # `HotspotActiveUnderline`[¶](#wx.stc.StyledTextCtrl.HotspotActiveUnderline "Permalink to this definition")See [`GetHotspotActiveUnderline`](#wx.stc.StyledTextCtrl.GetHotspotActiveUnderline "wx.stc.StyledTextCtrl.GetHotspotActiveUnderline") and [`SetHotspotActiveUnderline`](#wx.stc.StyledTextCtrl.SetHotspotActiveUnderline "wx.stc.StyledTextCtrl.SetHotspotActiveUnderline")
    HotspotSingleLine: bool  # `HotspotSingleLine`[¶](#wx.stc.StyledTextCtrl.HotspotSingleLine "Permalink to this definition")See [`GetHotspotSingleLine`](#wx.stc.StyledTextCtrl.GetHotspotSingleLine "wx.stc.StyledTextCtrl.GetHotspotSingleLine") and [`SetHotspotSingleLine`](#wx.stc.StyledTextCtrl.SetHotspotSingleLine "wx.stc.StyledTextCtrl.SetHotspotSingleLine")
    IMEInteraction: int  # `IMEInteraction`[¶](#wx.stc.StyledTextCtrl.IMEInteraction "Permalink to this definition")See [`GetIMEInteraction`](#wx.stc.StyledTextCtrl.GetIMEInteraction "wx.stc.StyledTextCtrl.GetIMEInteraction") and [`SetIMEInteraction`](#wx.stc.StyledTextCtrl.SetIMEInteraction "wx.stc.StyledTextCtrl.SetIMEInteraction")
    Identifier: int  # `Identifier`[¶](#wx.stc.StyledTextCtrl.Identifier "Permalink to this definition")See [`GetIdentifier`](#wx.stc.StyledTextCtrl.GetIdentifier "wx.stc.StyledTextCtrl.GetIdentifier") and [`SetIdentifier`](#wx.stc.StyledTextCtrl.SetIdentifier "wx.stc.StyledTextCtrl.SetIdentifier")
    IdleStyling: int  # `IdleStyling`[¶](#wx.stc.StyledTextCtrl.IdleStyling "Permalink to this definition")See [`GetIdleStyling`](#wx.stc.StyledTextCtrl.GetIdleStyling "wx.stc.StyledTextCtrl.GetIdleStyling") and [`SetIdleStyling`](#wx.stc.StyledTextCtrl.SetIdleStyling "wx.stc.StyledTextCtrl.SetIdleStyling")
    Indent: int  # `Indent`[¶](#wx.stc.StyledTextCtrl.Indent "Permalink to this definition")See [`GetIndent`](#wx.stc.StyledTextCtrl.GetIndent "wx.stc.StyledTextCtrl.GetIndent") and [`SetIndent`](#wx.stc.StyledTextCtrl.SetIndent "wx.stc.StyledTextCtrl.SetIndent")
    IndentationGuides: int  # `IndentationGuides`[¶](#wx.stc.StyledTextCtrl.IndentationGuides "Permalink to this definition")See [`GetIndentationGuides`](#wx.stc.StyledTextCtrl.GetIndentationGuides "wx.stc.StyledTextCtrl.GetIndentationGuides") and [`SetIndentationGuides`](#wx.stc.StyledTextCtrl.SetIndentationGuides "wx.stc.StyledTextCtrl.SetIndentationGuides")
    IndicatorCurrent: int  # `IndicatorCurrent`[¶](#wx.stc.StyledTextCtrl.IndicatorCurrent "Permalink to this definition")See [`GetIndicatorCurrent`](#wx.stc.StyledTextCtrl.GetIndicatorCurrent "wx.stc.StyledTextCtrl.GetIndicatorCurrent") and [`SetIndicatorCurrent`](#wx.stc.StyledTextCtrl.SetIndicatorCurrent "wx.stc.StyledTextCtrl.SetIndicatorCurrent")
    IndicatorValue: int  # `IndicatorValue`[¶](#wx.stc.StyledTextCtrl.IndicatorValue "Permalink to this definition")See [`GetIndicatorValue`](#wx.stc.StyledTextCtrl.GetIndicatorValue "wx.stc.StyledTextCtrl.GetIndicatorValue") and [`SetIndicatorValue`](#wx.stc.StyledTextCtrl.SetIndicatorValue "wx.stc.StyledTextCtrl.SetIndicatorValue")
    InsertionPoint: int  # `InsertionPoint`[¶](#wx.stc.StyledTextCtrl.InsertionPoint "Permalink to this definition")See [`GetInsertionPoint`](#wx.stc.StyledTextCtrl.GetInsertionPoint "wx.stc.StyledTextCtrl.GetInsertionPoint") and [`SetInsertionPoint`](#wx.stc.StyledTextCtrl.SetInsertionPoint "wx.stc.StyledTextCtrl.SetInsertionPoint")
    LastKeydownProcessed: bool  # `LastKeydownProcessed`[¶](#wx.stc.StyledTextCtrl.LastKeydownProcessed "Permalink to this definition")See [`GetLastKeydownProcessed`](#wx.stc.StyledTextCtrl.GetLastKeydownProcessed "wx.stc.StyledTextCtrl.GetLastKeydownProcessed") and [`SetLastKeydownProcessed`](#wx.stc.StyledTextCtrl.SetLastKeydownProcessed "wx.stc.StyledTextCtrl.SetLastKeydownProcessed")
    LastPosition: int  # `LastPosition`[¶](#wx.stc.StyledTextCtrl.LastPosition "Permalink to this definition")See [`GetLastPosition`](#wx.stc.StyledTextCtrl.GetLastPosition "wx.stc.StyledTextCtrl.GetLastPosition")
    LayoutCache: int  # `LayoutCache`[¶](#wx.stc.StyledTextCtrl.LayoutCache "Permalink to this definition")See [`GetLayoutCache`](#wx.stc.StyledTextCtrl.GetLayoutCache "wx.stc.StyledTextCtrl.GetLayoutCache") and [`SetLayoutCache`](#wx.stc.StyledTextCtrl.SetLayoutCache "wx.stc.StyledTextCtrl.SetLayoutCache")
    Length: int  # `Length`[¶](#wx.stc.StyledTextCtrl.Length "Permalink to this definition")See [`GetLength`](#wx.stc.StyledTextCtrl.GetLength "wx.stc.StyledTextCtrl.GetLength")
    Lexer: int  # `Lexer`[¶](#wx.stc.StyledTextCtrl.Lexer "Permalink to this definition")See [`GetLexer`](#wx.stc.StyledTextCtrl.GetLexer "wx.stc.StyledTextCtrl.GetLexer") and [`SetLexer`](#wx.stc.StyledTextCtrl.SetLexer "wx.stc.StyledTextCtrl.SetLexer")
    LexerLanguage: str  # `LexerLanguage`[¶](#wx.stc.StyledTextCtrl.LexerLanguage "Permalink to this definition")See [`GetLexerLanguage`](#wx.stc.StyledTextCtrl.GetLexerLanguage "wx.stc.StyledTextCtrl.GetLexerLanguage") and [`SetLexerLanguage`](#wx.stc.StyledTextCtrl.SetLexerLanguage "wx.stc.StyledTextCtrl.SetLexerLanguage")
    LineCount: int  # `LineCount`[¶](#wx.stc.StyledTextCtrl.LineCount "Permalink to this definition")See [`GetLineCount`](#wx.stc.StyledTextCtrl.GetLineCount "wx.stc.StyledTextCtrl.GetLineCount")
    LineEndTypesActive: int  # `LineEndTypesActive`[¶](#wx.stc.StyledTextCtrl.LineEndTypesActive "Permalink to this definition")See [`GetLineEndTypesActive`](#wx.stc.StyledTextCtrl.GetLineEndTypesActive "wx.stc.StyledTextCtrl.GetLineEndTypesActive")
    LineEndTypesAllowed: int  # `LineEndTypesAllowed`[¶](#wx.stc.StyledTextCtrl.LineEndTypesAllowed "Permalink to this definition")See [`GetLineEndTypesAllowed`](#wx.stc.StyledTextCtrl.GetLineEndTypesAllowed "wx.stc.StyledTextCtrl.GetLineEndTypesAllowed") and [`SetLineEndTypesAllowed`](#wx.stc.StyledTextCtrl.SetLineEndTypesAllowed "wx.stc.StyledTextCtrl.SetLineEndTypesAllowed")
    LineEndTypesSupported: int  # `LineEndTypesSupported`[¶](#wx.stc.StyledTextCtrl.LineEndTypesSupported "Permalink to this definition")See [`GetLineEndTypesSupported`](#wx.stc.StyledTextCtrl.GetLineEndTypesSupported "wx.stc.StyledTextCtrl.GetLineEndTypesSupported")
    MainSelection: int  # `MainSelection`[¶](#wx.stc.StyledTextCtrl.MainSelection "Permalink to this definition")See [`GetMainSelection`](#wx.stc.StyledTextCtrl.GetMainSelection "wx.stc.StyledTextCtrl.GetMainSelection") and [`SetMainSelection`](#wx.stc.StyledTextCtrl.SetMainSelection "wx.stc.StyledTextCtrl.SetMainSelection")
    MarginCount: int  # `MarginCount`[¶](#wx.stc.StyledTextCtrl.MarginCount "Permalink to this definition")See [`GetMarginCount`](#wx.stc.StyledTextCtrl.GetMarginCount "wx.stc.StyledTextCtrl.GetMarginCount") and [`SetMarginCount`](#wx.stc.StyledTextCtrl.SetMarginCount "wx.stc.StyledTextCtrl.SetMarginCount")
    MarginLeft: int  # `MarginLeft`[¶](#wx.stc.StyledTextCtrl.MarginLeft "Permalink to this definition")See [`GetMarginLeft`](#wx.stc.StyledTextCtrl.GetMarginLeft "wx.stc.StyledTextCtrl.GetMarginLeft") and [`SetMarginLeft`](#wx.stc.StyledTextCtrl.SetMarginLeft "wx.stc.StyledTextCtrl.SetMarginLeft")
    MarginOptions: int  # `MarginOptions`[¶](#wx.stc.StyledTextCtrl.MarginOptions "Permalink to this definition")See [`GetMarginOptions`](#wx.stc.StyledTextCtrl.GetMarginOptions "wx.stc.StyledTextCtrl.GetMarginOptions") and [`SetMarginOptions`](#wx.stc.StyledTextCtrl.SetMarginOptions "wx.stc.StyledTextCtrl.SetMarginOptions")
    MarginRight: int  # `MarginRight`[¶](#wx.stc.StyledTextCtrl.MarginRight "Permalink to this definition")See [`GetMarginRight`](#wx.stc.StyledTextCtrl.GetMarginRight "wx.stc.StyledTextCtrl.GetMarginRight") and [`SetMarginRight`](#wx.stc.StyledTextCtrl.SetMarginRight "wx.stc.StyledTextCtrl.SetMarginRight")
    Margins: 'Point'  # `Margins`[¶](#wx.stc.StyledTextCtrl.Margins "Permalink to this definition")See [`GetMargins`](#wx.stc.StyledTextCtrl.GetMargins "wx.stc.StyledTextCtrl.GetMargins")
    MaxLineState: int  # `MaxLineState`[¶](#wx.stc.StyledTextCtrl.MaxLineState "Permalink to this definition")See [`GetMaxLineState`](#wx.stc.StyledTextCtrl.GetMaxLineState "wx.stc.StyledTextCtrl.GetMaxLineState")
    ModEventMask: int  # `ModEventMask`[¶](#wx.stc.StyledTextCtrl.ModEventMask "Permalink to this definition")See [`GetModEventMask`](#wx.stc.StyledTextCtrl.GetModEventMask "wx.stc.StyledTextCtrl.GetModEventMask") and [`SetModEventMask`](#wx.stc.StyledTextCtrl.SetModEventMask "wx.stc.StyledTextCtrl.SetModEventMask")
    Modify: bool  # `Modify`[¶](#wx.stc.StyledTextCtrl.Modify "Permalink to this definition")See [`GetModify`](#wx.stc.StyledTextCtrl.GetModify "wx.stc.StyledTextCtrl.GetModify")
    MouseDownCaptures: bool  # `MouseDownCaptures`[¶](#wx.stc.StyledTextCtrl.MouseDownCaptures "Permalink to this definition")See [`GetMouseDownCaptures`](#wx.stc.StyledTextCtrl.GetMouseDownCaptures "wx.stc.StyledTextCtrl.GetMouseDownCaptures") and [`SetMouseDownCaptures`](#wx.stc.StyledTextCtrl.SetMouseDownCaptures "wx.stc.StyledTextCtrl.SetMouseDownCaptures")
    MouseDwellTime: int  # `MouseDwellTime`[¶](#wx.stc.StyledTextCtrl.MouseDwellTime "Permalink to this definition")See [`GetMouseDwellTime`](#wx.stc.StyledTextCtrl.GetMouseDwellTime "wx.stc.StyledTextCtrl.GetMouseDwellTime") and [`SetMouseDwellTime`](#wx.stc.StyledTextCtrl.SetMouseDwellTime "wx.stc.StyledTextCtrl.SetMouseDwellTime")
    MouseSelectionRectangularSwitch: bool  # `MouseSelectionRectangularSwitch`[¶](#wx.stc.StyledTextCtrl.MouseSelectionRectangularSwitch "Permalink to this definition")See [`GetMouseSelectionRectangularSwitch`](#wx.stc.StyledTextCtrl.GetMouseSelectionRectangularSwitch "wx.stc.StyledTextCtrl.GetMouseSelectionRectangularSwitch") and [`SetMouseSelectionRectangularSwitch`](#wx.stc.StyledTextCtrl.SetMouseSelectionRectangularSwitch "wx.stc.StyledTextCtrl.SetMouseSelectionRectangularSwitch")
    MouseWheelCaptures: bool  # `MouseWheelCaptures`[¶](#wx.stc.StyledTextCtrl.MouseWheelCaptures "Permalink to this definition")See [`GetMouseWheelCaptures`](#wx.stc.StyledTextCtrl.GetMouseWheelCaptures "wx.stc.StyledTextCtrl.GetMouseWheelCaptures") and [`SetMouseWheelCaptures`](#wx.stc.StyledTextCtrl.SetMouseWheelCaptures "wx.stc.StyledTextCtrl.SetMouseWheelCaptures")
    MultiPaste: int  # `MultiPaste`[¶](#wx.stc.StyledTextCtrl.MultiPaste "Permalink to this definition")See [`GetMultiPaste`](#wx.stc.StyledTextCtrl.GetMultiPaste "wx.stc.StyledTextCtrl.GetMultiPaste") and [`SetMultiPaste`](#wx.stc.StyledTextCtrl.SetMultiPaste "wx.stc.StyledTextCtrl.SetMultiPaste")
    MultipleSelection: bool  # `MultipleSelection`[¶](#wx.stc.StyledTextCtrl.MultipleSelection "Permalink to this definition")See [`GetMultipleSelection`](#wx.stc.StyledTextCtrl.GetMultipleSelection "wx.stc.StyledTextCtrl.GetMultipleSelection") and [`SetMultipleSelection`](#wx.stc.StyledTextCtrl.SetMultipleSelection "wx.stc.StyledTextCtrl.SetMultipleSelection")
    NumberOfLines: int  # `NumberOfLines`[¶](#wx.stc.StyledTextCtrl.NumberOfLines "Permalink to this definition")See [`GetNumberOfLines`](#wx.stc.StyledTextCtrl.GetNumberOfLines "wx.stc.StyledTextCtrl.GetNumberOfLines")
    Overtype: bool  # `Overtype`[¶](#wx.stc.StyledTextCtrl.Overtype "Permalink to this definition")See [`GetOvertype`](#wx.stc.StyledTextCtrl.GetOvertype "wx.stc.StyledTextCtrl.GetOvertype") and [`SetOvertype`](#wx.stc.StyledTextCtrl.SetOvertype "wx.stc.StyledTextCtrl.SetOvertype")
    PasteConvertEndings: bool  # `PasteConvertEndings`[¶](#wx.stc.StyledTextCtrl.PasteConvertEndings "Permalink to this definition")See [`GetPasteConvertEndings`](#wx.stc.StyledTextCtrl.GetPasteConvertEndings "wx.stc.StyledTextCtrl.GetPasteConvertEndings") and [`SetPasteConvertEndings`](#wx.stc.StyledTextCtrl.SetPasteConvertEndings "wx.stc.StyledTextCtrl.SetPasteConvertEndings")
    PhasesDraw: int  # `PhasesDraw`[¶](#wx.stc.StyledTextCtrl.PhasesDraw "Permalink to this definition")See [`GetPhasesDraw`](#wx.stc.StyledTextCtrl.GetPhasesDraw "wx.stc.StyledTextCtrl.GetPhasesDraw") and [`SetPhasesDraw`](#wx.stc.StyledTextCtrl.SetPhasesDraw "wx.stc.StyledTextCtrl.SetPhasesDraw")
    PositionCacheSize: int  # `PositionCacheSize`[¶](#wx.stc.StyledTextCtrl.PositionCacheSize "Permalink to this definition")See [`GetPositionCacheSize`](#wx.stc.StyledTextCtrl.GetPositionCacheSize "wx.stc.StyledTextCtrl.GetPositionCacheSize") and [`SetPositionCacheSize`](#wx.stc.StyledTextCtrl.SetPositionCacheSize "wx.stc.StyledTextCtrl.SetPositionCacheSize")
    PrintColourMode: int  # `PrintColourMode`[¶](#wx.stc.StyledTextCtrl.PrintColourMode "Permalink to this definition")See [`GetPrintColourMode`](#wx.stc.StyledTextCtrl.GetPrintColourMode "wx.stc.StyledTextCtrl.GetPrintColourMode") and [`SetPrintColourMode`](#wx.stc.StyledTextCtrl.SetPrintColourMode "wx.stc.StyledTextCtrl.SetPrintColourMode")
    PrintMagnification: int  # `PrintMagnification`[¶](#wx.stc.StyledTextCtrl.PrintMagnification "Permalink to this definition")See [`GetPrintMagnification`](#wx.stc.StyledTextCtrl.GetPrintMagnification "wx.stc.StyledTextCtrl.GetPrintMagnification") and [`SetPrintMagnification`](#wx.stc.StyledTextCtrl.SetPrintMagnification "wx.stc.StyledTextCtrl.SetPrintMagnification")
    PrintWrapMode: int  # `PrintWrapMode`[¶](#wx.stc.StyledTextCtrl.PrintWrapMode "Permalink to this definition")See [`GetPrintWrapMode`](#wx.stc.StyledTextCtrl.GetPrintWrapMode "wx.stc.StyledTextCtrl.GetPrintWrapMode") and [`SetPrintWrapMode`](#wx.stc.StyledTextCtrl.SetPrintWrapMode "wx.stc.StyledTextCtrl.SetPrintWrapMode")
    PunctuationChars: str  # `PunctuationChars`[¶](#wx.stc.StyledTextCtrl.PunctuationChars "Permalink to this definition")See [`GetPunctuationChars`](#wx.stc.StyledTextCtrl.GetPunctuationChars "wx.stc.StyledTextCtrl.GetPunctuationChars") and [`SetPunctuationChars`](#wx.stc.StyledTextCtrl.SetPunctuationChars "wx.stc.StyledTextCtrl.SetPunctuationChars")
    RangePointer: Any  # `RangePointer`[¶](#wx.stc.StyledTextCtrl.RangePointer "Permalink to this definition")See [`GetRangePointer`](#wx.stc.StyledTextCtrl.GetRangePointer "wx.stc.StyledTextCtrl.GetRangePointer")
    ReadOnly: bool  # `ReadOnly`[¶](#wx.stc.StyledTextCtrl.ReadOnly "Permalink to this definition")See [`GetReadOnly`](#wx.stc.StyledTextCtrl.GetReadOnly "wx.stc.StyledTextCtrl.GetReadOnly") and [`SetReadOnly`](#wx.stc.StyledTextCtrl.SetReadOnly "wx.stc.StyledTextCtrl.SetReadOnly")
    RectangularSelectionAnchor: int  # `RectangularSelectionAnchor`[¶](#wx.stc.StyledTextCtrl.RectangularSelectionAnchor "Permalink to this definition")See [`GetRectangularSelectionAnchor`](#wx.stc.StyledTextCtrl.GetRectangularSelectionAnchor "wx.stc.StyledTextCtrl.GetRectangularSelectionAnchor") and [`SetRectangularSelectionAnchor`](#wx.stc.StyledTextCtrl.SetRectangularSelectionAnchor "wx.stc.StyledTextCtrl.SetRectangularSelectionAnchor")
    RectangularSelectionAnchorVirtualSpace: int  # `RectangularSelectionAnchorVirtualSpace`[¶](#wx.stc.StyledTextCtrl.RectangularSelectionAnchorVirtualSpace "Permalink to this definition")See [`GetRectangularSelectionAnchorVirtualSpace`](#wx.stc.StyledTextCtrl.GetRectangularSelectionAnchorVirtualSpace "wx.stc.StyledTextCtrl.GetRectangularSelectionAnchorVirtualSpace") and [`SetRectangularSelectionAnchorVirtualSpace`](#wx.stc.StyledTextCtrl.SetRectangularSelectionAnchorVirtualSpace "wx.stc.StyledTextCtrl.SetRectangularSelectionAnchorVirtualSpace")
    RectangularSelectionCaret: int  # `RectangularSelectionCaret`[¶](#wx.stc.StyledTextCtrl.RectangularSelectionCaret "Permalink to this definition")See [`GetRectangularSelectionCaret`](#wx.stc.StyledTextCtrl.GetRectangularSelectionCaret "wx.stc.StyledTextCtrl.GetRectangularSelectionCaret") and [`SetRectangularSelectionCaret`](#wx.stc.StyledTextCtrl.SetRectangularSelectionCaret "wx.stc.StyledTextCtrl.SetRectangularSelectionCaret")
    RectangularSelectionCaretVirtualSpace: int  # `RectangularSelectionCaretVirtualSpace`[¶](#wx.stc.StyledTextCtrl.RectangularSelectionCaretVirtualSpace "Permalink to this definition")See [`GetRectangularSelectionCaretVirtualSpace`](#wx.stc.StyledTextCtrl.GetRectangularSelectionCaretVirtualSpace "wx.stc.StyledTextCtrl.GetRectangularSelectionCaretVirtualSpace") and [`SetRectangularSelectionCaretVirtualSpace`](#wx.stc.StyledTextCtrl.SetRectangularSelectionCaretVirtualSpace "wx.stc.StyledTextCtrl.SetRectangularSelectionCaretVirtualSpace")
    RectangularSelectionModifier: int  # `RectangularSelectionModifier`[¶](#wx.stc.StyledTextCtrl.RectangularSelectionModifier "Permalink to this definition")See [`GetRectangularSelectionModifier`](#wx.stc.StyledTextCtrl.GetRectangularSelectionModifier "wx.stc.StyledTextCtrl.GetRectangularSelectionModifier") and [`SetRectangularSelectionModifier`](#wx.stc.StyledTextCtrl.SetRectangularSelectionModifier "wx.stc.StyledTextCtrl.SetRectangularSelectionModifier")
    STCCursor: int  # `STCCursor`[¶](#wx.stc.StyledTextCtrl.STCCursor "Permalink to this definition")See [`GetSTCCursor`](#wx.stc.StyledTextCtrl.GetSTCCursor "wx.stc.StyledTextCtrl.GetSTCCursor") and [`SetSTCCursor`](#wx.stc.StyledTextCtrl.SetSTCCursor "wx.stc.StyledTextCtrl.SetSTCCursor")
    STCFocus: bool  # `STCFocus`[¶](#wx.stc.StyledTextCtrl.STCFocus "Permalink to this definition")See [`GetSTCFocus`](#wx.stc.StyledTextCtrl.GetSTCFocus "wx.stc.StyledTextCtrl.GetSTCFocus") and [`SetSTCFocus`](#wx.stc.StyledTextCtrl.SetSTCFocus "wx.stc.StyledTextCtrl.SetSTCFocus")
    ScrollWidth: int  # `ScrollWidth`[¶](#wx.stc.StyledTextCtrl.ScrollWidth "Permalink to this definition")See [`GetScrollWidth`](#wx.stc.StyledTextCtrl.GetScrollWidth "wx.stc.StyledTextCtrl.GetScrollWidth") and [`SetScrollWidth`](#wx.stc.StyledTextCtrl.SetScrollWidth "wx.stc.StyledTextCtrl.SetScrollWidth")
    ScrollWidthTracking: bool  # `ScrollWidthTracking`[¶](#wx.stc.StyledTextCtrl.ScrollWidthTracking "Permalink to this definition")See [`GetScrollWidthTracking`](#wx.stc.StyledTextCtrl.GetScrollWidthTracking "wx.stc.StyledTextCtrl.GetScrollWidthTracking") and [`SetScrollWidthTracking`](#wx.stc.StyledTextCtrl.SetScrollWidthTracking "wx.stc.StyledTextCtrl.SetScrollWidthTracking")
    SearchFlags: int  # `SearchFlags`[¶](#wx.stc.StyledTextCtrl.SearchFlags "Permalink to this definition")See [`GetSearchFlags`](#wx.stc.StyledTextCtrl.GetSearchFlags "wx.stc.StyledTextCtrl.GetSearchFlags") and [`SetSearchFlags`](#wx.stc.StyledTextCtrl.SetSearchFlags "wx.stc.StyledTextCtrl.SetSearchFlags")
    SelAlpha: int  # `SelAlpha`[¶](#wx.stc.StyledTextCtrl.SelAlpha "Permalink to this definition")See [`GetSelAlpha`](#wx.stc.StyledTextCtrl.GetSelAlpha "wx.stc.StyledTextCtrl.GetSelAlpha") and [`SetSelAlpha`](#wx.stc.StyledTextCtrl.SetSelAlpha "wx.stc.StyledTextCtrl.SetSelAlpha")
    SelEOLFilled: bool  # `SelEOLFilled`[¶](#wx.stc.StyledTextCtrl.SelEOLFilled "Permalink to this definition")See [`GetSelEOLFilled`](#wx.stc.StyledTextCtrl.GetSelEOLFilled "wx.stc.StyledTextCtrl.GetSelEOLFilled") and [`SetSelEOLFilled`](#wx.stc.StyledTextCtrl.SetSelEOLFilled "wx.stc.StyledTextCtrl.SetSelEOLFilled")
    SelectedText: str  # `SelectedText`[¶](#wx.stc.StyledTextCtrl.SelectedText "Permalink to this definition")See [`GetSelectedText`](#wx.stc.StyledTextCtrl.GetSelectedText "wx.stc.StyledTextCtrl.GetSelectedText")
    SelectedTextRaw: 'CharBuffer'  # `SelectedTextRaw`[¶](#wx.stc.StyledTextCtrl.SelectedTextRaw "Permalink to this definition")See [`GetSelectedTextRaw`](#wx.stc.StyledTextCtrl.GetSelectedTextRaw "wx.stc.StyledTextCtrl.GetSelectedTextRaw")
    SelectionEmpty: bool  # `SelectionEmpty`[¶](#wx.stc.StyledTextCtrl.SelectionEmpty "Permalink to this definition")See [`GetSelectionEmpty`](#wx.stc.StyledTextCtrl.GetSelectionEmpty "wx.stc.StyledTextCtrl.GetSelectionEmpty")
    SelectionEnd: int  # `SelectionEnd`[¶](#wx.stc.StyledTextCtrl.SelectionEnd "Permalink to this definition")See [`GetSelectionEnd`](#wx.stc.StyledTextCtrl.GetSelectionEnd "wx.stc.StyledTextCtrl.GetSelectionEnd") and [`SetSelectionEnd`](#wx.stc.StyledTextCtrl.SetSelectionEnd "wx.stc.StyledTextCtrl.SetSelectionEnd")
    SelectionMode: int  # `SelectionMode`[¶](#wx.stc.StyledTextCtrl.SelectionMode "Permalink to this definition")See [`GetSelectionMode`](#wx.stc.StyledTextCtrl.GetSelectionMode "wx.stc.StyledTextCtrl.GetSelectionMode") and [`SetSelectionMode`](#wx.stc.StyledTextCtrl.SetSelectionMode "wx.stc.StyledTextCtrl.SetSelectionMode")
    SelectionStart: int  # `SelectionStart`[¶](#wx.stc.StyledTextCtrl.SelectionStart "Permalink to this definition")See [`GetSelectionStart`](#wx.stc.StyledTextCtrl.GetSelectionStart "wx.stc.StyledTextCtrl.GetSelectionStart") and [`SetSelectionStart`](#wx.stc.StyledTextCtrl.SetSelectionStart "wx.stc.StyledTextCtrl.SetSelectionStart")
    Selections: int  # `Selections`[¶](#wx.stc.StyledTextCtrl.Selections "Permalink to this definition")See [`GetSelections`](#wx.stc.StyledTextCtrl.GetSelections "wx.stc.StyledTextCtrl.GetSelections")
    Status: int  # `Status`[¶](#wx.stc.StyledTextCtrl.Status "Permalink to this definition")See [`GetStatus`](#wx.stc.StyledTextCtrl.GetStatus "wx.stc.StyledTextCtrl.GetStatus") and [`SetStatus`](#wx.stc.StyledTextCtrl.SetStatus "wx.stc.StyledTextCtrl.SetStatus")
    StringSelection: str  # `StringSelection`[¶](#wx.stc.StyledTextCtrl.StringSelection "Permalink to this definition")See [`GetStringSelection`](#wx.stc.StyledTextCtrl.GetStringSelection "wx.stc.StyledTextCtrl.GetStringSelection")
    StyleBits: int  # `StyleBits`[¶](#wx.stc.StyledTextCtrl.StyleBits "Permalink to this definition")See [`GetStyleBits`](#wx.stc.StyledTextCtrl.GetStyleBits "wx.stc.StyledTextCtrl.GetStyleBits") and [`SetStyleBits`](#wx.stc.StyledTextCtrl.SetStyleBits "wx.stc.StyledTextCtrl.SetStyleBits")
    StyleBitsNeeded: int  # `StyleBitsNeeded`[¶](#wx.stc.StyledTextCtrl.StyleBitsNeeded "Permalink to this definition")See [`GetStyleBitsNeeded`](#wx.stc.StyledTextCtrl.GetStyleBitsNeeded "wx.stc.StyledTextCtrl.GetStyleBitsNeeded")
    SubStyleBases: str  # `SubStyleBases`[¶](#wx.stc.StyledTextCtrl.SubStyleBases "Permalink to this definition")See [`GetSubStyleBases`](#wx.stc.StyledTextCtrl.GetSubStyleBases "wx.stc.StyledTextCtrl.GetSubStyleBases")
    TabDrawMode: int  # `TabDrawMode`[¶](#wx.stc.StyledTextCtrl.TabDrawMode "Permalink to this definition")See [`GetTabDrawMode`](#wx.stc.StyledTextCtrl.GetTabDrawMode "wx.stc.StyledTextCtrl.GetTabDrawMode") and [`SetTabDrawMode`](#wx.stc.StyledTextCtrl.SetTabDrawMode "wx.stc.StyledTextCtrl.SetTabDrawMode")
    TabIndents: bool  # `TabIndents`[¶](#wx.stc.StyledTextCtrl.TabIndents "Permalink to this definition")See [`GetTabIndents`](#wx.stc.StyledTextCtrl.GetTabIndents "wx.stc.StyledTextCtrl.GetTabIndents") and [`SetTabIndents`](#wx.stc.StyledTextCtrl.SetTabIndents "wx.stc.StyledTextCtrl.SetTabIndents")
    TabWidth: int  # `TabWidth`[¶](#wx.stc.StyledTextCtrl.TabWidth "Permalink to this definition")See [`GetTabWidth`](#wx.stc.StyledTextCtrl.GetTabWidth "wx.stc.StyledTextCtrl.GetTabWidth") and [`SetTabWidth`](#wx.stc.StyledTextCtrl.SetTabWidth "wx.stc.StyledTextCtrl.SetTabWidth")
    TargetEnd: int  # `TargetEnd`[¶](#wx.stc.StyledTextCtrl.TargetEnd "Permalink to this definition")See [`GetTargetEnd`](#wx.stc.StyledTextCtrl.GetTargetEnd "wx.stc.StyledTextCtrl.GetTargetEnd") and [`SetTargetEnd`](#wx.stc.StyledTextCtrl.SetTargetEnd "wx.stc.StyledTextCtrl.SetTargetEnd")
    TargetStart: int  # `TargetStart`[¶](#wx.stc.StyledTextCtrl.TargetStart "Permalink to this definition")See [`GetTargetStart`](#wx.stc.StyledTextCtrl.GetTargetStart "wx.stc.StyledTextCtrl.GetTargetStart") and [`SetTargetStart`](#wx.stc.StyledTextCtrl.SetTargetStart "wx.stc.StyledTextCtrl.SetTargetStart")
    TargetText: str  # `TargetText`[¶](#wx.stc.StyledTextCtrl.TargetText "Permalink to this definition")See [`GetTargetText`](#wx.stc.StyledTextCtrl.GetTargetText "wx.stc.StyledTextCtrl.GetTargetText")
    TargetTextRaw: 'CharBuffer'  # `TargetTextRaw`[¶](#wx.stc.StyledTextCtrl.TargetTextRaw "Permalink to this definition")See [`GetTargetTextRaw`](#wx.stc.StyledTextCtrl.GetTargetTextRaw "wx.stc.StyledTextCtrl.GetTargetTextRaw")
    Technology: int  # `Technology`[¶](#wx.stc.StyledTextCtrl.Technology "Permalink to this definition")See [`GetTechnology`](#wx.stc.StyledTextCtrl.GetTechnology "wx.stc.StyledTextCtrl.GetTechnology") and [`SetTechnology`](#wx.stc.StyledTextCtrl.SetTechnology "wx.stc.StyledTextCtrl.SetTechnology")
    Text: str  # `Text`[¶](#wx.stc.StyledTextCtrl.Text "Permalink to this definition")See [`GetText`](#wx.stc.StyledTextCtrl.GetText "wx.stc.StyledTextCtrl.GetText") and [`SetText`](#wx.stc.StyledTextCtrl.SetText "wx.stc.StyledTextCtrl.SetText")
    TextLength: int  # `TextLength`[¶](#wx.stc.StyledTextCtrl.TextLength "Permalink to this definition")See [`GetTextLength`](#wx.stc.StyledTextCtrl.GetTextLength "wx.stc.StyledTextCtrl.GetTextLength")
    TextRaw: 'CharBuffer'  # `TextRaw`[¶](#wx.stc.StyledTextCtrl.TextRaw "Permalink to this definition")See [`GetTextRaw`](#wx.stc.StyledTextCtrl.GetTextRaw "wx.stc.StyledTextCtrl.GetTextRaw") and [`SetTextRaw`](#wx.stc.StyledTextCtrl.SetTextRaw "wx.stc.StyledTextCtrl.SetTextRaw")
    TwoPhaseDraw: bool  # `TwoPhaseDraw`[¶](#wx.stc.StyledTextCtrl.TwoPhaseDraw "Permalink to this definition")See [`GetTwoPhaseDraw`](#wx.stc.StyledTextCtrl.GetTwoPhaseDraw "wx.stc.StyledTextCtrl.GetTwoPhaseDraw") and [`SetTwoPhaseDraw`](#wx.stc.StyledTextCtrl.SetTwoPhaseDraw "wx.stc.StyledTextCtrl.SetTwoPhaseDraw")
    UndoCollection: bool  # `UndoCollection`[¶](#wx.stc.StyledTextCtrl.UndoCollection "Permalink to this definition")See [`GetUndoCollection`](#wx.stc.StyledTextCtrl.GetUndoCollection "wx.stc.StyledTextCtrl.GetUndoCollection") and [`SetUndoCollection`](#wx.stc.StyledTextCtrl.SetUndoCollection "wx.stc.StyledTextCtrl.SetUndoCollection")
    UseAntiAliasing: bool  # `UseAntiAliasing`[¶](#wx.stc.StyledTextCtrl.UseAntiAliasing "Permalink to this definition")See [`GetUseAntiAliasing`](#wx.stc.StyledTextCtrl.GetUseAntiAliasing "wx.stc.StyledTextCtrl.GetUseAntiAliasing") and [`SetUseAntiAliasing`](#wx.stc.StyledTextCtrl.SetUseAntiAliasing "wx.stc.StyledTextCtrl.SetUseAntiAliasing")
    UseHorizontalScrollBar: bool  # `UseHorizontalScrollBar`[¶](#wx.stc.StyledTextCtrl.UseHorizontalScrollBar "Permalink to this definition")See [`GetUseHorizontalScrollBar`](#wx.stc.StyledTextCtrl.GetUseHorizontalScrollBar "wx.stc.StyledTextCtrl.GetUseHorizontalScrollBar") and [`SetUseHorizontalScrollBar`](#wx.stc.StyledTextCtrl.SetUseHorizontalScrollBar "wx.stc.StyledTextCtrl.SetUseHorizontalScrollBar")
    UseTabs: bool  # `UseTabs`[¶](#wx.stc.StyledTextCtrl.UseTabs "Permalink to this definition")See [`GetUseTabs`](#wx.stc.StyledTextCtrl.GetUseTabs "wx.stc.StyledTextCtrl.GetUseTabs") and [`SetUseTabs`](#wx.stc.StyledTextCtrl.SetUseTabs "wx.stc.StyledTextCtrl.SetUseTabs")
    UseVerticalScrollBar: bool  # `UseVerticalScrollBar`[¶](#wx.stc.StyledTextCtrl.UseVerticalScrollBar "Permalink to this definition")See [`GetUseVerticalScrollBar`](#wx.stc.StyledTextCtrl.GetUseVerticalScrollBar "wx.stc.StyledTextCtrl.GetUseVerticalScrollBar") and [`SetUseVerticalScrollBar`](#wx.stc.StyledTextCtrl.SetUseVerticalScrollBar "wx.stc.StyledTextCtrl.SetUseVerticalScrollBar")
    Value: str  # `Value`[¶](#wx.stc.StyledTextCtrl.Value "Permalink to this definition")See [`GetValue`](#wx.stc.StyledTextCtrl.GetValue "wx.stc.StyledTextCtrl.GetValue") and [`SetValue`](#wx.stc.StyledTextCtrl.SetValue "wx.stc.StyledTextCtrl.SetValue")
    ViewEOL: bool  # `ViewEOL`[¶](#wx.stc.StyledTextCtrl.ViewEOL "Permalink to this definition")See [`GetViewEOL`](#wx.stc.StyledTextCtrl.GetViewEOL "wx.stc.StyledTextCtrl.GetViewEOL") and [`SetViewEOL`](#wx.stc.StyledTextCtrl.SetViewEOL "wx.stc.StyledTextCtrl.SetViewEOL")
    ViewWhiteSpace: int  # `ViewWhiteSpace`[¶](#wx.stc.StyledTextCtrl.ViewWhiteSpace "Permalink to this definition")See [`GetViewWhiteSpace`](#wx.stc.StyledTextCtrl.GetViewWhiteSpace "wx.stc.StyledTextCtrl.GetViewWhiteSpace") and [`SetViewWhiteSpace`](#wx.stc.StyledTextCtrl.SetViewWhiteSpace "wx.stc.StyledTextCtrl.SetViewWhiteSpace")
    VirtualSpaceOptions: int  # `VirtualSpaceOptions`[¶](#wx.stc.StyledTextCtrl.VirtualSpaceOptions "Permalink to this definition")See [`GetVirtualSpaceOptions`](#wx.stc.StyledTextCtrl.GetVirtualSpaceOptions "wx.stc.StyledTextCtrl.GetVirtualSpaceOptions") and [`SetVirtualSpaceOptions`](#wx.stc.StyledTextCtrl.SetVirtualSpaceOptions "wx.stc.StyledTextCtrl.SetVirtualSpaceOptions")
    WhitespaceChars: str  # `WhitespaceChars`[¶](#wx.stc.StyledTextCtrl.WhitespaceChars "Permalink to this definition")See [`GetWhitespaceChars`](#wx.stc.StyledTextCtrl.GetWhitespaceChars "wx.stc.StyledTextCtrl.GetWhitespaceChars") and [`SetWhitespaceChars`](#wx.stc.StyledTextCtrl.SetWhitespaceChars "wx.stc.StyledTextCtrl.SetWhitespaceChars")
    WhitespaceSize: int  # `WhitespaceSize`[¶](#wx.stc.StyledTextCtrl.WhitespaceSize "Permalink to this definition")See [`GetWhitespaceSize`](#wx.stc.StyledTextCtrl.GetWhitespaceSize "wx.stc.StyledTextCtrl.GetWhitespaceSize") and [`SetWhitespaceSize`](#wx.stc.StyledTextCtrl.SetWhitespaceSize "wx.stc.StyledTextCtrl.SetWhitespaceSize")
    WordChars: str  # `WordChars`[¶](#wx.stc.StyledTextCtrl.WordChars "Permalink to this definition")See [`GetWordChars`](#wx.stc.StyledTextCtrl.GetWordChars "wx.stc.StyledTextCtrl.GetWordChars") and [`SetWordChars`](#wx.stc.StyledTextCtrl.SetWordChars "wx.stc.StyledTextCtrl.SetWordChars")
    WrapIndentMode: int  # `WrapIndentMode`[¶](#wx.stc.StyledTextCtrl.WrapIndentMode "Permalink to this definition")See [`GetWrapIndentMode`](#wx.stc.StyledTextCtrl.GetWrapIndentMode "wx.stc.StyledTextCtrl.GetWrapIndentMode") and [`SetWrapIndentMode`](#wx.stc.StyledTextCtrl.SetWrapIndentMode "wx.stc.StyledTextCtrl.SetWrapIndentMode")
    WrapMode: int  # `WrapMode`[¶](#wx.stc.StyledTextCtrl.WrapMode "Permalink to this definition")See [`GetWrapMode`](#wx.stc.StyledTextCtrl.GetWrapMode "wx.stc.StyledTextCtrl.GetWrapMode") and [`SetWrapMode`](#wx.stc.StyledTextCtrl.SetWrapMode "wx.stc.StyledTextCtrl.SetWrapMode")
    WrapStartIndent: int  # `WrapStartIndent`[¶](#wx.stc.StyledTextCtrl.WrapStartIndent "Permalink to this definition")See [`GetWrapStartIndent`](#wx.stc.StyledTextCtrl.GetWrapStartIndent "wx.stc.StyledTextCtrl.GetWrapStartIndent") and [`SetWrapStartIndent`](#wx.stc.StyledTextCtrl.SetWrapStartIndent "wx.stc.StyledTextCtrl.SetWrapStartIndent")
    WrapVisualFlags: int  # `WrapVisualFlags`[¶](#wx.stc.StyledTextCtrl.WrapVisualFlags "Permalink to this definition")See [`GetWrapVisualFlags`](#wx.stc.StyledTextCtrl.GetWrapVisualFlags "wx.stc.StyledTextCtrl.GetWrapVisualFlags") and [`SetWrapVisualFlags`](#wx.stc.StyledTextCtrl.SetWrapVisualFlags "wx.stc.StyledTextCtrl.SetWrapVisualFlags")
    WrapVisualFlagsLocation: int  # `WrapVisualFlagsLocation`[¶](#wx.stc.StyledTextCtrl.WrapVisualFlagsLocation "Permalink to this definition")See [`GetWrapVisualFlagsLocation`](#wx.stc.StyledTextCtrl.GetWrapVisualFlagsLocation "wx.stc.StyledTextCtrl.GetWrapVisualFlagsLocation") and [`SetWrapVisualFlagsLocation`](#wx.stc.StyledTextCtrl.SetWrapVisualFlagsLocation "wx.stc.StyledTextCtrl.SetWrapVisualFlagsLocation")
    XOffset: int  # `XOffset`[¶](#wx.stc.StyledTextCtrl.XOffset "Permalink to this definition")See [`GetXOffset`](#wx.stc.StyledTextCtrl.GetXOffset "wx.stc.StyledTextCtrl.GetXOffset") and [`SetXOffset`](#wx.stc.StyledTextCtrl.SetXOffset "wx.stc.StyledTextCtrl.SetXOffset")
    Zoom: int  # `Zoom`[¶](#wx.stc.StyledTextCtrl.Zoom "Permalink to this definition")See [`GetZoom`](#wx.stc.StyledTextCtrl.GetZoom "wx.stc.StyledTextCtrl.GetZoom") and [`SetZoom`](#wx.stc.StyledTextCtrl.SetZoom "wx.stc.StyledTextCtrl.SetZoom")



STC_INVALID_POSITION: int

STC_STYLE_CALLTIP: int

STC_MOD_INSERTCHECK: int

STC_EOL_CRLF: int

STC_EOL_CR: int

STC_EOL_LF: int

TE_READONLY: int

OK: int

STC_UNDO_MAY_COALESCE: int

STC_MODEVENTMASKALL: int

STC_MULTILINEUNDOREDO: int

STC_MULTISTEPUNDOREDO: int

STC_LASTSTEPINUNDOREDO: int

STC_TIME_FOREVER: int

STC_WRAPINDENT_FIXED: int

STC_TECHNOLOGY_DIRECTWRITE: int

STC_MARGIN_COLOUR: int

STC_KEYMOD_CTRL: int

STC_KEYMOD_ALT: int

STC_KEYMOD_SUPER: int

STC_TECHNOLOGY_DEFAULT: int

STC_POPUP_NEVER: int

CharBuffer: TypeAlias = Any

