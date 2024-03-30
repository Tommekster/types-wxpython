# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import BookCtrlBase, Window, VisualAttributes, Bitmap, BookCtrlEvent, Event, Size, Control, Rect, _DC, DC, EvtHandler, Frame, Menu, NotifyEvent, Point, Panel, _Icon, IconBundle, _MenuBar, _StatusBar, _ToolBar, StatusBar, ToolBar, Icon, MenuBar, _Bitmap, _SizerItem, _Window, SizerItem, _Font, Font, Colour

class AuiNotebook(BookCtrlBase):
    """ **Possible constructors**:



```
AuiNotebook()

AuiNotebook(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
            style=AUI_NB_DEFAULT_STYLE)

```


AuiNotebook is part of the `AUI` class framework, which represents a
notebook control, managing multiple windows with associated tabs.


  


        Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiNotebook.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=AUI\_NB\_DEFAULT\_STYLE)*


Constructor.


Creates a AuiNotebok control.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def AddPage(self, *args, **kw) -> bool:
        """ 

`AddPage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiNotebook.AddPage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddPage** *(self, page, caption, select=False, bitmap=BitmapBundle())*


Adds a page.


If the `select` parameter is `True`, calling this will generate a page change event.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **caption** (*string*) –
* **select** (*bool*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –



Return type
*bool*






---

  



**AddPage** *(self, page, text, select, imageId)*


Adds a new page.


The page must have the book control itself as the parent and must not have been added to this control previously.


The call to this function may generate the page changing events.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Specifies the new page.
* **text** (*string*) – Specifies the text for the new page.
* **select** (*bool*) – Specifies whether the page should be selected.
* **imageId** (*int*) – Specifies the optional image index for the new page.



Return type
*bool*



Returns
`True` if successful, `False` otherwise.





New in version 2.9.3.




Note


Do not delete the page, it will be deleted by the book control.




See also


[`InsertPage`](#wx.aui.AuiNotebook.InsertPage "wx.aui.AuiNotebook.InsertPage")





---

  





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def AdvanceSelection(self, forward: bool=True) -> None:
        """ 

`AdvanceSelection`(*self*, *forward=True*)[¶](#wx.aui.AuiNotebook.AdvanceSelection "Permalink to this definition")
Sets the selection to the next or previous page.



Parameters
**forward** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def ChangeSelection(self, n: int) -> int:
        """ 

`ChangeSelection`(*self*, *n*)[¶](#wx.aui.AuiNotebook.ChangeSelection "Permalink to this definition")
Changes the selection for the given page, returning the previous selection.


This function behaves as [`SetSelection`](#wx.aui.AuiNotebook.SetSelection "wx.aui.AuiNotebook.SetSelection") but does *not* generate the page changing events.


See [User Generated Events vs Programmatically Generated Events](events_overview.html#user-generated-events-vs-programmatically-generated-events) for more information.



Parameters
**n** (*int*) – 



Return type
*int*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.aui.AuiNotebook.Create "Permalink to this definition")
Creates the notebook window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def DeleteAllPages(self) -> bool:
        """ 

`DeleteAllPages`(*self*)[¶](#wx.aui.AuiNotebook.DeleteAllPages "Permalink to this definition")
Deletes all pages.



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def DeletePage(self, page: int) -> bool:
        """ 

`DeletePage`(*self*, *page*)[¶](#wx.aui.AuiNotebook.DeletePage "Permalink to this definition")
Deletes a page at the given index.


Calling this method will generate a page change event.



Parameters
**page** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def FindTab(self, page, ctrl, idx) -> bool:
        """ 

`FindTab`(*self*, *page*, *ctrl*, *idx*)[¶](#wx.aui.AuiNotebook.FindTab "Permalink to this definition")
Finds tab control associated with a given window and its tab index.



Parameters
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **ctrl** ([*AuiTabCtrl*](wx.aui.AuiTabCtrl.html#wx.aui.AuiTabCtrl "wx.aui.AuiTabCtrl")) –
* **idx** (*int*) –



Return type
*bool*



Returns
`True` when the tab control is found, `False` otherwise.





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetActiveTabCtrl(self) -> 'AuiTabCtrl':
        """ 

`GetActiveTabCtrl`(*self*)[¶](#wx.aui.AuiNotebook.GetActiveTabCtrl "Permalink to this definition")
Returns active tab control for this notebook.



Return type
 [wx.aui.AuiTabCtrl](wx.aui.AuiTabCtrl.html#wx-aui-auitabctrl)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetArtProvider(self) -> 'AuiTabArt':
        """ 

`GetArtProvider`(*self*)[¶](#wx.aui.AuiNotebook.GetArtProvider "Permalink to this definition")
Returns the associated art provider.



Return type
 [wx.aui.AuiTabArt](wx.aui.AuiTabArt.html#wx-aui-auitabart)






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiNotebook.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetCurrentPage(self) -> 'Window':
        """ 

`GetCurrentPage`(*self*)[¶](#wx.aui.AuiNotebook.GetCurrentPage "Permalink to this definition")
Returns the currently selected page or `None`.



Return type
*Window*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetHeightForPageHeight(self, pageHeight: int) -> int:
        """ 

`GetHeightForPageHeight`(*self*, *pageHeight*)[¶](#wx.aui.AuiNotebook.GetHeightForPageHeight "Permalink to this definition")
Returns the desired height of the notebook for the given page height.


Use this to fit the notebook to a given page size.



Parameters
**pageHeight** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPage(self, page_idx: int) -> 'Window':
        """ 

`GetPage`(*self*, *page\_idx*)[¶](#wx.aui.AuiNotebook.GetPage "Permalink to this definition")
Returns the page specified by the given index.



Parameters
**page\_idx** (*int*) – 



Return type
*Window*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageBitmap(self, page: int) -> 'Bitmap':
        """ 

`GetPageBitmap`(*self*, *page*)[¶](#wx.aui.AuiNotebook.GetPageBitmap "Permalink to this definition")
Returns the tab bitmap for the page.



Parameters
**page** (*int*) – 



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageCount(self) -> int:
        """ 

`GetPageCount`(*self*)[¶](#wx.aui.AuiNotebook.GetPageCount "Permalink to this definition")
Returns the number of pages in the notebook.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageImage(self, nPage: int) -> int:
        """ 

`GetPageImage`(*self*, *nPage*)[¶](#wx.aui.AuiNotebook.GetPageImage "Permalink to this definition")
Returns the image index for the given page.



Parameters
**nPage** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageIndex(self, page_wnd: 'Window') -> int:
        """ 

`GetPageIndex`(*self*, *page\_wnd*)[¶](#wx.aui.AuiNotebook.GetPageIndex "Permalink to this definition")
Returns the page index for the specified window.


If the window is not found in the notebook, `wx.NOT_FOUND` is returned.


This is AUI-specific equivalent to *BookCtrl.FindPage()* and it is recommended to use that generic method instead of this one.



Parameters
**page\_wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageText(self, page: int) -> str:
        """ 

`GetPageText`(*self*, *page*)[¶](#wx.aui.AuiNotebook.GetPageText "Permalink to this definition")
Returns the tab label for the page.



Parameters
**page** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetPageToolTip(self, pageIdx: int) -> str:
        """ 

`GetPageToolTip`(*self*, *pageIdx*)[¶](#wx.aui.AuiNotebook.GetPageToolTip "Permalink to this definition")
Returns the tooltip for the tab label of the page.



Parameters
**pageIdx** (*int*) – 



Return type
`string`





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetSelection(self) -> int:
        """ 

`GetSelection`(*self*)[¶](#wx.aui.AuiNotebook.GetSelection "Permalink to this definition")
Returns the currently selected page.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetTabCtrlFromPoint(self, pt: Union[tuple[int, int], 'Point']) -> 'AuiTabCtrl':
        """ 

`GetTabCtrlFromPoint`(*self*, *pt*)[¶](#wx.aui.AuiNotebook.GetTabCtrlFromPoint "Permalink to this definition")
Returns tab control based on point coordinates inside the tab frame.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
 [wx.aui.AuiTabCtrl](wx.aui.AuiTabCtrl.html#wx-aui-auitabctrl)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def GetTabCtrlHeight(self) -> int:
        """ 

`GetTabCtrlHeight`(*self*)[¶](#wx.aui.AuiNotebook.GetTabCtrlHeight "Permalink to this definition")
Returns the height of the tab control.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def InsertPage(self, *args, **kw) -> bool:
        """ 

`InsertPage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiNotebook.InsertPage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**InsertPage** *(self, page\_idx, page, caption, select=False, bitmap=BitmapBundle())*


[`InsertPage`](#wx.aui.AuiNotebook.InsertPage "wx.aui.AuiNotebook.InsertPage") is similar to AddPage, but allows the ability to specify the insert location.


If the `select` parameter is `True`, calling this will generate a page change event.



Parameters
* **page\_idx** (*int*) –
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **caption** (*string*) –
* **select** (*bool*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –



Return type
*bool*






---

  



**InsertPage** *(self, index, page, text, select, imageId)*


Inserts a new page at the specified position.



Parameters
* **index** (*int*) – Specifies the position for the new page.
* **page** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Specifies the new page.
* **text** (*string*) – Specifies the text for the new page.
* **select** (*bool*) – Specifies whether the page should be selected.
* **imageId** (*int*) – Specifies the optional image index for the new page.



Return type
*bool*



Returns
`True` if successful, `False` otherwise.





New in version 2.9.3.




Note


Do not delete the page, it will be deleted by the book control.




See also


[`AddPage`](#wx.aui.AuiNotebook.AddPage "wx.aui.AuiNotebook.AddPage")





---

  





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def RemovePage(self, page: int) -> bool:
        """ 

`RemovePage`(*self*, *page*)[¶](#wx.aui.AuiNotebook.RemovePage "Permalink to this definition")
Removes a page, without deleting the window pointer.



Parameters
**page** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetArtProvider(self, art: 'aui.AuiTabArt') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.aui.AuiNotebook.SetArtProvider "Permalink to this definition")
Sets the art provider to be used by the notebook.



Parameters
**art** ([*wx.aui.AuiTabArt*](wx.aui.AuiTabArt.html#wx.aui.AuiTabArt "wx.aui.AuiTabArt")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.aui.AuiNotebook.SetFont "Permalink to this definition")
Sets the font for drawing the tab labels, using a bold version of the font for selected tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.aui.AuiNotebook.SetMeasuringFont "Permalink to this definition")
Sets the font for measuring tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.aui.AuiNotebook.SetNormalFont "Permalink to this definition")
Sets the font for drawing unselected tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageBitmap(self, page, bitmap) -> bool:
        """ 

`SetPageBitmap`(*self*, *page*, *bitmap*)[¶](#wx.aui.AuiNotebook.SetPageBitmap "Permalink to this definition")
Sets the bitmap for the page.


To remove a bitmap from the tab caption, pass an empty  [wx.BitmapBundle](wx.BitmapBundle.html#wx-bitmapbundle).



Parameters
* **page** (*int*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageImage(self, n, imageId) -> bool:
        """ 

`SetPageImage`(*self*, *n*, *imageId*)[¶](#wx.aui.AuiNotebook.SetPageImage "Permalink to this definition")
Sets the image index for the given page.


*image* is an index into the image list which was set with `SetImageList` .



Parameters
* **n** (*int*) –
* **imageId** (*int*) –



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageText(self, page, text) -> bool:
        """ 

`SetPageText`(*self*, *page*, *text*)[¶](#wx.aui.AuiNotebook.SetPageText "Permalink to this definition")
Sets the tab label for the page.



Parameters
* **page** (*int*) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetPageToolTip(self, page, text) -> bool:
        """ 

`SetPageToolTip`(*self*, *page*, *text*)[¶](#wx.aui.AuiNotebook.SetPageToolTip "Permalink to this definition")
Sets the tooltip displayed when hovering over the tab label of the page.



Parameters
* **page** (*int*) –
* **text** (*string*) –



Return type
*bool*



Returns
`True` if tooltip was updated, `False` if it failed, e.g. because the page index is invalid.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.aui.AuiNotebook.SetSelectedFont "Permalink to this definition")
Sets the font for drawing selected tab labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetSelection(self, new_page: int) -> int:
        """ 

`SetSelection`(*self*, *new\_page*)[¶](#wx.aui.AuiNotebook.SetSelection "Permalink to this definition")
Sets the page selection.


Calling this method will generate a page change event.



Parameters
**new\_page** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetTabCtrlHeight(self, height: int) -> None:
        """ 

`SetTabCtrlHeight`(*self*, *height*)[¶](#wx.aui.AuiNotebook.SetTabCtrlHeight "Permalink to this definition")
Sets the tab height.


By default, the tab control height is calculated by measuring the text height and bitmap sizes on the tab captions. Calling this method will override that calculation and set the tab control to the specified height parameter. A call to this method will override any call to [`SetUniformBitmapSize`](#wx.aui.AuiNotebook.SetUniformBitmapSize "wx.aui.AuiNotebook.SetUniformBitmapSize") .


Specifying -1 as the height will return the control to its default auto-sizing behaviour.



Parameters
**height** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def SetUniformBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetUniformBitmapSize`(*self*, *size*)[¶](#wx.aui.AuiNotebook.SetUniformBitmapSize "Permalink to this definition")
Ensure that all tabs have the same height, even if some of them don’t have bitmaps.


Passing `wx.DefaultSize` as *size* undoes the effect of a previous call to this function and instructs the control to use dynamic tab height.



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def ShowWindowMenu(self) -> bool:
        """ 

`ShowWindowMenu`(*self*)[¶](#wx.aui.AuiNotebook.ShowWindowMenu "Permalink to this definition")
Shows the window menu for the active tab control associated with this notebook, and returns `True` if a selection was made.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    def Split(self, page, direction) -> None:
        """ 

`Split`(*self*, *page*, *direction*)[¶](#wx.aui.AuiNotebook.Split "Permalink to this definition")
Split performs a split operation programmatically.


The argument *page* indicates the page that will be split off. This page will also become the active page after the split.


The *direction* argument specifies where the pane should go, it should be one of the following: `wx.TOP`, `wx.BOTTOM`, `wx.LEFT`, or `wx.RIGHT`.



Parameters
* **page** (*int*) –
* **direction** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiNotebook.html
        """

    ActiveTabCtrl: 'AuiTabCtrl'  # `ActiveTabCtrl`[¶](#wx.aui.AuiNotebook.ActiveTabCtrl "Permalink to this definition")See [`GetActiveTabCtrl`](#wx.aui.AuiNotebook.GetActiveTabCtrl "wx.aui.AuiNotebook.GetActiveTabCtrl")
    ArtProvider: 'AuiTabArt'  # `ArtProvider`[¶](#wx.aui.AuiNotebook.ArtProvider "Permalink to this definition")See [`GetArtProvider`](#wx.aui.AuiNotebook.GetArtProvider "wx.aui.AuiNotebook.GetArtProvider") and [`SetArtProvider`](#wx.aui.AuiNotebook.SetArtProvider "wx.aui.AuiNotebook.SetArtProvider")
    CurrentPage: 'Window'  # `CurrentPage`[¶](#wx.aui.AuiNotebook.CurrentPage "Permalink to this definition")See [`GetCurrentPage`](#wx.aui.AuiNotebook.GetCurrentPage "wx.aui.AuiNotebook.GetCurrentPage")
    PageCount: int  # `PageCount`[¶](#wx.aui.AuiNotebook.PageCount "Permalink to this definition")See [`GetPageCount`](#wx.aui.AuiNotebook.GetPageCount "wx.aui.AuiNotebook.GetPageCount")
    Selection: int  # `Selection`[¶](#wx.aui.AuiNotebook.Selection "Permalink to this definition")See [`GetSelection`](#wx.aui.AuiNotebook.GetSelection "wx.aui.AuiNotebook.GetSelection") and [`SetSelection`](#wx.aui.AuiNotebook.SetSelection "wx.aui.AuiNotebook.SetSelection")
    TabCtrlHeight: int  # `TabCtrlHeight`[¶](#wx.aui.AuiNotebook.TabCtrlHeight "Permalink to this definition")See [`GetTabCtrlHeight`](#wx.aui.AuiNotebook.GetTabCtrlHeight "wx.aui.AuiNotebook.GetTabCtrlHeight") and [`SetTabCtrlHeight`](#wx.aui.AuiNotebook.SetTabCtrlHeight "wx.aui.AuiNotebook.SetTabCtrlHeight")



AUI_NB_DEFAULT_STYLE: int  # Defined as wx.aui.AUI_NB_TOP | wx.aui.AUI_NB_TAB_SPLIT | wx.aui.AUI_NB_TAB_MOVE | wx.aui.AUI_NB_SCROLL_BUTTONS | wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB | wx.aui.AUI_NB_MIDDLE_CLICK_CLOSE.

AUI_NB_TAB_SPLIT: int  # Allows the tab control to be split by dragging a tab.

AUI_NB_TAB_MOVE: int  # Allows a tab to be moved horizontally by dragging.

AUI_NB_TAB_EXTERNAL_MOVE: int  # Allows a tab to be moved to another tab control.

AUI_NB_TAB_FIXED_WIDTH: int  # With this style, all tabs have the same width.

AUI_NB_SCROLL_BUTTONS: int  # With this style, left and right scroll buttons are displayed.

AUI_NB_WINDOWLIST_BUTTON: int  # With this style, a drop-down list of windows is available.

AUI_NB_CLOSE_BUTTON: int  # With this style, a close button is available on the tab bar.

AUI_NB_CLOSE_ON_ACTIVE_TAB: int  # With this style, the close button is visible on the active tab.

AUI_NB_CLOSE_ON_ALL_TABS: int  # With this style, the close button is visible on all tabs.

AUI_NB_MIDDLE_CLICK_CLOSE: int  # With this style, middle click on a tab closes the tab.

AUI_NB_TOP: int  # With this style, tabs are drawn along the top of the notebook.

AUI_NB_BOTTOM: int  # With this style, tabs are drawn along the bottom of the notebook. ^^

EVT_AUINOTEBOOK_PAGE_CLOSE: int  # A page is about to be closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSE   event.

EVT_AUINOTEBOOK_PAGE_CLOSED: int  # A page has been closed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CLOSED   event.

EVT_AUINOTEBOOK_PAGE_CHANGED: int  # The page selection was changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGED   event.

EVT_AUINOTEBOOK_PAGE_CHANGING: int  # The page selection is about to be changed. Processes a  wxEVT_AUINOTEBOOK_PAGE_CHANGING   event. This event can be vetoed.

EVT_AUINOTEBOOK_BUTTON: int  # The window list button has been pressed. Processes a  wxEVT_AUINOTEBOOK_BUTTON   event.

EVT_AUINOTEBOOK_BEGIN_DRAG: int  # Dragging is about to begin. Processes a  wxEVT_AUINOTEBOOK_BEGIN_DRAG   event.

EVT_AUINOTEBOOK_END_DRAG: int  # Dragging has ended. Processes a  wxEVT_AUINOTEBOOK_END_DRAG   event.

EVT_AUINOTEBOOK_DRAG_MOTION: int  # Emitted during a drag and drop operation. Processes a  wxEVT_AUINOTEBOOK_DRAG_MOTION   event.

EVT_AUINOTEBOOK_ALLOW_DND: int  # Whether to allow a tab to be dropped. Processes a  wxEVT_AUINOTEBOOK_ALLOW_DND   event. This event must be specially allowed.

EVT_AUINOTEBOOK_DRAG_DONE: int  # Notify that the tab has been dragged. Processes a  wxEVT_AUINOTEBOOK_DRAG_DONE   event.

EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN: int  # The middle mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_DOWN   event.

EVT_AUINOTEBOOK_TAB_MIDDLE_UP: int  # The middle mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_MIDDLE_UP   event.

EVT_AUINOTEBOOK_TAB_RIGHT_DOWN: int  # The right mouse button is pressed on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_DOWN   event.

EVT_AUINOTEBOOK_TAB_RIGHT_UP: int  # The right mouse button is released on a tab. Processes a  wxEVT_AUINOTEBOOK_TAB_RIGHT_UP   event.

EVT_AUINOTEBOOK_BG_DCLICK: int  # Double clicked on the tabs background area. Processes a  wxEVT_AUINOTEBOOK_BG_DCLICK   event. ^^

NOT_FOUND: int

TOP: int

BOTTOM: int

LEFT: int

RIGHT: int

class AuiNotebookEvent(BookCtrlEvent):
    """ **Possible constructors**:



```
AuiNotebookEvent(command_type=wxEVT_NULL, win_id=0)

```


This class is used by the events generated by AuiNotebook.


  


        Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*)[¶](#wx.aui.AuiNotebookEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
        """

    def Clone(self) -> 'Event':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiNotebookEvent.Clone "Permalink to this definition")

Return type
*Event*






            Source: https://docs.wxpython.org/wx.aui.AuiNotebookEvent.html
        """



class AuiDefaultTabArt(AuiTabArt):
    """ **Possible constructors**:



```
AuiDefaultTabArt()

```


Default art provider for AuiNotebook.


  


        Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiDefaultTabArt.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def Clone(self) -> 'AuiTabArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiDefaultTabArt.Clone "Permalink to this definition")
Clones the art object.



Return type
 [wx.aui.AuiTabArt](wx.aui.AuiTabArt.html#wx-aui-auitabart)






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiDefaultTabArt.DrawBackground "Permalink to this definition")
Draws a background on the given area.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *in\_rect*, *bitmap\_id*, *button\_state*, *orientation*, *out\_rect*)[¶](#wx.aui.AuiDefaultTabArt.DrawButton "Permalink to this definition")
Draws a button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **bitmap\_id** (*int*) –
* **button\_state** (*int*) –
* **orientation** (*int*) –
* **out\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *rect*, *close\_button\_state*, *out\_tab\_rect*, *out\_button\_rect*, *x\_extent*)[¶](#wx.aui.AuiDefaultTabArt.DrawTab "Permalink to this definition")
Draws a tab.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **page** ([*wx.aui.AuiNotebookPage*](wx.aui.AuiNotebookPage.html#wx.aui.AuiNotebookPage "wx.aui.AuiNotebookPage")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **close\_button\_state** (*int*) –
* **out\_tab\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **out\_button\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **x\_extent** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetBestTabCtrlSize(self) -> int:
        """ 

`GetBestTabCtrlSize`(*self*)[¶](#wx.aui.AuiDefaultTabArt.GetBestTabCtrlSize "Permalink to this definition")
Returns the tab control size.



Parameters
**``** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetIndentSize(self) -> int:
        """ 

`GetIndentSize`(*self*)[¶](#wx.aui.AuiDefaultTabArt.GetIndentSize "Permalink to this definition")
Returns the indent size.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, x_extent) -> 'Size':
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *x\_extent*)[¶](#wx.aui.AuiDefaultTabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and state.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **caption** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **active** (*bool*) –
* **close\_button\_state** (*int*) –
* **x\_extent** (*int*) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetActiveColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetActiveColour`(*self*, *colour*)[¶](#wx.aui.AuiDefaultTabArt.SetActiveColour "Permalink to this definition")
Sets the colour of the selected tab.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.aui.AuiDefaultTabArt.SetColour "Permalink to this definition")
Sets the colour of the inactive tabs.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiDefaultTabArt.SetFlags "Permalink to this definition")
Sets flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.aui.AuiDefaultTabArt.SetMeasuringFont "Permalink to this definition")
Sets the font used for calculating measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.aui.AuiDefaultTabArt.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.aui.AuiDefaultTabArt.SetSelectedFont "Permalink to this definition")
Sets the font for drawing text for selected UI elements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *wnd=None*)[¶](#wx.aui.AuiDefaultTabArt.SetSizingInfo "Permalink to this definition")
Sets sizing information.


The *wnd* argument is only present in wxWidgets 3.1.6 and newer and is required, it only has `None` default value for compatibility reasons.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **tab\_count** (*int*) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    def ShowDropDown(self, wnd, items, activeIdx) -> int:
        """ 

`ShowDropDown`(*self*, *wnd*, *items*, *activeIdx*)[¶](#wx.aui.AuiDefaultTabArt.ShowDropDown "Permalink to this definition")

Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **items** (*AuiNotebookPageArray*) –
* **activeIdx** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultTabArt.html
        """

    IndentSize: int  # `IndentSize`[¶](#wx.aui.AuiDefaultTabArt.IndentSize "Permalink to this definition")See [`GetIndentSize`](#wx.aui.AuiDefaultTabArt.GetIndentSize "wx.aui.AuiDefaultTabArt.GetIndentSize")



class AuiMDIClientWindow(AuiNotebook):
    """ **Possible constructors**:



```
AuiMDIClientWindow()

AuiMDIClientWindow(parent, style=0)

```


  


        Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiMDIClientWindow.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, parent, style=0)*



Parameters
* **parent** ([*wx.aui.AuiMDIParentFrame*](wx.aui.AuiMDIParentFrame.html#wx.aui.AuiMDIParentFrame "wx.aui.AuiMDIParentFrame")) –
* **style** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def CreateClient(self, parent, style=VSCROLL|HSCROLL) -> bool:
        """ 

`CreateClient`(*self*, *parent*, *style=VSCROLL|HSCROLL*)[¶](#wx.aui.AuiMDIClientWindow.CreateClient "Permalink to this definition")

Parameters
* **parent** ([*wx.aui.AuiMDIParentFrame*](wx.aui.AuiMDIParentFrame.html#wx.aui.AuiMDIParentFrame "wx.aui.AuiMDIParentFrame")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def GetActiveChild(self) -> 'AuiMDIChildFrame':
        """ 

`GetActiveChild`(*self*)[¶](#wx.aui.AuiMDIClientWindow.GetActiveChild "Permalink to this definition")

Return type
 [wx.aui.AuiMDIChildFrame](wx.aui.AuiMDIChildFrame.html#wx-aui-auimdichildframe)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiMDIClientWindow.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def SetActiveChild(self, pChildFrame: 'aui.AuiMDIChildFrame') -> None:
        """ 

`SetActiveChild`(*self*, *pChildFrame*)[¶](#wx.aui.AuiMDIClientWindow.SetActiveChild "Permalink to this definition")

Parameters
**pChildFrame** ([*wx.aui.AuiMDIChildFrame*](wx.aui.AuiMDIChildFrame.html#wx.aui.AuiMDIChildFrame "wx.aui.AuiMDIChildFrame")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    def SetSelection(self, new_page: int) -> int:
        """ 

`SetSelection`(*self*, *new\_page*)[¶](#wx.aui.AuiMDIClientWindow.SetSelection "Permalink to this definition")
Sets the page selection.


Calling this method will generate a page change event.



Parameters
**new\_page** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIClientWindow.html
        """

    ActiveChild: 'AuiMDIChildFrame'  # `ActiveChild`[¶](#wx.aui.AuiMDIClientWindow.ActiveChild "Permalink to this definition")See [`GetActiveChild`](#wx.aui.AuiMDIClientWindow.GetActiveChild "wx.aui.AuiMDIClientWindow.GetActiveChild") and [`SetActiveChild`](#wx.aui.AuiMDIClientWindow.SetActiveChild "wx.aui.AuiMDIClientWindow.SetActiveChild")



class AuiTabCtrl:
    """ **Possible constructors**:



```
AuiTabCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
           style=0)

```


  


        Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
    """
    def __init__(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> None:
        """ 

`__init__`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.aui.AuiTabCtrl.__init__ "Permalink to this definition")

Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** (`Point`) –
* **size** (`Size`) –
* **style** (*long*) –






            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiTabCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """

    def IsDragging(self) -> bool:
        """ 

`IsDragging`(*self*)[¶](#wx.aui.AuiTabCtrl.IsDragging "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiTabCtrl.html
        """



class AuiTabArt:
    """ **Possible constructors**:



```
AuiTabArt()

```


Tab art provider defines all the drawing functions used by
AuiNotebook.


  


        Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiTabArt.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def Clone(self) -> 'AuiTabArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiTabArt.Clone "Permalink to this definition")
Clones the art object.



Return type
 [wx.aui.AuiTabArt](#wx-aui-auitabart)






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiTabArt.DrawBackground "Permalink to this definition")
Draws a background on the given area.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *in\_rect*, *bitmap\_id*, *button\_state*, *orientation*, *out\_rect*)[¶](#wx.aui.AuiTabArt.DrawButton "Permalink to this definition")
Draws a button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **bitmap\_id** (*int*) –
* **button\_state** (*int*) –
* **orientation** (*int*) –
* **out\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *rect*, *close\_button\_state*, *out\_tab\_rect*, *out\_button\_rect*, *x\_extent*)[¶](#wx.aui.AuiTabArt.DrawTab "Permalink to this definition")
Draws a tab.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **page** ([*wx.aui.AuiNotebookPage*](wx.aui.AuiNotebookPage.html#wx.aui.AuiNotebookPage "wx.aui.AuiNotebookPage")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **close\_button\_state** (*int*) –
* **out\_tab\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **out\_button\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **x\_extent** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetBestTabCtrlSize(self) -> int:
        """ 

`GetBestTabCtrlSize`(*self*)[¶](#wx.aui.AuiTabArt.GetBestTabCtrlSize "Permalink to this definition")
Returns the tab control size.



Parameters
**``** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetIndentSize(self) -> int:
        """ 

`GetIndentSize`(*self*)[¶](#wx.aui.AuiTabArt.GetIndentSize "Permalink to this definition")
Returns the indent size.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, close_button_state, x_extent) -> 'Size':
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *close\_button\_state*, *x\_extent*)[¶](#wx.aui.AuiTabArt.GetTabSize "Permalink to this definition")
Returns the tab size for the given caption, bitmap and state.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **caption** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **active** (*bool*) –
* **close\_button\_state** (*int*) –
* **x\_extent** (*int*) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetActiveColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetActiveColour`(*self*, *colour*)[¶](#wx.aui.AuiTabArt.SetActiveColour "Permalink to this definition")
Sets the colour of the selected tab.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.aui.AuiTabArt.SetColour "Permalink to this definition")
Sets the colour of the inactive tabs.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiTabArt.SetFlags "Permalink to this definition")
Sets flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.aui.AuiTabArt.SetMeasuringFont "Permalink to this definition")
Sets the font used for calculating measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.aui.AuiTabArt.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.aui.AuiTabArt.SetSelectedFont "Permalink to this definition")
Sets the font for drawing text for selected UI elements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *wnd=None*)[¶](#wx.aui.AuiTabArt.SetSizingInfo "Permalink to this definition")
Sets sizing information.


The *wnd* argument is only present in wxWidgets 3.1.6 and newer and is required, it only has `None` default value for compatibility reasons.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **tab\_count** (*int*) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.aui.AuiTabArt.html
        """

    IndentSize: int  # `IndentSize`[¶](#wx.aui.AuiTabArt.IndentSize "Permalink to this definition")See [`GetIndentSize`](#wx.aui.AuiTabArt.GetIndentSize "wx.aui.AuiTabArt.GetIndentSize")



class AuiToolBar(Control):
    """ **Possible constructors**:



```
AuiToolBar()

AuiToolBar(parent, id=ID_ANY, position=DefaultPosition,
           size=DefaultSize, style=AUI_TB_DEFAULT_STYLE)

```


AuiToolBar is a dockable toolbar, part of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiToolBar.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor, use [`Create`](#wx.aui.AuiToolBar.Create "wx.aui.AuiToolBar.Create") later.



New in version 2.9.5.





---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, position=DefaultPosition, size=DefaultSize, style=AUI\_TB\_DEFAULT\_STYLE)*


Constructor creating and initializing the object.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddControl(self, control, label="") -> 'AuiToolBarItem':
        """ 

`AddControl`(*self*, *control*, *label=""*)[¶](#wx.aui.AuiToolBar.AddControl "Permalink to this definition")

Parameters
* **control** ([*wx.Control*](wx.Control.html#wx.Control "wx.Control")) –
* **label** (*string*) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddLabel(self, toolId, label="", width=-1) -> 'AuiToolBarItem':
        """ 

`AddLabel`(*self*, *toolId*, *label=""*, *width=-1*)[¶](#wx.aui.AuiToolBar.AddLabel "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **label** (*string*) –
* **width** (*int*) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddSeparator(self) -> 'AuiToolBarItem':
        """ 

`AddSeparator`(*self*)[¶](#wx.aui.AuiToolBar.AddSeparator "Permalink to this definition")

Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddSpacer(self, pixels: int) -> 'AuiToolBarItem':
        """ 

`AddSpacer`(*self*, *pixels*)[¶](#wx.aui.AuiToolBar.AddSpacer "Permalink to this definition")

Parameters
**pixels** (*int*) – 



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddStretchSpacer(self, proportion: int=1) -> 'AuiToolBarItem':
        """ 

`AddStretchSpacer`(*self*, *proportion=1*)[¶](#wx.aui.AuiToolBar.AddStretchSpacer "Permalink to this definition")

Parameters
**proportion** (*int*) – 



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def AddTool(self, *args, **kw) -> 'AuiToolBarItem':
        """ 

`AddTool`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiToolBar.AddTool "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddTool** *(self, toolId, label, bitmap, short\_help\_string=””, kind=ITEM\_NORMAL)*



Parameters
* **toolId** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **short\_help\_string** (*string*) –
* **kind** ([*ItemKind*](wx.ItemKind.enumeration.html "ItemKind")) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






---

  



**AddTool** *(self, toolId, label, bitmap, disabled\_bitmap, kind, short\_help\_string, long\_help\_string, client\_data)*



Parameters
* **toolId** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **disabled\_bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **kind** ([*ItemKind*](wx.ItemKind.enumeration.html "ItemKind")) –
* **short\_help\_string** (*string*) –
* **long\_help\_string** (*string*) –
* **client\_data** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






---

  



**AddTool** *(self, toolId, bitmap, disabled\_bitmap, toggle=False, client\_data=None, short\_help\_string=””, long\_help\_string=””)*



Parameters
* **toolId** (*int*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **disabled\_bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **toggle** (*bool*) –
* **client\_data** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **short\_help\_string** (*string*) –
* **long\_help\_string** (*string*) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.aui.AuiToolBar.Clear "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def ClearTools(self) -> None:
        """ 

`ClearTools`(*self*)[¶](#wx.aui.AuiToolBar.ClearTools "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=AUI_TB_DEFAULT_STYLE) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=AUI\_TB\_DEFAULT\_STYLE*)[¶](#wx.aui.AuiToolBar.Create "Permalink to this definition")
Really create  [wx.aui.AuiToolBar](#wx-aui-auitoolbar) created using default constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DeleteByIndex(self, idx: int) -> bool:
        """ 

`DeleteByIndex`(*self*, *idx*)[¶](#wx.aui.AuiToolBar.DeleteByIndex "Permalink to this definition")
Removes the tool at the given position from the toolbar.


Note that if this tool was added by [`AddControl`](#wx.aui.AuiToolBar.AddControl "wx.aui.AuiToolBar.AddControl") , the associated control is *not* deleted and must either be reused (e.g. by reparenting it under a different window) or destroyed by caller. If this behaviour is unwanted, prefer using [`DestroyToolByIndex`](#wx.aui.AuiToolBar.DestroyToolByIndex "wx.aui.AuiToolBar.DestroyToolByIndex") instead.



Parameters
**idx** (*int*) – The index, or position, of a previously added tool.



Return type
*bool*



Returns
`True` if the tool was removed or `False` otherwise, e.g. if the provided index is out of range.






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DeleteTool(self, toolId: int) -> bool:
        """ 

`DeleteTool`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.DeleteTool "Permalink to this definition")
Removes the tool with the given `ID` from the toolbar.


Note that if this tool was added by [`AddControl`](#wx.aui.AuiToolBar.AddControl "wx.aui.AuiToolBar.AddControl") , the associated control is *not* deleted and must either be reused (e.g. by reparenting it under a different window) or destroyed by caller. If this behaviour is unwanted, prefer using [`DestroyTool`](#wx.aui.AuiToolBar.DestroyTool "wx.aui.AuiToolBar.DestroyTool") instead.



Parameters
**toolId** (*int*) – `ID` of a previously added tool.



Return type
*bool*



Returns
`True` if the tool was removed or `False` otherwise, e.g. if the tool with the given `ID` was not found.






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DestroyTool(self, toolId: int) -> bool:
        """ 

`DestroyTool`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.DestroyTool "Permalink to this definition")
Destroys the tool with the given `ID` and its associated window, if any.



Parameters
**toolId** (*int*) – `ID` of a previously added tool.



Return type
*bool*



Returns
`True` if the tool was destroyed or `False` otherwise, e.g. if the tool with the given `ID` was not found.





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def DestroyToolByIndex(self, idx: int) -> bool:
        """ 

`DestroyToolByIndex`(*self*, *idx*)[¶](#wx.aui.AuiToolBar.DestroyToolByIndex "Permalink to this definition")
Destroys the tool at the given position and its associated window, if any.



Parameters
**idx** (*int*) – The index, or position, of a previously added tool.



Return type
*bool*



Returns
`True` if the tool was destroyed or `False` otherwise, e.g. if the provided index is out of range.






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def EnableTool(self, toolId, state) -> None:
        """ 

`EnableTool`(*self*, *toolId*, *state*)[¶](#wx.aui.AuiToolBar.EnableTool "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **state** (*bool*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindControl(self, window_id: int) -> 'Control':
        """ 

`FindControl`(*self*, *window\_id*)[¶](#wx.aui.AuiToolBar.FindControl "Permalink to this definition")

Parameters
**window\_id** (*int*) – 



Return type
*Control*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindTool(self, toolId: int) -> 'AuiToolBarItem':
        """ 

`FindTool`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.FindTool "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindToolByIndex(self, idx: int) -> 'AuiToolBarItem':
        """ 

`FindToolByIndex`(*self*, *idx*)[¶](#wx.aui.AuiToolBar.FindToolByIndex "Permalink to this definition")

Parameters
**idx** (*int*) – 



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def FindToolByPosition(self, x, y) -> 'AuiToolBarItem':
        """ 

`FindToolByPosition`(*self*, *x*, *y*)[¶](#wx.aui.AuiToolBar.FindToolByPosition "Permalink to this definition")

Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetArtProvider(self) -> 'AuiToolBarArt':
        """ 

`GetArtProvider`(*self*)[¶](#wx.aui.AuiToolBar.GetArtProvider "Permalink to this definition")

Return type
 [wx.aui.AuiToolBarArt](wx.aui.AuiToolBarArt.html#wx-aui-auitoolbarart)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiToolBar.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetGripperVisible(self) -> bool:
        """ 

`GetGripperVisible`(*self*)[¶](#wx.aui.AuiToolBar.GetGripperVisible "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetHintSize(self, dock_direction: int) -> 'Size':
        """ 

`GetHintSize`(*self*, *dock\_direction*)[¶](#wx.aui.AuiToolBar.GetHintSize "Permalink to this definition")
get size of hint rectangle for a particular dock location



Parameters
**dock\_direction** (*int*) – 



Return type
`Size`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetOverflowVisible(self) -> bool:
        """ 

`GetOverflowVisible`(*self*)[¶](#wx.aui.AuiToolBar.GetOverflowVisible "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBarFits(self) -> bool:
        """ 

`GetToolBarFits`(*self*)[¶](#wx.aui.AuiToolBar.GetToolBarFits "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBitmap(self, toolId: int) -> 'Bitmap':
        """ 

`GetToolBitmap`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolBitmap "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBitmapSize(self) -> 'Size':
        """ 

`GetToolBitmapSize`(*self*)[¶](#wx.aui.AuiToolBar.GetToolBitmapSize "Permalink to this definition")

Return type
`Size`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolBorderPadding(self) -> int:
        """ 

`GetToolBorderPadding`(*self*)[¶](#wx.aui.AuiToolBar.GetToolBorderPadding "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolCount(self) -> int:
        """ 

`GetToolCount`(*self*)[¶](#wx.aui.AuiToolBar.GetToolCount "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolDropDown(self, toolId: int) -> bool:
        """ 

`GetToolDropDown`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolDropDown "Permalink to this definition")
Returns whether the specified toolbar item has an associated drop down button.



Parameters
**toolId** (*int*) – 



Return type
*bool*





See also


[`wx.aui.AuiToolBarItem.HasDropDown`](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem.HasDropDown "wx.aui.AuiToolBarItem.HasDropDown")





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolEnabled(self, toolId: int) -> bool:
        """ 

`GetToolEnabled`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolEnabled "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolFits(self, toolId: int) -> bool:
        """ 

`GetToolFits`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolFits "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolFitsByIndex(self, toolId: int) -> bool:
        """ 

`GetToolFitsByIndex`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolFitsByIndex "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolIndex(self, toolId: int) -> int:
        """ 

`GetToolIndex`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolIndex "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolLabel(self, toolId: int) -> str:
        """ 

`GetToolLabel`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolLabel "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolLongHelp(self, toolId: int) -> str:
        """ 

`GetToolLongHelp`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolLongHelp "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolPacking(self) -> int:
        """ 

`GetToolPacking`(*self*)[¶](#wx.aui.AuiToolBar.GetToolPacking "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolPos(self, toolId: int) -> int:
        """ 

`GetToolPos`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolPos "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolProportion(self, toolId: int) -> int:
        """ 

`GetToolProportion`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolProportion "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolRect(self, toolId: int) -> 'Rect':
        """ 

`GetToolRect`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolRect "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
`Rect`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolSeparation(self) -> int:
        """ 

`GetToolSeparation`(*self*)[¶](#wx.aui.AuiToolBar.GetToolSeparation "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolShortHelp(self, toolId: int) -> str:
        """ 

`GetToolShortHelp`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolShortHelp "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolSticky(self, toolId: int) -> bool:
        """ 

`GetToolSticky`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolSticky "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolTextOrientation(self) -> int:
        """ 

`GetToolTextOrientation`(*self*)[¶](#wx.aui.AuiToolBar.GetToolTextOrientation "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetToolToggled(self, toolId: int) -> bool:
        """ 

`GetToolToggled`(*self*, *toolId*)[¶](#wx.aui.AuiToolBar.GetToolToggled "Permalink to this definition")

Parameters
**toolId** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def GetWindowStyleFlag(self) -> int:
        """ 

`GetWindowStyleFlag`(*self*)[¶](#wx.aui.AuiToolBar.GetWindowStyleFlag "Permalink to this definition")
Gets the window style that was passed to the constructor or [`Create`](#wx.aui.AuiToolBar.Create "wx.aui.AuiToolBar.Create") method.


`GetWindowStyle` is another name for the same function.



Return type
*long*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def IsPaneValid(self, pane: 'aui.AuiPaneInfo') -> bool:
        """ 

`IsPaneValid`(*self*, *pane*)[¶](#wx.aui.AuiToolBar.IsPaneValid "Permalink to this definition")

Parameters
**pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.aui.AuiToolBar.Realize "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetArtProvider(self, art: 'aui.AuiToolBarArt') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.aui.AuiToolBar.SetArtProvider "Permalink to this definition")

Parameters
**art** ([*wx.aui.AuiToolBarArt*](wx.aui.AuiToolBarArt.html#wx.aui.AuiToolBarArt "wx.aui.AuiToolBarArt")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetCustomOverflowItems(self, prepend, append) -> None:
        """ 

`SetCustomOverflowItems`(*self*, *prepend*, *append*)[¶](#wx.aui.AuiToolBar.SetCustomOverflowItems "Permalink to this definition")
Add toolbar items that are always displayed in the overflow menu.


If there are custom items set, then the overflow menu will be displayed even if there are no items from the main toolbar that overflow.



Parameters
* **prepend** (*AuiToolBarItemArray*) – are the items to show before any overflow items
* **append** (*AuiToolBarItemArray*) – are the items to show after any overflow items





Note


The toolbar must have the `AUI_TB_OVERFLOW` style.





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.aui.AuiToolBar.SetFont "Permalink to this definition")
Sets the font for this window.


This function should not be called for the parent window if you don’t want its font to be inherited by its children, use `SetOwnFont` instead in this case and see `InheritAttributes` for more explanations.


Please notice that the given font is not automatically used for  [wx.PaintDC](wx.PaintDC.html#wx-paintdc) objects associated with this window, you need to call [`wx.DC.SetFont`](wx.DC.html#wx.DC.SetFont "wx.DC.SetFont") too. However this font is used by any standard controls for drawing their text as well as by `GetTextExtent` .



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – Font to associate with this window, pass NullFont to reset to the default font.



Return type
*bool*



Returns
`True` if the font was really changed, `False` if it was already set to this font and nothing was done.





See also


`GetFont` , `InheritAttributes`





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetGripperVisible(self, visible: bool) -> None:
        """ 

`SetGripperVisible`(*self*, *visible*)[¶](#wx.aui.AuiToolBar.SetGripperVisible "Permalink to this definition")

Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ 

`SetMargins`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiToolBar.SetMargins "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetMargins** *(self, size)*



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






---

  



**SetMargins** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –






---

  



**SetMargins** *(self, left, right, top, bottom)*



Parameters
* **left** (*int*) –
* **right** (*int*) –
* **top** (*int*) –
* **bottom** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetOverflowVisible(self, visible: bool) -> None:
        """ 

`SetOverflowVisible`(*self*, *visible*)[¶](#wx.aui.AuiToolBar.SetOverflowVisible "Permalink to this definition")

Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBitmap(self, toolId, bitmap) -> None:
        """ 

`SetToolBitmap`(*self*, *toolId*, *bitmap*)[¶](#wx.aui.AuiToolBar.SetToolBitmap "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBitmapSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetToolBitmapSize`(*self*, *size*)[¶](#wx.aui.AuiToolBar.SetToolBitmapSize "Permalink to this definition")

Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolBorderPadding(self, padding: int) -> None:
        """ 

`SetToolBorderPadding`(*self*, *padding*)[¶](#wx.aui.AuiToolBar.SetToolBorderPadding "Permalink to this definition")

Parameters
**padding** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolDropDown(self, toolId, dropdown) -> None:
        """ 

`SetToolDropDown`(*self*, *toolId*, *dropdown*)[¶](#wx.aui.AuiToolBar.SetToolDropDown "Permalink to this definition")
Set whether the specified toolbar item has a drop down button.


This is only valid for `wx.ITEM_NORMAL` tools.



Parameters
* **toolId** (*int*) –
* **dropdown** (*bool*) –





See also


[`wx.aui.AuiToolBarItem.SetHasDropDown`](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem.SetHasDropDown "wx.aui.AuiToolBarItem.SetHasDropDown")





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolLabel(self, toolId, label) -> None:
        """ 

`SetToolLabel`(*self*, *toolId*, *label*)[¶](#wx.aui.AuiToolBar.SetToolLabel "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **label** (*string*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolLongHelp(self, toolId, help_string) -> None:
        """ 

`SetToolLongHelp`(*self*, *toolId*, *help\_string*)[¶](#wx.aui.AuiToolBar.SetToolLongHelp "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **help\_string** (*string*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolPacking(self, packing: int) -> None:
        """ 

`SetToolPacking`(*self*, *packing*)[¶](#wx.aui.AuiToolBar.SetToolPacking "Permalink to this definition")

Parameters
**packing** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolProportion(self, toolId, proportion) -> None:
        """ 

`SetToolProportion`(*self*, *toolId*, *proportion*)[¶](#wx.aui.AuiToolBar.SetToolProportion "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **proportion** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolSeparation(self, separation: int) -> None:
        """ 

`SetToolSeparation`(*self*, *separation*)[¶](#wx.aui.AuiToolBar.SetToolSeparation "Permalink to this definition")

Parameters
**separation** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolShortHelp(self, toolId, help_string) -> None:
        """ 

`SetToolShortHelp`(*self*, *toolId*, *help\_string*)[¶](#wx.aui.AuiToolBar.SetToolShortHelp "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **help\_string** (*string*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolSticky(self, toolId, sticky) -> None:
        """ 

`SetToolSticky`(*self*, *toolId*, *sticky*)[¶](#wx.aui.AuiToolBar.SetToolSticky "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **sticky** (*bool*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetToolTextOrientation(self, orientation: int) -> None:
        """ 

`SetToolTextOrientation`(*self*, *orientation*)[¶](#wx.aui.AuiToolBar.SetToolTextOrientation "Permalink to this definition")

Parameters
**orientation** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def SetWindowStyleFlag(self, style: int) -> None:
        """ 

`SetWindowStyleFlag`(*self*, *style*)[¶](#wx.aui.AuiToolBar.SetWindowStyleFlag "Permalink to this definition")
Sets the style of the window.


Please note that some styles cannot be changed after the window creation and that `Refresh` might need to be called after changing the others for the change to take place immediately.


See [Window styles](window_styles_overview.html#window-styles) for more information about flags.



Parameters
**style** (*long*) – 





See also


[`GetWindowStyleFlag`](#wx.aui.AuiToolBar.GetWindowStyleFlag "wx.aui.AuiToolBar.GetWindowStyleFlag")





            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    def ToggleTool(self, toolId, state) -> None:
        """ 

`ToggleTool`(*self*, *toolId*, *state*)[¶](#wx.aui.AuiToolBar.ToggleTool "Permalink to this definition")

Parameters
* **toolId** (*int*) –
* **state** (*bool*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBar.html
        """

    ArtProvider: 'AuiToolBarArt'  # `ArtProvider`[¶](#wx.aui.AuiToolBar.ArtProvider "Permalink to this definition")See [`GetArtProvider`](#wx.aui.AuiToolBar.GetArtProvider "wx.aui.AuiToolBar.GetArtProvider") and [`SetArtProvider`](#wx.aui.AuiToolBar.SetArtProvider "wx.aui.AuiToolBar.SetArtProvider")
    GripperVisible: bool  # `GripperVisible`[¶](#wx.aui.AuiToolBar.GripperVisible "Permalink to this definition")See [`GetGripperVisible`](#wx.aui.AuiToolBar.GetGripperVisible "wx.aui.AuiToolBar.GetGripperVisible") and [`SetGripperVisible`](#wx.aui.AuiToolBar.SetGripperVisible "wx.aui.AuiToolBar.SetGripperVisible")
    OverflowVisible: bool  # `OverflowVisible`[¶](#wx.aui.AuiToolBar.OverflowVisible "Permalink to this definition")See [`GetOverflowVisible`](#wx.aui.AuiToolBar.GetOverflowVisible "wx.aui.AuiToolBar.GetOverflowVisible") and [`SetOverflowVisible`](#wx.aui.AuiToolBar.SetOverflowVisible "wx.aui.AuiToolBar.SetOverflowVisible")
    ToolBarFits: bool  # `ToolBarFits`[¶](#wx.aui.AuiToolBar.ToolBarFits "Permalink to this definition")See [`GetToolBarFits`](#wx.aui.AuiToolBar.GetToolBarFits "wx.aui.AuiToolBar.GetToolBarFits")
    ToolBitmapSize: 'Size'  # `ToolBitmapSize`[¶](#wx.aui.AuiToolBar.ToolBitmapSize "Permalink to this definition")See [`GetToolBitmapSize`](#wx.aui.AuiToolBar.GetToolBitmapSize "wx.aui.AuiToolBar.GetToolBitmapSize") and [`SetToolBitmapSize`](#wx.aui.AuiToolBar.SetToolBitmapSize "wx.aui.AuiToolBar.SetToolBitmapSize")
    ToolBorderPadding: int  # `ToolBorderPadding`[¶](#wx.aui.AuiToolBar.ToolBorderPadding "Permalink to this definition")See [`GetToolBorderPadding`](#wx.aui.AuiToolBar.GetToolBorderPadding "wx.aui.AuiToolBar.GetToolBorderPadding") and [`SetToolBorderPadding`](#wx.aui.AuiToolBar.SetToolBorderPadding "wx.aui.AuiToolBar.SetToolBorderPadding")
    ToolCount: int  # `ToolCount`[¶](#wx.aui.AuiToolBar.ToolCount "Permalink to this definition")See [`GetToolCount`](#wx.aui.AuiToolBar.GetToolCount "wx.aui.AuiToolBar.GetToolCount")
    ToolPacking: int  # `ToolPacking`[¶](#wx.aui.AuiToolBar.ToolPacking "Permalink to this definition")See [`GetToolPacking`](#wx.aui.AuiToolBar.GetToolPacking "wx.aui.AuiToolBar.GetToolPacking") and [`SetToolPacking`](#wx.aui.AuiToolBar.SetToolPacking "wx.aui.AuiToolBar.SetToolPacking")
    ToolSeparation: int  # `ToolSeparation`[¶](#wx.aui.AuiToolBar.ToolSeparation "Permalink to this definition")See [`GetToolSeparation`](#wx.aui.AuiToolBar.GetToolSeparation "wx.aui.AuiToolBar.GetToolSeparation") and [`SetToolSeparation`](#wx.aui.AuiToolBar.SetToolSeparation "wx.aui.AuiToolBar.SetToolSeparation")
    ToolTextOrientation: int  # `ToolTextOrientation`[¶](#wx.aui.AuiToolBar.ToolTextOrientation "Permalink to this definition")See [`GetToolTextOrientation`](#wx.aui.AuiToolBar.GetToolTextOrientation "wx.aui.AuiToolBar.GetToolTextOrientation") and [`SetToolTextOrientation`](#wx.aui.AuiToolBar.SetToolTextOrientation "wx.aui.AuiToolBar.SetToolTextOrientation")
    WindowStyleFlag: int  # `WindowStyleFlag`[¶](#wx.aui.AuiToolBar.WindowStyleFlag "Permalink to this definition")See [`GetWindowStyleFlag`](#wx.aui.AuiToolBar.GetWindowStyleFlag "wx.aui.AuiToolBar.GetWindowStyleFlag") and [`SetWindowStyleFlag`](#wx.aui.AuiToolBar.SetWindowStyleFlag "wx.aui.AuiToolBar.SetWindowStyleFlag")



AUI_TB_TEXT: int  # Display the label strings on the toolbar buttons.

AUI_TB_NO_TOOLTIPS: int  # Do not show tooltips for the toolbar items.

AUI_TB_NO_AUTORESIZE: int  # Do not automatically resize the toolbar when new tools are added.

AUI_TB_GRIPPER: int  # Show the toolbar’s gripper control. If the toolbar is added to an AUI pane that contains a gripper, this style will be automatically set.

AUI_TB_OVERFLOW: int  # Show an overflow menu containing toolbar items that can’t fit on the toolbar if it is too small.

AUI_TB_VERTICAL: int  # Using this style forces the toolbar to be vertical and be only dockable to the left or right sides of the window whereas by default it can be horizontal or vertical and be docked anywhere.

AUI_TB_HORZ_LAYOUT: int

AUI_TB_HORIZONTAL: int  # Analogous to wx.aui.AUI_TB_VERTICAL, but forces the toolbar to be horizontal.

AUI_TB_PLAIN_BACKGROUND: int  # Draw a plain background (based on parent) instead of the default gradient background.

AUI_TB_HORZ_TEXT: int  # Equivalent to wx.aui.AUI_TB_HORZ_LAYOUT | wx.aui.AUI_TB_TEXT

AUI_TB_DEFAULT_STYLE: int  # The default is to have no styles. ^^

EVT_AUITOOLBAR_TOOL_DROPDOWN: int  # Process a wxEVT_AUITOOLBAR_TOOL_DROPDOWN event

EVT_AUITOOLBAR_OVERFLOW_CLICK: int  # Process a wxEVT_AUITOOLBAR_OVERFLOW_CLICK event

EVT_AUITOOLBAR_RIGHT_CLICK: int  # Process a wxEVT_AUITOOLBAR_RIGHT_CLICK event

EVT_AUITOOLBAR_MIDDLE_CLICK: int  # Process a wxEVT_AUITOOLBAR_MIDDLE_CLICK event

EVT_AUITOOLBAR_BEGIN_DRAG: int  # Process a wxEVT_AUITOOLBAR_BEGIN_DRAG event ^^

ITEM_NORMAL: int

class AuiManagerEvent(Event):
    """ **Possible constructors**:



```
AuiManagerEvent(type=wxEVT_NULL)

```


Event used to indicate various actions taken with AuiManager.


  


        Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
    """
    def __init__(self, type: int=wxEVT_NULL) -> None:
        """ 

`__init__`(*self*, *type=wxEVT\_NULL*)[¶](#wx.aui.AuiManagerEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
**type** (*wx.EventType*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def CanVeto(self) -> bool:
        """ 

`CanVeto`(*self*)[¶](#wx.aui.AuiManagerEvent.CanVeto "Permalink to this definition")

Return type
*bool*



Returns
`True` if this event can be vetoed.





See also


[`Veto`](#wx.aui.AuiManagerEvent.Veto "wx.aui.AuiManagerEvent.Veto")





            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetButton(self) -> int:
        """ 

`GetButton`(*self*)[¶](#wx.aui.AuiManagerEvent.GetButton "Permalink to this definition")

Return type
*int*



Returns
The `ID` of the button that was clicked.






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetDC(self) -> 'DC':
        """ 

`GetDC`(*self*)[¶](#wx.aui.AuiManagerEvent.GetDC "Permalink to this definition")

Return type
[`DC`](#wx.aui.AuiManagerEvent.DC "wx.aui.AuiManagerEvent.DC")





Todo


What is this?





            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetManager(self) -> 'AuiManager':
        """ 

`GetManager`(*self*)[¶](#wx.aui.AuiManagerEvent.GetManager "Permalink to this definition")

Return type
 [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager)



Returns
The  [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager) this event is associated with.






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetPane(self) -> 'AuiPaneInfo':
        """ 

`GetPane`(*self*)[¶](#wx.aui.AuiManagerEvent.GetPane "Permalink to this definition")

Return type
 [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo)



Returns
The pane this event is associated with.






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def GetVeto(self) -> bool:
        """ 

`GetVeto`(*self*)[¶](#wx.aui.AuiManagerEvent.GetVeto "Permalink to this definition")

Return type
*bool*



Returns
`True` if this event was vetoed.





See also


[`Veto`](#wx.aui.AuiManagerEvent.Veto "wx.aui.AuiManagerEvent.Veto")





            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetButton(self, button: int) -> None:
        """ 

`SetButton`(*self*, *button*)[¶](#wx.aui.AuiManagerEvent.SetButton "Permalink to this definition")
Sets the `ID` of the button clicked that triggered this event.



Parameters
**button** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetCanVeto(self, can_veto: bool) -> None:
        """ 

`SetCanVeto`(*self*, *can\_veto*)[¶](#wx.aui.AuiManagerEvent.SetCanVeto "Permalink to this definition")
Sets whether or not this event can be vetoed.



Parameters
**can\_veto** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetDC(self, pdc: 'DC') -> None:
        """ 

`SetDC`(*self*, *pdc*)[¶](#wx.aui.AuiManagerEvent.SetDC "Permalink to this definition")

Parameters
**pdc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 





Todo


What is this?





            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetManager(self, manager: 'aui.AuiManager') -> None:
        """ 

`SetManager`(*self*, *manager*)[¶](#wx.aui.AuiManagerEvent.SetManager "Permalink to this definition")
Sets the  [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager) this event is associated with.



Parameters
**manager** ([*wx.aui.AuiManager*](wx.aui.AuiManager.html#wx.aui.AuiManager "wx.aui.AuiManager")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def SetPane(self, pane: 'aui.AuiPaneInfo') -> None:
        """ 

`SetPane`(*self*, *pane*)[¶](#wx.aui.AuiManagerEvent.SetPane "Permalink to this definition")
Sets the pane this event is associated with.



Parameters
**pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    def Veto(self, veto: bool=True) -> None:
        """ 

`Veto`(*self*, *veto=True*)[¶](#wx.aui.AuiManagerEvent.Veto "Permalink to this definition")
Cancels the action indicated by this event if [`CanVeto`](#wx.aui.AuiManagerEvent.CanVeto "wx.aui.AuiManagerEvent.CanVeto") is `True`.



Parameters
**veto** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManagerEvent.html
        """

    Button: int  # `Button`[¶](#wx.aui.AuiManagerEvent.Button "Permalink to this definition")See [`GetButton`](#wx.aui.AuiManagerEvent.GetButton "wx.aui.AuiManagerEvent.GetButton") and [`SetButton`](#wx.aui.AuiManagerEvent.SetButton "wx.aui.AuiManagerEvent.SetButton")
    DC: '_DC'  # `DC`[¶](#wx.aui.AuiManagerEvent.DC "Permalink to this definition")See [`GetDC`](#wx.aui.AuiManagerEvent.GetDC "wx.aui.AuiManagerEvent.GetDC") and [`SetDC`](#wx.aui.AuiManagerEvent.SetDC "wx.aui.AuiManagerEvent.SetDC")
    Manager: 'AuiManager'  # `Manager`[¶](#wx.aui.AuiManagerEvent.Manager "Permalink to this definition")See [`GetManager`](#wx.aui.AuiManagerEvent.GetManager "wx.aui.AuiManagerEvent.GetManager") and [`SetManager`](#wx.aui.AuiManagerEvent.SetManager "wx.aui.AuiManagerEvent.SetManager")
    Pane: 'AuiPaneInfo'  # `Pane`[¶](#wx.aui.AuiManagerEvent.Pane "Permalink to this definition")See [`GetPane`](#wx.aui.AuiManagerEvent.GetPane "wx.aui.AuiManagerEvent.GetPane") and [`SetPane`](#wx.aui.AuiManagerEvent.SetPane "wx.aui.AuiManagerEvent.SetPane")



EVT_AUI_PANE_BUTTON: int  # Triggered when any button is pressed for any docked panes.

EVT_AUI_PANE_CLOSE: int  # Triggered when a docked or floating pane is closed.

EVT_AUI_PANE_MAXIMIZE: int  # Triggered when a pane is maximized.

EVT_AUI_PANE_RESTORE: int  # Triggered when a pane is restored.

EVT_AUI_PANE_ACTIVATED: int  # Triggered when a pane is made ‘active’. This event is new since wxWidgets 2.9.4.

EVT_AUI_RENDER: int  # This event can be caught to override the default renderer in order to custom draw your   wx.aui.AuiManager  window (not recommended). ^^

class AuiManager(EvtHandler):
    """ **Possible constructors**:



```
AuiManager(managed_wnd=None, flags=AUI_MGR_DEFAULT)

```


AuiManager is the central class of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiManager.html
    """
    def __init__(self, managed_wnd=None, flags=AUI_MGR_DEFAULT) -> None:
        """ 

`__init__`(*self*, *managed\_wnd=None*, *flags=AUI\_MGR\_DEFAULT*)[¶](#wx.aui.AuiManager.__init__ "Permalink to this definition")
Constructor.



Parameters
* **managed\_wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Specifies the  [wx.Frame](wx.Frame.html#wx-frame) which should be managed.
* **flags** (*int*) – Specifies the frame management behaviour and visual effects with the  [wx.aui.AuiManagerOption](wx.aui.AuiManagerOption.enumeration.html#wx-aui-auimanageroption)’s style flags.






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def AddPane(self, *args, **kw) -> bool:
        """ 

`AddPane`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiManager.AddPane "Permalink to this definition")
[`AddPane`](#wx.aui.AuiManager.AddPane "wx.aui.AuiManager.AddPane") tells the frame manager to start managing a child window.


There are several versions of this function. The first version allows the full spectrum of pane parameter possibilities. The second version is used for simpler user interfaces which do not require as much configuration. The last version allows a drop position to be specified, which will determine where the pane will be added.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddPane** *(self, window, pane\_info)*



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **pane\_info** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –



Return type
*bool*






---

  



**AddPane** *(self, window, direction=LEFT, caption=””)*



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **direction** (*int*) –
* **caption** (*string*) –



Return type
*bool*






---

  



**AddPane** *(self, window, pane\_info, drop\_pos)*



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **pane\_info** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –
* **drop\_pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    @staticmethod
    def AlwaysUsesLiveResize() -> bool:
        """ 

*static* `AlwaysUsesLiveResize`()[¶](#wx.aui.AuiManager.AlwaysUsesLiveResize "Permalink to this definition")
Returns `True` if live resize is always used on the current platform.


If this function returns `True`, `AUI_MGR_LIVE_RESIZE` flag is ignored and live resize is always used, whether it’s specified or not.


Currently this is the case for wxOSX and `GTK3` ports, as live resizing is the only implemented method there.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CalculateHintRect(self, paneWindow, pt, offset) -> 'Rect':
        """ 

`CalculateHintRect`(*self*, *paneWindow*, *pt*, *offset*)[¶](#wx.aui.AuiManager.CalculateHintRect "Permalink to this definition")
This function is used by controls to calculate the drop hint rectangle.


The method first calls DoDrop() to determine the exact position the pane would be at were if dropped.



Parameters
* **paneWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window pointer of the pane being dragged.
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The mouse position, in client coordinates.
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Describes the offset that the mouse is from the upper-left corner of the item being dragged.



Return type
*Rect*



Returns
The rectangle hint will be returned in screen coordinates if the pane would indeed become docked at the specified drop point. Otherwise, an empty rectangle is returned.






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CanDockPanel(self, p: 'aui.AuiPaneInfo') -> bool:
        """ 

`CanDockPanel`(*self*, *p*)[¶](#wx.aui.AuiManager.CanDockPanel "Permalink to this definition")
Check if a key modifier is pressed (actually or ) while dragging the frame to not dock the window.



Parameters
**p** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ClosePane(self, paneInfo: 'aui.AuiPaneInfo') -> None:
        """ 

`ClosePane`(*self*, *paneInfo*)[¶](#wx.aui.AuiManager.ClosePane "Permalink to this definition")
Destroys or hides the given pane depending on its flags.



Parameters
**paneInfo** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 





See also


[`wx.aui.AuiPaneInfo.DestroyOnClose`](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo.DestroyOnClose "wx.aui.AuiPaneInfo.DestroyOnClose")





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def CreateFloatingFrame(self, parent, p) -> 'AuiFloatingFrame':
        """ 

`CreateFloatingFrame`(*self*, *parent*, *p*)[¶](#wx.aui.AuiManager.CreateFloatingFrame "Permalink to this definition")
Creates a floating frame in this  [wx.aui.AuiManager](#wx-aui-auimanager) with the given parent and  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **p** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –



Return type
 [wx.aui.AuiFloatingFrame](wx.aui.AuiFloatingFrame.html#wx-aui-auifloatingframe)






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def DetachPane(self, window: 'Window') -> bool:
        """ 

`DetachPane`(*self*, *window*)[¶](#wx.aui.AuiManager.DetachPane "Permalink to this definition")
Tells the  [wx.aui.AuiManager](#wx-aui-auimanager) to stop managing the pane specified by window.


The window, if in a floated frame, is reparented to the frame managed by  [wx.aui.AuiManager](#wx-aui-auimanager).



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def DrawHintRect(self, paneWindow, pt, offset) -> None:
        """ 

`DrawHintRect`(*self*, *paneWindow*, *pt*, *offset*)[¶](#wx.aui.AuiManager.DrawHintRect "Permalink to this definition")
This function is used by controls to draw the hint window.


It is rarely called, and is mostly used by controls implementing custom pane drag/drop behaviour.



Parameters
* **paneWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetAllPanes(self) -> 'AuiPaneInfoArray':
        """ 

`GetAllPanes`(*self*)[¶](#wx.aui.AuiManager.GetAllPanes "Permalink to this definition")
Returns an array of all panes managed by the frame manager.



Return type
*AuiPaneInfoArray*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetArtProvider(self) -> 'AuiDockArt':
        """ 

`GetArtProvider`(*self*)[¶](#wx.aui.AuiManager.GetArtProvider "Permalink to this definition")
Returns the current art provider being used.



Return type
 [wx.aui.AuiDockArt](wx.aui.AuiDockArt.html#wx-aui-auidockart)





See also


 [wx.aui.AuiDockArt](wx.aui.AuiDockArt.html#wx-aui-auidockart).





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetDockSizeConstraint(self, widthpct, heightpct) -> None:
        """ 

`GetDockSizeConstraint`(*self*, *widthpct*, *heightpct*)[¶](#wx.aui.AuiManager.GetDockSizeConstraint "Permalink to this definition")
Returns the current dock constraint values.


See [`SetDockSizeConstraint`](#wx.aui.AuiManager.SetDockSizeConstraint "wx.aui.AuiManager.SetDockSizeConstraint") for more information.



Parameters
* **widthpct** (*float*) –
* **heightpct** (*float*) –






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.aui.AuiManager.GetFlags "Permalink to this definition")
Returns the current  [wx.aui.AuiManagerOption](wx.aui.AuiManagerOption.enumeration.html#wx-aui-auimanageroption)’s flags.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetManagedWindow(self) -> 'Window':
        """ 

`GetManagedWindow`(*self*)[¶](#wx.aui.AuiManager.GetManagedWindow "Permalink to this definition")
Returns the frame currently being managed by  [wx.aui.AuiManager](#wx-aui-auimanager).



Return type
*Window*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    @staticmethod
    def GetManager(window: 'Window') -> 'AuiManager':
        """ 

*static* `GetManager`(*window*)[¶](#wx.aui.AuiManager.GetManager "Permalink to this definition")
Calling this method will return the  [wx.aui.AuiManager](#wx-aui-auimanager) for a given window.


The *window* parameter should specify any child window or sub-child window of the frame or window managed by  [wx.aui.AuiManager](#wx-aui-auimanager).


The *window* parameter need not be managed by the manager itself, nor does it even need to be a child or sub-child of a managed window. It must however be inside the window hierarchy underneath the managed window.



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
 [wx.aui.AuiManager](#wx-aui-auimanager)






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def GetPane(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`GetPane`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiManager.GetPane "Permalink to this definition")
[`GetPane`](#wx.aui.AuiManager.GetPane "wx.aui.AuiManager.GetPane") is used to lookup a  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo) object either by window pointer or by pane name, which acts as a unique id for a window pane.


The returned  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo) object may then be modified to change a pane’s look, state or position. After one or more modifications to  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo), [`wx.aui.AuiManager.Update`](#wx.aui.AuiManager.Update "wx.aui.AuiManager.Update") should be called to commit the changes to the user interface. If the lookup failed (meaning the pane could not be found in the manager), a call to the returned  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo)’s IsOk() method will return `False`.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetPane** *(self, window)*



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
 [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo)






---

  



**GetPane** *(self, name)*



Parameters
**name** (*string*) – 



Return type
 [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def HasLiveResize(self) -> bool:
        """ 

`HasLiveResize`(*self*)[¶](#wx.aui.AuiManager.HasLiveResize "Permalink to this definition")
Returns `True` if windows are resized live.


This function combines the check for [`AlwaysUsesLiveResize`](#wx.aui.AuiManager.AlwaysUsesLiveResize "wx.aui.AuiManager.AlwaysUsesLiveResize") and, for the platforms where live resizing is optional, the check for `wx.aui.AUI_MGR_LIVE_RESIZE` flag.


Using this accessor allows to verify whether live resizing is being actually used.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def HideHint(self) -> None:
        """ 

`HideHint`(*self*)[¶](#wx.aui.AuiManager.HideHint "Permalink to this definition")
[`HideHint`](#wx.aui.AuiManager.HideHint "wx.aui.AuiManager.HideHint") hides any docking hint that may be visible.




            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def InsertPane(self, window, insert_location, insert_level=AUI_INSERT_PANE) -> bool:
        """ 

`InsertPane`(*self*, *window*, *insert\_location*, *insert\_level=AUI\_INSERT\_PANE*)[¶](#wx.aui.AuiManager.InsertPane "Permalink to this definition")
This method is used to insert either a previously unmanaged pane window into the frame manager, or to insert a currently managed pane somewhere else.


[`InsertPane`](#wx.aui.AuiManager.InsertPane "wx.aui.AuiManager.InsertPane") will push all panes, rows, or docks aside and insert the window into the position specified by *insert\_location*.


Because *insert\_location* can specify either a pane, dock row, or dock layer, the *insert\_level* parameter is used to disambiguate this. The parameter *insert\_level* can take a value of `AUI_INSERT_PANE`, `AUI_INSERT_ROW` or `AUI_INSERT_DOCK`.



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **insert\_location** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –
* **insert\_level** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def LoadPaneInfo(self, pane_part, pane) -> None:
        """ 

`LoadPaneInfo`(*self*, *pane\_part*, *pane*)[¶](#wx.aui.AuiManager.LoadPaneInfo "Permalink to this definition")
[`LoadPaneInfo`](#wx.aui.AuiManager.LoadPaneInfo "wx.aui.AuiManager.LoadPaneInfo") is similar to LoadPerspective, with the exception that it only loads information about a single pane.


This method writes the serialized data into the passed pane. Pointers to UI elements are not modified.



Parameters
* **pane\_part** (*string*) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –





Note


This operation also changes the name in the pane information!




See also


[`LoadPerspective`](#wx.aui.AuiManager.LoadPerspective "wx.aui.AuiManager.LoadPerspective")




See also


[`SavePaneInfo`](#wx.aui.AuiManager.SavePaneInfo "wx.aui.AuiManager.SavePaneInfo") .




See also


[`SavePerspective`](#wx.aui.AuiManager.SavePerspective "wx.aui.AuiManager.SavePerspective")





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def LoadPerspective(self, perspective, update=True) -> bool:
        """ 

`LoadPerspective`(*self*, *perspective*, *update=True*)[¶](#wx.aui.AuiManager.LoadPerspective "Permalink to this definition")
Loads a saved perspective.


A perspective is the layout state of an `AUI` managed window.


All currently existing panes that have an object in “perspective” with the same name (“equivalent”) will receive the layout parameters of the object in “perspective”. Existing panes that do not have an equivalent in “perspective” remain unchanged, objects in “perspective” having no equivalent in the manager are ignored.



Parameters
* **perspective** (*string*) – Serialized layout information of a perspective (excl. pointers to UI elements).
* **update** (*bool*) – If update is `True`, [`wx.aui.AuiManager.Update`](#wx.aui.AuiManager.Update "wx.aui.AuiManager.Update") is automatically invoked, thus realizing the specified perspective on screen.



Return type
*bool*





See also


[`LoadPaneInfo`](#wx.aui.AuiManager.LoadPaneInfo "wx.aui.AuiManager.LoadPaneInfo")




See also


[`LoadPerspective`](#wx.aui.AuiManager.LoadPerspective "wx.aui.AuiManager.LoadPerspective")




See also


[`SavePerspective`](#wx.aui.AuiManager.SavePerspective "wx.aui.AuiManager.SavePerspective")





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def MaximizePane(self, paneInfo: 'aui.AuiPaneInfo') -> None:
        """ 

`MaximizePane`(*self*, *paneInfo*)[¶](#wx.aui.AuiManager.MaximizePane "Permalink to this definition")
Maximize the given pane.



Parameters
**paneInfo** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ProcessDockResult(self, target, new_pos) -> bool:
        """ 

`ProcessDockResult`(*self*, *target*, *new\_pos*)[¶](#wx.aui.AuiManager.ProcessDockResult "Permalink to this definition")
[`ProcessDockResult`](#wx.aui.AuiManager.ProcessDockResult "wx.aui.AuiManager.ProcessDockResult") is a protected member of the `AUI` layout manager.


It can be overridden by derived classes to provide custom docking calculations.



Parameters
* **target** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –
* **new\_pos** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def RestoreMaximizedPane(self) -> None:
        """ 

`RestoreMaximizedPane`(*self*)[¶](#wx.aui.AuiManager.RestoreMaximizedPane "Permalink to this definition")
Restore the previously maximized pane.




            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def RestorePane(self, paneInfo: 'aui.AuiPaneInfo') -> None:
        """ 

`RestorePane`(*self*, *paneInfo*)[¶](#wx.aui.AuiManager.RestorePane "Permalink to this definition")
Restore the last state of the given pane.



Parameters
**paneInfo** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SavePaneInfo(self, pane: 'aui.AuiPaneInfo') -> str:
        """ 

`SavePaneInfo`(*self*, *pane*)[¶](#wx.aui.AuiManager.SavePaneInfo "Permalink to this definition")
[`SavePaneInfo`](#wx.aui.AuiManager.SavePaneInfo "wx.aui.AuiManager.SavePaneInfo") is similar to SavePerspective, with the exception that it only saves information about a single pane.



Parameters
**pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – Pane whose layout parameters should be serialized.



Return type
`string`



Returns
The serialized layout parameters of the pane are returned within the string. Information about the pointers to UI elements stored in the pane are not serialized.





See also


[`LoadPaneInfo`](#wx.aui.AuiManager.LoadPaneInfo "wx.aui.AuiManager.LoadPaneInfo")




See also


[`LoadPerspective`](#wx.aui.AuiManager.LoadPerspective "wx.aui.AuiManager.LoadPerspective")




See also


[`SavePerspective`](#wx.aui.AuiManager.SavePerspective "wx.aui.AuiManager.SavePerspective")





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SavePerspective(self) -> str:
        """ 

`SavePerspective`(*self*)[¶](#wx.aui.AuiManager.SavePerspective "Permalink to this definition")
Saves the entire user interface layout into an encoded *String* , which can then be stored by the application (probably using Config).



Return type
`string`





See also


[`LoadPerspective`](#wx.aui.AuiManager.LoadPerspective "wx.aui.AuiManager.LoadPerspective")




See also


[`LoadPaneInfo`](#wx.aui.AuiManager.LoadPaneInfo "wx.aui.AuiManager.LoadPaneInfo")




See also


[`SavePaneInfo`](#wx.aui.AuiManager.SavePaneInfo "wx.aui.AuiManager.SavePaneInfo")





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetArtProvider(self, art_provider: 'aui.AuiDockArt') -> None:
        """ 

`SetArtProvider`(*self*, *art\_provider*)[¶](#wx.aui.AuiManager.SetArtProvider "Permalink to this definition")
Instructs  [wx.aui.AuiManager](#wx-aui-auimanager) to use art provider specified by parameter *art\_provider* for all drawing calls.


This allows pluggable look-and-feel features. The previous art provider object, if any, will be deleted by  [wx.aui.AuiManager](#wx-aui-auimanager).



Parameters
**art\_provider** ([*wx.aui.AuiDockArt*](wx.aui.AuiDockArt.html#wx.aui.AuiDockArt "wx.aui.AuiDockArt")) – 





See also


 [wx.aui.AuiDockArt](wx.aui.AuiDockArt.html#wx-aui-auidockart).





            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetDockSizeConstraint(self, widthpct, heightpct) -> None:
        """ 

`SetDockSizeConstraint`(*self*, *widthpct*, *heightpct*)[¶](#wx.aui.AuiManager.SetDockSizeConstraint "Permalink to this definition")
When a user creates a new dock by dragging a window into a docked position, often times the large size of the window will create a dock that is unwieldy large.


 [wx.aui.AuiManager](#wx-aui-auimanager) by default limits the size of any new dock to 1/3 of the window size. For horizontal docks, this would be 1/3 of the window height. For vertical docks, 1/3 of the width.


Calling this function will adjust this constraint value. The numbers must be between 0.0 and 1.0. For instance, calling SetDockSizeContraint with 0.5, 0.5 will cause new docks to be limited to half of the size of the entire managed window.



Parameters
* **widthpct** (*float*) –
* **heightpct** (*float*) –






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiManager.SetFlags "Permalink to this definition")
This method is used to specify  [wx.aui.AuiManagerOption](wx.aui.AuiManagerOption.enumeration.html#wx-aui-auimanageroption)’s flags.


*flags* specifies options which allow the frame management behaviour to be modified.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def SetManagedWindow(self, managed_wnd: 'Window') -> None:
        """ 

`SetManagedWindow`(*self*, *managed\_wnd*)[¶](#wx.aui.AuiManager.SetManagedWindow "Permalink to this definition")
Called to specify the frame or window which is to be managed by  [wx.aui.AuiManager](#wx-aui-auimanager).


Frame management is not restricted to just frames. Child windows or custom controls are also allowed.



Parameters
**managed\_wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def ShowHint(self, rect: 'Rect') -> None:
        """ 

`ShowHint`(*self*, *rect*)[¶](#wx.aui.AuiManager.ShowHint "Permalink to this definition")
This function is used by controls to explicitly show a hint window at the specified rectangle.


It is rarely called, and is mostly used by controls implementing custom pane drag/drop behaviour. The specified rectangle should be in screen coordinates.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def StartPaneDrag(self, paneWindow, offset) -> None:
        """ 

`StartPaneDrag`(*self*, *paneWindow*, *offset*)[¶](#wx.aui.AuiManager.StartPaneDrag "Permalink to this definition")
Mostly used internally to define the drag action parameters.



Parameters
* **paneWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –






            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def UnInit(self) -> None:
        """ 

`UnInit`(*self*)[¶](#wx.aui.AuiManager.UnInit "Permalink to this definition")
Dissociate the managed window from the manager.


This function may be called before the managed frame or window is destroyed, but, since wxWidgets 3.1.4, it’s unnecessary to call it explicitly, as it will be called automatically when this window is destroyed, as well as when the manager itself is.




            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    def Update(self) -> None:
        """ 

`Update`(*self*)[¶](#wx.aui.AuiManager.Update "Permalink to this definition")
This method is called after any number of changes are made to any of the managed panes.


[`Update`](#wx.aui.AuiManager.Update "wx.aui.AuiManager.Update") must be invoked after [`AddPane`](#wx.aui.AuiManager.AddPane "wx.aui.AuiManager.AddPane") or [`InsertPane`](#wx.aui.AuiManager.InsertPane "wx.aui.AuiManager.InsertPane") are called in order to “realize” or “commit” the changes. In addition, any number of changes may be made to  [wx.aui.AuiPaneInfo](wx.aui.AuiPaneInfo.html#wx-aui-auipaneinfo) structures (retrieved with [`wx.aui.AuiManager.GetPane`](#wx.aui.AuiManager.GetPane "wx.aui.AuiManager.GetPane") ), but to realize the changes, [`Update`](#wx.aui.AuiManager.Update "wx.aui.AuiManager.Update") must be called. This construction allows pane flicker to be avoided by updating the whole layout at one time.




            Source: https://docs.wxpython.org/wx.aui.AuiManager.html
        """

    AllPanes: 'AuiPaneInfoArray'  # `AllPanes`[¶](#wx.aui.AuiManager.AllPanes "Permalink to this definition")See [`GetAllPanes`](#wx.aui.AuiManager.GetAllPanes "wx.aui.AuiManager.GetAllPanes")
    ArtProvider: 'AuiDockArt'  # `ArtProvider`[¶](#wx.aui.AuiManager.ArtProvider "Permalink to this definition")See [`GetArtProvider`](#wx.aui.AuiManager.GetArtProvider "wx.aui.AuiManager.GetArtProvider") and [`SetArtProvider`](#wx.aui.AuiManager.SetArtProvider "wx.aui.AuiManager.SetArtProvider")
    Flags: int  # `Flags`[¶](#wx.aui.AuiManager.Flags "Permalink to this definition")See [`GetFlags`](#wx.aui.AuiManager.GetFlags "wx.aui.AuiManager.GetFlags") and [`SetFlags`](#wx.aui.AuiManager.SetFlags "wx.aui.AuiManager.SetFlags")
    ManagedWindow: 'Window'  # `ManagedWindow`[¶](#wx.aui.AuiManager.ManagedWindow "Permalink to this definition")See [`GetManagedWindow`](#wx.aui.AuiManager.GetManagedWindow "wx.aui.AuiManager.GetManagedWindow") and [`SetManagedWindow`](#wx.aui.AuiManager.SetManagedWindow "wx.aui.AuiManager.SetManagedWindow")



AUI_MGR_ALLOW_FLOATING: int  # Allow a pane to be undocked to take the form of a   wx.MiniFrame.

AUI_MGR_ALLOW_ACTIVE_PANE: int  # Change the color of the title bar of the pane when it is activated.

AUI_MGR_TRANSPARENT_DRAG: int  # Make the pane transparent during its movement.

AUI_MGR_TRANSPARENT_HINT: int  # The possible location for docking is indicated by a translucent area.

AUI_MGR_VENETIAN_BLINDS_HINT: int  # The possible location for docking is indicated by gradually appearing partially transparent hint.

AUI_MGR_RECTANGLE_HINT: int  # The possible location for docking is indicated by a rectangular outline.

AUI_MGR_HINT_FADE: int  # The translucent area where the pane could be docked appears gradually.

AUI_MGR_NO_VENETIAN_BLINDS_FADE: int  # Used in complement of wx.aui.AUI_MGR_VENETIAN_BLINDS_HINT to show the docking hint immediately.

AUI_MGR_LIVE_RESIZE: int  # When a docked pane is resized, its content is refreshed in live (instead of moving the border alone and refreshing the content at the end).

AUI_MGR_DEFAULT: int  # Default behaviour, combines: wx.aui.AUI_MGR_ALLOW_FLOATING | wx.aui.AUI_MGR_TRANSPARENT_HINT | wx.aui.AUI_MGR_HINT_FADE | wx.aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE. ^^

class AuiFloatingFrame(Frame):
    """ **Possible constructors**:



```
AuiFloatingFrame(parent, ownerMgr, pane, id=ID_ANY, style=RESIZE_BORDER|
                 SYSTEM_MENU|CAPTION|FRAME_NO_TASKBAR|FRAME_FLOAT_ON_PARENT|CLIP_CHILDREN
                 )

```


  


        Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
    """
    def __init__(self, parent, ownerMgr, pane, id=ID_ANY, style=RESIZE_BORDER|SYSTEM_MENU|CAPTION|FRAME_NO_TASKBAR|FRAME_FLOAT_ON_PARENT|CLIP_CHILDREN) -> None:
        """ 

`__init__`(*self*, *parent*, *ownerMgr*, *pane*, *id=ID\_ANY*, *style=RESIZE\_BORDER|SYSTEM\_MENU|CAPTION|FRAME\_NO\_TASKBAR|FRAME\_FLOAT\_ON\_PARENT|CLIP\_CHILDREN*)[¶](#wx.aui.AuiFloatingFrame.__init__ "Permalink to this definition")

Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **ownerMgr** ([*wx.aui.AuiManager*](wx.aui.AuiManager.html#wx.aui.AuiManager "wx.aui.AuiManager")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –
* **id** (*wx.WindowID*) –
* **style** (*long*) –






            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def GetAuiManager(self) -> 'AuiManager':
        """ 

`GetAuiManager`(*self*)[¶](#wx.aui.AuiFloatingFrame.GetAuiManager "Permalink to this definition")
Returns the embedded  [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager) managing this floating pane’s contents.



Return type
 [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager)





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def GetOwnerManager(self) -> 'AuiManager':
        """ 

`GetOwnerManager`(*self*)[¶](#wx.aui.AuiFloatingFrame.GetOwnerManager "Permalink to this definition")

Return type
 [wx.aui.AuiManager](wx.aui.AuiManager.html#wx-aui-auimanager)






            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    def SetPaneWindow(self, pane: 'aui.AuiPaneInfo') -> None:
        """ 

`SetPaneWindow`(*self*, *pane*)[¶](#wx.aui.AuiFloatingFrame.SetPaneWindow "Permalink to this definition")

Parameters
**pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiFloatingFrame.html
        """

    AuiManager: 'AuiManager'  # `AuiManager`[¶](#wx.aui.AuiFloatingFrame.AuiManager "Permalink to this definition")See [`GetAuiManager`](#wx.aui.AuiFloatingFrame.GetAuiManager "wx.aui.AuiFloatingFrame.GetAuiManager")
    OwnerManager: 'AuiManager'  # `OwnerManager`[¶](#wx.aui.AuiFloatingFrame.OwnerManager "Permalink to this definition")See [`GetOwnerManager`](#wx.aui.AuiFloatingFrame.GetOwnerManager "wx.aui.AuiFloatingFrame.GetOwnerManager")



class AuiMDIParentFrame(Frame):
    """ **Possible constructors**:



```
AuiMDIParentFrame()

AuiMDIParentFrame(parent, winid=ID_ANY, title="", pos=DefaultPosition,
                  size=DefaultSize, style=DEFAULT_FRAME_STYLE|VSCROLL|HSCROLL,
                  name=FrameNameStr)

```


  


        Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiMDIParentFrame.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, parent, winid=ID\_ANY, title=””, pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_FRAME\_STYLE|VSCROLL|HSCROLL, name=FrameNameStr)*



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **winid** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ActivateNext(self) -> None:
        """ 

`ActivateNext`(*self*)[¶](#wx.aui.AuiMDIParentFrame.ActivateNext "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ActivatePrevious(self) -> None:
        """ 

`ActivatePrevious`(*self*)[¶](#wx.aui.AuiMDIParentFrame.ActivatePrevious "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def ArrangeIcons(self) -> None:
        """ 

`ArrangeIcons`(*self*)[¶](#wx.aui.AuiMDIParentFrame.ArrangeIcons "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Cascade(self) -> None:
        """ 

`Cascade`(*self*)[¶](#wx.aui.AuiMDIParentFrame.Cascade "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Create(self, parent, winid=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE|VSCROLL|HSCROLL, name=FrameNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *winid=ID\_ANY*, *title=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DEFAULT\_FRAME\_STYLE|VSCROLL|HSCROLL*, *name=FrameNameStr*)[¶](#wx.aui.AuiMDIParentFrame.Create "Permalink to this definition")

Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **winid** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetActiveChild(self) -> 'AuiMDIChildFrame':
        """ 

`GetActiveChild`(*self*)[¶](#wx.aui.AuiMDIParentFrame.GetActiveChild "Permalink to this definition")

Return type
 [wx.aui.AuiMDIChildFrame](wx.aui.AuiMDIChildFrame.html#wx-aui-auimdichildframe)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetArtProvider(self) -> 'AuiTabArt':
        """ 

`GetArtProvider`(*self*)[¶](#wx.aui.AuiMDIParentFrame.GetArtProvider "Permalink to this definition")

Return type
 [wx.aui.AuiTabArt](wx.aui.AuiTabArt.html#wx-aui-auitabart)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiMDIParentFrame.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetClientWindow(self) -> 'AuiMDIClientWindow':
        """ 

`GetClientWindow`(*self*)[¶](#wx.aui.AuiMDIParentFrame.GetClientWindow "Permalink to this definition")

Return type
 [wx.aui.AuiMDIClientWindow](wx.aui.AuiMDIClientWindow.html#wx-aui-auimdiclientwindow)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetNotebook(self) -> 'AuiNotebook':
        """ 

`GetNotebook`(*self*)[¶](#wx.aui.AuiMDIParentFrame.GetNotebook "Permalink to this definition")

Return type
 [wx.aui.AuiNotebook](wx.aui.AuiNotebook.html#wx-aui-auinotebook)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def GetWindowMenu(self) -> 'Menu':
        """ 

`GetWindowMenu`(*self*)[¶](#wx.aui.AuiMDIParentFrame.GetWindowMenu "Permalink to this definition")

Return type
*Menu*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def OnCreateClient(self) -> 'AuiMDIClientWindow':
        """ 

`OnCreateClient`(*self*)[¶](#wx.aui.AuiMDIParentFrame.OnCreateClient "Permalink to this definition")

Return type
 [wx.aui.AuiMDIClientWindow](wx.aui.AuiMDIClientWindow.html#wx-aui-auimdiclientwindow)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetActiveChild(self, pChildFrame: 'aui.AuiMDIChildFrame') -> None:
        """ 

`SetActiveChild`(*self*, *pChildFrame*)[¶](#wx.aui.AuiMDIParentFrame.SetActiveChild "Permalink to this definition")

Parameters
**pChildFrame** ([*wx.aui.AuiMDIChildFrame*](wx.aui.AuiMDIChildFrame.html#wx.aui.AuiMDIChildFrame "wx.aui.AuiMDIChildFrame")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetArtProvider(self, provider: 'aui.AuiTabArt') -> None:
        """ 

`SetArtProvider`(*self*, *provider*)[¶](#wx.aui.AuiMDIParentFrame.SetArtProvider "Permalink to this definition")

Parameters
**provider** ([*wx.aui.AuiTabArt*](wx.aui.AuiTabArt.html#wx.aui.AuiTabArt "wx.aui.AuiTabArt")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetChildMenuBar(self, pChild: 'aui.AuiMDIChildFrame') -> None:
        """ 

`SetChildMenuBar`(*self*, *pChild*)[¶](#wx.aui.AuiMDIParentFrame.SetChildMenuBar "Permalink to this definition")

Parameters
**pChild** ([*wx.aui.AuiMDIChildFrame*](wx.aui.AuiMDIChildFrame.html#wx.aui.AuiMDIChildFrame "wx.aui.AuiMDIChildFrame")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetMenuBar(self, menuBar: 'MenuBar') -> None:
        """ 

`SetMenuBar`(*self*, *menuBar*)[¶](#wx.aui.AuiMDIParentFrame.SetMenuBar "Permalink to this definition")
Tells the frame to show the given menu bar.



Parameters
**menuBar** ([*wx.MenuBar*](wx.MenuBar.html#wx.MenuBar "wx.MenuBar")) – The menu bar to associate with the frame.





Note


If the frame is destroyed, the menu bar and its menus will be destroyed also, so do not delete the menu bar explicitly (except by resetting the frame’s menu bar to another frame or `None`). Under Windows, a size event is generated, so be sure to initialize data members properly before calling [`SetMenuBar`](#wx.aui.AuiMDIParentFrame.SetMenuBar "wx.aui.AuiMDIParentFrame.SetMenuBar") . Note that on some platforms, it is not possible to call this function twice for the same frame object.




See also


[`GetMenuBar`](wx.Frame.html#wx.Frame.GetMenuBar "wx.Frame.GetMenuBar") ,  [wx.MenuBar](wx.MenuBar.html#wx-menubar),  [wx.Menu](wx.Menu.html#wx-menu).





            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def SetWindowMenu(self, pMenu: 'Menu') -> None:
        """ 

`SetWindowMenu`(*self*, *pMenu*)[¶](#wx.aui.AuiMDIParentFrame.SetWindowMenu "Permalink to this definition")

Parameters
**pMenu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    def Tile(self, orient: Orientation=HORIZONTAL) -> None:
        """ 

`Tile`(*self*, *orient=HORIZONTAL*)[¶](#wx.aui.AuiMDIParentFrame.Tile "Permalink to this definition")

Parameters
**orient** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIParentFrame.html
        """

    ActiveChild: 'AuiMDIChildFrame'  # `ActiveChild`[¶](#wx.aui.AuiMDIParentFrame.ActiveChild "Permalink to this definition")See [`GetActiveChild`](#wx.aui.AuiMDIParentFrame.GetActiveChild "wx.aui.AuiMDIParentFrame.GetActiveChild") and [`SetActiveChild`](#wx.aui.AuiMDIParentFrame.SetActiveChild "wx.aui.AuiMDIParentFrame.SetActiveChild")
    ArtProvider: 'AuiTabArt'  # `ArtProvider`[¶](#wx.aui.AuiMDIParentFrame.ArtProvider "Permalink to this definition")See [`GetArtProvider`](#wx.aui.AuiMDIParentFrame.GetArtProvider "wx.aui.AuiMDIParentFrame.GetArtProvider") and [`SetArtProvider`](#wx.aui.AuiMDIParentFrame.SetArtProvider "wx.aui.AuiMDIParentFrame.SetArtProvider")
    ClientWindow: 'AuiMDIClientWindow'  # `ClientWindow`[¶](#wx.aui.AuiMDIParentFrame.ClientWindow "Permalink to this definition")See [`GetClientWindow`](#wx.aui.AuiMDIParentFrame.GetClientWindow "wx.aui.AuiMDIParentFrame.GetClientWindow")
    Notebook: 'AuiNotebook'  # `Notebook`[¶](#wx.aui.AuiMDIParentFrame.Notebook "Permalink to this definition")See [`GetNotebook`](#wx.aui.AuiMDIParentFrame.GetNotebook "wx.aui.AuiMDIParentFrame.GetNotebook")
    WindowMenu: 'Menu'  # `WindowMenu`[¶](#wx.aui.AuiMDIParentFrame.WindowMenu "Permalink to this definition")See [`GetWindowMenu`](#wx.aui.AuiMDIParentFrame.GetWindowMenu "wx.aui.AuiMDIParentFrame.GetWindowMenu") and [`SetWindowMenu`](#wx.aui.AuiMDIParentFrame.SetWindowMenu "wx.aui.AuiMDIParentFrame.SetWindowMenu")



class AuiToolBarEvent(NotifyEvent):
    """ **Possible constructors**:



```
AuiToolBarEvent(commandType=wxEVT_NULL, winId=0)

AuiToolBarEvent(c)

```


AuiToolBarEvent is used for the events generated by AuiToolBar.


  


        Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiToolBarEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, commandType=wxEVT\_NULL, winId=0)*



Parameters
* **commandType** (*wx.EventType*) –
* **winId** (*int*) –






---

  



**\_\_init\_\_** *(self, c)*



Parameters
**c** ([*wx.aui.AuiToolBarEvent*](#wx.aui.AuiToolBarEvent "wx.aui.AuiToolBarEvent")) – 






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetClickPoint(self) -> 'Point':
        """ 

`GetClickPoint`(*self*)[¶](#wx.aui.AuiToolBarEvent.GetClickPoint "Permalink to this definition")
Returns the point where the user clicked with the mouse.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetItemRect(self) -> 'Rect':
        """ 

`GetItemRect`(*self*)[¶](#wx.aui.AuiToolBarEvent.GetItemRect "Permalink to this definition")
Returns the  [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem) rectangle bounding the mouse click point.



Return type
*Rect*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def GetToolId(self) -> int:
        """ 

`GetToolId`(*self*)[¶](#wx.aui.AuiToolBarEvent.GetToolId "Permalink to this definition")
Returns the  [wx.aui.AuiToolBarItem](wx.aui.AuiToolBarItem.html#wx-aui-auitoolbaritem) identifier.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def IsDropDownClicked(self) -> bool:
        """ 

`IsDropDownClicked`(*self*)[¶](#wx.aui.AuiToolBarEvent.IsDropDownClicked "Permalink to this definition")
Returns whether the drop down menu has been clicked.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetClickPoint(self, p: Union[tuple[int, int], 'Point']) -> None:
        """ 

`SetClickPoint`(*self*, *p*)[¶](#wx.aui.AuiToolBarEvent.SetClickPoint "Permalink to this definition")

Parameters
**p** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetDropDownClicked(self, c: bool) -> None:
        """ 

`SetDropDownClicked`(*self*, *c*)[¶](#wx.aui.AuiToolBarEvent.SetDropDownClicked "Permalink to this definition")

Parameters
**c** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetItemRect(self, r: 'Rect') -> None:
        """ 

`SetItemRect`(*self*, *r*)[¶](#wx.aui.AuiToolBarEvent.SetItemRect "Permalink to this definition")

Parameters
**r** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    def SetToolId(self, toolId: int) -> None:
        """ 

`SetToolId`(*self*, *toolId*)[¶](#wx.aui.AuiToolBarEvent.SetToolId "Permalink to this definition")

Parameters
**toolId** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarEvent.html
        """

    ClickPoint: 'Point'  # `ClickPoint`[¶](#wx.aui.AuiToolBarEvent.ClickPoint "Permalink to this definition")See [`GetClickPoint`](#wx.aui.AuiToolBarEvent.GetClickPoint "wx.aui.AuiToolBarEvent.GetClickPoint") and [`SetClickPoint`](#wx.aui.AuiToolBarEvent.SetClickPoint "wx.aui.AuiToolBarEvent.SetClickPoint")
    ItemRect: 'Rect'  # `ItemRect`[¶](#wx.aui.AuiToolBarEvent.ItemRect "Permalink to this definition")See [`GetItemRect`](#wx.aui.AuiToolBarEvent.GetItemRect "wx.aui.AuiToolBarEvent.GetItemRect") and [`SetItemRect`](#wx.aui.AuiToolBarEvent.SetItemRect "wx.aui.AuiToolBarEvent.SetItemRect")
    ToolId: int  # `ToolId`[¶](#wx.aui.AuiToolBarEvent.ToolId "Permalink to this definition")See [`GetToolId`](#wx.aui.AuiToolBarEvent.GetToolId "wx.aui.AuiToolBarEvent.GetToolId") and [`SetToolId`](#wx.aui.AuiToolBarEvent.SetToolId "wx.aui.AuiToolBarEvent.SetToolId")



class AuiMDIChildFrame(Panel):
    """ **Possible constructors**:



```
AuiMDIChildFrame()

AuiMDIChildFrame(parent, winid=ID_ANY, title="", pos=DefaultPosition,
                 size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr)

```


  


        Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiMDIChildFrame.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, parent, winid=ID\_ANY, title=””, pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_FRAME\_STYLE, name=FrameNameStr)*



Parameters
* **parent** ([*wx.aui.AuiMDIParentFrame*](wx.aui.AuiMDIParentFrame.html#wx.aui.AuiMDIParentFrame "wx.aui.AuiMDIParentFrame")) –
* **winid** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Activate(self) -> None:
        """ 

`Activate`(*self*)[¶](#wx.aui.AuiMDIChildFrame.Activate "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Create(self, parent, winid=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize, style=DEFAULT_FRAME_STYLE, name=FrameNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *winid=ID\_ANY*, *title=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DEFAULT\_FRAME\_STYLE*, *name=FrameNameStr*)[¶](#wx.aui.AuiMDIChildFrame.Create "Permalink to this definition")

Parameters
* **parent** ([*wx.aui.AuiMDIParentFrame*](wx.aui.AuiMDIParentFrame.html#wx.aui.AuiMDIParentFrame "wx.aui.AuiMDIParentFrame")) –
* **winid** (*wx.WindowID*) –
* **title** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def CreateStatusBar(self, number=1, style=1, winid=1, name="") -> 'StatusBar':
        """ 

`CreateStatusBar`(*self*, *number=1*, *style=1*, *winid=1*, *name=""*)[¶](#wx.aui.AuiMDIChildFrame.CreateStatusBar "Permalink to this definition")

Parameters
* **number** (*int*) –
* **style** (*long*) –
* **winid** (*wx.WindowID*) –
* **name** (*string*) –



Return type
[`StatusBar`](#wx.aui.AuiMDIChildFrame.StatusBar "wx.aui.AuiMDIChildFrame.StatusBar")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def CreateToolBar(self, style, winid, name) -> 'ToolBar':
        """ 

`CreateToolBar`(*self*, *style*, *winid*, *name*)[¶](#wx.aui.AuiMDIChildFrame.CreateToolBar "Permalink to this definition")

Parameters
* **style** (*long*) –
* **winid** (*wx.WindowID*) –
* **name** (*string*) –



Return type
[`ToolBar`](#wx.aui.AuiMDIChildFrame.ToolBar "wx.aui.AuiMDIChildFrame.ToolBar")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Destroy(self) -> bool:
        """ 

`Destroy`(*self*)[¶](#wx.aui.AuiMDIChildFrame.Destroy "Permalink to this definition")
Destroys the window safely.


Use this function instead of the delete operator, since different window classes can be destroyed differently. Frames and dialogs are not destroyed immediately when this function is called – they are added to a list of windows to be deleted on idle time, when all the window’s events have been processed. This prevents problems with events being sent to non-existent windows.



Return type
*bool*



Returns
`True` if the window has either been successfully deleted, or it has been added to the list of windows pending real deletion.






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.aui.AuiMDIChildFrame.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetIcon(self) -> 'Icon':
        """ 

`GetIcon`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetIcon "Permalink to this definition")

Return type
[`Icon`](#wx.aui.AuiMDIChildFrame.Icon "wx.aui.AuiMDIChildFrame.Icon")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetIcons(self) -> 'IconBundle':
        """ 

`GetIcons`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetIcons "Permalink to this definition")

Return type
*IconBundle*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetMDIParentFrame(self) -> 'AuiMDIParentFrame':
        """ 

`GetMDIParentFrame`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetMDIParentFrame "Permalink to this definition")

Return type
 [wx.aui.AuiMDIParentFrame](wx.aui.AuiMDIParentFrame.html#wx-aui-auimdiparentframe)






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetMenuBar(self) -> 'MenuBar':
        """ 

`GetMenuBar`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetMenuBar "Permalink to this definition")

Return type
[`MenuBar`](#wx.aui.AuiMDIChildFrame.MenuBar "wx.aui.AuiMDIChildFrame.MenuBar")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetStatusBar(self) -> 'StatusBar':
        """ 

`GetStatusBar`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetStatusBar "Permalink to this definition")

Return type
[`StatusBar`](#wx.aui.AuiMDIChildFrame.StatusBar "wx.aui.AuiMDIChildFrame.StatusBar")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetTitle(self) -> str:
        """ 

`GetTitle`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetTitle "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def GetToolBar(self) -> 'ToolBar':
        """ 

`GetToolBar`(*self*)[¶](#wx.aui.AuiMDIChildFrame.GetToolBar "Permalink to this definition")

Return type
[`ToolBar`](#wx.aui.AuiMDIChildFrame.ToolBar "wx.aui.AuiMDIChildFrame.ToolBar")






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Iconize(self, iconize: bool=True) -> None:
        """ 

`Iconize`(*self*, *iconize=True*)[¶](#wx.aui.AuiMDIChildFrame.Iconize "Permalink to this definition")

Parameters
**iconize** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsFullScreen(self) -> bool:
        """ 

`IsFullScreen`(*self*)[¶](#wx.aui.AuiMDIChildFrame.IsFullScreen "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsIconized(self) -> bool:
        """ 

`IsIconized`(*self*)[¶](#wx.aui.AuiMDIChildFrame.IsIconized "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsMaximized(self) -> bool:
        """ 

`IsMaximized`(*self*)[¶](#wx.aui.AuiMDIChildFrame.IsMaximized "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def IsTopLevel(self) -> bool:
        """ 

`IsTopLevel`(*self*)[¶](#wx.aui.AuiMDIChildFrame.IsTopLevel "Permalink to this definition")
Returns `True` if the given window is a top-level one.


Currently all frames and dialogs are considered to be top-level windows (even if they have a parent window).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Maximize(self, maximize: bool=True) -> None:
        """ 

`Maximize`(*self*, *maximize=True*)[¶](#wx.aui.AuiMDIChildFrame.Maximize "Permalink to this definition")

Parameters
**maximize** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Restore(self) -> None:
        """ 

`Restore`(*self*)[¶](#wx.aui.AuiMDIChildFrame.Restore "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ 

`SetIcon`(*self*, *icon*)[¶](#wx.aui.AuiMDIChildFrame.SetIcon "Permalink to this definition")

Parameters
**icon** ([*wx.Icon*](wx.Icon.html#wx.Icon "wx.Icon")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetIcons(self, icons: 'IconBundle') -> None:
        """ 

`SetIcons`(*self*, *icons*)[¶](#wx.aui.AuiMDIChildFrame.SetIcons "Permalink to this definition")

Parameters
**icons** ([*wx.IconBundle*](wx.IconBundle.html#wx.IconBundle "wx.IconBundle")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetMDIParentFrame(self, parent: 'aui.AuiMDIParentFrame') -> None:
        """ 

`SetMDIParentFrame`(*self*, *parent*)[¶](#wx.aui.AuiMDIChildFrame.SetMDIParentFrame "Permalink to this definition")

Parameters
**parent** ([*wx.aui.AuiMDIParentFrame*](wx.aui.AuiMDIParentFrame.html#wx.aui.AuiMDIParentFrame "wx.aui.AuiMDIParentFrame")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetMenuBar(self, menuBar: 'MenuBar') -> None:
        """ 

`SetMenuBar`(*self*, *menuBar*)[¶](#wx.aui.AuiMDIChildFrame.SetMenuBar "Permalink to this definition")

Parameters
**menuBar** ([*wx.MenuBar*](wx.MenuBar.html#wx.MenuBar "wx.MenuBar")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetStatusText(self, text, number=0) -> None:
        """ 

`SetStatusText`(*self*, *text*, *number=0*)[¶](#wx.aui.AuiMDIChildFrame.SetStatusText "Permalink to this definition")

Parameters
* **text** (*string*) –
* **number** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetStatusWidths(self, widths: int) -> None:
        """ 

`SetStatusWidths`(*self*, *widths*)[¶](#wx.aui.AuiMDIChildFrame.SetStatusWidths "Permalink to this definition")

Parameters
**widths** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def SetTitle(self, title: str) -> None:
        """ 

`SetTitle`(*self*, *title*)[¶](#wx.aui.AuiMDIChildFrame.SetTitle "Permalink to this definition")

Parameters
**title** (*string*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def Show(self, show: bool=True) -> bool:
        """ 

`Show`(*self*, *show=True*)[¶](#wx.aui.AuiMDIChildFrame.Show "Permalink to this definition")
Shows or hides the window.


You may need to call `Raise` for a top level window if you want to bring it to top, although this is not needed if [`Show`](#wx.aui.AuiMDIChildFrame.Show "wx.aui.AuiMDIChildFrame.Show") is called immediately after the frame creation.


Notice that the default state of newly created top level windows is hidden (to allow you to create their contents without flicker) unlike for all the other, not derived from  [wx.TopLevelWindow](wx.TopLevelWindow.html#wx-toplevelwindow), windows that are by default created in the shown state.



Parameters
**show** (*bool*) – If `True` displays the window. Otherwise, hides it.



Return type
*bool*



Returns
`True` if the window has been shown or hidden or `False` if nothing was done because it already was in the requested state.





See also


`IsShown` , `Hide` , `wx.RadioBox.Show` ,  [wx.ShowEvent](wx.ShowEvent.html#wx-showevent).





            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    def ShowFullScreen(self, show, style) -> bool:
        """ 

`ShowFullScreen`(*self*, *show*, *style*)[¶](#wx.aui.AuiMDIChildFrame.ShowFullScreen "Permalink to this definition")

Parameters
* **show** (*bool*) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiMDIChildFrame.html
        """

    Icon: '_Icon'  # `Icon`[¶](#wx.aui.AuiMDIChildFrame.Icon "Permalink to this definition")See [`GetIcon`](#wx.aui.AuiMDIChildFrame.GetIcon "wx.aui.AuiMDIChildFrame.GetIcon") and [`SetIcon`](#wx.aui.AuiMDIChildFrame.SetIcon "wx.aui.AuiMDIChildFrame.SetIcon")
    Icons: 'IconBundle'  # `Icons`[¶](#wx.aui.AuiMDIChildFrame.Icons "Permalink to this definition")See [`GetIcons`](#wx.aui.AuiMDIChildFrame.GetIcons "wx.aui.AuiMDIChildFrame.GetIcons") and [`SetIcons`](#wx.aui.AuiMDIChildFrame.SetIcons "wx.aui.AuiMDIChildFrame.SetIcons")
    MDIParentFrame: 'AuiMDIParentFrame'  # `MDIParentFrame`[¶](#wx.aui.AuiMDIChildFrame.MDIParentFrame "Permalink to this definition")See [`GetMDIParentFrame`](#wx.aui.AuiMDIChildFrame.GetMDIParentFrame "wx.aui.AuiMDIChildFrame.GetMDIParentFrame") and [`SetMDIParentFrame`](#wx.aui.AuiMDIChildFrame.SetMDIParentFrame "wx.aui.AuiMDIChildFrame.SetMDIParentFrame")
    MenuBar: '_MenuBar'  # `MenuBar`[¶](#wx.aui.AuiMDIChildFrame.MenuBar "Permalink to this definition")See [`GetMenuBar`](#wx.aui.AuiMDIChildFrame.GetMenuBar "wx.aui.AuiMDIChildFrame.GetMenuBar") and [`SetMenuBar`](#wx.aui.AuiMDIChildFrame.SetMenuBar "wx.aui.AuiMDIChildFrame.SetMenuBar")
    StatusBar: '_StatusBar'  # `StatusBar`[¶](#wx.aui.AuiMDIChildFrame.StatusBar "Permalink to this definition")See [`GetStatusBar`](#wx.aui.AuiMDIChildFrame.GetStatusBar "wx.aui.AuiMDIChildFrame.GetStatusBar")
    Title: str  # `Title`[¶](#wx.aui.AuiMDIChildFrame.Title "Permalink to this definition")See [`GetTitle`](#wx.aui.AuiMDIChildFrame.GetTitle "wx.aui.AuiMDIChildFrame.GetTitle") and [`SetTitle`](#wx.aui.AuiMDIChildFrame.SetTitle "wx.aui.AuiMDIChildFrame.SetTitle")
    ToolBar: '_ToolBar'  # `ToolBar`[¶](#wx.aui.AuiMDIChildFrame.ToolBar "Permalink to this definition")See [`GetToolBar`](#wx.aui.AuiMDIChildFrame.GetToolBar "wx.aui.AuiMDIChildFrame.GetToolBar")



class AuiNotebookPage:
    """ A simple class which holds information about the notebook’s pages and
their state.


  


        Source: https://docs.wxpython.org/wx.aui.AuiNotebookPage.html
    """
    active: Any  # `active`[¶](#wx.aui.AuiNotebookPage.active "Permalink to this definition")A public C++ attribute of type `bool`.
    bitmap: Any  # `bitmap`[¶](#wx.aui.AuiNotebookPage.bitmap "Permalink to this definition")A public C++ attribute of type [`BitmapBundle`](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle") .
    caption: Any  # `caption`[¶](#wx.aui.AuiNotebookPage.caption "Permalink to this definition")A public C++ attribute of type `string`.
    rect: Any  # `rect`[¶](#wx.aui.AuiNotebookPage.rect "Permalink to this definition")A public C++ attribute of type [`Rect`](wx.Rect.html#wx.Rect "wx.Rect") .
    tooltip: Any  # `tooltip`[¶](#wx.aui.AuiNotebookPage.tooltip "Permalink to this definition")A public C++ attribute of type `string`.
    window: Any  # `window`[¶](#wx.aui.AuiNotebookPage.window "Permalink to this definition")A public C++ attribute of type [`Window`](wx.Window.html#wx.Window "wx.Window") .



class AuiSimpleTabArt(AuiTabArt):
    """ **Possible constructors**:



```
AuiSimpleTabArt()

```


Another standard tab art provider for AuiNotebook.


  


        Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiSimpleTabArt.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def Clone(self) -> 'AuiTabArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiSimpleTabArt.Clone "Permalink to this definition")
Clones the art object.



Return type
 [wx.aui.AuiTabArt](wx.aui.AuiTabArt.html#wx-aui-auitabart)






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiSimpleTabArt.DrawBackground "Permalink to this definition")
Draws a background on the given area.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawButton(self, dc, wnd, in_rect, bitmap_id, button_state, orientation, out_rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *in\_rect*, *bitmap\_id*, *button\_state*, *orientation*, *out\_rect*)[¶](#wx.aui.AuiSimpleTabArt.DrawButton "Permalink to this definition")
Draws a button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **in\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **bitmap\_id** (*int*) –
* **button\_state** (*int*) –
* **orientation** (*int*) –
* **out\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def DrawTab(self, dc, wnd, page, rect, close_button_state, out_tab_rect, out_button_rect, x_extent) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *page*, *rect*, *close\_button\_state*, *out\_tab\_rect*, *out\_button\_rect*, *x\_extent*)[¶](#wx.aui.AuiSimpleTabArt.DrawTab "Permalink to this definition")
Draws a tab.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **page** ([*wx.aui.AuiNotebookPage*](wx.aui.AuiNotebookPage.html#wx.aui.AuiNotebookPage "wx.aui.AuiNotebookPage")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **close\_button\_state** (*int*) –
* **out\_tab\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **out\_button\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **x\_extent** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetBestTabCtrlSize(self) -> int:
        """ 

`GetBestTabCtrlSize`(*self*)[¶](#wx.aui.AuiSimpleTabArt.GetBestTabCtrlSize "Permalink to this definition")
Returns the tab control size.



Parameters
**``** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetIndentSize(self) -> int:
        """ 

`GetIndentSize`(*self*)[¶](#wx.aui.AuiSimpleTabArt.GetIndentSize "Permalink to this definition")
Returns the indent size.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def GetTabSize(self, dc, wnd, caption, bitmap, active, closeButtonState, xExtent) -> 'Size':
        """ 

`GetTabSize`(*self*, *dc*, *wnd*, *caption*, *bitmap*, *active*, *closeButtonState*, *xExtent*)[¶](#wx.aui.AuiSimpleTabArt.GetTabSize "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **caption** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **active** (*bool*) –
* **closeButtonState** (*int*) –
* **xExtent** (*int*) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetActiveColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetActiveColour`(*self*, *colour*)[¶](#wx.aui.AuiSimpleTabArt.SetActiveColour "Permalink to this definition")
Sets the colour of the selected tab.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.aui.AuiSimpleTabArt.SetColour "Permalink to this definition")
Sets the colour of the inactive tabs.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiSimpleTabArt.SetFlags "Permalink to this definition")
Sets flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetMeasuringFont(self, font: 'Font') -> None:
        """ 

`SetMeasuringFont`(*self*, *font*)[¶](#wx.aui.AuiSimpleTabArt.SetMeasuringFont "Permalink to this definition")
Sets the font used for calculating measurements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetNormalFont(self, font: 'Font') -> None:
        """ 

`SetNormalFont`(*self*, *font*)[¶](#wx.aui.AuiSimpleTabArt.SetNormalFont "Permalink to this definition")
Sets the normal font for drawing labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetSelectedFont(self, font: 'Font') -> None:
        """ 

`SetSelectedFont`(*self*, *font*)[¶](#wx.aui.AuiSimpleTabArt.SetSelectedFont "Permalink to this definition")
Sets the font for drawing text for selected UI elements.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def SetSizingInfo(self, tab_ctrl_size, tab_count, wnd=None) -> None:
        """ 

`SetSizingInfo`(*self*, *tab\_ctrl\_size*, *tab\_count*, *wnd=None*)[¶](#wx.aui.AuiSimpleTabArt.SetSizingInfo "Permalink to this definition")
Sets sizing information.


The *wnd* argument is only present in wxWidgets 3.1.6 and newer and is required, it only has `None` default value for compatibility reasons.



Parameters
* **tab\_ctrl\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **tab\_count** (*int*) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    def ShowDropDown(self, wnd, items, activeIdx) -> int:
        """ 

`ShowDropDown`(*self*, *wnd*, *items*, *activeIdx*)[¶](#wx.aui.AuiSimpleTabArt.ShowDropDown "Permalink to this definition")

Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **items** (*AuiNotebookPageArray*) –
* **activeIdx** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiSimpleTabArt.html
        """

    IndentSize: int  # `IndentSize`[¶](#wx.aui.AuiSimpleTabArt.IndentSize "Permalink to this definition")See [`GetIndentSize`](#wx.aui.AuiSimpleTabArt.GetIndentSize "wx.aui.AuiSimpleTabArt.GetIndentSize")



class AuiToolBarItem:
    """ **Possible constructors**:



```
AuiToolBarItem()

AuiToolBarItem(c)

```


AuiToolBarItem is part of the `AUI` class framework, representing a
toolbar element.


  


        Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiToolBarItem.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default Constructor.




---

  



**\_\_init\_\_** *(self, c)*


Assigns the properties of the  [wx.aui.AuiToolBarItem](#wx-aui-auitoolbaritem) “c” to this.



Parameters
**c** ([*wx.aui.AuiToolBarItem*](#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) – 






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def Assign(self, c: 'aui.AuiToolBarItem') -> None:
        """ 

`Assign`(*self*, *c*)[¶](#wx.aui.AuiToolBarItem.Assign "Permalink to this definition")
Assigns the properties of the  [wx.aui.AuiToolBarItem](#wx-aui-auitoolbaritem) “c” to this.



Parameters
**c** ([*wx.aui.AuiToolBarItem*](#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def CanBeToggled(self) -> bool:
        """ 

`CanBeToggled`(*self*)[¶](#wx.aui.AuiToolBarItem.CanBeToggled "Permalink to this definition")
Returns whether the toolbar item can be toggled.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetAlignment(self) -> int:
        """ 

`GetAlignment`(*self*)[¶](#wx.aui.AuiToolBarItem.GetAlignment "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.aui.AuiToolBarItem.GetBitmap "Permalink to this definition")

Return type
[`Bitmap`](#wx.aui.AuiToolBarItem.Bitmap "wx.aui.AuiToolBarItem.Bitmap")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetDisabledBitmap(self) -> 'Bitmap':
        """ 

`GetDisabledBitmap`(*self*)[¶](#wx.aui.AuiToolBarItem.GetDisabledBitmap "Permalink to this definition")

Return type
[`Bitmap`](#wx.aui.AuiToolBarItem.Bitmap "wx.aui.AuiToolBarItem.Bitmap")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetHoverBitmap(self) -> 'Bitmap':
        """ 

`GetHoverBitmap`(*self*)[¶](#wx.aui.AuiToolBarItem.GetHoverBitmap "Permalink to this definition")

Return type
[`Bitmap`](#wx.aui.AuiToolBarItem.Bitmap "wx.aui.AuiToolBarItem.Bitmap")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetId(self) -> int:
        """ 

`GetId`(*self*)[¶](#wx.aui.AuiToolBarItem.GetId "Permalink to this definition")
Returns the toolbar item identifier.



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetKind(self) -> int:
        """ 

`GetKind`(*self*)[¶](#wx.aui.AuiToolBarItem.GetKind "Permalink to this definition")
Returns the toolbar item kind.



Return type
*int*



Returns
one of `ITEM_NORMAL` , `ITEM_CHECK` or `ITEM_RADIO` , `ITEM_SEPARATOR` , `ITEM_CONTROL` , `ITEM_SPACER` , `ITEM_LABEL` ,






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetLabel(self) -> str:
        """ 

`GetLabel`(*self*)[¶](#wx.aui.AuiToolBarItem.GetLabel "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetLongHelp(self) -> str:
        """ 

`GetLongHelp`(*self*)[¶](#wx.aui.AuiToolBarItem.GetLongHelp "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetMinSize(self) -> 'Size':
        """ 

`GetMinSize`(*self*)[¶](#wx.aui.AuiToolBarItem.GetMinSize "Permalink to this definition")

Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetProportion(self) -> int:
        """ 

`GetProportion`(*self*)[¶](#wx.aui.AuiToolBarItem.GetProportion "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetShortHelp(self) -> str:
        """ 

`GetShortHelp`(*self*)[¶](#wx.aui.AuiToolBarItem.GetShortHelp "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetSizerItem(self) -> 'SizerItem':
        """ 

`GetSizerItem`(*self*)[¶](#wx.aui.AuiToolBarItem.GetSizerItem "Permalink to this definition")

Return type
[`SizerItem`](#wx.aui.AuiToolBarItem.SizerItem "wx.aui.AuiToolBarItem.SizerItem")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetSpacerPixels(self) -> int:
        """ 

`GetSpacerPixels`(*self*)[¶](#wx.aui.AuiToolBarItem.GetSpacerPixels "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetState(self) -> int:
        """ 

`GetState`(*self*)[¶](#wx.aui.AuiToolBarItem.GetState "Permalink to this definition")
Gets the current state of the toolbar item.



Return type
*int*



Returns
an or’d combination of flags from AuiPaneButtonState representing the current state






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetUserData(self) -> int:
        """ 

`GetUserData`(*self*)[¶](#wx.aui.AuiToolBarItem.GetUserData "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def GetWindow(self) -> 'Window':
        """ 

`GetWindow`(*self*)[¶](#wx.aui.AuiToolBarItem.GetWindow "Permalink to this definition")
Returns the Window associated to the toolbar item.



Return type
[`Window`](#wx.aui.AuiToolBarItem.Window "wx.aui.AuiToolBarItem.Window")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def HasDropDown(self) -> bool:
        """ 

`HasDropDown`(*self*)[¶](#wx.aui.AuiToolBarItem.HasDropDown "Permalink to this definition")
Returns whether the toolbar item has an associated drop down button.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def IsActive(self) -> bool:
        """ 

`IsActive`(*self*)[¶](#wx.aui.AuiToolBarItem.IsActive "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def IsSticky(self) -> bool:
        """ 

`IsSticky`(*self*)[¶](#wx.aui.AuiToolBarItem.IsSticky "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetActive(self, b: bool) -> None:
        """ 

`SetActive`(*self*, *b*)[¶](#wx.aui.AuiToolBarItem.SetActive "Permalink to this definition")

Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetAlignment(self, l: int) -> None:
        """ 

`SetAlignment`(*self*, *l*)[¶](#wx.aui.AuiToolBarItem.SetAlignment "Permalink to this definition")

Parameters
**l** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetBitmap`(*self*, *bmp*)[¶](#wx.aui.AuiToolBarItem.SetBitmap "Permalink to this definition")

Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetDisabledBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetDisabledBitmap`(*self*, *bmp*)[¶](#wx.aui.AuiToolBarItem.SetDisabledBitmap "Permalink to this definition")

Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetHasDropDown(self, b: bool) -> None:
        """ 

`SetHasDropDown`(*self*, *b*)[¶](#wx.aui.AuiToolBarItem.SetHasDropDown "Permalink to this definition")
Set whether this tool has a drop down button.


This is only valid for `wx.ITEM_NORMAL` tools.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetHoverBitmap(self, bmp: 'BitmapBundle') -> None:
        """ 

`SetHoverBitmap`(*self*, *bmp*)[¶](#wx.aui.AuiToolBarItem.SetHoverBitmap "Permalink to this definition")

Parameters
**bmp** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetId(self, new_id: int) -> None:
        """ 

`SetId`(*self*, *new\_id*)[¶](#wx.aui.AuiToolBarItem.SetId "Permalink to this definition")
Sets the toolbar item identifier.



Parameters
**new\_id** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetKind(self, new_kind: int) -> None:
        """ 

`SetKind`(*self*, *new\_kind*)[¶](#wx.aui.AuiToolBarItem.SetKind "Permalink to this definition")
Sets the  [wx.aui.AuiToolBarItem](#wx-aui-auitoolbaritem) kind.



Parameters
**new\_kind** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetLabel(self, s: str) -> None:
        """ 

`SetLabel`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetLabel "Permalink to this definition")

Parameters
**s** (*string*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetLongHelp(self, s: str) -> None:
        """ 

`SetLongHelp`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetLongHelp "Permalink to this definition")

Parameters
**s** (*string*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetMinSize(self, s: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetMinSize`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetMinSize "Permalink to this definition")

Parameters
**s** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetProportion(self, p: int) -> None:
        """ 

`SetProportion`(*self*, *p*)[¶](#wx.aui.AuiToolBarItem.SetProportion "Permalink to this definition")

Parameters
**p** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetShortHelp(self, s: str) -> None:
        """ 

`SetShortHelp`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetShortHelp "Permalink to this definition")

Parameters
**s** (*string*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSizerItem(self, s: 'SizerItem') -> None:
        """ 

`SetSizerItem`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetSizerItem "Permalink to this definition")

Parameters
**s** ([*wx.SizerItem*](wx.SizerItem.html#wx.SizerItem "wx.SizerItem")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSpacerPixels(self, s: int) -> None:
        """ 

`SetSpacerPixels`(*self*, *s*)[¶](#wx.aui.AuiToolBarItem.SetSpacerPixels "Permalink to this definition")

Parameters
**s** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetState(self, new_state: int) -> None:
        """ 

`SetState`(*self*, *new\_state*)[¶](#wx.aui.AuiToolBarItem.SetState "Permalink to this definition")
Set the current state of the toolbar item.



Parameters
**new\_state** (*int*) – is an or’d combination of flags from AuiPaneButtonState






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetSticky(self, b: bool) -> None:
        """ 

`SetSticky`(*self*, *b*)[¶](#wx.aui.AuiToolBarItem.SetSticky "Permalink to this definition")

Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetUserData(self, l: int) -> None:
        """ 

`SetUserData`(*self*, *l*)[¶](#wx.aui.AuiToolBarItem.SetUserData "Permalink to this definition")

Parameters
**l** (*long*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    def SetWindow(self, w: 'Window') -> None:
        """ 

`SetWindow`(*self*, *w*)[¶](#wx.aui.AuiToolBarItem.SetWindow "Permalink to this definition")
Assigns a window to the toolbar item.



Parameters
**w** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarItem.html
        """

    Alignment: int  # `Alignment`[¶](#wx.aui.AuiToolBarItem.Alignment "Permalink to this definition")See [`GetAlignment`](#wx.aui.AuiToolBarItem.GetAlignment "wx.aui.AuiToolBarItem.GetAlignment") and [`SetAlignment`](#wx.aui.AuiToolBarItem.SetAlignment "wx.aui.AuiToolBarItem.SetAlignment")
    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.aui.AuiToolBarItem.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.aui.AuiToolBarItem.GetBitmap "wx.aui.AuiToolBarItem.GetBitmap") and [`SetBitmap`](#wx.aui.AuiToolBarItem.SetBitmap "wx.aui.AuiToolBarItem.SetBitmap")
    DisabledBitmap: 'Bitmap'  # `DisabledBitmap`[¶](#wx.aui.AuiToolBarItem.DisabledBitmap "Permalink to this definition")See [`GetDisabledBitmap`](#wx.aui.AuiToolBarItem.GetDisabledBitmap "wx.aui.AuiToolBarItem.GetDisabledBitmap") and [`SetDisabledBitmap`](#wx.aui.AuiToolBarItem.SetDisabledBitmap "wx.aui.AuiToolBarItem.SetDisabledBitmap")
    HoverBitmap: 'Bitmap'  # `HoverBitmap`[¶](#wx.aui.AuiToolBarItem.HoverBitmap "Permalink to this definition")See [`GetHoverBitmap`](#wx.aui.AuiToolBarItem.GetHoverBitmap "wx.aui.AuiToolBarItem.GetHoverBitmap") and [`SetHoverBitmap`](#wx.aui.AuiToolBarItem.SetHoverBitmap "wx.aui.AuiToolBarItem.SetHoverBitmap")
    Id: int  # `Id`[¶](#wx.aui.AuiToolBarItem.Id "Permalink to this definition")See [`GetId`](#wx.aui.AuiToolBarItem.GetId "wx.aui.AuiToolBarItem.GetId") and [`SetId`](#wx.aui.AuiToolBarItem.SetId "wx.aui.AuiToolBarItem.SetId")
    Kind: int  # `Kind`[¶](#wx.aui.AuiToolBarItem.Kind "Permalink to this definition")See [`GetKind`](#wx.aui.AuiToolBarItem.GetKind "wx.aui.AuiToolBarItem.GetKind") and [`SetKind`](#wx.aui.AuiToolBarItem.SetKind "wx.aui.AuiToolBarItem.SetKind")
    Label: str  # `Label`[¶](#wx.aui.AuiToolBarItem.Label "Permalink to this definition")See [`GetLabel`](#wx.aui.AuiToolBarItem.GetLabel "wx.aui.AuiToolBarItem.GetLabel") and [`SetLabel`](#wx.aui.AuiToolBarItem.SetLabel "wx.aui.AuiToolBarItem.SetLabel")
    LongHelp: str  # `LongHelp`[¶](#wx.aui.AuiToolBarItem.LongHelp "Permalink to this definition")See [`GetLongHelp`](#wx.aui.AuiToolBarItem.GetLongHelp "wx.aui.AuiToolBarItem.GetLongHelp") and [`SetLongHelp`](#wx.aui.AuiToolBarItem.SetLongHelp "wx.aui.AuiToolBarItem.SetLongHelp")
    MinSize: 'Size'  # `MinSize`[¶](#wx.aui.AuiToolBarItem.MinSize "Permalink to this definition")See [`GetMinSize`](#wx.aui.AuiToolBarItem.GetMinSize "wx.aui.AuiToolBarItem.GetMinSize") and [`SetMinSize`](#wx.aui.AuiToolBarItem.SetMinSize "wx.aui.AuiToolBarItem.SetMinSize")
    Proportion: int  # `Proportion`[¶](#wx.aui.AuiToolBarItem.Proportion "Permalink to this definition")See [`GetProportion`](#wx.aui.AuiToolBarItem.GetProportion "wx.aui.AuiToolBarItem.GetProportion") and [`SetProportion`](#wx.aui.AuiToolBarItem.SetProportion "wx.aui.AuiToolBarItem.SetProportion")
    ShortHelp: str  # `ShortHelp`[¶](#wx.aui.AuiToolBarItem.ShortHelp "Permalink to this definition")See [`GetShortHelp`](#wx.aui.AuiToolBarItem.GetShortHelp "wx.aui.AuiToolBarItem.GetShortHelp") and [`SetShortHelp`](#wx.aui.AuiToolBarItem.SetShortHelp "wx.aui.AuiToolBarItem.SetShortHelp")
    SizerItem: '_SizerItem'  # `SizerItem`[¶](#wx.aui.AuiToolBarItem.SizerItem "Permalink to this definition")See [`GetSizerItem`](#wx.aui.AuiToolBarItem.GetSizerItem "wx.aui.AuiToolBarItem.GetSizerItem") and [`SetSizerItem`](#wx.aui.AuiToolBarItem.SetSizerItem "wx.aui.AuiToolBarItem.SetSizerItem")
    SpacerPixels: int  # `SpacerPixels`[¶](#wx.aui.AuiToolBarItem.SpacerPixels "Permalink to this definition")See [`GetSpacerPixels`](#wx.aui.AuiToolBarItem.GetSpacerPixels "wx.aui.AuiToolBarItem.GetSpacerPixels") and [`SetSpacerPixels`](#wx.aui.AuiToolBarItem.SetSpacerPixels "wx.aui.AuiToolBarItem.SetSpacerPixels")
    State: int  # `State`[¶](#wx.aui.AuiToolBarItem.State "Permalink to this definition")See [`GetState`](#wx.aui.AuiToolBarItem.GetState "wx.aui.AuiToolBarItem.GetState") and [`SetState`](#wx.aui.AuiToolBarItem.SetState "wx.aui.AuiToolBarItem.SetState")
    UserData: int  # `UserData`[¶](#wx.aui.AuiToolBarItem.UserData "Permalink to this definition")See [`GetUserData`](#wx.aui.AuiToolBarItem.GetUserData "wx.aui.AuiToolBarItem.GetUserData") and [`SetUserData`](#wx.aui.AuiToolBarItem.SetUserData "wx.aui.AuiToolBarItem.SetUserData")
    Window: '_Window'  # `Window`[¶](#wx.aui.AuiToolBarItem.Window "Permalink to this definition")See [`GetWindow`](#wx.aui.AuiToolBarItem.GetWindow "wx.aui.AuiToolBarItem.GetWindow") and [`SetWindow`](#wx.aui.AuiToolBarItem.SetWindow "wx.aui.AuiToolBarItem.SetWindow")



class AuiToolBarArt:
    """ **Possible constructors**:



```
AuiToolBarArt()

```


AuiToolBarArt is part of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiToolBarArt.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def Clone(self) -> 'AuiToolBarArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiToolBarArt.Clone "Permalink to this definition")

Return type
 [wx.aui.AuiToolBarArt](#wx-aui-auitoolbarart)






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawBackground "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawControlLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawControlLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawDropDownButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawDropDownButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ 

`DrawGripper`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawGripper "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ 

`DrawOverflowButton`(*self*, *dc*, *wnd*, *rect*, *state*)[¶](#wx.aui.AuiToolBarArt.DrawOverflowButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **state** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPlainBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawPlainBackground "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, rect) -> None:
        """ 

`DrawSeparator`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiToolBarArt.DrawSeparator "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetElementSize(self, element_id: int) -> int:
        """ 

`GetElementSize`(*self*, *element\_id*)[¶](#wx.aui.AuiToolBarArt.GetElementSize "Permalink to this definition")

Parameters
**element\_id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.aui.AuiToolBarArt.GetFlags "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.aui.AuiToolBarArt.GetFont "Permalink to this definition")

Return type
[`Font`](#wx.aui.AuiToolBarArt.Font "wx.aui.AuiToolBarArt.Font")






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> 'Size':
        """ 

`GetLabelSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.aui.AuiToolBarArt.GetLabelSize "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetTextOrientation(self) -> int:
        """ 

`GetTextOrientation`(*self*)[¶](#wx.aui.AuiToolBarArt.GetTextOrientation "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> 'Size':
        """ 

`GetToolSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.aui.AuiToolBarArt.GetToolSize "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ 

`SetElementSize`(*self*, *element\_id*, *size*)[¶](#wx.aui.AuiToolBarArt.SetElementSize "Permalink to this definition")

Parameters
* **element\_id** (*int*) –
* **size** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiToolBarArt.SetFlags "Permalink to this definition")

Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.aui.AuiToolBarArt.SetFont "Permalink to this definition")

Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def SetTextOrientation(self, orientation: int) -> None:
        """ 

`SetTextOrientation`(*self*, *orientation*)[¶](#wx.aui.AuiToolBarArt.SetTextOrientation "Permalink to this definition")

Parameters
**orientation** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> int:
        """ 

`ShowDropDown`(*self*, *wnd*, *items*)[¶](#wx.aui.AuiToolBarArt.ShowDropDown "Permalink to this definition")

Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **items** (*AuiToolBarItemArray*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiToolBarArt.html
        """

    Flags: int  # `Flags`[¶](#wx.aui.AuiToolBarArt.Flags "Permalink to this definition")See [`GetFlags`](#wx.aui.AuiToolBarArt.GetFlags "wx.aui.AuiToolBarArt.GetFlags") and [`SetFlags`](#wx.aui.AuiToolBarArt.SetFlags "wx.aui.AuiToolBarArt.SetFlags")
    Font: '_Font'  # `Font`[¶](#wx.aui.AuiToolBarArt.Font "Permalink to this definition")See [`GetFont`](#wx.aui.AuiToolBarArt.GetFont "wx.aui.AuiToolBarArt.GetFont") and [`SetFont`](#wx.aui.AuiToolBarArt.SetFont "wx.aui.AuiToolBarArt.SetFont")
    TextOrientation: int  # `TextOrientation`[¶](#wx.aui.AuiToolBarArt.TextOrientation "Permalink to this definition")See [`GetTextOrientation`](#wx.aui.AuiToolBarArt.GetTextOrientation "wx.aui.AuiToolBarArt.GetTextOrientation") and [`SetTextOrientation`](#wx.aui.AuiToolBarArt.SetTextOrientation "wx.aui.AuiToolBarArt.SetTextOrientation")



class AuiPaneInfo:
    """ **Possible constructors**:



```
AuiPaneInfo()

AuiPaneInfo(c)

```


AuiPaneInfo is part of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, c)*


Copy constructor.



Parameters
**c** ([*wx.aui.AuiPaneInfo*](#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def BestSize(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`BestSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.BestSize "Permalink to this definition")
[`BestSize`](#wx.aui.AuiPaneInfo.BestSize "wx.aui.AuiPaneInfo.BestSize") sets the ideal size for the pane.


The docking manager will attempt to use this size as much as possible when docking or floating the pane.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**BestSize** *(self, size)*



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  



**BestSize** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Bottom(self) -> 'AuiPaneInfo':
        """ 

`Bottom`(*self*)[¶](#wx.aui.AuiPaneInfo.Bottom "Permalink to this definition")
`wx.Bottom` sets the pane dock position to the bottom side of the frame.


This is the same thing as calling Direction(wxAUI\_DOCK\_BOTTOM).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def BottomDockable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`BottomDockable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.BottomDockable "Permalink to this definition")
[`BottomDockable`](#wx.aui.AuiPaneInfo.BottomDockable "wx.aui.AuiPaneInfo.BottomDockable") indicates whether a pane can be docked at the bottom of the frame.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Caption(self, c: str) -> 'AuiPaneInfo':
        """ 

`Caption`(*self*, *c*)[¶](#wx.aui.AuiPaneInfo.Caption "Permalink to this definition")
[`Caption`](#wx.aui.AuiPaneInfo.Caption "wx.aui.AuiPaneInfo.Caption") sets the caption of the pane.



Parameters
**c** (*string*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CaptionVisible(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`CaptionVisible`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.CaptionVisible "Permalink to this definition")
CaptionVisible indicates that a pane caption should be visible.


If `False`, no pane caption is drawn.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Center(self) -> 'AuiPaneInfo':
        """ 

`Center`(*self*)[¶](#wx.aui.AuiPaneInfo.Center "Permalink to this definition")
`wx.Center` sets the pane dock position to the left side of the frame.


The centre pane is the space in the middle after all border panes (left, top, right, bottom) are subtracted from the layout. This is the same thing as calling Direction(wxAUI\_DOCK\_CENTRE).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CenterPane(self) -> 'AuiPaneInfo':
        """ 

`CenterPane`(*self*)[¶](#wx.aui.AuiPaneInfo.CenterPane "Permalink to this definition")
[`CentrePane`](#wx.aui.AuiPaneInfo.CentrePane "wx.aui.AuiPaneInfo.CentrePane") specifies that the pane should adopt the default center pane settings.


Centre panes usually do not have caption bars. This function provides an easy way of preparing a pane to be displayed in the center dock position.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Centre(self) -> 'AuiPaneInfo':
        """ 

`Centre`(*self*)[¶](#wx.aui.AuiPaneInfo.Centre "Permalink to this definition")
`wx.Center` sets the pane dock position to the left side of the frame.


The centre pane is the space in the middle after all border panes (left, top, right, bottom) are subtracted from the layout. This is the same thing as calling Direction(wxAUI\_DOCK\_CENTRE).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CentrePane(self) -> 'AuiPaneInfo':
        """ 

`CentrePane`(*self*)[¶](#wx.aui.AuiPaneInfo.CentrePane "Permalink to this definition")
[`CentrePane`](#wx.aui.AuiPaneInfo.CentrePane "wx.aui.AuiPaneInfo.CentrePane") specifies that the pane should adopt the default center pane settings.


Centre panes usually do not have caption bars. This function provides an easy way of preparing a pane to be displayed in the center dock position.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def CloseButton(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`CloseButton`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.CloseButton "Permalink to this definition")
[`CloseButton`](#wx.aui.AuiPaneInfo.CloseButton "wx.aui.AuiPaneInfo.CloseButton") indicates that a close button should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DefaultPane(self) -> 'AuiPaneInfo':
        """ 

`DefaultPane`(*self*)[¶](#wx.aui.AuiPaneInfo.DefaultPane "Permalink to this definition")
[`DefaultPane`](#wx.aui.AuiPaneInfo.DefaultPane "wx.aui.AuiPaneInfo.DefaultPane") specifies that the pane should adopt the default pane settings.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DestroyOnClose(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`DestroyOnClose`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.DestroyOnClose "Permalink to this definition")
[`DestroyOnClose`](#wx.aui.AuiPaneInfo.DestroyOnClose "wx.aui.AuiPaneInfo.DestroyOnClose") indicates whether a pane should be destroyed when it is closed.


Normally a pane is simply hidden when the close button is clicked. Setting DestroyOnClose to `True` will cause the window to be destroyed when the user clicks the pane’s close button.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Direction(self, direction: int) -> 'AuiPaneInfo':
        """ 

`Direction`(*self*, *direction*)[¶](#wx.aui.AuiPaneInfo.Direction "Permalink to this definition")
 [wx.DataObject.Direction](wx.DataObject.Direction.enumeration.html#wx-dataobject-direction) determines the direction of the docked pane.


It is functionally the same as calling `wx.Left` , `wx.Right` , `wx.Top` or `wx.Bottom` , except that docking direction may be specified programmatically via the parameter.



Parameters
**direction** (*int*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Dock(self) -> 'AuiPaneInfo':
        """ 

`Dock`(*self*)[¶](#wx.aui.AuiPaneInfo.Dock "Permalink to this definition")
[`Dock`](#wx.aui.AuiPaneInfo.Dock "wx.aui.AuiPaneInfo.Dock") indicates that a pane should be docked.


It is the opposite of [`Float`](#wx.aui.AuiPaneInfo.Float "wx.aui.AuiPaneInfo.Float") .



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def DockFixed(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`DockFixed`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.DockFixed "Permalink to this definition")
[`DockFixed`](#wx.aui.AuiPaneInfo.DockFixed "wx.aui.AuiPaneInfo.DockFixed") causes the containing dock to have no resize sash.


This is useful for creating panes that span the entire width or height of a dock, but should not be resizable in the other direction.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Dockable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`Dockable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.Dockable "Permalink to this definition")
[`Dockable`](#wx.aui.AuiPaneInfo.Dockable "wx.aui.AuiPaneInfo.Dockable") specifies whether a frame can be docked or not.


It is the same as specifying TopDockable(b).BottomDockable(b).LeftDockable(b).RightDockable(b).



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Fixed(self) -> 'AuiPaneInfo':
        """ 

`Fixed`(*self*)[¶](#wx.aui.AuiPaneInfo.Fixed "Permalink to this definition")
[`Fixed`](#wx.aui.AuiPaneInfo.Fixed "wx.aui.AuiPaneInfo.Fixed") forces a pane to be fixed size so that it cannot be resized.


After calling [`Fixed`](#wx.aui.AuiPaneInfo.Fixed "wx.aui.AuiPaneInfo.Fixed") , [`IsFixed`](#wx.aui.AuiPaneInfo.IsFixed "wx.aui.AuiPaneInfo.IsFixed") will return `True`.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Float(self) -> 'AuiPaneInfo':
        """ 

`Float`(*self*)[¶](#wx.aui.AuiPaneInfo.Float "Permalink to this definition")
[`Float`](#wx.aui.AuiPaneInfo.Float "wx.aui.AuiPaneInfo.Float") indicates that a pane should be floated.


It is the opposite of [`Dock`](#wx.aui.AuiPaneInfo.Dock "wx.aui.AuiPaneInfo.Dock") .



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Floatable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`Floatable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.Floatable "Permalink to this definition")
[`Floatable`](#wx.aui.AuiPaneInfo.Floatable "wx.aui.AuiPaneInfo.Floatable") sets whether the user will be able to undock a pane and turn it into a floating window.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def FloatingPosition(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`FloatingPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.FloatingPosition "Permalink to this definition")
[`FloatingPosition`](#wx.aui.AuiPaneInfo.FloatingPosition "wx.aui.AuiPaneInfo.FloatingPosition") sets the position of the floating pane.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**FloatingPosition** *(self, pos)*



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  



**FloatingPosition** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def FloatingSize(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`FloatingSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.FloatingSize "Permalink to this definition")
[`FloatingSize`](#wx.aui.AuiPaneInfo.FloatingSize "wx.aui.AuiPaneInfo.FloatingSize") sets the size of the floating pane.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**FloatingSize** *(self, size)*



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  



**FloatingSize** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Gripper(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`Gripper`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.Gripper "Permalink to this definition")
[`Gripper`](#wx.aui.AuiPaneInfo.Gripper "wx.aui.AuiPaneInfo.Gripper") indicates that a gripper should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def GripperTop(self, attop: bool=True) -> 'AuiPaneInfo':
        """ 

`GripperTop`(*self*, *attop=True*)[¶](#wx.aui.AuiPaneInfo.GripperTop "Permalink to this definition")
[`GripperTop`](#wx.aui.AuiPaneInfo.GripperTop "wx.aui.AuiPaneInfo.GripperTop") indicates that a gripper should be drawn at the top of the pane.



Parameters
**attop** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasBorder(self) -> bool:
        """ 

`HasBorder`(*self*)[¶](#wx.aui.AuiPaneInfo.HasBorder "Permalink to this definition")
[`HasBorder`](#wx.aui.AuiPaneInfo.HasBorder "wx.aui.AuiPaneInfo.HasBorder") returns `True` if the pane displays a border.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasCaption(self) -> bool:
        """ 

`HasCaption`(*self*)[¶](#wx.aui.AuiPaneInfo.HasCaption "Permalink to this definition")
[`HasCaption`](#wx.aui.AuiPaneInfo.HasCaption "wx.aui.AuiPaneInfo.HasCaption") returns `True` if the pane displays a caption.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasCloseButton(self) -> bool:
        """ 

`HasCloseButton`(*self*)[¶](#wx.aui.AuiPaneInfo.HasCloseButton "Permalink to this definition")
[`HasCloseButton`](#wx.aui.AuiPaneInfo.HasCloseButton "wx.aui.AuiPaneInfo.HasCloseButton") returns `True` if the pane displays a button to close the pane.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasFlag(self, flag: int) -> bool:
        """ 

`HasFlag`(*self*, *flag*)[¶](#wx.aui.AuiPaneInfo.HasFlag "Permalink to this definition")
[`HasFlag`](#wx.aui.AuiPaneInfo.HasFlag "wx.aui.AuiPaneInfo.HasFlag") returns `True` if the property specified by flag is active for the pane.



Parameters
**flag** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasGripper(self) -> bool:
        """ 

`HasGripper`(*self*)[¶](#wx.aui.AuiPaneInfo.HasGripper "Permalink to this definition")
[`HasGripper`](#wx.aui.AuiPaneInfo.HasGripper "wx.aui.AuiPaneInfo.HasGripper") returns `True` if the pane displays a gripper.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasGripperTop(self) -> bool:
        """ 

`HasGripperTop`(*self*)[¶](#wx.aui.AuiPaneInfo.HasGripperTop "Permalink to this definition")
[`HasGripper`](#wx.aui.AuiPaneInfo.HasGripper "wx.aui.AuiPaneInfo.HasGripper") returns `True` if the pane displays a gripper at the top.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasMaximizeButton(self) -> bool:
        """ 

`HasMaximizeButton`(*self*)[¶](#wx.aui.AuiPaneInfo.HasMaximizeButton "Permalink to this definition")
[`HasMaximizeButton`](#wx.aui.AuiPaneInfo.HasMaximizeButton "wx.aui.AuiPaneInfo.HasMaximizeButton") returns `True` if the pane displays a button to maximize the pane.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasMinimizeButton(self) -> bool:
        """ 

`HasMinimizeButton`(*self*)[¶](#wx.aui.AuiPaneInfo.HasMinimizeButton "Permalink to this definition")
[`HasMinimizeButton`](#wx.aui.AuiPaneInfo.HasMinimizeButton "wx.aui.AuiPaneInfo.HasMinimizeButton") returns `True` if the pane displays a button to minimize the pane.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def HasPinButton(self) -> bool:
        """ 

`HasPinButton`(*self*)[¶](#wx.aui.AuiPaneInfo.HasPinButton "Permalink to this definition")
[`HasPinButton`](#wx.aui.AuiPaneInfo.HasPinButton "wx.aui.AuiPaneInfo.HasPinButton") returns `True` if the pane displays a button to float the pane.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Hide(self) -> 'AuiPaneInfo':
        """ 

`Hide`(*self*)[¶](#wx.aui.AuiPaneInfo.Hide "Permalink to this definition")
[`Hide`](#wx.aui.AuiPaneInfo.Hide "wx.aui.AuiPaneInfo.Hide") indicates that a pane should be hidden.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Icon(self, b: 'BitmapBundle') -> 'AuiPaneInfo':
        """ 

`Icon`(*self*, *b*)[¶](#wx.aui.AuiPaneInfo.Icon "Permalink to this definition")
 [wx.Icon](wx.Icon.html#wx-icon) sets the icon of the pane.


Notice that the height of the icon should be smaller than the value returned by *AuiDockArt.GetMetric(wxAUI\_DOCKART\_CAPTION\_SIZE)* to ensure that it appears correctly.



Parameters
**b** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsBottomDockable(self) -> bool:
        """ 

`IsBottomDockable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsBottomDockable "Permalink to this definition")
[`IsBottomDockable`](#wx.aui.AuiPaneInfo.IsBottomDockable "wx.aui.AuiPaneInfo.IsBottomDockable") returns `True` if the pane can be docked at the bottom of the managed frame.



Return type
*bool*





See also


[`IsDockable`](#wx.aui.AuiPaneInfo.IsDockable "wx.aui.AuiPaneInfo.IsDockable")





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsDockable(self) -> bool:
        """ 

`IsDockable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsDockable "Permalink to this definition")
Returns `True` if the pane can be docked at any side.



Return type
*bool*





New in version 2.9.2.




See also


[`IsTopDockable`](#wx.aui.AuiPaneInfo.IsTopDockable "wx.aui.AuiPaneInfo.IsTopDockable") , [`IsBottomDockable`](#wx.aui.AuiPaneInfo.IsBottomDockable "wx.aui.AuiPaneInfo.IsBottomDockable") , [`IsLeftDockable`](#wx.aui.AuiPaneInfo.IsLeftDockable "wx.aui.AuiPaneInfo.IsLeftDockable") , [`IsRightDockable`](#wx.aui.AuiPaneInfo.IsRightDockable "wx.aui.AuiPaneInfo.IsRightDockable")





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsDocked(self) -> bool:
        """ 

`IsDocked`(*self*)[¶](#wx.aui.AuiPaneInfo.IsDocked "Permalink to this definition")
[`IsDocked`](#wx.aui.AuiPaneInfo.IsDocked "wx.aui.AuiPaneInfo.IsDocked") returns `True` if the pane is currently docked.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFixed(self) -> bool:
        """ 

`IsFixed`(*self*)[¶](#wx.aui.AuiPaneInfo.IsFixed "Permalink to this definition")
[`IsFixed`](#wx.aui.AuiPaneInfo.IsFixed "wx.aui.AuiPaneInfo.IsFixed") returns `True` if the pane cannot be resized.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFloatable(self) -> bool:
        """ 

`IsFloatable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsFloatable "Permalink to this definition")
[`IsFloatable`](#wx.aui.AuiPaneInfo.IsFloatable "wx.aui.AuiPaneInfo.IsFloatable") returns `True` if the pane can be undocked and displayed as a floating window.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsFloating(self) -> bool:
        """ 

`IsFloating`(*self*)[¶](#wx.aui.AuiPaneInfo.IsFloating "Permalink to this definition")
[`IsFloating`](#wx.aui.AuiPaneInfo.IsFloating "wx.aui.AuiPaneInfo.IsFloating") returns `True` if the pane is floating.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsLeftDockable(self) -> bool:
        """ 

`IsLeftDockable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsLeftDockable "Permalink to this definition")
[`IsLeftDockable`](#wx.aui.AuiPaneInfo.IsLeftDockable "wx.aui.AuiPaneInfo.IsLeftDockable") returns `True` if the pane can be docked on the left of the managed frame.



Return type
*bool*





See also


[`IsDockable`](#wx.aui.AuiPaneInfo.IsDockable "wx.aui.AuiPaneInfo.IsDockable")





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsMovable(self) -> bool:
        """ 

`IsMovable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsMovable "Permalink to this definition")
IsMoveable() returns `True` if the docked frame can be undocked or moved to another dock position.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.aui.AuiPaneInfo.IsOk "Permalink to this definition")
[`IsOk`](#wx.aui.AuiPaneInfo.IsOk "wx.aui.AuiPaneInfo.IsOk") returns `True` if the  [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo) structure is valid.


A pane structure is valid if it has an associated window.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsResizable(self) -> bool:
        """ 

`IsResizable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsResizable "Permalink to this definition")
[`IsResizable`](#wx.aui.AuiPaneInfo.IsResizable "wx.aui.AuiPaneInfo.IsResizable") returns `True` if the pane can be resized.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsRightDockable(self) -> bool:
        """ 

`IsRightDockable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsRightDockable "Permalink to this definition")
[`IsRightDockable`](#wx.aui.AuiPaneInfo.IsRightDockable "wx.aui.AuiPaneInfo.IsRightDockable") returns `True` if the pane can be docked on the right of the managed frame.



Return type
*bool*





See also


[`IsDockable`](#wx.aui.AuiPaneInfo.IsDockable "wx.aui.AuiPaneInfo.IsDockable")





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsShown(self) -> bool:
        """ 

`IsShown`(*self*)[¶](#wx.aui.AuiPaneInfo.IsShown "Permalink to this definition")
[`IsShown`](#wx.aui.AuiPaneInfo.IsShown "wx.aui.AuiPaneInfo.IsShown") returns `True` if the pane is currently shown.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsToolbar(self) -> bool:
        """ 

`IsToolbar`(*self*)[¶](#wx.aui.AuiPaneInfo.IsToolbar "Permalink to this definition")
[`IsToolbar`](#wx.aui.AuiPaneInfo.IsToolbar "wx.aui.AuiPaneInfo.IsToolbar") returns `True` if the pane contains a toolbar.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsTopDockable(self) -> bool:
        """ 

`IsTopDockable`(*self*)[¶](#wx.aui.AuiPaneInfo.IsTopDockable "Permalink to this definition")
[`IsTopDockable`](#wx.aui.AuiPaneInfo.IsTopDockable "wx.aui.AuiPaneInfo.IsTopDockable") returns `True` if the pane can be docked at the top of the managed frame.



Return type
*bool*





See also


[`IsDockable`](#wx.aui.AuiPaneInfo.IsDockable "wx.aui.AuiPaneInfo.IsDockable")





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.aui.AuiPaneInfo.IsValid "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Layer(self, layer: int) -> 'AuiPaneInfo':
        """ 

`Layer`(*self*, *layer*)[¶](#wx.aui.AuiPaneInfo.Layer "Permalink to this definition")
[`Layer`](#wx.aui.AuiPaneInfo.Layer "wx.aui.AuiPaneInfo.Layer") determines the layer of the docked pane.


The dock layer is similar to an onion, the inner-most layer being layer 0. Each shell moving in the outward direction has a higher layer number. This allows for more complex docking layout formation.



Parameters
**layer** (*int*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Left(self) -> 'AuiPaneInfo':
        """ 

`Left`(*self*)[¶](#wx.aui.AuiPaneInfo.Left "Permalink to this definition")
`wx.Left` sets the pane dock position to the left side of the frame.


This is the same thing as calling Direction(wxAUI\_DOCK\_LEFT).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def LeftDockable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`LeftDockable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.LeftDockable "Permalink to this definition")
[`LeftDockable`](#wx.aui.AuiPaneInfo.LeftDockable "wx.aui.AuiPaneInfo.LeftDockable") indicates whether a pane can be docked on the left of the frame.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MaxSize(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`MaxSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.MaxSize "Permalink to this definition")
[`MaxSize`](#wx.aui.AuiPaneInfo.MaxSize "wx.aui.AuiPaneInfo.MaxSize") sets the maximum size of the pane.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**MaxSize** *(self, size)*



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  



**MaxSize** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MaximizeButton(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`MaximizeButton`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.MaximizeButton "Permalink to this definition")
[`MaximizeButton`](#wx.aui.AuiPaneInfo.MaximizeButton "wx.aui.AuiPaneInfo.MaximizeButton") indicates that a maximize button should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MinSize(self, *args, **kw) -> 'AuiPaneInfo':
        """ 

`MinSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.aui.AuiPaneInfo.MinSize "Permalink to this definition")
[`MinSize`](#wx.aui.AuiPaneInfo.MinSize "wx.aui.AuiPaneInfo.MinSize") sets the minimum size of the pane.


Please note that this is only partially supported as of this writing.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**MinSize** *(self, size)*



Parameters
**size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  



**MinSize** *(self, x, y)*



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






---

  





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def MinimizeButton(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`MinimizeButton`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.MinimizeButton "Permalink to this definition")
[`MinimizeButton`](#wx.aui.AuiPaneInfo.MinimizeButton "wx.aui.AuiPaneInfo.MinimizeButton") indicates that a minimize button should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Movable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`Movable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.Movable "Permalink to this definition")
Movable indicates whether a frame can be moved.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Name(self, n: str) -> 'AuiPaneInfo':
        """ 

`Name`(*self*, *n*)[¶](#wx.aui.AuiPaneInfo.Name "Permalink to this definition")
[`Name`](#wx.aui.AuiPaneInfo.Name "wx.aui.AuiPaneInfo.Name") sets the name of the pane so it can be referenced in lookup functions.


If a name is not specified by the user, a random name is assigned to the pane when it is added to the manager.



Parameters
**n** (*string*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def PaneBorder(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`PaneBorder`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.PaneBorder "Permalink to this definition")
PaneBorder indicates that a border should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def PinButton(self, visible: bool=True) -> 'AuiPaneInfo':
        """ 

`PinButton`(*self*, *visible=True*)[¶](#wx.aui.AuiPaneInfo.PinButton "Permalink to this definition")
[`PinButton`](#wx.aui.AuiPaneInfo.PinButton "wx.aui.AuiPaneInfo.PinButton") indicates that a pin button should be drawn for the pane.



Parameters
**visible** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Position(self, pos: int) -> 'AuiPaneInfo':
        """ 

`Position`(*self*, *pos*)[¶](#wx.aui.AuiPaneInfo.Position "Permalink to this definition")
 [wx.Position](wx.Position.html#wx-position) determines the position of the docked pane.



Parameters
**pos** (*int*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Resizable(self, resizable: bool=True) -> 'AuiPaneInfo':
        """ 

`Resizable`(*self*, *resizable=True*)[¶](#wx.aui.AuiPaneInfo.Resizable "Permalink to this definition")
[`Resizable`](#wx.aui.AuiPaneInfo.Resizable "wx.aui.AuiPaneInfo.Resizable") allows a pane to be resized if the parameter is `True`, and forces it to be a fixed size if the parameter is `False`.


This is simply an antonym for [`Fixed`](#wx.aui.AuiPaneInfo.Fixed "wx.aui.AuiPaneInfo.Fixed") .



Parameters
**resizable** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Right(self) -> 'AuiPaneInfo':
        """ 

`Right`(*self*)[¶](#wx.aui.AuiPaneInfo.Right "Permalink to this definition")
`wx.Right` sets the pane dock position to the right side of the frame.


This is the same thing as calling Direction(wxAUI\_DOCK\_RIGHT).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def RightDockable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`RightDockable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.RightDockable "Permalink to this definition")
[`RightDockable`](#wx.aui.AuiPaneInfo.RightDockable "wx.aui.AuiPaneInfo.RightDockable") indicates whether a pane can be docked on the right of the frame.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Row(self, row: int) -> 'AuiPaneInfo':
        """ 

`Row`(*self*, *row*)[¶](#wx.aui.AuiPaneInfo.Row "Permalink to this definition")
[`Row`](#wx.aui.AuiPaneInfo.Row "wx.aui.AuiPaneInfo.Row") determines the row of the docked pane.



Parameters
**row** (*int*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def SafeSet(self, source: 'aui.AuiPaneInfo') -> None:
        """ 

`SafeSet`(*self*, *source*)[¶](#wx.aui.AuiPaneInfo.SafeSet "Permalink to this definition")
Write the safe parts of a PaneInfo object “source” into “this”.


“Safe parts” are all non-UI elements (e.g. all layout determining parameters like the size, position etc.). “Unsafe parts” (pointers to button, frame and window) are not modified by this write operation.



Parameters
**source** ([*wx.aui.AuiPaneInfo*](#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) – 





Note


This method is used when loading perspectives.





            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def SetFlag(self, flag, option_state) -> 'AuiPaneInfo':
        """ 

`SetFlag`(*self*, *flag*, *option\_state*)[¶](#wx.aui.AuiPaneInfo.SetFlag "Permalink to this definition")
[`SetFlag`](#wx.aui.AuiPaneInfo.SetFlag "wx.aui.AuiPaneInfo.SetFlag") turns the property given by flag on or off with the option\_state parameter.



Parameters
* **flag** (*int*) –
* **option\_state** (*bool*) –



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Show(self, show: bool=True) -> 'AuiPaneInfo':
        """ 

`Show`(*self*, *show=True*)[¶](#wx.aui.AuiPaneInfo.Show "Permalink to this definition")
[`Show`](#wx.aui.AuiPaneInfo.Show "wx.aui.AuiPaneInfo.Show") indicates that a pane should be shown.



Parameters
**show** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def ToolbarPane(self) -> 'AuiPaneInfo':
        """ 

`ToolbarPane`(*self*)[¶](#wx.aui.AuiPaneInfo.ToolbarPane "Permalink to this definition")
[`ToolbarPane`](#wx.aui.AuiPaneInfo.ToolbarPane "wx.aui.AuiPaneInfo.ToolbarPane") specifies that the pane should adopt the default toolbar pane settings.



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Top(self) -> 'AuiPaneInfo':
        """ 

`Top`(*self*)[¶](#wx.aui.AuiPaneInfo.Top "Permalink to this definition")
`wx.Top` sets the pane dock position to the top of the frame.


This is the same thing as calling Direction(wxAUI\_DOCK\_TOP).



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def TopDockable(self, b: bool=True) -> 'AuiPaneInfo':
        """ 

`TopDockable`(*self*, *b=True*)[¶](#wx.aui.AuiPaneInfo.TopDockable "Permalink to this definition")
[`TopDockable`](#wx.aui.AuiPaneInfo.TopDockable "wx.aui.AuiPaneInfo.TopDockable") indicates whether a pane can be docked at the top of the frame.



Parameters
**b** (*bool*) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    def Window(self, w: 'Window') -> 'AuiPaneInfo':
        """ 

`Window`(*self*, *w*)[¶](#wx.aui.AuiPaneInfo.Window "Permalink to this definition")
 [wx.Window](wx.Window.html#wx-window) assigns the window pointer that the  [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo) should use.


This normally does not need to be specified, as the window pointer is automatically assigned to the  [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo) structure as soon as it is added to the manager.



Parameters
**w** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
 [wx.aui.AuiPaneInfo](#wx-aui-auipaneinfo)






            Source: https://docs.wxpython.org/wx.aui.AuiPaneInfo.html
        """

    best_size: Any  # `best_size`[¶](#wx.aui.AuiPaneInfo.best_size "Permalink to this definition")A public C++ attribute of type [`Size`](wx.Size.html#wx.Size "wx.Size") . size that the layout engine will prefer
    caption: Any  # `caption`[¶](#wx.aui.AuiPaneInfo.caption "Permalink to this definition")A public C++ attribute of type `string`. caption displayed on the window
    dock_direction: Any  # `dock_direction`[¶](#wx.aui.AuiPaneInfo.dock_direction "Permalink to this definition")A public C++ attribute of type `int`. dock direction (top, bottom, left, right, center)
    dock_layer: Any  # `dock_layer`[¶](#wx.aui.AuiPaneInfo.dock_layer "Permalink to this definition")A public C++ attribute of type `int`. layer number (0 = innermost layer)
    dock_pos: Any  # `dock_pos`[¶](#wx.aui.AuiPaneInfo.dock_pos "Permalink to this definition")A public C++ attribute of type `int`. position inside the row (0 = first position)
    dock_proportion: Any  # `dock_proportion`[¶](#wx.aui.AuiPaneInfo.dock_proportion "Permalink to this definition")A public C++ attribute of type `int`. proportion while docked
    dock_row: Any  # `dock_row`[¶](#wx.aui.AuiPaneInfo.dock_row "Permalink to this definition")A public C++ attribute of type `int`. row number on the docking bar (0 = first row)
    floating_pos: Any  # `floating_pos`[¶](#wx.aui.AuiPaneInfo.floating_pos "Permalink to this definition")A public C++ attribute of type [`Point`](wx.Point.html#wx.Point "wx.Point") . position while floating
    floating_size: Any  # `floating_size`[¶](#wx.aui.AuiPaneInfo.floating_size "Permalink to this definition")A public C++ attribute of type [`Size`](wx.Size.html#wx.Size "wx.Size") . size while floating
    frame: Any  # `frame`[¶](#wx.aui.AuiPaneInfo.frame "Permalink to this definition")A public C++ attribute of type [`Frame`](wx.Frame.html#wx.Frame "wx.Frame") . floating frame window that holds the pane
    icon: Any  # `icon`[¶](#wx.aui.AuiPaneInfo.icon "Permalink to this definition")A public C++ attribute of type [`BitmapBundle`](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle") . icon of the pane, may be invalid
    max_size: Any  # `max_size`[¶](#wx.aui.AuiPaneInfo.max_size "Permalink to this definition")A public C++ attribute of type [`Size`](wx.Size.html#wx.Size "wx.Size") . maximum size the pane window can tolerate
    min_size: Any  # `min_size`[¶](#wx.aui.AuiPaneInfo.min_size "Permalink to this definition")A public C++ attribute of type [`Size`](wx.Size.html#wx.Size "wx.Size") . minimum size the pane window can tolerate
    name: Any  # `name`[¶](#wx.aui.AuiPaneInfo.name "Permalink to this definition")A public C++ attribute of type `string`. name of the pane
    rect: Any  # `rect`[¶](#wx.aui.AuiPaneInfo.rect "Permalink to this definition")A public C++ attribute of type [`Rect`](wx.Rect.html#wx.Rect "wx.Rect") . current rectangle (populated by `AUI`)
    state: Any  # `state`[¶](#wx.aui.AuiPaneInfo.state "Permalink to this definition")A public C++ attribute of type `int`. a combination of PaneState values
    window: Any  # `window`[¶](#wx.aui.AuiPaneInfo.window "Permalink to this definition")A public C++ attribute of type [`Window`](wx.Window.html#wx.Window "wx.Window") . window that is in this pane



class AuiDockArt:
    """ **Possible constructors**:



```
AuiDockArt()

```


AuiDockArt is part of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiDockArt.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def Clone(self) -> 'AuiDockArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiDockArt.Clone "Permalink to this definition")
Create a copy of this  [wx.aui.AuiDockArt](#wx-aui-auidockart) instance.



Return type
 [wx.aui.AuiDockArt](#wx-aui-auidockart)






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawBackground(self, dc, window, orientation, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *window*, *orientation*, *rect*)[¶](#wx.aui.AuiDockArt.DrawBackground "Permalink to this definition")
Draws a background.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **orientation** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawBorder(self, dc, window, rect, pane) -> None:
        """ 

`DrawBorder`(*self*, *dc*, *window*, *rect*, *pane*)[¶](#wx.aui.AuiDockArt.DrawBorder "Permalink to this definition")
Draws a border.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawCaption(self, dc, window, text, rect, pane) -> None:
        """ 

`DrawCaption`(*self*, *dc*, *window*, *text*, *rect*, *pane*)[¶](#wx.aui.AuiDockArt.DrawCaption "Permalink to this definition")
Draws a caption.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **text** (*string*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawGripper(self, dc, window, rect, pane) -> None:
        """ 

`DrawGripper`(*self*, *dc*, *window*, *rect*, *pane*)[¶](#wx.aui.AuiDockArt.DrawGripper "Permalink to this definition")
Draws a gripper.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawPaneButton(self, dc, window, button, button_state, rect, pane) -> None:
        """ 

`DrawPaneButton`(*self*, *dc*, *window*, *button*, *button\_state*, *rect*, *pane*)[¶](#wx.aui.AuiDockArt.DrawPaneButton "Permalink to this definition")
Draws a button in the pane’s title bar.


*button* can be one of the values of **AuiButtonId**. *button\_state* can be one of the values of **AuiPaneButtonState**.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **button** (*int*) –
* **button\_state** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def DrawSash(self, dc, window, orientation, rect) -> None:
        """ 

`DrawSash`(*self*, *dc*, *window*, *orientation*, *rect*)[¶](#wx.aui.AuiDockArt.DrawSash "Permalink to this definition")
Draws a sash between two windows.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **orientation** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ 

`GetColour`(*self*, *id*)[¶](#wx.aui.AuiDockArt.GetColour "Permalink to this definition")
Get the colour of a certain setting.


*id* can be one of the colour values of **AuiPaneDockArtSetting**.



Parameters
**id** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ 

`GetFont`(*self*, *id*)[¶](#wx.aui.AuiDockArt.GetFont "Permalink to this definition")
Get a font setting.



Parameters
**id** (*int*) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def GetMetric(self, id: int) -> int:
        """ 

`GetMetric`(*self*, *id*)[¶](#wx.aui.AuiDockArt.GetMetric "Permalink to this definition")
Get the value of a certain setting.


*id* can be one of the size values of **AuiPaneDockArtSetting**.



Parameters
**id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetColour(self, id, colour) -> None:
        """ 

`SetColour`(*self*, *id*, *colour*)[¶](#wx.aui.AuiDockArt.SetColour "Permalink to this definition")
Set a certain setting with the value *colour*.


*id* can be one of the colour values of **AuiPaneDockArtSetting**.



Parameters
* **id** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetFont(self, id, font) -> None:
        """ 

`SetFont`(*self*, *id*, *font*)[¶](#wx.aui.AuiDockArt.SetFont "Permalink to this definition")
Set a font setting.



Parameters
* **id** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ 

`SetMetric`(*self*, *id*, *new\_val*)[¶](#wx.aui.AuiDockArt.SetMetric "Permalink to this definition")
Set a certain setting with the value *new\_val*.


*id* can be one of the size values of **AuiPaneDockArtSetting**.



Parameters
* **id** (*int*) –
* **new\_val** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiDockArt.html
        """



AuiManagerOption: TypeAlias = int  # Enumeration

class AuiDefaultToolBarArt(AuiToolBarArt):
    """ **Possible constructors**:



```
AuiDefaultToolBarArt()

```


AuiDefaultToolBarArt is part of the `AUI` class framework.


  


        Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiDefaultToolBarArt.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def Clone(self) -> 'AuiToolBarArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiDefaultToolBarArt.Clone "Permalink to this definition")

Return type
 [wx.aui.AuiToolBarArt](wx.aui.AuiToolBarArt.html#wx-aui-auitoolbarart)






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawBackground "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawControlLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawControlLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawControlLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawDropDownButton(self, dc, wnd, item, rect) -> None:
        """ 

`DrawDropDownButton`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawDropDownButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawGripper(self, dc, wnd, rect) -> None:
        """ 

`DrawGripper`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawGripper "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawLabel(self, dc, wnd, item, rect) -> None:
        """ 

`DrawLabel`(*self*, *dc*, *wnd*, *item*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawOverflowButton(self, dc, wnd, rect, state) -> None:
        """ 

`DrawOverflowButton`(*self*, *dc*, *wnd*, *rect*, *state*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawOverflowButton "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **state** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawPlainBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPlainBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawPlainBackground "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def DrawSeparator(self, dc, wnd, rect) -> None:
        """ 

`DrawSeparator`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.aui.AuiDefaultToolBarArt.DrawSeparator "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetElementSize(self, element: int) -> int:
        """ 

`GetElementSize`(*self*, *element*)[¶](#wx.aui.AuiDefaultToolBarArt.GetElementSize "Permalink to this definition")

Parameters
**element** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.aui.AuiDefaultToolBarArt.GetFlags "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.aui.AuiDefaultToolBarArt.GetFont "Permalink to this definition")

Return type
[`Font`](#wx.aui.AuiDefaultToolBarArt.Font "wx.aui.AuiDefaultToolBarArt.Font")






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetLabelSize(self, dc, wnd, item) -> 'Size':
        """ 

`GetLabelSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.aui.AuiDefaultToolBarArt.GetLabelSize "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetTextOrientation(self) -> int:
        """ 

`GetTextOrientation`(*self*)[¶](#wx.aui.AuiDefaultToolBarArt.GetTextOrientation "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def GetToolSize(self, dc, wnd, item) -> 'Size':
        """ 

`GetToolSize`(*self*, *dc*, *wnd*, *item*)[¶](#wx.aui.AuiDefaultToolBarArt.GetToolSize "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **item** ([*wx.aui.AuiToolBarItem*](wx.aui.AuiToolBarItem.html#wx.aui.AuiToolBarItem "wx.aui.AuiToolBarItem")) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetElementSize(self, element_id, size) -> None:
        """ 

`SetElementSize`(*self*, *element\_id*, *size*)[¶](#wx.aui.AuiDefaultToolBarArt.SetElementSize "Permalink to this definition")

Parameters
* **element\_id** (*int*) –
* **size** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.aui.AuiDefaultToolBarArt.SetFlags "Permalink to this definition")

Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.aui.AuiDefaultToolBarArt.SetFont "Permalink to this definition")

Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def SetTextOrientation(self, orientation: int) -> None:
        """ 

`SetTextOrientation`(*self*, *orientation*)[¶](#wx.aui.AuiDefaultToolBarArt.SetTextOrientation "Permalink to this definition")

Parameters
**orientation** (*int*) – 






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    def ShowDropDown(self, wnd, items) -> int:
        """ 

`ShowDropDown`(*self*, *wnd*, *items*)[¶](#wx.aui.AuiDefaultToolBarArt.ShowDropDown "Permalink to this definition")

Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **items** (*AuiToolBarItemArray*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultToolBarArt.html
        """

    Flags: int  # `Flags`[¶](#wx.aui.AuiDefaultToolBarArt.Flags "Permalink to this definition")See [`GetFlags`](#wx.aui.AuiDefaultToolBarArt.GetFlags "wx.aui.AuiDefaultToolBarArt.GetFlags") and [`SetFlags`](#wx.aui.AuiDefaultToolBarArt.SetFlags "wx.aui.AuiDefaultToolBarArt.SetFlags")
    Font: '_Font'  # `Font`[¶](#wx.aui.AuiDefaultToolBarArt.Font "Permalink to this definition")See [`GetFont`](#wx.aui.AuiDefaultToolBarArt.GetFont "wx.aui.AuiDefaultToolBarArt.GetFont") and [`SetFont`](#wx.aui.AuiDefaultToolBarArt.SetFont "wx.aui.AuiDefaultToolBarArt.SetFont")
    TextOrientation: int  # `TextOrientation`[¶](#wx.aui.AuiDefaultToolBarArt.TextOrientation "Permalink to this definition")See [`GetTextOrientation`](#wx.aui.AuiDefaultToolBarArt.GetTextOrientation "wx.aui.AuiDefaultToolBarArt.GetTextOrientation") and [`SetTextOrientation`](#wx.aui.AuiDefaultToolBarArt.SetTextOrientation "wx.aui.AuiDefaultToolBarArt.SetTextOrientation")



class AuiDefaultDockArt(AuiDockArt):
    """ **Possible constructors**:



```
AuiDefaultDockArt()

```


This is the default art provider for AuiManager.


  


        Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.aui.AuiDefaultDockArt.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def Clone(self) -> 'AuiDockArt':
        """ 

`Clone`(*self*)[¶](#wx.aui.AuiDefaultDockArt.Clone "Permalink to this definition")
Create a copy of this  [wx.aui.AuiDockArt](wx.aui.AuiDockArt.html#wx-aui-auidockart) instance.



Return type
 [wx.aui.AuiDockArt](wx.aui.AuiDockArt.html#wx-aui-auidockart)






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawBackground(self, dc, window, orientation, rect) -> None:
        """ 

`DrawBackground`(*self*, *dc*, *window*, *orientation*, *rect*)[¶](#wx.aui.AuiDefaultDockArt.DrawBackground "Permalink to this definition")
Draws a background.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **orientation** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawBorder(self, dc, window, rect, pane) -> None:
        """ 

`DrawBorder`(*self*, *dc*, *window*, *rect*, *pane*)[¶](#wx.aui.AuiDefaultDockArt.DrawBorder "Permalink to this definition")
Draws a border.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawCaption(self, dc, window, text, rect, pane) -> None:
        """ 

`DrawCaption`(*self*, *dc*, *window*, *text*, *rect*, *pane*)[¶](#wx.aui.AuiDefaultDockArt.DrawCaption "Permalink to this definition")
Draws a caption.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **text** (*string*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawGripper(self, dc, window, rect, pane) -> None:
        """ 

`DrawGripper`(*self*, *dc*, *window*, *rect*, *pane*)[¶](#wx.aui.AuiDefaultDockArt.DrawGripper "Permalink to this definition")
Draws a gripper.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawIcon(self, dc, rect, pane) -> None:
        """ 

`DrawIcon`(*self*, *dc*, *rect*, *pane*)[¶](#wx.aui.AuiDefaultDockArt.DrawIcon "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –





Deprecated


Not intended for the public API.





            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawPaneButton(self, dc, window, button, button_state, rect, pane) -> None:
        """ 

`DrawPaneButton`(*self*, *dc*, *window*, *button*, *button\_state*, *rect*, *pane*)[¶](#wx.aui.AuiDefaultDockArt.DrawPaneButton "Permalink to this definition")
Draws a button in the pane’s title bar.


*button* can be one of the values of **AuiButtonId**. *button\_state* can be one of the values of **AuiPaneButtonState**.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **button** (*int*) –
* **button\_state** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **pane** ([*wx.aui.AuiPaneInfo*](wx.aui.AuiPaneInfo.html#wx.aui.AuiPaneInfo "wx.aui.AuiPaneInfo")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def DrawSash(self, dc, window, orientation, rect) -> None:
        """ 

`DrawSash`(*self*, *dc*, *window*, *orientation*, *rect*)[¶](#wx.aui.AuiDefaultDockArt.DrawSash "Permalink to this definition")
Draws a sash between two windows.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **orientation** (*int*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ 

`GetColour`(*self*, *id*)[¶](#wx.aui.AuiDefaultDockArt.GetColour "Permalink to this definition")
Get the colour of a certain setting.


*id* can be one of the colour values of **AuiPaneDockArtSetting**.



Parameters
**id** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ 

`GetFont`(*self*, *id*)[¶](#wx.aui.AuiDefaultDockArt.GetFont "Permalink to this definition")
Get a font setting.



Parameters
**id** (*int*) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def GetMetric(self, id: int) -> int:
        """ 

`GetMetric`(*self*, *id*)[¶](#wx.aui.AuiDefaultDockArt.GetMetric "Permalink to this definition")
Get the value of a certain setting.


*id* can be one of the size values of **AuiPaneDockArtSetting**.



Parameters
**id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetColour(self, id, colour) -> None:
        """ 

`SetColour`(*self*, *id*, *colour*)[¶](#wx.aui.AuiDefaultDockArt.SetColour "Permalink to this definition")
Set a certain setting with the value *colour*.


*id* can be one of the colour values of **AuiPaneDockArtSetting**.



Parameters
* **id** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetFont(self, id, font) -> None:
        """ 

`SetFont`(*self*, *id*, *font*)[¶](#wx.aui.AuiDefaultDockArt.SetFont "Permalink to this definition")
Set a font setting.



Parameters
* **id** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ 

`SetMetric`(*self*, *id*, *new\_val*)[¶](#wx.aui.AuiDefaultDockArt.SetMetric "Permalink to this definition")
Set a certain setting with the value *new\_val*.


*id* can be one of the size values of **AuiPaneDockArtSetting**.



Parameters
* **id** (*int*) –
* **new\_val** (*int*) –






            Source: https://docs.wxpython.org/wx.aui.AuiDefaultDockArt.html
        """



AuiPaneInfoArray: TypeAlias = list['AuiPaneInfo']

