# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Object, Bitmap, Dialog, Frame, Icon, Menu, MenuBar, Window, Panel, ToolBar, _Bitmap, _BitmapBundle, FileSystem, _Font, _Icon, _ImageList, Point, _Size, BitmapBundle, Colour, Coord, Font, IconBundle, ImageList, Size

class XmlResource(Object):
    """ **Possible constructors**:



```
XmlResource(filemask, flags=XRC_USE_LOCALE, domain="")

XmlResource(flags=XRC_USE_LOCALE, domain="")

```


This is the main class for interacting with the XML-based resource
system.


  


        Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, filemask, flags=XRC\_USE\_LOCALE, domain=””)*


Constructor.



Parameters
* **filemask** (*string*) – The `XRC` file, archive file, or wildcard specification that will be used to load all resource files inside a zip archive.
* **flags** (*int*) – One or more value of the  [wx.xrc.XmlResourceFlags](wx.xrc.XmlResourceFlags.enumeration.html#wx-xrc-xmlresourceflags) enumeration.
* **domain** (*string*) – The name of the gettext catalog to search for translatable strings. By default all loaded catalogs will be searched. This provides a way to allow the strings to only come from a specific catalog.






---

  



**\_\_init\_\_** *(self, flags=XRC\_USE\_LOCALE, domain=””)*


Constructor.



Parameters
* **flags** (*int*) – One or more value of the  [wx.xrc.XmlResourceFlags](wx.xrc.XmlResourceFlags.enumeration.html#wx-xrc-xmlresourceflags) enumeration.
* **domain** (*string*) – The name of the gettext catalog to search for translatable strings. By default all loaded catalogs will be searched. This provides a way to allow the strings to only come from a specific catalog.






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AddHandler(self, handler: 'xrc.XmlResourceHandler') -> None:
        """ 

`AddHandler`(*self*, *handler*)[¶](#wx.xrc.XmlResource.AddHandler "Permalink to this definition")
Initializes only a specific handler (or custom handler).


Convention says that the handler name is equal to the control’s name plus ‘XmlHandler’, for example TextCtrlXmlHandler, HtmlWindowXmlHandler.


The `XML` resource compiler (wxxrc) can create include file that contains initialization code for all controls used within the resource. Note that this handler must be allocated on the heap, since it will be deleted by [`ClearHandlers`](#wx.xrc.XmlResource.ClearHandlers "wx.xrc.XmlResource.ClearHandlers") later.



Parameters
**handler** ([*wx.xrc.XmlResourceHandler*](wx.xrc.XmlResourceHandler.html#wx.xrc.XmlResourceHandler "wx.xrc.XmlResourceHandler")) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def AddSubclassFactory(factory: 'xrc.XmlSubclassFactory') -> None:
        """ 

*static* `AddSubclassFactory`(*factory*)[¶](#wx.xrc.XmlResource.AddSubclassFactory "Permalink to this definition")
Registers subclasses factory for use in `XRC`.


This is useful only for language bindings developers who need a way to implement subclassing in wxWidgets ports that don’t support `RTTI` (e.g. wxPython).



Parameters
**factory** ([*wx.xrc.XmlSubclassFactory*](wx.xrc.XmlSubclassFactory.html#wx.xrc.XmlSubclassFactory "wx.xrc.XmlSubclassFactory")) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def AttachUnknownControl(self, name, control, parent=None) -> bool:
        """ 

`AttachUnknownControl`(*self*, *name*, *control*, *parent=None*)[¶](#wx.xrc.XmlResource.AttachUnknownControl "Permalink to this definition")
Attaches an unknown control to the given panel/window/dialog.


Unknown controls are used in conjunction with <object class=”unknown”>.



Parameters
* **name** (*string*) –
* **control** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def ClearHandlers(self) -> None:
        """ 

`ClearHandlers`(*self*)[¶](#wx.xrc.XmlResource.ClearHandlers "Permalink to this definition")
Removes all handlers and deletes them (this means that any handlers added using [`AddHandler`](#wx.xrc.XmlResource.AddHandler "wx.xrc.XmlResource.AddHandler") must be allocated on the heap).




            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def CompareVersion(self, major, minor, release, revision) -> int:
        """ 

`CompareVersion`(*self*, *major*, *minor*, *release*, *revision*)[¶](#wx.xrc.XmlResource.CompareVersion "Permalink to this definition")
Compares the `XRC` version to the argument.


Returns -1 if the `XRC` version is less than the argument, +1 if greater, and 0 if they are equal.



Parameters
* **major** (*int*) –
* **minor** (*int*) –
* **release** (*int*) –
* **revision** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def FindXRCIDById(numId: int) -> str:
        """ 

*static* `FindXRCIDById`(*numId*)[¶](#wx.xrc.XmlResource.FindXRCIDById "Permalink to this definition")
Returns a string `ID` corresponding to the given numeric `ID`.


The string returned is such that calling [`GetXRCID`](#wx.xrc.XmlResource.GetXRCID "wx.xrc.XmlResource.GetXRCID") with it as parameter yields *numId*. If there is no string identifier corresponding to the given numeric one, an empty string is returned.


Notice that, unlike [`GetXRCID`](#wx.xrc.XmlResource.GetXRCID "wx.xrc.XmlResource.GetXRCID") , this function is slow as it checks all of the identifiers used in `XRC`.



Parameters
**numId** (*int*) – 



Return type
`string`





New in version 2.9.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Get() -> 'XmlResource':
        """ 

*static* `Get`()[¶](#wx.xrc.XmlResource.Get "Permalink to this definition")
Gets the global resources object or creates one if none exists.



Return type
 [wx.xrc.XmlResource](#wx-xrc-xmlresource)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetDomain(self) -> str:
        """ 

`GetDomain`(*self*)[¶](#wx.xrc.XmlResource.GetDomain "Permalink to this definition")
Returns the domain (message catalog) that will be used to load translatable strings in the `XRC`.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.xrc.XmlResource.GetFlags "Permalink to this definition")
Returns flags, which may be a bitlist of  [wx.xrc.XmlResourceFlags](wx.xrc.XmlResourceFlags.enumeration.html#wx-xrc-xmlresourceflags) enumeration values.



Return type
*int*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetResourceNode(self, name: str) -> 'XmlNode':
        """ 

`GetResourceNode`(*self*, *name*)[¶](#wx.xrc.XmlResource.GetResourceNode "Permalink to this definition")
Returns the  [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode) containing the definition of the object with the given name or `None`.


This function recursively searches all the loaded `XRC` files for an object with the specified *name*. If the object is found, the  [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode) corresponding to it is returned, so this function can be used to access additional information defined in the `XRC` file and not used by  [wx.xrc.XmlResource](#wx-xrc-xmlresource) itself, e.g. contents of application-specific `XML` tags.



Parameters
**name** (*string*) – The name of the resource which must be unique for this function to work correctly, if there is more than one resource with the given name the choice of the one returned by this function is undefined.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)



Returns
The node corresponding to the resource with the given name or `None`.






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def GetVersion(self) -> int:
        """ 

`GetVersion`(*self*)[¶](#wx.xrc.XmlResource.GetVersion "Permalink to this definition")
Returns version information (a.b.c.d = d + 256c + 2562b + 2563a).



Return type
*long*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def GetXRCID(str_id, value_if_not_found=ID_NONE) -> int:
        """ 

*static* `GetXRCID`(*str\_id*, *value\_if\_not\_found=ID\_NONE*)[¶](#wx.xrc.XmlResource.GetXRCID "Permalink to this definition")
Returns a numeric `ID` that is equivalent to the string `ID` used in an `XML` resource.


If an unknown *str\_id* is requested (i.e. other than `ID_XXX` or integer), a new record is created which associates the given string with a number.


If *value\_if\_not\_found* is `ID_NONE` , the number is obtained via [`wx.NewId`](wx.functions.html#wx.NewId "wx.NewId") . Otherwise *value\_if\_not\_found* is used.


Macro `XRCID(name)` is provided for convenient use in event tables.



Parameters
* **str\_id** (*string*) –
* **value\_if\_not\_found** (*int*) –



Return type
*int*





Note


IDs returned by XRCID() cannot be used with the `EVT_*_RANGE` macros, because the order in which they are assigned to symbolic *name* values is not guaranteed.





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InitAllHandlers(self) -> None:
        """ 

`InitAllHandlers`(*self*)[¶](#wx.xrc.XmlResource.InitAllHandlers "Permalink to this definition")
Initializes handlers for all supported controls/windows.


This will make the executable quite big because it forces linking against most of the wxWidgets library.




            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def InsertHandler(self, handler: 'xrc.XmlResourceHandler') -> None:
        """ 

`InsertHandler`(*self*, *handler*)[¶](#wx.xrc.XmlResource.InsertHandler "Permalink to this definition")
Add a new handler at the beginning of the handler list.



Parameters
**handler** ([*wx.xrc.XmlResourceHandler*](wx.xrc.XmlResourceHandler.html#wx.xrc.XmlResourceHandler "wx.xrc.XmlResourceHandler")) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Load(self, filemask: str) -> bool:
        """ 

`Load`(*self*, *filemask*)[¶](#wx.xrc.XmlResource.Load "Permalink to this definition")
Loads resources from `XML` files that match given filemask.


Example:



```
if not wx.xml.XmlResource.Get().Load("rc/*.xrc"):
    wx.LogError("Couldn't load resources!")

```



Parameters
**filemask** (*string*) – 



Return type
*bool*





Note


If `USE_FILESYS` is enabled, this method understands  [wx.FileSystem](wx.FileSystem.html#wx-filesystem) URLs (see [`wx.FileSystem.FindFirst`](wx.FileSystem.html#wx.FileSystem.FindFirst "wx.FileSystem.FindFirst") ).




Note


If you are sure that the argument is name of single `XRC` file (rather than an URL or a wildcard), use [`LoadFile`](#wx.xrc.XmlResource.LoadFile "wx.xrc.XmlResource.LoadFile") instead.




See also


[`LoadFile`](#wx.xrc.XmlResource.LoadFile "wx.xrc.XmlResource.LoadFile") , [`LoadAllFiles`](#wx.xrc.XmlResource.LoadAllFiles "wx.xrc.XmlResource.LoadAllFiles")





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadAllFiles(self, dirname: str) -> bool:
        """ 

`LoadAllFiles`(*self*, *dirname*)[¶](#wx.xrc.XmlResource.LoadAllFiles "Permalink to this definition")
Loads all .xrc files from directory *dirname*.


Tries to load as many files as possible; if there’s an error while loading one file, it still attempts to load other files.



Parameters
**dirname** (*string*) – 



Return type
*bool*





New in version 2.9.0.




See also


[`LoadFile`](#wx.xrc.XmlResource.LoadFile "wx.xrc.XmlResource.LoadFile") , [`Load`](#wx.xrc.XmlResource.Load "wx.xrc.XmlResource.Load")





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadBitmap(self, name: str) -> 'Bitmap':
        """ 

`LoadBitmap`(*self*, *name*)[¶](#wx.xrc.XmlResource.LoadBitmap "Permalink to this definition")
Loads a bitmap resource from a file.



Parameters
**name** (*string*) – 



Return type
 [wx.Bitmap](wx.Bitmap.html#wx-bitmap)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDialog(self, *args, **kw) -> 'Dialog':
        """ 

`LoadDialog`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadDialog "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadDialog** *(self, parent, name)*


Loads a dialog.


*parent* points to parent window (if any).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
 [wx.Dialog](wx.Dialog.html#wx-dialog)






---

  



**LoadDialog** *(self, dlg, parent, name)*


Loads a dialog.


*parent* points to parent window (if any).


This form is used to finish creation of an already existing instance (the main reason for this is that you may want to use derived class with a new event table). Example:



```
# Without a class
dlg = wx.Dialog()
wx.xml.XmlResource.Get().LoadDialog(dlg, mainFrame, "my_dialog")
dlg.ShowModal()

# Or, as a class
class MyDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__()
        wx.xml.XmlResource.Get().LoadDialog(self, parent, "my_dialog")

```



Parameters
* **dlg** ([*wx.Dialog*](wx.Dialog.html#wx.Dialog "wx.Dialog")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadDocument(self, doc, name="") -> bool:
        """ 

`LoadDocument`(*self*, *doc*, *name=""*)[¶](#wx.xrc.XmlResource.LoadDocument "Permalink to this definition")
Load resources from the `XML` document containing them.


This can be useful when `XRC` contents comes from some place other than a file or, more generally, an URL, as it can still be read into a *MemoryInputStream* and then  [wx.xml.XmlDocument](wx.xml.XmlDocument.html#wx-xml-xmldocument) can be created from this stream and used with this function.


For example:



```
xrc_data = ... # Retrieve it from wherever.
xmlDoc = wx.xml.XmlDocument(io.BytesIO(xrc_data))
if not xmlDoc.IsOk():
    ... handle invalid XML here ...
    return

if not wx.XmlResource.Get().LoadDocument(xmlDoc):
    ... handle invalid XRC here ...
    return

... use the just loaded XRC as usual ...

```



Parameters
* **doc** ([*wx.xml.XmlDocument*](wx.xml.XmlDocument.html#wx.xml.XmlDocument "wx.xml.XmlDocument")) – A valid, i.e. non-null, document pointer ownership of which is passed to  [wx.xrc.XmlResource](#wx-xrc-xmlresource), i.e. this pointer can’t be used after this function rteturns.
* **name** (*string*) – The name argument is optional, but may be provided if you plan to call [`Unload`](#wx.xrc.XmlResource.Unload "wx.xrc.XmlResource.Unload") later. It doesn’t need to be an existing file or even conform to the usual form of file names as it is not interpreted in any way by  [wx.xrc.XmlResource](#wx-xrc-xmlresource), but it should be unique among the other documents and file names used if specified.



Return type
*bool*



Returns
`True` on success, `False` if the document couldn’t be loaded (note that *doc* is still destroyed in this case to avoid memory leaks).





New in version 4.1/wxWidgets-3.1.6.




See also


[`Load`](#wx.xrc.XmlResource.Load "wx.xrc.XmlResource.Load") , [`LoadFile`](#wx.xrc.XmlResource.LoadFile "wx.xrc.XmlResource.LoadFile")





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFile(self, file: str) -> bool:
        """ 

`LoadFile`(*self*, *file*)[¶](#wx.xrc.XmlResource.LoadFile "Permalink to this definition")
Simpler form of [`Load`](#wx.xrc.XmlResource.Load "wx.xrc.XmlResource.Load") for loading a single `XRC` file.



Parameters
**file** (*string*) – 



Return type
*bool*





New in version 2.9.0.




See also


[`Load`](#wx.xrc.XmlResource.Load "wx.xrc.XmlResource.Load") , [`LoadAllFiles`](#wx.xrc.XmlResource.LoadAllFiles "wx.xrc.XmlResource.LoadAllFiles") , [`LoadDocument`](#wx.xrc.XmlResource.LoadDocument "wx.xrc.XmlResource.LoadDocument")





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFrame(self, *args, **kw) -> 'Frame':
        """ 

`LoadFrame`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadFrame "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadFrame** *(self, parent, name)*


Loads a frame from the resource.


*parent* points to parent window (if any).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
 [wx.Frame](wx.Frame.html#wx-frame)






---

  



**LoadFrame** *(self, frame, parent, name)*


Loads the contents of a frame onto an existing  [wx.Frame](wx.Frame.html#wx-frame).


This form is used to finish creation of an already existing instance (the main reason for this is that you may want to use derived class with a new event table).



Parameters
* **frame** ([*wx.Frame*](wx.Frame.html#wx.Frame "wx.Frame")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadFromBuffer(self, data) -> bool:
        """ 

`LoadFromBuffer`(*self*, *data*)[¶](#wx.xrc.XmlResource.LoadFromBuffer "Permalink to this definition")
Load the resource from a bytes string or other data buffer compatible object.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadIcon(self, name: str) -> 'Icon':
        """ 

`LoadIcon`(*self*, *name*)[¶](#wx.xrc.XmlResource.LoadIcon "Permalink to this definition")
Loads an icon resource from a file.



Parameters
**name** (*string*) – 



Return type
 [wx.Icon](wx.Icon.html#wx-icon)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenu(self, name: str) -> 'Menu':
        """ 

`LoadMenu`(*self*, *name*)[¶](#wx.xrc.XmlResource.LoadMenu "Permalink to this definition")
Loads menu from resource.


Returns `None` on failure.



Parameters
**name** (*string*) – 



Return type
 [wx.Menu](wx.Menu.html#wx-menu)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadMenuBar(self, *args, **kw) -> 'MenuBar':
        """ 

`LoadMenuBar`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadMenuBar "Permalink to this definition")
Loads a menubar from resource.


Returns `None` on failure.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadMenuBar** *(self, parent, name)*



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
 [wx.MenuBar](wx.MenuBar.html#wx-menubar)






---

  



**LoadMenuBar** *(self, name)*



Parameters
**name** (*string*) – 



Return type
 [wx.MenuBar](wx.MenuBar.html#wx-menubar)






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObject(self, *args, **kw) -> 'Window':
        """ 

`LoadObject`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadObject "Permalink to this definition")
Load an object from the resource specifying both the resource name and the class name.


The first overload lets you load nonstandard container windows and returns `None` on failure. The second one lets you finish the creation of an existing instance and returns `False` on failure.


In either case, only the resources defined at the top level of `XRC` files can be loaded by this function, use [`LoadObjectRecursively`](#wx.xrc.XmlResource.LoadObjectRecursively "wx.xrc.XmlResource.LoadObjectRecursively") if you need to load an object defined deeper in the hierarchy.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadObject** *(self, parent, name, classname)*



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –
* **classname** (*string*) –



Return type
 [wx.Object](wx.Object.html#wx-object)






---

  



**LoadObject** *(self, instance, parent, name, classname)*



Parameters
* **instance** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –
* **classname** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadObjectRecursively(self, *args, **kw) -> 'Window':
        """ 

`LoadObjectRecursively`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadObjectRecursively "Permalink to this definition")
Load an object from anywhere in the resource tree.


These methods are similar to [`LoadObject`](#wx.xrc.XmlResource.LoadObject "wx.xrc.XmlResource.LoadObject") but may be used to load an object from anywhere in the resource tree and not only the top level. Note that you will very rarely need to do this as in normal use the entire container window (defined at the top level) is loaded and not its individual children but this method can be useful in some particular situations.



New in version 2.9.1.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadObjectRecursively** *(self, parent, name, classname)*



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –
* **classname** (*string*) –



Return type
 [wx.Object](wx.Object.html#wx-object)






---

  



**LoadObjectRecursively** *(self, instance, parent, name, classname)*



Parameters
* **instance** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –
* **classname** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadPanel(self, *args, **kw) -> 'Panel':
        """ 

`LoadPanel`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResource.LoadPanel "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadPanel** *(self, parent, name)*


Loads a panel.


*parent* points to the parent window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
 [wx.Panel](wx.Panel.html#wx-panel)






---

  



**LoadPanel** *(self, panel, parent, name)*


Loads a panel.


*parent* points to the parent window. This form is used to finish creation of an already existing instance.



Parameters
* **panel** ([*wx.Panel*](wx.Panel.html#wx.Panel "wx.Panel")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def LoadToolBar(self, parent, name) -> 'ToolBar':
        """ 

`LoadToolBar`(*self*, *parent*, *name*)[¶](#wx.xrc.XmlResource.LoadToolBar "Permalink to this definition")
Loads a toolbar.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **name** (*string*) –



Return type
 [wx.ToolBar](wx.ToolBar.html#wx-toolbar)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    @staticmethod
    def Set(res: 'xrc.XmlResource') -> 'XmlResource':
        """ 

*static* `Set`(*res*)[¶](#wx.xrc.XmlResource.Set "Permalink to this definition")
Sets the global resources object and returns a pointer to the previous one (may be `None`).



Parameters
**res** ([*wx.xrc.XmlResource*](#wx.xrc.XmlResource "wx.xrc.XmlResource")) – 



Return type
 [wx.xrc.XmlResource](#wx-xrc-xmlresource)






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetDomain(self, domain: str) -> None:
        """ 

`SetDomain`(*self*, *domain*)[¶](#wx.xrc.XmlResource.SetDomain "Permalink to this definition")
Sets the domain (message catalog) that will be used to load translatable strings in the `XRC`.



Parameters
**domain** (*string*) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.xrc.XmlResource.SetFlags "Permalink to this definition")
Sets flags (bitlist of  [wx.xrc.XmlResourceFlags](wx.xrc.XmlResourceFlags.enumeration.html#wx-xrc-xmlresourceflags) enumeration values).



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    def Unload(self, filename: str) -> bool:
        """ 

`Unload`(*self*, *filename*)[¶](#wx.xrc.XmlResource.Unload "Permalink to this definition")
This function unloads a resource previously loaded by [`Load`](#wx.xrc.XmlResource.Load "wx.xrc.XmlResource.Load") .


Returns `True` if the resource was successfully unloaded and `False` if it hasn’t been found in the list of loaded resources.



Parameters
**filename** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResource.html
        """

    Domain: str  # `Domain`[¶](#wx.xrc.XmlResource.Domain "Permalink to this definition")See [`GetDomain`](#wx.xrc.XmlResource.GetDomain "wx.xrc.XmlResource.GetDomain") and [`SetDomain`](#wx.xrc.XmlResource.SetDomain "wx.xrc.XmlResource.SetDomain")
    Flags: int  # `Flags`[¶](#wx.xrc.XmlResource.Flags "Permalink to this definition")See [`GetFlags`](#wx.xrc.XmlResource.GetFlags "wx.xrc.XmlResource.GetFlags") and [`SetFlags`](#wx.xrc.XmlResource.SetFlags "wx.xrc.XmlResource.SetFlags")
    Version: int  # `Version`[¶](#wx.xrc.XmlResource.Version "Permalink to this definition")See [`GetVersion`](#wx.xrc.XmlResource.GetVersion "wx.xrc.XmlResource.GetVersion")



class XmlResourceHandler(Object):
    """ **Possible constructors**:



```
XmlResourceHandler()

```


SizerXmlHandler is a class for resource handlers capable of creating
a Sizer object from an `XML` node.


  


        Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.xrc.XmlResourceHandler.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddStyle(self, name, value) -> None:
        """ 

`AddStyle`(*self*, *name*, *value*)[¶](#wx.xrc.XmlResourceHandler.AddStyle "Permalink to this definition")
Add a style flag (e.g.



> `MB_DOCKABLE` ) to the list of flags understood by this handler.



Parameters
* **name** (*string*) –
* **value** (*int*) –






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def AddWindowStyles(self) -> None:
        """ 

`AddWindowStyles`(*self*)[¶](#wx.xrc.XmlResourceHandler.AddWindowStyles "Permalink to this definition")
Add styles common to all Window-derived classes.




            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CanHandle(self, node: 'xml.XmlNode') -> bool:
        """ 

`CanHandle`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.CanHandle "Permalink to this definition")
Returns `True` if it understands this node and can create a resource from it, `False` otherwise.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
*bool*





Note


You must not call any  [wx.xrc.XmlResourceHandler](#wx-xrc-xmlresourcehandler) methods except [`IsOfClass`](#wx.xrc.XmlResourceHandler.IsOfClass "wx.xrc.XmlResourceHandler.IsOfClass") from this method! The instance is not yet initialized with node data at the time [`CanHandle`](#wx.xrc.XmlResourceHandler.CanHandle "wx.xrc.XmlResourceHandler.CanHandle") is called and it is only safe to operate on node directly or to call [`IsOfClass`](#wx.xrc.XmlResourceHandler.IsOfClass "wx.xrc.XmlResourceHandler.IsOfClass") .





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildren(self, parent, this_hnd_only=False) -> None:
        """ 

`CreateChildren`(*self*, *parent*, *this\_hnd\_only=False*)[¶](#wx.xrc.XmlResourceHandler.CreateChildren "Permalink to this definition")
Creates children.



Parameters
* **parent** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **this\_hnd\_only** (*bool*) –






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateChildrenPrivately(self, parent, rootnode=None) -> None:
        """ 

`CreateChildrenPrivately`(*self*, *parent*, *rootnode=None*)[¶](#wx.xrc.XmlResourceHandler.CreateChildrenPrivately "Permalink to this definition")
Helper function.



Parameters
* **parent** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **rootnode** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResFromNode(self, node, parent, instance=None) -> 'Window':
        """ 

`CreateResFromNode`(*self*, *node*, *parent*, *instance=None*)[¶](#wx.xrc.XmlResourceHandler.CreateResFromNode "Permalink to this definition")
Creates a resource from a node.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **parent** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **instance** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –



Return type
 [wx.Object](wx.Object.html#wx-object)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def CreateResource(self, node, parent, instance) -> 'Window':
        """ 

`CreateResource`(*self*, *node*, *parent*, *instance*)[¶](#wx.xrc.XmlResourceHandler.CreateResource "Permalink to this definition")
Creates an object (menu, dialog, control, …) from an `XML` node.


Should check for validity. *parent* is a higher-level object (usually window, dialog or panel) that is often necessary to create the resource.


If **instance** is not `None` it should not create a new instance via ‘new’ but should rather use this one, and call its Create method.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **parent** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **instance** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –



Return type
 [wx.Object](wx.Object.html#wx-object)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def DoCreateResource(self) -> 'Window':
        """ 

`DoCreateResource`(*self*)[¶](#wx.xrc.XmlResourceHandler.DoCreateResource "Permalink to this definition")
Called from CreateResource after variables were filled.



Return type
 [wx.Object](wx.Object.html#wx-object)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetAnimation(self, param="animation", ctrl=None) -> 'Animation':
        """ 

`GetAnimation`(*self*, *param="animation"*, *ctrl=None*)[¶](#wx.xrc.XmlResourceHandler.GetAnimation "Permalink to this definition")
Creates an animation (see  [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)) from the filename specified in *param*.


It is recommended to provide *ctrl* argument to this function (which is only available in wxWidgets 3.1.4 or later) to make sure that the created animation is compatible with the specified control, otherwise a  [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation) object compatible with the default  [wx.adv.AnimationCtrl](wx.adv.AnimationCtrl.html#wx-adv-animationctrl) implementation is created.



Parameters
* **param** (*string*) –
* **ctrl** ([*wx.adv.AnimationCtrl*](wx.adv.AnimationCtrl.html#wx.adv.AnimationCtrl "wx.adv.AnimationCtrl")) –



Return type
 [wx.adv.Animation](wx.adv.Animation.html#wx-adv-animation)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmap(self, *args, **kw) -> 'Bitmap':
        """ 

`GetBitmap`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResourceHandler.GetBitmap "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetBitmap** *(self, param=”bitmap”, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Gets a bitmap.



Parameters
* **param** (*string*) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.Bitmap](wx.Bitmap.html#wx-bitmap)






---

  



**GetBitmap** *(self, node, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Gets a bitmap from an XmlNode.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.Bitmap](wx.Bitmap.html#wx-bitmap)





New in version 2.9.1.





---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBitmapBundle(self, *args, **kw) -> 'BitmapBundle':
        """ 

`GetBitmapBundle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResourceHandler.GetBitmapBundle "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetBitmapBundle** *(self, param=”bitmap”, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Gets a bitmap bundle.



Parameters
* **param** (*string*) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.BitmapBundle](wx.BitmapBundle.html#wx-bitmapbundle)





New in version 4.1/wxWidgets-3.1.6.





---

  



**GetBitmapBundle** *(self, node, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Gets a bitmap bundle from the provided node.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.BitmapBundle](wx.BitmapBundle.html#wx-bitmapbundle)





New in version 4.1/wxWidgets-3.1.6.





---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetBool(self, param, defaultv=False) -> bool:
        """ 

`GetBool`(*self*, *param*, *defaultv=False*)[¶](#wx.xrc.XmlResourceHandler.GetBool "Permalink to this definition")
Gets a bool flag (1, t, yes, on, `True` are `True`, everything else is `False`).



Parameters
* **param** (*string*) –
* **defaultv** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetClass(self) -> str:
        """ 

`GetClass`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetClass "Permalink to this definition")
After CreateResource has been called this will return the class name of the `XML` resource node being processed.



Return type
`string`





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetColour(self, param, defaultColour=NullColour) -> 'Colour':
        """ 

`GetColour`(*self*, *param*, *defaultColour=NullColour*)[¶](#wx.xrc.XmlResourceHandler.GetColour "Permalink to this definition")
Gets colour in HTML syntax (#``RRGGBB``).



Parameters
* **param** (*string*) –
* **defaultColour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –



Return type
 [wx.Colour](wx.Colour.html#wx-colour)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetCurFileSystem(self) -> 'FileSystem':
        """ 

`GetCurFileSystem`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetCurFileSystem "Permalink to this definition")
Returns the current file system.



Return type
 [wx.FileSystem](wx.FileSystem.html#wx-filesystem)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDimension(self, param, defaultv=0, windowToUse=0) -> 'Coord':
        """ 

`GetDimension`(*self*, *param*, *defaultv=0*, *windowToUse=0*)[¶](#wx.xrc.XmlResourceHandler.GetDimension "Permalink to this definition")
Gets a dimension (may be in dialog units).



Parameters
* **param** (*string*) –
* **defaultv** (*int*) –
* **windowToUse** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*wx.Coord*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetDirection(self, param, dirDefault=LEFT) -> int:
        """ 

`GetDirection`(*self*, *param*, *dirDefault=LEFT*)[¶](#wx.xrc.XmlResourceHandler.GetDirection "Permalink to this definition")
Gets a direction.


If the given *param* is not present or has empty value, *dirDefault* is returned by default. Otherwise the value of the parameter is parsed and a warning is generated if it’s not one of `LEFT` , `TOP` , `RIGHT` or `BOTTOM` .



Parameters
* **param** (*string*) –
* **dirDefault** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) –



Return type
 [wx.DataObject.Direction](wx.DataObject.Direction.enumeration.html#wx-dataobject-direction)





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFloat(self, param, defaultv=0) -> float:
        """ 

`GetFloat`(*self*, *param*, *defaultv=0*)[¶](#wx.xrc.XmlResourceHandler.GetFloat "Permalink to this definition")
Gets a float value from the parameter.



Parameters
* **param** (*string*) –
* **defaultv** (*float*) –



Return type
*float*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetFont(self, param: str="font") -> 'Font':
        """ 

`GetFont`(*self*, *param="font"*)[¶](#wx.xrc.XmlResourceHandler.GetFont "Permalink to this definition")
Gets a font.



Parameters
**param** (*string*) – 



Return type
 [wx.Font](wx.Font.html#wx-font)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetID(self) -> int:
        """ 

`GetID`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetID "Permalink to this definition")
Returns the `wx.xrc.XRCID`.



Return type
*int*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIcon(self, *args, **kw) -> 'Icon':
        """ 

`GetIcon`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResourceHandler.GetIcon "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetIcon** *(self, param=”icon”, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Returns an icon.



Parameters
* **param** (*string*) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.Icon](wx.Icon.html#wx-icon)






---

  



**GetIcon** *(self, node, defaultArtClient=ART\_OTHER, size=DefaultSize)*


Gets an icon from an XmlNode.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **defaultArtClient** (*wx.ArtClient*) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
 [wx.Icon](wx.Icon.html#wx-icon)





New in version 2.9.1.





---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetIconBundle(self, param, defaultArtClient=ART_OTHER) -> 'IconBundle':
        """ 

`GetIconBundle`(*self*, *param*, *defaultArtClient=ART\_OTHER*)[¶](#wx.xrc.XmlResourceHandler.GetIconBundle "Permalink to this definition")
Returns an icon bundle.



Parameters
* **param** (*string*) –
* **defaultArtClient** (*wx.ArtClient*) –



Return type
 [wx.IconBundle](wx.IconBundle.html#wx-iconbundle)





New in version 2.9.0.




Note


Bundles can be loaded either with stock IDs or from files that contain more than one image (e.g. Windows icon files). If a file contains only single image, a bundle with only one icon will be created.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetImageList(self, param: str="imagelist") -> 'ImageList':
        """ 

`GetImageList`(*self*, *param="imagelist"*)[¶](#wx.xrc.XmlResourceHandler.GetImageList "Permalink to this definition")
Creates an image list from the *param* markup data.



Parameters
**param** (*string*) – 



Return type
 [wx.ImageList](wx.ImageList.html#wx-imagelist)



Returns
The new instance of  [wx.ImageList](wx.ImageList.html#wx-imagelist) or `None` if no data is found.





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetInstance(self) -> 'Window':
        """ 

`GetInstance`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetInstance "Permalink to this definition")
After CreateResource has been called this will return the instance that the `XML` resource content should be created upon, if it has already been created.


If `None` then the handler should create the object itself.



Return type
 [wx.Object](wx.Object.html#wx-object)





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetLong(self, param, defaultv=0) -> int:
        """ 

`GetLong`(*self*, *param*, *defaultv=0*)[¶](#wx.xrc.XmlResourceHandler.GetLong "Permalink to this definition")
Gets the integer value from the parameter.



Parameters
* **param** (*string*) –
* **defaultv** (*long*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetName "Permalink to this definition")
Returns the resource name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNode(self) -> 'XmlNode':
        """ 

`GetNode`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetNode "Permalink to this definition")
After CreateResource has been called this will return the `XML` node being processed.



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeChildren(self, node: 'xml.XmlNode') -> 'XmlNode':
        """ 

`GetNodeChildren`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.GetNodeChildren "Permalink to this definition")
Gets the first child of the given node or `None`.


This method is safe to call with `None` argument, it just returns `None` in this case.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeContent(self, node: 'xml.XmlNode') -> str:
        """ 

`GetNodeContent`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.GetNodeContent "Permalink to this definition")
Gets node content from `wx.xml.XML_ENTITY_NODE`.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeNext(self, node: 'xml.XmlNode') -> 'XmlNode':
        """ 

`GetNodeNext`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.GetNodeNext "Permalink to this definition")
Gets the next sibling node related to the given node, possibly `None`.


This method is safe to call with `None` argument, it just returns `None` in this case.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetNodeParent(self, node: 'xml.XmlNode') -> 'XmlNode':
        """ 

`GetNodeParent`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.GetNodeParent "Permalink to this definition")
Gets the parent of the node given.


This method is safe to call with `None` argument, it just returns `None` in this case.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamNode(self, param: str) -> 'XmlNode':
        """ 

`GetParamNode`(*self*, *param*)[¶](#wx.xrc.XmlResourceHandler.GetParamNode "Permalink to this definition")
Finds the node or returns `None`.



Parameters
**param** (*string*) – 



Return type
 [wx.xml.XmlNode](wx.xml.XmlNode.html#wx-xml-xmlnode)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParamValue(self, *args, **kw) -> str:
        """ 

`GetParamValue`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResourceHandler.GetParamValue "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetParamValue** *(self, param)*


Finds the parameter value or returns the empty string.



Parameters
**param** (*string*) – 



Return type
`string`






---

  



**GetParamValue** *(self, node)*


Returns the node parameter value.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
`string`





New in version 2.9.1.





---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParent(self) -> 'Window':
        """ 

`GetParent`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetParent "Permalink to this definition")
After CreateResource has been called this will return the current item’s parent, if any.



Return type
 [wx.Object](wx.Object.html#wx-object)





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetParentAsWindow(self) -> 'Window':
        """ 

`GetParentAsWindow`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetParentAsWindow "Permalink to this definition")
After CreateResource has been called this will return the item’s parent as a  [wx.Window](wx.Window.html#wx-window).



Return type
 [wx.Window](wx.Window.html#wx-window)





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetPosition(self, param: str="pos") -> 'Point':
        """ 

`GetPosition`(*self*, *param="pos"*)[¶](#wx.xrc.XmlResourceHandler.GetPosition "Permalink to this definition")
Gets the position (may be in dialog units).



Parameters
**param** (*string*) – 



Return type
 [wx.Point](wx.Point.html#wx-point)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetResource(self) -> 'XmlResource':
        """ 

`GetResource`(*self*)[¶](#wx.xrc.XmlResourceHandler.GetResource "Permalink to this definition")
After CreateResource has been called this will return the current  [wx.xrc.XmlResource](wx.xrc.XmlResource.html#wx-xrc-xmlresource) object.



Return type
 [wx.xrc.XmlResource](wx.xrc.XmlResource.html#wx-xrc-xmlresource)





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetSize(self, param="size", windowToUse=0) -> 'Size':
        """ 

`GetSize`(*self*, *param="size"*, *windowToUse=0*)[¶](#wx.xrc.XmlResourceHandler.GetSize "Permalink to this definition")
Gets the size (may be in dialog units).



Parameters
* **param** (*string*) –
* **windowToUse** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
 [wx.Size](wx.Size.html#wx-size)






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetStyle(self, param="style", defaults=0) -> int:
        """ 

`GetStyle`(*self*, *param="style"*, *defaults=0*)[¶](#wx.xrc.XmlResourceHandler.GetStyle "Permalink to this definition")
Gets style flags from text in form “flag | flag2| flag3 [|](#id3)…” Only understands flags added with [`AddStyle`](#wx.xrc.XmlResourceHandler.AddStyle "wx.xrc.XmlResourceHandler.AddStyle") .



Parameters
* **param** (*string*) –
* **defaults** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def GetText(self, param, translate=True) -> str:
        """ 

`GetText`(*self*, *param*, *translate=True*)[¶](#wx.xrc.XmlResourceHandler.GetText "Permalink to this definition")
Gets text from param and does some conversions:


* replaces \n, \r, \t by respective characters (according to C syntax)
* replaces `$` by `and` `$$` by `$` (needed for `_File` to `File` translation because of `XML` syntax)
* calls GetTranslations (unless disabled in  [wx.xrc.XmlResource](wx.xrc.XmlResource.html#wx-xrc-xmlresource))



Parameters
* **param** (*string*) –
* **translate** (*bool*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def HasParam(self, param: str) -> bool:
        """ 

`HasParam`(*self*, *param*)[¶](#wx.xrc.XmlResourceHandler.HasParam "Permalink to this definition")
Check to see if a parameter exists.



Parameters
**param** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsObjectNode(self, node: 'xml.XmlNode') -> bool:
        """ 

`IsObjectNode`(*self*, *node*)[¶](#wx.xrc.XmlResourceHandler.IsObjectNode "Permalink to this definition")
Checks if the given node is an object node.


Object nodes are those named “object” or “object\_ref”.



Parameters
**node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def IsOfClass(self, node, classname) -> bool:
        """ 

`IsOfClass`(*self*, *node*, *classname*)[¶](#wx.xrc.XmlResourceHandler.IsOfClass "Permalink to this definition")
Convenience function.


Returns `True` if the node has a property class equal to classname, e.g. object class=”wxDialog”.



Parameters
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **classname** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportError(self, *args, **kw) -> None:
        """ 

`ReportError`(*self*, *\*args*, *\*\*kw*)[¶](#wx.xrc.XmlResourceHandler.ReportError "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ReportError** *(self, context, message)*


Reports error in `XRC` resources to the user.


See `wx.xrc.XmlResource.ReportError` for more information.



Parameters
* **context** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **message** (*string*) –





New in version 2.9.0.





---

  



**ReportError** *(self, message)*


Like [`ReportError`](#wx.xrc.XmlResourceHandler.ReportError "wx.xrc.XmlResourceHandler.ReportError") , but uses the node of currently processed object (m\_node) as the context.



Parameters
**message** (*string*) – 





New in version 2.9.0.





---

  





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def ReportParamError(self, param, message) -> None:
        """ 

`ReportParamError`(*self*, *param*, *message*)[¶](#wx.xrc.XmlResourceHandler.ReportParamError "Permalink to this definition")
Like [`ReportError`](#wx.xrc.XmlResourceHandler.ReportError "wx.xrc.XmlResourceHandler.ReportError") , but uses the node of parameter *param* of the currently processed object as the context.


This is convenience function for reporting errors in particular parameters.



Parameters
* **param** (*string*) –
* **message** (*string*) –





New in version 2.9.0.





            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetParentResource(self, res: 'xrc.XmlResource') -> None:
        """ 

`SetParentResource`(*self*, *res*)[¶](#wx.xrc.XmlResourceHandler.SetParentResource "Permalink to this definition")
Sets the parent resource.



Parameters
**res** ([*wx.xrc.XmlResource*](wx.xrc.XmlResource.html#wx.xrc.XmlResource "wx.xrc.XmlResource")) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    def SetupWindow(self, wnd: 'Window') -> None:
        """ 

`SetupWindow`(*self*, *wnd*)[¶](#wx.xrc.XmlResourceHandler.SetupWindow "Permalink to this definition")
Sets common window options.



Parameters
**wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.xrc.XmlResourceHandler.html
        """

    Animation: 'Animation'  # `Animation`[¶](#wx.xrc.XmlResourceHandler.Animation "Permalink to this definition")See [`GetAnimation`](#wx.xrc.XmlResourceHandler.GetAnimation "wx.xrc.XmlResourceHandler.GetAnimation")
    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.xrc.XmlResourceHandler.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.xrc.XmlResourceHandler.GetBitmap "wx.xrc.XmlResourceHandler.GetBitmap")
    BitmapBundle: '_BitmapBundle'  # `BitmapBundle`[¶](#wx.xrc.XmlResourceHandler.BitmapBundle "Permalink to this definition")See [`GetBitmapBundle`](#wx.xrc.XmlResourceHandler.GetBitmapBundle "wx.xrc.XmlResourceHandler.GetBitmapBundle")
    Class: str  # `Class`[¶](#wx.xrc.XmlResourceHandler.Class "Permalink to this definition")See [`GetClass`](#wx.xrc.XmlResourceHandler.GetClass "wx.xrc.XmlResourceHandler.GetClass")
    CurFileSystem: 'FileSystem'  # `CurFileSystem`[¶](#wx.xrc.XmlResourceHandler.CurFileSystem "Permalink to this definition")See [`GetCurFileSystem`](#wx.xrc.XmlResourceHandler.GetCurFileSystem "wx.xrc.XmlResourceHandler.GetCurFileSystem")
    Font: '_Font'  # `Font`[¶](#wx.xrc.XmlResourceHandler.Font "Permalink to this definition")See [`GetFont`](#wx.xrc.XmlResourceHandler.GetFont "wx.xrc.XmlResourceHandler.GetFont")
    ID: int  # `ID`[¶](#wx.xrc.XmlResourceHandler.ID "Permalink to this definition")See [`GetID`](#wx.xrc.XmlResourceHandler.GetID "wx.xrc.XmlResourceHandler.GetID")
    Icon: '_Icon'  # `Icon`[¶](#wx.xrc.XmlResourceHandler.Icon "Permalink to this definition")See [`GetIcon`](#wx.xrc.XmlResourceHandler.GetIcon "wx.xrc.XmlResourceHandler.GetIcon")
    ImageList: '_ImageList'  # `ImageList`[¶](#wx.xrc.XmlResourceHandler.ImageList "Permalink to this definition")See [`GetImageList`](#wx.xrc.XmlResourceHandler.GetImageList "wx.xrc.XmlResourceHandler.GetImageList")
    Instance: 'Window'  # `Instance`[¶](#wx.xrc.XmlResourceHandler.Instance "Permalink to this definition")See [`GetInstance`](#wx.xrc.XmlResourceHandler.GetInstance "wx.xrc.XmlResourceHandler.GetInstance")
    Name: str  # `Name`[¶](#wx.xrc.XmlResourceHandler.Name "Permalink to this definition")See [`GetName`](#wx.xrc.XmlResourceHandler.GetName "wx.xrc.XmlResourceHandler.GetName")
    Node: 'XmlNode'  # `Node`[¶](#wx.xrc.XmlResourceHandler.Node "Permalink to this definition")See [`GetNode`](#wx.xrc.XmlResourceHandler.GetNode "wx.xrc.XmlResourceHandler.GetNode")
    Parent: 'Window'  # `Parent`[¶](#wx.xrc.XmlResourceHandler.Parent "Permalink to this definition")See [`GetParent`](#wx.xrc.XmlResourceHandler.GetParent "wx.xrc.XmlResourceHandler.GetParent")
    ParentAsWindow: 'Window'  # `ParentAsWindow`[¶](#wx.xrc.XmlResourceHandler.ParentAsWindow "Permalink to this definition")See [`GetParentAsWindow`](#wx.xrc.XmlResourceHandler.GetParentAsWindow "wx.xrc.XmlResourceHandler.GetParentAsWindow")
    Position: 'Point'  # `Position`[¶](#wx.xrc.XmlResourceHandler.Position "Permalink to this definition")See [`GetPosition`](#wx.xrc.XmlResourceHandler.GetPosition "wx.xrc.XmlResourceHandler.GetPosition")
    Resource: 'XmlResource'  # `Resource`[¶](#wx.xrc.XmlResourceHandler.Resource "Permalink to this definition")See [`GetResource`](#wx.xrc.XmlResourceHandler.GetResource "wx.xrc.XmlResourceHandler.GetResource")
    Size: '_Size'  # `Size`[¶](#wx.xrc.XmlResourceHandler.Size "Permalink to this definition")See [`GetSize`](#wx.xrc.XmlResourceHandler.GetSize "wx.xrc.XmlResourceHandler.GetSize")
    Style: int  # `Style`[¶](#wx.xrc.XmlResourceHandler.Style "Permalink to this definition")See [`GetStyle`](#wx.xrc.XmlResourceHandler.GetStyle "wx.xrc.XmlResourceHandler.GetStyle")



XRCID: int

XML_ENTITY_NODE: int

XmlResourceFlags: TypeAlias = int  # Enumeration

XRC_USE_LOCALE: int

XRC_NO_SUBCLASSING: int

XRC_NO_RELOADING: int

XRC_USE_ENVVARS: int

class XmlSubclassFactory:
    """ **Possible constructors**:



```
XmlSubclassFactory()

```


  


        Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.xrc.XmlSubclassFactory.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """

    def Create(self, className: str) -> 'Window':
        """ 

`Create`(*self*, *className*)[¶](#wx.xrc.XmlSubclassFactory.Create "Permalink to this definition")

Parameters
**className** (`String`) – 



Return type
 [wx.Object](wx.Object.html#wx-object)






            Source: https://docs.wxpython.org/wx.xrc.XmlSubclassFactory.html
        """



Animation: TypeAlias = Any

XmlNode: TypeAlias = Any

