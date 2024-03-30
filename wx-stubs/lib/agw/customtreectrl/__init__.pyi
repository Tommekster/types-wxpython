# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class CommandTreeEvent(CommandEvent):
    """ [`CommandTreeEvent`](#wx.lib.agw.customtreectrl.CommandTreeEvent "wx.lib.agw.customtreectrl.CommandTreeEvent") is a special subclassing of `CommandEvent`.



Note


Not all the accessors make sense for all the events, see the event description for every method in this class.



  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
    """
    def __init__(self, evtType, evtId, item=None, evtKey=None, point=None, label=None, **kwargs) -> None:
        """ 

`__init__`(*self*, *evtType*, *evtId*, *item=None*, *evtKey=None*, *point=None*, *label=None*, *\*\*kwargs*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **evtType** (*integer*) – the event type;
* **evtId** (*integer*) – the event identifier;
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **evtKey** (*integer*) – a character ordinal;
* **point** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point");
* **label** (*string*) – a [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") text label.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetItem(self) -> None:
        """ 

`GetItem`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetItem "Permalink to this definition")
Gets the item on which the operation was performed or the newly selected
item for `EVT_TREE_SEL_CHANGED` and `EVT_TREE_SEL_CHANGING` events.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetKeyCode(self) -> None:
        """ 

`GetKeyCode`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetKeyCode "Permalink to this definition")
Returns the virtual key code. ASCII events return normal ASCII values, while
non-ASCII events return values such as `wx.WXK_LEFT` for the left cursor key.


This method is for `EVT_TREE_KEY_DOWN` events only.



Returns
An integer representing the virtual key code.





Note


In Unicode build, the returned value is meaningful only if the user entered
a character that can be represented in current locale’s default charset. You can
obtain the corresponding Unicode character using *GetUnicodeKey*.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetKeyEvent(self) -> None:
        """ 

`GetKeyEvent`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetKeyEvent "Permalink to this definition")
Returns the keyboard data (for `EVT_TREE_KEY_DOWN` event only).



Returns
An instance of `KeyEvent`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetLabel(self) -> None:
        """ 

`GetLabel`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetLabel "Permalink to this definition")
Returns the item text (for `EVT_TREE_BEGIN_LABEL_EDIT` and
`EVT_TREE_END_LABEL_EDIT` events only).



Returns
A string containing the item text.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetOldItem(self) -> None:
        """ 

`GetOldItem`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetOldItem "Permalink to this definition")
Returns the previously selected item for `EVT_TREE_SEL_CHANGED` and
`EVT_TREE_SEL_CHANGING` events.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetPoint(self) -> None:
        """ 

`GetPoint`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetPoint "Permalink to this definition")
Returns the point where the mouse was when the drag operation started
(for `EVT_TREE_BEGIN_DRAG` and `EVT_TREE_BEGIN_RDRAG` events only)
or the click position.



Returns
An instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def GetToolTip(self) -> None:
        """ 

`GetToolTip`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.GetToolTip "Permalink to this definition")
Returns the tooltip for the item (for `EVT_TREE_ITEM_GETTOOLTIP` events).



Returns
A string containing the item tooltip.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ 

`IsEditCancelled`(*self*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.IsEditCancelled "Permalink to this definition")
Returns the edit cancel flag (for `EVT_TREE_BEGIN_LABEL_EDIT` and
`EVT_TREE_END_LABEL_EDIT` events only).



Returns
`True` is the item editing has been cancelled, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ 

`SetEditCanceled`(*self*, *editCancelled*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetEditCanceled "Permalink to this definition")
Sets the edit cancel flag (for `EVT_TREE_BEGIN_LABEL_EDIT` and
`EVT_TREE_END_LABEL_EDIT` events only).



Parameters
**editCancelled** (*bool*) – `True` to cancel the editing, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetItem(self, item: GenericTreeItem) -> None:
        """ 

`SetItem`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetItem "Permalink to this definition")
Sets the item on which the operation was performed or the newly selected
item for `EVT_TREE_SEL_CHANGED` and `EVT_TREE_SEL_CHANGING` events.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetKeyEvent(self, event: CommandTreeEvent) -> None:
        """ 

`SetKeyEvent`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetKeyEvent "Permalink to this definition")
Sets the keyboard data (for `EVT_TREE_KEY_DOWN` event only).



Parameters
**event** – a [`CommandTreeEvent`](#wx.lib.agw.customtreectrl.CommandTreeEvent "wx.lib.agw.customtreectrl.CommandTreeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetLabel "Permalink to this definition")
Sets the item text (for `EVT_TREE_BEGIN_LABEL_EDIT` and
`EVT_TREE_END_LABEL_EDIT` events only).



Parameters
**label** (*string*) – a string containing the new item text.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetOldItem(self, item: GenericTreeItem) -> None:
        """ 

`SetOldItem`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetOldItem "Permalink to this definition")
Returns the previously selected item for `EVT_TREE_SEL_CHANGED` and
`EVT_TREE_SEL_CHANGING` events.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetPoint(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`SetPoint`(*self*, *pt*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetPoint "Permalink to this definition")
Sets the point where the mouse was when the drag operation started
(for `EVT_TREE_BEGIN_DRAG` and `EVT_TREE_BEGIN_RDRAG` events only)
or the click position.



Parameters
**pt** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """

    def SetToolTip(self, toolTip) -> None:
        """ 

`SetToolTip`(*self*, *toolTip*)[¶](#wx.lib.agw.customtreectrl.CommandTreeEvent.SetToolTip "Permalink to this definition")
Sets the tooltip for the item (for `EVT_TREE_ITEM_GETTOOLTIP` events).



Parameters
**tooltip** (*string*) – a string representing the item tooltip.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CommandTreeEvent.html
        """



WXK_LEFT: int

class CustomTreeCtrl(ScrolledWindow):
    """ [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") is a class that mimics the behaviour of `TreeCtrl`, with almost the
same base functionalities plus some more enhancements. This class does not rely on
the native control, as it is a full owner-drawn tree control.


  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=TR_DEFAULT_STYLE, validator=wx.DefaultValidator, name="CustomTreeCtrl") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=TR\_DEFAULT\_STYLE*, *validator=wx.DefaultValidator*, *name="CustomTreeCtrl"*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying `ScrolledWindow` style;
* **agwStyle** (*integer*) – can be a combination of various bits. See
[`customtreectrl`](wx.lib.agw.customtreectrl.html#module-wx.lib.agw.customtreectrl "wx.lib.agw.customtreectrl") for a full list of flags.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – window validator;
* **name** (*string*) – window name.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AcceptsFocus(self) -> None:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AcceptsFocus "Permalink to this definition")
Can this window be given focus by mouse click?



Note


This method always returns `True` as we always accept focus from
mouse click.




Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AddRoot(self, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, on_the_right=True) -> 'GenericTreeItem':
        """ 

`AddRoot`(*self*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AddRoot "Permalink to this definition")
Adds a root item to the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item,
any subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") except top-level windows;
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.



Raise
*Exception* in the following cases:


* There already is a root item in the tree;
* The item window is not `None` but the `TR_HAS_VARIABLE_ROW_HEIGHT` flag has not been
set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl");
* The item has multiline text (with line-breaks in it) but the `TR_HAS_VARIABLE_ROW_HEIGHT`
flag has not been set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl");
* The *ct\_type* attribute is less than `0` or greater than `2`.





Warning


Only one root is allowed to exist in any given instance of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AdjustMyScrollbars(self) -> None:
        """ 

`AdjustMyScrollbars`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AdjustMyScrollbars "Permalink to this definition")
Internal method used to adjust the `ScrolledWindow` scrollbars.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AppendItem(self, parentId, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, on_the_right=True) -> 'GenericTreeItem':
        """ 

`AppendItem`(*self*, *parentId*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AppendItem "Permalink to this definition")
Appends an item as a last child of its parent.



Parameters
* **parentId** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent;
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item,
any subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AppendSeparator(self, parentId: GenericTreeItem) -> None:
        """ 

`AppendSeparator`(*self*, *parentId*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AppendSeparator "Permalink to this definition")
Appends an horizontal line separator as a last child of its parent.



Parameters
**parentId** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
separator’s parent.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignButtonsImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignButtonsImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AssignButtonsImageList "Permalink to this definition")
Assigns the button image list.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AssignImageList "Permalink to this definition")
Assigns the normal image list.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignLeftImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignLeftImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AssignLeftImageList "Permalink to this definition")
Assigns the image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AssignStateImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignStateImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AssignStateImageList "Permalink to this definition")
Assigns the state image list.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoCheckChild(self, item, checked) -> None:
        """ 

`AutoCheckChild`(*self*, *item*, *checked*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AutoCheckChild "Permalink to this definition")
Transverses the tree and checks/unchecks the items.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoCheckParent(self, item, checked) -> None:
        """ 

`AutoCheckParent`(*self*, *item*, *checked*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AutoCheckParent "Permalink to this definition")
Traverses up the tree and checks/unchecks parent items.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def AutoToggleChild(self, item: GenericTreeItem) -> None:
        """ 

`AutoToggleChild`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.AutoToggleChild "Permalink to this definition")
Transverses the tree and toggles the items.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateLevel(self, item, dc, level, y, align=0) -> None:
        """ 

`CalculateLevel`(*self*, *item*, *dc*, *level*, *y*, *align=0*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculateLevel "Permalink to this definition")
Calculates the level of an item inside the tree hierarchy.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **level** (*integer*) – the item level in the tree hierarchy;
* **y** (*integer*) – the current vertical position inside the `ScrolledWindow`;
* **align** (*integer*) – an integer specifying the alignment type:





| *align* Value | Description |
| --- | --- |
| 0 | No horizontal alignment of windows (in items with windows). |
| 1 | Windows (in items with windows) are aligned at the same horizontal position. |
| 2 | Windows (in items with windows) are aligned at the rightmost edge of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). |



Returns
The new *y* vertical position inside the `ScrolledWindow`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateLineHeight(self) -> None:
        """ 

`CalculateLineHeight`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculateLineHeight "Permalink to this definition")
Calculates the base height for all lines in the tree.


Only used if the TR\_HAS\_VARIABLE\_ROW\_HEIGHT style is not used.
This base line height gets adjusted to the max line height
of all items as they are displayed. All rows use this largest
height until this method is called to reset it.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculatePositions(self) -> None:
        """ 

`CalculatePositions`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculatePositions "Permalink to this definition")
Calculates all the positions of the visible items.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CalculateSize(self, item, dc, level=-1, align=0) -> None:
        """ 

`CalculateSize`(*self*, *item*, *dc*, *level=-1*, *align=0*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculateSize "Permalink to this definition")
Calculates overall position and size of an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **level** (*integer*) – the item level in the tree hierarchy;
* **align** (*integer*) – an integer specifying the alignment type:





| *align* Value | Description |
| --- | --- |
| 0 | No horizontal alignment of windows (in items with windows). |
| 1 | Windows (in items with windows) are aligned at the same horizontal position. |
| 2 | Windows (in items with windows) are aligned at the rightmost edge of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). |






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckChilds(self, item, checked=True) -> None:
        """ 

`CheckChilds`(*self*, *item*, *checked=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckChilds "Permalink to this definition")
Programmatically check/uncheck item children.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.




Note


This method does not generate `EVT_TREE_ITEM_CHECKING` and
`EVT_TREE_ITEM_CHECKED` events.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckItem(self, item, checked=True) -> None:
        """ 

`CheckItem`(*self*, *item*, *checked=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckItem "Permalink to this definition")
Actually checks/uncheks an item, sending (eventually) the two
events `EVT_TREE_ITEM_CHECKING` and `EVT_TREE_ITEM_CHECKED`.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – for a radiobutton-type item, `True` to check it, `False`
to uncheck it. For a checkbox-type item, it can be one of `wx.CHK_UNCHECKED`
when the checkbox is unchecked, `wx.CHK_CHECKED` when it is checked and
`wx.CHK_UNDETERMINED` when it’s in the undetermined state.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckItem2(self, item, checked=True, torefresh=False) -> None:
        """ 

`CheckItem2`(*self*, *item*, *checked=True*, *torefresh=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckItem2 "Permalink to this definition")
Used internally to avoid `EVT_TREE_ITEM_CHECKED` events.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it;
* **torefresh** (*bool*) – whether to redraw the item or not.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CheckSameLevel(self, item, checked=False) -> None:
        """ 

`CheckSameLevel`(*self*, *item*, *checked=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckSameLevel "Permalink to this definition")
Uncheck radio items which are on the same level of the checked one.
Used internally.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it.





Note


This method is meaningful only for radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ChildrenClosing(self, item: GenericTreeItem) -> None:
        """ 

`ChildrenClosing`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ChildrenClosing "Permalink to this definition")
We are about to destroy the item children.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Collapse(self, item: GenericTreeItem) -> None:
        """ 

`Collapse`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Collapse "Permalink to this definition")
Collapse an item, sending a `EVT_TREE_ITEM_COLLAPSING` and
`EVT_TREE_ITEM_COLLAPSED` events.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Raise
*Exception* if you try to collapse a hidden root (i.e., when the `TR_HIDE_ROOT`
style is set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl")).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def CollapseAndReset(self, item: GenericTreeItem) -> None:
        """ 

`CollapseAndReset`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CollapseAndReset "Permalink to this definition")
Collapse the given item and deletes its children.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Delete(self, item: GenericTreeItem) -> None:
        """ 

`Delete`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Delete "Permalink to this definition")
Deletes an item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Note


This method sends the `EVT_TREE_DELETE_ITEM` event.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteAllItems "Permalink to this definition")
Deletes all items in the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteChildren(self, item: GenericTreeItem) -> None:
        """ 

`DeleteChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteChildren "Permalink to this definition")
Delete all the item’s children.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DeleteItemWindow(self, item: GenericTreeItem) -> None:
        """ 

`DeleteItemWindow`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteItemWindow "Permalink to this definition")
Deletes the window associated to an item (if any).



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same size
as it would have after a call to *Fit()*.



Returns
An instance of [`wx.Size`](wx.Size.html#wx.Size "wx.Size").





Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoInsertItem(self, parentId, previous, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`DoInsertItem`(*self*, *parentId*, *previous*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "Permalink to this definition")
Actually inserts an item in the tree.



Parameters
* **parentId** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent;
* **previous** (*integer*) – the index at which we should insert the item;
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item, any
subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") except top-level windows;
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item;
* **separator** (*bool*) – `True` if the item is a separator, `False` otherwise.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.



Raise
*Exception* in the following cases:


* The item window is not `None` but the `TR_HAS_VARIABLE_ROW_HEIGHT` flag has not been
set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl");
* The item has multiline text (with line-breaks in it) but the `TR_HAS_VARIABLE_ROW_HEIGHT`
flag has not been set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl");
* The *ct\_type* attribute is less than `0` or greater than `2`;
* The parent item is a separator;
* The item is a separator but it has text or an associated window.





Note


Separator items should not have children, text labels or an associated window.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DoSelectItem(self, item, unselect_others=True, extended_select=False, from_key=False) -> None:
        """ 

`DoSelectItem`(*self*, *item*, *unselect\_others=True*, *extended\_select=False*, *from\_key=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoSelectItem "Permalink to this definition")
Actually selects/unselects an item, sending `EVT_TREE_SEL_CHANGING` and
`EVT_TREE_SEL_CHANGED` events.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **unselect\_others** (*bool*) – if `True`, all the other selected items are
unselected.
* **extended\_select** (*bool*) – `True` if the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") is using the
`TR_EXTENDED` style;
* **from\_key** (*bool*) – `True` to indicate that the selection was made via a keyboard
key, `False` if it was a mouse selection.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawHorizontalGradient(self, dc, rect, hasfocus) -> None:
        """ 

`DrawHorizontalGradient`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DrawHorizontalGradient "Permalink to this definition")
Gradient fill from colour 1 to colour 2 from left to right.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the rectangle to be filled with the gradient shading;
* **hasfocus** (*bool*) – `True` if the main [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawVerticalGradient(self, dc, rect, hasfocus) -> None:
        """ 

`DrawVerticalGradient`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DrawVerticalGradient "Permalink to this definition")
Gradient fill from colour 1 to colour 2 from top to bottom.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the rectangle to be filled with the gradient shading;
* **hasfocus** (*bool*) – `True` if the main [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def DrawVistaRectangle(self, dc, rect, hasfocus) -> None:
        """ 

`DrawVistaRectangle`(*self*, *dc*, *rect*, *hasfocus*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DrawVistaRectangle "Permalink to this definition")
Draws the selected item(s) with the Windows Vista style.



Parameters
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the rectangle to be filled with the gradient shading;
* **hasfocus** (*bool*) – `True` if the main [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has focus, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Edit(self, item: GenericTreeItem) -> None:
        """ 

`Edit`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Edit "Permalink to this definition")
Internal function. Starts the editing of an item label, sending a
`EVT_TREE_BEGIN_LABEL_EDIT` event.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Warning


Separator-type items can not be edited.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EditLabel(self, item: GenericTreeItem) -> None:
        """ 

`EditLabel`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EditLabel "Permalink to this definition")
Starts editing an item label.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableChildren(self, item, enable=True) -> None:
        """ 

`EnableChildren`(*self*, *item*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableChildren "Permalink to this definition")
Enables/disables the item children.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **enable** (*bool*) – `True` to enable the children, `False` to disable them.





Note


This method is used internally.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableItem(self, item, enable=True, torefresh=True) -> None:
        """ 

`EnableItem`(*self*, *item*, *enable=True*, *torefresh=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableItem "Permalink to this definition")
Enables/disables an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **enable** (*bool*) – `True` to enable the item, `False` to disable it;
* **torefresh** (*bool*) – whether to redraw the item or not.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableSelectionGradient(self, enable: bool=True) -> None:
        """ 

`EnableSelectionGradient`(*self*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableSelectionGradient "Permalink to this definition")
Globally enables/disables drawing of gradient selections.



Parameters
**enable** (*bool*) – `True` to enable gradient-style selections, `False`
to disable it.





Note


Calling this method disables any Vista-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnableSelectionVista(self, enable: bool=True) -> None:
        """ 

`EnableSelectionVista`(*self*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableSelectionVista "Permalink to this definition")
Globally enables/disables drawing of Windows Vista selections.



Parameters
**enable** (*bool*) – `True` to enable Vista-style selections, `False` to
disable it.





Note


Calling this method disables any gradient-style selection previously
enabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def EnsureVisible(self, item: GenericTreeItem) -> None:
        """ 

`EnsureVisible`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnsureVisible "Permalink to this definition")
Scrolls and/or expands items to ensure that the given item is visible.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Expand(self, item: GenericTreeItem) -> None:
        """ 

`Expand`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Expand "Permalink to this definition")
Expands an item, sending a `EVT_TREE_ITEM_EXPANDING` and
`EVT_TREE_ITEM_EXPANDED` events.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Raise
*Exception* if you try to expand a hidden root (i.e., when the `TR_HIDE_ROOT`
style is set for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl")).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ExpandAll(self) -> None:
        """ 

`ExpandAll`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ExpandAll "Permalink to this definition")
Expands all [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") items.



Note


This method suppresses the `EVT_TREE_ITEM_EXPANDING` and
`EVT_TREE_ITEM_EXPANDED` events because expanding many items int the
control would be too slow then.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ExpandAllChildren(self, item: GenericTreeItem) -> None:
        """ 

`ExpandAllChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ExpandAllChildren "Permalink to this definition")
Expands all the items children of the input item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Note


This method suppresses the `EVT_TREE_ITEM_EXPANDING` and
`EVT_TREE_ITEM_EXPANDED` events because expanding many items int the
control would be too slow then.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def FillArray(self, item, array=[]) -> None:
        """ 

`FillArray`(*self*, *item*, *array=[]*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.FillArray "Permalink to this definition")
Internal function. Used to populate an array of selected items when
the style `TR_MULTIPLE` is used.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **array** (*list*) – a Python list containing the selected items.



Returns
A Python list containing the selected items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def FindItem(self, idParent, prefixOrig) -> None:
        """ 

`FindItem`(*self*, *idParent*, *prefixOrig*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.FindItem "Permalink to this definition")
Finds the first item starting with the given prefix after the given parent.



Parameters
* **idParent** (*integer*) – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **prefixOrig** (*string*) – a string containing the item text prefix.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if no item has been found.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Freeze(self) -> None:
        """ 

`Freeze`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze "Permalink to this definition")
Freeze [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").


Freezes the window or, in other words, prevents any updates from taking place
on screen, the window is not redrawn at all. [`Thaw`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Thaw "wx.lib.agw.customtreectrl.CustomTreeCtrl.Thaw") must be called to re-enable
window redrawing. Calls to these two functions may be nested.



Note


This method is useful for visual appearance optimization (for example,
it is a good idea to use it before doing many large text insertions in a row
into a `TextCtrl` under wxGTK) but is not implemented on all platforms nor
for all controls so it is mostly just a hint to wxWidgets and not a mandatory
directive.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ 

`GetAGWWindowStyleFlag`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetAGWWindowStyleFlag "Permalink to this definition")
Returns the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") style.



See also


The [`__init__`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__ "wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__") method for a list of possible style flags.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBackgroundImage(self) -> None:
        """ 

`GetBackgroundImage`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetBackgroundImage "Permalink to this definition")
Returns the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") background image (if any).



Returns
An instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") if a background image is present, `None` otherwise.





Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBorderPen(self) -> None:
        """ 

`GetBorderPen`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetBorderPen "Permalink to this definition")
Returns the pen used to draw the selected item border.



Returns
An instance of [`wx.Pen`](wx.Pen.html#wx.Pen "wx.Pen").





Note


The border pen is not used if the Windows Vista selection style is applied.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetBoundingRect(self, item, textOnly=False) -> None:
        """ 

`GetBoundingRect`(*self*, *item*, *textOnly=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetBoundingRect "Permalink to this definition")
Retrieves the rectangle bounding the item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **textOnly** (*bool*) – if `True`, only the rectangle around the item’s label will
be returned, otherwise the item’s image is also taken into account.



Returns
An instance of [`wx.Rect`](wx.Rect.html#wx.Rect "wx.Rect").





Note


The rectangle coordinates are logical, not physical ones. So, for example,
the *x* coordinate may be negative if the tree has a horizontal scrollbar and its
position is not `0`.




Warning


The `textOnly` flag is currently ignored and this method
always returns the rectangle including the item’s image, checkbox,
and window (if they exist) along with the item’s text. A separator’s
bounding box stretches the width of the entire client area. The height
may be 0 for newly added items until [`CustomTreeCtrl.CalculateSize`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculateSize "wx.lib.agw.customtreectrl.CustomTreeCtrl.CalculateSize")
is called while the tree is not frozen.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetButtonsImageList(self) -> None:
        """ 

`GetButtonsImageList`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetButtonsImageList "Permalink to this definition")
Returns the buttons image list associated with [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") (from
which application-defined button images are taken).



Returns
An instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetChildrenCount(self, item, recursively=True) -> int:
        """ 

`GetChildrenCount`(*self*, *item*, *recursively=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetChildrenCount "Permalink to this definition")
Returns the item children count.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **recursively** (*bool*) – if `True`, returns the total number of descendants,
otherwise only one level of children is counted.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetConnectionPen(self) -> None:
        """ 

`GetConnectionPen`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetConnectionPen "Permalink to this definition")
Returns the pen used to draw the connecting lines between items.



Returns
An instance of [`wx.Pen`](wx.Pen.html#wx.Pen "wx.Pen").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetControlBmp(self, checkbox=True, checked=False, enabled=True, x=16, y=16) -> None:
        """ 

`GetControlBmp`(*self*, *checkbox=True*, *checked=False*, *enabled=True*, *x=16*, *y=16*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetControlBmp "Permalink to this definition")
Returns a native looking checkbox or radio button bitmap.



Parameters
* **checkbox** (*bool*) – `True` to get a checkbox image, `False` for a radiobutton one;
* **checked** (*bool*) – `True` if the control is marked, `False` if it is not;
* **enabled** (*bool*) – `True` if the control is enabled, `False` if it is not;
* **x** (*integer*) – the width of the bitmap;
* **y** (*integer*) – the height of the bitmap.



Returns
An instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap"), representing a native looking checkbox or radiobutton.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetCount(self) -> None:
        """ 

`GetCount`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetCount "Permalink to this definition")
Returns the global number of items in the tree.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetDisabledColour(self) -> None:
        """ 

`GetDisabledColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetDisabledColour "Permalink to this definition")
Returns the colour for items in a disabled state.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetDragFullScreen(self) -> None:
        """ 

`GetDragFullScreen`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetDragFullScreen "Permalink to this definition")
Returns whether built-in drag/drop will be full screen or not.



Returns
`True` if the drag/drop operation will be full screen, or
`False` if only within the tree.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetEditControl(self) -> None:
        """ 

`GetEditControl`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetEditControl "Permalink to this definition")
Returns a reference to the edit [`TreeTextCtrl`](wx.lib.agw.customtreectrl.TreeTextCtrl.html#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl") if the item is being edited or
`None` otherwise (it is assumed that no more than one item may be edited
simultaneously).




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstChild(self, item: GenericTreeItem) -> None:
        """ 

`GetFirstChild`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetFirstChild "Permalink to this definition")
Returns the item’s first child and an integer value ‘cookie’.
Call [`GetNextChild`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextChild "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextChild") for the next child using this very ‘cookie’ return
value as an input.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
A tuple with the first value being an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further children, and as second value an integer parameter ‘cookie’.





Note


This method returns `None` if there are no further children.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstGradientColour(self) -> None:
        """ 

`GetFirstGradientColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetFirstGradientColour "Permalink to this definition")
Returns the first gradient colour for gradient-style selections.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetFirstVisibleItem(self) -> None:
        """ 

`GetFirstVisibleItem`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetFirstVisibleItem "Permalink to this definition")
Returns the first visible item.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
visible items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetGradientStyle(self) -> None:
        """ 

`GetGradientStyle`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetGradientStyle "Permalink to this definition")
Returns the gradient style for gradient-style selections.



Returns
`0` for horizontal gradient-style selections, `1` for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHilightFocusColour(self) -> None:
        """ 

`GetHilightFocusColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetHilightFocusColour "Permalink to this definition")
Returns the colour used to highlight focused selected items.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





Note


This is used only if gradient and Windows Vista selection
styles are disabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHilightNonFocusColour(self) -> None:
        """ 

`GetHilightNonFocusColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetHilightNonFocusColour "Permalink to this definition")
Returns the colour used to highlight unfocused selected items.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





Note


This is used only if gradient and Windows Vista selection
styles are disabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextFont(self) -> None:
        """ 

`GetHyperTextFont`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetHyperTextFont "Permalink to this definition")
Returns the font used to render hypertext items.



Returns
An instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextNewColour(self) -> None:
        """ 

`GetHyperTextNewColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetHyperTextNewColour "Permalink to this definition")
Returns the colour used to render a non-visited hypertext item.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetHyperTextVisitedColour(self) -> None:
        """ 

`GetHyperTextVisitedColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetHyperTextVisitedColour "Permalink to this definition")
Returns the colour used to render a visited hypertext item.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetImageList(self) -> None:
        """ 

`GetImageList`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetImageList "Permalink to this definition")
Returns the normal image list associated with [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Returns
An instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetImageListCheck(self) -> None:
        """ 

`GetImageListCheck`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetImageListCheck "Permalink to this definition")
Returns the image list used to build the check/radio buttons in [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Returns
An instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetIndent(self) -> None:
        """ 

`GetIndent`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetIndent "Permalink to this definition")
Returns the item indentation, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItem3StateValue(self, item: GenericTreeItem) -> None:
        """ 

`GetItem3StateValue`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItem3StateValue "Permalink to this definition")
Gets the state of a 3-state checkbox item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`wx.CHK_UNCHECKED` when the checkbox is unchecked, `wx.CHK_CHECKED`
when it is checked and `wx.CHK_UNDETERMINED` when it’s in the undetermined
state.





Note


This method raises an exception when the function is used with a 2-state
checkbox item.




Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemBackgroundColour(self, item: GenericTreeItem) -> None:
        """ 

`GetItemBackgroundColour`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemBackgroundColour "Permalink to this definition")
Returns the item background colour.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemFont(self, item: GenericTreeItem) -> None:
        """ 

`GetItemFont`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemFont "Permalink to this definition")
Returns the item font.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemImage(self, item, which=TreeItemIcon_Normal) -> None:
        """ 

`GetItemImage`(*self*, *item*, *which=TreeItemIcon\_Normal*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemImage "Permalink to this definition")
Returns the item image.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **which** (*integer*) – can be one of the following bits:





| Item State | Description |
| --- | --- |
| `TreeItemIcon_Normal` | To get the normal item image |
| `TreeItemIcon_Selected` | To get the selected item image (i.e. the image which is shown when the item is currently selected) |
| `TreeItemIcon_Expanded` | To get the expanded image (this only makes sense for items which have children - then this image is shown when the item is expanded and the normal image is shown when it is collapsed) |
| `TreeItemIcon_SelectedExpanded` | To get the selected expanded image (which is shown when an expanded item is currently selected) |



Returns
An integer index that can be used to retrieve the item image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemLeftImage(self, item: GenericTreeItem) -> None:
        """ 

`GetItemLeftImage`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemLeftImage "Permalink to this definition")
Returns the item leftmost image, i.e. the image associated to the item on the leftmost
part of the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") client area.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An integer index that can be used to retrieve the item leftmost image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemParent(self, item: GenericTreeItem) -> Optional['GenericTreeItem']:
        """ 

`GetItemParent`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemParent "Permalink to this definition")
Returns the item parent (can be `None` for root items).



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` for root items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemSize(self, item: GenericTreeItem) -> None:
        """ 

`GetItemSize`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemSize "Permalink to this definition")
Returns the horizontal space available in [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"), in pixels, to draw this item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





New in version 0.9.3.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemText(self, item: GenericTreeItem) -> str:
        """ 

`GetItemText`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemText "Permalink to this definition")
Returns the item text.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemTextColour(self, item: GenericTreeItem) -> None:
        """ 

`GetItemTextColour`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemTextColour "Permalink to this definition")
Returns the item text colour or separator horizontal line colour.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemType(self, item: GenericTreeItem) -> None:
        """ 

`GetItemType`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemType "Permalink to this definition")
Returns the item type.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An integer representing the item type.





See also


[`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a description of valid item types.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemVisited(self, item: GenericTreeItem) -> None:
        """ 

`GetItemVisited`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemVisited "Permalink to this definition")
Returns whether an hypertext item was visited.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the hypertext item has been visited, `False` otherwise.





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemWindow(self, item: GenericTreeItem) -> None:
        """ 

`GetItemWindow`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemWindow "Permalink to this definition")
Returns the window associated to the item (if any).



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") if the item has an associated window, `None` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetItemWindowEnabled(self, item: GenericTreeItem) -> None:
        """ 

`GetItemWindowEnabled`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemWindowEnabled "Permalink to this definition")
Returns whether the window associated to the item is enabled.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item has an associated window and this window is
enabled, `False` in all other cases.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLastChild(self, item: GenericTreeItem) -> None:
        """ 

`GetLastChild`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetLastChild "Permalink to this definition")
Returns the item last child.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further children.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLeftImageList(self) -> None:
        """ 

`GetLeftImageList`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetLeftImageList "Permalink to this definition")
Returns the image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.



Returns
An instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetLineHeight(self, item: GenericTreeItem) -> None:
        """ 

`GetLineHeight`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetLineHeight "Permalink to this definition")
Returns the line height for the given item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
the item height, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetMaxWidth(self, respect_expansion_state: bool=True) -> None:
        """ 

`GetMaxWidth`(*self*, *respect\_expansion\_state=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetMaxWidth "Permalink to this definition")
Returns the maximum width of the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**respect\_expansion\_state** (*bool*) – if `True`, only the expanded items (and their
children) will be measured. Otherwise all the items are expanded and
their width measured.



Returns
the maximum width of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"), in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNext(self, item: GenericTreeItem) -> None:
        """ 

`GetNext`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNext "Permalink to this definition")
Returns the next item. Only for internal use right now.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further items.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextActiveItem(self, item, down=True) -> None:
        """ 

`GetNextActiveItem`(*self*, *item*, *down=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextActiveItem "Permalink to this definition")
Returns the next active item. Used Internally at present.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **down** (*bool*) – `True` to search downwards in the hierarchy for an active item,
`False` to search upwards.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") if an active item has been found or
`None` if none has been found.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextChild(self, item, cookie) -> None:
        """ 

`GetNextChild`(*self*, *item*, *cookie*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextChild "Permalink to this definition")
Returns the item’s next child.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **cookie** – a parameter which is opaque for the application but is necessary
for the library to make these functions reentrant (i.e. allow more than one
enumeration on one and the same object simultaneously).



Returns
A tuple with the first value being an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further children, and as second value an integer parameter ‘cookie’.





Note


This method returns `None` if there are no further children.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextExpanded(self, item: 'GenericTreeItem') -> None:
        """ 

`GetNextExpanded`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextExpanded "Permalink to this definition")
Returns the next expanded item after the input one.



Parameters
**item** – an instance of `TreeListItem`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextShown(self, item: GenericTreeItem) -> None:
        """ 

`GetNextShown`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextShown "Permalink to this definition")
Returns the next displayed item in the tree. This is either the first
child of the item (if it is expanded and has children) or its next
sibling. If there is no next sibling the tree is walked backwards
until a next sibling for one of its parents is found.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if no item follows this one.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextSibling(self, item: GenericTreeItem) -> None:
        """ 

`GetNextSibling`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextSibling "Permalink to this definition")
Returns the next sibling of an item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further siblings.





Note


This method returns `None` if there are no further siblings.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetNextVisible(self, item: GenericTreeItem) -> None:
        """ 

`GetNextVisible`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetNextVisible "Permalink to this definition")
Returns the next visible item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
next visible items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrev(self, item: GenericTreeItem) -> None:
        """ 

`GetPrev`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrev "Permalink to this definition")
Returns the previous item. Only for internal use right now.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem")






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevExpanded(self, item: 'GenericTreeItem') -> None:
        """ 

`GetPrevExpanded`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrevExpanded "Permalink to this definition")
Returns the previous expanded item before the input one.



Parameters
**item** – an instance of `TreeListItem`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevShown(self, item: GenericTreeItem) -> None:
        """ 

`GetPrevShown`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrevShown "Permalink to this definition")
Returns the previous displayed item in the tree. This is either the
last displayed child of its previous sibling, or its parent item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if no previous item found (root).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevSibling(self, item: GenericTreeItem) -> None:
        """ 

`GetPrevSibling`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrevSibling "Permalink to this definition")
Returns the previous sibling of an item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
further siblings.





Note


This method returns `None` if there are no further siblings.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPrevVisible(self, item: GenericTreeItem) -> None:
        """ 

`GetPrevVisible`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPrevVisible "Permalink to this definition")
Returns the previous visible item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if there are no
previous visible items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetPyData(self, item: GenericTreeItem) -> None:
        """ 

`GetPyData`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetPyData "Permalink to this definition")
Returns the data associated to an item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
A Python object representing the item data, or `None` if no data
has been assigned to this item.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetRootItem(self) -> Optional['GenericTreeItem']:
        """ 

`GetRootItem`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetRootItem "Permalink to this definition")
Returns the root item, an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSecondGradientColour(self) -> None:
        """ 

`GetSecondGradientColour`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSecondGradientColour "Permalink to this definition")
Returns the second gradient colour for gradient-style selections.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSelection(self) -> Optional['GenericTreeItem']:
        """ 

`GetSelection`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelection "Permalink to this definition")
Returns the current selected item (i.e. focused item).



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Note


Similar to GetFocusedItem of wx.TreeCtrl. Use
[`GetSelections`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelections "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelections") for obtaining all items
selected in multiple-selection trees (i.e. TR\_MULTIPLE flag set).





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSelections(self) -> list['GenericTreeItem']:
        """ 

`GetSelections`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSelections "Permalink to this definition")
Returns a list of selected items.



Note


This method can be used only if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_MULTIPLE` or `TR_EXTENDED`
style set.




Returns
A Python list containing the selected items, all instances of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSeparatorColour(self, colour) -> None:
        """ 

`GetSeparatorColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSeparatorColour "Permalink to this definition")
Returns the pen colour for separator-type items.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") representing the separator pen colour.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetSpacing(self) -> None:
        """ 

`GetSpacing`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetSpacing "Permalink to this definition")
Returns the spacing between the start and the text, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def GetStateImageList(self) -> None:
        """ 

`GetStateImageList`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetStateImageList "Permalink to this definition")
Returns the state image list associated with [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") (from which
application-defined state images are taken).



Returns
An instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HandleHyperLink(self, item: GenericTreeItem) -> None:
        """ 

`HandleHyperLink`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HandleHyperLink "Permalink to this definition")
Handles the hyperlink items, sending the `EVT_TREE_ITEM_HYPERLINK` event.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasAGWFlag(self, flag: int) -> bool:
        """ 

`HasAGWFlag`(*self*, *flag*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HasAGWFlag "Permalink to this definition")
Returns `True` if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the *flag* bit set.



Parameters
**flag** (*integer*) – any possible window style for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").





See also


The [`__init__`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__ "wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__") method for the *flag* parameter description.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasButtons(self) -> None:
        """ 

`HasButtons`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HasButtons "Permalink to this definition")
Returns whether [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_HAS_BUTTONS` flag set.



Returns
`True` if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_HAS_BUTTONS` flag set,
`False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HasChildren(self, item: GenericTreeItem) -> None:
        """ 

`HasChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HasChildren "Permalink to this definition")
Returns whether an item has children or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideItem(self, item, hide=True) -> None:
        """ 

`HideItem`(*self*, *item*, *hide=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HideItem "Permalink to this definition")
Hides/shows an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **hide** – `True` to hide the item, `False` to show it.





Note


A hidden item always reports that it is collapsed and disabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideItemWindows(self, item) -> None:
        """ 

`HideItemWindows`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HideItemWindows "Permalink to this definition")
Hide all windows belonging to the item and its children.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HideWindows(self) -> None:
        """ 

`HideWindows`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HideWindows "Permalink to this definition")
Hides the windows associated to the items. Used internally.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def HitTest(self, point, flags=0) -> tuple['GenericTreeItem', int]:
        """ 

`HitTest`(*self*, *point*, *flags=0*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.HitTest "Permalink to this definition")
Calculates which (if any) item is under the given point, returning the tree item
at this point plus extra information flags.



Parameters
* **point** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point"), a point to test for hits;
* **flags** (*integer*) – a bitlist of the following values:






| HitTest Flags | Hex Value | Description |
| --- | --- | --- |
| `TREE_HITTEST_ABOVE` | 0x1 | Above the client area |
| `TREE_HITTEST_BELOW` | 0x2 | Below the client area |
| `TREE_HITTEST_NOWHERE` | 0x4 | No item has been hit |
| `TREE_HITTEST_ONITEMBUTTON` | 0x8 | On the button associated to an item |
| `TREE_HITTEST_ONITEMICON` | 0x10 | On the icon associated to an item |
| `TREE_HITTEST_ONITEMINDENT` | 0x20 | On the indent associated to an item |
| `TREE_HITTEST_ONITEMLABEL` | 0x40 | On the label (string) associated to an item |
| `TREE_HITTEST_ONITEM` | 0x50 | Anywhere on the item |
| `TREE_HITTEST_ONITEMRIGHT` | 0x80 | On the right of the label associated to an item |
| `TREE_HITTEST_TOLEFT` | 0x200 | On the left of the client area |
| `TREE_HITTEST_TORIGHT` | 0x400 | On the right of the client area |
| `TREE_HITTEST_ONITEMUPPERPART` | 0x800 | On the upper part (first half) of the item |
| `TREE_HITTEST_ONITEMLOWERPART` | 0x1000 | On the lower part (second half) of the item |
| `TREE_HITTEST_ONITEMCHECKICON` | 0x2000 | On the check/radio icon, if present |



Returns
A tuple with the first value being an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` if
no item has been hit-tested, and as second value an integer parameter *flag*.





Note


both the item (if any, `None` otherwise) and the *flags* are always returned as a tuple.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItem(self, parentId, input, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`InsertItem`(*self*, *parentId*, *input*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItem "Permalink to this definition")
Inserts an item after the given previous.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`InsertItemByIndex`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByIndex "wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByIndex") and [`InsertItemByItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByItem") for an explanation of
the input parameters.




See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItemByIndex(self, parentId, idPrevious, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`InsertItemByIndex`(*self*, *parentId*, *idPrevious*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByIndex "Permalink to this definition")
Inserts an item after the given previous.



Parameters
* **parentId** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent;
* **idPrevious** – the index at which we should insert the new item;
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item,
any subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item;
* **separator** (*bool*) – `True` if the item is a separator, `False` otherwise.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertItemByItem(self, parentId, idPrevious, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`InsertItemByItem`(*self*, *parentId*, *idPrevious*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByItem "Permalink to this definition")
Inserts an item after the given previous.



Parameters
* **parentId** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent;
* **idPrevious** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
previous item;
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item,
any subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item;
* **separator** (*bool*) – `True` if the item is a separator, `False` otherwise.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.



Raise
*Exception* if the previous item is not a sibling.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for other possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def InsertSeparator(self, parentId, input) -> None:
        """ 

`InsertSeparator`(*self*, *parentId*, *input*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertSeparator "Permalink to this definition")
Inserts a separator item after the given previous.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`InsertItemByIndex`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByIndex "wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByIndex") and [`InsertItemByItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.InsertItemByItem") for an explanation of
the input parameters.




See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsBold(self, item: GenericTreeItem) -> None:
        """ 

`IsBold`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsBold "Permalink to this definition")
Returns whether the item font is bold or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item has bold text, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsDescendantOf(self, parent, item) -> None:
        """ 

`IsDescendantOf`(*self*, *parent*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsDescendantOf "Permalink to this definition")
Checks if the given item is under another one in the tree hierarchy.



Parameters
* **parent** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem"), representing the possible
parent of *item*;
* **item** – another instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if *item* is a descendant of *parent*, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsExpanded(self, item: GenericTreeItem) -> None:
        """ 

`IsExpanded`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsExpanded "Permalink to this definition")
Returns whether the item is expanded or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item is expanded, `False` if it is collapsed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItalic(self, item: GenericTreeItem) -> None:
        """ 

`IsItalic`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItalic "Permalink to this definition")
Returns whether the item font is italic or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item has italic text, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItem3State(self, item: GenericTreeItem) -> None:
        """ 

`IsItem3State`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItem3State "Permalink to this definition")
Returns whether or not the checkbox item is a 3-state checkbox.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if this checkbox is a 3-state checkbox, `False` if it’s a
2-state checkbox item.





Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemChecked(self, item: GenericTreeItem) -> None:
        """ 

`IsItemChecked`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItemChecked "Permalink to this definition")
Returns whether an item is checked or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item is in a ‘checked’ state, `False` otherwise.





Note


This method is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemEnabled(self, item: GenericTreeItem) -> None:
        """ 

`IsItemEnabled`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItemEnabled "Permalink to this definition")
Returns whether an item is enabled or disabled.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemHyperText(self, item: GenericTreeItem) -> None:
        """ 

`IsItemHyperText`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItemHyperText "Permalink to this definition")
Returns whether an item is hypertext or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item is hypertext-like, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsItemSeparator(self, item: GenericTreeItem) -> None:
        """ 

`IsItemSeparator`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsItemSeparator "Permalink to this definition")
Returns whether an item is of separator type or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsSelected(self, item: GenericTreeItem) -> None:
        """ 

`IsSelected`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsSelected "Permalink to this definition")
Returns whether the item is selected or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item is selected, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def IsVisible(self, item: GenericTreeItem) -> None:
        """ 

`IsVisible`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.IsVisible "Permalink to this definition")
Returns whether the item is visible or not (i.e., its hierarchy is expanded
enough to show the item, and it has not been hidden).



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item is visible, `False` if it is hidden.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ItemHasChildren(self, item: GenericTreeItem) -> None:
        """ 

`ItemHasChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ItemHasChildren "Permalink to this definition")
Returns whether the item has children or not.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
`True` if the item has children, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnAcceptEdit(self, item, value) -> None:
        """ 

`OnAcceptEdit`(*self*, *item*, *value*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnAcceptEdit "Permalink to this definition")
Called by [`TreeTextCtrl`](wx.lib.agw.customtreectrl.TreeTextCtrl.html#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl"), to accept the changes and to send the
`EVT_TREE_END_LABEL_EDIT` event.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **value** (*string*) – the new value of the item label.



Returns
`True` if the editing has not been vetoed, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnCancelEdit(self, item: GenericTreeItem) -> None:
        """ 

`OnCancelEdit`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCancelEdit "Permalink to this definition")
Called by [`TreeTextCtrl`](wx.lib.agw.customtreectrl.TreeTextCtrl.html#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl"), to cancel the changes and to send the
`EVT_TREE_END_LABEL_EDIT` event.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnCompareItems(self, item1, item2) -> None:
        """ 

`OnCompareItems`(*self*, *item1*, *item2*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCompareItems "Permalink to this definition")
Returns whether 2 items have the same text.


Override this function in the derived class to change the sort order of the items
in the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). The function should return a negative, zero or positive
value if the first item is less than, equal to or greater than the second one.



Parameters
* **item1** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **item2** – another instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Returns
The return value is negative if *item1* < *item2*, zero if *item1* == *item2*
and strictly positive if *item1* < *item2*.





Note


The base class version compares items alphabetically.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnDestroy(self, event: 'WindowDestroyEvent') -> None:
        """ 

`OnDestroy`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnDestroy "Permalink to this definition")
Handles the `wx.EVT_WINDOW_DESTROY` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a [`wx.WindowDestroyEvent`](wx.WindowDestroyEvent.html#wx.WindowDestroyEvent "wx.WindowDestroyEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnEditTimer(self) -> None:
        """ 

`OnEditTimer`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnEditTimer "Permalink to this definition")
The timer for editing has expired. Start editing.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a `EraseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnGetToolTip(self, event: CommandTreeEvent) -> None:
        """ 

`OnGetToolTip`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnGetToolTip "Permalink to this definition")
Process the tooltip event, to speed up event processing. Does not actually
get a tooltip.



Parameters
**event** – a [`CommandTreeEvent`](wx.lib.agw.customtreectrl.CommandTreeEvent.html#wx.lib.agw.customtreectrl.CommandTreeEvent "wx.lib.agw.customtreectrl.CommandTreeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnInternalIdle(self) -> None:
        """ 

`OnInternalIdle`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnInternalIdle "Permalink to this definition")
This method is normally only used internally, but sometimes an application
may need it to implement functionality that should not be disabled by an
application defining an *OnIdle* handler in a derived class.


This method may be used to do delayed painting, for example, and most
implementations call [`wx.Window.UpdateWindowUI`](wx.Window.html#wx.Window.UpdateWindowUI "wx.Window.UpdateWindowUI") in order to send update events
to the window in idle time.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnKeyDown "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"), sending a
`EVT_TREE_KEY_DOWN` event.



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnMouse(self, event: MouseEvent) -> None:
        """ 

`OnMouse`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnMouse "Permalink to this definition")
Handles a bunch of `wx.EVT_MOUSE_EVENTS` events for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PaintItem(self, item, dc, level, align) -> None:
        """ 

`PaintItem`(*self*, *item*, *dc*, *level*, *align*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.PaintItem "Permalink to this definition")
Actually draws an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **level** (*integer*) – the item level in the tree hierarchy;
* **align** (*integer*) – an integer specifying the alignment type:





| *align* Value | Description |
| --- | --- |
| 0 | No horizontal alignment of windows (in items with windows). |
| 1 | Windows (in items with windows) are aligned at the same horizontal position. |
| 2 | Windows (in items with windows) are aligned at the rightmost edge of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). |






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PaintLevel(self, item, dc, level, y, align) -> None:
        """ 

`PaintLevel`(*self*, *item*, *dc*, *level*, *y*, *align*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.PaintLevel "Permalink to this definition")
Paint a level in the hierarchy of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **level** (*integer*) – the item level in the tree hierarchy;
* **y** (*integer*) – the current vertical position in the `ScrolledWindow`;
* **align** (*integer*) – an integer specifying the alignment type:





| *align* Value | Description |
| --- | --- |
| 0 | No horizontal alignment of windows (in items with windows). |
| 1 | Windows (in items with windows) are aligned at the same horizontal position. |
| 2 | Windows (in items with windows) are aligned at the rightmost edge of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). |






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PrependItem(self, parent, text, ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`PrependItem`(*self*, *parent*, *text*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.PrependItem "Permalink to this definition")
Prepends an item as a first child of parent.



Parameters
* **parent** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent;
* **text** (*string*) – the item text label;
* **ct\_type** (*integer*) – the item type (see [`SetItemType`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") for a list of valid
item types);
* **wnd** – if not `None`, a non-toplevel window to show next to the item, any
subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") except top-level windows;
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item;
* **separator** (*bool*) – `True` if the item is a separator, `False` otherwise.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def PrependSeparator(self, parent: GenericTreeItem) -> None:
        """ 

`PrependSeparator`(*self*, *parent*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.PrependSeparator "Permalink to this definition")
Prepends a separator item as a first child of parent.



Parameters
**parent** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") representing the
item’s parent.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") upon successful insertion.





See also


[`DoInsertItem`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.DoInsertItem") for possible exceptions generated by this method.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RecurseOnChildren(self, item, maxwidth, respect_expansion_state) -> None:
        """ 

`RecurseOnChildren`(*self*, *item*, *maxwidth*, *respect\_expansion\_state*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RecurseOnChildren "Permalink to this definition")
Recurses over all the children of the spcified items, calculating their
maximum width.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **maxwidth** (*integer*) – the current maximum width for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"), in pixels;
* **respect\_expansion\_state** (*bool*) – if `True`, only the expanded items (and their
children) will be measured. Otherwise all the items are expanded and
their width measured.



Returns
A tuple containing the maximum width and item height, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshItemWithWindows(self, item: 'GenericTreeItem') -> None:
        """ 

`RefreshItemWithWindows`(*self*, *item=None*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshItemWithWindows "Permalink to this definition")
Refreshes the items with which a window is associated.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem"). If *item* is `None`, then the
recursive refresh starts from the root node.





Note


This method is called only if the style `TR_ALIGN_WINDOWS_RIGHT` is used.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshLine(self, item: GenericTreeItem) -> None:
        """ 

`RefreshLine`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshLine "Permalink to this definition")
Refreshes a damaged item line.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSelected(self) -> None:
        """ 

`RefreshSelected`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshSelected "Permalink to this definition")
Refreshes a damaged selected item line.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSelectedUnder(self, item: GenericTreeItem) -> None:
        """ 

`RefreshSelectedUnder`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshSelectedUnder "Permalink to this definition")
Refreshes the selected items under the given item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def RefreshSubtree(self, item: GenericTreeItem) -> None:
        """ 

`RefreshSubtree`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.RefreshSubtree "Permalink to this definition")
Refreshes a damaged subtree of an item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ResetEditControl(self) -> None:
        """ 

`ResetEditControl`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ResetEditControl "Permalink to this definition")
Called by [`TreeTextCtrl`](wx.lib.agw.customtreectrl.TreeTextCtrl.html#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl") when it marks itself for deletion.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ScrollTo(self, item: GenericTreeItem) -> None:
        """ 

`ScrollTo`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ScrollTo "Permalink to this definition")
Scrolls the specified item into view.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectAll "Permalink to this definition")
Selects all the item in the tree.



Raise
*Exception* if used without the `TR_EXTENDED` or `TR_MULTIPLE` style set.





Note


This method can be used only if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_MULTIPLE` or `TR_EXTENDED`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectAllChildren(self, item: GenericTreeItem) -> None:
        """ 

`SelectAllChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectAllChildren "Permalink to this definition")
Selects all the children of the given item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Raise
*Exception* if used without the `TR_EXTENDED` or `TR_MULTIPLE` style set.





Note


This method can be used only if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_MULTIPLE` or `TR_EXTENDED`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectItem(self, item, select=True) -> None:
        """ 

`SelectItem`(*self*, *item*, *select=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectItem "Permalink to this definition")
Selects/deselects an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **select** (*bool*) – `True` to select an item, `False` to deselect it.





Note


If TR\_MULTIPLE is set, this actually toggles selection when select=True.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SelectItemRange(self, item1, item2) -> None:
        """ 

`SelectItemRange`(*self*, *item1*, *item2*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectItemRange "Permalink to this definition")
Selects all the items between *item1* and *item2*.



Parameters
* **item1** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem"), representing the first
item in the range to select;
* **item2** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem"), representing the last
item in the range to select.



Raise
*Exception* if used without the `TR_EXTENDED` or `TR_MULTIPLE` style set.





Note


This method can be used only if [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_MULTIPLE` or `TR_EXTENDED`
style set.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SendDeleteEvent(self, item: GenericTreeItem) -> None:
        """ 

`SendDeleteEvent`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SendDeleteEvent "Permalink to this definition")
Actually sends the `EVT_TREE_DELETE_ITEM` event.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ 

`SetAGWWindowStyleFlag`(*self*, *agwStyle*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetAGWWindowStyleFlag "Permalink to this definition")
Sets the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") window style.



Parameters
**agwStyle** (*integer*) – the new [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") window style.





See also


The [`__init__`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__ "wx.lib.agw.customtreectrl.CustomTreeCtrl.__init__") method for the *agwStyle* parameter description.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBackgroundColour(self, colour: NullColour) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetBackgroundColour "Permalink to this definition")
Changes the background colour of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**colour** – the colour to be used as the background colour, pass
`NullColour` to reset to the default colour.



Returns
`False` if the underlying `ScrolledWindow` does not accept
the new colour, `True` otherwise.





Note


The background colour is usually painted by the default `EraseEvent`
event handler function under Windows and automatically under GTK.




Note


Setting the background colour does not cause an immediate refresh, so
you may wish to call [`wx.Window.ClearBackground`](wx.Window.html#wx.Window.ClearBackground "wx.Window.ClearBackground") or [`wx.Window.Refresh`](wx.Window.html#wx.Window.Refresh "wx.Window.Refresh") after
calling this function.




Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBackgroundImage(self, image: None) -> None:
        """ 

`SetBackgroundImage`(*self*, *image*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetBackgroundImage "Permalink to this definition")
Sets the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") background image.



Parameters
**image** – if not `None`, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").





Note


At present, the background image can only be used in “tile” mode.




Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetBorderPen(self, pen: 'Pen') -> None:
        """ 

`SetBorderPen`(*self*, *pen*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetBorderPen "Permalink to this definition")
Sets the pen used to draw the selected item border.



Parameters
**pen** – an instance of [`wx.Pen`](wx.Pen.html#wx.Pen "wx.Pen").





Note


The border pen is not used if the Windows Vista selection style is applied.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetButtonsImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetButtonsImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetButtonsImageList "Permalink to this definition")
Sets the buttons image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") (from which application-defined
button images are taken).



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetConnectionPen(self, pen: 'Pen') -> None:
        """ 

`SetConnectionPen`(*self*, *pen*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetConnectionPen "Permalink to this definition")
Sets the pen used to draw the connecting lines between items.



Parameters
**pen** – an instance of [`wx.Pen`](wx.Pen.html#wx.Pen "wx.Pen").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetDisabledColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetDisabledColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetDisabledColour "Permalink to this definition")
Sets the colour for items in a disabled state.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetDragFullScreen(self, fullScreen: bool=False) -> None:
        """ 

`SetDragFullScreen`(*self*, *fullScreen=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetDragFullScreen "Permalink to this definition")
Sets whether a drag operation will be performed full screen or not.


A full screen drag allows the user to drag outside of the tree to
other controls. When the drag is finished the destination will have
to be found manually in the `EVT_TREE_END_DRAG` handler with
something like:


example:



```
wnd = wx.FindWindowAtPoint(self.ClientToScreen(event.GetPoint()))

```



Parameters
**fullScreen** (*bool*) – `False` (default) to drag within tree only.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetFirstGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetFirstGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetFirstGradientColour "Permalink to this definition")
Sets the first gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour is taken from the system value `wx.SYS_COLOUR_HIGHLIGHT`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetFont "Permalink to this definition")
Sets the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") font.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.





Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetForegroundColour(self, colour: NullColour) -> None:
        """ 

`SetForegroundColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetForegroundColour "Permalink to this definition")
Changes the foreground colour of [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**colour** – the colour to be used as the foreground colour, pass
`NullColour` to reset to the default colour.



Returns
`False` if the underlying `ScrolledWindow` does not accept
the new colour, `True` otherwise.





Note


Overridden from `ScrolledWindow`.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetGradientStyle(self, vertical: int=0) -> None:
        """ 

`SetGradientStyle`(*self*, *vertical=0*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetGradientStyle "Permalink to this definition")
Sets the gradient style for gradient-style selections.



Parameters
**vertical** (*integer*) – `0` for horizontal gradient-style selections, `1` for vertical
gradient-style selections.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHilightFocusColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHilightFocusColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetHilightFocusColour "Permalink to this definition")
Sets the colour used to highlight focused selected items.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.





Note


This is applied only if gradient and Windows Vista selection
styles are disabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHilightNonFocusColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHilightNonFocusColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetHilightNonFocusColour "Permalink to this definition")
Sets the colour used to highlight unfocused selected items.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.





Note


This is applied only if gradient and Windows Vista selection
styles are disabled.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextFont(self, font: 'Font') -> None:
        """ 

`SetHyperTextFont`(*self*, *font*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetHyperTextFont "Permalink to this definition")
Sets the font used to render hypertext items.



Parameters
**font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextNewColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextNewColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetHyperTextNewColour "Permalink to this definition")
Sets the colour used to render a non-visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetHyperTextVisitedColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHyperTextVisitedColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetHyperTextVisitedColour "Permalink to this definition")
Sets the colour used to render a visited hypertext item.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetImageList "Permalink to this definition")
Sets the normal image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetImageListCheck(self, sizex, sizey, imglist=None) -> None:
        """ 

`SetImageListCheck`(*self*, *sizex*, *sizey*, *imglist=None*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetImageListCheck "Permalink to this definition")
Sets the checkbox/radiobutton image list.



Parameters
* **sizex** (*integer*) – the width of the bitmaps in the *imglist*, in pixels;
* **sizey** (*integer*) – the height of the bitmaps in the *imglist*, in pixels;
* **imglist** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetIndent(self, indent: int) -> None:
        """ 

`SetIndent`(*self*, *indent*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetIndent "Permalink to this definition")
Sets the indentation for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**indent** (*integer*) – an integer representing the indentation for the items in the tree.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItem3State(self, item, allow) -> None:
        """ 

`SetItem3State`(*self*, *item*, *allow*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItem3State "Permalink to this definition")
Sets whether the item has a 3-state value checkbox assigned to it or not.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **allow** (*bool*) – `True` to set an item as a 3-state checkbox, `False` to set it
to a 2-state checkbox.



Returns
`True` if the change was successful, `False` otherwise.





Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItem3StateValue(self, item, state) -> None:
        """ 

`SetItem3StateValue`(*self*, *item*, *state*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItem3StateValue "Permalink to this definition")
Sets the checkbox item to the given *state*.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **state** (*integer*) – can be one of: `wx.CHK_UNCHECKED` (check is off), `wx.CHK_CHECKED`
(check is on) or `wx.CHK_UNDETERMINED` (check is mixed).





Note


This method raises an exception when the checkbox item is a 2-state checkbox
and setting the state to `wx.CHK_UNDETERMINED`.




Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemBackgroundColour(self, item, colour) -> None:
        """ 

`SetItemBackgroundColour`(*self*, *item*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemBackgroundColour "Permalink to this definition")
Sets the item background colour.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemBold(self, item, bold=True) -> None:
        """ 

`SetItemBold`(*self*, *item*, *bold=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemBold "Permalink to this definition")
Sets the item font as bold/unbold.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **bold** (*bool*) – `True` to set the item font as bold, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemDropHighlight(self, item, highlight=True) -> None:
        """ 

`SetItemDropHighlight`(*self*, *item*, *highlight=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemDropHighlight "Permalink to this definition")
Gives the item the visual feedback for drag and drop operations.
This is useful when something is dragged from outside the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **highlight** (*bool*) – `True` to highlight the dragged items, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemFont(self, item, font) -> None:
        """ 

`SetItemFont`(*self*, *item*, *font*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemFont "Permalink to this definition")
Sets the item font.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **font** – a valid [`wx.Font`](wx.Font.html#wx.Font "wx.Font") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemHasChildren(self, item, has=True) -> None:
        """ 

`SetItemHasChildren`(*self*, *item*, *has=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHasChildren "Permalink to this definition")
Forces the appearance/disappearance of the button next to the item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **has** (*bool*) – `True` to have a button next to an item, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemHyperText(self, item, hyper=True) -> None:
        """ 

`SetItemHyperText`(*self*, *item*, *hyper=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **hyper** (*bool*) – `True` to have an item with hypertext behaviour, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemImage(self, item, image, which=TreeItemIcon_Normal) -> None:
        """ 

`SetItemImage`(*self*, *item*, *image*, *which=TreeItemIcon\_Normal*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemImage "Permalink to this definition")
Sets the item image, depending on the item state.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in the state specified by the *which* parameter;
* **which** (*integer*) – the item state.





See also


[`GetItemImage`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemImage "wx.lib.agw.customtreectrl.CustomTreeCtrl.GetItemImage") for an explanation of the *which* parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemItalic(self, item, italic=True) -> None:
        """ 

`SetItemItalic`(*self*, *item*, *italic=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemItalic "Permalink to this definition")
Sets the item font as italic/non-italic.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **italic** (*bool*) – `True` to set the item font as italic, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemLeftImage(self, item, image) -> None:
        """ 

`SetItemLeftImage`(*self*, *item*, *image*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemLeftImage "Permalink to this definition")
Sets the item leftmost image, i.e. the image associated to the item on the leftmost
part of the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") client area.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **image** (*integer*) – an index within the left image list specifying the image to
use for the item in the leftmost part of the client area.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ 

`SetItemText`(*self*, *item*, *text*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemText "Permalink to this definition")
Sets the item text.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **text** (*string*) – the new item label.



Raise
*Exception* if the input *item* is a separator.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemTextColour(self, item, colour) -> None:
        """ 

`SetItemTextColour`(*self*, *item*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemTextColour "Permalink to this definition")
Sets the item text colour or separator horizontal line colour.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemType(self, item, ct_type) -> None:
        """ 

`SetItemType`(*self*, *item*, *ct\_type*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "Permalink to this definition")
Sets the item type.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **ct\_type** (*integer*) – may be one of the following integers:





| *ct\_type* Value | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |





Note


Regarding radiobutton-type items (with *ct\_type* = 2), the following
approach is used:


* All peer-nodes that are radiobuttons will be mutually exclusive. In other words,
only one of a set of radiobuttons that share a common parent can be checked at
once. If a radiobutton node becomes checked, then all of its peer radiobuttons
must be unchecked.
* If a radiobutton node becomes unchecked, then all of its child nodes will become
inactive.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemVisited(self, item, visited=True) -> None:
        """ 

`SetItemVisited`(*self*, *item*, *visited=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemVisited "Permalink to this definition")
Sets whether an hypertext item was visited.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **visited** (*bool*) – `True` to mark an hypertext item as visited, `False` otherwise.





Note


This method is meaningful only for hypertext-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemWindow(self, item, wnd, on_the_right=True) -> None:
        """ 

`SetItemWindow`(*self*, *item*, *wnd*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemWindow "Permalink to this definition")
Sets the window for the given item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **wnd** – if not `None`, a non-toplevel window to be displayed next to
the item.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image. New in wxPython 4.0.4.



Raise
*Exception* if the input *item* is a separator and *wnd* is not `None`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetItemWindowEnabled(self, item, enable=True) -> None:
        """ 

`SetItemWindowEnabled`(*self*, *item*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemWindowEnabled "Permalink to this definition")
Enables/disables the window associated to the item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **enable** (*bool*) – `True` to enable the associated window, `False` to
disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetLeftImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetLeftImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetLeftImageList "Permalink to this definition")
Sets the image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") filled with images to be used on
the leftmost part of the client area. Any item can have a leftmost image associated
with it.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetPyData(self, item, data) -> None:
        """ 

`SetPyData`(*self*, *item*, *data*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetPyData "Permalink to this definition")
Sets the data associated to an item.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **data** (*object*) – can be any Python object.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSecondGradientColour(self, colour: Optional[None]=None) -> None:
        """ 

`SetSecondGradientColour`(*self*, *colour=None*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetSecondGradientColour "Permalink to this definition")
Sets the second gradient colour for gradient-style selections.



Parameters
**colour** – if not `None`, a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") instance. Otherwise,
the colour generated is a slightly darker version of the [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl")
background colour.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSeparatorColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetSeparatorColour`(*self*, *colour*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetSeparatorColour "Permalink to this definition")
Sets the pen colour for separator-type items.



Parameters
**colour** – a valid instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetSpacing(self, spacing: int) -> None:
        """ 

`SetSpacing`(*self*, *spacing*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetSpacing "Permalink to this definition")
Sets the spacing between items in [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**spacing** (*integer*) – an integer representing the spacing between items in the tree.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SetStateImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetStateImageList`(*self*, *imageList*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetStateImageList "Permalink to this definition")
Sets the state image list for [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") (from which application-defined
state images are taken).



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ShouldInheritColours(self) -> None:
        """ 

`ShouldInheritColours`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ShouldInheritColours "Permalink to this definition")
Return `True` from here to allow the colours of this window to be
changed by `InheritAttributes`, returning `False` forbids inheriting them
from the parent window.


The base class version returns `False`, but this method is overridden in
[`wx.Control`](wx.Control.html#wx.Control "wx.Control") where it returns `True`.


[`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") does not inherit colours from anyone.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def SortChildren(self, item: GenericTreeItem) -> None:
        """ 

`SortChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.SortChildren "Permalink to this definition")
Sorts the children of the given item using the [`OnCompareItems`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCompareItems "wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCompareItems") method of
[`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").





Note


You should override the [`OnCompareItems`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCompareItems "wx.lib.agw.customtreectrl.CustomTreeCtrl.OnCompareItems") method in your derived class to change
the sort order (the default is ascending case-sensitive alphabetical order).





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TagAllChildrenUntilLast(self, crt_item, last_item, select) -> None:
        """ 

`TagAllChildrenUntilLast`(*self*, *crt\_item*, *last\_item*, *select*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.TagAllChildrenUntilLast "Permalink to this definition")
Used internally.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TagNextChildren(self, crt_item, last_item, select) -> None:
        """ 

`TagNextChildren`(*self*, *crt\_item*, *last\_item*, *select*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.TagNextChildren "Permalink to this definition")
Used internally.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Thaw(self) -> None:
        """ 

`Thaw`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Thaw "Permalink to this definition")
Thaw [`CustomTreeCtrl`](#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").


Reenables window updating after a previous call to [`Freeze`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze "wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze"). To really thaw the
control, it must be called exactly the same number of times as [`Freeze`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze "wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze").



Raise
*Exception* if [`Thaw`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Thaw "wx.lib.agw.customtreectrl.CustomTreeCtrl.Thaw") has been called without an un-matching [`Freeze`](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze "wx.lib.agw.customtreectrl.CustomTreeCtrl.Freeze").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def TileBackground(self, dc: 'DC') -> None:
        """ 

`TileBackground`(*self*, *dc*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.TileBackground "Permalink to this definition")
Tiles the background image to fill all the available area.



Parameters
**dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC").





Todo


Support background images also in stretch and centered modes.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Toggle(self, item: GenericTreeItem) -> None:
        """ 

`Toggle`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Toggle "Permalink to this definition")
Toggles the item state (collapsed/expanded).



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def ToggleItemSelection(self, item: GenericTreeItem) -> None:
        """ 

`ToggleItemSelection`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.ToggleItemSelection "Permalink to this definition")
Toggles the item selection.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnCheckRadioParent(self, item, checked=False) -> None:
        """ 

`UnCheckRadioParent`(*self*, *item*, *checked=False*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.UnCheckRadioParent "Permalink to this definition")
Used internally to handle radio node parent correctly.



Parameters
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **checked** (*bool*) – `True` to check an item, `False` to uncheck it.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def Unselect(self) -> None:
        """ 

`Unselect`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.Unselect "Permalink to this definition")
Unselects the current selection.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnselectAll(self) -> None:
        """ 

`UnselectAll`(*self*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.UnselectAll "Permalink to this definition")
Unselect all the items.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """

    def UnselectAllChildren(self, item: GenericTreeItem) -> None:
        """ 

`UnselectAllChildren`(*self*, *item*)[¶](#wx.lib.agw.customtreectrl.CustomTreeCtrl.UnselectAllChildren "Permalink to this definition")
Unselects all the children of the given item.



Parameters
**item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.CustomTreeCtrl.html
        """



EVT_WINDOW_DESTROY: int

EVT_ERASE_BACKGROUND: int

EVT_KEY_DOWN: int

EVT_KILL_FOCUS: int

EVT_MOUSE_EVENTS: int

EVT_PAINT: int

EVT_SET_FOCUS: int

EVT_SIZE: int

CHK_UNCHECKED: int

CHK_CHECKED: int

CHK_UNDETERMINED: int

SYS_COLOUR_HIGHLIGHT: int

class DragImage(DragImage):
    """ This class handles the creation of a custom image in case of item drag
and drop.


  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
    """
    def __init__(self, treeCtrl, item) -> None:
        """ 

`__init__`(*self*, *treeCtrl*, *item*)[¶](#wx.lib.agw.customtreectrl.DragImage.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **treeCtrl** – the parent [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl");
* **item** – one of the tree control item (an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem")).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
        """

    def CreateBitmap(self) -> None:
        """ 

`CreateBitmap`(*self*)[¶](#wx.lib.agw.customtreectrl.DragImage.CreateBitmap "Permalink to this definition")
Actually creates the drag and drop bitmap for [`DragImage`](#wx.lib.agw.customtreectrl.DragImage "wx.lib.agw.customtreectrl.DragImage").



Returns
An instance of [`DragImage`](#wx.lib.agw.customtreectrl.DragImage "wx.lib.agw.customtreectrl.DragImage"), a close representation of the item’s
appearance (i.e., a screenshot of the item).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.DragImage.html
        """



class GenericTreeItem:
    """ This class holds all the information and methods for every single item in
[`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"). This is a generic implementation of `TreeItem`.


  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
    """
    def __init__(self, parent, text="", ct_type=0, wnd=None, image=-1, selImage=-1, data=None, separator=False, on_the_right=True) -> None:
        """ 

`__init__`(*self*, *parent*, *text=""*, *ct\_type=0*, *wnd=None*, *image=-1*, *selImage=-1*, *data=None*, *separator=False*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **parent** – the tree item parent, an instance of [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") (may
be `None` for root items);
* **text** (*string*) – the tree item text;
* **ct\_type** (*integer*) – the tree item kind. May be one of the following integers:





| *ct\_type* Value | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |
* **wnd** – if not `None`, a non-toplevel window to be displayed next to
the item, an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **image** (*integer*) – an index within the normal image list specifying the image to
use for the item in unselected state;
* **selImage** (*integer*) – an index within the normal image list specifying the image to
use for the item in selected state; if *image* > -1 and *selImage* is -1, the
same image is used for both selected and unselected items;
* **data** (*object*) – associate the given Python object *data* with the item;
* **separator** (*bool*) – `True` if the item is a separator, `False` otherwise.
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image.





Note


Regarding radiobutton-type items (with *ct\_type* = 2), the following
approach is used:


* All peer-nodes that are radiobuttons will be mutually exclusive. In other words,
only one of a set of radiobuttons that share a common parent can be checked at
once. If a radiobutton node becomes checked, then all of its peer radiobuttons
must be unchecked.
* If a radiobutton node becomes unchecked, then all of its child nodes will become
inactive.




Note


Separator items should not have children, labels, data or an associated window.
Other issues/features associated to separator items:


* You can change the color of individual separators by using `CustomTreeCtrl.SetItemTextColour()`,
or you can use `CustomTreeCtrl.SetSeparatorColour()` to change the color of all
separators. The default separator colour is that returned by *SystemSettings.GetColour(wx.SYS\_COLOUR\_GRAYTEXT)*;
* Separators can be selected just like any other tree item;
* Separators cannot have text;
* Separators cannot have children;
* Separators cannot be edited via the `EVT_TREE_BEGIN_LABEL_EDIT` event.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def AssignAttributes(self, attr: TreeItemAttr) -> None:
        """ 

`AssignAttributes`(*self*, *attr*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.AssignAttributes "Permalink to this definition")
Assigns the item attributes (font, colours, etc…) for this item.



Parameters
**attr** – an instance of [`TreeItemAttr`](wx.lib.agw.customtreectrl.TreeItemAttr.html#wx.lib.agw.customtreectrl.TreeItemAttr "wx.lib.agw.customtreectrl.TreeItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Attr(self) -> None:
        """ 

`Attr`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Attr "Permalink to this definition")
Creates a new attribute (font, colours, etc…) for this item.



Returns
An instance of [`TreeItemAttr`](wx.lib.agw.customtreectrl.TreeItemAttr.html#wx.lib.agw.customtreectrl.TreeItemAttr "wx.lib.agw.customtreectrl.TreeItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Check(self, checked: bool=True) -> None:
        """ 

`Check`(*self*, *checked=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Check "Permalink to this definition")
Checks/unchecks an item. Internal use only.



Parameters
**checked** (*bool*) – `True` to check an item, `False` to uncheck it.





Note


This is meaningful only for checkbox-like and radiobutton-like items.




Note


Always use [`CustomTreeCtrl.CheckItem`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.CheckItem") instead to update the tree properly and send events.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Collapse(self) -> None:
        """ 

`Collapse`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Collapse "Permalink to this definition")
Collapses the item. Internal use only.



Note


Always use [`CustomTreeCtrl.Collapse`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.Collapse "wx.lib.agw.customtreectrl.CustomTreeCtrl.Collapse") instead to update the tree properly and send events.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def DeleteChildren(self, tree: CustomTreeCtrl) -> None:
        """ 

`DeleteChildren`(*self*, *tree*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.DeleteChildren "Permalink to this definition")
Deletes the item children. Internal use only.



Parameters
**tree** – the main [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") instance.





Note


Always use [`CustomTreeCtrl.DeleteChildren`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteChildren "wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteChildren") instead to update the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def DeleteWindow(self) -> None:
        """ 

`DeleteWindow`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.DeleteWindow "Permalink to this definition")
Deletes the window associated to the item (if any). Internal use only.



Note


Always use [`CustomTreeCtrl.DeleteItemWindow`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteItemWindow "wx.lib.agw.customtreectrl.CustomTreeCtrl.DeleteItemWindow") instead to update the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Enable(self, enable: bool=True) -> None:
        """ 

`Enable`(*self*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Enable "Permalink to this definition")
Enables/disables the item.



Parameters
**enable** (*bool*) – `True` to enable the item, `False` to disable it.





Note


Call [`CustomTreeCtrl.EnableItem`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.EnableItem") instead to update the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Expand(self) -> None:
        """ 

`Expand`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Expand "Permalink to this definition")
Expands the item. Internal use only.



Note


Always use [`CustomTreeCtrl.Expand`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.Expand "wx.lib.agw.customtreectrl.CustomTreeCtrl.Expand") instead to update the tree properly and send events.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Get3StateValue(self) -> None:
        """ 

`Get3StateValue`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Get3StateValue "Permalink to this definition")
Gets the state of a 3-state checkbox item.



Returns
`wx.CHK_UNCHECKED` when the checkbox is unchecked, `wx.CHK_CHECKED`
when it is checked and `wx.CHK_UNDETERMINED` when it’s in the undetermined
state.



Raise
*Exception* when the item is not a 3-state checkbox item.





Note


This method raises an exception when the function is used with a 2-state
checkbox item.




Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetAttributes(self) -> None:
        """ 

`GetAttributes`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetAttributes "Permalink to this definition")
Returns the item attributes (font, colours, etc…).



Returns
An instance of [`TreeItemAttr`](wx.lib.agw.customtreectrl.TreeItemAttr.html#wx.lib.agw.customtreectrl.TreeItemAttr "wx.lib.agw.customtreectrl.TreeItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCheckedImage(self, which: int=TreeItemIcon_Checked) -> None:
        """ 

`GetCheckedImage`(*self*, *which=TreeItemIcon\_Checked*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetCheckedImage "Permalink to this definition")
Returns the item check image.



Parameters
**which** (*integer*) – can be one of the following bits:





| Item State | Description |
| --- | --- |
| `TreeItemIcon_Checked` | To get the checkbox checked item image |
| `TreeItemIcon_NotChecked` | To get the checkbox unchecked item image |
| `TreeItemIcon_Undetermined` | To get the checkbox undetermined state item image |
| `TreeItemIcon_Flagged` | To get the radiobutton checked image |
| `TreeItemIcon_NotFlagged` | To get the radiobutton unchecked image |






Returns
An integer index that can be used to retrieve the item check image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").





Note


This method is meaningful only for radio & check items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetChildren(self) -> list['GenericTreeItem']:
        """ 

`GetChildren`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetChildren "Permalink to this definition")
Returns the item’s children.



Returns
A Python list containing instances of [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem"), representing
this item’s children.





Note


The returned value is a reference to the list of children
used internally by the tree. It is advised not to change this list
and to make a copy before calling other tree methods as they could
change the contents of the list.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetChildrenCount(self, recursively: bool=True) -> None:
        """ 

`GetChildrenCount`(*self*, *recursively=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetChildrenCount "Permalink to this definition")
Gets the number of children of this item.



Parameters
**recursively** (*bool*) – if `True`, returns the total number of descendants,
otherwise only one level of children is counted.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCurrentCheckedImage(self) -> None:
        """ 

`GetCurrentCheckedImage`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetCurrentCheckedImage "Permalink to this definition")
Returns the current item check image.



Returns
An integer index that can be used to retrieve the item check image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetCurrentImage(self) -> None:
        """ 

`GetCurrentImage`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetCurrentImage "Permalink to this definition")
Returns the current item image.



Returns
An integer index that can be used to retrieve the item image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetData(self) -> Any:
        """ 

`GetData`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetData "Permalink to this definition")
Returns the data associated to this item.



Returns
A Python object representing the item data, or `None` if no data
has been assigned to this item.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetHeight(self) -> None:
        """ 

`GetHeight`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetHeight "Permalink to this definition")
Returns the height of the item, in pixels.


This will be 0 when the item is first created and always 0 for hidden
items. It is updated when the item is calculated.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetImage(self, which: int=TreeItemIcon_Normal) -> None:
        """ 

`GetImage`(*self*, *which=TreeItemIcon\_Normal*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetImage "Permalink to this definition")
Returns the item image for a particular item state.



Parameters
**which** (*integer*) – can be one of the following bits:





| Item State | Description |
| --- | --- |
| `TreeItemIcon_Normal` | To get the normal item image |
| `TreeItemIcon_Selected` | To get the selected item image (i.e. the image which is shown when the item is currently selected) |
| `TreeItemIcon_Expanded` | To get the expanded image (this only makes sense for items which have children - then this image is shown when the item is expanded and the normal image is shown when it is collapsed) |
| `TreeItemIcon_SelectedExpanded` | To get the selected expanded image (which is shown when an expanded item is currently selected) |






Returns
An integer index that can be used to retrieve the item image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetLeftImage(self) -> None:
        """ 

`GetLeftImage`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetLeftImage "Permalink to this definition")
Returns the leftmost image associated to this item, i.e. the image on the
leftmost part of the client area of [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Returns
An integer index that can be used to retrieve the item leftmost image inside
a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetParent(self) -> Optional['GenericTreeItem']:
        """ 

`GetParent`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetParent "Permalink to this definition")
Gets the item parent (another instance of [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` for
root items.



Returns
An instance of [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") or `None` for root items.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetSize(self, x, y, theButton) -> None:
        """ 

`GetSize`(*self*, *x*, *y*, *theButton*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetSize "Permalink to this definition")
Returns the item size.



Parameters
* **x** (*integer*) – the current item’s x position;
* **y** (*integer*) – the current item’s y position;
* **theButton** – an instance of the main [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").



Returns
A tuple of (*x*, *y*) dimensions, in pixels, representing the
item’s width and height.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetText "Permalink to this definition")
Returns the item text.



Returns
A string containing the item text.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetType(self) -> None:
        """ 

`GetType`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetType "Permalink to this definition")
Returns the item type.



See also


[`SetType`](#wx.lib.agw.customtreectrl.GenericTreeItem.SetType "wx.lib.agw.customtreectrl.GenericTreeItem.SetType") and [`__init__`](#wx.lib.agw.customtreectrl.GenericTreeItem.__init__ "wx.lib.agw.customtreectrl.GenericTreeItem.__init__") for a description of valid item types.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetValue(self) -> None:
        """ 

`GetValue`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetValue "Permalink to this definition")
Returns whether the item is checked or not.



Note


This is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetVisited(self) -> None:
        """ 

`GetVisited`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetVisited "Permalink to this definition")
Returns whether an hypertext item was visited or not.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWidth(self) -> None:
        """ 

`GetWidth`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetWidth "Permalink to this definition")
Returns the width of the item’s contents, in pixels.


This is the width of the item’s text plus the widths of the item’s
image, checkbox, and window (if they exist).
A separator’s width is the width of the entire client area.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindow(self) -> None:
        """ 

`GetWindow`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetWindow "Permalink to this definition")
Returns the window associated to the item (if any).



Returns
An instance of any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived class, excluding top-level windows.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindowEnabled(self) -> None:
        """ 

`GetWindowEnabled`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetWindowEnabled "Permalink to this definition")
Returns whether the associated window is enabled or not.



Returns
`True` if the associated window is enabled, `False` if it is disabled.



Raise
*Exception* when the item has no associated window.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetWindowSize(self) -> None:
        """ 

`GetWindowSize`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetWindowSize "Permalink to this definition")
Returns the associated window size.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetX(self) -> None:
        """ 

`GetX`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetX "Permalink to this definition")
Returns the *x* position on an item, in logical coordinates.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def GetY(self) -> None:
        """ 

`GetY`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.GetY "Permalink to this definition")
Returns the *y* position on an item, in logical coordinates.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HasChildren(self) -> None:
        """ 

`HasChildren`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.HasChildren "Permalink to this definition")
Returns whether the item has children or not.



Returns
`True` if the item has children, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HasPlus(self) -> None:
        """ 

`HasPlus`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.HasPlus "Permalink to this definition")
Returns whether the item has the plus button or not.



Returns
`True` if the item has a ‘plus’ mark, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Hide(self, hide: bool) -> None:
        """ 

`Hide`(*self*, *hide*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Hide "Permalink to this definition")
Hides/shows the item. Internal use only.



Parameters
**hide** – `True` to hide the item, `False` to show it.





Note


Always use [`CustomTreeCtrl.HideItem`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.HideItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.HideItem") instead to update the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def HitTest(self, point, theCtrl, flags=0, level=0) -> None:
        """ 

`HitTest`(*self*, *point*, *theCtrl*, *flags=0*, *level=0*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.HitTest "Permalink to this definition")
[`HitTest`](#wx.lib.agw.customtreectrl.GenericTreeItem.HitTest "wx.lib.agw.customtreectrl.GenericTreeItem.HitTest") method for an item. Called from the main window `CustomTreeCtrl.HitTest()`.



Parameters
* **point** – the point to test for the hit (an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point"));
* **theCtrl** – the main [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") tree;
* **flags** (*integer*) – a bitlist of hit locations;
* **level** (*integer*) – the item’s level inside the tree hierarchy.





See also


`CustomTreeCtrl.HitTest()` method for the flags explanation.




Returns
A 2-tuple of (item, flags). The item may be `None`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Insert(self, child, index) -> None:
        """ 

`Insert`(*self*, *child*, *index*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Insert "Permalink to this definition")
Inserts an item in the item children list for this item.



Parameters
* **child** – an instance of [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **index** (*integer*) – the index at which we should insert the new child.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Is3State(self) -> None:
        """ 

`Is3State`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Is3State "Permalink to this definition")
Returns whether or not the checkbox item is a 3-state checkbox.



Returns
`True` if this checkbox is a 3-state checkbox, `False` if it’s a
2-state checkbox item.





Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsBold(self) -> None:
        """ 

`IsBold`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsBold "Permalink to this definition")
Returns whether the item font is bold or not.



Returns
`True` if the item has bold text, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsChecked(self) -> None:
        """ 

`IsChecked`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsChecked "Permalink to this definition")
This is just a maybe more readable synonym for [`GetValue`](#wx.lib.agw.customtreectrl.GenericTreeItem.GetValue "wx.lib.agw.customtreectrl.GenericTreeItem.GetValue").
Returns whether the item is checked or not.



Note


This is meaningful only for checkbox-like and radiobutton-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsEnabled(self) -> None:
        """ 

`IsEnabled`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsEnabled "Permalink to this definition")
Returns whether the item is enabled or not. Hidden items always return False.



Returns
`True` if the item is enabled, `False` if it is disabled.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsExpanded(self) -> None:
        """ 

`IsExpanded`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsExpanded "Permalink to this definition")
Returns whether the item is expanded or not. Hidden items always return False.



Returns
`True` if the item is expanded, `False` if it is collapsed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsHidden(self) -> None:
        """ 

`IsHidden`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsHidden "Permalink to this definition")
Returns whether the item is hidden or not.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsHyperText(self) -> None:
        """ 

`IsHyperText`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsHyperText "Permalink to this definition")
Returns whether the item is hypetext or not.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsItalic(self) -> None:
        """ 

`IsItalic`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsItalic "Permalink to this definition")
Returns whether the item font is italic or not.



Returns
`True` if the item has italic text, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsOk(self) -> None:
        """ 

`IsOk`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsOk "Permalink to this definition")
Returns whether the item is ok or not.



Note


This method always returns `True`, it has been added for
backward compatibility with the wxWidgets C++ implementation.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsSelected(self) -> None:
        """ 

`IsSelected`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsSelected "Permalink to this definition")
Returns whether the item is selected or not.



Returns
`True` if the item is selected, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def IsSeparator(self) -> None:
        """ 

`IsSeparator`(*self*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.IsSeparator "Permalink to this definition")
Returns whether the item is meant to be an horizontal line separator or not.



Returns
`True` if this item is a separator, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for the window associated with the item.



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def OnTreeItemCollapsing(self, event: GenericTreeItem) -> None:
        """ 

`OnTreeItemCollapsing`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.OnTreeItemCollapsing "Permalink to this definition")
Handles the `wx.EVT_TREE_ITEM_COLLAPSING` event for the window associated with the item.



Parameters
**event** – a [`GenericTreeItem`](#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Set3State(self, allow: bool) -> None:
        """ 

`Set3State`(*self*, *allow*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Set3State "Permalink to this definition")
Sets whether the item has a 3-state value checkbox assigned to it or not.



Parameters
**allow** (*bool*) – `True` to set an item as a 3-state checkbox, `False` to set it
to a 2-state checkbox.



Returns
`True` if the change was successful, `False` otherwise.





Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def Set3StateValue(self, state: int) -> None:
        """ 

`Set3StateValue`(*self*, *state*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.Set3StateValue "Permalink to this definition")
Sets the checkbox item to the given *state*.



Parameters
**state** (*integer*) – can be one of: `wx.CHK_UNCHECKED` (check is off), `wx.CHK_CHECKED`
(check is on) or `wx.CHK_UNDETERMINED` (check is mixed).



Raise
*Exception* when the item is not a 3-state checkbox item.





Note


This method raises an exception when the checkbox item is a 2-state checkbox
and setting the state to `wx.CHK_UNDETERMINED`.




Note


This method is meaningful only for checkbox-like items.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetAttributes(self, attr: TreeItemAttr) -> None:
        """ 

`SetAttributes`(*self*, *attr*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetAttributes "Permalink to this definition")
Sets the item attributes (font, colours, etc…).



Parameters
**attr** – an instance of [`TreeItemAttr`](wx.lib.agw.customtreectrl.TreeItemAttr.html#wx.lib.agw.customtreectrl.TreeItemAttr "wx.lib.agw.customtreectrl.TreeItemAttr").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetBold(self, bold: bool) -> None:
        """ 

`SetBold`(*self*, *bold*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetBold "Permalink to this definition")
Sets the item font bold.



Parameters
**bold** (*bool*) – `True` to have a bold font item, `False` otherwise.





Note


Call [`CustomTreeCtrl.SetItemBold`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemBold "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemBold") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetData(self, data: Any) -> None:
        """ 

`SetData`(*self*, *data*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetData "Permalink to this definition")
Sets the data associated to this item.



Parameters
**data** (*object*) – can be any Python object.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHasPlus(self, has: bool=True) -> None:
        """ 

`SetHasPlus`(*self*, *has=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetHasPlus "Permalink to this definition")
Sets whether an item has the ‘plus’ button.



Parameters
**has** (*bool*) – `True` to set the ‘plus’ button on the item, `False` otherwise.





Note


Call [`CustomTreeCtrl.SetItemHasChildren`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHasChildren "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHasChildren") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHeight(self, h: int) -> None:
        """ 

`SetHeight`(*self*, *h*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetHeight "Permalink to this definition")
Sets the item’s height. Used internally.



Parameters
**h** (*integer*) – an integer specifying the item’s height, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHilight(self, set: bool=True) -> None:
        """ 

`SetHilight`(*self*, *set=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetHilight "Permalink to this definition")
Sets the item focus/unfocus.



Parameters
**set** (*bool*) – `True` to set the focus to the item, `False` otherwise.





Note


Call [`CustomTreeCtrl.SelectItem`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectItem "wx.lib.agw.customtreectrl.CustomTreeCtrl.SelectItem") instead to update the tree properly and send events.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetHyperText(self, hyper: bool=True) -> None:
        """ 

`SetHyperText`(*self*, *hyper=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetHyperText "Permalink to this definition")
Sets whether the item is hypertext or not.



Parameters
**hyper** (*bool*) – `True` to set hypertext behaviour, `False` otherwise.





Note


Call [`CustomTreeCtrl.SetItemHyperText`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHyperText "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemHyperText") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetImage(self, image, which) -> None:
        """ 

`SetImage`(*self*, *image*, *which*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetImage "Permalink to this definition")
Sets the item image.



Parameters
* **image** (*integer*) – an index within the normal image list specifying the image to use;
* **which** (*integer*) – the image kind.





See also


[`GetImage`](#wx.lib.agw.customtreectrl.GenericTreeItem.GetImage "wx.lib.agw.customtreectrl.GenericTreeItem.GetImage") for a description of the *which* parameter.




Note


Call [`CustomTreeCtrl.SetItemImage`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemImage "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemImage") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetItalic(self, italic: bool) -> None:
        """ 

`SetItalic`(*self*, *italic*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetItalic "Permalink to this definition")
Sets the item font italic.



Parameters
**italic** (*bool*) – `True` to have an italic font item, `False` otherwise.





Note


Call [`CustomTreeCtrl.SetItemItalic`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemItalic "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemItalic") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetLeftImage(self, image: int) -> None:
        """ 

`SetLeftImage`(*self*, *image*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetLeftImage "Permalink to this definition")
Sets the item leftmost image, i.e. the image associated to the item on the leftmost
part of the [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") client area.



Parameters
**image** (*integer*) – an index within the left image list specifying the image to
use for the item in the leftmost part of the client area.





Note


Call [`CustomTreeCtrl.SetItemLeftImage`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemLeftImage "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemLeftImage") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetText "Permalink to this definition")
Sets the item text.



Parameters
**text** (*string*) – the new item label.



Raise
*Exception* if the item is a separator.





Note


Call [`CustomTreeCtrl.SetItemText`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemText "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemText") to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetType(self, ct_type: int) -> None:
        """ 

`SetType`(*self*, *ct\_type*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetType "Permalink to this definition")
Sets the item type.



Parameters
**ct\_type** (*integer*) – may be one of the following integers:





| *ct\_type* Value | Description |
| --- | --- |
| 0 | A normal item |
| 1 | A checkbox-like item |
| 2 | A radiobutton-type item |








Note


Regarding radiobutton-type items (with *ct\_type* = 2), the following
approach is used:


* All peer-nodes that are radiobuttons will be mutually exclusive. In other words,
only one of a set of radiobuttons that share a common parent can be checked at
once. If a radiobutton node becomes checked, then all of its peer radiobuttons
must be unchecked.
* If a radiobutton node becomes unchecked, then all of its child nodes will become
inactive.




Note


Call [`CustomTreeCtrl.SetItemType`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemType") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetVisited(self, visited: bool=True) -> None:
        """ 

`SetVisited`(*self*, *visited=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetVisited "Permalink to this definition")
Sets whether an hypertext item was visited or not.



Parameters
**visited** (*bool*) – `True` to set a hypertext item as visited, `False` otherwise.





Note


Call [`CustomTreeCtrl.SetItemVisited`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemVisited "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemVisited") instead to refresh the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWidth(self, w: int) -> None:
        """ 

`SetWidth`(*self*, *w*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetWidth "Permalink to this definition")
Sets the item’s width. Used internally.



Parameters
**w** (*integer*) – an integer specifying the item’s width, in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWindow(self, wnd, on_the_right=True) -> None:
        """ 

`SetWindow`(*self*, *wnd*, *on\_the\_right=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetWindow "Permalink to this definition")
Sets the window associated to the item. Internal use only.



Parameters
* **wnd** – a non-toplevel window to be displayed next to the item, any
subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window").
* **on\_the\_right** (*bool*) – `True` positions the window on the right of text, `False`
on the left of text and overlapping the image. New in wxPython 4.0.4.



Raise
*Exception* if the input *item* is a separator and *wnd* is not `None`.





Note


Always use [`CustomTreeCtrl.SetItemWindow`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemWindow "wx.lib.agw.customtreectrl.CustomTreeCtrl.SetItemWindow") instead to update the tree properly.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetWindowEnabled(self, enable: bool=True) -> None:
        """ 

`SetWindowEnabled`(*self*, *enable=True*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetWindowEnabled "Permalink to this definition")
Sets whether the associated window is enabled or not.



Parameters
**enable** (*bool*) – `True` to enable the associated window, `False` to disable it.



Raise
*Exception* when the item has no associated window.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetX(self, x: int) -> None:
        """ 

`SetX`(*self*, *x*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetX "Permalink to this definition")
Sets the *x* position on an item, in logical coordinates.



Parameters
**x** (*integer*) – an integer specifying the x position of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """

    def SetY(self, y: int) -> None:
        """ 

`SetY`(*self*, *y*)[¶](#wx.lib.agw.customtreectrl.GenericTreeItem.SetY "Permalink to this definition")
Sets the *y* position on an item, in logical coordinates.



Parameters
**y** (*integer*) – an integer specifying the y position of the item.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.GenericTreeItem.html
        """



EVT_TREE_ITEM_COLLAPSING: int

class TreeEditTimer(Timer):
    """ Timer used for enabling in-place edit.


  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
    """
    def __init__(self, owner: Timer) -> None:
        """ 

`__init__`(*self*, *owner*)[¶](#wx.lib.agw.customtreectrl.TreeEditTimer.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
**owner** – the `Timer` owner (an instance of [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl")).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
        """

    def Notify(self) -> None:
        """ 

`Notify`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeEditTimer.Notify "Permalink to this definition")
The timer has expired, starts the item editing.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEditTimer.html
        """



class TreeEvent(CommandTreeEvent):
    """ [`CommandTreeEvent`](wx.lib.agw.customtreectrl.CommandTreeEvent.html#wx.lib.agw.customtreectrl.CommandTreeEvent "wx.lib.agw.customtreectrl.CommandTreeEvent") is a special class for all events associated with tree controls.



Note


Not all accessors make sense for all events, see the event descriptions below.



  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
    """
    def __init__(self, evtType, evtId, item=None, evtKey=None, point=None, label=None, **kwargs) -> None:
        """ 

`__init__`(*self*, *evtType*, *evtId*, *item=None*, *evtKey=None*, *point=None*, *label=None*, *\*\*kwargs*)[¶](#wx.lib.agw.customtreectrl.TreeEvent.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **evtType** (*integer*) – the event type;
* **evtId** (*integer*) – the event identifier;
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem");
* **evtKey** (*integer*) – a character ordinal;
* **point** – an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point");
* **label** (*string*) – a [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem") text label.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def Allow(self) -> None:
        """ 

`Allow`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeEvent.Allow "Permalink to this definition")
This is the opposite of [`Veto`](#wx.lib.agw.customtreectrl.TreeEvent.Veto "wx.lib.agw.customtreectrl.TreeEvent.Veto"): it explicitly allows the event to be processed.
For most events it is not necessary to call this method as the events are
allowed anyhow but some are forbidden by default (this will be mentioned
in the corresponding event description).




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ 

`GetNotifyEvent`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeEvent.GetNotifyEvent "Permalink to this definition")
Returns the actual `NotifyEvent`.



Returns
An instance of `NotifyEvent`.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def IsAllowed(self) -> None:
        """ 

`IsAllowed`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeEvent.IsAllowed "Permalink to this definition")
Returns `True` if the change is allowed ( [`Veto`](#wx.lib.agw.customtreectrl.TreeEvent.Veto "wx.lib.agw.customtreectrl.TreeEvent.Veto") hasn’t been called) or
`False` otherwise (if it was).




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """

    def Veto(self) -> None:
        """ 

`Veto`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeEvent.Veto "Permalink to this definition")
Prevents the change announced by this event from happening.



Note


It is in general a good idea to notify the user about the reasons
for vetoing the change because otherwise the applications behaviour (which
just refuses to do what the user wants) might be quite surprising.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeEvent.html
        """



class TreeFindTimer(Timer):
    """ Timer used to clear the [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") *\_findPrefix* attribute if no
key was pressed for a sufficiently long time.


  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
    """
    def __init__(self, owner: Timer) -> None:
        """ 

`__init__`(*self*, *owner*)[¶](#wx.lib.agw.customtreectrl.TreeFindTimer.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
**owner** – the `Timer` owner (an instance of [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl")).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
        """

    def Notify(self) -> None:
        """ 

`Notify`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeFindTimer.Notify "Permalink to this definition")
The timer has expired, clear the *\_findPrefix* attribute in [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeFindTimer.html
        """



class TreeItemAttr:
    """ Creates the item attributes (text colour, background colour and font).



Note


This class is inspired by the wxWidgets generic implementation of [`TreeItemAttr`](#wx.lib.agw.customtreectrl.TreeItemAttr "wx.lib.agw.customtreectrl.TreeItemAttr").



  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
    """
    def __init__(self, colText=wx.NullColour, colBack=wx.NullColour, colBorder=wx.NullColour, font=wx.NullFont) -> None:
        """ 

`__init__`(*self*, *colText=wx.NullColour*, *colBack=wx.NullColour*, *colBorder=wx.NullColour*, *font=wx.NullFont*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **colText** – the text colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");
* **colBack** – the tree item background colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");
* **colBorder** – the tree item border colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");
* **font** – the tree item font, an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetBackgroundColour(self) -> None:
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.GetBackgroundColour "Permalink to this definition")
Returns the attribute background colour.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetBorderColour(self) -> None:
        """ 

`GetBorderColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.GetBorderColour "Permalink to this definition")
Returns the attribute border colour.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





New in version 0.9.6.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetFont(self) -> None:
        """ 

`GetFont`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.GetFont "Permalink to this definition")
Returns the attribute font.



Returns
An instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def GetTextColour(self) -> None:
        """ 

`GetTextColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.GetTextColour "Permalink to this definition")
Returns the attribute text colour.



Returns
An instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasBackgroundColour(self) -> None:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.HasBackgroundColour "Permalink to this definition")
Returns whether the attribute has background colour.



Returns
`True` if the background colour attribute has been set, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasBorderColour(self) -> None:
        """ 

`HasBorderColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.HasBorderColour "Permalink to this definition")
Returns whether the attribute has border colour.



Returns
`True` if the border colour attribute has been set, `False` otherwise.





New in version 0.9.6.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasFont(self) -> None:
        """ 

`HasFont`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.HasFont "Permalink to this definition")
Returns whether the attribute has font.



Returns
`True` if the font attribute has been set, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def HasTextColour(self) -> None:
        """ 

`HasTextColour`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.HasTextColour "Permalink to this definition")
Returns whether the attribute has text colour.



Returns
`True` if the text colour attribute has been set, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colBack*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.SetBackgroundColour "Permalink to this definition")
Sets the item background colour attribute.



Parameters
**colBack** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetBorderColour(self, colBorder) -> None:
        """ 

`SetBorderColour`(*self*, *colBorder*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.SetBorderColour "Permalink to this definition")
Sets the item border colour attribute.



Parameters
**colBack** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").





New in version 0.9.6.





            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.SetFont "Permalink to this definition")
Sets the item font attribute.



Parameters
**font** – an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colText*)[¶](#wx.lib.agw.customtreectrl.TreeItemAttr.SetTextColour "Permalink to this definition")
Sets the text colour attribute.



Parameters
**colText** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeItemAttr.html
        """



class TreeTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.


This is a subclass of `lib.expando.ExpandoTextCtrl` as [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") supports multiline
text items.



Note


To add a newline character in a multiline item, press `Shift` + `Enter` as the `Enter`
key alone is consumed by [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") to finish the editing and `Ctrl` + `Enter` is
consumed by the platform for tab navigation.



  


        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
    """
    def __init__(self, owner, item=None) -> None:
        """ 

`__init__`(*self*, *owner*, *item=None*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **owner** – the control parent (an instance of [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl"));
* **item** – an instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").



Raise
*Exception* when the item has an associated image but the parent
[`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") does not have a [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList") assigned.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ 

`AcceptChanges`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.AcceptChanges "Permalink to this definition")
Accepts/rejects the changes made by the user.



Returns
`True` if the changes to the item text have been accepted, `False`
if they have been rejected (i.e., vetoed by the user).






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def Finish(self) -> None:
        """ 

`Finish`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.Finish "Permalink to this definition")
Finish editing.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def item(self) -> None:
        """ 

`item`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.item "Permalink to this definition")
Returns the item currently edited.



Returns
An instance of [`GenericTreeItem`](wx.lib.agw.customtreectrl.GenericTreeItem.html#wx.lib.agw.customtreectrl.GenericTreeItem "wx.lib.agw.customtreectrl.GenericTreeItem").






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.OnChar "Permalink to this definition")
Handles the `wx.EVT_CHAR` event for [`TreeTextCtrl`](#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`TreeTextCtrl`](#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`TreeTextCtrl`](#wx.lib.agw.customtreectrl.TreeTextCtrl "wx.lib.agw.customtreectrl.TreeTextCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ 

`StopEditing`(*self*)[¶](#wx.lib.agw.customtreectrl.TreeTextCtrl.StopEditing "Permalink to this definition")
Suddenly stops the editing.




            Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.TreeTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

TreeItemIcon_Normal: int

TreeItemIcon_Selected: int

TreeItemIcon_Expanded: int

TreeItemIcon_SelectedExpanded: int

TREE_HITTEST_ABOVE: int

TREE_HITTEST_BELOW: int

TREE_HITTEST_NOWHERE: int

TREE_HITTEST_ONITEMBUTTON: int

TREE_HITTEST_ONITEMICON: int

TREE_HITTEST_ONITEMINDENT: int

TREE_HITTEST_ONITEMLABEL: int

TREE_HITTEST_ONITEM: int

TREE_HITTEST_ONITEMRIGHT: int

TREE_HITTEST_TOLEFT: int

TREE_HITTEST_TORIGHT: int

TREE_HITTEST_ONITEMUPPERPART: int

TREE_HITTEST_ONITEMLOWERPART: int

TREE_HITTEST_ONITEMCHECKICON: int

