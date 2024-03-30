# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


def ChopText(dc, text, max_size) -> None:
    """ 

`ChopText`(*dc*, *text*, *max\_size*)[¶](#wx.lib.agw.customtreectrl.ChopText "Permalink to this definition")
Chops the input *text* if its size does not fit in *max\_size*, by cutting the
text and adding ellipsis at the end.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **text** – the text to chop;
* **max\_size** – the maximum size in which the text should fit.





Note


This method is used exclusively when [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_ELLIPSIZE_LONG_ITEMS`
style set.




New in version 0.9.3.





        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def DrawTreeItemButton(win, dc, rect, flags) -> None:
    """ 

`DrawTreeItemButton`(*win*, *dc*, *rect*, *flags*)[¶](#wx.lib.agw.customtreectrl.DrawTreeItemButton "Permalink to this definition")
Draw the expanded/collapsed icon for a tree control item.



Parameters
* **win** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **dc** – an instance of [`wx.DC`](wx.DC.html#wx.DC "wx.DC");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the client rectangle where to draw the tree item button;
* **flags** (*integer*) – contains `wx.CONTROL_EXPANDED` bit for expanded tree items.





Note


This is a simple replacement of `RendererNative.DrawTreeItemButton`.




Note


This method is never used in wxPython versions newer than 2.6.2.1.





        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def EventFlagsToSelType(style, shiftDown=False, ctrlDown=False) -> None:
    """ 

`EventFlagsToSelType`(*style*, *shiftDown=False*, *ctrlDown=False*)[¶](#wx.lib.agw.customtreectrl.EventFlagsToSelType "Permalink to this definition")
Translate the key or mouse event flag to the type of selection we
are dealing with.



Parameters
* **style** (*integer*) – the main [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") window style flag;
* **shiftDown** (*bool*) – `True` if the `Shift` key is pressed, `False` otherwise;
* **ctrlDown** (*bool*) – `True` if the `Ctrl` key is pressed, `False` otherwise;



Returns
A 3-elements tuple, with the following elements:


* *is\_multiple*: `True` if [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the `TR_MULTIPLE` flag set, `False` otherwise;
* *extended\_select*: `True` if the `Shift` key is pressend and if [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the
`TR_MULTIPLE` flag set, `False` otherwise;
* *unselect\_others*: `True` if the `Ctrl` key is pressend and if [`CustomTreeCtrl`](wx.lib.agw.customtreectrl.CustomTreeCtrl.html#wx.lib.agw.customtreectrl.CustomTreeCtrl "wx.lib.agw.customtreectrl.CustomTreeCtrl") has the
`TR_MULTIPLE` flag set, `False` otherwise.









        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


def MakeDisabledBitmap(original: 'Bitmap') -> None:
    """ 

`MakeDisabledBitmap`(*original*)[¶](#wx.lib.agw.customtreectrl.MakeDisabledBitmap "Permalink to this definition")
Creates a disabled-looking bitmap starting from the input one.



Parameters
**original** – an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") to be greyed-out.



Returns
An instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap"), containing a disabled-looking
representation of the original item image.






        Source: https://docs.wxpython.org/wx.lib.agw.customtreectrl.html
    """


DragImage: int

WANTS_CHARS: int

TR_NO_BUTTONS: int

TR_SINGLE: int

TR_HAS_BUTTONS: int

TR_NO_LINES: int

TR_LINES_AT_ROOT: int

TR_TWIST_BUTTONS: int

TR_MULTIPLE: int

TR_HAS_VARIABLE_ROW_HEIGHT: int

TR_EDIT_LABELS: int

TR_ROW_LINES: int

TR_HIDE_ROOT: int

TR_FULL_ROW_HIGHLIGHT: int

TR_HAS_VARIABLE_LINE_HEIGHT: int

CONTROL_EXPANDED: int

