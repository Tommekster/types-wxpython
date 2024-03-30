# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class wxpTagHandler(Object):
    """ HtmlWinTagHandler()


This is basically wxHtmlTagHandler except that it is extended with
protected member m\_WParser pointing to the wxHtmlWinParser object
(value of this member is identical to wxHtmlParser’s m\_Parser).


  


        Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.lib.wxpTag.wxpTagHandler.__init__ "Permalink to this definition")
Initialize self. See help(type(self)) for accurate signature.




            Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
        """

    def GetSupportedTags(self) -> None:
        """ 

`GetSupportedTags`(*self*)[¶](#wx.lib.wxpTag.wxpTagHandler.GetSupportedTags "Permalink to this definition")
GetSupportedTags() -> String


Returns list of supported tags.




            Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
        """

    def HandleParamTag(self, tag) -> None:
        """ 

`HandleParamTag`(*self*, *tag*)[¶](#wx.lib.wxpTag.wxpTagHandler.HandleParamTag "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
        """

    def HandleTag(self, tag) -> None:
        """ 

`HandleTag`(*self*, *tag*)[¶](#wx.lib.wxpTag.wxpTagHandler.HandleTag "Permalink to this definition")
HandleTag(tag) -> bool


This is the core method of each handler.




            Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
        """

    def HandleWxpTag(self, tag) -> None:
        """ 

`HandleWxpTag`(*self*, *tag*)[¶](#wx.lib.wxpTag.wxpTagHandler.HandleWxpTag "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.lib.wxpTag.wxpTagHandler.html
        """



