# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class AuiManager(EvtHandler):
    """ AuiManager manages the panes associated with it for a particular [`wx.Frame`](wx.Frame.html#wx.Frame "wx.Frame"),
using a pane’s [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") information to determine each pane’s docking and
floating behavior. [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") uses wxPython’s sizer mechanism to plan the
layout of each frame. It uses a replaceable dock art class to do all drawing,
so all drawing is localized in one area, and may be customized depending on an
applications’ specific needs.


[`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") works as follows: the programmer adds panes to the class, or makes
changes to existing pane properties (dock position, floating state, show state, etc…).
To apply these changes, the [`AuiManager.Update()`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update") function is called. This batch
processing can be used to avoid flicker, by modifying more than one pane at a time,
and then “committing” all of the changes at once by calling *Update()*.


Panes can be added quite easily:



```
text1 = wx.TextCtrl(self, -1)
text2 = wx.TextCtrl(self, -1)
self._mgr.AddPane(text1, AuiPaneInfo().Left().Caption("Pane Number One"))
self._mgr.AddPane(text2, AuiPaneInfo().Bottom().Caption("Pane Number Two"))

self._mgr.Update()

```


Later on, the positions can be modified easily. The following will float an
existing pane in a tool window:



```
self._mgr.GetPane(text1).Float()

```


**Layers, Rows and Directions, Positions:**


Inside AUI, the docking layout is figured out by checking several pane parameters.
Four of these are important for determining where a pane will end up.


**Direction** - Each docked pane has a direction, *Top*, *Bottom*, *Left*, *Right*, or *Center*.
This is fairly self-explanatory. The pane will be placed in the location specified
by this variable.


**Position** - More than one pane can be placed inside of a “dock”. Imagine two panes
being docked on the left side of a window. One pane can be placed over another.
In proportionally managed docks, the pane position indicates it’s sequential position,
starting with zero. So, in our scenario with two panes docked on the left side, the
top pane in the dock would have position 0, and the second one would occupy position 1.


**Row** - A row can allow for two docks to be placed next to each other. One of the most
common places for this to happen is in the toolbar. Multiple toolbar rows are allowed,
the first row being in row 0, and the second in row 1. Rows can also be used on
vertically docked panes.


**Layer** - A layer is akin to an onion. Layer 0 is the very center of the managed pane.
Thus, if a pane is in layer 0, it will be closest to the center window (also sometimes
known as the “content window”). Increasing layers “swallow up” all layers of a lower
value. This can look very similar to multiple rows, but is different because all panes
in a lower level yield to panes in higher levels. The best way to understand layers
is by running the AUI sample (*AUI.py*).


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
    """
    def __init__(self, managed_window=None, agwFlags=None) -> None:
        """ 

`__init__`(*self*, *managed\_window=None*, *agwFlags=None*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **managed\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – specifies the window which should be managed;
* **agwFlags** (*integer*) – specifies options which allow the frame management behavior to be
modified. *agwFlags* can be a combination of the following style bits:







| Flag name | Description |
| --- | --- |
| `AUI_MGR_ALLOW_FLOATING` | Allow floating of panes |
| `AUI_MGR_ALLOW_ACTIVE_PANE` | If a pane becomes active, “highlight” it in the interface |
| `AUI_MGR_TRANSPARENT_DRAG` | If the platform supports it, set transparency on a floating pane while it is dragged by the user |
| `AUI_MGR_TRANSPARENT_HINT` | If the platform supports it, show a transparent hint window when the user is about to dock a floating pane |
| `AUI_MGR_VENETIAN_BLINDS_HINT` | Show a “venetian blind” effect when the user is about to dock a floating pane |
| `AUI_MGR_RECTANGLE_HINT` | Show a rectangle hint effect when the user is about to dock a floating pane |
| `AUI_MGR_HINT_FADE` | If the platform supports it, the hint window will fade in and out |
| `AUI_MGR_NO_VENETIAN_BLINDS_FADE` | Disables the “venetian blind” fade in and out |
| `AUI_MGR_LIVE_RESIZE` | Live resize when the user drag a sash |
| `AUI_MGR_ANIMATE_FRAMES` | Fade-out floating panes when they are closed (all platforms which support frames transparency) and show a moving rectangle when they are docked (Windows < Vista and GTK only) |
| `AUI_MGR_AERO_DOCKING_GUIDES` | Use the new Aero-style bitmaps as docking guides |
| `AUI_MGR_PREVIEW_MINIMIZED_PANES` | Slide in and out minimized panes to preview them |
| `AUI_MGR_WHIDBEY_DOCKING_GUIDES` | Use the new Whidbey-style bitmaps as docking guides |
| `AUI_MGR_SMOOTH_DOCKING` | Performs a “smooth” docking of panes (a la PyQT) |
| `AUI_MGR_USE_NATIVE_MINIFRAMES` | Use miniframes with native caption bar as floating panes instead or custom drawn caption bars (forced on wxMAC) |
| `AUI_MGR_AUTONB_NO_CAPTION` | Panes that merge into an automatic notebook will not have the pane caption visible |


Default value for *agwFlags* is:
`AUI_MGR_DEFAULT` = `AUI_MGR_ALLOW_FLOATING` | `AUI_MGR_TRANSPARENT_HINT` | `AUI_MGR_HINT_FADE` | `AUI_MGR_NO_VENETIAN_BLINDS_FADE`



Note


If using the `AUI_MGR_USE_NATIVE_MINIFRAMES`, double-clicking on a
floating pane caption will not re-dock the pane, but simply maximize it (if
[`AuiPaneInfo.MaximizeButton`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaximizeButton "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaximizeButton") has been set to `True`) or do nothing.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ActivatePane(self, window: 'Window') -> None:
        """ 

`ActivatePane`(*self*, *window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ActivatePane "Permalink to this definition")
Activates the pane to which *window* is associated.



Parameters
**window** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane(self, window, arg1=None, arg2=None, target=None) -> None:
        """ 

`AddPane`(*self*, *window*, *arg1=None*, *arg2=None*, *target=None*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "Permalink to this definition")
Tells the frame manager to start managing a child window. There
are four versions of this function. The first version allows the full spectrum
of pane parameter possibilities ( [`AddPane1`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane1 "wx.lib.agw.aui.framemanager.AuiManager.AddPane1")). The second version is used for
simpler user interfaces which do not require as much configuration ( [`AddPane2`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane2 "wx.lib.agw.aui.framemanager.AuiManager.AddPane2")).
The [`AddPane3`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane3 "wx.lib.agw.aui.framemanager.AuiManager.AddPane3") version allows a drop position to be specified, which will determine
where the pane will be added. The [`AddPane4`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane4 "wx.lib.agw.aui.framemanager.AuiManager.AddPane4") version allows to turn the target
[`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") pane into a notebook and the added pane into a page.


In your code, simply call [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane").



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the child window to manage;
* **arg1** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") or an integer value (direction);
* **arg2** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") or a [`wx.Point`](wx.Point.html#wx.Point "wx.Point") (drop position);
* **target** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") to be turned into a notebook
and new pane added to it as a page. (additionally, target can be any pane in
an existing notebook)






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane1(self, window, pane_info) -> None:
        """ 

`AddPane1`(*self*, *window*, *pane\_info*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AddPane1 "Permalink to this definition")
See comments on [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane2(self, window, direction, caption) -> None:
        """ 

`AddPane2`(*self*, *window*, *direction*, *caption*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AddPane2 "Permalink to this definition")
See comments on [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane3(self, window, pane_info, drop_pos) -> None:
        """ 

`AddPane3`(*self*, *window*, *pane\_info*, *drop\_pos*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AddPane3 "Permalink to this definition")
See comments on [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AddPane4(self, window, pane_info, target) -> None:
        """ 

`AddPane4`(*self*, *window*, *pane\_info*, *target*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AddPane4 "Permalink to this definition")
See comments on [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def AnimateDocking(self, win_rect, pane_rect) -> None:
        """ 

`AnimateDocking`(*self*, *win\_rect*, *pane\_rect*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.AnimateDocking "Permalink to this definition")
Animates the minimization/docking of a pane a la Eclipse, using a `ScreenDC`
to draw a “moving docking rectangle” on the screen.



Parameters
* **win\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the original pane screen rectangle;
* **pane\_rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the newly created toolbar/pane screen rectangle.





Note


This functionality is not available on wxMAC as this platform doesn’t have
the ability to use `ScreenDC` to draw on-screen and on Windows > Vista.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculateDockSizerLimits(self, dock: AuiDockInfo) -> None:
        """ 

`CalculateDockSizerLimits`(*self*, *dock*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CalculateDockSizerLimits "Permalink to this definition")
Calculates the minimum and maximum sizes allowed for the input dock.



Parameters
**dock** – the [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structure to analyze.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculateHintRect(self, pane_window, pt, offset) -> None:
        """ 

`CalculateHintRect`(*self*, *pane\_window*, *pt*, *offset*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CalculateHintRect "Permalink to this definition")
Calculates the drop hint rectangle.


The method first calls [`DoDrop`](#wx.lib.agw.aui.framemanager.AuiManager.DoDrop "wx.lib.agw.aui.framemanager.AuiManager.DoDrop") to determine the exact position the pane would
be at were if dropped. If the pane would indeed become docked at the
specified drop point, the the rectangle hint will be returned in
screen coordinates. Otherwise, an empty rectangle is returned.



Parameters
* **pane\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – it is the window pointer of the pane being dragged;
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – is the mouse position, in client coordinates;
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – describes the offset that the mouse is from the upper-left
corner of the item being dragged.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CalculatePaneSizerLimits(self, dock, pane) -> None:
        """ 

`CalculatePaneSizerLimits`(*self*, *dock*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CalculatePaneSizerLimits "Permalink to this definition")
Calculates the minimum and maximum sizes allowed for the input pane.



Parameters
* **dock** – the [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structure to which *pane* belongs to;
* **pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") class for which calculation are requested.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CanDockPanel(self, p: AuiPaneInfo) -> None:
        """ 

`CanDockPanel`(*self*, *p*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CanDockPanel "Permalink to this definition")
Returns whether a pane can be docked or not.



Parameters
**p** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") class with all the pane’s information.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CanUseModernDockArt(self) -> None:
        """ 

`CanUseModernDockArt`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CanUseModernDockArt "Permalink to this definition")
Returns whether `dockart` can be used (Windows XP / Vista / 7 only,
requires Mark Hammonds’s [pywin32](https://sourceforge.net/projects/pywin32/) package).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CheckMovableSizer(self, part: AuiDockUIPart) -> None:
        """ 

`CheckMovableSizer`(*self*, *part*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CheckMovableSizer "Permalink to this definition")
Checks if a UI part can be actually resized.



Parameters
**part** – a UI part, an instance of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CheckPaneMove(self, pane: AuiPaneInfo) -> None:
        """ 

`CheckPaneMove`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CheckPaneMove "Permalink to this definition")
Checks if a pane has moved by a visible amount.



Parameters
**pane** – an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ClosePane(self, pane_info: AuiPaneInfo) -> None:
        """ 

`ClosePane`(*self*, *pane\_info*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ClosePane "Permalink to this definition")
Destroys or hides the pane depending on its flags.



Parameters
**pane\_info** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CopyTarget(self, target: AuiPaneInfo) -> None:
        """ 

`CopyTarget`(*self*, *target*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CopyTarget "Permalink to this definition")
Copies all the attributes of the input *target* into another [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").



Parameters
**target** – the source [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") from where to copy attributes.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateFloatingFrame(self, parent, pane_info) -> None:
        """ 

`CreateFloatingFrame`(*self*, *parent*, *pane\_info*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CreateFloatingFrame "Permalink to this definition")
Creates a floating frame for the windows.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the floating frame parent;
* **pane\_info** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") class with all the pane’s information.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateGuideWindows(self) -> None:
        """ 

`CreateGuideWindows`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CreateGuideWindows "Permalink to this definition")
Creates the VS2005 HUD guide windows.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateHintWindow(self) -> None:
        """ 

`CreateHintWindow`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CreateHintWindow "Permalink to this definition")
Creates the standard wxAUI hint window.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateNotebook(self) -> None:
        """ 

`CreateNotebook`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CreateNotebook "Permalink to this definition")
Creates an automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") when a pane is docked on
top of another pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def CreateNotebookBase(self, panes, paneInfo) -> None:
        """ 

`CreateNotebookBase`(*self*, *panes*, *paneInfo*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.CreateNotebookBase "Permalink to this definition")
Creates an auto-notebook base from a pane, and then add that pane as a page.



Parameters
* **panes** (*list*) – set of panes to append new notebook base pane to
* **paneInfo** – the pane to be converted to a new notebook, an instance of
[`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DestroyGuideWindows(self) -> None:
        """ 

`DestroyGuideWindows`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DestroyGuideWindows "Permalink to this definition")
Destroys the VS2005 HUD guide windows.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DestroyHintWindow(self) -> None:
        """ 

`DestroyHintWindow`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DestroyHintWindow "Permalink to this definition")
Destroys the standard wxAUI hint window.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DetachPane(self, window: 'Window') -> None:
        """ 

`DetachPane`(*self*, *window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DetachPane "Permalink to this definition")
Tells the [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to stop managing the pane specified
by *window*. The window, if in a floated frame, is reparented to the frame
managed by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window to be un-managed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDrop(*args, **kwargs) -> None:
        """ 

`DoDrop`(*self*, *docks*, *panes*, *target*, *pt*, *offset=wx.Point(0*, *0)*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDrop "Permalink to this definition")
This is an important function. It basically takes a mouse position,
and determines where the panes new position would be. If the pane is to be
dropped, it performs the drop operation using the specified dock and pane
arrays. By specifying copy dock and pane arrays when calling, a “what-if”
scenario can be performed, giving precise coordinates for drop hints.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a mouse position to check for a drop operation;
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a possible offset from the input point *pt*.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropFloatingPane(self, docks, panes, target, pt) -> None:
        """ 

`DoDropFloatingPane`(*self*, *docks*, *panes*, *target*, *pt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropFloatingPane "Permalink to this definition")
Handles the situation in which the dropped pane contains a normal window.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **target** – the target pane containing the window, an instance of
[`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a mouse position to check for a drop operation.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropLayer(self, docks, target, dock_direction) -> None:
        """ 

`DoDropLayer`(*self*, *docks*, *target*, *dock\_direction*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropLayer "Permalink to this definition")
Handles the situation in which *target* is a single dock guide.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **target** – the target pane, an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **dock\_direction** (*integer*) – the docking direction.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropNonFloatingPane(self, docks, panes, target, pt) -> None:
        """ 

`DoDropNonFloatingPane`(*self*, *docks*, *panes*, *target*, *pt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropNonFloatingPane "Permalink to this definition")
Handles the situation in which the dropped pane is not floating.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **target** – the target pane containing the toolbar, an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a mouse position to check for a drop operation.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropPane(self, panes, target, dock_direction, dock_layer, dock_row, dock_pos) -> None:
        """ 

`DoDropPane`(*self*, *panes*, *target*, *dock\_direction*, *dock\_layer*, *dock\_row*, *dock\_pos*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropPane "Permalink to this definition")
Drop a pane in the interface.



Parameters
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") classes;
* **target** – the target pane, an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **dock\_direction** (*integer*) – the docking direction;
* **dock\_layer** (*integer*) – the docking layer;
* **dock\_row** (*integer*) – the docking row;
* **dock\_pos** (*integer*) – the docking position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropRow(self, panes, target, dock_direction, dock_layer, dock_row) -> None:
        """ 

`DoDropRow`(*self*, *panes*, *target*, *dock\_direction*, *dock\_layer*, *dock\_row*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropRow "Permalink to this definition")
Insert a row in the interface before dropping.



Parameters
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") classes;
* **target** – the target pane, an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **dock\_direction** (*integer*) – the docking direction;
* **dock\_layer** (*integer*) – the docking layer;
* **dock\_row** (*integer*) – the docking row.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoDropToolbar(self, docks, panes, target, pt, offset) -> None:
        """ 

`DoDropToolbar`(*self*, *docks*, *panes*, *target*, *pt*, *offset*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoDropToolbar "Permalink to this definition")
Handles the situation in which the dropped pane contains a toolbar.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **target** – the target pane containing the toolbar, an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo");
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a mouse position to check for a drop operation;
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – a possible offset from the input point *pt*.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoEndResizeAction(self, event: MouseEvent) -> None:
        """ 

`DoEndResizeAction`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoEndResizeAction "Permalink to this definition")
Ends a resize action, or for live update, resizes the sash.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoFrameLayout(self) -> None:
        """ 

`DoFrameLayout`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoFrameLayout "Permalink to this definition")
This is an internal function which invokes `wx.Sizer.Layout()`
on the frame’s main sizer, then measures all the various UI items
and updates their internal rectangles.



Note


This should always be called instead of calling
*self.\_managed\_window.Layout()* directly.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoUpdate(self) -> None:
        """ 

`DoUpdate`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoUpdate "Permalink to this definition")
This method is called after any number of changes are made to any of the
managed panes. [`Update`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update") must be invoked after [`AddPane`](#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane")
or [`InsertPane`](#wx.lib.agw.aui.framemanager.AuiManager.InsertPane "wx.lib.agw.aui.framemanager.AuiManager.InsertPane") are called in order to “realize” or “commit” the changes.


In addition, any number of changes may be made to [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") structures
(retrieved with [`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane")), but to realize the changes, [`Update`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update")
must be called. This construction allows pane flicker to be avoided by updating
the whole layout at one time.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DoUpdateEvt(self, evt) -> None:
        """ 

`DoUpdateEvt`(*self*, *evt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DoUpdateEvt "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DrawHintRect(self, pane_window, pt, offset) -> None:
        """ 

`DrawHintRect`(*self*, *pane\_window*, *pt*, *offset*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DrawHintRect "Permalink to this definition")
Calculates the hint rectangle by calling [`CalculateHintRect`](#wx.lib.agw.aui.framemanager.AuiManager.CalculateHintRect "wx.lib.agw.aui.framemanager.AuiManager.CalculateHintRect"). If there is a
rectangle, it shows it by calling [`ShowHint`](#wx.lib.agw.aui.framemanager.AuiManager.ShowHint "wx.lib.agw.aui.framemanager.AuiManager.ShowHint"), otherwise it hides any hint
rectangle currently shown.



Parameters
* **pane\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – it is the window pointer of the pane being dragged;
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – is the mouse position, in client coordinates;
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – describes the offset that the mouse is from the upper-left
corner of the item being dragged.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def DrawPaneButton(self, dc, part, pt) -> None:
        """ 

`DrawPaneButton`(*self*, *dc*, *part*, *pt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.DrawPaneButton "Permalink to this definition")
Draws a pane button in the caption (convenience function).



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object;
* **part** – the UI part to analyze, an instance of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart");
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse location.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def FireEvent(self, evtType, pane, canVeto=False) -> None:
        """ 

`FireEvent`(*self*, *evtType*, *pane*, *canVeto=False*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.FireEvent "Permalink to this definition")
Fires one of the `EVT_AUI_PANE_FLOATED` / `FLOATING` / `DOCKING` / `DOCKED` / `ACTIVATED` event.



Parameters
* **evtType** (*integer*) – one of the aforementioned events;
* **pane** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance associated to this event;
* **canVeto** (*bool*) – whether the event can be vetoed or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAGWFlags(self) -> None:
        """ 

`GetAGWFlags`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAGWFlags "Permalink to this definition")
Returns the current manager’s flags.



See also


[`SetAGWFlags`](#wx.lib.agw.aui.framemanager.AuiManager.SetAGWFlags "wx.lib.agw.aui.framemanager.AuiManager.SetAGWFlags") for a list of possible [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") flags.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAllPanes(self) -> None:
        """ 

`GetAllPanes`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAllPanes "Permalink to this definition")
Returns a reference to all the pane info structures.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAnimationStep(self) -> None:
        """ 

`GetAnimationStep`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAnimationStep "Permalink to this definition")
Returns the animation step speed (a float) to use in [`AnimateDocking`](#wx.lib.agw.aui.framemanager.AuiManager.AnimateDocking "wx.lib.agw.aui.framemanager.AuiManager.AnimateDocking").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetArtProvider(self) -> None:
        """ 

`GetArtProvider`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetArtProvider "Permalink to this definition")
Returns the current art provider being used.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAttributes(self, pane: AuiPaneInfo) -> None:
        """ 

`GetAttributes`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAttributes "Permalink to this definition")
Returns all the attributes of a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").



Parameters
**pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAutoNotebookStyle(self) -> None:
        """ 

`GetAutoNotebookStyle`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAutoNotebookStyle "Permalink to this definition")
Returns the default AGW-specific window style for automatic notebooks.



See also


[`SetAutoNotebookStyle`](#wx.lib.agw.aui.framemanager.AuiManager.SetAutoNotebookStyle "wx.lib.agw.aui.framemanager.AuiManager.SetAutoNotebookStyle") method for a list of possible styles.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetAutoNotebookTabArt(self) -> None:
        """ 

`GetAutoNotebookTabArt`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetAutoNotebookTabArt "Permalink to this definition")
Returns the default tab art provider for automatic notebooks.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetDockPixelOffset(self, test: AuiPaneInfo) -> None:
        """ 

`GetDockPixelOffset`(*self*, *test*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetDockPixelOffset "Permalink to this definition")
This is an internal function which returns a dock’s offset in pixels from
the left side of the window (for horizontal docks) or from the top of the
window (for vertical docks).


This value is necessary for calculating fixed-pane/toolbar offsets
when they are dragged.



Parameters
**test** – a fake [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") for testing purposes.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetDockSizeConstraint(self) -> None:
        """ 

`GetDockSizeConstraint`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetDockSizeConstraint "Permalink to this definition")
Returns the current dock constraint values.



See also


[`SetDockSizeConstraint`](#wx.lib.agw.aui.framemanager.AuiManager.SetDockSizeConstraint "wx.lib.agw.aui.framemanager.AuiManager.SetDockSizeConstraint")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetFrame(self) -> None:
        """ 

`GetFrame`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetFrame "Permalink to this definition")
Returns the window being managed by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Deprecated since version 0.6: This method is now deprecated, use [`GetManagedWindow`](#wx.lib.agw.aui.framemanager.AuiManager.GetManagedWindow "wx.lib.agw.aui.framemanager.AuiManager.GetManagedWindow") instead.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetManagedWindow(self) -> None:
        """ 

`GetManagedWindow`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetManagedWindow "Permalink to this definition")
Returns the window being managed by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetNotebooks(self) -> None:
        """ 

`GetNotebooks`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetNotebooks "Permalink to this definition")
Returns all the automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") in the [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetOppositeDockTotalSize(self, docks, direction) -> None:
        """ 

`GetOppositeDockTotalSize`(*self*, *docks*, *direction*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetOppositeDockTotalSize "Permalink to this definition")
Returns the dimensions of the dock which lives opposite of the input dock.



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structures to analyze;
* **direction** (*integer*) – the direction in which to look for the opposite dock.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPane(self, item: 'Window') -> None:
        """ 

`GetPane`(*self*, *item*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "Permalink to this definition")
Looks up a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") structure based on the supplied window pointer. Upon failure,
[`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane") returns an empty [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo"), a condition which can be checked
by calling [`AuiPaneInfo.IsOk()`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsOk "wx.lib.agw.aui.framemanager.AuiPaneInfo.IsOk").


The pane info’s structure may then be modified. Once a pane’s info is modified, [`Update`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update")
must be called to realize the changes in the UI.



Parameters
**item** – either a pane name or a [`wx.Window`](wx.Window.html#wx.Window "wx.Window").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPaneByName(self, name: str) -> None:
        """ 

`GetPaneByName`(*self*, *name*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPaneByName "Permalink to this definition")
This version of [`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane") looks up a pane based on a ‘pane name’.



Parameters
**name** (*string*) – the pane name.





See also


[`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPaneByWidget(self, window: 'Window') -> None:
        """ 

`GetPaneByWidget`(*self*, *window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPaneByWidget "Permalink to this definition")
This version of [`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane") looks up a pane based on a ‘pane window’.



Parameters
**window** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.





See also


[`GetPane`](#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPanePart(self, wnd: 'Window') -> None:
        """ 

`GetPanePart`(*self*, *wnd*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPanePart "Permalink to this definition")
Looks up the pane border UI part of the
pane specified. This allows the caller to get the exact rectangle
of the pane in question, including decorations like caption and border.



Parameters
**wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window to which the pane border belongs to.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPanePositionsAndSizes(self, dock: AuiDockInfo) -> None:
        """ 

`GetPanePositionsAndSizes`(*self*, *dock*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPanePositionsAndSizes "Permalink to this definition")
Returns all the panes positions and sizes in a dock.



Parameters
**dock** – a [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartnerDock(self, dock: AuiDockInfo) -> None:
        """ 

`GetPartnerDock`(*self*, *dock*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPartnerDock "Permalink to this definition")
Returns the partner dock for the input dock.



Parameters
**dock** – a [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartnerPane(self, dock, pane) -> None:
        """ 

`GetPartnerPane`(*self*, *dock*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPartnerPane "Permalink to this definition")
Returns the partner pane for the input pane. They both need to live
in the same [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo").



Parameters
* **dock** – a [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") instance;
* **pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") class.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetPartSizerRect(self, uiparts: list) -> None:
        """ 

`GetPartSizerRect`(*self*, *uiparts*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetPartSizerRect "Permalink to this definition")
Returns the rectangle surrounding the specified UI parts.



Parameters
**uiparts** (*list*) – list of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart") parts.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetSnapPosition(self) -> None:
        """ 

`GetSnapPosition`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetSnapPosition "Permalink to this definition")
Returns the main frame snapping position.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def GetTotalPixSizeAndProportion(self, dock: AuiDockInfo) -> None:
        """ 

`GetTotalPixSizeAndProportion`(*self*, *dock*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.GetTotalPixSizeAndProportion "Permalink to this definition")
Returns the dimensions and proportion of the input dock.



Parameters
**dock** – the [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structure to analyze.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def HideHint(self) -> None:
        """ 

`HideHint`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.HideHint "Permalink to this definition")
Hides a transparent window hint if there is one.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.HitTest "Permalink to this definition")
This is an internal function which determines
which UI item the specified coordinates are over.



Parameters
* **x** (*integer*) – specifies a x position in client coordinates;
* **y** (*integer*) – specifies a y position in client coordinates.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def InsertPane(self, window, pane_info, insert_level=AUI_INSERT_PANE) -> None:
        """ 

`InsertPane`(*self*, *window*, *pane\_info*, *insert\_level=AUI\_INSERT\_PANE*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.InsertPane "Permalink to this definition")
This method is used to insert either a previously unmanaged pane window
into the frame manager, or to insert a currently managed pane somewhere else.
[`InsertPane`](#wx.lib.agw.aui.framemanager.AuiManager.InsertPane "wx.lib.agw.aui.framemanager.AuiManager.InsertPane") will push all panes, rows, or docks aside and insert the window
into the position specified by *pane\_info*.


Because *pane\_info* can specify either a pane, dock row, or dock layer, the
*insert\_level* parameter is used to disambiguate this. The parameter *insert\_level*
can take a value of `AUI_INSERT_PANE`, `AUI_INSERT_ROW` or `AUI_INSERT_DOCK`.



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window to be inserted and managed;
* **pane\_info** – the insert location for the new window;
* **insert\_level** (*integer*) – the insertion level of the new pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def IsPaneButtonVisible(self, part: AuiDockUIPart) -> None:
        """ 

`IsPaneButtonVisible`(*self*, *part*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.IsPaneButtonVisible "Permalink to this definition")
Returns whether a pane button in the pane caption is visible.



Parameters
**part** – the UI part to analyze, an instance of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAddDock(self, cont, dock, uiparts, spacer_only) -> None:
        """ 

`LayoutAddDock`(*self*, *cont*, *dock*, *uiparts*, *spacer\_only*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.LayoutAddDock "Permalink to this definition")
Adds a dock into the existing layout.



Parameters
* **cont** – a [`wx.Sizer`](wx.Sizer.html#wx.Sizer "wx.Sizer") object;
* **dock** – the [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structure to add to the layout;
* **uiparts** – a list of UI parts in the interface;
* **spacer\_only** (*bool*) – whether to add a simple spacer or a real window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAddPane(self, cont, dock, pane, uiparts, spacer_only) -> None:
        """ 

`LayoutAddPane`(*self*, *cont*, *dock*, *pane*, *uiparts*, *spacer\_only*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.LayoutAddPane "Permalink to this definition")
Adds a pane into the existing layout (in an existing dock).



Parameters
* **cont** – a [`wx.Sizer`](wx.Sizer.html#wx.Sizer "wx.Sizer") object;
* **dock** – the [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") structure in which to add the pane;
* **pane** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance to add to the dock;
* **uiparts** – a list of UI parts in the interface;
* **spacer\_only** (*bool*) – whether to add a simple spacer or a real window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LayoutAll(self, panes, docks, uiparts, spacer_only=False, oncheck=True) -> None:
        """ 

`LayoutAll`(*self*, *panes*, *docks*, *uiparts*, *spacer\_only=False*, *oncheck=True*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.LayoutAll "Permalink to this definition")
Layouts all the UI structures in the interface.



Parameters
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") classes;
* **uiparts** – a list of UI parts in the interface;
* **spacer\_only** (*bool*) – whether to add a simple spacer or a real window;
* **oncheck** (*bool*) – whether to store the results in a class member or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LoadPaneInfo(self, pane_part, pane) -> None:
        """ 

`LoadPaneInfo`(*self*, *pane\_part*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.LoadPaneInfo "Permalink to this definition")
This method is similar to to [`LoadPerspective`](#wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective "wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective"), with the exception that
it only loads information about a single pane. It is used in combination
with [`SavePaneInfo`](#wx.lib.agw.aui.framemanager.AuiManager.SavePaneInfo "wx.lib.agw.aui.framemanager.AuiManager.SavePaneInfo").



Parameters
* **pane\_part** (*string*) – the string to analyze;
* **pane** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") structure in which to load *pane\_part*.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def LoadPerspective(self, layout, update=True, restorecaption=False) -> None:
        """ 

`LoadPerspective`(*self*, *layout*, *update=True*, *restorecaption=False*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective "Permalink to this definition")
Loads a layout which was saved with [`SavePerspective`](#wx.lib.agw.aui.framemanager.AuiManager.SavePerspective "wx.lib.agw.aui.framemanager.AuiManager.SavePerspective").


If the *update* flag parameter is `True`, [`Update`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update") will be
automatically invoked, thus realizing the saved perspective on screen.



Parameters
* **layout** (*string*) – a string which contains a saved AUI layout;
* **update** (*bool*) – whether to update immediately the window or not;
* **restorecaption** (*bool*) – `False`, restore from persist storage,
otherwise use the caption defined in code.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def MaximizePane(self, pane_info, savesizes=True) -> None:
        """ 

`MaximizePane`(*self*, *pane\_info*, *savesizes=True*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.MaximizePane "Permalink to this definition")
Maximizes the input pane.



Parameters
* **pane\_info** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.
* **savesizes** (*bool*) – whether to save previous dock sizes.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def MinimizePane(self, paneInfo, mgrUpdate=True) -> None:
        """ 

`MinimizePane`(*self*, *paneInfo*, *mgrUpdate=True*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.MinimizePane "Permalink to this definition")
Minimizes a pane in a newly and automatically created [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").


Clicking on the minimize button causes a new [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") to be created
and added to the frame manager (currently the implementation is such that
panes at West will have a toolbar at the right, panes at South will have
toolbars at the bottom etc…) and the pane is hidden in the manager.


Clicking on the restore button on the newly created toolbar will result in the
toolbar being removed and the original pane being restored.



Parameters
* **paneInfo** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance for the pane to be minimized;
* **mgrUpdate** (*bool*) – `True` to call [`Update`](#wx.lib.agw.aui.framemanager.AuiManager.Update "wx.lib.agw.aui.framemanager.AuiManager.Update") to realize the new layout,
`False` otherwise.





Note


The *mgrUpdate* parameter is currently only used while loading perspectives using
[`LoadPerspective`](#wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective "wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective"), as minimized panes were not correctly taken into account before.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnCaptionDoubleClicked(self, pane_window: 'Window') -> None:
        """ 

`OnCaptionDoubleClicked`(*self*, *pane\_window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnCaptionDoubleClicked "Permalink to this definition")
Handles the mouse double click on the pane caption.



Parameters
**pane\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnCaptureLost(self, event: MouseCaptureLostEvent) -> None:
        """ 

`OnCaptureLost`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnCaptureLost "Permalink to this definition")
Handles the `wx.EVT_MOUSE_CAPTURE_LOST` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseCaptureLostEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnChildFocus(self, event: ChildFocusEvent) -> None:
        """ 

`OnChildFocus`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnChildFocus "Permalink to this definition")
Handles the `wx.EVT_CHILD_FOCUS` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `ChildFocusEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnClose(self, event) -> None:
        """ 

`OnClose`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnClose "Permalink to this definition")
Called when the managed window is closed. Makes sure that [`UnInit`](#wx.lib.agw.aui.framemanager.AuiManager.UnInit "wx.lib.agw.aui.framemanager.AuiManager.UnInit")
is called.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnDestroy(self, event) -> None:
        """ 

`OnDestroy`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnDestroy "Permalink to this definition")
Called when the managed window is destroyed. Makes sure that [`UnInit`](#wx.lib.agw.aui.framemanager.AuiManager.UnInit "wx.lib.agw.aui.framemanager.AuiManager.UnInit")
is called.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – `EraseEvent` to be processed.





Note


This is intentionally empty (excluding wxMAC) to reduce
flickering while drawing.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFindManager(self, event: AuiManagerEvent) -> None:
        """ 

`OnFindManager`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnFindManager "Permalink to this definition")
Handles the `EVT_AUI_FIND_MANAGER` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneActivated(self, wnd: 'Window') -> None:
        """ 

`OnFloatingPaneActivated`(*self*, *wnd*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnFloatingPaneActivated "Permalink to this definition")
Handles the activation event of a floating pane.



Parameters
**wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneClosed(self, wnd, event) -> None:
        """ 

`OnFloatingPaneClosed`(*self*, *wnd*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnFloatingPaneClosed "Permalink to this definition")
Handles the close event of a floating pane.



Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane;
* **event** – a `CloseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneMoved(self, wnd, eventOrPt) -> None:
        """ 

`OnFloatingPaneMoved`(*self*, *wnd*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnFloatingPaneMoved "Permalink to this definition")
Handles the move event of a floating pane.



Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane;
* **eventOrPt** – a `MoveEvent` to be processed or an instance of [`wx.Point`](wx.Point.html#wx.Point "wx.Point").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnFloatingPaneResized(self, wnd, size) -> None:
        """ 

`OnFloatingPaneResized`(*self*, *wnd*, *size*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnFloatingPaneResized "Permalink to this definition")
Handles the resizing of a floating pane.



Parameters
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane;
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the new pane floating size.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnGripperClicked(self, pane_window, start, offset) -> None:
        """ 

`OnGripperClicked`(*self*, *pane\_window*, *start*, *offset*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnGripperClicked "Permalink to this definition")
Handles the mouse click on the pane gripper.



Parameters
* **pane\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane;
* **start** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse-click position;
* **offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – an offset point from the *start* position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnHintFadeTimer(self, event: TimerEvent) -> None:
        """ 

`OnHintFadeTimer`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnHintFadeTimer "Permalink to this definition")
Handles the `wx.EVT_TIMER` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `TimerEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeaveWindow(self, event: MouseEvent) -> None:
        """ 

`OnLeaveWindow`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeaveWindow "Permalink to this definition")
Handles the `wx.EVT_LEAVE_WINDOW` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftDClick(self, event: MouseEvent) -> None:
        """ 

`OnLeftDClick`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftDClick "Permalink to this definition")
Handles the `wx.EVT_LEFT_DCLICK` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftDown(self, event: MouseEvent) -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftDown "Permalink to this definition")
Handles the `wx.EVT_LEFT_DOWN` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "Permalink to this definition")
Handles the `wx.EVT_LEFT_UP` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_ClickButton(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp_ClickButton`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_ClickButton "Permalink to this definition")
Sub-handler for the [`OnLeftUp`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragFloatingPane(self, eventOrPt) -> None:
        """ 

`OnLeftUp_DragFloatingPane`(*self*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_DragFloatingPane "Permalink to this definition")
Sub-handler for the [`OnLeftUp`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragMovablePane(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp_DragMovablePane`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_DragMovablePane "Permalink to this definition")
Sub-handler for the [`OnLeftUp`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_DragToolbarPane(self, eventOrPt) -> None:
        """ 

`OnLeftUp_DragToolbarPane`(*self*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_DragToolbarPane "Permalink to this definition")
Sub-handler for the [`OnLeftUp`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnLeftUp_Resize(self, event: MouseEvent) -> None:
        """ 

`OnLeftUp_Resize`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_Resize "Permalink to this definition")
Sub-handler for the [`OnLeftUp`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion(self, event: MouseEvent) -> None:
        """ 

`OnMotion`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "Permalink to this definition")
Handles the `wx.EVT_MOTION` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_ClickCaption(self, event: MouseEvent) -> None:
        """ 

`OnMotion_ClickCaption`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_ClickCaption "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragFloatingPane(self, eventOrPt) -> None:
        """ 

`OnMotion_DragFloatingPane`(*self*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_DragFloatingPane "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragMovablePane(self, eventOrPt) -> None:
        """ 

`OnMotion_DragMovablePane`(*self*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_DragMovablePane "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_DragToolbarPane(self, eventOrPt) -> None:
        """ 

`OnMotion_DragToolbarPane`(*self*, *eventOrPt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_DragToolbarPane "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_Other(self, event: MouseEvent) -> None:
        """ 

`OnMotion_Other`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_Other "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMotion_Resize(self, event: MouseEvent) -> None:
        """ 

`OnMotion_Resize`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion_Resize "Permalink to this definition")
Sub-handler for the [`OnMotion`](#wx.lib.agw.aui.framemanager.AuiManager.OnMotion "wx.lib.agw.aui.framemanager.AuiManager.OnMotion") event.



Parameters
**event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnMove(self, event: MoveEvent) -> None:
        """ 

`OnMove`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnMove "Permalink to this definition")
Handles the `wx.EVT_MOVE` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `MoveEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – an instance of `PaintEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaneButton(self, event: AuiManagerEvent) -> None:
        """ 

`OnPaneButton`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnPaneButton "Permalink to this definition")
Handles the `EVT_AUI_PANE_BUTTON` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnPaneDocked(self, event: AuiManagerEvent) -> None:
        """ 

`OnPaneDocked`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnPaneDocked "Permalink to this definition")
Handles the `EVT_AUI_PANE_DOCKED` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – an instance of [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnRender(self, event: AuiManagerEvent) -> None:
        """ 

`OnRender`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnRender "Permalink to this definition")
Draws all of the pane captions, sashes, backgrounds, captions, grippers, pane borders and buttons.
It renders the entire user interface. It binds the `EVT_AUI_RENDER` event.



Parameters
**event** – an instance of [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnRestoreMinimizedPane(self, event: AuiManagerEvent) -> None:
        """ 

`OnRestoreMinimizedPane`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnRestoreMinimizedPane "Permalink to this definition")
Handles the `EVT_AUI_PANE_MIN_RESTORE` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – an instance of [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSetCursor(self, event: SetCursorEvent) -> None:
        """ 

`OnSetCursor`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnSetCursor "Permalink to this definition")
Handles the `wx.EVT_SET_CURSOR` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `SetCursorEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnSysColourChanged(self, event: SysColourChangedEvent) -> None:
        """ 

`OnSysColourChanged`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnSysColourChanged "Permalink to this definition")
Handles the `wx.EVT_SYS_COLOUR_CHANGED` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `SysColourChangedEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabBeginDrag(self, event: Any) -> None:
        """ 

`OnTabBeginDrag`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnTabBeginDrag "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_BEGIN_DRAG` event.



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabEndDrag(self, event: Any) -> None:
        """ 

`OnTabEndDrag`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnTabEndDrag "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_END_DRAG` event.



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabPageClose(self, event: Any) -> None:
        """ 

`OnTabPageClose`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnTabPageClose "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_PAGE_CLOSE` event.



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def OnTabSelected(self, event: Any) -> None:
        """ 

`OnTabSelected`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.OnTabSelected "Permalink to this definition")
Handles the `EVT_AUINOTEBOOK_PAGE_CHANGED` event.



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def PaneFromTabEvent(self, event: Any) -> None:
        """ 

`PaneFromTabEvent`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.PaneFromTabEvent "Permalink to this definition")
Returns a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") from a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") event.



Parameters
**event** – a [`AuiNotebookEvent`](wx.lib.agw.aui.auibook.AuiNotebookEvent.html#wx.lib.agw.aui.auibook.AuiNotebookEvent "wx.lib.agw.aui.auibook.AuiNotebookEvent") event.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def PaneHitTest(self, panes, pt) -> None:
        """ 

`PaneHitTest`(*self*, *panes*, *pt*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.PaneHitTest "Permalink to this definition")
Similar to [`HitTest`](#wx.lib.agw.aui.framemanager.AuiManager.HitTest "wx.lib.agw.aui.framemanager.AuiManager.HitTest"), but it checks in which [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") rectangle the
input point belongs to.



Parameters
* **panes** – a list of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instances;
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ProcessDockResult(self, target, new_pos) -> None:
        """ 

`ProcessDockResult`(*self*, *target*, *new\_pos*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ProcessDockResult "Permalink to this definition")
This is a utility function used by [`DoDrop`](#wx.lib.agw.aui.framemanager.AuiManager.DoDrop "wx.lib.agw.aui.framemanager.AuiManager.DoDrop") - it checks
if a dock operation is allowed, the new dock position is copied into
the target info. If the operation was allowed, the function returns `True`.



Parameters
* **target** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance to be docked;
* **new\_pos** (*integer*) – the new docking position if the docking operation is allowed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ProcessMgrEvent(self, event: AuiManagerEvent) -> None:
        """ 

`ProcessMgrEvent`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ProcessMgrEvent "Permalink to this definition")
Process the AUI events sent to the manager.



Parameters
**event** – the event to process, an instance of [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RefreshButton(self, part: AuiDockUIPart) -> None:
        """ 

`RefreshButton`(*self*, *part*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RefreshButton "Permalink to this definition")
Refreshes a pane button in the caption.



Parameters
**part** – the UI part to analyze, an instance of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RefreshCaptions(self) -> None:
        """ 

`RefreshCaptions`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RefreshCaptions "Permalink to this definition")
Refreshes all pane captions.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RemoveAutoNBCaption(self, pane: AuiPaneInfo) -> None:
        """ 

`RemoveAutoNBCaption`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RemoveAutoNBCaption "Permalink to this definition")
Removes the caption on newly created automatic notebooks.



Parameters
**pane** – an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") (the target notebook).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Render(self, dc: 'DC') -> None:
        """ 

`Render`(*self*, *dc*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.Render "Permalink to this definition")
Fires a render event, which is normally handled by [`OnRender`](#wx.lib.agw.aui.framemanager.AuiManager.OnRender "wx.lib.agw.aui.framemanager.AuiManager.OnRender"). This allows the
render function to be overridden via the render event.


This can be useful for painting custom graphics in the main window.
Default behavior can be invoked in the overridden function by calling
[`OnRender`](#wx.lib.agw.aui.framemanager.AuiManager.OnRender "wx.lib.agw.aui.framemanager.AuiManager.OnRender").



Parameters
**dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Repaint(self, dc: Optional[None]=None) -> None:
        """ 

`Repaint`(*self*, *dc=None*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.Repaint "Permalink to this definition")
Repaints the entire frame decorations (sashes, borders, buttons and so on).
It renders the entire user interface.



Parameters
**dc** – if not `None`, an instance of `PaintDC`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RepositionPane(self, pane, wnd_pos, wnd_size) -> None:
        """ 

`RepositionPane`(*self*, *pane*, *wnd\_pos*, *wnd\_size*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RepositionPane "Permalink to this definition")
Repositions a pane after the main frame has been moved/resized.



Parameters
* **pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance;
* **wnd\_pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the main frame position;
* **wnd\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the main frame size.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RequestUserAttention(self, pane_window: 'Window') -> None:
        """ 

`RequestUserAttention`(*self*, *pane\_window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RequestUserAttention "Permalink to this definition")
Requests the user attention by intermittently highlighting the pane caption.



Parameters
**pane\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – the window managed by the pane;






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestoreMaximizedPane(self) -> None:
        """ 

`RestoreMaximizedPane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RestoreMaximizedPane "Permalink to this definition")
Restores the current maximized pane (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestoreMinimizedPane(self, paneInfo: AuiPaneInfo) -> None:
        """ 

`RestoreMinimizedPane`(*self*, *paneInfo*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RestoreMinimizedPane "Permalink to this definition")
Restores a previously minimized pane.



Parameters
**paneInfo** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance for the pane to be restored.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestorePane(self, pane_info: AuiPaneInfo) -> None:
        """ 

`RestorePane`(*self*, *pane\_info*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RestorePane "Permalink to this definition")
Restores the input pane from a previous maximized or minimized state.



Parameters
**pane\_info** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def RestrictResize(self, clientPt, screenPt, createDC) -> None:
        """ 

`RestrictResize`(*self*, *clientPt*, *screenPt*, *createDC*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.RestrictResize "Permalink to this definition")
Common method between [`DoEndResizeAction`](#wx.lib.agw.aui.framemanager.AuiManager.DoEndResizeAction "wx.lib.agw.aui.framemanager.AuiManager.DoEndResizeAction") and [`OnLeftUp_Resize`](#wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_Resize "wx.lib.agw.aui.framemanager.AuiManager.OnLeftUp_Resize").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePaneInfo(self, pane: AuiPaneInfo) -> None:
        """ 

`SavePaneInfo`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SavePaneInfo "Permalink to this definition")
This method is similar to [`SavePerspective`](#wx.lib.agw.aui.framemanager.AuiManager.SavePerspective "wx.lib.agw.aui.framemanager.AuiManager.SavePerspective"), with the exception
that it only saves information about a single pane. It is used in
combination with [`LoadPaneInfo`](#wx.lib.agw.aui.framemanager.AuiManager.LoadPaneInfo "wx.lib.agw.aui.framemanager.AuiManager.LoadPaneInfo").



Parameters
**pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance to save.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePerspective(self) -> None:
        """ 

`SavePerspective`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SavePerspective "Permalink to this definition")
Saves the entire user interface layout into an encoded string, which can then
be stored by the application (probably using `Config`).


When a perspective is restored using [`LoadPerspective`](#wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective "wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective"), the entire user
interface will return to the state it was when the perspective was saved.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SavePreviousDockSizes(self, pane_info: AuiPaneInfo) -> None:
        """ 

`SavePreviousDockSizes`(*self*, *pane\_info*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SavePreviousDockSizes "Permalink to this definition")
Stores the previous dock sizes, to be used in a “restore” action later.



Parameters
**pane\_info** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAGWFlags(self, agwFlags: int) -> None:
        """ 

`SetAGWFlags`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetAGWFlags "Permalink to this definition")
This method is used to specify [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") ‘s settings flags.



Parameters
**agwFlags** (*integer*) – specifies options which allow the frame management behavior
to be modified. *agwFlags* can be one of the following style bits:







| Flag name | Description |
| --- | --- |
| `AUI_MGR_ALLOW_FLOATING` | Allow floating of panes |
| `AUI_MGR_ALLOW_ACTIVE_PANE` | If a pane becomes active, “highlight” it in the interface |
| `AUI_MGR_TRANSPARENT_DRAG` | If the platform supports it, set transparency on a floating pane while it is dragged by the user |
| `AUI_MGR_TRANSPARENT_HINT` | If the platform supports it, show a transparent hint window when the user is about to dock a floating pane |
| `AUI_MGR_VENETIAN_BLINDS_HINT` | Show a “venetian blind” effect when the user is about to dock a floating pane |
| `AUI_MGR_RECTANGLE_HINT` | Show a rectangle hint effect when the user is about to dock a floating pane |
| `AUI_MGR_HINT_FADE` | If the platform supports it, the hint window will fade in and out |
| `AUI_MGR_NO_VENETIAN_BLINDS_FADE` | Disables the “venetian blind” fade in and out |
| `AUI_MGR_LIVE_RESIZE` | Live resize when the user drag a sash |
| `AUI_MGR_ANIMATE_FRAMES` | Fade-out floating panes when they are closed (all platforms which support frames transparency) and show a moving rectangle when they are docked (Windows < Vista and GTK only) |
| `AUI_MGR_AERO_DOCKING_GUIDES` | Use the new Aero-style bitmaps as docking guides |
| `AUI_MGR_PREVIEW_MINIMIZED_PANES` | Slide in and out minimized panes to preview them |
| `AUI_MGR_WHIDBEY_DOCKING_GUIDES` | Use the new Whidbey-style bitmaps as docking guides |
| `AUI_MGR_SMOOTH_DOCKING` | Performs a “smooth” docking of panes (a la PyQT) |
| `AUI_MGR_USE_NATIVE_MINIFRAMES` | Use miniframes with native caption bar as floating panes instead or custom drawn caption bars (forced on wxMAC) |
| `AUI_MGR_AUTONB_NO_CAPTION` | Panes that merge into an automatic notebook will not have the pane caption visible |



Note


If using the `AUI_MGR_USE_NATIVE_MINIFRAMES`, double-clicking on a
floating pane caption will not re-dock the pane, but simply maximize it (if
[`AuiPaneInfo.MaximizeButton`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaximizeButton "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaximizeButton") has been set to `True`) or do nothing.










            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAnimationStep(self, step: float) -> None:
        """ 

`SetAnimationStep`(*self*, *step*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetAnimationStep "Permalink to this definition")
Sets the animation step speed (a float) to use in [`AnimateDocking`](#wx.lib.agw.aui.framemanager.AuiManager.AnimateDocking "wx.lib.agw.aui.framemanager.AuiManager.AnimateDocking").



Parameters
**step** (*float*) – the animation speed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetArtProvider(self, art_provider: Any) -> None:
        """ 

`SetArtProvider`(*self*, *art\_provider*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetArtProvider "Permalink to this definition")
Instructs [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to use art provider specified by the parameter
*art\_provider* for all drawing calls. This allows pluggable look-and-feel
features.



Parameters
**art\_provider** – a AUI dock art provider.





Note


The previous art provider object, if any, will be deleted by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAttributes(self, pane, attrs) -> None:
        """ 

`SetAttributes`(*self*, *pane*, *attrs*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetAttributes "Permalink to this definition")
Sets all the attributes contained in *attrs* to a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").



Parameters
* **pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance;
* **attrs** (*list*) – a list of attributes.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAutoNotebookStyle(self, agwStyle: int) -> None:
        """ 

`SetAutoNotebookStyle`(*self*, *agwStyle*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetAutoNotebookStyle "Permalink to this definition")
Sets the default AGW-specific window style for automatic notebooks.



Parameters
**agwStyle** (*integer*) – the underlying [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") window style.
This can be a combination of the following bits:







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
| `AUI_NB_SUB_NOTEBOOK` | This style is used by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to create automatic AuiNotebooks |
| `AUI_NB_HIDE_ON_SINGLE_TAB` | Hides the tab window if only one tab is present |
| `AUI_NB_SMART_TABS` | Use Smart Tabbing, like `Alt` + `Tab` on Windows |
| `AUI_NB_USE_IMAGES_DROPDOWN` | Uses images on dropdown window list menu instead of check items |
| `AUI_NB_CLOSE_ON_TAB_LEFT` | Draws the tab close button on the left instead of on the right (a la Camino browser) |
| `AUI_NB_TAB_FLOAT` | Allows the floating of single tabs. Known limitation: when the notebook is more or less full screen, tabs cannot be dragged far enough outside of the notebook to become floating pages |
| `AUI_NB_DRAW_DND_TAB` | Draws an image representation of a tab while dragging (on by default) |
| `AUI_NB_ORDER_BY_ACCESS` | Tab navigation order by last access time for the tabs |
| `AUI_NB_NO_TAB_FOCUS` | Don’t draw tab focus rectangle |









            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetAutoNotebookTabArt(self, art: Any) -> None:
        """ 

`SetAutoNotebookTabArt`(*self*, *art*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetAutoNotebookTabArt "Permalink to this definition")
Sets the default tab art provider for automatic notebooks.



Parameters
**art** – a tab art provider.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetDockSizeConstraint(self, width_pct, height_pct) -> None:
        """ 

`SetDockSizeConstraint`(*self*, *width\_pct*, *height\_pct*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetDockSizeConstraint "Permalink to this definition")
When a user creates a new dock by dragging a window into a docked position,
often times the large size of the window will create a dock that is unwieldy
large.


[`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") by default limits the size of any new dock to 1/3 of the window
size. For horizontal docks, this would be 1/3 of the window height. For vertical
docks, 1/3 of the width. Calling this function will adjust this constraint value.


The numbers must be between 0.0 and 1.0. For instance, calling [`SetDockSizeConstraint`](#wx.lib.agw.aui.framemanager.AuiManager.SetDockSizeConstraint "wx.lib.agw.aui.framemanager.AuiManager.SetDockSizeConstraint")
with (0.5, 0.5) will cause new docks to be limited to half of the size of the entire
managed window.



Parameters
* **width\_pct** (*float*) – a number representing the *x* dock size constraint;
* **width\_pct** – a number representing the *y* dock size constraint.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetFrame(self, managed_window: 'Window') -> None:
        """ 

`SetFrame`(*self*, *managed\_window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetFrame "Permalink to this definition")
Called to specify the frame or window which is to be managed by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").
Frame management is not restricted to just frames. Child windows or custom
controls are also allowed.



Parameters
**managed\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – specifies the window which should be managed by
the AUI manager.





Deprecated since version 0.6: This method is now deprecated, use [`SetManagedWindow`](#wx.lib.agw.aui.framemanager.AuiManager.SetManagedWindow "wx.lib.agw.aui.framemanager.AuiManager.SetManagedWindow") instead.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetManagedWindow(self, managed_window: 'Window') -> None:
        """ 

`SetManagedWindow`(*self*, *managed\_window*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetManagedWindow "Permalink to this definition")
Called to specify the frame or window which is to be managed by [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").
Frame management is not restricted to just frames. Child windows or custom
controls are also allowed.



Parameters
**managed\_window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – specifies the window which should be managed by
the AUI manager.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetMasterManager(self, manager: AuiManager) -> None:
        """ 

`SetMasterManager`(*self*, *manager*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetMasterManager "Permalink to this definition")
Sets the master manager for an automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**manager** – an instance of [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SetSnapLimits(self, x, y) -> None:
        """ 

`SetSnapLimits`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SetSnapLimits "Permalink to this definition")
Modifies the snap limits used when snapping the *managed\_window* to the screen
(using [`SnapToScreen`](#wx.lib.agw.aui.framemanager.AuiManager.SnapToScreen "wx.lib.agw.aui.framemanager.AuiManager.SnapToScreen")) or when snapping the floating panes to one side of the
*managed\_window* (using [`SnapPane`](#wx.lib.agw.aui.framemanager.AuiManager.SnapPane "wx.lib.agw.aui.framemanager.AuiManager.SnapPane")).


To change the limit after which the *managed\_window* or the floating panes are
automatically stickled to the screen border (or to the *managed\_window* side),
set these two variables. Default values are 15 pixels.



Parameters
* **x** (*integer*) – the minimum horizontal distance below which the snap occurs;
* **y** (*integer*) – the minimum vertical distance below which the snap occurs.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ShowHint(self, rect: 'Rect') -> None:
        """ 

`ShowHint`(*self*, *rect*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ShowHint "Permalink to this definition")
Shows the AUI hint window.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the hint rect calculated in advance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def ShowPane(self, window, show) -> None:
        """ 

`ShowPane`(*self*, *window*, *show*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.ShowPane "Permalink to this definition")
Shows or hides a pane based on the window passed as input.



Parameters
* **window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – any subclass or derivation of [`wx.Window`](wx.Window.html#wx.Window "wx.Window");
* **show** (*bool*) – `True` to show the pane, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SlideIn(self, event: TimerEvent) -> None:
        """ 

`SlideIn`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SlideIn "Permalink to this definition")
Handles the `wx.EVT_TIMER` event for [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").



Parameters
**event** – a `TimerEvent` to be processed.





Note


This is used solely for sliding in and out minimized panes.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SlideOut(self) -> None:
        """ 

`SlideOut`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SlideOut "Permalink to this definition")
Slides out a preview of a minimized pane.



Note


This is used solely for sliding in and out minimized panes.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SmartShrink(self, docks, direction) -> None:
        """ 

`SmartShrink`(*self*, *docks*, *direction*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SmartShrink "Permalink to this definition")
Used to intelligently shrink the docks’ size (if needed).



Parameters
* **docks** – a list of [`AuiDockInfo`](wx.lib.agw.aui.framemanager.AuiDockInfo.html#wx.lib.agw.aui.framemanager.AuiDockInfo "wx.lib.agw.aui.framemanager.AuiDockInfo") instances;
* **direction** (*integer*) – the direction in which to shrink.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SmoothDock(self, paneInfo: AuiPaneInfo) -> None:
        """ 

`SmoothDock`(*self*, *paneInfo*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SmoothDock "Permalink to this definition")
This method implements a smooth docking effect for floating panes, similar to
what the PyQT library does with its floating windows.



Parameters
**paneInfo** – an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").





Note


The smooth docking effect can only be used if you set the `AUI_MGR_SMOOTH_DOCKING`
style to [`AuiManager`](#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Snap(self) -> None:
        """ 

`Snap`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.Snap "Permalink to this definition")
Snaps the main frame to specified position on the screen.



See also


[`SnapToScreen`](#wx.lib.agw.aui.framemanager.AuiManager.SnapToScreen "wx.lib.agw.aui.framemanager.AuiManager.SnapToScreen")





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SnapPane(self, pane, pane_pos, pane_size, toSnap=False) -> None:
        """ 

`SnapPane`(*self*, *pane*, *pane\_pos*, *pane\_size*, *toSnap=False*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SnapPane "Permalink to this definition")
Snaps a floating pane to one of the main frame sides.



Parameters
* **pane** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance;
* **pane\_pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the new pane floating position;
* **pane\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the new pane floating size;
* **toSnap** (*bool*) – a bool variable to check if [`SnapPane`](#wx.lib.agw.aui.framemanager.AuiManager.SnapPane "wx.lib.agw.aui.framemanager.AuiManager.SnapPane") was called from
a move event.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SnapToScreen(self, snap=True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP) -> None:
        """ 

`SnapToScreen`(*self*, *snap=True*, *monitor=0*, *hAlign=wx.RIGHT*, *vAlign=wx.TOP*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SnapToScreen "Permalink to this definition")
Snaps the main frame to specified position on the screen.



Parameters
* **snap** (*bool*) – whether to snap the main frame or not;
* **monitor** (*integer*) – the monitor display in which snapping the window;
* **hAlign** (*integer*) – the horizontal alignment of the snapping position;
* **vAlign** (*integer*) – the vertical alignment of the snapping position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def StartPreviewTimer(self, toolbar: Any) -> None:
        """ 

`StartPreviewTimer`(*self*, *toolbar*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.StartPreviewTimer "Permalink to this definition")
Starts a timer for sliding in and out a minimized pane.



Parameters
**toolbar** – the [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") containing the minimized pane tool.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def StopPreviewTimer(self) -> None:
        """ 

`StopPreviewTimer`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.StopPreviewTimer "Permalink to this definition")
Stops a timer for sliding in and out a minimized pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def SwitchToolBarOrientation(self, pane: AuiPaneInfo) -> None:
        """ 

`SwitchToolBarOrientation`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.SwitchToolBarOrientation "Permalink to this definition")
Switches the toolbar orientation from vertical to horizontal and vice-versa.
This is especially useful for vertical docked toolbars once they float.



Parameters
**pane** – an instance of [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo"), which may have a [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar")
window associated with it.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UnInit(self) -> None:
        """ 

`UnInit`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.UnInit "Permalink to this definition")
Uninitializes the framework and should be called before a managed frame or
window is destroyed. [`UnInit`](#wx.lib.agw.aui.framemanager.AuiManager.UnInit "wx.lib.agw.aui.framemanager.AuiManager.UnInit") is usually called in the managed [`wx.Frame`](wx.Frame.html#wx.Frame "wx.Frame") / [`wx.Window`](wx.Window.html#wx.Window "wx.Window")
destructor.


It is necessary to call this function before the managed frame or window is
destroyed, otherwise the manager cannot remove its custom event handlers
from a window.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def Update(self) -> None:
        """ 

`Update`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.Update "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateButtonOnScreen(self, button_ui_part, event) -> None:
        """ 

`UpdateButtonOnScreen`(*self*, *button\_ui\_part*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.UpdateButtonOnScreen "Permalink to this definition")
Updates/redraws the UI part containing a pane button.



Parameters
* **button\_ui\_part** – the UI part the button belongs to, an instance of [`AuiDockUIPart`](wx.lib.agw.aui.framemanager.AuiDockUIPart.html#wx.lib.agw.aui.framemanager.AuiDockUIPart "wx.lib.agw.aui.framemanager.AuiDockUIPart").;
* **event** – a `MouseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateDockingGuides(self, paneInfo: AuiPaneInfo) -> None:
        """ 

`UpdateDockingGuides`(*self*, *paneInfo*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.UpdateDockingGuides "Permalink to this definition")
Updates the docking guide windows positions and appearance.



Parameters
**paneInfo** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """

    def UpdateNotebook(self) -> None:
        """ 

`UpdateNotebook`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager.UpdateNotebook "Permalink to this definition")
Updates the automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") in the layout (if any exists).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager.html
        """



EVT_MOUSE_CAPTURE_LOST: int

EVT_CHILD_FOCUS: int

EVT_ERASE_BACKGROUND: int

EVT_TIMER: int

EVT_LEAVE_WINDOW: int

EVT_LEFT_DCLICK: int

EVT_LEFT_DOWN: int

EVT_LEFT_UP: int

EVT_MOTION: int

EVT_MOVE: int

EVT_PAINT: int

EVT_SET_CURSOR: int

EVT_SIZE: int

EVT_SYS_COLOUR_CHANGED: int

class AuiPaneInfo:
    """ AuiPaneInfo specifies all the parameters for a pane. These parameters specify where
the pane is on the screen, whether it is docked or floating, or hidden. In addition,
these parameters specify the pane’s docked position, floating position, preferred
size, minimum size, caption text among many other parameters.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.__init__ "Permalink to this definition")
Default class constructor.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize(self, arg1=None, arg2=None) -> None:
        """ 

`BestSize`(*self*, *arg1=None*, *arg2=None*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize "Permalink to this definition")
Sets the ideal size for the pane. The docking manager will attempt to use
this size as much as possible when docking or floating the pane.


This method is split in 2 versions depending on the input type. If *arg1* is
a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, then [`BestSize1`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize1 "wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize1") is called. Otherwise, [`BestSize2`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize2 "wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize2") is called.



Parameters
* **arg1** – a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, a (x, y) tuple or a *x* coordinate.
* **arg2** – a *y* coordinate (only if *arg1* is a *x* coordinate, otherwise unused).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize1(self, size) -> None:
        """ 

`BestSize1`(*self*, *size*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize1 "Permalink to this definition")
Sets the best size of the pane.



See also


[`BestSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BestSize2(self, x, y) -> None:
        """ 

`BestSize2`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize2 "Permalink to this definition")
Sets the best size of the pane.



See also


[`BestSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.BestSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Bottom(self) -> None:
        """ 

`Bottom`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Bottom "Permalink to this definition")
Sets the pane dock position to the bottom of the frame.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_BOTTOM` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BottomDockable(self, b: bool=True) -> None:
        """ 

`BottomDockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomDockable "Permalink to this definition")
Indicates whether a pane can be docked at the bottom of the frame.



Parameters
**b** (*bool*) – whether the pane can be docked at the bottom or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def BottomSnappable(self, b: bool=True) -> None:
        """ 

`BottomSnappable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomSnappable "Permalink to this definition")
Indicates whether a pane can be snapped at the bottom of the main frame.



Parameters
**b** (*bool*) – whether the pane can be snapped at the bottom of the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Caption(self, caption: str) -> None:
        """ 

`Caption`(*self*, *caption*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Caption "Permalink to this definition")
Sets the caption of the pane.



Parameters
**caption** (*string*) – a string specifying the pane caption.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CaptionVisible(self, visible=True, left=False) -> None:
        """ 

`CaptionVisible`(*self*, *visible=True*, *left=False*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.CaptionVisible "Permalink to this definition")
Indicates that a pane caption should be visible. If *visible* is `False`, no pane
caption is drawn.



Parameters
* **visible** (*bool*) – whether the caption should be visible or not;
* **left** (*bool*) – whether the caption should be drawn on the left (rotated by 90 degrees) or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Center(self) -> None:
        """ 

`Center`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Center "Permalink to this definition")
Sets the pane to the center position of the frame.


The centre pane is the space in the middle after all border panes (left, top,
right, bottom) are subtracted from the layout.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_CENTER` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CenterPane(self) -> None:
        """ 

`CenterPane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.CenterPane "Permalink to this definition")
Specifies that the pane should adopt the default center pane settings.


Centre panes usually do not have caption bars. This function provides an easy way of
preparing a pane to be displayed in the center dock position.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Centre(self) -> None:
        """ 

`Centre`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Centre "Permalink to this definition")
Sets the pane to the center position of the frame.


The centre pane is the space in the middle after all border panes (left, top,
right, bottom) are subtracted from the layout.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_CENTRE` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CentrePane(self) -> None:
        """ 

`CentrePane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.CentrePane "Permalink to this definition")
Specifies that the pane should adopt the default center pane settings.


Centre panes usually do not have caption bars. This function provides an easy way of
preparing a pane to be displayed in the center dock position.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CloseButton(self, visible: bool=True) -> None:
        """ 

`CloseButton`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.CloseButton "Permalink to this definition")
Indicates that a close button should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the close button should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def CountButtons(self) -> None:
        """ 

`CountButtons`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.CountButtons "Permalink to this definition")
Returns the number of visible buttons in the docked pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DefaultPane(self) -> None:
        """ 

`DefaultPane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.DefaultPane "Permalink to this definition")
Specifies that the pane should adopt the default pane settings.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DestroyOnClose(self, b: bool=True) -> None:
        """ 

`DestroyOnClose`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.DestroyOnClose "Permalink to this definition")
Indicates whether a pane should be destroyed when it is closed.


Normally a pane is simply hidden when the close button is clicked. Setting
*b* to `True` will cause the window to be destroyed when the user clicks
the pane’s close button.



Parameters
**b** (*bool*) – whether the pane should be destroyed when it is closed or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Direction(self, direction: int) -> None:
        """ 

`Direction`(*self*, *direction*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "Permalink to this definition")
Determines the direction of the docked pane. It is functionally the
same as calling [`Left`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Left "wx.lib.agw.aui.framemanager.AuiPaneInfo.Left"), [`Right`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Right "wx.lib.agw.aui.framemanager.AuiPaneInfo.Right"), [`Top`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Top "wx.lib.agw.aui.framemanager.AuiPaneInfo.Top") or [`Bottom`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Bottom "wx.lib.agw.aui.framemanager.AuiPaneInfo.Bottom"),
except that docking direction may be specified programmatically via the parameter *direction*.



Parameters
**direction** (*integer*) – the direction of the docked pane.





See also


[`dock_direction_set`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set") for a list of valid docking directions.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Dock(self) -> None:
        """ 

`Dock`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Dock "Permalink to this definition")
Indicates that a pane should be docked. It is the opposite of [`Float`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Float "wx.lib.agw.aui.framemanager.AuiPaneInfo.Float").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def dock_direction_get(self) -> None:
        """ 

`dock_direction_get`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_get "Permalink to this definition")
Getter for the [`dock_direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction").



See also


[`dock_direction_set`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set") for a set of valid docking directions.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def dock_direction_set(self, value: int) -> None:
        """ 

`dock_direction_set`(*self*, *value*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set "Permalink to this definition")
Setter for the [`dock_direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction").



Parameters
**value** (*integer*) – the docking direction. This can be one of the following bits:










| Dock Flag | Value | Description |
| --- | --- | --- |
| `AUI_DOCK_NONE` | 0 | No docking direction. |
| `AUI_DOCK_TOP` | 1 | Top docking direction. |
| `AUI_DOCK_RIGHT` | 2 | Right docking direction. |
| `AUI_DOCK_BOTTOM` | 3 | Bottom docking direction. |
| `AUI_DOCK_LEFT` | 4 | Left docking direction. |
| `AUI_DOCK_CENTER` | 5 | Center docking direction. |
| `AUI_DOCK_CENTRE` | 5 | Centre docking direction. |
| `AUI_DOCK_NOTEBOOK_PAGE` | 6 | Automatic AuiNotebooks docking style. |




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Dockable(self, b: bool=True) -> None:
        """ 

`Dockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Dockable "Permalink to this definition")
Specifies whether a frame can be docked or not. It is the same as specifying
[`TopDockable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.TopDockable "wx.lib.agw.aui.framemanager.AuiPaneInfo.TopDockable") . [`BottomDockable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomDockable "wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomDockable") . [`LeftDockable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftDockable "wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftDockable") . [`RightDockable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.RightDockable "wx.lib.agw.aui.framemanager.AuiPaneInfo.RightDockable") .



Parameters
**b** (*bool*) – whether the frame can be docked or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def DockFixed(self, b: bool=True) -> None:
        """ 

`DockFixed`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.DockFixed "Permalink to this definition")
Causes the containing dock to have no resize sash. This is useful
for creating panes that span the entire width or height of a dock, but should
not be resizable in the other direction.



Parameters
**b** (*bool*) – whether the pane will have a resize sash or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Fixed(self) -> None:
        """ 

`Fixed`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Fixed "Permalink to this definition")
Forces a pane to be fixed size so that it cannot be resized.
After calling [`Fixed`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Fixed "wx.lib.agw.aui.framemanager.AuiPaneInfo.Fixed"), [`IsFixed`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFixed "wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFixed") will return `True`.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Float(self) -> None:
        """ 

`Float`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Float "Permalink to this definition")
Indicates that a pane should be floated. It is the opposite of [`Dock`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Dock "wx.lib.agw.aui.framemanager.AuiPaneInfo.Dock").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Floatable(self, b: bool=True) -> None:
        """ 

`Floatable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Floatable "Permalink to this definition")
Sets whether the user will be able to undock a pane and turn it
into a floating window.



Parameters
**b** (*bool*) – whether the pane can be floated or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FloatingPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`FloatingPosition`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.FloatingPosition "Permalink to this definition")
Sets the position of the floating pane.



Parameters
**pos** – a [`wx.Point`](wx.Point.html#wx.Point "wx.Point") or a tuple indicating the pane floating position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FloatingSize(self, size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`FloatingSize`(*self*, *size*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.FloatingSize "Permalink to this definition")
Sets the size of the floating pane.



Parameters
**size** – a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") or a tuple indicating the pane floating size.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def FlyOut(self, b: bool=True) -> None:
        """ 

`FlyOut`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.FlyOut "Permalink to this definition")
Indicates whether a pane, when floating, has a “fly-out” effect
(i.e., floating panes which only show themselves when moused over).



Parameters
**b** (*bool*) – whether the pane can be snapped on the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def GetMinimizeMode(self) -> None:
        """ 

`GetMinimizeMode`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.GetMinimizeMode "Permalink to this definition")
Returns the minimization style for this pane.


Possible return values are:








| Minimize Mode Flag | Hex Value | Description |
| --- | --- | --- |
| `AUI_MINIMIZE_POS_SMART` | 0x01 | Minimizes the pane on the closest tool bar |
| `AUI_MINIMIZE_POS_TOP` | 0x02 | Minimizes the pane on the top tool bar |
| `AUI_MINIMIZE_POS_LEFT` | 0x03 | Minimizes the pane on its left tool bar |
| `AUI_MINIMIZE_POS_RIGHT` | 0x04 | Minimizes the pane on its right tool bar |
| `AUI_MINIMIZE_POS_BOTTOM` | 0x05 | Minimizes the pane on its bottom tool bar |
| `AUI_MINIMIZE_POS_TOOLBAR` | 0x06 | Minimizes the pane on a target [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |
| `AUI_MINIMIZE_POS_MASK` | 0x17 | Mask to filter the position flags |
| `AUI_MINIMIZE_CAPT_HIDE` | 0x0 | Hides the caption of the minimized pane |
| `AUI_MINIMIZE_CAPT_SMART` | 0x08 | Displays the caption in the best rotation (horizontal or clockwise) |
| `AUI_MINIMIZE_CAPT_HORZ` | 0x10 | Displays the caption horizontally |
| `AUI_MINIMIZE_CAPT_MASK` | 0x18 | Mask to filter the caption flags |


The flags can be filtered with the following masks:








| Minimize Mask Flag | Hex Value | Description |
| --- | --- | --- |
| `AUI_MINIMIZE_POS_MASK` | 0x17 | Filters the position flags |
| `AUI_MINIMIZE_CAPT_MASK` | 0x18 | Filters the caption flags |




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Gripper(self, visible: bool=True) -> None:
        """ 

`Gripper`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Gripper "Permalink to this definition")
Indicates that a gripper should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the gripper should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def GripperTop(self, attop: bool=True) -> None:
        """ 

`GripperTop`(*self*, *attop=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.GripperTop "Permalink to this definition")
Indicates that a gripper should be drawn at the top of the pane.



Parameters
**attop** (*bool*) – whether the gripper should be drawn at the top or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasBorder(self) -> None:
        """ 

`HasBorder`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasBorder "Permalink to this definition")
Returns `True` if the pane displays a border.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCaption(self) -> None:
        """ 

`HasCaption`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasCaption "Permalink to this definition")
Returns `True` if the pane displays a caption.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCaptionLeft(self) -> None:
        """ 

`HasCaptionLeft`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasCaptionLeft "Permalink to this definition")
Returns `True` if the pane displays a caption on the left (rotated by 90 degrees).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasCloseButton(self) -> None:
        """ 

`HasCloseButton`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasCloseButton "Permalink to this definition")
Returns `True` if the pane displays a button to close the pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasFlag(self, flag: int) -> None:
        """ 

`HasFlag`(*self*, *flag*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasFlag "Permalink to this definition")
Returns `True` if the the property specified by flag is active for the pane.



Parameters
**flag** (*integer*) – the property to check for activity.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasGripper(self) -> None:
        """ 

`HasGripper`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasGripper "Permalink to this definition")
Returns `True` if the pane displays a gripper.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasGripperTop(self) -> None:
        """ 

`HasGripperTop`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasGripperTop "Permalink to this definition")
Returns `True` if the pane displays a gripper at the top.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasMaximizeButton(self) -> None:
        """ 

`HasMaximizeButton`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasMaximizeButton "Permalink to this definition")
Returns `True` if the pane displays a button to maximize the pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasMinimizeButton(self) -> None:
        """ 

`HasMinimizeButton`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasMinimizeButton "Permalink to this definition")
Returns `True` if the pane displays a button to minimize the pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasNotebook(self) -> None:
        """ 

`HasNotebook`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasNotebook "Permalink to this definition")
Returns whether a pane has a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def HasPinButton(self) -> None:
        """ 

`HasPinButton`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.HasPinButton "Permalink to this definition")
Returns `True` if the pane displays a button to float the pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Hide(self) -> None:
        """ 

`Hide`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Hide "Permalink to this definition")
Indicates that a pane should be hidden.


Calling [`Show(False)`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Show "wx.lib.agw.aui.framemanager.AuiPaneInfo.Show") achieve the same effect.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Icon(self, icon: Icon) -> None:
        """ 

`Icon`(*self*, *icon*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Icon "Permalink to this definition")
Specifies whether an icon is drawn on the left of the caption text when
the pane is docked. If *icon* is `None` or `NullIcon`, no icon is drawn on
the caption space.



Parameters
**icon** ([`Icon`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Icon "wx.lib.agw.aui.framemanager.AuiPaneInfo.Icon") or `None`) – an icon to draw on the caption space, or `None`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsBottomDockable(self) -> None:
        """ 

`IsBottomDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsBottomDockable "Permalink to this definition")
Returns `True` if the pane can be docked at the bottom
of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsBottomSnappable(self) -> None:
        """ 

`IsBottomSnappable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsBottomSnappable "Permalink to this definition")
Returns `True` if the pane can be snapped at the bottom of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDestroyOnClose(self) -> None:
        """ 

`IsDestroyOnClose`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsDestroyOnClose "Permalink to this definition")
Returns `True` if the pane should be destroyed when it is closed.


Normally a pane is simply hidden when the close button is clicked. Calling [`DestroyOnClose`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.DestroyOnClose "wx.lib.agw.aui.framemanager.AuiPaneInfo.DestroyOnClose")
with a `True` input parameter will cause the window to be destroyed when the user clicks
the pane’s close button.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDockable(self) -> None:
        """ 

`IsDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsDockable "Permalink to this definition")
Returns `True` if the pane can be docked.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsDocked(self) -> None:
        """ 

`IsDocked`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsDocked "Permalink to this definition")
Returns `True` if the pane is docked.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFixed(self) -> None:
        """ 

`IsFixed`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFixed "Permalink to this definition")
Returns `True` if the pane cannot be resized.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFloatable(self) -> None:
        """ 

`IsFloatable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFloatable "Permalink to this definition")
Returns `True` if the pane can be undocked and displayed as a
floating window.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFloating(self) -> None:
        """ 

`IsFloating`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFloating "Permalink to this definition")
Returns `True` if the pane is floating.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsFlyOut(self) -> None:
        """ 

`IsFlyOut`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsFlyOut "Permalink to this definition")
Returns `True` if the floating pane has a “fly-out” effect.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsHorizontal(self) -> None:
        """ 

`IsHorizontal`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsHorizontal "Permalink to this definition")
Returns `True` if the pane [`dock_direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction") is horizontal.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsLeftDockable(self) -> None:
        """ 

`IsLeftDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsLeftDockable "Permalink to this definition")
Returns `True` if the pane can be docked at the left
of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsLeftSnappable(self) -> None:
        """ 

`IsLeftSnappable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsLeftSnappable "Permalink to this definition")
Returns `True` if the pane can be snapped on the left of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMaximized(self) -> None:
        """ 

`IsMaximized`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsMaximized "Permalink to this definition")
Returns `True` if the pane is maximized.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMinimized(self) -> None:
        """ 

`IsMinimized`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsMinimized "Permalink to this definition")
Returns `True` if the pane is minimized.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsMovable(self) -> None:
        """ 

`IsMovable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsMovable "Permalink to this definition")
Returns `True` if the docked frame can be undocked or moved to
another dock position.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookControl(self) -> None:
        """ 

`IsNotebookControl`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsNotebookControl "Permalink to this definition")
Returns whether the pane is a notebook control ([`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook")).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookDockable(self) -> None:
        """ 

`IsNotebookDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsNotebookDockable "Permalink to this definition")
Returns `True` if a pane can be docked on top to another to create a
[`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsNotebookPage(self) -> None:
        """ 

`IsNotebookPage`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsNotebookPage "Permalink to this definition")
Returns whether the pane is a notebook page in a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsOk(self) -> None:
        """ 

`IsOk`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsOk "Permalink to this definition")
Returns `True` if the [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") structure is valid.



Note


A pane structure is valid if it has an associated window.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsResizeable(self) -> None:
        """ 

`IsResizeable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsResizeable "Permalink to this definition")
Returns `True` if the pane can be resized.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsRightDockable(self) -> None:
        """ 

`IsRightDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsRightDockable "Permalink to this definition")
Returns `True` if the pane can be docked at the right
of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsRightSnappable(self) -> None:
        """ 

`IsRightSnappable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsRightSnappable "Permalink to this definition")
Returns `True` if the pane can be snapped on the right of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsShown(self) -> None:
        """ 

`IsShown`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsShown "Permalink to this definition")
Returns `True` if the pane is currently shown.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsSnappable(self) -> None:
        """ 

`IsSnappable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsSnappable "Permalink to this definition")
Returns `True` if the pane can be snapped.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsToolbar(self) -> None:
        """ 

`IsToolbar`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsToolbar "Permalink to this definition")
Returns `True` if the pane contains a toolbar.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsTopDockable(self) -> None:
        """ 

`IsTopDockable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsTopDockable "Permalink to this definition")
Returns `True` if the pane can be docked at the top
of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsTopSnappable(self) -> None:
        """ 

`IsTopSnappable`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsTopSnappable "Permalink to this definition")
Returns `True` if the pane can be snapped at the top of the managed frame.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def IsVertical(self) -> None:
        """ 

`IsVertical`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.IsVertical "Permalink to this definition")
Returns `True` if the pane [`dock_direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction") is vertical.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Layer(self, layer: int) -> None:
        """ 

`Layer`(*self*, *layer*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Layer "Permalink to this definition")
Determines the layer of the docked pane.


The dock layer is similar to an onion, the inner-most layer being layer 0. Each
shell moving in the outward direction has a higher layer number. This allows for
more complex docking layout formation.



Parameters
**layer** (*integer*) – the layer of the docked pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Left(self) -> None:
        """ 

`Left`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Left "Permalink to this definition")
Sets the pane dock position to the left side of the frame.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_LEFT` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def LeftDockable(self, b: bool=True) -> None:
        """ 

`LeftDockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftDockable "Permalink to this definition")
Indicates whether a pane can be docked on the left of the frame.



Parameters
**b** (*bool*) – whether the pane can be docked at the left or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def LeftSnappable(self, b: bool=True) -> None:
        """ 

`LeftSnappable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftSnappable "Permalink to this definition")
Indicates whether a pane can be snapped on the left of the main frame.



Parameters
**b** (*bool*) – whether the pane can be snapped at the left of the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Maximize(self) -> None:
        """ 

`Maximize`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Maximize "Permalink to this definition")
Makes the pane take up the full area.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaximizeButton(self, visible: bool=True) -> None:
        """ 

`MaximizeButton`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaximizeButton "Permalink to this definition")
Indicates that a maximize button should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the maximize button should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize(self, arg1=None, arg2=None) -> None:
        """ 

`MaxSize`(*self*, *arg1=None*, *arg2=None*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize "Permalink to this definition")
Sets the maximum size of the pane.


This method is split in 2 versions depending on the input type. If *arg1* is
a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, then [`MaxSize1`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize1 "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize1") is called. Otherwise, [`MaxSize2`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize2 "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize2") is called.



Parameters
* **arg1** – a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, a (x, y) tuple or a *x* coordinate.
* **arg2** – a *y* coordinate (only if *arg1* is a *x* coordinate, otherwise unused).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize1(self, size) -> None:
        """ 

`MaxSize1`(*self*, *size*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize1 "Permalink to this definition")
Sets the maximum size of the pane.



See also


[`MaxSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MaxSize2(self, x, y) -> None:
        """ 

`MaxSize2`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize2 "Permalink to this definition")
Sets the maximum size of the pane.



See also


[`MaxSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.MaxSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Minimize(self) -> None:
        """ 

`Minimize`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Minimize "Permalink to this definition")
Makes the pane minimized in a [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").


Clicking on the minimize button causes a new [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") to be created
and added to the frame manager, (currently the implementation is such that
panes at West will have a toolbar at the right, panes at South will have
toolbars at the bottom etc…) and the pane is hidden in the manager.


Clicking on the restore button on the newly created toolbar will result in the
toolbar being removed and the original pane being restored.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeButton(self, visible: bool=True) -> None:
        """ 

`MinimizeButton`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinimizeButton "Permalink to this definition")
Indicates that a minimize button should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the minimize button should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeMode(self, mode: int) -> None:
        """ 

`MinimizeMode`(*self*, *mode*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinimizeMode "Permalink to this definition")
Sets the expected minimized mode if the minimize button is visible.



Parameters
**mode** (*integer*) – the minimized pane can have a specific position in the work space:










| Minimize Mode Flag | Hex Value | Description |
| --- | --- | --- |
| `AUI_MINIMIZE_POS_SMART` | 0x01 | Minimizes the pane on the closest tool bar |
| `AUI_MINIMIZE_POS_TOP` | 0x02 | Minimizes the pane on the top tool bar |
| `AUI_MINIMIZE_POS_LEFT` | 0x03 | Minimizes the pane on its left tool bar |
| `AUI_MINIMIZE_POS_RIGHT` | 0x04 | Minimizes the pane on its right tool bar |
| `AUI_MINIMIZE_POS_BOTTOM` | 0x05 | Minimizes the pane on its bottom tool bar |
| `AUI_MINIMIZE_POS_TOOLBAR` | 0x06 | Minimizes the pane on a target [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar") |


The caption of the minimized pane can be displayed in different modes:








| Caption Mode Flag | Hex Value | Description |
| --- | --- | --- |
| `AUI_MINIMIZE_CAPT_HIDE` | 0x0 | Hides the caption of the minimized pane |
| `AUI_MINIMIZE_CAPT_SMART` | 0x08 | Displays the caption in the best rotation (horizontal in the top and in the bottom tool bar or clockwise in the right and in the left tool bar) |
| `AUI_MINIMIZE_CAPT_HORZ` | 0x10 | Displays the caption horizontally |



Note


In order to use the `AUI_MINIMIZE_POS_TOOLBAR` flag, the instance of [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager")
you pass as an input for [`MinimizeTarget`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinimizeTarget "wx.lib.agw.aui.framemanager.AuiPaneInfo.MinimizeTarget") **must** have a real name and not the randomly
generated one. Remember to set the [`Name`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Name "wx.lib.agw.aui.framemanager.AuiPaneInfo.Name") property of the toolbar pane before calling this method.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinimizeTarget(self, toolbarPane: AuiPaneInfo) -> None:
        """ 

`MinimizeTarget`(*self*, *toolbarPane*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinimizeTarget "Permalink to this definition")
Minimizes the panes using a [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") as a target. As [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") properties
need to be copied back and forth every time the perspective has changed, we
only store the toobar **name**.



Parameters
**toolbarPane** – an instance of [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo"), containing a [`AuiToolBar`](wx.lib.agw.aui.auibar.AuiToolBar.html#wx.lib.agw.aui.auibar.AuiToolBar "wx.lib.agw.aui.auibar.AuiToolBar").





Note


In order to use this functionality (and with the `AUI_MINIMIZE_POS_TOOLBAR`
flag set), the instance of [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") you pass as an input **must** have a real
name and not the randomly generated one. Remember to set the [`Name`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Name "wx.lib.agw.aui.framemanager.AuiPaneInfo.Name") property of
the toolbar pane before calling this method.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize(self, arg1=None, arg2=None) -> None:
        """ 

`MinSize`(*self*, *arg1=None*, *arg2=None*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize "Permalink to this definition")
Sets the minimum size of the pane.


This method is split in 2 versions depending on the input type. If *arg1* is
a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, then [`MinSize1`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize1 "wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize1") is called. Otherwise, [`MinSize2`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize2 "wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize2") is called.



Parameters
* **arg1** – a [`wx.Size`](wx.Size.html#wx.Size "wx.Size") object, a (x, y) tuple or or a *x* coordinate.
* **arg2** – a *y* coordinate (only if *arg1* is a *x* coordinate, otherwise unused).






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize1(self, size) -> None:
        """ 

`MinSize1`(*self*, *size*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize1 "Permalink to this definition")
Sets the minimum size of the pane.



See also


[`MinSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def MinSize2(self, x, y) -> None:
        """ 

`MinSize2`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize2 "Permalink to this definition")
Sets the minimum size of the pane.



See also


[`MinSize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize "wx.lib.agw.aui.framemanager.AuiPaneInfo.MinSize") for an explanation of input parameters.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Movable(self, b: bool=True) -> None:
        """ 

`Movable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Movable "Permalink to this definition")
Indicates whether a pane can be moved.



Parameters
**b** (*bool*) – whether the pane can be moved or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Name(self, name: Any) -> None:
        """ 

`Name`(*self*, *name*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Name "Permalink to this definition")
Sets the name of the pane so it can be referenced in lookup functions.


If a name is not specified by the user, a random name is assigned to the pane
when it is added to the manager.



Parameters
**name** – a string specifying the pane name.





Warning


If you are using [`AuiManager.SavePerspective`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.SavePerspective "wx.lib.agw.aui.framemanager.AuiManager.SavePerspective") and [`AuiManager.LoadPerspective`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective "wx.lib.agw.aui.framemanager.AuiManager.LoadPerspective"),
you will have to specify a name for your pane using [`Name`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Name "wx.lib.agw.aui.framemanager.AuiPaneInfo.Name"), as perspectives
containing randomly generated names can not be properly restored.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookControl(self, id: int) -> None:
        """ 

`NotebookControl`(*self*, *id*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.NotebookControl "Permalink to this definition")
Forces a pane to be a notebook control ([`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook")).



Parameters
**id** (*integer*) – the notebook id.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookDockable(self, b: bool=True) -> None:
        """ 

`NotebookDockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.NotebookDockable "Permalink to this definition")
Indicates whether a pane can be docked in an automatic [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**b** (*bool*) – whether the pane can be docked in a notebook or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def NotebookPage(self, id, tab_position=1000) -> None:
        """ 

`NotebookPage`(*self*, *id*, *tab\_position=1000*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.NotebookPage "Permalink to this definition")
Forces a pane to be a notebook page, so that the pane can be
docked on top to another to create a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
* **id** (*integer*) – the notebook id;
* **tab\_position** (*integer*) – the tab number of the pane once docked in a notebook.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def PaneBorder(self, visible: bool=True) -> None:
        """ 

`PaneBorder`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.PaneBorder "Permalink to this definition")
Indicates that a border should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the pane border should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def PinButton(self, visible: bool=True) -> None:
        """ 

`PinButton`(*self*, *visible=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.PinButton "Permalink to this definition")
Indicates that a pin button should be drawn for the pane.



Parameters
**visible** (*bool*) – whether the pin button should be visible or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Position(self, pos: int) -> None:
        """ 

`Position`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Position "Permalink to this definition")
Determines the position of the docked pane.



Parameters
**pos** (*integer*) – the position of the docked pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def ResetButtons(self) -> None:
        """ 

`ResetButtons`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.ResetButtons "Permalink to this definition")
Resets all the buttons and recreates them from scratch depending on the
[`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") flags.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Resizable(self, resizable: bool=True) -> None:
        """ 

`Resizable`(*self*, *resizable=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Resizable "Permalink to this definition")
Allows a pane to be resizable if *resizable* is `True`, and forces
it to be a fixed size if *resizeable* is `False`.


If *resizable* is `False`, this is simply an antonym for [`Fixed`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Fixed "wx.lib.agw.aui.framemanager.AuiPaneInfo.Fixed").



Parameters
**resizable** (*bool*) – whether the pane will be resizeable or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Restore(self) -> None:
        """ 

`Restore`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Restore "Permalink to this definition")
Is the reverse of [`Maximize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Maximize "wx.lib.agw.aui.framemanager.AuiPaneInfo.Maximize") and [`Minimize`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Minimize "wx.lib.agw.aui.framemanager.AuiPaneInfo.Minimize").




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Right(self) -> None:
        """ 

`Right`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Right "Permalink to this definition")
Sets the pane dock position to the right side of the frame.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_RIGHT` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def RightDockable(self, b: bool=True) -> None:
        """ 

`RightDockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.RightDockable "Permalink to this definition")
Indicates whether a pane can be docked on the right of the frame.



Parameters
**b** (*bool*) – whether the pane can be docked at the right or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def RightSnappable(self, b: bool=True) -> None:
        """ 

`RightSnappable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.RightSnappable "Permalink to this definition")
Indicates whether a pane can be snapped on the right of the main frame.



Parameters
**b** (*bool*) – whether the pane can be snapped at the right of the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Row(self, row: int) -> None:
        """ 

`Row`(*self*, *row*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Row "Permalink to this definition")
Determines the row of the docked pane.



Parameters
**row** (*integer*) – the row of the docked pane.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetDockPos(self, source: AuiPaneInfo) -> None:
        """ 

`SetDockPos`(*self*, *source*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.SetDockPos "Permalink to this definition")
Copies the *source* pane members that pertain to docking position to *self*.



Parameters
**source** – the source pane from where to copy the attributes,
an instance of [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetFlag(self, flag, option_state) -> None:
        """ 

`SetFlag`(*self*, *flag*, *option\_state*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.SetFlag "Permalink to this definition")
Turns the property given by *flag* on or off with the *option\_state*
parameter.



Parameters
* **flag** (*integer*) – the property to set;
* **option\_state** (*bool*) – either `True` or `False`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def SetNameFromNotebookId(self) -> None:
        """ 

`SetNameFromNotebookId`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.SetNameFromNotebookId "Permalink to this definition")
Sets the pane name once docked in a [`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook") using the notebook id.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Show(self, show: bool=True) -> None:
        """ 

`Show`(*self*, *show=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Show "Permalink to this definition")
Indicates that a pane should be shown.



Parameters
**show** (*bool*) – whether the pane should be shown or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Snappable(self, b: bool=True) -> None:
        """ 

`Snappable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Snappable "Permalink to this definition")
Indicates whether a pane can be snapped on the main frame. This is
equivalent as calling [`TopSnappable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.TopSnappable "wx.lib.agw.aui.framemanager.AuiPaneInfo.TopSnappable") . [`BottomSnappable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomSnappable "wx.lib.agw.aui.framemanager.AuiPaneInfo.BottomSnappable") . [`LeftSnappable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftSnappable "wx.lib.agw.aui.framemanager.AuiPaneInfo.LeftSnappable") . [`RightSnappable`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.RightSnappable "wx.lib.agw.aui.framemanager.AuiPaneInfo.RightSnappable") .



Parameters
**b** (*bool*) – whether the pane can be snapped on the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def ToolbarPane(self) -> None:
        """ 

`ToolbarPane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.ToolbarPane "Permalink to this definition")
Specifies that the pane should adopt the default toolbar pane settings.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Top(self) -> None:
        """ 

`Top`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Top "Permalink to this definition")
Sets the pane dock position to the top of the frame.



Note


This is the same thing as calling [`Direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.Direction") with `AUI_DOCK_TOP` as
parameter.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def TopDockable(self, b: bool=True) -> None:
        """ 

`TopDockable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.TopDockable "Permalink to this definition")
Indicates whether a pane can be docked at the top of the frame.



Parameters
**b** (*bool*) – whether the pane can be docked at the top or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def TopSnappable(self, b: bool=True) -> None:
        """ 

`TopSnappable`(*self*, *b=True*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.TopSnappable "Permalink to this definition")
Indicates whether a pane can be snapped at the top of the main frame.



Parameters
**b** (*bool*) – whether the pane can be snapped at the top of the main frame or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Transparent(self, alpha: int) -> None:
        """ 

`Transparent`(*self*, *alpha*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Transparent "Permalink to this definition")
Makes the pane transparent when floating.



Parameters
**alpha** (*integer*) – a value between 0 and 255 for pane transparency.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    def Window(self, w: 'Window') -> None:
        """ 

`Window`(*self*, *w*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.Window "Permalink to this definition")
Associate a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window to this pane.


This normally does not need to be specified, as the window pointer is
automatically assigned to the [`AuiPaneInfo`](#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") structure as soon as it is
added to the manager.



Parameters
**w** – a [`wx.Window`](wx.Window.html#wx.Window "wx.Window") derived window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneInfo.html
        """

    dock_direction: Any  # `dock_direction`[¶](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "Permalink to this definition")Getter for the [`dock_direction`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction").See also[`dock_direction_set`](#wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set "wx.lib.agw.aui.framemanager.AuiPaneInfo.dock_direction_set") for a set of valid docking directions.



class AuiManager_DCP(AuiManager):
    """ A class similar to [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") but with a Dummy Center Pane (**DCP**).
The code for this class is still flickery due to the call to `CallAfter`
and the double-update call.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
    """
    def __init__(self, *args, **keys) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*keys*)[¶](#wx.lib.agw.aui.framemanager.AuiManager_DCP.__init__ "Permalink to this definition")
See [`AuiManager.__init__`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.__init__ "wx.lib.agw.aui.framemanager.AuiManager.__init__") for the class construction.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
        """

    def Update(self) -> None:
        """ 

`Update`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManager_DCP.Update "Permalink to this definition")
This method is called after any number of changes are made to any of the
managed panes. [`Update`](#wx.lib.agw.aui.framemanager.AuiManager_DCP.Update "wx.lib.agw.aui.framemanager.AuiManager_DCP.Update") must be invoked after [`AuiManager.AddPane`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.AddPane "wx.lib.agw.aui.framemanager.AuiManager.AddPane") or
[`AuiManager.InsertPane`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.InsertPane "wx.lib.agw.aui.framemanager.AuiManager.InsertPane") are called in order to “realize” or “commit” the changes.


In addition, any number of changes may be made to [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") structures
(retrieved with [`AuiManager.GetPane`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager.GetPane "wx.lib.agw.aui.framemanager.AuiManager.GetPane")), but to realize the changes,
[`Update`](#wx.lib.agw.aui.framemanager.AuiManager_DCP.Update "wx.lib.agw.aui.framemanager.AuiManager_DCP.Update") must be called. This construction allows pane flicker to
be avoided by updating the whole layout at one time.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManager_DCP.html
        """



class AuiDockInfo:
    """ A class to store all properties of a dock.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockInfo.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsHorizontal(self) -> None:
        """ 

`IsHorizontal`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockInfo.IsHorizontal "Permalink to this definition")
Returns whether the dock is horizontal or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsOk(self) -> None:
        """ 

`IsOk`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockInfo.IsOk "Permalink to this definition")
Returns whether a dock is valid or not.


In order to be valid, a dock needs to have a non-zero *dock\_direction*.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """

    def IsVertical(self) -> None:
        """ 

`IsVertical`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockInfo.IsVertical "Permalink to this definition")
Returns whether the dock is vertical or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockInfo.html
        """



class AuiDockUIPart:
    """ A class which holds attributes for a UI part in the interface.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockUIPart.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockUIPart.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockUIPart.html
        """



class AuiManagerEvent(PyCommandEvent):
    """ A specialized command event class for events sent by [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
    """
    def __init__(self, eventType, id=1) -> None:
        """ 

`__init__`(*self*, *eventType*, *id=1*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **eventType** (*integer*) – the event kind;
* **id** (*integer*) – the event identification number.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def CanVeto(self) -> None:
        """ 

`CanVeto`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.CanVeto "Permalink to this definition")
Returns whether the event can be vetoed and has been vetoed.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetButton(self) -> None:
        """ 

`GetButton`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.GetButton "Permalink to this definition")
Returns the associated [`AuiPaneButton`](wx.lib.agw.aui.framemanager.AuiPaneButton.html#wx.lib.agw.aui.framemanager.AuiPaneButton "wx.lib.agw.aui.framemanager.AuiPaneButton") instance (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetDC(self) -> None:
        """ 

`GetDC`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.GetDC "Permalink to this definition")
Returns the associated [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetManager(self) -> None:
        """ 

`GetManager`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.GetManager "Permalink to this definition")
Returns the associated [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetPane(self) -> None:
        """ 

`GetPane`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.GetPane "Permalink to this definition")
Returns the associated [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") structure (if any).




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def GetVeto(self) -> None:
        """ 

`GetVeto`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.GetVeto "Permalink to this definition")
Returns whether the event has been vetoed or not.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetButton(self, b: AuiPaneButton) -> None:
        """ 

`SetButton`(*self*, *b*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.SetButton "Permalink to this definition")
Associates a [`AuiPaneButton`](wx.lib.agw.aui.framemanager.AuiPaneButton.html#wx.lib.agw.aui.framemanager.AuiPaneButton "wx.lib.agw.aui.framemanager.AuiPaneButton") instance to this event.



Parameters
**b** – a [`AuiPaneButton`](wx.lib.agw.aui.framemanager.AuiPaneButton.html#wx.lib.agw.aui.framemanager.AuiPaneButton "wx.lib.agw.aui.framemanager.AuiPaneButton") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetCanVeto(self, can_veto: bool) -> None:
        """ 

`SetCanVeto`(*self*, *can\_veto*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.SetCanVeto "Permalink to this definition")
Sets whether the event can be vetoed or not.



Parameters
**can\_veto** (*bool*) – `True` if the event can be vetoed, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetDC(self, pdc: 'DC') -> None:
        """ 

`SetDC`(*self*, *pdc*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.SetDC "Permalink to this definition")
Associates a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context to this event.



Parameters
**pdc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetManager(self, mgr: AuiManager) -> None:
        """ 

`SetManager`(*self*, *mgr*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.SetManager "Permalink to this definition")
Associates a [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") to the current event.



Parameters
**mgr** – an instance of [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def SetPane(self, p: AuiPaneInfo) -> None:
        """ 

`SetPane`(*self*, *p*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.SetPane "Permalink to this definition")
Associates a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance to this event.



Parameters
**p** – a [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") instance.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """

    def Veto(self, veto: bool=True) -> None:
        """ 

`Veto`(*self*, *veto=True*)[¶](#wx.lib.agw.aui.framemanager.AuiManagerEvent.Veto "Permalink to this definition")
Prevents the change announced by this event from happening.


It is in general a good idea to notify the user about the reasons for
vetoing the change because otherwise the applications behaviour (which
just refuses to do what the user wants) might be quite surprising.



Parameters
**veto** (*bool*) – `True` to veto the event, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiManagerEvent.html
        """



class AuiPaneButton:
    """ A simple class which describes the caption pane button attributes.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneButton.html
    """
    def __init__(self, button_id: int) -> None:
        """ 

`__init__`(*self*, *button\_id*)[¶](#wx.lib.agw.aui.framemanager.AuiPaneButton.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!



Parameters
**button\_id** (*integer*) – the pane button identifier.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiPaneButton.html
        """



class AuiCenterDockingGuide(AuiDockingGuide):
    """ A docking guide window for multiple docking hint (diamond-shaped HUD).


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
    """
    def __init__(self, parent: AuiManager) -> None:
        """ 

`__init__`(*self*, *parent*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!



Parameters
**parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def AeroMove(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`AeroMove`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.AeroMove "Permalink to this definition")
Moves the docking guide window to the new position.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the new docking guide position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def CreateShapesWithStyle(self) -> None:
        """ 

`CreateShapesWithStyle`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.CreateShapesWithStyle "Permalink to this definition")
Creates the docking guide window shape based on which docking bitmaps are used.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.HitTest "Permalink to this definition")
Checks if the mouse position is inside the target windows rect.



Parameters
* **x** (*integer*) – the *x* mouse position;
* **y** (*integer*) – the *y* mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`AuiCenterDockingGuide`](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide "wx.lib.agw.aui.framemanager.AuiCenterDockingGuide").



Parameters
**event** – `EraseEvent` to be processed.





Note


This is intentionally empty to reduce flickering while drawing.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiCenterDockingGuide`](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide "wx.lib.agw.aui.framemanager.AuiCenterDockingGuide").



Parameters
**event** – a `PaintEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def SetGuideShape(self, event: Optional['WindowCreateEvent']=None) -> None:
        """ 

`SetGuideShape`(*self*, *event=None*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.SetGuideShape "Permalink to this definition")
Sets the correct shape for the docking guide window.



Parameters
**event** – on wxGTK, a [`wx.WindowCreateEvent`](wx.WindowCreateEvent.html#wx.WindowCreateEvent "wx.WindowCreateEvent") event to process.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`UpdateDockGuide`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.UpdateDockGuide "Permalink to this definition")
Updates the docking guides images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """

    def ValidateNotebookDocking(self, valid: bool) -> None:
        """ 

`ValidateNotebookDocking`(*self*, *valid*)[¶](#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.ValidateNotebookDocking "Permalink to this definition")
Sets whether a pane can be docked on top of another to create an automatic
[`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").



Parameters
**valid** (*bool*) – whether a pane can be docked on top to another to form an automatic
[`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html
        """



class AuiDockingGuide(Frame):
    """ Base class for [`AuiSingleDockingGuide`](wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide "wx.lib.agw.aui.framemanager.AuiSingleDockingGuide") and [`AuiCenterDockingGuide`](wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide "wx.lib.agw.aui.framemanager.AuiCenterDockingGuide").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
    """
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.NO_BORDER, name="AuiDockingGuide") -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *title=""*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=wx.FRAME\_TOOL\_WINDOW | wx.STAY\_ON\_TOP | wx.FRAME\_NO\_TASKBAR | wx.NO\_BORDER*, *name="AuiDockingGuide"*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuide.__init__ "Permalink to this definition")
Default class constructor. Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent;
* **id** (*integer*) – the window identifier. It may take a value of -1 to indicate a default value.
* **title** (*string*) – the caption to be displayed on the frame’s title bar.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the window position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the window size. A value of (-1, -1) indicates a default size, chosen by
either the windowing system or wxPython, depending on platform.
* **style** (*integer*) – the window style.
* **name** (*string*) – the name of the window. This parameter is used to associate a name with the
item, allowing the application user to set Motif resource values for individual windows.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuide.HitTest "Permalink to this definition")
To be overridden by parent classes.



Parameters
* **x** (*integer*) – the *x* mouse position;
* **y** (*integer*) – the *y* mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """

    def ValidateNotebookDocking(self, valid: bool) -> None:
        """ 

`ValidateNotebookDocking`(*self*, *valid*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuide.ValidateNotebookDocking "Permalink to this definition")
To be overridden by parent classes.



Parameters
**valid** (*bool*) – whether a pane can be docked on top to another to form an automatic
[`AuiNotebook`](wx.lib.agw.aui.auibook.AuiNotebook.html#wx.lib.agw.aui.auibook.AuiNotebook "wx.lib.agw.aui.auibook.AuiNotebook").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuide.html
        """



class AuiSingleDockingGuide(AuiDockingGuide):
    """ A docking guide window for single docking hint (not diamond-shaped HUD).


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
    """
    def __init__(self, parent, direction=0) -> None:
        """ 

`__init__`(*self*, *parent*, *direction=0*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.__init__ "Permalink to this definition")
Default class constructor. Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent;
* **direction** (*integer*) – one of `wx.TOP`, `wx.BOTTOM`, `wx.LEFT`, `wx.RIGHT`.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def AeroMove(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`AeroMove`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.AeroMove "Permalink to this definition")
Moves the docking window to the new position. Overridden in children classes.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the new docking guide position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def CreateShapesWithStyle(self, useWhidbey: bool) -> None:
        """ 

`CreateShapesWithStyle`(*self*, *useWhidbey*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.CreateShapesWithStyle "Permalink to this definition")
Creates the docking guide window shape based on which docking bitmaps are used.



Parameters
**useWhidbey** (*bool*) – if `True`, use Whidbey-style bitmaps; if `False`, use the
Aero-style bitmaps.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def HitTest(self, x, y) -> None:
        """ 

`HitTest`(*self*, *x*, *y*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.HitTest "Permalink to this definition")
Checks if the mouse position is inside the target window rect.



Parameters
* **x** (*integer*) – the *x* mouse position;
* **y** (*integer*) – the *y* mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def IsValid(self) -> None:
        """ 

`IsValid`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.IsValid "Permalink to this definition")
Returns whether the docking direction is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetGuideShape(self, event: Optional['WindowCreateEvent']=None) -> None:
        """ 

`SetGuideShape`(*self*, *event=None*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.SetGuideShape "Permalink to this definition")
Sets the correct shape for the docking guide window.



Parameters
**event** – on wxGTK, a [`wx.WindowCreateEvent`](wx.WindowCreateEvent.html#wx.WindowCreateEvent "wx.WindowCreateEvent") event to process.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetShape(self, region: Region) -> None:
        """ 

`SetShape`(*self*, *region*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.SetShape "Permalink to this definition")
If the platform supports it, sets the shape of the window to that depicted by *region*.
The system will not display or respond to any mouse event for the pixels that lie
outside of the region. To reset the window to the normal rectangular shape simply call
[`SetShape`](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.SetShape "wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.SetShape") again with an empty region.



Parameters
**region** ([*Region*](wx.Region.html#wx.Region "wx.Region")) – the shape of the frame.





Note


Overridden for wxMAC.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def SetValid(self, valid: bool) -> None:
        """ 

`SetValid`(*self*, *valid*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.SetValid "Permalink to this definition")
Sets the docking direction as valid or invalid.



Parameters
**valid** (*bool*) – whether the docking direction is allowed or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`UpdateDockGuide`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.UpdateDockGuide "Permalink to this definition")
Updates the docking guide images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiSingleDockingGuide.html
        """



TOP: int

BOTTOM: int

LEFT: int

RIGHT: int

class AuiDockingGuideInfo:
    """ A class which holds information about VS2005 docking guide windows.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
    """
    def __init__(self, other: Optional[AuiDockingGuideInfo]=None) -> None:
        """ 

`__init__`(*self*, *other=None*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.__init__ "Permalink to this definition")
Default class constructor.
Used internally, do not call it in your code!



Parameters
**other** – another instance of [`AuiDockingGuideInfo`](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo "wx.lib.agw.aui.framemanager.AuiDockingGuideInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Assign(self, other: AuiDockingGuideInfo) -> None:
        """ 

`Assign`(*self*, *other*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Assign "Permalink to this definition")
Assigns the properties of the *other* [`AuiDockingGuideInfo`](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo "wx.lib.agw.aui.framemanager.AuiDockingGuideInfo") to *self*.



Parameters
**other** – another instance of [`AuiDockingGuideInfo`](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo "wx.lib.agw.aui.framemanager.AuiDockingGuideInfo").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Bottom(self) -> None:
        """ 

`Bottom`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Bottom "Permalink to this definition")
Sets the guide window to bottom docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Center(self) -> None:
        """ 

`Center`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Center "Permalink to this definition")
Sets the guide window to center docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Centre(self) -> None:
        """ 

`Centre`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Centre "Permalink to this definition")
Sets the guide window to centre docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Host(self, h: AuiDockingGuideWindow) -> None:
        """ 

`Host`(*self*, *h*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Host "Permalink to this definition")
Hosts a docking guide window.



Parameters
**h** – an instance of [`AuiDockingGuideWindow`](wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow "wx.lib.agw.aui.framemanager.AuiDockingGuideWindow") or [`AuiDockingHintWindow`](wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html#wx.lib.agw.aui.framemanager.AuiDockingHintWindow "wx.lib.agw.aui.framemanager.AuiDockingHintWindow").






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Left(self) -> None:
        """ 

`Left`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Left "Permalink to this definition")
Sets the guide window to left docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Right(self) -> None:
        """ 

`Right`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Right "Permalink to this definition")
Sets the guide window to right docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """

    def Top(self) -> None:
        """ 

`Top`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.Top "Permalink to this definition")
Sets the guide window to top docking.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideInfo.html
        """



class AuiDockingGuideWindow(Window):
    """ Target class for [`AuiDockingGuide`](wx.lib.agw.aui.framemanager.AuiDockingGuide.html#wx.lib.agw.aui.framemanager.AuiDockingGuide "wx.lib.agw.aui.framemanager.AuiDockingGuide") and [`AuiCenterDockingGuide`](wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide "wx.lib.agw.aui.framemanager.AuiCenterDockingGuide").


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
    """
    def __init__(self, parent, rect, direction=0, center=False, useAero=False) -> None:
        """ 

`__init__`(*self*, *parent*, *rect*, *direction=0*, *center=False*, *useAero=False*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.__init__ "Permalink to this definition")
Default class constructor. Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent;
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the window rect;
* **direction** (*integer*) – one of `wx.TOP`, `wx.BOTTOM`, `wx.LEFT`, `wx.RIGHT`,
`wx.CENTER`;
* **center** (*bool*) – whether the calling class is a [`AuiCenterDockingGuide`](wx.lib.agw.aui.framemanager.AuiCenterDockingGuide.html#wx.lib.agw.aui.framemanager.AuiCenterDockingGuide "wx.lib.agw.aui.framemanager.AuiCenterDockingGuide");
* **useAero** (*bool*) – whether to use the new Aero-style bitmaps or Whidbey-style bitmaps
for the docking guide.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def Draw(self, dc: 'DC') -> None:
        """ 

`Draw`(*self*, *dc*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.Draw "Permalink to this definition")
Draws the whole docking guide window (not used if the docking guide images are ok).



Parameters
**dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawArrow(self, dc: 'DC') -> None:
        """ 

`DrawArrow`(*self*, *dc*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.DrawArrow "Permalink to this definition")
Draws the docking guide arrow icon (not used if the docking guide images are ok).



Parameters
**dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawBackground(self, dc: 'DC') -> None:
        """ 

`DrawBackground`(*self*, *dc*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.DrawBackground "Permalink to this definition")
Draws the docking guide background.



Parameters
**dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawDottedLine(self, dc, point, length, vertical) -> None:
        """ 

`DrawDottedLine`(*self*, *dc*, *point*, *length*, *vertical*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.DrawDottedLine "Permalink to this definition")
Draws a dotted line (not used if the docking guide images are ok).



Parameters
* **dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object;
* **point** – a [`wx.Point`](wx.Point.html#wx.Point "wx.Point") where to start drawing the dotted line;
* **length** (*integer*) – the length of the dotted line;
* **vertical** (*bool*) – whether it is a vertical docking guide window or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def DrawIcon(self, dc: 'DC') -> None:
        """ 

`DrawIcon`(*self*, *dc*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.DrawIcon "Permalink to this definition")
Draws the docking guide icon (not used if the docking guide images are ok).



Parameters
**dc** – a [`wx.DC`](wx.DC.html#wx.DC "wx.DC") device context object.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def IsValid(self) -> None:
        """ 

`IsValid`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.IsValid "Permalink to this definition")
Returns whether the docking direction is valid.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def OnEraseBackground(self, event: EraseEvent) -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.OnEraseBackground "Permalink to this definition")
Handles the `wx.EVT_ERASE_BACKGROUND` event for [`AuiDockingGuideWindow`](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow "wx.lib.agw.aui.framemanager.AuiDockingGuideWindow").



Parameters
**event** – a `EraseEvent` to be processed.





Note


This is intentionally empty to reduce flickering while drawing.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiDockingGuideWindow`](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow "wx.lib.agw.aui.framemanager.AuiDockingGuideWindow").



Parameters
**event** – a `PaintEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def SetValid(self, valid: bool) -> None:
        """ 

`SetValid`(*self*, *valid*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.SetValid "Permalink to this definition")
Sets the docking direction as valid or invalid.



Parameters
**valid** (*bool*) – whether the docking direction is allowed or not.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """

    def UpdateDockGuide(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`UpdateDockGuide`(*self*, *pos*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.UpdateDockGuide "Permalink to this definition")
Updates the docking guide images depending on the mouse position, using focused
images if the mouse is inside the docking guide or unfocused images if it is
outside.



Parameters
**pos** – a [`wx.Point`](wx.Point.html#wx.Point "wx.Point") mouse position.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingGuideWindow.html
        """



CENTER: int

class AuiDockingHintWindow(Frame):
    """ The original wxAUI docking window hint.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=wx.ID\_ANY*, *title=""*, *pos=wx.DefaultPosition*, *size=wx.Size(1*, *1)*, *style=wx.FRAME\_TOOL\_WINDOW | wx.FRAME\_FLOAT\_ON\_PARENT | wx.FRAME\_NO\_TASKBAR | wx.NO\_BORDER | wx.FRAME\_SHAPED*, *name="auiHintWindow"*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.__init__ "Permalink to this definition")
Default class constructor. Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent;
* **id** (*integer*) – the window identifier. It may take a value of -1 to indicate a default value.
* **title** (*string*) – the caption to be displayed on the frame’s title bar;
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – the window position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – the window size. A value of (-1, -1) indicates a default size, chosen by
either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the window style;
* **name** (*string*) – the name of the window. This parameter is used to associate a name with the
item, allowing the application user to set Motif resource values for individual windows.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def MakeVenetianBlinds(self) -> None:
        """ 

`MakeVenetianBlinds`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.MakeVenetianBlinds "Permalink to this definition")
Creates the “venetian blind” effect if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") has the `AUI_MGR_VENETIAN_BLINDS_HINT`
flag set.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def OnPaint(self, event: PaintEvent) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.OnPaint "Permalink to this definition")
Handles the `wx.EVT_PAINT` event for [`AuiDockingHintWindow`](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow "wx.lib.agw.aui.framemanager.AuiDockingHintWindow").



Parameters
**event** – an instance of `PaintEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiDockingHintWindow`](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow "wx.lib.agw.aui.framemanager.AuiDockingHintWindow").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def SetBlindMode(self, agwFlags: int) -> None:
        """ 

`SetBlindMode`(*self*, *agwFlags*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.SetBlindMode "Permalink to this definition")
Sets whether venetian blinds or transparent hints will be shown as docking hint.
This depends on the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") flags.



Parameters
**agwFlags** (*integer*) – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") flags.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def SetShape(self, region: Region) -> None:
        """ 

`SetShape`(*self*, *region*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.SetShape "Permalink to this definition")
If the platform supports it, sets the shape of the window to that depicted by *region*.
The system will not display or respond to any mouse event for the pixels that lie
outside of the region. To reset the window to the normal rectangular shape simply call
[`SetShape`](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.SetShape "wx.lib.agw.aui.framemanager.AuiDockingHintWindow.SetShape") again with an empty region.



Parameters
**region** ([*Region*](wx.Region.html#wx.Region "wx.Region")) – the shape of the frame.





Note


Overridden for wxMAC.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """

    def Show(self, show: bool=True) -> None:
        """ 

`Show`(*self*, *show=True*)[¶](#wx.lib.agw.aui.framemanager.AuiDockingHintWindow.Show "Permalink to this definition")
Show the hint window.



Parameters
**show** (*bool*) – whether to show or hide the hint docking window.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiDockingHintWindow.html
        """



class AuiFloatingFrame(MiniFrame):
    """ AuiFloatingFrame is the frame class that holds floating panes.


  


        Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
    """
    def __init__(self, parent, owner_mgr, pane=None, id=wx.ID_ANY, title="", style=wx.FRAME_TOOL_WINDOW | wx.FRAME_FLOAT_ON_PARENT | wx.FRAME_NO_TASKBAR | wx.CLIP_CHILDREN) -> None:
        """ 

`__init__`(*self*, *parent*, *owner\_mgr*, *pane=None*, *id=wx.ID\_ANY*, *title=""*, *style=wx.FRAME\_TOOL\_WINDOW | wx.FRAME\_FLOAT\_ON\_PARENT | wx.FRAME\_NO\_TASKBAR | wx.CLIP\_CHILDREN*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.__init__ "Permalink to this definition")
Default class constructor. Used internally, do not call it in your code!



Parameters
* **parent** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") parent;
* **owner\_mgr** – the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") that manages the floating pane;
* **pane** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") pane that is about to float;
* **id** (*integer*) – the window identifier. It may take a value of -1 to indicate a default value.
* **title** (*string*) – the caption to be displayed on the frame’s title bar.
* **style** (*integer*) – the window style.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def CopyAttributes(self, pane: AuiPaneInfo) -> None:
        """ 

`CopyAttributes`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.CopyAttributes "Permalink to this definition")
Copies all the attributes of the input *pane* into another [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo").



Parameters
**pane** – the source [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") from where to copy attributes.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def FadeOut(self) -> None:
        """ 

`FadeOut`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.FadeOut "Permalink to this definition")
Actually starts the fading out of the floating pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def FlyOut(self) -> None:
        """ 

`FlyOut`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.FlyOut "Permalink to this definition")
Starts the flying in and out of a floating pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def GetOwnerManager(self) -> None:
        """ 

`GetOwnerManager`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.GetOwnerManager "Permalink to this definition")
Returns the [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") that manages the pane.




            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnActivate(self, event: ActivateEvent) -> None:
        """ 

`OnActivate`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnActivate "Permalink to this definition")
Handles the `wx.EVT_ACTIVATE` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `ActivateEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnCheckFlyTimer(self, event: TimerEvent) -> None:
        """ 

`OnCheckFlyTimer`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnCheckFlyTimer "Permalink to this definition")
Handles the `wx.EVT_TIMER` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `TimerEvent` to be processed.





Note


This is used solely for “fly-out” panes.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnClose(self, event: CloseEvent) -> None:
        """ 

`OnClose`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnClose "Permalink to this definition")
Handles the `wx.EVT_CLOSE` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `CloseEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnFindManager(self, event: AuiManagerEvent) -> None:
        """ 

`OnFindManager`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnFindManager "Permalink to this definition")
Handles the `EVT_AUI_FIND_MANAGER` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a [`AuiManagerEvent`](wx.lib.agw.aui.framemanager.AuiManagerEvent.html#wx.lib.agw.aui.framemanager.AuiManagerEvent "wx.lib.agw.aui.framemanager.AuiManagerEvent") event to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnFlyTimer(self, event: TimerEvent) -> None:
        """ 

`OnFlyTimer`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnFlyTimer "Permalink to this definition")
Handles the `wx.EVT_TIMER` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `TimerEvent` to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnIdle(self, event: IdleEvent) -> None:
        """ 

`OnIdle`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnIdle "Permalink to this definition")
Handles the `wx.EVT_IDLE` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `IdleEvent` event to be processed.





Note


This event is only processed on wxMAC if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMove(self, event: MoveEvent) -> None:
        """ 

`OnMove`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnMove "Permalink to this definition")
Handles the `wx.EVT_MOVE` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `MoveEvent` to be processed.





Note


This event is not processed on wxMAC or if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is not using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveEvent(self, event: MoveEvent) -> None:
        """ 

`OnMoveEvent`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnMoveEvent "Permalink to this definition")
Handles the `wx.EVT_MOVE` and `wx.EVT_MOVING` events for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a `MoveEvent` to be processed.





Note


This event is only processed on wxMAC or if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveFinished(self) -> None:
        """ 

`OnMoveFinished`(*self*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnMoveFinished "Permalink to this definition")
The user has just finished moving the floating pane.



Note


This method is used only on wxMAC if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoveStart(self, event: MouseEvent) -> None:
        """ 

`OnMoveStart`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnMoveStart "Permalink to this definition")
The user has just started moving the floating pane.



Parameters
**event** – an instance of `MouseEvent`.





Note


This event is only processed on wxMAC if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnMoving(self, rect, direction) -> None:
        """ 

`OnMoving`(*self*, *rect*, *direction*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnMoving "Permalink to this definition")
The user is moving the floating pane.



Parameters
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – the pane client rectangle;
* **direction** (*integer*) – the direction in which the pane is moving, can be one of
`wx.NORTH`, `wx.SOUTH`, `wx.EAST` or `wx.WEST`.





Note


This event is only processed on wxMAC if [`AuiManager`](wx.lib.agw.aui.framemanager.AuiManager.html#wx.lib.agw.aui.framemanager.AuiManager "wx.lib.agw.aui.framemanager.AuiManager") is using the
`AUI_MGR_USE_NATIVE_MINIFRAMES` style.





            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.OnSize "Permalink to this definition")
Handles the `wx.EVT_SIZE` event for [`AuiFloatingFrame`](#wx.lib.agw.aui.framemanager.AuiFloatingFrame "wx.lib.agw.aui.framemanager.AuiFloatingFrame").



Parameters
**event** – a [`wx.SizeEvent`](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent") to be processed.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """

    def SetPaneWindow(self, pane: AuiPaneInfo) -> None:
        """ 

`SetPaneWindow`(*self*, *pane*)[¶](#wx.lib.agw.aui.framemanager.AuiFloatingFrame.SetPaneWindow "Permalink to this definition")
Sets all the properties of a pane.



Parameters
**pane** – the [`AuiPaneInfo`](wx.lib.agw.aui.framemanager.AuiPaneInfo.html#wx.lib.agw.aui.framemanager.AuiPaneInfo "wx.lib.agw.aui.framemanager.AuiPaneInfo") to analyze.






            Source: https://docs.wxpython.org/wx.lib.agw.aui.framemanager.AuiFloatingFrame.html
        """



EVT_ACTIVATE: int

EVT_CLOSE: int

EVT_IDLE: int

EVT_MOVING: int

NORTH: int

SOUTH: int

EAST: int

WEST: int

