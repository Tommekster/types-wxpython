# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class TabTextCtrl(ExpandoTextCtrl):
    """ Control used for in-place edit.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
    """
    def __init__(self, owner, tab, page_index) -> None:
        """ 

`__init__`(*self*, *owner*, *tab*, *page\_index*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.__init__ "Permalink to this definition")
Default class constructor.
For internal use: do not call it in your code!



Parameters
* **owner** – the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") owning the tab;
* **tab** – the actual [`AuiTabCtrl`](wx.lib.agw.aui.auibook.AuiTabCtrl.html#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl") tab;
* **page\_index** (*integer*) – the [`AuiTabContainer`](wx.lib.agw.aui.auibook.AuiTabContainer.html#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer") page index for the tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def AcceptChanges(self) -> None:
        """ 

`AcceptChanges`(*self*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.AcceptChanges "Permalink to this definition")
Accepts/refuses the changes made by the user.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def Finish(self) -> None:
        """ 

`Finish`(*self*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.Finish "Permalink to this definition")
Finish editing.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def item(self) -> None:
        """ 

`item`(*self*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.item "Permalink to this definition")
Returns the item currently edited.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnChar(self, event: KeyEvent) -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.OnChar "Permalink to this definition")
Handles the `wx.EVT_CHAR` event for [`TabTextCtrl`](#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` event for [`TabTextCtrl`](#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`TabTextCtrl`](#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """

    def StopEditing(self) -> None:
        """ 

`StopEditing`(*self*)[¶](#wx.lib.agw.aui.auibook.TabTextCtrl.StopEditing "Permalink to this definition")
Suddenly stops the editing.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabTextCtrl.html
        """



EVT_CHAR: int

EVT_KEY_UP: int

EVT_KILL_FOCUS: int

class AuiNotebook(Panel):
    """ AuiNotebook is a notebook control which implements many features common in applications with dockable panes.
Specifically, AuiNotebook implements functionality which allows the user to rearrange tab
order via drag-and-drop, split the tab window into many different splitter configurations, and toggle
through different themes to customize the control’s look and feel.


An effort has been made to try to maintain an API as similar to that of `Notebook`.


The default theme that is used is [`AuiDefaultTabArt`](wx.lib.agw.aui.tabart.AuiDefaultTabArt.html#wx.lib.agw.aui.tabart.AuiDefaultTabArt "wx.lib.agw.aui.tabart.AuiDefaultTabArt"), which provides a modern, glossy
look and feel. The theme can be changed by calling [`AuiNotebook.SetArtProvider`](#wx.lib.agw.aui.auibook.AuiNotebook.SetArtProvider "wx.lib.agw.aui.auibook.AuiNotebook.SetArtProvider").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=AUI_NB_DEFAULT_STYLE, name="AuiNotebook") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=AUI\_NB\_DEFAULT\_STYLE*, *name="AuiNotebook"*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") parent;
* **id** (*integer*) – an identifier for the control: a value of -1 is taken to mean a default;
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying `Panel` window style;
* **agwStyle** (*integer*) – the AGW-specific window style. This can be a combination of the following bits:





| Flag name | Description |
| --- | --- |
| `AUI_NB_TOP` | With this style, tabs are drawn along the top of the notebook |
| `AUI_NB_LEFT` | With this style, tabs are drawn along the left of the notebook. Not implemented yet. |
| `AUI_NB_RIGHT` | With this style, tabs are drawn along the right of the notebook. Not implemented yet. |
| `AUI_NB_BOTTOM` | With this style, tabs are drawn along the bottom of the notebook |
| `AUI_NB_TAB_SPLIT` | Allows the tab control to be split by dragging a tab |
| `AUI_NB_TAB_MOVE` | Allows a tab to be moved horizontally by dragging |
| `AUI_NB_TAB_EXTERNAL_MOVE` | Allows a tab to be moved to another tab control |
| `AUI_NB_TAB_FIXED_WIDTH` | With this style, all tabs have the same width |
| `AUI_NB_SCROLL_BUTTONS` | With this style, left and right scroll buttons are displayed |
| `AUI_NB_WINDOWLIST_BUTTON` | With this style, a drop-down list of windows is available |
| `AUI_NB_CLOSE_BUTTON` | With this style, a close button is available on the tab bar |
| `AUI_NB_CLOSE_ON_ACTIVE_TAB` | With this style, a close button is available on the active tab |
| `AUI_NB_CLOSE_ON_ALL_TABS` | With this style, a close button is available on all tabs |
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tabs by mouse middle button click |
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |


Default value for *agwStyle* is:
`AUI_NB_DEFAULT_STYLE` = `AUI_NB_TOP` | `AUI_NB_TAB_SPLIT` | `AUI_NB_TAB_MOVE` | `AUI_NB_SCROLL_BUTTONS` | `AUI_NB_CLOSE_ON_ACTIVE_TAB` | `AUI_NB_MIDDLE_CLICK_CLOSE` | `AUI_NB_DRAW_DND_TAB`
* **name** (*string*) – the window name.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddControlToPage(self, page_idx, control) -> None:
        """ 

`AddControlToPage`(*self*, *page\_idx*, *control*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.AddControlToPage "Permalink to this definition")
Adds a control inside a tab (not in the tab area).



Parameters
* **page\_idx** (*integer*) – the page index;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – almost any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") -derived instance to be located
inside a tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddPage(self, page, caption, select=False, bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, control=None, tooltip="") -> None:
        """ 

`AddPage`(*self*, *page*, *caption*, *select=False*, *bitmap=wx.NullBitmap*, *disabled\_bitmap=wx.NullBitmap*, *control=None*, *tooltip=""*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.AddPage "Permalink to this definition")
Adds a page. If the `select` parameter is `True`, calling this will generate a
page change event.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the page to be added;
* **caption** (*string*) – specifies the text for the new page;
* **select** (*bool*) – specifies whether the page should be selected;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to display in the enabled tab;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to display in the disabled tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – almost any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") -derived instance to be located
inside a tab;
* **tooltip** (*string*) – the tooltip to display when the mouse hovers over the tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AddTabAreaButton(self, id, location, normal_bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, name="") -> None:
        """ 

`AddTabAreaButton`(*self*, *id*, *location*, *normal\_bitmap=wx.NullBitmap*, *disabled\_bitmap=wx.NullBitmap*, *name=""*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.AddTabAreaButton "Permalink to this definition")
Adds a button in the tab area.



Parameters
* **id** (*integer*) – the button identifier. This can be one of the following:





| Button Identifier | Description |
| --- | --- |
| `AUI_BUTTON_CLOSE` | Shows a close button on the tab area |
| `AUI_BUTTON_WINDOWLIST` | Shows a window list button on the tab area |
| `AUI_BUTTON_LEFT` | Shows a left button on the tab area |
| `AUI_BUTTON_RIGHT` | Shows a right button on the tab area |
* **location** (*integer*) – the button location. Can be `wx.LEFT` or `wx.RIGHT`;
* **normal\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for an enabled tab;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for a disabled tab;
* **name** (*string*) – the button name.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AdvanceSelection(self, forward=True, wrap=True) -> None:
        """ 

`AdvanceSelection`(*self*, *forward=True*, *wrap=True*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.AdvanceSelection "Permalink to this definition")
Cycles through the tabs.



Parameters
* **forward** (*bool*) – whether to advance forward or backward;
* **wrap** (*bool*) – `True` to return to the first tab if we reach the last tab.





Note


The call to this function generates the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignImageList`(*self*, *imageList*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.AssignImageList "Permalink to this definition")
Sets the image list for the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") control.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CalculateNewSplitSize(self) -> None:
        """ 

`CalculateNewSplitSize`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.CalculateNewSplitSize "Permalink to this definition")
Calculates the size of the new split.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CalculateTabCtrlHeight(self) -> None:
        """ 

`CalculateTabCtrlHeight`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.CalculateTabCtrlHeight "Permalink to this definition")
Calculates the tab control area height.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def CloneTabAreaButtons(self) -> None:
        """ 

`CloneTabAreaButtons`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.CloneTabAreaButtons "Permalink to this definition")
Clones the tab area buttons when the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") is being split.



See also


[`AddTabAreaButton`](#wx.lib.agw.aui.auibook.AuiNotebook.AddTabAreaButton "wx.lib.agw.aui.auibook.AuiNotebook.AddTabAreaButton")




Note


Standard buttons for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") are not cloned, only custom ones.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def DeletePage(self, page_idx: int) -> None:
        """ 

`DeletePage`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.DeletePage "Permalink to this definition")
Deletes a page at the given index. Calling this method will generate a page
change event.



Parameters
**page\_idx** (*integer*) – the page index to be deleted.





Note


[`DeletePage`](#wx.lib.agw.aui.auibook.AuiNotebook.DeletePage "wx.lib.agw.aui.auibook.AuiNotebook.DeletePage") removes a tab from the multi-notebook, and destroys the window as well.




See also


[`RemovePage`](#wx.lib.agw.aui.auibook.AuiNotebook.RemovePage "wx.lib.agw.aui.auibook.AuiNotebook.RemovePage")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def Destroy(self) -> None:
        """ 

`Destroy`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.Destroy "Permalink to this definition")
Destroys the window safely.


Use this function instead of the `del` operator, since different window
classes can be destroyed differently. Frames and dialogs are not destroyed
immediately when this function is called – they are added to a list of
windows to be deleted on idle time, when all the window’s events have been
processed. This prevents problems with events being sent to non-existent windows.



Returns
`True` if the window has either been successfully deleted, or
it has been added to the list of windows pending real deletion.





Note


This method has been added to safely un-initialize the underlying
[`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") which manages the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook")
layout (i.e., tab split, re-ordering, tab floating etc…).





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def DoSizing(self) -> None:
        """ 

`DoSizing`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.DoSizing "Permalink to this definition")
Performs all sizing operations in each tab control.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EditTab(self, page_index: int) -> None:
        """ 

`EditTab`(*self*, *page\_index*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.EditTab "Permalink to this definition")
Starts the editing of an item label, sending a `EVT_AUINOTEBOOK_BEGIN_LABEL_EDIT` event.



Parameters
**page\_index** (*integer*) – the page index we want to edit.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EnableTab(self, page_idx, enable=True) -> None:
        """ 

`EnableTab`(*self*, *page\_idx*, *enable=True*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.EnableTab "Permalink to this definition")
Enables/disables a page in the notebook.



Parameters
* **page\_idx** (*integer*) – the page index;
* **enable** (*bool*) – `True` to enable the page, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def EnsureVisible(self, indx: int) -> None:
        """ 

`EnsureVisible`(*self*, *indx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.EnsureVisible "Permalink to this definition")
Ensures the input page index *indx* is visible.



Parameters
**indx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FindNextActiveTab(self, idx: int) -> None:
        """ 

`FindNextActiveTab`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.FindNextActiveTab "Permalink to this definition")
Finds the next active tab (used mainly when [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") has inactive/disabled
tabs in it).



Parameters
**idx** (*integer*) – the index of the first (most obvious) tab to check for active status;






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FindTab(self, page: AuiNotebookPage) -> None:
        """ 

`FindTab`(*self*, *page*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.FindTab "Permalink to this definition")
Finds the tab control that currently contains the window as well
as the index of the window in the tab control. It returns `True` if the
window was found, otherwise `False`.



Parameters
**page** – an instance of [`AuiNotebookPage`](wx.lib.agw.aui.auibook.AuiNotebookPage.html#wx.lib.agw.aui.auibook.AuiNotebookPage "wx.lib.agw.aui.auibook.AuiNotebookPage").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def FloatPage(self, page_index: int) -> None:
        """ 

`FloatPage`(*self*, *page\_index*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.FloatPage "Permalink to this definition")
Float the page in *page\_index* by reparenting it to a floating frame.



Parameters
**page\_index** (*integer*) – the index of the page to be floated.





Warning


When the notebook is more or less full screen, tabs cannot be dragged far
enough outside of the notebook to become floating pages.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetActiveTabCtrl(self) -> None:
        """ 

`GetActiveTabCtrl`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetActiveTabCtrl "Permalink to this definition")
Returns the active tab control. It is called to determine which control
gets new windows being added.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ 

`GetAGWWindowStyleFlag`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetAGWWindowStyleFlag "Permalink to this definition")
Returns the AGW-specific style of the window.



See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.aui.auibook.AuiNotebook.SetAGWWindowStyleFlag "wx.lib.agw.aui.auibook.AuiNotebook.SetAGWWindowStyleFlag") for a list of possible AGW-specific window styles.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetArtProvider(self) -> None:
        """ 

`GetArtProvider`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetArtProvider "Permalink to this definition")
Returns the associated art provider.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetAuiManager(self) -> None:
        """ 

`GetAuiManager`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetAuiManager "Permalink to this definition")
Returns the associated [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetCurrentPage(self) -> None:
        """ 

`GetCurrentPage`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetCurrentPage "Permalink to this definition")
Returns the currently active page (not the index), or `None` if none was selected.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetDefaultBorder(self) -> None:
        """ 

`GetDefaultBorder`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetDefaultBorder "Permalink to this definition")
Returns the default border style for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetEnabled(self, page_idx: int) -> None:
        """ 

`GetEnabled`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetEnabled "Permalink to this definition")
Returns whether the page specified by the index *page\_idx* is enabled.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetHeightForPageHeight(self, pageHeight: int) -> None:
        """ 

`GetHeightForPageHeight`(*self*, *pageHeight*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetHeightForPageHeight "Permalink to this definition")
Gets the height of the notebook for a given page height.



Parameters
**pageHeight** (*integer*) – the given page height.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetHidden(self, page_idx: int) -> None:
        """ 

`GetHidden`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetHidden "Permalink to this definition")
Returns whether the page specified by the index *page\_idx* is hidden.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetImageList(self) -> None:
        """ 

`GetImageList`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetImageList "Permalink to this definition")
Returns the associated image list (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetMinMaxTabWidth(self) -> None:
        """ 

`GetMinMaxTabWidth`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetMinMaxTabWidth "Permalink to this definition")
Returns the minimum and the maximum tab widths for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") when the
`AUI_NB_TAB_FIXED_WIDTH` style is defined.



Note


Minimum and maximum tabs widths are used only when the `AUI_NB_TAB_FIXED_WIDTH`
style is present.




See also


[`SetMinMaxTabWidth`](#wx.lib.agw.aui.auibook.AuiNotebook.SetMinMaxTabWidth "wx.lib.agw.aui.auibook.AuiNotebook.SetMinMaxTabWidth") for more information.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPage(self, page_idx: int) -> None:
        """ 

`GetPage`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPage "Permalink to this definition")
Returns the page specified by the given index.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageBitmap(self, page_idx: int) -> None:
        """ 

`GetPageBitmap`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageBitmap "Permalink to this definition")
Returns the tab bitmap for the page.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageCount(self) -> None:
        """ 

`GetPageCount`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageCount "Permalink to this definition")
Returns the number of pages in the notebook.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageImage(self, page: int) -> None:
        """ 

`GetPageImage`(*self*, *page*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageImage "Permalink to this definition")
Returns the image index for the given page.



Parameters
**page** (*integer*) – the given page for which to retrieve the image index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageIndex(self, page_wnd: 'Window') -> None:
        """ 

`GetPageIndex`(*self*, *page\_wnd*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageIndex "Permalink to this definition")
Returns the page index for the specified window. If the window is not
found in the notebook, `wx.NOT_FOUND` is returned.



Parameters
**page\_wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window we are looking for.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageInfo(self, page_idx: int) -> None:
        """ 

`GetPageInfo`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageInfo "Permalink to this definition")
Returns the [`AuiNotebookPage`](wx.lib.agw.aui.auibook.AuiNotebookPage.html#wx.lib.agw.aui.auibook.AuiNotebookPage "wx.lib.agw.aui.auibook.AuiNotebookPage") info structure specified by the given index.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageText(self, page_idx: int) -> None:
        """ 

`GetPageText`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageText "Permalink to this definition")
Returns the tab label for the page.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageTextColour(self, page_idx: int) -> None:
        """ 

`GetPageTextColour`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageTextColour "Permalink to this definition")
Returns the tab text colour for the page.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetPageTooltip(self, page_idx: int) -> None:
        """ 

`GetPageTooltip`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetPageTooltip "Permalink to this definition")
Returns the tab tooltip for the page.



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetSashDClickUnsplit(self) -> None:
        """ 

`GetSashDClickUnsplit`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetSashDClickUnsplit "Permalink to this definition")
Returns whether a splitted [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") can be unsplitted by double-clicking
on the splitter sash.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetSelection(self) -> None:
        """ 

`GetSelection`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetSelection "Permalink to this definition")
Returns the index of the currently active page, or -1 if none was selected.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetShownPageCount(self) -> None:
        """ 

`GetShownPageCount`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetShownPageCount "Permalink to this definition")
Returns the number of pages shown in the notebook.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabContainer(self) -> None:
        """ 

`GetTabContainer`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetTabContainer "Permalink to this definition")
Returns the instance of [`AuiTabContainer`](wx.lib.agw.aui.auibook.AuiTabContainer.html#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabCtrlFromPoint(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`GetTabCtrlFromPoint`(*self*, *pt*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetTabCtrlFromPoint "Permalink to this definition")
Returns the tab control at the specified point.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse location.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabCtrlHeight(self) -> None:
        """ 

`GetTabCtrlHeight`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetTabCtrlHeight "Permalink to this definition")
Returns the tab control height.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabFrameFromTabCtrl(self, tab_ctrl: AuiTabCtrl) -> None:
        """ 

`GetTabFrameFromTabCtrl`(*self*, *tab\_ctrl*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetTabFrameFromTabCtrl "Permalink to this definition")
Returns the tab frame associated with a tab control.



Parameters
**tab\_ctrl** – an instance of [`AuiTabCtrl`](wx.lib.agw.aui.auibook.AuiTabCtrl.html#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def GetTabFrameFromWindow(self, wnd: 'Window') -> None:
        """ 

`GetTabFrameFromWindow`(*self*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.GetTabFrameFromWindow "Permalink to this definition")
Returns the tab frame associated with a window.



Parameters
**wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window for which we want to locate the [`TabFrame`](wx.lib.agw.aui.auibook.TabFrame.html#wx.lib.agw.aui.auibook.TabFrame "wx.lib.agw.aui.auibook.TabFrame").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HasCloseButton(self, page_idx: int) -> None:
        """ 

`HasCloseButton`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.HasCloseButton "Permalink to this definition")
Returns whether a tab displays a close button or not.



Parameters
**page\_idx** (*integer*) – the page index.





Note


This can only be called if `AUI_NB_CLOSE_ON_ALL_TABS` is specified.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HasMultiplePages(self) -> None:
        """ 

`HasMultiplePages`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.HasMultiplePages "Permalink to this definition")
This method should be overridden to return `True` if this window has multiple pages. All
standard class with multiple pages such as `Notebook`, `Listbook` and `Treebook`
already override it to return `True` and user-defined classes with similar behaviour
should do it as well to allow the library to handle such windows appropriately.



Note


Overridden from `Panel`.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HideAllTabs(self, hidden: bool=True) -> None:
        """ 

`HideAllTabs`(*self*, *hidden=True*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.HideAllTabs "Permalink to this definition")
Hides all tabs on the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") control.



Parameters
**hidden** (*bool*) – if `True` hides all tabs.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def HidePage(self, page_idx, hidden=True) -> None:
        """ 

`HidePage`(*self*, *page\_idx*, *hidden=True*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.HidePage "Permalink to this definition")
Sets whether a page is hidden.



Parameters
* **page\_idx** (*integer*) – the page index;
* **hidden** (*bool*) – `True` to hide the page, `False` to show it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def InitNotebook(self, agwStyle: int) -> None:
        """ 

`InitNotebook`(*self*, *agwStyle*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.InitNotebook "Permalink to this definition")
Contains common initialization code called by all constructors.



Parameters
**agwStyle** (*integer*) – the notebook style.





See also


[`__init__`](#wx.lib.agw.aui.auibook.AuiNotebook.__init__ "wx.lib.agw.aui.auibook.AuiNotebook.__init__") for a list of available *agwStyle* bits.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def InsertPage(self, page_idx, page, caption, select=False, bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, control=None, tooltip="") -> None:
        """ 

`InsertPage`(*self*, *page\_idx*, *page*, *caption*, *select=False*, *bitmap=wx.NullBitmap*, *disabled\_bitmap=wx.NullBitmap*, *control=None*, *tooltip=""*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.InsertPage "Permalink to this definition")
This is similar to [`AddPage`](#wx.lib.agw.aui.auibook.AuiNotebook.AddPage "wx.lib.agw.aui.auibook.AuiNotebook.AddPage"), but allows the ability to specify the insert location.



Parameters
* **page\_idx** (*integer*) – specifies the position for the new page;
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the page to be added;
* **caption** (*string*) – specifies the text for the new page;
* **select** (*bool*) – specifies whether the page should be selected;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to display in the enabled tab;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to display in the disabled tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – almost any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") -derived instance to be located
inside a ;
* **tooltip** (*string*) – the tooltip to display when the mouse hovers over the tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def IsMouseWellOutsideWindow(self) -> None:
        """ 

`IsMouseWellOutsideWindow`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.IsMouseWellOutsideWindow "Permalink to this definition")
Returns whether the mouse is well outside the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") screen rectangle.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def IsRenamable(self, page_idx: int) -> None:
        """ 

`IsRenamable`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.IsRenamable "Permalink to this definition")
Returns whether a tab can be renamed or not.



Parameters
**page\_idx** (*integer*) – the page index.



Returns
`True` is a page can be renamed, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def LoadPerspective(self, layout: str) -> None:
        """ 

`LoadPerspective`(*self*, *layout*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.LoadPerspective "Permalink to this definition")
Loads a layout which was saved with [`SavePerspective`](#wx.lib.agw.aui.auibook.AuiNotebook.SavePerspective "wx.lib.agw.aui.auibook.AuiNotebook.SavePerspective").



Parameters
**layout** (*string*) – a string which contains a saved [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") layout.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def NotebookPreview(self, thumbnail_size: int=200) -> None:
        """ 

`NotebookPreview`(*self*, *thumbnail\_size=200*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.NotebookPreview "Permalink to this definition")
Generates a preview of all the pages in the notebook (MSW and GTK only).



Parameters
**thumbnail\_size** (*integer*) – the maximum size of every page thumbnail
(default=200 pixels).





Note


this functionality is currently unavailable on wxMAC.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnChildFocusNotebook(self, event: ChildFocusEvent) -> None:
        """ 

`OnChildFocusNotebook`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnChildFocusNotebook "Permalink to this definition")
Handles the `wx.EVT_CHILD_FOCUS` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a `ChildFocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnCloseFloatingPage(self, event: CloseEvent) -> None:
        """ 

`OnCloseFloatingPage`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnCloseFloatingPage "Permalink to this definition")
Handles the `wx.EVT_CLOSE` event for a floating page in [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a `CloseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnNavigationKeyNotebook(self, event: NavigationKeyEvent) -> None:
        """ 

`OnNavigationKeyNotebook`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnNavigationKeyNotebook "Permalink to this definition")
Handles the `wx.EVT_NAVIGATION_KEY` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a `NavigationKeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnRenameAccept(self, page_index, value) -> None:
        """ 

`OnRenameAccept`(*self*, *page\_index*, *value*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnRenameAccept "Permalink to this definition")
Called by [`TabTextCtrl`](wx.lib.agw.aui.auibook.TabTextCtrl.html#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl"), to accept the changes and to send the
`EVT_AUINOTEBOOK_END_LABEL_EDIT` event.



Parameters
* **page\_index** (*integer*) – the page index in the notebook;
* **value** (*string*) – the new label for the tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnRenameCancelled(self, page_index: int) -> None:
        """ 

`OnRenameCancelled`(*self*, *page\_index*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnRenameCancelled "Permalink to this definition")
Called by [`TabTextCtrl`](wx.lib.agw.aui.auibook.TabTextCtrl.html#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl"), to cancel the changes and to send the
`EVT_AUINOTEBOOK_END_LABEL_EDIT` event.



Parameters
**page\_index** (*integer*) – the page index in the notebook.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabBeginDrag(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabBeginDrag`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabBeginDrag "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_BEGIN_DRAG` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabBgDClick(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabBgDClick`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabBgDClick "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_BG_DCLICK` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabButton(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabButton`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabButton "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_BUTTON` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabCancelDrag(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabCancelDrag`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabCancelDrag "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_CANCEL_DRAG` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabClicked(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabClicked`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabClicked "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_PAGE_CHANGING` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabDClick(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabDClick`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabDClick "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_TAB_DCLICK` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabDragMotion(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabDragMotion`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabDragMotion "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_DRAG_MOTION` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabEndDrag(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabEndDrag`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabEndDrag "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_END_DRAG` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabMiddleDown(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabMiddleDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabMiddleDown "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabMiddleUp(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabMiddleUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabMiddleUp "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_TAB_MIDDLE_UP` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabRightDown(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabRightDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabRightDown "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_TAB_RIGHT_DOWN` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def OnTabRightUp(self, event: AuiNotebookEvent) -> None:
        """ 

`OnTabRightUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.OnTabRightUp "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_TAB_RIGHT_UP` event for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ReDockPage(self, pane: Any) -> None:
        """ 

`ReDockPage`(*self*, *pane*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.ReDockPage "Permalink to this definition")
Re-docks a floating [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tab in the original position, when possible.



Parameters
**pane** – an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveControlFromPage(self, page_idx: int) -> None:
        """ 

`RemoveControlFromPage`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.RemoveControlFromPage "Permalink to this definition")
Removes a control from a tab (not from the tab area).



Parameters
**page\_idx** (*integer*) – the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveEmptyTabFrames(self) -> None:
        """ 

`RemoveEmptyTabFrames`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.RemoveEmptyTabFrames "Permalink to this definition")
Removes all the empty tab frames.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemovePage(self, page_idx: int) -> None:
        """ 

`RemovePage`(*self*, *page\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.RemovePage "Permalink to this definition")
Removes a page, without deleting the window pointer.



Parameters
**page\_idx** (*integer*) – the page index to be removed.





Note


[`RemovePage`](#wx.lib.agw.aui.auibook.AuiNotebook.RemovePage "wx.lib.agw.aui.auibook.AuiNotebook.RemovePage") removes a tab from the multi-notebook, but does not destroy the window.




See also


[`DeletePage`](#wx.lib.agw.aui.auibook.AuiNotebook.DeletePage "wx.lib.agw.aui.auibook.AuiNotebook.DeletePage")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def RemoveTabAreaButton(self, id: int) -> None:
        """ 

`RemoveTabAreaButton`(*self*, *id*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.RemoveTabAreaButton "Permalink to this definition")
Removes a button from the tab area.



Parameters
**id** (*integer*) – the button identifier.





See also


[`AddTabAreaButton`](#wx.lib.agw.aui.auibook.AuiNotebook.AddTabAreaButton "wx.lib.agw.aui.auibook.AuiNotebook.AddTabAreaButton") for a list of button identifiers.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ReparentControl(self, control, dest_tabs) -> None:
        """ 

`ReparentControl`(*self*, *control*, *dest\_tabs*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.ReparentControl "Permalink to this definition")
Reparents a control added inside a tab.



Parameters
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – almost any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") -derived instance to be located
inside a tab;
* **dest\_tabs** – the destination [`AuiTabCtrl`](wx.lib.agw.aui.auibook.AuiTabCtrl.html#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ResetTextControl(self) -> None:
        """ 

`ResetTextControl`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.ResetTextControl "Permalink to this definition")
Called by [`TabTextCtrl`](wx.lib.agw.aui.auibook.TabTextCtrl.html#wx.lib.agw.aui.auibook.TabTextCtrl "wx.lib.agw.aui.auibook.TabTextCtrl") when it marks itself for deletion.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SavePerspective(self) -> None:
        """ 

`SavePerspective`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SavePerspective "Permalink to this definition")
Saves the entire user interface layout into an encoded string, which can then
be stored by the application (probably using `Config`). When a perspective
is restored using [`LoadPerspective`](#wx.lib.agw.aui.auibook.AuiNotebook.LoadPerspective "wx.lib.agw.aui.auibook.AuiNotebook.LoadPerspective"), the entire user interface will return
to the state it was when the perspective was saved.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ 

`SetAGWWindowStyleFlag`(*self*, *agwStyle*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetAGWWindowStyleFlag "Permalink to this definition")
Sets the AGW-specific style of the window.



Parameters
**agwStyle** (*integer*) – the new window style. This can be a combination of the following bits:





| Flag name | Description |
| --- | --- |
| `AUI_NB_TOP` | With this style, tabs are drawn along the top of the notebook |
| `AUI_NB_LEFT` | With this style, tabs are drawn along the left of the notebook. Not implemented yet. |
| `AUI_NB_RIGHT` | With this style, tabs are drawn along the right of the notebook. Not implemented yet. |
| `AUI_NB_BOTTOM` | With this style, tabs are drawn along the bottom of the notebook |
| `AUI_NB_TAB_SPLIT` | Allows the tab control to be split by dragging a tab |
| `AUI_NB_TAB_MOVE` | Allows a tab to be moved horizontally by dragging |
| `AUI_NB_TAB_EXTERNAL_MOVE` | Allows a tab to be moved to another tab control |
| `AUI_NB_TAB_FIXED_WIDTH` | With this style, all tabs have the same width |
| `AUI_NB_SCROLL_BUTTONS` | With this style, left and right scroll buttons are displayed |
| `AUI_NB_WINDOWLIST_BUTTON` | With this style, a drop-down list of windows is available |
| `AUI_NB_CLOSE_BUTTON` | With this style, a close button is available on the tab bar |
| `AUI_NB_CLOSE_ON_ACTIVE_TAB` | With this style, a close button is available on the active tab |
| `AUI_NB_CLOSE_ON_ALL_TABS` | With this style, a close button is available on all tabs |
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tabs by mouse middle button click |
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |








Note


Please note that some styles cannot be changed after the window
creation and that `Refresh` might need to be be called after changing the
others for the change to take place immediately.




Todo


Implementation of flags `AUI_NB_RIGHT` and `AUI_NB_LEFT`.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetArtProvider "Permalink to this definition")
Sets the art provider to be used by the notebook.



Parameters
**art** – an art provider.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetCloseButton(self, page_idx, hasCloseButton) -> None:
        """ 

`SetCloseButton`(*self*, *page\_idx*, *hasCloseButton*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetCloseButton "Permalink to this definition")
Sets whether a tab should display a close button or not.



Parameters
* **page\_idx** (*integer*) – the page index;
* **hasCloseButton** (*bool*) – `True` if the page displays a close button.





Note


This can only be called if `AUI_NB_CLOSE_ON_ALL_TABS` is specified.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetFont "Permalink to this definition")
Sets the tab font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their normal, un-selected state.





Note


Overridden from `Panel`.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imageList*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetImageList "Permalink to this definition")
Sets the image list for the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") control.



Parameters
**imageList** ([*wx.ImageList*](wx.ImageList.html#wx.ImageList "wx.ImageList")) – the bitmap image list to associate to [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetMeasuringFont "Permalink to this definition")
Sets the font for calculating text measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to measure tab label text extents.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetMinMaxTabWidth(self, minTabWidth, maxTabWidth) -> None:
        """ 

`SetMinMaxTabWidth`(*self*, *minTabWidth*, *maxTabWidth*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetMinMaxTabWidth "Permalink to this definition")
Sets the minimum and/or the maximum tab widths for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") when the
`AUI_NB_TAB_FIXED_WIDTH` style is defined.


Pass -1 to either *minTabWidth* or *maxTabWidth* to reset to the default tab
width behaviour for [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
* **minTabWidth** (*integer*) – the minimum allowed tab width, in pixels;
* **maxTabWidth** (*integer*) – the maximum allowed tab width, in pixels.





Note


Minimum and maximum tabs widths are used only when the `AUI_NB_TAB_FIXED_WIDTH`
style is present.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetNavigatorIcon(self, bmp: 'Bitmap') -> None:
        """ 

`SetNavigatorIcon`(*self*, *bmp*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetNavigatorIcon "Permalink to this definition")
Sets the icon used by the [`TabNavigatorWindow`](wx.lib.agw.aui.auibook.TabNavigatorWindow.html#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow").



Parameters
**bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the new bitmap for the [`TabNavigatorWindow`](wx.lib.agw.aui.auibook.TabNavigatorWindow.html#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their normal, un-selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageBitmap(self, page_idx, bitmap) -> None:
        """ 

`SetPageBitmap`(*self*, *page\_idx*, *bitmap*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetPageBitmap "Permalink to this definition")
Sets the tab bitmap for the page.



Parameters
* **page\_idx** (*integer*) – the page index;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap to display on the page tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageImage(self, page, image) -> None:
        """ 

`SetPageImage`(*self*, *page*, *image*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetPageImage "Permalink to this definition")
Sets the image index for the given page.



Parameters
* **page** (*integer*) – the page index;
* **image** (*integer*) – an index into the image list which was set with [`SetImageList`](#wx.lib.agw.aui.auibook.AuiNotebook.SetImageList "wx.lib.agw.aui.auibook.AuiNotebook.SetImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageText(self, page_idx, text) -> None:
        """ 

`SetPageText`(*self*, *page\_idx*, *text*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetPageText "Permalink to this definition")
Sets the tab label for the page.



Parameters
* **page\_idx** (*integer*) – the page index;
* **text** (*string*) – the new tab label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageTextColour(self, page_idx, colour) -> None:
        """ 

`SetPageTextColour`(*self*, *page\_idx*, *colour*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetPageTextColour "Permalink to this definition")
Sets the tab text colour for the page.



Parameters
* **page\_idx** (*integer*) – the page index;
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – the new tab label text colour.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetPageTooltip(self, page_idx, tooltip) -> None:
        """ 

`SetPageTooltip`(*self*, *page\_idx*, *tooltip*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetPageTooltip "Permalink to this definition")
Sets the tab tooltip for the page.



Parameters
* **page\_idx** (*integer*) – the page index;
* **tooltip** (*string*) – the new tooltip.



Returns
`True` if the page tooltip has been set, `False` otherwise
(for example when the input *page\_idx* is greater than the number of
pages in the notebook.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetRenamable(self, page_idx, renamable) -> None:
        """ 

`SetRenamable`(*self*, *page\_idx*, *renamable*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetRenamable "Permalink to this definition")
Sets whether a tab can be renamed via a left double-click or not.



Parameters
* **page\_idx** (*integer*) – the page index;
* **renamable** (*bool*) – `True` if the page can be renamed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSashDClickUnsplit(self, unsplit: bool=True) -> None:
        """ 

`SetSashDClickUnsplit`(*self*, *unsplit=True*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetSashDClickUnsplit "Permalink to this definition")
Sets whether to unsplit a splitted [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") when double-clicking on a sash.



Parameters
**unsplit** (*bool*) – `True` to unsplit on sash double-clicking, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetSelectedFont "Permalink to this definition")
Sets the selected tab font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelection(self, new_page, force=False) -> None:
        """ 

`SetSelection`(*self*, *new\_page*, *force=False*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetSelection "Permalink to this definition")
Sets the page selection. Calling this method will generate a page change event.



Parameters
* **new\_page** (*integer*) – the index of the new selection;
* **force** (*bool*) – whether to force the selection or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectionToPage(self, page: AuiNotebookPage) -> None:
        """ 

`SetSelectionToPage`(*self*, *page*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetSelectionToPage "Permalink to this definition")
Sets the selection based on the input page.



Parameters
**page** – an instance of [`AuiNotebookPage`](wx.lib.agw.aui.auibook.AuiNotebookPage.html#wx.lib.agw.aui.auibook.AuiNotebookPage "wx.lib.agw.aui.auibook.AuiNotebookPage").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetSelectionToWindow(self, win: 'Window') -> None:
        """ 

`SetSelectionToWindow`(*self*, *win*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetSelectionToWindow "Permalink to this definition")
Sets the selection based on the input window *win*.



Parameters
**win** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetTabCtrlHeight(self, height: int) -> None:
        """ 

`SetTabCtrlHeight`(*self*, *height*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetTabCtrlHeight "Permalink to this definition")
Sets the tab height.


By default, the tab control height is calculated by measuring the text
height and bitmap sizes on the tab captions.


Calling this method will override that calculation and set the tab control
to the specified height parameter. A call to this method will override
any call to [`SetUniformBitmapSize`](#wx.lib.agw.aui.auibook.AuiNotebook.SetUniformBitmapSize "wx.lib.agw.aui.auibook.AuiNotebook.SetUniformBitmapSize"). Specifying -1 as the height will
return the control to its default auto-sizing behaviour.



Parameters
**height** (*integer*) – the tab control area height.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def SetUniformBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetUniformBitmapSize`(*self*, *size*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.SetUniformBitmapSize "Permalink to this definition")
Ensures that all tabs will have the same height, even if some tabs don’t have bitmaps.
Passing `wx.DefaultSize` to this method will instruct the control to use dynamic tab
height, which is the default behaviour. Under the default behaviour, when a tab with a
large bitmap is added, the tab control’s height will automatically increase to accommodate
the larger bitmap.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the tab bitmap size.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def ShowWindowMenu(self) -> None:
        """ 

`ShowWindowMenu`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.ShowWindowMenu "Permalink to this definition")
Shows the window menu for the active tab control associated with this
notebook, and returns `True` if a selection was made.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def Split(self, page, direction) -> None:
        """ 

`Split`(*self*, *page*, *direction*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.Split "Permalink to this definition")
Performs a split operation programmatically.



Parameters
* **page** (*integer*) – indicates the page that will be split off. This page will also become
the active page after the split.
* **direction** (*integer*) – specifies where the pane should go, it should be one of the
following: `wx.TOP`, `wx.BOTTOM`, `wx.LEFT`, or `wx.RIGHT`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UnSplit(self) -> None:
        """ 

`UnSplit`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.UnSplit "Permalink to this definition")
Restores original view after a tab split.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UnsplitDClick(self, part, sash_size, pos) -> None:
        """ 

`UnsplitDClick`(*self*, *part*, *sash\_size*, *pos*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.UnsplitDClick "Permalink to this definition")
Unsplit the [`AuiNotebook`](#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") on sash double-click.



Parameters
* **part** – an UI part representing the sash;
* **sash\_size** (*integer*) – the sash size;
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the double-click mouse position.





Warning


Due to a bug on MSW, for disabled pages `FindWindowAtPoint`
returns the wrong window. See <http://trac.wxwidgets.org/ticket/2942>





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UpdateHintWindowSize(self) -> None:
        """ 

`UpdateHintWindowSize`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.UpdateHintWindowSize "Permalink to this definition")
Updates the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") hint window size.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """

    def UpdateTabCtrlHeight(self, force: bool=False) -> None:
        """ 

`UpdateTabCtrlHeight`(*self*, *force=False*)[¶](#wx.lib.agw.aui.auibook.AuiNotebook.UpdateTabCtrlHeight "Permalink to this definition")
[`UpdateTabCtrlHeight`](#wx.lib.agw.aui.auibook.AuiNotebook.UpdateTabCtrlHeight "wx.lib.agw.aui.auibook.AuiNotebook.UpdateTabCtrlHeight") does the actual tab resizing. It’s meant
to be used internally.



Parameters
**force** (*bool*) – `True` to force the tab art to repaint.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebook.html
        """



EVT_CHILD_FOCUS: int

EVT_CLOSE: int

EVT_NAVIGATION_KEY: int

EVT_SIZE: int

LEFT: int

RIGHT: int

NOT_FOUND: int

DefaultSize: int

TOP: int

BOTTOM: int

class AuiTabCtrl(Control,AuiTabContainer):
    """ This is an actual [`wx.Window`](wx.Window.html#wx.Window "wx.Window") - derived window which can be used as a tab control in the normal sense.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER|wx.WANTS_CHARS|wx.TAB_TRAVERSAL) -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=wx.NO\_BORDER|wx.WANTS\_CHARS|wx.TAB\_TRAVERSAL*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") parent;
* **id** (*integer*) – an identifier for the control: a value of -1 is taken to mean a default;
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the window style.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same
size as it would have after a call to *Fit()*.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def GetDefaultBorder(self) -> None:
        """ 

`GetDefaultBorder`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.GetDefaultBorder "Permalink to this definition")
Returns the default border style for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def GetPointedToTab(self) -> Any:
        """ 

`GetPointedToTab`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.GetPointedToTab "Permalink to this definition")
Returns the page at which the mouse is pointing (if any).



Return type
[`wx.Window`](wx.Window.html#wx.Window "wx.Window").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def IsDragging(self) -> None:
        """ 

`IsDragging`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.IsDragging "Permalink to this definition")
Returns whether the user is dragging a tab with the mouse or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnButton(self, event: AuiNotebookEvent) -> None:
        """ 

`OnButton`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnButton "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_BUTTON` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnCaptureLost(self, event: MouseCaptureLostEvent) -> None:
        """ 

`OnCaptureLost`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnCaptureLost "Permalink to this definition")
Handles the `wx.EVT_MOUSE_CAPTURE_LOST` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseCaptureLostEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnEnterWindow(self, event: MouseEvent) -> None:
        """ 

`OnEnterWindow`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnEnterWindow "Permalink to this definition")
Handles the `wx.EVT_ENTER_WINDOW` event fof [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `EraseEvent` event to be processed.





Note


This is intentionally empty, to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKeyDown(self, event: KeyEvent) -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnKeyDown "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKeyDown2(self, event: KeyEvent) -> None:
        """ 

`OnKeyDown2`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnKeyDown2 "Permalink to this definition")
Handles the `wx.EVT_KEY_DOWN` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `KeyEvent` event to be processed.





Deprecated since version 0.6: This implementation is now deprecated. Refer to [`OnKeyDown`](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnKeyDown "wx.lib.agw.aui.auibook.AuiTabCtrl.OnKeyDown") for the correct one.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnKillFocus(self, event: FocusEvent) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnKillFocus "Permalink to this definition")
Handles the `wx.EVT_KILL_FOCUS` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ 

`OnLeaveWindow`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnLeaveWindow "Permalink to this definition")
Handles the `wx.EVT_LEAVE_WINDOW` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftDClick(self, event: MouseEvent) -> None:
        """ 

`OnLeftDClick`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnLeftDClick "Permalink to this definition")
Handles the `wx.EVT_LEFT_DCLICK` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMiddleDown(self, event: MouseEvent) -> None:
        """ 

`OnMiddleDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnMiddleDown "Permalink to this definition")
Handles the `wx.EVT_MIDDLE_DOWN` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMiddleUp(self, event: MouseEvent) -> None:
        """ 

`OnMiddleUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnMiddleUp "Permalink to this definition")
Handles the `wx.EVT_MIDDLE_UP` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnRightDown(self, event: MouseEvent) -> None:
        """ 

`OnRightDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnRightDown "Permalink to this definition")
Handles the `wx.EVT_RIGHT_DOWN` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnRightUp(self, event: MouseEvent) -> None:
        """ 

`OnRightUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnRightUp "Permalink to this definition")
Handles the `wx.EVT_RIGHT_UP` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnSetFocus(self, event: FocusEvent) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnSetFocus "Permalink to this definition")
Handles the `wx.EVT_SET_FOCUS` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a `FocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiTabCtrl`](#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def RestartTooltipTimer(self, wnd: 'Window') -> None:
        """ 

`RestartTooltipTimer`(*self*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.RestartTooltipTimer "Permalink to this definition")
Starts a timer: when it fires, a tooltip will be shown on the notebook tab
the mouse is pointing at.



Parameters
**wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window pointed by the mouse.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def ShowTooltip(self) -> None:
        """ 

`ShowTooltip`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.ShowTooltip "Permalink to this definition")
Shows the tooltip on the tab.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """

    def StopTooltipTimer(self) -> None:
        """ 

`StopTooltipTimer`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabCtrl.StopTooltipTimer "Permalink to this definition")
Stops the timer keeping track of tooltips and mouse movements on the tab area.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabCtrl.html
        """



EVT_MOUSE_CAPTURE_LOST: int

EVT_ENTER_WINDOW: int

EVT_ERASE_BACKGROUND: int

EVT_KEY_DOWN: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DCLICK: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MIDDLE_DOWN: int

EVT_MIDDLE_UP: int

EVT_MOTION: int

EVT_PAINT: int

EVT_RIGHT_DOWN: int

EVT_RIGHT_UP: int

EVT_SET_FOCUS: int

class AuiTabContainer:
    """ AuiTabContainer is a class which contains information about each tab.
It also can render an entire tab control to a specified DC.
It’s not a window class itself, because this code will be used by
the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook"), where it is disadvantageous to have separate
windows for each tab control in the case of “docked tabs”.


A derived class, [`AuiTabCtrl`](wx.lib.agw.aui.auibook.AuiTabCtrl.html#wx.lib.agw.aui.auibook.AuiTabCtrl "wx.lib.agw.aui.auibook.AuiTabCtrl"), is an actual [`wx.Window`](wx.Window.html#wx.Window "wx.Window") - derived window
which can be used as a tab control in the normal sense.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
    """
    def __init__(self, auiNotebook: AuiNotebook) -> None:
        """ 

`__init__`(*self*, *auiNotebook*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!



Parameters
**auiNotebook** – the parent [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def AddButton(self, id, location, normal_bitmap=wx.NullBitmap, disabled_bitmap=wx.NullBitmap, name="") -> None:
        """ 

`AddButton`(*self*, *id*, *location*, *normal\_bitmap=wx.NullBitmap*, *disabled\_bitmap=wx.NullBitmap*, *name=""*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.AddButton "Permalink to this definition")
Adds a button in the tab area.



Parameters
* **id** (*integer*) – the button identifier. This can be one of the following:





| Button Identifier | Description |
| --- | --- |
| `AUI_BUTTON_CLOSE` | Shows a close button on the tab area |
| `AUI_BUTTON_WINDOWLIST` | Shows a window list button on the tab area |
| `AUI_BUTTON_LEFT` | Shows a left button on the tab area |
| `AUI_BUTTON_RIGHT` | Shows a right button on the tab area |
* **location** (*integer*) – the button location. Can be `wx.LEFT` or `wx.RIGHT`;
* **normal\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for an enabled tab;
* **disabled\_bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap for a disabled tab;
* **name** (*string*) – the button name.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def AddPage(self, page, info) -> None:
        """ 

`AddPage`(*self*, *page*, *info*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.AddPage "Permalink to this definition")
Adds a page to the tab control.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window associated with this tab;
* **info** – an instance of [`AuiNotebookPage`](wx.lib.agw.aui.auibook.AuiNotebookPage.html#wx.lib.agw.aui.auibook.AuiNotebookPage "wx.lib.agw.aui.auibook.AuiNotebookPage").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def ButtonHitTest(self, x, y, state_flags=AUI_BUTTON_STATE_HIDDEN|AUI_BUTTON_STATE_DISABLED) -> None:
        """ 

`ButtonHitTest`(*self*, *x*, *y*, *state\_flags=AUI\_BUTTON\_STATE\_HIDDEN|AUI\_BUTTON\_STATE\_DISABLED*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.ButtonHitTest "Permalink to this definition")
Tests if a button was hit.



Parameters
* **x** (*integer*) – the mouse *x* position;
* **y** (*integer*) – the mouse *y* position;
* **state\_flags** (*integer*) – the current button state (hidden, disabled, etc…).



Returns
and instance of [`AuiTabContainerButton`](wx.lib.agw.aui.auibook.AuiTabContainerButton.html#wx.lib.agw.aui.auibook.AuiTabContainerButton "wx.lib.agw.aui.auibook.AuiTabContainerButton") if a button was hit, `None` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def CloneButtons(self) -> None:
        """ 

`CloneButtons`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.CloneButtons "Permalink to this definition")
Clones the tab area buttons when the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") is being split.



See also


[`AddButton`](#wx.lib.agw.aui.auibook.AuiTabContainer.AddButton "wx.lib.agw.aui.auibook.AuiTabContainer.AddButton")




Note


Standard buttons for [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") are not cloned, only custom ones.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def DoShowHide(self) -> None:
        """ 

`DoShowHide`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.DoShowHide "Permalink to this definition")
This function shows the active window, then hides all of the other windows
(in that order).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def EnableTab(self, idx, enable=True) -> None:
        """ 

`EnableTab`(*self*, *idx*, *enable=True*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.EnableTab "Permalink to this definition")
Enables/disables a tab in the [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").



Parameters
* **idx** (*integer*) – the tab index;
* **enable** (*bool*) – `True` to enable a tab, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def FindNextActiveTab(self, idx: int) -> None:
        """ 

`FindNextActiveTab`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.FindNextActiveTab "Permalink to this definition")
Finds the next active tab in the [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").



Parameters
**idx** (*integer*) – the index of the first (most obvious) tab to check for active status;






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetActivePage(self) -> None:
        """ 

`GetActivePage`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetActivePage "Permalink to this definition")
Returns the current selected tab or `wx.NOT_FOUND` if none is selected.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetAGWFlags(self) -> None:
        """ 

`GetAGWFlags`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetAGWFlags "Permalink to this definition")
Returns the tab art flags.



See also


[`SetAGWFlags`](#wx.lib.agw.aui.auibook.AuiTabContainer.SetAGWFlags "wx.lib.agw.aui.auibook.AuiTabContainer.SetAGWFlags") for a list of possible return values.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetArtProvider(self) -> None:
        """ 

`GetArtProvider`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetArtProvider "Permalink to this definition")
Returns the current art provider being used.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetEnabled(self, idx: int) -> None:
        """ 

`GetEnabled`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetEnabled "Permalink to this definition")
Returns whether a tab is enabled or not.



Parameters
**idx** (*integer*) – the tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetHidden(self, idx: int) -> None:
        """ 

`GetHidden`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetHidden "Permalink to this definition")
Returns whether a tab is hidden or not.



Parameters
**idx** (*integer*) – the tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetIdxFromWindow(self, wnd: 'Window') -> None:
        """ 

`GetIdxFromWindow`(*self*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetIdxFromWindow "Permalink to this definition")
Returns the tab index based on the window *wnd* associated with it.



Parameters
**wnd** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPage(self, idx: int) -> None:
        """ 

`GetPage`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetPage "Permalink to this definition")
Returns the page specified by the given index.



Parameters
**idx** (*integer*) – the tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPageCount(self) -> None:
        """ 

`GetPageCount`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetPageCount "Permalink to this definition")
Returns the number of pages in the [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetPages(self) -> None:
        """ 

`GetPages`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetPages "Permalink to this definition")
Returns a list of all the pages in this [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetShownPageCount(self) -> None:
        """ 

`GetShownPageCount`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetShownPageCount "Permalink to this definition")
Returns the number of pages shown in the [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetTabOffset(self) -> None:
        """ 

`GetTabOffset`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetTabOffset "Permalink to this definition")
Returns the tab offset.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def GetWindowFromIdx(self, idx: int) -> None:
        """ 

`GetWindowFromIdx`(*self*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.GetWindowFromIdx "Permalink to this definition")
Returns the window associated with the tab with index *idx*.



Parameters
**idx** (*integer*) – the tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def HideTab(self, idx, hidden=True) -> None:
        """ 

`HideTab`(*self*, *idx*, *hidden=True*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.HideTab "Permalink to this definition")
hides/shows a tab in the [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").



Parameters
* **idx** (*integer*) – the tab index;
* **hidden** (*bool*) – `True` to hide a tab, `False` to show it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def InsertPage(self, page, info, idx) -> None:
        """ 

`InsertPage`(*self*, *page*, *info*, *idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.InsertPage "Permalink to this definition")
Inserts a page in the tab control in the position specified by *idx*.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window associated with this tab;
* **info** – an instance of [`AuiNotebookPage`](wx.lib.agw.aui.auibook.AuiNotebookPage.html#wx.lib.agw.aui.auibook.AuiNotebookPage "wx.lib.agw.aui.auibook.AuiNotebookPage");
* **idx** (*integer*) – the page insertion index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def IsTabVisible(self, tabPage, tabOffset, dc, wnd) -> None:
        """ 

`IsTabVisible`(*self*, *tabPage*, *tabOffset*, *dc*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.IsTabVisible "Permalink to this definition")
Returns whether a tab is visible or not.



Parameters
* **tabPage** (*integer*) – the tab index;
* **tabOffset** (*integer*) – the tab offset;
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def MakeTabVisible(self, tabPage, win) -> None:
        """ 

`MakeTabVisible`(*self*, *tabPage*, *win*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.MakeTabVisible "Permalink to this definition")
Make the tab visible if it wasn’t already.



Parameters
* **tabPage** (*integer*) – the tab index;
* **win** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def MovePage(self, page, new_idx) -> None:
        """ 

`MovePage`(*self*, *page*, *new\_idx*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.MovePage "Permalink to this definition")
Moves a page in a new position specified by *new\_idx*.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window associated with this tab;
* **new\_idx** (*integer*) – the new page position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def RemoveButton(self, id: int) -> None:
        """ 

`RemoveButton`(*self*, *id*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.RemoveButton "Permalink to this definition")
Removes a button from the tab area.



Parameters
**id** (*integer*) – the button identifier. See [`AddButton`](#wx.lib.agw.aui.auibook.AuiTabContainer.AddButton "wx.lib.agw.aui.auibook.AuiTabContainer.AddButton") for a list of button identifiers.





See also


[`AddButton`](#wx.lib.agw.aui.auibook.AuiTabContainer.AddButton "wx.lib.agw.aui.auibook.AuiTabContainer.AddButton")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def RemovePage(self, wnd: 'Window') -> None:
        """ 

`RemovePage`(*self*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.RemovePage "Permalink to this definition")
Removes a page from the tab control.



Parameters
**wnd** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window"), a window associated with this tab.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def Render(self, raw_dc, wnd) -> None:
        """ 

`Render`(*self*, *raw\_dc*, *wnd*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.Render "Permalink to this definition")
Renders the tab catalog to the specified [`wx.DC`](wx.DC.html#wx.DC "wx.DC").


It is a virtual function and can be overridden to provide custom drawing
capabilities.



Parameters
* **raw\_dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetActivePage(self, wndOrInt: 'Window') -> None:
        """ 

`SetActivePage`(*self*, *wndOrInt*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetActivePage "Permalink to this definition")
Sets the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") active page.



Parameters
**wndOrInt** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") or an integer specifying a tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ 

`SetAGWFlags`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetAGWFlags "Permalink to this definition")
Sets the tab art flags.



Parameters
**agwFlags** (*integer*) – a combination of the following values:





| Flag name | Description |
| --- | --- |
| `AUI_NB_TOP` | With this style, tabs are drawn along the top of the notebook |
| `AUI_NB_LEFT` | With this style, tabs are drawn along the left of the notebook. Not implemented yet |
| `AUI_NB_RIGHT` | With this style, tabs are drawn along the right of the notebook. Not implemented yet |
| `AUI_NB_BOTTOM` | With this style, tabs are drawn along the bottom of the notebook |
| `AUI_NB_TAB_SPLIT` | Allows the tab control to be split by dragging a tab |
| `AUI_NB_TAB_MOVE` | Allows a tab to be moved horizontally by dragging |
| `AUI_NB_TAB_EXTERNAL_MOVE` | Allows a tab to be moved to another tab control |
| `AUI_NB_TAB_FIXED_WIDTH` | With this style, all tabs have the same width |
| `AUI_NB_SCROLL_BUTTONS` | With this style, left and right scroll buttons are displayed |
| `AUI_NB_WINDOWLIST_BUTTON` | With this style, a drop-down list of windows is available |
| `AUI_NB_CLOSE_BUTTON` | With this style, a close button is available on the tab bar |
| `AUI_NB_CLOSE_ON_ACTIVE_TAB` | With this style, a close button is available on the active tab |
| `AUI_NB_CLOSE_ON_ALL_TABS` | With this style, a close button is available on all tabs |
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tabs by mouse middle button click |
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |








Todo


Implementation of flags `AUI_NB_RIGHT` and `AUI_NB_LEFT`.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetArtProvider(self, art: Any) -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetArtProvider "Permalink to this definition")
Instructs [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer") to use art provider specified by parameter *art*
for all drawing calls. This allows pluggable look-and-feel features.



Parameters
**art** – an art provider.





Note


The previous art provider object, if any, will be deleted by [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetMeasuringFont "Permalink to this definition")
Sets the font for calculating text measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to measure tab label text extents.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetNoneActive(self) -> None:
        """ 

`SetNoneActive`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetNoneActive "Permalink to this definition")
Sets all the tabs as inactive (non-selected).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their normal, un-selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetSelectedFont "Permalink to this definition")
Sets the selected tab font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetTabOffset(self, offset: int) -> None:
        """ 

`SetTabOffset`(*self*, *offset*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetTabOffset "Permalink to this definition")
Sets the tab offset.



Parameters
**offset** (*integer*) – the tab offset.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def SetTabRect(self, rect: 'Rect') -> None:
        """ 

`SetTabRect`(*self*, *rect*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.SetTabRect "Permalink to this definition")
Sets the tab area rectangle.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the available area for [`AuiTabContainer`](#wx.lib.agw.aui.auibook.AuiTabContainer "wx.lib.agw.aui.auibook.AuiTabContainer").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """

    def TabHitTest(self, x, y) -> None:
        """ 

`TabHitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainer.TabHitTest "Permalink to this definition")
TabHitTest() tests if a tab was hit, passing the window pointer
back if that condition was fulfilled.



Parameters
* **x** (*integer*) – the mouse *x* position;
* **y** (*integer*) – the mouse *y* position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainer.html
        """



class AuiNotebookPage:
    """ A simple class which holds information about tab captions, bitmaps and
colours.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookPage.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
        """

    def IsMultiline(self) -> None:
        """ 

`IsMultiline`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookPage.IsMultiline "Permalink to this definition")
Returns whether the tab contains multiline text.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookPage.html
        """



class TabNavigatorWindow(Dialog):
    """ This class is used to create a modal dialog that enables “Smart Tabbing”,
similar to what you would get by hitting `Alt` + `Tab` on Windows.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
    """
    def __init__(self, parent, props, centreOnMouse=False) -> None:
        """ 

`__init__`(*self*, *parent*, *props*, *centreOnMouse=False*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.__init__ "Permalink to this definition")
Default class constructor. Used internally.



Parameters
* **parent** – the [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") parent;
* **props** – the [`TabNavigatorProps`](wx.lib.agw.aui.auibook.TabNavigatorProps.html#wx.lib.agw.aui.auibook.TabNavigatorProps "wx.lib.agw.aui.auibook.TabNavigatorProps") object.
* **centreOnMouse** – popup position of the dialog at mouse cursor. Defaults to Centre.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def CloseDialog(self, returnId=wx.ID_OK) -> None:
        """ 

`CloseDialog`(*self*, *returnId=wx.ID\_OK*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.CloseDialog "Permalink to this definition")
Closes the [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") dialog, setting selection in [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def GetSelectedPage(self) -> None:
        """ 

`GetSelectedPage`(*self*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.GetSelectedPage "Permalink to this definition")
Gets the page index that was selected when the dialog was closed.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnItemSelected(self, event: ListEvent) -> None:
        """ 

`OnItemSelected`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnItemSelected "Permalink to this definition")
Handles the `wx.EVT_LISTBOX_DCLICK` event for the `ListBox` inside [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow").



Parameters
**event** – a `ListEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` for the [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for self.\_panel.



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for self.\_panel.



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for self.\_panel.



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ 

`OnNavigationKey`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnNavigationKey "Permalink to this definition")
Handles the `wx.EVT_NAVIGATION_KEY` for the [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow").



Parameters
**event** – a `NavigationKeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnPanelEraseBg(self, event: EraseEvent) -> None:
        """ 

`OnPanelEraseBg`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnPanelEraseBg "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") top panel.



Parameters
**event** – a `EraseEvent` event to be processed.





Note


This is intentionally empty, to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def OnPanelPaint(self, event: PaintEvent) -> None:
        """ 

`OnPanelPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.OnPanelPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") top panel.



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """

    def PopulateListControl(self, book: AuiNotebook) -> None:
        """ 

`PopulateListControl`(*self*, *book*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorWindow.PopulateListControl "Permalink to this definition")
Populates the [`TabNavigatorWindow`](#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") listbox with a list of tabs.



Parameters
**book** – the actual [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorWindow.html
        """



EVT_LISTBOX_DCLICK: int

class TabFrame(Window):
    """ TabFrame is an interesting case. It’s important that all child pages
of the multi-notebook control are all actually children of that control
(and not grandchildren). TabFrame facilitates this. There is one
instance of TabFrame for each tab control inside the multi-notebook.


It’s important to know that TabFrame is not a real window, but it merely
used to capture the dimensions/positioning of the internal tab control and
it’s managed page windows.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
    """
    def __init__(self, parent) -> None:
        """ 

`__init__`(*self*, *parent*)[¶](#wx.lib.agw.aui.auibook.TabFrame.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoGetClientSize(self) -> None:
        """ 

`DoGetClientSize`(*self*)[¶](#wx.lib.agw.aui.auibook.TabFrame.DoGetClientSize "Permalink to this definition")
Returns the window client size.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoGetSize(self) -> None:
        """ 

`DoGetSize`(*self*)[¶](#wx.lib.agw.aui.auibook.TabFrame.DoGetSize "Permalink to this definition")
Returns the window size.



Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoSetSize(self, x, y, width, height, flags=wx.SIZE_AUTO) -> None:
        """ 

`DoSetSize`(*self*, *x*, *y*, *width*, *height*, *flags=wx.SIZE\_AUTO*)[¶](#wx.lib.agw.aui.auibook.TabFrame.DoSetSize "Permalink to this definition")
Sets the position and size of the window in pixels. The *flags*
parameter indicates the interpretation of the other params if they are
equal to -1.



Parameters
* **x** (*integer*) – the window *x* position;
* **y** (*integer*) – the window *y* position;
* **width** (*integer*) – the window width;
* **height** (*integer*) – the window height;
* **flags** (*integer*) – may have one of this bit set:





| Size Flags | Description |
| --- | --- |
| `wx.SIZE_AUTO` | A -1 indicates that a class-specific default should be used. |
| `wx.SIZE_AUTO_WIDTH` | A -1 indicates that a class-specific default should be used for the width. |
| `wx.SIZE_AUTO_HEIGHT` | A -1 indicates that a class-specific default should be used for the height. |
| `wx.SIZE_USE_EXISTING` | Existing dimensions should be used if -1 values are supplied. |
| `wx.SIZE_ALLOW_MINUS_ONE` | Allow dimensions of -1 and less to be interpreted as real dimensions, not default values. |
| `wx.SIZE_FORCE` | Normally, if the position and the size of the window are already the same as the parameters of this function, nothing is done. but with this flag a window resize may be forced even in this case (supported in wx 2.6.2 and later and only implemented for MSW and ignored elsewhere currently) |





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def DoSizing(self) -> None:
        """ 

`DoSizing`(*self*)[¶](#wx.lib.agw.aui.auibook.TabFrame.DoSizing "Permalink to this definition")
Does the actual sizing of the tab control.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def SetTabCtrlHeight(self, h: int) -> None:
        """ 

`SetTabCtrlHeight`(*self*, *h*)[¶](#wx.lib.agw.aui.auibook.TabFrame.SetTabCtrlHeight "Permalink to this definition")
Sets the tab control height.



Parameters
**h** (*integer*) – the tab area height.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def Show(self, show: bool=True) -> None:
        """ 

`Show`(*self*, *show=True*)[¶](#wx.lib.agw.aui.auibook.TabFrame.Show "Permalink to this definition")
Shows/hides the window.



Parameters
**show** (*bool*) – `True` to show the window, `False` otherwise.





Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control"), this method always returns `False` as
[`TabFrame`](#wx.lib.agw.aui.auibook.TabFrame "wx.lib.agw.aui.auibook.TabFrame") should never be phisically shown on screen.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """

    def Update(self) -> None:
        """ 

`Update`(*self*)[¶](#wx.lib.agw.aui.auibook.TabFrame.Update "Permalink to this definition")
Calling this method immediately repaints the invalidated area of the window
and all of its children recursively while this would usually only happen when
the flow of control returns to the event loop.



Note


Notice that this function doesn’t invalidate any area of the window so
nothing happens if nothing has been invalidated (i.e. marked as requiring a redraw).
Use `Refresh` first if you want to immediately redraw the window unconditionally.




Note


Overridden from [`wx.Control`](wx.Control.html#wx.Control "wx.Control").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabFrame.html
        """



SIZE_AUTO: int

SIZE_AUTO_WIDTH: int

SIZE_AUTO_HEIGHT: int

SIZE_USE_EXISTING: int

SIZE_ALLOW_MINUS_ONE: int

SIZE_FORCE: int

class AuiNotebookEvent(CommandNotebookEvent):
    """ A specialized command event class for events sent by [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
    """
    def __init__(self, command_type=None, win_id=0) -> None:
        """ 

`__init__`(*self*, *command\_type=None*, *win\_id=0*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookEvent.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **command\_type** – the event kind or an instance of `PyCommandEvent`.
* **win\_id** (*integer*) – the window identification number.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def Allow(self) -> None:
        """ 

`Allow`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookEvent.Allow "Permalink to this definition")
This is the opposite of [`Veto`](#wx.lib.agw.aui.auibook.AuiNotebookEvent.Veto "wx.lib.agw.aui.auibook.AuiNotebookEvent.Veto"): it explicitly allows the event to be
processed. For most events it is not necessary to call this method as the
events are allowed anyhow but some are forbidden by default (this will
be mentioned in the corresponding event description).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def GetNotifyEvent(self) -> None:
        """ 

`GetNotifyEvent`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookEvent.GetNotifyEvent "Permalink to this definition")
Returns the actual `NotifyEvent`.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def IsAllowed(self) -> None:
        """ 

`IsAllowed`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookEvent.IsAllowed "Permalink to this definition")
Returns whether the event is allowed or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """

    def Veto(self) -> None:
        """ 

`Veto`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiNotebookEvent.Veto "Permalink to this definition")
Prevents the change announced by this event from happening.


It is in general a good idea to notify the user about the reasons for
vetoing the change because otherwise the applications behaviour (which
just refuses to do what the user wants) might be quite surprising.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiNotebookEvent.html
        """



class AuiTabContainerButton:
    """ A simple class which holds information about tab buttons and their state.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainerButton.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.auibook.AuiTabContainerButton.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.AuiTabContainerButton.html
        """



class TabNavigatorProps:
    """ Data storage class for managing and providing access to [`TabNavigatorWindow`](wx.lib.agw.aui.auibook.TabNavigatorWindow.html#wx.lib.agw.aui.auibook.TabNavigatorWindow "wx.lib.agw.aui.auibook.TabNavigatorWindow") properties.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorProps.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.auibook.TabNavigatorProps.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.TabNavigatorProps.html
        """

    Font: Any  # `Font`[¶](#wx.lib.agw.aui.auibook.TabNavigatorProps.Font "Permalink to this definition")Sets/Gets the font for the L{TabNavigatorWindow}, an instance of [`wx.Font`](wx.Font.html#wx.Font "wx.Font").
    Icon: Any  # `Icon`[¶](#wx.lib.agw.aui.auibook.TabNavigatorProps.Icon "Permalink to this definition")Sets/Gets the icon for the L{TabNavigatorWindow}, an instance of [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap").
    MinSize: Any  # `MinSize`[¶](#wx.lib.agw.aui.auibook.TabNavigatorProps.MinSize "Permalink to this definition")Sets/Gets the minimum size for the L{TabNavigatorWindow}, an instance of [`wx.Size`](wx.Size.html#wx.Size "wx.Size").



class CommandNotebookEvent(PyCommandEvent):
    """ A specialized command event class for events sent by [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") .


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
    """
    def __init__(self, command_type=None, win_id=0) -> None:
        """ 

`__init__`(*self*, *command\_type=None*, *win\_id=0*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **command\_type** – the event kind or an instance of `PyCommandEvent`.
* **win\_id** (*integer*) – the window identification number.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetDispatched(self) -> None:
        """ 

`GetDispatched`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.GetDispatched "Permalink to this definition")
Returns whether the event was dispatched (used for automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") ).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetDragSource(self) -> None:
        """ 

`GetDragSource`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.GetDragSource "Permalink to this definition")
Returns the drag and drop source.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetLabel(self) -> None:
        """ 

`GetLabel`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.GetLabel "Permalink to this definition")
Returns the label-itemtext (for `EVT_AUINOTEBOOK_BEGIN` | `END_LABEL_EDIT` only).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetOldSelection(self) -> None:
        """ 

`GetOldSelection`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.GetOldSelection "Permalink to this definition")
Returns the page that was selected before the change, or -1 if none was
selected.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def GetSelection(self) -> None:
        """ 

`GetSelection`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.GetSelection "Permalink to this definition")
Returns the currently selected page, or -1 if none was selected.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def IsEditCancelled(self) -> None:
        """ 

`IsEditCancelled`(*self*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.IsEditCancelled "Permalink to this definition")
Returns the edit cancel flag (for `EVT_AUINOTEBOOK_BEGIN` | `END_LABEL_EDIT` only).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetDispatched(self, b: Any) -> None:
        """ 

`SetDispatched`(*self*, *b*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetDispatched "Permalink to this definition")
Sets the event as dispatched (used for automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") ).



Parameters
**b** – whether the event was dispatched or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetDragSource(self, s: Any) -> None:
        """ 

`SetDragSource`(*self*, *s*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetDragSource "Permalink to this definition")
Sets the drag and drop source.



Parameters
**s** – the drag source.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetEditCanceled(self, editCancelled: bool) -> None:
        """ 

`SetEditCanceled`(*self*, *editCancelled*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetEditCanceled "Permalink to this definition")
Sets the edit cancel flag (for `EVT_AUINOTEBOOK_BEGIN` | `END_LABEL_EDIT` only).



Parameters
**editCancelled** (*bool*) – whether the editing action has been cancelled or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetLabel "Permalink to this definition")
Sets the label. Useful only for `EVT_AUINOTEBOOK_END_LABEL_EDIT`.



Parameters
**label** (*string*) – the new label.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetOldSelection(self, s: int) -> None:
        """ 

`SetOldSelection`(*self*, *s*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetOldSelection "Permalink to this definition")
Sets the id of the page selected before the change.



Parameters
**s** (*integer*) – the old selection.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """

    def SetSelection(self, s: int) -> None:
        """ 

`SetSelection`(*self*, *s*)[¶](#wx.lib.agw.aui.auibook.CommandNotebookEvent.SetSelection "Permalink to this definition")
Sets the selection member variable.



Parameters
**s** (*integer*) – the new selection.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.auibook.CommandNotebookEvent.html
        """



