# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import CommandEvent, Control, Size, VisualAttributes, NotifyEvent, ClientData, Rect, Bitmap, PyUserData, Coord, Colour, Font, Orientation

class RibbonButtonBarEvent(CommandEvent):
    """ **Possible constructors**:



```
RibbonButtonBarEvent(command_type=wxEVT_NULL, win_id=0, bar=None,
                     button=None)

```


Event used to indicate various actions relating to a button on a
RibbonButtonBar.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None, button=None) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*, *bar=None*, *button=None*)[¶](#wx.ribbon.RibbonButtonBarEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –
* **bar** ([*wx.ribbon.RibbonButtonBar*](wx.ribbon.RibbonButtonBar.html#wx.ribbon.RibbonButtonBar "wx.ribbon.RibbonButtonBar")) –
* **button** ([*RibbonButtonBarButtonBase*](wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase.html#wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase "wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def GetBar(self) -> 'RibbonButtonBar':
        """ 

`GetBar`(*self*)[¶](#wx.ribbon.RibbonButtonBarEvent.GetBar "Permalink to this definition")
Returns the bar which contains the button which the event relates to.



Return type
 [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def GetButton(self) -> 'RibbonButtonBarButtonBase':
        """ 

`GetButton`(*self*)[¶](#wx.ribbon.RibbonButtonBarEvent.GetButton "Permalink to this definition")
Returns the button which the event relates to.



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ 

`PopupMenu`(*self*, *menu*)[¶](#wx.ribbon.RibbonButtonBarEvent.PopupMenu "Permalink to this definition")
Display a popup menu as a result of this (dropdown clicked) event.



Parameters
**menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def SetBar(self, bar: 'ribbon.RibbonButtonBar') -> None:
        """ 

`SetBar`(*self*, *bar*)[¶](#wx.ribbon.RibbonButtonBarEvent.SetBar "Permalink to this definition")
Sets the button bar relating to this event.



Parameters
**bar** ([*wx.ribbon.RibbonButtonBar*](wx.ribbon.RibbonButtonBar.html#wx.ribbon.RibbonButtonBar "wx.ribbon.RibbonButtonBar")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    def SetButton(self, bar: RibbonButtonBarButtonBase) -> None:
        """ 

`SetButton`(*self*, *bar*)[¶](#wx.ribbon.RibbonButtonBarEvent.SetButton "Permalink to this definition")
Sets the button relating to this event.



Parameters
**bar** ([*RibbonButtonBarButtonBase*](wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase.html#wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase "wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase")) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBarEvent.html
        """

    Bar: 'RibbonButtonBar'  # `Bar`[¶](#wx.ribbon.RibbonButtonBarEvent.Bar "Permalink to this definition")See [`GetBar`](#wx.ribbon.RibbonButtonBarEvent.GetBar "wx.ribbon.RibbonButtonBarEvent.GetBar") and [`SetBar`](#wx.ribbon.RibbonButtonBarEvent.SetBar "wx.ribbon.RibbonButtonBarEvent.SetBar")
    Button: 'RibbonButtonBarButtonBase'  # `Button`[¶](#wx.ribbon.RibbonButtonBarEvent.Button "Permalink to this definition")See [`GetButton`](#wx.ribbon.RibbonButtonBarEvent.GetButton "wx.ribbon.RibbonButtonBarEvent.GetButton") and [`SetButton`](#wx.ribbon.RibbonButtonBarEvent.SetButton "wx.ribbon.RibbonButtonBarEvent.SetButton")



class RibbonGalleryEvent(CommandEvent):
    """ **Possible constructors**:



```
RibbonGalleryEvent(command_type=wxEVT_NULL, win_id=0, gallery=None,
                   item=None)

```


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, gallery=None, item=None) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*, *gallery=None*, *item=None*)[¶](#wx.ribbon.RibbonGalleryEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –
* **gallery** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) –
* **item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def GetGallery(self) -> 'RibbonGallery':
        """ 

`GetGallery`(*self*)[¶](#wx.ribbon.RibbonGalleryEvent.GetGallery "Permalink to this definition")
Returns the gallery which the event relates to.



Return type
 [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def GetGalleryItem(self) -> 'RibbonGalleryItem':
        """ 

`GetGalleryItem`(*self*)[¶](#wx.ribbon.RibbonGalleryEvent.GetGalleryItem "Permalink to this definition")
Returns the gallery item which the event relates to, or `None` if it does not relate to an item.



Return type
*RibbonGalleryItem*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def SetGallery(self, gallery: 'ribbon.RibbonGallery') -> None:
        """ 

`SetGallery`(*self*, *gallery*)[¶](#wx.ribbon.RibbonGalleryEvent.SetGallery "Permalink to this definition")
Sets the gallery relating to this event.



Parameters
**gallery** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    def SetGalleryItem(self, item: RibbonGalleryItem) -> None:
        """ 

`SetGalleryItem`(*self*, *item*)[¶](#wx.ribbon.RibbonGalleryEvent.SetGalleryItem "Permalink to this definition")
Sets the gallery item relating to this event.



Parameters
**item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGalleryEvent.html
        """

    Gallery: 'RibbonGallery'  # `Gallery`[¶](#wx.ribbon.RibbonGalleryEvent.Gallery "Permalink to this definition")See [`GetGallery`](#wx.ribbon.RibbonGalleryEvent.GetGallery "wx.ribbon.RibbonGalleryEvent.GetGallery") and [`SetGallery`](#wx.ribbon.RibbonGalleryEvent.SetGallery "wx.ribbon.RibbonGalleryEvent.SetGallery")
    GalleryItem: 'RibbonGalleryItem'  # `GalleryItem`[¶](#wx.ribbon.RibbonGalleryEvent.GalleryItem "Permalink to this definition")See [`GetGalleryItem`](#wx.ribbon.RibbonGalleryEvent.GetGalleryItem "wx.ribbon.RibbonGalleryEvent.GetGalleryItem") and [`SetGalleryItem`](#wx.ribbon.RibbonGalleryEvent.SetGalleryItem "wx.ribbon.RibbonGalleryEvent.SetGalleryItem")



class RibbonPanelEvent(CommandEvent):
    """ **Possible constructors**:



```
RibbonPanelEvent(command_type=wxEVT_NULL, win_id=0, panel=None)

```


Event used to indicate various actions relating to a RibbonPanel.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, panel=None) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*, *panel=None*)[¶](#wx.ribbon.RibbonPanelEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –
* **panel** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    def GetPanel(self) -> 'RibbonPanel':
        """ 

`GetPanel`(*self*)[¶](#wx.ribbon.RibbonPanelEvent.GetPanel "Permalink to this definition")
Returns the panel relating to this event.



Return type
 [wx.ribbon.RibbonPanel](wx.ribbon.RibbonPanel.html#wx-ribbon-ribbonpanel)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    def SetPanel(self, page: 'ribbon.RibbonPanel') -> None:
        """ 

`SetPanel`(*self*, *page*)[¶](#wx.ribbon.RibbonPanelEvent.SetPanel "Permalink to this definition")
Sets the page relating to this event.



Parameters
**page** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanelEvent.html
        """

    Panel: 'RibbonPanel'  # `Panel`[¶](#wx.ribbon.RibbonPanelEvent.Panel "Permalink to this definition")See [`GetPanel`](#wx.ribbon.RibbonPanelEvent.GetPanel "wx.ribbon.RibbonPanelEvent.GetPanel") and [`SetPanel`](#wx.ribbon.RibbonPanelEvent.SetPanel "wx.ribbon.RibbonPanelEvent.SetPanel")



class RibbonToolBarEvent(CommandEvent):
    """ **Possible constructors**:



```
RibbonToolBarEvent(command_type=wxEVT_NULL, win_id=0, bar=None)

```


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, bar=None) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*, *bar=None*)[¶](#wx.ribbon.RibbonToolBarEvent.__init__ "Permalink to this definition")

Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –
* **bar** ([*wx.ribbon.RibbonToolBar*](wx.ribbon.RibbonToolBar.html#wx.ribbon.RibbonToolBar "wx.ribbon.RibbonToolBar")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def GetBar(self) -> 'RibbonToolBar':
        """ 

`GetBar`(*self*)[¶](#wx.ribbon.RibbonToolBarEvent.GetBar "Permalink to this definition")

Return type
 [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def PopupMenu(self, menu: 'Menu') -> bool:
        """ 

`PopupMenu`(*self*, *menu*)[¶](#wx.ribbon.RibbonToolBarEvent.PopupMenu "Permalink to this definition")

Parameters
**menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    def SetBar(self, bar: 'ribbon.RibbonToolBar') -> None:
        """ 

`SetBar`(*self*, *bar*)[¶](#wx.ribbon.RibbonToolBarEvent.SetBar "Permalink to this definition")

Parameters
**bar** ([*wx.ribbon.RibbonToolBar*](wx.ribbon.RibbonToolBar.html#wx.ribbon.RibbonToolBar "wx.ribbon.RibbonToolBar")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBarEvent.html
        """

    Bar: 'RibbonToolBar'  # `Bar`[¶](#wx.ribbon.RibbonToolBarEvent.Bar "Permalink to this definition")See [`GetBar`](#wx.ribbon.RibbonToolBarEvent.GetBar "wx.ribbon.RibbonToolBarEvent.GetBar") and [`SetBar`](#wx.ribbon.RibbonToolBarEvent.SetBar "wx.ribbon.RibbonToolBarEvent.SetBar")



class RibbonControl(Control):
    """ **Possible constructors**:



```
RibbonControl()

RibbonControl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
              style=0, validator=DefaultValidator, name=ControlNameStr)

```


RibbonControl serves as a base class for all controls which share
the ribbon characteristics of having a ribbon art provider, and
(optionally) non-continuous resizing.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonControl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=ControlNameStr)*


Constructor.


If *parent* is a  [wx.ribbon.RibbonControl](#wx-ribbon-ribboncontrol) with a not `None` art provider, then the art provider of new control is set to that of *parent*.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def DoGetNextLargerSize(self, direction, relative_to) -> 'Size':
        """ 

`DoGetNextLargerSize`(*self*, *direction*, *relative\_to*)[¶](#wx.ribbon.RibbonControl.DoGetNextLargerSize "Permalink to this definition")
Implementation of [`GetNextLargerSize`](#wx.ribbon.RibbonControl.GetNextLargerSize "wx.ribbon.RibbonControl.GetNextLargerSize") .


Controls which have non-continuous sizing must override this virtual function rather than [`GetNextLargerSize`](#wx.ribbon.RibbonControl.GetNextLargerSize "wx.ribbon.RibbonControl.GetNextLargerSize") .



Parameters
* **direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) –
* **relative\_to** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
`Size`






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def DoGetNextSmallerSize(self, direction, relative_to) -> 'Size':
        """ 

`DoGetNextSmallerSize`(*self*, *direction*, *relative\_to*)[¶](#wx.ribbon.RibbonControl.DoGetNextSmallerSize "Permalink to this definition")
Implementation of [`GetNextSmallerSize`](#wx.ribbon.RibbonControl.GetNextSmallerSize "wx.ribbon.RibbonControl.GetNextSmallerSize") .


Controls which have non-continuous sizing must override this virtual function rather than [`GetNextSmallerSize`](#wx.ribbon.RibbonControl.GetNextSmallerSize "wx.ribbon.RibbonControl.GetNextSmallerSize") .



Parameters
* **direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) –
* **relative\_to** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
`Size`






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetAncestorRibbonBar(self) -> 'RibbonBar':
        """ 

`GetAncestorRibbonBar`(*self*)[¶](#wx.ribbon.RibbonControl.GetAncestorRibbonBar "Permalink to this definition")
Get the first ancestor which is a  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) (or derived) or `None` if not having such parent.



Return type
 [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar)





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetArtProvider(self) -> 'RibbonArtProvider':
        """ 

`GetArtProvider`(*self*)[¶](#wx.ribbon.RibbonControl.GetArtProvider "Permalink to this definition")
Get the art provider to be used.


Note that until an art provider has been set in some way, this function may return `None`.



Return type
 [wx.ribbon.RibbonArtProvider](wx.ribbon.RibbonArtProvider.html#wx-ribbon-ribbonartprovider)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetBestSizeForParentSize(self, parentSize: Union[tuple[int, int], 'Size']) -> 'Size':
        """ 

`GetBestSizeForParentSize`(*self*, *parentSize*)[¶](#wx.ribbon.RibbonControl.GetBestSizeForParentSize "Permalink to this definition")
Finds the best width and height given the parent’s width and height.


Used to implement the `wx.ribbon.RIBBON_PANEL_FLEXIBLE` panel style.



Parameters
**parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
`Size`






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonControl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetNextLargerSize(self, *args, **kw) -> 'Size':
        """ 

`GetNextLargerSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonControl.GetNextLargerSize "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetNextLargerSize** *(self, direction)*


If sizing is not continuous, then return a suitable size for the control which is larger than the current size.



Parameters
**direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) – The direction(s) in which the size should increase.



Return type
`Size`



Returns
The current size if there is no larger size, otherwise a suitable size which is larger in the given direction(s), and the same as the current size in the other direction (if any).





See also


[`IsSizingContinuous`](#wx.ribbon.RibbonControl.IsSizingContinuous "wx.ribbon.RibbonControl.IsSizingContinuous")





---

  



**GetNextLargerSize** *(self, direction, relative\_to)*


If sizing is not continuous, then return a suitable size for the control which is larger than the given size.



Parameters
* **direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) – The direction(s) in which the size should increase.
* **relative\_to** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size for which a larger size should be found.



Return type
`Size`



Returns
*relative\_to* if there is no larger size, otherwise a suitable size which is larger in the given direction(s), and the same as *relative\_to* in the other direction (if any).





See also


[`IsSizingContinuous`](#wx.ribbon.RibbonControl.IsSizingContinuous "wx.ribbon.RibbonControl.IsSizingContinuous")




See also


[`DoGetNextLargerSize`](#wx.ribbon.RibbonControl.DoGetNextLargerSize "wx.ribbon.RibbonControl.DoGetNextLargerSize")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def GetNextSmallerSize(self, *args, **kw) -> 'Size':
        """ 

`GetNextSmallerSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonControl.GetNextSmallerSize "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetNextSmallerSize** *(self, direction)*


If sizing is not continuous, then return a suitable size for the control which is smaller than the current size.



Parameters
**direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) – The direction(s) in which the size should reduce.



Return type
`Size`



Returns
The current size if there is no smaller size, otherwise a suitable size which is smaller in the given direction(s), and the same as the current size in the other direction (if any).





See also


[`IsSizingContinuous`](#wx.ribbon.RibbonControl.IsSizingContinuous "wx.ribbon.RibbonControl.IsSizingContinuous")





---

  



**GetNextSmallerSize** *(self, direction, relative\_to)*


If sizing is not continuous, then return a suitable size for the control which is smaller than the given size.



Parameters
* **direction** ([*Orientation*](wx.Orientation.enumeration.html "Orientation")) – The direction(s) in which the size should reduce.
* **relative\_to** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size for which a smaller size should be found.



Return type
`Size`



Returns
*relative\_to* if there is no smaller size, otherwise a suitable size which is smaller in the given direction(s), and the same as *relative\_to* in the other direction (if any).





See also


[`IsSizingContinuous`](#wx.ribbon.RibbonControl.IsSizingContinuous "wx.ribbon.RibbonControl.IsSizingContinuous")




See also


[`DoGetNextSmallerSize`](#wx.ribbon.RibbonControl.DoGetNextSmallerSize "wx.ribbon.RibbonControl.DoGetNextSmallerSize")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def IsSizingContinuous(self) -> bool:
        """ 

`IsSizingContinuous`(*self*)[¶](#wx.ribbon.RibbonControl.IsSizingContinuous "Permalink to this definition")

Return type
*bool*



Returns
`True` if this window can take any size (greater than its minimum size), `False` if it can only take certain sizes.





See also


[`GetNextSmallerSize`](#wx.ribbon.RibbonControl.GetNextSmallerSize "wx.ribbon.RibbonControl.GetNextSmallerSize")




See also


[`GetNextLargerSize`](#wx.ribbon.RibbonControl.GetNextLargerSize "wx.ribbon.RibbonControl.GetNextLargerSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def Realise(self) -> bool:
        """ 

`Realise`(*self*)[¶](#wx.ribbon.RibbonControl.Realise "Permalink to this definition")
Alias for [`Realize`](#wx.ribbon.RibbonControl.Realize "wx.ribbon.RibbonControl.Realize") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonControl.Realize "Permalink to this definition")
Perform initial size and layout calculations after children have been added, and/or realize children.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.ribbon.RibbonControl.SetArtProvider "Permalink to this definition")
Set the art provider to be used.


In many cases, setting the art provider will also set the art provider on all child windows which extend  [wx.ribbon.RibbonControl](#wx-ribbon-ribboncontrol).


In most cases, controls will not take ownership of the given pointer, with the notable exception being [`wx.ribbon.RibbonBar.SetArtProvider`](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar.SetArtProvider "wx.ribbon.RibbonBar.SetArtProvider") .



Parameters
**art** ([*wx.ribbon.RibbonArtProvider*](wx.ribbon.RibbonArtProvider.html#wx.ribbon.RibbonArtProvider "wx.ribbon.RibbonArtProvider")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonControl.html
        """

    AncestorRibbonBar: 'RibbonBar'  # `AncestorRibbonBar`[¶](#wx.ribbon.RibbonControl.AncestorRibbonBar "Permalink to this definition")See [`GetAncestorRibbonBar`](#wx.ribbon.RibbonControl.GetAncestorRibbonBar "wx.ribbon.RibbonControl.GetAncestorRibbonBar")
    ArtProvider: 'RibbonArtProvider'  # `ArtProvider`[¶](#wx.ribbon.RibbonControl.ArtProvider "Permalink to this definition")See [`GetArtProvider`](#wx.ribbon.RibbonControl.GetArtProvider "wx.ribbon.RibbonControl.GetArtProvider") and [`SetArtProvider`](#wx.ribbon.RibbonControl.SetArtProvider "wx.ribbon.RibbonControl.SetArtProvider")



RIBBON_PANEL_FLEXIBLE: int

class RibbonBarEvent(NotifyEvent):
    """ **Possible constructors**:



```
RibbonBarEvent(command_type=wxEVT_NULL, win_id=0, page=None)

```


Event used to indicate various actions relating to a RibbonBar.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
    """
    def __init__(self, command_type=wxEVT_NULL, win_id=0, page=None) -> None:
        """ 

`__init__`(*self*, *command\_type=wxEVT\_NULL*, *win\_id=0*, *page=None*)[¶](#wx.ribbon.RibbonBarEvent.__init__ "Permalink to this definition")
Constructor.



Parameters
* **command\_type** (*wx.EventType*) –
* **win\_id** (*int*) –
* **page** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    def GetPage(self) -> 'RibbonPage':
        """ 

`GetPage`(*self*)[¶](#wx.ribbon.RibbonBarEvent.GetPage "Permalink to this definition")
Returns the page being changed to, or being clicked on.



Return type
 [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    def SetPage(self, page: 'ribbon.RibbonPage') -> None:
        """ 

`SetPage`(*self*, *page*)[¶](#wx.ribbon.RibbonBarEvent.SetPage "Permalink to this definition")
Sets the page relating to this event.



Parameters
**page** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBarEvent.html
        """

    Page: 'RibbonPage'  # `Page`[¶](#wx.ribbon.RibbonBarEvent.Page "Permalink to this definition")See [`GetPage`](#wx.ribbon.RibbonBarEvent.GetPage "wx.ribbon.RibbonBarEvent.GetPage") and [`SetPage`](#wx.ribbon.RibbonBarEvent.SetPage "wx.ribbon.RibbonBarEvent.SetPage")



class RibbonButtonBar(RibbonControl):
    """ **Possible constructors**:



```
RibbonButtonBar()

RibbonButtonBar(parent, id=ID_ANY, pos=DefaultPosition,
                size=DefaultSize, style=0)

```


A ribbon button bar is similar to a traditional toolbar.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonButtonBar.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonButtonBar.Create "wx.ribbon.RibbonButtonBar.Create") should be called in order to create the button bar.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*


Construct a ribbon button bar with the given parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window for the button bar (typically a  [wx.ribbon.RibbonPanel](wx.ribbon.RibbonPanel.html#wx-ribbon-ribbonpanel)).
* **id** (*wx.WindowID*) – An identifier for the button bar. `ID_ANY` is taken to mean a default.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position of the button bar.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size of the button bar.
* **style** (*long*) – Button bar style, currently unused.






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddButton(self, *args, **kw) -> 'RibbonButtonBarButtonBase':
        """ 

`AddButton`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonButtonBar.AddButton "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddButton** *(self, button\_id, label, bitmap, help\_string, kind=RIBBON\_BUTTON\_NORMAL)*


Add a button to the button bar (simple version).



Parameters
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) –



Return type
*RibbonButtonBarButtonBase*






---

  



**AddButton** *(self, button\_id, label, bitmap, bitmap\_small=NullBitmap, bitmap\_disabled=NullBitmap, bitmap\_small\_disabled=NullBitmap, kind=RIBBON\_BUTTON\_NORMAL, help\_string=””)*


Add a button to the button bar.



Parameters
* **button\_id** (*int*) – `ID` of the new button (used for event callbacks).
* **label** (*string*) – Label of the new button.
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button. Must be the same size as all other large bitmaps used on the button bar.
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button. If left as null, then a small bitmap will be automatically generated. Must be the same size as all other small bitmaps used on the button bar.
* **bitmap\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap*.
* **bitmap\_small\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap\_small*.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button to add.
* **help\_string** (*string*) – The UI help string to associate with the new button.



Return type
*RibbonButtonBarButtonBase*



Returns
An opaque pointer which can be used only with other button bar methods.





See also


[`AddDropdownButton`](#wx.ribbon.RibbonButtonBar.AddDropdownButton "wx.ribbon.RibbonButtonBar.AddDropdownButton")




See also


[`AddHybridButton`](#wx.ribbon.RibbonButtonBar.AddHybridButton "wx.ribbon.RibbonButtonBar.AddHybridButton")




See also


[`AddToggleButton`](#wx.ribbon.RibbonButtonBar.AddToggleButton "wx.ribbon.RibbonButtonBar.AddToggleButton")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddDropdownButton(self, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`AddDropdownButton`(*self*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.AddDropdownButton "Permalink to this definition")
Add a dropdown button to the button bar (simple version).



Parameters
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddHybridButton(self, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`AddHybridButton`(*self*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.AddHybridButton "Permalink to this definition")
Add a hybrid button to the button bar (simple version).



Parameters
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def AddToggleButton(self, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`AddToggleButton`(*self*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.AddToggleButton "Permalink to this definition")
Add a toggle button to the button bar (simple version).



Parameters
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def ClearButtons(self) -> None:
        """ 

`ClearButtons`(*self*)[¶](#wx.ribbon.RibbonButtonBar.ClearButtons "Permalink to this definition")
Delete all buttons from the button bar.



See also


[`DeleteButton`](#wx.ribbon.RibbonButtonBar.DeleteButton "wx.ribbon.RibbonButtonBar.DeleteButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.ribbon.RibbonButtonBar.Create "Permalink to this definition")
Create a button bar in two-step button bar construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def DeleteButton(self, button_id: int) -> bool:
        """ 

`DeleteButton`(*self*, *button\_id*)[¶](#wx.ribbon.RibbonButtonBar.DeleteButton "Permalink to this definition")
Delete a single button from the button bar.


The corresponding button is deleted by this function, so any pointers to it previously obtained by [`GetItem`](#wx.ribbon.RibbonButtonBar.GetItem "wx.ribbon.RibbonButtonBar.GetItem") or [`GetItemById`](#wx.ribbon.RibbonButtonBar.GetItemById "wx.ribbon.RibbonButtonBar.GetItemById") become invalid.



Parameters
**button\_id** (*int*) – 



Return type
*bool*





See also


[`ClearButtons`](#wx.ribbon.RibbonButtonBar.ClearButtons "wx.ribbon.RibbonButtonBar.ClearButtons")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def EnableButton(self, button_id, enable=True) -> None:
        """ 

`EnableButton`(*self*, *button\_id*, *enable=True*)[¶](#wx.ribbon.RibbonButtonBar.EnableButton "Permalink to this definition")
Enable or disable a single button on the bar.



Parameters
* **button\_id** (*int*) – `ID` of the button to enable or disable.
* **enable** (*bool*) – `True` to enable the button, `False` to disable it.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetActiveItem(self) -> 'RibbonButtonBarButtonBase':
        """ 

`GetActiveItem`(*self*)[¶](#wx.ribbon.RibbonButtonBar.GetActiveItem "Permalink to this definition")
Returns the active item of the button bar or `None` if there is none.


The active button is the one being clicked.



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetButtonCount(self) -> int:
        """ 

`GetButtonCount`(*self*)[¶](#wx.ribbon.RibbonButtonBar.GetButtonCount "Permalink to this definition")
Returns the number of buttons in this button bar.



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonButtonBar.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetHoveredItem(self) -> 'RibbonButtonBarButtonBase':
        """ 

`GetHoveredItem`(*self*)[¶](#wx.ribbon.RibbonButtonBar.GetHoveredItem "Permalink to this definition")
Returns the hovered item of the button bar or `None` if there is none.


The hovered button is the one the mouse is over.



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItem(self, n: int) -> 'RibbonButtonBarButtonBase':
        """ 

`GetItem`(*self*, *n*)[¶](#wx.ribbon.RibbonButtonBar.GetItem "Permalink to this definition")
Returns the N-th button of the bar.



Parameters
**n** (*int*) – 



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.5.




See also


[`GetButtonCount`](#wx.ribbon.RibbonButtonBar.GetButtonCount "wx.ribbon.RibbonButtonBar.GetButtonCount")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemById(self, id: int) -> 'RibbonButtonBarButtonBase':
        """ 

`GetItemById`(*self*, *id*)[¶](#wx.ribbon.RibbonButtonBar.GetItemById "Permalink to this definition")
Returns the first button having a given id or `None` if none matches.



Parameters
**id** (*int*) – 



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemClientData(self, item: RibbonButtonBarButtonBase) -> 'ClientData':
        """ 

`GetItemClientData`(*self*, *item*)[¶](#wx.ribbon.RibbonButtonBar.GetItemClientData "Permalink to this definition")
Get the client object associated with a button.



Parameters
**item** ([*RibbonButtonBarButtonBase*](wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase.html#wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase "wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase")) – 



Return type
*ClientData*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemId(self, item: RibbonButtonBarButtonBase) -> int:
        """ 

`GetItemId`(*self*, *item*)[¶](#wx.ribbon.RibbonButtonBar.GetItemId "Permalink to this definition")
Returns the id of a button.



Parameters
**item** ([*RibbonButtonBarButtonBase*](wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase.html#wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase "wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase")) – 



Return type
*int*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetItemRect(self, button_id: int) -> 'Rect':
        """ 

`GetItemRect`(*self*, *button\_id*)[¶](#wx.ribbon.RibbonButtonBar.GetItemRect "Permalink to this definition")
Returns the items’s rect with coordinates relative to the button bar’s parent, or a default-constructed rect if the tool is not found.



Parameters
**button\_id** (*int*) – `ID` of the button in question.



Return type
`Rect`





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def GetShowToolTipsForDisabled(self) -> bool:
        """ 

`GetShowToolTipsForDisabled`(*self*)[¶](#wx.ribbon.RibbonButtonBar.GetShowToolTipsForDisabled "Permalink to this definition")
Sets whether tooltips should be shown for disabled buttons or not.


You may wish to show it to explain why a button is disabled or what it normally does when enabled.



Return type
*bool*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertButton(self, *args, **kw) -> 'RibbonButtonBarButtonBase':
        """ 

`InsertButton`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonButtonBar.InsertButton "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**InsertButton** *(self, pos, button\_id, label, bitmap, help\_string, kind=RIBBON\_BUTTON\_NORMAL)*


Inserts a button to the button bar (simple version) at the given position.



Parameters
* **pos** (*int*) –
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) –



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.4.




See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





---

  



**InsertButton** *(self, pos, button\_id, label, bitmap, bitmap\_small=NullBitmap, bitmap\_disabled=NullBitmap, bitmap\_small\_disabled=NullBitmap, kind=RIBBON\_BUTTON\_NORMAL, help\_string=””)*


Insert a button to the button bar at the given position.



Parameters
* **pos** (*int*) – Position of the new button in the button bar.
* **button\_id** (*int*) – `ID` of the new button (used for event callbacks).
* **label** (*string*) – Label of the new button.
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button. Must be the same size as all other large bitmaps used on the button bar.
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button. If left as null, then a small bitmap will be automatically generated. Must be the same size as all other small bitmaps used on the button bar.
* **bitmap\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap*.
* **bitmap\_small\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap\_small*.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button to add.
* **help\_string** (*string*) – The UI help string to associate with the new button.



Return type
*RibbonButtonBarButtonBase*



Returns
An opaque pointer which can be used only with other button bar methods.





New in version 2.9.4.




See also


[`InsertDropdownButton`](#wx.ribbon.RibbonButtonBar.InsertDropdownButton "wx.ribbon.RibbonButtonBar.InsertDropdownButton")




See also


[`InsertHybridButton`](#wx.ribbon.RibbonButtonBar.InsertHybridButton "wx.ribbon.RibbonButtonBar.InsertHybridButton")




See also


[`InsertToggleButton`](#wx.ribbon.RibbonButtonBar.InsertToggleButton "wx.ribbon.RibbonButtonBar.InsertToggleButton")




See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertDropdownButton(self, pos, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`InsertDropdownButton`(*self*, *pos*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.InsertDropdownButton "Permalink to this definition")
Inserts a dropdown button to the button bar (simple version) at the given position.



Parameters
* **pos** (*int*) –
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.4.




See also


[`InsertButton`](#wx.ribbon.RibbonButtonBar.InsertButton "wx.ribbon.RibbonButtonBar.InsertButton")




See also


[`AddDropdownButton`](#wx.ribbon.RibbonButtonBar.AddDropdownButton "wx.ribbon.RibbonButtonBar.AddDropdownButton")




See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertHybridButton(self, pos, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`InsertHybridButton`(*self*, *pos*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.InsertHybridButton "Permalink to this definition")
Inserts a hybrid button to the button bar (simple version) at the given position.



Parameters
* **pos** (*int*) –
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.4.




See also


[`InsertButton`](#wx.ribbon.RibbonButtonBar.InsertButton "wx.ribbon.RibbonButtonBar.InsertButton")




See also


[`AddHybridButton`](#wx.ribbon.RibbonButtonBar.AddHybridButton "wx.ribbon.RibbonButtonBar.AddHybridButton")




See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def InsertToggleButton(self, pos, button_id, label, bitmap, help_string="") -> 'RibbonButtonBarButtonBase':
        """ 

`InsertToggleButton`(*self*, *pos*, *button\_id*, *label*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonButtonBar.InsertToggleButton "Permalink to this definition")
Inserts a toggle button to the button bar (simple version) at the given position.



Parameters
* **pos** (*int*) –
* **button\_id** (*int*) –
* **label** (*string*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonButtonBarButtonBase*





New in version 2.9.4.




See also


[`InsertButton`](#wx.ribbon.RibbonButtonBar.InsertButton "wx.ribbon.RibbonButtonBar.InsertButton")




See also


[`AddToggleButton`](#wx.ribbon.RibbonButtonBar.AddToggleButton "wx.ribbon.RibbonButtonBar.AddToggleButton")




See also


[`AddButton`](#wx.ribbon.RibbonButtonBar.AddButton "wx.ribbon.RibbonButtonBar.AddButton")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonButtonBar.Realize "Permalink to this definition")
Calculate button layouts and positions.


Must be called after buttons are added to the button bar, as otherwise the newly added buttons will not be displayed. In normal situations, it will be called automatically when [`wx.ribbon.RibbonBar.Realize`](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar.Realize "wx.ribbon.RibbonBar.Realize") is called.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonIcon(self, button_id, bitmap, bitmap_small=NullBitmap, bitmap_disabled=NullBitmap, bitmap_small_disabled=NullBitmap) -> None:
        """ 

`SetButtonIcon`(*self*, *button\_id*, *bitmap*, *bitmap\_small=NullBitmap*, *bitmap\_disabled=NullBitmap*, *bitmap\_small\_disabled=NullBitmap*)[¶](#wx.ribbon.RibbonButtonBar.SetButtonIcon "Permalink to this definition")
Changes the bitmap of an existing button.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button. Must be the same size as all other large bitmaps used on the button bar.
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button. If left as null, then a small bitmap will be automatically generated. Must be the same size as all other small bitmaps used on the button bar.
* **bitmap\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Large bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap*.
* **bitmap\_small\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Small bitmap of the new button when it is disabled. If left as null, then a bitmap will be automatically generated from *bitmap\_small*.





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonMaxSizeClass(self, button_id, max_size_class) -> None:
        """ 

`SetButtonMaxSizeClass`(*self*, *button\_id*, *max\_size\_class*)[¶](#wx.ribbon.RibbonButtonBar.SetButtonMaxSizeClass "Permalink to this definition")
Sets the maximum size class of a ribbon button.


You have to call [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") after calling this function to apply the given maximum size.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **max\_size\_class** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The maximum size-class of the button. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`.





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonMinSizeClass(self, button_id, min_size_class) -> None:
        """ 

`SetButtonMinSizeClass`(*self*, *button\_id*, *min\_size\_class*)[¶](#wx.ribbon.RibbonButtonBar.SetButtonMinSizeClass "Permalink to this definition")
Sets the minimum size class of a ribbon button.


You have to call [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") after calling this function to apply the given minimum size.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **min\_size\_class** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The minimum size-class of the button. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`.





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonText(self, button_id, label) -> None:
        """ 

`SetButtonText`(*self*, *button\_id*, *label*)[¶](#wx.ribbon.RibbonButtonBar.SetButtonText "Permalink to this definition")
Changes the label text of an existing button.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **label** (*string*) – New label of the button.





New in version 4.1/wxWidgets-3.1.2.




Note


If text size has changed, [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") must be called on the top level  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) object to recalculate panel sizes. Use [`SetButtonTextMinWidth`](#wx.ribbon.RibbonButtonBar.SetButtonTextMinWidth "wx.ribbon.RibbonButtonBar.SetButtonTextMinWidth") to avoid calling [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") after every change.




See also


[`SetButtonTextMinWidth`](#wx.ribbon.RibbonButtonBar.SetButtonTextMinWidth "wx.ribbon.RibbonButtonBar.SetButtonTextMinWidth")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetButtonTextMinWidth(self, *args, **kw) -> None:
        """ 

`SetButtonTextMinWidth`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonButtonBar.SetButtonTextMinWidth "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetButtonTextMinWidth** *(self, button\_id, min\_width\_medium, min\_width\_large)*


Sets the minimum width of the button label, to indicate to the  [wx.ribbon.RibbonArtProvider](wx.ribbon.RibbonArtProvider.html#wx-ribbon-ribbonartprovider) layout mechanism that this is the minimum required size.


You have to call [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") after calling this function to apply the given minimum width.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **min\_width\_medium** (*int*) – Requested minimum width of the button text in pixel if the button is medium size.
* **min\_width\_large** (*int*) – Requested minimum width of the button text in pixel if the button is large size.





New in version 4.1/wxWidgets-3.1.2.




Note


This function is used together with [`SetButtonText`](#wx.ribbon.RibbonButtonBar.SetButtonText "wx.ribbon.RibbonButtonBar.SetButtonText") to change button labels on the fly without modifying the button bar layout.




See also


[`SetButtonText`](#wx.ribbon.RibbonButtonBar.SetButtonText "wx.ribbon.RibbonButtonBar.SetButtonText")





---

  



**SetButtonTextMinWidth** *(self, button\_id, label)*


Sets the minimum width of the button label, to indicate to the  [wx.ribbon.RibbonArtProvider](wx.ribbon.RibbonArtProvider.html#wx-ribbon-ribbonartprovider) layout mechanism that this is the minimum required size.


You have to call [`Realize`](#wx.ribbon.RibbonButtonBar.Realize "wx.ribbon.RibbonButtonBar.Realize") after calling this function to apply the given minimum width.



Parameters
* **button\_id** (*int*) – `ID` of the button to manipulate.
* **label** (*string*) – The minimum width is set to the width of this label.





New in version 4.1/wxWidgets-3.1.2.




Note


This function is used together with [`SetButtonText`](#wx.ribbon.RibbonButtonBar.SetButtonText "wx.ribbon.RibbonButtonBar.SetButtonText") to change button labels on the fly without modifying the button bar layout.




See also


[`SetButtonText`](#wx.ribbon.RibbonButtonBar.SetButtonText "wx.ribbon.RibbonButtonBar.SetButtonText")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetItemClientData(self, item, data) -> None:
        """ 

`SetItemClientData`(*self*, *item*, *data*)[¶](#wx.ribbon.RibbonButtonBar.SetItemClientData "Permalink to this definition")
Set the client object associated with a button.


The button bar owns the given object and takes care of its deletion. Please, note that you cannot use both client object and client data.



Parameters
* **item** ([*RibbonButtonBarButtonBase*](wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase.html#wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase "wx.lib.agw.ribbon.buttonbar.RibbonButtonBarButtonBase")) –
* **data** (*ClientData*) –





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def SetShowToolTipsForDisabled(self, show: bool) -> None:
        """ 

`SetShowToolTipsForDisabled`(*self*, *show*)[¶](#wx.ribbon.RibbonButtonBar.SetShowToolTipsForDisabled "Permalink to this definition")
Indicates whether tooltips are shown for disabled buttons.


By default they are not shown.



Parameters
**show** (*bool*) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    def ToggleButton(self, button_id, checked) -> None:
        """ 

`ToggleButton`(*self*, *button\_id*, *checked*)[¶](#wx.ribbon.RibbonButtonBar.ToggleButton "Permalink to this definition")
Set a toggle button to the checked or unchecked state.



Parameters
* **button\_id** (*int*) – `ID` of the toggle button to manipulate.
* **checked** (*bool*) – `True` to set the button to the toggled/pressed/checked state, `False` to set it to the untoggled/unpressed/unchecked state.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonButtonBar.html
        """

    ActiveItem: 'RibbonButtonBarButtonBase'  # `ActiveItem`[¶](#wx.ribbon.RibbonButtonBar.ActiveItem "Permalink to this definition")See [`GetActiveItem`](#wx.ribbon.RibbonButtonBar.GetActiveItem "wx.ribbon.RibbonButtonBar.GetActiveItem")
    ButtonCount: int  # `ButtonCount`[¶](#wx.ribbon.RibbonButtonBar.ButtonCount "Permalink to this definition")See [`GetButtonCount`](#wx.ribbon.RibbonButtonBar.GetButtonCount "wx.ribbon.RibbonButtonBar.GetButtonCount")
    HoveredItem: 'RibbonButtonBarButtonBase'  # `HoveredItem`[¶](#wx.ribbon.RibbonButtonBar.HoveredItem "Permalink to this definition")See [`GetHoveredItem`](#wx.ribbon.RibbonButtonBar.GetHoveredItem "wx.ribbon.RibbonButtonBar.GetHoveredItem")
    ShowToolTipsForDisabled: bool  # `ShowToolTipsForDisabled`[¶](#wx.ribbon.RibbonButtonBar.ShowToolTipsForDisabled "Permalink to this definition")See [`GetShowToolTipsForDisabled`](#wx.ribbon.RibbonButtonBar.GetShowToolTipsForDisabled "wx.ribbon.RibbonButtonBar.GetShowToolTipsForDisabled") and [`SetShowToolTipsForDisabled`](#wx.ribbon.RibbonButtonBar.SetShowToolTipsForDisabled "wx.ribbon.RibbonButtonBar.SetShowToolTipsForDisabled")



EVT_RIBBONBUTTONBAR_CLICKED: int  # Triggered when the normal (non-dropdown) region of a button on the button bar is clicked.

EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED: int  # Triggered when the dropdown region of a button on the button bar is clicked. wx.ribbon.RibbonButtonBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown buttons should be doing). ^^

RIBBON_BUTTONBAR_BUTTON_SMALL: int

RIBBON_BUTTONBAR_BUTTON_MEDIUM: int

RIBBON_BUTTONBAR_BUTTON_LARGE: int

class RibbonBar(RibbonControl):
    """ **Possible constructors**:



```
RibbonBar()

RibbonBar(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
          style=RIBBON_BAR_DEFAULT_STYLE)

```


Top-level control in a ribbon user interface.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonBar.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonBar.Create "wx.ribbon.RibbonBar.Create") should be called in order to create the ribbon bar.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=RIBBON\_BAR\_DEFAULT\_STYLE)*


Construct a ribbon bar with the given parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def AddPageHighlight(self, page, highlight=True) -> None:
        """ 

`AddPageHighlight`(*self*, *page*, *highlight=True*)[¶](#wx.ribbon.RibbonBar.AddPageHighlight "Permalink to this definition")
Highlight the specified tab.


Highlighted tabs have a colour between that of the active tab and a tab over which the mouse is hovering. This can be used to make a tab (usually temporarily) more noticeable to the user.



Parameters
* **page** (*int*) –
* **highlight** (*bool*) –





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ArePanelsShown(self) -> bool:
        """ 

`ArePanelsShown`(*self*)[¶](#wx.ribbon.RibbonBar.ArePanelsShown "Permalink to this definition")
Indicates whether the panel area of the ribbon bar is shown.



Return type
*bool*





New in version 2.9.2.




See also


[`ShowPanels`](#wx.ribbon.RibbonBar.ShowPanels "wx.ribbon.RibbonBar.ShowPanels")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ClearPages(self) -> None:
        """ 

`ClearPages`(*self*)[¶](#wx.ribbon.RibbonBar.ClearPages "Permalink to this definition")
Delete all pages from the ribbon bar.



New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=RIBBON_BAR_DEFAULT_STYLE) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=RIBBON\_BAR\_DEFAULT\_STYLE*)[¶](#wx.ribbon.RibbonBar.Create "Permalink to this definition")
Create a ribbon bar in two-step ribbon bar construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def DeletePage(self, n: int) -> None:
        """ 

`DeletePage`(*self*, *n*)[¶](#wx.ribbon.RibbonBar.DeletePage "Permalink to this definition")
Delete a single page from this ribbon bar.


The user must call [`wx.ribbon.RibbonBar.Realize`](#wx.ribbon.RibbonBar.Realize "wx.ribbon.RibbonBar.Realize") after one (or more) calls to this function.



Parameters
**n** (*int*) – 





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def DismissExpandedPanel(self) -> bool:
        """ 

`DismissExpandedPanel`(*self*)[¶](#wx.ribbon.RibbonBar.DismissExpandedPanel "Permalink to this definition")
Dismiss the expanded panel of the currently active page.


Calls and returns the value from [`wx.ribbon.RibbonPage.DismissExpandedPanel`](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage.DismissExpandedPanel "wx.ribbon.RibbonPage.DismissExpandedPanel") for the currently active page, or `False` if there is no active page.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetActivePage(self) -> int:
        """ 

`GetActivePage`(*self*)[¶](#wx.ribbon.RibbonBar.GetActivePage "Permalink to this definition")
Get the index of the active page.


In the rare case of no page being active, -1 is returned.



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonBar.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetDisplayMode(self) -> 'RibbonDisplayMode':
        """ 

`GetDisplayMode`(*self*)[¶](#wx.ribbon.RibbonBar.GetDisplayMode "Permalink to this definition")
Returns the current display mode of the panel area.



Return type
 [wx.ribbon.RibbonDisplayMode](wx.ribbon.RibbonDisplayMode.enumeration.html#wx-ribbon-ribbondisplaymode)





New in version 4.1/wxWidgets-3.1.0.




See also


[`ShowPanels`](#wx.ribbon.RibbonBar.ShowPanels "wx.ribbon.RibbonBar.ShowPanels")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPage(self, n: int) -> 'RibbonPage':
        """ 

`GetPage`(*self*, *n*)[¶](#wx.ribbon.RibbonBar.GetPage "Permalink to this definition")
Get a page by index.


`None` will be returned if the given index is out of range.



Parameters
**n** (*int*) – 



Return type
 [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPageCount(self) -> int:
        """ 

`GetPageCount`(*self*)[¶](#wx.ribbon.RibbonBar.GetPageCount "Permalink to this definition")
Get the number of pages in this bar.



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def GetPageNumber(self, page: 'ribbon.RibbonPage') -> int:
        """ 

`GetPageNumber`(*self*, *page*)[¶](#wx.ribbon.RibbonBar.GetPageNumber "Permalink to this definition")
Returns the number for a given ribbon bar page.


The number can be used in other ribbon bar calls.



Parameters
**page** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) – 



Return type
*int*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def HidePage(self, page: int) -> None:
        """ 

`HidePage`(*self*, *page*)[¶](#wx.ribbon.RibbonBar.HidePage "Permalink to this definition")
Hides the tab for a given page.


Equivalent to `ShowPage(page, false)` .



Parameters
**page** (*int*) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def HidePanels(self) -> None:
        """ 

`HidePanels`(*self*)[¶](#wx.ribbon.RibbonBar.HidePanels "Permalink to this definition")
Hides the panel area of the ribbon bar.


This method behaves like [`ShowPanels`](#wx.ribbon.RibbonBar.ShowPanels "wx.ribbon.RibbonBar.ShowPanels") with `False` argument.



New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def IsPageHighlighted(self, page: int) -> bool:
        """ 

`IsPageHighlighted`(*self*, *page*)[¶](#wx.ribbon.RibbonBar.IsPageHighlighted "Permalink to this definition")
Indicates whether a tab is currently highlighted.



Parameters
**page** (*int*) – 



Return type
*bool*





New in version 2.9.5.




See also


[`AddPageHighlight`](#wx.ribbon.RibbonBar.AddPageHighlight "wx.ribbon.RibbonBar.AddPageHighlight")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def IsPageShown(self, page: int) -> bool:
        """ 

`IsPageShown`(*self*, *page*)[¶](#wx.ribbon.RibbonBar.IsPageShown "Permalink to this definition")
Indicates whether the tab for the given page is shown to the user or not.


By default all page tabs are shown.



Parameters
**page** (*int*) – 



Return type
*bool*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonBar.Realize "Permalink to this definition")
Perform initial layout and size calculations of the bar and its children.


This must be called after all of the bar’s children have been created (and their children created, etc.) - if it is not, then windows may not be laid out or sized correctly.


Also calls [`wx.ribbon.RibbonPage.Realize`](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage.Realize "wx.ribbon.RibbonPage.Realize") on each child page.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def RemovePageHighlight(self, page: int) -> None:
        """ 

`RemovePageHighlight`(*self*, *page*)[¶](#wx.ribbon.RibbonBar.RemovePageHighlight "Permalink to this definition")
Changes a tab to not be highlighted.



Parameters
**page** (*int*) – 





New in version 2.9.5.




See also


[`AddPageHighlight`](#wx.ribbon.RibbonBar.AddPageHighlight "wx.ribbon.RibbonBar.AddPageHighlight")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetActivePage(self, *args, **kw) -> bool:
        """ 

`SetActivePage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonBar.SetActivePage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetActivePage** *(self, page)*


Set the active page by index, without triggering any events.



Parameters
**page** (*int*) – The zero-based index of the page to activate.



Return type
*bool*



Returns
`True` if the specified page is now active, `False` if it could not be activated (for example because the page index is invalid).






---

  



**SetActivePage** *(self, page)*


Set the active page, without triggering any events.



Parameters
**page** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) – The page to activate.



Return type
*bool*



Returns
`True` if the specified page is now active, `False` if it could not be activated (for example because the given page is not a child of the ribbon bar).






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.ribbon.RibbonBar.SetArtProvider "Permalink to this definition")
Set the art provider to be used be the ribbon bar.


Also sets the art provider on all current  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) children, and any  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) children added in the future.


Note that unlike most other ribbon controls, the ribbon bar creates a default art provider when initialised, so an explicit call to [`SetArtProvider`](#wx.ribbon.RibbonBar.SetArtProvider "wx.ribbon.RibbonBar.SetArtProvider") is not required if the default art provider is sufficient. Also, unlike other ribbon controls, the ribbon bar takes ownership of the given pointer, and will delete it when the art provider is changed or the bar is destroyed. If this behaviour is not desired, then clone the art provider before setting it.



Parameters
**art** ([*wx.ribbon.RibbonArtProvider*](wx.ribbon.RibbonArtProvider.html#wx.ribbon.RibbonArtProvider "wx.ribbon.RibbonArtProvider")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def SetTabCtrlMargins(self, left, right) -> None:
        """ 

`SetTabCtrlMargins`(*self*, *left*, *right*)[¶](#wx.ribbon.RibbonBar.SetTabCtrlMargins "Permalink to this definition")
Set the margin widths (in pixels) on the left and right sides of the tab bar region of the ribbon bar.


These margins will be painted with the tab background, but tabs and scroll buttons will never be painted in the margins.


The left margin could be used for rendering something equivalent to the “Office Button”, though this is not currently implemented. The right margin could be used for rendering a help button, and/or MDI buttons, but again, this is not currently implemented.



Parameters
* **left** (*int*) –
* **right** (*int*) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ShowPage(self, page, show_tab=True) -> None:
        """ 

`ShowPage`(*self*, *page*, *show\_tab=True*)[¶](#wx.ribbon.RibbonBar.ShowPage "Permalink to this definition")
Show or hide the tab for a given page.


After showing or hiding a tab, you need to call [`wx.ribbon.RibbonBar.Realize`](#wx.ribbon.RibbonBar.Realize "wx.ribbon.RibbonBar.Realize") . If you hide the tab for the currently active page (GetActivePage) then you should call SetActivePage to activate a different page.



Parameters
* **page** (*int*) –
* **show\_tab** (*bool*) –





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    def ShowPanels(self, *args, **kw) -> None:
        """ 

`ShowPanels`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonBar.ShowPanels "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ShowPanels** *(self, mode)*


Shows or hide the panel area of the ribbon bar according to the given display mode.



Parameters
**mode** ([*RibbonDisplayMode*](wx.ribbon.RibbonDisplayMode.enumeration.html "RibbonDisplayMode")) – 





New in version 4.1/wxWidgets-3.1.0.





---

  



**ShowPanels** *(self, show=True)*


Shows or hides the panel area of the ribbon bar.


If the panel area is hidden, then only the tab of the ribbon bar will be shown. This is useful for giving the user more screen space to work with when he/she doesn’t need to see the ribbon’s options.


If the panel is currently shown, this method pins it, use the other overload of this method to specify the exact panel display mode to avoid it.



Parameters
**show** (*bool*) – 





New in version 2.9.2.





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonBar.html
        """

    ActivePage: int  # `ActivePage`[¶](#wx.ribbon.RibbonBar.ActivePage "Permalink to this definition")See [`GetActivePage`](#wx.ribbon.RibbonBar.GetActivePage "wx.ribbon.RibbonBar.GetActivePage") and [`SetActivePage`](#wx.ribbon.RibbonBar.SetActivePage "wx.ribbon.RibbonBar.SetActivePage")
    DisplayMode: 'RibbonDisplayMode'  # `DisplayMode`[¶](#wx.ribbon.RibbonBar.DisplayMode "Permalink to this definition")See [`GetDisplayMode`](#wx.ribbon.RibbonBar.GetDisplayMode "wx.ribbon.RibbonBar.GetDisplayMode")
    PageCount: int  # `PageCount`[¶](#wx.ribbon.RibbonBar.PageCount "Permalink to this definition")See [`GetPageCount`](#wx.ribbon.RibbonBar.GetPageCount "wx.ribbon.RibbonBar.GetPageCount")



RIBBON_BAR_DEFAULT_STYLE: int  # Defined as wx.ribbon.RIBBON_BAR_FLOW_HORIZONTAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_LABELS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_TOGGLE_BUTTON | wx.ribbon.RIBBON_BAR_SHOW_HELP_BUTTON.

RIBBON_BAR_FOLDBAR_STYLE: int  # Defined as wx.ribbon.RIBBON_BAR_FLOW_VERTICAL | wx.ribbon.RIBBON_BAR_SHOW_PAGE_ICONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS | wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS

RIBBON_BAR_SHOW_PAGE_LABELS: int  # Causes labels to be shown on the tabs in the ribbon bar.

RIBBON_BAR_SHOW_PAGE_ICONS: int  # Causes icons to be shown on the tabs in the ribbon bar.

RIBBON_BAR_FLOW_HORIZONTAL: int  # Causes panels within pages to stack horizontally.

RIBBON_BAR_FLOW_VERTICAL: int  # Causes panels within pages to stack vertically.

RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS: int  # Causes extension buttons to be shown on panels (where the panel has such a button).

RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS: int  # Causes minimise buttons to be shown on panels (where the panel has such a button).

RIBBON_BAR_SHOW_TOGGLE_BUTTON: int  # Causes a toggle button to appear on the ribbon bar at top-right corner. This style is new since wxWidgets 2.9.5.

RIBBON_BAR_SHOW_HELP_BUTTON: int  # Causes a help button to appear on the ribbon bar at the top-right corner. This style is new since wxWidgets 2.9.5. ^^

EVT_RIBBONBAR_PAGE_CHANGED: int  # Triggered after the transition from one page being active to a different page being active.

EVT_RIBBONBAR_PAGE_CHANGING: int  # Triggered prior to the transition from one page being active to a different page being active, and can veto the change.

EVT_RIBBONBAR_TAB_MIDDLE_DOWN: int  # Triggered when the middle mouse button is pressed on a tab.

EVT_RIBBONBAR_TAB_MIDDLE_UP: int  # Triggered when the middle mouse button is released on a tab.

EVT_RIBBONBAR_TAB_RIGHT_DOWN: int  # Triggered when the right mouse button is pressed on a tab.

EVT_RIBBONBAR_TAB_RIGHT_UP: int  # Triggered when the right mouse button is released on a tab.

EVT_RIBBONBAR_TAB_LEFT_DCLICK: int  # Triggered when the left mouse button is double clicked on a tab.

EVT_RIBBONBAR_TOGGLED: int  # Triggered when the button triggering the ribbon bar is clicked. This event is new since wxWidgets 2.9.5.

EVT_RIBBONBAR_HELP_CLICK: int  # Triggered when the help button is clicked. This even is new since wxWidgets 2.9.5. ^^

class RibbonGallery(RibbonControl):
    """ **Possible constructors**:



```
RibbonGallery()

RibbonGallery(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
              style=0)

```


A ribbon gallery is like a ListBox, but for bitmaps rather than
strings.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonGallery.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonGallery.Create "wx.ribbon.RibbonGallery.Create") should be called in order to create the gallery.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*


Construct a ribbon gallery with the given parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window for the gallery (typically a  [wx.ribbon.RibbonPanel](wx.ribbon.RibbonPanel.html#wx-ribbon-ribbonpanel)).
* **id** (*wx.WindowID*) – An identifier for the gallery. `ID_ANY` is taken to mean a default.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position of the gallery.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size of the gallery.
* **style** (*long*) – Gallery style, currently unused.






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Append(self, *args, **kw) -> 'RibbonGalleryItem':
        """ 

`Append`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonGallery.Append "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Append** *(self, bitmap, id)*


Add an item to the gallery (with no client data).



Parameters
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap to display for the item. Note that all items must have equally sized bitmaps.
* **id** (*int*) – `ID` number to associate with the item. Not currently used for anything important.



Return type
*RibbonGalleryItem*






---

  



**Append** *(self, bitmap, id, clientData)*


Add an item to the gallery (with complex client data)



Parameters
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap to display for the item. Note that all items must have equally sized bitmaps.
* **id** (*int*) – `ID` number to associate with the item. Not currently used for anything important.
* **clientData** (*ClientData*) – An object which contains data to associate with the item. The item takes ownership of this pointer, and will delete it when the item client data is changed to something else, or when the item is destroyed.



Return type
*RibbonGalleryItem*






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.ribbon.RibbonGallery.Clear "Permalink to this definition")
Remove all items from the gallery.




            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.ribbon.RibbonGallery.Create "Permalink to this definition")
Create a gallery in two-step gallery construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def EnsureVisible(self, item: RibbonGalleryItem) -> None:
        """ 

`EnsureVisible`(*self*, *item*)[¶](#wx.ribbon.RibbonGallery.EnsureVisible "Permalink to this definition")
Scroll the gallery to ensure that the given item is visible.



Parameters
**item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetActiveItem(self) -> 'RibbonGalleryItem':
        """ 

`GetActiveItem`(*self*)[¶](#wx.ribbon.RibbonGallery.GetActiveItem "Permalink to this definition")
Get the currently active item, or `None` if there is none.


The active item is the item being pressed by the user, and will thus become the selected item if the user releases the mouse button.



Return type
*RibbonGalleryItem*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonGallery.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.ribbon.RibbonGallery.GetCount "Permalink to this definition")
Get the number of items in the gallery.



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetDownButtonState(self) -> 'RibbonGalleryButtonState':
        """ 

`GetDownButtonState`(*self*)[¶](#wx.ribbon.RibbonGallery.GetDownButtonState "Permalink to this definition")
Get the state of the scroll down button.



Return type
 [wx.ribbon.RibbonGalleryButtonState](wx.ribbon.RibbonGalleryButtonState.enumeration.html#wx-ribbon-ribbongallerybuttonstate)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetExtensionButtonState(self) -> 'RibbonGalleryButtonState':
        """ 

`GetExtensionButtonState`(*self*)[¶](#wx.ribbon.RibbonGallery.GetExtensionButtonState "Permalink to this definition")
Get the state of the “extension” button.



Return type
 [wx.ribbon.RibbonGalleryButtonState](wx.ribbon.RibbonGalleryButtonState.enumeration.html#wx-ribbon-ribbongallerybuttonstate)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetHoveredItem(self) -> 'RibbonGalleryItem':
        """ 

`GetHoveredItem`(*self*)[¶](#wx.ribbon.RibbonGallery.GetHoveredItem "Permalink to this definition")
Get the currently hovered item, or `None` if there is none.


The hovered item is the item underneath the mouse cursor.



Return type
*RibbonGalleryItem*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetItem(self, n: int) -> 'RibbonGalleryItem':
        """ 

`GetItem`(*self*, *n*)[¶](#wx.ribbon.RibbonGallery.GetItem "Permalink to this definition")
Get an item by index.



Parameters
**n** (*int*) – 



Return type
*RibbonGalleryItem*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetItemClientData(self, item: RibbonGalleryItem) -> 'ClientData':
        """ 

`GetItemClientData`(*self*, *item*)[¶](#wx.ribbon.RibbonGallery.GetItemClientData "Permalink to this definition")
Get the client object associated with a gallery item.



Parameters
**item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – 



Return type
*ClientData*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetSelection(self) -> 'RibbonGalleryItem':
        """ 

`GetSelection`(*self*)[¶](#wx.ribbon.RibbonGallery.GetSelection "Permalink to this definition")
Get the currently selected item, or `None` if there is none.


The selected item is set by [`SetSelection`](#wx.ribbon.RibbonGallery.SetSelection "wx.ribbon.RibbonGallery.SetSelection") , or by the user clicking on an item.



Return type
*RibbonGalleryItem*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def GetUpButtonState(self) -> 'RibbonGalleryButtonState':
        """ 

`GetUpButtonState`(*self*)[¶](#wx.ribbon.RibbonGallery.GetUpButtonState "Permalink to this definition")
Get the state of the scroll up button.



Return type
 [wx.ribbon.RibbonGalleryButtonState](wx.ribbon.RibbonGalleryButtonState.enumeration.html#wx-ribbon-ribbongallerybuttonstate)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.ribbon.RibbonGallery.IsEmpty "Permalink to this definition")
Query if the gallery has no items in it.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def IsHovered(self) -> bool:
        """ 

`IsHovered`(*self*)[¶](#wx.ribbon.RibbonGallery.IsHovered "Permalink to this definition")
Query is the mouse is currently hovered over the gallery.



Return type
*bool*



Returns
`True` if the cursor is within the bounds of the gallery (not just hovering over an item), `False` otherwise.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def ScrollLines(self, lines: int) -> bool:
        """ 

`ScrollLines`(*self*, *lines*)[¶](#wx.ribbon.RibbonGallery.ScrollLines "Permalink to this definition")
Scroll the gallery contents by some amount.



Parameters
**lines** (*int*) – Positive values scroll toward the end of the gallery, while negative values scroll toward the start.



Return type
*bool*



Returns
`True` if the gallery scrolled at least one pixel in the given direction, `False` if it did not scroll.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def ScrollPixels(self, pixels: int) -> bool:
        """ 

`ScrollPixels`(*self*, *pixels*)[¶](#wx.ribbon.RibbonGallery.ScrollPixels "Permalink to this definition")
Scroll the gallery contents by some fine-grained amount.



Parameters
**pixels** (*int*) – Positive values scroll toward the end of the gallery, while negative values scroll toward the start.



Return type
*bool*



Returns
`True` if the gallery scrolled at least one pixel in the given direction, `False` if it did not scroll.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def SetItemClientData(self, item, data) -> None:
        """ 

`SetItemClientData`(*self*, *item*, *data*)[¶](#wx.ribbon.RibbonGallery.SetItemClientData "Permalink to this definition")
Set the client object associated with a gallery item.



Parameters
* **item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) –
* **data** (*ClientData*) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    def SetSelection(self, item: RibbonGalleryItem) -> None:
        """ 

`SetSelection`(*self*, *item*)[¶](#wx.ribbon.RibbonGallery.SetSelection "Permalink to this definition")
Set the selection to the given item, or removes the selection if *item* == `None`.


Note that this not cause any events to be emitted.



Parameters
**item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonGallery.html
        """

    ActiveItem: 'RibbonGalleryItem'  # `ActiveItem`[¶](#wx.ribbon.RibbonGallery.ActiveItem "Permalink to this definition")See [`GetActiveItem`](#wx.ribbon.RibbonGallery.GetActiveItem "wx.ribbon.RibbonGallery.GetActiveItem")
    Count: int  # `Count`[¶](#wx.ribbon.RibbonGallery.Count "Permalink to this definition")See [`GetCount`](#wx.ribbon.RibbonGallery.GetCount "wx.ribbon.RibbonGallery.GetCount")
    DownButtonState: 'RibbonGalleryButtonState'  # `DownButtonState`[¶](#wx.ribbon.RibbonGallery.DownButtonState "Permalink to this definition")See [`GetDownButtonState`](#wx.ribbon.RibbonGallery.GetDownButtonState "wx.ribbon.RibbonGallery.GetDownButtonState")
    ExtensionButtonState: 'RibbonGalleryButtonState'  # `ExtensionButtonState`[¶](#wx.ribbon.RibbonGallery.ExtensionButtonState "Permalink to this definition")See [`GetExtensionButtonState`](#wx.ribbon.RibbonGallery.GetExtensionButtonState "wx.ribbon.RibbonGallery.GetExtensionButtonState")
    HoveredItem: 'RibbonGalleryItem'  # `HoveredItem`[¶](#wx.ribbon.RibbonGallery.HoveredItem "Permalink to this definition")See [`GetHoveredItem`](#wx.ribbon.RibbonGallery.GetHoveredItem "wx.ribbon.RibbonGallery.GetHoveredItem")
    Selection: 'RibbonGalleryItem'  # `Selection`[¶](#wx.ribbon.RibbonGallery.Selection "Permalink to this definition")See [`GetSelection`](#wx.ribbon.RibbonGallery.GetSelection "wx.ribbon.RibbonGallery.GetSelection") and [`SetSelection`](#wx.ribbon.RibbonGallery.SetSelection "wx.ribbon.RibbonGallery.SetSelection")
    UpButtonState: 'RibbonGalleryButtonState'  # `UpButtonState`[¶](#wx.ribbon.RibbonGallery.UpButtonState "Permalink to this definition")See [`GetUpButtonState`](#wx.ribbon.RibbonGallery.GetUpButtonState "wx.ribbon.RibbonGallery.GetUpButtonState")



EVT_RIBBONGALLERY_SELECTED: int  # Triggered when the user selects an item from the gallery. Note that the ID is that of the gallery, not of the item.

EVT_RIBBONGALLERY_CLICKED: int  # Similar to EVT_RIBBONGALLERY_SELECTED but triggered every time a gallery item is clicked, even if it is already selected. Note that the ID of the event is that of the gallery, not of the item, just as above. This event is available since wxWidgets 2.9.2.

EVT_RIBBONGALLERY_HOVER_CHANGED: int  # Triggered when the item being hovered over by the user changes. The item in the event will be the new item being hovered, or None if there is no longer an item being hovered. Note that the ID is that of the gallery, not of the item. ^^ ^^

class RibbonPanel(RibbonControl):
    """ **Possible constructors**:



```
RibbonPanel()

RibbonPanel(parent, id=ID_ANY, label="", minimised_icon=NullBitmap,
            pos=DefaultPosition, size=DefaultSize, style=RIBBON_PANEL_DEFAULT_STYLE)

```


Serves as a container for a group of (ribbon) controls.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonPanel.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonPanel.Create "wx.ribbon.RibbonPanel.Create") should be called in order to create the ribbon panel.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, label=””, minimised\_icon=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=RIBBON\_PANEL\_DEFAULT\_STYLE)*


Constructs a ribbon panel.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Pointer to a parent window, which is typically a  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage), though it can be any window.
* **id** (*wx.WindowID*) – Window identifier.
* **label** (*string*) – Label to be used in the  [wx.ribbon.RibbonPanel](#wx-ribbon-ribbonpanel)’s chrome.
* **minimised\_icon** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Icon to be used in place of the panel’s children when the panel is minimised.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The initial position of the panel. Not relevant when the parent is a ribbon page, as the position and size of the panel will be dictated by the page.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The initial size of the panel. Not relevant when the parent is a ribbon page, as the position and size of the panel will be dictated by the page.
* **style** (*long*) – Style flags for the panel.






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def CanAutoMinimise(self) -> bool:
        """ 

`CanAutoMinimise`(*self*)[¶](#wx.ribbon.RibbonPanel.CanAutoMinimise "Permalink to this definition")
Query if the panel can automatically minimise itself at small sizes.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, pos=DefaultPosition, size=DefaultSize, style=RIBBON_PANEL_DEFAULT_STYLE) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *label=""*, *icon=NullBitmap*, *pos=DefaultPosition*, *size=DefaultSize*, *style=RIBBON\_PANEL\_DEFAULT\_STYLE*)[¶](#wx.ribbon.RibbonPanel.Create "Permalink to this definition")
Create a ribbon panel in two-step ribbon panel construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **label** (*string*) –
* **icon** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonPanel.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetExpandedDummy(self) -> 'RibbonPanel':
        """ 

`GetExpandedDummy`(*self*)[¶](#wx.ribbon.RibbonPanel.GetExpandedDummy "Permalink to this definition")
Get the dummy panel of an expanded panel.


Note that this should be called on an expanded panel to get the dummy associated with it - it will return `None` when called on the dummy itself.



Return type
 [wx.ribbon.RibbonPanel](#wx-ribbon-ribbonpanel)





See also


[`ShowExpanded`](#wx.ribbon.RibbonPanel.ShowExpanded "wx.ribbon.RibbonPanel.ShowExpanded")




See also


[`GetExpandedPanel`](#wx.ribbon.RibbonPanel.GetExpandedPanel "wx.ribbon.RibbonPanel.GetExpandedPanel")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetExpandedPanel(self) -> 'RibbonPanel':
        """ 

`GetExpandedPanel`(*self*)[¶](#wx.ribbon.RibbonPanel.GetExpandedPanel "Permalink to this definition")
Get the expanded panel of a dummy panel.


Note that this should be called on a dummy panel to get the expanded panel associated with it - it will return `None` when called on the expanded panel itself.



Return type
 [wx.ribbon.RibbonPanel](#wx-ribbon-ribbonpanel)





See also


[`ShowExpanded`](#wx.ribbon.RibbonPanel.ShowExpanded "wx.ribbon.RibbonPanel.ShowExpanded")




See also


[`GetExpandedDummy`](#wx.ribbon.RibbonPanel.GetExpandedDummy "wx.ribbon.RibbonPanel.GetExpandedDummy")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def GetMinimisedIcon(self) -> 'Bitmap':
        """ 

`GetMinimisedIcon`(*self*)[¶](#wx.ribbon.RibbonPanel.GetMinimisedIcon "Permalink to this definition")
Get the bitmap to be used in place of the panel children when it is minimised.



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def HasExtButton(self) -> bool:
        """ 

`HasExtButton`(*self*)[¶](#wx.ribbon.RibbonPanel.HasExtButton "Permalink to this definition")
Test if the panel has an extension button.


Such button is shown in the top right corner of the panel if `RIBBON_PANEL_EXT_BUTTON` style is used for it.



Return type
*bool*



Returns
`True` if the panel and its  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) allow it in their styles.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def HideExpanded(self) -> bool:
        """ 

`HideExpanded`(*self*)[¶](#wx.ribbon.RibbonPanel.HideExpanded "Permalink to this definition")
Hide the panel’s external expansion.



Return type
*bool*



Returns
`True` if the panel was un-expanded, `False` if it was not (normally due to it not being expanded in the first place).





See also


[`HideExpanded`](#wx.ribbon.RibbonPanel.HideExpanded "wx.ribbon.RibbonPanel.HideExpanded")




See also


[`GetExpandedPanel`](#wx.ribbon.RibbonPanel.GetExpandedPanel "wx.ribbon.RibbonPanel.GetExpandedPanel")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsExtButtonHovered(self) -> bool:
        """ 

`IsExtButtonHovered`(*self*)[¶](#wx.ribbon.RibbonPanel.IsExtButtonHovered "Permalink to this definition")
Query if the mouse is currently hovered over the extension button.


Extension button is only shown for panels with `RIBBON_PANEL_EXT_BUTTON` style.



Return type
*bool*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsHovered(self) -> bool:
        """ 

`IsHovered`(*self*)[¶](#wx.ribbon.RibbonPanel.IsHovered "Permalink to this definition")
Query is the mouse is currently hovered over the panel.



Return type
*bool*



Returns
`True` if the cursor is within the bounds of the panel (i.e. hovered over the panel or one of its children), `False` otherwise.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def IsMinimised(self, *args, **kw) -> bool:
        """ 

`IsMinimised`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonPanel.IsMinimised "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**IsMinimised** *(self)*


Query if the panel is currently minimised.



Return type
*bool*






---

  



**IsMinimised** *(self, at\_size)*


Query if the panel would be minimised at a given size.



Parameters
**at\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonPanel.Realize "Permalink to this definition")
Realize all children of the panel.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.ribbon.RibbonPanel.SetArtProvider "Permalink to this definition")
Set the art provider to be used.


Normally called automatically by  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) when the panel is created, or the art provider changed on the page.


The new art provider will be propagated to the children of the panel.



Parameters
**art** ([*wx.ribbon.RibbonArtProvider*](wx.ribbon.RibbonArtProvider.html#wx.ribbon.RibbonArtProvider "wx.ribbon.RibbonArtProvider")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    def ShowExpanded(self) -> bool:
        """ 

`ShowExpanded`(*self*)[¶](#wx.ribbon.RibbonPanel.ShowExpanded "Permalink to this definition")
Show the panel externally expanded.


When a panel is minimised, it can be shown full-size in a pop-out window, which is referred to as being (externally) expanded. Note that when a panel is expanded, there exist two panels - the original panel (which is referred to as the dummy panel) and the expanded panel. The original is termed a dummy as it sits in the ribbon bar doing nothing, while the expanded panel holds the panel children.



Return type
*bool*



Returns
`True` if the panel was expanded, `False` if it was not (possibly due to it not being minimised, or already being expanded).





See also


[`HideExpanded`](#wx.ribbon.RibbonPanel.HideExpanded "wx.ribbon.RibbonPanel.HideExpanded")




See also


[`GetExpandedPanel`](#wx.ribbon.RibbonPanel.GetExpandedPanel "wx.ribbon.RibbonPanel.GetExpandedPanel")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPanel.html
        """

    ExpandedDummy: 'RibbonPanel'  # `ExpandedDummy`[¶](#wx.ribbon.RibbonPanel.ExpandedDummy "Permalink to this definition")See [`GetExpandedDummy`](#wx.ribbon.RibbonPanel.GetExpandedDummy "wx.ribbon.RibbonPanel.GetExpandedDummy")
    ExpandedPanel: 'RibbonPanel'  # `ExpandedPanel`[¶](#wx.ribbon.RibbonPanel.ExpandedPanel "Permalink to this definition")See [`GetExpandedPanel`](#wx.ribbon.RibbonPanel.GetExpandedPanel "wx.ribbon.RibbonPanel.GetExpandedPanel")
    MinimisedIcon: 'Bitmap'  # `MinimisedIcon`[¶](#wx.ribbon.RibbonPanel.MinimisedIcon "Permalink to this definition")See [`GetMinimisedIcon`](#wx.ribbon.RibbonPanel.GetMinimisedIcon "wx.ribbon.RibbonPanel.GetMinimisedIcon")



RIBBON_PANEL_DEFAULT_STYLE: int  # Defined as no other flags set.

RIBBON_PANEL_NO_AUTO_MINIMISE: int  # Prevents the panel from automatically minimising to conserve screen space.

RIBBON_PANEL_EXT_BUTTON: int  # Causes an extension button to be shown in the panel’s chrome (if the bar in which it is contained has wx.ribbon.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS set). The behaviour of this button is application controlled, but typically will show an extended drop-down menu relating to the panel.

RIBBON_PANEL_MINIMISE_BUTTON: int  # Causes a (de)minimise button to be shown in the panel’s chrome (if the bar in which it is contained has the wx.ribbon.RIBBON_BAR_SHOW_PANEL_MINIMISE_BUTTONS style set). This flag is typically combined with wx.ribbon.RIBBON_PANEL_NO_AUTO_MINIMISE to make a panel which the user always has manual control over when it minimises.

RIBBON_PANEL_STRETCH: int  # Stretches a single panel to fit the parent page.

EVT_RIBBONPANEL_EXTBUTTON_ACTIVATED: int  # Triggered when the user activate the panel extension button. ^^

class RibbonToolBar(RibbonControl):
    """ **Possible constructors**:



```
RibbonToolBar()

RibbonToolBar(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
              style=0)

```


A ribbon tool bar is similar to a traditional toolbar which has no
labels.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonToolBar.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonToolBar.Create "wx.ribbon.RibbonToolBar.Create") should be called in order to create the tool bar.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*


Construct a ribbon tool bar with the given parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window for the tool bar (typically a  [wx.ribbon.RibbonPanel](wx.ribbon.RibbonPanel.html#wx-ribbon-ribbonpanel)).
* **id** (*wx.WindowID*) – An identifier for the toolbar. `ID_ANY` is taken to mean a default.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Initial position of the tool bar.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Initial size of the tool bar.
* **style** (*long*) – Tool bar style, currently unused.






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddDropdownTool(self, tool_id, bitmap, help_string="") -> 'RibbonToolBarToolBase':
        """ 

`AddDropdownTool`(*self*, *tool\_id*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonToolBar.AddDropdownTool "Permalink to this definition")
Add a dropdown tool to the tool bar (simple version).



Parameters
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





See also


[`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddHybridTool(self, tool_id, bitmap, help_string="") -> 'RibbonToolBarToolBase':
        """ 

`AddHybridTool`(*self*, *tool\_id*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonToolBar.AddHybridTool "Permalink to this definition")
Add a hybrid tool to the tool bar (simple version).



Parameters
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





See also


[`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddSeparator(self) -> 'RibbonToolBarToolBase':
        """ 

`AddSeparator`(*self*)[¶](#wx.ribbon.RibbonToolBar.AddSeparator "Permalink to this definition")
Add a separator to the tool bar.


Separators are used to separate tools into groups. As such, a separator is not explicitly drawn, but is visually seen as the gap between tool groups.



Return type
*RibbonToolBarToolBase*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddToggleTool(self, tool_id, bitmap, help_string) -> 'RibbonToolBarToolBase':
        """ 

`AddToggleTool`(*self*, *tool\_id*, *bitmap*, *help\_string*)[¶](#wx.ribbon.RibbonToolBar.AddToggleTool "Permalink to this definition")
Add a toggle tool to the tool bar (simple version).



Parameters
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def AddTool(self, *args, **kw) -> 'RibbonToolBarToolBase':
        """ 

`AddTool`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonToolBar.AddTool "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AddTool** *(self, tool\_id, bitmap, help\_string, kind=RIBBON\_BUTTON\_NORMAL)*


Add a tool to the tool bar (simple version).



Parameters
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) –



Return type
*RibbonToolBarToolBase*






---

  



**AddTool** *(self, tool\_id, bitmap, bitmap\_disabled=NullBitmap, help\_string=””, kind=RIBBON\_BUTTON\_NORMAL, clientData=None)*


Add a tool to the tool bar.



Parameters
* **tool\_id** (*int*) – `ID` of the new tool (used for event callbacks).
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use as the foreground for the new tool. Does not have to be the same size as other tool bitmaps, but should be similar as otherwise it will look visually odd.
* **bitmap\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use when the tool is disabled. If left as NullBitmap, then a bitmap will be automatically generated from *bitmap*.
* **help\_string** (*string*) – The UI help string to associate with the new tool.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool to add.
* **clientData** (*PyUserData*) – Client data to associate with the new tool.



Return type
*RibbonToolBarToolBase*



Returns
An opaque pointer which can be used only with other tool bar methods.





See also


[`AddDropdownTool`](#wx.ribbon.RibbonToolBar.AddDropdownTool "wx.ribbon.RibbonToolBar.AddDropdownTool") , [`AddHybridTool`](#wx.ribbon.RibbonToolBar.AddHybridTool "wx.ribbon.RibbonToolBar.AddHybridTool") , [`AddSeparator`](#wx.ribbon.RibbonToolBar.AddSeparator "wx.ribbon.RibbonToolBar.AddSeparator") , [`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def ClearTools(self) -> None:
        """ 

`ClearTools`(*self*)[¶](#wx.ribbon.RibbonToolBar.ClearTools "Permalink to this definition")
Deletes all the tools in the toolbar.



New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.ribbon.RibbonToolBar.Create "Permalink to this definition")
Create a tool bar in two-step tool bar construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def DeleteTool(self, tool_id: int) -> bool:
        """ 

`DeleteTool`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.DeleteTool "Permalink to this definition")
Removes the specified tool from the toolbar and deletes it.



Parameters
**tool\_id** (*int*) – `ID` of the tool to delete.



Return type
*bool*



Returns
`True` if the tool was deleted, `False` otherwise.





New in version 2.9.4.




See also


[`DeleteToolByPos`](#wx.ribbon.RibbonToolBar.DeleteToolByPos "wx.ribbon.RibbonToolBar.DeleteToolByPos")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def DeleteToolByPos(self, pos: int) -> bool:
        """ 

`DeleteToolByPos`(*self*, *pos*)[¶](#wx.ribbon.RibbonToolBar.DeleteToolByPos "Permalink to this definition")
This function behaves like [`DeleteTool`](#wx.ribbon.RibbonToolBar.DeleteTool "wx.ribbon.RibbonToolBar.DeleteTool") but it deletes the tool at the specified position and not the one with the given id.


Useful to delete separators.



Parameters
**pos** (*int*) – 



Return type
*bool*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def EnableTool(self, tool_id, enable=True) -> None:
        """ 

`EnableTool`(*self*, *tool\_id*, *enable=True*)[¶](#wx.ribbon.RibbonToolBar.EnableTool "Permalink to this definition")
Enable or disable a single tool on the bar.



Parameters
* **tool\_id** (*int*) – `ID` of the tool to enable or disable.
* **enable** (*bool*) – `True` to enable the tool, `False` to disable it.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def FindById(self, tool_id: int) -> 'RibbonToolBarToolBase':
        """ 

`FindById`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.FindById "Permalink to this definition")
Returns a pointer to the tool opaque structure by *id* or `None` if no corresponding tool is found.



Parameters
**tool\_id** (*int*) – 



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetActiveTool(self) -> 'RibbonToolBarToolBase':
        """ 

`GetActiveTool`(*self*)[¶](#wx.ribbon.RibbonToolBar.GetActiveTool "Permalink to this definition")
Returns the active item of the tool bar or `None` if there is none.


The active tool is the one being clicked.



Return type
*RibbonToolBarToolBase*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonToolBar.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolByPos(self, *args, **kw) -> 'RibbonToolBarToolBase':
        """ 

`GetToolByPos`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonToolBar.GetToolByPos "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetToolByPos** *(self, pos)*


Return the opaque pointer corresponding to the given tool.



Parameters
**pos** (*int*) – 



Return type
*RibbonToolBarToolBase*



Returns
an opaque pointer, `None` if is a separator or not found.





New in version 2.9.4.





---

  



**GetToolByPos** *(self, x, y)*


Returns the opaque pointer for the tool at the given coordinates, which are relative to the toolbar’s parent.



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
*RibbonToolBarToolBase*



Returns
an opaque pointer, `None` if is not found.





New in version 4.1/wxWidgets-3.1.5.





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolClientData(self, tool_id: int) -> 'PyUserData':
        """ 

`GetToolClientData`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolClientData "Permalink to this definition")
Get any client data associated with the tool.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
*PyUserData*



Returns
Client data, or `None` if there is none.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolCount(self) -> int:
        """ 

`GetToolCount`(*self*)[¶](#wx.ribbon.RibbonToolBar.GetToolCount "Permalink to this definition")
Returns the number of tools in the toolbar.



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolEnabled(self, tool_id: int) -> bool:
        """ 

`GetToolEnabled`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolEnabled "Permalink to this definition")
Called to determine whether a tool is enabled (responds to user input).



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
*bool*



Returns
`True` if the tool is enabled, `False` otherwise.





New in version 2.9.4.




See also


[`EnableTool`](#wx.ribbon.RibbonToolBar.EnableTool "wx.ribbon.RibbonToolBar.EnableTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolHelpString(self, tool_id: int) -> str:
        """ 

`GetToolHelpString`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolHelpString "Permalink to this definition")
Returns the help string for the given tool.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
`string`





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolId(self, tool: RibbonToolBarToolBase) -> int:
        """ 

`GetToolId`(*self*, *tool*)[¶](#wx.ribbon.RibbonToolBar.GetToolId "Permalink to this definition")
Return the id associated to the tool opaque structure.


The structure pointer must not be `None`.



Parameters
**tool** ([*RibbonToolBarToolBase*](wx.lib.agw.ribbon.toolbar.RibbonToolBarToolBase.html#wx.lib.agw.ribbon.toolbar.RibbonToolBarToolBase "wx.lib.agw.ribbon.toolbar.RibbonToolBarToolBase")) – 



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolKind(self, tool_id: int) -> 'RibbonButtonKind':
        """ 

`GetToolKind`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolKind "Permalink to this definition")
Return the kind of the given tool.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
 [wx.ribbon.RibbonButtonKind](wx.ribbon.RibbonButtonKind.enumeration.html#wx-ribbon-ribbonbuttonkind)





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolPos(self, tool_id: int) -> int:
        """ 

`GetToolPos`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolPos "Permalink to this definition")
Returns the tool position in the toolbar, or `NOT_FOUND` if the tool is not found.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolRect(self, tool_id: int) -> 'Rect':
        """ 

`GetToolRect`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolRect "Permalink to this definition")
Returns the tool’s rect with coordinates relative to the toolbar’s parent, or a default-constructed rect if the tool is not found.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
`Rect`





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def GetToolState(self, tool_id: int) -> bool:
        """ 

`GetToolState`(*self*, *tool\_id*)[¶](#wx.ribbon.RibbonToolBar.GetToolState "Permalink to this definition")
Gets the on/off state of a toggle tool.



Parameters
**tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .



Return type
*bool*



Returns
`True` if the tool is toggled on, `False` otherwise.





New in version 2.9.4.




See also


[`ToggleTool`](#wx.ribbon.RibbonToolBar.ToggleTool "wx.ribbon.RibbonToolBar.ToggleTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertDropdownTool(self, pos, tool_id, bitmap, help_string="") -> 'RibbonToolBarToolBase':
        """ 

`InsertDropdownTool`(*self*, *pos*, *tool\_id*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonToolBar.InsertDropdownTool "Permalink to this definition")
Insert a dropdown tool to the tool bar (simple version) as the specified position.



Parameters
* **pos** (*int*) –
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`AddDropdownTool`](#wx.ribbon.RibbonToolBar.AddDropdownTool "wx.ribbon.RibbonToolBar.AddDropdownTool") , [`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertHybridTool(self, pos, tool_id, bitmap, help_string="") -> 'RibbonToolBarToolBase':
        """ 

`InsertHybridTool`(*self*, *pos*, *tool\_id*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonToolBar.InsertHybridTool "Permalink to this definition")
Insert a hybrid tool to the tool bar (simple version) as the specified position.



Parameters
* **pos** (*int*) –
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`AddHybridTool`](#wx.ribbon.RibbonToolBar.AddHybridTool "wx.ribbon.RibbonToolBar.AddHybridTool") , [`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertSeparator(self, pos: int) -> 'RibbonToolBarToolBase':
        """ 

`InsertSeparator`(*self*, *pos*)[¶](#wx.ribbon.RibbonToolBar.InsertSeparator "Permalink to this definition")
Insert a separator to the tool bar at the specified position.



Parameters
**pos** (*int*) – 



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`AddSeparator`](#wx.ribbon.RibbonToolBar.AddSeparator "wx.ribbon.RibbonToolBar.AddSeparator") , [`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertToggleTool(self, pos, tool_id, bitmap, help_string="") -> 'RibbonToolBarToolBase':
        """ 

`InsertToggleTool`(*self*, *pos*, *tool\_id*, *bitmap*, *help\_string=""*)[¶](#wx.ribbon.RibbonToolBar.InsertToggleTool "Permalink to this definition")
Insert a toggle tool to the tool bar (simple version) as the specified position.



Parameters
* **pos** (*int*) –
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`AddToggleTool`](#wx.ribbon.RibbonToolBar.AddToggleTool "wx.ribbon.RibbonToolBar.AddToggleTool") , [`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def InsertTool(self, *args, **kw) -> 'RibbonToolBarToolBase':
        """ 

`InsertTool`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonToolBar.InsertTool "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**InsertTool** *(self, pos, tool\_id, bitmap, help\_string, kind=RIBBON\_BUTTON\_NORMAL)*


Insert a tool to the tool bar (simple version) as the specified position.



Parameters
* **pos** (*int*) –
* **tool\_id** (*int*) –
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **help\_string** (*string*) –
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) –



Return type
*RibbonToolBarToolBase*





New in version 2.9.4.




See also


[`InsertTool`](#wx.ribbon.RibbonToolBar.InsertTool "wx.ribbon.RibbonToolBar.InsertTool")





---

  



**InsertTool** *(self, pos, tool\_id, bitmap, bitmap\_disabled=NullBitmap, help\_string=””, kind=RIBBON\_BUTTON\_NORMAL, clientData=None)*


Insert a tool to the tool bar at the specified position.



Parameters
* **pos** (*int*) – Position of the new tool (number of tools and separators from the beginning of the toolbar).
* **tool\_id** (*int*) – `ID` of the new tool (used for event callbacks).
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use as the foreground for the new tool. Does not have to be the same size as other tool bitmaps, but should be similar as otherwise it will look visually odd.
* **bitmap\_disabled** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use when the tool is disabled. If left as NullBitmap, then a bitmap will be automatically generated from *bitmap*.
* **help\_string** (*string*) – The UI help string to associate with the new tool.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool to add.
* **clientData** (*PyUserData*) – Client data to associate with the new tool.



Return type
*RibbonToolBarToolBase*



Returns
An opaque pointer which can be used only with other tool bar methods.





New in version 2.9.4.




See also


[`InsertDropdownTool`](#wx.ribbon.RibbonToolBar.InsertDropdownTool "wx.ribbon.RibbonToolBar.InsertDropdownTool") , [`InsertHybridTool`](#wx.ribbon.RibbonToolBar.InsertHybridTool "wx.ribbon.RibbonToolBar.InsertHybridTool") , [`InsertSeparator`](#wx.ribbon.RibbonToolBar.InsertSeparator "wx.ribbon.RibbonToolBar.InsertSeparator")





---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonToolBar.Realize "Permalink to this definition")
Calculate tool layouts and positions.


Must be called after tools are added to the tool bar, as otherwise the newly added tools will not be displayed.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetRows(self, nMin, nMax=-1) -> None:
        """ 

`SetRows`(*self*, *nMin*, *nMax=-1*)[¶](#wx.ribbon.RibbonToolBar.SetRows "Permalink to this definition")
Set the number of rows to distribute tool groups over.


Tool groups can be distributed over a variable number of rows. The way in which groups are assigned to rows is not specified, and the order of groups may change, but they will be distributed in such a way as to minimise the overall size of the tool bar.



Parameters
* **nMin** (*int*) – The minimum number of rows to use.
* **nMax** (*int*) – The maximum number of rows to use (defaults to nMin).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolClientData(self, tool_id, clientData) -> None:
        """ 

`SetToolClientData`(*self*, *tool\_id*, *clientData*)[¶](#wx.ribbon.RibbonToolBar.SetToolClientData "Permalink to this definition")
Sets the client data associated with the tool.



Parameters
* **tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .
* **clientData** (*PyUserData*) – The client data to use.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolDisabledBitmap(self, tool_id, bitmap) -> None:
        """ 

`SetToolDisabledBitmap`(*self*, *tool\_id*, *bitmap*)[¶](#wx.ribbon.RibbonToolBar.SetToolDisabledBitmap "Permalink to this definition")
Sets the bitmap to be used by the tool with the given `ID` when the tool is in a disabled state.



Parameters
* **tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use for disabled tools.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolHelpString(self, tool_id, helpString) -> None:
        """ 

`SetToolHelpString`(*self*, *tool\_id*, *helpString*)[¶](#wx.ribbon.RibbonToolBar.SetToolHelpString "Permalink to this definition")
Sets the help string shown in tooltip for the given tool.



Parameters
* **tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .
* **helpString** (*string*) – A string for the help.





New in version 2.9.4.




See also


[`GetToolHelpString`](#wx.ribbon.RibbonToolBar.GetToolHelpString "wx.ribbon.RibbonToolBar.GetToolHelpString")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def SetToolNormalBitmap(self, tool_id, bitmap) -> None:
        """ 

`SetToolNormalBitmap`(*self*, *tool\_id*, *bitmap*)[¶](#wx.ribbon.RibbonToolBar.SetToolNormalBitmap "Permalink to this definition")
Sets the bitmap to be used by the tool with the given `ID`.



Parameters
* **tool\_id** (*int*) – `ID` of the tool in question, as passed to [`AddTool`](#wx.ribbon.RibbonToolBar.AddTool "wx.ribbon.RibbonToolBar.AddTool") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Bitmap to use for normals tools.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    def ToggleTool(self, tool_id, checked) -> None:
        """ 

`ToggleTool`(*self*, *tool\_id*, *checked*)[¶](#wx.ribbon.RibbonToolBar.ToggleTool "Permalink to this definition")
Set a toggle tool to the checked or unchecked state.



Parameters
* **tool\_id** (*int*) – `ID` of the toggle tool to manipulate.
* **checked** (*bool*) – `True` to set the tool to the toggled/pressed/checked state, `False` to set it to the untoggled/unpressed/unchecked state.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonToolBar.html
        """

    ActiveTool: 'RibbonToolBarToolBase'  # `ActiveTool`[¶](#wx.ribbon.RibbonToolBar.ActiveTool "Permalink to this definition")See [`GetActiveTool`](#wx.ribbon.RibbonToolBar.GetActiveTool "wx.ribbon.RibbonToolBar.GetActiveTool")
    ToolCount: int  # `ToolCount`[¶](#wx.ribbon.RibbonToolBar.ToolCount "Permalink to this definition")See [`GetToolCount`](#wx.ribbon.RibbonToolBar.GetToolCount "wx.ribbon.RibbonToolBar.GetToolCount")



EVT_RIBBONTOOLBAR_CLICKED: int  # Triggered when the normal (non-dropdown) region of a tool on the tool bar is clicked.

EVT_RIBBONTOOLBAR_DROPDOWN_CLICKED: int  # Triggered when the dropdown region of a tool on the tool bar is clicked. wx.ribbon.RibbonToolBarEvent.PopupMenu   should be called by the event handler if it wants to display a popup menu (which is what most dropdown tools should be doing). ^^

class RibbonArtProvider:
    """ **Possible constructors**:



```
RibbonArtProvider()

```


RibbonArtProvider is responsible for drawing all the components of
the ribbon interface.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.ribbon.RibbonArtProvider.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def Clone(self) -> 'RibbonArtProvider':
        """ 

`Clone`(*self*)[¶](#wx.ribbon.RibbonArtProvider.Clone "Permalink to this definition")
Create a new art provider which is a clone of this one.



Return type
 [wx.ribbon.RibbonArtProvider](#wx-ribbon-ribbonartprovider)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawButtonBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawButtonBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which will typically be the button bar itself, though this is not guaranteed).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ 

`DrawButtonBarButton`(*self*, *dc*, *wnd*, *rect*, *kind*, *state*, *label*, *bitmap\_large*, *bitmap\_small*)[¶](#wx.ribbon.RibbonArtProvider.DrawButtonBarButton "Permalink to this definition")
Draw a single button for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be a size previously returned by [`GetButtonBarButtonSize`](#wx.ribbon.RibbonArtProvider.GetButtonBarButtonSize "wx.ribbon.RibbonArtProvider.GetButtonBarButtonSize") , and the rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawButtonBarBackground`](#wx.ribbon.RibbonArtProvider.DrawButtonBarBackground "wx.ribbon.RibbonArtProvider.DrawButtonBarBackground") .
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button to draw (normal, dropdown or hybrid).
* **state** (*long*) – Combination of a size flag and state flags from the RibbonButtonBarButtonState enumeration.
* **label** (*string*) – The label of the button.
* **bitmap\_large** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The large bitmap of the button (or the large disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The small bitmap of the button (or the small disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawGalleryBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawGalleryBackground "Permalink to this definition")
Draw the background and chrome for a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This should draw the border, background, scroll buttons, extension button, and any other UI elements which are not attached to a specific gallery item.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery whose background and chrome is being drawn. Attributes used during drawing like the gallery hover state and individual button states can be queried from this parameter by [`wx.ribbon.RibbonGallery.IsHovered`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.IsHovered "wx.ribbon.RibbonGallery.IsHovered") , [`wx.ribbon.RibbonGallery.GetExtensionButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetExtensionButtonState "wx.ribbon.RibbonGallery.GetExtensionButtonState") , [`wx.ribbon.RibbonGallery.GetUpButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetUpButtonState "wx.ribbon.RibbonGallery.GetUpButtonState") , and [`wx.ribbon.RibbonGallery.GetDownButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetDownButtonState "wx.ribbon.RibbonGallery.GetDownButtonState") .
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is the entire area of the gallery control, not just the client rectangle.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ 

`DrawGalleryItemBackground`(*self*, *dc*, *wnd*, *rect*, *item*)[¶](#wx.ribbon.RibbonArtProvider.DrawGalleryItemBackground "Permalink to this definition")
Draw the background of a single item in a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This is painted on top of a gallery background, and behind the items bitmap. Unlike [`DrawButtonBarButton`](#wx.ribbon.RibbonArtProvider.DrawButtonBarButton "wx.ribbon.RibbonArtProvider.DrawButtonBarButton") and [`DrawTool`](#wx.ribbon.RibbonArtProvider.DrawTool "wx.ribbon.RibbonArtProvider.DrawTool") , it is not expected to draw the item bitmap - that is done by the gallery control itself.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery which contains the item being drawn.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be the size of the item’s bitmap, expanded by gallery item padding values (wx``wx.ribbon.RIBBON\_ART\_GALLERY\_BITMAP\_PADDING\_LEFT\_SIZE``, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE`, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE`, and `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE`). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawGalleryBackground`](#wx.ribbon.RibbonArtProvider.DrawGalleryBackground "wx.ribbon.RibbonArtProvider.DrawGalleryBackground") .
* **item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – The item whose background is being painted. Typically the background will vary if the item is hovered, active, or selected; [`wx.ribbon.RibbonGallery.GetSelection`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetSelection "wx.ribbon.RibbonGallery.GetSelection") , [`wx.ribbon.RibbonGallery.GetActiveItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetActiveItem "wx.ribbon.RibbonGallery.GetActiveItem") , and [`wx.ribbon.RibbonGallery.GetHoveredItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetHoveredItem "wx.ribbon.RibbonGallery.GetHoveredItem") can be called to test if the given item is in one of these states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawHelpButton(self, dc, wnd, rect) -> None:
        """ 

`DrawHelpButton`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawHelpButton "Permalink to this definition")
Draw help button on  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar).


This should draw a help button at top right corner of ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ 

`DrawMinimisedPanel`(*self*, *dc*, *wnd*, *rect*, *bitmap*)[¶](#wx.ribbon.RibbonArtProvider.DrawMinimisedPanel "Permalink to this definition")
Draw a minimised ribbon panel.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel which is minimised. The panel label can be obtained from this window. The minimised icon obtained from querying the window may not be the size requested by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize") - the *bitmap* argument contains the icon in the requested size.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of the rectangle will be at least the size returned by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – A copy of the panel’s minimised bitmap rescaled to the size returned by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPageBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawPageBackground "Permalink to this definition")
Draw the background of a ribbon page.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which is commonly the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) whose background is being drawn, but doesn’t have to be).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.





See also


[`GetPageBackgroundRedrawArea`](#wx.ribbon.RibbonArtProvider.GetPageBackgroundRedrawArea "wx.ribbon.RibbonArtProvider.GetPageBackgroundRedrawArea")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPanelBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawPanelBackground "Permalink to this definition")
Draw the background and chrome for a ribbon panel.


This should draw the border, background, label, and any other items of a panel which are outside the client area of a panel.


Note that when a panel is minimised, this function is not called - only [`DrawMinimisedPanel`](#wx.ribbon.RibbonArtProvider.DrawMinimisedPanel "wx.ribbon.RibbonArtProvider.DrawMinimisedPanel") is called, so a background should be explicitly painted by that if required.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ 

`DrawScrollButton`(*self*, *dc*, *wnd*, *rect*, *style*)[¶](#wx.ribbon.RibbonArtProvider.DrawScrollButton "Permalink to this definition")
Draw a ribbon-style scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be at least the size returned by [`GetScrollButtonMinimumSize`](#wx.ribbon.RibbonArtProvider.GetScrollButtonMinimumSize "wx.ribbon.RibbonArtProvider.GetScrollButtonMinimumSize") for a scroll button with the same style. For tab scroll buttons, this rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground") , but this is not guaranteed for other types of button (for example, page scroll buttons will not be painted on an area previously painted with [`DrawPageBackground`](#wx.ribbon.RibbonArtProvider.DrawPageBackground "wx.ribbon.RibbonArtProvider.DrawPageBackground") ).
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, a for flag, and one or more states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *tab*)[¶](#wx.ribbon.RibbonArtProvider.DrawTab "Permalink to this definition")
Draw a single tab in the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (not the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) associated with the tab being drawn).
* **tab** ([*wx.ribbon.RibbonPageTabInfo*](wx.ribbon.RibbonPageTabInfo.html#wx.ribbon.RibbonPageTabInfo "wx.ribbon.RibbonPageTabInfo")) – The rectangle within which to draw, and also the tab label, icon, and state (active and/or hovered). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground") . The rectangle’s width will be at least the minimum value returned by [`GetBarTabWidth`](#wx.ribbon.RibbonArtProvider.GetBarTabWidth "wx.ribbon.RibbonArtProvider.GetBarTabWidth") , and height will be the value returned by [`GetTabCtrlHeight`](#wx.ribbon.RibbonArtProvider.GetTabCtrlHeight "wx.ribbon.RibbonArtProvider.GetTabCtrlHeight") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawTabCtrlBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground "Permalink to this definition")
Draw the background of the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ 

`DrawTabSeparator`(*self*, *dc*, *wnd*, *rect*, *visibility*)[¶](#wx.ribbon.RibbonArtProvider.DrawTabSeparator "Permalink to this definition")
Draw a separator between two tabs in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw, which will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonArtProvider.DrawTabCtrlBackground") .
* **visibility** (*float*) – The opacity with which to draw the separator. Values are in the range `[0`, `1]`, with 0 being totally transparent, and 1 being totally opaque.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
        """ 

`DrawToggleButton`(*self*, *dc*, *wnd*, *rect*, *mode*)[¶](#wx.ribbon.RibbonArtProvider.DrawToggleButton "Permalink to this definition")
Draw toggle button on  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar).


This should draw a small toggle button at top right corner of ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.
* **mode** ([*RibbonDisplayMode*](wx.ribbon.RibbonDisplayMode.enumeration.html "RibbonDisplayMode")) – The RibbonDisplayMode which should be applied to display button





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ 

`DrawTool`(*self*, *dc*, *wnd*, *rect*, *bitmap*, *kind*, *state*)[¶](#wx.ribbon.RibbonArtProvider.DrawTool "Permalink to this definition")
Draw a single tool (for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will at least the size returned by [`GetToolSize`](#wx.ribbon.RibbonArtProvider.GetToolSize "wx.ribbon.RibbonArtProvider.GetToolSize") , and the height of it will be equal for all tools within the same group. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolGroupBackground`](#wx.ribbon.RibbonArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonArtProvider.DrawToolGroupBackground") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap to use as the tool’s foreground. If the tool is a hybrid or dropdown tool, then the foreground should also contain a standard dropdown button.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool to draw (normal, dropdown, or hybrid).
* **state** (*long*) – A combination of RibbonToolBarToolState flags giving the state of the tool and it’s relative position within a tool group.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawToolBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. Some of this rectangle will later be drawn over using [`DrawToolGroupBackground`](#wx.ribbon.RibbonArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonArtProvider.DrawToolGroupBackground") and [`DrawTool`](#wx.ribbon.RibbonArtProvider.DrawTool "wx.ribbon.RibbonArtProvider.DrawTool") , but not all of it will (unless there is only a single group of tools).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolGroupBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.DrawToolGroupBackground "Permalink to this definition")
Draw the background for a group of tools on a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is a union of the individual tools’ rectangles. As there are no gaps between tools, this rectangle will be painted over exactly once by calls to [`DrawTool`](#wx.ribbon.RibbonArtProvider.DrawTool "wx.ribbon.RibbonArtProvider.DrawTool") . The group background could therefore be painted by [`DrawTool`](#wx.ribbon.RibbonArtProvider.DrawTool "wx.ribbon.RibbonArtProvider.DrawTool") , though it can be conceptually easier and more efficient to draw it all at once here. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolBarBackground`](#wx.ribbon.RibbonArtProvider.DrawToolBarBackground "wx.ribbon.RibbonArtProvider.DrawToolBarBackground") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ 

`GetBarTabWidth`(*self*, *dc*, *wnd*, *label*, *bitmap*, *ideal*, *small\_begin\_need\_separator*, *small\_must\_have\_separator*, *minimum*)[¶](#wx.ribbon.RibbonArtProvider.GetBarTabWidth "Permalink to this definition")
Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tab will eventually be drawn.
* **label** (*string*) – The tab’s label (or “” if it has none).
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The tab’s icon (or NullBitmap if it has none).
* **ideal** (*int*) – The ideal width (in pixels) of the tab.
* **small\_begin\_need\_separator** (*int*) – A size less than the *ideal* size, at which a tab separator should begin to be drawn (i.e. drawn, but still fairly transparent).
* **small\_must\_have\_separator** (*int*) – A size less than the *small\_begin\_need\_separator* size, at which a tab separator must be drawn (i.e. drawn at full opacity).
* **minimum** (*int*) – A size less than the *small\_must\_have\_separator* size, and greater than or equal to zero, which is the minimum pixel width for the tab.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetBarToggleButtonArea(self, rect: 'Rect') -> 'Rect':
        """ 

`GetBarToggleButtonArea`(*self*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.GetBarToggleButtonArea "Permalink to this definition")
Calculate the position and size of the ribbon’s toggle button.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The ribbon bar rectangle from which calculate toggle button rectangle.



Return type
*Rect*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
        """ 

`GetButtonBarButtonSize`(*self*, *dc*, *wnd*, *kind*, *size*, *label*, *text\_min\_width*, *bitmap\_size\_large*, *bitmap\_size\_small*, *button\_size*, *normal\_region*, *dropdown\_region*)[¶](#wx.ribbon.RibbonArtProvider.GetButtonBarButtonSize "Permalink to this definition")
Calculate the size of a button within a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the button will eventually be drawn (which is normally a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar), though this is not guaranteed).
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button.
* **size** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The size-class to calculate the size for. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`. If the requested size-class is not applicable, then `False` should be returned.
* **label** (*string*) – The label of the button.
* **text\_min\_width** (*int*) – The minimum width of the button label. Set this to 0 if it is not used.
* **bitmap\_size\_large** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of all “large” bitmaps on the button bar.
* **bitmap\_size\_small** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of all “small” bitmaps on the button bar.
* **button\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size, in pixels, of the button.
* **normal\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The region of the button which constitutes the normal button.
* **dropdown\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The region of the button which constitutes the dropdown button.



Return type
*bool*



Returns
`True` if a size exists for the button, `False` otherwise.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
        """ 

`GetButtonBarButtonTextWidth`(*self*, *dc*, *label*, *kind*, *size*)[¶](#wx.ribbon.RibbonArtProvider.GetButtonBarButtonTextWidth "Permalink to this definition")
Gets the width of the string if it is used as a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) button label.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **label** (*string*) – The string whose width shall be calculated.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button.
* **size** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The size-class to calculate the size for. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`. If the requested size-class is not applicable, then `None` should be returned.



Return type
*wx.Coord*



Returns
Width of the given label text in pixel.





New in version 4.1/wxWidgets-3.1.2.




Note


This function only works with single-line strings.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColor(self, id: int) -> 'Colour':
        """ 

`GetColor`(*self*, *id*)[¶](#wx.ribbon.RibbonArtProvider.GetColor "Permalink to this definition")

Parameters
**id** (*int*) – 



Return type
*Colour*





See also


[`wx.ribbon.RibbonArtProvider.GetColour`](#wx.ribbon.RibbonArtProvider.GetColour "wx.ribbon.RibbonArtProvider.GetColour")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ 

`GetColour`(*self*, *id*)[¶](#wx.ribbon.RibbonArtProvider.GetColour "Permalink to this definition")
Get the value of a certain colour setting.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetColourScheme(self) -> tuple:
        """ 

`GetColourScheme`(*self*)[¶](#wx.ribbon.RibbonArtProvider.GetColourScheme "Permalink to this definition")
Get the current colour scheme.


Returns three colours such that if [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") were called with them, the colour scheme would be restored to what it was when [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") was last called. In practice, this usually means that the returned values are the three colours given in the last call to [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") , however if [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") performs an idempotent operation upon the colours it is given (like clamping a component of the colour), then the returned values may not be the three colours given in the last call to [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") . If [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") has not been called, then the returned values should result in a colour scheme similar to, if not identical to, the default colours of the art provider. Note that if [`SetColour`](#wx.ribbon.RibbonArtProvider.SetColour "wx.ribbon.RibbonArtProvider.SetColour") is called, then [`GetColourScheme`](#wx.ribbon.RibbonArtProvider.GetColourScheme "wx.ribbon.RibbonArtProvider.GetColourScheme") does not try and return a colour scheme similar to colours being used - it’s return values are dependent upon the last values given to [`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme") , as described above.



Return type
*tuple*





Note


The Python version of this method returns the three scheme colours as a tuple of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") objects.




Returns
( *primary*, *secondary*, *tertiary* )






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.ribbon.RibbonArtProvider.GetFlags "Permalink to this definition")
Get the previously set style flags.



Return type
*long*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ 

`GetFont`(*self*, *id*)[¶](#wx.ribbon.RibbonArtProvider.GetFont "Permalink to this definition")
Get the value of a certain font setting.


*id* can be one of the font values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> 'Size':
        """ 

`GetGalleryClientSize`(*self*, *dc*, *wnd*, *size*, *client\_offset*, *scroll\_up\_button*, *scroll\_down\_button*, *extension\_button*)[¶](#wx.ribbon.RibbonArtProvider.GetGalleryClientSize "Permalink to this definition")
Calculate the client size of a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control for a given size.


This should act as the inverse to [`GetGallerySize`](#wx.ribbon.RibbonArtProvider.GetGallerySize "wx.ribbon.RibbonArtProvider.GetGallerySize") , and decrement the given size by enough to fit the gallery border, buttons, and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The gallery in question.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The overall size to calculate the client size for.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The position within the given size at which the returned client size begins.
* **scroll\_up\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the scroll up button occupies.
* **scroll\_down\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the scroll down button occupies.
* **extension\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the extension button occupies.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetGallerySize(self, dc, wnd, client_size) -> 'Size':
        """ 

`GetGallerySize`(*self*, *dc*, *wnd*, *client\_size*)[¶](#wx.ribbon.RibbonArtProvider.GetGallerySize "Permalink to this definition")
Calculate the size of a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control for a given client size.


This should increment the given size by enough to fit the gallery border, buttons, and any other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The gallery in question.
* **client\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The client size.



Return type
*Size*





See also


[`GetGalleryClientSize`](#wx.ribbon.RibbonArtProvider.GetGalleryClientSize "wx.ribbon.RibbonArtProvider.GetGalleryClientSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetMetric(self, id: int) -> int:
        """ 

`GetMetric`(*self*, *id*)[¶](#wx.ribbon.RibbonArtProvider.GetMetric "Permalink to this definition")
Get the value of a certain integer setting.


*id* can be one of the size values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> 'Size':
        """ 

`GetMinimisedPanelMinimumSize`(*self*, *dc*, *wnd*, *desired\_bitmap\_size*, *expanded\_panel\_direction*)[¶](#wx.ribbon.RibbonArtProvider.GetMinimisedPanelMinimumSize "Permalink to this definition")
Calculate the size of a minimised ribbon panel.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question. Attributes like the panel label can be queried from this.
* **desired\_bitmap\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Optional parameter which is filled with the size of the bitmap suitable for a minimised ribbon panel.
* **expanded\_panel\_direction** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) – Optional parameter which is filled with the direction of the minimised panel ( `EAST` or `SOUTH` depending on the style).



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> 'Rect':
        """ 

`GetPageBackgroundRedrawArea`(*self*, *dc*, *wnd*, *page\_old\_size*, *page\_new\_size*)[¶](#wx.ribbon.RibbonArtProvider.GetPageBackgroundRedrawArea "Permalink to this definition")
Calculate the portion of a page background which needs to be redrawn when a page is resized.


To optimise the drawing of page backgrounds, as small an area as possible should be returned. Of course, if the way in which a background is drawn means that the entire background needs to be repainted on resize, then the entire new size should be returned.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) – The page which is being resized.
* **page\_old\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the page prior to the resize (which has already been painted).
* **page\_new\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the page after the resize.



Return type
*Rect*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ 

`GetPanelClientSize`(*self*, *dc*, *wnd*, *size*, *client\_offset*)[¶](#wx.ribbon.RibbonArtProvider.GetPanelClientSize "Permalink to this definition")
Calculate the client size of a panel for a given overall size.


This should act as the inverse to [`GetPanelSize`](#wx.ribbon.RibbonArtProvider.GetPanelSize "wx.ribbon.RibbonArtProvider.GetPanelSize") , and decrement the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The overall size to calculate client size for.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the returned client size begins within the given *size* (may be `None`).



Return type
*Size*





See also


[`GetPanelSize`](#wx.ribbon.RibbonArtProvider.GetPanelSize "wx.ribbon.RibbonArtProvider.GetPanelSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ 

`GetPanelExtButtonArea`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.GetPanelExtButtonArea "Permalink to this definition")
Calculate the position and size of the panel extension button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The panel rectangle from which calculate extension button rectangle.



Return type
*Rect*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ 

`GetPanelSize`(*self*, *dc*, *wnd*, *client\_size*, *client\_offset*)[¶](#wx.ribbon.RibbonArtProvider.GetPanelSize "Permalink to this definition")
Calculate the size of a panel for a given client size.


This should increment the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **client\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The client size.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the client rectangle begins within the panel (may be `None`).



Return type
*Size*





See also


[`GetPanelClientSize`](#wx.ribbon.RibbonArtProvider.GetPanelClientSize "wx.ribbon.RibbonArtProvider.GetPanelClientSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetRibbonHelpButtonArea(self, rect: 'Rect') -> 'Rect':
        """ 

`GetRibbonHelpButtonArea`(*self*, *rect*)[¶](#wx.ribbon.RibbonArtProvider.GetRibbonHelpButtonArea "Permalink to this definition")
Calculate the position and size of the ribbon’s help button.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The ribbon bar rectangle from which calculate help button rectangle.



Return type
*Rect*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ 

`GetScrollButtonMinimumSize`(*self*, *dc*, *wnd*, *style*)[¶](#wx.ribbon.RibbonArtProvider.GetScrollButtonMinimumSize "Permalink to this definition")
Calculate the minimum size (in pixels) of a scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the scroll button will eventually be drawn.
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, and a for flag (state flags may be given too, but should be ignored, as a button should retain a constant size, regardless of its state).



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ 

`GetTabCtrlHeight`(*self*, *dc*, *wnd*, *pages*)[¶](#wx.ribbon.RibbonArtProvider.GetTabCtrlHeight "Permalink to this definition")
Calculate the height (in pixels) of the tab region of a ribbon bar.


Note that as the tab region can contain scroll buttons, the height should be greater than or equal to the minimum height for a tab scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tabs will eventually be drawn.
* **pages** (*RibbonPageTabInfoArray*) – The tabs which will acquire the returned height.



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> 'Size':
        """ 

`GetToolSize`(*self*, *dc*, *wnd*, *bitmap\_size*, *kind*, *is\_first*, *is\_last*, *dropdown\_region*)[¶](#wx.ribbon.RibbonArtProvider.GetToolSize "Permalink to this definition")
Calculate the size of a tool within a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tool will eventually be drawn.
* **bitmap\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the tool’s foreground bitmap.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool (normal, dropdown, or hybrid).
* **is\_first** (*bool*) – `True` if the tool is the first within its group. `False` otherwise.
* **is\_last** (*bool*) – `True` if the tool is the last within its group. `False` otherwise.
* **dropdown\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – For dropdown and hybrid tools, the region within the returned size which counts as the dropdown part.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColor(self, id, color) -> None:
        """ 

`SetColor`(*self*, *id*, *color*)[¶](#wx.ribbon.RibbonArtProvider.SetColor "Permalink to this definition")

Parameters
* **id** (*int*) –
* **color** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`wx.ribbon.RibbonArtProvider.SetColour`](#wx.ribbon.RibbonArtProvider.SetColour "wx.ribbon.RibbonArtProvider.SetColour")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ 

`SetColour`(*self*, *id*, *colour*)[¶](#wx.ribbon.RibbonArtProvider.SetColour "Permalink to this definition")
Set the value of a certain colour setting to the value *colour*.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting), though not all colour settings will have an effect on every art provider.



Parameters
* **id** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColourScheme`](#wx.ribbon.RibbonArtProvider.SetColourScheme "wx.ribbon.RibbonArtProvider.SetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ 

`SetColourScheme`(*self*, *primary*, *secondary*, *tertiary*)[¶](#wx.ribbon.RibbonArtProvider.SetColourScheme "Permalink to this definition")
Set all applicable colour settings from a few base colours.


Uses any or all of the three given colours to create a colour scheme, and then sets all colour settings which are relevant to the art provider using that scheme. Note that some art providers may not use the tertiary colour for anything, and some may not use the secondary colour either.



Parameters
* **primary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **secondary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **tertiary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColour`](#wx.ribbon.RibbonArtProvider.SetColour "wx.ribbon.RibbonArtProvider.SetColour")




See also


[`GetColourScheme`](#wx.ribbon.RibbonArtProvider.GetColourScheme "wx.ribbon.RibbonArtProvider.GetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.ribbon.RibbonArtProvider.SetFlags "Permalink to this definition")
Set the style flags.


Normally called automatically by [`wx.ribbon.RibbonBar.SetArtProvider`](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar.SetArtProvider "wx.ribbon.RibbonBar.SetArtProvider") with the ribbon bar’s style flags, so that the art provider has the same flags as the bar which it is serving.



Parameters
**flags** (*long*) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ 

`SetFont`(*self*, *id*, *font*)[¶](#wx.ribbon.RibbonArtProvider.SetFont "Permalink to this definition")
Set the value of a certain font setting to the value *font*.


*id* can be one of the font values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
* **id** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ 

`SetMetric`(*self*, *id*, *new\_val*)[¶](#wx.ribbon.RibbonArtProvider.SetMetric "Permalink to this definition")
Set the value of a certain integer setting to the value *new\_val*.


*id* can be one of the size values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
* **id** (*int*) –
* **new\_val** (*int*) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonArtProvider.html
        """

    Flags: int  # `Flags`[¶](#wx.ribbon.RibbonArtProvider.Flags "Permalink to this definition")See [`GetFlags`](#wx.ribbon.RibbonArtProvider.GetFlags "wx.ribbon.RibbonArtProvider.GetFlags") and [`SetFlags`](#wx.ribbon.RibbonArtProvider.SetFlags "wx.ribbon.RibbonArtProvider.SetFlags")



RIBBON_BUTTONBAR_BUTTON_DISABLED: int

RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE: int

class RibbonPage(RibbonControl):
    """ **Possible constructors**:



```
RibbonPage()

RibbonPage(parent, id=ID_ANY, label="", icon=NullBitmap, style=0)

```


Container for related ribbon panels, and a tab within a ribbon bar.


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.ribbon.RibbonPage.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


With this constructor, [`Create`](#wx.ribbon.RibbonPage.Create "wx.ribbon.RibbonPage.Create") should be called in order to create the ribbon page.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, label=””, icon=NullBitmap, style=0)*


Constructs a ribbon page, which must be a child of a ribbon bar.



Parameters
* **parent** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) – Pointer to a parent  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) (unlike most controls, a  [wx.ribbon.RibbonPage](#wx-ribbon-ribbonpage) can only have  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) as a parent).
* **id** (*wx.WindowID*) – Window identifier.
* **label** (*string*) – Label to be used in the  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar)’s tab list for this page (if the ribbon bar is set to display labels).
* **icon** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – Icon to be used in the  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar)’s tab list for this page (if the ribbon bar is set to display icons).
* **style** (*long*) – Currently unused, should be zero.






---

  





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def AdjustRectToIncludeScrollButtons(self, rect: 'Rect') -> None:
        """ 

`AdjustRectToIncludeScrollButtons`(*self*, *rect*)[¶](#wx.ribbon.RibbonPage.AdjustRectToIncludeScrollButtons "Permalink to this definition")
Expand a rectangle of the page to include external scroll buttons (if any).


When no scroll buttons are shown, has no effect.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle to adjust. The width and height will not be reduced, and the x and y will not be increased.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def Create(self, parent, id=ID_ANY, label="", icon=NullBitmap, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *label=""*, *icon=NullBitmap*, *style=0*)[¶](#wx.ribbon.RibbonPage.Create "Permalink to this definition")
Create a ribbon page in two-step ribbon page construction.


Should only be called when the default constructor is used, and arguments have the same meaning as in the full constructor.



Parameters
* **parent** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) –
* **id** (*wx.WindowID*) –
* **label** (*string*) –
* **icon** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def DismissExpandedPanel(self) -> bool:
        """ 

`DismissExpandedPanel`(*self*)[¶](#wx.ribbon.RibbonPage.DismissExpandedPanel "Permalink to this definition")
Dismiss the current externally expanded panel, if there is one.


When a ribbon panel automatically minimises, it can be externally expanded into a floating window. When the user clicks a button in such a panel, the panel should generally re-minimise. Event handlers for buttons on ribbon panels should call this method to achieve this behaviour.



Return type
*bool*



Returns
`True` if a panel was minimised, `False` otherwise.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.ribbon.RibbonPage.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def GetIcon(self) -> 'Bitmap':
        """ 

`GetIcon`(*self*)[¶](#wx.ribbon.RibbonPage.GetIcon "Permalink to this definition")
Get the icon used for the page in the ribbon bar tab area (only displayed if the ribbon bar is actually showing icons).



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def GetMajorAxis(self) -> 'Orientation':
        """ 

`GetMajorAxis`(*self*)[¶](#wx.ribbon.RibbonPage.GetMajorAxis "Permalink to this definition")
Get the direction in which ribbon panels are stacked within the page.


This is controlled by the style of the containing  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar), meaning that all pages within a bar will have the same major axis. As well as being the direction in which panels are stacked, it is also the axis in which scrolling will occur (when required).



Return type
 [wx.Orientation](wx.Orientation.enumeration.html#wx-orientation)



Returns
`wx.HORIZONTAL` or `wx.VERTICAL` (never `wx.BOTH`).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def Realize(self) -> bool:
        """ 

`Realize`(*self*)[¶](#wx.ribbon.RibbonPage.Realize "Permalink to this definition")
Perform a full re-layout of all panels on the page.


Should be called after panels are added to the page, or the sizing behaviour of a panel on the page changes (i.e. due to children being added to it). Usually called automatically when [`wx.ribbon.RibbonBar.Realize`](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar.Realize "wx.ribbon.RibbonBar.Realize") is called.


Will invoke [`wx.ribbon.RibbonPanel.Realize`](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel.Realize "wx.ribbon.RibbonPanel.Realize") for all child panels.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollLines(self, lines: int) -> bool:
        """ 

`ScrollLines`(*self*, *lines*)[¶](#wx.ribbon.RibbonPage.ScrollLines "Permalink to this definition")
Scroll the page by some amount up / down / left / right.


When the page’s children are too big to fit in the onscreen area given to the page, scroll buttons will appear, and the page can be programmatically scrolled. Positive values of *lines* will scroll right or down, while negative values will scroll up or left (depending on the direction in which panels are stacked). A line is equivalent to a constant number of pixels.



Parameters
**lines** (*int*) – 



Return type
*bool*



Returns
`True` if the page scrolled at least one pixel in the given direction, `False` if it did not scroll.





See also


[`GetMajorAxis`](#wx.ribbon.RibbonPage.GetMajorAxis "wx.ribbon.RibbonPage.GetMajorAxis")




See also


[`ScrollPixels`](#wx.ribbon.RibbonPage.ScrollPixels "wx.ribbon.RibbonPage.ScrollPixels")




See also


[`ScrollSections`](#wx.ribbon.RibbonPage.ScrollSections "wx.ribbon.RibbonPage.ScrollSections")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollPixels(self, pixels: int) -> bool:
        """ 

`ScrollPixels`(*self*, *pixels*)[¶](#wx.ribbon.RibbonPage.ScrollPixels "Permalink to this definition")
Scroll the page by a set number of pixels up / down / left / right.


When the page’s children are too big to fit in the onscreen area given to the page, scroll buttons will appear, and the page can be programmatically scrolled. Positive values of *lines* will scroll right or down, while negative values will scroll up or left (depending on the direction in which panels are stacked).



Parameters
**pixels** (*int*) – 



Return type
*bool*



Returns
`True` if the page scrolled at least one pixel in the given direction, `False` if it did not scroll.





See also


[`GetMajorAxis`](#wx.ribbon.RibbonPage.GetMajorAxis "wx.ribbon.RibbonPage.GetMajorAxis")




See also


[`ScrollLines`](#wx.ribbon.RibbonPage.ScrollLines "wx.ribbon.RibbonPage.ScrollLines")




See also


[`ScrollSections`](#wx.ribbon.RibbonPage.ScrollSections "wx.ribbon.RibbonPage.ScrollSections")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def ScrollSections(self, sections: int) -> bool:
        """ 

`ScrollSections`(*self*, *sections*)[¶](#wx.ribbon.RibbonPage.ScrollSections "Permalink to this definition")
Scroll the page by an entire child section.


The *sections* parameter value should be 1 or -1. This will scroll enough to uncover a partially visible child section or totally uncover the next child section that may not be visible at all.



Parameters
**sections** (*int*) – 



Return type
*bool*



Returns
`True` if the page scrolled at least one pixel in the given direction, `False` if it did not scroll.





New in version 2.9.5.




See also


[`ScrollPixels`](#wx.ribbon.RibbonPage.ScrollPixels "wx.ribbon.RibbonPage.ScrollPixels")




See also


[`ScrollSections`](#wx.ribbon.RibbonPage.ScrollSections "wx.ribbon.RibbonPage.ScrollSections")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def SetArtProvider(self, art: 'ribbon.RibbonArtProvider') -> None:
        """ 

`SetArtProvider`(*self*, *art*)[¶](#wx.ribbon.RibbonPage.SetArtProvider "Permalink to this definition")
Set the art provider to be used.


Normally called automatically by  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar) when the page is created, or the art provider changed on the bar.


The new art provider will be propagated to the children of the page.



Parameters
**art** ([*wx.ribbon.RibbonArtProvider*](wx.ribbon.RibbonArtProvider.html#wx.ribbon.RibbonArtProvider "wx.ribbon.RibbonArtProvider")) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    def SetSizeWithScrollButtonAdjustment(self, x, y, width, height) -> None:
        """ 

`SetSizeWithScrollButtonAdjustment`(*self*, *x*, *y*, *width*, *height*)[¶](#wx.ribbon.RibbonPage.SetSizeWithScrollButtonAdjustment "Permalink to this definition")
Set the size of the page and the external scroll buttons (if any).


When a page is too small to display all of its children, scroll buttons will appear (and if the page is sized up enough, they will disappear again). Slightly counter-intuitively, these buttons are created as siblings of the page rather than children of the page (to achieve correct cropping and paint ordering of the children and the buttons). When there are no scroll buttons, this function behaves the same as `SetSize` , however when there are scroll buttons, it positions them at the edges of the given area, and then calls `SetSize` with the remaining area.


This is provided as a separate function to `SetSize` rather than within the implementation of `SetSize` , as interacting algorithms may not expect `SetSize` to also set the size of siblings.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **width** (*int*) –
* **height** (*int*) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonPage.html
        """

    Icon: 'Bitmap'  # `Icon`[¶](#wx.ribbon.RibbonPage.Icon "Permalink to this definition")See [`GetIcon`](#wx.ribbon.RibbonPage.GetIcon "wx.ribbon.RibbonPage.GetIcon")
    MajorAxis: 'Orientation'  # `MajorAxis`[¶](#wx.ribbon.RibbonPage.MajorAxis "Permalink to this definition")See [`GetMajorAxis`](#wx.ribbon.RibbonPage.GetMajorAxis "wx.ribbon.RibbonPage.GetMajorAxis")



HORIZONTAL: int

VERTICAL: int

BOTH: int

RibbonButtonKind: TypeAlias = int  # Enumeration

RIBBON_BUTTON_NORMAL: int

RIBBON_BUTTON_DROPDOWN: int

RIBBON_BUTTON_HYBRID: int

RIBBON_BUTTON_TOGGLE: int

RibbonButtonBarButtonState: TypeAlias = int  # Enumeration

RIBBON_BUTTONBAR_BUTTON_SIZE_MASK: int

RIBBON_BUTTONBAR_BUTTON_NORMAL_HOVERED: int

RIBBON_BUTTONBAR_BUTTON_DROPDOWN_HOVERED: int

RIBBON_BUTTONBAR_BUTTON_HOVER_MASK: int

RIBBON_BUTTONBAR_BUTTON_NORMAL_ACTIVE: int

RIBBON_BUTTONBAR_BUTTON_DROPDOWN_ACTIVE: int

RIBBON_BUTTONBAR_BUTTON_ACTIVE_MASK: int

RIBBON_BUTTONBAR_BUTTON_TOGGLED: int

RIBBON_BUTTONBAR_BUTTON_STATE_MASK: int

RibbonDisplayMode: TypeAlias = int  # Enumeration

RIBBON_BAR_PINNED: int

RIBBON_BAR_MINIMIZED: int

RIBBON_BAR_EXPANDED: int

RibbonGalleryButtonState: TypeAlias = int  # Enumeration

RIBBON_GALLERY_BUTTON_NORMAL: int

RIBBON_GALLERY_BUTTON_HOVERED: int

RIBBON_GALLERY_BUTTON_ACTIVE: int

RIBBON_GALLERY_BUTTON_DISABLED: int

class RibbonAUIArtProvider(RibbonMSWArtProvider):
    """ **Possible constructors**:



```
RibbonAUIArtProvider()

```


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.ribbon.RibbonAUIArtProvider.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def Clone(self) -> 'RibbonArtProvider':
        """ 

`Clone`(*self*)[¶](#wx.ribbon.RibbonAUIArtProvider.Clone "Permalink to this definition")
Create a new art provider which is a clone of this one.



Return type
 [wx.ribbon.RibbonArtProvider](wx.ribbon.RibbonArtProvider.html#wx-ribbon-ribbonartprovider)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawButtonBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawButtonBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which will typically be the button bar itself, though this is not guaranteed).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ 

`DrawButtonBarButton`(*self*, *dc*, *wnd*, *rect*, *kind*, *state*, *label*, *bitmap\_large*, *bitmap\_small*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawButtonBarButton "Permalink to this definition")
Draw a single button for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be a size previously returned by [`GetButtonBarButtonSize`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonSize "wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonSize") , and the rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawButtonBarBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawButtonBarBackground "wx.ribbon.RibbonAUIArtProvider.DrawButtonBarBackground") .
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button to draw (normal, dropdown or hybrid).
* **state** (*long*) – Combination of a size flag and state flags from the RibbonButtonBarButtonState enumeration.
* **label** (*string*) – The label of the button.
* **bitmap\_large** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The large bitmap of the button (or the large disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The small bitmap of the button (or the small disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawGalleryBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawGalleryBackground "Permalink to this definition")
Draw the background and chrome for a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This should draw the border, background, scroll buttons, extension button, and any other UI elements which are not attached to a specific gallery item.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery whose background and chrome is being drawn. Attributes used during drawing like the gallery hover state and individual button states can be queried from this parameter by [`wx.ribbon.RibbonGallery.IsHovered`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.IsHovered "wx.ribbon.RibbonGallery.IsHovered") , [`wx.ribbon.RibbonGallery.GetExtensionButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetExtensionButtonState "wx.ribbon.RibbonGallery.GetExtensionButtonState") , [`wx.ribbon.RibbonGallery.GetUpButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetUpButtonState "wx.ribbon.RibbonGallery.GetUpButtonState") , and [`wx.ribbon.RibbonGallery.GetDownButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetDownButtonState "wx.ribbon.RibbonGallery.GetDownButtonState") .
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is the entire area of the gallery control, not just the client rectangle.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ 

`DrawGalleryItemBackground`(*self*, *dc*, *wnd*, *rect*, *item*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawGalleryItemBackground "Permalink to this definition")
Draw the background of a single item in a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This is painted on top of a gallery background, and behind the items bitmap. Unlike [`DrawButtonBarButton`](#wx.ribbon.RibbonAUIArtProvider.DrawButtonBarButton "wx.ribbon.RibbonAUIArtProvider.DrawButtonBarButton") and [`DrawTool`](#wx.ribbon.RibbonAUIArtProvider.DrawTool "wx.ribbon.RibbonAUIArtProvider.DrawTool") , it is not expected to draw the item bitmap - that is done by the gallery control itself.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery which contains the item being drawn.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be the size of the item’s bitmap, expanded by gallery item padding values (wx``wx.ribbon.RIBBON\_ART\_GALLERY\_BITMAP\_PADDING\_LEFT\_SIZE``, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE`, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE`, and `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE`). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawGalleryBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawGalleryBackground "wx.ribbon.RibbonAUIArtProvider.DrawGalleryBackground") .
* **item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – The item whose background is being painted. Typically the background will vary if the item is hovered, active, or selected; [`wx.ribbon.RibbonGallery.GetSelection`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetSelection "wx.ribbon.RibbonGallery.GetSelection") , [`wx.ribbon.RibbonGallery.GetActiveItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetActiveItem "wx.ribbon.RibbonGallery.GetActiveItem") , and [`wx.ribbon.RibbonGallery.GetHoveredItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetHoveredItem "wx.ribbon.RibbonGallery.GetHoveredItem") can be called to test if the given item is in one of these states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ 

`DrawMinimisedPanel`(*self*, *dc*, *wnd*, *rect*, *bitmap*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawMinimisedPanel "Permalink to this definition")
Draw a minimised ribbon panel.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel which is minimised. The panel label can be obtained from this window. The minimised icon obtained from querying the window may not be the size requested by [`GetMinimisedPanelMinimumSize`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") - the *bitmap* argument contains the icon in the requested size.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of the rectangle will be at least the size returned by [`GetMinimisedPanelMinimumSize`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – A copy of the panel’s minimised bitmap rescaled to the size returned by [`GetMinimisedPanelMinimumSize`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPageBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawPageBackground "Permalink to this definition")
Draw the background of a ribbon page.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which is commonly the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) whose background is being drawn, but doesn’t have to be).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.





See also


[`GetPageBackgroundRedrawArea`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetPageBackgroundRedrawArea "wx.ribbon.RibbonMSWArtProvider.GetPageBackgroundRedrawArea")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPanelBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawPanelBackground "Permalink to this definition")
Draw the background and chrome for a ribbon panel.


This should draw the border, background, label, and any other items of a panel which are outside the client area of a panel.


Note that when a panel is minimised, this function is not called - only [`DrawMinimisedPanel`](#wx.ribbon.RibbonAUIArtProvider.DrawMinimisedPanel "wx.ribbon.RibbonAUIArtProvider.DrawMinimisedPanel") is called, so a background should be explicitly painted by that if required.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ 

`DrawScrollButton`(*self*, *dc*, *wnd*, *rect*, *style*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawScrollButton "Permalink to this definition")
Draw a ribbon-style scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be at least the size returned by [`GetScrollButtonMinimumSize`](#wx.ribbon.RibbonAUIArtProvider.GetScrollButtonMinimumSize "wx.ribbon.RibbonAUIArtProvider.GetScrollButtonMinimumSize") for a scroll button with the same style. For tab scroll buttons, this rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground") , but this is not guaranteed for other types of button (for example, page scroll buttons will not be painted on an area previously painted with [`DrawPageBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawPageBackground "wx.ribbon.RibbonAUIArtProvider.DrawPageBackground") ).
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, a for flag, and one or more states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *tab*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawTab "Permalink to this definition")
Draw a single tab in the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (not the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) associated with the tab being drawn).
* **tab** ([*wx.ribbon.RibbonPageTabInfo*](wx.ribbon.RibbonPageTabInfo.html#wx.ribbon.RibbonPageTabInfo "wx.ribbon.RibbonPageTabInfo")) – The rectangle within which to draw, and also the tab label, icon, and state (active and/or hovered). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground") . The rectangle’s width will be at least the minimum value returned by [`GetBarTabWidth`](#wx.ribbon.RibbonAUIArtProvider.GetBarTabWidth "wx.ribbon.RibbonAUIArtProvider.GetBarTabWidth") , and height will be the value returned by [`GetTabCtrlHeight`](#wx.ribbon.RibbonAUIArtProvider.GetTabCtrlHeight "wx.ribbon.RibbonAUIArtProvider.GetTabCtrlHeight") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawTabCtrlBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground "Permalink to this definition")
Draw the background of the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ 

`DrawTabSeparator`(*self*, *dc*, *wnd*, *rect*, *visibility*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawTabSeparator "Permalink to this definition")
Draw a separator between two tabs in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw, which will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonAUIArtProvider.DrawTabCtrlBackground") .
* **visibility** (*float*) – The opacity with which to draw the separator. Values are in the range `[0`, `1]`, with 0 being totally transparent, and 1 being totally opaque.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ 

`DrawTool`(*self*, *dc*, *wnd*, *rect*, *bitmap*, *kind*, *state*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawTool "Permalink to this definition")
Draw a single tool (for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will at least the size returned by [`GetToolSize`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetToolSize "wx.ribbon.RibbonMSWArtProvider.GetToolSize") , and the height of it will be equal for all tools within the same group. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolGroupBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonAUIArtProvider.DrawToolGroupBackground") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap to use as the tool’s foreground. If the tool is a hybrid or dropdown tool, then the foreground should also contain a standard dropdown button.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool to draw (normal, dropdown, or hybrid).
* **state** (*long*) – A combination of RibbonToolBarToolState flags giving the state of the tool and it’s relative position within a tool group.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawToolBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. Some of this rectangle will later be drawn over using [`DrawToolGroupBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonAUIArtProvider.DrawToolGroupBackground") and [`DrawTool`](#wx.ribbon.RibbonAUIArtProvider.DrawTool "wx.ribbon.RibbonAUIArtProvider.DrawTool") , but not all of it will (unless there is only a single group of tools).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolGroupBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.DrawToolGroupBackground "Permalink to this definition")
Draw the background for a group of tools on a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is a union of the individual tools’ rectangles. As there are no gaps between tools, this rectangle will be painted over exactly once by calls to [`DrawTool`](#wx.ribbon.RibbonAUIArtProvider.DrawTool "wx.ribbon.RibbonAUIArtProvider.DrawTool") . The group background could therefore be painted by [`DrawTool`](#wx.ribbon.RibbonAUIArtProvider.DrawTool "wx.ribbon.RibbonAUIArtProvider.DrawTool") , though it can be conceptually easier and more efficient to draw it all at once here. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolBarBackground`](#wx.ribbon.RibbonAUIArtProvider.DrawToolBarBackground "wx.ribbon.RibbonAUIArtProvider.DrawToolBarBackground") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ 

`GetBarTabWidth`(*self*, *dc*, *wnd*, *label*, *bitmap*, *ideal*, *small\_begin\_need\_separator*, *small\_must\_have\_separator*, *minimum*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetBarTabWidth "Permalink to this definition")
Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tab will eventually be drawn.
* **label** (*string*) – The tab’s label (or “” if it has none).
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The tab’s icon (or NullBitmap if it has none).
* **ideal** (*int*) – The ideal width (in pixels) of the tab.
* **small\_begin\_need\_separator** (*int*) – A size less than the *ideal* size, at which a tab separator should begin to be drawn (i.e. drawn, but still fairly transparent).
* **small\_must\_have\_separator** (*int*) – A size less than the *small\_begin\_need\_separator* size, at which a tab separator must be drawn (i.e. drawn at full opacity).
* **minimum** (*int*) – A size less than the *small\_must\_have\_separator* size, and greater than or equal to zero, which is the minimum pixel width for the tab.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ 

`GetColour`(*self*, *id*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetColour "Permalink to this definition")
Get the value of a certain colour setting.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ 

`GetPanelClientSize`(*self*, *dc*, *wnd*, *size*, *client\_offset*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetPanelClientSize "Permalink to this definition")
Calculate the client size of a panel for a given overall size.


This should act as the inverse to [`GetPanelSize`](#wx.ribbon.RibbonAUIArtProvider.GetPanelSize "wx.ribbon.RibbonAUIArtProvider.GetPanelSize") , and decrement the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The overall size to calculate client size for.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the returned client size begins within the given *size* (may be `None`).



Return type
*Size*





See also


[`GetPanelSize`](#wx.ribbon.RibbonAUIArtProvider.GetPanelSize "wx.ribbon.RibbonAUIArtProvider.GetPanelSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ 

`GetPanelExtButtonArea`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetPanelExtButtonArea "Permalink to this definition")
Calculate the position and size of the panel extension button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The panel rectangle from which calculate extension button rectangle.



Return type
*Rect*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ 

`GetPanelSize`(*self*, *dc*, *wnd*, *client\_size*, *client\_offset*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetPanelSize "Permalink to this definition")
Calculate the size of a panel for a given client size.


This should increment the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **client\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The client size.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the client rectangle begins within the panel (may be `None`).



Return type
*Size*





See also


[`GetPanelClientSize`](#wx.ribbon.RibbonAUIArtProvider.GetPanelClientSize "wx.ribbon.RibbonAUIArtProvider.GetPanelClientSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ 

`GetScrollButtonMinimumSize`(*self*, *dc*, *wnd*, *style*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetScrollButtonMinimumSize "Permalink to this definition")
Calculate the minimum size (in pixels) of a scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the scroll button will eventually be drawn.
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, and a for flag (state flags may be given too, but should be ignored, as a button should retain a constant size, regardless of its state).



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ 

`GetTabCtrlHeight`(*self*, *dc*, *wnd*, *pages*)[¶](#wx.ribbon.RibbonAUIArtProvider.GetTabCtrlHeight "Permalink to this definition")
Calculate the height (in pixels) of the tab region of a ribbon bar.


Note that as the tab region can contain scroll buttons, the height should be greater than or equal to the minimum height for a tab scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tabs will eventually be drawn.
* **pages** (*RibbonPageTabInfoArray*) – The tabs which will acquire the returned height.



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ 

`SetColour`(*self*, *id*, *colour*)[¶](#wx.ribbon.RibbonAUIArtProvider.SetColour "Permalink to this definition")
Set the value of a certain colour setting to the value *colour*.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting), though not all colour settings will have an effect on every art provider.



Parameters
* **id** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColourScheme`](#wx.ribbon.RibbonAUIArtProvider.SetColourScheme "wx.ribbon.RibbonAUIArtProvider.SetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ 

`SetColourScheme`(*self*, *primary*, *secondary*, *tertiary*)[¶](#wx.ribbon.RibbonAUIArtProvider.SetColourScheme "Permalink to this definition")
Set all applicable colour settings from a few base colours.


Uses any or all of the three given colours to create a colour scheme, and then sets all colour settings which are relevant to the art provider using that scheme. Note that some art providers may not use the tertiary colour for anything, and some may not use the secondary colour either.



Parameters
* **primary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **secondary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **tertiary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColour`](#wx.ribbon.RibbonAUIArtProvider.SetColour "wx.ribbon.RibbonAUIArtProvider.SetColour")




See also


[`GetColourScheme`](wx.ribbon.RibbonMSWArtProvider.html#wx.ribbon.RibbonMSWArtProvider.GetColourScheme "wx.ribbon.RibbonMSWArtProvider.GetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ 

`SetFont`(*self*, *id*, *font*)[¶](#wx.ribbon.RibbonAUIArtProvider.SetFont "Permalink to this definition")
Set the value of a certain font setting to the value *font*.


*id* can be one of the font values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
* **id** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonAUIArtProvider.html
        """



class RibbonMSWArtProvider(RibbonArtProvider):
    """ **Possible constructors**:



```
RibbonMSWArtProvider(set_colour_scheme=True)

```


  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
    """
    def __init__(self, set_colour_scheme: bool=True) -> None:
        """ 

`__init__`(*self*, *set\_colour\_scheme=True*)[¶](#wx.ribbon.RibbonMSWArtProvider.__init__ "Permalink to this definition")

Parameters
**set\_colour\_scheme** (*bool*) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def Clone(self) -> 'RibbonArtProvider':
        """ 

`Clone`(*self*)[¶](#wx.ribbon.RibbonMSWArtProvider.Clone "Permalink to this definition")
Create a new art provider which is a clone of this one.



Return type
 [wx.ribbon.RibbonArtProvider](wx.ribbon.RibbonArtProvider.html#wx-ribbon-ribbonartprovider)






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawButtonBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawButtonBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawButtonBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which will typically be the button bar itself, though this is not guaranteed).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawButtonBarButton(self, dc, wnd, rect, kind, state, label, bitmap_large, bitmap_small) -> None:
        """ 

`DrawButtonBarButton`(*self*, *dc*, *wnd*, *rect*, *kind*, *state*, *label*, *bitmap\_large*, *bitmap\_small*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawButtonBarButton "Permalink to this definition")
Draw a single button for a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be a size previously returned by [`GetButtonBarButtonSize`](#wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonSize "wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonSize") , and the rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawButtonBarBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawButtonBarBackground "wx.ribbon.RibbonMSWArtProvider.DrawButtonBarBackground") .
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button to draw (normal, dropdown or hybrid).
* **state** (*long*) – Combination of a size flag and state flags from the RibbonButtonBarButtonState enumeration.
* **label** (*string*) – The label of the button.
* **bitmap\_large** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The large bitmap of the button (or the large disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).
* **bitmap\_small** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The small bitmap of the button (or the small disabled bitmap when `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_DISABLED` is set in *state*).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawGalleryBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawGalleryBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawGalleryBackground "Permalink to this definition")
Draw the background and chrome for a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This should draw the border, background, scroll buttons, extension button, and any other UI elements which are not attached to a specific gallery item.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery whose background and chrome is being drawn. Attributes used during drawing like the gallery hover state and individual button states can be queried from this parameter by [`wx.ribbon.RibbonGallery.IsHovered`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.IsHovered "wx.ribbon.RibbonGallery.IsHovered") , [`wx.ribbon.RibbonGallery.GetExtensionButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetExtensionButtonState "wx.ribbon.RibbonGallery.GetExtensionButtonState") , [`wx.ribbon.RibbonGallery.GetUpButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetUpButtonState "wx.ribbon.RibbonGallery.GetUpButtonState") , and [`wx.ribbon.RibbonGallery.GetDownButtonState`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetDownButtonState "wx.ribbon.RibbonGallery.GetDownButtonState") .
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is the entire area of the gallery control, not just the client rectangle.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawGalleryItemBackground(self, dc, wnd, rect, item) -> None:
        """ 

`DrawGalleryItemBackground`(*self*, *dc*, *wnd*, *rect*, *item*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawGalleryItemBackground "Permalink to this definition")
Draw the background of a single item in a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control.


This is painted on top of a gallery background, and behind the items bitmap. Unlike [`DrawButtonBarButton`](#wx.ribbon.RibbonMSWArtProvider.DrawButtonBarButton "wx.ribbon.RibbonMSWArtProvider.DrawButtonBarButton") and [`DrawTool`](#wx.ribbon.RibbonMSWArtProvider.DrawTool "wx.ribbon.RibbonMSWArtProvider.DrawTool") , it is not expected to draw the item bitmap - that is done by the gallery control itself.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The window which is being drawn onto, which is always the gallery which contains the item being drawn.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be the size of the item’s bitmap, expanded by gallery item padding values (wx``wx.ribbon.RIBBON\_ART\_GALLERY\_BITMAP\_PADDING\_LEFT\_SIZE``, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_RIGHT_SIZE`, `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_TOP_SIZE`, and `wx.ribbon.RIBBON_ART_GALLERY_BITMAP_PADDING_BOTTOM_SIZE`). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawGalleryBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawGalleryBackground "wx.ribbon.RibbonMSWArtProvider.DrawGalleryBackground") .
* **item** ([*RibbonGalleryItem*](wx.lib.agw.ribbon.gallery.RibbonGalleryItem.html#wx.lib.agw.ribbon.gallery.RibbonGalleryItem "wx.lib.agw.ribbon.gallery.RibbonGalleryItem")) – The item whose background is being painted. Typically the background will vary if the item is hovered, active, or selected; [`wx.ribbon.RibbonGallery.GetSelection`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetSelection "wx.ribbon.RibbonGallery.GetSelection") , [`wx.ribbon.RibbonGallery.GetActiveItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetActiveItem "wx.ribbon.RibbonGallery.GetActiveItem") , and [`wx.ribbon.RibbonGallery.GetHoveredItem`](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery.GetHoveredItem "wx.ribbon.RibbonGallery.GetHoveredItem") can be called to test if the given item is in one of these states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawHelpButton(self, dc, wnd, rect) -> None:
        """ 

`DrawHelpButton`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawHelpButton "Permalink to this definition")
Draw help button on  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar).


This should draw a help button at top right corner of ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawMinimisedPanel(self, dc, wnd, rect, bitmap) -> None:
        """ 

`DrawMinimisedPanel`(*self*, *dc*, *wnd*, *rect*, *bitmap*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawMinimisedPanel "Permalink to this definition")
Draw a minimised ribbon panel.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel which is minimised. The panel label can be obtained from this window. The minimised icon obtained from querying the window may not be the size requested by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") - the *bitmap* argument contains the icon in the requested size.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of the rectangle will be at least the size returned by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – A copy of the panel’s minimised bitmap rescaled to the size returned by [`GetMinimisedPanelMinimumSize`](#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawPageBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPageBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawPageBackground "Permalink to this definition")
Draw the background of a ribbon page.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (which is commonly the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) whose background is being drawn, but doesn’t have to be).
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.





See also


[`GetPageBackgroundRedrawArea`](#wx.ribbon.RibbonMSWArtProvider.GetPageBackgroundRedrawArea "wx.ribbon.RibbonMSWArtProvider.GetPageBackgroundRedrawArea")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawPanelBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawPanelBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawPanelBackground "Permalink to this definition")
Draw the background and chrome for a ribbon panel.


This should draw the border, background, label, and any other items of a panel which are outside the client area of a panel.


Note that when a panel is minimised, this function is not called - only [`DrawMinimisedPanel`](#wx.ribbon.RibbonMSWArtProvider.DrawMinimisedPanel "wx.ribbon.RibbonMSWArtProvider.DrawMinimisedPanel") is called, so a background should be explicitly painted by that if required.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawScrollButton(self, dc, wnd, rect, style) -> None:
        """ 

`DrawScrollButton`(*self*, *dc*, *wnd*, *rect*, *style*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawScrollButton "Permalink to this definition")
Draw a ribbon-style scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will be at least the size returned by [`GetScrollButtonMinimumSize`](#wx.ribbon.RibbonMSWArtProvider.GetScrollButtonMinimumSize "wx.ribbon.RibbonMSWArtProvider.GetScrollButtonMinimumSize") for a scroll button with the same style. For tab scroll buttons, this rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground") , but this is not guaranteed for other types of button (for example, page scroll buttons will not be painted on an area previously painted with [`DrawPageBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawPageBackground "wx.ribbon.RibbonMSWArtProvider.DrawPageBackground") ).
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, a for flag, and one or more states.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTab(self, dc, wnd, tab) -> None:
        """ 

`DrawTab`(*self*, *dc*, *wnd*, *tab*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawTab "Permalink to this definition")
Draw a single tab in the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto (not the  [wx.ribbon.RibbonPage](wx.ribbon.RibbonPage.html#wx-ribbon-ribbonpage) associated with the tab being drawn).
* **tab** ([*wx.ribbon.RibbonPageTabInfo*](wx.ribbon.RibbonPageTabInfo.html#wx.ribbon.RibbonPageTabInfo "wx.ribbon.RibbonPageTabInfo")) – The rectangle within which to draw, and also the tab label, icon, and state (active and/or hovered). The drawing rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground") . The rectangle’s width will be at least the minimum value returned by [`GetBarTabWidth`](#wx.ribbon.RibbonMSWArtProvider.GetBarTabWidth "wx.ribbon.RibbonMSWArtProvider.GetBarTabWidth") , and height will be the value returned by [`GetTabCtrlHeight`](#wx.ribbon.RibbonMSWArtProvider.GetTabCtrlHeight "wx.ribbon.RibbonMSWArtProvider.GetTabCtrlHeight") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTabCtrlBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawTabCtrlBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground "Permalink to this definition")
Draw the background of the tab region of a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTabSeparator(self, dc, wnd, rect, visibility) -> None:
        """ 

`DrawTabSeparator`(*self*, *dc*, *wnd*, *rect*, *visibility*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawTabSeparator "Permalink to this definition")
Draw a separator between two tabs in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw, which will be entirely within a rectangle on the same device context previously painted with [`DrawTabCtrlBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground "wx.ribbon.RibbonMSWArtProvider.DrawTabCtrlBackground") .
* **visibility** (*float*) – The opacity with which to draw the separator. Values are in the range `[0`, `1]`, with 0 being totally transparent, and 1 being totally opaque.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToggleButton(self, dc, wnd, rect, mode) -> None:
        """ 

`DrawToggleButton`(*self*, *dc*, *wnd*, *rect*, *mode*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawToggleButton "Permalink to this definition")
Draw toggle button on  [wx.ribbon.RibbonBar](wx.ribbon.RibbonBar.html#wx-ribbon-ribbonbar).


This should draw a small toggle button at top right corner of ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.ribbon.RibbonBar*](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar "wx.ribbon.RibbonBar")) – The window which is being drawn onto, which is always the panel whose background and chrome is being drawn. The panel label and other panel attributes can be obtained by querying this.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw.
* **mode** ([*RibbonDisplayMode*](wx.ribbon.RibbonDisplayMode.enumeration.html "RibbonDisplayMode")) – The RibbonDisplayMode which should be applied to display button





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawTool(self, dc, wnd, rect, bitmap, kind, state) -> None:
        """ 

`DrawTool`(*self*, *dc*, *wnd*, *rect*, *bitmap*, *kind*, *state*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawTool "Permalink to this definition")
Draw a single tool (for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. The size of this rectangle will at least the size returned by [`GetToolSize`](#wx.ribbon.RibbonMSWArtProvider.GetToolSize "wx.ribbon.RibbonMSWArtProvider.GetToolSize") , and the height of it will be equal for all tools within the same group. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolGroupBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonMSWArtProvider.DrawToolGroupBackground") .
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap to use as the tool’s foreground. If the tool is a hybrid or dropdown tool, then the foreground should also contain a standard dropdown button.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool to draw (normal, dropdown, or hybrid).
* **state** (*long*) – A combination of RibbonToolBarToolState flags giving the state of the tool and it’s relative position within a tool group.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToolBarBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolBarBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawToolBarBackground "Permalink to this definition")
Draw the background for a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. Some of this rectangle will later be drawn over using [`DrawToolGroupBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawToolGroupBackground "wx.ribbon.RibbonMSWArtProvider.DrawToolGroupBackground") and [`DrawTool`](#wx.ribbon.RibbonMSWArtProvider.DrawTool "wx.ribbon.RibbonMSWArtProvider.DrawTool") , but not all of it will (unless there is only a single group of tools).






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def DrawToolGroupBackground(self, dc, wnd, rect) -> None:
        """ 

`DrawToolGroupBackground`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.DrawToolGroupBackground "Permalink to this definition")
Draw the background for a group of tools on a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar) control.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to draw onto.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window which is being drawn onto. In most cases this will be a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar), but it doesn’t have to be.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within which to draw. This rectangle is a union of the individual tools’ rectangles. As there are no gaps between tools, this rectangle will be painted over exactly once by calls to [`DrawTool`](#wx.ribbon.RibbonMSWArtProvider.DrawTool "wx.ribbon.RibbonMSWArtProvider.DrawTool") . The group background could therefore be painted by [`DrawTool`](#wx.ribbon.RibbonMSWArtProvider.DrawTool "wx.ribbon.RibbonMSWArtProvider.DrawTool") , though it can be conceptually easier and more efficient to draw it all at once here. The rectangle will be entirely within a rectangle on the same device context previously painted with [`DrawToolBarBackground`](#wx.ribbon.RibbonMSWArtProvider.DrawToolBarBackground "wx.ribbon.RibbonMSWArtProvider.DrawToolBarBackground") .






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetBarTabWidth(self, dc, wnd, label, bitmap, ideal, small_begin_need_separator, small_must_have_separator, minimum) -> None:
        """ 

`GetBarTabWidth`(*self*, *dc*, *wnd*, *label*, *bitmap*, *ideal*, *small\_begin\_need\_separator*, *small\_must\_have\_separator*, *minimum*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetBarTabWidth "Permalink to this definition")
Calculate the ideal and minimum width (in pixels) of a tab in a ribbon bar.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tab will eventually be drawn.
* **label** (*string*) – The tab’s label (or “” if it has none).
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The tab’s icon (or NullBitmap if it has none).
* **ideal** (*int*) – The ideal width (in pixels) of the tab.
* **small\_begin\_need\_separator** (*int*) – A size less than the *ideal* size, at which a tab separator should begin to be drawn (i.e. drawn, but still fairly transparent).
* **small\_must\_have\_separator** (*int*) – A size less than the *small\_begin\_need\_separator* size, at which a tab separator must be drawn (i.e. drawn at full opacity).
* **minimum** (*int*) – A size less than the *small\_must\_have\_separator* size, and greater than or equal to zero, which is the minimum pixel width for the tab.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetBarToggleButtonArea(self, rect: 'Rect') -> 'Rect':
        """ 

`GetBarToggleButtonArea`(*self*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetBarToggleButtonArea "Permalink to this definition")
Calculate the position and size of the ribbon’s toggle button.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The ribbon bar rectangle from which calculate toggle button rectangle.



Return type
*Rect*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetButtonBarButtonSize(self, dc, wnd, kind, size, label, text_min_width, bitmap_size_large, bitmap_size_small, button_size, normal_region, dropdown_region) -> bool:
        """ 

`GetButtonBarButtonSize`(*self*, *dc*, *wnd*, *kind*, *size*, *label*, *text\_min\_width*, *bitmap\_size\_large*, *bitmap\_size\_small*, *button\_size*, *normal\_region*, *dropdown\_region*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonSize "Permalink to this definition")
Calculate the size of a button within a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the button will eventually be drawn (which is normally a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar), though this is not guaranteed).
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button.
* **size** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The size-class to calculate the size for. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`. If the requested size-class is not applicable, then `False` should be returned.
* **label** (*string*) – The label of the button.
* **text\_min\_width** (*int*) – The minimum width of the button label. Set this to 0 if it is not used.
* **bitmap\_size\_large** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of all “large” bitmaps on the button bar.
* **bitmap\_size\_small** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of all “small” bitmaps on the button bar.
* **button\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size, in pixels, of the button.
* **normal\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The region of the button which constitutes the normal button.
* **dropdown\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The region of the button which constitutes the dropdown button.



Return type
*bool*



Returns
`True` if a size exists for the button, `False` otherwise.






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetButtonBarButtonTextWidth(self, dc, label, kind, size) -> 'Coord':
        """ 

`GetButtonBarButtonTextWidth`(*self*, *dc*, *label*, *kind*, *size*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetButtonBarButtonTextWidth "Permalink to this definition")
Gets the width of the string if it is used as a  [wx.ribbon.RibbonButtonBar](wx.ribbon.RibbonButtonBar.html#wx-ribbon-ribbonbuttonbar) button label.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **label** (*string*) – The string whose width shall be calculated.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of button.
* **size** ([*RibbonButtonBarButtonState*](wx.ribbon.RibbonButtonBarButtonState.enumeration.html "RibbonButtonBarButtonState")) – The size-class to calculate the size for. Buttons on a button bar can have three distinct sizes: `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_SMALL`, `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_MEDIUM`, and `wx.ribbon.RIBBON_BUTTONBAR_BUTTON_LARGE`. If the requested size-class is not applicable, then `None` should be returned.



Return type
*wx.Coord*



Returns
Width of the given label text in pixel.





New in version 4.1/wxWidgets-3.1.2.




Note


This function only works with single-line strings.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetColour(self, id: int) -> 'Colour':
        """ 

`GetColour`(*self*, *id*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetColour "Permalink to this definition")
Get the value of a certain colour setting.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetColourScheme(self) -> tuple:
        """ 

`GetColourScheme`(*self*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetColourScheme "Permalink to this definition")
Get the current colour scheme.


Returns three colours such that if [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") were called with them, the colour scheme would be restored to what it was when [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") was last called. In practice, this usually means that the returned values are the three colours given in the last call to [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") , however if [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") performs an idempotent operation upon the colours it is given (like clamping a component of the colour), then the returned values may not be the three colours given in the last call to [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") . If [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") has not been called, then the returned values should result in a colour scheme similar to, if not identical to, the default colours of the art provider. Note that if [`SetColour`](#wx.ribbon.RibbonMSWArtProvider.SetColour "wx.ribbon.RibbonMSWArtProvider.SetColour") is called, then [`GetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.GetColourScheme "wx.ribbon.RibbonMSWArtProvider.GetColourScheme") does not try and return a colour scheme similar to colours being used - it’s return values are dependent upon the last values given to [`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme") , as described above.



Return type
*tuple*





Note


The Python version of this method returns the three scheme colours as a tuple of [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") objects.




Returns
( *primary*, *secondary*, *tertiary* )






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetFlags "Permalink to this definition")
Get the previously set style flags.



Return type
*long*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetFont(self, id: int) -> 'Font':
        """ 

`GetFont`(*self*, *id*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetFont "Permalink to this definition")
Get the value of a certain font setting.


*id* can be one of the font values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetGalleryClientSize(self, dc, wnd, size, client_offset, scroll_up_button, scroll_down_button, extension_button) -> 'Size':
        """ 

`GetGalleryClientSize`(*self*, *dc*, *wnd*, *size*, *client\_offset*, *scroll\_up\_button*, *scroll\_down\_button*, *extension\_button*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetGalleryClientSize "Permalink to this definition")
Calculate the client size of a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control for a given size.


This should act as the inverse to [`GetGallerySize`](#wx.ribbon.RibbonMSWArtProvider.GetGallerySize "wx.ribbon.RibbonMSWArtProvider.GetGallerySize") , and decrement the given size by enough to fit the gallery border, buttons, and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The gallery in question.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The overall size to calculate the client size for.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The position within the given size at which the returned client size begins.
* **scroll\_up\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the scroll up button occupies.
* **scroll\_down\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the scroll down button occupies.
* **extension\_button** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The rectangle within the given size which the extension button occupies.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetGallerySize(self, dc, wnd, client_size) -> 'Size':
        """ 

`GetGallerySize`(*self*, *dc*, *wnd*, *client\_size*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetGallerySize "Permalink to this definition")
Calculate the size of a  [wx.ribbon.RibbonGallery](wx.ribbon.RibbonGallery.html#wx-ribbon-ribbongallery) control for a given client size.


This should increment the given size by enough to fit the gallery border, buttons, and any other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonGallery*](wx.ribbon.RibbonGallery.html#wx.ribbon.RibbonGallery "wx.ribbon.RibbonGallery")) – The gallery in question.
* **client\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The client size.



Return type
*Size*





See also


[`GetGalleryClientSize`](#wx.ribbon.RibbonMSWArtProvider.GetGalleryClientSize "wx.ribbon.RibbonMSWArtProvider.GetGalleryClientSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetMetric(self, id: int) -> int:
        """ 

`GetMetric`(*self*, *id*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetMetric "Permalink to this definition")
Get the value of a certain integer setting.


*id* can be one of the size values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
**id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetMinimisedPanelMinimumSize(self, dc, wnd, desired_bitmap_size, expanded_panel_direction) -> 'Size':
        """ 

`GetMinimisedPanelMinimumSize`(*self*, *dc*, *wnd*, *desired\_bitmap\_size*, *expanded\_panel\_direction*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetMinimisedPanelMinimumSize "Permalink to this definition")
Calculate the size of a minimised ribbon panel.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question. Attributes like the panel label can be queried from this.
* **desired\_bitmap\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Optional parameter which is filled with the size of the bitmap suitable for a minimised ribbon panel.
* **expanded\_panel\_direction** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) – Optional parameter which is filled with the direction of the minimised panel ( `EAST` or `SOUTH` depending on the style).



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPageBackgroundRedrawArea(self, dc, wnd, page_old_size, page_new_size) -> 'Rect':
        """ 

`GetPageBackgroundRedrawArea`(*self*, *dc*, *wnd*, *page\_old\_size*, *page\_new\_size*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetPageBackgroundRedrawArea "Permalink to this definition")
Calculate the portion of a page background which needs to be redrawn when a page is resized.


To optimise the drawing of page backgrounds, as small an area as possible should be returned. Of course, if the way in which a background is drawn means that the entire background needs to be repainted on resize, then the entire new size should be returned.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPage*](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage")) – The page which is being resized.
* **page\_old\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the page prior to the resize (which has already been painted).
* **page\_new\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the page after the resize.



Return type
*Rect*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelClientSize(self, dc, wnd, size, client_offset) -> 'Size':
        """ 

`GetPanelClientSize`(*self*, *dc*, *wnd*, *size*, *client\_offset*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetPanelClientSize "Permalink to this definition")
Calculate the client size of a panel for a given overall size.


This should act as the inverse to [`GetPanelSize`](#wx.ribbon.RibbonMSWArtProvider.GetPanelSize "wx.ribbon.RibbonMSWArtProvider.GetPanelSize") , and decrement the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The overall size to calculate client size for.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the returned client size begins within the given *size* (may be `None`).



Return type
*Size*





See also


[`GetPanelSize`](#wx.ribbon.RibbonMSWArtProvider.GetPanelSize "wx.ribbon.RibbonMSWArtProvider.GetPanelSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelExtButtonArea(self, dc, wnd, rect) -> 'Rect':
        """ 

`GetPanelExtButtonArea`(*self*, *dc*, *wnd*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetPanelExtButtonArea "Permalink to this definition")
Calculate the position and size of the panel extension button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The panel rectangle from which calculate extension button rectangle.



Return type
*Rect*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetPanelSize(self, dc, wnd, client_size, client_offset) -> 'Size':
        """ 

`GetPanelSize`(*self*, *dc*, *wnd*, *client\_size*, *client\_offset*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetPanelSize "Permalink to this definition")
Calculate the size of a panel for a given client size.


This should increment the given size by enough to fit the panel label and other chrome.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use if one is required for size calculations.
* **wnd** ([*wx.ribbon.RibbonPanel*](wx.ribbon.RibbonPanel.html#wx.ribbon.RibbonPanel "wx.ribbon.RibbonPanel")) – The ribbon panel in question.
* **client\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The client size.
* **client\_offset** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The offset where the client rectangle begins within the panel (may be `None`).



Return type
*Size*





See also


[`GetPanelClientSize`](#wx.ribbon.RibbonMSWArtProvider.GetPanelClientSize "wx.ribbon.RibbonMSWArtProvider.GetPanelClientSize")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetRibbonHelpButtonArea(self, rect: 'Rect') -> 'Rect':
        """ 

`GetRibbonHelpButtonArea`(*self*, *rect*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetRibbonHelpButtonArea "Permalink to this definition")
Calculate the position and size of the ribbon’s help button.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – The ribbon bar rectangle from which calculate help button rectangle.



Return type
*Rect*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetScrollButtonMinimumSize(self, dc, wnd, style) -> 'Size':
        """ 

`GetScrollButtonMinimumSize`(*self*, *dc*, *wnd*, *style*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetScrollButtonMinimumSize "Permalink to this definition")
Calculate the minimum size (in pixels) of a scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the scroll button will eventually be drawn.
* **style** (*long*) – A combination of flags from  [wx.ribbon.RibbonScrollButtonStyle](wx.ribbon.RibbonScrollButtonStyle.enumeration.html#wx-ribbon-ribbonscrollbuttonstyle), including a direction, and a for flag (state flags may be given too, but should be ignored, as a button should retain a constant size, regardless of its state).



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetTabCtrlHeight(self, dc, wnd, pages) -> int:
        """ 

`GetTabCtrlHeight`(*self*, *dc*, *wnd*, *pages*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetTabCtrlHeight "Permalink to this definition")
Calculate the height (in pixels) of the tab region of a ribbon bar.


Note that as the tab region can contain scroll buttons, the height should be greater than or equal to the minimum height for a tab scroll button.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tabs will eventually be drawn.
* **pages** (*RibbonPageTabInfoArray*) – The tabs which will acquire the returned height.



Return type
*int*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def GetToolSize(self, dc, wnd, bitmap_size, kind, is_first, is_last, dropdown_region) -> 'Size':
        """ 

`GetToolSize`(*self*, *dc*, *wnd*, *bitmap\_size*, *kind*, *is\_first*, *is\_last*, *dropdown\_region*)[¶](#wx.ribbon.RibbonMSWArtProvider.GetToolSize "Permalink to this definition")
Calculate the size of a tool within a  [wx.ribbon.RibbonToolBar](wx.ribbon.RibbonToolBar.html#wx-ribbon-ribbontoolbar).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – A device context to use when one is required for size calculations.
* **wnd** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The window onto which the tool will eventually be drawn.
* **bitmap\_size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the tool’s foreground bitmap.
* **kind** ([*RibbonButtonKind*](wx.ribbon.RibbonButtonKind.enumeration.html "RibbonButtonKind")) – The kind of tool (normal, dropdown, or hybrid).
* **is\_first** (*bool*) – `True` if the tool is the first within its group. `False` otherwise.
* **is\_last** (*bool*) – `True` if the tool is the last within its group. `False` otherwise.
* **dropdown\_region** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – For dropdown and hybrid tools, the region within the returned size which counts as the dropdown part.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetColour(self, id, colour) -> None:
        """ 

`SetColour`(*self*, *id*, *colour*)[¶](#wx.ribbon.RibbonMSWArtProvider.SetColour "Permalink to this definition")
Set the value of a certain colour setting to the value *colour*.


*id* can be one of the colour values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting), though not all colour settings will have an effect on every art provider.



Parameters
* **id** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "wx.ribbon.RibbonMSWArtProvider.SetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetColourScheme(self, primary, secondary, tertiary) -> None:
        """ 

`SetColourScheme`(*self*, *primary*, *secondary*, *tertiary*)[¶](#wx.ribbon.RibbonMSWArtProvider.SetColourScheme "Permalink to this definition")
Set all applicable colour settings from a few base colours.


Uses any or all of the three given colours to create a colour scheme, and then sets all colour settings which are relevant to the art provider using that scheme. Note that some art providers may not use the tertiary colour for anything, and some may not use the secondary colour either.



Parameters
* **primary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **secondary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **tertiary** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –





See also


[`SetColour`](#wx.ribbon.RibbonMSWArtProvider.SetColour "wx.ribbon.RibbonMSWArtProvider.SetColour")




See also


[`GetColourScheme`](#wx.ribbon.RibbonMSWArtProvider.GetColourScheme "wx.ribbon.RibbonMSWArtProvider.GetColourScheme")





            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.ribbon.RibbonMSWArtProvider.SetFlags "Permalink to this definition")
Set the style flags.


Normally called automatically by [`wx.ribbon.RibbonBar.SetArtProvider`](wx.ribbon.RibbonBar.html#wx.ribbon.RibbonBar.SetArtProvider "wx.ribbon.RibbonBar.SetArtProvider") with the ribbon bar’s style flags, so that the art provider has the same flags as the bar which it is serving.



Parameters
**flags** (*long*) – 






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetFont(self, id, font) -> None:
        """ 

`SetFont`(*self*, *id*, *font*)[¶](#wx.ribbon.RibbonMSWArtProvider.SetFont "Permalink to this definition")
Set the value of a certain font setting to the value *font*.


*id* can be one of the font values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
* **id** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    def SetMetric(self, id, new_val) -> None:
        """ 

`SetMetric`(*self*, *id*, *new\_val*)[¶](#wx.ribbon.RibbonMSWArtProvider.SetMetric "Permalink to this definition")
Set the value of a certain integer setting to the value *new\_val*.


*id* can be one of the size values of  [wx.ribbon.RibbonArtSetting](wx.ribbon.RibbonArtSetting.enumeration.html#wx-ribbon-ribbonartsetting).



Parameters
* **id** (*int*) –
* **new\_val** (*int*) –






            Source: https://docs.wxpython.org/wx.ribbon.RibbonMSWArtProvider.html
        """

    Flags: int  # `Flags`[¶](#wx.ribbon.RibbonMSWArtProvider.Flags "Permalink to this definition")See [`GetFlags`](#wx.ribbon.RibbonMSWArtProvider.GetFlags "wx.ribbon.RibbonMSWArtProvider.GetFlags") and [`SetFlags`](#wx.ribbon.RibbonMSWArtProvider.SetFlags "wx.ribbon.RibbonMSWArtProvider.SetFlags")



RibbonScrollButtonStyle: TypeAlias = int  # Enumeration

RIBBON_SCROLL_BTN_LEFT: int

RIBBON_SCROLL_BTN_RIGHT: int

RIBBON_SCROLL_BTN_UP: int

RIBBON_SCROLL_BTN_DOWN: int

RIBBON_SCROLL_BTN_DIRECTION_MASK: int

RIBBON_SCROLL_BTN_NORMAL: int

RIBBON_SCROLL_BTN_HOVERED: int

RIBBON_SCROLL_BTN_ACTIVE: int

RIBBON_SCROLL_BTN_STATE_MASK: int

RIBBON_SCROLL_BTN_FOR_OTHER: int

RIBBON_SCROLL_BTN_FOR_TABS: int

RIBBON_SCROLL_BTN_FOR_PAGE: int

RIBBON_SCROLL_BTN_FOR_MASK: int

class RibbonPageTabInfo:
    """ 
  


        Source: https://docs.wxpython.org/wx.ribbon.RibbonPageTabInfo.html
    """
    active: Any  # `active`[¶](#wx.ribbon.RibbonPageTabInfo.active "Permalink to this definition")A public C++ attribute of type `bool`.
    highlight: Any  # `highlight`[¶](#wx.ribbon.RibbonPageTabInfo.highlight "Permalink to this definition")A public C++ attribute of type `bool`.
    hovered: Any  # `hovered`[¶](#wx.ribbon.RibbonPageTabInfo.hovered "Permalink to this definition")A public C++ attribute of type `bool`.
    ideal_width: Any  # `ideal_width`[¶](#wx.ribbon.RibbonPageTabInfo.ideal_width "Permalink to this definition")A public C++ attribute of type `int`.
    minimum_width: Any  # `minimum_width`[¶](#wx.ribbon.RibbonPageTabInfo.minimum_width "Permalink to this definition")A public C++ attribute of type `int`.
    page: Any  # `page`[¶](#wx.ribbon.RibbonPageTabInfo.page "Permalink to this definition")A public C++ attribute of type [`RibbonPage`](wx.ribbon.RibbonPage.html#wx.ribbon.RibbonPage "wx.ribbon.RibbonPage") .
    rect: Any  # `rect`[¶](#wx.ribbon.RibbonPageTabInfo.rect "Permalink to this definition")A public C++ attribute of type [`Rect`](wx.Rect.html#wx.Rect "wx.Rect") .
    shown: Any  # `shown`[¶](#wx.ribbon.RibbonPageTabInfo.shown "Permalink to this definition")A public C++ attribute of type `bool`.
    small_begin_need_separator_width: Any  # `small_begin_need_separator_width`[¶](#wx.ribbon.RibbonPageTabInfo.small_begin_need_separator_width "Permalink to this definition")A public C++ attribute of type `int`.
    small_must_have_separator_width: Any  # `small_must_have_separator_width`[¶](#wx.ribbon.RibbonPageTabInfo.small_must_have_separator_width "Permalink to this definition")A public C++ attribute of type `int`.



RibbonArtSetting: TypeAlias = int  # Enumeration

RIBBON_ART_TAB_SEPARATION_SIZE: int

RIBBON_ART_PAGE_BORDER_LEFT_SIZE: int

RIBBON_ART_PAGE_BORDER_TOP_SIZE: int

RIBBON_ART_PAGE_BORDER_RIGHT_SIZE: int

RIBBON_ART_PAGE_BORDER_BOTTOM_SIZE: int

RIBBON_ART_PANEL_X_SEPARATION_SIZE: int

RIBBON_ART_PANEL_Y_SEPARATION_SIZE: int

RIBBON_ART_TOOL_GROUP_SEPARATION_SIZE: int

RIBBON_ART_GALLERY_BITMAP_PADDING_LEFT_SIZE: int

RIBBON_ART_PANEL_LABEL_FONT: int

RIBBON_ART_BUTTON_BAR_LABEL_FONT: int

RIBBON_ART_TAB_LABEL_FONT: int

RIBBON_ART_BUTTON_BAR_LABEL_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_DISABLED_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BORDER_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_BUTTON_BAR_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BORDER_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_BUTTON_BAR_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BORDER_COLOUR: int

RIBBON_ART_GALLERY_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_HOVER_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_ACTIVE_FACE_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_GALLERY_BUTTON_DISABLED_FACE_COLOUR: int

RIBBON_ART_GALLERY_ITEM_BORDER_COLOUR: int

RIBBON_ART_TAB_LABEL_COLOUR: int

RIBBON_ART_TAB_ACTIVE_LABEL_COLOUR: int

RIBBON_ART_TAB_HOVER_LABEL_COLOUR: int

RIBBON_ART_TAB_SEPARATOR_COLOUR: int

RIBBON_ART_TAB_SEPARATOR_GRADIENT_COLOUR: int

RIBBON_ART_TAB_CTRL_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_CTRL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_TAB_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TAB_BORDER_COLOUR: int

RIBBON_ART_PANEL_BORDER_COLOUR: int

RIBBON_ART_PANEL_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_HOVER_BORDER_COLOUR: int

RIBBON_ART_PANEL_HOVER_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_BORDER_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_BORDER_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_LABEL_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_LABEL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_LABEL_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_HOVER_LABEL_COLOUR: int

RIBBON_ART_PANEL_MINIMISED_LABEL_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_PANEL_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_BORDER_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_COLOUR: int

RIBBON_ART_PAGE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_PAGE_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOLBAR_BORDER_COLOUR: int

RIBBON_ART_TOOLBAR_HOVER_BORDER_COLOUR: int

RIBBON_ART_TOOLBAR_FACE_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_HOVER_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_TOP_GRADIENT_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_COLOUR: int

RIBBON_ART_TOOL_ACTIVE_BACKGROUND_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_GRADIENT_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_TOP_COLOUR: int

RIBBON_ART_BUTTON_BAR_LABEL_HIGHLIGHT_GRADIENT_TOP_COLOUR: int

RibbonButtonBarButtonBase: TypeAlias = Any

RibbonToolBarToolBase: TypeAlias = Any

RibbonGalleryItem: TypeAlias = Any

