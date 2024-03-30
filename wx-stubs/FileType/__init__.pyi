# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class MessageParameters:
    """ **Possible constructors**:



```
MessageParameters()

MessageParameters(filename, mimetype="")

```


Class representing message parameters.


  


        Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.FileType.MessageParameters.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Trivial default constructor.




---

  



**\_\_init\_\_** *(self, filename, mimetype=””)*


Constructor taking a filename and a mime type.



Parameters
* **filename** (*string*) –
* **mimetype** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetFileName(self) -> str:
        """ 

`GetFileName`(*self*)[¶](#wx.FileType.MessageParameters.GetFileName "Permalink to this definition")
Return the filename.



Return type
`string`






            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetMimeType(self) -> str:
        """ 

`GetMimeType`(*self*)[¶](#wx.FileType.MessageParameters.GetMimeType "Permalink to this definition")
Return the MIME type.



Return type
`string`






            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    def GetParamValue(self, name: str) -> str:
        """ 

`GetParamValue`(*self*, *name*)[¶](#wx.FileType.MessageParameters.GetParamValue "Permalink to this definition")
Overridable method for derived classes. Returns empty string by default.



Parameters
**name** (*string*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.FileType.MessageParameters.html
        """

    FileName: str  # `FileName`[¶](#wx.FileType.MessageParameters.FileName "Permalink to this definition")See [`GetFileName`](#wx.FileType.MessageParameters.GetFileName "wx.FileType.MessageParameters.GetFileName")
    MimeType: str  # `MimeType`[¶](#wx.FileType.MessageParameters.MimeType "Permalink to this definition")See [`GetMimeType`](#wx.FileType.MessageParameters.GetMimeType "wx.FileType.MessageParameters.GetMimeType")



