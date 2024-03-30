# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Control, Window, VisualAttributes, Rect, CheckBoxState, ClientData, _ImageList, ImageList, Icon, RefCounter, SettableHeaderColumn, Object, _EllipsizeMode, EllipsizeMode, _Size, Size, NotifyEvent, _DataFormat, _DataObject, DragResult, Point, DataFormat, DataObject, _BitmapBundle, _Icon, BitmapBundle, Colour, _Colour, Font

class DataViewCtrl(Control):
    """ **Possible constructors**:



```
DataViewCtrl()

DataViewCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
             style=0, validator=DefaultValidator, name=DataViewCtrlNameStr)

```


DataViewCtrl is a control to display data either in a tree like
fashion or in a tabular form or both.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default Constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=DataViewCtrlNameStr)*


Constructor.


Calls [`Create`](#wx.dataview.DataViewCtrl.Create "wx.dataview.DataViewCtrl.Create") .



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AllowMultiColumnSort(self, allow: bool) -> bool:
        """ 

`AllowMultiColumnSort`(*self*, *allow*)[¶](#wx.dataview.DataViewCtrl.AllowMultiColumnSort "Permalink to this definition")
Call to allow using multiple columns for sorting.


When using multiple column for sorting, `GetSortingColumns` method should be used to retrieve all the columns which should be used to effectively sort the data when processing the sorted event.


Currently multiple column sort is only implemented in the generic version, i.e. this functionality is not available when using the native  [wx.dataview.DataViewCtrl](#wx-dataview-dataviewctrl) implementation in wxGTK nor wxOSX.



Parameters
**allow** (*bool*) – 



Return type
*bool*



Returns
`True` if sorting by multiple columns could be enabled, `False` otherwise, typically because this feature is not supported.





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendBitmapColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendBitmapColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendBitmapColumn "Permalink to this definition")
Appends a column for rendering a bitmap.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendBitmapColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendBitmapColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendColumn(self, col: 'dataview.DataViewColumn') -> bool:
        """ 

`AppendColumn`(*self*, *col*)[¶](#wx.dataview.DataViewCtrl.AppendColumn "Permalink to this definition")
Appends a  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) to the control.


Returns `True` on success.


Note that there is a number of short cut methods which implicitly create a  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) and a  [wx.dataview.DataViewRenderer](wx.dataview.DataViewRenderer.html#wx-dataview-dataviewrenderer) for it (see below).



Parameters
**col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendDateColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendDateColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendDateColumn "Permalink to this definition")
Appends a column for rendering a date.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendDateColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_ACTIVATABLE, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendDateColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_ACTIVATABLE, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendIconTextColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendIconTextColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendIconTextColumn "Permalink to this definition")
Appends a column for rendering text with an icon.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure. This method uses the  [wx.dataview.DataViewIconTextRenderer](wx.dataview.DataViewIconTextRenderer.html#wx-dataview-dataviewicontextrenderer) class.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendIconTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendIconTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendProgressColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendProgressColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendProgressColumn "Permalink to this definition")
Appends a column for rendering a progress indicator.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendProgressColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=80, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendProgressColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=80, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendTextColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendTextColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendTextColumn "Permalink to this definition")
Appends a column for rendering text.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AppendToggleColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`AppendToggleColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.AppendToggleColumn "Permalink to this definition")
Appends a column for rendering a toggle.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendToggleColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=30, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**AppendToggleColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=30, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def _AssociateModel(self, model: 'dataview.DataViewModel') -> bool:
        """ 

`_AssociateModel`(*self*, *model*)[¶](#wx.dataview.DataViewCtrl._AssociateModel "Permalink to this definition")
Associates a  [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel) with the control.


This increases the reference count of the model by 1.



Parameters
**model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def AssociateModel(self, model) -> None:
        """ 

`AssociateModel`(*self*, *model*)[¶](#wx.dataview.DataViewCtrl.AssociateModel "Permalink to this definition")
Associates a `DataViewModel` with the control.
Ownership of the model object is passed to C++, however it
is reference counted so it can be shared with other views.




            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ClearColumns(self) -> bool:
        """ 

`ClearColumns`(*self*)[¶](#wx.dataview.DataViewCtrl.ClearColumns "Permalink to this definition")
Removes all columns.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Collapse(self, item: 'dataview.DataViewItem') -> None:
        """ 

`Collapse`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.Collapse "Permalink to this definition")
Collapses the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, validator=DefaultValidator, name=DataViewCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *validator=DefaultValidator*, *name=DataViewCtrlNameStr*)[¶](#wx.dataview.DataViewCtrl.Create "Permalink to this definition")
Create the control.


Useful for two step creation.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def DeleteColumn(self, column: 'dataview.DataViewColumn') -> bool:
        """ 

`DeleteColumn`(*self*, *column*)[¶](#wx.dataview.DataViewCtrl.DeleteColumn "Permalink to this definition")
Deletes given column.



Parameters
**column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EditItem(self, item, column) -> None:
        """ 

`EditItem`(*self*, *item*, *column*)[¶](#wx.dataview.DataViewCtrl.EditItem "Permalink to this definition")
Programmatically starts editing given cell of *item*.


Doesn’t do anything if the item or this column is not editable.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDragSource(self, format: 'DataFormat') -> bool:
        """ 

`EnableDragSource`(*self*, *format*)[¶](#wx.dataview.DataViewCtrl.EnableDragSource "Permalink to this definition")
Enable drag operations using the given *format*.



Parameters
**format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDropTarget(self, format: 'DataFormat') -> bool:
        """ 

`EnableDropTarget`(*self*, *format*)[¶](#wx.dataview.DataViewCtrl.EnableDropTarget "Permalink to this definition")
Enable drop operations using the given *format*.


See [`EnableDropTargets`](#wx.dataview.DataViewCtrl.EnableDropTargets "wx.dataview.DataViewCtrl.EnableDropTargets") for providing more than one supported format.



Parameters
**format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) – 



Return type
*bool*





Note


Since 3.1.6 `wx.DF_INVALID` can be passed to disable drag and drop support.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableDropTargets(self, formats: Vector) -> bool:
        """ 

`EnableDropTargets`(*self*, *formats*)[¶](#wx.dataview.DataViewCtrl.EnableDropTargets "Permalink to this definition")
Enable drop operations using any of the specified *formats*.


Currently this is fully implemented in the generic and native macOS versions. In wxGTK only the first element of the array is used.



Parameters
**formats** (*Vector*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.6.




Note


Passing empty array disables drag and drop operations completely.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnableSystemTheme(self, enable: bool=True) -> None:
        """ 

`EnableSystemTheme`(*self*, *enable=True*)[¶](#wx.dataview.DataViewCtrl.EnableSystemTheme "Permalink to this definition")
Can be used to disable the system theme of controls using it by default.


On Windows there an alternative theme available for the list and list-like
controls since Windows Vista. This theme is used by Windows Explorer list
and tree view and so is arguably more familiar to the users than the standard
appearance of these controls. This class automatically uses the new theme,
but if that is not desired then this method can be used to turn it off.


Please note that this method should be called before the widget is
actually created, using the 2-phase create pattern. Something like this:



```
# This creates the object, but not the window
widget = wx.dataview.DataViewCtrl()

# Disable the system theme
widget.EnableSystemTheme(False)

# Now create the window
widget.Create(parent, wx.``wx.ID_ANY``)

```


This method has no effect on other platorms



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def EnsureVisible(self, item, column=None) -> None:
        """ 

`EnsureVisible`(*self*, *item*, *column=None*)[¶](#wx.dataview.DataViewCtrl.EnsureVisible "Permalink to this definition")
Call this to ensure that the given item is visible.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Expand(self, item: 'dataview.DataViewItem') -> None:
        """ 

`Expand`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.Expand "Permalink to this definition")
Expands the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ExpandAncestors(self, item: 'dataview.DataViewItem') -> None:
        """ 

`ExpandAncestors`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.ExpandAncestors "Permalink to this definition")
Expands all ancestors of the *item*.


This method also ensures that the item itself as well as all ancestor items have been read from the model by the control.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ExpandChildren(self, item: 'dataview.DataViewItem') -> None:
        """ 

`ExpandChildren`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.ExpandChildren "Permalink to this definition")
Expand all children of the given item recursively.


This is the same as calling [`Expand`](#wx.dataview.DataViewCtrl.Expand "wx.dataview.DataViewCtrl.Expand") on the *item* itself and then calling it for all of its children, grandchildren etc recursively.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.dataview.DataViewCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumn(self, pos: int) -> 'DataViewColumn':
        """ 

`GetColumn`(*self*, *pos*)[¶](#wx.dataview.DataViewCtrl.GetColumn "Permalink to this definition")
Returns pointer to the column.


*pos* refers to the position in the control which may change after reordering columns by the user.



Parameters
**pos** (*int*) – 



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumnCount(self) -> int:
        """ 

`GetColumnCount`(*self*)[¶](#wx.dataview.DataViewCtrl.GetColumnCount "Permalink to this definition")
Returns the number of columns.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumnPosition(self, column: 'dataview.DataViewColumn') -> int:
        """ 

`GetColumnPosition`(*self*, *column*)[¶](#wx.dataview.DataViewCtrl.GetColumnPosition "Permalink to this definition")
Returns the position of the column or -1 if not found in the control.



Parameters
**column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetColumns(self) -> None:
        """ 

`GetColumns`(*self*)[¶](#wx.dataview.DataViewCtrl.GetColumns "Permalink to this definition")
Returns a list of column objects.




            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCountPerPage(self) -> int:
        """ 

`GetCountPerPage`(*self*)[¶](#wx.dataview.DataViewCtrl.GetCountPerPage "Permalink to this definition")
Return the number of items that can fit vertically in the visible area of the control.


Returns -1 if the number of items per page couldn’t be determined. On wxGTK this method can only determine the number of items per page if there is at least one item in the control.



Return type
*int*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCurrentColumn(self) -> 'DataViewColumn':
        """ 

`GetCurrentColumn`(*self*)[¶](#wx.dataview.DataViewCtrl.GetCurrentColumn "Permalink to this definition")
Returns the column that currently has focus.


If the focus is set to individual cell within the currently focused item (as opposed to being on the item as a whole), then this is the column that the focus is on.


Returns `None` if no column currently has focus.



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)





New in version 2.9.4.




See also


[`GetCurrentItem`](#wx.dataview.DataViewCtrl.GetCurrentItem "wx.dataview.DataViewCtrl.GetCurrentItem")





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetCurrentItem(self) -> 'DataViewItem':
        """ 

`GetCurrentItem`(*self*)[¶](#wx.dataview.DataViewCtrl.GetCurrentItem "Permalink to this definition")
Returns the currently focused item.


This is the item that the keyboard commands apply to. It may be invalid if there is no focus currently.


This method is mostly useful for the controls with `DV_MULTIPLE` style as in the case of single selection it returns the same thing as [`GetSelection`](#wx.dataview.DataViewCtrl.GetSelection "wx.dataview.DataViewCtrl.GetSelection") .


Notice that under all platforms except macOS the currently focused item may be selected or not but under macOS the current item is always selected.



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)





New in version 2.9.2.




See also


[`SetCurrentItem`](#wx.dataview.DataViewCtrl.SetCurrentItem "wx.dataview.DataViewCtrl.SetCurrentItem") , [`GetCurrentColumn`](#wx.dataview.DataViewCtrl.GetCurrentColumn "wx.dataview.DataViewCtrl.GetCurrentColumn")





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetExpanderColumn(self) -> 'DataViewColumn':
        """ 

`GetExpanderColumn`(*self*)[¶](#wx.dataview.DataViewCtrl.GetExpanderColumn "Permalink to this definition")
Returns column containing the expanders.



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetIndent(self) -> int:
        """ 

`GetIndent`(*self*)[¶](#wx.dataview.DataViewCtrl.GetIndent "Permalink to this definition")
Returns indentation.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetItemRect(self, item, col=None) -> 'Rect':
        """ 

`GetItemRect`(*self*, *item*, *col=None*)[¶](#wx.dataview.DataViewCtrl.GetItemRect "Permalink to this definition")
Returns item rectangle.


If item is not currently visible, either because its parent is collapsed or it is outside of the visible part of the control due to the current vertical scrollbar position, return an empty rectangle.


Coordinates of the rectangle are specified in  [wx.dataview.DataViewCtrl](#wx-dataview-dataviewctrl) client area coordinates.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – A valid item.
* **col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – If not `None`, the rectangle returned corresponds to the intersection of the item with the specified column. If `None`, the rectangle spans all the columns.



Return type
`Rect`






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetMainWindow(self) -> 'Window':
        """ 

`GetMainWindow`(*self*)[¶](#wx.dataview.DataViewCtrl.GetMainWindow "Permalink to this definition")
Returns the window corresponding to the main area of the control.


This is the window that actually shows the control items and may be different from  [wx.dataview.DataViewCtrl](#wx-dataview-dataviewctrl) window itself in some ports (currently this is only the case for the generic implementation used by default under MSW).



Return type
*Window*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetModel(self) -> 'DataViewModel':
        """ 

`GetModel`(*self*)[¶](#wx.dataview.DataViewCtrl.GetModel "Permalink to this definition")
Returns pointer to the data model associated with the control (if any).



Return type
 [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel)






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelectedItemsCount(self) -> int:
        """ 

`GetSelectedItemsCount`(*self*)[¶](#wx.dataview.DataViewCtrl.GetSelectedItemsCount "Permalink to this definition")
Returns the number of currently selected items.


This method may be called for both the controls with single and multiple selections and returns the number of selected item, possibly 0, in any case.



Return type
*int*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelection(self) -> 'DataViewItem':
        """ 

`GetSelection`(*self*)[¶](#wx.dataview.DataViewCtrl.GetSelection "Permalink to this definition")
Returns first selected item or an invalid item if none is selected.


This method may be called for both the controls with single and multiple selections but returns an invalid item if more than one item is selected in the latter case, use [`HasSelection`](#wx.dataview.DataViewCtrl.HasSelection "wx.dataview.DataViewCtrl.HasSelection") to determine if there are any selected items when using multiple selection.



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSelections(self) -> 'DataViewItemArray':
        """ 

`GetSelections`(*self*)[¶](#wx.dataview.DataViewCtrl.GetSelections "Permalink to this definition")
Returns a list of the currently selected items.



Return type
*DataViewItemArray*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetSortingColumn(self) -> 'DataViewColumn':
        """ 

`GetSortingColumn`(*self*)[¶](#wx.dataview.DataViewCtrl.GetSortingColumn "Permalink to this definition")
Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) currently responsible for sorting or `None` if none has been selected.



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def GetTopItem(self) -> 'DataViewItem':
        """ 

`GetTopItem`(*self*)[¶](#wx.dataview.DataViewCtrl.GetTopItem "Permalink to this definition")
Return the topmost visible item.


Returns an invalid item if there is no topmost visible item or if the method is not implemented for the current platform.



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def HasSelection(self) -> bool:
        """ 

`HasSelection`(*self*)[¶](#wx.dataview.DataViewCtrl.HasSelection "Permalink to this definition")
Returns `True` if any items are currently selected.


This method may be called for both the controls with single and multiple selections.


Calling this method is equivalent to calling [`GetSelectedItemsCount`](#wx.dataview.DataViewCtrl.GetSelectedItemsCount "wx.dataview.DataViewCtrl.GetSelectedItemsCount") and comparing its result with 0 but is more clear and might also be implemented more efficiently in the future.



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def HitTest(self, point) -> Any:
        """ 

`HitTest`(*self*, *point*)[¶](#wx.dataview.DataViewCtrl.HitTest "Permalink to this definition")

> HitTest(point) . (item, col)
> 
> 
> Returns the item and column located at point, as a 2 element tuple.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def InsertColumn(self, pos, col) -> bool:
        """ 

`InsertColumn`(*self*, *pos*, *col*)[¶](#wx.dataview.DataViewCtrl.InsertColumn "Permalink to this definition")
Inserts a  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) to the control.


Returns `True` on success.



Parameters
* **pos** (*int*) –
* **col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsExpanded(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`IsExpanded`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.IsExpanded "Permalink to this definition")
Return `True` if the item is expanded.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*





Note


When using the native macOS version this method has a bug which may result in returning `True` even for items without children.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsMultiColumnSortAllowed(self) -> bool:
        """ 

`IsMultiColumnSortAllowed`(*self*)[¶](#wx.dataview.DataViewCtrl.IsMultiColumnSortAllowed "Permalink to this definition")
Return `True` if using more than one column for sorting is allowed.


See [`AllowMultiColumnSort`](#wx.dataview.DataViewCtrl.AllowMultiColumnSort "wx.dataview.DataViewCtrl.AllowMultiColumnSort") and `GetSortingColumns` .



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def IsSelected(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`IsSelected`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.IsSelected "Permalink to this definition")
Return `True` if the item is selected.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependBitmapColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependBitmapColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependBitmapColumn "Permalink to this definition")
Prepends a column for rendering a bitmap.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependBitmapColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependBitmapColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependColumn(self, col: 'dataview.DataViewColumn') -> bool:
        """ 

`PrependColumn`(*self*, *col*)[¶](#wx.dataview.DataViewCtrl.PrependColumn "Permalink to this definition")
Prepends a  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) to the control.


Returns `True` on success.


Note that there is a number of short cut methods which implicitly create a  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) and a  [wx.dataview.DataViewRenderer](wx.dataview.DataViewRenderer.html#wx-dataview-dataviewrenderer) for it.



Parameters
**col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependDateColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependDateColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependDateColumn "Permalink to this definition")
Prepends a column for rendering a date.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependDateColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_ACTIVATABLE, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependDateColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_ACTIVATABLE, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependIconTextColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependIconTextColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependIconTextColumn "Permalink to this definition")
Prepends a column for rendering text with an icon.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure. This method uses the  [wx.dataview.DataViewIconTextRenderer](wx.dataview.DataViewIconTextRenderer.html#wx-dataview-dataviewicontextrenderer) class.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependIconTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependIconTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependProgressColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependProgressColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependProgressColumn "Permalink to this definition")
Prepends a column for rendering a progress indicator.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependProgressColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=80, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependProgressColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=80, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependTextColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependTextColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependTextColumn "Permalink to this definition")
Prepends a column for rendering text.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependTextColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=-1, align=ALIGN\_NOT, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def PrependToggleColumn(self, *args, **kw) -> 'DataViewColumn':
        """ 

`PrependToggleColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewCtrl.PrependToggleColumn "Permalink to this definition")
Prepends a column for rendering a toggle.


Returns the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) created in the function or `None` on failure.



Note


The *align* parameter is applied to both the column header and the column renderer.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependToggleColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=30, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** (*string*) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  



**PrependToggleColumn** *(self, label, model\_column, mode=DATAVIEW\_CELL\_INERT, width=30, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*



Parameters
* **label** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **model\_column** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Select(self, item: 'dataview.DataViewItem') -> None:
        """ 

`Select`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.Select "Permalink to this definition")
Select the given item.


In single selection mode this changes the (unique) currently selected item. In multi selection mode, the *item* is selected and the previously selected items remain selected.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.dataview.DataViewCtrl.SelectAll "Permalink to this definition")
Select all items.




            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetAlternateRowColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ 

`SetAlternateRowColour`(*self*, *colour*)[¶](#wx.dataview.DataViewCtrl.SetAlternateRowColour "Permalink to this definition")
Set custom colour for the alternate rows used with `wx.dataview.DV_ROW_LINES` style.


Note that calling this method has no effect if `wx.dataview.DV_ROW_LINES` is off.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – The colour to use for the alternate rows.



Return type
*bool*



Returns
`True` if customizing this colour is supported (currently only in the generic version), `False` if this method is not implemented under this platform.





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetCurrentItem(self, item: 'dataview.DataViewItem') -> None:
        """ 

`SetCurrentItem`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.SetCurrentItem "Permalink to this definition")
Changes the currently focused item.


The *item* parameter must be valid, there is no way to remove the current item from the control.


In single selection mode, calling this method is the same as calling [`Select`](#wx.dataview.DataViewCtrl.Select "wx.dataview.DataViewCtrl.Select") and is thus not very useful. In multiple selection mode this method only moves the current item however without changing the selection except under macOS where the current item is always selected, so calling [`SetCurrentItem`](#wx.dataview.DataViewCtrl.SetCurrentItem "wx.dataview.DataViewCtrl.SetCurrentItem") selects *item* if it hadn’t been selected before.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 





New in version 2.9.2.




See also


[`GetCurrentItem`](#wx.dataview.DataViewCtrl.GetCurrentItem "wx.dataview.DataViewCtrl.GetCurrentItem")





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetExpanderColumn(self, col: 'dataview.DataViewColumn') -> None:
        """ 

`SetExpanderColumn`(*self*, *col*)[¶](#wx.dataview.DataViewCtrl.SetExpanderColumn "Permalink to this definition")
Set which column shall contain the tree-like expanders.



Parameters
**col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetHeaderAttr(self, attr: 'ItemAttr') -> bool:
        """ 

`SetHeaderAttr`(*self*, *attr*)[¶](#wx.dataview.DataViewCtrl.SetHeaderAttr "Permalink to this definition")
Set custom colours and/or font to use for the header.


This method allows customizing the display of the control header (it does nothing if `DV_NO_HEADER` style is used).


Currently it is only implemented in the generic version and just returns `False` without doing anything elsewhere.



Parameters
**attr** ([*wx.ItemAttr*](wx.ItemAttr.html#wx.ItemAttr "wx.ItemAttr")) – The attribute defining the colour(s) and font to use. It can be default, in which case the attributes are reset to their default values.



Return type
*bool*



Returns
`True` if the attributes were updated, `False` if the method is not implemented or failed.





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetIndent(self, indent: int) -> None:
        """ 

`SetIndent`(*self*, *indent*)[¶](#wx.dataview.DataViewCtrl.SetIndent "Permalink to this definition")
Sets the indentation.



Parameters
**indent** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetRowHeight(self, rowHeight: int) -> bool:
        """ 

`SetRowHeight`(*self*, *rowHeight*)[¶](#wx.dataview.DataViewCtrl.SetRowHeight "Permalink to this definition")
Sets the row height.


This function can only be used when all rows have the same height, i.e. when `wx.dataview.DV_VARIABLE_LINE_HEIGHT` flag is not used.


Currently this is implemented in the generic and native GTK and macOS (since 3.1.1) versions.


Also notice that this method can only be used to increase the row height compared with the default one (as determined by the return value of *DataViewRenderer.GetSize()),* if it is set to a too small value then the minimum required by the renderers will be used.



Parameters
**rowHeight** (*int*) – 



Return type
*bool*



Returns
`True` if the line height was changed or `False` otherwise.





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def SetSelections(self, sel: DataViewItemArray) -> None:
        """ 

`SetSelections`(*self*, *sel*)[¶](#wx.dataview.DataViewCtrl.SetSelections "Permalink to this definition")
Sets the selection to the array of DataViewItems.


Note that if *sel* contains any invalid items, they are simply ignored.



Parameters
**sel** (*DataViewItemArray*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def ToggleSortByColumn(self, column: int) -> None:
        """ 

`ToggleSortByColumn`(*self*, *column*)[¶](#wx.dataview.DataViewCtrl.ToggleSortByColumn "Permalink to this definition")
Toggle sorting by the given column.


This method should only be used when sorting by multiple columns is allowed, see [`AllowMultiColumnSort`](#wx.dataview.DataViewCtrl.AllowMultiColumnSort "wx.dataview.DataViewCtrl.AllowMultiColumnSort") , and does nothing otherwise.



Parameters
**column** (*int*) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def Unselect(self, item: 'dataview.DataViewItem') -> None:
        """ 

`Unselect`(*self*, *item*)[¶](#wx.dataview.DataViewCtrl.Unselect "Permalink to this definition")
Unselect the given item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    def UnselectAll(self) -> None:
        """ 

`UnselectAll`(*self*)[¶](#wx.dataview.DataViewCtrl.UnselectAll "Permalink to this definition")
Unselect all item.


This method only has effect if multiple selections are allowed.




            Source: https://docs.wxpython.org/wx.dataview.DataViewCtrl.html
        """

    ColumnCount: int  # `ColumnCount`[¶](#wx.dataview.DataViewCtrl.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.dataview.DataViewCtrl.GetColumnCount "wx.dataview.DataViewCtrl.GetColumnCount")
    Columns: None  # `Columns`[¶](#wx.dataview.DataViewCtrl.Columns "Permalink to this definition")See [`GetColumns`](#wx.dataview.DataViewCtrl.GetColumns "wx.dataview.DataViewCtrl.GetColumns")
    CountPerPage: int  # `CountPerPage`[¶](#wx.dataview.DataViewCtrl.CountPerPage "Permalink to this definition")See [`GetCountPerPage`](#wx.dataview.DataViewCtrl.GetCountPerPage "wx.dataview.DataViewCtrl.GetCountPerPage")
    CurrentColumn: 'DataViewColumn'  # `CurrentColumn`[¶](#wx.dataview.DataViewCtrl.CurrentColumn "Permalink to this definition")See [`GetCurrentColumn`](#wx.dataview.DataViewCtrl.GetCurrentColumn "wx.dataview.DataViewCtrl.GetCurrentColumn")
    CurrentItem: 'DataViewItem'  # `CurrentItem`[¶](#wx.dataview.DataViewCtrl.CurrentItem "Permalink to this definition")See [`GetCurrentItem`](#wx.dataview.DataViewCtrl.GetCurrentItem "wx.dataview.DataViewCtrl.GetCurrentItem") and [`SetCurrentItem`](#wx.dataview.DataViewCtrl.SetCurrentItem "wx.dataview.DataViewCtrl.SetCurrentItem")
    ExpanderColumn: 'DataViewColumn'  # `ExpanderColumn`[¶](#wx.dataview.DataViewCtrl.ExpanderColumn "Permalink to this definition")See [`GetExpanderColumn`](#wx.dataview.DataViewCtrl.GetExpanderColumn "wx.dataview.DataViewCtrl.GetExpanderColumn") and [`SetExpanderColumn`](#wx.dataview.DataViewCtrl.SetExpanderColumn "wx.dataview.DataViewCtrl.SetExpanderColumn")
    Indent: int  # `Indent`[¶](#wx.dataview.DataViewCtrl.Indent "Permalink to this definition")See [`GetIndent`](#wx.dataview.DataViewCtrl.GetIndent "wx.dataview.DataViewCtrl.GetIndent") and [`SetIndent`](#wx.dataview.DataViewCtrl.SetIndent "wx.dataview.DataViewCtrl.SetIndent")
    MainWindow: 'Window'  # `MainWindow`[¶](#wx.dataview.DataViewCtrl.MainWindow "Permalink to this definition")See [`GetMainWindow`](#wx.dataview.DataViewCtrl.GetMainWindow "wx.dataview.DataViewCtrl.GetMainWindow")
    Model: 'DataViewModel'  # `Model`[¶](#wx.dataview.DataViewCtrl.Model "Permalink to this definition")See [`GetModel`](#wx.dataview.DataViewCtrl.GetModel "wx.dataview.DataViewCtrl.GetModel")
    SelectedItemsCount: int  # `SelectedItemsCount`[¶](#wx.dataview.DataViewCtrl.SelectedItemsCount "Permalink to this definition")See [`GetSelectedItemsCount`](#wx.dataview.DataViewCtrl.GetSelectedItemsCount "wx.dataview.DataViewCtrl.GetSelectedItemsCount")
    Selection: 'DataViewItem'  # `Selection`[¶](#wx.dataview.DataViewCtrl.Selection "Permalink to this definition")See [`GetSelection`](#wx.dataview.DataViewCtrl.GetSelection "wx.dataview.DataViewCtrl.GetSelection")
    Selections: 'DataViewItemArray'  # `Selections`[¶](#wx.dataview.DataViewCtrl.Selections "Permalink to this definition")See [`GetSelections`](#wx.dataview.DataViewCtrl.GetSelections "wx.dataview.DataViewCtrl.GetSelections") and [`SetSelections`](#wx.dataview.DataViewCtrl.SetSelections "wx.dataview.DataViewCtrl.SetSelections")
    SortingColumn: 'DataViewColumn'  # `SortingColumn`[¶](#wx.dataview.DataViewCtrl.SortingColumn "Permalink to this definition")See [`GetSortingColumn`](#wx.dataview.DataViewCtrl.GetSortingColumn "wx.dataview.DataViewCtrl.GetSortingColumn")
    TopItem: 'DataViewItem'  # `TopItem`[¶](#wx.dataview.DataViewCtrl.TopItem "Permalink to this definition")See [`GetTopItem`](#wx.dataview.DataViewCtrl.GetTopItem "wx.dataview.DataViewCtrl.GetTopItem")



DV_SINGLE: int  # Single selection mode. This is the default.

DV_MULTIPLE: int  # Multiple selection mode.

DV_ROW_LINES: int  # Use alternating colours for odd and even rows.

DV_HORIZ_RULES: int  # Display the separator lines between rows.

DV_VERT_RULES: int  # Display the separator lines between columns.

DV_VARIABLE_LINE_HEIGHT: int  # Allow variable line heights. This can be inefficient when displaying large number of items.

DV_NO_HEADER: int  # Do not show column headers (which are shown by default). ^^

EVT_DATAVIEW_SELECTION_CHANGED: int  # Process a  wxEVT_DATAVIEW_SELECTION_CHANGED   event.

EVT_DATAVIEW_ITEM_ACTIVATED: int  # Process a  wxEVT_DATAVIEW_ITEM_ACTIVATED   event. This event is triggered by double clicking an item or pressing some special key (usually “Enter”) when it is focused.

EVT_DATAVIEW_ITEM_START_EDITING: int  # Process a  wxEVT_DATAVIEW_ITEM_START_EDITING   event. This event can be vetoed in order to prevent editing on an item by item basis.

EVT_DATAVIEW_ITEM_EDITING_STARTED: int  # Process a  wxEVT_DATAVIEW_ITEM_EDITING_STARTED   event.

EVT_DATAVIEW_ITEM_EDITING_DONE: int  # Process a  wxEVT_DATAVIEW_ITEM_EDITING_DONE   event.

EVT_DATAVIEW_ITEM_COLLAPSING: int  # Process a  wxEVT_DATAVIEW_ITEM_COLLAPSING   event.

EVT_DATAVIEW_ITEM_COLLAPSED: int  # Process a  wxEVT_DATAVIEW_ITEM_COLLAPSED   event.

EVT_DATAVIEW_ITEM_EXPANDING: int  # Process a  wxEVT_DATAVIEW_ITEM_EXPANDING   event.

EVT_DATAVIEW_ITEM_EXPANDED: int  # Process a  wxEVT_DATAVIEW_ITEM_EXPANDED   event.

EVT_DATAVIEW_ITEM_VALUE_CHANGED: int  # Process a  wxEVT_DATAVIEW_ITEM_VALUE_CHANGED   event.

EVT_DATAVIEW_ITEM_CONTEXT_MENU: int  # Process a  wxEVT_DATAVIEW_ITEM_CONTEXT_MENU   event generated when the user right clicks inside the control. Notice that this menu is generated even if the click didn’t occur on any valid item, in this case  wx.dataview.DataViewEvent.GetItem   simply returns an invalid item.

EVT_DATAVIEW_COLUMN_HEADER_CLICK: int  # Process a  wxEVT_DATAVIEW_COLUMN_HEADER_CLICK   event.

EVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK: int  # Process a  wxEVT_DATAVIEW_COLUMN_HEADER_RIGHT_CLICK   event.

EVT_DATAVIEW_COLUMN_SORTED: int  # Process a  wxEVT_DATAVIEW_COLUMN_SORTED   event.

EVT_DATAVIEW_COLUMN_REORDERED: int  # Process a  wxEVT_DATAVIEW_COLUMN_REORDERED   event.

EVT_DATAVIEW_ITEM_BEGIN_DRAG: int  # Process a  wxEVT_DATAVIEW_ITEM_BEGIN_DRAG   event which is generated when the user starts dragging a valid item. This event must be processed and  wx.dataview.DataViewEvent.SetDataObject   must be called to actually start dragging the item.

EVT_DATAVIEW_ITEM_DROP_POSSIBLE: int  # Process a  wxEVT_DATAVIEW_ITEM_DROP_POSSIBLE   event.

EVT_DATAVIEW_ITEM_DROP: int  # Process a  wxEVT_DATAVIEW_ITEM_DROP   event. ^^

DF_INVALID: int

class TreeListCtrl(Window):
    """ **Possible constructors**:



```
TreeListCtrl()

TreeListCtrl(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
             style=TL_DEFAULT_STYLE, name=TreeListCtrlNameStr)

```


A control combining TreeCtrl and ListCtrl features.


  


        Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.TreeListCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor, call [`Create`](#wx.dataview.TreeListCtrl.Create "wx.dataview.TreeListCtrl.Create") later.


This constructor is used during two-part construction process when it is impossible or undesirable to create the window when constructing the object.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=TL\_DEFAULT\_STYLE, name=TreeListCtrlNameStr)*


Full constructing, creating the object and its window.


See [`Create`](#wx.dataview.TreeListCtrl.Create "wx.dataview.TreeListCtrl.Create") for the parameters description.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AppendColumn(self, title, width=COL_WIDTH_AUTOSIZE, align=ALIGN_LEFT, flags=COL_RESIZABLE) -> int:
        """ 

`AppendColumn`(*self*, *title*, *width=COL\_WIDTH\_AUTOSIZE*, *align=ALIGN\_LEFT*, *flags=COL\_RESIZABLE*)[¶](#wx.dataview.TreeListCtrl.AppendColumn "Permalink to this definition")
Add a column with the given title and attributes.



Parameters
* **title** (*string*) – The column label.
* **width** (*int*) – The width of the column in pixels or the special `wx.COL_WIDTH_AUTOSIZE` value indicating that the column should adjust to its contents. Notice that the last column is special and will be always resized to fill all the space not taken by the other columns, i.e. the width specified here is ignored for it.
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) – Alignment of both the column header and its items.
* **flags** (*int*) – Column flags, currently can include `wx.COL_RESIZABLE` to allow the user to resize the column and `wx.COL_SORTABLE` to allow the user to resort the control contents by clicking on this column.



Return type
*int*



Returns
Index of the new column or -1 on failure.






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AppendItem(self, parent, text, imageClosed=-1, imageOpened=-1, data=None) -> 'TreeListItem':
        """ 

`AppendItem`(*self*, *parent*, *text*, *imageClosed=-1*, *imageOpened=-1*, *data=None*)[¶](#wx.dataview.TreeListCtrl.AppendItem "Permalink to this definition")
Same as [`InsertItem`](#wx.dataview.TreeListCtrl.InsertItem "wx.dataview.TreeListCtrl.InsertItem") with `wx.dataview.TLI_LAST`.



Parameters
* **parent** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **text** (*string*) –
* **imageClosed** (*int*) –
* **imageOpened** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AreAllChildrenInState(self, item, state) -> bool:
        """ 

`AreAllChildrenInState`(*self*, *item*, *state*)[¶](#wx.dataview.TreeListCtrl.AreAllChildrenInState "Permalink to this definition")
Return `True` if all children of the given item are in the specified state.


This is especially useful for the controls with `TL_3STATE` style to allow to decide whether the parent effective state should be the same *state*, if all its children are in it, or `CHK_UNDETERMINED`.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **state** ([*CheckBoxState*](wx.CheckBoxState.enumeration.html "CheckBoxState")) –



Return type
*bool*





See also


[`UpdateItemParentStateRecursively`](#wx.dataview.TreeListCtrl.UpdateItemParentStateRecursively "wx.dataview.TreeListCtrl.UpdateItemParentStateRecursively")





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def AssignImageList(self, imageList: 'ImageList') -> None:
        """ 

`AssignImageList`(*self*, *imageList*)[¶](#wx.dataview.TreeListCtrl.AssignImageList "Permalink to this definition")
Sets the image list and gives its ownership to the control.


The image list assigned with this method will be automatically deleted by  [wx.TreeCtrl](wx.TreeCtrl.html#wx-treectrl) as appropriate (i.e. it takes ownership of the list).



Parameters
**imageList** ([*wx.ImageList*](wx.ImageList.html#wx.ImageList "wx.ImageList")) – 





See also


[`SetImageList`](#wx.dataview.TreeListCtrl.SetImageList "wx.dataview.TreeListCtrl.SetImageList") .





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def CheckItem(self, item, state=CHK_CHECKED) -> None:
        """ 

`CheckItem`(*self*, *item*, *state=CHK\_CHECKED*)[¶](#wx.dataview.TreeListCtrl.CheckItem "Permalink to this definition")
Change the item checked state.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – Valid non-root tree item.
* **state** ([*CheckBoxState*](wx.CheckBoxState.enumeration.html "CheckBoxState")) – One of `wx.CHK_CHECKED`, `wx.CHK_UNCHECKED` or, for the controls with `wx.dataview.TL_3STATE` or `wx.dataview.TL_USER_3STATE` styles, `wx.CHK_UNDETERMINED`.






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def CheckItemRecursively(self, item, state=CHK_CHECKED) -> None:
        """ 

`CheckItemRecursively`(*self*, *item*, *state=CHK\_CHECKED*)[¶](#wx.dataview.TreeListCtrl.CheckItemRecursively "Permalink to this definition")
Change the checked state of the given item and all its children.


This is the same as [`CheckItem`](#wx.dataview.TreeListCtrl.CheckItem "wx.dataview.TreeListCtrl.CheckItem") but checks or unchecks not only this item itself but all its children recursively as well.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **state** ([*CheckBoxState*](wx.CheckBoxState.enumeration.html "CheckBoxState")) –






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def ClearColumns(self) -> None:
        """ 

`ClearColumns`(*self*)[¶](#wx.dataview.TreeListCtrl.ClearColumns "Permalink to this definition")
Delete all columns.



See also


[`DeleteAllItems`](#wx.dataview.TreeListCtrl.DeleteAllItems "wx.dataview.TreeListCtrl.DeleteAllItems")





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Collapse(self, item: 'dataview.TreeListItem') -> None:
        """ 

`Collapse`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.Collapse "Permalink to this definition")
Collapse the given tree branch.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TL_DEFAULT_STYLE, name=TreeListCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=TL\_DEFAULT\_STYLE*, *name=TreeListCtrlNameStr*)[¶](#wx.dataview.TreeListCtrl.Create "Permalink to this definition")
Create the control window.


Can be only called for the objects created using the default constructor and exactly once.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The parent window, must be not `None`.
* **id** (*wx.WindowID*) – The window identifier, may be `ID_ANY`.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The initial window position, usually unused.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The initial window size, usually unused.
* **style** (*long*) – The window style, see their description in the class documentation.
* **name** (*string*) – The name of the window.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.dataview.TreeListCtrl.DeleteAllItems "Permalink to this definition")
Delete all tree items.




            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteColumn(self, col: int) -> bool:
        """ 

`DeleteColumn`(*self*, *col*)[¶](#wx.dataview.TreeListCtrl.DeleteColumn "Permalink to this definition")
Delete the column with the given index.



Parameters
**col** – Column index in 0 to [`GetColumnCount`](#wx.dataview.TreeListCtrl.GetColumnCount "wx.dataview.TreeListCtrl.GetColumnCount") (exclusive) range.



Return type
*bool*



Returns
True if the column was deleted, `False` if index is invalid or deleting the column failed for some other reason.






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def DeleteItem(self, item: 'dataview.TreeListItem') -> None:
        """ 

`DeleteItem`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.DeleteItem "Permalink to this definition")
Delete the specified item.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def EnsureVisible(self, item: 'dataview.TreeListItem') -> None:
        """ 

`EnsureVisible`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.EnsureVisible "Permalink to this definition")
Call this to ensure that the given item is visible.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Expand(self, item: 'dataview.TreeListItem') -> None:
        """ 

`Expand`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.Expand "Permalink to this definition")
Expand the given tree branch.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetCheckedState(self, item: 'dataview.TreeListItem') -> 'CheckBoxState':
        """ 

`GetCheckedState`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetCheckedState "Permalink to this definition")
Return the checked state of the item.


The return value can be `wx.CHK_CHECKED`, `wx.CHK_UNCHECKED` or `wx.CHK_UNDETERMINED`.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
 [wx.CheckBoxState](wx.CheckBoxState.enumeration.html#wx-checkboxstate)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.dataview.TreeListCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetColumnCount(self) -> None:
        """ 

`GetColumnCount`(*self*)[¶](#wx.dataview.TreeListCtrl.GetColumnCount "Permalink to this definition")
Return the total number of columns.




            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetColumnWidth(self, col: Any) -> int:
        """ 

`GetColumnWidth`(*self*, *col*)[¶](#wx.dataview.TreeListCtrl.GetColumnWidth "Permalink to this definition")
Get the current width of the given column in pixels.



Parameters
**col** – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetDataView(self) -> 'DataViewCtrl':
        """ 

`GetDataView`(*self*)[¶](#wx.dataview.TreeListCtrl.GetDataView "Permalink to this definition")
Return the view part of this control as  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl).


This method may return `None` in the future, non DataViewCtrl-based, versions of this class, use [`GetView`](#wx.dataview.TreeListCtrl.GetView "wx.dataview.TreeListCtrl.GetView") unless you really need to use  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) methods on the returned object.



Return type
 [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetFirstChild(self, item: 'dataview.TreeListItem') -> 'TreeListItem':
        """ 

`GetFirstChild`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetFirstChild "Permalink to this definition")
Return the first child of the given item.


Item may be the root item.


Return value may be invalid if the item doesn’t have any children.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetFirstItem(self) -> 'TreeListItem':
        """ 

`GetFirstItem`(*self*)[¶](#wx.dataview.TreeListCtrl.GetFirstItem "Permalink to this definition")
Return the first item in the tree.


This is the first child of the root item.



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)





See also


[`GetNextItem`](#wx.dataview.TreeListCtrl.GetNextItem "wx.dataview.TreeListCtrl.GetNextItem")





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemData(self, item: 'dataview.TreeListItem') -> 'ClientData':
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetItemData "Permalink to this definition")
Get the data associated with the given item.


The returned pointer may be `None`.


It must not be deleted by the caller as this will be done by the control itself.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
*ClientData*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemParent(self, item: 'dataview.TreeListItem') -> 'TreeListItem':
        """ 

`GetItemParent`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetItemParent "Permalink to this definition")
Return the parent of the given item.


All the tree items visible in the tree have valid parent items, only the never shown root item has no parent.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetItemText(self, item, col=0) -> str:
        """ 

`GetItemText`(*self*, *item*, *col=0*)[¶](#wx.dataview.TreeListCtrl.GetItemText "Permalink to this definition")
Return the text of the given item.


By default, returns the text of the first column but any other one can be specified using *col* argument.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **col** –



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetNextItem(self, item: 'dataview.TreeListItem') -> 'TreeListItem':
        """ 

`GetNextItem`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetNextItem "Permalink to this definition")
Get item after the given one in the depth-first tree-traversal order.


Calling this function starting with the result of [`GetFirstItem`](#wx.dataview.TreeListCtrl.GetFirstItem "wx.dataview.TreeListCtrl.GetFirstItem") allows iterating over all items in the tree.


The iteration stops when this function returns an invalid item, i.e.



```
item = tree.GetFirstItem()

while item.IsOk():
    item = tree.GetNextItem(item)

    # Do something with every tree item ...

```



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetNextSibling(self, item: 'dataview.TreeListItem') -> 'TreeListItem':
        """ 

`GetNextSibling`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.GetNextSibling "Permalink to this definition")
Return the next sibling of the given item.


Return value may be invalid if there are no more siblings.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetRootItem(self) -> 'TreeListItem':
        """ 

`GetRootItem`(*self*)[¶](#wx.dataview.TreeListCtrl.GetRootItem "Permalink to this definition")
Return the (never shown) root item.



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSelection(self) -> 'TreeListItem':
        """ 

`GetSelection`(*self*)[¶](#wx.dataview.TreeListCtrl.GetSelection "Permalink to this definition")
Return the currently selected item.


This method can’t be used with multi-selection controls, use [`GetSelections`](#wx.dataview.TreeListCtrl.GetSelections "wx.dataview.TreeListCtrl.GetSelections") instead.


The return value may be invalid if no item has been selected yet. Once an item in a single selection control was selected, it will keep a valid selection.



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSelections(self) -> Any:
        """ 

`GetSelections`(*self*)[¶](#wx.dataview.TreeListCtrl.GetSelections "Permalink to this definition")

> Returns a list of all selected items. This method can be used in
> both single and multi-selection case.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetSortColumn(self) -> tuple:
        """ 

`GetSortColumn`(*self*)[¶](#wx.dataview.TreeListCtrl.GetSortColumn "Permalink to this definition")
Return the column currently used for sorting, if any.


If the control is currently unsorted, the function simply returns `False` and doesn’t modify any of its output parameters.



Return type
*tuple*



Returns
( *bool*, *col*, *ascendingOrder* )






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def GetView(self) -> 'Window':
        """ 

`GetView`(*self*)[¶](#wx.dataview.TreeListCtrl.GetView "Permalink to this definition")
Return the view part of this control as a  [wx.Window](wx.Window.html#wx-window).


This method always returns not `None` pointer once the window was created.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def InsertItem(self, parent, previous, text, imageClosed=-1, imageOpened=-1, data=None) -> 'TreeListItem':
        """ 

`InsertItem`(*self*, *parent*, *previous*, *text*, *imageClosed=-1*, *imageOpened=-1*, *data=None*)[¶](#wx.dataview.TreeListCtrl.InsertItem "Permalink to this definition")
Insert a new item into the tree.



Parameters
* **parent** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – The item parent. Must be valid, may be [`GetRootItem`](#wx.dataview.TreeListCtrl.GetRootItem "wx.dataview.TreeListCtrl.GetRootItem") .
* **previous** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – The previous item that this one should be inserted immediately after. It must be valid but may be one of the special values `wx.dataview.TLI_FIRST` or `wx.dataview.TLI_LAST` indicating that the item should be either inserted before the first child of its parent (if any) or after the last one.
* **text** (*string*) – The item text.
* **imageClosed** (*int*) – The normal item image, may be `wx.NO_IMAGE` to not show any image.
* **imageOpened** (*int*) – The item image shown when it’s in the expanded state.
* **data** (*ClientData*) – Optional client data pointer that can be later retrieved using [`GetItemData`](#wx.dataview.TreeListCtrl.GetItemData "wx.dataview.TreeListCtrl.GetItemData") and will be deleted by the tree when the item itself is deleted.



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def IsExpanded(self, item: 'dataview.TreeListItem') -> bool:
        """ 

`IsExpanded`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.IsExpanded "Permalink to this definition")
Return whether the given item is expanded.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def IsSelected(self, item: 'dataview.TreeListItem') -> bool:
        """ 

`IsSelected`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.IsSelected "Permalink to this definition")
Return `True` if the item is selected.


This method can be used in both single and multiple selection modes.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def PrependItem(self, parent, text, imageClosed=-1, imageOpened=-1, data=None) -> 'TreeListItem':
        """ 

`PrependItem`(*self*, *parent*, *text*, *imageClosed=-1*, *imageOpened=-1*, *data=None*)[¶](#wx.dataview.TreeListCtrl.PrependItem "Permalink to this definition")
Same as [`InsertItem`](#wx.dataview.TreeListCtrl.InsertItem "wx.dataview.TreeListCtrl.InsertItem") with `wx.dataview.TLI_FIRST`.



Parameters
* **parent** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **text** (*string*) –
* **imageClosed** (*int*) –
* **imageOpened** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Select(self, item: 'dataview.TreeListItem') -> None:
        """ 

`Select`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.Select "Permalink to this definition")
Select the given item.


In single selection mode, deselects any other selected items, in multi-selection case it adds to the selection.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.dataview.TreeListCtrl.SelectAll "Permalink to this definition")
Select all the control items.


Can be only used in multi-selection mode.




            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetColumnWidth(self, col, width) -> None:
        """ 

`SetColumnWidth`(*self*, *col*, *width*)[¶](#wx.dataview.TreeListCtrl.SetColumnWidth "Permalink to this definition")
Change the width of the given column.


Set column width to either the given value in pixels or to the value large enough to fit all of the items if width is `wx.COL_WIDTH_AUTOSIZE`.


Notice that setting the width of the last column is ignored as this column is always resized to fill the space left by the other columns.



Parameters
* **col** –
* **width** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imageList*)[¶](#wx.dataview.TreeListCtrl.SetImageList "Permalink to this definition")
Sets the image list.


The image list assigned with this method will **not** be deleted by the control itself and you will need to delete it yourself, use [`AssignImageList`](#wx.dataview.TreeListCtrl.AssignImageList "wx.dataview.TreeListCtrl.AssignImageList") to give the image list ownership to the control.



Parameters
**imageList** ([*wx.ImageList*](wx.ImageList.html#wx.ImageList "wx.ImageList")) – Image list to use, may be `None` to not show any images any more.






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemComparator(self, comparator: 'dataview.TreeListItemComparator') -> None:
        """ 

`SetItemComparator`(*self*, *comparator*)[¶](#wx.dataview.TreeListCtrl.SetItemComparator "Permalink to this definition")
Set the object to use for comparing the items.


This object will be used when the control is being sorted because the user clicked on a sortable column or [`SetSortColumn`](#wx.dataview.TreeListCtrl.SetSortColumn "wx.dataview.TreeListCtrl.SetSortColumn") was called.


The provided pointer is stored by the control so the object it points to must have a life-time equal or greater to that of the control itself. In addition, the pointer can be `None` to stop using custom comparator and revert to the default alphabetical comparison.



Parameters
**comparator** ([*wx.dataview.TreeListItemComparator*](wx.dataview.TreeListItemComparator.html#wx.dataview.TreeListItemComparator "wx.dataview.TreeListItemComparator")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.dataview.TreeListCtrl.SetItemData "Permalink to this definition")
Set the data associated with the given item.


Previous client data, if any, is deleted when this function is called so it may be used to delete the current item data object and reset it by passing `None` as *data* argument.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **data** (*ClientData*) –






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemImage(self, item, closed, opened=-1) -> None:
        """ 

`SetItemImage`(*self*, *item*, *closed*, *opened=-1*)[¶](#wx.dataview.TreeListCtrl.SetItemImage "Permalink to this definition")
Set the images for the given item.


See [`InsertItem`](#wx.dataview.TreeListCtrl.InsertItem "wx.dataview.TreeListCtrl.InsertItem") for the images parameters descriptions.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **closed** (*int*) –
* **opened** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetItemText(self, *args, **kw) -> None:
        """ 

`SetItemText`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.TreeListCtrl.SetItemText "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetItemText** *(self, item, col, text)*


Set the text of the specified column of the given item.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **col** –
* **text** (*string*) –






---

  



**SetItemText** *(self, item, text)*


Set the text of the first column of the given item.



Parameters
* **item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) –
* **text** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def SetSortColumn(self, col, ascendingOrder=True) -> None:
        """ 

`SetSortColumn`(*self*, *col*, *ascendingOrder=True*)[¶](#wx.dataview.TreeListCtrl.SetSortColumn "Permalink to this definition")
Set the column to use for sorting and the order in which to sort.


Calling this method resorts the control contents using the values of the items in the specified column. Sorting uses custom comparator set with [`SetItemComparator`](#wx.dataview.TreeListCtrl.SetItemComparator "wx.dataview.TreeListCtrl.SetItemComparator") or alphabetical comparison of items texts if none was specified.


Notice that currently there is no way to reset sort order.



Parameters
* **col** – A valid column index.
* **ascendingOrder** (*bool*) – Indicates whether the items should be sorted in ascending (A to Z) or descending (Z to A) order.






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UncheckItem(self, item: 'dataview.TreeListItem') -> None:
        """ 

`UncheckItem`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.UncheckItem "Permalink to this definition")
Uncheck the given item.


This is synonymous with CheckItem(wxCHK\_UNCHECKED).



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def Unselect(self, item: 'dataview.TreeListItem') -> None:
        """ 

`Unselect`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.Unselect "Permalink to this definition")
Deselect the given item.


This method can be used in multiple selection mode only.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UnselectAll(self) -> None:
        """ 

`UnselectAll`(*self*)[¶](#wx.dataview.TreeListCtrl.UnselectAll "Permalink to this definition")
Deselect all the control items.


Can be only used in multi-selection mode.




            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def UpdateItemParentStateRecursively(self, item: 'dataview.TreeListItem') -> None:
        """ 

`UpdateItemParentStateRecursively`(*self*, *item*)[¶](#wx.dataview.TreeListCtrl.UpdateItemParentStateRecursively "Permalink to this definition")
Update the state of the parent item to reflect the checked state of its children.


This method updates the parent of this item recursively: if this item and all its siblings are checked, the parent will become checked as well. If this item and all its siblings are unchecked, the parent will be unchecked. And if the siblings of this item are not all in the same state, the parent will be switched to indeterminate state. And then the same logic will be applied to the parents parent and so on recursively.


This is typically called when the state of the given item has changed from EVT\_TREELIST\_ITEM\_CHECKED() handler in the controls which have `wx.dataview.TL_3STATE` flag. Notice that without this flag this function can’t work as it would be unable to set the state of a parent with both checked and unchecked items so it’s only allowed to call it when this flag is set.



Parameters
**item** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    def WidthFor(self, text: str) -> int:
        """ 

`WidthFor`(*self*, *text*)[¶](#wx.dataview.TreeListCtrl.WidthFor "Permalink to this definition")
Get the width appropriate for showing the given text.


This is typically used as second argument for [`AppendColumn`](#wx.dataview.TreeListCtrl.AppendColumn "wx.dataview.TreeListCtrl.AppendColumn") or with [`SetColumnWidth`](#wx.dataview.TreeListCtrl.SetColumnWidth "wx.dataview.TreeListCtrl.SetColumnWidth") .



Parameters
**text** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.TreeListCtrl.html
        """

    ColumnCount: None  # `ColumnCount`[¶](#wx.dataview.TreeListCtrl.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.dataview.TreeListCtrl.GetColumnCount "wx.dataview.TreeListCtrl.GetColumnCount")
    DataView: 'DataViewCtrl'  # `DataView`[¶](#wx.dataview.TreeListCtrl.DataView "Permalink to this definition")See [`GetDataView`](#wx.dataview.TreeListCtrl.GetDataView "wx.dataview.TreeListCtrl.GetDataView")
    FirstItem: 'TreeListItem'  # `FirstItem`[¶](#wx.dataview.TreeListCtrl.FirstItem "Permalink to this definition")See [`GetFirstItem`](#wx.dataview.TreeListCtrl.GetFirstItem "wx.dataview.TreeListCtrl.GetFirstItem")
    NO_IMAGE: Any  # `NO_IMAGE`[¶](#wx.dataview.TreeListCtrl.NO_IMAGE "Permalink to this definition")A public C++ attribute of type `int`. A constant indicating that no image should be used for an item.
    RootItem: 'TreeListItem'  # `RootItem`[¶](#wx.dataview.TreeListCtrl.RootItem "Permalink to this definition")See [`GetRootItem`](#wx.dataview.TreeListCtrl.GetRootItem "wx.dataview.TreeListCtrl.GetRootItem")
    Selection: 'TreeListItem'  # `Selection`[¶](#wx.dataview.TreeListCtrl.Selection "Permalink to this definition")See [`GetSelection`](#wx.dataview.TreeListCtrl.GetSelection "wx.dataview.TreeListCtrl.GetSelection")
    Selections: Any  # `Selections`[¶](#wx.dataview.TreeListCtrl.Selections "Permalink to this definition")See [`GetSelections`](#wx.dataview.TreeListCtrl.GetSelections "wx.dataview.TreeListCtrl.GetSelections")
    SortColumn: tuple  # `SortColumn`[¶](#wx.dataview.TreeListCtrl.SortColumn "Permalink to this definition")See [`GetSortColumn`](#wx.dataview.TreeListCtrl.GetSortColumn "wx.dataview.TreeListCtrl.GetSortColumn") and [`SetSortColumn`](#wx.dataview.TreeListCtrl.SetSortColumn "wx.dataview.TreeListCtrl.SetSortColumn")
    View: 'Window'  # `View`[¶](#wx.dataview.TreeListCtrl.View "Permalink to this definition")See [`GetView`](#wx.dataview.TreeListCtrl.GetView "wx.dataview.TreeListCtrl.GetView")



TL_SINGLE: int  # Single selection, this is the default.

TL_MULTIPLE: int  # Allow multiple selection, see GetSelections.

TL_CHECKBOX: int  # Show the usual, 2 state, checkboxes for the items in the first column.

TL_3STATE: int  # Show the checkboxes that can possibly be set by the program, but not the user, to a third, undetermined, state, for the items in the first column. Implies wx.dataview.TL_CHECKBOX.

TL_USER_3STATE: int  # Same as wx.dataview.TL_3STATE but the user can also set the checkboxes to the undetermined state. Implies wx.dataview.TL_3STATE.

TL_NO_HEADER: int  # Don’t show the column headers, that are shown by default. Notice that this style is only available since wxWidgets 2.9.5.

TL_DEFAULT_STYLE: int  # Style used by the control by default, just wx.dataview.TL_SINGLE currently. ^^

EVT_TREELIST_SELECTION_CHANGED: int  # Process  wxEVT_TREELIST_SELECTION_CHANGED   event and notifies about the selection change in the control. In the single selection case the item indicated by the event has been selected and previously selected item, if any, was deselected. In multiple selection case, the selection of this item has just changed (it may have been either selected or deselected) but notice that the selection of other items could have changed as well, use  wx.dataview.TreeListCtrl.GetSelections   to retrieve the new selection if necessary.

EVT_TREELIST_ITEM_EXPANDING: int  # Process  wxEVT_TREELIST_ITEM_EXPANDING   event notifying about the given branch being expanded. This event is sent before the expansion occurs and can be vetoed to prevent it from happening.

EVT_TREELIST_ITEM_EXPANDED: int  # Process  wxEVT_TREELIST_ITEM_EXPANDED   event notifying about the expansion of the given branch. This event is sent after the expansion occurs and can’t be vetoed.

EVT_TREELIST_ITEM_CHECKED: int  # Process  wxEVT_TREELIST_ITEM_CHECKED   event notifying about the user checking or unchecking the item. You can use  wx.dataview.TreeListCtrl.GetCheckedState   to retrieve the new item state and wx.dataview.TreeListEvent.GetOldCheckedState   to get the previous one.

EVT_TREELIST_ITEM_ACTIVATED: int  # Process  wxEVT_TREELIST_ITEM_ACTIVATED   event notifying about the user double clicking the item or activating it from keyboard.

EVT_TREELIST_ITEM_CONTEXT_MENU: int  # Process  wxEVT_TREELIST_ITEM_CONTEXT_MENU   event indicating that the popup menu for the given item should be displayed.

EVT_TREELIST_COLUMN_SORTED: int  # Process  wxEVT_TREELIST_COLUMN_SORTED   event indicating that the control contents has just been resorted using the specified column. The event doesn’t carry the sort direction, use  GetSortColumn  method if you need to know it. ^^

COL_SORTABLE: int

TLI_LAST: int

TLI_FIRST: int

COL_WIDTH_AUTOSIZE: int

COL_RESIZABLE: int

CHK_CHECKED: int

CHK_UNCHECKED: int

CHK_UNDETERMINED: int

NO_IMAGE: int

class DataViewTreeCtrl(DataViewCtrl):
    """ **Possible constructors**:



```
DataViewTreeCtrl()

DataViewTreeCtrl(parent, id=ID_ANY, pos=DefaultPosition,
                 size=DefaultSize, style=DV_NO_HEADER|DV_ROW_LINES,
                 validator=DefaultValidator)

```


This class is a DataViewCtrl which internally uses a
DataViewTreeStore and forwards most of its API to that class.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewTreeCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=DV\_NO\_HEADER|DV\_ROW\_LINES, validator=DefaultValidator)*


Constructor.


Calls [`Create`](#wx.dataview.DataViewTreeCtrl.Create "wx.dataview.DataViewTreeCtrl.Create") .



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def AppendContainer(self, parent, text, icon=-1, expanded=-1, data=None) -> 'DataViewItem':
        """ 

`AppendContainer`(*self*, *parent*, *text*, *icon=-1*, *expanded=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.AppendContainer "Permalink to this definition")
Appends a container to the given *parent*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **expanded** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def AppendItem(self, parent, text, icon=-1, data=None) -> 'DataViewItem':
        """ 

`AppendItem`(*self*, *parent*, *text*, *icon=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.AppendItem "Permalink to this definition")
Appends an item to the given *parent*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=DV_NO_HEADER|DV_ROW_LINES, validator=DefaultValidator) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DV\_NO\_HEADER|DV\_ROW\_LINES*, *validator=DefaultValidator*)[¶](#wx.dataview.DataViewTreeCtrl.Create "Permalink to this definition")
Creates the control and a  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore) as its internal model.


The default tree column created by this method is an editable column using  [wx.dataview.DataViewIconTextRenderer](wx.dataview.DataViewIconTextRenderer.html#wx-dataview-dataviewicontextrenderer) as its renderer.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.dataview.DataViewTreeCtrl.DeleteAllItems "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).




            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteChildren(self, item: 'dataview.DataViewItem') -> None:
        """ 

`DeleteChildren`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.DeleteChildren "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def DeleteItem(self, item: 'dataview.DataViewItem') -> None:
        """ 

`DeleteItem`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.DeleteItem "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetChildCount(self, parent: 'dataview.DataViewItem') -> int:
        """ 

`GetChildCount`(*self*, *parent*)[¶](#wx.dataview.DataViewTreeCtrl.GetChildCount "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.dataview.DataViewTreeCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetImageList(self) -> 'ImageList':
        """ 

`GetImageList`(*self*)[¶](#wx.dataview.DataViewTreeCtrl.GetImageList "Permalink to this definition")
Returns the image list.



Return type
[`ImageList`](#wx.dataview.DataViewTreeCtrl.ImageList "wx.dataview.DataViewTreeCtrl.ImageList")






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemData(self, item: 'dataview.DataViewItem') -> 'ClientData':
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.GetItemData "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*ClientData*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemExpandedIcon(self, item: 'dataview.DataViewItem') -> 'Icon':
        """ 

`GetItemExpandedIcon`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.GetItemExpandedIcon "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*Icon*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemIcon(self, item: 'dataview.DataViewItem') -> 'Icon':
        """ 

`GetItemIcon`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.GetItemIcon "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*Icon*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemParent(self, item: 'dataview.DataViewItem') -> 'DataViewItem':
        """ 

`GetItemParent`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.GetItemParent "Permalink to this definition")
Returns the item’s parent.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)





New in version 4.1/wxWidgets-3.1.6.





            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetItemText(self, item: 'dataview.DataViewItem') -> str:
        """ 

`GetItemText`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.GetItemText "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetNthChild(self, parent, pos) -> 'DataViewItem':
        """ 

`GetNthChild`(*self*, *parent*, *pos*)[¶](#wx.dataview.DataViewTreeCtrl.GetNthChild "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **pos** (*int*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def GetStore(self) -> 'DataViewTreeStore':
        """ 

`GetStore`(*self*)[¶](#wx.dataview.DataViewTreeCtrl.GetStore "Permalink to this definition")
Returns the store.



Return type
 [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def InsertContainer(self, parent, previous, text, icon=-1, expanded=-1, data=None) -> 'DataViewItem':
        """ 

`InsertContainer`(*self*, *parent*, *previous*, *text*, *icon=-1*, *expanded=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.InsertContainer "Permalink to this definition")
Calls the same method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore) but uses an index position in the image list instead of a  [wx.Icon](wx.Icon.html#wx-icon).



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **previous** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **expanded** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def InsertItem(self, parent, previous, text, icon=-1, data=None) -> 'DataViewItem':
        """ 

`InsertItem`(*self*, *parent*, *previous*, *text*, *icon=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.InsertItem "Permalink to this definition")
Calls the same method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore) but uses an index position in the image list instead of a  [wx.Icon](wx.Icon.html#wx-icon).



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **previous** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def IsContainer(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`IsContainer`(*self*, *item*)[¶](#wx.dataview.DataViewTreeCtrl.IsContainer "Permalink to this definition")
Returns `True` if item is a container.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def PrependContainer(self, parent, text, icon=-1, expanded=-1, data=None) -> 'DataViewItem':
        """ 

`PrependContainer`(*self*, *parent*, *text*, *icon=-1*, *expanded=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.PrependContainer "Permalink to this definition")
Calls the same method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore) but uses an index position in the image list instead of a  [wx.Icon](wx.Icon.html#wx-icon).



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **expanded** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def PrependItem(self, parent, text, icon=-1, data=None) -> 'DataViewItem':
        """ 

`PrependItem`(*self*, *parent*, *text*, *icon=-1*, *data=None*)[¶](#wx.dataview.DataViewTreeCtrl.PrependItem "Permalink to this definition")
Calls the same method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore) but uses an index position in the image list instead of a  [wx.Icon](wx.Icon.html#wx-icon).



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** (*int*) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetImageList(self, imagelist: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imagelist*)[¶](#wx.dataview.DataViewTreeCtrl.SetImageList "Permalink to this definition")
Sets the image list.



Parameters
**imagelist** ([*wx.ImageList*](wx.ImageList.html#wx.ImageList "wx.ImageList")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.dataview.DataViewTreeCtrl.SetItemData "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **data** (*ClientData*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemExpandedIcon(self, item, icon) -> None:
        """ 

`SetItemExpandedIcon`(*self*, *item*, *icon*)[¶](#wx.dataview.DataViewTreeCtrl.SetItemExpandedIcon "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemIcon(self, item, icon) -> None:
        """ 

`SetItemIcon`(*self*, *item*, *icon*)[¶](#wx.dataview.DataViewTreeCtrl.SetItemIcon "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    def SetItemText(self, item, text) -> None:
        """ 

`SetItemText`(*self*, *item*, *text*)[¶](#wx.dataview.DataViewTreeCtrl.SetItemText "Permalink to this definition")
Calls the identical method from  [wx.dataview.DataViewTreeStore](wx.dataview.DataViewTreeStore.html#wx-dataview-dataviewtreestore).



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeCtrl.html
        """

    ImageList: '_ImageList'  # `ImageList`[¶](#wx.dataview.DataViewTreeCtrl.ImageList "Permalink to this definition")See [`GetImageList`](#wx.dataview.DataViewTreeCtrl.GetImageList "wx.dataview.DataViewTreeCtrl.GetImageList") and [`SetImageList`](#wx.dataview.DataViewTreeCtrl.SetImageList "wx.dataview.DataViewTreeCtrl.SetImageList")
    Store: 'DataViewTreeStore'  # `Store`[¶](#wx.dataview.DataViewTreeCtrl.Store "Permalink to this definition")See [`GetStore`](#wx.dataview.DataViewTreeCtrl.GetStore "wx.dataview.DataViewTreeCtrl.GetStore")



class DataViewListCtrl(DataViewCtrl):
    """ **Possible constructors**:



```
DataViewListCtrl()

DataViewListCtrl(parent, id=ID_ANY, pos=DefaultPosition,
                 size=DefaultSize, style=DV_ROW_LINES, validator=DefaultValidator)

```


This class is a DataViewCtrl which internally uses a
DataViewListStore and forwards most of its API to that class.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewListCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=DV\_ROW\_LINES, validator=DefaultValidator)*


Constructor.


Calls [`Create`](#wx.dataview.DataViewListCtrl.Create "wx.dataview.DataViewListCtrl.Create") .



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendColumn(self, *args, **kw) -> bool:
        """ 

`AppendColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewListCtrl.AppendColumn "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AppendColumn** *(self, column)*


Appends a column to the control and additionally appends a column to the store with the type string.



Parameters
**column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*bool*






---

  



**AppendColumn** *(self, column, varianttype)*


Appends a column to the control and additionally appends a column to the list store with the type *varianttype*.



Parameters
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –
* **varianttype** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendIconTextColumn(self, label, mode=DATAVIEW_CELL_INERT, width=-1, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> 'DataViewColumn':
        """ 

`AppendIconTextColumn`(*self*, *label*, *mode=DATAVIEW\_CELL\_INERT*, *width=-1*, *align=ALIGN\_LEFT*, *flags=DATAVIEW\_COL\_RESIZABLE*)[¶](#wx.dataview.DataViewListCtrl.AppendIconTextColumn "Permalink to this definition")
Appends an icon-and-text column to the control and the store.


See `DataViewColumn.__init__` for more info about the parameters.



Parameters
* **label** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendItem(self, values, data=None) -> None:
        """ 

`AppendItem`(*self*, *values*, *data=None*)[¶](#wx.dataview.DataViewListCtrl.AppendItem "Permalink to this definition")
Appends an item (i.e. a row) to the control.


Note that the size of *values* vector must be exactly equal to the number of columns in the control and that columns must not be modified after adding any items to the control (or, conversely, items must not be added before the columns are set up).



Parameters
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendProgressColumn(self, label, mode=DATAVIEW_CELL_INERT, width=-1, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> 'DataViewColumn':
        """ 

`AppendProgressColumn`(*self*, *label*, *mode=DATAVIEW\_CELL\_INERT*, *width=-1*, *align=ALIGN\_LEFT*, *flags=DATAVIEW\_COL\_RESIZABLE*)[¶](#wx.dataview.DataViewListCtrl.AppendProgressColumn "Permalink to this definition")
Appends a progress column to the control and the store.


See `DataViewColumn.__init__` for more info about the parameters.



Parameters
* **label** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendTextColumn(self, label, mode=DATAVIEW_CELL_INERT, width=-1, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> 'DataViewColumn':
        """ 

`AppendTextColumn`(*self*, *label*, *mode=DATAVIEW\_CELL\_INERT*, *width=-1*, *align=ALIGN\_LEFT*, *flags=DATAVIEW\_COL\_RESIZABLE*)[¶](#wx.dataview.DataViewListCtrl.AppendTextColumn "Permalink to this definition")
Appends a text column to the control and the store.


See `DataViewColumn.__init__` for more info about the parameters.



Parameters
* **label** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def AppendToggleColumn(self, label, mode=DATAVIEW_CELL_ACTIVATABLE, width=-1, align=ALIGN_LEFT, flags=DATAVIEW_COL_RESIZABLE) -> 'DataViewColumn':
        """ 

`AppendToggleColumn`(*self*, *label*, *mode=DATAVIEW\_CELL\_ACTIVATABLE*, *width=-1*, *align=ALIGN\_LEFT*, *flags=DATAVIEW\_COL\_RESIZABLE*)[¶](#wx.dataview.DataViewListCtrl.AppendToggleColumn "Permalink to this definition")
Appends a toggle column to the control and the store.


See `DataViewColumn.__init__` for more info about the parameters.



Parameters
* **label** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **width** (*int*) –
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) –
* **flags** (*int*) –



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=DV_ROW_LINES, validator=DefaultValidator) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=DV\_ROW\_LINES*, *validator=DefaultValidator*)[¶](#wx.dataview.DataViewListCtrl.Create "Permalink to this definition")
Creates the control and a  [wx.dataview.DataViewListStore](wx.dataview.DataViewListStore.html#wx-dataview-dataviewliststore) as its internal model.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.dataview.DataViewListCtrl.DeleteAllItems "Permalink to this definition")
Delete all items (= all rows).




            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def DeleteItem(self, row: Any) -> None:
        """ 

`DeleteItem`(*self*, *row*)[¶](#wx.dataview.DataViewListCtrl.DeleteItem "Permalink to this definition")
Delete the row at position *row*.



Parameters
**row** – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.dataview.DataViewListCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetItemCount(self) -> int:
        """ 

`GetItemCount`(*self*)[¶](#wx.dataview.DataViewListCtrl.GetItemCount "Permalink to this definition")
Returns the number of items (=rows) in the control.



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetItemData(self, item: 'dataview.DataViewItem') -> int:
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.dataview.DataViewListCtrl.GetItemData "Permalink to this definition")
Returns the client data associated with the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*wx.UIntPtr*





New in version 2.9.4.




See also


[`SetItemData`](#wx.dataview.DataViewListCtrl.SetItemData "wx.dataview.DataViewListCtrl.SetItemData")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetSelectedRow(self) -> int:
        """ 

`GetSelectedRow`(*self*)[¶](#wx.dataview.DataViewListCtrl.GetSelectedRow "Permalink to this definition")
Returns index of the selected row or `wx.NOT_FOUND`.



Return type
*int*





New in version 2.9.2.




See also


[`wx.dataview.DataViewCtrl.GetSelection`](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl.GetSelection "wx.dataview.DataViewCtrl.GetSelection")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetStore(self) -> 'DataViewListStore':
        """ 

`GetStore`(*self*)[¶](#wx.dataview.DataViewListCtrl.GetStore "Permalink to this definition")
Returns the store.



Return type
 [wx.dataview.DataViewListStore](wx.dataview.DataViewListStore.html#wx-dataview-dataviewliststore)






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetTextValue(self, row, col) -> str:
        """ 

`GetTextValue`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.GetTextValue "Permalink to this definition")
Returns the value from the store.


This method assumes that the string is stored in respective column.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetToggleValue(self, row, col) -> bool:
        """ 

`GetToggleValue`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.GetToggleValue "Permalink to this definition")
Returns the value from the store.


This method assumes that the boolean value is stored in respective column.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def GetValue(self, row, col) -> Any:
        """ 

`GetValue`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.GetValue "Permalink to this definition")
Returns the value from the store.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*value*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def InsertColumn(self, *args, **kw) -> bool:
        """ 

`InsertColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewListCtrl.InsertColumn "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**InsertColumn** *(self, pos, column)*


Inserts a column to the control and additionally inserts a column to the store with the type string.



Parameters
* **pos** (*int*) –
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –



Return type
*bool*






---

  



**InsertColumn** *(self, pos, column, varianttype)*


Inserts a column to the control and additionally inserts a column to the list store with the type *varianttype*.



Parameters
* **pos** (*int*) –
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –
* **varianttype** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def InsertItem(self, row, values, data=None) -> None:
        """ 

`InsertItem`(*self*, *row*, *values*, *data=None*)[¶](#wx.dataview.DataViewListCtrl.InsertItem "Permalink to this definition")
Inserts an item (i.e. a row) to the control.


See remarks for [`AppendItem`](#wx.dataview.DataViewListCtrl.AppendItem "wx.dataview.DataViewListCtrl.AppendItem") for preconditions of this method.


Additionally, *row* must be less than or equal to the current number of items in the control (see [`GetItemCount`](#wx.dataview.DataViewListCtrl.GetItemCount "wx.dataview.DataViewListCtrl.GetItemCount") ).



Parameters
* **row** (*int*) –
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def IsRowSelected(self, row: Any) -> bool:
        """ 

`IsRowSelected`(*self*, *row*)[¶](#wx.dataview.DataViewListCtrl.IsRowSelected "Permalink to this definition")
Returns `True` if *row* is selected.



Parameters
**row** – 



Return type
*bool*





New in version 2.9.2.




See also


[`wx.dataview.DataViewCtrl.IsSelected`](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl.IsSelected "wx.dataview.DataViewCtrl.IsSelected")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def ItemToRow(self, item: 'dataview.DataViewItem') -> int:
        """ 

`ItemToRow`(*self*, *item*)[¶](#wx.dataview.DataViewListCtrl.ItemToRow "Permalink to this definition")
Returns the position of given *item* or `wx.NOT_FOUND` if it’s not a valid item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*int*





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def PrependColumn(self, *args, **kw) -> bool:
        """ 

`PrependColumn`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewListCtrl.PrependColumn "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PrependColumn** *(self, column)*


Prepends a column to the control and additionally prepends a column to the store with the type string.



Parameters
**column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 



Return type
*bool*






---

  



**PrependColumn** *(self, column, varianttype)*


Prepends a column to the control and additionally prepends a column to the list store with the type *varianttype*.



Parameters
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –
* **varianttype** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def PrependItem(self, values, data=None) -> None:
        """ 

`PrependItem`(*self*, *values*, *data=None*)[¶](#wx.dataview.DataViewListCtrl.PrependItem "Permalink to this definition")
Prepends an item (i.e. a row) to the control.


See remarks for [`AppendItem`](#wx.dataview.DataViewListCtrl.AppendItem "wx.dataview.DataViewListCtrl.AppendItem") for preconditions of this method.



Parameters
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def RowToItem(self, row: int) -> 'DataViewItem':
        """ 

`RowToItem`(*self*, *row*)[¶](#wx.dataview.DataViewListCtrl.RowToItem "Permalink to this definition")
Returns the  [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem) at the given *row*.



Parameters
**row** (*int*) – 



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SelectRow(self, row: Any) -> None:
        """ 

`SelectRow`(*self*, *row*)[¶](#wx.dataview.DataViewListCtrl.SelectRow "Permalink to this definition")
Selects given row.



Parameters
**row** – 





New in version 2.9.2.




See also


[`wx.dataview.DataViewCtrl.Select`](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl.Select "wx.dataview.DataViewCtrl.Select")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.dataview.DataViewListCtrl.SetItemData "Permalink to this definition")
Associates a client data pointer with the given item.


Notice that the control does *not* take ownership of the pointer for compatibility with  [wx.ListCtrl](wx.ListCtrl.html#wx-listctrl). I.e. it will *not* delete the pointer (if it is a pointer and not a number) itself, it is up to you to do it.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **data** (*wx.UIntPtr*) –





New in version 2.9.4.




See also


[`GetItemData`](#wx.dataview.DataViewListCtrl.GetItemData "wx.dataview.DataViewListCtrl.GetItemData")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetTextValue(self, value, row, col) -> None:
        """ 

`SetTextValue`(*self*, *value*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.SetTextValue "Permalink to this definition")
Sets the value in the store and update the control.


This method assumes that the string is stored in respective column.



Parameters
* **value** (*string*) –
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetToggleValue(self, value, row, col) -> None:
        """ 

`SetToggleValue`(*self*, *value*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.SetToggleValue "Permalink to this definition")
Sets the value in the store and update the control.


This method assumes that the boolean value is stored in respective column.



Parameters
* **value** (*bool*) –
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def SetValue(self, value, row, col) -> None:
        """ 

`SetValue`(*self*, *value*, *row*, *col*)[¶](#wx.dataview.DataViewListCtrl.SetValue "Permalink to this definition")
Sets the value in the store and update the control.



Parameters
* **value** (*DVCVariant*) –
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    def UnselectRow(self, row: Any) -> None:
        """ 

`UnselectRow`(*self*, *row*)[¶](#wx.dataview.DataViewListCtrl.UnselectRow "Permalink to this definition")
Unselects given row.



Parameters
**row** – 





New in version 2.9.2.




See also


[`wx.dataview.DataViewCtrl.Unselect`](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl.Unselect "wx.dataview.DataViewCtrl.Unselect")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListCtrl.html
        """

    ItemCount: int  # `ItemCount`[¶](#wx.dataview.DataViewListCtrl.ItemCount "Permalink to this definition")See [`GetItemCount`](#wx.dataview.DataViewListCtrl.GetItemCount "wx.dataview.DataViewListCtrl.GetItemCount")
    SelectedRow: int  # `SelectedRow`[¶](#wx.dataview.DataViewListCtrl.SelectedRow "Permalink to this definition")See [`GetSelectedRow`](#wx.dataview.DataViewListCtrl.GetSelectedRow "wx.dataview.DataViewListCtrl.GetSelectedRow")
    Store: 'DataViewListStore'  # `Store`[¶](#wx.dataview.DataViewListCtrl.Store "Permalink to this definition")See [`GetStore`](#wx.dataview.DataViewListCtrl.GetStore "wx.dataview.DataViewListCtrl.GetStore")



NOT_FOUND: int

class DataViewModel(RefCounter):
    """ **Possible constructors**:



```
DataViewModel()

```


DataViewModel is the base class for all data model to be displayed
by a DataViewCtrl.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.DataViewModel.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def AddNotifier(self, notifier: 'dataview.DataViewModelNotifier') -> None:
        """ 

`AddNotifier`(*self*, *notifier*)[¶](#wx.dataview.DataViewModel.AddNotifier "Permalink to this definition")
Adds a  [wx.dataview.DataViewModelNotifier](wx.dataview.DataViewModelNotifier.html#wx-dataview-dataviewmodelnotifier) to the model.



Parameters
**notifier** ([*wx.dataview.DataViewModelNotifier*](wx.dataview.DataViewModelNotifier.html#wx.dataview.DataViewModelNotifier "wx.dataview.DataViewModelNotifier")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ChangeValue(self, variant, item, col) -> bool:
        """ 

`ChangeValue`(*self*, *variant*, *item*, *col*)[¶](#wx.dataview.DataViewModel.ChangeValue "Permalink to this definition")
Change the value of the given item and update the control to reflect it.


This function simply calls [`SetValue`](#wx.dataview.DataViewModel.SetValue "wx.dataview.DataViewModel.SetValue") and, if it succeeded, [`ValueChanged`](#wx.dataview.DataViewModel.ValueChanged "wx.dataview.DataViewModel.ValueChanged") .



Parameters
* **variant** (*DVCVariant*) – The new value.
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – The item (row) to update.
* **col** (*int*) – The column to update.



Return type
*bool*



Returns
`True` if both [`SetValue`](#wx.dataview.DataViewModel.SetValue "wx.dataview.DataViewModel.SetValue") and [`ValueChanged`](#wx.dataview.DataViewModel.ValueChanged "wx.dataview.DataViewModel.ValueChanged") returned `True`.





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Cleared(self) -> bool:
        """ 

`Cleared`(*self*)[¶](#wx.dataview.DataViewModel.Cleared "Permalink to this definition")
Called to inform the model that all of its data has been changed.


This method should be called if so many of the model items have changed, that the control should just reread all of them, repopulating itself entirely.


Note that, contrary to the name of the method, it doesn’t necessarily indicate that model has become empty – although this is the right method to call, rather than [`ItemsDeleted`](#wx.dataview.DataViewModel.ItemsDeleted "wx.dataview.DataViewModel.ItemsDeleted") , if it was indeed cleared, which explains the origin of its name.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Compare(self, item1, item2, column, ascending) -> int:
        """ 

`Compare`(*self*, *item1*, *item2*, *column*, *ascending*)[¶](#wx.dataview.DataViewModel.Compare "Permalink to this definition")
The compare function to be used by the control.


The default compare function sorts most data types implemented by *Variant* (i.e. bool, int, long, double, string) as well as datetime and  [wx.dataview.DataViewIconText](wx.dataview.DataViewIconText.html#wx-dataview-dataviewicontext). Override this method to implement a different sorting behaviour or override just `DoCompareValues` to extend it to support other *Variant* types.


The function should return negative, null or positive for an ascending comparison, depending on whether the first item is less than, equal to or greater than the second one. The reverse is `True` for descending comparisons. The items should be compared using the appropriate type for the column passed.



Parameters
* **item1** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – First item to compare.
* **item2** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – Second item to compare.
* **column** (*int*) – The column holding the items to be compared. If the model class overrides [`HasDefaultCompare`](#wx.dataview.DataViewModel.HasDefaultCompare "wx.dataview.DataViewModel.HasDefaultCompare") to return `True`, this parameter will be
* **ascending** (*bool*) – Indicates whether the sort is being performed in ascending or descending order.



Return type
*int*



Returns
For an ascending comparison: a negative value if the item1 is less than (i.e. should appear above) item2, zero if the two items are equal or a positive value if item1 is greater than (i.e. should appear below) the second one. The reverse for a descending comparison.





Note


If there can be multiple rows with the same value, consider differentiating them form each other by their IDs rather than returning zero. This to prevent rows with the same value jumping positions when items are added etc. For example:



```
obj1 = self.ItemToObject(item1)
obj2 = self.ItemToObject(item2)
if obj1[column] == obj2[column]:
    return 1 if ascending == (item1.GetId() > item2.GetId()) else -1
else:
    return 1 if ascending == (obj1[column] > obj2[column]) else -1

```




See also


[`HasDefaultCompare`](#wx.dataview.DataViewModel.HasDefaultCompare "wx.dataview.DataViewModel.HasDefaultCompare") , `DoCompareValues`





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetAttr(self, item, col, attr) -> bool:
        """ 

`GetAttr`(*self*, *item*, *col*, *attr*)[¶](#wx.dataview.DataViewModel.GetAttr "Permalink to this definition")
Override this to indicate that the item has special font attributes.


This only affects the DataViewTextRendererText renderer.


The base class version always simply returns `False`.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – The item for which the attribute is requested.
* **col** (*int*) – The column of the item for which the attribute is requested.
* **attr** ([*wx.dataview.DataViewItemAttr*](wx.dataview.DataViewItemAttr.html#wx.dataview.DataViewItemAttr "wx.dataview.DataViewItemAttr")) – The attribute to be filled in if the function returns `True`.



Return type
*bool*



Returns
`True` if this item has an attribute or `False` otherwise.





See also


 [wx.dataview.DataViewItemAttr](wx.dataview.DataViewItemAttr.html#wx-dataview-dataviewitemattr).





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetChildren(self, item, children) -> int:
        """ 

`GetChildren`(*self*, *item*, *children*)[¶](#wx.dataview.DataViewModel.GetChildren "Permalink to this definition")
Override this so the control can query the child items of an item.


Returns the number of items.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **children** (*DataViewItemArray*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetParent(self, item: 'dataview.DataViewItem') -> 'DataViewItem':
        """ 

`GetParent`(*self*, *item*)[¶](#wx.dataview.DataViewModel.GetParent "Permalink to this definition")
Override this to indicate which  [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem) representing the parent of *item* or an invalid  [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem) if the root item is the parent item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def GetValue(self, item, col) -> Any:
        """ 

`GetValue`(*self*, *item*, *col*)[¶](#wx.dataview.DataViewModel.GetValue "Permalink to this definition")
Override this to indicate the value of *item*.


This function should fill the provided *variant* with the value to be shown for the specified item in the given column. The value returned in this *Variant* must have the appropriate type, e.g. string for the text columns, boolean for the columns using  [wx.dataview.DataViewToggleRenderer](wx.dataview.DataViewToggleRenderer.html#wx-dataview-dataviewtogglerenderer) etc, and if there is a type mismatch, nothing will be shown and a debug error message will be logged.


It is also possible to not return any value, in which case nothing will be shown in the corresponding cell, in the same way as if [`HasValue`](#wx.dataview.DataViewModel.HasValue "wx.dataview.DataViewModel.HasValue") returned `False`.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*variant*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasContainerColumns(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`HasContainerColumns`(*self*, *item*)[¶](#wx.dataview.DataViewModel.HasContainerColumns "Permalink to this definition")
Override this method to indicate if a container item merely acts as a headline (or for categorisation) or if it also acts a normal item with entries for further columns.


By default returns `False`.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasDefaultCompare(self) -> bool:
        """ 

`HasDefaultCompare`(*self*)[¶](#wx.dataview.DataViewModel.HasDefaultCompare "Permalink to this definition")
Override this to indicate that the model provides a default compare function that the control should use if no  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) has been chosen for sorting.


Usually, the user clicks on a column header for sorting, the data will be sorted alphanumerically.


If any other order (e.g. by index or order of appearance) is required, then this should be used.


Note that if this method is overridden to return `True`, the implementation of [`Compare`](#wx.dataview.DataViewModel.Compare "wx.dataview.DataViewModel.Compare") should be ready to accept


See  [wx.dataview.DataViewIndexListModel](wx.dataview.DataViewIndexListModel.html#wx-dataview-dataviewindexlistmodel) for a model which makes use of this.



Return type
*bool*





See also


[`Compare`](#wx.dataview.DataViewModel.Compare "wx.dataview.DataViewModel.Compare")





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def HasValue(self, item, col) -> bool:
        """ 

`HasValue`(*self*, *item*, *col*)[¶](#wx.dataview.DataViewModel.HasValue "Permalink to this definition")
Return `True` if there is a value in the given column of this item.


All normal items have values in all columns but the container items only show their label in the first column (*col* == 0) by default (but see [`HasContainerColumns`](#wx.dataview.DataViewModel.HasContainerColumns "wx.dataview.DataViewModel.HasContainerColumns") ). So this function by default returns `True` for the first column while for the other ones it returns `True` only if the item is not a container or [`HasContainerColumns`](#wx.dataview.DataViewModel.HasContainerColumns "wx.dataview.DataViewModel.HasContainerColumns") was overridden to return `True` for it.


Since wxWidgets 3.1.4, this method is virtual and can be overridden to explicitly specify for which columns a given item has, and doesn’t have, values.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** –



Return type
*bool*





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsContainer(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`IsContainer`(*self*, *item*)[¶](#wx.dataview.DataViewModel.IsContainer "Permalink to this definition")
Override this to indicate if *item* is a container, i.e. if it can have child items.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsEnabled(self, item, col) -> bool:
        """ 

`IsEnabled`(*self*, *item*, *col*)[¶](#wx.dataview.DataViewModel.IsEnabled "Permalink to this definition")
Override this to indicate that the item should be disabled.


Disabled items are displayed differently (e.g. grayed out) and cannot be interacted with.


The base class version always returns `True`, thus making all items enabled by default.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – The item whose enabled status is requested.
* **col** (*int*) – The column of the item whose enabled status is requested.



Return type
*bool*



Returns
`True` if this item should be enabled, `False` otherwise.





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsListModel(self) -> bool:
        """ 

`IsListModel`(*self*)[¶](#wx.dataview.DataViewModel.IsListModel "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def IsVirtualListModel(self) -> bool:
        """ 

`IsVirtualListModel`(*self*)[¶](#wx.dataview.DataViewModel.IsVirtualListModel "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemAdded(self, parent, item) -> bool:
        """ 

`ItemAdded`(*self*, *parent*, *item*)[¶](#wx.dataview.DataViewModel.ItemAdded "Permalink to this definition")
Call this to inform the model that an item has been added to the data.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemChanged(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`ItemChanged`(*self*, *item*)[¶](#wx.dataview.DataViewModel.ItemChanged "Permalink to this definition")
Call this to inform the model that an item has changed.


This will eventually emit a `wxEVT_DATAVIEW_ITEM_VALUE_CHANGED` event (in which the column fields will not be set) to the user.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemDeleted(self, parent, item) -> bool:
        """ 

`ItemDeleted`(*self*, *parent*, *item*)[¶](#wx.dataview.DataViewModel.ItemDeleted "Permalink to this definition")
Call this to inform the model that an item has been deleted from the data.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsAdded(self, parent, items) -> bool:
        """ 

`ItemsAdded`(*self*, *parent*, *items*)[¶](#wx.dataview.DataViewModel.ItemsAdded "Permalink to this definition")
Call this to inform the model that several items have been added to the data.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **items** (*DataViewItemArray*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsChanged(self, items: DataViewItemArray) -> bool:
        """ 

`ItemsChanged`(*self*, *items*)[¶](#wx.dataview.DataViewModel.ItemsChanged "Permalink to this definition")
Call this to inform the model that several items have changed.


This will eventually emit `wxEVT_DATAVIEW_ITEM_VALUE_CHANGED` events (in which the column fields will not be set) to the user.



Parameters
**items** (*DataViewItemArray*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ItemsDeleted(self, parent, items) -> bool:
        """ 

`ItemsDeleted`(*self*, *parent*, *items*)[¶](#wx.dataview.DataViewModel.ItemsDeleted "Permalink to this definition")
Call this to inform the model that several items have been deleted.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **items** (*DataViewItemArray*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def RemoveNotifier(self, notifier: 'dataview.DataViewModelNotifier') -> None:
        """ 

`RemoveNotifier`(*self*, *notifier*)[¶](#wx.dataview.DataViewModel.RemoveNotifier "Permalink to this definition")
Remove the *notifier* from the list of notifiers.



Parameters
**notifier** ([*wx.dataview.DataViewModelNotifier*](wx.dataview.DataViewModelNotifier.html#wx.dataview.DataViewModelNotifier "wx.dataview.DataViewModelNotifier")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def Resort(self) -> None:
        """ 

`Resort`(*self*)[¶](#wx.dataview.DataViewModel.Resort "Permalink to this definition")
Call this to initiate a resort after the sort function has been changed.




            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def SetValue(self, variant, item, col) -> bool:
        """ 

`SetValue`(*self*, *variant*, *item*, *col*)[¶](#wx.dataview.DataViewModel.SetValue "Permalink to this definition")
This gets called in order to set a value in the data model.


The most common scenario is that the  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) calls this method after the user changed some data in the view.


This is the function you need to override in your derived class but if you want to call it, [`ChangeValue`](#wx.dataview.DataViewModel.ChangeValue "wx.dataview.DataViewModel.ChangeValue") is usually more convenient as otherwise you need to manually call [`ValueChanged`](#wx.dataview.DataViewModel.ValueChanged "wx.dataview.DataViewModel.ValueChanged") to update the control itself.



Parameters
* **variant** (*DVCVariant*) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """

    def ValueChanged(self, item, col) -> bool:
        """ 

`ValueChanged`(*self*, *item*, *col*)[¶](#wx.dataview.DataViewModel.ValueChanged "Permalink to this definition")
Call this to inform this model that a value in the model has been changed.


This is also called from  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl)’s internal editing code, e.g. when editing a text field in the control.


This will eventually emit a `wxEVT_DATAVIEW_ITEM_VALUE_CHANGED` event to the user.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModel.html
        """



class DataViewItem:
    """ **Possible constructors**:



```
DataViewItem()

DataViewItem(item)

DataViewItem(id)

```


DataViewItem is a small opaque class that represents an item in a
DataViewCtrl in a persistent way, i.e.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewItem.__init__ "Permalink to this definition")
Constructor.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, item)*



Parameters
**item** ([*wx.dataview.DataViewItem*](#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






---

  



**\_\_init\_\_** *(self, id)*



Parameters
**id** – 






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def GetID(self) -> None:
        """ 

`GetID`(*self*)[¶](#wx.dataview.DataViewItem.GetID "Permalink to this definition")
Returns the `ID`.




            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.dataview.DataViewItem.IsOk "Permalink to this definition")
Returns `True` if the `ID` is not `None`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.dataview.DataViewItem.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*, *other*)[¶](#wx.dataview.DataViewItem.__eq__ "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __hash__(self) -> int:
        """ 

`__hash__`(*self*)[¶](#wx.dataview.DataViewItem.__hash__ "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __ne__(self, item: Any) -> bool:
        """ 

`__ne__`(*self*, *other*)[¶](#wx.dataview.DataViewItem.__ne__ "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.dataview.DataViewItem.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItem.html
        """

    ID: None  # `ID`[¶](#wx.dataview.DataViewItem.ID "Permalink to this definition")See [`GetID`](#wx.dataview.DataViewItem.GetID "wx.dataview.DataViewItem.GetID")



class DataViewColumn(SettableHeaderColumn):
    """ **Possible constructors**:



```
DataViewColumn(title, renderer, model_column, width=DVC_DEFAULT_WIDTH,
               align=ALIGN_CENTER, flags=DATAVIEW_COL_RESIZABLE)

DataViewColumn(bitmap, renderer, model_column, width=DVC_DEFAULT_WIDTH,
               align=ALIGN_CENTER, flags=DATAVIEW_COL_RESIZABLE)

```


This class represents a column in a DataViewCtrl.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewColumn.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, title, renderer, model\_column, width=DVC\_DEFAULT\_WIDTH, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*


Constructs a text column.



Parameters
* **title** (*string*) – The title of the column.
* **renderer** ([*wx.dataview.DataViewRenderer*](wx.dataview.DataViewRenderer.html#wx.dataview.DataViewRenderer "wx.dataview.DataViewRenderer")) – The class which will render the contents of this column.
* **model\_column** (*int*) – The index of the model’s column which is associated with this object.
* **width** (*int*) – The width of the column. The `DVC_DEFAULT_WIDTH` value is the fixed default value.
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) – The alignment of the column title.
* **flags** (*int*) – One or more flags of the  [wx.dataview.DataViewColumnFlags](wx.dataview.DataViewColumnFlags.enumeration.html#wx-dataview-dataviewcolumnflags) enumeration.






---

  



**\_\_init\_\_** *(self, bitmap, renderer, model\_column, width=DVC\_DEFAULT\_WIDTH, align=ALIGN\_CENTER, flags=DATAVIEW\_COL\_RESIZABLE)*


Constructs a bitmap column.



Parameters
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – The bitmap of the column.
* **renderer** ([*wx.dataview.DataViewRenderer*](wx.dataview.DataViewRenderer.html#wx.dataview.DataViewRenderer "wx.dataview.DataViewRenderer")) – The class which will render the contents of this column.
* **model\_column** (*int*) – The index of the model’s column which is associated with this object.
* **width** (*int*) – The width of the column. The `DVC_DEFAULT_WIDTH` value is the fixed default value.
* **align** ([*Alignment*](wx.Alignment.enumeration.html "Alignment")) – The alignment of the column title.
* **flags** (*int*) – One or more flags of the  [wx.dataview.DataViewColumnFlags](wx.dataview.DataViewColumnFlags.enumeration.html#wx-dataview-dataviewcolumnflags) enumeration.






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetModelColumn(self) -> int:
        """ 

`GetModelColumn`(*self*)[¶](#wx.dataview.DataViewColumn.GetModelColumn "Permalink to this definition")
Returns the index of the column of the model, which this  [wx.dataview.DataViewColumn](#wx-dataview-dataviewcolumn) is displaying.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetOwner(self) -> 'DataViewCtrl':
        """ 

`GetOwner`(*self*)[¶](#wx.dataview.DataViewColumn.GetOwner "Permalink to this definition")
Returns the owning  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl).



Return type
 [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl)






            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    def GetRenderer(self) -> 'DataViewRenderer':
        """ 

`GetRenderer`(*self*)[¶](#wx.dataview.DataViewColumn.GetRenderer "Permalink to this definition")
Returns the renderer of this  [wx.dataview.DataViewColumn](#wx-dataview-dataviewcolumn).



Return type
 [wx.dataview.DataViewRenderer](wx.dataview.DataViewRenderer.html#wx-dataview-dataviewrenderer)





See also


 [wx.dataview.DataViewRenderer](wx.dataview.DataViewRenderer.html#wx-dataview-dataviewrenderer).





            Source: https://docs.wxpython.org/wx.dataview.DataViewColumn.html
        """

    Alignment: Any  # `Alignment`[¶](#wx.dataview.DataViewColumn.Alignment "Permalink to this definition")See `GetAlignment` and [`SetAlignment`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetAlignment "wx.SettableHeaderColumn.SetAlignment")
    Bitmap: Any  # `Bitmap`[¶](#wx.dataview.DataViewColumn.Bitmap "Permalink to this definition")See `GetBitmap` and [`SetBitmap`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetBitmap "wx.SettableHeaderColumn.SetBitmap")
    Flags: Any  # `Flags`[¶](#wx.dataview.DataViewColumn.Flags "Permalink to this definition")See `GetFlags` and [`SetFlags`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetFlags "wx.SettableHeaderColumn.SetFlags")
    MinWidth: Any  # `MinWidth`[¶](#wx.dataview.DataViewColumn.MinWidth "Permalink to this definition")See `GetMinWidth` and [`SetMinWidth`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetMinWidth "wx.SettableHeaderColumn.SetMinWidth")
    ModelColumn: int  # `ModelColumn`[¶](#wx.dataview.DataViewColumn.ModelColumn "Permalink to this definition")See [`GetModelColumn`](#wx.dataview.DataViewColumn.GetModelColumn "wx.dataview.DataViewColumn.GetModelColumn")
    Owner: 'DataViewCtrl'  # `Owner`[¶](#wx.dataview.DataViewColumn.Owner "Permalink to this definition")See [`GetOwner`](#wx.dataview.DataViewColumn.GetOwner "wx.dataview.DataViewColumn.GetOwner")
    Renderer: 'DataViewRenderer'  # `Renderer`[¶](#wx.dataview.DataViewColumn.Renderer "Permalink to this definition")See [`GetRenderer`](#wx.dataview.DataViewColumn.GetRenderer "wx.dataview.DataViewColumn.GetRenderer")
    SortOrder: Any  # `SortOrder`[¶](#wx.dataview.DataViewColumn.SortOrder "Permalink to this definition")See `IsSortOrderAscending` and [`SetSortOrder`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetSortOrder "wx.SettableHeaderColumn.SetSortOrder")
    Title: Any  # `Title`[¶](#wx.dataview.DataViewColumn.Title "Permalink to this definition")See `GetTitle` and [`SetTitle`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetTitle "wx.SettableHeaderColumn.SetTitle")
    Width: Any  # `Width`[¶](#wx.dataview.DataViewColumn.Width "Permalink to this definition")See `GetWidth` and [`SetWidth`](wx.SettableHeaderColumn.html#wx.SettableHeaderColumn.SetWidth "wx.SettableHeaderColumn.SetWidth")



class DataViewRenderer(Object):
    """ **Possible constructors**:



```
DataViewRenderer(varianttype, mode=DATAVIEW_CELL_INERT,
                 align=DVR_DEFAULT_ALIGNMENT)

```


This class is used by DataViewCtrl to render the individual cells.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
    """
    def __init__(self, varianttype, mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ 

`__init__`(*self*, *varianttype*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewRenderer.__init__ "Permalink to this definition")
Constructor.


The *varianttype* parameter is the main type of *Variant* objects supported by this renderer, i.e. those that can be passed to its [`SetValue`](#wx.dataview.DataViewRenderer.SetValue "wx.dataview.DataViewRenderer.SetValue") , e.g. “string” for  [wx.dataview.DataViewTextRenderer](wx.dataview.DataViewTextRenderer.html#wx-dataview-dataviewtextrenderer). The value of this parameter is returned by [`GetVariantType`](#wx.dataview.DataViewRenderer.GetVariantType "wx.dataview.DataViewRenderer.GetVariantType") .


When deriving a custom renderer, either an existing variant type or a new custom one can be used, see *Variant* documentation for more details.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def CancelEditing(self) -> None:
        """ 

`CancelEditing`(*self*)[¶](#wx.dataview.DataViewRenderer.CancelEditing "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def CreateEditorCtrl(self, parent, labelRect, value) -> 'Window':
        """ 

`CreateEditorCtrl`(*self*, *parent*, *labelRect*, *value*)[¶](#wx.dataview.DataViewRenderer.CreateEditorCtrl "Permalink to this definition")

Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **labelRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **value** (*DVCVariant*) –



Return type
*Window*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def DisableEllipsize(self) -> None:
        """ 

`DisableEllipsize`(*self*)[¶](#wx.dataview.DataViewRenderer.DisableEllipsize "Permalink to this definition")
Disable replacing parts of the item text with ellipsis.


If ellipsizing is disabled, the string will be truncated if it doesn’t fit.


This is the same as:



```
EnableEllipsize(wx.ELLIPSIZE_NONE)

```



New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def EnableEllipsize(self, mode: EllipsizeMode=ELLIPSIZE_MIDDLE) -> None:
        """ 

`EnableEllipsize`(*self*, *mode=ELLIPSIZE\_MIDDLE*)[¶](#wx.dataview.DataViewRenderer.EnableEllipsize "Permalink to this definition")
Enable or disable replacing parts of the item text with ellipsis to make it fit the column width.


This method only makes sense for the renderers working with text, such as  [wx.dataview.DataViewTextRenderer](wx.dataview.DataViewTextRenderer.html#wx-dataview-dataviewtextrenderer) or  [wx.dataview.DataViewIconTextRenderer](wx.dataview.DataViewIconTextRenderer.html#wx-dataview-dataviewicontextrenderer).


By default `wx.ELLIPSIZE_MIDDLE` is used.



Parameters
**mode** ([*EllipsizeMode*](wx.EllipsizeMode.enumeration.html "EllipsizeMode")) – Ellipsization mode, use `wx.ELLIPSIZE_NONE` to disable.





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def FinishEditing(self) -> bool:
        """ 

`FinishEditing`(*self*)[¶](#wx.dataview.DataViewRenderer.FinishEditing "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetAlignment(self) -> int:
        """ 

`GetAlignment`(*self*)[¶](#wx.dataview.DataViewRenderer.GetAlignment "Permalink to this definition")
Returns the alignment.


See [`SetAlignment`](#wx.dataview.DataViewRenderer.SetAlignment "wx.dataview.DataViewRenderer.SetAlignment")



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetEditorCtrl(self) -> 'Window':
        """ 

`GetEditorCtrl`(*self*)[¶](#wx.dataview.DataViewRenderer.GetEditorCtrl "Permalink to this definition")

Return type
*Window*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetEllipsizeMode(self) -> 'EllipsizeMode':
        """ 

`GetEllipsizeMode`(*self*)[¶](#wx.dataview.DataViewRenderer.GetEllipsizeMode "Permalink to this definition")
Returns the ellipsize mode used by the renderer.


If the return value is `wx.ELLIPSIZE_NONE`, the text is simply truncated if it doesn’t fit.



Return type
 [wx.EllipsizeMode](wx.EllipsizeMode.enumeration.html#wx-ellipsizemode)





See also


[`EnableEllipsize`](#wx.dataview.DataViewRenderer.EnableEllipsize "wx.dataview.DataViewRenderer.EnableEllipsize")





            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetMode(self) -> 'DataViewCellMode':
        """ 

`GetMode`(*self*)[¶](#wx.dataview.DataViewRenderer.GetMode "Permalink to this definition")
Returns the cell mode.



Return type
 [wx.dataview.DataViewCellMode](wx.dataview.DataViewCellMode.enumeration.html#wx-dataview-dataviewcellmode)






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetOwner(self) -> 'DataViewColumn':
        """ 

`GetOwner`(*self*)[¶](#wx.dataview.DataViewRenderer.GetOwner "Permalink to this definition")
Returns pointer to the owning  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn).



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetValue(self) -> Any:
        """ 

`GetValue`(*self*)[¶](#wx.dataview.DataViewRenderer.GetValue "Permalink to this definition")
This methods retrieves the value from the renderer in order to transfer the value back to the data model.


Returns `False` on failure.



Return type
*value*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetValueFromEditorCtrl(self, editor: 'Window') -> Any:
        """ 

`GetValueFromEditorCtrl`(*self*, *editor*)[¶](#wx.dataview.DataViewRenderer.GetValueFromEditorCtrl "Permalink to this definition")

Parameters
**editor** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*value*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetVariantType(self) -> str:
        """ 

`GetVariantType`(*self*)[¶](#wx.dataview.DataViewRenderer.GetVariantType "Permalink to this definition")
Returns a string with the type of the *Variant* supported by this renderer.


Note that a renderer may support more than one variant type, in which case it needs to override [`IsCompatibleVariantType`](#wx.dataview.DataViewRenderer.IsCompatibleVariantType "wx.dataview.DataViewRenderer.IsCompatibleVariantType") to return `True` for all types it supports. But by default only the type returned by this function is supported.



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def GetView(self) -> 'DataViewCtrl':
        """ 

`GetView`(*self*)[¶](#wx.dataview.DataViewRenderer.GetView "Permalink to this definition")

Return type
 [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl)






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def HasEditorCtrl(self) -> bool:
        """ 

`HasEditorCtrl`(*self*)[¶](#wx.dataview.DataViewRenderer.HasEditorCtrl "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def IsCompatibleVariantType(self, variantType: str) -> bool:
        """ 

`IsCompatibleVariantType`(*self*, *variantType*)[¶](#wx.dataview.DataViewRenderer.IsCompatibleVariantType "Permalink to this definition")
Check if the given variant type is compatible with the type expected by this renderer.


The base class implementation just compares *variantType* with the value returned by [`GetVariantType`](#wx.dataview.DataViewRenderer.GetVariantType "wx.dataview.DataViewRenderer.GetVariantType") , but this function can be overridden to accept other types that can be converted to the type needed by the renderer.



Parameters
**variantType** (*string*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetAlignment(self, align: int) -> None:
        """ 

`SetAlignment`(*self*, *align*)[¶](#wx.dataview.DataViewRenderer.SetAlignment "Permalink to this definition")
Sets the alignment of the renderer’s content.


The default value of `DVR_DEFAULT_ALIGNMENT` indicates that the content should have the same alignment as the column header.


The method is not implemented under macOS and the renderer always aligns its contents as the column header on that platform. The other platforms support both vertical and horizontal alignment.



Parameters
**align** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetOwner(self, owner: 'dataview.DataViewColumn') -> None:
        """ 

`SetOwner`(*self*, *owner*)[¶](#wx.dataview.DataViewRenderer.SetOwner "Permalink to this definition")
Sets the owning  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn).


This is usually called from within  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn).



Parameters
**owner** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetValue(self, value: DVCVariant) -> bool:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.dataview.DataViewRenderer.SetValue "Permalink to this definition")
Set the value of the renderer (and thus its cell) to *value*.


The internal code will then render this cell with this data.



Parameters
**value** (`DVCVariant`) – A valid, i.e. non-null, value to be shown.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def SetValueAdjuster(self, transformer: 'dataview.DataViewValueAdjuster') -> None:
        """ 

`SetValueAdjuster`(*self*, *transformer*)[¶](#wx.dataview.DataViewRenderer.SetValueAdjuster "Permalink to this definition")
Set the transformer object to be used to customize values before they are rendered.


Can be used to change the value if it is shown on a highlighted row (i.e. in selection) which typically has dark background. It is useful in combination with  [wx.dataview.DataViewTextRenderer](wx.dataview.DataViewTextRenderer.html#wx-dataview-dataviewtextrenderer) with markup and can be used e.g. to remove background color attributes inside selection, as a lightweight alternative to implementing an entire  [wx.dataview.DataViewCustomRenderer](wx.dataview.DataViewCustomRenderer.html#wx-dataview-dataviewcustomrenderer) specialization.


*transformer* can be `None` to reset any transformer currently being used.


Takes ownership of *transformer*.



Parameters
**transformer** ([*wx.dataview.DataViewValueAdjuster*](wx.dataview.DataViewValueAdjuster.html#wx.dataview.DataViewValueAdjuster "wx.dataview.DataViewValueAdjuster")) – 





New in version 4.1/wxWidgets-3.1.1.




See also


 [wx.dataview.DataViewValueAdjuster](wx.dataview.DataViewValueAdjuster.html#wx-dataview-dataviewvalueadjuster)





            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def StartEditing(self, item, labelRect) -> bool:
        """ 

`StartEditing`(*self*, *item*, *labelRect*)[¶](#wx.dataview.DataViewRenderer.StartEditing "Permalink to this definition")

Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **labelRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    def Validate(self, value: DVCVariant) -> bool:
        """ 

`Validate`(*self*, *value*)[¶](#wx.dataview.DataViewRenderer.Validate "Permalink to this definition")
Before data is committed to the data model, it is passed to this method where it can be checked for validity.


This can also be used for checking a valid range or limiting the user input in a certain aspect (e.g. max number of characters or only alphanumeric input, `ASCII` only etc.). Return `False` if the value is not valid.


Please note that due to implementation limitations, this validation is done after the editing control already is destroyed and the editing process finished.



Parameters
**value** (*DVCVariant*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewRenderer.html
        """

    Alignment: int  # `Alignment`[¶](#wx.dataview.DataViewRenderer.Alignment "Permalink to this definition")See [`GetAlignment`](#wx.dataview.DataViewRenderer.GetAlignment "wx.dataview.DataViewRenderer.GetAlignment") and [`SetAlignment`](#wx.dataview.DataViewRenderer.SetAlignment "wx.dataview.DataViewRenderer.SetAlignment")
    EditorCtrl: 'Window'  # `EditorCtrl`[¶](#wx.dataview.DataViewRenderer.EditorCtrl "Permalink to this definition")See [`GetEditorCtrl`](#wx.dataview.DataViewRenderer.GetEditorCtrl "wx.dataview.DataViewRenderer.GetEditorCtrl")
    EllipsizeMode: '_EllipsizeMode'  # `EllipsizeMode`[¶](#wx.dataview.DataViewRenderer.EllipsizeMode "Permalink to this definition")See [`GetEllipsizeMode`](#wx.dataview.DataViewRenderer.GetEllipsizeMode "wx.dataview.DataViewRenderer.GetEllipsizeMode")
    Mode: 'DataViewCellMode'  # `Mode`[¶](#wx.dataview.DataViewRenderer.Mode "Permalink to this definition")See [`GetMode`](#wx.dataview.DataViewRenderer.GetMode "wx.dataview.DataViewRenderer.GetMode")
    Owner: 'DataViewColumn'  # `Owner`[¶](#wx.dataview.DataViewRenderer.Owner "Permalink to this definition")See [`GetOwner`](#wx.dataview.DataViewRenderer.GetOwner "wx.dataview.DataViewRenderer.GetOwner") and [`SetOwner`](#wx.dataview.DataViewRenderer.SetOwner "wx.dataview.DataViewRenderer.SetOwner")
    VariantType: str  # `VariantType`[¶](#wx.dataview.DataViewRenderer.VariantType "Permalink to this definition")See [`GetVariantType`](#wx.dataview.DataViewRenderer.GetVariantType "wx.dataview.DataViewRenderer.GetVariantType")
    View: 'DataViewCtrl'  # `View`[¶](#wx.dataview.DataViewRenderer.View "Permalink to this definition")See [`GetView`](#wx.dataview.DataViewRenderer.GetView "wx.dataview.DataViewRenderer.GetView")



ELLIPSIZE_MIDDLE: int

ELLIPSIZE_NONE: int

class DataViewCustomRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewCustomRenderer(varianttype=DataViewCustomRenderer.GetDefaultType
                       (), mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


You need to derive a new class from DataViewCustomRenderer in order
to write a new renderer.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewCustomRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewCustomRenderer.__init__ "Permalink to this definition")
Constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def Activate(self, cell, model, item, col) -> bool:
        """ 

`Activate`(*self*, *cell*, *model*, *item*, *col*)[¶](#wx.dataview.DataViewCustomRenderer.Activate "Permalink to this definition")
Override this to react to the activation of a cell.



Parameters
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*





Deprecated


Use ActivateCell instead.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def ActivateCell(self, cell, model, item, col, mouseEvent) -> bool:
        """ 

`ActivateCell`(*self*, *cell*, *model*, *item*, *col*, *mouseEvent*)[¶](#wx.dataview.DataViewCustomRenderer.ActivateCell "Permalink to this definition")
Override this to react to cell *activation*.


Activating a cell is an alternative to showing inline editor when the value can be edited in a simple way that doesn’t warrant full editor control. The most typical use of cell activation is toggling the checkbox in  [wx.dataview.DataViewToggleRenderer](wx.dataview.DataViewToggleRenderer.html#wx-dataview-dataviewtogglerenderer); others would be e.g. an embedded volume slider or a five-star rating column.


The exact means of activating a cell are platform-dependent, but they are usually similar to those used for inline editing of values. Typically, a cell would be activated by Space or Enter keys or by left mouse click.


This method will only be called if the cell has the `wx.dataview.DATAVIEW_CELL_ACTIVATABLE` mode.



Parameters
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Coordinates of the activated cell’s area.
* **model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) – The model to manipulate in response.
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – Activated item.
* **col** (*int*) – Activated column of *item*.
* **mouseEvent** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – If the activation was triggered by mouse click, contains the corresponding event. Is `None` otherwise (for keyboard activation). Mouse coordinates are adjusted to be relative to the cell.



Return type
*bool*





New in version 2.9.3.




Note


Do not confuse this method with item activation in  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) and the wxEVT\_DATAVIEW\_ITEM\_ACTIVATED event. That one is used for activating the item (or, to put it differently, the entire row) similarly to analogous messages in  [wx.TreeCtrl](wx.TreeCtrl.html#wx-treectrl) and  [wx.ListCtrl](wx.ListCtrl.html#wx-listctrl), and the effect differs (play a song, open a file etc.). Cell activation, on the other hand, is all about interacting with the individual cell.




See also


[`CreateEditorCtrl`](#wx.dataview.DataViewCustomRenderer.CreateEditorCtrl "wx.dataview.DataViewCustomRenderer.CreateEditorCtrl")





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def CreateEditorCtrl(self, parent, labelRect, value) -> 'Window':
        """ 

`CreateEditorCtrl`(*self*, *parent*, *labelRect*, *value*)[¶](#wx.dataview.DataViewCustomRenderer.CreateEditorCtrl "Permalink to this definition")
Override this to create the actual editor control once editing is about to start.


This method will only be called if the cell has the `wx.dataview.DATAVIEW_CELL_EDITABLE` mode. Editing is typically triggered by slowly double-clicking the cell or by a platform-dependent keyboard shortcut (`F2` is typical on Windows, Space and/or Enter is common elsewhere and supported on Windows too).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The parent of the editor control.
* **labelRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Indicates the position and size of the editor control. The control should be created in place of the cell and *labelRect* should be respected as much as possible.
* **value** (*DVCVariant*) – Initial value of the editor.



Return type
*Window*





```
# Some integer...
l = value
return wx.SpinCtrl(parent, wx.ID_ANY, "",
                   labelRect.GetTopLeft(), labelRect.GetSize(), 0, 0, 100, l)

```



Note


Currently support for this method is not implemented in the native macOS version of the control, i.e. it will be never called there.




See also


[`ActivateCell`](#wx.dataview.DataViewCustomRenderer.ActivateCell "wx.dataview.DataViewCustomRenderer.ActivateCell")





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetAttr(self) -> 'DataViewItemAttr':
        """ 

`GetAttr`(*self*)[¶](#wx.dataview.DataViewCustomRenderer.GetAttr "Permalink to this definition")
Return the attribute to be used for rendering.


This function may be called from [`Render`](#wx.dataview.DataViewCustomRenderer.Render "wx.dataview.DataViewCustomRenderer.Render") implementation to use the attributes defined for the item if the renderer supports them.


Notice that when [`Render`](#wx.dataview.DataViewCustomRenderer.Render "wx.dataview.DataViewCustomRenderer.Render") is called, the  [wx.DC](wx.DC.html#wx-dc) object passed to it is already set up to use the correct attributes (e.g. its font is set to bold or italic version if [`wx.dataview.DataViewItemAttr.GetBold`](wx.dataview.DataViewItemAttr.html#wx.dataview.DataViewItemAttr.GetBold "wx.dataview.DataViewItemAttr.GetBold") or GetItalic() returns `True`) so it may not be necessary to call it explicitly if you only want to render text using the items attributes.



Return type
 [wx.dataview.DataViewItemAttr](wx.dataview.DataViewItemAttr.html#wx-dataview-dataviewitemattr)





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewCustomRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetSize(self) -> 'Size':
        """ 

`GetSize`(*self*)[¶](#wx.dataview.DataViewCustomRenderer.GetSize "Permalink to this definition")
Return size required to show content.



Return type
[`Size`](#wx.dataview.DataViewCustomRenderer.Size "wx.dataview.DataViewCustomRenderer.Size")






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetTextExtent(self, str: str) -> 'Size':
        """ 

`GetTextExtent`(*self*, *str*)[¶](#wx.dataview.DataViewCustomRenderer.GetTextExtent "Permalink to this definition")
Helper for [`GetSize`](#wx.dataview.DataViewCustomRenderer.GetSize "wx.dataview.DataViewCustomRenderer.GetSize") implementations, respects attributes.



Parameters
**str** (*string*) – 



Return type
[`Size`](#wx.dataview.DataViewCustomRenderer.Size "wx.dataview.DataViewCustomRenderer.Size")






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def GetValueFromEditorCtrl(self, editor: 'Window') -> Any:
        """ 

`GetValueFromEditorCtrl`(*self*, *editor*)[¶](#wx.dataview.DataViewCustomRenderer.GetValueFromEditorCtrl "Permalink to this definition")
Override this so that the renderer can get the value from the editor control (pointed to by *editor*):



```
# sc is a wx.SpinCtrl
l = sc.GetValue()
value = l
return True

```



Parameters
**editor** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*value*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def HasEditorCtrl(self) -> bool:
        """ 

`HasEditorCtrl`(*self*)[¶](#wx.dataview.DataViewCustomRenderer.HasEditorCtrl "Permalink to this definition")
Override this and make it return `True` in order to indicate that this renderer supports in-place editing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def LeftClick(self, cursor, cell, model, item, col) -> bool:
        """ 

`LeftClick`(*self*, *cursor*, *cell*, *model*, *item*, *col*)[¶](#wx.dataview.DataViewCustomRenderer.LeftClick "Permalink to this definition")
Override this to react to a left click.


This method will only be called in `DATAVIEW_CELL_ACTIVATABLE` mode.



Parameters
* **cursor** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*





Deprecated


Use ActivateCell instead.





            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def Render(self, cell, dc, state) -> bool:
        """ 

`Render`(*self*, *cell*, *dc*, *state*)[¶](#wx.dataview.DataViewCustomRenderer.Render "Permalink to this definition")
Override this to render the cell.


Before this is called, [`wx.dataview.DataViewRenderer.SetValue`](wx.dataview.DataViewRenderer.html#wx.dataview.DataViewRenderer.SetValue "wx.dataview.DataViewRenderer.SetValue") was called so that this instance knows what to render.



Parameters
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **state** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def RenderText(self, text, xoffset, cell, dc, state) -> None:
        """ 

`RenderText`(*self*, *text*, *xoffset*, *cell*, *dc*, *state*)[¶](#wx.dataview.DataViewCustomRenderer.RenderText "Permalink to this definition")
This method should be called from within [`Render`](#wx.dataview.DataViewCustomRenderer.Render "wx.dataview.DataViewCustomRenderer.Render") whenever you need to render simple text.


This will ensure that the correct colour, font and vertical alignment will be chosen so the text will look the same as text drawn by native renderers.



Parameters
* **text** (*string*) –
* **xoffset** (*int*) –
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **state** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    def StartDrag(self, cursor, cell, model, item, col) -> bool:
        """ 

`StartDrag`(*self*, *cursor*, *cell*, *model*, *item*, *col*)[¶](#wx.dataview.DataViewCustomRenderer.StartDrag "Permalink to this definition")
Override this to start a drag operation.


Not yet supported.



Parameters
* **cursor** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **cell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewCustomRenderer.html
        """

    Attr: 'DataViewItemAttr'  # `Attr`[¶](#wx.dataview.DataViewCustomRenderer.Attr "Permalink to this definition")See [`GetAttr`](#wx.dataview.DataViewCustomRenderer.GetAttr "wx.dataview.DataViewCustomRenderer.GetAttr")
    Size: '_Size'  # `Size`[¶](#wx.dataview.DataViewCustomRenderer.Size "Permalink to this definition")See [`GetSize`](#wx.dataview.DataViewCustomRenderer.GetSize "wx.dataview.DataViewCustomRenderer.GetSize")



DATAVIEW_CELL_ACTIVATABLE: int

DATAVIEW_CELL_EDITABLE: int

class DataViewEvent(NotifyEvent):
    """ **Possible constructors**:



```
DataViewEvent()

DataViewEvent(evtType, dvc, column, item=DataViewItem())

DataViewEvent(evtType, dvc, item)

DataViewEvent(event)

```


This is the event class for the DataViewCtrl notifications.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor, normally shouldn’t be used and mostly exists only for backwards compatibility.




---

  



**\_\_init\_\_** *(self, evtType, dvc, column, item=DataViewItem())*


Constructor for the events affecting columns (and possibly also items).



Parameters
* **evtType** (*wx.EventType*) –
* **dvc** ([*wx.dataview.DataViewCtrl*](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl "wx.dataview.DataViewCtrl")) –
* **column** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –






---

  



**\_\_init\_\_** *(self, evtType, dvc, item)*


Constructor for the events affecting only the items.



Parameters
* **evtType** (*wx.EventType*) –
* **dvc** ([*wx.dataview.DataViewCtrl*](wx.dataview.DataViewCtrl.html#wx.dataview.DataViewCtrl "wx.dataview.DataViewCtrl")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –






---

  



**\_\_init\_\_** *(self, event)*


Copy constructor.



Parameters
**event** ([*wx.dataview.DataViewEvent*](#wx.dataview.DataViewEvent "wx.dataview.DataViewEvent")) – 






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetCacheFrom(self) -> int:
        """ 

`GetCacheFrom`(*self*)[¶](#wx.dataview.DataViewEvent.GetCacheFrom "Permalink to this definition")
Return the first row that will be displayed.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetCacheTo(self) -> int:
        """ 

`GetCacheTo`(*self*)[¶](#wx.dataview.DataViewEvent.GetCacheTo "Permalink to this definition")
Return the last row that will be displayed.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetColumn(self) -> int:
        """ 

`GetColumn`(*self*)[¶](#wx.dataview.DataViewEvent.GetColumn "Permalink to this definition")
Returns the position of the column in the control or -1 if column field is unavailable for this event.


For wxEVT\_DATAVIEW\_COLUMN\_REORDERED, this is the new position of the column.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataBuffer(self) -> Any:
        """ 

`GetDataBuffer`(*self*)[¶](#wx.dataview.DataViewEvent.GetDataBuffer "Permalink to this definition")
Gets the data buffer for a drop data transfer



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataFormat(self) -> 'DataFormat':
        """ 

`GetDataFormat`(*self*)[¶](#wx.dataview.DataViewEvent.GetDataFormat "Permalink to this definition")
Gets the  [wx.DataFormat](wx.DataFormat.html#wx-dataformat) during a drop operation.



Return type
[`DataFormat`](#wx.dataview.DataViewEvent.DataFormat "wx.dataview.DataViewEvent.DataFormat")






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataObject(self) -> 'DataObject':
        """ 

`GetDataObject`(*self*)[¶](#wx.dataview.DataViewEvent.GetDataObject "Permalink to this definition")

Return type
[`DataObject`](#wx.dataview.DataViewEvent.DataObject "wx.dataview.DataViewEvent.DataObject")






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataSize(self) -> int:
        """ 

`GetDataSize`(*self*)[¶](#wx.dataview.DataViewEvent.GetDataSize "Permalink to this definition")
Gets the data size for a drop data transfer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDataViewColumn(self) -> 'DataViewColumn':
        """ 

`GetDataViewColumn`(*self*)[¶](#wx.dataview.DataViewEvent.GetDataViewColumn "Permalink to this definition")
Returns a pointer to the  [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn) from which the event was emitted or `None`.



Return type
 [wx.dataview.DataViewColumn](wx.dataview.DataViewColumn.html#wx-dataview-dataviewcolumn)






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDragFlags(self) -> int:
        """ 

`GetDragFlags`(*self*)[¶](#wx.dataview.DataViewEvent.GetDragFlags "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetDropEffect(self) -> 'DragResult':
        """ 

`GetDropEffect`(*self*)[¶](#wx.dataview.DataViewEvent.GetDropEffect "Permalink to this definition")
Returns the effect the user requested to happen to the dropped data.


This function can be used inside wxEVT\_DATAVIEW\_ITEM\_DROP\_POSSIBLE and wxEVT\_DATAVIEW\_ITEM\_DROP handlers and returns whether the user is trying to copy (the return value is `wx.DragCopy` ) or move (if the return value is `wx.DragMove` ) the data.


Currently this is only available when using the generic version of  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) (used e.g. under MSW) and always returns `wx.DragNone` in the GTK and macOS native versions.



Return type
 [wx.DragResult](wx.DragResult.enumeration.html#wx-dragresult)





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetItem(self) -> 'DataViewItem':
        """ 

`GetItem`(*self*)[¶](#wx.dataview.DataViewEvent.GetItem "Permalink to this definition")
Returns the item affected by the event.


Notice that for `wxEVT_DATAVIEW_ITEM_DROP_POSSIBLE` and `wxEVT_DATAVIEW_ITEM_DROP` event handlers, the item may be invalid, indicating that the drop is about to happen outside of the item area.



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetModel(self) -> 'DataViewModel':
        """ 

`GetModel`(*self*)[¶](#wx.dataview.DataViewEvent.GetModel "Permalink to this definition")
Returns the  [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel) associated with the event.



Return type
 [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel)






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetPosition(self) -> 'Point':
        """ 

`GetPosition`(*self*)[¶](#wx.dataview.DataViewEvent.GetPosition "Permalink to this definition")
Returns the position of a context menu event in client coordinates.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetProposedDropIndex(self) -> int:
        """ 

`GetProposedDropIndex`(*self*)[¶](#wx.dataview.DataViewEvent.GetProposedDropIndex "Permalink to this definition")
Returns the index of the child item at which an item currently being dragged would be dropped.


This function can be used from wxEVT\_DATAVIEW\_ITEM\_DROP\_POSSIBLE handlers to determine the exact position of the item being dropped.


Note that it currently always returns `wx.NOT_FOUND` when using native GTK implementation of this control.



Return type
*int*





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def GetValue(self) -> 'DVCVariant':
        """ 

`GetValue`(*self*)[¶](#wx.dataview.DataViewEvent.GetValue "Permalink to this definition")
Returns a reference to a value.



Return type
*DVCVariant*






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def IsEditCancelled(self) -> bool:
        """ 

`IsEditCancelled`(*self*)[¶](#wx.dataview.DataViewEvent.IsEditCancelled "Permalink to this definition")
Can be used to determine whether the new value is going to be accepted in wxEVT\_DATAVIEW\_ITEM\_EDITING\_DONE handler.


Returns `True` if editing the item was cancelled or if the user tried to enter an invalid value (refused by [`wx.dataview.DataViewRenderer.Validate`](wx.dataview.DataViewRenderer.html#wx.dataview.DataViewRenderer.Validate "wx.dataview.DataViewRenderer.Validate") ). If this method returns `False`, it means that the value in the model is about to be changed to the new one.


Notice that wxEVT\_DATAVIEW\_ITEM\_EDITING\_DONE event handler can call [`wx.NotifyEvent.Veto`](wx.NotifyEvent.html#wx.NotifyEvent.Veto "wx.NotifyEvent.Veto") to prevent this from happening.


Currently support for setting this field and for vetoing the change is only available in the generic version of  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl), i.e. under MSW but not GTK nor macOS.



Return type
*bool*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetCache(self, from_, to_) -> None:
        """ 

`SetCache`(*self*, *from\_*, *to\_*)[¶](#wx.dataview.DataViewEvent.SetCache "Permalink to this definition")

Parameters
* **from\_** (*int*) –
* **to\_** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetColumn(self, col: int) -> None:
        """ 

`SetColumn`(*self*, *col*)[¶](#wx.dataview.DataViewEvent.SetColumn "Permalink to this definition")
Sets the column index associated with this event.



Parameters
**col** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataBuffer(self, buf: Any) -> None:
        """ 

`SetDataBuffer`(*self*, *buf*)[¶](#wx.dataview.DataViewEvent.SetDataBuffer "Permalink to this definition")

Parameters
**buf** – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataFormat(self, format: 'DataFormat') -> None:
        """ 

`SetDataFormat`(*self*, *format*)[¶](#wx.dataview.DataViewEvent.SetDataFormat "Permalink to this definition")

Parameters
**format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataObject(self, obj: 'DataObject') -> None:
        """ 

`SetDataObject`(*self*, *obj*)[¶](#wx.dataview.DataViewEvent.SetDataObject "Permalink to this definition")
Set  [wx.DataObject](wx.DataObject.html#wx-dataobject) for data transfer within a drag operation.


This method must be used inside a `wxEVT_DATAVIEW_ITEM_BEGIN_DRAG` handler to associate the data object to be dragged with the item.


Note that the control takes ownership of the data object, i.e. *obj* must be heap-allocated and will be deleted by  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) itself.



Parameters
**obj** ([*wx.DataObject*](wx.DataObject.html#wx.DataObject "wx.DataObject")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataSize(self, size: int) -> None:
        """ 

`SetDataSize`(*self*, *size*)[¶](#wx.dataview.DataViewEvent.SetDataSize "Permalink to this definition")

Parameters
**size** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDataViewColumn(self, col: 'dataview.DataViewColumn') -> None:
        """ 

`SetDataViewColumn`(*self*, *col*)[¶](#wx.dataview.DataViewEvent.SetDataViewColumn "Permalink to this definition")
For `wxEVT_DATAVIEW_COLUMN_HEADER_CLICK` only.



Parameters
**col** ([*wx.dataview.DataViewColumn*](wx.dataview.DataViewColumn.html#wx.dataview.DataViewColumn "wx.dataview.DataViewColumn")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDragFlags(self, flags: int) -> None:
        """ 

`SetDragFlags`(*self*, *flags*)[¶](#wx.dataview.DataViewEvent.SetDragFlags "Permalink to this definition")
Specify the kind of the drag operation to perform.


This method can be used inside a `wxEVT_DATAVIEW_ITEM_BEGIN_DRAG` handler in order to configure the drag operation. Valid values are `wx.Drag_CopyOnly` (default), `wx.Drag_AllowMove` (allow the data to be moved) and `wx.Drag_DefaultMove` .


Currently it is only honoured by the generic version of  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) (used e.g. under MSW) and not supported by the native GTK and macOS versions.



Parameters
**flags** (*int*) – 





New in version 2.9.4.




See also


[`GetDropEffect`](#wx.dataview.DataViewEvent.GetDropEffect "wx.dataview.DataViewEvent.GetDropEffect")





            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetDropEffect(self, effect: DragResult) -> None:
        """ 

`SetDropEffect`(*self*, *effect*)[¶](#wx.dataview.DataViewEvent.SetDropEffect "Permalink to this definition")

Parameters
**effect** ([*DragResult*](wx.DragResult.enumeration.html "DragResult")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetItem(self, item: 'dataview.DataViewItem') -> None:
        """ 

`SetItem`(*self*, *item*)[¶](#wx.dataview.DataViewEvent.SetItem "Permalink to this definition")

Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetModel(self, model: 'dataview.DataViewModel') -> None:
        """ 

`SetModel`(*self*, *model*)[¶](#wx.dataview.DataViewEvent.SetModel "Permalink to this definition")
Sets the dataview model associated with this event.



Parameters
**model** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetPosition(self, x, y) -> None:
        """ 

`SetPosition`(*self*, *x*, *y*)[¶](#wx.dataview.DataViewEvent.SetPosition "Permalink to this definition")

Parameters
* **x** (*int*) –
* **y** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    def SetValue(self, value: DVCVariant) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.dataview.DataViewEvent.SetValue "Permalink to this definition")
Sets the value associated with this event.



Parameters
**value** (*DVCVariant*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewEvent.html
        """

    CacheFrom: int  # `CacheFrom`[¶](#wx.dataview.DataViewEvent.CacheFrom "Permalink to this definition")See [`GetCacheFrom`](#wx.dataview.DataViewEvent.GetCacheFrom "wx.dataview.DataViewEvent.GetCacheFrom")
    CacheTo: int  # `CacheTo`[¶](#wx.dataview.DataViewEvent.CacheTo "Permalink to this definition")See [`GetCacheTo`](#wx.dataview.DataViewEvent.GetCacheTo "wx.dataview.DataViewEvent.GetCacheTo")
    Column: int  # `Column`[¶](#wx.dataview.DataViewEvent.Column "Permalink to this definition")See [`GetColumn`](#wx.dataview.DataViewEvent.GetColumn "wx.dataview.DataViewEvent.GetColumn") and [`SetColumn`](#wx.dataview.DataViewEvent.SetColumn "wx.dataview.DataViewEvent.SetColumn")
    DataBuffer: Any  # `DataBuffer`[¶](#wx.dataview.DataViewEvent.DataBuffer "Permalink to this definition")See [`GetDataBuffer`](#wx.dataview.DataViewEvent.GetDataBuffer "wx.dataview.DataViewEvent.GetDataBuffer") and [`SetDataBuffer`](#wx.dataview.DataViewEvent.SetDataBuffer "wx.dataview.DataViewEvent.SetDataBuffer")
    DataFormat: '_DataFormat'  # `DataFormat`[¶](#wx.dataview.DataViewEvent.DataFormat "Permalink to this definition")See [`GetDataFormat`](#wx.dataview.DataViewEvent.GetDataFormat "wx.dataview.DataViewEvent.GetDataFormat") and [`SetDataFormat`](#wx.dataview.DataViewEvent.SetDataFormat "wx.dataview.DataViewEvent.SetDataFormat")
    DataObject: '_DataObject'  # `DataObject`[¶](#wx.dataview.DataViewEvent.DataObject "Permalink to this definition")See [`GetDataObject`](#wx.dataview.DataViewEvent.GetDataObject "wx.dataview.DataViewEvent.GetDataObject") and [`SetDataObject`](#wx.dataview.DataViewEvent.SetDataObject "wx.dataview.DataViewEvent.SetDataObject")
    DataSize: int  # `DataSize`[¶](#wx.dataview.DataViewEvent.DataSize "Permalink to this definition")See [`GetDataSize`](#wx.dataview.DataViewEvent.GetDataSize "wx.dataview.DataViewEvent.GetDataSize") and [`SetDataSize`](#wx.dataview.DataViewEvent.SetDataSize "wx.dataview.DataViewEvent.SetDataSize")
    DataViewColumn: 'DataViewColumn'  # `DataViewColumn`[¶](#wx.dataview.DataViewEvent.DataViewColumn "Permalink to this definition")See [`GetDataViewColumn`](#wx.dataview.DataViewEvent.GetDataViewColumn "wx.dataview.DataViewEvent.GetDataViewColumn") and [`SetDataViewColumn`](#wx.dataview.DataViewEvent.SetDataViewColumn "wx.dataview.DataViewEvent.SetDataViewColumn")
    DragFlags: int  # `DragFlags`[¶](#wx.dataview.DataViewEvent.DragFlags "Permalink to this definition")See [`GetDragFlags`](#wx.dataview.DataViewEvent.GetDragFlags "wx.dataview.DataViewEvent.GetDragFlags") and [`SetDragFlags`](#wx.dataview.DataViewEvent.SetDragFlags "wx.dataview.DataViewEvent.SetDragFlags")
    DropEffect: 'DragResult'  # `DropEffect`[¶](#wx.dataview.DataViewEvent.DropEffect "Permalink to this definition")See [`GetDropEffect`](#wx.dataview.DataViewEvent.GetDropEffect "wx.dataview.DataViewEvent.GetDropEffect") and [`SetDropEffect`](#wx.dataview.DataViewEvent.SetDropEffect "wx.dataview.DataViewEvent.SetDropEffect")
    Item: 'DataViewItem'  # `Item`[¶](#wx.dataview.DataViewEvent.Item "Permalink to this definition")See [`GetItem`](#wx.dataview.DataViewEvent.GetItem "wx.dataview.DataViewEvent.GetItem") and [`SetItem`](#wx.dataview.DataViewEvent.SetItem "wx.dataview.DataViewEvent.SetItem")
    Model: 'DataViewModel'  # `Model`[¶](#wx.dataview.DataViewEvent.Model "Permalink to this definition")See [`GetModel`](#wx.dataview.DataViewEvent.GetModel "wx.dataview.DataViewEvent.GetModel") and [`SetModel`](#wx.dataview.DataViewEvent.SetModel "wx.dataview.DataViewEvent.SetModel")
    Position: 'Point'  # `Position`[¶](#wx.dataview.DataViewEvent.Position "Permalink to this definition")See [`GetPosition`](#wx.dataview.DataViewEvent.GetPosition "wx.dataview.DataViewEvent.GetPosition") and [`SetPosition`](#wx.dataview.DataViewEvent.SetPosition "wx.dataview.DataViewEvent.SetPosition")
    ProposedDropIndex: int  # `ProposedDropIndex`[¶](#wx.dataview.DataViewEvent.ProposedDropIndex "Permalink to this definition")See [`GetProposedDropIndex`](#wx.dataview.DataViewEvent.GetProposedDropIndex "wx.dataview.DataViewEvent.GetProposedDropIndex")
    Value: 'DVCVariant'  # `Value`[¶](#wx.dataview.DataViewEvent.Value "Permalink to this definition")See [`GetValue`](#wx.dataview.DataViewEvent.GetValue "wx.dataview.DataViewEvent.GetValue") and [`SetValue`](#wx.dataview.DataViewEvent.SetValue "wx.dataview.DataViewEvent.SetValue")



EVT_DATAVIEW_CACHE_HINT: int  # Process a  wxEVT_DATAVIEW_CACHE_HINT   event. ^^

DataViewCellMode: TypeAlias = int  # Enumeration

DATAVIEW_CELL_INERT: int

class DataViewIconTextRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewIconTextRenderer(varianttype=DataViewIconTextRenderer.GetDefault
                         Type(), mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


The DataViewIconTextRenderer class is used to display text with a
small icon next to it as it is typically done in a file manager.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewIconTextRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewIconTextRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewIconTextRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewIconTextRenderer.html
        """



class TreeListEvent(NotifyEvent):
    """ **Possible constructors**:



```
TreeListEvent()

```


Event generated by TreeListCtrl.


  


        Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.TreeListEvent.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetColumn(self) -> None:
        """ 

`GetColumn`(*self*)[¶](#wx.dataview.TreeListEvent.GetColumn "Permalink to this definition")
Return the column affected by the event.


This is currently only used with `wxEVT_TREELIST_COLUMN_SORTED` event.




            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetItem(self) -> 'TreeListItem':
        """ 

`GetItem`(*self*)[¶](#wx.dataview.TreeListEvent.GetItem "Permalink to this definition")
Return the item affected by the event.


This is the item being selected, expanded, checked or activated (depending on the event type).



Return type
 [wx.dataview.TreeListItem](wx.dataview.TreeListItem.html#wx-dataview-treelistitem)






            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    def GetOldCheckedState(self) -> 'CheckBoxState':
        """ 

`GetOldCheckedState`(*self*)[¶](#wx.dataview.TreeListEvent.GetOldCheckedState "Permalink to this definition")
Return the previous state of the item checkbox.


This method can be used with `wxEVT_TREELIST_ITEM_CHECKED` events only.


Notice that the new state of the item can be retrieved using [`wx.dataview.TreeListCtrl.GetCheckedState`](wx.dataview.TreeListCtrl.html#wx.dataview.TreeListCtrl.GetCheckedState "wx.dataview.TreeListCtrl.GetCheckedState") .



Return type
 [wx.CheckBoxState](wx.CheckBoxState.enumeration.html#wx-checkboxstate)






            Source: https://docs.wxpython.org/wx.dataview.TreeListEvent.html
        """

    Column: None  # `Column`[¶](#wx.dataview.TreeListEvent.Column "Permalink to this definition")See [`GetColumn`](#wx.dataview.TreeListEvent.GetColumn "wx.dataview.TreeListEvent.GetColumn")
    Item: 'TreeListItem'  # `Item`[¶](#wx.dataview.TreeListEvent.Item "Permalink to this definition")See [`GetItem`](#wx.dataview.TreeListEvent.GetItem "wx.dataview.TreeListEvent.GetItem")
    OldCheckedState: 'CheckBoxState'  # `OldCheckedState`[¶](#wx.dataview.TreeListEvent.OldCheckedState "Permalink to this definition")See [`GetOldCheckedState`](#wx.dataview.TreeListEvent.GetOldCheckedState "wx.dataview.TreeListEvent.GetOldCheckedState")



class DataViewIconText(Object):
    """ **Possible constructors**:



```
DataViewIconText(text="", bitmap=BitmapBundle())

DataViewIconText(other)

```


DataViewIconText is used by DataViewIconTextRenderer for data
transfer.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.dataview.DataViewIconText.__init__ "Permalink to this definition")
Constructor.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, text=””, bitmap=BitmapBundle())*



Parameters
* **text** (*string*) –
* **bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






---

  



**\_\_init\_\_** *(self, other)*



Parameters
**other** ([*wx.dataview.DataViewIconText*](#wx.dataview.DataViewIconText "wx.dataview.DataViewIconText")) – 






---

  





            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetBitmapBundle(self) -> 'BitmapBundle':
        """ 

`GetBitmapBundle`(*self*)[¶](#wx.dataview.DataViewIconText.GetBitmapBundle "Permalink to this definition")
Gets the associated image.



Return type
[`BitmapBundle`](#wx.dataview.DataViewIconText.BitmapBundle "wx.dataview.DataViewIconText.BitmapBundle")





New in version 4.1/wxWidgets-3.1.6.





            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetIcon(self) -> 'Icon':
        """ 

`GetIcon`(*self*)[¶](#wx.dataview.DataViewIconText.GetIcon "Permalink to this definition")
Gets the icon.


This function can only return the icon in the size appropriate for the standard 100% `DPI` scaling, use [`GetBitmapBundle`](#wx.dataview.DataViewIconText.GetBitmapBundle "wx.dataview.DataViewIconText.GetBitmapBundle") to retrieve image representation suitable for another `DPI` scaling value.



Return type
[`Icon`](#wx.dataview.DataViewIconText.Icon "wx.dataview.DataViewIconText.Icon")






            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.dataview.DataViewIconText.GetText "Permalink to this definition")
Gets the text.



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetBitmapBundle(self, bitmap: 'BitmapBundle') -> None:
        """ 

`SetBitmapBundle`(*self*, *bitmap*)[¶](#wx.dataview.DataViewIconText.SetBitmapBundle "Permalink to this definition")
Sets the associated image.


This function allows to provide several representations of the same image, so that the most appropriate one for the current `DPI` scaling could be used, and so should be preferred to [`SetIcon`](#wx.dataview.DataViewIconText.SetIcon "wx.dataview.DataViewIconText.SetIcon") .



Parameters
**bitmap** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) – 





New in version 4.1/wxWidgets-3.1.6.





            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetIcon(self, icon: 'Icon') -> None:
        """ 

`SetIcon`(*self*, *icon*)[¶](#wx.dataview.DataViewIconText.SetIcon "Permalink to this definition")
Set the icon.


Use [`SetBitmapBundle`](#wx.dataview.DataViewIconText.SetBitmapBundle "wx.dataview.DataViewIconText.SetBitmapBundle") instead to allow specifying different image representations for different `DPI` scaling values.



Parameters
**icon** ([*wx.Icon*](wx.Icon.html#wx.Icon "wx.Icon")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.dataview.DataViewIconText.SetText "Permalink to this definition")
Set the text.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIconText.html
        """

    BitmapBundle: '_BitmapBundle'  # `BitmapBundle`[¶](#wx.dataview.DataViewIconText.BitmapBundle "Permalink to this definition")See [`GetBitmapBundle`](#wx.dataview.DataViewIconText.GetBitmapBundle "wx.dataview.DataViewIconText.GetBitmapBundle") and [`SetBitmapBundle`](#wx.dataview.DataViewIconText.SetBitmapBundle "wx.dataview.DataViewIconText.SetBitmapBundle")
    Icon: '_Icon'  # `Icon`[¶](#wx.dataview.DataViewIconText.Icon "Permalink to this definition")See [`GetIcon`](#wx.dataview.DataViewIconText.GetIcon "wx.dataview.DataViewIconText.GetIcon") and [`SetIcon`](#wx.dataview.DataViewIconText.SetIcon "wx.dataview.DataViewIconText.SetIcon")
    Text: str  # `Text`[¶](#wx.dataview.DataViewIconText.Text "Permalink to this definition")See [`GetText`](#wx.dataview.DataViewIconText.GetText "wx.dataview.DataViewIconText.GetText") and [`SetText`](#wx.dataview.DataViewIconText.SetText "wx.dataview.DataViewIconText.SetText")



class TreeListItem:
    """ **Possible constructors**:



```
TreeListItem()

```


Unique identifier of an item in TreeListCtrl.


  


        Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.TreeListItem.__init__ "Permalink to this definition")
Only the default constructor is publicly accessible.


Default constructing a  [wx.dataview.TreeListItem](#wx-dataview-treelistitem) creates an invalid item.




            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.dataview.TreeListItem.IsOk "Permalink to this definition")
Return `True` if the item is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.dataview.TreeListItem.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*, *other*)[¶](#wx.dataview.TreeListItem.__eq__ "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __hash__(self) -> int:
        """ 

`__hash__`(*self*)[¶](#wx.dataview.TreeListItem.__hash__ "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __ne__(self, item: Any) -> bool:
        """ 

`__ne__`(*self*, *other*)[¶](#wx.dataview.TreeListItem.__ne__ "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.dataview.TreeListItem.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.TreeListItem.html
        """



class TreeListItemComparator:
    """ **Possible constructors**:



```
TreeListItemComparator()

```


Class defining sort order for the items in TreeListCtrl.


  


        Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.TreeListItemComparator.__init__ "Permalink to this definition")
Default constructor.


Notice that this class is not copiable, comparators are not passed by value.




            Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
        """

    def Compare(self, treelist, column, first, second) -> int:
        """ 

`Compare`(*self*, *treelist*, *column*, *first*, *second*)[¶](#wx.dataview.TreeListItemComparator.Compare "Permalink to this definition")
Pure virtual function which must be overridden to define sort order.


The comparison function should return negative, null or positive value depending on whether the first item is less than, equal to or greater than the second one. The items should be compared using their values for the given column.



Parameters
* **treelist** ([*wx.dataview.TreeListCtrl*](wx.dataview.TreeListCtrl.html#wx.dataview.TreeListCtrl "wx.dataview.TreeListCtrl")) – The control whose contents is being sorted.
* **column** – The column of this control used for sorting.
* **first** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – First item to compare.
* **second** ([*wx.dataview.TreeListItem*](wx.dataview.TreeListItem.html#wx.dataview.TreeListItem "wx.dataview.TreeListItem")) – Second item to compare.



Return type
*int*



Returns
A negative value if the first item is less than (i.e. should appear above) the second one, zero if the two items are equal or a positive value if the first item is greater than (i.e. should appear below) the second one.






            Source: https://docs.wxpython.org/wx.dataview.TreeListItemComparator.html
        """



class DataViewTreeStore(DataViewModel):
    """ **Possible constructors**:



```
DataViewTreeStore()

```


DataViewTreeStore is a specialised DataViewModel for storing
simple trees very much like TreeCtrl does and it offers a similar
API.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.DataViewTreeStore.__init__ "Permalink to this definition")
Constructor.


Creates the invisible root node internally.




            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def AppendContainer(*args, **kwargs) -> 'DataViewItem':
        """ 

`AppendContainer`(*self*, *parent*, *text*, *icon=BitmapBundle()*, *expanded=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.AppendContainer "Permalink to this definition")
Append a container.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **expanded** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def AppendItem(*args, **kwargs) -> 'DataViewItem':
        """ 

`AppendItem`(*self*, *parent*, *text*, *icon=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.AppendItem "Permalink to this definition")
Append an item.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.dataview.DataViewTreeStore.DeleteAllItems "Permalink to this definition")
Delete all item in the model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteChildren(self, item: 'dataview.DataViewItem') -> None:
        """ 

`DeleteChildren`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.DeleteChildren "Permalink to this definition")
Delete all children of the item, but not the item itself.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def DeleteItem(self, item: 'dataview.DataViewItem') -> None:
        """ 

`DeleteItem`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.DeleteItem "Permalink to this definition")
Delete this item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetChildCount(self, parent: 'dataview.DataViewItem') -> int:
        """ 

`GetChildCount`(*self*, *parent*)[¶](#wx.dataview.DataViewTreeStore.GetChildCount "Permalink to this definition")
Return the number of children of item.



Parameters
**parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemData(self, item: 'dataview.DataViewItem') -> 'ClientData':
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.GetItemData "Permalink to this definition")
Returns the client data associated with the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*ClientData*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemExpandedIcon(self, item: 'dataview.DataViewItem') -> 'Icon':
        """ 

`GetItemExpandedIcon`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.GetItemExpandedIcon "Permalink to this definition")
Returns the icon to display in expanded containers.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*Icon*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemIcon(self, item: 'dataview.DataViewItem') -> 'Icon':
        """ 

`GetItemIcon`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.GetItemIcon "Permalink to this definition")
Returns the icon of the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*Icon*






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetItemText(self, item: 'dataview.DataViewItem') -> str:
        """ 

`GetItemText`(*self*, *item*)[¶](#wx.dataview.DataViewTreeStore.GetItemText "Permalink to this definition")
Returns the text of the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def GetNthChild(self, parent, pos) -> 'DataViewItem':
        """ 

`GetNthChild`(*self*, *parent*, *pos*)[¶](#wx.dataview.DataViewTreeStore.GetNthChild "Permalink to this definition")
Returns the nth child item of item.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **pos** (*int*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def InsertContainer(*args, **kwargs) -> 'DataViewItem':
        """ 

`InsertContainer`(*self*, *parent*, *previous*, *text*, *icon=BitmapBundle()*, *expanded=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.InsertContainer "Permalink to this definition")
Inserts a container after *previous*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **previous** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **expanded** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def InsertItem(*args, **kwargs) -> 'DataViewItem':
        """ 

`InsertItem`(*self*, *parent*, *previous*, *text*, *icon=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.InsertItem "Permalink to this definition")
Inserts an item after *previous*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **previous** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def PrependContainer(*args, **kwargs) -> 'DataViewItem':
        """ 

`PrependContainer`(*self*, *parent*, *text*, *icon=BitmapBundle()*, *expanded=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.PrependContainer "Permalink to this definition")
Inserts a container before the first child item or *parent*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **expanded** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def PrependItem(*args, **kwargs) -> 'DataViewItem':
        """ 

`PrependItem`(*self*, *parent*, *text*, *icon=BitmapBundle()*, *data=None*)[¶](#wx.dataview.DataViewTreeStore.PrependItem "Permalink to this definition")
Inserts an item before the first child item or *parent*.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **text** (*string*) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –
* **data** (*ClientData*) –



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.dataview.DataViewTreeStore.SetItemData "Permalink to this definition")
Sets the client data associated with the item.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **data** (*ClientData*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemExpandedIcon(self, item, icon) -> None:
        """ 

`SetItemExpandedIcon`(*self*, *item*, *icon*)[¶](#wx.dataview.DataViewTreeStore.SetItemExpandedIcon "Permalink to this definition")
Sets the expanded icon for the item.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """

    def SetItemIcon(self, item, icon) -> None:
        """ 

`SetItemIcon`(*self*, *item*, *icon*)[¶](#wx.dataview.DataViewTreeStore.SetItemIcon "Permalink to this definition")
Sets the icon for the item.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **icon** ([*wx.BitmapBundle*](wx.BitmapBundle.html#wx.BitmapBundle "wx.BitmapBundle")) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTreeStore.html
        """



class DataViewListStore(DataViewIndexListModel):
    """ **Possible constructors**:



```
DataViewListStore()

```


DataViewListStore is a specialised DataViewModel for storing a
simple table of data.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.DataViewListStore.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def AppendColumn(self, varianttype: str) -> None:
        """ 

`AppendColumn`(*self*, *varianttype*)[¶](#wx.dataview.DataViewListStore.AppendColumn "Permalink to this definition")
Appends a data column.


*variantype* indicates the type of values store in the column.


This does not automatically fill in any (default) values in rows which exist in the store already.



Parameters
**varianttype** (*string*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def AppendItem(self, values, data=None) -> None:
        """ 

`AppendItem`(*self*, *values*, *data=None*)[¶](#wx.dataview.DataViewListStore.AppendItem "Permalink to this definition")
Appends an item (=row) and fills it with *values*.


The values must match the values specifies in the column in number and type. No (default) values are filled in automatically.



Parameters
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def DeleteAllItems(self) -> None:
        """ 

`DeleteAllItems`(*self*)[¶](#wx.dataview.DataViewListStore.DeleteAllItems "Permalink to this definition")
Delete all item (=all rows) in the store.




            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def DeleteItem(self, pos: Any) -> None:
        """ 

`DeleteItem`(*self*, *pos*)[¶](#wx.dataview.DataViewListStore.DeleteItem "Permalink to this definition")
Delete the item (=row) at position *pos*.



Parameters
**pos** – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetItemCount(self) -> int:
        """ 

`GetItemCount`(*self*)[¶](#wx.dataview.DataViewListStore.GetItemCount "Permalink to this definition")
Returns the number of items (=rows) in the control.



Return type
*int*





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetItemData(self, item: 'dataview.DataViewItem') -> int:
        """ 

`GetItemData`(*self*, *item*)[¶](#wx.dataview.DataViewListStore.GetItemData "Permalink to this definition")
Returns the client data associated with the item.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*wx.UIntPtr*





New in version 2.9.4.




See also


[`SetItemData`](#wx.dataview.DataViewListStore.SetItemData "wx.dataview.DataViewListStore.SetItemData")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def GetValueByRow(self, row, col) -> Any:
        """ 

`GetValueByRow`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListStore.GetValueByRow "Permalink to this definition")
Overridden from  [wx.dataview.DataViewIndexListModel](wx.dataview.DataViewIndexListModel.html#wx-dataview-dataviewindexlistmodel).



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*value*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def InsertColumn(self, pos, varianttype) -> None:
        """ 

`InsertColumn`(*self*, *pos*, *varianttype*)[¶](#wx.dataview.DataViewListStore.InsertColumn "Permalink to this definition")
Inserts a data column before *pos*.


*variantype* indicates the type of values store in the column.


This does not automatically fill in any (default) values in rows which exist in the store already.



Parameters
* **pos** (*int*) –
* **varianttype** (*string*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def InsertItem(self, row, values, data=None) -> None:
        """ 

`InsertItem`(*self*, *row*, *values*, *data=None*)[¶](#wx.dataview.DataViewListStore.InsertItem "Permalink to this definition")
Inserts an item (=row) and fills it with *values*.


The values must match the values specifies in the column in number and type. No (default) values are filled in automatically.



Parameters
* **row** (*int*) –
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def PrependColumn(self, varianttype: str) -> None:
        """ 

`PrependColumn`(*self*, *varianttype*)[¶](#wx.dataview.DataViewListStore.PrependColumn "Permalink to this definition")
Prepends a data column.


*variantype* indicates the type of values store in the column.


This does not automatically fill in any (default) values in rows which exist in the store already.



Parameters
**varianttype** (*string*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def PrependItem(self, values, data=None) -> None:
        """ 

`PrependItem`(*self*, *values*, *data=None*)[¶](#wx.dataview.DataViewListStore.PrependItem "Permalink to this definition")
Prepends an item (=row) and fills it with *values*.


The values must match the values specifies in the column in number and type. No (default) values are filled in automatically.



Parameters
* **values** (`VariantVector`) –
* **data** (*wx.UIntPtr*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def SetItemData(self, item, data) -> None:
        """ 

`SetItemData`(*self*, *item*, *data*)[¶](#wx.dataview.DataViewListStore.SetItemData "Permalink to this definition")
Sets the client data associated with the item.


Notice that this class does *not* take ownership of the passed in pointer and will not delete it.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **data** (*wx.UIntPtr*) –





New in version 2.9.4.




See also


[`GetItemData`](#wx.dataview.DataViewListStore.GetItemData "wx.dataview.DataViewListStore.GetItemData")





            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    def SetValueByRow(self, value, row, col) -> bool:
        """ 

`SetValueByRow`(*self*, *value*, *row*, *col*)[¶](#wx.dataview.DataViewListStore.SetValueByRow "Permalink to this definition")
Overridden from  [wx.dataview.DataViewIndexListModel](wx.dataview.DataViewIndexListModel.html#wx-dataview-dataviewindexlistmodel).



Parameters
* **value** (*DVCVariant*) –
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListStore.html
        """

    ItemCount: int  # `ItemCount`[¶](#wx.dataview.DataViewListStore.ItemCount "Permalink to this definition")See [`GetItemCount`](#wx.dataview.DataViewListStore.GetItemCount "wx.dataview.DataViewListStore.GetItemCount")



class DataViewModelNotifier:
    """ **Possible constructors**:



```
DataViewModelNotifier()

```


A DataViewModelNotifier instance is owned by a DataViewModel and
mirrors its notification interface.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.DataViewModelNotifier.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def Cleared(self) -> bool:
        """ 

`Cleared`(*self*)[¶](#wx.dataview.DataViewModelNotifier.Cleared "Permalink to this definition")
Called by owning model.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def GetOwner(self) -> 'DataViewModel':
        """ 

`GetOwner`(*self*)[¶](#wx.dataview.DataViewModelNotifier.GetOwner "Permalink to this definition")
Get owning  [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel).



Return type
 [wx.dataview.DataViewModel](wx.dataview.DataViewModel.html#wx-dataview-dataviewmodel)






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemAdded(self, parent, item) -> bool:
        """ 

`ItemAdded`(*self*, *parent*, *item*)[¶](#wx.dataview.DataViewModelNotifier.ItemAdded "Permalink to this definition")
Called by owning model.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemChanged(self, item: 'dataview.DataViewItem') -> bool:
        """ 

`ItemChanged`(*self*, *item*)[¶](#wx.dataview.DataViewModelNotifier.ItemChanged "Permalink to this definition")
Called by owning model.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemDeleted(self, parent, item) -> bool:
        """ 

`ItemDeleted`(*self*, *parent*, *item*)[¶](#wx.dataview.DataViewModelNotifier.ItemDeleted "Permalink to this definition")
Called by owning model.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsAdded(self, parent, items) -> bool:
        """ 

`ItemsAdded`(*self*, *parent*, *items*)[¶](#wx.dataview.DataViewModelNotifier.ItemsAdded "Permalink to this definition")
Called by owning model.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **items** (*DataViewItemArray*) –



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsChanged(self, items: DataViewItemArray) -> bool:
        """ 

`ItemsChanged`(*self*, *items*)[¶](#wx.dataview.DataViewModelNotifier.ItemsChanged "Permalink to this definition")
Called by owning model.



Parameters
**items** (*DataViewItemArray*) – 



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ItemsDeleted(self, parent, items) -> bool:
        """ 

`ItemsDeleted`(*self*, *parent*, *items*)[¶](#wx.dataview.DataViewModelNotifier.ItemsDeleted "Permalink to this definition")
Called by owning model.



Parameters
* **parent** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **items** (*DataViewItemArray*) –



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def Resort(self) -> None:
        """ 

`Resort`(*self*)[¶](#wx.dataview.DataViewModelNotifier.Resort "Permalink to this definition")
Called by owning model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def SetOwner(self, owner: 'dataview.DataViewModel') -> None:
        """ 

`SetOwner`(*self*, *owner*)[¶](#wx.dataview.DataViewModelNotifier.SetOwner "Permalink to this definition")
Set owner of this notifier.


Used internally.



Parameters
**owner** ([*wx.dataview.DataViewModel*](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel "wx.dataview.DataViewModel")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    def ValueChanged(self, item, col) -> bool:
        """ 

`ValueChanged`(*self*, *item*, *col*)[¶](#wx.dataview.DataViewModelNotifier.ValueChanged "Permalink to this definition")
Called by owning model.



Parameters
* **item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **col** (*int*) –



Return type
*bool*



Returns
Always return `True` from this function in derived classes.






            Source: https://docs.wxpython.org/wx.dataview.DataViewModelNotifier.html
        """

    Owner: 'DataViewModel'  # `Owner`[¶](#wx.dataview.DataViewModelNotifier.Owner "Permalink to this definition")See [`GetOwner`](#wx.dataview.DataViewModelNotifier.GetOwner "wx.dataview.DataViewModelNotifier.GetOwner") and [`SetOwner`](#wx.dataview.DataViewModelNotifier.SetOwner "wx.dataview.DataViewModelNotifier.SetOwner")



class DataViewIndexListModel(DataViewListModel):
    """ **Possible constructors**:



```
DataViewIndexListModel(initial_size=0)

```


DataViewIndexListModel is a specialized data model which lets you
address an item by its position (row) rather than its DataViewItem
(which you can obtain from this class).


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
    """
    def __init__(self, initial_size: int=0) -> None:
        """ 

`__init__`(*self*, *initial\_size=0*)[¶](#wx.dataview.DataViewIndexListModel.__init__ "Permalink to this definition")
Constructor.



Parameters
**initial\_size** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def GetItem(self, row: int) -> 'DataViewItem':
        """ 

`GetItem`(*self*, *row*)[¶](#wx.dataview.DataViewIndexListModel.GetItem "Permalink to this definition")
Returns the  [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem) at the given *row*.



Parameters
**row** (*int*) – 



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def Reset(self, new_size: int) -> None:
        """ 

`Reset`(*self*, *new\_size*)[¶](#wx.dataview.DataViewIndexListModel.Reset "Permalink to this definition")
Call this after if the data has to be read again from the model.


This is useful after major changes when calling the methods below (possibly thousands of times) doesn’t make sense.



Parameters
**new\_size** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowAppended(self) -> None:
        """ 

`RowAppended`(*self*)[¶](#wx.dataview.DataViewIndexListModel.RowAppended "Permalink to this definition")
Call this after a row has been appended to the model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowChanged(self, row: int) -> None:
        """ 

`RowChanged`(*self*, *row*)[¶](#wx.dataview.DataViewIndexListModel.RowChanged "Permalink to this definition")
Call this after a row has been changed.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowDeleted(self, row: int) -> None:
        """ 

`RowDeleted`(*self*, *row*)[¶](#wx.dataview.DataViewIndexListModel.RowDeleted "Permalink to this definition")
Call this after a row has been deleted.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowInserted(self, before: int) -> None:
        """ 

`RowInserted`(*self*, *before*)[¶](#wx.dataview.DataViewIndexListModel.RowInserted "Permalink to this definition")
Call this after a row has been inserted at the given position.



Parameters
**before** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowPrepended(self) -> None:
        """ 

`RowPrepended`(*self*)[¶](#wx.dataview.DataViewIndexListModel.RowPrepended "Permalink to this definition")
Call this after a row has been prepended to the model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowValueChanged(self, row, col) -> None:
        """ 

`RowValueChanged`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewIndexListModel.RowValueChanged "Permalink to this definition")
Call this after a value has been changed.



Parameters
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """

    def RowsDeleted(self, rows: int) -> None:
        """ 

`RowsDeleted`(*self*, *rows*)[¶](#wx.dataview.DataViewIndexListModel.RowsDeleted "Permalink to this definition")
Call this after rows have been deleted.


The array will internally get copied and sorted in descending order so that the rows with the highest position will be deleted first.



Parameters
**rows** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewIndexListModel.html
        """



class DataViewVirtualListModel(DataViewListModel):
    """ **Possible constructors**:



```
DataViewVirtualListModel(initial_size=0)

```


DataViewVirtualListModel is a specialized data model which lets you
address an item by its position (row) rather than its DataViewItem
and as such offers the exact same interface as
DataViewIndexListModel.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
    """
    def __init__(self, initial_size: int=0) -> None:
        """ 

`__init__`(*self*, *initial\_size=0*)[¶](#wx.dataview.DataViewVirtualListModel.__init__ "Permalink to this definition")
Constructor.



Parameters
**initial\_size** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def GetItem(self, row: int) -> 'DataViewItem':
        """ 

`GetItem`(*self*, *row*)[¶](#wx.dataview.DataViewVirtualListModel.GetItem "Permalink to this definition")
Returns the  [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem) at the given *row*.



Parameters
**row** (*int*) – 



Return type
 [wx.dataview.DataViewItem](wx.dataview.DataViewItem.html#wx-dataview-dataviewitem)






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def Reset(self, new_size: int) -> None:
        """ 

`Reset`(*self*, *new\_size*)[¶](#wx.dataview.DataViewVirtualListModel.Reset "Permalink to this definition")
Call this after if the data has to be read again from the model.


This is useful after major changes when calling the methods below (possibly thousands of times) doesn’t make sense.



Parameters
**new\_size** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowAppended(self) -> None:
        """ 

`RowAppended`(*self*)[¶](#wx.dataview.DataViewVirtualListModel.RowAppended "Permalink to this definition")
Call this after a row has been appended to the model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowChanged(self, row: int) -> None:
        """ 

`RowChanged`(*self*, *row*)[¶](#wx.dataview.DataViewVirtualListModel.RowChanged "Permalink to this definition")
Call this after a row has been changed.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowDeleted(self, row: int) -> None:
        """ 

`RowDeleted`(*self*, *row*)[¶](#wx.dataview.DataViewVirtualListModel.RowDeleted "Permalink to this definition")
Call this after a row has been deleted.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowInserted(self, before: int) -> None:
        """ 

`RowInserted`(*self*, *before*)[¶](#wx.dataview.DataViewVirtualListModel.RowInserted "Permalink to this definition")
Call this after a row has been inserted at the given position.



Parameters
**before** (*int*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowPrepended(self) -> None:
        """ 

`RowPrepended`(*self*)[¶](#wx.dataview.DataViewVirtualListModel.RowPrepended "Permalink to this definition")
Call this after a row has been prepended to the model.




            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowValueChanged(self, row, col) -> None:
        """ 

`RowValueChanged`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewVirtualListModel.RowValueChanged "Permalink to this definition")
Call this after a value has been changed.



Parameters
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """

    def RowsDeleted(self, rows: int) -> None:
        """ 

`RowsDeleted`(*self*, *rows*)[¶](#wx.dataview.DataViewVirtualListModel.RowsDeleted "Permalink to this definition")
Call this after rows have been deleted.


The array will internally get copied and sorted in descending order so that the rows with the highest position will be deleted first.



Parameters
**rows** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewVirtualListModel.html
        """



class DataViewListModel(DataViewModel):
    """ Base class with abstract API for DataViewIndexListModel and
DataViewVirtualListModel.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
    """
    def Compare(self, item1, item2, column, ascending) -> int:
        """ 

`Compare`(*self*, *item1*, *item2*, *column*, *ascending*)[¶](#wx.dataview.DataViewListModel.Compare "Permalink to this definition")
Compare method that sorts the items by their index.



Parameters
* **item1** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **item2** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) –
* **column** (*int*) –
* **ascending** (*bool*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetAttrByRow(self, row, col, attr) -> bool:
        """ 

`GetAttrByRow`(*self*, *row*, *col*, *attr*)[¶](#wx.dataview.DataViewListModel.GetAttrByRow "Permalink to this definition")
Override this to indicate that the row has special font attributes.


This only affects the DataViewTextRendererText() renderer.


The base class version always simply returns `False`.



Parameters
* **row** (*int*) – The row for which the attribute is requested.
* **col** (*int*) – The column for which the attribute is requested.
* **attr** ([*wx.dataview.DataViewItemAttr*](wx.dataview.DataViewItemAttr.html#wx.dataview.DataViewItemAttr "wx.dataview.DataViewItemAttr")) – The attribute to be filled in if the function returns `True`.



Return type
*bool*



Returns
`True` if this item has an attribute or `False` otherwise.





See also


 [wx.dataview.DataViewItemAttr](wx.dataview.DataViewItemAttr.html#wx-dataview-dataviewitemattr).





            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.dataview.DataViewListModel.GetCount "Permalink to this definition")
Returns the number of items (or rows) in the list.



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetRow(self, item: 'dataview.DataViewItem') -> int:
        """ 

`GetRow`(*self*, *item*)[¶](#wx.dataview.DataViewListModel.GetRow "Permalink to this definition")
Returns the position of given *item*.



Parameters
**item** ([*wx.dataview.DataViewItem*](wx.dataview.DataViewItem.html#wx.dataview.DataViewItem "wx.dataview.DataViewItem")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def GetValueByRow(self, row, col) -> Any:
        """ 

`GetValueByRow`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListModel.GetValueByRow "Permalink to this definition")
Override this to allow getting values from the model.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*variant*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def IsEnabledByRow(self, row, col) -> bool:
        """ 

`IsEnabledByRow`(*self*, *row*, *col*)[¶](#wx.dataview.DataViewListModel.IsEnabledByRow "Permalink to this definition")
Override this if you want to disable specific items.


The base class version always returns `True`, thus making all items enabled by default.



Parameters
* **row** (*int*) – The row of the item whose enabled status is requested.
* **col** (*int*) – The column of the item whose enabled status is requested.



Return type
*bool*



Returns
`True` if the item at this row and column should be enabled, `False` otherwise.





New in version 2.9.2.




Note


See [`wx.dataview.DataViewModel.IsEnabled`](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel.IsEnabled "wx.dataview.DataViewModel.IsEnabled") for the current status of support for disabling the items under different platforms.





            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    def SetValueByRow(self, variant, row, col) -> bool:
        """ 

`SetValueByRow`(*self*, *variant*, *row*, *col*)[¶](#wx.dataview.DataViewListModel.SetValueByRow "Permalink to this definition")
Called in order to set a value in the model.



Parameters
* **variant** (*DVCVariant*) –
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewListModel.html
        """

    Count: int  # `Count`[¶](#wx.dataview.DataViewListModel.Count "Permalink to this definition")See [`GetCount`](#wx.dataview.DataViewListModel.GetCount "wx.dataview.DataViewListModel.GetCount")



class DataViewItemAttr:
    """ **Possible constructors**:



```
DataViewItemAttr()

```


This class is used to indicate to a DataViewCtrl that a certain item
(see DataViewItem) has extra font attributes for its renderer.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.dataview.DataViewItemAttr.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.dataview.DataViewItemAttr.GetBackgroundColour "Permalink to this definition")
Returns the colour to be used for the background.



Return type
[`Colour`](#wx.dataview.DataViewItemAttr.Colour "wx.dataview.DataViewItemAttr.Colour")






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetBold(self) -> bool:
        """ 

`GetBold`(*self*)[¶](#wx.dataview.DataViewItemAttr.GetBold "Permalink to this definition")
Returns value of the bold property.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetColour(self) -> 'Colour':
        """ 

`GetColour`(*self*)[¶](#wx.dataview.DataViewItemAttr.GetColour "Permalink to this definition")
Returns this attribute’s colour.



Return type
[`Colour`](#wx.dataview.DataViewItemAttr.Colour "wx.dataview.DataViewItemAttr.Colour")






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetEffectiveFont(self, font: 'Font') -> 'Font':
        """ 

`GetEffectiveFont`(*self*, *font*)[¶](#wx.dataview.DataViewItemAttr.GetEffectiveFont "Permalink to this definition")
Return the font based on the given one with this attribute applied to it.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def GetItalic(self) -> bool:
        """ 

`GetItalic`(*self*)[¶](#wx.dataview.DataViewItemAttr.GetItalic "Permalink to this definition")
Returns value of the italics property.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasBackgroundColour(self) -> bool:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.dataview.DataViewItemAttr.HasBackgroundColour "Permalink to this definition")
Returns `True` if the background colour property has been set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasColour(self) -> bool:
        """ 

`HasColour`(*self*)[¶](#wx.dataview.DataViewItemAttr.HasColour "Permalink to this definition")
Returns `True` if the colour property has been set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def HasFont(self) -> bool:
        """ 

`HasFont`(*self*)[¶](#wx.dataview.DataViewItemAttr.HasFont "Permalink to this definition")
Returns `True` if any property affecting the font has been set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def IsDefault(self) -> bool:
        """ 

`IsDefault`(*self*)[¶](#wx.dataview.DataViewItemAttr.IsDefault "Permalink to this definition")
Returns `True` if none of the properties have been set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.dataview.DataViewItemAttr.SetBackgroundColour "Permalink to this definition")
Call this to set the background colour to use.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 





New in version 2.9.4: - Generic




New in version 4.1/wxWidgets-3.1.1: - wxGTK




New in version 4.1/wxWidgets-3.1.4: - wxOSX





            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetBold(self, set: bool) -> None:
        """ 

`SetBold`(*self*, *set*)[¶](#wx.dataview.DataViewItemAttr.SetBold "Permalink to this definition")
Call this to indicate that the item shall be displayed in bold text.



Parameters
**set** (*bool*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.dataview.DataViewItemAttr.SetColour "Permalink to this definition")
Call this to indicate that the item shall be displayed with that colour.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetItalic(self, set: bool) -> None:
        """ 

`SetItalic`(*self*, *set*)[¶](#wx.dataview.DataViewItemAttr.SetItalic "Permalink to this definition")
Call this to indicate that the item shall be displayed in italic text.



Parameters
**set** (*bool*) – 






            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    def SetStrikethrough(self, set: bool) -> None:
        """ 

`SetStrikethrough`(*self*, *set*)[¶](#wx.dataview.DataViewItemAttr.SetStrikethrough "Permalink to this definition")
Call this to indicate that the item shall be displayed in strikethrough text.


Currently this attribute is only supported in the generic version of  [wx.dataview.DataViewCtrl](wx.dataview.DataViewCtrl.html#wx-dataview-dataviewctrl) and GTK and ignored by the native macOS implementations.



Parameters
**set** (*bool*) – 





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewItemAttr.html
        """

    BackgroundColour: 'Colour'  # `BackgroundColour`[¶](#wx.dataview.DataViewItemAttr.BackgroundColour "Permalink to this definition")See [`GetBackgroundColour`](#wx.dataview.DataViewItemAttr.GetBackgroundColour "wx.dataview.DataViewItemAttr.GetBackgroundColour") and [`SetBackgroundColour`](#wx.dataview.DataViewItemAttr.SetBackgroundColour "wx.dataview.DataViewItemAttr.SetBackgroundColour")
    Bold: bool  # `Bold`[¶](#wx.dataview.DataViewItemAttr.Bold "Permalink to this definition")See [`GetBold`](#wx.dataview.DataViewItemAttr.GetBold "wx.dataview.DataViewItemAttr.GetBold") and [`SetBold`](#wx.dataview.DataViewItemAttr.SetBold "wx.dataview.DataViewItemAttr.SetBold")
    Colour: '_Colour'  # `Colour`[¶](#wx.dataview.DataViewItemAttr.Colour "Permalink to this definition")See [`GetColour`](#wx.dataview.DataViewItemAttr.GetColour "wx.dataview.DataViewItemAttr.GetColour") and [`SetColour`](#wx.dataview.DataViewItemAttr.SetColour "wx.dataview.DataViewItemAttr.SetColour")
    Italic: bool  # `Italic`[¶](#wx.dataview.DataViewItemAttr.Italic "Permalink to this definition")See [`GetItalic`](#wx.dataview.DataViewItemAttr.GetItalic "wx.dataview.DataViewItemAttr.GetItalic") and [`SetItalic`](#wx.dataview.DataViewItemAttr.SetItalic "wx.dataview.DataViewItemAttr.SetItalic")



class DataViewToggleRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewToggleRenderer(varianttype=DataViewToggleRenderer.GetDefaultType
                       (), mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


This class is used by DataViewCtrl to render toggle controls.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewToggleRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewToggleRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewToggleRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """

    def ShowAsRadio(self) -> None:
        """ 

`ShowAsRadio`(*self*)[¶](#wx.dataview.DataViewToggleRenderer.ShowAsRadio "Permalink to this definition")
Switch to using radiobutton-like appearance instead of the default checkbox-like one.


By default, this renderer uses checkboxes to represent the boolean values, but using this method its appearance can be changed to use radio buttons instead.


Notice that only the appearance is changed, the cells don’t really start behaving as radio buttons after a call to [`ShowAsRadio`](#wx.dataview.DataViewToggleRenderer.ShowAsRadio "wx.dataview.DataViewToggleRenderer.ShowAsRadio") , i.e. the application code also needs to react to selecting one of the cells shown by this renderer and clearing all the other ones in the same row or column to actually implement radio button-like behaviour.



New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.dataview.DataViewToggleRenderer.html
        """



DataViewColumnFlags: TypeAlias = int  # Enumeration

DATAVIEW_COL_RESIZABLE: int

DATAVIEW_COL_SORTABLE: int

DATAVIEW_COL_REORDERABLE: int

DATAVIEW_COL_HIDDEN: int

class DataViewTextRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewTextRenderer(varianttype=DataViewTextRenderer.GetDefaultType(),
                     mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


DataViewTextRenderer is used for rendering text.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewTextRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewTextRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """

    def EnableMarkup(self, enable: bool=True) -> None:
        """ 

`EnableMarkup`(*self*, *enable=True*)[¶](#wx.dataview.DataViewTextRenderer.EnableMarkup "Permalink to this definition")
Enable interpretation of markup in the item data.


If this method is called with `True` argument, markup ( [`wx.Control.SetLabelMarkup`](wx.Control.html#wx.Control.SetLabelMarkup "wx.Control.SetLabelMarkup") ) in the data of the items in this column will be interpreted, which can be used for a more fine-grained appearance control than just setting an attribute, which affects all of the item text.


For example, as shown in the DataViewCtrl Sample, after creating a column using a markup-enabled renderer:



```
renderer = wx.DataViewTextRenderer()
renderer.EnableMarkup()
dataViewCtrl.AppendColumn(wx.DataViewColumn("title", renderer, 0))

```


The overridden model [`wx.dataview.DataViewModel.GetValue`](wx.dataview.DataViewModel.html#wx.dataview.DataViewModel.GetValue "wx.dataview.DataViewModel.GetValue") method may return values containing markup for this column:



```
def GetValue(self, item, col):

    if col == 0 and item == ...:

        value = ("<span color=\"#87ceeb\">light</span> and "
                 "<span color=\"#000080\">dark</span> blue")

    return value

```



Parameters
**enable** (*bool*) – 





New in version 4.1/wxWidgets-3.1.1.




Note


Currently  [wx.dataview.DataViewIconTextRenderer](wx.dataview.DataViewIconTextRenderer.html#wx-dataview-dataviewicontextrenderer) only provides [`EnableMarkup`](#wx.dataview.DataViewTextRenderer.EnableMarkup "wx.dataview.DataViewTextRenderer.EnableMarkup") [`EnableMarkup`](#wx.dataview.DataViewTextRenderer.EnableMarkup "wx.dataview.DataViewTextRenderer.EnableMarkup") in wxGTK, but not under the other platforms, so you should only use it for plain  [wx.dataview.DataViewTextRenderer](#wx-dataview-dataviewtextrenderer) columns, without icons, in portable code.





            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewTextRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewTextRenderer.html
        """



class DataViewCheckIconTextRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewCheckIconTextRenderer(mode=DATAVIEW_CELL_ACTIVATABLE,
                              align=DVR_DEFAULT_ALIGNMENT)

```


This renderer class shows a checkbox in addition to the icon and text
shown by the base class and also allows the user to toggle this
checkbox.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
    """
    def __init__(self, mode=DATAVIEW_CELL_ACTIVATABLE, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ 

`__init__`(*self*, *mode=DATAVIEW\_CELL\_ACTIVATABLE*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewCheckIconTextRenderer.__init__ "Permalink to this definition")
Create a new renderer.


By default the renderer is activatable, i.e. allows the user to toggle the checkbox.



Parameters
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """

    def Allow3rdStateForUser(self, allow: bool=True) -> None:
        """ 

`Allow3rdStateForUser`(*self*, *allow=True*)[¶](#wx.dataview.DataViewCheckIconTextRenderer.Allow3rdStateForUser "Permalink to this definition")
Allow the user to interactively select the 3rd state for the items rendered by this object.


As described in the class overview, this renderer can always display the 3rd (“indeterminate”) checkbox state if the model contains cells with `wx.CHK_UNDETERMINED` value, but it doesn’t allow the user to set it by default. Call this method to allow this to happen.



Parameters
**allow** (*bool*) – If `True`, interactively clicking a checked cell switches it to the indeterminate value and clicking it again unchecks it. If `False`, clicking a checked cell switches to the unchecked value, skipping the indeterminate one.






            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewCheckIconTextRenderer.GetDefaultType "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewCheckIconTextRenderer.html
        """



class DataViewProgressRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewProgressRenderer(label="",
                         varianttype=DataViewProgressRenderer.GetDefaultType(),
                         mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


This class is used by DataViewCtrl to render progress bars.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *label=""*, *varianttype=DataViewProgressRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewProgressRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **label** (*string*) –
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewProgressRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewProgressRenderer.html
        """



class DataViewBitmapRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewBitmapRenderer(varianttype=DataViewBitmapRenderer.GetDefaultType
                       (), mode=DATAVIEW_CELL_INERT, align=DVR_DEFAULT_ALIGNMENT)

```


This class is used by DataViewCtrl to render bitmaps.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewBitmapRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_INERT*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewBitmapRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewBitmapRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.


Note that the value returned by this function has changed from “wxBitmap” to “wxBitmapBundle” in wxWidgets 3.1.7, however the exact value shouldn’t matter, as it is only supposed to be used as the value for the first constructor argument.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewBitmapRenderer.html
        """



class DataViewDateRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewDateRenderer(varianttype=DataViewDateRenderer.GetDefaultType(),
                     mode=DATAVIEW_CELL_ACTIVATABLE, align=DVR_DEFAULT_ALIGNMENT)

```


This class is used by DataViewCtrl to render calendar controls.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *varianttype=DataViewDateRenderer.GetDefaultType()*, *mode=DATAVIEW\_CELL\_ACTIVATABLE*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewDateRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **varianttype** (*string*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
        """

    @staticmethod
    def GetDefaultType() -> str:
        """ 

*static* `GetDefaultType`()[¶](#wx.dataview.DataViewDateRenderer.GetDefaultType "Permalink to this definition")
Returns the *Variant* type used with this renderer.



Return type
`string`





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.dataview.DataViewDateRenderer.html
        """



class DataViewSpinRenderer(DataViewCustomRenderer):
    """ **Possible constructors**:



```
DataViewSpinRenderer(min, max, mode=DATAVIEW_CELL_EDITABLE,
                     align=DVR_DEFAULT_ALIGNMENT)

```


This is a specialized renderer for rendering integer values.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewSpinRenderer.html
    """
    def __init__(self, min, max, mode=DATAVIEW_CELL_EDITABLE, align=DVR_DEFAULT_ALIGNMENT) -> None:
        """ 

`__init__`(*self*, *min*, *max*, *mode=DATAVIEW\_CELL\_EDITABLE*, *align=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewSpinRenderer.__init__ "Permalink to this definition")
Constructor.


*min* and *max* indicate the minimum and maximum values for the  [wx.SpinCtrl](wx.SpinCtrl.html#wx-spinctrl).



Parameters
* **min** (*int*) –
* **max** (*int*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **align** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewSpinRenderer.html
        """



class DataViewChoiceRenderer(DataViewRenderer):
    """ **Possible constructors**:



```
DataViewChoiceRenderer(choices, mode=DATAVIEW_CELL_EDITABLE,
                       alignment=DVR_DEFAULT_ALIGNMENT)

```


A DataViewCtrl renderer using Choice control and values of strings
in it.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
    """
    def __init__(self, choices, mode=DATAVIEW_CELL_EDITABLE, alignment=DVR_DEFAULT_ALIGNMENT) -> None:
        """ 

`__init__`(*self*, *choices*, *mode=DATAVIEW\_CELL\_EDITABLE*, *alignment=DVR\_DEFAULT\_ALIGNMENT*)[¶](#wx.dataview.DataViewChoiceRenderer.__init__ "Permalink to this definition")
The constructor.



Parameters
* **choices** (*list of strings*) –
* **mode** ([*DataViewCellMode*](wx.dataview.DataViewCellMode.enumeration.html "DataViewCellMode")) –
* **alignment** (*int*) –






            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    def GetChoice(self, index: int) -> str:
        """ 

`GetChoice`(*self*, *index*)[¶](#wx.dataview.DataViewChoiceRenderer.GetChoice "Permalink to this definition")
Returns the choice referred to by index.



Parameters
**index** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    def GetChoices(self) -> list[str]:
        """ 

`GetChoices`(*self*)[¶](#wx.dataview.DataViewChoiceRenderer.GetChoices "Permalink to this definition")
Returns all choices.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.dataview.DataViewChoiceRenderer.html
        """

    Choices: list[str]  # `Choices`[¶](#wx.dataview.DataViewChoiceRenderer.Choices "Permalink to this definition")See [`GetChoices`](#wx.dataview.DataViewChoiceRenderer.GetChoices "wx.dataview.DataViewChoiceRenderer.GetChoices")



DataViewCellRenderState: TypeAlias = int  # Enumeration

DATAVIEW_CELL_SELECTED: int

DATAVIEW_CELL_PRELIT: int

DATAVIEW_CELL_INSENSITIVE: int

DATAVIEW_CELL_FOCUSED: int

class DataViewValueAdjuster:
    """ This class can be used with *DataViewRenderer.SetValueAdjuster()* to
customize rendering of model values with standard renderers.


  


        Source: https://docs.wxpython.org/wx.dataview.DataViewValueAdjuster.html
    """
    def MakeHighlighted(self, value: DVCVariant) -> 'DVCVariant':
        """ 

`MakeHighlighted`(*self*, *value*)[¶](#wx.dataview.DataViewValueAdjuster.MakeHighlighted "Permalink to this definition")
Change value for rendering when highlighted.


Override to customize the value when it is shown in a highlighted (selected) row, typically on a dark background.


Default implementation returns *value* unmodified.


The *value* passed to this method is always non-null and it must return a non-null value too.



Parameters
**value** (*DVCVariant*) – 



Return type
*DVCVariant*






            Source: https://docs.wxpython.org/wx.dataview.DataViewValueAdjuster.html
        """



DataViewItemArray: TypeAlias = list['DataViewItem']

DVCVariant: TypeAlias = Any

