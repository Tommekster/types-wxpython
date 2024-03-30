# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class AuiMDIClientWindow(AuiNotebook):
    """ AuiNotebook is a notebook control which implements many features common in applications with dockable panes.
Specifically, AuiNotebook implements functionality which allows the user to rearrange tab
order via drag-and-drop, split the tab window into many different splitter configurations, and toggle
through different themes to customize the control’s look and feel.


An effort has been made to try to maintain an API as similar to that of `Notebook`.


The default theme that is used is [`AuiDefaultTabArt`](wx.lib.agw.aui.tabart.AuiDefaultTabArt.html#wx.lib.agw.aui.tabart.AuiDefaultTabArt "wx.lib.agw.aui.tabart.AuiDefaultTabArt"), which provides a modern, glossy
look and feel. The theme can be changed by calling `AuiNotebook.SetArtProvider`.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
    """
    def __init__(self, parent, agwStyle=0) -> None:
        """ 

`__init__`(*self*, *parent*, *agwStyle=0*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the `AuiNotebook` parent;
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
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close `AuiNotebook` tabs by mouse middle button click |
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






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnPageChanged(self, event) -> None:
        """ 

`OnPageChanged`(*self*, *event*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.OnPageChanged "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnPageClose(self, event) -> None:
        """ 

`OnPageClose`(*self*, *event*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.OnPageClose "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for `AuiNotebook`.



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def PageChanged(self, old_selection, new_selection) -> None:
        """ 

`PageChanged`(*self*, *old\_selection*, *new\_selection*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.PageChanged "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """

    def SetSelection(self, nPage) -> None:
        """ 

`SetSelection`(*self*, *nPage*)[¶](#wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.SetSelection "Permalink to this definition")
Sets the page selection. Calling this method will generate a page change event.



Parameters
* **new\_page** (*integer*) – the index of the new selection;
* **force** (*bool*) – whether to force the selection or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabmdi.AuiMDIClientWindow.html
        """



EVT_SIZE: int

