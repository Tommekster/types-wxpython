# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class ScrolledPanel(ScrolledWindow):
    """ [`ScrolledPanel`](#wx.lib.scrolledpanel.ScrolledPanel "wx.lib.scrolledpanel.ScrolledPanel") fills a “hole” in the implementation of
`ScrolledWindow`, providing automatic scrollbar and scrolling
behavior and the tab traversal management that `ScrolledWindow` lacks.


  


        Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
    """
    def __init__(self, parent, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name="scrolledpanel") -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *pos=wx.DefaultPosition*, *size=wx.DefaultSize*, *style=wx.TAB\_TRAVERSAL*, *name="scrolledpanel"*)[¶](#wx.lib.scrolledpanel.ScrolledPanel.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the underlying [`wx.ScrolledWindow`](wx.ScrolledWindow.html#wx.ScrolledWindow "wx.ScrolledWindow") style;
* **name** (*string*) – the scrolled panel name.






            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def OnChildFocus(self, evt: ChildFocusEvent) -> None:
        """ 

`OnChildFocus`(*self*, *evt*)[¶](#wx.lib.scrolledpanel.ScrolledPanel.OnChildFocus "Permalink to this definition")
If the child window that gets the focus is not fully visible,
this handler will try to scroll enough to see it.



Parameters
**evt** – a `ChildFocusEvent` event to be processed.






            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def ScrollChildIntoView(self, child: 'Window') -> None:
        """ 

`ScrollChildIntoView`(*self*, *child*)[¶](#wx.lib.scrolledpanel.ScrolledPanel.ScrollChildIntoView "Permalink to this definition")
Scroll the panel so that the specified child window is in view.



Parameters
**child** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – any [`wx.Window`](wx.Window.html#wx.Window "wx.Window") - derived control.





Note


This method looks redundant if *evt.Skip()* is
called as well - the base `ScrolledWindow` widget now seems
to be doing the same thing anyway.





            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """

    def SetupScrolling(self, scroll_x=True, scroll_y=True, rate_x=20, rate_y=20, scrollToTop=True, scrollIntoView=True) -> None:
        """ 

`SetupScrolling`(*self*, *scroll\_x=True*, *scroll\_y=True*, *rate\_x=20*, *rate\_y=20*, *scrollToTop=True*, *scrollIntoView=True*)[¶](#wx.lib.scrolledpanel.ScrolledPanel.SetupScrolling "Permalink to this definition")
This function sets up the event handling necessary to handle
scrolling properly. It should be called within the [`__init__`](#wx.lib.scrolledpanel.ScrolledPanel.__init__ "wx.lib.scrolledpanel.ScrolledPanel.__init__")
function of any class that is derived from [`ScrolledPanel`](#wx.lib.scrolledpanel.ScrolledPanel "wx.lib.scrolledpanel.ScrolledPanel"),
once the controls on the panel have been constructed and
thus the size of the scrolling area can be determined.



Parameters
* **scroll\_x** (*bool*) – `True` to allow horizontal scrolling, `False` otherwise;
* **scroll\_y** (*bool*) – `True` to allow vertical scrolling, `False` otherwise;
* **rate\_x** (*int*) – the horizontal scroll increment;
* **rate\_y** (*int*) – the vertical scroll increment;
* **scrollToTop** (*bool*) – `True` to scroll all way to the top, `False` otherwise;
* **scrollIntoView** (*bool*) – `True` to scroll a focused child into view, `False` otherwise.






            Source: https://docs.wxpython.org/wx.lib.scrolledpanel.ScrolledPanel.html
        """



