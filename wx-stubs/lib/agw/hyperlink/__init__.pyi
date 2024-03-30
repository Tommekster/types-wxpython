# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class HyperLinkCtrl(GenStaticText):
    """ [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") is a control for wxPython that acts like a hyper
link in a typical browser. Latest features include the ability to
capture your own left, middle, and right click events to perform
your own custom event handling and ability to open link in a new
or current browser window.


  


        Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
    """
    def __init__(self, parent, id=-1, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name="staticText", URL="") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *label=""*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=0*, *name="staticText"*, *URL=""*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** – the window parent. Must not be `None`;
* **id** – window identifier. A value of -1 indicates a default value;
* **label** – the control label;
* **pos** – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** – the window style;
* **name** – the window name;
* **URL** – a string specifying the url link to navigate to.





Note


Pass URL=”” to use the label as the url link to navigate to.





            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def AutoBrowse(self, AutoBrowse: bool=True) -> None:
        """ 

`AutoBrowse`(*self*, *AutoBrowse=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.AutoBrowse "Permalink to this definition")
Automatically browse to URL when clicked.



Parameters
**AutoBrowse** – `True` to automatically browse to an URL when clicked,
`False` otherwise.





Note


Set [`AutoBrowse`](#wx.lib.agw.hyperlink.HyperLinkCtrl.AutoBrowse "wx.lib.agw.hyperlink.HyperLinkCtrl.AutoBrowse") to `False` to receive `EVT_HYPERLINK_LEFT` events.





            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def DisplayError(self, ErrorMessage, ReportErrors=True) -> None:
        """ 

`DisplayError`(*self*, *ErrorMessage*, *ReportErrors=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.DisplayError "Permalink to this definition")
Displays an error message (according to the [`ReportErrors`](#wx.lib.agw.hyperlink.HyperLinkCtrl.ReportErrors "wx.lib.agw.hyperlink.HyperLinkCtrl.ReportErrors") parameter) in a
`MessageBox`.



Parameters
* **ErrorMessage** – a string representing the error to display;
* **ReportErrors** – `True` to display error dialog if an error occurs
navigating to the URL.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def DoPopup(self, DoPopup: bool=True) -> None:
        """ 

`DoPopup`(*self*, *DoPopup=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.DoPopup "Permalink to this definition")
Sets whether to show popup menu on right click or not.



Parameters
**DoPopup** – `True` to show a popup menu on right click, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def EnableRollover(self, EnableRollover: bool=False) -> None:
        """ 

`EnableRollover`(*self*, *EnableRollover=False*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.EnableRollover "Permalink to this definition")
Enable/disable rollover.



Parameters
**EnableRollover** – `True` to enable text effects during rollover,
`False` to disable them.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetBold(self) -> None:
        """ 

`GetBold`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetBold "Permalink to this definition")
Returns whether the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") has text in bold or not.




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetColours(self) -> None:
        """ 

`GetColours`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetColours "Permalink to this definition")
Gets the colours for the link, the visited link and the mouse
rollover.




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetLinkCursor(self) -> None:
        """ 

`GetLinkCursor`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetLinkCursor "Permalink to this definition")
Gets the link cursor.




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetUnderlines(self) -> None:
        """ 

`GetUnderlines`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetUnderlines "Permalink to this definition")
Returns if link is underlined, if the mouse rollover is
underlined and if the visited link is underlined.




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetURL(self) -> None:
        """ 

`GetURL`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetURL "Permalink to this definition")
Retrieve the URL associated to the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl").




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GetVisited(self) -> None:
        """ 

`GetVisited`(*self*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GetVisited "Permalink to this definition")
Returns whether a link has been visited or not.




            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def GotoURL(self, URL, ReportErrors=True, NotSameWinIfPossible=False) -> None:
        """ 

`GotoURL`(*self*, *URL*, *ReportErrors=True*, *NotSameWinIfPossible=False*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.GotoURL "Permalink to this definition")
Goto the specified URL.



Parameters
* **URL** – the url link we wish to navigate;
* **ReportErrors** – Use `True` to display error dialog if an error
occurs navigating to the URL;
* **NotSameWinIfPossible** – Use `True` to attempt to open the URL
in new browser window.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OnMouseEvent(self, event: MouseEvent) -> None:
        """ 

`OnMouseEvent`(*self*, *event*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.OnMouseEvent "Permalink to this definition")
Handles the `wx.EVT_MOUSE_EVENTS` events for [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl").



Parameters
**event** – a `MouseEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OnPopUpCopy(self, event: 'MenuEvent') -> None:
        """ 

`OnPopUpCopy`(*self*, *event*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.OnPopUpCopy "Permalink to this definition")
Handles the `wx.EVT_MENU` event for [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl").



Parameters
**event** – a [`wx.MenuEvent`](wx.MenuEvent.html#wx.MenuEvent "wx.MenuEvent") event to be processed.





Note


This method copies the data from the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") to the clipboard.





            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def OpenInSameWindow(self, NotSameWinIfPossible: bool=False) -> None:
        """ 

`OpenInSameWindow`(*self*, *NotSameWinIfPossible=False*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.OpenInSameWindow "Permalink to this definition")
Open multiple URL in the same window (if possible).



Parameters
**NotSameWinIfPossible** – `True` to open an hyperlink in a new browser
window, `False` to use an existing browser window.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def ReportErrors(self, ReportErrors: bool=True) -> None:
        """ 

`ReportErrors`(*self*, *ReportErrors=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.ReportErrors "Permalink to this definition")
Set whether to report browser errors or not.



Parameters
**ReportErrors** – Use `True` to display error dialog if an error
occurs navigating to the URL;






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetBold(self, Bold: bool=False) -> None:
        """ 

`SetBold`(*self*, *Bold=False*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetBold "Permalink to this definition")
Sets the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") label in bold text.



Parameters
**Bold** – `True` to set the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") label as bold, `False`
otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetColours(*args, **kwargs) -> None:
        """ 

`SetColours`(*self*, *link=wx.BLUE*, *visited=wx.Colour(79*, *47*, *79)*, *rollover=wx.BLUE*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetColours "Permalink to this definition")
Sets the colours for the link, the visited link and the mouse rollover.


* Visited link: VIOLET
* Rollover: BLUE



Parameters
* **link** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") to use as text foreground for new links
(default=RED);
* **visited** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") to use as text foreground for visited
links (default=VIOLET);
* **rollover** – a valid [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") to use as text foreground for links
rollovers (default=BLUE).






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetLinkCursor(self, cur: Cursor=wx.CURSOR_HAND) -> None:
        """ 

`SetLinkCursor`(*self*, *cur=wx.CURSOR\_HAND*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetLinkCursor "Permalink to this definition")
Sets link cursor properties.



Parameters
**cur** – an integer representing a `Cursor` constant.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetUnderlines(self, link=True, visited=True, rollover=True) -> None:
        """ 

`SetUnderlines`(*self*, *link=True*, *visited=True*, *rollover=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetUnderlines "Permalink to this definition")
Sets whether the text should be underlined or not for new links, visited
links and rollovers.



Parameters
* **link** – `True` to set the text of new links as underlined, `False`
otherwise;
* **visited** – `True` to set the text of visited links as underlined,
`False` otherwise;
* **rollover** – `True` to set the text of rollovers as underlined,
`False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetURL(self, URL: HyperLinkCtrl) -> None:
        """ 

`SetURL`(*self*, *URL*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetURL "Permalink to this definition")
Sets the [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl") text to the specified URL.



Parameters
**URL** – the new URL associated with [`HyperLinkCtrl`](#wx.lib.agw.hyperlink.HyperLinkCtrl "wx.lib.agw.hyperlink.HyperLinkCtrl").






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def SetVisited(self, Visited: bool=False) -> None:
        """ 

`SetVisited`(*self*, *Visited=False*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.SetVisited "Permalink to this definition")
Sets a link as visited.



Parameters
**Visited** – `True` to set a link as visited, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """

    def UpdateLink(self, OnRefresh: bool=True) -> None:
        """ 

`UpdateLink`(*self*, *OnRefresh=True*)[¶](#wx.lib.agw.hyperlink.HyperLinkCtrl.UpdateLink "Permalink to this definition")
Updates the link, changing text properties if:


* User specific setting;
* Link visited;
* New link;



Parameters
**OnRefresh** – `True` to refresh the control, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.hyperlink.HyperLinkCtrl.html
        """



EVT_MOUSE_EVENTS: int

EVT_MENU: int

