# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class UltimateListTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.


This is a subclass of [`ExpandoTextCtrl`](wx.lib.expando.ExpandoTextCtrl.html#wx.lib.expando.ExpandoTextCtrl "wx.lib.expando.ExpandoTextCtrl") as [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
supports multiline text items.



Note


To add a newline character in a multiline item, press `Shift` + `Enter`
as the `Enter` key alone is consumed by [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") to finish
the editing and `Ctrl` + `Enter` is consumed by the platform for tab navigation.



  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
    """
    def __init__(self, owner, itemEdit) -> None:
        """ 

`__init__`(*self*, *owner*, *itemEdit*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **owner** – the control parent (an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") );
* **itemEdit** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ 

`AcceptChanges`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.AcceptChanges "Permalink to this definition")
Accepts/refuses the changes made by the user.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def Finish(self) -> None:
        """ 

`Finish`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.Finish "Permalink to this definition")
Finish editing.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.OnChar "Permalink to this definition")
Handles the `wx.EVT_CHAR` event for [`UltimateListTextCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`UltimateListTextCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`UltimateListTextCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ 

`StopEditing`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.StopEditing "Permalink to this definition")
Suddenly stops the editing.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

EVT_KILL_FOCUS: int

class UltimateListCtrl(Control):
    """ UltimateListCtrl is a class that mimics the behaviour of `ListCtrl`, with almost
the same base functionalities plus some more enhancements. This class does
not rely on the native control, as it is a full owner-drawn list control.


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, validator=wx.DefaultValidator, name="UltimateListCtrl") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=0*, *validator=wx.DefaultValidator*, *name="UltimateListCtrl"*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – parent window. Must not be `None`;
* **id** – window identifier. A value of -1 indicates a default value;
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the underlying [`wx.Control`](wx.Control.html#wx.Control "wx.Control") window style;
* **agwStyle** – the AGW-specific window style; can be almost any combination of the following
bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `ULC_VRULES` | 0x1 | Draws light vertical rules between rows in report mode. |
| `ULC_HRULES` | 0x2 | Draws light horizontal rules between rows in report mode. |
| `ULC_ICON` | 0x4 | Large icon view, with optional labels. |
| `ULC_SMALL_ICON` | 0x8 | Small icon view, with optional labels. |
| `ULC_LIST` | 0x10 | Multicolumn list view, with optional small icons. Columns are computed automatically, i.e. you don’t set columns as in `ULC_REPORT`. In other words, the list wraps, unlike a `ListBox`. |
| `ULC_REPORT` | 0x20 | Single or multicolumn report view, with optional header. |
| `ULC_ALIGN_TOP` | 0x40 | Icons align to the top. Win32 default, Win32 only. |
| `ULC_ALIGN_LEFT` | 0x80 | Icons align to the left. |
| `ULC_AUTOARRANGE` | 0x100 | Icons arrange themselves. Win32 only. |
| `ULC_VIRTUAL` | 0x200 | The application provides items text on demand. May only be used with `ULC_REPORT`. |
| `ULC_EDIT_LABELS` | 0x400 | Labels are editable: the application will be notified when editing starts. |
| `ULC_NO_HEADER` | 0x800 | No header in report mode. |
| `ULC_NO_SORT_HEADER` | 0x1000 | No Docs. |
| `ULC_SINGLE_SEL` | 0x2000 | Single selection (default is multiple). |
| `ULC_SORT_ASCENDING` | 0x4000 | Sort in ascending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_SORT_DESCENDING` | 0x8000 | Sort in descending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_TILE` | 0x10000 | Each item appears as a full-sized icon with a label of one or more lines beside it (partially implemented). |
| `ULC_NO_HIGHLIGHT` | 0x20000 | No highlight when an item is selected. |
| `ULC_STICKY_HIGHLIGHT` | 0x40000 | Items are selected by simply hovering on them, with no need to click on them. |
| `ULC_STICKY_NOSELEVENT` | 0x80000 | Don’t send a selection event when using `ULC_STICKY_HIGHLIGHT` style. |
| `ULC_SEND_LEFTCLICK` | 0x100000 | Send a left click event when an item is selected. |
| `ULC_HAS_VARIABLE_ROW_HEIGHT` | 0x200000 | The list has variable row heights. |
| `ULC_AUTO_CHECK_CHILD` | 0x400000 | When a column header has a checkbox associated, auto-check all the subitems in that column. |
| `ULC_AUTO_TOGGLE_CHILD` | 0x800000 | When a column header has a checkbox associated, toggle all the subitems in that column. |
| `ULC_AUTO_CHECK_PARENT` | 0x1000000 | Only meaningful foe checkbox-type items: when an item is checked/unchecked its column header item is checked/unchecked as well. |
| `ULC_SHOW_TOOLTIPS` | 0x2000000 | Show tooltips for ellipsized items/subitems (text too long to be shown in the available space) containing the full item/subitem text. |
| `ULC_HOT_TRACKING` | 0x4000000 | Enable hot tracking of items on mouse motion. |
| `ULC_BORDER_SELECT` | 0x8000000 | Changes border colour when an item is selected, instead of highlighting the item. |
| `ULC_TRACK_SELECT` | 0x10000000 | Enables hot-track selection in a list control. Hot track selection means that an item is automatically selected when the cursor remains over the item for a certain period of time. The delay is retrieved on Windows using the `win32api` call *win32gui.SystemParametersInfo(win32con.SPI\_GETMOUSEHOVERTIME)*, and is defaulted to 400ms on other platforms. This style applies to all views of [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). |
| `ULC_HEADER_IN_ALL_VIEWS` | 0x20000000 | Show column headers in all view modes. |
| `ULC_NO_FULL_ROW_SELECT` | 0x40000000 | When an item is selected, the only the item in the first column is highlighted. |
| `ULC_FOOTER` | 0x80000000 | Show a footer too (only when header is present). |
| `ULC_USER_ROW_HEIGHT` | 0x100000000 | Allows to set a custom row height (one value for all the items, only in report mode). |
* **validator** – the window validator;
* **name** – the window name.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Append(self, entry: Any) -> None:
        """ 

`Append`(*self*, *entry*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Append "Permalink to this definition")
Append an item to the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**entry** – should be a sequence with an item for each column.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Arrange(self, flag: ULC_ALIGN_DEFAULT) -> None:
        """ 

`Arrange`(*self*, *flag*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Arrange "Permalink to this definition")
Arranges the items in icon or small icon view.



Parameters
**flag** – one of the following bits:






| Alignment Flag | Hex Value | Description |
| --- | --- | --- |
| `ULC_ALIGN_DEFAULT` | 0x0 | Default alignment |
| `ULC_ALIGN_SNAP_TO_GRID` | 0x3 | Snap to grid |








Note


This method is currently unimplemented and does nothing.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def AssignImageList(self, imageList, which) -> None:
        """ 

`AssignImageList`(*self*, *imageList*, *which*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.AssignImageList "Permalink to this definition")
Assigns the image list associated with the control.



Parameters
* **imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList") or an instance of [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList");
* **which** – one of `wx.IMAGE_LIST_NORMAL`, `wx.IMAGE_LIST_SMALL`,
`wx.IMAGE_LIST_STATE` (the last is unimplemented).





Note


Using [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") enables you to have images of different size inside the
image list. In your derived class, instead of doing this:



```
imageList = wx.ImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```


You should do this:



```
imageList = PyImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClearAll(self) -> None:
        """ 

`ClearAll`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ClearAll "Permalink to this definition")
Deletes everything in [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClearColumnImage(self, col: Any) -> None:
        """ 

`ClearColumnImage`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ClearColumnImage "Permalink to this definition")
Clears all the images in the specified column.



Parameters
**col** – the column index;






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClientToScreen(self, x: int, y: int) -> None:
        """ 

`ClientToScreen`(*self*, *pointOrTuple*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ClientToScreen "Permalink to this definition")
Converts to screen coordinates from coordinates relative to this window.



Parameters
**pointOrTuple** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point") or a tuple representing the
*x*, *y* coordinates for this point.



Returns
the coordinates relative to the screen.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ClientToScreenXY(self, x, y) -> None:
        """ 

`ClientToScreenXY`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ClientToScreenXY "Permalink to this definition")
Converts to screen coordinates from coordinates relative to this window.



Parameters
* **x** – an integer specifying the *x* client coordinate;
* **y** – an integer specifying the *y* client coordinate.



Returns
the coordinates relative to the screen.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def CreateOrDestroyFooterWindowAsNeeded(self) -> None:
        """ 

`CreateOrDestroyFooterWindowAsNeeded`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.CreateOrDestroyFooterWindowAsNeeded "Permalink to this definition")
Creates or destroys the footer window depending on the window style flags.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def CreateOrDestroyHeaderWindowAsNeeded(self) -> None:
        """ 

`CreateOrDestroyHeaderWindowAsNeeded`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.CreateOrDestroyHeaderWindowAsNeeded "Permalink to this definition")
Creates or destroys the header window depending on the window style flags.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteAllColumns(self) -> None:
        """ 

`DeleteAllColumns`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteAllColumns "Permalink to this definition")
Deletes all the column in [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteAllItems "Permalink to this definition")
Deletes all items in the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Note


This function does not send the `EVT_LIST_DELETE_ITEM` event because
deleting many items from the control would be too slow then (unlike [`DeleteItem`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteItem "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteItem")).





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteColumn(self, col: Any) -> None:
        """ 

`DeleteColumn`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteColumn "Permalink to this definition")
Deletes the specified column.



Parameters
**col** – the index of the column to delete.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteItem(self, item: Any) -> None:
        """ 

`DeleteItem`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteItem "Permalink to this definition")
Deletes the specified item.



Parameters
**item** – the index of the item to delete.





Note


This function sends the `EVT_LIST_DELETE_ITEM` event for the item
being deleted.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DeleteItemWindow(self, itemOrId, col=0) -> None:
        """ 

`DeleteItemWindow`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DeleteItemWindow "Permalink to this definition")
Deletes the window associated to an item (if any).



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same size
as it would have after a call to *Fit()*.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def DoLayout(self) -> None:
        """ 

`DoLayout`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.DoLayout "Permalink to this definition")
Layouts the header, main and footer windows. This is an auxiliary method to avoid code
duplication.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EditLabel(self, item: Any) -> None:
        """ 

`EditLabel`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.EditLabel "Permalink to this definition")
Starts editing an item label.



Parameters
**item** – the index of the item to edit.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableItem(self, itemOrId, col=0, enable=True) -> None:
        """ 

`EnableItem`(*self*, *itemOrId*, *col=0*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.EnableItem "Permalink to this definition")
Enables/disables an item.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **enable** – `True` to enable the item, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ 

`EnableSelectionGradient`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.EnableSelectionGradient "Permalink to this definition")
Globally enables/disables drawing of gradient selections.



Parameters
**enable** – `True` to enable gradient-style selections, `False`
to disable it.





Note


Calling this method disables any Vista-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ 

`EnableSelectionVista`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.EnableSelectionVista "Permalink to this definition")
Globally enables/disables drawing of Windows Vista selections.



Parameters
**enable** – `True` to enable Vista-style selections, `False` to
disable it.





Note


Calling this method disables any gradient-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def EnsureVisible(self, item) -> None:
        """ 

`EnsureVisible`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.EnsureVisible "Permalink to this definition")
Ensures this item is visible.



Parameters
**index** – the index of the item to scroll into view.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItem(self, start, str, partial=False) -> None:
        """ 

`FindItem`(*self*, *start*, *str*, *partial=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.FindItem "Permalink to this definition")
Find an item whose label matches this string.



Parameters
* **start** – the starting point of the input `string` or the beginning
if *start* is -1;
* **string** – the string to look for matches;
* **partial** – if `True` then this method will look for items which
begin with `string`.





Note


The string comparison is case insensitive.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItemAtPos(self, start, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`FindItemAtPos`(*self*, *start*, *pt*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.FindItemAtPos "Permalink to this definition")
Find an item nearest this position.



Parameters
**pt** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def FindItemData(self, start, data) -> None:
        """ 

`FindItemData`(*self*, *start*, *data*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.FindItemData "Permalink to this definition")
Find an item whose data matches this data.



Parameters
* **start** – the starting point of the input *data* or the beginning
if *start* is -1;
* **data** – the data to look for matches.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Focus(self, idx: Any) -> None:
        """ 

`Focus`(*self*, *idx*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Focus "Permalink to this definition")
Focus and show the given item.



Parameters
**idx** – the index of the item to be focused.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ 

`GetAGWWindowStyleFlag`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetAGWWindowStyleFlag "Permalink to this definition")
Returns the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") AGW-specific style flag.



See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag") for a list of possible style flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetBackgroundColour(self) -> None:
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetBackgroundColour "Permalink to this definition")
Returns the background colour of the window.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetBackgroundImage(self) -> None:
        """ 

`GetBackgroundImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetBackgroundImage "Permalink to this definition")
Returns the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") background image (if any).



Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetCheckedItemCount(self, col=0) -> int:
        """ 

`GetCheckedItemCount`(*self*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetCheckedItemCount "Permalink to this definition")
Returns the number of checked items in the given column.



Parameters
**'col'** – an integer specifying the column index.



Returns
the number of checked items.



Return type
int






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetClassDefaultAttributes(self, variant) -> None:
        """ 

`GetClassDefaultAttributes`(*self*, *variant*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetClassDefaultAttributes "Permalink to this definition")
Returns the default font and colours which are used by the control. This is
useful if you want to use the same font or colour in your own control as in
a standard control – which is a much better idea than hard coding specific
colours or fonts which might look completely out of place on the users system,
especially if it uses themes.


This static method is “overridden’’ in many derived classes and so calling,
for example, `Button.GetClassDefaultAttributes` () will typically return the
values appropriate for a button which will be normally different from those
returned by, say, `ListCtrl.GetClassDefaultAttributes` ().



Note


The `VisualAttributes` structure has at least the fields *font*,
*colFg* and *colBg*. All of them may be invalid if it was not possible to
determine the default control appearance or, especially for the background
colour, if the field doesn’t make sense as is the case for *colBg* for the
controls with themed background.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumn(self, col: Any) -> None:
        """ 

`GetColumn`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetColumn "Permalink to this definition")
Returns information about this column.



Parameters
**col** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumnCount(self) -> None:
        """ 

`GetColumnCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetColumnCount "Permalink to this definition")
Returns the total number of columns in the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetColumnWidth(self, col: Any) -> None:
        """ 

`GetColumnWidth`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetColumnWidth "Permalink to this definition")
Returns the column width for the input column.



Parameters
**col** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetCountPerPage(self) -> None:
        """ 

`GetCountPerPage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetCountPerPage "Permalink to this definition")
Returns the number of items that can fit vertically in the visible area
of the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") (list or report view) or the total number of
items in the list control (icon or small icon view).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDefaultBorder(self) -> None:
        """ 

`GetDefaultBorder`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetDefaultBorder "Permalink to this definition")
Returns the default window border.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDisabledTextColour(self) -> None:
        """ 

`GetDisabledTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetDisabledTextColour "Permalink to this definition")
Returns the items disabled colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetDropTarget(self) -> None:
        """ 

`GetDropTarget`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetDropTarget "Permalink to this definition")
Returns the associated drop target, which may be `None`.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetEditControl(self) -> None:
        """ 

`GetEditControl`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetEditControl "Permalink to this definition")
Returns a pointer to the edit [`UltimateListTextCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl") if the item is being edited or
`None` otherwise (it is assumed that no more than one item may be edited
simultaneously).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFirstGradientColour(self) -> None:
        """ 

`GetFirstGradientColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetFirstGradientColour "Permalink to this definition")
Returns the first gradient colour for gradient-style selections.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFirstSelected(self) -> None:
        """ 

`GetFirstSelected`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetFirstSelected "Permalink to this definition")
Return first selected item, or -1 when none is selected.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFocusedItem(self) -> None:
        """ 

`GetFocusedItem`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetFocusedItem "Permalink to this definition")
Returns the currently focused item or -1 if none is focused.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetFooterHeight(self) -> None:
        """ 

`GetFooterHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetFooterHeight "Permalink to this definition")
Returns the [`UltimateListHeaderWindow`](wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetForegroundColour(self) -> None:
        """ 

`GetForegroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetForegroundColour "Permalink to this definition")
Returns the foreground colour of the window.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetGradientStyle(self) -> None:
        """ 

`GetGradientStyle`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetGradientStyle "Permalink to this definition")
Returns the gradient style for gradient-style selections.



Returns
0 for horizontal gradient-style selections, 1 for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHeaderHeight(self) -> None:
        """ 

`GetHeaderHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetHeaderHeight "Permalink to this definition")
Returns the [`UltimateListHeaderWindow`](wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextFont(self) -> None:
        """ 

`GetHyperTextFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetHyperTextFont "Permalink to this definition")
Returns the font used to render an hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ 

`GetHyperTextNewColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetHyperTextNewColour "Permalink to this definition")
Returns the colour used to render a non-visited hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ 

`GetHyperTextVisitedColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetHyperTextVisitedColour "Permalink to this definition")
Returns the colour used to render a visited hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetImageList(self, which: 'IMAGE_LIST_NORMAL') -> None:
        """ 

`GetImageList`(*self*, *which*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetImageList "Permalink to this definition")
Returns the image list associated with the control.



Parameters
**which** – one of `wx.IMAGE_LIST_NORMAL`, `wx.IMAGE_LIST_SMALL`,
`wx.IMAGE_LIST_STATE` (the last is unimplemented).





Note


As [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") allows you to use a standard [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList") or
[`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList"), the returned object depends on which kind of image list you
chose.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItem(self, itemOrId, col=0) -> None:
        """ 

`GetItem`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItem "Permalink to this definition")
Returns the information about the input item.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or an integer specifying
the item index;
* **col** – the column to which the item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemBackgroundColour(self, item: Any) -> None:
        """ 

`GetItemBackgroundColour`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemBackgroundColour "Permalink to this definition")
Returns the item background colour.



Parameters
**item** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemCount(self) -> None:
        """ 

`GetItemCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemCount "Permalink to this definition")
Returns the number of items in the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemCustomRenderer(self, itemOrId, col=0) -> None:
        """ 

`GetItemCustomRenderer`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemCustomRenderer "Permalink to this definition")
Returns the custom renderer used to draw the input item (if any).



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemData(self, item: Any) -> None:
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemData "Permalink to this definition")
Gets the application-defined data associated with this item.



Parameters
**item** – an integer specifying the item index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemFont(self, item: Any) -> None:
        """ 

`GetItemFont`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemFont "Permalink to this definition")
Returns the item font.



Parameters
**item** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemKind(self, itemOrId, col=0) -> None:
        """ 

`GetItemKind`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemKind "Permalink to this definition")
Returns the item kind.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.





See also


[`SetItemKind`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemOverFlow(self, itemOrId, col=0) -> None:
        """ 

`GetItemOverFlow`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemOverFlow "Permalink to this definition")
Returns if the item is in the overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemPosition(self, item: Any) -> None:
        """ 

`GetItemPosition`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemPosition "Permalink to this definition")
Returns the position of the item, in icon or small icon view.



Parameters
**item** – the row in which the item lives.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemPyData(self, item: Any) -> None:
        """ 

`GetItemPyData`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemPyData "Permalink to this definition")
Returns the data for the item, which can be any Python object.



Parameters
**item** – an integer specifying the item index.





Note


Please note that Python data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemRect(self, item, code=ULC_RECT_BOUNDS) -> None:
        """ 

`GetItemRect`(*self*, *item*, *code=ULC\_RECT\_BOUNDS*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemRect "Permalink to this definition")
Returns the rectangle representing the item’s size and position, in physical
coordinates.



Parameters
* **item** – the row in which the item lives;
* **code** – one of `ULC_RECT_BOUNDS`, `ULC_RECT_ICON`, `ULC_RECT_LABEL`.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemSpacing(self, isSmall: bool=False) -> None:
        """ 

`GetItemSpacing`(*self*, *isSmall=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemSpacing "Permalink to this definition")
Returns the spacing between item texts and icons, in pixels.



Parameters
**isSmall** – `True` if using a `wx.IMAGE_LIST_SMALL` image list,
`False` if using a `wx.IMAGE_LIST_NORMAL` image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemState(self, item, stateMask) -> None:
        """ 

`GetItemState`(*self*, *item*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemState "Permalink to this definition")
Returns the item state flags for the input item.



Parameters
* **item** – the index of the item;
* **stateMask** – the bitmask for the state flag.





See also


[`SetItemState`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemState "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemState") for a list of valid state flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemText(self, item: UltimateListItem) -> None:
        """ 

`GetItemText`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemText "Permalink to this definition")
Returns the item text.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or an integer specifying
the item index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemTextColour(self, item: Any) -> None:
        """ 

`GetItemTextColour`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemTextColour "Permalink to this definition")
Returns the item text colour.



Parameters
**item** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemVisited(self, itemOrId, col=0) -> None:
        """ 

`GetItemVisited`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemVisited "Permalink to this definition")
Returns whether an hypertext item was visited.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemWindow(self, itemOrId, col=0) -> None:
        """ 

`GetItemWindow`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemWindow "Permalink to this definition")
Returns the window associated to the item (if any).



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetItemWindowEnabled(self, itemOrId, col=0) -> None:
        """ 

`GetItemWindowEnabled`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemWindowEnabled "Permalink to this definition")
Returns whether the window associated to the item is enabled.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetNextItem(self, item, geometry=ULC_NEXT_ALL, state=ULC_STATE_DONTCARE) -> None:
        """ 

`GetNextItem`(*self*, *item*, *geometry=ULC\_NEXT\_ALL*, *state=ULC\_STATE\_DONTCARE*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetNextItem "Permalink to this definition")
Searches for an item with the given *geometry* or *state*, starting from *item*
but excluding the *item* itself.



Parameters
* **item** – the item at which starting the search. If set to -1, the first
item that matches the specified flags will be returned.
* **geometry** – can be one of:






| Geometry Flag | Hex Value | Description |
| --- | --- | --- |
| `ULC_NEXT_ABOVE` | 0x0 | Searches for an item above the specified item |
| `ULC_NEXT_ALL` | 0x1 | Searches for subsequent item by index |
| `ULC_NEXT_BELOW` | 0x2 | Searches for an item below the specified item |
| `ULC_NEXT_LEFT` | 0x3 | Searches for an item to the left of the specified item |
| `ULC_NEXT_RIGHT` | 0x4 | Searches for an item to the right of the specified item |
* **state** – any combination of the following bits:






| State Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_STATE_DONTCARE` | 0x0 | Don’t care what the state is |
| `ULC_STATE_DROPHILITED` | 0x1 | The item is highlighted to receive a drop event |
| `ULC_STATE_FOCUSED` | 0x2 | The item has the focus |
| `ULC_STATE_SELECTED` | 0x4 | The item is selected |
| `ULC_STATE_CUT` | 0x8 | The item is in the cut state |
| `ULC_STATE_DISABLED` | 0x10 | The item is disabled |
| `ULC_STATE_FILTERED` | 0x20 | The item has been filtered |
| `ULC_STATE_INUSE` | 0x40 | The item is in use |
| `ULC_STATE_PICKED` | 0x80 | The item has been picked |
| `ULC_STATE_SOURCE` | 0x100 | The item is a drag and drop source |



Returns
The first item with given *state* following *item* or -1 if no such item found.





Note


This function may be used to find all selected items in the
control like this:



```
item = -1

while 1:
    item = listctrl.GetNextItem(item, ULC_NEXT_ALL, ULC_STATE_SELECTED)

    if item == -1:
        break

    # This item is selected - do whatever is needed with it

    wx.LogMessage("Item %ld is selected."%item)

```





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetNextSelected(self, item: Any) -> None:
        """ 

`GetNextSelected`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetNextSelected "Permalink to this definition")
Returns subsequent selected items, or -1 when no more are selected.



Parameters
**item** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrolledWin(self) -> None:
        """ 

`GetScrolledWin`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetScrolledWin "Permalink to this definition")
Returns the header window owner.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollPos(self, orientation: Any) -> None:
        """ 

`GetScrollPos`(*self*, *orientation*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetScrollPos "Permalink to this definition")
Returns the scrollbar position.



Note


This method is forwarded to [`UltimateListMainWindow`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").




Parameters
**orientation** – May be wx.HORIZONTAL or wx.VERTICAL.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollRange(self) -> None:
        """ 

`GetScrollRange`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetScrollRange "Permalink to this definition")
Returns the scrollbar range in pixels.



Note


This method is forwarded to [`UltimateListMainWindow`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetScrollThumb(self) -> None:
        """ 

`GetScrollThumb`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetScrollThumb "Permalink to this definition")
Returns the scrollbar size in pixels.



Note


This method is forwarded to [`UltimateListMainWindow`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSecondGradientColour(self) -> None:
        """ 

`GetSecondGradientColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetSecondGradientColour "Permalink to this definition")
Returns the second gradient colour for gradient-style selections.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSelectedItemCount(self) -> None:
        """ 

`GetSelectedItemCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetSelectedItemCount "Permalink to this definition")
Returns the number of selected items in [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetSubItemRect(self, item, subItem, code) -> None:
        """ 

`GetSubItemRect`(*self*, *item*, *subItem*, *code*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetSubItemRect "Permalink to this definition")
Returns the rectangle representing the size and position, in physical coordinates,
of the given subitem, i.e. the part of the row *item* in the column *subItem*.



Parameters
* **item** – the row in which the item lives;
* **subItem** – the column in which the item lives. If set equal to the special
value `ULC_GETSUBITEMRECT_WHOLEITEM` the return value is the same as for
[`GetItemRect`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemRect "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetItemRect");
* **code** – one of `ULC_RECT_BOUNDS`, `ULC_RECT_ICON`, `ULC_RECT_LABEL`.





Note


This method is only meaningful when the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") is in the
report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetTextColour(self) -> None:
        """ 

`GetTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetTextColour "Permalink to this definition")
Returns the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") foreground colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetTopItem(self) -> None:
        """ 

`GetTopItem`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetTopItem "Permalink to this definition")
Gets the index of the topmost visible item when in list or report view.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetUserLineHeight(self) -> None:
        """ 

`GetUserLineHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetUserLineHeight "Permalink to this definition")
Returns the custom value for the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") item height, if previously set with
[`SetUserLineHeight`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetUserLineHeight "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetUserLineHeight").



Note


This method can be used only with `ULC_REPORT` and `ULC_USER_ROW_HEIGHT` styles set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetViewRect(self) -> None:
        """ 

`GetViewRect`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetViewRect "Permalink to this definition")
Returns the rectangle taken by all items in the control. In other words,
if the controls client size were equal to the size of this rectangle, no
scrollbars would be needed and no free space would be left.



Note


This function only works in the icon and small icon views, not in
list or report views.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def GetWaterMark(self) -> None:
        """ 

`GetWaterMark`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.GetWaterMark "Permalink to this definition")
Returns the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") watermark image (if any), displayed in the
bottom right part of the window.



Todo


Better support for this is needed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasAGWFlag(self, flag: Any) -> None:
        """ 

`HasAGWFlag`(*self*, *flag*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.HasAGWFlag "Permalink to this definition")
Returns `True` if the window has the given flag bit set.



Parameters
**flag** – the window style to check.





See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag") for a list of valid window styles.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasFooter(self) -> None:
        """ 

`HasFooter`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.HasFooter "Permalink to this definition")
Returns `True` if [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has a footer window.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HasHeader(self) -> None:
        """ 

`HasHeader`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.HasHeader "Permalink to this definition")
Returns `True` if [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has a header window.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def HitTest(self, pointOrTuple: Any) -> None:
        """ 

`HitTest`(*self*, *pointOrTuple*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.HitTest "Permalink to this definition")
HitTest method for a [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**pointOrTuple** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point") or a tuple representing
the mouse *x*, *y* position.





See also


[`UltimateListMainWindow.HitTestLine()`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTestLine "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTestLine") for a list of return flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertColumn(self, col, heading, format=ULC_FORMAT_LEFT, width=-1) -> None:
        """ 

`InsertColumn`(*self*, *col*, *heading*, *format=ULC\_FORMAT\_LEFT*, *width=-1*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertColumn "Permalink to this definition")
Inserts a column into [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **col** – the column index at which we wish to insert a column;
* **heading** – the header text;
* **format** – the column alignment flag. This can be one of the following
bits:








| Alignment Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_FORMAT_LEFT` | 0x0 | The item is left-aligned |
| `ULC_FORMAT_RIGHT` | 0x1 | The item is right-aligned |
| `ULC_FORMAT_CENTRE` | 0x2 | The item is centre-aligned |
| `ULC_FORMAT_CENTER` | 0x2 | The item is center-aligned |
* **width** – can be a width in pixels or `wx.LIST_AUTOSIZE` (-1) or
`wx.LIST_AUTOSIZE_USEHEADER` (-2) or `LIST_AUTOSIZE_FILL` (-3).
`wx.LIST_AUTOSIZE` will resize the column to the length of its longest
item. `wx.LIST_AUTOSIZE_USEHEADER` will resize the column to the
length of the header (Win32) or 80 pixels (other platforms).
`LIST_AUTOSIZE_FILL` will resize the column fill the remaining width
of the window.



Returns
the index at which the column has been inserted.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertColumnInfo(self, col, item) -> None:
        """ 

`InsertColumnInfo`(*self*, *col*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertColumnInfo "Permalink to this definition")
Inserts a column into [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **col** – the column index at which we wish to insert a column;
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").



Returns
the index at which the column has been inserted.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertImageItem(self, index, imageIds, it_kind=0) -> None:
        """ 

`InsertImageItem`(*self*, *index*, *imageIds*, *it\_kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertImageItem "Permalink to this definition")
Inserts an image item at the given location.



Parameters
* **index** – the index at which we wish to insert the item;
* **imageIds** – a Python list containing the image indexes for the
images associated to this item;
* **it\_kind** – the item kind.





See also


[`SetStringItem`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertImageStringItem(self, index, label, imageIds, it_kind=0) -> None:
        """ 

`InsertImageStringItem`(*self*, *index*, *label*, *imageIds*, *it\_kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertImageStringItem "Permalink to this definition")
Inserts an image+string item at the given location.



Parameters
* **index** – the index at which we wish to insert the item;
* **label** – the item text;
* **imageIds** – a Python list containing the image indexes for the
images associated to this item;
* **it\_kind** – the item kind.





See also


[`SetStringItem`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertItem(self, info: UltimateListItem) -> None:
        """ 

`InsertItem`(*self*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertItem "Permalink to this definition")
Inserts an item into [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**info** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def InsertStringItem(self, index, label, it_kind=0) -> None:
        """ 

`InsertStringItem`(*self*, *index*, *label*, *it\_kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.InsertStringItem "Permalink to this definition")
Inserts a string item at the given location.



Parameters
* **index** – the index at which we wish to insert the item;
* **label** – the item text;
* **it\_kind** – the item kind.





See also


[`SetStringItem`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ 

`IsColumnShown`(*self*, *column*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsColumnShown "Permalink to this definition")
Returns `True` if the input column is shown, `False` if it is hidden.



Parameters
**column** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemChecked(self, itemOrId, col=0) -> None:
        """ 

`IsItemChecked`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsItemChecked "Permalink to this definition")
Returns whether an item is checked or not.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemEnabled(self, itemOrId, col=0) -> None:
        """ 

`IsItemEnabled`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsItemEnabled "Permalink to this definition")
Returns whether an item is enabled or not.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsItemHyperText(self, itemOrId, col=0) -> None:
        """ 

`IsItemHyperText`(*self*, *itemOrId*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsItemHyperText "Permalink to this definition")
Returns whether an item is hypertext or not.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsSelected(self, idx: Any) -> None:
        """ 

`IsSelected`(*self*, *idx*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsSelected "Permalink to this definition")
Returns `True` if the item is selected.



Parameters
**idx** – the index of the item to check for selection.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def IsVirtual(self) -> None:
        """ 

`IsVirtual`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.IsVirtual "Permalink to this definition")
Returns `True` if the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_VIRTUAL` style set.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemAttr(self, item: Any) -> None:
        """ 

`OnGetItemAttr`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemAttr "Permalink to this definition")
This function may be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return the attribute for the specified
item or `None` to use the default appearance parameters.



Parameters
**item** – an integer specifying the item index.





Note


[`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") will not delete the pointer or keep a reference of it.
You can return the same [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr") pointer for every
[`OnGetItemAttr`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemAttr") call.




Note


The base class version always returns `None`.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemCheck(self, item: Any) -> None:
        """ 

`OnGetItemCheck`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemCheck "Permalink to this definition")
This function may be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return whether a checkbox-like item or
a radiobutton-like item is checked or unchecked.



Parameters
**item** – an integer specifying the item index.





Note


The base class version always returns an empty list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnCheck(self, item: Any, column=0) -> None:
        """ 

`OnGetItemColumnCheck`(*self*, *item*, *column=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemColumnCheck "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` and `ULC_REPORT` style. It should return whether a
checkbox-like item or a radiobutton-like item in the column header is checked
or unchecked.



Parameters
**item** – an integer specifying the item index.





Note


The base class version always returns an empty Python list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnImage(self, item: Any, column=0) -> None:
        """ 

`OnGetItemColumnImage`(*self*, *item*, *column=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemColumnImage "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` and `ULC_REPORT` style. It should return a Python list of
indexes representing the images associated to the input item or an empty list
for no images.



Parameters
**item** – an integer specifying the item index.





Note


The base class version always returns an empty Python list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemColumnKind(self, item, column=0) -> None:
        """ 

`OnGetItemColumnKind`(*self*, *item*, *column=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemColumnKind "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return the item kind for the input item in
the header window.



Parameters
* **item** – an integer specifying the item index;
* **column** – the column index.





Note


The base class version always returns 0 (a standard item).




See also


[`SetItemKind`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemImage(self, item: Any) -> None:
        """ 

`OnGetItemImage`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemImage "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style having an image list (if the control doesn’t have an
image list, it is not necessary to overload it). It should return a Python
list of indexes representing the images associated to the input item or an
empty list for no images.



Parameters
**item** – an integer specifying the item index;





Note


In a control with `ULC_REPORT` style, [`OnGetItemImage`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemImage "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemImage") only gets called
for the first column of each line.




Note


The base class version always returns an empty Python list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemKind(self, item: Any) -> None:
        """ 

`OnGetItemKind`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemKind "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return the item kind for the input item.



Parameters
**item** – an integer specifying the item index.





Note


The base class version always returns 0 (a standard item).




See also


[`SetItemKind`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemText(self, item, col) -> None:
        """ 

`OnGetItemText`(*self*, *item*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemText "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return the string containing the text of
the given column for the specified item.



Parameters
* **item** – an integer specifying the item index;
* **col** – the column index to which the item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemTextColour(self, item, col) -> None:
        """ 

`OnGetItemTextColour`(*self*, *item*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemTextColour "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return a [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or `None` for
the default color.



Parameters
* **item** – an integer specifying the item index;
* **col** – the column index to which the item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnGetItemToolTip(self, item, col) -> None:
        """ 

`OnGetItemToolTip`(*self*, *item*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemToolTip "Permalink to this definition")
This function **must** be overloaded in the derived class for a control with
`ULC_VIRTUAL` style. It should return the string containing the text of
the tooltip for the specified item.



Parameters
* **item** – an integer specifying the item index;
* **col** – the column index to which the item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnInternalIdle(self) -> None:
        """ 

`OnInternalIdle`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnInternalIdle "Permalink to this definition")
This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an *OnIdle* handler in a derived class.


This method may be used to do delayed painting, for example, and most
implementations call [`wx.Window.UpdateWindowUI`](wx.Window.html#wx.Window.UpdateWindowUI "wx.Window.UpdateWindowUI") in order to send update events
to the window in idle time.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def PopupMenu(self, menu, pos=wx.DefaultPosition) -> None:
        """ 

`PopupMenu`(*self*, *menu*, *pos=wx.DefaultPosition*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.PopupMenu "Permalink to this definition")
Pops up the given *menu* at the specified coordinates, relative to this window,
and returns control when the user has dismissed the menu. If a menu item is
selected, the corresponding menu event is generated and will be processed as
usual. If the coordinates are not specified, the current mouse cursor position
is used.



Parameters
* **menu** – an instance of [`wx.Menu`](wx.Menu.html#wx.Menu "wx.Menu") to pop up;
* **pos** – the position where the menu will appear.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Refresh(self, eraseBackground=True, rect=None) -> None:
        """ 

`Refresh`(*self*, *eraseBackground=True*, *rect=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Refresh "Permalink to this definition")
Causes this window, and all of its children recursively (except under wxGTK1
where this is not implemented), to be repainted.



Parameters
* **eraseBackground** – If `True`, the background will be erased;
* **rect** – If not `None`, only the given rectangle will be treated as damaged.





Note


Note that repainting doesn’t happen immediately but only during the next
event loop iteration, if you need to update the window immediately you should
use [`Update`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Update "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Update") instead.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def RefreshItem(self, item: Any) -> None:
        """ 

`RefreshItem`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.RefreshItem "Permalink to this definition")
Redraws the given item.



Parameters
**item** – an integer specifying the item index;





Note


This is only useful for the virtual list controls as without calling
this function the displayed value of the item doesn’t change even when the
underlying data does change.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def RefreshItems(self, itemFrom, itemTo) -> None:
        """ 

`RefreshItems`(*self*, *itemFrom*, *itemTo*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.RefreshItems "Permalink to this definition")
Redraws the items between *itemFrom* and *itemTo*.
The starting item must be less than or equal to the ending one.


Just as [`RefreshItem`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.RefreshItem "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.RefreshItem") this is only useful for virtual list controls



Parameters
* **itemFrom** – the first index of the refresh range;
* **itemTo** – the last index of the refresh range.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScreenToClient(self, x: int, y: int) -> None:
        """ 

`ScreenToClient`(*self*, *pointOrTuple*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ScreenToClient "Permalink to this definition")
Converts from screen to client window coordinates.



Parameters
**pointOrTuple** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point") or a tuple representing the
*x*, *y* coordinates for this point.



Returns
the coordinates relative to this window.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScreenToClientXY(self, x, y) -> None:
        """ 

`ScreenToClientXY`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ScreenToClientXY "Permalink to this definition")
Converts from screen to client window coordinates.



Parameters
* **x** – an integer specifying the *x* screen coordinate;
* **y** – an integer specifying the *y* screen coordinate.



Returns
the coordinates relative to this window.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def ScrollList(self, dx, dy) -> None:
        """ 

`ScrollList`(*self*, *dx*, *dy*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.ScrollList "Permalink to this definition")
Scrolls the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **dx** – if in icon, small icon or report view mode, specifies the number
of pixels to scroll. If in list view mode, *dx* specifies the number of
columns to scroll.
* **dy** – always specifies the number of pixels to scroll vertically.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Select(self, idx, on=True) -> None:
        """ 

`Select`(*self*, *idx*, *on=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Select "Permalink to this definition")
Selects/deselects an item.



Parameters
* **idx** – the index of the item to select;
* **on** – `True` to select the item, `False` to deselect it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetAGWWindowStyleFlag(self, style: int) -> None:
        """ 

`SetAGWWindowStyleFlag`(*self*, *style*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetAGWWindowStyleFlag "Permalink to this definition")
Sets the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") AGW-specific style flag.



Parameters
**style** – the AGW-specific window style; can be almost any combination of the following
bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `ULC_VRULES` | 0x1 | Draws light vertical rules between rows in report mode. |
| `ULC_HRULES` | 0x2 | Draws light horizontal rules between rows in report mode. |
| `ULC_ICON` | 0x4 | Large icon view, with optional labels. |
| `ULC_SMALL_ICON` | 0x8 | Small icon view, with optional labels. |
| `ULC_LIST` | 0x10 | Multicolumn list view, with optional small icons. Columns are computed automatically, i.e. you don’t set columns as in `ULC_REPORT`. In other words, the list wraps, unlike a `ListBox`. |
| `ULC_REPORT` | 0x20 | Single or multicolumn report view, with optional header. |
| `ULC_ALIGN_TOP` | 0x40 | Icons align to the top. Win32 default, Win32 only. |
| `ULC_ALIGN_LEFT` | 0x80 | Icons align to the left. |
| `ULC_AUTOARRANGE` | 0x100 | Icons arrange themselves. Win32 only. |
| `ULC_VIRTUAL` | 0x200 | The application provides items text on demand. May only be used with `ULC_REPORT`. |
| `ULC_EDIT_LABELS` | 0x400 | Labels are editable: the application will be notified when editing starts. |
| `ULC_NO_HEADER` | 0x800 | No header in report mode. |
| `ULC_NO_SORT_HEADER` | 0x1000 | No Docs. |
| `ULC_SINGLE_SEL` | 0x2000 | Single selection (default is multiple). |
| `ULC_SORT_ASCENDING` | 0x4000 | Sort in ascending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_SORT_DESCENDING` | 0x8000 | Sort in descending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_TILE` | 0x10000 | Each item appears as a full-sized icon with a label of one or more lines beside it (partially implemented). |
| `ULC_NO_HIGHLIGHT` | 0x20000 | No highlight when an item is selected. |
| `ULC_STICKY_HIGHLIGHT` | 0x40000 | Items are selected by simply hovering on them, with no need to click on them. |
| `ULC_STICKY_NOSELEVENT` | 0x80000 | Don’t send a selection event when using `ULC_STICKY_HIGHLIGHT` style. |
| `ULC_SEND_LEFTCLICK` | 0x100000 | Send a left click event when an item is selected. |
| `ULC_HAS_VARIABLE_ROW_HEIGHT` | 0x200000 | The list has variable row heights. |
| `ULC_AUTO_CHECK_CHILD` | 0x400000 | When a column header has a checkbox associated, auto-check all the subitems in that column. |
| `ULC_AUTO_TOGGLE_CHILD` | 0x800000 | When a column header has a checkbox associated, toggle all the subitems in that column. |
| `ULC_AUTO_CHECK_PARENT` | 0x1000000 | Only meaningful foe checkbox-type items: when an item is checked/unchecked its column header item is checked/unchecked as well. |
| `ULC_SHOW_TOOLTIPS` | 0x2000000 | Show tooltips for ellipsized items/subitems (text too long to be shown in the available space) containing the full item/subitem text. |
| `ULC_HOT_TRACKING` | 0x4000000 | Enable hot tracking of items on mouse motion. |
| `ULC_BORDER_SELECT` | 0x8000000 | Changes border colour when an item is selected, instead of highlighting the item. |
| `ULC_TRACK_SELECT` | 0x10000000 | Enables hot-track selection in a list control. Hot track selection means that an item is automatically selected when the cursor remains over the item for a certain period of time. The delay is retrieved on Windows using the `win32api` call *win32gui.SystemParametersInfo(win32con.SPI\_GETMOUSEHOVERTIME)*, and is defaulted to 400ms on other platforms. This style applies to all views of [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). |
| `ULC_HEADER_IN_ALL_VIEWS` | 0x20000000 | Show column headers in all view modes. |
| `ULC_NO_FULL_ROW_SELECT` | 0x40000000 | When an item is selected, the only the item in the first column is highlighted. |
| `ULC_FOOTER` | 0x80000000 | Show a footer too (only when header is present). |
| `ULC_USER_ROW_HEIGHT` | 0x100000000 | Allows to set a custom row height (one value for all the items, only in report mode). |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetBackgroundColour(self, colour: NullColour) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetBackgroundColour "Permalink to this definition")
Changes the background colour of [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**colour** – the colour to be used as the background colour, pass
`NullColour` to reset to the default colour.





Note


The background colour is usually painted by the default `EraseEvent`
event handler function under Windows and automatically under GTK.




Note


Setting the background colour does not cause an immediate refresh, so
you may wish to call [`wx.Window.ClearBackground`](wx.Window.html#wx.Window.ClearBackground "wx.Window.ClearBackground") or [`wx.Window.Refresh`](wx.Window.html#wx.Window.Refresh "wx.Window.Refresh") after
calling this function.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetBackgroundImage(self, image: Optional[None]=None) -> None:
        """ 

`SetBackgroundImage`(*self*, *image=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetBackgroundImage "Permalink to this definition")
Sets the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") background image.



Parameters
**image** – if not `None`, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").





Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumn(self, col, item) -> None:
        """ 

`SetColumn`(*self*, *col*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumn "Permalink to this definition")
Sets information about this column.



Parameters
* **col** – an integer specifying the column index;
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnCustomRenderer(self, col=0, renderer=None) -> None:
        """ 

`SetColumnCustomRenderer`(*self*, *col=0*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnCustomRenderer "Permalink to this definition")
Associate a custom renderer to this column’s header.



Parameters
* **col** – the column index.
* **renderer** – a class able to correctly render the input item.





Note


the renderer class **must** implement the methods *DrawHeaderButton*
and *GetForegroundColor*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnImage(self, col, image) -> None:
        """ 

`SetColumnImage`(*self*, *col*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnImage "Permalink to this definition")
Sets one or more images to the specified column.



Parameters
* **col** – the column index;
* **image** – a Python list containing the image indexes for the
images associated to this column item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnShown(self, column, shown=True) -> None:
        """ 

`SetColumnShown`(*self*, *column*, *shown=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnShown "Permalink to this definition")
Sets the specified column as shown or hidden.



Parameters
* **column** – an integer specifying the column index;
* **shown** – `True` to show the column, `False` to hide it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnToolTip(self, col, tip) -> None:
        """ 

`SetColumnToolTip`(*self*, *col*, *tip*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnToolTip "Permalink to this definition")
Sets the tooltip for the column header



Parameters
* **col** – the column index;
* **tip** – the tooltip text






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetColumnWidth(self, col, width: 'LIST_AUTOSIZE') -> None:
        """ 

`SetColumnWidth`(*self*, *col*, *width*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnWidth "Permalink to this definition")
Sets the column width.



Parameters
**width** – can be a width in pixels or `wx.LIST_AUTOSIZE` (-1) or
`wx.LIST_AUTOSIZE_USEHEADER` (-2) or `LIST_AUTOSIZE_FILL` (-3).
`wx.LIST_AUTOSIZE` will resize the column to the length of its longest
item. `wx.LIST_AUTOSIZE_USEHEADER` will resize the column to the
length of the header (Win32) or 80 pixels (other platforms).
`LIST_AUTOSIZE_FILL` will resize the column fill the remaining width
of the window.





Note


In small or normal icon view, col must be -1, and the column width
is set for all columns.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetCursor(self, cursor: Any) -> None:
        """ 

`SetCursor`(*self*, *cursor*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetCursor "Permalink to this definition")
Sets the window’s cursor.



Parameters
**cursor** – specifies the cursor that the window should normally display.
The *cursor* may be `NullCursor` in which case the window cursor will be
reset back to default.





Note


The window cursor also sets it for the children of the window implicitly.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetDisabledTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetDisabledTextColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetDisabledTextColour "Permalink to this definition")
Sets the items disabled colour.



Parameters
**colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetDropTarget(self, dropTarget: DropTarget) -> None:
        """ 

`SetDropTarget`(*self*, *dropTarget*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetDropTarget "Permalink to this definition")
Associates a drop target with this window.
If the window already has a drop target, it is deleted.



Parameters
**dropTarget** – an instance of `DropTarget`.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetFirstGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetFirstGradientColour "Permalink to this definition")
Sets the first gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour is taken from the system value `wx.SYS_COLOUR_HIGHLIGHT`.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFocus(self) -> None:
        """ 

`SetFocus`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetFocus "Permalink to this definition")
This sets the window to receive keyboard input.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetFont "Permalink to this definition")
Sets the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") font.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFooterCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ 

`SetFooterCustomRenderer`(*self*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetFooterCustomRenderer "Permalink to this definition")
Associate a custom renderer with the footer - all columns will use it.



Parameters
**renderer** – a class able to correctly render header buttons





Note


the renderer class **must** implement the methods *DrawHeaderButton*
and *GetForegroundColor*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetFooterHeight(self, height: None) -> None:
        """ 

`SetFooterHeight`(*self*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetFooterHeight "Permalink to this definition")
Sets the [`UltimateListHeaderWindow`](wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") height, in pixels. This overrides the default
footer window size derived from `RendererNative`. If *height* is `None`, the
default behaviour is restored.



Parameters
**height** – the footer window height, in pixels (if it is `None`, the default
height obtained using `RendererNative` is used).






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetForegroundColour(self, colour: NullColour) -> None:
        """ 

`SetForegroundColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetForegroundColour "Permalink to this definition")
Changes the foreground colour of [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**colour** – the colour to be used as the foreground colour, pass
`NullColour` to reset to the default colour.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetGradientStyle(self, vertical: Any=0) -> None:
        """ 

`SetGradientStyle`(*self*, *vertical=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetGradientStyle "Permalink to this definition")
Sets the gradient style for gradient-style selections.



Parameters
**vertical** – 0 for horizontal gradient-style selections, 1 for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHeaderCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ 

`SetHeaderCustomRenderer`(*self*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetHeaderCustomRenderer "Permalink to this definition")
Associate a custom renderer with the header - all columns will use it.



Parameters
**renderer** – a class able to correctly render header buttons





Note


the renderer class **must** implement the methods *DrawHeaderButton*
and *GetForegroundColor*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHeaderHeight(self, height: None) -> None:
        """ 

`SetHeaderHeight`(*self*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetHeaderHeight "Permalink to this definition")
Sets the [`UltimateListHeaderWindow`](wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") height, in pixels. This overrides the default
header window size derived from `RendererNative`. If *height* is `None`, the
default behaviour is restored.



Parameters
**height** – the header window height, in pixels (if it is `None`, the default
height obtained using `RendererNative` is used).






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ 

`SetHyperTextFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetHyperTextFont "Permalink to this definition")
Sets the font used to render hypertext items.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextNewColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetHyperTextNewColour "Permalink to this definition")
Sets the colour used to render a non-visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextVisitedColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetHyperTextVisitedColour "Permalink to this definition")
Sets the colour used to render a visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetImageList(self, imageList, which) -> None:
        """ 

`SetImageList`(*self*, *imageList*, *which*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetImageList "Permalink to this definition")
Sets the image list associated with the control.



Parameters
* **imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList") or an instance of [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList");
* **which** – one of `wx.IMAGE_LIST_NORMAL`, `wx.IMAGE_LIST_SMALL`,
`wx.IMAGE_LIST_STATE` (the last is unimplemented).





Note


Using [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") enables you to have images of different size inside the
image list. In your derived class, instead of doing this:



```
imageList = wx.ImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```


You should do this:



```
imageList = PyImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItem(self, info: UltimateListItem) -> None:
        """ 

`SetItem`(*self*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItem "Permalink to this definition")
Sets the information about the input item.



Parameters
**info** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemBackgroundColour(self, item, col) -> None:
        """ 

`SetItemBackgroundColour`(*self*, *item*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemBackgroundColour "Permalink to this definition")
Sets the item background colour.



Parameters
* **item** – the index of the item;
* **col** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemColumnImage(self, item, column, image) -> None:
        """ 

`SetItemColumnImage`(*self*, *item*, *column*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemColumnImage "Permalink to this definition")
Sets a Python list of image indexes associated with the item in the input
column.



Parameters
* **item** – an integer specifying the item index;
* **column** – the column to which the item belongs to;
* **image** – a Python list of indexes into the image list associated
with the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemCount(self, count: Any) -> None:
        """ 

`SetItemCount`(*self*, *count*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemCount "Permalink to this definition")
Sets the total number of items we handle.



Parameters
**count** – the total number of items we handle.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemCustomRenderer(self, itemOrId, col=0, renderer=None) -> None:
        """ 

`SetItemCustomRenderer`(*self*, *itemOrId*, *col=0*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemCustomRenderer "Permalink to this definition")
Associate a custom renderer to this item.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **renderer** – a class able to correctly render the input item.





Note


the renderer class **must** implement the methods *DrawSubItem*,
*GetLineHeight* and *GetSubItemWidth*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemData "Permalink to this definition")
Sets the application-defined data associated with this item.



Parameters
* **item** – an integer specifying the item index;
* **data** – the data to be associated with the input item.





Note


This function cannot be used to associate pointers with
the control items, use [`SetItemPyData`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemPyData "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemPyData") instead.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemFont(self, item, f) -> None:
        """ 

`SetItemFont`(*self*, *item*, *f*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemFont "Permalink to this definition")
Sets the item font.



Parameters
* **item** – the index of the item;
* **f** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemHyperText(self, itemOrId, col=0, hyper=True) -> None:
        """ 

`SetItemHyperText`(*self*, *itemOrId*, *col=0*, *hyper=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **hyper** – `True` to have an item with hypertext behaviour, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemImage(self, item, image, selImage=-1) -> None:
        """ 

`SetItemImage`(*self*, *item*, *image*, *selImage=-1*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemImage "Permalink to this definition")
Sets a Python list of image indexes associated with the item.



Parameters
* **item** – an integer specifying the item index;
* **image** – a Python list of indexes into the image list associated
with the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). In report view, this only sets the images
for the first column;
* **selImage** – not used at present.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemKind(self, itemOrId, col=0, kind=0) -> None:
        """ 

`SetItemKind`(*self*, *itemOrId*, *col=0*, *kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemKind "Permalink to this definition")
Sets the item kind.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemOverFlow(self, itemOrId, col=0, over=True) -> None:
        """ 

`SetItemOverFlow`(*self*, *itemOrId*, *col=0*, *over=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemOverFlow "Permalink to this definition")
Sets the item in the overflow/non overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **over** – `True` to set the item in a overflow state, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemPosition(self, item, pos) -> None:
        """ 

`SetItemPosition`(*self*, *item*, *pos*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemPosition "Permalink to this definition")
Sets the position of the item, in icon or small icon view.



Parameters
* **item** – the row in which the item lives;
* **pos** – the item position.





Note


This method is currently unimplemented and does nothing.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemPyData(self, item, pyData) -> None:
        """ 

`SetItemPyData`(*self*, *item*, *pyData*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemPyData "Permalink to this definition")
Sets the data for the item, which can be any Python object.



Parameters
* **item** – an integer specifying the item index;
* **pyData** – any Python object.





Note


Please note that Python data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemSpacing(self, spacing, isSmall=False) -> None:
        """ 

`SetItemSpacing`(*self*, *spacing*, *isSmall=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemSpacing "Permalink to this definition")
Sets the spacing between item texts and icons.



Parameters
* **spacing** – the spacing between item texts and icons, in pixels;
* **isSmall** – `True` if using a `wx.IMAGE_LIST_SMALL` image list,
`False` if using a `wx.IMAGE_LIST_NORMAL` image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemState(self, item, state, stateMask) -> None:
        """ 

`SetItemState`(*self*, *item*, *state*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemState "Permalink to this definition")
Sets the item state flags for the input item.



Parameters
* **item** – the index of the item; if defaulted to -1, the state flag
will be set for all the items;
* **state** – any combination of the following bits:






| State Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_STATE_DONTCARE` | 0x0 | Don’t care what the state is |
| `ULC_STATE_DROPHILITED` | 0x1 | The item is highlighted to receive a drop event |
| `ULC_STATE_FOCUSED` | 0x2 | The item has the focus |
| `ULC_STATE_SELECTED` | 0x4 | The item is selected |
| `ULC_STATE_CUT` | 0x8 | The item is in the cut state |
| `ULC_STATE_DISABLED` | 0x10 | The item is disabled |
| `ULC_STATE_FILTERED` | 0x20 | The item has been filtered |
| `ULC_STATE_INUSE` | 0x40 | The item is in use |
| `ULC_STATE_PICKED` | 0x80 | The item has been picked |
| `ULC_STATE_SOURCE` | 0x100 | The item is a drag and drop source |
* **stateMask** – the bitmask for the state flag.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ 

`SetItemText`(*self*, *item*, *text*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemText "Permalink to this definition")
Sets the item text.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or an integer specifying
the item index;
* **text** – the new item text.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemTextColour(self, item, col) -> None:
        """ 

`SetItemTextColour`(*self*, *item*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemTextColour "Permalink to this definition")
Sets the item text colour.



Parameters
* **item** – the index of the item;
* **col** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemVisited(self, itemOrId, col=0, visited=True) -> None:
        """ 

`SetItemVisited`(*self*, *itemOrId*, *col=0*, *visited=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemVisited "Permalink to this definition")
Sets whether an hypertext item was visited or not.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **visited** – `True` to mark an hypertext item as visited, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemWindow(self, itemOrId, col=0, wnd=None, expand=False) -> None:
        """ 

`SetItemWindow`(*self*, *itemOrId*, *col=0*, *wnd=None*, *expand=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemWindow "Permalink to this definition")
Sets the window for the given item.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **wnd** – a non-toplevel window to be displayed next to the item;
* **expand** – `True` to expand the column where the item/subitem lives,
so that the window will be fully visible.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetItemWindowEnabled(self, itemOrId, col=0, enable=True) -> None:
        """ 

`SetItemWindowEnabled`(*self*, *itemOrId*, *col=0*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetItemWindowEnabled "Permalink to this definition")
Enables/disables the window associated to the item.



Parameters
* **itemOrId** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") or the item index;
* **col** – the column index to which the input item belongs to;
* **enable** – `True` to enable the associated window, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetScrollPos(self, orientation, pos, refresh=True) -> None:
        """ 

`SetScrollPos`(*self*, *orientation*, *pos*, *refresh=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetScrollPos "Permalink to this definition")
Sets the scrollbar position.



Parameters
* **orientation** – determines the scrollbar whose position is to be set.
May be `wx.HORIZONTAL` or `wx.VERTICAL`;
* **pos** – the scrollbar position in scroll units;
* **refresh** – `True` to redraw the scrollbar, `False` otherwise.





Note


This method is forwarded to [`UltimateListMainWindow`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetSecondGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetSecondGradientColour "Permalink to this definition")
Sets the second gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour generated is a slightly darker version of the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
background colour.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetSingleStyle(self, style, add=True) -> None:
        """ 

`SetSingleStyle`(*self*, *style*, *add=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetSingleStyle "Permalink to this definition")
Adds or removes a single window style.



Parameters
* **style** – can be one of the following bits:






| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `ULC_VRULES` | 0x1 | Draws light vertical rules between rows in report mode. |
| `ULC_HRULES` | 0x2 | Draws light horizontal rules between rows in report mode. |
| `ULC_ICON` | 0x4 | Large icon view, with optional labels. |
| `ULC_SMALL_ICON` | 0x8 | Small icon view, with optional labels. |
| `ULC_LIST` | 0x10 | Multicolumn list view, with optional small icons. Columns are computed automatically, i.e. you don’t set columns as in `ULC_REPORT`. In other words, the list wraps, unlike a `ListBox`. |
| `ULC_REPORT` | 0x20 | Single or multicolumn report view, with optional header. |
| `ULC_ALIGN_TOP` | 0x40 | Icons align to the top. Win32 default, Win32 only. |
| `ULC_ALIGN_LEFT` | 0x80 | Icons align to the left. |
| `ULC_AUTOARRANGE` | 0x100 | Icons arrange themselves. Win32 only. |
| `ULC_VIRTUAL` | 0x200 | The application provides items text on demand. May only be used with `ULC_REPORT`. |
| `ULC_EDIT_LABELS` | 0x400 | Labels are editable: the application will be notified when editing starts. |
| `ULC_NO_HEADER` | 0x800 | No header in report mode. |
| `ULC_NO_SORT_HEADER` | 0x1000 | No Docs. |
| `ULC_SINGLE_SEL` | 0x2000 | Single selection (default is multiple). |
| `ULC_SORT_ASCENDING` | 0x4000 | Sort in ascending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_SORT_DESCENDING` | 0x8000 | Sort in descending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_TILE` | 0x10000 | Each item appears as a full-sized icon with a label of one or more lines beside it (partially implemented). |
| `ULC_NO_HIGHLIGHT` | 0x20000 | No highlight when an item is selected. |
| `ULC_STICKY_HIGHLIGHT` | 0x40000 | Items are selected by simply hovering on them, with no need to click on them. |
| `ULC_STICKY_NOSELEVENT` | 0x80000 | Don’t send a selection event when using `ULC_STICKY_HIGHLIGHT` style. |
| `ULC_SEND_LEFTCLICK` | 0x100000 | Send a left click event when an item is selected. |
| `ULC_HAS_VARIABLE_ROW_HEIGHT` | 0x200000 | The list has variable row heights. |
| `ULC_AUTO_CHECK_CHILD` | 0x400000 | When a column header has a checkbox associated, auto-check all the subitems in that column. |
| `ULC_AUTO_TOGGLE_CHILD` | 0x800000 | When a column header has a checkbox associated, toggle all the subitems in that column. |
| `ULC_AUTO_CHECK_PARENT` | 0x1000000 | Only meaningful foe checkbox-type items: when an item is checked/unchecked its column header item is checked/unchecked as well. |
| `ULC_SHOW_TOOLTIPS` | 0x2000000 | Show tooltips for ellipsized items/subitems (text too long to be shown in the available space) containing the full item/subitem text. |
| `ULC_HOT_TRACKING` | 0x4000000 | Enable hot tracking of items on mouse motion. |
| `ULC_BORDER_SELECT` | 0x8000000 | Changes border colour when an item is selected, instead of highlighting the item. |
| `ULC_TRACK_SELECT` | 0x10000000 | Enables hot-track selection in a list control. Hot track selection means that an item is automatically selected when the cursor remains over the item for a certain period of time. The delay is retrieved on Windows using the `win32api` call *win32gui.SystemParametersInfo(win32con.SPI\_GETMOUSEHOVERTIME)*, and is defaulted to 400ms on other platforms. This style applies to all views of [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). |
| `ULC_HEADER_IN_ALL_VIEWS` | 0x20000000 | Show column headers in all view modes. |
| `ULC_NO_FULL_ROW_SELECT` | 0x40000000 | When an item is selected, the only the item in the first column is highlighted. |
| `ULC_FOOTER` | 0x80000000 | Show a footer too (only when header is present). |
* **add** – `True` to add the window style, `False` to remove it.





Note


The style `ULC_VIRTUAL` can not be set/unset after construction.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetStringItem(self, index, col, label, imageIds=[], it_kind=0) -> None:
        """ 

`SetStringItem`(*self*, *index*, *col*, *label*, *imageIds=[]*, *it\_kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetStringItem "Permalink to this definition")
Sets a string or image at the given location.



Parameters
* **index** – the item index;
* **col** – the column to which the item belongs to;
* **label** – the item text;
* **imageIds** – a Python list containing the image indexes for the
images associated to this item;
* **it\_kind** – the item kind. May be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetTextColour "Permalink to this definition")
Sets the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") foreground colour.



Parameters
**col** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetUserLineHeight(self, height: Any) -> None:
        """ 

`SetUserLineHeight`(*self*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetUserLineHeight "Permalink to this definition")
Sets a custom value for the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") item height.



Parameters
**height** – the custom height for all the items, in pixels.





Note


This method can be used only with `ULC_REPORT` and `ULC_USER_ROW_HEIGHT` styles set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SetWaterMark(self, watermark: Optional[None]=None) -> None:
        """ 

`SetWaterMark`(*self*, *watermark=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetWaterMark "Permalink to this definition")
Sets the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") watermark image to be displayed in the bottom
right part of the window.



Parameters
**watermark** – if not `None`, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").





Todo


Better support for this is needed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def SortItems(self, func: Any = None) -> None:
        """ 

`SortItems`(*self*, *func=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SortItems "Permalink to this definition")
Call this function to sort the items in the [`UltimateListCtrl`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). Sorting is done
using the specified function *func*. This function must have the
following prototype:



```
def OnCompareItems(self, line1, line2):

    DoSomething(line1, line2)
    # function code

```


It is called each time when the two items must be compared and should return 0
if the items are equal, negative value if the first item is less than the second
one and positive value if the first one is greater than the second one.



Parameters
**func** – the method to use to sort the items. The default is to use the
[`UltimateListMainWindow.OnCompareItems()`](wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnCompareItems "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnCompareItems") method.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """

    def Update(self) -> None:
        """ 

`Update`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Update "Permalink to this definition")
Calling this method immediately repaints the invalidated area of the window
and all of its children recursively while this would usually only happen when
the flow of control returns to the event loop.



Note


This function doesn’t invalidate any area of the window so nothing
happens if nothing has been invalidated (i.e. marked as requiring a redraw).
Use [`Refresh`](#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Refresh "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.Refresh") first if you want to immediately redraw the window unconditionally.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html
        """



EVT_SET_FOCUS: int

EVT_SIZE: int

IMAGE_LIST_NORMAL: int

IMAGE_LIST_SMALL: int

IMAGE_LIST_STATE: int

LIST_AUTOSIZE: int

LIST_AUTOSIZE_USEHEADER: int

SYS_COLOUR_HIGHLIGHT: int

HORIZONTAL: int

VERTICAL: int

class UltimateListItem(Object):
    """ This class stores information about a [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") item or column.


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
    """
    def __init__(self, item: Optional[None]=None) -> None:
        """ 

`__init__`(*self*, *item=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.__init__ "Permalink to this definition")
Default class constructor.



Parameters
**item** – if not `None`, another instance of [`UltimateListItem`](#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Attributes(self) -> None:
        """ 

`Attributes`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.Attributes "Permalink to this definition")
Returns the associated attributes if they exist, or create a new [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr")
structure and associate it with this item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Check(self, checked: bool=True) -> None:
        """ 

`Check`(*self*, *checked=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.Check "Permalink to this definition")
Checks/unchecks an item.



Parameters
**checked** – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for check and radio items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def CheckFooter(self, checked: bool=True) -> None:
        """ 

`CheckFooter`(*self*, *checked=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.CheckFooter "Permalink to this definition")
Checks/unchecks a footer item.



Parameters
**checked** – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for check and radio footer items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.Clear "Permalink to this definition")
Resets the item state to the default.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def ClearAttributes(self) -> None:
        """ 

`ClearAttributes`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.ClearAttributes "Permalink to this definition")
Deletes the item attributes if they have been stored.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def DeleteWindow(self) -> None:
        """ 

`DeleteWindow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.DeleteWindow "Permalink to this definition")
Deletes the window associated to the item (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.Enable "Permalink to this definition")
Enables or disables the item.



Parameters
**enable** – `True` to enable the item, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetAlign(self) -> None:
        """ 

`GetAlign`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetAlign "Permalink to this definition")
Returns the alignment for the item.



See also


[`SetAlign`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign") for a list of valid alignment bits.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetAttributes(self) -> None:
        """ 

`GetAttributes`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetAttributes "Permalink to this definition")
Returns the associated [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr") attributes.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetBackgroundColour(self) -> None:
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetBackgroundColour "Permalink to this definition")
Returns the background colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetColumn(self) -> None:
        """ 

`GetColumn`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetColumn "Permalink to this definition")
Returns the zero-based column.



Note


This method is meaningful only in report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetCustomRenderer(self) -> None:
        """ 

`GetCustomRenderer`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetCustomRenderer "Permalink to this definition")
Returns the custom renderer associated with this item (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetData(self) -> None:
        """ 

`GetData`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetData "Permalink to this definition")
Returns client data associated with the control.



Note


Please note that client data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFont(self) -> None:
        """ 

`GetFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFont "Permalink to this definition")
Returns the item font.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterAlign(self) -> None:
        """ 

`GetFooterAlign`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterAlign "Permalink to this definition")
Returns the alignment for the footer item.



See also


[`SetAlign`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign") for a list of valid alignment flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterBackgroundColour(self) -> None:
        """ 

`GetFooterBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterBackgroundColour "Permalink to this definition")
Returns the footer item background colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterFont(self) -> None:
        """ 

`GetFooterFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFont "Permalink to this definition")
Returns the footer item font.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterFormat(self) -> None:
        """ 

`GetFooterFormat`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFormat "Permalink to this definition")
Returns the footer item format.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterImage(self) -> None:
        """ 

`GetFooterImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterImage "Permalink to this definition")
Returns the zero-based index of the image associated with the footer item into
the image list.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterKind(self) -> None:
        """ 

`GetFooterKind`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterKind "Permalink to this definition")
Returns the footer item kind.



See also


[`SetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind") for a list of valid items kind.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterText(self) -> None:
        """ 

`GetFooterText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterText "Permalink to this definition")
Returns the footer text.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFooterTextColour(self) -> None:
        """ 

`GetFooterTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterTextColour "Permalink to this definition")
Returns the footer item text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetFormat(self) -> None:
        """ 

`GetFormat`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFormat "Permalink to this definition")
Returns the header item format.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetId(self) -> None:
        """ 

`GetId`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetId "Permalink to this definition")
Returns the zero-based item position.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetImage(self) -> None:
        """ 

`GetImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetImage "Permalink to this definition")
Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetKind(self) -> None:
        """ 

`GetKind`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetKind "Permalink to this definition")
Returns the item kind.



See also


[`SetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind") for a valid list of item’s kind.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetMask(self) -> None:
        """ 

`GetMask`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetMask "Permalink to this definition")
Returns a bit mask indicating which fields of the structure are valid.



See also


[`SetMask`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetMask "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetMask") for a list of valid bit masks.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetOverFlow(self) -> None:
        """ 

`GetOverFlow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetOverFlow "Permalink to this definition")
Returns if the item is in the overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetPyData(self) -> None:
        """ 

`GetPyData`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetPyData "Permalink to this definition")
Returns data for the item, which can be any Python object.



Note


Please note that Python data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetState(self) -> None:
        """ 

`GetState`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetState "Permalink to this definition")
Returns a bit field representing the state of the item.



See also


[`SetState`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetState "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetState") for a list of valid item states.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetText(self) -> None:
        """ 

`GetText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetText "Permalink to this definition")
Returns the label/header text.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetTextColour(self) -> None:
        """ 

`GetTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetTextColour "Permalink to this definition")
Returns the text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetToolTip(self) -> None:
        """ 

`GetToolTip`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetToolTip "Permalink to this definition")
Returns the label/header tooltip.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetVisited(self) -> None:
        """ 

`GetVisited`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetVisited "Permalink to this definition")
Returns whether an hypertext item was visited or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWidth(self) -> None:
        """ 

`GetWidth`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWidth "Permalink to this definition")
Returns the column width.



Note


This method is meaningful only for column headers in report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindow(self) -> None:
        """ 

`GetWindow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWindow "Permalink to this definition")
Returns the window associated to the item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindowEnabled(self) -> None:
        """ 

`GetWindowEnabled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWindowEnabled "Permalink to this definition")
Returns whether the associated window is enabled or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def GetWindowSize(self) -> None:
        """ 

`GetWindowSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWindowSize "Permalink to this definition")
Returns the associated window size.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def HasAttributes(self) -> None:
        """ 

`HasAttributes`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.HasAttributes "Permalink to this definition")
Returns `True` if the item has attributes associated with it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.Init "Permalink to this definition")
Initializes an empty [`UltimateListItem`](#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsChecked(self) -> None:
        """ 

`IsChecked`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsChecked "Permalink to this definition")
Returns whether the item is checked or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsEnabled(self) -> None:
        """ 

`IsEnabled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsEnabled "Permalink to this definition")
Returns `True` if the item is enabled.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsFooterChecked(self) -> None:
        """ 

`IsFooterChecked`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsFooterChecked "Permalink to this definition")
Returns whether the footer item is checked or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsHyperText(self) -> None:
        """ 

`IsHyperText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsHyperText "Permalink to this definition")
Returns whether the item is hypetext or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def IsShown(self) -> None:
        """ 

`IsShown`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsShown "Permalink to this definition")
Returns `True` if the item is shown, or `False` if it is hidden.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for the window associated to an item.



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetAlign(self, align: ULC_FORMAT_LEFT) -> None:
        """ 

`SetAlign`(*self*, *align*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign "Permalink to this definition")
Sets the alignment for the item.



Parameters
**align** – one of the following bits:






| Alignment Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_FORMAT_LEFT` | 0x0 | The item is left-aligned |
| `ULC_FORMAT_RIGHT` | 0x1 | The item is right-aligned |
| `ULC_FORMAT_CENTRE` | 0x2 | The item is centre-aligned |
| `ULC_FORMAT_CENTER` | 0x2 | The item is center-aligned |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colBack*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetBackgroundColour "Permalink to this definition")
Sets the background colour for the item.



Parameters
**colBack** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetColumn(self, col: Any) -> None:
        """ 

`SetColumn`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetColumn "Permalink to this definition")
Sets the zero-based column.



Parameters
**col** – the zero-based column.





Note


This method is neaningful only in report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetCustomRenderer(self, renderer: Any) -> None:
        """ 

`SetCustomRenderer`(*self*, *renderer*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetCustomRenderer "Permalink to this definition")
Associate a custom renderer to this item.



Parameters
**renderer** – a class able to correctly render the item.





Note


the renderer class **must** implement the methods *DrawSubItem*,
*GetLineHeight* and *GetSubItemWidth*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetData(self, data: Any) -> None:
        """ 

`SetData`(*self*, *data*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetData "Permalink to this definition")
Sets client data for the item.



Parameters
**data** – the client data associated to the item.





Note


Please note that client data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFont "Permalink to this definition")
Sets the font for the item.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterAlign(self, align) -> None:
        """ 

`SetFooterAlign`(*self*, *align*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterAlign "Permalink to this definition")
Sets the alignment for the footer item.



See also


[`SetAlign`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetAlign") for a list of valid alignment flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetFooterBackgroundColour`(*self*, *colBack*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterBackgroundColour "Permalink to this definition")
Sets the background colour for the footer item.



Parameters
**colBack** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterFont(self, font: 'Font') -> None:
        """ 

`SetFooterFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterFont "Permalink to this definition")
Sets the font for the footer item.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterFormat(self, format: Any) -> None:
        """ 

`SetFooterFormat`(*self*, *format*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterFormat "Permalink to this definition")
Sets the footer item format.



Parameters
**format** – the footer item format.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterImage(self, image: Any) -> None:
        """ 

`SetFooterImage`(*self*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterImage "Permalink to this definition")
Sets the zero-based index of the image associated with the footer item into the
image list.



Parameters
**image** – the zero-based index of the image associated with the footer item
into the image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterKind(self, kind) -> None:
        """ 

`SetFooterKind`(*self*, *kind*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterKind "Permalink to this definition")
Sets the footer item kind.



See also


[`SetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind") for a list of valid items kind.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterText(self, text: Any) -> None:
        """ 

`SetFooterText`(*self*, *text*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterText "Permalink to this definition")
Sets the text label for the footer item.



Parameters
**text** – the text label for the footer item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetFooterTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetFooterTextColour`(*self*, *colText*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetFooterTextColour "Permalink to this definition")
Sets the text colour for the footer item.



Parameters
**colText** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ 

`SetHyperText`(*self*, *hyper=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
**hyper** – `True` to set hypertext behaviour, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetId(self, id: Any) -> None:
        """ 

`SetId`(*self*, *id*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetId "Permalink to this definition")
Sets the zero-based item position.



Parameters
**id** – the zero-based item position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetImage(self, image: Any) -> None:
        """ 

`SetImage`(*self*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetImage "Permalink to this definition")
Sets the zero-based indexes of the images associated with the item into the
image list.



Parameters
**image** – a Python list with the zero-based indexes of the images
associated with the item into the image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetKind(self, kind: Any) -> None:
        """ 

`SetKind`(*self*, *kind*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetKind "Permalink to this definition")
Sets the item kind.



Parameters
**kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetMask(self, mask: ULC_MASK_STATE) -> None:
        """ 

`SetMask`(*self*, *mask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetMask "Permalink to this definition")
Sets the mask of valid fields.



Parameters
**mask** – any combination of the following bits:






| Mask Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_MASK_STATE` | 0x1 | [`GetState`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetState "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetState") is valid |
| `ULC_MASK_TEXT` | 0x2 | [`GetText`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetText "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetText") is valid |
| `ULC_MASK_IMAGE` | 0x4 | [`GetImage`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetImage "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetImage") is valid |
| `ULC_MASK_DATA` | 0x8 | [`GetData`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetData "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetData") is valid |
| `ULC_MASK_WIDTH` | 0x20 | [`GetWidth`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWidth "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWidth") is valid |
| `ULC_MASK_FORMAT` | 0x40 | [`GetFormat`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFormat "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFormat") is valid |
| `ULC_MASK_FONTCOLOUR` | 0x80 | [`GetTextColour`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetTextColour "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetTextColour") is valid |
| `ULC_MASK_FONT` | 0x100 | [`GetFont`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFont "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFont") is valid |
| `ULC_MASK_BACKCOLOUR` | 0x200 | [`GetBackgroundColour`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetBackgroundColour "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetBackgroundColour") is valid |
| `ULC_MASK_KIND` | 0x400 | [`GetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetKind "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetKind") is valid |
| `ULC_MASK_ENABLE` | 0x800 | [`IsEnabled`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsEnabled "wx.lib.agw.ultimatelistctrl.UltimateListItem.IsEnabled") is valid |
| `ULC_MASK_CHECK` | 0x1000 | [`IsChecked`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsChecked "wx.lib.agw.ultimatelistctrl.UltimateListItem.IsChecked") is valid |
| `ULC_MASK_HYPERTEXT` | 0x2000 | [`IsHyperText`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsHyperText "wx.lib.agw.ultimatelistctrl.UltimateListItem.IsHyperText") is valid |
| `ULC_MASK_WINDOW` | 0x4000 | [`GetWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWindow "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetWindow") is valid |
| `ULC_MASK_PYDATA` | 0x8000 | [`GetPyData`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetPyData "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetPyData") is valid |
| `ULC_MASK_SHOWN` | 0x10000 | [`IsShown`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsShown "wx.lib.agw.ultimatelistctrl.UltimateListItem.IsShown") is valid |
| `ULC_MASK_RENDERER` | 0x20000 | [`GetCustomRenderer`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetCustomRenderer "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetCustomRenderer") is valid |
| `ULC_MASK_OVERFLOW` | 0x40000 | [`GetOverFlow`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetOverFlow "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetOverFlow") is valid |
| `ULC_MASK_FOOTER_TEXT` | 0x80000 | [`GetFooterText`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterText "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterText") is valid |
| `ULC_MASK_FOOTER_IMAGE` | 0x100000 | [`GetFooterImage`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterImage "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterImage") is valid |
| `ULC_MASK_FOOTER_FORMAT` | 0x200000 | [`GetFooterFormat`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFormat "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFormat") is valid |
| `ULC_MASK_FOOTER_FONT` | 0x400000 | [`GetFooterFont`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFont "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterFont") is valid |
| `ULC_MASK_FOOTER_CHECK` | 0x800000 | [`IsFooterChecked`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.IsFooterChecked "wx.lib.agw.ultimatelistctrl.UltimateListItem.IsFooterChecked") is valid |
| `ULC_MASK_FOOTER_KIND` | 0x1000000 | [`GetFooterKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterKind "wx.lib.agw.ultimatelistctrl.UltimateListItem.GetFooterKind") is valid |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetOverFlow(self, over: bool=True) -> None:
        """ 

`SetOverFlow`(*self*, *over=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetOverFlow "Permalink to this definition")
Sets the item in the overflow/non overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
**over** – `True` to set the item in a overflow state, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetPyData(self, pyData) -> None:
        """ 

`SetPyData`(*self*, *pyData*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetPyData "Permalink to this definition")
Sets data for the item, which can be any Python object.



Parameters
**data** – any Python object associated to the item.





Note


Please note that Python data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetShown(self, shown: bool=True) -> None:
        """ 

`SetShown`(*self*, *shown=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetShown "Permalink to this definition")
Sets an item as shown/hidden.



Parameters
**shown** – `True` to show the item, `False` to hide it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetState(self, state: ULC_STATE_DONTCARE) -> None:
        """ 

`SetState`(*self*, *state*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetState "Permalink to this definition")
Sets the item state flags.



Parameters
**state** – any combination of the following bits:






| State Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_STATE_DONTCARE` | 0x0 | Don’t care what the state is |
| `ULC_STATE_DROPHILITED` | 0x1 | The item is highlighted to receive a drop event |
| `ULC_STATE_FOCUSED` | 0x2 | The item has the focus |
| `ULC_STATE_SELECTED` | 0x4 | The item is selected |
| `ULC_STATE_CUT` | 0x8 | The item is in the cut state |
| `ULC_STATE_DISABLED` | 0x10 | The item is disabled |
| `ULC_STATE_FILTERED` | 0x20 | The item has been filtered |
| `ULC_STATE_INUSE` | 0x40 | The item is in use |
| `ULC_STATE_PICKED` | 0x80 | The item has been picked |
| `ULC_STATE_SOURCE` | 0x100 | The item is a drag and drop source |








Note


The valid state flags are influenced by the value of the state mask.




See also


[`SetStateMask`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetStateMask "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetStateMask")





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetStateMask(self, stateMask: Any) -> None:
        """ 

`SetStateMask`(*self*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetStateMask "Permalink to this definition")
Sets the bitmask that is used to determine which of the state flags are
to be set.



Parameters
**stateMask** – the state bitmask.





See also


[`SetState`](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetState "wx.lib.agw.ultimatelistctrl.UltimateListItem.SetState") for a list of valid state bits.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetText(self, text: Any) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetText "Permalink to this definition")
Sets the text label for the item.



Parameters
**text** – the text label for the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colText*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetTextColour "Permalink to this definition")
Sets the text colour for the item.



Parameters
**colText** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetToolTip(self, text: Any) -> None:
        """ 

`SetToolTip`(*self*, *text*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetToolTip "Permalink to this definition")
Sets the tooltip text for the item.



Parameters
**text** – the tooltip text for the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ 

`SetVisited`(*self*, *visited=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetVisited "Permalink to this definition")
Sets whether an hypertext item was visited or not.



Parameters
**visited** – `True` to set a hypertext item as visited, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWidth(self, width: Any) -> None:
        """ 

`SetWidth`(*self*, *width*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetWidth "Permalink to this definition")
Sets the column width.



Parameters
**width** – the column width.





Note


This method is meaningful only for column headers in report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWindow(self, wnd, expand=False) -> None:
        """ 

`SetWindow`(*self*, *wnd*, *expand=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetWindow "Permalink to this definition")
Sets the window associated to the item.



Parameters
* **wnd** – a non-toplevel window to be displayed next to the item;
* **expand** – `True` to expand the column where the item/subitem lives,
so that the window will be fully visible.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ 

`SetWindowEnabled`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItem.SetWindowEnabled "Permalink to this definition")
Sets whether the associated window is enabled or not.



Parameters
**enable** – `True` to enable the associated window, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItem.html
        """



class UltimateListHeaderWindow(Control):
    """ This class holds the header window for [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
    """
    def __init__(self, win, id, owner, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name="UltimateListCtrlcolumntitles", isFooter=False) -> None:
        """ 

`__init__`(*self*, *win*, *id*, *owner*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *validator=wx.DefaultValidator*, *name="UltimateListCtrlcolumntitles"*, *isFooter=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – parent window. Must not be `None`;
* **id** – window identifier. A value of -1 indicates a default value;
* **owner** – an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl");
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the window style;
* **validator** – the window validator;
* **name** – the window name;
* **isFooter** – `True` if the [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") is in a footer
position, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def AdjustDC(self, dc: 'DC') -> None:
        """ 

`AdjustDC`(*self*, *dc*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.AdjustDC "Permalink to this definition")
Shifts the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") origin to match the position of the main window horizontal
scrollbar: this allows us to always use logical coordinates.



Parameters
**dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same size
as it would have after a call to *Fit()*.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DrawCurrent(self) -> None:
        """ 

`DrawCurrent`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.DrawCurrent "Permalink to this definition")
Force the redrawing of the column window.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def DrawTextFormatted(self, dc, text, rect) -> None:
        """ 

`DrawTextFormatted`(*self*, *dc*, *text*, *rect*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.DrawTextFormatted "Permalink to this definition")
Draws the item text, correctly formatted.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **text** – the item text;
* **rect** – the item client rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetOwner(self) -> None:
        """ 

`GetOwner`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.GetOwner "Permalink to this definition")
Returns the header window owner, an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetTextHeight(self) -> None:
        """ 

`GetTextHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.GetTextHeight "Permalink to this definition")
Returns the column text height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def GetWindowHeight(self) -> None:
        """ 

`GetWindowHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.GetWindowHeight "Permalink to this definition")
Returns the [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow") height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def HandleColumnCheck(self, column, pos) -> None:
        """ 

`HandleColumnCheck`(*self*, *column*, *pos*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.HandleColumnCheck "Permalink to this definition")
Handles the case in which a column contains a checkbox-like item.



Parameters
* **column** – the column index;
* **pos** – the mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def HitTestColumn(self, x, y) -> None:
        """ 

`HitTestColumn`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.HitTestColumn "Permalink to this definition")
HitTest method for column headers.



Parameters
* **x** – the mouse *x* position;
* **y** – the mouse *y* position.



Returns
The column index if any column client rectangle contains the mouse
position, `wx.NOT_FOUND` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ 

`IsColumnShown`(*self*, *column*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.IsColumnShown "Permalink to this definition")
Returns `True` if the input column is shown, `False` if it is hidden.



Parameters
**column** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnEnterWindow(self, event: MouseEvent) -> None:
        """ 

`OnEnterWindow`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnEnterWindow "Permalink to this definition")
Handles the `wx.EVT_ENTER_WINDOW` event for [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnInternalIdle(self) -> None:
        """ 

`OnInternalIdle`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnInternalIdle "Permalink to this definition")
This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an *OnIdle* handler in a derived class.


This method may be used to do delayed painting, for example, and most
implementations call [`wx.Window.UpdateWindowUI`](wx.Window.html#wx.Window.UpdateWindowUI "wx.Window.UpdateWindowUI") in order to send update events
to the window in idle time.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ 

`OnLeaveWindow`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnLeaveWindow "Permalink to this definition")
Handles the `wx.EVT_LEAVE_WINDOW` event for [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ 

`OnMouse`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnMouse "Permalink to this definition")
Handles the `wx.EVT_MOUSE_EVENTS` event for [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow").



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`UltimateListHeaderWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow "wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def SendListEvent(self, eventType, pos) -> None:
        """ 

`SendListEvent`(*self*, *eventType*, *pos*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.SendListEvent "Permalink to this definition")
Sends a [`UltimateListEvent`](wx.lib.agw.ultimatelistctrl.UltimateListEvent.html#wx.lib.agw.ultimatelistctrl.UltimateListEvent "wx.lib.agw.ultimatelistctrl.UltimateListEvent") for the parent window.



Parameters
* **eventType** – the event type;
* **pos** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """

    def SetCustomRenderer(self, renderer: Optional[Any]=None) -> None:
        """ 

`SetCustomRenderer`(*self*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.SetCustomRenderer "Permalink to this definition")
Associate a custom renderer with the header - all columns will use it



Parameters
**renderer** – a class able to correctly render header buttons





Note


the renderer class **must** implement the methods *DrawHeaderButton*
and *GetForegroundColor*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListHeaderWindow.html
        """



EVT_ENTER_WINDOW: int

EVT_LEAVE_WINDOW: int

EVT_MOUSE_EVENTS: int

EVT_PAINT: int

NOT_FOUND: int

class PyImageList:
    """ A [`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") contains a list of images. Images can have masks for
transparent drawing, and can be made from a variety of sources including
bitmaps and icons.


[`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") is used in conjunction with [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Note


The main improvements that [`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") introduces is the removal
of the limitation of same-size images inside the image list. If you use
the style `IL_VARIABLE_SIZE` then each image can have any size (in terms
of width and height).



  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
    """
    def __init__(self, width, height, mask=True, initialCount=1, style=IL_VARIABLE_SIZE) -> None:
        """ 

`__init__`(*self*, *width*, *height*, *mask=True*, *initialCount=1*, *style=IL\_VARIABLE\_SIZE*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **width** – the width of the images in the image list, in pixels (unused
if you specify the `IL_VARIABLE_SIZE` style;
* **height** – the height of the images in the image list, in pixels (unused
if you specify the `IL_VARIABLE_SIZE` style;
* **mask** – `True` if masks should be created for all images (unused in
[`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList"));
* **initialCount** – the initial size of the list (unused in [`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList"));
* **style** – can be one of the following bits:






| Style Flag | Value | Description |
| --- | --- | --- |
| `IL_FIXED_SIZE` | 0 | All the images in [`PyImageList`](#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") have the same size (width, height) |
| `IL_VARIABLE_SIZE` | 1 | Each image can have any size (in terms of width and height) |






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Add(self, bitmap: 'Bitmap') -> None:
        """ 

`Add`(*self*, *bitmap*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.Add "Permalink to this definition")
Adds a new image or images using a bitmap.



Parameters
**bitmap** – a valid [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") object.



Returns
The new zero-based image index.





Note


If the bitmap is wider than the images in the list and you are not using
the `IL_VARIABLE_SIZE` style, then the bitmap will automatically be split
into smaller images, each matching the dimensions of the image list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def AddIcon(self, icon: Icon) -> None:
        """ 

`AddIcon`(*self*, *icon*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.AddIcon "Permalink to this definition")
Adds a new image using an icon.



Parameters
**icon** – a valid `Icon` object.



Returns
The new zero-based image index.





Note


If the icon is wider than the images in the list and you are not using
the `IL_VARIABLE_SIZE` style, then the icon will automatically be split
into smaller images, each matching the dimensions of the image list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def AddWithColourMask(self, bitmap, maskColour) -> None:
        """ 

`AddWithColourMask`(*self*, *bitmap*, *maskColour*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.AddWithColourMask "Permalink to this definition")
Adds a new image or images using a bitmap and a colour mask.



Parameters
* **bitmap** – a valid [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") object;
* **colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour"), a colour indicating which parts
of the image are transparent.



Returns
The new zero-based image index.





Note


If the bitmap is wider than the images in the list and you are not using
the `IL_VARIABLE_SIZE` style, then the bitmap will automatically be split
into smaller images, each matching the dimensions of the image list.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Draw(self, index, dc, x, y, flags, solidBackground=True) -> None:
        """ 

`Draw`(*self*, *index*, *dc*, *x*, *y*, *flags*, *solidBackground=True*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.Draw "Permalink to this definition")
Draws a specified image onto a device context.



Parameters
* **index** – the image index, starting from zero;
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **x** – x position on the device context;
* **y** – y position on the device context;
* **flags** – how to draw the image. A bitlist of a selection of the following:





| Flag Paarameter | Description |
| --- | --- |
| `wx.IMAGELIST_DRAW_NORMAL` | Draw the image normally |
| `wx.IMAGELIST_DRAW_TRANSPARENT` | Draw the image with transparency |
| `wx.IMAGELIST_DRAW_SELECTED` | Draw the image in selected state |
| `wx.IMAGELIST_DRAW_FOCUSED` | Draw the image in a focused state |
* **solidBackground** – currently unused.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetBitmap(self, index: Any) -> None:
        """ 

`GetBitmap`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.GetBitmap "Permalink to this definition")
Returns the bitmap corresponding to the given *index*, or `NullBitmap`
if the index is invalid.



Parameters
**index** – the bitmap index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetIcon(self, index: Any) -> None:
        """ 

`GetIcon`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.GetIcon "Permalink to this definition")
Returns the icon corresponding to the given *index*, or `NullIcon`
if the index is invalid.



Parameters
**index** – the icon index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetImageCount(self) -> None:
        """ 

`GetImageCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.GetImageCount "Permalink to this definition")
Returns the number of images in the list.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def GetSize(self, index: Any) -> None:
        """ 

`GetSize`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.GetSize "Permalink to this definition")
Retrieves the size of an image in the list.



Parameters
**index** – the zero-based index of the image.



Returns
a tuple of *(width, height)* properties of the chosen bitmap.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Remove(self, index: Any) -> None:
        """ 

`Remove`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.Remove "Permalink to this definition")
Removes the image at the given position.



Parameters
**index** – the zero-based index of the image to be removed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def RemoveAll(self) -> None:
        """ 

`RemoveAll`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.RemoveAll "Permalink to this definition")
Removes all the images in the list.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def Replace(self, index, bitmap) -> None:
        """ 

`Replace`(*self*, *index*, *bitmap*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.Replace "Permalink to this definition")
Replaces the existing image with the new bitmap.



Parameters
* **index** – the index at which the image should be replaced;
* **bitmap** – the new bitmap to add to the image list, an instance of
[`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """

    def ReplaceIcon(self, index, icon) -> None:
        """ 

`ReplaceIcon`(*self*, *index*, *icon*)[¶](#wx.lib.agw.ultimatelistctrl.PyImageList.ReplaceIcon "Permalink to this definition")
Replaces the existing image with the new icon.



Parameters
* **index** – the index at which the image should be replaced;
* **icon** – the new icon to add to the image list, an instance of
`Icon`.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.PyImageList.html
        """



IMAGELIST_DRAW_NORMAL: int

IMAGELIST_DRAW_TRANSPARENT: int

IMAGELIST_DRAW_SELECTED: int

IMAGELIST_DRAW_FOCUSED: int

class UltimateListMainWindow(ScrolledWindow):
    """ This is the main widget implementation of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
    """
    def __init__(self, parent, id, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="listctrlmainwindow") -> None:
        """ 

`__init__`(*self*, *parent*, *id*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=0*, *name="listctrlmainwindow"*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – parent window. Must not be `None`;
* **id** – window identifier. A value of -1 indicates a default value;
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the underlying `ScrolledWindow` window style;
* **agwStyle** – the AGW-specific window style; can be almost any combination of the following
bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `ULC_VRULES` | 0x1 | Draws light vertical rules between rows in report mode. |
| `ULC_HRULES` | 0x2 | Draws light horizontal rules between rows in report mode. |
| `ULC_ICON` | 0x4 | Large icon view, with optional labels. |
| `ULC_SMALL_ICON` | 0x8 | Small icon view, with optional labels. |
| `ULC_LIST` | 0x10 | Multicolumn list view, with optional small icons. Columns are computed automatically, i.e. you don’t set columns as in `ULC_REPORT`. In other words, the list wraps, unlike a `ListBox`. |
| `ULC_REPORT` | 0x20 | Single or multicolumn report view, with optional header. |
| `ULC_ALIGN_TOP` | 0x40 | Icons align to the top. Win32 default, Win32 only. |
| `ULC_ALIGN_LEFT` | 0x80 | Icons align to the left. |
| `ULC_AUTOARRANGE` | 0x100 | Icons arrange themselves. Win32 only. |
| `ULC_VIRTUAL` | 0x200 | The application provides items text on demand. May only be used with `ULC_REPORT`. |
| `ULC_EDIT_LABELS` | 0x400 | Labels are editable: the application will be notified when editing starts. |
| `ULC_NO_HEADER` | 0x800 | No header in report mode. |
| `ULC_NO_SORT_HEADER` | 0x1000 | No Docs. |
| `ULC_SINGLE_SEL` | 0x2000 | Single selection (default is multiple). |
| `ULC_SORT_ASCENDING` | 0x4000 | Sort in ascending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_SORT_DESCENDING` | 0x8000 | Sort in descending order. (You must still supply a comparison callback in `ListCtrl.SortItems`.) |
| `ULC_TILE` | 0x10000 | Each item appears as a full-sized icon with a label of one or more lines beside it (partially implemented). |
| `ULC_NO_HIGHLIGHT` | 0x20000 | No highlight when an item is selected. |
| `ULC_STICKY_HIGHLIGHT` | 0x40000 | Items are selected by simply hovering on them, with no need to click on them. |
| `ULC_STICKY_NOSELEVENT` | 0x80000 | Don’t send a selection event when using `ULC_STICKY_HIGHLIGHT` style. |
| `ULC_SEND_LEFTCLICK` | 0x100000 | Send a left click event when an item is selected. |
| `ULC_HAS_VARIABLE_ROW_HEIGHT` | 0x200000 | The list has variable row heights. |
| `ULC_AUTO_CHECK_CHILD` | 0x400000 | When a column header has a checkbox associated, auto-check all the subitems in that column. |
| `ULC_AUTO_TOGGLE_CHILD` | 0x800000 | When a column header has a checkbox associated, toggle all the subitems in that column. |
| `ULC_AUTO_CHECK_PARENT` | 0x1000000 | Only meaningful foe checkbox-type items: when an item is checked/unchecked its column header item is checked/unchecked as well. |
| `ULC_SHOW_TOOLTIPS` | 0x2000000 | Show tooltips for ellipsized items/subitems (text too long to be shown in the available space) containing the full item/subitem text. |
| `ULC_HOT_TRACKING` | 0x4000000 | Enable hot tracking of items on mouse motion. |
| `ULC_BORDER_SELECT` | 0x8000000 | Changes border colour when an item is selected, instead of highlighting the item. |
| `ULC_TRACK_SELECT` | 0x10000000 | Enables hot-track selection in a list control. Hot track selection means that an item is automatically selected when the cursor remains over the item for a certain period of time. The delay is retrieved on Windows using the `win32api` call *win32gui.SystemParametersInfo(win32con.SPI\_GETMOUSEHOVERTIME)*, and is defaulted to 400ms on other platforms. This style applies to all views of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). |
| `ULC_HEADER_IN_ALL_VIEWS` | 0x20000000 | Show column headers in all view modes. |
| `ULC_NO_FULL_ROW_SELECT` | 0x40000000 | When an item is selected, the only the item in the first column is highlighted. |
| `ULC_FOOTER` | 0x80000000 | Show a footer too (only when header is present). |
| `ULC_USER_ROW_HEIGHT` | 0x100000000 | Allows to set a custom row height (one value for all the items, only in report mode). |
| `ULC_NO_ITEM_DRAG` | 0x200000000 | Disable item dragging |
* **name** – the window name.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def AutoCheckChild(self, isChecked, column) -> None:
        """ 

`AutoCheckChild`(*self*, *isChecked*, *column*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.AutoCheckChild "Permalink to this definition")
Checks/unchecks all the items.



Parameters
* **isChecked** – `True` to check the items, `False` to uncheck them;
* **column** – the column to which the items belongs to.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def AutoToggleChild(self, column: Any) -> None:
        """ 

`AutoToggleChild`(*self*, *column*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.AutoToggleChild "Permalink to this definition")
Toggles all the items.



Parameters
**column** – the column to which the items belongs to.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def CacheLineData(self, line: UltimateListLineData) -> None:
        """ 

`CacheLineData`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.CacheLineData "Permalink to this definition")
Saves the current line attributes.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").





Note


This method is used only if the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_VIRTUAL`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ChangeCurrent(self, current: Any) -> None:
        """ 

`ChangeCurrent`(*self*, *current*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ChangeCurrent "Permalink to this definition")
Changes the current line to the specified one.



Parameters
**current** – an integer specifying the index of the current line.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def CheckItem(self, item, checked=True, sendEvent=True) -> None:
        """ 

`CheckItem`(*self*, *item*, *checked=True*, *sendEvent=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.CheckItem "Permalink to this definition")
Actually checks/uncheks an item, sending (eventually) the two
events `EVT_LIST_ITEM_CHECKING` / `EVT_LIST_ITEM_CHECKED`.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **checked** – `True` to check an item, `False` to uncheck it;
* **sendEvent** – `True` to send a {UltimateListEvent}, `False` otherwise.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteAllItems "Permalink to this definition")
Deletes all items in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Note


This function does not send the `EVT_LIST_DELETE_ITEM` event because
deleting many items from the control would be too slow then (unlike [`DeleteItem`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteItem "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteItem")).





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteColumn(self, col: Any) -> None:
        """ 

`DeleteColumn`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteColumn "Permalink to this definition")
Deletes the specified column.



Parameters
**col** – the index of the column to delete.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteEverything(self) -> None:
        """ 

`DeleteEverything`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteEverything "Permalink to this definition")
Deletes all items in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"), resetting column widths to zero.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteItem(self, lindex: Any) -> None:
        """ 

`DeleteItem`(*self*, *lindex*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteItem "Permalink to this definition")
Deletes the specified item.



Parameters
**lindex** – the index of the item to delete.





Note


This function sends the `EVT_LIST_DELETE_ITEM` event for the item
being deleted.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DeleteItemWindow(self, item: UltimateListItem) -> None:
        """ 

`DeleteItemWindow`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DeleteItemWindow "Permalink to this definition")
Deletes the window associated to an item (if any).



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DoDeleteAllItems(self) -> None:
        """ 

`DoDeleteAllItems`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DoDeleteAllItems "Permalink to this definition")
Actually performs the deletion of all the items.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same size
as it would have after a call to *Fit()*.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DragFinish(self, event: MouseEvent) -> None:
        """ 

`DragFinish`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DragFinish "Permalink to this definition")
A drag and drop operation has just finished.



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawCheckbox(self, dc, x, y, kind, checked, enabled) -> None:
        """ 

`DrawCheckbox`(*self*, *dc*, *x*, *y*, *kind*, *checked*, *enabled*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DrawCheckbox "Permalink to this definition")
Draws the item checkbox/radiobutton image.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **x** – the x position where to draw the image;
* **y** – the y position where to draw the image;
* **kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |
* **checked** – `True` if the item is checked, `False` otherwise;
* **enabled** – `True` if the item is enabled, `False` if it is disabled.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawDnDArrow(self) -> None:
        """ 

`DrawDnDArrow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DrawDnDArrow "Permalink to this definition")
Draws a drag and drop visual representation of an arrow.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def DrawImage(self, index, dc, x, y, enabled) -> None:
        """ 

`DrawImage`(*self*, *index*, *dc*, *x*, *y*, *enabled*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.DrawImage "Permalink to this definition")
Draws one of the item images.



Parameters
* **index** – the index of the image inside the image list;
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **x** – the x position where to draw the image;
* **y** – the y position where to draw the image;
* **enabled** – `True` if the item is enabled, `False` if it is disabled.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EditLabel(self, item: UltimateListItem) -> None:
        """ 

`EditLabel`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.EditLabel "Permalink to this definition")
Starts editing an item label.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableItem(self, item, enable=True) -> None:
        """ 

`EnableItem`(*self*, *item*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.EnableItem "Permalink to this definition")
Enables/disables an item.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **enable** – `True` to enable the item, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ 

`EnableSelectionGradient`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.EnableSelectionGradient "Permalink to this definition")
Globally enables/disables drawing of gradient selections.



Parameters
**enable** – `True` to enable gradient-style selections, `False`
to disable it.





Note


Calling this method disables any Vista-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ 

`EnableSelectionVista`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.EnableSelectionVista "Permalink to this definition")
Globally enables/disables drawing of Windows Vista selections.



Parameters
**enable** – `True` to enable Vista-style selections, `False` to
disable it.





Note


Calling this method disables any gradient-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def EnsureVisible(self, index: Any) -> None:
        """ 

`EnsureVisible`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.EnsureVisible "Permalink to this definition")
Ensures this item is visible.



Parameters
**index** – the index of the item to scroll into view.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItem(self, start, string, partial=False) -> None:
        """ 

`FindItem`(*self*, *start*, *string*, *partial=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.FindItem "Permalink to this definition")
Find an item whose label matches this string.



Parameters
* **start** – the starting point of the input `string` or the beginning
if *start* is -1;
* **string** – the string to look for matches;
* **partial** – if `True` then this method will look for items which
begin with `string`.





Note


The string comparison is case insensitive.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItemAtPos(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`FindItemAtPos`(*self*, *pt*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.FindItemAtPos "Permalink to this definition")
Find an item nearest this position.



Parameters
**pt** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def FindItemData(self, start, data) -> None:
        """ 

`FindItemData`(*self*, *start*, *data*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.FindItemData "Permalink to this definition")
Find an item whose data matches this data.



Parameters
* **start** – the starting point of the input *data* or the beginning
if *start* is -1;
* **data** – the data to look for matches.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetBackgroundImage(self) -> None:
        """ 

`GetBackgroundImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetBackgroundImage "Permalink to this definition")
Returns the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") background image (if any).



Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCheckboxImageSize(self) -> None:
        """ 

`GetCheckboxImageSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetCheckboxImageSize "Permalink to this definition")
Returns the checkbox/radiobutton image size.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCheckedItemCount(self, col: Any=0) -> int:
        """ 

`GetCheckedItemCount`(*self*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetCheckedItemCount "Permalink to this definition")
Returns the number of checked items in the given column.



Parameters
**col** – an integer specifying the column index.



Returns
the number of checked items.



Return type
int






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumn(self, col: Any) -> None:
        """ 

`GetColumn`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetColumn "Permalink to this definition")
Returns information about this column.



Parameters
**col** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnCount(self) -> None:
        """ 

`GetColumnCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetColumnCount "Permalink to this definition")
Returns the total number of columns in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnCustomRenderer(self, col: Any) -> None:
        """ 

`GetColumnCustomRenderer`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetColumnCustomRenderer "Permalink to this definition")
Returns the custom renderer used to draw the column header



Parameters
**col** – the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetColumnWidth(self, col: Any) -> None:
        """ 

`GetColumnWidth`(*self*, *col*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetColumnWidth "Permalink to this definition")
Returns the column width for the input column.



Parameters
**col** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetControlBmp(self, checkbox=True, checked=False, enabled=True, x=16, y=16) -> None:
        """ 

`GetControlBmp`(*self*, *checkbox=True*, *checked=False*, *enabled=True*, *x=16*, *y=16*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetControlBmp "Permalink to this definition")
Returns a native looking checkbox or radio button bitmap.



Parameters
* **checkbox** – `True` to get a checkbox image, `False` for a radiobutton
one;
* **checked** – `True` if the control is marked, `False` if it is not;
* **enabled** – `True` if the control is enabled, `False` if it is not;
* **x** – the width of the bitmap, in pixels;
* **y** – the height of the bitmap, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetCountPerPage(self) -> None:
        """ 

`GetCountPerPage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetCountPerPage "Permalink to this definition")
Returns the number of items that can fit vertically in the visible area
of the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") (list or report view) or the total number of
items in the list control (icon or small icon view).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetDisabledTextColour(self) -> None:
        """ 

`GetDisabledTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetDisabledTextColour "Permalink to this definition")
Returns the items disabled colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetDummyLine(self) -> None:
        """ 

`GetDummyLine`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetDummyLine "Permalink to this definition")
Returns a dummy line.



Note


This method is used only if the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_VIRTUAL`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetFirstGradientColour(self) -> None:
        """ 

`GetFirstGradientColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetFirstGradientColour "Permalink to this definition")
Returns the first gradient colour for gradient-style selections.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetGradientStyle(self) -> None:
        """ 

`GetGradientStyle`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetGradientStyle "Permalink to this definition")
Returns the gradient style for gradient-style selections.



Returns
0 for horizontal gradient-style selections, 1 for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHeaderWidth(self) -> None:
        """ 

`GetHeaderWidth`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetHeaderWidth "Permalink to this definition")
Returns the header window width, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHighlightBrush(self) -> None:
        """ 

`GetHighlightBrush`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetHighlightBrush "Permalink to this definition")
Returns the brush to use for the item highlighting.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextFont(self) -> None:
        """ 

`GetHyperTextFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetHyperTextFont "Permalink to this definition")
Returns the font used to render an hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ 

`GetHyperTextNewColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetHyperTextNewColour "Permalink to this definition")
Returns the colour used to render a non-visited hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ 

`GetHyperTextVisitedColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetHyperTextVisitedColour "Permalink to this definition")
Returns the colour used to render a visited hypertext item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetImageSize(self, index: Any) -> None:
        """ 

`GetImageSize`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetImageSize "Permalink to this definition")
Returns the image size for the item.



Parameters
**index** – the image index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItem(self, item, col=0) -> None:
        """ 

`GetItem`(*self*, *item*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItem "Permalink to this definition")
Returns the information about the input item.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **col** – the column to which the item belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemCount(self) -> None:
        """ 

`GetItemCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemCount "Permalink to this definition")
Returns the number of items in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemCustomRenderer(self, item: UltimateListItem) -> None:
        """ 

`GetItemCustomRenderer`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemCustomRenderer "Permalink to this definition")
Returns the custom renderer used to draw the input item (if any).



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemKind(self, item: UltimateListItem) -> None:
        """ 

`GetItemKind`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemKind "Permalink to this definition")
Returns the item kind.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").





See also


[`SetItemKind`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemKind "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemOverFlow(self, item: UltimateListItem) -> None:
        """ 

`GetItemOverFlow`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemOverFlow "Permalink to this definition")
Returns if the item is in the overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemPosition(self, item: Any) -> None:
        """ 

`GetItemPosition`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemPosition "Permalink to this definition")
Returns the position of the item, in icon or small icon view.



Parameters
**item** – the row in which the item lives.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemRect(self, item: Any) -> None:
        """ 

`GetItemRect`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemRect "Permalink to this definition")
Returns the rectangle representing the item’s size and position, in physical
coordinates.



Parameters
**item** – the row in which the item lives.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemSpacing(self, isSmall: bool=False) -> None:
        """ 

`GetItemSpacing`(*self*, *isSmall=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemSpacing "Permalink to this definition")
Returns the spacing between item texts and icons, in pixels.



Parameters
**isSmall** – `True` if using a `wx.IMAGE_LIST_SMALL` image list,
`False` if using a `wx.IMAGE_LIST_NORMAL` image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemState(self, item, stateMask) -> None:
        """ 

`GetItemState`(*self*, *item*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemState "Permalink to this definition")
Returns the item state flags for the input item.



Parameters
* **item** – the index of the item;
* **stateMask** – the bitmask for the state flag.





See also


[`SetItemStateAll`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemStateAll "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemStateAll") for a list of valid state flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemText(self, item: UltimateListItem) -> None:
        """ 

`GetItemText`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemText "Permalink to this definition")
Returns the item text.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemTextSize(self, item: UltimateListItem) -> None:
        """ 

`GetItemTextSize`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemTextSize "Permalink to this definition")
Returns the item width, in pixels, considering only the item text.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemVisited(self, item: UltimateListItem) -> None:
        """ 

`GetItemVisited`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemVisited "Permalink to this definition")
Returns whether an hypertext item was visited.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWidthWithImage(self, item: UltimateListItem) -> None:
        """ 

`GetItemWidthWithImage`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemWidthWithImage "Permalink to this definition")
Returns the item width, in pixels, considering the item text and its images.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWindow(self, item: UltimateListItem) -> None:
        """ 

`GetItemWindow`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemWindow "Permalink to this definition")
Returns the window associated to the item (if any).



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetItemWindowEnabled(self, item: UltimateListItem) -> None:
        """ 

`GetItemWindowEnabled`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemWindowEnabled "Permalink to this definition")
Returns whether the window associated to the item is enabled.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLine(self, n: Any) -> None:
        """ 

`GetLine`(*self*, *n*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLine "Permalink to this definition")
Returns the line data for the given index.



Parameters
**n** – the line index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineCheckboxRect(self, line: UltimateListLineData) -> None:
        """ 

`GetLineCheckboxRect`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineCheckboxRect "Permalink to this definition")
Returns the line client rectangle for the item checkbox image only.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineHeight(self, item: Optional[None]=None) -> None:
        """ 

`GetLineHeight`(*self*, *item=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineHeight "Permalink to this definition")
Returns the line height for a specific item.



Parameters
**item** – if not `None`, an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineHighlightRect(self, line: UltimateListLineData) -> None:
        """ 

`GetLineHighlightRect`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineHighlightRect "Permalink to this definition")
Returns the line client rectangle when the line is highlighted.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineIconRect(self, line: UltimateListLineData) -> None:
        """ 

`GetLineIconRect`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineIconRect "Permalink to this definition")
Returns the line client rectangle for the item image only.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineLabelRect(self, line: UltimateListLineData, col=0) -> None:
        """ 

`GetLineLabelRect`(*self*, *line*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineLabelRect "Permalink to this definition")
Returns the line client rectangle for the item text only.
Note this is the full column width unless an image or
checkbox exists. It is not the width of the text itself



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineRect(self, line: UltimateListLineData) -> None:
        """ 

`GetLineRect`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineRect "Permalink to this definition")
Returns the line client rectangle.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineSize(self, line: UltimateListLineData) -> None:
        """ 

`GetLineSize`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineSize "Permalink to this definition")
Returns the size of the total line client rectangle.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetLineY(self, line: UltimateListLineData) -> None:
        """ 

`GetLineY`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineY "Permalink to this definition")
Returns the line *y* position.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetListCtrl(self) -> None:
        """ 

`GetListCtrl`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetListCtrl "Permalink to this definition")
Returns the parent widget, an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetMainWindowOfCompositeControl(self) -> None:
        """ 

`GetMainWindowOfCompositeControl`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetMainWindowOfCompositeControl "Permalink to this definition")
Returns the [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow") parent.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetNextActiveItem(self, item, down=True) -> None:
        """ 

`GetNextActiveItem`(*self*, *item*, *down=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetNextActiveItem "Permalink to this definition")
Returns the next active item. Used Internally at present.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **down** – `True` to search downwards for an active item, `False`
to search upwards.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetNextItem(self, item, geometry=ULC_NEXT_ALL, state=ULC_STATE_DONTCARE) -> None:
        """ 

`GetNextItem`(*self*, *item*, *geometry=ULC\_NEXT\_ALL*, *state=ULC\_STATE\_DONTCARE*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetNextItem "Permalink to this definition")
Searches for an item with the given *geometry* or *state*, starting from *item*
but excluding the *item* itself.



Parameters
* **item** – the item at which starting the search. If set to -1, the first
item that matches the specified flags will be returned.
* **geometry** – can be one of:






| Geometry Flag | Hex Value | Description |
| --- | --- | --- |
| `ULC_NEXT_ABOVE` | 0x0 | Searches for an item above the specified item |
| `ULC_NEXT_ALL` | 0x1 | Searches for subsequent item by index |
| `ULC_NEXT_BELOW` | 0x2 | Searches for an item below the specified item |
| `ULC_NEXT_LEFT` | 0x3 | Searches for an item to the left of the specified item |
| `ULC_NEXT_RIGHT` | 0x4 | Searches for an item to the right of the specified item |
* **state** – any combination of the following bits:






| State Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_STATE_DONTCARE` | 0x0 | Don’t care what the state is |
| `ULC_STATE_DROPHILITED` | 0x1 | The item is highlighted to receive a drop event |
| `ULC_STATE_FOCUSED` | 0x2 | The item has the focus |
| `ULC_STATE_SELECTED` | 0x4 | The item is selected |
| `ULC_STATE_CUT` | 0x8 | The item is in the cut state |
| `ULC_STATE_DISABLED` | 0x10 | The item is disabled |
| `ULC_STATE_FILTERED` | 0x20 | The item has been filtered |
| `ULC_STATE_INUSE` | 0x40 | The item is in use |
| `ULC_STATE_PICKED` | 0x80 | The item has been picked |
| `ULC_STATE_SOURCE` | 0x100 | The item is a drag and drop source |



Returns
The first item with given *state* following *item* or -1 if no such item found.





Note


This function may be used to find all selected items in the
control like this:



```
item = -1

while 1:
    item = listctrl.GetNextItem(item, ULC_NEXT_ALL, ULC_STATE_SELECTED)

    if item == -1:
        break

    # This item is selected - do whatever is needed with it

    wx.LogMessage("Item %ld is selected."%item)

```





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetRuleColour(self) -> None:
        """ 

`GetRuleColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetRuleColour "Permalink to this definition")
Returns the colour to be used for drawing the horizontal and vertical rules.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSecondGradientColour(self) -> None:
        """ 

`GetSecondGradientColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetSecondGradientColour "Permalink to this definition")
Returns the second gradient colour for gradient-style selections.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSelectedItemCount(self) -> None:
        """ 

`GetSelectedItemCount`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetSelectedItemCount "Permalink to this definition")
Returns the number of selected items in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetSubItemRect(self, item, subItem) -> None:
        """ 

`GetSubItemRect`(*self*, *item*, *subItem*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetSubItemRect "Permalink to this definition")
Returns the rectangle representing the size and position, in physical coordinates,
of the given subitem, i.e. the part of the row *item* in the column *subItem*.



Parameters
* **item** – the row in which the item lives;
* **subItem** – the column in which the item lives. If set equal to the special
value `ULC_GETSUBITEMRECT_WHOLEITEM` the return value is the same as for
[`GetItemRect`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemRect "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetItemRect").





Note


This method is only meaningful when the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") is in the
report mode.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetTextLength(self, s: Any) -> None:
        """ 

`GetTextLength`(*self*, *s*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetTextLength "Permalink to this definition")
Returns the text width for the input string.



Parameters
**s** – the string to measure.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetTotalWidth(self) -> None:
        """ 

`GetTotalWidth`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetTotalWidth "Permalink to this definition")
Returns the total width of the columns in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetUserLineHeight(self) -> None:
        """ 

`GetUserLineHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetUserLineHeight "Permalink to this definition")
Returns the custom value for the [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow") item height, if previously set with
[`SetUserLineHeight`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetUserLineHeight "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetUserLineHeight").



Note


This method can be used only with `ULC_REPORT` and `ULC_USER_ROW_HEIGHT` styles set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetViewRect(self) -> None:
        """ 

`GetViewRect`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetViewRect "Permalink to this definition")
Returns the rectangle taken by all items in the control. In other words,
if the controls client size were equal to the size of this rectangle, no
scrollbars would be needed and no free space would be left.



Note


This function only works in the icon and small icon views, not in
list or report views.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetVisibleLinesRange(self) -> None:
        """ 

`GetVisibleLinesRange`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetVisibleLinesRange "Permalink to this definition")
Returns the range of visible items on screen.



Note


This method can be used only if [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_REPORT`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def GetWaterMark(self) -> None:
        """ 

`GetWaterMark`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetWaterMark "Permalink to this definition")
Returns the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") watermark image (if any), displayed in the
bottom right part of the window.



Todo


Better support for this is needed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HandleHyperLink(self, item: UltimateListItem) -> None:
        """ 

`HandleHyperLink`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HandleHyperLink "Permalink to this definition")
Handles the hyperlink items, sending the `EVT_LIST_ITEM_HYPERLINK` event.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasAGWFlag(self, flag: Any) -> None:
        """ 

`HasAGWFlag`(*self*, *flag*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HasAGWFlag "Permalink to this definition")
Returns `True` if the window has the given *flag* bit set.



Parameters
**flag** – the bit to check.





See also


[`UltimateListCtrl.SetSingleStyle()`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetSingleStyle "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetSingleStyle") for a list of valid flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasCurrent(self) -> None:
        """ 

`HasCurrent`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HasCurrent "Permalink to this definition")
Returns `True` if the current item has been set, either programmatically
or by user intervention.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasFocus(self) -> None:
        """ 

`HasFocus`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HasFocus "Permalink to this definition")
Returns `True` if the window has focus.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasFooter(self) -> None:
        """ 

`HasFooter`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HasFooter "Permalink to this definition")
Returns `True` if the footer window is shown.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HasHeader(self) -> None:
        """ 

`HasHeader`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HasHeader "Permalink to this definition")
Returns `True` if the header window is shown.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HideWindows(self) -> None:
        """ 

`HideWindows`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HideWindows "Permalink to this definition")
Hides the windows associated to the items. Used internally.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightAll(self, on: bool=True) -> None:
        """ 

`HighlightAll`(*self*, *on=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HighlightAll "Permalink to this definition")
Highlights/unhighlights all the lines in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**on** – `True` to highlight all the lines, `False` to unhighlight them.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightLine(self, line, highlight=True) -> None:
        """ 

`HighlightLine`(*self*, *line*, *highlight=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HighlightLine "Permalink to this definition")
Highlights a line in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData");
* **highlight** – `True` to highlight the line, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HighlightLines(self, lineFrom, lineTo, highlight=True) -> None:
        """ 

`HighlightLines`(*self*, *lineFrom*, *lineTo*, *highlight=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HighlightLines "Permalink to this definition")
Highlights a range of lines in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **lineFrom** – an integer representing the first line to highlight;
* **lineTo** – an integer representing the last line to highlight;
* **highlight** – `True` to highlight the lines, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTest "Permalink to this definition")
HitTest method for a [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **x** – the mouse *x* position;
* **y** – the mouse *y* position.





See also


[`HitTestLine`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTestLine "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTestLine") for a list of return flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def HitTestLine(self, line, x, y) -> None:
        """ 

`HitTestLine`(*self*, *line*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.HitTestLine "Permalink to this definition")
HitTest method for a [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") line.



Parameters
* **line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData");
* **x** – the mouse *x* position;
* **y** – the mouse *y* position.



Returns
a tuple of values, representing the item hit and a hit flag. The
hit flag can be one of the following bits:








| HitTest Flag | Hex Value | Description |
| --- | --- | --- |
| `ULC_HITTEST_ABOVE` | 0x1 | Above the client area |
| `ULC_HITTEST_BELOW` | 0x2 | Below the client area |
| `ULC_HITTEST_NOWHERE` | 0x4 | In the client area but below the last item |
| `ULC_HITTEST_ONITEM` | 0x2a0 | Anywhere on the item (text, icon, checkbox image) |
| `ULC_HITTEST_ONITEMICON` | 0x20 | On the bitmap associated with an item |
| `ULC_HITTEST_ONITEMLABEL` | 0x80 | On the label (string) associated with an item |
| `ULC_HITTEST_ONITEMSTATEICON` | 0x200 | On the state icon for a list view item that is in a user-defined state |
| `ULC_HITTEST_TOLEFT` | 0x400 | To the left of the client area |
| `ULC_HITTEST_TORIGHT` | 0x800 | To the right of the client area |
| `ULC_HITTEST_ONITEMCHECK` | 0x1000 | On the item checkbox (if any) |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.Init "Permalink to this definition")
Initializes the [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow") widget.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InReportView(self) -> None:
        """ 

`InReportView`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.InReportView "Permalink to this definition")
Returns `True` if the window is in report mode.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InsertColumn(self, col, item) -> None:
        """ 

`InsertColumn`(*self*, *col*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.InsertColumn "Permalink to this definition")
Inserts a column into [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **col** – the column index at which we wish to insert a new column;
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").



Returns
the index at which the column has been inserted.





Note


This method is meaningful only if [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_REPORT`
or the `ULC_TILE` styles set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InsertItem(self, item: UltimateListItem) -> None:
        """ 

`InsertItem`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.InsertItem "Permalink to this definition")
Inserts an item into [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def InTileView(self) -> None:
        """ 

`InTileView`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.InTileView "Permalink to this definition")
Returns `True` if the window is in tile mode (partially implemented).



Todo


Fully implement tile view for [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsColumnShown(self, column: Any) -> None:
        """ 

`IsColumnShown`(*self*, *column*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsColumnShown "Permalink to this definition")
Returns `True` if the input column is shown, `False` if it is hidden.



Parameters
**column** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsEmpty(self) -> None:
        """ 

`IsEmpty`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsEmpty "Permalink to this definition")
Returns `True` if the window has no items in it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsHighlighted(self, line: UltimateListLineData) -> None:
        """ 

`IsHighlighted`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsHighlighted "Permalink to this definition")
Returns `True` if the input line is highlighted.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemChecked(self, item: UltimateListItem) -> None:
        """ 

`IsItemChecked`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsItemChecked "Permalink to this definition")
Returns whether an item is checked or not.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemEnabled(self, item: UltimateListItem) -> None:
        """ 

`IsItemEnabled`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsItemEnabled "Permalink to this definition")
Returns whether an item is enabled or not.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsItemHyperText(self, item: UltimateListItem) -> None:
        """ 

`IsItemHyperText`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsItemHyperText "Permalink to this definition")
Returns whether an item is hypertext or not.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsSingleSel(self) -> None:
        """ 

`IsSingleSel`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsSingleSel "Permalink to this definition")
Returns `True` if we are in single selection mode, `False` if multi selection.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def IsVirtual(self) -> None:
        """ 

`IsVirtual`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.IsVirtual "Permalink to this definition")
Returns `True` if the window has the `ULC_VIRTUAL` style set.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def MoveToFocus(self) -> None:
        """ 

`MoveToFocus`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.MoveToFocus "Permalink to this definition")
Brings the current item into view.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def MoveToItem(self, item: UltimateListItem) -> None:
        """ 

`MoveToItem`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.MoveToItem "Permalink to this definition")
Scrolls the input item into view.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnArrowChar(self, newCurrent, event) -> None:
        """ 

`OnArrowChar`(*self*, *newCurrent*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnArrowChar "Permalink to this definition")
Handles the keyboard arrows key events.



Parameters
* **newCurrent** – an integer specifying the new current item;
* **event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnChar "Permalink to this definition")
Handles the `wx.EVT_CHAR` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnChildFocus(self, event: ChildFocusEvent) -> None:
        """ 

`OnChildFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnChildFocus "Permalink to this definition")
Handles the `wx.EVT_CHILD_FOCUS` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `ChildFocusEvent` event to be processed.





Note


This method is intentionally empty to prevent the default handler in
`ScrolledWindow` from needlessly scrolling the window when the edit
control is dismissed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnCompareItems(self, line1, line2) -> None:
        """ 

`OnCompareItems`(*self*, *line1*, *line2*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnCompareItems "Permalink to this definition")
Returns whether 2 lines have the same index.


Override this function in the derived class to change the sort order of the items
in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). The function should return a negative, zero or positive
value if the first line is less than, equal to or greater than the second one.



Parameters
* **line1** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **line2** – another instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").





Note


The base class version compares lines by their index.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `EraseEvent` event to be processed.





Note


This method is intentionally empty to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnHoverTimer(self, event: TimerEvent) -> None:
        """ 

`OnHoverTimer`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnHoverTimer "Permalink to this definition")
Handles the `wx.EVT_TIMER` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `TimerEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnKeyDown "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ 

`OnMouse`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnMouse "Permalink to this definition")
Handles the `wx.EVT_MOUSE_EVENTS` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameAccept(self, itemEdit, value) -> None:
        """ 

`OnRenameAccept`(*self*, *itemEdit*, *value*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnRenameAccept "Permalink to this definition")
Called by [`UltimateListTextCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl"), to accept the changes and to send the
`EVT_LIST_END_LABEL_EDIT` event.



Parameters
* **itemEdit** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **value** – the new value of the item label.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameCancelled(self, itemEdit) -> None:
        """ 

`OnRenameCancelled`(*self*, *itemEdit*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnRenameCancelled "Permalink to this definition")
Called by [`UltimateListTextCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl"), to cancel the changes and to send the
`EVT_LIST_END_LABEL_EDIT` event.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnRenameTimer(self) -> None:
        """ 

`OnRenameTimer`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnRenameTimer "Permalink to this definition")
The timer for renaming has expired. Start editing.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnScroll(self, event: ScrollEvent) -> None:
        """ 

`OnScroll`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnScroll "Permalink to this definition")
Handles the `wx.EVT_SCROLLWIN` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `ScrollEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def PaintWaterMark(self, dc: 'DC') -> None:
        """ 

`PaintWaterMark`(*self*, *dc*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.PaintWaterMark "Permalink to this definition")
Draws a watermark at the bottom right of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
**dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC").





Todo


Better support for this is needed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RecalculatePositions(self, noRefresh: bool=False) -> None:
        """ 

`RecalculatePositions`(*self*, *noRefresh=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RecalculatePositions "Permalink to this definition")
Recalculates all the items positions, and sets the scrollbars positions
too.



Parameters
**noRefresh** – `True` to avoid calling `Refresh`, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshAfter(self, lineFrom: Any) -> None:
        """ 

`RefreshAfter`(*self*, *lineFrom*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RefreshAfter "Permalink to this definition")
Redraws all the lines after the input one.



Parameters
**lineFrom** – an integer representing the first line to refresh.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshAll(self) -> None:
        """ 

`RefreshAll`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RefreshAll "Permalink to this definition")
Refreshes the entire [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshLine(self, line: UltimateListLineData) -> None:
        """ 

`RefreshLine`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RefreshLine "Permalink to this definition")
Redraws the input line.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshLines(self, lineFrom, lineTo) -> None:
        """ 

`RefreshLines`(*self*, *lineFrom*, *lineTo*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RefreshLines "Permalink to this definition")
Redraws a range of lines in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **lineFrom** – an integer representing the first line to refresh;
* **lineTo** – an integer representing the last line to refresh.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def RefreshSelected(self) -> None:
        """ 

`RefreshSelected`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.RefreshSelected "Permalink to this definition")
Redraws the selected lines.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetCurrent(self) -> None:
        """ 

`ResetCurrent`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ResetCurrent "Permalink to this definition")
Resets the current item to `None`.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetLineDimensions(self, force: bool=False) -> None:
        """ 

`ResetLineDimensions`(*self*, *force=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ResetLineDimensions "Permalink to this definition")
Resets the line dimensions, so that client rectangles and positions are
recalculated.



Parameters
**force** – `True` to reset all line dimensions.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetTextControl(self) -> None:
        """ 

`ResetTextControl`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ResetTextControl "Permalink to this definition")
Called by [`UltimateListTextCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl "wx.lib.agw.ultimatelistctrl.UltimateListTextCtrl") when it marks itself for deletion.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResetVisibleLinesRange(self, reset: bool=False) -> None:
        """ 

`ResetVisibleLinesRange`(*self*, *reset=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ResetVisibleLinesRange "Permalink to this definition")
Forces us to recalculate the range of visible lines.



Parameters
**reset** – `True` to reset all line dimensions, which will then be
recalculated.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ResizeColumns(self) -> None:
        """ 

`ResizeColumns`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ResizeColumns "Permalink to this definition")
If `ULC_AUTOSIZE_FILL` was passed to [`UltimateListCtrl.SetColumnWidth()`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnWidth "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.SetColumnWidth") then
that column’s width will be expanded to fill the window on a resize event.


Called by [`UltimateListCtrl.OnSize()`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnSize "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnSize") when the window is resized.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ReverseHighlight(self, line: UltimateListLineData) -> None:
        """ 

`ReverseHighlight`(*self*, *line*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ReverseHighlight "Permalink to this definition")
Toggles the line state and refreshes it.



Parameters
**line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def ScrollList(self, dx, dy) -> None:
        """ 

`ScrollList`(*self*, *dx*, *dy*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.ScrollList "Permalink to this definition")
Scrolls the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").



Parameters
* **dx** – if in icon, small icon or report view mode, specifies the number
of pixels to scroll. If in list view mode, *dx* specifies the number of
columns to scroll.
* **dy** – always specifies the number of pixels to scroll vertically.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SendNotify(self, line, command, point=wx.DefaultPosition, col=0) -> None:
        """ 

`SendNotify`(*self*, *line*, *command*, *point=wx.DefaultPosition*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SendNotify "Permalink to this definition")
Actually sends a [`UltimateListEvent`](wx.lib.agw.ultimatelistctrl.UltimateListEvent.html#wx.lib.agw.ultimatelistctrl.UltimateListEvent "wx.lib.agw.ultimatelistctrl.UltimateListEvent").



Parameters
* **line** – an instance of [`UltimateListLineData`](wx.lib.agw.ultimatelistctrl.UltimateListLineData.html#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData");
* **command** – the event type to send;
* **point** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").
* **col** – an integer specifying the column index.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetBackgroundImage(self, image: None) -> None:
        """ 

`SetBackgroundImage`(*self*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetBackgroundImage "Permalink to this definition")
Sets the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") background image.



Parameters
**image** – if not `None`, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").





Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumn(self, col, item) -> None:
        """ 

`SetColumn`(*self*, *col*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetColumn "Permalink to this definition")
Sets information about this column.



Parameters
* **col** – an integer specifying the column index;
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumnCustomRenderer(self, col=0, renderer=None) -> None:
        """ 

`SetColumnCustomRenderer`(*self*, *col=0*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetColumnCustomRenderer "Permalink to this definition")
Associate a custom renderer to this column’s header



Parameters
* **col** – the column index.
* **renderer** – a class able to correctly render the input item.





Note


the renderer class **must** implement the methods *DrawHeaderButton*
and *GetForegroundColor*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetColumnWidth(self, col, width: 'LIST_AUTOSIZE') -> None:
        """ 

`SetColumnWidth`(*self*, *col*, *width*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetColumnWidth "Permalink to this definition")
Sets the column width.



Parameters
**width** – can be a width in pixels or `wx.LIST_AUTOSIZE` (-1) or
`wx.LIST_AUTOSIZE_USEHEADER` (-2) or `ULC_AUTOSIZE_FILL` (-3).
`wx.LIST_AUTOSIZE` will resize the column to the length of its longest
item. `wx.LIST_AUTOSIZE_USEHEADER` will resize the column to the
length of the header (Win32) or 80 pixels (other platforms).
`ULC_AUTOSIZE_FILL` will resize the column fill the remaining width
of the window.





Note


In small or normal icon view, col must be -1, and the column width
is set for all columns.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetDisabledTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetDisabledTextColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetDisabledTextColour "Permalink to this definition")
Sets the items disabled colour.



Parameters
**colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetFirstGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetFirstGradientColour "Permalink to this definition")
Sets the first gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour is taken from the system value `wx.SYS_COLOUR_HIGHLIGHT`.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetFont "Permalink to this definition")
Overridden base class virtual to reset the line height when the font changes.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") object.





Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetGradientStyle(self, vertical: Any=0) -> None:
        """ 

`SetGradientStyle`(*self*, *vertical=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetGradientStyle "Permalink to this definition")
Sets the gradient style for gradient-style selections.



Parameters
**vertical** – 0 for horizontal gradient-style selections, 1 for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ 

`SetHyperTextFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetHyperTextFont "Permalink to this definition")
Sets the font used to render hypertext items.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextNewColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetHyperTextNewColour "Permalink to this definition")
Sets the colour used to render a non-visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextVisitedColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetHyperTextVisitedColour "Permalink to this definition")
Sets the colour used to render a visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetImageList(self, imageList, which) -> None:
        """ 

`SetImageList`(*self*, *imageList*, *which*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetImageList "Permalink to this definition")
Sets the image list associated with the control.



Parameters
* **imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList") or an instance of [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList");
* **which** – one of `wx.IMAGE_LIST_NORMAL`, `wx.IMAGE_LIST_SMALL`,
`wx.IMAGE_LIST_STATE` (the last is unimplemented).





Note


Using [`PyImageList`](wx.lib.agw.ultimatelistctrl.PyImageList.html#wx.lib.agw.ultimatelistctrl.PyImageList "wx.lib.agw.ultimatelistctrl.PyImageList") enables you to have images of different size inside the
image list. In your derived class, instead of doing this:



```
imageList = wx.ImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```


You should do this:



```
imageList = PyImageList(16, 16)
imageList.Add(someBitmap)
self.SetImageList(imageList, wx.IMAGE_LIST_SMALL)

```





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetImageListCheck(self, sizex, sizey, imglist=None) -> None:
        """ 

`SetImageListCheck`(*self*, *sizex*, *sizey*, *imglist=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetImageListCheck "Permalink to this definition")
Sets the checkbox/radiobutton image list.



Parameters
* **sizex** – the width of the bitmaps in the *imglist*;
* **sizey** – the height of the bitmaps in the *imglist*;
* **imglist** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItem(self, item: UltimateListItemData) -> None:
        """ 

`SetItem`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItem "Permalink to this definition")
Sets information about the item.



Parameters
**item** – an instance of [`UltimateListItemData`](wx.lib.agw.ultimatelistctrl.UltimateListItemData.html#wx.lib.agw.ultimatelistctrl.UltimateListItemData "wx.lib.agw.ultimatelistctrl.UltimateListItemData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemCount(self, count: UltimateListCtrl) -> None:
        """ 

`SetItemCount`(*self*, *count*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemCount "Permalink to this definition")
This method can only be used with virtual [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). It is used to
indicate to the control the number of items it contains. After calling it,
the main program should be ready to handle calls to various item callbacks
(such as [`UltimateListCtrl.OnGetItemText()`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemText "wx.lib.agw.ultimatelistctrl.UltimateListCtrl.OnGetItemText")) for all items in the range from 0 to *count*.



Parameters
**count** – the total number of items in [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemCustomRenderer(self, item, renderer=None) -> None:
        """ 

`SetItemCustomRenderer`(*self*, *item*, *renderer=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemCustomRenderer "Permalink to this definition")
Associate a custom renderer to this item.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **renderer** – a class able to correctly render the item.





Note


the renderer class **must** implement the methods *DrawSubItem*,
[`GetLineHeight`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineHeight "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.GetLineHeight") and *GetSubItemWidth*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemHyperText(self, item, hyper=True) -> None:
        """ 

`SetItemHyperText`(*self*, *item*, *hyper=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **hyper** – `True` to have an item with hypertext behaviour, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemKind(self, item, kind) -> None:
        """ 

`SetItemKind`(*self*, *item*, *kind*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemKind "Permalink to this definition")
Sets the item kind.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemOverFlow(self, item, over=True) -> None:
        """ 

`SetItemOverFlow`(*self*, *item*, *over=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemOverFlow "Permalink to this definition")
Sets the item in the overflow/non overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **over** – `True` to set the item in a overflow state, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemSpacing(self, spacing, isSmall=False) -> None:
        """ 

`SetItemSpacing`(*self*, *spacing*, *isSmall=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemSpacing "Permalink to this definition")
Sets the spacing between item texts and icons.



Parameters
* **spacing** – the spacing between item texts and icons, in pixels;
* **isSmall** – `True` if using a `wx.IMAGE_LIST_SMALL` image list,
`False` if using a `wx.IMAGE_LIST_NORMAL` image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemState(self, litem, state, stateMask) -> None:
        """ 

`SetItemState`(*self*, *litem*, *state*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemState "Permalink to this definition")
Sets the item state flags for the input item.



Parameters
* **litem** – the index of the item; if defaulted to -1, the state flag
will be set for all the items;
* **state** – the item state flag;
* **stateMask** – the bitmask for the state flag.





See also


[`SetItemStateAll`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemStateAll "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemStateAll") for a list of valid state flags.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemStateAll(self, state, stateMask) -> None:
        """ 

`SetItemStateAll`(*self*, *state*, *stateMask*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemStateAll "Permalink to this definition")
Sets the item state flags for all the items.



Parameters
* **state** – any combination of the following bits:






| State Bits | Hex Value | Description |
| --- | --- | --- |
| `ULC_STATE_DONTCARE` | 0x0 | Don’t care what the state is |
| `ULC_STATE_DROPHILITED` | 0x1 | The item is highlighted to receive a drop event |
| `ULC_STATE_FOCUSED` | 0x2 | The item has the focus |
| `ULC_STATE_SELECTED` | 0x4 | The item is selected |
| `ULC_STATE_CUT` | 0x8 | The item is in the cut state |
| `ULC_STATE_DISABLED` | 0x10 | The item is disabled |
| `ULC_STATE_FILTERED` | 0x20 | The item has been filtered |
| `ULC_STATE_INUSE` | 0x40 | The item is in use |
| `ULC_STATE_PICKED` | 0x80 | The item has been picked |
| `ULC_STATE_SOURCE` | 0x100 | The item is a drag and drop source |
* **stateMask** – the bitmask for the state flag.





Note


The valid state flags are influenced by the value of the state mask.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemText(self, item, value) -> None:
        """ 

`SetItemText`(*self*, *item*, *value*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemText "Permalink to this definition")
Sets the item text.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **value** – the new item text.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemVisited(self, item, visited=True) -> None:
        """ 

`SetItemVisited`(*self*, *item*, *visited=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemVisited "Permalink to this definition")
Sets whether an hypertext item was visited.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **visited** – `True` to mark an hypertext item as visited, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemWindow(self, item, wnd, expand=False) -> None:
        """ 

`SetItemWindow`(*self*, *item*, *wnd*, *expand=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemWindow "Permalink to this definition")
Sets the window for the given item.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **wnd** – if not `None`, a non-toplevel window to be displayed next to
the item;
* **expand** – `True` to expand the column where the item/subitem lives,
so that the window will be fully visible.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetItemWindowEnabled(self, item, enable=True) -> None:
        """ 

`SetItemWindowEnabled`(*self*, *item*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetItemWindowEnabled "Permalink to this definition")
Enables/disables the window associated to the item.



Parameters
* **item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem");
* **enable** – `True` to enable the associated window, `False` to
disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetReportView(self, inReportView: bool) -> None:
        """ 

`SetReportView`(*self*, *inReportView*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetReportView "Permalink to this definition")
Sets whether [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") is in report view or not.



Parameters
**inReportView** – `True` to set [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") in report view, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetSecondGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetSecondGradientColour "Permalink to this definition")
Sets the second gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour generated is a slightly darker version of the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
background colour.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetUserLineHeight(self, height: Any) -> None:
        """ 

`SetUserLineHeight`(*self*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetUserLineHeight "Permalink to this definition")
Sets a custom value for the [`UltimateListMainWindow`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow") item height.



Parameters
**height** – the custom height for all the items, in pixels.





Note


This method can be used only with `ULC_REPORT` and `ULC_USER_ROW_HEIGHT` styles set.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SetWaterMark(self, watermark: None) -> None:
        """ 

`SetWaterMark`(*self*, *watermark*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SetWaterMark "Permalink to this definition")
Sets the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") watermark image to be displayed in the bottom
right part of the window.



Parameters
**watermark** – if not `None`, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").





Todo


Better support for this is needed.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def SortItems(self, func: Any = None) -> None:
        """ 

`SortItems`(*self*, *func*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.SortItems "Permalink to this definition")
Call this function to sort the items in the [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl"). Sorting is done
using the specified function *func*. This function must have the
following prototype:



```
def OnCompareItems(self, line1, line2):

    DoSomething(line1, line2)
    # function code

```


It is called each time when the two items must be compared and should return 0
if the items are equal, negative value if the first item is less than the second
one and positive value if the first one is greater than the second one.



Parameters
**func** – the method to use to sort the items. The default is to use the
[`OnCompareItems`](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnCompareItems "wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.OnCompareItems") method.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def TileBackground(self, dc: 'DC') -> None:
        """ 

`TileBackground`(*self*, *dc*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.TileBackground "Permalink to this definition")
Tiles the background image to fill all the available area.



Parameters
**dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC").





Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """

    def UpdateCurrent(self) -> None:
        """ 

`UpdateCurrent`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.UpdateCurrent "Permalink to this definition")
Updates the current line selection.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListMainWindow.html
        """



EVT_CHILD_FOCUS: int

EVT_ERASE_BACKGROUND: int

EVT_TIMER: int

EVT_KEY_DOWN: int

EVT_SCROLLWIN: int

class UltimateListItemAttr:
    """ Represents the attributes (colour, font, …) of a [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
[`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
    """
    def __init__(self, colText=wx.NullColour, colBack=wx.NullColour, font=wx.NullFont, enabled=True, footerColText=wx.NullColour, footerColBack=wx.NullColour, footerFont=wx.NullFont) -> None:
        """ 

`__init__`(*self*, *colText=wx.NullColour*, *colBack=wx.NullColour*, *font=wx.NullFont*, *enabled=True*, *footerColText=wx.NullColour*, *footerColBack=wx.NullColour*, *footerFont=wx.NullFont*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **colText** – the item text colour;
* **colBack** – the item background colour;
* **font** – the item font;
* **enabled** – `True` if the item should be enabled, `False` if it is disabled;
* **footerColText** – for footer items, the item text colour;
* **footerColBack** – for footer items, the item background colour;
* **footerFont** – for footer items, the item font.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.Enable "Permalink to this definition")
Enables or disables the item.



Parameters
**enable** – `True` to enable the item, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetBackgroundColour(self) -> None:
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetBackgroundColour "Permalink to this definition")
Returns the currently set background colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFont(self) -> None:
        """ 

`GetFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetFont "Permalink to this definition")
Returns the currently set item font.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterBackgroundColour(self) -> None:
        """ 

`GetFooterBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetFooterBackgroundColour "Permalink to this definition")
Returns the currently set background colour for a footer item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterFont(self) -> None:
        """ 

`GetFooterFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetFooterFont "Permalink to this definition")
Returns the currently set font for a footer item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetFooterTextColour(self) -> None:
        """ 

`GetFooterTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetFooterTextColour "Permalink to this definition")
Returns the currently set text colour for a footer item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def GetTextColour(self) -> None:
        """ 

`GetTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.GetTextColour "Permalink to this definition")
Returns the currently set text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasBackgroundColour(self) -> None:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasBackgroundColour "Permalink to this definition")
Returns `True` if the currently set background colour is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFont(self) -> None:
        """ 

`HasFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasFont "Permalink to this definition")
Returns `True` if the currently set font is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterBackgroundColour(self) -> None:
        """ 

`HasFooterBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasFooterBackgroundColour "Permalink to this definition")
Returns `True` if the currently set background colour for the footer item
is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterFont(self) -> None:
        """ 

`HasFooterFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasFooterFont "Permalink to this definition")
Returns `True` if the currently set font for the footer item
is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasFooterTextColour(self) -> None:
        """ 

`HasFooterTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasFooterTextColour "Permalink to this definition")
Returns `True` if the currently set text colour for the footer item
is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def HasTextColour(self) -> None:
        """ 

`HasTextColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.HasTextColour "Permalink to this definition")
Returns `True` if the currently set text colour is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def IsEnabled(self) -> None:
        """ 

`IsEnabled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.IsEnabled "Permalink to this definition")
Returns `True` if the item is enabled.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colBack*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetBackgroundColour "Permalink to this definition")
Sets a new background colour.



Parameters
**colBack** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetFont "Permalink to this definition")
Sets a new font for the item.



Parameters
**font** – an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetFooterBackgroundColour`(*self*, *colBack*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetFooterBackgroundColour "Permalink to this definition")
Sets a new footer item background colour.



Parameters
**colBack** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterFont(self, font: 'Font') -> None:
        """ 

`SetFooterFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetFooterFont "Permalink to this definition")
Sets a new font for the footer item.



Parameters
**font** – an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetFooterTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetFooterTextColour`(*self*, *colText*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetFooterTextColour "Permalink to this definition")
Sets a new footer item text colour.



Parameters
**colText** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colText*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.SetTextColour "Permalink to this definition")
Sets a new text colour.



Parameters
**colText** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html
        """



class UltimateListEvent(CommandListEvent):
    """ A list event holds information about events associated with [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
objects.


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
    """
    def __init__(self, commandTypeOrEvent=None, winid=0) -> None:
        """ 

`__init__`(*self*, *commandTypeOrEvent=None*, *winid=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **commandTypeOrEvent** – the event type or another instance of
`PyCommandEvent`;
* **winid** – the event identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def Allow(self) -> None:
        """ 

`Allow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.Allow "Permalink to this definition")
This is the opposite of [`Veto`](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.Veto "wx.lib.agw.ultimatelistctrl.UltimateListEvent.Veto"): it explicitly allows the event to be processed.
For most events it is not necessary to call this method as the events are
allowed anyhow but some are forbidden by default (this will be mentioned
in the corresponding event description).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ 

`GetNotifyEvent`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.GetNotifyEvent "Permalink to this definition")
Returns the actual `NotifyEvent`.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def IsAllowed(self) -> None:
        """ 

`IsAllowed`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.IsAllowed "Permalink to this definition")
Returns `True` if the change is allowed ( [`Veto`](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.Veto "wx.lib.agw.ultimatelistctrl.UltimateListEvent.Veto") hasn’t been called) or
`False` otherwise (if it was).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """

    def Veto(self) -> None:
        """ 

`Veto`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListEvent.Veto "Permalink to this definition")
Prevents the change announced by this event from happening.



Note


It is in general a good idea to notify the user about the reasons
for vetoing the change because otherwise the applications behaviour (which
just refuses to do what the user wants) might be quite surprising.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListEvent.html
        """



class UltimateListLineData:
    """ A simple class which holds line geometries for [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
    """
    def __init__(self, owner: UltimateListCtrl) -> None:
        """ 

`__init__`(*self*, *owner*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.__init__ "Permalink to this definition")
Default class constructor.



Parameters
**owner** – an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def CalculateSize(self, dc, spacing) -> None:
        """ 

`CalculateSize`(*self*, *dc*, *spacing*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.CalculateSize "Permalink to this definition")
Calculates the line size and item positions.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **spacing** – the spacing between the items, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Check(self, index, checked=True) -> None:
        """ 

`Check`(*self*, *index*, *checked=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.Check "Permalink to this definition")
Checks/unchecks an item.



Parameters
* **index** – the index of the item;
* **checked** – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for check and radio items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Draw(self, line, dc) -> None:
        """ 

`Draw`(*self*, *line*, *dc*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.Draw "Permalink to this definition")
Draws the line on the specified device context.



Parameters
* **line** – an instance of [`UltimateListLineData`](#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawHorizontalGradient(self, dc, rect, hasfocus) -> None:
        """ 

`DrawHorizontalGradient`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.DrawHorizontalGradient "Permalink to this definition")
Gradient fill from colour 1 to colour 2 from left to right.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** – the rectangle to be filled with the gradient shading;
* **hasfocus** – `True` if the main [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawInReportMode(self, dc, line, rect, rectHL, highlighted, current, enabled, oldPN, oldBR) -> None:
        """ 

`DrawInReportMode`(*self*, *dc*, *line*, *rect*, *rectHL*, *highlighted*, *current*, *enabled*, *oldPN*, *oldBR*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.DrawInReportMode "Permalink to this definition")
Draws the line on the specified device context when the parent [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
is in report mode.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **line** – an instance of [`UltimateListLineData`](#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData");
* **rect** – the item client rectangle;
* **rectHL** – the item client rectangle when the item is highlighted;
* **highlighted** – `True` if the item is highlighted, `False` otherwise;
* **current** – `True` if the item is the current item;
* **enabled** – `True` if the item is enabled, `False` otherwise;
* **oldPN** – an instance of [`wx.Pen`](wx.Pen.html#wx.Pen "wx.Pen"), to save and restore at the end of
the drawing;
* **oldBR** – an instance of [`wx.Brush`](wx.Brush.html#wx.Brush "wx.Brush"), to save and restore at the end of
the drawing.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawTextFormatted(self, dc, text, row, col, itemRect, overflow) -> None:
        """ 

`DrawTextFormatted`(*self*, *dc*, *text*, *row*, *col*, *itemRect*, *overflow*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.DrawTextFormatted "Permalink to this definition")
Draws the item text, correctly formatted.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **text** – the item text;
* **row** – the line number to which this item belongs to;
* **col** – the column number to which this item belongs to;
* **itemRect** – the item client rectangle;
* **overflow** – `True` if the item should overflow into neighboring columns,
`False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawVerticalGradient(self, dc, rect, hasfocus) -> None:
        """ 

`DrawVerticalGradient`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.DrawVerticalGradient "Permalink to this definition")
Gradient fill from colour 1 to colour 2 from top to bottom.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** – the rectangle to be filled with the gradient shading;
* **hasfocus** – `True` if the main [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def DrawVistaRectangle(self, dc, rect, hasfocus) -> None:
        """ 

`DrawVistaRectangle`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.DrawVistaRectangle "Permalink to this definition")
Draws the selected item(s) with the Windows Vista style.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** – the rectangle to be filled with the gradient shading;
* **hasfocus** – `True` if the main [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetAttr(self) -> None:
        """ 

`GetAttr`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetAttr "Permalink to this definition")
Returns an instance of [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr") associated with the first item
in the line.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetHeight(self) -> None:
        """ 

`GetHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetHeight "Permalink to this definition")
Returns the line height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetImage(self, index: Any=0) -> None:
        """ 

`GetImage`(*self*, *index=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetImage "Permalink to this definition")
Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.



Parameters
**index** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetItem(self, index, info) -> None:
        """ 

`GetItem`(*self*, *index*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetItem "Permalink to this definition")
Returns information about the item.



Parameters
* **index** – the index of the item;
* **info** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetKind(self, index: Any=0) -> None:
        """ 

`GetKind`(*self*, *index=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetKind "Permalink to this definition")
Returns the item kind.



Parameters
**index** – the index of the item.





See also


[`SetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetKind "wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetMode(self) -> None:
        """ 

`GetMode`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetMode "Permalink to this definition")
Returns the current highlighting mode.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetText(self, index: Any) -> None:
        """ 

`GetText`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetText "Permalink to this definition")
Returns the item text at the position *index*.



Parameters
**index** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetToolTip(self, index: Any) -> None:
        """ 

`GetToolTip`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetToolTip "Permalink to this definition")
Returns the item tooltip at the position *index*.



Parameters
**index** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetWidth(self) -> None:
        """ 

`GetWidth`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetWidth "Permalink to this definition")
Returns the line width.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetX(self) -> None:
        """ 

`GetX`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetX "Permalink to this definition")
Returns the line *x* position.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def GetY(self) -> None:
        """ 

`GetY`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.GetY "Permalink to this definition")
Returns the line *y* position.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasImage(self, col=0) -> None:
        """ 

`HasImage`(*self*, *col=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.HasImage "Permalink to this definition")
Returns `True` if the first item in the line has at least one image
associated with it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasMode(self, mode: Any) -> None:
        """ 

`HasMode`(*self*, *mode*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.HasMode "Permalink to this definition")
Returns `True` if the parent [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the window
style specified by *mode*.



Parameters
**mode** – the window style to check.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HasText(self) -> None:
        """ 

`HasText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.HasText "Permalink to this definition")
Returns `True` if the text of first item in the line is not the empty
string.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def HideItemWindow(self, item: UltimateListItem) -> None:
        """ 

`HideItemWindow`(*self*, *item*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.HideItemWindow "Permalink to this definition")
If the input item has a window associated with it, hide it.



Parameters
**item** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def Highlight(self, on: bool) -> None:
        """ 

`Highlight`(*self*, *on*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.Highlight "Permalink to this definition")
Sets the current line as highlighted or not highlighted.



Parameters
**on** – `True` to set the current line as highlighted, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def InitItems(self, num: Any) -> None:
        """ 

`InitItems`(*self*, *num*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.InitItems "Permalink to this definition")
Initializes the list of items.



Parameters
**num** – the initial number of items to store.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def InReportView(self) -> None:
        """ 

`InReportView`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.InReportView "Permalink to this definition")
Returns `True` if the parent [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") is in report view.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsChecked(self, index: Any) -> None:
        """ 

`IsChecked`(*self*, *index*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.IsChecked "Permalink to this definition")
Returns whether the item is checked or not.



Parameters
**index** – the index of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsHighlighted(self) -> None:
        """ 

`IsHighlighted`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.IsHighlighted "Permalink to this definition")
Returns `True` if the line is highlighted.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def IsVirtual(self) -> None:
        """ 

`IsVirtual`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.IsVirtual "Permalink to this definition")
Returns `True` if the parent [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl") has the `ULC_VIRTUAL` style set.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def ResetDimensions(self) -> None:
        """ 

`ResetDimensions`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.ResetDimensions "Permalink to this definition")
Resets the line dimensions (client rectangle).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def ReverseHighlight(self) -> None:
        """ 

`ReverseHighlight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.ReverseHighlight "Permalink to this definition")
Reverses the line highlighting, switching it off if it was on and vice-versa.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetAttr(self, attr: UltimateListItemAttr) -> None:
        """ 

`SetAttr`(*self*, *attr*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetAttr "Permalink to this definition")
Sets an instance of [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr") to the first item in the line.



Parameters
**attr** – an instance of [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetAttributes(self, dc, attr, highlighted) -> None:
        """ 

`SetAttributes`(*self*, *dc*, *attr*, *highlighted*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetAttributes "Permalink to this definition")
Sets various attributes to the input device context.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **attr** – an instance of [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr");
* **highlighted** – `True` if the item is highlighted, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetColour(self, index, c) -> None:
        """ 

`SetColour`(*self*, *index*, *c*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetColour "Permalink to this definition")
Sets the text colour for the item.



Parameters
* **index** – the index of the item;
* **c** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetHeight(self, height: Any) -> None:
        """ 

`SetHeight`(*self*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetHeight "Permalink to this definition")
Sets the line height.



Parameters
**height** – the new line height.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetImage(self, index, image) -> None:
        """ 

`SetImage`(*self*, *index*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetImage "Permalink to this definition")
Sets the zero-based indexes of the images associated with the item into the
image list.



Parameters
* **index** – the index of the item;
* **image** – a Python list with the zero-based indexes of the images
associated with the item into the image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetItem(self, index, info) -> None:
        """ 

`SetItem`(*self*, *index*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetItem "Permalink to this definition")
Sets information about the item.



Parameters
* **index** – the index of the item;
* **info** – an instance of [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetKind(self, index, kind=0) -> None:
        """ 

`SetKind`(*self*, *index*, *kind=0*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetKind "Permalink to this definition")
Sets the item kind.



Parameters
* **index** – the index of the item;
* **kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetPosition(self, x, y, spacing) -> None:
        """ 

`SetPosition`(*self*, *x*, *y*, *spacing*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetPosition "Permalink to this definition")
Sets the line position.



Parameters
* **x** – the current *x* coordinate;
* **y** – the current *y* coordinate;
* **spacing** – the spacing between items, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetReportView(self, inReportView: bool) -> None:
        """ 

`SetReportView`(*self*, *inReportView*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetReportView "Permalink to this definition")
Sets whether [`UltimateListLineData`](#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData") is in report view or not.



Parameters
**inReportView** – `True` to set [`UltimateListLineData`](#wx.lib.agw.ultimatelistctrl.UltimateListLineData "wx.lib.agw.ultimatelistctrl.UltimateListLineData") in report view, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetText(self, index, s) -> None:
        """ 

`SetText`(*self*, *index*, *s*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetText "Permalink to this definition")
Sets the item text at the position *index*.



Parameters
* **index** – the index of the item;
* **s** – the new item text.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetToolTip(self, index, s) -> None:
        """ 

`SetToolTip`(*self*, *index*, *s*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetToolTip "Permalink to this definition")
Sets the item tooltip at the position *index*.



Parameters
* **index** – the index of the item;
* **s** – the new item tooltip.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetWidth(self, width: Any) -> None:
        """ 

`SetWidth`(*self*, *width*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetWidth "Permalink to this definition")
Sets the line width.



Parameters
**width** – the new line width.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetX(self, x: int) -> None:
        """ 

`SetX`(*self*, *x*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetX "Permalink to this definition")
Sets the line *x* position.



Parameters
**x** – the new line *x* position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """

    def SetY(self, y: int) -> None:
        """ 

`SetY`(*self*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListLineData.SetY "Permalink to this definition")
Sets the line *y* position.



Parameters
**y** – the new line *y* position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListLineData.html
        """



class UltimateListItemData:
    """ A simple class which holds information about [`UltimateListItem`](wx.lib.agw.ultimatelistctrl.UltimateListItem.html#wx.lib.agw.ultimatelistctrl.UltimateListItem "wx.lib.agw.ultimatelistctrl.UltimateListItem") visual
attributes (client rectangles, positions, etc…).


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
    """
    def __init__(self, owner: UltimateListCtrl) -> None:
        """ 

`__init__`(*self*, *owner*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.__init__ "Permalink to this definition")
Default class constructor



Parameters
**owner** – an instance of [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Check(self, checked: bool=True) -> None:
        """ 

`Check`(*self*, *checked=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.Check "Permalink to this definition")
Checks/unchecks an item.



Parameters
**checked** – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for check and radio items.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def DeleteWindow(self) -> None:
        """ 

`DeleteWindow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.DeleteWindow "Permalink to this definition")
Deletes the window associated to the item (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.Enable "Permalink to this definition")
Enables or disables the item.



Parameters
**enable** – `True` to enable the item, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetAttr(self) -> None:
        """ 

`GetAttr`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetAttr "Permalink to this definition")
Returns the item attributes.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetBackgroundColour(self) -> None:
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetBackgroundColour "Permalink to this definition")
Returns the currently set background colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetColour(self) -> None:
        """ 

`GetColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetColour "Permalink to this definition")
Returns the currently set text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetCustomRenderer(self) -> None:
        """ 

`GetCustomRenderer`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetCustomRenderer "Permalink to this definition")
Returns the custom renderer associated with this item (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetFont(self) -> None:
        """ 

`GetFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetFont "Permalink to this definition")
Returns the currently set font.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetHeight(self) -> None:
        """ 

`GetHeight`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetHeight "Permalink to this definition")
Returns the item height, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetImage(self) -> None:
        """ 

`GetImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetImage "Permalink to this definition")
Returns a Python list with the zero-based indexes of the images associated
with the item into the image list.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetItem(self, info: UltimateListItemData) -> None:
        """ 

`GetItem`(*self*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetItem "Permalink to this definition")
Returns information about the item.



Parameters
**info** – an instance of [`UltimateListItemData`](#wx.lib.agw.ultimatelistctrl.UltimateListItemData "wx.lib.agw.ultimatelistctrl.UltimateListItemData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetKind(self) -> None:
        """ 

`GetKind`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetKind "Permalink to this definition")
Returns the item kind.



See also


[`SetKind`](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetKind "wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetKind") for a list of valid item kinds.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetOverFlow(self) -> None:
        """ 

`GetOverFlow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetOverFlow "Permalink to this definition")
Returns if the item is in the overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetText(self) -> None:
        """ 

`GetText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetText "Permalink to this definition")
Returns the item text.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetTextForMeasuring(self) -> None:
        """ 

`GetTextForMeasuring`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetTextForMeasuring "Permalink to this definition")
Returns the item text or a simple string if the item text is the
empty string.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetToolTip(self) -> None:
        """ 

`GetToolTip`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetToolTip "Permalink to this definition")
Returns the item tooltip.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetVisited(self) -> None:
        """ 

`GetVisited`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetVisited "Permalink to this definition")
Returns whether an hypertext item was visited or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWidth(self) -> None:
        """ 

`GetWidth`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetWidth "Permalink to this definition")
Returns the item width, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindow(self) -> None:
        """ 

`GetWindow`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetWindow "Permalink to this definition")
Returns the window associated to the item.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindowEnabled(self) -> None:
        """ 

`GetWindowEnabled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetWindowEnabled "Permalink to this definition")
Returns whether the associated window is enabled or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetWindowSize(self) -> None:
        """ 

`GetWindowSize`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetWindowSize "Permalink to this definition")
Returns the associated window size.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetX(self) -> None:
        """ 

`GetX`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetX "Permalink to this definition")
Returns the item *x* position.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def GetY(self) -> None:
        """ 

`GetY`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.GetY "Permalink to this definition")
Returns the item *y* position.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasBackgroundColour(self) -> None:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.HasBackgroundColour "Permalink to this definition")
Returns `True` if the currently set background colour is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasColour(self) -> None:
        """ 

`HasColour`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.HasColour "Permalink to this definition")
Returns `True` if the currently set text colour is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasFont(self) -> None:
        """ 

`HasFont`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.HasFont "Permalink to this definition")
Returns `True` if the currently set font is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasImage(self) -> None:
        """ 

`HasImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.HasImage "Permalink to this definition")
Returns `True` if the item has at least one image associated with it.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def HasText(self) -> None:
        """ 

`HasText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.HasText "Permalink to this definition")
Returns `True` if the item text is not the empty string.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.Init "Permalink to this definition")
Initializes the item data structure.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsChecked(self) -> None:
        """ 

`IsChecked`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.IsChecked "Permalink to this definition")
Returns whether the item is checked or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsEnabled(self) -> None:
        """ 

`IsEnabled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.IsEnabled "Permalink to this definition")
Returns `True` if the item is enabled, `False` if it is disabled.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsHit(self, x, y) -> None:
        """ 

`IsHit`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.IsHit "Permalink to this definition")
Returns `True` if the input position is inside the item client rectangle.



Parameters
* **x** – the *x* mouse position;
* **y** – the *y* mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def IsHyperText(self) -> None:
        """ 

`IsHyperText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.IsHyperText "Permalink to this definition")
Returns whether the item is hypetext or not.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetAttr(self, attr: UltimateListItemAttr) -> None:
        """ 

`SetAttr`(*self*, *attr*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetAttr "Permalink to this definition")
Sets the item attributes.



Parameters
**attr** – an instance of [`UltimateListItemAttr`](wx.lib.agw.ultimatelistctrl.UltimateListItemAttr.html#wx.lib.agw.ultimatelistctrl.UltimateListItemAttr "wx.lib.agw.ultimatelistctrl.UltimateListItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetBackgroundColour "Permalink to this definition")
Sets the background colour for the item.



Parameters
**colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetColour "Permalink to this definition")
Sets the text colour for the item.



Parameters
**colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetCustomRenderer(self, renderer: Any) -> None:
        """ 

`SetCustomRenderer`(*self*, *renderer*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetCustomRenderer "Permalink to this definition")
Associate a custom renderer to this item.



Parameters
**renderer** – a class able to correctly render the item.





Note


the renderer class **must** implement the methods *DrawSubItem*,
*GetLineHeight* and *GetSubItemWidth*.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetData(self, data: Any) -> None:
        """ 

`SetData`(*self*, *data*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetData "Permalink to this definition")
Sets client data for the item.



Parameters
**data** – the client data associated to the item.





Note


Please note that client data is associated with the item and not
with subitems.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetFont "Permalink to this definition")
Sets the text font for the item.



Parameters
**font** – an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ 

`SetHyperText`(*self*, *hyper=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
**hyper** – `True` to set hypertext behaviour, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetImage(self, image: Any) -> None:
        """ 

`SetImage`(*self*, *image*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetImage "Permalink to this definition")
Sets the zero-based indexes of the images associated with the item into the
image list.



Parameters
**image** – a Python list with the zero-based indexes of the images
associated with the item into the image list.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetItem(self, info: UltimateListItemData) -> None:
        """ 

`SetItem`(*self*, *info*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetItem "Permalink to this definition")
Sets information about the item.



Parameters
**info** – an instance of [`UltimateListItemData`](#wx.lib.agw.ultimatelistctrl.UltimateListItemData "wx.lib.agw.ultimatelistctrl.UltimateListItemData").






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetKind(self, kind: Any) -> None:
        """ 

`SetKind`(*self*, *kind*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetKind "Permalink to this definition")
Sets the item kind.



Parameters
**kind** – may be one of the following integers:





| Item Kind | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |









            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetOverFlow(self, over: bool=True) -> None:
        """ 

`SetOverFlow`(*self*, *over=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetOverFlow "Permalink to this definition")
Sets the item in the overflow/non overflow state.


An item/subitem may overwrite neighboring items/subitems if its text would
not normally fit in the space allotted to it.



Parameters
**over** – `True` to set the item in a overflow state, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetPosition(self, x, y) -> None:
        """ 

`SetPosition`(*self*, *x*, *y*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetPosition "Permalink to this definition")
Sets the item position.



Parameters
* **x** – the item *x* position;
* **y** – the item *y* position.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetSize(self, width, height) -> None:
        """ 

`SetSize`(*self*, *width*, *height*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetSize "Permalink to this definition")
Sets the item size.



Parameters
* **width** – the item width, in pixels;
* **height** – the item height, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetText(self, text: Any) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetText "Permalink to this definition")
Sets the text label for the item.



Parameters
**text** – the text label for the item.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetToolTip(self, tooltip: Any) -> None:
        """ 

`SetToolTip`(*self*, *tooltip*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetToolTip "Permalink to this definition")
Sets the tooltip for the item



Parameters
**tooltip** – the tooltip text






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ 

`SetVisited`(*self*, *visited=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetVisited "Permalink to this definition")
Sets whether an hypertext item was visited or not.



Parameters
**visited** – `True` to set a hypertext item as visited, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetWindow(self, wnd, expand=False) -> None:
        """ 

`SetWindow`(*self*, *wnd*, *expand=False*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetWindow "Permalink to this definition")
Sets the window associated to the item.



Parameters
* **wnd** – a non-toplevel window to be displayed next to the item;
* **expand** – `True` to expand the column where the item/subitem lives,
so that the window will be fully visible.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ 

`SetWindowEnabled`(*self*, *enable=True*)[¶](#wx.lib.agw.ultimatelistctrl.UltimateListItemData.SetWindowEnabled "Permalink to this definition")
Sets whether the associated window is enabled or not.



Parameters
**enable** – `True` to enable the associated window, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.UltimateListItemData.html
        """



class CommandListEvent(PyCommandEvent):
    """ A list event holds information about events associated with [`UltimateListCtrl`](wx.lib.agw.ultimatelistctrl.UltimateListCtrl.html#wx.lib.agw.ultimatelistctrl.UltimateListCtrl "wx.lib.agw.ultimatelistctrl.UltimateListCtrl")
objects.


  


        Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
    """
    def __init__(self, commandTypeOrEvent=None, winid=0) -> None:
        """ 

`__init__`(*self*, *commandTypeOrEvent=None*, *winid=0*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **commandTypeOrEvent** – the event type or another instance of
`PyCommandEvent`;
* **winid** – the event identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetCacheFrom(self) -> None:
        """ 

`GetCacheFrom`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetCacheFrom "Permalink to this definition")
Returns the first item which the list control advises us to cache.



Note


This method is meaningful for `EVT_LIST_CACHE_HINT` event only.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetCacheTo(self) -> None:
        """ 

`GetCacheTo`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetCacheTo "Permalink to this definition")
Returns the last item (inclusive) which the list control advises us to cache.



Note


This method is meaningful for `EVT_LIST_CACHE_HINT` event only.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetColumn(self) -> None:
        """ 

`GetColumn`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetColumn "Permalink to this definition")
Returns the column position: it is only used with `COL` events.


For the column dragging events, it is the column to the left of the divider
being dragged, for the column click events it may be -1 if the user clicked
in the list control header outside any column.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetData(self) -> None:
        """ 

`GetData`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetData "Permalink to this definition")
Returns the item data.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetImage(self) -> None:
        """ 

`GetImage`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetImage "Permalink to this definition")
Returns the item image.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetIndex(self) -> None:
        """ 

`GetIndex`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetIndex "Permalink to this definition")
Returns the item index.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetItem(self) -> None:
        """ 

`GetItem`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetItem "Permalink to this definition")
Returns the item itself.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetKeyCode(self) -> None:
        """ 

`GetKeyCode`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetKeyCode "Permalink to this definition")
Returns the key code if the event is a keypress event.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetLabel(self) -> None:
        """ 

`GetLabel`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetLabel "Permalink to this definition")
Returns the (new) item label for `EVT_LIST_END_LABEL_EDIT` event.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetMask(self) -> None:
        """ 

`GetMask`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetMask "Permalink to this definition")
Returns the item mask.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetPoint(self) -> None:
        """ 

`GetPoint`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetPoint "Permalink to this definition")
Returns the position of the mouse pointer if the event is a drag event.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def GetText(self) -> None:
        """ 

`GetText`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetText "Permalink to this definition")
Returns the item text.




            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ 

`IsEditCancelled`(*self*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.IsEditCancelled "Permalink to this definition")
Returns `True` if it the label editing has been cancelled by the user
( [`GetLabel`](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetLabel "wx.lib.agw.ultimatelistctrl.CommandListEvent.GetLabel") returns an empty string in this case but it doesn’t allow
the application to distinguish between really cancelling the edit and
the admittedly rare case when the user wants to rename it to an empty
string).



Note


This method only makes sense for `EVT_LIST_END_LABEL_EDIT` messages.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ 

`SetEditCanceled`(*self*, *editCancelled*)[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.SetEditCanceled "Permalink to this definition")
Sets the item editing as cancelled/not cancelled.



Parameters
**editCancelled** – `True` to set the item editing as cancelled, `False`
otherwise.





Note


This method only makes sense for `EVT_LIST_END_LABEL_EDIT` messages.





            Source: https://docs.wxpython.org/wx.lib.agw.ultimatelistctrl.CommandListEvent.html
        """

    Index: None  # `Index`[¶](#wx.lib.agw.ultimatelistctrl.CommandListEvent.Index "Permalink to this definition")See [`GetIndex`](#wx.lib.agw.ultimatelistctrl.CommandListEvent.GetIndex "wx.lib.agw.ultimatelistctrl.CommandListEvent.GetIndex")



ULC_ALIGN_DEFAULT: int

ULC_ALIGN_SNAP_TO_GRID: int

ULC_VRULES: int

ULC_HRULES: int

ULC_ICON: int

ULC_SMALL_ICON: int

ULC_LIST: int

ULC_REPORT: int

ULC_ALIGN_TOP: int

ULC_ALIGN_LEFT: int

ULC_AUTOARRANGE: int

ULC_VIRTUAL: int

ULC_EDIT_LABELS: int

ULC_NO_HEADER: int

ULC_NO_SORT_HEADER: int

ULC_SINGLE_SEL: int

ULC_SORT_ASCENDING: int

ULC_SORT_DESCENDING: int

ULC_TILE: int

ULC_NO_HIGHLIGHT: int

ULC_STICKY_HIGHLIGHT: int

ULC_STICKY_NOSELEVENT: int

ULC_SEND_LEFTCLICK: int

ULC_HAS_VARIABLE_ROW_HEIGHT: int

ULC_AUTO_CHECK_CHILD: int

ULC_AUTO_TOGGLE_CHILD: int

ULC_AUTO_CHECK_PARENT: int

ULC_SHOW_TOOLTIPS: int

ULC_HOT_TRACKING: int

ULC_BORDER_SELECT: int

ULC_TRACK_SELECT: int

ULC_HEADER_IN_ALL_VIEWS: int

ULC_NO_FULL_ROW_SELECT: int

ULC_FOOTER: int

ULC_USER_ROW_HEIGHT: int

ULC_FORMAT_LEFT: int

ULC_FORMAT_RIGHT: int

ULC_FORMAT_CENTRE: int

ULC_FORMAT_CENTER: int

ULC_MASK_STATE: int

ULC_MASK_TEXT: int

ULC_MASK_IMAGE: int

ULC_MASK_DATA: int

ULC_MASK_WIDTH: int

ULC_MASK_FORMAT: int

ULC_MASK_FONTCOLOUR: int

ULC_MASK_FONT: int

ULC_MASK_BACKCOLOUR: int

ULC_MASK_KIND: int

ULC_MASK_ENABLE: int

ULC_MASK_CHECK: int

ULC_MASK_HYPERTEXT: int

ULC_MASK_WINDOW: int

ULC_MASK_PYDATA: int

ULC_MASK_SHOWN: int

ULC_MASK_RENDERER: int

ULC_MASK_OVERFLOW: int

ULC_MASK_FOOTER_TEXT: int

ULC_MASK_FOOTER_IMAGE: int

ULC_MASK_FOOTER_FORMAT: int

ULC_MASK_FOOTER_FONT: int

ULC_MASK_FOOTER_CHECK: int

ULC_MASK_FOOTER_KIND: int

ULC_STATE_DONTCARE: int

ULC_STATE_DROPHILITED: int

ULC_STATE_FOCUSED: int

ULC_STATE_SELECTED: int

ULC_STATE_CUT: int

ULC_STATE_DISABLED: int

ULC_STATE_FILTERED: int

ULC_STATE_INUSE: int

ULC_STATE_PICKED: int

ULC_STATE_SOURCE: int

