# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class ChildrenRepositioningGuard:
    """ **Possible constructors**:



```
ChildrenRepositioningGuard(win)

```


Helper for ensuring EndRepositioningChildren() is called correctly.


  


        Source: https://docs.wxpython.org/wx.Window.ChildrenRepositioningGuard.html
    """
    def __init__(self, win: 'Window') -> None:
        """ 

`__init__`(*self*, *win*)[¶](#wx.Window.ChildrenRepositioningGuard.__init__ "Permalink to this definition")
Constructor calls [`wx.Window.BeginRepositioningChildren`](wx.Window.html#wx.Window.BeginRepositioningChildren "wx.Window.BeginRepositioningChildren") .



Parameters
**win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window to call `BeginRepositioningChildren` on. If it is `None`, nothing is done.






            Source: https://docs.wxpython.org/wx.Window.ChildrenRepositioningGuard.html
        """



