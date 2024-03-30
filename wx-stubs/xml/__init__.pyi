# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Object, TextFileType, VersionInfo

class XmlDocument(Object):
    """ **Possible constructors**:



```
XmlDocument()

XmlDocument(doc)

XmlDocument(filename, encoding="UTF-8")

XmlDocument(stream, encoding="UTF-8")

```


This class holds `XML` data/document as parsed by `XML` parser in the root
node.


  


        Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlDocument.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, doc)*


Copy constructor.


Deep copies all the `XML` tree of the given document.



Parameters
**doc** ([*wx.xml.XmlDocument*](#wx.xml.XmlDocument "wx.xml.XmlDocument")) – 






---

  



**\_\_init\_\_** *(self, filename, encoding=”UTF-8”)*


Loads the given filename using the given encoding.


See [`Load`](#wx.xml.XmlDocument.Load "wx.xml.XmlDocument.Load") .



Parameters
* **filename** (*string*) –
* **encoding** (*string*) –






---

  



**\_\_init\_\_** *(self, stream, encoding=”UTF-8”)*


Loads the `XML` document from given stream using the given encoding.


See [`Load`](#wx.xml.XmlDocument.Load "wx.xml.XmlDocument.Load") .



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **encoding** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def AppendToProlog(self, node: 'xml.XmlNode') -> None:
        """ 

`AppendToProlog`(*self*, *node*)[¶](#wx.xml.XmlDocument.AppendToProlog "Permalink to this definition")
Appends a Process Instruction or Comment node to the document prologue.


Calling this function will create a prologue or attach the node to the end of an existing prologue.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachDocumentNode(self) -> 'XmlNode':
        """ 

`DetachDocumentNode`(*self*)[¶](#wx.xml.XmlDocument.DetachDocumentNode "Permalink to this definition")
Detaches the document node and returns it.


The document node will be set to `None` and thus [`IsOk`](#wx.xml.XmlDocument.IsOk "wx.xml.XmlDocument.IsOk") will return `False` after calling this function.


Note that the caller is responsible for deleting the returned node in order to avoid memory leaks.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def DetachRoot(self) -> 'XmlNode':
        """ 

`DetachRoot`(*self*)[¶](#wx.xml.XmlDocument.DetachRoot "Permalink to this definition")
Detaches the root entity node and returns it.


After calling this function, the document node will remain together with any prologue nodes, but [`IsOk`](#wx.xml.XmlDocument.IsOk "wx.xml.XmlDocument.IsOk") will return `False` since the root entity will be missing.


Note that the caller is responsible for deleting the returned node in order to avoid memory leaks.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDoctype(self) -> 'XmlDoctype':
        """ 

`GetDoctype`(*self*)[¶](#wx.xml.XmlDocument.GetDoctype "Permalink to this definition")
Returns the `DOCTYPE` declaration data for the document.



Return type
 [wx.xml.XmlDoctype](wx.xml.XmlDoctype.html#wx-xml-xmldoctype)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetDocumentNode(self) -> 'XmlNode':
        """ 

`GetDocumentNode`(*self*)[¶](#wx.xml.XmlDocument.GetDocumentNode "Permalink to this definition")
Returns the document node of the document.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetEOL(self) -> str:
        """ 

`GetEOL`(*self*)[¶](#wx.xml.XmlDocument.GetEOL "Permalink to this definition")
Returns the output line ending string used for documents.


This string is determined by the last call to [`SetFileType`](#wx.xml.XmlDocument.SetFileType "wx.xml.XmlDocument.SetFileType") .



Return type
`string`





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileEncoding(self) -> str:
        """ 

`GetFileEncoding`(*self*)[¶](#wx.xml.XmlDocument.GetFileEncoding "Permalink to this definition")
Returns encoding of document (may be empty).



Return type
`string`





Note


This is the encoding original file was saved in, **not** the encoding of in-memory representation!





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetFileType(self) -> 'TextFileType':
        """ 

`GetFileType`(*self*)[¶](#wx.xml.XmlDocument.GetFileType "Permalink to this definition")
Returns the output line ending format used for documents.



Return type
 [wx.TextFileType](wx.TextFileType.enumeration.html#wx-textfiletype)





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    @staticmethod
    def GetLibraryVersionInfo() -> 'VersionInfo':
        """ 

*static* `GetLibraryVersionInfo`()[¶](#wx.xml.XmlDocument.GetLibraryVersionInfo "Permalink to this definition")
Get expat library version information.



Return type
 [wx.VersionInfo](wx.VersionInfo.html#wx-versioninfo)





New in version 2.9.2.




See also


 [wx.VersionInfo](wx.VersionInfo.html#wx-versioninfo)





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetRoot(self) -> 'XmlNode':
        """ 

`GetRoot`(*self*)[¶](#wx.xml.XmlDocument.GetRoot "Permalink to this definition")
Returns the root element node of the document.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def GetVersion(self) -> str:
        """ 

`GetVersion`(*self*)[¶](#wx.xml.XmlDocument.GetVersion "Permalink to this definition")
Returns the version of document.


This is the value in the `<` ?xml version=”1.0”?> header of the `XML` document. If the version attribute was not explicitly given in the header, this function returns an empty string.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.xml.XmlDocument.IsOk "Permalink to this definition")
Returns `True` if the document has been loaded successfully.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Load(self, *args, **kw) -> bool:
        """ 

`Load`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlDocument.Load "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Load** *(self, filename, encoding=”UTF-8”, flags=XMLDOC\_NONE)*


Parses *filename* as an xml document and loads its data.


If *flags* does not contain `wx.xml.XMLDOC_KEEP_WHITESPACE_NODES`, then, while loading, all nodes of type `XML_TEXT_NODE` (see  [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)) are automatically skipped if they contain whitespaces only.


The removal of these nodes makes the load process slightly faster and requires less memory however makes impossible to recreate exactly the loaded text with a [`Save`](#wx.xml.XmlDocument.Save "wx.xml.XmlDocument.Save") call later. Read the initial description of this class for more info.


Returns `True` on success, `False` otherwise.



Parameters
* **filename** (*string*) –
* **encoding** (*string*) –
* **flags** (*int*) –



Return type
*bool*






---

  



**Load** *(self, stream, encoding=”UTF-8”, flags=XMLDOC\_NONE)*


Like [`Load`](#wx.xml.XmlDocument.Load "wx.xml.XmlDocument.Load") but takes the data from given input stream.



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **encoding** (*string*) –
* **flags** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def Save(self, *args, **kw) -> bool:
        """ 

`Save`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlDocument.Save "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Save** *(self, filename, indentstep=2)*


Saves `XML` tree creating a file named with given string.


If *indentstep* is greater than or equal to zero, then, while saving, an automatic indentation is added with steps composed by indentstep spaces.


If *indentstep* is `XML_NO_INDENTATION` , then, automatic indentation is turned off.



Parameters
* **filename** (*string*) –
* **indentstep** (*int*) –



Return type
*bool*






---

  



**Save** *(self, stream, indentstep=2)*


Saves `XML` tree in the given output stream.


See Save(const String&, int) for a description of *indentstep*.



Parameters
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –
* **indentstep** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDoctype(self, doctype: 'xml.XmlDoctype') -> None:
        """ 

`SetDoctype`(*self*, *doctype*)[¶](#wx.xml.XmlDocument.SetDoctype "Permalink to this definition")
Sets the data which will appear in the `DOCTYPE` declaration when the document is saved.



Parameters
**doctype** ([*wx.xml.XmlDoctype*](wx.xml.XmlDoctype.html#wx.xml.XmlDoctype "wx.xml.XmlDoctype")) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetDocumentNode(self, node: 'xml.XmlNode') -> None:
        """ 

`SetDocumentNode`(*self*, *node*)[¶](#wx.xml.XmlDocument.SetDocumentNode "Permalink to this definition")
Sets the document node of this document.


Deletes any previous document node. Use [`DetachDocumentNode`](#wx.xml.XmlDocument.DetachDocumentNode "wx.xml.XmlDocument.DetachDocumentNode") and then [`SetDocumentNode`](#wx.xml.XmlDocument.SetDocumentNode "wx.xml.XmlDocument.SetDocumentNode") if you want to replace the document node without deleting the old document tree.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileEncoding(self, encoding: str) -> None:
        """ 

`SetFileEncoding`(*self*, *encoding*)[¶](#wx.xml.XmlDocument.SetFileEncoding "Permalink to this definition")
Sets the encoding of the file which will be used to save the document.



Parameters
**encoding** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetFileType(self, fileType: TextFileType) -> None:
        """ 

`SetFileType`(*self*, *fileType*)[¶](#wx.xml.XmlDocument.SetFileType "Permalink to this definition")
Sets the output line ending formats when the document is saved.


By default Unix file type is used, i.e. a single `ASCII` `LF` (10) character is used at the end of lines.



Parameters
**fileType** ([*TextFileType*](wx.TextFileType.enumeration.html "TextFileType")) – 





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetRoot(self, node: 'xml.XmlNode') -> None:
        """ 

`SetRoot`(*self*, *node*)[¶](#wx.xml.XmlDocument.SetRoot "Permalink to this definition")
Sets the root element node of this document.


Will create the document node if necessary. Any previous root element node is deleted.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    def SetVersion(self, version: str) -> None:
        """ 

`SetVersion`(*self*, *version*)[¶](#wx.xml.XmlDocument.SetVersion "Permalink to this definition")
Sets the version of the `XML` file which will be used to save the document.



Parameters
**version** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlDocument.html
        """

    Doctype: 'XmlDoctype'  # `Doctype`[¶](#wx.xml.XmlDocument.Doctype "Permalink to this definition")See [`GetDoctype`](#wx.xml.XmlDocument.GetDoctype "wx.xml.XmlDocument.GetDoctype") and [`SetDoctype`](#wx.xml.XmlDocument.SetDoctype "wx.xml.XmlDocument.SetDoctype")
    DocumentNode: 'XmlNode'  # `DocumentNode`[¶](#wx.xml.XmlDocument.DocumentNode "Permalink to this definition")See [`GetDocumentNode`](#wx.xml.XmlDocument.GetDocumentNode "wx.xml.XmlDocument.GetDocumentNode") and [`SetDocumentNode`](#wx.xml.XmlDocument.SetDocumentNode "wx.xml.XmlDocument.SetDocumentNode")
    EOL: str  # `EOL`[¶](#wx.xml.XmlDocument.EOL "Permalink to this definition")See [`GetEOL`](#wx.xml.XmlDocument.GetEOL "wx.xml.XmlDocument.GetEOL")
    FileEncoding: str  # `FileEncoding`[¶](#wx.xml.XmlDocument.FileEncoding "Permalink to this definition")See [`GetFileEncoding`](#wx.xml.XmlDocument.GetFileEncoding "wx.xml.XmlDocument.GetFileEncoding") and [`SetFileEncoding`](#wx.xml.XmlDocument.SetFileEncoding "wx.xml.XmlDocument.SetFileEncoding")
    FileType: 'TextFileType'  # `FileType`[¶](#wx.xml.XmlDocument.FileType "Permalink to this definition")See [`GetFileType`](#wx.xml.XmlDocument.GetFileType "wx.xml.XmlDocument.GetFileType") and [`SetFileType`](#wx.xml.XmlDocument.SetFileType "wx.xml.XmlDocument.SetFileType")
    Root: 'XmlNode'  # `Root`[¶](#wx.xml.XmlDocument.Root "Permalink to this definition")See [`GetRoot`](#wx.xml.XmlDocument.GetRoot "wx.xml.XmlDocument.GetRoot") and [`SetRoot`](#wx.xml.XmlDocument.SetRoot "wx.xml.XmlDocument.SetRoot")
    Version: str  # `Version`[¶](#wx.xml.XmlDocument.Version "Permalink to this definition")See [`GetVersion`](#wx.xml.XmlDocument.GetVersion "wx.xml.XmlDocument.GetVersion") and [`SetVersion`](#wx.xml.XmlDocument.SetVersion "wx.xml.XmlDocument.SetVersion")



XMLDOC_KEEP_WHITESPACE_NODES: int

class XmlNode:
    """ **Possible constructors**:



```
XmlNode(parent, type, name, content="", attrs=None, next=None,
        lineNo=-1)

XmlNode(type, name, content="", lineNo=-1)

XmlNode(node)

```


Represents a node in an `XML` document.


  


        Source: https://docs.wxpython.org/wx.xml.XmlNode.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlNode.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, type, name, content=””, attrs=None, next=None, lineNo=-1)*


Creates this `XML` node and inserts it into the `XML` tree as a child of the specified parent.


Once added, the `XML` tree takes ownership of this object and there is no need to delete it.



Parameters
* **parent** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – The parent node to which append this node instance. If this argument is `None` this new node will be floating and it can be appended later to another one using the [`AddChild`](#wx.xml.XmlNode.AddChild "wx.xml.XmlNode.AddChild") or [`InsertChild`](#wx.xml.XmlNode.InsertChild "wx.xml.XmlNode.InsertChild") functions. Otherwise the child is added to the `XML` tree by this constructor and it shouldn’t be done again.
* **type** ([*XmlNodeType*](wx.xml.XmlNodeType.enumeration.html "XmlNodeType")) – One of the  [wx.xml.XmlNodeType](wx.xml.XmlNodeType.enumeration.html#wx-xml-xmlnodetype) enumeration value.
* **name** (*string*) – The name of the node. This is the string which appears between angular brackets.
* **content** (*string*) – The content of the node. Only meaningful when type is `XML_TEXT_NODE` or `XML_CDATA_SECTION_NODE` .
* **attrs** ([*wx.xml.XmlAttribute*](wx.xml.XmlAttribute.html#wx.xml.XmlAttribute "wx.xml.XmlAttribute")) – If not `None`, this  [wx.xml.XmlAttribute](wx.xml.XmlAttribute.html#wx-xml-xmlattribute) object and its eventual siblings are attached to the node.
* **next** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – If not `None`, this node and its eventual siblings are attached to the node.
* **lineNo** (*int*) – Number of line this node was present at in input file or -1.






---

  



**\_\_init\_\_** *(self, type, name, content=””, lineNo=-1)*


A simplified version of the first constructor form, assuming a `None` parent.



Parameters
* **type** ([*XmlNodeType*](wx.xml.XmlNodeType.enumeration.html "XmlNodeType")) – One of the  [wx.xml.XmlNodeType](wx.xml.XmlNodeType.enumeration.html#wx-xml-xmlnodetype) enumeration value.
* **name** (*string*) – The name of the node. This is the string which appears between angular brackets.
* **content** (*string*) – The content of the node. Only meaningful when type is `XML_TEXT_NODE` or `XML_CDATA_SECTION_NODE` .
* **lineNo** (*int*) – Number of line this node was present at in input file or -1.






---

  



**\_\_init\_\_** *(self, node)*


Copy constructor.


Note that this does NOT copy siblings and parent pointer, i.e. [`GetParent`](#wx.xml.XmlNode.GetParent "wx.xml.XmlNode.GetParent") and [`GetNext`](#wx.xml.XmlNode.GetNext "wx.xml.XmlNode.GetNext") will return `None` after using copy constructor and are never unmodified by `operator=` . On the other hand, it DOES copy children and attributes.



Parameters
**node** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddAttribute(self, *args, **kw) -> None:
        """ 

`AddAttribute`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlNode.AddAttribute "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddAttribute** *(self, name, value)*


Appends an attribute with given *name* and *value* to the list of attributes for this node.



Parameters
* **name** (*string*) –
* **value** (*string*) –






---

  



**AddAttribute** *(self, attr)*


Appends given attribute to the list of attributes for this node.



Parameters
**attr** ([*wx.xml.XmlAttribute*](wx.xml.XmlAttribute.html#wx.xml.XmlAttribute "wx.xml.XmlAttribute")) – 






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def AddChild(self, child: 'xml.XmlNode') -> None:
        """ 

`AddChild`(*self*, *child*)[¶](#wx.xml.XmlNode.AddChild "Permalink to this definition")
Adds node *child* as the last child of this node.


Once added, the `XML` tree takes ownership of this object and there is no need to delete it.



Parameters
**child** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 





Note


Note that this function works in O(n) time where *n* is the number of existing children. Consequently, adding large number of child nodes using this method can be expensive, because it has O(n^2) time complexity in number of nodes to be added. Use [`InsertChildAfter`](#wx.xml.XmlNode.InsertChildAfter "wx.xml.XmlNode.InsertChildAfter") to populate `XML` tree in linear time.




See also


[`InsertChild`](#wx.xml.XmlNode.InsertChild "wx.xml.XmlNode.InsertChild") , [`InsertChildAfter`](#wx.xml.XmlNode.InsertChildAfter "wx.xml.XmlNode.InsertChildAfter")





            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def DeleteAttribute(self, name: str) -> bool:
        """ 

`DeleteAttribute`(*self*, *name*)[¶](#wx.xml.XmlNode.DeleteAttribute "Permalink to this definition")
Removes the first attributes which has the given *name* from the list of attributes for this node.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttribute(self, attrName, defaultVal="") -> str:
        """ 

`GetAttribute`(*self*, *attrName*, *defaultVal=""*)[¶](#wx.xml.XmlNode.GetAttribute "Permalink to this definition")
Returns the value of the attribute named *attrName* if it does exist.


If it does not exist, the *defaultVal* is returned.



Parameters
* **attrName** (*string*) –
* **defaultVal** (*string*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetAttributes(self) -> 'XmlAttribute':
        """ 

`GetAttributes`(*self*)[¶](#wx.xml.XmlNode.GetAttributes "Permalink to this definition")
Return a pointer to the first attribute of this node.



Return type
 [wx.xml.XmlAttribute](wx.xml.XmlAttribute.html#wx-xml-xmlattribute)






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetChildren(self) -> 'XmlNode':
        """ 

`GetChildren`(*self*)[¶](#wx.xml.XmlNode.GetChildren "Permalink to this definition")
Returns the first child of this node.


To get a pointer to the second child of this node (if it does exist), use the [`GetNext`](#wx.xml.XmlNode.GetNext "wx.xml.XmlNode.GetNext") function on the returned value.



Return type
 [wx.xml.XmlNode](#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetContent(self) -> str:
        """ 

`GetContent`(*self*)[¶](#wx.xml.XmlNode.GetContent "Permalink to this definition")
Returns the content of this node.


Can be an empty string. Be aware that for nodes of type `XML_ELEMENT_NODE` (the most used node type) the content is an empty string. See [`GetNodeContent`](#wx.xml.XmlNode.GetNodeContent "wx.xml.XmlNode.GetNodeContent") for more details.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetDepth(self, grandparent: Optional['xml.XmlNode']=None) -> int:
        """ 

`GetDepth`(*self*, *grandparent=None*)[¶](#wx.xml.XmlNode.GetDepth "Permalink to this definition")
Returns the number of nodes which separate this node from `grandparent` .


This function searches only the parents of this node until it finds *grandparent* or the `None` node (which is the parent of non-linked nodes or the parent of a  [wx.xml.XmlDocument](wx.xml.XmlDocument.html#wx-xml-xmldocument)’s root element node).



Parameters
**grandparent** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetLineNumber(self) -> int:
        """ 

`GetLineNumber`(*self*)[¶](#wx.xml.XmlNode.GetLineNumber "Permalink to this definition")
Returns line number of the node in the input `XML` file or `-1` if it is unknown.



Return type
*int*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.xml.XmlNode.GetName "Permalink to this definition")
Returns the name of this node.


Can be an empty string (e.g. for nodes of type `XML_TEXT_NODE` or `XML_CDATA_SECTION_NODE` ).



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNext(self) -> 'XmlNode':
        """ 

`GetNext`(*self*)[¶](#wx.xml.XmlNode.GetNext "Permalink to this definition")
Returns a pointer to the sibling of this node or `None` if there are no siblings.



Return type
 [wx.xml.XmlNode](#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNoConversion(self) -> bool:
        """ 

`GetNoConversion`(*self*)[¶](#wx.xml.XmlNode.GetNoConversion "Permalink to this definition")
Returns a flag indicating whether encoding conversion is necessary when saving.


The default is `False`.


You can improve saving efficiency considerably by setting this value.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetNodeContent(self) -> str:
        """ 

`GetNodeContent`(*self*)[¶](#wx.xml.XmlNode.GetNodeContent "Permalink to this definition")
Returns the content of the first child node of type `XML_TEXT_NODE` or `XML_CDATA_SECTION_NODE` .


This function is very useful since the `XML` snippet `"tagnametagcontent/tagname"` is represented by expat with the following tag tree:



```
XML_ELEMENT_NODE name="tagname", content=""
|-- XML_TEXT_NODE name="", content="tagcontent"

```


or eventually:



```
XML_ELEMENT_NODE name="tagname", content=""
|-- XML_CDATA_SECTION_NODE name="", content="tagcontent"

```


An empty string is returned if the node has no children of type `XML_TEXT_NODE` or `XML_CDATA_SECTION_NODE` , or if the content of the first child of such types is empty.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetParent(self) -> 'XmlNode':
        """ 

`GetParent`(*self*)[¶](#wx.xml.XmlNode.GetParent "Permalink to this definition")
Returns a pointer to the parent of this node or `None` if this node has no parent.



Return type
 [wx.xml.XmlNode](#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def GetType(self) -> 'XmlNodeType':
        """ 

`GetType`(*self*)[¶](#wx.xml.XmlNode.GetType "Permalink to this definition")
Returns the type of this node.



Return type
 [wx.xml.XmlNodeType](wx.xml.XmlNodeType.enumeration.html#wx-xml-xmlnodetype)






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def HasAttribute(self, attrName: str) -> bool:
        """ 

`HasAttribute`(*self*, *attrName*)[¶](#wx.xml.XmlNode.HasAttribute "Permalink to this definition")
Returns `True` if this node has a attribute named *attrName*.



Parameters
**attrName** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChild(self, child, followingNode) -> bool:
        """ 

`InsertChild`(*self*, *child*, *followingNode*)[¶](#wx.xml.XmlNode.InsertChild "Permalink to this definition")
Inserts the *child* node immediately before *followingNode* in the children list.


Once inserted, the `XML` tree takes ownership of the new child and there is no need to delete it.



Parameters
* **child** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **followingNode** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) –



Return type
*bool*



Returns
`True` if *followingNode* has been found and the *child* node has been inserted.





Note


For historical reasons, *followingNode* may be `None`. In that case, then *child* is prepended to the list of children and becomes the first child of this node, i.e. it behaves identically to using the first children (as returned by [`GetChildren`](#wx.xml.XmlNode.GetChildren "wx.xml.XmlNode.GetChildren") ) for *followingNode*).




See also


[`AddChild`](#wx.xml.XmlNode.AddChild "wx.xml.XmlNode.AddChild") , [`InsertChildAfter`](#wx.xml.XmlNode.InsertChildAfter "wx.xml.XmlNode.InsertChildAfter")





            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def InsertChildAfter(self, child, precedingNode) -> bool:
        """ 

`InsertChildAfter`(*self*, *child*, *precedingNode*)[¶](#wx.xml.XmlNode.InsertChildAfter "Permalink to this definition")
Inserts the *child* node immediately after *precedingNode* in the children list.


Once inserted, the `XML` tree takes ownership of the new child and there is no need to delete it.



Parameters
* **child** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – The child to insert.
* **precedingNode** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – The node to insert *child* after. As a special case, this can be `None` if this node has no children yet – in that case, *child* will become this node’s only child node.



Return type
*bool*



Returns
`True` if *precedingNode* has been found and the *child* node has been inserted.





New in version 2.8.8.




See also


[`InsertChild`](#wx.xml.XmlNode.InsertChild "wx.xml.XmlNode.InsertChild") , [`AddChild`](#wx.xml.XmlNode.AddChild "wx.xml.XmlNode.AddChild")





            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def IsWhitespaceOnly(self) -> bool:
        """ 

`IsWhitespaceOnly`(*self*)[¶](#wx.xml.XmlNode.IsWhitespaceOnly "Permalink to this definition")
Returns `True` if the content of this node is a string containing only whitespaces (spaces, tabs, new lines, etc).


Note that this function is locale-independent since the parsing of `XML` documents must always produce the exact same tree regardless of the locale it runs under.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def RemoveChild(self, child: 'xml.XmlNode') -> bool:
        """ 

`RemoveChild`(*self*, *child*)[¶](#wx.xml.XmlNode.RemoveChild "Permalink to this definition")
Removes the given node from the children list.


Returns `True` if the node was found and removed or `False` if the node could not be found. Note that the caller is responsible for deleting the removed node in order to avoid memory leaks.



Parameters
**child** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetContent(self, con: str) -> None:
        """ 

`SetContent`(*self*, *con*)[¶](#wx.xml.XmlNode.SetContent "Permalink to this definition")
Sets the content of this node.



Parameters
**con** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.xml.XmlNode.SetName "Permalink to this definition")
Sets the name of this node.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNext(self, next: 'xml.XmlNode') -> None:
        """ 

`SetNext`(*self*, *next*)[¶](#wx.xml.XmlNode.SetNext "Permalink to this definition")
Sets as sibling the given node.


The caller is responsible for deleting any previously present sibling node.



Parameters
**next** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetNoConversion(self, noconversion: bool) -> None:
        """ 

`SetNoConversion`(*self*, *noconversion*)[¶](#wx.xml.XmlNode.SetNoConversion "Permalink to this definition")
Sets a flag to indicate whether encoding conversion is necessary when saving.


The default is `False`.


You can improve saving efficiency considerably by setting this value.



Parameters
**noconversion** (*bool*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetParent(self, parent: 'xml.XmlNode') -> None:
        """ 

`SetParent`(*self*, *parent*)[¶](#wx.xml.XmlNode.SetParent "Permalink to this definition")
Sets as parent the given node.


The caller is responsible for deleting any previously present parent node.



Parameters
**parent** ([*wx.xml.XmlNode*](#wx.xml.XmlNode "wx.xml.XmlNode")) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    def SetType(self, type: XmlNodeType) -> None:
        """ 

`SetType`(*self*, *type*)[¶](#wx.xml.XmlNode.SetType "Permalink to this definition")
Sets the type of this node.



Parameters
**type** ([*XmlNodeType*](wx.xml.XmlNodeType.enumeration.html "XmlNodeType")) – 






            Source: https://docs.wxpython.org/wx.xml.XmlNode.html
        """

    Attributes: 'XmlAttribute'  # `Attributes`[¶](#wx.xml.XmlNode.Attributes "Permalink to this definition")See [`GetAttributes`](#wx.xml.XmlNode.GetAttributes "wx.xml.XmlNode.GetAttributes")
    Children: 'XmlNode'  # `Children`[¶](#wx.xml.XmlNode.Children "Permalink to this definition")See [`GetChildren`](#wx.xml.XmlNode.GetChildren "wx.xml.XmlNode.GetChildren")
    Content: str  # `Content`[¶](#wx.xml.XmlNode.Content "Permalink to this definition")See [`GetContent`](#wx.xml.XmlNode.GetContent "wx.xml.XmlNode.GetContent") and [`SetContent`](#wx.xml.XmlNode.SetContent "wx.xml.XmlNode.SetContent")
    Depth: int  # `Depth`[¶](#wx.xml.XmlNode.Depth "Permalink to this definition")See [`GetDepth`](#wx.xml.XmlNode.GetDepth "wx.xml.XmlNode.GetDepth")
    LineNumber: int  # `LineNumber`[¶](#wx.xml.XmlNode.LineNumber "Permalink to this definition")See [`GetLineNumber`](#wx.xml.XmlNode.GetLineNumber "wx.xml.XmlNode.GetLineNumber")
    Name: str  # `Name`[¶](#wx.xml.XmlNode.Name "Permalink to this definition")See [`GetName`](#wx.xml.XmlNode.GetName "wx.xml.XmlNode.GetName") and [`SetName`](#wx.xml.XmlNode.SetName "wx.xml.XmlNode.SetName")
    Next: 'XmlNode'  # `Next`[¶](#wx.xml.XmlNode.Next "Permalink to this definition")See [`GetNext`](#wx.xml.XmlNode.GetNext "wx.xml.XmlNode.GetNext") and [`SetNext`](#wx.xml.XmlNode.SetNext "wx.xml.XmlNode.SetNext")
    NoConversion: bool  # `NoConversion`[¶](#wx.xml.XmlNode.NoConversion "Permalink to this definition")See [`GetNoConversion`](#wx.xml.XmlNode.GetNoConversion "wx.xml.XmlNode.GetNoConversion") and [`SetNoConversion`](#wx.xml.XmlNode.SetNoConversion "wx.xml.XmlNode.SetNoConversion")
    NodeContent: str  # `NodeContent`[¶](#wx.xml.XmlNode.NodeContent "Permalink to this definition")See [`GetNodeContent`](#wx.xml.XmlNode.GetNodeContent "wx.xml.XmlNode.GetNodeContent")
    Parent: 'XmlNode'  # `Parent`[¶](#wx.xml.XmlNode.Parent "Permalink to this definition")See [`GetParent`](#wx.xml.XmlNode.GetParent "wx.xml.XmlNode.GetParent") and [`SetParent`](#wx.xml.XmlNode.SetParent "wx.xml.XmlNode.SetParent")
    Type: 'XmlNodeType'  # `Type`[¶](#wx.xml.XmlNode.Type "Permalink to this definition")See [`GetType`](#wx.xml.XmlNode.GetType "wx.xml.XmlNode.GetType") and [`SetType`](#wx.xml.XmlNode.SetType "wx.xml.XmlNode.SetType")



class XmlAttribute:
    """ **Possible constructors**:



```
XmlAttribute()

XmlAttribute(name, value, next=None)

```


Represents a node attribute.


  


        Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xml.XmlAttribute.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, name, value, next=None)*


Creates the attribute with given *name* and *value*.


If *next* is not `None`, then sets it as sibling of this attribute.



Parameters
* **name** (*string*) –
* **value** (*string*) –
* **next** ([*wx.xml.XmlAttribute*](#wx.xml.XmlAttribute "wx.xml.XmlAttribute")) –






---

  





            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.xml.XmlAttribute.GetName "Permalink to this definition")
Returns the name of this attribute.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetNext(self) -> 'XmlAttribute':
        """ 

`GetNext`(*self*)[¶](#wx.xml.XmlAttribute.GetNext "Permalink to this definition")
Returns the sibling of this attribute or `None` if there are no siblings.



Return type
 [wx.xml.XmlAttribute](#wx-xml-xmlattribute)






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def GetValue(self) -> str:
        """ 

`GetValue`(*self*)[¶](#wx.xml.XmlAttribute.GetValue "Permalink to this definition")
Returns the value of this attribute.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.xml.XmlAttribute.SetName "Permalink to this definition")
Sets the name of this attribute.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetNext(self, next: 'xml.XmlAttribute') -> None:
        """ 

`SetNext`(*self*, *next*)[¶](#wx.xml.XmlAttribute.SetNext "Permalink to this definition")
Sets the sibling of this attribute.



Parameters
**next** ([*wx.xml.XmlAttribute*](#wx.xml.XmlAttribute "wx.xml.XmlAttribute")) – 






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    def SetValue(self, value: str) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.xml.XmlAttribute.SetValue "Permalink to this definition")
Sets the value of this attribute.



Parameters
**value** (*string*) – 






            Source: https://docs.wxpython.org/wx.xml.XmlAttribute.html
        """

    Name: str  # `Name`[¶](#wx.xml.XmlAttribute.Name "Permalink to this definition")See [`GetName`](#wx.xml.XmlAttribute.GetName "wx.xml.XmlAttribute.GetName") and [`SetName`](#wx.xml.XmlAttribute.SetName "wx.xml.XmlAttribute.SetName")
    Next: 'XmlAttribute'  # `Next`[¶](#wx.xml.XmlAttribute.Next "Permalink to this definition")See [`GetNext`](#wx.xml.XmlAttribute.GetNext "wx.xml.XmlAttribute.GetNext") and [`SetNext`](#wx.xml.XmlAttribute.SetNext "wx.xml.XmlAttribute.SetNext")
    Value: str  # `Value`[¶](#wx.xml.XmlAttribute.Value "Permalink to this definition")See [`GetValue`](#wx.xml.XmlAttribute.GetValue "wx.xml.XmlAttribute.GetValue") and [`SetValue`](#wx.xml.XmlAttribute.SetValue "wx.xml.XmlAttribute.SetValue")



class XmlDoctype:
    """ **Possible constructors**:



```
XmlDoctype(rootName="", systemId="", publicId="")

```


Represents a `DOCTYPE` Declaration.


  


        Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
    """
    def __init__(self, rootName="", systemId="", publicId="") -> None:
        """ 

`__init__`(*self*, *rootName=""*, *systemId=""*, *publicId=""*)[¶](#wx.xml.XmlDoctype.__init__ "Permalink to this definition")
Creates and possible initializes the `DOCTYPE`.



Parameters
* **rootName** (*string*) – The root name.
* **systemId** (*string*) – The system identifier.
* **publicId** (*string*) – The public identifier.






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.xml.XmlDoctype.Clear "Permalink to this definition")
Removes all the `DOCTYPE` values.




            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetFullString(self) -> str:
        """ 

`GetFullString`(*self*)[¶](#wx.xml.XmlDoctype.GetFullString "Permalink to this definition")
Returns the formatted `DOCTYPE` contents.


This consists of all the text shown between the opening “<!``DOCTYPE`` ” and closing “>” of a `DOCTYPE` declaration.


If this object is empty or invalid, i.e. [`IsValid`](#wx.xml.XmlDoctype.IsValid "wx.xml.XmlDoctype.IsValid") returns `False`, this method returns an empty string.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetPublicId(self) -> str:
        """ 

`GetPublicId`(*self*)[¶](#wx.xml.XmlDoctype.GetPublicId "Permalink to this definition")
Returns the public id of the document.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetRootName(self) -> str:
        """ 

`GetRootName`(*self*)[¶](#wx.xml.XmlDoctype.GetRootName "Permalink to this definition")
Returns the root name of the document.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def GetSystemId(self) -> str:
        """ 

`GetSystemId`(*self*)[¶](#wx.xml.XmlDoctype.GetSystemId "Permalink to this definition")
Returns the system id of the document.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.xml.XmlDoctype.IsValid "Permalink to this definition")
Returns `True` if the contents can produce a valid `DOCTYPE` string.


For an object to be valid, it must have a non-empty root name and a valid system identifier (currently the validity checks of the latter are limited to checking that it doesn’t contain both single and float quotes).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xml.XmlDoctype.html
        """

    FullString: str  # `FullString`[¶](#wx.xml.XmlDoctype.FullString "Permalink to this definition")See [`GetFullString`](#wx.xml.XmlDoctype.GetFullString "wx.xml.XmlDoctype.GetFullString")
    PublicId: str  # `PublicId`[¶](#wx.xml.XmlDoctype.PublicId "Permalink to this definition")See [`GetPublicId`](#wx.xml.XmlDoctype.GetPublicId "wx.xml.XmlDoctype.GetPublicId")
    RootName: str  # `RootName`[¶](#wx.xml.XmlDoctype.RootName "Permalink to this definition")See [`GetRootName`](#wx.xml.XmlDoctype.GetRootName "wx.xml.XmlDoctype.GetRootName")
    SystemId: str  # `SystemId`[¶](#wx.xml.XmlDoctype.SystemId "Permalink to this definition")See [`GetSystemId`](#wx.xml.XmlDoctype.GetSystemId "wx.xml.XmlDoctype.GetSystemId")



XmlNodeType: TypeAlias = int  # Enumeration

XML_ELEMENT_NODE: int

XML_ATTRIBUTE_NODE: int

XML_TEXT_NODE: int

XML_CDATA_SECTION_NODE: int

XML_ENTITY_REF_NODE: int

XML_ENTITY_NODE: int

XML_PI_NODE: int

XML_COMMENT_NODE: int

XML_DOCUMENT_NODE: int

XML_DOCUMENT_TYPE_NODE: int

XML_DOCUMENT_FRAG_NODE: int

XML_NOTATION_NODE: int

XML_HTML_DOCUMENT_NODE: int

