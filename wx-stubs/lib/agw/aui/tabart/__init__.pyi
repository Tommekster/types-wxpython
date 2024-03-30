# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class AuiDefaultTabArt:
    """ Tab art provider code - a tab provider provides all drawing functionality to the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").
This allows the [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") to have a pluggable look-and-feel.


By default, a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") uses an instance of this class called
[`AuiDefaultTabArt`](#wx.lib.agw.aui.tabart.AuiDefaultTabArt "wx.lib.agw.aui.tabart.AuiDefaultTabArt") which provides bitmap art and a colour scheme that is adapted to the major platforms’
look. You can either derive from that class to alter its behaviour or write a
completely new tab art class. Call `AuiNotebook.SetArtProvider()` to make use this
new tab art.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.Clone "Permalink to this definition")
Clones the art object.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.DrawBackground "Permalink to this definition")
Draws the tab area background.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the tab control rectangle.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, button, orientation) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *in\_rect*, *button*, *orientation*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.DrawButton "Permalink to this definition")
Draws a button on the tab or on the tab area, depending on the button identifier.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **button** – an instance of the button class;
* **orientation** (*integer*) – the tab orientation.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawFocusRectangle(self, dc, page, wnd, draw_text, text_offset, bitmap_offset, drawn_tab_yoff, drawn_tab_height, textx, texty) -> None:
        """ 

`DrawFocusRectangle`(*self*, *dc*, *page*, *wnd*, *draw\_text*, *text\_offset*, *bitmap\_offset*, *drawn\_tab\_yoff*, *drawn\_tab\_height*, *textx*, *texty*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.DrawFocusRectangle "Permalink to this definition")
Draws the focus rectangle on a tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **page** – the page associated with the tab;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **draw\_text** (*string*) – the text that has been drawn on the tab;
* **text\_offset** (*integer*) – the text offset on the tab;
* **bitmap\_offset** (*integer*) – the bitmap offset on the tab;
* **drawn\_tab\_yoff** (*integer*) – the y offset of the tab text;
* **drawn\_tab\_height** (*integer*) – the height of the tab;
* **textx** (*integer*) – the x text extent;
* **texty** (*integer*) – the y text extent.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *in\_rect*, *close\_button\_state*, *paint\_control=False*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.DrawTab "Permalink to this definition")
Draws a single tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **page** – the tab control page associated with the tab;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **paint\_control** (*bool*) – whether to draw the control inside a tab (if any) on a `MemoryDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetAGWFlags(self) -> None:
        """ 

`GetAGWFlags`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetAGWFlags "Permalink to this definition")
Returns the tab art flags.



See also


[`SetAGWFlags`](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetAGWFlags "wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetAGWFlags") for a list of possible return values.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetBestTabCtrlSize(self, wnd, pages, required_bmp_size) -> None:
        """ 

`GetBestTabCtrlSize`(*self*, *wnd*, *pages*, *required\_bmp\_size*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetBestTabCtrlSize "Permalink to this definition")
Returns the best tab control size.



Parameters
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **pages** (*list*) – the pages associated with the tabs;
* **required\_bmp\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the size of the bitmap on the tabs.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetIndentSize(self) -> None:
        """ 

`GetIndentSize`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetIndentSize "Permalink to this definition")
Returns the tabs indent size.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetMeasuringFont(self) -> None:
        """ 

`GetMeasuringFont`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetMeasuringFont "Permalink to this definition")
Returns the font for calculating text measurements.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetNormalFont(self) -> None:
        """ 

`GetNormalFont`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetNormalFont "Permalink to this definition")
Returns the normal font for drawing tab labels.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetSelectedFont(self) -> None:
        """ 

`GetSelectedFont`(*self*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetSelectedFont "Permalink to this definition")
Returns the selected tab font for drawing tab labels.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *control=None*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and button state.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **caption** (*string*) – the tab text caption;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap displayed on the tab;
* **active** (*bool*) – whether the tab is selected or not;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance inside a tab (or `None`).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ 

`SetAGWFlags`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetAGWFlags "Permalink to this definition")
Sets the tab art flags.



Parameters
**agwFlags** (*integer*) – a combination of the following values:





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
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tabs by mouse middle button click |
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetBaseColour(self, base_colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBaseColour`(*self*, *base\_colour*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetBaseColour "Permalink to this definition")
Sets a new base colour.



Parameters
**base\_colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetCustomButton(self, bitmap_id, button_state, bmp) -> None:
        """ 

`SetCustomButton`(*self*, *bitmap\_id*, *button\_state*, *bmp*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetCustomButton "Permalink to this definition")
Sets a custom bitmap for the close, left, right and window list buttons.



Parameters
* **bitmap\_id** (*integer*) – the button identifier;
* **button\_state** (*integer*) – the button state;
* **bmp** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the custom bitmap to use for the button.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetDefaultColours(self, base_colour: Optional[Union[int, str, 'Colour']]=None) -> None:
        """ 

`SetDefaultColours`(*self*, *base\_colour=None*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetDefaultColours "Permalink to this definition")
Sets the default colours, which are calculated from the given base colour.



Parameters
**base\_colour** – an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour"). If defaulted to `None`, a colour
is generated accordingly to the platform and theme.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetMeasuringFont "Permalink to this definition")
Sets the font for calculating text measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to measure tab labels text extents.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their normal, un-selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetSelectedFont "Permalink to this definition")
Sets the selected tab font for drawing tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – the new font to use to draw tab labels in their selected state.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *minMaxTabWidth*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.SetSizingInfo "Permalink to this definition")
Sets the tab sizing information.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the size of the tab control area;
* **tab\_count** (*integer*) – the number of tabs;
* **minMaxTabWidth** (*tuple*) – a tuple containing the minimum and maximum tab widths
to be used when the `AUI_NB_TAB_FIXED_WIDTH` style is active.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """

    def ShowDropDown(self, wnd, pages, active_idx) -> None:
        """ 

`ShowDropDown`(*self*, *wnd*, *pages*, *active\_idx*)[¶](#wx.lib.agw.aui.tabart.AuiDefaultTabArt.ShowDropDown "Permalink to this definition")
Shows the drop-down window menu on the tab area.



Parameters
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window instance;
* **pages** (*list*) – the pages associated with the tabs;
* **active\_idx** (*integer*) – the active tab index.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.AuiDefaultTabArt.html
        """



class ChromeTabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Google Chrome browser style.
It uses custom bitmap to render the tabs, so that the look and feel is as close
as possible to the Chrome style.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.Clone "Permalink to this definition")
Clones the art object.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *in\_rect*, *close\_button\_state*, *paint\_control=False*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.DrawTab "Permalink to this definition")
Draws a single tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **page** – the tab control page associated with the tab;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **paint\_control** (*bool*) – whether to draw the control inside a tab (if any) on a `MemoryDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *control=None*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and button state.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **caption** (*string*) – the tab text caption;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap displayed on the tab;
* **active** (*bool*) – whether the tab is selected or not;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance inside a tab (or `None`).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ 

`SetAGWFlags`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.SetAGWFlags "Permalink to this definition")
Sets the tab art flags.



Parameters
**agwFlags** (*integer*) – a combination of the following values:





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
| `AUI_NB_MIDDLE_CLICK_CLOSE` | Allows to close [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") tabs by mouse middle button click |
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |








Note


Overridden from [`AuiDefaultTabArt`](wx.lib.agw.aui.tabart.AuiDefaultTabArt.html#wx.lib.agw.aui.tabart.AuiDefaultTabArt "wx.lib.agw.aui.tabart.AuiDefaultTabArt").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetBitmaps(self, mirror: bool) -> None:
        """ 

`SetBitmaps`(*self*, *mirror*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.SetBitmaps "Permalink to this definition")
Assigns the tab custom bitmaps



Parameters
**mirror** (*bool*) – whether to vertically mirror the bitmap or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *minMaxTabWidth*)[¶](#wx.lib.agw.aui.tabart.ChromeTabArt.SetSizingInfo "Permalink to this definition")
Sets the tab sizing information.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the size of the tab control area;
* **tab\_count** (*integer*) – the number of tabs;
* **minMaxTabWidth** (*tuple*) – a tuple containing the minimum and maximum tab widths
to be used when the `AUI_NB_TAB_FIXED_WIDTH` style is active.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.ChromeTabArt.html
        """



class FF2TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Firefox 2 (FF2) style.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.tabart.FF2TabArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.tabart.FF2TabArt.Clone "Permalink to this definition")
Clones the art object.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *in\_rect*, *close\_button\_state*, *paint\_control=False*)[¶](#wx.lib.agw.aui.tabart.FF2TabArt.DrawTab "Permalink to this definition")
Draws a single tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **page** – the tab control page associated with the tab;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **paint\_control** (*bool*) – whether to draw the control inside a tab (if any) on a `MemoryDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def DrawTabBackground(self, dc, rect, focus, upperTabs) -> None:
        """ 

`DrawTabBackground`(*self*, *dc*, *rect*, *focus*, *upperTabs*)[¶](#wx.lib.agw.aui.tabart.FF2TabArt.DrawTabBackground "Permalink to this definition")
Draws the tab background for the Firefox 2 style.
This is more consistent with [`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") than before.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **focus** (*bool*) – whether the tab has focus or not;
* **upperTabs** (*bool*) – whether the style is `AUI_NB_TOP` or `AUI_NB_BOTTOM`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control) -> None:
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *control*)[¶](#wx.lib.agw.aui.tabart.FF2TabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and button state.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **caption** (*string*) – the tab text caption;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap displayed on the tab;
* **active** (*bool*) – whether the tab is selected or not;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance inside a tab (or `None`).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.FF2TabArt.html
        """



class VC71TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Visual Studio 2003 (VC71) style.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.tabart.VC71TabArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.tabart.VC71TabArt.Clone "Permalink to this definition")
Clones the art object.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *in\_rect*, *close\_button\_state*, *paint\_control=False*)[¶](#wx.lib.agw.aui.tabart.VC71TabArt.DrawTab "Permalink to this definition")
Draws a single tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **page** – the tab control page associated with the tab;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **paint\_control** (*bool*) – whether to draw the control inside a tab (if any) on a `MemoryDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC71TabArt.html
        """



class VC8TabArt(AuiDefaultTabArt):
    """ A class to draw tabs using the Visual Studio 2005 (VC8) style.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def Clone(self) -> None:
        """ 

`Clone`(*self*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.Clone "Permalink to this definition")
Clones the art object.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def DrawTab(self, dc, wnd, page, in_rect, close_button_state, paint_control=False) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *in\_rect*, *close\_button\_state*, *paint\_control=False*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.DrawTab "Permalink to this definition")
Draws a single tab.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **page** – the tab control page associated with the tab;
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – rectangle the tab should be confined to;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **paint\_control** (*bool*) – whether to draw the control inside a tab (if any) on a `MemoryDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def FillVC8GradientColour(self, dc, tabPoints, active) -> None:
        """ 

`FillVC8GradientColour`(*self*, *dc*, *tabPoints*, *active*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.FillVC8GradientColour "Permalink to this definition")
Fills the tab with the Visual Studio 2005 gradient background.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **tabPoints** (*list*) – a list of [`wx.Point`](wx.Point.html#wx.Point "wx.Point") objects describing the tab shape;
* **active** (*bool*) – whether the tab is selected or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, control=None) -> None:
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *control=None*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and button state.



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context;
* **wnd** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance object;
* **caption** (*string*) – the tab text caption;
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – the bitmap displayed on the tab;
* **active** (*bool*) – whether the tab is selected or not;
* **close\_button\_state** (*integer*) – the state of the close button on the tab;
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") instance inside a tab (or `None`).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, minMaxTabWidth) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *minMaxTabWidth*)[¶](#wx.lib.agw.aui.tabart.VC8TabArt.SetSizingInfo "Permalink to this definition")
Sets the tab sizing information.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the size of the tab control area;
* **tab\_count** (*integer*) – the number of tabs;
* **minMaxTabWidth** (*tuple*) – a tuple containing the minimum and maximum tab widths
to be used when the `AUI_NB_TAB_FIXED_WIDTH` style is active.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.tabart.VC8TabArt.html
        """



