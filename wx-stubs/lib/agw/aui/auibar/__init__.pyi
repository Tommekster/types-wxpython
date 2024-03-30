# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class AuiToolBar(Control):
    """ AuiToolBar is a completely owner-drawn toolbar perfectly integrated with the AUI layout system.
This allows drag and drop of toolbars, docking/floating behaviour and the possibility to define
“overflow” items in the toolbar itself.


The default theme that is used is [`AuiDefaultToolBarArt`](wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt"), which provides a modern,
glossy look and feel. The theme can be changed by calling [`AuiToolBar.SetArtProvider`](#wx.lib.agw.aui.auibar.AuiToolBar.SetArtProvider "wx.lib.agw.aui.auibar.AuiToolBar.SetArtProvider").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=AUI_TB_DEFAULT_STYLE) -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=AUI\_TB\_DEFAULT\_STYLE*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") parent;
* **id** (*integer*) – an identifier for the control: a value of -1 is taken to mean a default;
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the control window style;
* **agwStyle** (*integer*) – the AGW-specific window style. This can be a combination of the
following bits:







| Flag name | Description |
| --- | --- |
| `AUI_TB_TEXT` | Shows the text in the toolbar buttons; by default only icons are shown |
| `AUI_TB_NO_TOOLTIPS` | Don’t show tooltips on [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items |
| `AUI_TB_NO_AUTORESIZE` | Do not auto-resize the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_GRIPPER` | Shows a gripper on the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_OVERFLOW` | The [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") can contain overflow items |
| `AUI_TB_VERTICAL` | The [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is vertical |
| `AUI_TB_HORZ_LAYOUT` | Shows the text and the icons alongside, not vertically stacked. This style must be used with `AUI_TB_TEXT` |
| `AUI_TB_PLAIN_BACKGROUND` | Don’t draw a gradient background on the toolbar |
| `AUI_TB_HORZ_TEXT` | Combination of `AUI_TB_HORZ_LAYOUT` and `AUI_TB_TEXT` |


The default value for *agwStyle* is: `AUI_TB_DEFAULT_STYLE` = 0






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddCheckTool(self, tool_id, label, bitmap, disabled_bitmap, short_help_string="", long_help_string="", client_data=None) -> None:
        """ 

`AddCheckTool`(*self*, *tool\_id*, *label*, *bitmap*, *disabled\_bitmap*, *short\_help\_string=""*, *long\_help\_string=""*, *client\_data=None*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddCheckTool "Permalink to this definition")
Adds a new check (or toggle) tool to the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



See also


[`AddTool`](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "wx.lib.agw.aui.auibar.AuiToolBar.AddTool") for an explanation of the input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddControl(self, control, label="") -> None:
        """ 

`AddControl`(*self*, *control*, *label=""*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddControl "Permalink to this definition")
Adds any control to the toolbar, typically e.g. a `ComboBox`.



Parameters
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the control to be added;
* **label** (*string*) – the label which appears if the control goes into the
overflow items in the toolbar.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddLabel(self, tool_id, label="", width=0) -> None:
        """ 

`AddLabel`(*self*, *tool\_id*, *label=""*, *width=0*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddLabel "Permalink to this definition")
Adds a label tool to the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
* **tool\_id** (*integer*) – an integer by which the tool may be identified in subsequent operations;
* **label** (*string*) – the toolbar tool label;
* **width** (*integer*) – the tool width.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddRadioTool(self, tool_id, label, bitmap, disabled_bitmap, short_help_string="", long_help_string="", client_data=None) -> None:
        """ 

`AddRadioTool`(*self*, *tool\_id*, *label*, *bitmap*, *disabled\_bitmap*, *short\_help\_string=""*, *long\_help\_string=""*, *client\_data=None*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddRadioTool "Permalink to this definition")
Adds a new radio tool to the toolbar.


Consecutive radio tools form a radio group such that exactly one button
in the group is pressed at any moment, in other words whenever a button
in the group is pressed the previously pressed button is automatically
released. You should avoid having the radio groups of only one element
as it would be impossible for the user to use such button.



Note


By default, the first button in the radio group is initially pressed,
the others are not.




See also


[`AddTool`](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "wx.lib.agw.aui.auibar.AuiToolBar.AddTool") for an explanation of the input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSeparator(self) -> None:
        """ 

`AddSeparator`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddSeparator "Permalink to this definition")
Adds a separator for spacing groups of tools.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSimpleTool(self, tool_id, label, bitmap, short_help_string="", kind=ITEM_NORMAL, target=None) -> None:
        """ 

`AddSimpleTool`(*self*, *tool\_id*, *label*, *bitmap*, *short\_help\_string=""*, *kind=ITEM\_NORMAL*, *target=None*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddSimpleTool "Permalink to this definition")
Adds a tool to the toolbar. This is the simplest method you can use to
add an item to the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
* **tool\_id** (*integer*) – an integer by which the tool may be identified in subsequent operations;
* **label** (*string*) – the toolbar tool label;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the primary tool bitmap;
* **short\_help\_string** (*string*) – this string is used for the tools tooltip;
* **kind** (*integer*) – the item kind. Can be one of the following:





| Item Kind | Description |
| --- | --- |
| `ITEM_CONTROL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a control |
| `ITEM_LABEL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a text label |
| `ITEM_SPACER` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a spacer |
| `ITEM_SEPARATOR` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a separator |
| `ITEM_CHECK` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar check item |
| `ITEM_NORMAL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a standard toolbar item |
| `ITEM_RADIO` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar radio item |
* **target** – a custom string indicating that an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo")
has been minimized into this toolbar.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddSpacer(self, pixels: int) -> None:
        """ 

`AddSpacer`(*self*, *pixels*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddSpacer "Permalink to this definition")
Adds a spacer for spacing groups of tools.



Parameters
**pixels** (*integer*) – the width of the spacer.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddStretchSpacer(self, proportion: int=1) -> None:
        """ 

`AddStretchSpacer`(*self*, *proportion=1*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddStretchSpacer "Permalink to this definition")
Adds a stretchable spacer for spacing groups of tools.



Parameters
**proportion** (*integer*) – the stretchable spacer proportion.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddToggleTool(self, tool_id, bitmap, disabled_bitmap, toggle=False, client_data=None, short_help_string="", long_help_string="") -> None:
        """ 

`AddToggleTool`(*self*, *tool\_id*, *bitmap*, *disabled\_bitmap*, *toggle=False*, *client\_data=None*, *short\_help\_string=""*, *long\_help\_string=""*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddToggleTool "Permalink to this definition")
Adds a toggle tool to the toolbar.



Parameters
* **tool\_id** (*integer*) – an integer by which the tool may be identified in subsequent operations;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the primary tool bitmap;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to use when the tool is disabled. If it is equal to
`NullBitmap`, the disabled bitmap is automatically generated by greing the normal one;
* **client\_data** (*PyObject*) – whatever Python object to associate with the toolbar item;
* **short\_help\_string** (*string*) – this string is used for the tools tooltip;
* **long\_help\_string** (*string*) – this string is shown in the statusbar (if any) of the parent
frame when the mouse pointer is inside the tool.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def AddTool(self, tool_id, label, bitmap, disabled_bitmap, kind, short_help_string='', long_help_string='', client_data=None, target=None) -> None:
        """ 

`AddTool`(*self*, *tool\_id*, *label*, *bitmap*, *disabled\_bitmap*, *kind*, *short\_help\_string=''*, *long\_help\_string=''*, *client\_data=None*, *target=None*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "Permalink to this definition")
Adds a tool to the toolbar. This is the full feature version of [`AddTool`](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "wx.lib.agw.aui.auibar.AuiToolBar.AddTool").



Parameters
* **tool\_id** (*integer*) – an integer by which the tool may be identified in subsequent operations;
* **label** (*string*) – the toolbar tool label;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the primary tool bitmap;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to use when the tool is disabled. If it is equal to
`NullBitmap`, the disabled bitmap is automatically generated by greing the normal one;
* **kind** (*integer*) – the item kind. Can be one of the following:





| Item Kind | Description |
| --- | --- |
| `ITEM_CONTROL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a control |
| `ITEM_LABEL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a text label |
| `ITEM_SPACER` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a spacer |
| `ITEM_SEPARATOR` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a separator |
| `ITEM_CHECK` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar check item |
| `ITEM_NORMAL` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a standard toolbar item |
| `ITEM_RADIO` | The item in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar radio item |
* **short\_help\_string** (*string*) – this string is used for the tools tooltip;
* **long\_help\_string** (*string*) – this string is shown in the statusbar (if any) of the parent
frame when the mouse pointer is inside the tool.
* **client\_data** (*PyObject*) – whatever Python object to associate with the toolbar item.
* **target** – a custom string indicating that an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo")
has been minimized into this toolbar.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.Clear "Permalink to this definition")
Deletes all the tools in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def ClearTools(self) -> None:
        """ 

`ClearTools`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.ClearTools "Permalink to this definition")
Deletes all the tools in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DeleteTool(self, tool_id: int) -> None:
        """ 

`DeleteTool`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.DeleteTool "Permalink to this definition")
Removes the specified tool from the toolbar and deletes it.



Parameters
**tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier.



Returns
`True` if the tool was deleted, `False` otherwise.





Note


Note that it is unnecessary to call [`Realize`](#wx.lib.agw.aui.auibar.AuiToolBar.Realize "wx.lib.agw.aui.auibar.AuiToolBar.Realize") for the change to
take place, it will happen immediately.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DeleteToolByPos(self, pos: int) -> None:
        """ 

`DeleteToolByPos`(*self*, *pos*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.DeleteToolByPos "Permalink to this definition")
This function behaves like [`DeleteTool`](#wx.lib.agw.aui.auibar.AuiToolBar.DeleteTool "wx.lib.agw.aui.auibar.AuiToolBar.DeleteTool") but it deletes the tool at the specified position and not the one with the given id.



Parameters
**pos** (*integer*) – the tool position.





See also


[`DeleteTool`](#wx.lib.agw.aui.auibar.AuiToolBar.DeleteTool "wx.lib.agw.aui.auibar.AuiToolBar.DeleteTool")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same
size as it would have after a call to *Fit()*.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoIdleUpdate(self) -> None:
        """ 

`DoIdleUpdate`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.DoIdleUpdate "Permalink to this definition")
Updates the toolbar during idle times.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def DoSetSize(self, x, y, width, height, sizeFlags=wx.SIZE_AUTO) -> None:
        """ 

`DoSetSize`(*self*, *x*, *y*, *width*, *height*, *sizeFlags=wx.SIZE\_AUTO*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.DoSetSize "Permalink to this definition")
Sets the position and size of the window in pixels. The *sizeFlags*
parameter indicates the interpretation of the other params if they are
equal to -1.



Parameters
* **x** (*integer*) – the window *x* position;
* **y** (*integer*) – the window *y* position;
* **width** (*integer*) – the window width;
* **height** (*integer*) – the window height;
* **sizeFlags** (*integer*) – may have one of this bit set:





| Size Flags | Description |
| --- | --- |
| `wx.SIZE_AUTO` | A -1 indicates that a class-specific default should be used. |
| `wx.SIZE_AUTO_WIDTH` | A -1 indicates that a class-specific default should be used for the width. |
| `wx.SIZE_AUTO_HEIGHT` | A -1 indicates that a class-specific default should be used for the height. |
| `wx.SIZE_USE_EXISTING` | Existing dimensions should be used if -1 values are supplied. |
| `wx.SIZE_ALLOW_MINUS_ONE` | Allow dimensions of -1 and less to be interpreted as real dimensions, not default values. |
| `wx.SIZE_FORCE` | Normally, if the position and the size of the window are already the same as the parameters of this function, nothing is done. but with this flag a window resize may be forced even in this case (supported in wx 2.6.2 and later and only implemented for MSW and ignored elsewhere currently) |





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def EnableTool(self, tool_id, state) -> None:
        """ 

`EnableTool`(*self*, *tool\_id*, *state*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.EnableTool "Permalink to this definition")
Enables or disables the tool.



Parameters
* **tool\_id** (*integer*) – identifier for the tool to enable or disable.
* **state** (*bool*) – if `True`, enables the tool, otherwise disables it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindControl(self, id: int) -> None:
        """ 

`FindControl`(*self*, *id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindControl "Permalink to this definition")
Returns a pointer to the control identified by *id* or `None` if no corresponding control is found.



Parameters
**id** (*integer*) – the control identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindTool(self, tool_id: int) -> None:
        """ 

`FindTool`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindTool "Permalink to this definition")
Finds a tool for the given tool id.



Parameters
**tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolByIndex(self, pos: int) -> None:
        """ 

`FindToolByIndex`(*self*, *pos*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindToolByIndex "Permalink to this definition")
Finds a tool for the given tool position in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**pos** (*integer*) – the tool position in the toolbar.



Returns
a pointer to a [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") if a tool is found, or `None` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolByLabel(self, label: str) -> None:
        """ 

`FindToolByLabel`(*self*, *label*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindToolByLabel "Permalink to this definition")
Finds a tool for the given label.



Parameters
**label** (*string*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolForPosition(self, x, y) -> None:
        """ 

`FindToolForPosition`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindToolForPosition "Permalink to this definition")
Finds a tool for the given mouse position.



Parameters
* **x** (*integer*) – mouse *x* position;
* **y** (*integer*) – mouse *y* position.



Returns
a pointer to a [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") if a tool is found, or `None` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def FindToolForPositionWithPacking(self, x, y) -> None:
        """ 

`FindToolForPositionWithPacking`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.FindToolForPositionWithPacking "Permalink to this definition")
Finds a tool for the given mouse position, taking into account also the tool packing.



Parameters
* **x** (*integer*) – mouse *x* position;
* **y** (*integer*) – mouse *y* position.



Returns
a pointer to a [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") if a tool is found, or `None` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ 

`GetAGWWindowStyleFlag`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetAGWWindowStyleFlag "Permalink to this definition")
Returns the AGW-specific window style flag.



See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.aui.auibar.AuiToolBar.SetAGWWindowStyleFlag "wx.lib.agw.aui.auibar.AuiToolBar.SetAGWWindowStyleFlag") for an explanation of various AGW-specific style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetArtProvider(self) -> None:
        """ 

`GetArtProvider`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetArtProvider "Permalink to this definition")
Returns the current art provider being used.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetAuiManager(self) -> None:
        """ 

`GetAuiManager`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetAuiManager "Permalink to this definition")
Returns the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") which manages the toolbar.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetGripperVisible(self) -> None:
        """ 

`GetGripperVisible`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetGripperVisible "Permalink to this definition")
Returns whether the toolbar gripper is visible or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetLabelSize(self, label: str) -> None:
        """ 

`GetLabelSize`(*self*, *label*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetLabelSize "Permalink to this definition")
Returns the standard size of a toolbar item.



Parameters
**label** (*string*) – a test label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowRect(self) -> None:
        """ 

`GetOverflowRect`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetOverflowRect "Permalink to this definition")
Returns the rectangle of the overflow button.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowState(self) -> None:
        """ 

`GetOverflowState`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetOverflowState "Permalink to this definition")
Returns the state of the overflow button.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetOverflowVisible(self) -> None:
        """ 

`GetOverflowVisible`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetOverflowVisible "Permalink to this definition")
Returns whether the overflow button is visible or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBarFits(self) -> None:
        """ 

`GetToolBarFits`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolBarFits "Permalink to this definition")
Returns whether the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") size fits in a specified size.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBitmap(self, tool_id: int) -> None:
        """ 

`GetToolBitmap`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolBitmap "Permalink to this definition")
Returns the tool bitmap for the tool identified by *tool\_id*.



Parameters
**tool\_id** (*integer*) – the tool identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBitmapSize(self) -> None:
        """ 

`GetToolBitmapSize`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolBitmapSize "Permalink to this definition")
Returns the size of bitmap that the toolbar expects to have. The default bitmap size is 16 by 15 pixels.



Note


Note that this is the size of the bitmap you pass to [`AddTool`](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "wx.lib.agw.aui.auibar.AuiToolBar.AddTool"),
and not the eventual size of the tool button.




Todo


Add `ToolBar` compatibility, actually implementing this method.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolBorderPadding(self) -> None:
        """ 

`GetToolBorderPadding`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolBorderPadding "Permalink to this definition")
Returns the padding between the tool border and the label, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolCount(self) -> None:
        """ 

`GetToolCount`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolCount "Permalink to this definition")
Returns the number of tools in the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolDropDown(self, tool_id: int) -> None:
        """ 

`GetToolDropDown`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolDropDown "Permalink to this definition")
Returns whether the toolbar item identified by *tool\_id* has an associated drop down window menu or not.



Parameters
**tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolEnabled(self, tool_id: int) -> None:
        """ 

`GetToolEnabled`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolEnabled "Permalink to this definition")
Returns whether the tool identified by *tool\_id* is enabled or not.



Parameters
**tool\_id** (*integer*) – the tool identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolFits(self, tool_id: int) -> None:
        """ 

`GetToolFits`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolFits "Permalink to this definition")
Returns whether the tool identified by *tool\_id* fits into the toolbar or not.



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolFitsByIndex(self, tool_id: int) -> None:
        """ 

`GetToolFitsByIndex`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolFitsByIndex "Permalink to this definition")
Returns whether the tool identified by *tool\_id* fits into the toolbar or not.



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolIndex(self, tool_id: int) -> None:
        """ 

`GetToolIndex`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolIndex "Permalink to this definition")
Returns the position of the tool in the toolbar given its identifier.



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolLabel(self, tool_id: int) -> None:
        """ 

`GetToolLabel`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolLabel "Permalink to this definition")
Returns the tool label for the tool identified by *tool\_id*.



Parameters
**tool\_id** (*integer*) – the tool identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolLongHelp(self, tool_id: int) -> None:
        """ 

`GetToolLongHelp`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolLongHelp "Permalink to this definition")
Returns the long help for the given tool.



Parameters
**tool\_id** (*integer*) – the tool identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolOrientation(self) -> None:
        """ 

`GetToolOrientation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolOrientation "Permalink to this definition")
Returns the orientation for the toolbar items.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolPacking(self) -> None:
        """ 

`GetToolPacking`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolPacking "Permalink to this definition")
Returns the value used for spacing tools. The default value is 1 pixel.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolPos(self, tool_id: int) -> None:
        """ 

`GetToolPos`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolPos "Permalink to this definition")
Returns the position of the tool in the toolbar given its identifier.



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolProportion(self, tool_id: int) -> None:
        """ 

`GetToolProportion`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolProportion "Permalink to this definition")
Returns the tool proportion in the toolbar.



Parameters
**tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolRect(self, tool_id: int) -> None:
        """ 

`GetToolRect`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolRect "Permalink to this definition")
Returns the toolbar item rectangle



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolSeparation(self) -> None:
        """ 

`GetToolSeparation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolSeparation "Permalink to this definition")
Returns the separator size for the toolbar, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolShortHelp(self, tool_id: int) -> None:
        """ 

`GetToolShortHelp`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolShortHelp "Permalink to this definition")
Returns the short help for the given tool.



Parameters
**tool\_id** (*integer*) – the tool identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolSticky(self, tool_id: int) -> None:
        """ 

`GetToolSticky`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolSticky "Permalink to this definition")
Returns whether the toolbar item identified by *tool\_id* has a sticky behaviour or not.



Parameters
**tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolTextOrientation(self) -> None:
        """ 

`GetToolTextOrientation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolTextOrientation "Permalink to this definition")
Returns the label orientation for the toolbar items.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def GetToolToggled(self, tool_id: int) -> None:
        """ 

`GetToolToggled`(*self*, *tool\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.GetToolToggled "Permalink to this definition")
Returns whether a tool is toggled or not.



Parameters
**tool\_id** (*integer*) – the toolbar item identifier.





Note


This only applies to a tool that has been specified as a toggle tool.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.HitTest "Permalink to this definition")
Finds a tool for the given mouse position.



Parameters
* **x** (*integer*) – mouse *x* screen position;
* **y** (*integer*) – mouse *y* screen position.



Returns
a pointer to a [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") if a tool is found, or `None` otherwise.





Note


This method is similar to [`FindToolForPosition`](#wx.lib.agw.aui.auibar.AuiToolBar.FindToolForPosition "wx.lib.agw.aui.auibar.AuiToolBar.FindToolForPosition") but it works with absolute coordinates.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def IsPaneMinimized(self) -> None:
        """ 

`IsPaneMinimized`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.IsPaneMinimized "Permalink to this definition")
Returns whether this [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") contains a minimized pane tool.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnCustomRender(self, dc, item, rect) -> None:
        """ 

`OnCustomRender`(*self*, *dc*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnCustomRender "Permalink to this definition")
Handles custom render for single [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the toolbar item rect.





Note


This method must be overridden to provide custom rendering of items.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `EraseEvent` event to be processed.





Note


This is intentionally empty, to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnIdle(self, event: IdleEvent) -> None:
        """ 

`OnIdle`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnIdle "Permalink to this definition")
Handles the `wx.EVT_IDLE` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `IdleEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ 

`OnLeaveWindow`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnLeaveWindow "Permalink to this definition")
Handles the `wx.EVT_LEAVE_WINDOW` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMiddleDown(self, event: MouseEvent) -> None:
        """ 

`OnMiddleDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnMiddleDown "Permalink to this definition")
Handles the `wx.EVT_MIDDLE_DOWN` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMiddleUp(self, event: MouseEvent) -> None:
        """ 

`OnMiddleUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnMiddleUp "Permalink to this definition")
Handles the `wx.EVT_MIDDLE_UP` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnRightDown(self, event: MouseEvent) -> None:
        """ 

`OnRightDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnRightDown "Permalink to this definition")
Handles the `wx.EVT_RIGHT_DOWN` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnRightUp(self, event: MouseEvent) -> None:
        """ 

`OnRightUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnRightUp "Permalink to this definition")
Handles the `wx.EVT_RIGHT_UP` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnSetCursor(self, event: SetCursorEvent) -> None:
        """ 

`OnSetCursor`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnSetCursor "Permalink to this definition")
Handles the `wx.EVT_SET_CURSOR` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a `SetCursorEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def Realize(self) -> None:
        """ 

`Realize`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.Realize "Permalink to this definition")
Realizes the toolbar. This function should be called after you have added tools.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def RefreshOverflowState(self) -> None:
        """ 

`RefreshOverflowState`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.RefreshOverflowState "Permalink to this definition")
Refreshes the overflow button.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ 

`SetAGWWindowStyleFlag`(*self*, *agwStyle*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetAGWWindowStyleFlag "Permalink to this definition")
Sets the AGW-specific style of the window.



Parameters
**agwStyle** (*integer*) – the new window style. This can be a combination of the
following bits:







| Flag name | Description |
| --- | --- |
| `AUI_TB_TEXT` | Shows the text in the toolbar buttons; by default only icons are shown |
| `AUI_TB_NO_TOOLTIPS` | Don’t show tooltips on [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items |
| `AUI_TB_NO_AUTORESIZE` | Do not auto-resize the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_GRIPPER` | Shows a gripper on the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_OVERFLOW` | The [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") can contain overflow items |
| `AUI_TB_VERTICAL` | The [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is vertical |
| `AUI_TB_HORZ_LAYOUT` | Shows the text and the icons alongside, not vertically stacked. This style must be used with `AUI_TB_TEXT` |
| `AUI_TB_PLAIN_BACKGROUND` | Don’t draw a gradient background on the toolbar |
| `AUI_TB_HORZ_TEXT` | Combination of `AUI_TB_HORZ_LAYOUT` and `AUI_TB_TEXT` |








Note


Please note that some styles cannot be changed after the window
creation and that `Refresh` might need to be be called after changing the
others for the change to take place immediately.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetArtProvider "Permalink to this definition")
Instructs [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") to use art provider specified by parameter *art*
for all drawing calls. This allows pluggable look-and-feel features.



Parameters
**art** – an art provider.





Note


The previous art provider object, if any, will be deleted by [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetAuiManager(self, auiManager) -> None:
        """ 

`SetAuiManager`(*self*, *auiManager*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetAuiManager "Permalink to this definition")
Sets the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") which manages the toolbar.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetCustomOverflowItems(self, prepend, append) -> None:
        """ 

`SetCustomOverflowItems`(*self*, *prepend*, *append*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetCustomOverflowItems "Permalink to this definition")
Sets the two lists *prepend* and *append* as custom overflow items.



Parameters
* **prepend** (*list*) – a list of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") to be prepended;
* **append** (*list*) – a list of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") to be appended.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetFont "Permalink to this definition")
Sets the [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new toolbar font.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetGripperVisible(self, visible: bool) -> None:
        """ 

`SetGripperVisible`(*self*, *visible*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetGripperVisible "Permalink to this definition")
Sets whether the toolbar gripper is visible or not.



Parameters
**visible** (*bool*) – `True` for a visible gripper, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetHoverItem(self, pitem: AuiToolBarItem) -> None:
        """ 

`SetHoverItem`(*self*, *pitem*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetHoverItem "Permalink to this definition")
Sets a toolbar item to be currently hovered by the mouse.



Parameters
**pitem** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMargins(self, left=-1, right=-1, top=-1, bottom=-1) -> None:
        """ 

`SetMargins`(*self*, *left=-1*, *right=-1*, *top=-1*, *bottom=-1*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetMargins "Permalink to this definition")
Set the values to be used as margins for the toolbar.



Parameters
* **left** (*integer*) – the left toolbar margin;
* **right** (*integer*) – the right toolbar margin;
* **top** (*integer*) – the top toolbar margin;
* **bottom** (*integer*) – the bottom toolbar margin.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMarginsSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetMarginsSize`(*self*, *size*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetMarginsSize "Permalink to this definition")
Set the values to be used as margins for the toolbar.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the margin size (an instance of [`wx.Size`](wx.Size.html#wx.Size "wx.Size")).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetMarginsXY(self, x, y) -> None:
        """ 

`SetMarginsXY`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetMarginsXY "Permalink to this definition")
Set the values to be used as margins for the toolbar.



Parameters
* **x** (*integer*) – left margin, right margin and inter-tool separation value;
* **y** (*integer*) – top margin, bottom margin and inter-tool separation value.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetOrientation(self, orientation: int) -> None:
        """ 

`SetOrientation`(*self*, *orientation*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetOrientation "Permalink to this definition")
Sets the toolbar orientation.



Parameters
**orientation** (*integer*) – either `wx.VERTICAL` or `wx.HORIZONTAL`.





Note


This can be temporarily overridden by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") when floating and
docking a [`AuiToolBar`](#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetOverflowVisible(self, visible: bool) -> None:
        """ 

`SetOverflowVisible`(*self*, *visible*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetOverflowVisible "Permalink to this definition")
Sets whether the overflow button is visible or not.



Parameters
**visible** (*bool*) – `True` for a visible overflow button, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetPressedItem(self, pitem: AuiToolBarItem) -> None:
        """ 

`SetPressedItem`(*self*, *pitem*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetPressedItem "Permalink to this definition")
Sets a toolbar item to be currently in a “pressed” state.



Parameters
**pitem** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolAlignment(self, alignment: int=wx.EXPAND) -> None:
        """ 

`SetToolAlignment`(*self*, *alignment=wx.EXPAND*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolAlignment "Permalink to this definition")
This sets the alignment for all of the tools within the toolbar
(only has an effect when the toolbar is expanded).



Parameters
**alignment** (*integer*) – [`wx.Sizer`](wx.Sizer.html#wx.Sizer "wx.Sizer") alignment value
(`wx.ALIGN_CENTER_HORIZONTAL` or `wx.ALIGN_CENTER_VERTICAL`).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBitmap(self, tool_id, bitmap) -> None:
        """ 

`SetToolBitmap`(*self*, *tool\_id*, *bitmap*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolBitmap "Permalink to this definition")
Sets the tool bitmap for the tool identified by *tool\_id*.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new bitmap for the toolbar item.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetToolBitmapSize`(*self*, *size*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolBitmapSize "Permalink to this definition")
Sets the default size of each tool bitmap. The default bitmap size is 16 by 15 pixels.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the size of the bitmaps in the toolbar.





Note


This should be called to tell the toolbar what the tool bitmap
size is. Call it before you add tools.




Note


Note that this is the size of the bitmap you pass to [`AddTool`](#wx.lib.agw.aui.auibar.AuiToolBar.AddTool "wx.lib.agw.aui.auibar.AuiToolBar.AddTool"),
and not the eventual size of the tool button.




Todo


Add `ToolBar` compatibility, actually implementing this method.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolBorderPadding(self, padding: int) -> None:
        """ 

`SetToolBorderPadding`(*self*, *padding*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolBorderPadding "Permalink to this definition")
Sets the padding between the tool border and the label.



Parameters
**padding** (*integer*) – the padding in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolDisabledBitmap(self, tool_id, bitmap) -> None:
        """ 

`SetToolDisabledBitmap`(*self*, *tool\_id*, *bitmap*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolDisabledBitmap "Permalink to this definition")
Sets the tool disabled bitmap for the tool identified by *tool\_id*.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new disabled bitmap for the toolbar item.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolDropDown(self, tool_id, dropdown) -> None:
        """ 

`SetToolDropDown`(*self*, *tool\_id*, *dropdown*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolDropDown "Permalink to this definition")
Assigns a drop down window menu to the toolbar item.



Parameters
* **tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier;
* **dropdown** (*bool*) – whether to assign a drop down menu or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolLabel(self, tool_id, label) -> None:
        """ 

`SetToolLabel`(*self*, *tool\_id*, *label*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolLabel "Permalink to this definition")
Sets the tool label for the tool identified by *tool\_id*.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **label** (*string*) – the new toolbar item label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolLongHelp(self, tool_id, help_string) -> None:
        """ 

`SetToolLongHelp`(*self*, *tool\_id*, *help\_string*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolLongHelp "Permalink to this definition")
Sets the long help for the given tool.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **help\_string** (*string*) – the string for the long help.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolNormalBitmap(self, tool_id, bitmap) -> None:
        """ 

`SetToolNormalBitmap`(*self*, *tool\_id*, *bitmap*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolNormalBitmap "Permalink to this definition")
Sets the tool bitmap for the tool identified by *tool\_id*.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new bitmap for the toolbar item.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolOrientation(self, orientation: int) -> None:
        """ 

`SetToolOrientation`(*self*, *orientation*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolOrientation "Permalink to this definition")
Sets the tool orientation for the toolbar items.



Parameters
**orientation** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") orientation.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolPacking(self, packing: int) -> None:
        """ 

`SetToolPacking`(*self*, *packing*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolPacking "Permalink to this definition")
Sets the value used for spacing tools. The default value is 1 pixel.



Parameters
**packing** (*integer*) – the value for packing.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolProportion(self, tool_id, proportion) -> None:
        """ 

`SetToolProportion`(*self*, *tool\_id*, *proportion*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolProportion "Permalink to this definition")
Sets the tool proportion in the toolbar.



Parameters
* **tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier;
* **proportion** (*integer*) – the tool proportion in the toolbar.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolSeparation(self, separation: int) -> None:
        """ 

`SetToolSeparation`(*self*, *separation*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolSeparation "Permalink to this definition")
Sets the separator size for the toolbar.



Parameters
**separation** (*integer*) – the separator size in pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolShortHelp(self, tool_id, help_string) -> None:
        """ 

`SetToolShortHelp`(*self*, *tool\_id*, *help\_string*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolShortHelp "Permalink to this definition")
Sets the short help for the given tool.



Parameters
* **tool\_id** (*integer*) – the tool identifier;
* **help\_string** (*string*) – the string for the short help.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolSticky(self, tool_id, sticky) -> None:
        """ 

`SetToolSticky`(*self*, *tool\_id*, *sticky*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolSticky "Permalink to this definition")
Sets the toolbar item as sticky or non-sticky.



Parameters
* **tool\_id** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") identifier;
* **sticky** (*bool*) – whether the tool should be sticky or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetToolTextOrientation(self, orientation: int) -> None:
        """ 

`SetToolTextOrientation`(*self*, *orientation*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetToolTextOrientation "Permalink to this definition")
Sets the label orientation for the toolbar items.



Parameters
**orientation** (*integer*) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") label orientation.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def SetWindowStyleFlag(self, style: int) -> None:
        """ 

`SetWindowStyleFlag`(*self*, *style*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.SetWindowStyleFlag "Permalink to this definition")
Sets the style of the window.



Parameters
**style** (*integer*) – the new window style.





Note


Please note that some styles cannot be changed after the window
creation and that `Refresh` might need to be be called after changing the
others for the change to take place immediately.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def StartPreviewTimer(self) -> None:
        """ 

`StartPreviewTimer`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.StartPreviewTimer "Permalink to this definition")
Starts a timer in [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to slide-in/slide-out the minimized pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def StopPreviewTimer(self) -> None:
        """ 

`StopPreviewTimer`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.StopPreviewTimer "Permalink to this definition")
Stops a timer in [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to slide-in/slide-out the minimized pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """

    def ToggleTool(self, tool_id, state) -> None:
        """ 

`ToggleTool`(*self*, *tool\_id*, *state*)[¶](#wx.lib.agw.aui.auibar.AuiToolBar.ToggleTool "Permalink to this definition")
Toggles a tool on or off. This does not cause any event to get emitted.



Parameters
* **tool\_id** (*integer*) – tool in question.
* **state** (*bool*) – if `True`, toggles the tool on, otherwise toggles it off.





Note


This only applies to a tool that has been specified as a toggle tool.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBar.html
        """



EVT_ERASE_BACKGROUND: int

EVT_IDLE: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MIDDLE_DOWN: int

EVT_MIDDLE_UP: int

EVT_MOTION: int

EVT_PAINT: int

EVT_RIGHT_DOWN: int

EVT_RIGHT_UP: int

EVT_SET_CURSOR: int

EVT_SIZE: int

SIZE_AUTO: int

SIZE_AUTO_WIDTH: int

SIZE_AUTO_HEIGHT: int

SIZE_USE_EXISTING: int

SIZE_ALLOW_MINUS_ONE: int

SIZE_FORCE: int

VERTICAL: int

HORIZONTAL: int

ALIGN_CENTER_HORIZONTAL: int

ALIGN_CENTER_VERTICAL: int

class AuiDefaultToolBarArt:
    """ Toolbar art provider code - a tab provider provides all drawing functionality to the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").
This allows the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") to have a pluggable look-and-feel.


By default, a [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") uses an instance of this class called [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt")
which provides bitmap art and a colour scheme that is adapted to the major platforms’
look. You can either derive from that class to alter its behaviour or write a
completely new tab art class. Call [`AuiToolBar.SetArtProvider`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar.SetArtProvider "wx.lib.agw.aui.auibar.AuiToolBar.SetArtProvider") to make use this new tab art.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.Clone "Permalink to this definition")
Clones the [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt") art.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, _rect, horizontal=True) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *\_rect*, *horizontal=True*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawBackground "Permalink to this definition")
Draws a toolbar background with a gradient shading.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle;
* **horizontal** (*bool*) – `True` if the toolbar is horizontal, `False` if it is vertical.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawButton "Permalink to this definition")
Draws a toolbar item button.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawControlLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawControlLabel "Permalink to this definition")
Draws a label for a toolbar control.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawDropDownButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawDropDownButton "Permalink to this definition")
Draws a toolbar dropdown button.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ 

`DrawGripper`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawGripper "Permalink to this definition")
Draws the toolbar gripper.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawLabel "Permalink to this definition")
Draws a toolbar item label.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ 

`DrawOverflowButton`(*self*, *dc*, *wnd*, *rect*, *state*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawOverflowButton "Permalink to this definition")
Draws the overflow button for the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle;
* **state** (*integer*) – the overflow button state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, _rect) -> None:
        """ 

`DrawPlainBackground`(*self*, *dc*, *wnd*, *\_rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawPlainBackground "Permalink to this definition")
Draws a toolbar background with a plain colour.


This method contrasts with the default behaviour of the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") that
draws a background gradient and this break the window design when putting
it within a control that has margin between the borders and the toolbar
(example: put [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") within a `StaticBoxSizer` that has a plain background).



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, _rect) -> None:
        """ 

`DrawSeparator`(*self*, *dc*, *wnd*, *\_rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.DrawSeparator "Permalink to this definition")
Draws a toolbar separator.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetAGWFlags(self) -> None:
        """ 

`GetAGWFlags`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetAGWFlags "Permalink to this definition")
Returns the [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt") flags.



See also


[`SetAGWFlags`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetAGWFlags "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetAGWFlags") for more details.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetElementSize(self, element_id: int) -> None:
        """ 

`GetElementSize`(*self*, *element\_id*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetElementSize "Permalink to this definition")
Returns the size of a UI element in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
**element\_id** (*integer*) – can be one of the following:





| Element Identifier | Description |
| --- | --- |
| `AUI_TBART_SEPARATOR_SIZE` | Separator size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TBART_GRIPPER_SIZE` | Gripper size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TBART_OVERFLOW_SIZE` | Overflow button size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetFont(self) -> None:
        """ 

`GetFont`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetFont "Permalink to this definition")
Returns the [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt") font.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> None:
        """ 

`GetLabelSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetLabelSize "Permalink to this definition")
Returns the label size for a toolbar item.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetOrientation(self) -> None:
        """ 

`GetOrientation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetOrientation "Permalink to this definition")
Returns the toolbar orientation.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetTextOrientation(self) -> None:
        """ 

`GetTextOrientation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetTextOrientation "Permalink to this definition")
Returns the [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt") text orientation.



See also


[`SetTextOrientation`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetTextOrientation "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetTextOrientation") for more details.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> None:
        """ 

`GetToolSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetToolSize "Permalink to this definition")
Returns the toolbar item size.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def GetToolsPosition(self, dc, item, rect) -> None:
        """ 

`GetToolsPosition`(*self*, *dc*, *item*, *rect*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.GetToolsPosition "Permalink to this definition")
Returns the bitmap and text rectangles for a toolbar item.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **item** – an instance of [`AuiToolBarItem`](wx.lib.agw.aui.auibar.AuiToolBarItem.html#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem");
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the tool rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ 

`SetAGWFlags`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetAGWFlags "Permalink to this definition")
Sets the toolbar art flags.



Parameters
**agwFlags** (*integer*) – a combination of the following values:





| Flag name | Description |
| --- | --- |
| `AUI_TB_TEXT` | Shows the text in the toolbar buttons; by default only icons are shown |
| `AUI_TB_NO_TOOLTIPS` | Don’t show tooltips on [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items |
| `AUI_TB_NO_AUTORESIZE` | Do not auto-resize the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_GRIPPER` | Shows a gripper on the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TB_OVERFLOW` | The [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") can contain overflow items |
| `AUI_TB_VERTICAL` | The [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is vertical |
| `AUI_TB_HORZ_LAYOUT` | Shows the text and the icons alongside, not vertically stacked. This style must be used with `AUI_TB_TEXT` |
| `AUI_TB_PLAIN_BACKGROUND` | Don’t draw a gradient background on the toolbar |
| `AUI_TB_HORZ_TEXT` | Combination of `AUI_TB_HORZ_LAYOUT` and `AUI_TB_TEXT` |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetDefaultColours(self, base_colour: Optional[Union[int, str, 'Colour']]=None) -> None:
        """ 

`SetDefaultColours`(*self*, *base\_colour=None*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetDefaultColours "Permalink to this definition")
Sets the default colours, which are calculated from the given base colour.



Parameters
**base\_colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour"). If defaulted to `None`, a colour
is generated accordingly to the platform and theme.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ 

`SetElementSize`(*self*, *element\_id*, *size*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetElementSize "Permalink to this definition")
Sets the size of a UI element in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").



Parameters
* **element\_id** (*integer*) – can be one of the following:





| Element Identifier | Description |
| --- | --- |
| `AUI_TBART_SEPARATOR_SIZE` | Separator size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TBART_GRIPPER_SIZE` | Gripper size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_TBART_OVERFLOW_SIZE` | Overflow button size in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
* **size** (*integer*) – the new size of the UI element.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetFont "Permalink to this definition")
Sets the [`AuiDefaultToolBarArt`](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt "wx.lib.agw.aui.auibar.AuiDefaultToolBarArt") font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the font used for displaying toolbar item labels.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetOrientation(self, orientation: int) -> None:
        """ 

`SetOrientation`(*self*, *orientation*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetOrientation "Permalink to this definition")
Sets the toolbar tool orientation.



Parameters
**orientation** (*integer*) – one of `AUI_TBTOOL_HORIZONTAL`, `AUI_TBTOOL_VERT_CLOCKWISE` or
`AUI_TBTOOL_VERT_COUNTERCLOCKWISE`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def SetTextOrientation(self, orientation: int) -> None:
        """ 

`SetTextOrientation`(*self*, *orientation*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.SetTextOrientation "Permalink to this definition")
Sets the text orientation.



Parameters
**orientation** (*integer*) – can be one of the following constants:





| Orientation Switches | Description |
| --- | --- |
| `AUI_TBTOOL_TEXT_LEFT` | Text in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items is aligned left |
| `AUI_TBTOOL_TEXT_RIGHT` | Text in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items is aligned right |
| `AUI_TBTOOL_TEXT_TOP` | Text in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items is aligned top |
| `AUI_TBTOOL_TEXT_BOTTOM` | Text in [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") items is aligned bottom |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> None:
        """ 

`ShowDropDown`(*self*, *wnd*, *items*)[¶](#wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.ShowDropDown "Permalink to this definition")
Shows the drop down window menu for overflow items.



Parameters
* **wnd** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **items** (*list*) – a list of the overflow toolbar items.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiDefaultToolBarArt.html
        """



class AuiToolBarItem:
    """ AuiToolBarItem is a toolbar element.


It has a unique id (except for the separators which always have id = -1), the
style (telling whether it is a normal button, separator or a control), the
state (toggled or not, enabled or not) and short and long help strings. The
default implementations use the short help string for the tooltip text which
is popped up when the mouse pointer enters the tool and the long help string
for the applications status bar.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
    """
    def __init__(self, item: Optional[AuiToolBarItem]=None) -> None:
        """ 

`__init__`(*self*, *item=None*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.__init__ "Permalink to this definition")
Default class constructor.



Parameters
**item** – another instance of [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def Assign(self, c: AuiToolBarItem) -> None:
        """ 

`Assign`(*self*, *c*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.Assign "Permalink to this definition")
Assigns the properties of the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") *c* to *self*.



Parameters
**c** – another instance of [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetAlignment(self) -> None:
        """ 

`GetAlignment`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetAlignment "Permalink to this definition")
Returns the toolbar item alignment.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetBitmap(self) -> None:
        """ 

`GetBitmap`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetBitmap "Permalink to this definition")
Returns the toolbar item bitmap.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetDisabledBitmap(self) -> None:
        """ 

`GetDisabledBitmap`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetDisabledBitmap "Permalink to this definition")
Returns the toolbar item disabled bitmap.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetHoverBitmap(self) -> None:
        """ 

`GetHoverBitmap`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetHoverBitmap "Permalink to this definition")
Returns the toolbar item hover bitmap.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetId(self) -> None:
        """ 

`GetId`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetId "Permalink to this definition")
Returns the toolbar item identifier.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetKind(self) -> None:
        """ 

`GetKind`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetKind "Permalink to this definition")
Returns the toolbar item kind.


See [`SetKind`](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetKind "wx.lib.agw.aui.auibar.AuiToolBarItem.SetKind") for more details.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetLabel(self) -> None:
        """ 

`GetLabel`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetLabel "Permalink to this definition")
Returns the toolbar item label.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetLongHelp(self) -> None:
        """ 

`GetLongHelp`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetLongHelp "Permalink to this definition")
Returns the long help string for the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetMinSize(self) -> None:
        """ 

`GetMinSize`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetMinSize "Permalink to this definition")
Returns the toolbar item minimum size.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetOrientation(self) -> None:
        """ 

`GetOrientation`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetOrientation "Permalink to this definition")
Returns the toolbar tool orientation.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetProportion(self) -> None:
        """ 

`GetProportion`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetProportion "Permalink to this definition")
Returns the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") proportion in the toolbar.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetRotatedBitmap(self, disabled: bool) -> None:
        """ 

`GetRotatedBitmap`(*self*, *disabled*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetRotatedBitmap "Permalink to this definition")
Returns the correct bitmap depending on the tool orientation.



Parameters
**disabled** (*bool*) – whether to return the disabled bitmap or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetShortHelp(self) -> None:
        """ 

`GetShortHelp`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetShortHelp "Permalink to this definition")
Returns the short help string for the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetSizerItem(self) -> None:
        """ 

`GetSizerItem`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetSizerItem "Permalink to this definition")
Returns the associated sizer item.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetSpacerPixels(self) -> None:
        """ 

`GetSpacerPixels`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetSpacerPixels "Permalink to this definition")
Returns the number of pixels for a toolbar item with kind = `ITEM_SEPARATOR`.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetState(self) -> None:
        """ 

`GetState`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetState "Permalink to this definition")
Returns the toolbar item state.



See also


[`SetState`](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetState "wx.lib.agw.aui.auibar.AuiToolBarItem.SetState") for more details.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetUserData(self) -> None:
        """ 

`GetUserData`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetUserData "Permalink to this definition")
Returns the associated user data.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def GetWindow(self) -> None:
        """ 

`GetWindow`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.GetWindow "Permalink to this definition")
Returns window associated to the toolbar item.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def HasDropDown(self) -> None:
        """ 

`HasDropDown`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.HasDropDown "Permalink to this definition")
Returns whether the toolbar item has an associated dropdown menu or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def IsActive(self) -> None:
        """ 

`IsActive`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.IsActive "Permalink to this definition")
Returns whether the toolbar item is active or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def IsSticky(self) -> None:
        """ 

`IsSticky`(*self*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.IsSticky "Permalink to this definition")
Returns whether the toolbar item has a sticky behaviour or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetActive(self, b: bool) -> None:
        """ 

`SetActive`(*self*, *b*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetActive "Permalink to this definition")
Activates/deactivates the toolbar item.



Parameters
**b** (*bool*) – `True` to activate the item, `False` to deactivate it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetAlignment(self, align: int) -> None:
        """ 

`SetAlignment`(*self*, *align*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetAlignment "Permalink to this definition")
Sets the toolbar item alignment.



Parameters
**align** (*integer*) – the item alignment, which can be one of the available [`wx.Sizer`](wx.Sizer.html#wx.Sizer "wx.Sizer")
alignments.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetBitmap(self, bmp: 'Bitmap') -> None:
        """ 

`SetBitmap`(*self*, *bmp*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetBitmap "Permalink to this definition")
Sets the toolbar item bitmap.



Parameters
**bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the image associated with this [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetDisabledBitmap(self, bmp: 'Bitmap') -> None:
        """ 

`SetDisabledBitmap`(*self*, *bmp*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetDisabledBitmap "Permalink to this definition")
Sets the toolbar item disabled bitmap.



Parameters
**bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the disabled image associated with this [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetHasDropDown(self, b: bool) -> None:
        """ 

`SetHasDropDown`(*self*, *b*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetHasDropDown "Permalink to this definition")
Sets whether the toolbar item has an associated dropdown menu.



Parameters
**b** (*bool*) – `True` to set a dropdown menu, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetHoverBitmap(self, bmp: 'Bitmap') -> None:
        """ 

`SetHoverBitmap`(*self*, *bmp*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetHoverBitmap "Permalink to this definition")
Sets the toolbar item hover bitmap.



Parameters
**bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the hover image associated with this [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetId(self, new_id: int) -> None:
        """ 

`SetId`(*self*, *new\_id*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetId "Permalink to this definition")
Sets the toolbar item identifier.



Parameters
**new\_id** (*integer*) – the new tool id.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetKind(self, new_kind: int) -> None:
        """ 

`SetKind`(*self*, *new\_kind*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetKind "Permalink to this definition")
Sets the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") kind.



Parameters
**new\_kind** (*integer*) – can be one of the following items:





| Item Kind | Description |
| --- | --- |
| `ITEM_CONTROL` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a control |
| `ITEM_LABEL` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a text label |
| `ITEM_SPACER` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a spacer |
| `ITEM_SEPARATOR` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a separator |
| `ITEM_CHECK` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar check item |
| `ITEM_NORMAL` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a standard toolbar item |
| `ITEM_RADIO` | The item in the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") is a toolbar radio item |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetLabel(self, s: str) -> None:
        """ 

`SetLabel`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetLabel "Permalink to this definition")
Sets the toolbar item label.



Parameters
**s** (*string*) – the toolbar item label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetLongHelp(self, s: str) -> None:
        """ 

`SetLongHelp`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetLongHelp "Permalink to this definition")
Sets the long help string for the toolbar item. This string is shown in the
statusbar (if any) of the parent frame when the mouse pointer is inside the
tool.



Parameters
**s** (*string*) – the tool long help string.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetMinSize(self, s: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetMinSize`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetMinSize "Permalink to this definition")
Sets the toolbar item minimum size.



Parameters
**s** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the toolbar item minimum size.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetOrientation(self, a: int) -> None:
        """ 

`SetOrientation`(*self*, *a*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetOrientation "Permalink to this definition")
Sets the toolbar tool orientation.



Parameters
**a** (*integer*) – one of `AUI_TBTOOL_HORIZONTAL`, `AUI_TBTOOL_VERT_CLOCKWISE` or
`AUI_TBTOOL_VERT_COUNTERCLOCKWISE`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetProportion(self, p: int) -> None:
        """ 

`SetProportion`(*self*, *p*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetProportion "Permalink to this definition")
Sets the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem") proportion in the toolbar.



Parameters
**p** (*integer*) – the item proportion.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetShortHelp(self, s: str) -> None:
        """ 

`SetShortHelp`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetShortHelp "Permalink to this definition")
Sets the short help string for the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem"), to be displayed in a
`ToolTip` when the mouse hover over the toolbar item.



Parameters
**s** (*string*) – the tool short help string.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSizerItem(self, s: 'SizerItem') -> None:
        """ 

`SetSizerItem`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetSizerItem "Permalink to this definition")
Associates a sizer item to this toolbar item.



Parameters
**s** – an instance of [`wx.SizerItem`](wx.SizerItem.html#wx.SizerItem "wx.SizerItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSpacerPixels(self, s: int) -> None:
        """ 

`SetSpacerPixels`(*self*, *s*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetSpacerPixels "Permalink to this definition")
Sets the number of pixels for a toolbar item with kind = `ITEM_SEPARATOR`.



Parameters
**s** (*integer*) – number of pixels.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetState(self, new_state: AUI_BUTTON_STATE_NORMAL) -> None:
        """ 

`SetState`(*self*, *new\_state*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetState "Permalink to this definition")
Sets the toolbar item state.



Parameters
**new\_state** – can be one of the following states:





| Button State Constant | Description |
| --- | --- |
| `AUI_BUTTON_STATE_NORMAL` | Normal button state |
| `AUI_BUTTON_STATE_HOVER` | Hovered button state |
| `AUI_BUTTON_STATE_PRESSED` | Pressed button state |
| `AUI_BUTTON_STATE_DISABLED` | Disabled button state |
| `AUI_BUTTON_STATE_HIDDEN` | Hidden button state |
| `AUI_BUTTON_STATE_CHECKED` | Checked button state |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetSticky(self, b: bool) -> None:
        """ 

`SetSticky`(*self*, *b*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetSticky "Permalink to this definition")
Sets whether the toolbar item is sticky (permanent highlight after mouse enter)
or not.



Parameters
**b** (*bool*) – `True` to set the item as sticky, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetUserData(self, data: Any) -> None:
        """ 

`SetUserData`(*self*, *data*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetUserData "Permalink to this definition")
Associates some kind of user data to the toolbar item.



Parameters
**data** (*PyObject*) – a Python object.





Note


The user data can be any Python object.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """

    def SetWindow(self, w: 'Window') -> None:
        """ 

`SetWindow`(*self*, *w*)[¶](#wx.lib.agw.aui.auibar.AuiToolBarItem.SetWindow "Permalink to this definition")
Assigns a window to the toolbar item.



Parameters
**w** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – associate this window *w* to the [`AuiToolBarItem`](#wx.lib.agw.aui.auibar.AuiToolBarItem "wx.lib.agw.aui.auibar.AuiToolBarItem").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibar.AuiToolBarItem.html
        """



AUI_BUTTON_STATE_NORMAL: int

AUI_BUTTON_STATE_HOVER: int

AUI_BUTTON_STATE_PRESSED: int

AUI_BUTTON_STATE_DISABLED: int

AUI_BUTTON_STATE_HIDDEN: int

AUI_BUTTON_STATE_CHECKED: int

