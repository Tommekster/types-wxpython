# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class FlatNotebook(Panel):
    """ The [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") is a full implementation of the `Notebook`, and designed to be
a drop-in replacement for `Notebook`. The API functions are similar so one can
expect the function to behave in the same way.


  


        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="FlatNotebook") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=0*, *name="FlatNotebook"*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") parent;
* **id** – an identifier for the control: a value of -1 is taken to mean a default;
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the underlying `Panel` window style;
* **agwStyle** – the AGW-specific window style. This can be a combination of the
following bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `FNB_VC71` | 0x1 | Use Visual Studio 2003 (VC7.1) style for tabs. |
| `FNB_FANCY_TABS` | 0x2 | Use fancy style - square tabs filled with gradient colouring. |
| `FNB_TABS_BORDER_SIMPLE` | 0x4 | Draw thin border around the page. |
| `FNB_NO_X_BUTTON` | 0x8 | Do not display the ‘X’ button. |
| `FNB_NO_NAV_BUTTONS` | 0x10 | Do not display the right/left arrows. |
| `FNB_MOUSE_MIDDLE_CLOSES_TABS` | 0x20 | Use the mouse middle button for cloing tabs. |
| `FNB_BOTTOM` | 0x40 | Place tabs at bottom - the default is to place them at top. |
| `FNB_NODRAG` | 0x80 | Disable dragging of tabs. |
| `FNB_VC8` | 0x100 | Use Visual Studio 2005 (VC8) style for tabs. |
| `FNB_X_ON_TAB` | 0x200 | Place ‘X’ close button on the active tab. |
| `FNB_BACKGROUND_GRADIENT` | 0x400 | Use gradients to paint the tabs background. |
| `FNB_COLOURFUL_TABS` | 0x800 | Use colourful tabs (VC8 style only). |
| `FNB_DCLICK_CLOSES_TABS` | 0x1000 | Style to close tab using double click. |
| `FNB_SMART_TABS` | 0x2000 | Use *Smart Tabbing*, like `Alt` + `Tab` on Windows. |
| `FNB_DROPDOWN_TABS_LIST` | 0x4000 | Use a dropdown menu on the left in place of the arrows. |
| `FNB_ALLOW_FOREIGN_DND` | 0x8000 | Allows drag ‘n’ drop operations between different [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook"). |
| `FNB_HIDE_ON_SINGLE_TAB` | 0x10000 | Hides the Page Container when there is one or fewer tabs. |
| `FNB_DEFAULT_STYLE` | 0x10020 | [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") default style. |
| `FNB_FF2` | 0x20000 | Use Firefox 2 style for tabs. |
| `FNB_NO_TAB_FOCUS` | 0x40000 | Does not allow tabs to have focus. |
| `FNB_RIBBON_TABS` | 0x80000 | Use the Ribbon Tabs style. |
| `FNB_HIDE_TABS` | 0x100000 | Hides the Page Container allowing only keyboard navigation |
| `FNB_NAV_BUTTONS_WHEN_NEEDED` | 0x200000 | Hides the navigation left/right arrows if all tabs fit |
* **name** – the window name.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AddPage(self, page, text, select=False, imageId=-1) -> None:
        """ 

`AddPage`(*self*, *page*, *text*, *select=False*, *imageId=-1*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.AddPage "Permalink to this definition")
Adds a page to the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").



Parameters
* **page** – specifies the new page;
* **text** – specifies the text for the new page;
* **select** – specifies whether the page should be selected;
* **imageId** – specifies the optional image index for the new page.



Returns
`True` if successful, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AdvanceSelection(self, forward: bool=True) -> None:
        """ 

`AdvanceSelection`(*self*, *forward=True*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.AdvanceSelection "Permalink to this definition")
Cycles through the tabs.



Parameters
**forward** – if `True`, the selection is advanced in ascending order
(to the right), otherwise the selection is advanced in descending order.





Note


The call to this function generates the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignImageList`(*self*, *imageList*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.AssignImageList "Permalink to this definition")
Assigns the image list for the page control.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DeleteAllPages(self) -> None:
        """ 

`DeleteAllPages`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.DeleteAllPages "Permalink to this definition")
Deletes all the pages in the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DeletePage(self, page: Any) -> None:
        """ 

`DeletePage`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.DeletePage "Permalink to this definition")
Deletes the specified page, and the associated window.



Parameters
**page** – an integer specifying the new selected page.





Note


The call to this function generates the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def DoGetBestSize(self) -> None:
        """ 

`DoGetBestSize`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.DoGetBestSize "Permalink to this definition")
Gets the size which best suits the window: for a control, it would be the
minimal size which doesn’t truncate the control, for a panel - the same
size as it would have after a call to *Fit()*.



Note


Overridden from `Panel`.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def EnableTab(self, page, enabled=True) -> None:
        """ 

`EnableTab`(*self*, *page*, *enabled=True*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.EnableTab "Permalink to this definition")
Enables or disables a tab.



Parameters
* **page** – an integer specifying the page index;
* **enabled** – `True` to enable a tab, `False` to disable it.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def EnsureVisible(self, page: Any) -> None:
        """ 

`EnsureVisible`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.EnsureVisible "Permalink to this definition")
Ensures that a tab is visible.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetActiveTabColour(self) -> None:
        """ 

`GetActiveTabColour`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetActiveTabColour "Permalink to this definition")
Returns the active tab colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetActiveTabTextColour(self) -> None:
        """ 

`GetActiveTabTextColour`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetActiveTabTextColour "Permalink to this definition")
Get the active tab text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetAGWWindowStyleFlag(self) -> None:
        """ 

`GetAGWWindowStyleFlag`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetAGWWindowStyleFlag "Permalink to this definition")
Returns the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") window style.



See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag "wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag") for a list of valid window styles.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetBorderColour(self) -> None:
        """ 

`GetBorderColour`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetBorderColour "Permalink to this definition")
Returns the border colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetCurrentPage(self) -> None:
        """ 

`GetCurrentPage`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetCurrentPage "Permalink to this definition")
Returns the currently selected notebook page or `None` if none is selected.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetCustomPage(self) -> None:
        """ 

`GetCustomPage`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetCustomPage "Permalink to this definition")
Returns a custom panel to show when there are no pages left in [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetEnabled(self, page: Any) -> None:
        """ 

`GetEnabled`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetEnabled "Permalink to this definition")
Returns whether a tab is enabled or not.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourBorder(self) -> None:
        """ 

`GetGradientColourBorder`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetGradientColourBorder "Permalink to this definition")
Gets the tab border colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourFrom(self) -> None:
        """ 

`GetGradientColourFrom`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetGradientColourFrom "Permalink to this definition")
Gets first gradient colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetGradientColourTo(self) -> None:
        """ 

`GetGradientColourTo`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetGradientColourTo "Permalink to this definition")
Gets second gradient colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetImageList(self) -> None:
        """ 

`GetImageList`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetImageList "Permalink to this definition")
Returns the associated image list.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetNonActiveTabTextColour(self) -> None:
        """ 

`GetNonActiveTabTextColour`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetNonActiveTabTextColour "Permalink to this definition")
Returns the non active tabs text colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPadding(self) -> None:
        """ 

`GetPadding`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPadding "Permalink to this definition")
Returns the amount of space around each page’s icon and label, in pixels.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPage(self, page) -> None:
        """ 

`GetPage`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPage "Permalink to this definition")
Returns the window at the given page position, or `None`.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageBestSize(self) -> None:
        """ 

`GetPageBestSize`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageBestSize "Permalink to this definition")
Return the page best size.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageCount(self) -> None:
        """ 

`GetPageCount`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageCount "Permalink to this definition")
Returns the number of pages in the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") control.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageImage(self, page: Any) -> None:
        """ 

`GetPageImage`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageImage "Permalink to this definition")
Returns the image index for the given page.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageIndex(self, win: 'Window') -> None:
        """ 

`GetPageIndex`(*self*, *win*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageIndex "Permalink to this definition")
Returns the index at which the window is found.



Parameters
**win** – an instance of [`wx.Window`](wx.Window.html#wx.Window "wx.Window").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageShapeAngle(self, page_index: Any) -> None:
        """ 

`GetPageShapeAngle`(*self*, *page\_index*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageShapeAngle "Permalink to this definition")
Returns the angle associated to a tab.



Parameters
**page\_index** – the index of the tab for which we wish to get the shape angle.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageText(self, page: Any) -> None:
        """ 

`GetPageText`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageText "Permalink to this definition")
Returns the string for the given page.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPageTextColour(self, page: Any) -> None:
        """ 

`GetPageTextColour`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPageTextColour "Permalink to this definition")
Returns the tab text colour if it has been set previously, or `None` otherwise.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetPreviousSelection(self) -> None:
        """ 

`GetPreviousSelection`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetPreviousSelection "Permalink to this definition")
Returns the previous selection.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetSelection(self) -> None:
        """ 

`GetSelection`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetSelection "Permalink to this definition")
Returns the currently selected page, or -1 if none was selected.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTabArea(self) -> None:
        """ 

`GetTabArea`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetTabArea "Permalink to this definition")
Returns the associated page.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTabAreaColour(self) -> None:
        """ 

`GetTabAreaColour`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetTabAreaColour "Permalink to this definition")
Returns the area behind the tabs colour.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def GetTileOrientation(self) -> None:
        """ 

`GetTileOrientation`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.GetTileOrientation "Permalink to this definition")
Returns the orientation when on tiling mode. This method can return
`wx.VERTICAL` when the panels are vertically stacked, `wx.HORIZONTAL`
when they are horizontally stacked panels or `None` when there is no
stacking and [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") behaves like a normal notebook.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def HasAGWFlag(self, flag: FlatNotebook) -> None:
        """ 

`HasAGWFlag`(*self*, *flag*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.HasAGWFlag "Permalink to this definition")
Returns whether a flag is present in the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") style.



Parameters
**flag** – one of the possible [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") window styles.





See also


[`SetAGWWindowStyleFlag`](#wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag "wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag") for a list of possible window style flags.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def HideTabs(self) -> None:
        """ 

`HideTabs`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.HideTabs "Permalink to this definition")
Hides the tabs.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.Init "Permalink to this definition")
Initializes all the class attributes.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def InsertPage(self, indx, page, text, select=True, imageId=-1) -> None:
        """ 

`InsertPage`(*self*, *indx*, *page*, *text*, *select=True*, *imageId=-1*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.InsertPage "Permalink to this definition")
Inserts a new page at the specified position.



Parameters
* **indx** – specifies the position of the new page;
* **page** – specifies the new page;
* **text** – specifies the text for the new page;
* **select** – specifies whether the page should be selected;
* **imageId** – specifies the optional image index for the new page.



Returns
`True` if successful, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def OnDropTarget(self, x, y, nTabPage, wnd_oldContainer) -> None:
        """ 

`OnDropTarget`(*self*, *x*, *y*, *nTabPage*, *wnd\_oldContainer*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.OnDropTarget "Permalink to this definition")
Handles the drop action from a drag and drop operation.



Parameters
* **x** – the x position of the drop action;
* **y** – the y position of the drop action;
* **nTabPage** – the index of the tab being dropped;
* **wnd\_oldContainer** – the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") to which the dropped tab previously
belonged to.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ 

`OnNavigationKey`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.OnNavigationKey "Permalink to this definition")
Handles the `wx.EVT_NAVIGATION_KEY` event for [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").



Parameters
**event** – a `NavigationKeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def RemovePage(self, page: Any) -> None:
        """ 

`RemovePage`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.RemovePage "Permalink to this definition")
Deletes the specified page, without deleting the associated window.



Parameters
**page** – an integer specifying the page index.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetActiveTabColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetActiveTabColour`(*self*, *colour*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetActiveTabColour "Permalink to this definition")
Sets the active tab colour.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or any typemap supported by wxWidgets/wxPython
to generate a colour (i.e., a hex string, a colour name, a 3 or 4 integer tuple).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetActiveTabTextColour(self, textColour: Union[int, str, 'Colour']) -> None:
        """ 

`SetActiveTabTextColour`(*self*, *textColour*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetActiveTabTextColour "Permalink to this definition")
Sets the text colour for the active tab.



Parameters
**textColour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or any typemap supported by wxWidgets/wxPython
to generate a colour (i.e., a hex string, a colour name, a 3 or 4 integer tuple).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetAGWWindowStyleFlag(self, agwStyle: int) -> None:
        """ 

`SetAGWWindowStyleFlag`(*self*, *agwStyle*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetAGWWindowStyleFlag "Permalink to this definition")
Sets the [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") window style flags.



Parameters
**agwStyle** – the AGW-specific window style. This can be a combination of the
following bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `FNB_VC71` | 0x1 | Use Visual Studio 2003 (VC7.1) style for tabs. |
| `FNB_FANCY_TABS` | 0x2 | Use fancy style - square tabs filled with gradient colouring. |
| `FNB_TABS_BORDER_SIMPLE` | 0x4 | Draw thin border around the page. |
| `FNB_NO_X_BUTTON` | 0x8 | Do not display the ‘X’ button. |
| `FNB_NO_NAV_BUTTONS` | 0x10 | Do not display the right/left arrows. |
| `FNB_MOUSE_MIDDLE_CLOSES_TABS` | 0x20 | Use the mouse middle button for cloing tabs. |
| `FNB_BOTTOM` | 0x40 | Place tabs at bottom - the default is to place them at top. |
| `FNB_NODRAG` | 0x80 | Disable dragging of tabs. |
| `FNB_VC8` | 0x100 | Use Visual Studio 2005 (VC8) style for tabs. |
| `FNB_X_ON_TAB` | 0x200 | Place ‘X’ close button on the active tab. |
| `FNB_BACKGROUND_GRADIENT` | 0x400 | Use gradients to paint the tabs background. |
| `FNB_COLOURFUL_TABS` | 0x800 | Use colourful tabs (VC8 style only). |
| `FNB_DCLICK_CLOSES_TABS` | 0x1000 | Style to close tab using double click. |
| `FNB_SMART_TABS` | 0x2000 | Use *Smart Tabbing*, like `Alt` + `Tab` on Windows. |
| `FNB_DROPDOWN_TABS_LIST` | 0x4000 | Use a dropdown menu on the left in place of the arrows. |
| `FNB_ALLOW_FOREIGN_DND` | 0x8000 | Allows drag ‘n’ drop operations between different [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook"). |
| `FNB_HIDE_ON_SINGLE_TAB` | 0x10000 | Hides the Page Container when there is one or fewer tabs. |
| `FNB_DEFAULT_STYLE` | 0x10020 | [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") default style. |
| `FNB_FF2` | 0x20000 | Use Firefox 2 style for tabs. |
| `FNB_NO_TAB_FOCUS` | 0x40000 | Does not allow tabs to have focus. |
| `FNB_RIBBON_TABS` | 0x80000 | Use the Ribbon Tabs style. |
| `FNB_HIDE_TABS` | 0x100000 | Hides the Page Container allowing only keyboard navigation |
| `FNB_NAV_BUTTONS_WHEN_NEEDED` | 0x200000 | Hides the navigation left/right arrows if all tabs fit |









            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetAllPagesShapeAngle(self, angle: Any) -> None:
        """ 

`SetAllPagesShapeAngle`(*self*, *angle*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetAllPagesShapeAngle "Permalink to this definition")
Sets the angle associated to all the tab.



Parameters
**angle** – the new shape angle for the tab (must be less than 15 degrees).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetCustomPage(self, panel: 'Window') -> None:
        """ 

`SetCustomPage`(*self*, *panel*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetCustomPage "Permalink to this definition")
Sets a custom panel to show when there are no pages left in [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").



Parameters
**panel** – any subclass of [`wx.Window`](wx.Window.html#wx.Window "wx.Window") will do, as long as it is suitable
to be used as a notebook page. Examples include `Panel`, `ScrolledWindow`,
and so on.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourBorder(self, border: Union[int, str, 'Colour']) -> None:
        """ 

`SetGradientColourBorder`(*self*, *border*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetGradientColourBorder "Permalink to this definition")
Sets the tab border colour.



Parameters
**border** – the border colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourFrom(self, fr: Union[int, str, 'Colour']) -> None:
        """ 

`SetGradientColourFrom`(*self*, *fr*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetGradientColourFrom "Permalink to this definition")
Sets the starting colour for the gradient.



Parameters
**fr** – the first gradient colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColours(self, fr, to, border) -> None:
        """ 

`SetGradientColours`(*self*, *fr*, *to*, *border*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetGradientColours "Permalink to this definition")
Sets the gradient colours for the tab.



Parameters
* **fr** – the first gradient colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");
* **to** – the second gradient colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");
* **border** – the border colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetGradientColourTo(self, to: Union[int, str, 'Colour']) -> None:
        """ 

`SetGradientColourTo`(*self*, *to*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetGradientColourTo "Permalink to this definition")
Sets the ending colour for the gradient.



Parameters
**to** – the second gradient colour, an instance of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour");






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imageList*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetImageList "Permalink to this definition")
Sets the image list for the page control.



Parameters
**imageList** – an instance of [`wx.ImageList`](wx.ImageList.html#wx.ImageList "wx.ImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetNavigatorIcon(self, bmp: 'Bitmap') -> None:
        """ 

`SetNavigatorIcon`(*self*, *bmp*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetNavigatorIcon "Permalink to this definition")
Set the icon used by the [`TabNavigatorWindow`](wx.lib.agw.flatnotebook.TabNavigatorWindow.html#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow").



Parameters
**bmp** – a valid [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") object.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetNonActiveTabTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetNonActiveTabTextColour`(*self*, *colour*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetNonActiveTabTextColour "Permalink to this definition")
Sets the non active tabs text colour.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or any typemap supported by wxWidgets/wxPython
to generate a colour (i.e., a hex string, a colour name, a 3 or 4 integer tuple).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPadding(self, padding: Any) -> None:
        """ 

`SetPadding`(*self*, *padding*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetPadding "Permalink to this definition")
Sets the amount of space around each page’s icon and label, in pixels.



Parameters
**padding** – the amount of space around each page’s icon and label,
in pixels.





Note


Only the horizontal padding is considered.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageImage(self, page, image) -> None:
        """ 

`SetPageImage`(*self*, *page*, *image*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetPageImage "Permalink to this definition")
Sets the image index for the given page.



Parameters
* **page** – an integer specifying the page index;
* **image** – an index into the image list which was set with [`SetImageList`](#wx.lib.agw.flatnotebook.FlatNotebook.SetImageList "wx.lib.agw.flatnotebook.FlatNotebook.SetImageList").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageShapeAngle(self, page_index, angle) -> None:
        """ 

`SetPageShapeAngle`(*self*, *page\_index*, *angle*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetPageShapeAngle "Permalink to this definition")
Sets the angle associated to a tab.



Parameters
* **page\_index** – the index of the tab for which we wish to get the shape angle;
* **angle** – the new shape angle for the tab (must be less than 15 degrees).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageText(self, page, text) -> None:
        """ 

`SetPageText`(*self*, *page*, *text*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetPageText "Permalink to this definition")
Sets the text for the given page.



Parameters
* **page** – an integer specifying the page index;
* **text** – the new tab label.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetPageTextColour(self, page, colour) -> None:
        """ 

`SetPageTextColour`(*self*, *page*, *colour*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetPageTextColour "Permalink to this definition")
Sets the tab text colour individually.



Parameters
* **page** – an integer specifying the page index;
* **colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or any typemap supported by wxWidgets/wxPython
to generate a colour (i.e., a hex string, a colour name, a 3 or 4 integer tuple). You can
pass `None` or `NullColour` to return to the default page text colour.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetRightClickMenu(self, menu: 'Menu') -> None:
        """ 

`SetRightClickMenu`(*self*, *menu*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetRightClickMenu "Permalink to this definition")
Sets the popup menu associated to a right click on a tab.



Parameters
**menu** – an instance of [`wx.Menu`](wx.Menu.html#wx.Menu "wx.Menu").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetSelection(self, page: Any) -> None:
        """ 

`SetSelection`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetSelection "Permalink to this definition")
Sets the selection for the given page.



Parameters
**page** – an integer specifying the new selected page.





Note


The call to this function **does not** generate the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def SetTabAreaColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetTabAreaColour`(*self*, *colour*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.SetTabAreaColour "Permalink to this definition")
Sets the area behind the tabs colour.



Parameters
**colour** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") object or any typemap supported by wxWidgets/wxPython
to generate a colour (i.e., a hex string, a colour name, a 3 or 4 integer tuple).






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def ShowCustomPage(self, show=True) -> None:
        """ 

`ShowCustomPage`(*self*, *show=True*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.ShowCustomPage "Permalink to this definition")
Hides the custom panel which is shown when there are no pages left in [`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def ShowTabs(self) -> None:
        """ 

`ShowTabs`(*self*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.ShowTabs "Permalink to this definition")
Shows the tabs if hidden previously.




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """

    def Tile(self, orient: Optional['VERTICAL']=None) -> None:
        """ 

`Tile`(*self*, *orient=None*)[¶](#wx.lib.agw.flatnotebook.FlatNotebook.Tile "Permalink to this definition")
Shows pages in column/row mode (one panel after the other in columns/rows).



Parameters
**orient** – this parameter represents the orientation of the stacked
panels. Pass `wx.VERTICAL` to get vertically stacked panels, `wx.HORIZONTAL`
to get horizontally stacked panels or `None` to return to the default
[`FlatNotebook`](#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") behaviour with tabs.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebook.html
        """



EVT_NAVIGATION_KEY: int

VERTICAL: int

HORIZONTAL: int

class FlatNotebookCompatible(FlatNotebook):
    """ This class is more compatible with the `Notebook` API, especially regarding
page changing events. Use the [`FlatNotebookCompatible.SetSelection()`](#wx.lib.agw.flatnotebook.FlatNotebookCompatible.SetSelection "wx.lib.agw.flatnotebook.FlatNotebookCompatible.SetSelection") method if you wish to send page
changing events, or [`FlatNotebookCompatible.ChangeSelection()`](#wx.lib.agw.flatnotebook.FlatNotebookCompatible.ChangeSelection "wx.lib.agw.flatnotebook.FlatNotebookCompatible.ChangeSelection") otherwise.


  


        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
    """
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, agwStyle=0, name="FlatNotebook") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *agwStyle=0*, *name="FlatNotebook"*)[¶](#wx.lib.agw.flatnotebook.FlatNotebookCompatible.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – the [`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") parent;
* **id** – an identifier for the control: a value of -1 is taken to mean a default;
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the underlying `Panel` window style;
* **agwStyle** – the AGW-specific window style. This can be a combination of the
following bits:








| Window Styles | Hex Value | Description |
| --- | --- | --- |
| `FNB_VC71` | 0x1 | Use Visual Studio 2003 (VC7.1) style for tabs. |
| `FNB_FANCY_TABS` | 0x2 | Use fancy style - square tabs filled with gradient colouring. |
| `FNB_TABS_BORDER_SIMPLE` | 0x4 | Draw thin border around the page. |
| `FNB_NO_X_BUTTON` | 0x8 | Do not display the ‘X’ button. |
| `FNB_NO_NAV_BUTTONS` | 0x10 | Do not display the right/left arrows. |
| `FNB_MOUSE_MIDDLE_CLOSES_TABS` | 0x20 | Use the mouse middle button for cloing tabs. |
| `FNB_BOTTOM` | 0x40 | Place tabs at bottom - the default is to place them at top. |
| `FNB_NODRAG` | 0x80 | Disable dragging of tabs. |
| `FNB_VC8` | 0x100 | Use Visual Studio 2005 (VC8) style for tabs. |
| `FNB_X_ON_TAB` | 0x200 | Place ‘X’ close button on the active tab. |
| `FNB_BACKGROUND_GRADIENT` | 0x400 | Use gradients to paint the tabs background. |
| `FNB_COLOURFUL_TABS` | 0x800 | Use colourful tabs (VC8 style only). |
| `FNB_DCLICK_CLOSES_TABS` | 0x1000 | Style to close tab using double click. |
| `FNB_SMART_TABS` | 0x2000 | Use *Smart Tabbing*, like `Alt` + `Tab` on Windows. |
| `FNB_DROPDOWN_TABS_LIST` | 0x4000 | Use a dropdown menu on the left in place of the arrows. |
| `FNB_ALLOW_FOREIGN_DND` | 0x8000 | Allows drag ‘n’ drop operations between different [`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook"). |
| `FNB_HIDE_ON_SINGLE_TAB` | 0x10000 | Hides the Page Container when there is one or fewer tabs. |
| `FNB_DEFAULT_STYLE` | 0x10020 | [`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") default style. |
| `FNB_FF2` | 0x20000 | Use Firefox 2 style for tabs. |
| `FNB_NO_TAB_FOCUS` | 0x40000 | Does not allow tabs to have focus. |
| `FNB_RIBBON_TABS` | 0x80000 | Use the Ribbon Tabs style. |
| `FNB_HIDE_TABS` | 0x100000 | Hides the Page Container allowing only keyboard navigation |
| `FNB_NAV_BUTTONS_WHEN_NEEDED` | 0x200000 | Hides the navigation left/right arrows if all tabs fit |
* **name** – the window name.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """

    def ChangeSelection(self, page: Any) -> None:
        """ 

`ChangeSelection`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebookCompatible.ChangeSelection "Permalink to this definition")
Sets the selection for the given page.



Parameters
**page** – an integer specifying the new selected page.





Note


The call to this function **does not** generate the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """

    def SetSelection(self, page: Any) -> None:
        """ 

`SetSelection`(*self*, *page*)[¶](#wx.lib.agw.flatnotebook.FlatNotebookCompatible.SetSelection "Permalink to this definition")
Sets the selection for the given page.



Parameters
**page** – an integer specifying the new selected page.





Note


The call to this function **generates** the page changing events.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.FlatNotebookCompatible.html
        """



class TabNavigatorWindow(Dialog):
    """ This class is used to create a modal dialog that enables *Smart Tabbing*,
similar to what you would get by hitting `Alt` + `Tab` on Windows.


  


        Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
    """
    def __init__(self, parent=None, icon=None) -> None:
        """ 

`__init__`(*self*, *parent=None*, *icon=None*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.__init__ "Permalink to this definition")
Default class constructor.
Used internally.



Parameters
* **parent** – the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow") parent window;
* **icon** – a valid [`wx.Bitmap`](wx.Bitmap.html#wx.Bitmap "wx.Bitmap") object representing the icon to be displayed
in the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow").






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def CloseDialog(self) -> None:
        """ 

`CloseDialog`(*self*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.CloseDialog "Permalink to this definition")
Closes the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow") dialog, setting the new selection in
[`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnItemSelected(self, event: ListEvent) -> None:
        """ 

`OnItemSelected`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.OnItemSelected "Permalink to this definition")
Handles the `wx.EVT_LISTBOX_DCLICK` for the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow").



Parameters
**event** – a `ListEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnKeyUp(self, event: KeyEvent) -> None:
        """ 

`OnKeyUp`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.OnKeyUp "Permalink to this definition")
Handles the `wx.EVT_KEY_UP` for the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow").



Parameters
**event** – a `KeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnNavigationKey(self, event: NavigationKeyEvent) -> None:
        """ 

`OnNavigationKey`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.OnNavigationKey "Permalink to this definition")
Handles the `wx.EVT_NAVIGATION_KEY` for the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow").



Parameters
**event** – a `NavigationKeyEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnPanelEraseBg(self, event: EraseEvent) -> None:
        """ 

`OnPanelEraseBg`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.OnPanelEraseBg "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` for the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow") top panel.



Parameters
**event** – a `EraseEvent` event to be processed.





Note


This method is intentionally empty to reduce flicker.





            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def OnPanelPaint(self, event: PaintEvent) -> None:
        """ 

`OnPanelPaint`(*self*, *event*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.OnPanelPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` for the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow") top panel.



Parameters
**event** – a `PaintEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """

    def PopulateListControl(self, book: FlatNotebook) -> None:
        """ 

`PopulateListControl`(*self*, *book*)[¶](#wx.lib.agw.flatnotebook.TabNavigatorWindow.PopulateListControl "Permalink to this definition")
Populates the [`TabNavigatorWindow`](#wx.lib.agw.flatnotebook.TabNavigatorWindow "wx.lib.agw.flatnotebook.TabNavigatorWindow") listbox with a list of tabs.



Parameters
**book** – an instance of [`FlatNotebook`](wx.lib.agw.flatnotebook.FlatNotebook.html#wx.lib.agw.flatnotebook.FlatNotebook "wx.lib.agw.flatnotebook.FlatNotebook") containing the tabs to be
displayed in the listbox.






            Source: https://docs.wxpython.org/wx.lib.agw.flatnotebook.TabNavigatorWindow.html
        """



EVT_LISTBOX_DCLICK: int

EVT_KEY_UP: int

EVT_ERASE_BACKGROUND: int

EVT_PAINT: int

FNB_VC71: int

FNB_FANCY_TABS: int

FNB_TABS_BORDER_SIMPLE: int

FNB_NO_X_BUTTON: int

FNB_NO_NAV_BUTTONS: int

FNB_MOUSE_MIDDLE_CLOSES_TABS: int

FNB_BOTTOM: int

FNB_NODRAG: int

FNB_VC8: int

FNB_X_ON_TAB: int

FNB_BACKGROUND_GRADIENT: int

FNB_COLOURFUL_TABS: int

FNB_DCLICK_CLOSES_TABS: int

FNB_SMART_TABS: int

FNB_DROPDOWN_TABS_LIST: int

FNB_ALLOW_FOREIGN_DND: int

FNB_HIDE_ON_SINGLE_TAB: int

FNB_DEFAULT_STYLE: int

FNB_FF2: int

FNB_NO_TAB_FOCUS: int

FNB_RIBBON_TABS: int

FNB_HIDE_TABS: int

FNB_NAV_BUTTONS_WHEN_NEEDED: int

