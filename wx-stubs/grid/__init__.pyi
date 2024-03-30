# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Scrolled, Colour, Font, Pen, Window, HeaderCtrl, Rect, VisualAttributes, Point, ClientDataContainer, CommandEvent, _Control, _Window, Control, Object, SharedClientDataContainer, RefCounter, Size, _Font, NotifyEvent, _EllipsizeMode, EllipsizeMode, _KeyEvent, _MouseEvent, KeyEvent, MouseEvent
from .Grid import CellSpan
from .GridBlocks import iterator
from .GridActivationSource import Origin

GridTableRequest: TypeAlias = int  # Enumeration

GRIDTABLE_NOTIFY_ROWS_INSERTED: int

GRIDTABLE_NOTIFY_ROWS_APPENDED: int

GRIDTABLE_NOTIFY_ROWS_DELETED: int

GRIDTABLE_NOTIFY_COLS_INSERTED: int

GRIDTABLE_NOTIFY_COLS_APPENDED: int

GRIDTABLE_NOTIFY_COLS_DELETED: int

class Grid(Scrolled):
    """ **Possible constructors**:



```
Grid()

Grid(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
     style=WANTS_CHARS, name=GridNameStr)

```


Grid and its related classes are used for displaying and editing
tabular data.


  


        Source: https://docs.wxpython.org/wx.grid.Grid.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


You must call [`Create`](#wx.grid.Grid.Create "wx.grid.Grid.Create") to really create the grid window and also call [`CreateGrid`](#wx.grid.Grid.CreateGrid "wx.grid.Grid.CreateGrid") or [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") or [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") to initialize its contents.




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=WANTS\_CHARS, name=GridNameStr)*


Constructor creating the grid window.


You must call either [`CreateGrid`](#wx.grid.Grid.CreateGrid "wx.grid.Grid.CreateGrid") or [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") or [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") to initialize the grid contents before using it.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AppendCols(self, numCols=1, updateLabels=True) -> bool:
        """ 

`AppendCols`(*self*, *numCols=1*, *updateLabels=True*)[¶](#wx.grid.Grid.AppendCols "Permalink to this definition")
Appends one or more new columns to the right of the grid.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.AppendCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.AppendCols "wx.grid.GridTableBase.AppendCols") . See [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for further information.



Parameters
* **numCols** (*int*) –
* **updateLabels** (*bool*) –



Return type
*bool*



Returns
`True` on success or `False` if appending columns failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AppendRows(self, numRows=1, updateLabels=True) -> bool:
        """ 

`AppendRows`(*self*, *numRows=1*, *updateLabels=True*)[¶](#wx.grid.Grid.AppendRows "Permalink to this definition")
Appends one or more new rows to the bottom of the grid.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.AppendRows`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.AppendRows "wx.grid.GridTableBase.AppendRows") . See [`InsertRows`](#wx.grid.Grid.InsertRows "wx.grid.Grid.InsertRows") for further information.



Parameters
* **numRows** (*int*) –
* **updateLabels** (*bool*) –



Return type
*bool*



Returns
`True` on success or `False` if appending rows failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AreHorzGridLinesClipped(self) -> bool:
        """ 

`AreHorzGridLinesClipped`(*self*)[¶](#wx.grid.Grid.AreHorzGridLinesClipped "Permalink to this definition")
Return `True` if the horizontal grid lines stop at the last column boundary or `False` if they continue to the end of the window.


The default is to clip grid lines.



Return type
*bool*





See also


[`ClipHorzGridLines`](#wx.grid.Grid.ClipHorzGridLines "wx.grid.Grid.ClipHorzGridLines") , [`AreVertGridLinesClipped`](#wx.grid.Grid.AreVertGridLinesClipped "wx.grid.Grid.AreVertGridLinesClipped")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AreVertGridLinesClipped(self) -> bool:
        """ 

`AreVertGridLinesClipped`(*self*)[¶](#wx.grid.Grid.AreVertGridLinesClipped "Permalink to this definition")
Return `True` if the vertical grid lines stop at the last row boundary or `False` if they continue to the end of the window.


The default is to clip grid lines.



Return type
*bool*





See also


[`ClipVertGridLines`](#wx.grid.Grid.ClipVertGridLines "wx.grid.Grid.ClipVertGridLines") , [`AreHorzGridLinesClipped`](#wx.grid.Grid.AreHorzGridLinesClipped "wx.grid.Grid.AreHorzGridLinesClipped")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AssignTable(self, table, selmode=GridSelectCells) -> None:
        """ 

`AssignTable`(*self*, *table*, *selmode=GridSelectCells*)[¶](#wx.grid.Grid.AssignTable "Permalink to this definition")
Assigns a pointer to a custom grid table to be used by the grid.


This function is identical to [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") with `takeOwnership` parameter set to `True`, i.e. it simply always takes the ownership of the passed in pointer. This makes it simpler to use than [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") in the common case when the table should be owned by the grid object.


Note that this function should be called at most once and can’t be used to change the table used by the grid later on or reset it: if such extra flexibility is needed, use [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") directly.



Parameters
* **table** ([*wx.grid.GridTableBase*](wx.grid.GridTableBase.html#wx.grid.GridTableBase "wx.grid.GridTableBase")) – The heap-allocated pointer to the table.
* **selmode** ([*GridSelectionModes*](wx.grid.Grid.GridSelectionModes.enumeration.html "GridSelectionModes")) – Selection mode to use.





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSize(self) -> None:
        """ 

`AutoSize`(*self*)[¶](#wx.grid.Grid.AutoSize "Permalink to this definition")
Automatically sets the height and width of all rows and columns to fit their contents.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColLabelSize(self, col: int) -> None:
        """ 

`AutoSizeColLabelSize`(*self*, *col*)[¶](#wx.grid.Grid.AutoSizeColLabelSize "Permalink to this definition")
Automatically adjusts width of the column to fit its label.



Parameters
**col** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColumn(self, col, setAsMin=True) -> None:
        """ 

`AutoSizeColumn`(*self*, *col*, *setAsMin=True*)[¶](#wx.grid.Grid.AutoSizeColumn "Permalink to this definition")
Automatically sizes the column to fit its contents.


If *setAsMin* is `True` the calculated width will also be set as the minimal width for the column.



Parameters
* **col** (*int*) –
* **setAsMin** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeColumns(self, setAsMin: bool=True) -> None:
        """ 

`AutoSizeColumns`(*self*, *setAsMin=True*)[¶](#wx.grid.Grid.AutoSizeColumns "Permalink to this definition")
Automatically sizes all columns to fit their contents.


If *setAsMin* is `True` the calculated widths will also be set as the minimal widths for the columns.



Parameters
**setAsMin** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRow(self, row, setAsMin=True) -> None:
        """ 

`AutoSizeRow`(*self*, *row*, *setAsMin=True*)[¶](#wx.grid.Grid.AutoSizeRow "Permalink to this definition")
Automatically sizes the row to fit its contents.


If *setAsMin* is `True` the calculated height will also be set as the minimal height for the row.



Parameters
* **row** (*int*) –
* **setAsMin** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRowLabelSize(self, col: int) -> None:
        """ 

`AutoSizeRowLabelSize`(*self*, *col*)[¶](#wx.grid.Grid.AutoSizeRowLabelSize "Permalink to this definition")
Automatically adjusts height of the row to fit its label.



Parameters
**col** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def AutoSizeRows(self, setAsMin: bool=True) -> None:
        """ 

`AutoSizeRows`(*self*, *setAsMin=True*)[¶](#wx.grid.Grid.AutoSizeRows "Permalink to this definition")
Automatically sizes all rows to fit their contents.


If *setAsMin* is `True` the calculated heights will also be set as the minimal heights for the rows.



Parameters
**setAsMin** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def BeginBatch(self) -> None:
        """ 

`BeginBatch`(*self*)[¶](#wx.grid.Grid.BeginBatch "Permalink to this definition")
Increments the grid’s batch count.


When the count is greater than zero repainting of the grid is suppressed. Each call to BeginBatch must be matched by a later call to [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") . Code that does a lot of grid modification can be enclosed between [`BeginBatch`](#wx.grid.Grid.BeginBatch "wx.grid.Grid.BeginBatch") and [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") calls to avoid screen flicker. The final [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") call will cause the grid to be repainted.


Notice that you should use  [wx.grid.GridUpdateLocker](wx.grid.GridUpdateLocker.html#wx-grid-gridupdatelocker) which ensures that there is always a matching [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") call for this [`BeginBatch`](#wx.grid.Grid.BeginBatch "wx.grid.Grid.BeginBatch") if possible instead of calling this method directly.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def BlockToDeviceRect(self, topLeft, bottomRight, gridWindow=None) -> 'Rect':
        """ 

`BlockToDeviceRect`(*self*, *topLeft*, *bottomRight*, *gridWindow=None*)[¶](#wx.grid.Grid.BlockToDeviceRect "Permalink to this definition")
Convert grid cell coordinates to grid window pixel coordinates.


This function returns the rectangle that encloses the block of cells limited by *topLeft* and *bottomRight* cell in device coords and clipped to the client size of the grid window.



Parameters
* **topLeft** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **bottomRight** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
`Rect`





New in version 4.1/wxWidgets-3.1.3: Parameter *gridWindow* has been added.




See also


[`CellToRect`](#wx.grid.Grid.CellToRect "wx.grid.Grid.CellToRect")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcCellsExposed(self, reg, gridWindow=None) -> 'GridCellCoordsArray':
        """ 

`CalcCellsExposed`(*self*, *reg*, *gridWindow=None*)[¶](#wx.grid.Grid.CalcCellsExposed "Permalink to this definition")
Appends one or more new columns to the right of the grid.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.AppendCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.AppendCols "wx.grid.GridTableBase.AppendCols") . See [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for further information.



Parameters
* **reg** ([*wx.Region*](wx.Region.html#wx.Region "wx.Region")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*GridCellCoordsArray*



Returns
`True` on success or `False` if appending columns failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcColLabelsExposed(self, reg, gridWindow=None) -> int:
        """ 

`CalcColLabelsExposed`(*self*, *reg*, *gridWindow=None*)[¶](#wx.grid.Grid.CalcColLabelsExposed "Permalink to this definition")
Appends one or more new columns to the right of the grid.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.AppendCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.AppendCols "wx.grid.GridTableBase.AppendCols") . See [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for further information.



Parameters
* **reg** ([*wx.Region*](wx.Region.html#wx.Region "wx.Region")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*list of integers*



Returns
`True` on success or `False` if appending columns failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcGridWindowScrolledPosition(self, *args, **kw) -> None:
        """ 

`CalcGridWindowScrolledPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.CalcGridWindowScrolledPosition "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CalcGridWindowScrolledPosition** *(self, x, y, xx, yy, gridWindow)*


Translates the logical coordinates to the device ones, taking into account the grid window type.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **xx** (*int*) –
* **yy** (*int*) –
* **gridWindow** (*wx.grid.GridWindow*) –





New in version 4.1/wxWidgets-3.1.3.




See also


[`wx.Scrolled.CalcScrolledPosition`](wx.Scrolled.html#wx.Scrolled.CalcScrolledPosition "wx.Scrolled.CalcScrolledPosition")





---

  



**CalcGridWindowScrolledPosition** *(self, pt, gridWindow)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*Point*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcGridWindowUnscrolledPosition(self, *args, **kw) -> None:
        """ 

`CalcGridWindowUnscrolledPosition`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.CalcGridWindowUnscrolledPosition "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CalcGridWindowUnscrolledPosition** *(self, x, y, xx, yy, gridWindow)*


Translates the device coordinates to the logical ones, taking into account the grid window type.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **xx** (*int*) –
* **yy** (*int*) –
* **gridWindow** (*wx.grid.GridWindow*) –





New in version 4.1/wxWidgets-3.1.3.




See also


[`wx.Scrolled.CalcUnscrolledPosition`](wx.Scrolled.html#wx.Scrolled.CalcUnscrolledPosition "wx.Scrolled.CalcUnscrolledPosition")





---

  



**CalcGridWindowUnscrolledPosition** *(self, pt, gridWindow)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*Point*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CalcRowLabelsExposed(self, reg, gridWindow=None) -> int:
        """ 

`CalcRowLabelsExposed`(*self*, *reg*, *gridWindow=None*)[¶](#wx.grid.Grid.CalcRowLabelsExposed "Permalink to this definition")
Appends one or more new columns to the right of the grid.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.AppendCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.AppendCols "wx.grid.GridTableBase.AppendCols") . See [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for further information.



Parameters
* **reg** ([*wx.Region*](wx.Region.html#wx.Region "wx.Region")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*list of integers*



Returns
`True` on success or `False` if appending columns failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragCell(self) -> bool:
        """ 

`CanDragCell`(*self*)[¶](#wx.grid.Grid.CanDragCell "Permalink to this definition")
Return `True` if the dragging of cells is enabled or `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragColMove(self) -> bool:
        """ 

`CanDragColMove`(*self*)[¶](#wx.grid.Grid.CanDragColMove "Permalink to this definition")
Returns `True` if columns can be moved by dragging with the mouse.


Columns can be moved by dragging on their labels.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragColSize(self, col: int) -> bool:
        """ 

`CanDragColSize`(*self*, *col*)[¶](#wx.grid.Grid.CanDragColSize "Permalink to this definition")
Returns `True` if the given column can be resized by dragging with the mouse.


This function returns `True` if resizing the columns interactively is globally enabled, i.e. if [`DisableDragColSize`](#wx.grid.Grid.DisableDragColSize "wx.grid.Grid.DisableDragColSize") hadn’t been called, and if this column wasn’t explicitly marked as non-resizable with [`DisableColResize`](#wx.grid.Grid.DisableColResize "wx.grid.Grid.DisableColResize") .



Parameters
**col** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridColEdges(self) -> bool:
        """ 

`CanDragGridColEdges`(*self*)[¶](#wx.grid.Grid.CanDragGridColEdges "Permalink to this definition")
Return `True` if column edges inside the grid can be dragged to resize the rows.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.




See also


[`CanDragGridSize`](#wx.grid.Grid.CanDragGridSize "wx.grid.Grid.CanDragGridSize") , [`CanDragColSize`](#wx.grid.Grid.CanDragColSize "wx.grid.Grid.CanDragColSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridRowEdges(self) -> bool:
        """ 

`CanDragGridRowEdges`(*self*)[¶](#wx.grid.Grid.CanDragGridRowEdges "Permalink to this definition")
Return `True` if row edges inside the grid can be dragged to resize the rows.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.




See also


[`CanDragGridSize`](#wx.grid.Grid.CanDragGridSize "wx.grid.Grid.CanDragGridSize") , [`CanDragRowSize`](#wx.grid.Grid.CanDragRowSize "wx.grid.Grid.CanDragRowSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragGridSize(self) -> bool:
        """ 

`CanDragGridSize`(*self*)[¶](#wx.grid.Grid.CanDragGridSize "Permalink to this definition")
Return `True` if the dragging of grid lines to resize rows and columns is enabled or `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragRowMove(self) -> bool:
        """ 

`CanDragRowMove`(*self*)[¶](#wx.grid.Grid.CanDragRowMove "Permalink to this definition")
Returns `True` if rows can be moved by dragging with the mouse.


Rows can be moved by dragging on their labels.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanDragRowSize(self, row: int) -> bool:
        """ 

`CanDragRowSize`(*self*, *row*)[¶](#wx.grid.Grid.CanDragRowSize "Permalink to this definition")
Returns `True` if the given row can be resized by dragging with the mouse.


This is the same as [`CanDragColSize`](#wx.grid.Grid.CanDragColSize "wx.grid.Grid.CanDragColSize") but for rows.



Parameters
**row** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanEnableCellControl(self) -> bool:
        """ 

`CanEnableCellControl`(*self*)[¶](#wx.grid.Grid.CanEnableCellControl "Permalink to this definition")
Returns `True` if the in-place edit control for the current grid cell can be used and `False` otherwise.


This function always returns `False` for the read-only cells.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanHaveAttributes(self) -> bool:
        """ 

`CanHaveAttributes`(*self*)[¶](#wx.grid.Grid.CanHaveAttributes "Permalink to this definition")
Returns `True` if this grid has support for cell attributes.


The grid supports attributes if it has the associated table which, in turn, has attributes support, i.e. [`wx.grid.GridTableBase.CanHaveAttributes`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.CanHaveAttributes "wx.grid.GridTableBase.CanHaveAttributes") returns `True`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CanHideColumns(self) -> bool:
        """ 

`CanHideColumns`(*self*)[¶](#wx.grid.Grid.CanHideColumns "Permalink to this definition")
Returns `True` if columns can be hidden from the popup menu of the native header.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CellToGridWindow(self, *args, **kw) -> 'GridWindow':
        """ 

`CellToGridWindow`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.CellToGridWindow "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CellToGridWindow** *(self, row, col)*


Returns the grid window that contains the cell.


In a grid without frozen rows or columns (see [`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo") ), this will always return the same window as [`GetGridWindow`](#wx.grid.Grid.GetGridWindow "wx.grid.Grid.GetGridWindow") , however if some parts of the grid are frozen, this function returns the window containing the given cell.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*wx.grid.GridWindow*





New in version 4.1/wxWidgets-3.1.3.





---

  



**CellToGridWindow** *(self, coords)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
*wx.grid.GridWindow*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CellToRect(self, *args, **kw) -> 'Rect':
        """ 

`CellToRect`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.CellToRect "Permalink to this definition")
Return the rectangle corresponding to the grid cell’s size and position in logical coordinates.



See also


[`BlockToDeviceRect`](#wx.grid.Grid.BlockToDeviceRect "wx.grid.Grid.BlockToDeviceRect")



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**CellToRect** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`Rect`






---

  



**CellToRect** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
`Rect`






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClearGrid(self) -> None:
        """ 

`ClearGrid`(*self*)[¶](#wx.grid.Grid.ClearGrid "Permalink to this definition")
Clears all data in the underlying grid table and repaints the grid.


The table is not deleted by this function. If you are using a derived table class then you need to override [`wx.grid.GridTableBase.Clear`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.Clear "wx.grid.GridTableBase.Clear") for this function to have any effect.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClearSelection(self) -> None:
        """ 

`ClearSelection`(*self*)[¶](#wx.grid.Grid.ClearSelection "Permalink to this definition")
Deselects all cells that are currently selected.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClipHorzGridLines(self, clip: bool) -> None:
        """ 

`ClipHorzGridLines`(*self*, *clip*)[¶](#wx.grid.Grid.ClipHorzGridLines "Permalink to this definition")
Change whether the horizontal grid lines are clipped by the end of the last column.


By default the grid lines are not drawn beyond the end of the last column but after calling this function with *clip* set to `False` they will be drawn across the entire grid window.



Parameters
**clip** (*bool*) – 





See also


[`AreHorzGridLinesClipped`](#wx.grid.Grid.AreHorzGridLinesClipped "wx.grid.Grid.AreHorzGridLinesClipped") , [`ClipVertGridLines`](#wx.grid.Grid.ClipVertGridLines "wx.grid.Grid.ClipVertGridLines")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ClipVertGridLines(self, clip: bool) -> None:
        """ 

`ClipVertGridLines`(*self*, *clip*)[¶](#wx.grid.Grid.ClipVertGridLines "Permalink to this definition")
Change whether the vertical grid lines are clipped by the end of the last row.


By default the grid lines are not drawn beyond the end of the last row but after calling this function with *clip* set to `False` they will be drawn across the entire grid window.



Parameters
**clip** (*bool*) – 





See also


[`AreVertGridLinesClipped`](#wx.grid.Grid.AreVertGridLinesClipped "wx.grid.Grid.AreVertGridLinesClipped") , [`ClipHorzGridLines`](#wx.grid.Grid.ClipHorzGridLines "wx.grid.Grid.ClipHorzGridLines")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=WANTS_CHARS, name=GridNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=WANTS\_CHARS*, *name=GridNameStr*)[¶](#wx.grid.Grid.Create "Permalink to this definition")
Creates the grid window for an object initialized using the default constructor.


You must call either [`CreateGrid`](#wx.grid.Grid.CreateGrid "wx.grid.Grid.CreateGrid") or [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") or [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") to initialize the grid contents before using it.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def CreateGrid(self, numRows, numCols, selmode=GridSelectCells) -> bool:
        """ 

`CreateGrid`(*self*, *numRows*, *numCols*, *selmode=GridSelectCells*)[¶](#wx.grid.Grid.CreateGrid "Permalink to this definition")
Creates a grid with the specified initial number of rows and columns.


Call this directly after the grid constructor. When you use this function  [wx.grid.Grid](#wx-grid-grid) will create and manage a simple table of string values for you. All of the grid data will be stored in memory.


For applications with more complex data types or relationships, or for dealing with very large datasets, you should derive your own grid table class and pass a table object to the grid with [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") or [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") .



Parameters
* **numRows** (*int*) –
* **numCols** (*int*) –
* **selmode** ([*GridSelectionModes*](wx.grid.Grid.GridSelectionModes.enumeration.html "GridSelectionModes")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeleteCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
        """ 

`DeleteCols`(*self*, *pos=0*, *numCols=1*, *updateLabels=True*)[¶](#wx.grid.Grid.DeleteCols "Permalink to this definition")
Deletes one or more columns from a grid starting at the specified position.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.DeleteCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.DeleteCols "wx.grid.GridTableBase.DeleteCols") . See [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for further information.



Parameters
* **pos** (*int*) –
* **numCols** (*int*) –
* **updateLabels** (*bool*) –



Return type
*bool*



Returns
`True` on success or `False` if deleting columns failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeleteRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
        """ 

`DeleteRows`(*self*, *pos=0*, *numRows=1*, *updateLabels=True*)[¶](#wx.grid.Grid.DeleteRows "Permalink to this definition")
Deletes one or more rows from a grid starting at the specified position.


The *updateLabels* argument is not used at present. If you are using a derived grid table class you will need to override [`wx.grid.GridTableBase.DeleteRows`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.DeleteRows "wx.grid.GridTableBase.DeleteRows") . See [`InsertRows`](#wx.grid.Grid.InsertRows "wx.grid.Grid.InsertRows") for further information.



Parameters
* **pos** (*int*) –
* **numRows** (*int*) –
* **updateLabels** (*bool*) –



Return type
*bool*



Returns
`True` on success or `False` if deleting rows failed.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectCell(self, row, col) -> None:
        """ 

`DeselectCell`(*self*, *row*, *col*)[¶](#wx.grid.Grid.DeselectCell "Permalink to this definition")
Deselects a cell.



Parameters
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectCol(self, col: int) -> None:
        """ 

`DeselectCol`(*self*, *col*)[¶](#wx.grid.Grid.DeselectCol "Permalink to this definition")
Deselects a column of cells.



Parameters
**col** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DeselectRow(self, row: int) -> None:
        """ 

`DeselectRow`(*self*, *row*)[¶](#wx.grid.Grid.DeselectRow "Permalink to this definition")
Deselects a row of cells.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DevicePosToGridWindow(self, *args, **kw) -> 'GridWindow':
        """ 

`DevicePosToGridWindow`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.DevicePosToGridWindow "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**DevicePosToGridWindow** *(self, pos)*


Returns the grid window that includes the input coordinates.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*wx.grid.GridWindow*





New in version 4.1/wxWidgets-3.1.3.





---

  



**DevicePosToGridWindow** *(self, x, y)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **x** (*int*) –
* **y** (*int*) –



Return type
*wx.grid.GridWindow*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableCellEditControl(self) -> None:
        """ 

`DisableCellEditControl`(*self*)[¶](#wx.grid.Grid.DisableCellEditControl "Permalink to this definition")
Disables in-place editing of grid cells.


Equivalent to calling EnableCellEditControl(false).




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableColResize(self, col: int) -> None:
        """ 

`DisableColResize`(*self*, *col*)[¶](#wx.grid.Grid.DisableColResize "Permalink to this definition")
Disable interactive resizing of the specified column.


This method allows one to disable resizing of an individual column in a grid where the columns are otherwise resizable (which is the case by default).


Notice that currently there is no way to make some columns resizable in a grid where columns can’t be resized by default as there doesn’t seem to be any need for this in practice. There is also no way to make the column marked as fixed using this method resizable again because it is supposed that fixed columns are used for static parts of the grid and so should remain fixed during the entire grid lifetime.


Also notice that disabling interactive column resizing will not prevent the program from changing the column size.



Parameters
**col** (*int*) – 





See also


[`EnableDragColSize`](#wx.grid.Grid.EnableDragColSize "wx.grid.Grid.EnableDragColSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragColMove(self) -> None:
        """ 

`DisableDragColMove`(*self*)[¶](#wx.grid.Grid.DisableDragColMove "Permalink to this definition")
Disables column moving by dragging with the mouse.


Equivalent to passing `False` to [`EnableDragColMove`](#wx.grid.Grid.EnableDragColMove "wx.grid.Grid.EnableDragColMove") .




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragColSize(self) -> None:
        """ 

`DisableDragColSize`(*self*)[¶](#wx.grid.Grid.DisableDragColSize "Permalink to this definition")
Disables column sizing by dragging with the mouse.


Equivalent to passing `False` to [`EnableDragColSize`](#wx.grid.Grid.EnableDragColSize "wx.grid.Grid.EnableDragColSize") .




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragGridSize(self) -> None:
        """ 

`DisableDragGridSize`(*self*)[¶](#wx.grid.Grid.DisableDragGridSize "Permalink to this definition")
Disable mouse dragging of grid lines to resize rows and columns.


Equivalent to passing `False` to [`EnableDragGridSize`](#wx.grid.Grid.EnableDragGridSize "wx.grid.Grid.EnableDragGridSize")




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragRowMove(self) -> None:
        """ 

`DisableDragRowMove`(*self*)[¶](#wx.grid.Grid.DisableDragRowMove "Permalink to this definition")
Disables row moving by dragging with the mouse.


Equivalent to passing `False` to [`EnableDragRowMove`](#wx.grid.Grid.EnableDragRowMove "wx.grid.Grid.EnableDragRowMove") .



New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableDragRowSize(self) -> None:
        """ 

`DisableDragRowSize`(*self*)[¶](#wx.grid.Grid.DisableDragRowSize "Permalink to this definition")
Disables row sizing by dragging with the mouse.


Equivalent to passing `False` to [`EnableDragRowSize`](#wx.grid.Grid.EnableDragRowSize "wx.grid.Grid.EnableDragRowSize") .




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableHidingColumns(self) -> None:
        """ 

`DisableHidingColumns`(*self*)[¶](#wx.grid.Grid.DisableHidingColumns "Permalink to this definition")
Disables column hiding from the header popup menu.


Equivalent to passing `False` to [`EnableHidingColumns`](#wx.grid.Grid.EnableHidingColumns "wx.grid.Grid.EnableHidingColumns") .



New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DisableRowResize(self, row: int) -> None:
        """ 

`DisableRowResize`(*self*, *row*)[¶](#wx.grid.Grid.DisableRowResize "Permalink to this definition")
Disable interactive resizing of the specified row.


This is the same as [`DisableColResize`](#wx.grid.Grid.DisableColResize "wx.grid.Grid.DisableColResize") but for rows.



Parameters
**row** (*int*) – 





See also


[`EnableDragRowSize`](#wx.grid.Grid.EnableDragRowSize "wx.grid.Grid.EnableDragRowSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawCellHighlight(self, dc, attr) -> None:
        """ 

`DrawCellHighlight`(*self*, *dc*, *attr*)[¶](#wx.grid.Grid.DrawCellHighlight "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawColLabel(self, dc, col) -> None:
        """ 

`DrawColLabel`(*self*, *dc*, *col*)[¶](#wx.grid.Grid.DrawColLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawColLabels(self, dc, cols) -> None:
        """ 

`DrawColLabels`(*self*, *dc*, *cols*)[¶](#wx.grid.Grid.DrawColLabels "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **cols** (*list of integers*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawCornerLabel(self, dc: 'DC') -> None:
        """ 

`DrawCornerLabel`(*self*, *dc*)[¶](#wx.grid.Grid.DrawCornerLabel "Permalink to this definition")

Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawRowLabel(self, dc, row) -> None:
        """ 

`DrawRowLabel`(*self*, *dc*, *row*)[¶](#wx.grid.Grid.DrawRowLabel "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **row** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawRowLabels(self, dc, rows) -> None:
        """ 

`DrawRowLabels`(*self*, *dc*, *rows*)[¶](#wx.grid.Grid.DrawRowLabels "Permalink to this definition")

Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rows** (*list of integers*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def DrawTextRectangle(self, *args, **kw) -> None:
        """ 

`DrawTextRectangle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.DrawTextRectangle "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**DrawTextRectangle** *(self, dc, text, rect, horizontalAlignment=ALIGN\_LEFT, verticalAlignment=ALIGN\_TOP, textOrientation=HORIZONTAL)*



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **text** (*string*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **horizontalAlignment** (*int*) –
* **verticalAlignment** (*int*) –
* **textOrientation** (*int*) –






---

  



**DrawTextRectangle** *(self, dc, lines, rect, horizontalAlignment=ALIGN\_LEFT, verticalAlignment=ALIGN\_TOP, textOrientation=HORIZONTAL)*



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **lines** (*list of strings*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **horizontalAlignment** (*int*) –
* **verticalAlignment** (*int*) –
* **textOrientation** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableCellEditControl(self, enable: bool=True) -> None:
        """ 

`EnableCellEditControl`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableCellEditControl "Permalink to this definition")
Enables or disables in-place editing of grid cell data.


Enabling in-place editing generates `wxEVT_GRID_EDITOR_SHOWN` and, if it isn’t vetoed by the application, shows the in-place editor which allows the user to change the cell value.


Disabling in-place editing does nothing if the in-place editor isn’t currently shown, otherwise the `wxEVT_GRID_EDITOR_HIDDEN` event is generated but, unlike the “shown” event, it can’t be vetoed and the in-place editor is dismissed unconditionally.


Note that it is an error to call this function if the current cell is read-only, use [`CanEnableCellControl`](#wx.grid.Grid.CanEnableCellControl "wx.grid.Grid.CanEnableCellControl") to check for this precondition.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragCell(self, enable: bool=True) -> None:
        """ 

`EnableDragCell`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragCell "Permalink to this definition")
Enables or disables cell dragging with the mouse.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragColMove(self, enable: bool=True) -> bool:
        """ 

`EnableDragColMove`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragColMove "Permalink to this definition")
Enables or disables column moving by dragging with the mouse.


Note that reordering columns by dragging them is currently not supported when the grid has any frozen columns (see [`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo") ) and if this method is called with *enable* equal to `True` in this situation, it returns `False` without doing anything. Otherwise it returns `True` to indicate that it was successful.



Parameters
**enable** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragColSize(self, enable: bool=True) -> None:
        """ 

`EnableDragColSize`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragColSize "Permalink to this definition")
Enables or disables column sizing by dragging with the mouse.



Parameters
**enable** (*bool*) – 





See also


[`DisableColResize`](#wx.grid.Grid.DisableColResize "wx.grid.Grid.DisableColResize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragGridSize(self, enable: bool=True) -> None:
        """ 

`EnableDragGridSize`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragGridSize "Permalink to this definition")
Enables or disables row and column resizing by dragging gridlines with the mouse.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragRowMove(self, enable: bool=True) -> bool:
        """ 

`EnableDragRowMove`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragRowMove "Permalink to this definition")
Enables or disables row moving by dragging with the mouse.


Note that reordering rows by dragging them is currently not supported when the grid has any frozen columns (see [`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo") ) and if this method is called with *enable* equal to `True` in this situation, it returns `False` without doing anything. Otherwise it returns `True` to indicate that it was successful.



Parameters
**enable** (*bool*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableDragRowSize(self, enable: bool=True) -> None:
        """ 

`EnableDragRowSize`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableDragRowSize "Permalink to this definition")
Enables or disables row sizing by dragging with the mouse.



Parameters
**enable** (*bool*) – 





See also


[`DisableRowResize`](#wx.grid.Grid.DisableRowResize "wx.grid.Grid.DisableRowResize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableEditing(self, edit: bool) -> None:
        """ 

`EnableEditing`(*self*, *edit*)[¶](#wx.grid.Grid.EnableEditing "Permalink to this definition")
Makes the grid globally editable or read-only.


If the edit argument is `False` this function sets the whole grid as read-only. If the argument is `True` the grid is set to the default state where cells may be editable. In the default state you can set single grid cells and whole rows and columns to be editable or read-only via [`wx.grid.GridCellAttr.SetReadOnly`](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr.SetReadOnly "wx.grid.GridCellAttr.SetReadOnly") . For single cells you can also use the shortcut function [`SetReadOnly`](#wx.grid.Grid.SetReadOnly "wx.grid.Grid.SetReadOnly") .


For more information about controlling grid cell attributes see the  [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr) class and the [Grid Overview](grid_overview.html#grid-overview).



Parameters
**edit** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableGridLines(self, enable: bool=True) -> None:
        """ 

`EnableGridLines`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableGridLines "Permalink to this definition")
Turns the drawing of grid lines on or off.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EnableHidingColumns(self, enable: bool=True) -> bool:
        """ 

`EnableHidingColumns`(*self*, *enable=True*)[¶](#wx.grid.Grid.EnableHidingColumns "Permalink to this definition")
Enables or disables column hiding from the header popup menu.


Note that currently the popup menu can only be shown when using  [wx.HeaderCtrl](wx.HeaderCtrl.html#wx-headerctrl), i.e. if [`UseNativeColHeader`](#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader") had been called.


If the native header is not used, this method always simply returns `False` without doing anything, as hiding columns is not supported anyhow. If *enable* value is the same as [`CanHideColumns`](#wx.grid.Grid.CanHideColumns "wx.grid.Grid.CanHideColumns") , it also returns `False` to indicate that nothing was done. Otherwise, it returns `True` to indicate that the value of this option was successfully changed.


The main use case for this method is to disallow hiding the columns interactively when using the native header.



Parameters
**enable** (*bool*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.3.




See also


[`DisableHidingColumns`](#wx.grid.Grid.DisableHidingColumns "wx.grid.Grid.DisableHidingColumns")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def EndBatch(self) -> None:
        """ 

`EndBatch`(*self*)[¶](#wx.grid.Grid.EndBatch "Permalink to this definition")
Decrements the grid’s batch count.


When the count is greater than zero repainting of the grid is suppressed. Each previous call to [`BeginBatch`](#wx.grid.Grid.BeginBatch "wx.grid.Grid.BeginBatch") must be matched by a later call to [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") . Code that does a lot of grid modification can be enclosed between [`BeginBatch`](#wx.grid.Grid.BeginBatch "wx.grid.Grid.BeginBatch") and [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") calls to avoid screen flicker. The final [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") will cause the grid to be repainted.



See also


 [wx.grid.GridUpdateLocker](wx.grid.GridUpdateLocker.html#wx-grid-gridupdatelocker)





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Fit(self) -> None:
        """ 

`Fit`(*self*)[¶](#wx.grid.Grid.Fit "Permalink to this definition")
Overridden  [wx.Window](wx.Window.html#wx-window) method.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ForceRefresh(self) -> None:
        """ 

`ForceRefresh`(*self*)[¶](#wx.grid.Grid.ForceRefresh "Permalink to this definition")
Causes immediate repainting of the grid.


Use this instead of the usual [`wx.Window.Refresh`](wx.Window.html#wx.Window.Refresh "wx.Window.Refresh") .




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def FreezeTo(self, *args, **kw) -> bool:
        """ 

`FreezeTo`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.FreezeTo "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**FreezeTo** *(self, row, col)*


Sets or resets the frozen columns and rows.



Parameters
* **row** – The number of rows to freeze, 0 means to unfreeze all rows.
* **col** – The number of columns to freeze, 0 means to unfreeze all columns.



Return type
*bool*




Note that this method doesn’t do anything, and returns `False`, if any of the following conditions are `True`:


* Either *row* or *col* are out of range
* Size of the frozen area would be bigger than the current viewing area
* There are any merged cells in the area to be frozen
* Grid uses a native header control (see [`UseNativeColHeader`](#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader") )


(some of these limitations could be lifted in the future).



Returns
`True` on success or `False` if it failed.





New in version 4.1/wxWidgets-3.1.3.





---

  



**FreezeTo** *(self, coords)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetBatchCount(self) -> int:
        """ 

`GetBatchCount`(*self*)[¶](#wx.grid.Grid.GetBatchCount "Permalink to this definition")
Returns the number of times that [`BeginBatch`](#wx.grid.Grid.BeginBatch "wx.grid.Grid.BeginBatch") has been called without (yet) matching calls to [`EndBatch`](#wx.grid.Grid.EndBatch "wx.grid.Grid.EndBatch") .


While the grid’s batch count is greater than zero the display will not be updated.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellAlignment(self, row, col) -> tuple:
        """ 

`GetCellAlignment`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellAlignment "Permalink to this definition")
Sets the arguments to the horizontal and vertical text alignment values for the grid cell at the specified location.


Horizontal alignment will be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment will be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*tuple*



Returns
( *horiz*, *vert* )






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellBackgroundColour(self, row, col) -> 'Colour':
        """ 

`GetCellBackgroundColour`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellBackgroundColour "Permalink to this definition")
Returns the background colour of the cell at the specified location.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellEditor(self, row, col) -> 'GridCellEditor':
        """ 

`GetCellEditor`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellEditor "Permalink to this definition")
Returns a pointer to the editor for the cell at the specified location.


See  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.


The caller must call DecRef() on the returned pointer.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellFitMode(self, row, col) -> 'GridFitMode':
        """ 

`GetCellFitMode`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellFitMode "Permalink to this definition")
Returns the cell fitting mode.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





New in version 4.1/wxWidgets-3.1.4.




See also


 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellFont(self, row, col) -> 'Font':
        """ 

`GetCellFont`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellFont "Permalink to this definition")
Returns the font for text in the grid cell at the specified location.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`Font`






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightColour(self) -> 'Colour':
        """ 

`GetCellHighlightColour`(*self*)[¶](#wx.grid.Grid.GetCellHighlightColour "Permalink to this definition")

Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightPenWidth(self) -> int:
        """ 

`GetCellHighlightPenWidth`(*self*)[¶](#wx.grid.Grid.GetCellHighlightPenWidth "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellHighlightROPenWidth(self) -> int:
        """ 

`GetCellHighlightROPenWidth`(*self*)[¶](#wx.grid.Grid.GetCellHighlightROPenWidth "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellOverflow(self, row, col) -> bool:
        """ 

`GetCellOverflow`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellOverflow "Permalink to this definition")
Returns `True` if the cell value can overflow.


This is identical to calling [`GetCellFitMode`](#wx.grid.Grid.GetCellFitMode "wx.grid.Grid.GetCellFitMode") and using [`wx.grid.GridFitMode.IsOverflow`](wx.grid.GridFitMode.html#wx.grid.GridFitMode.IsOverflow "wx.grid.GridFitMode.IsOverflow") on the returned value.


Prefer using [`GetCellFitMode`](#wx.grid.Grid.GetCellFitMode "wx.grid.Grid.GetCellFitMode") directly in the new code.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellRenderer(self, row, col) -> 'GridCellRenderer':
        """ 

`GetCellRenderer`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellRenderer "Permalink to this definition")
Returns a pointer to the renderer for the grid cell at the specified location.


See  [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.


The caller must call DecRef() on the returned pointer.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellSize(self, *args, **kw) -> 'CellSpan':
        """ 

`GetCellSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.GetCellSize "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetCellSize** *(self, row, col, num\_rows, num\_cols)*


Get the size of the cell in number of cells covered by it.


For normal cells, the function fills both *num\_rows* and *num\_cols* with 1 and returns CellSpan\_None. For cells which span multiple cells, i.e. for which [`SetCellSize`](#wx.grid.Grid.SetCellSize "wx.grid.Grid.SetCellSize") had been called, the returned values are the same ones as were passed to [`SetCellSize`](#wx.grid.Grid.SetCellSize "wx.grid.Grid.SetCellSize") call and the function return value is CellSpan\_Main.


More unexpectedly, perhaps, the returned values may be *negative* for the cells which are inside a span covered by a cell occupying multiple rows or columns. They correspond to the offset of the main cell of the span from the cell passed to this functions and the function returns CellSpan\_Inside value to indicate this.


As an example, consider a 3x3 grid with the cell (1, 1) (the one in the middle) having a span of 2 rows and 2 columns, i.e. the grid looks like



```
+----+----+----+
|    |    |    |
+----+----+----+
|    |         |
+----+         |
|    |         |
+----+----+----+

```


Then the function returns 2 and 2 in *num\_rows* and *num\_cols* for the cell (1, 1) itself and -1 and -1 for the cell (2, 2) as well as -1 and 0 for the cell (2, 1).



Parameters
* **row** (*int*) – The row of the cell.
* **col** (*int*) – The column of the cell.
* **num\_rows** (*int*) – Pointer to variable receiving the number of rows, must not be `None`.
* **num\_cols** (*int*) – Pointer to variable receiving the number of columns, must not be `None`.



Return type
 [wx.grid.Grid.CellSpan](wx.grid.Grid.CellSpan.enumeration.html#wx-grid-grid-cellspan)



Returns
The kind of this cell span (the return value is new in wxWidgets 2.9.1, this function was in previous wxWidgets versions).






---

  



**GetCellSize** *(self, coords)*


Get the number of rows and columns allocated for this cell.


This overload doesn’t return a CellSpan value but the values returned may still be negative, see GetCellSize(int, int, int, int ) for details.



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
`Size`






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellTextColour(self, row, col) -> 'Colour':
        """ 

`GetCellTextColour`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetCellTextColour "Permalink to this definition")
Returns the text colour for the grid cell at the specified location.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCellValue(self, *args, **kw) -> str:
        """ 

`GetCellValue`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.GetCellValue "Permalink to this definition")
Returns the string contained in the cell at the specified location.


For simple applications where a grid object automatically uses a default grid table of string values you use this function together with [`SetCellValue`](#wx.grid.Grid.SetCellValue "wx.grid.Grid.SetCellValue") to access cell values. For more complex applications where you have derived your own grid table class that contains various data types (e.g. numeric, boolean or user-defined custom types) then you only use this function for those cells that contain string values.


See [`wx.grid.GridTableBase.CanGetValueAs`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.CanGetValueAs "wx.grid.GridTableBase.CanGetValueAs") and the [Grid Overview](grid_overview.html#grid-overview) for more information.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetCellValue** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`string`






---

  



**GetCellValue** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
`string`






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.grid.Grid.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColAt(self, colPos: int) -> int:
        """ 

`GetColAt`(*self*, *colPos*)[¶](#wx.grid.Grid.GetColAt "Permalink to this definition")
Returns the column `ID` of the specified column position.



Parameters
**colPos** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColGridLinePen(self, col: int) -> 'Pen':
        """ 

`GetColGridLinePen`(*self*, *col*)[¶](#wx.grid.Grid.GetColGridLinePen "Permalink to this definition")
Returns the pen used for vertical grid lines.


This virtual function may be overridden in derived classes in order to change the appearance of individual grid lines for the given column *col*.


See [`GetRowGridLinePen`](#wx.grid.Grid.GetRowGridLinePen "wx.grid.Grid.GetRowGridLinePen") for an example.



Parameters
**col** (*int*) – 



Return type
*Pen*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelAlignment(self) -> tuple:
        """ 

`GetColLabelAlignment`(*self*)[¶](#wx.grid.Grid.GetColLabelAlignment "Permalink to this definition")
Sets the arguments to the current column label alignment values.


Horizontal alignment will be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment will be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Return type
*tuple*



Returns
( *horiz*, *vert* )






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelSize(self) -> int:
        """ 

`GetColLabelSize`(*self*)[¶](#wx.grid.Grid.GetColLabelSize "Permalink to this definition")
Returns the current height of the column labels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelTextOrientation(self) -> int:
        """ 

`GetColLabelTextOrientation`(*self*)[¶](#wx.grid.Grid.GetColLabelTextOrientation "Permalink to this definition")
Returns the orientation of the column labels (either `HORIZONTAL` or `VERTICAL` ).



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ 

`GetColLabelValue`(*self*, *col*)[¶](#wx.grid.Grid.GetColLabelValue "Permalink to this definition")
Returns the specified column label.


The default grid table class provides column labels of the form A,B…Z,AA,AB…ZZ,AAA… If you are using a custom grid table you can override [`wx.grid.GridTableBase.GetColLabelValue`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.GetColLabelValue "wx.grid.GridTableBase.GetColLabelValue") to provide your own labels.



Parameters
**col** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColLeft(self, col: int) -> int:
        """ 

`GetColLeft`(*self*, *col*)[¶](#wx.grid.Grid.GetColLeft "Permalink to this definition")
Returns the coordinate of the left border specified column.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColMinimalAcceptableWidth(self) -> int:
        """ 

`GetColMinimalAcceptableWidth`(*self*)[¶](#wx.grid.Grid.GetColMinimalAcceptableWidth "Permalink to this definition")
Returns the minimal width to which a column may be resized.


Use [`SetColMinimalAcceptableWidth`](#wx.grid.Grid.SetColMinimalAcceptableWidth "wx.grid.Grid.SetColMinimalAcceptableWidth") to change this value globally or [`SetColMinimalWidth`](#wx.grid.Grid.SetColMinimalWidth "wx.grid.Grid.SetColMinimalWidth") to do it for individual columns.



Return type
*int*





See also


[`GetRowMinimalAcceptableHeight`](#wx.grid.Grid.GetRowMinimalAcceptableHeight "wx.grid.Grid.GetRowMinimalAcceptableHeight")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColMinimalWidth(self, col: int) -> int:
        """ 

`GetColMinimalWidth`(*self*, *col*)[¶](#wx.grid.Grid.GetColMinimalWidth "Permalink to this definition")
Get the minimal width of the given column/row.


The value returned by this function may be different from that returned by [`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth") if [`SetColMinimalWidth`](#wx.grid.Grid.SetColMinimalWidth "wx.grid.Grid.SetColMinimalWidth") had been called for this column.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColPos(self, colID: int) -> int:
        """ 

`GetColPos`(*self*, *colID*)[¶](#wx.grid.Grid.GetColPos "Permalink to this definition")
Returns the position of the specified column.



Parameters
**colID** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColRight(self, col: int) -> int:
        """ 

`GetColRight`(*self*, *col*)[¶](#wx.grid.Grid.GetColRight "Permalink to this definition")
Returns the coordinate of the right border specified column.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColSize(self, col: int) -> int:
        """ 

`GetColSize`(*self*, *col*)[¶](#wx.grid.Grid.GetColSize "Permalink to this definition")
Returns the width of the specified column.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetColSizes(self) -> 'GridSizesInfo':
        """ 

`GetColSizes`(*self*)[¶](#wx.grid.Grid.GetColSizes "Permalink to this definition")
Get size information for all columns at once.


This method is useful when the information about all column widths needs to be saved. The widths can be later restored using [`SetColSizes`](#wx.grid.Grid.SetColSizes "wx.grid.Grid.SetColSizes") .



Return type
 [wx.grid.GridSizesInfo](wx.grid.GridSizesInfo.html#wx-grid-gridsizesinfo)





See also


 [wx.grid.GridSizesInfo](wx.grid.GridSizesInfo.html#wx-grid-gridsizesinfo), [`GetRowSizes`](#wx.grid.Grid.GetRowSizes "wx.grid.Grid.GetRowSizes")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelAlignment(self, horiz, vert) -> None:
        """ 

`GetCornerLabelAlignment`(*self*, *horiz*, *vert*)[¶](#wx.grid.Grid.GetCornerLabelAlignment "Permalink to this definition")
Sets the arguments to the current corner label alignment values.


Horizontal alignment will be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment will be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **horiz** (*int*) –
* **vert** (*int*) –





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelTextOrientation(self) -> int:
        """ 

`GetCornerLabelTextOrientation`(*self*)[¶](#wx.grid.Grid.GetCornerLabelTextOrientation "Permalink to this definition")
Returns the orientation of the corner label (either `HORIZONTAL` or `VERTICAL` ).



Return type
*int*





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetCornerLabelValue(self) -> str:
        """ 

`GetCornerLabelValue`(*self*)[¶](#wx.grid.Grid.GetCornerLabelValue "Permalink to this definition")
Returns the (top-left) corner label.



Return type
`string`





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellAlignment(self) -> tuple:
        """ 

`GetDefaultCellAlignment`(*self*)[¶](#wx.grid.Grid.GetDefaultCellAlignment "Permalink to this definition")
Returns the default cell alignment.


Horizontal alignment will be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment will be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Return type
*tuple*



Returns
( *horiz*, *vert* )





See also


[`SetDefaultCellAlignment`](#wx.grid.Grid.SetDefaultCellAlignment "wx.grid.Grid.SetDefaultCellAlignment")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellBackgroundColour(self) -> 'Colour':
        """ 

`GetDefaultCellBackgroundColour`(*self*)[¶](#wx.grid.Grid.GetDefaultCellBackgroundColour "Permalink to this definition")
Returns the current default background colour for grid cells.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellFitMode(self) -> 'GridFitMode':
        """ 

`GetDefaultCellFitMode`(*self*)[¶](#wx.grid.Grid.GetDefaultCellFitMode "Permalink to this definition")
Returns the default cell fitting mode.


The default mode is “overflow”, but can be modified using [`SetDefaultCellFitMode`](#wx.grid.Grid.SetDefaultCellFitMode "wx.grid.Grid.SetDefaultCellFitMode") .



Return type
 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





New in version 4.1/wxWidgets-3.1.4.




See also


 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellFont(self) -> 'Font':
        """ 

`GetDefaultCellFont`(*self*)[¶](#wx.grid.Grid.GetDefaultCellFont "Permalink to this definition")
Returns the current default font for grid cell text.



Return type
`Font`






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellOverflow(self) -> bool:
        """ 

`GetDefaultCellOverflow`(*self*)[¶](#wx.grid.Grid.GetDefaultCellOverflow "Permalink to this definition")
Returns `True` if the cells can overflow by default.


This is identical to calling [`GetDefaultCellFitMode`](#wx.grid.Grid.GetDefaultCellFitMode "wx.grid.Grid.GetDefaultCellFitMode") and using [`wx.grid.GridFitMode.IsOverflow`](wx.grid.GridFitMode.html#wx.grid.GridFitMode.IsOverflow "wx.grid.GridFitMode.IsOverflow") on the returned value.


Prefer using [`GetDefaultCellFitMode`](#wx.grid.Grid.GetDefaultCellFitMode "wx.grid.Grid.GetDefaultCellFitMode") directly in the new code.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultCellTextColour(self) -> 'Colour':
        """ 

`GetDefaultCellTextColour`(*self*)[¶](#wx.grid.Grid.GetDefaultCellTextColour "Permalink to this definition")
Returns the current default colour for grid cell text.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultColLabelSize(self) -> int:
        """ 

`GetDefaultColLabelSize`(*self*)[¶](#wx.grid.Grid.GetDefaultColLabelSize "Permalink to this definition")
Returns the default height for column labels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultColSize(self) -> int:
        """ 

`GetDefaultColSize`(*self*)[¶](#wx.grid.Grid.GetDefaultColSize "Permalink to this definition")
Returns the current default width for grid columns.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditor(self) -> 'GridCellEditor':
        """ 

`GetDefaultEditor`(*self*)[¶](#wx.grid.Grid.GetDefaultEditor "Permalink to this definition")
Returns a pointer to the current default grid cell editor.


See  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditorForCell(self, *args, **kw) -> 'GridCellEditor':
        """ 

`GetDefaultEditorForCell`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.GetDefaultEditorForCell "Permalink to this definition")
Returns the default editor for the specified cell.


The base class version returns the editor appropriate for the current cell type but this method may be overridden in the derived classes to use custom editors for some cells by default.


Notice that the same may be achieved in a usually simpler way by associating a custom editor with the given cell or cells.


The caller must call DecRef() on the returned pointer.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetDefaultEditorForCell** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






---

  



**GetDefaultEditorForCell** *(self, c)*



Parameters
**c** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultEditorForType(self, typeName: str) -> 'GridCellEditor':
        """ 

`GetDefaultEditorForType`(*self*, *typeName*)[¶](#wx.grid.Grid.GetDefaultEditorForType "Permalink to this definition")
Returns the default editor for the cells containing values of the given type.


The base class version returns the editor which was associated with the specified *typeName* when it was registered [`RegisterDataType`](#wx.grid.Grid.RegisterDataType "wx.grid.Grid.RegisterDataType") but this function may be overridden to return something different. This allows overriding an editor used for one of the standard types.


The caller must call DecRef() on the returned pointer.



Parameters
**typeName** (*string*) – 



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultGridLinePen(self) -> 'Pen':
        """ 

`GetDefaultGridLinePen`(*self*)[¶](#wx.grid.Grid.GetDefaultGridLinePen "Permalink to this definition")
Returns the pen used for grid lines.


This virtual function may be overridden in derived classes in order to change the appearance of grid lines. Note that currently the pen width must be 1.



Return type
*Pen*





See also


[`GetColGridLinePen`](#wx.grid.Grid.GetColGridLinePen "wx.grid.Grid.GetColGridLinePen") , [`GetRowGridLinePen`](#wx.grid.Grid.GetRowGridLinePen "wx.grid.Grid.GetRowGridLinePen")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRenderer(self) -> 'GridCellRenderer':
        """ 

`GetDefaultRenderer`(*self*)[¶](#wx.grid.Grid.GetDefaultRenderer "Permalink to this definition")
Returns a pointer to the current default grid cell renderer.


See  [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.


The caller must call DecRef() on the returned pointer.



Return type
 [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRendererForCell(self, row, col) -> 'GridCellRenderer':
        """ 

`GetDefaultRendererForCell`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetDefaultRendererForCell "Permalink to this definition")
Returns the default renderer for the given cell.


The base class version returns the renderer appropriate for the current cell type but this method may be overridden in the derived classes to use custom renderers for some cells by default.


The caller must call DecRef() on the returned pointer.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRendererForType(self, typeName: str) -> 'GridCellRenderer':
        """ 

`GetDefaultRendererForType`(*self*, *typeName*)[¶](#wx.grid.Grid.GetDefaultRendererForType "Permalink to this definition")
Returns the default renderer for the cell containing values of the given type.



Parameters
**typeName** (*string*) – 



Return type
 [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer)





See also


[`GetDefaultEditorForType`](#wx.grid.Grid.GetDefaultEditorForType "wx.grid.Grid.GetDefaultEditorForType")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRowLabelSize(self) -> int:
        """ 

`GetDefaultRowLabelSize`(*self*)[¶](#wx.grid.Grid.GetDefaultRowLabelSize "Permalink to this definition")
Returns the default width for the row labels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetDefaultRowSize(self) -> int:
        """ 

`GetDefaultRowSize`(*self*)[¶](#wx.grid.Grid.GetDefaultRowSize "Permalink to this definition")
Returns the current default height for grid rows.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFirstFullyVisibleColumn(self) -> int:
        """ 

`GetFirstFullyVisibleColumn`(*self*)[¶](#wx.grid.Grid.GetFirstFullyVisibleColumn "Permalink to this definition")
Returns the leftmost column of the current visible area.


Returns -1 if the grid doesn’t have any columns.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFirstFullyVisibleRow(self) -> int:
        """ 

`GetFirstFullyVisibleRow`(*self*)[¶](#wx.grid.Grid.GetFirstFullyVisibleRow "Permalink to this definition")
Returns the topmost row of the current visible area.


Returns -1 if the grid doesn’t have any rows.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenColGridWindow(self) -> 'Window':
        """ 

`GetFrozenColGridWindow`(*self*)[¶](#wx.grid.Grid.GetFrozenColGridWindow "Permalink to this definition")
Return the columns grid window containing column frozen cells.


This window is shown only when there are frozen columns.



Return type
*Window*





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenCornerGridWindow(self) -> 'Window':
        """ 

`GetFrozenCornerGridWindow`(*self*)[¶](#wx.grid.Grid.GetFrozenCornerGridWindow "Permalink to this definition")
Return the corner grid window containing frozen cells.


This window is shown only when there are frozen rows and columns.



Return type
*Window*





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetFrozenRowGridWindow(self) -> 'Window':
        """ 

`GetFrozenRowGridWindow`(*self*)[¶](#wx.grid.Grid.GetFrozenRowGridWindow "Permalink to this definition")
Return the rows grid window containing row frozen cells.


This window is shown only when there are frozen rows.



Return type
*Window*





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridColHeader(self) -> 'HeaderCtrl':
        """ 

`GetGridColHeader`(*self*)[¶](#wx.grid.Grid.GetGridColHeader "Permalink to this definition")
Return the header control used for column labels display.


This function can only be called if [`UseNativeColHeader`](#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader") had been called.



Return type
*HeaderCtrl*





See also


[`IsUsingNativeHeader`](#wx.grid.Grid.IsUsingNativeHeader "wx.grid.Grid.IsUsingNativeHeader")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridColLabelWindow(self) -> 'Window':
        """ 

`GetGridColLabelWindow`(*self*)[¶](#wx.grid.Grid.GetGridColLabelWindow "Permalink to this definition")
Return the column labels window.


This window is not shown if the columns labels were hidden using [`HideColLabels`](#wx.grid.Grid.HideColLabels "wx.grid.Grid.HideColLabels") .


Depending on whether [`UseNativeColHeader`](#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader") was called or not this can be either a  [wx.HeaderCtrl](wx.HeaderCtrl.html#wx-headerctrl) or a plain  [wx.Window](wx.Window.html#wx-window). This function returns a valid window pointer in either case but in the former case you can also use [`GetGridColHeader`](#wx.grid.Grid.GetGridColHeader "wx.grid.Grid.GetGridColHeader") to access it if you need HeaderCtrl-specific functionality.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCornerLabelWindow(self) -> 'Window':
        """ 

`GetGridCornerLabelWindow`(*self*)[¶](#wx.grid.Grid.GetGridCornerLabelWindow "Permalink to this definition")
Return the window in the top left grid corner.


This window is shown only of both columns and row labels are shown and normally doesn’t contain anything. Clicking on it is handled by  [wx.grid.Grid](#wx-grid-grid) however and can be used to select the entire grid.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorCol(self) -> int:
        """ 

`GetGridCursorCol`(*self*)[¶](#wx.grid.Grid.GetGridCursorCol "Permalink to this definition")
Returns the current grid cell column position.



Return type
*int*





See also


[`GetGridCursorCoords`](#wx.grid.Grid.GetGridCursorCoords "wx.grid.Grid.GetGridCursorCoords")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorCoords(self) -> 'GridCellCoords':
        """ 

`GetGridCursorCoords`(*self*)[¶](#wx.grid.Grid.GetGridCursorCoords "Permalink to this definition")
Returns the current grid cursor position.


If grid cursor doesn’t have any valid position (e.g. if the grid is completely empty and doesn’t have any rows or columns), returns `GridNoCellCoords` which has both row and columns set to `-1` .



Return type
 [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords)





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridCursorRow(self) -> int:
        """ 

`GetGridCursorRow`(*self*)[¶](#wx.grid.Grid.GetGridCursorRow "Permalink to this definition")
Returns the current grid cell row position.



Return type
*int*





See also


[`GetGridCursorCoords`](#wx.grid.Grid.GetGridCursorCoords "wx.grid.Grid.GetGridCursorCoords")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridLineColour(self) -> 'Colour':
        """ 

`GetGridLineColour`(*self*)[¶](#wx.grid.Grid.GetGridLineColour "Permalink to this definition")
Returns the colour used for grid lines.



Return type
*Colour*





See also


[`GetDefaultGridLinePen`](#wx.grid.Grid.GetDefaultGridLinePen "wx.grid.Grid.GetDefaultGridLinePen")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridRowLabelWindow(self) -> 'Window':
        """ 

`GetGridRowLabelWindow`(*self*)[¶](#wx.grid.Grid.GetGridRowLabelWindow "Permalink to this definition")
Return the row labels window.


This window is not shown if the row labels were hidden using [`HideRowLabels`](#wx.grid.Grid.HideRowLabels "wx.grid.Grid.HideRowLabels") .



Return type
*Window*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridWindow(self) -> 'Window':
        """ 

`GetGridWindow`(*self*)[¶](#wx.grid.Grid.GetGridWindow "Permalink to this definition")
Return the main grid window containing the grid cells.


This window is always shown.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetGridWindowOffset(self, gridWindow: 'grid.GridWindow') -> 'Point':
        """ 

`GetGridWindowOffset`(*self*, *gridWindow*)[¶](#wx.grid.Grid.GetGridWindowOffset "Permalink to this definition")
This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
**gridWindow** (*wx.grid.GridWindow*) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelBackgroundColour(self) -> 'Colour':
        """ 

`GetLabelBackgroundColour`(*self*)[¶](#wx.grid.Grid.GetLabelBackgroundColour "Permalink to this definition")
Returns the colour used for the background of row and column labels.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelFont(self) -> 'Font':
        """ 

`GetLabelFont`(*self*)[¶](#wx.grid.Grid.GetLabelFont "Permalink to this definition")
Returns the font used for row and column labels.



Return type
`Font`






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetLabelTextColour(self) -> 'Colour':
        """ 

`GetLabelTextColour`(*self*)[¶](#wx.grid.Grid.GetLabelTextColour "Permalink to this definition")
Returns the colour used for row and column label text.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberCols(self) -> int:
        """ 

`GetNumberCols`(*self*)[¶](#wx.grid.Grid.GetNumberCols "Permalink to this definition")
Returns the total number of grid columns.


This is the same as the number of columns in the underlying grid table.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberFrozenCols(self) -> int:
        """ 

`GetNumberFrozenCols`(*self*)[¶](#wx.grid.Grid.GetNumberFrozenCols "Permalink to this definition")
Returns the number of frozen grid columns.


If there are no frozen columns, returns 0.



Return type
*int*





New in version 4.1/wxWidgets-3.1.3.




See also


[`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberFrozenRows(self) -> int:
        """ 

`GetNumberFrozenRows`(*self*)[¶](#wx.grid.Grid.GetNumberFrozenRows "Permalink to this definition")
Returns the number of frozen grid rows.


If there are no frozen rows, returns 0.



Return type
*int*





New in version 4.1/wxWidgets-3.1.3.




See also


[`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetNumberRows(self) -> int:
        """ 

`GetNumberRows`(*self*)[¶](#wx.grid.Grid.GetNumberRows "Permalink to this definition")
Returns the total number of grid rows.


This is the same as the number of rows in the underlying grid table.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetOrCreateCellAttr(self, row, col) -> 'GridCellAttr':
        """ 

`GetOrCreateCellAttr`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetOrCreateCellAttr "Permalink to this definition")
Returns the attribute for the given cell creating one if necessary.


If the cell already has an attribute, it is returned. Otherwise a new attribute is created, associated with the cell and returned. In any case the caller must call DecRef() on the returned pointer.


Prefer to use [`GetOrCreateCellAttrPtr`](#wx.grid.Grid.GetOrCreateCellAttrPtr "wx.grid.Grid.GetOrCreateCellAttrPtr") to avoid the need to call DecRef() on the returned pointer.


This function may only be called if [`CanHaveAttributes`](#wx.grid.Grid.CanHaveAttributes "wx.grid.Grid.CanHaveAttributes") returns `True`.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetOrCreateCellAttrPtr(self, row, col) -> 'GridCellAttrPtr':
        """ 

`GetOrCreateCellAttrPtr`(*self*, *row*, *col*)[¶](#wx.grid.Grid.GetOrCreateCellAttrPtr "Permalink to this definition")
Returns the attribute for the given cell creating one if necessary.


This method is identical to [`GetOrCreateCellAttr`](#wx.grid.Grid.GetOrCreateCellAttr "wx.grid.Grid.GetOrCreateCellAttr") , but returns a smart pointer, which frees the caller from the need to call DecRef() manually.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`wx.grid.GridCellAttrPtr`





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowAt(self, rowPos: int) -> int:
        """ 

`GetRowAt`(*self*, *rowPos*)[¶](#wx.grid.Grid.GetRowAt "Permalink to this definition")
Returns the row `ID` of the specified row position.



Parameters
**rowPos** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowGridLinePen(self, row: int) -> 'Pen':
        """ 

`GetRowGridLinePen`(*self*, *row*)[¶](#wx.grid.Grid.GetRowGridLinePen "Permalink to this definition")
Returns the pen used for horizontal grid lines.


This virtual function may be overridden in derived classes in order to change the appearance of individual grid line for the given *row*.


Example:



```
# in a grid displaying music notation, use a solid black pen between
# octaves (C0=row 127, C1=row 115 etc.)
def GetRowGridLinePen(self, row):

    if row % 12 == 7:
        return wx.Pen(wx.BLACK, 1, wx.SOLID)
    else:
        return self.GetDefaultGridLinePen()

```



Parameters
**row** (*int*) – 



Return type
*Pen*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelAlignment(self) -> tuple:
        """ 

`GetRowLabelAlignment`(*self*)[¶](#wx.grid.Grid.GetRowLabelAlignment "Permalink to this definition")
Returns the alignment used for row labels.


Horizontal alignment will be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment will be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Return type
*tuple*



Returns
( *horiz*, *vert* )






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelSize(self) -> int:
        """ 

`GetRowLabelSize`(*self*)[¶](#wx.grid.Grid.GetRowLabelSize "Permalink to this definition")
Returns the current width of the row labels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ 

`GetRowLabelValue`(*self*, *row*)[¶](#wx.grid.Grid.GetRowLabelValue "Permalink to this definition")
Returns the specified row label.


The default grid table class provides numeric row labels. If you are using a custom grid table you can override [`wx.grid.GridTableBase.GetRowLabelValue`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.GetRowLabelValue "wx.grid.GridTableBase.GetRowLabelValue") to provide your own labels.



Parameters
**row** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowMinimalAcceptableHeight(self) -> int:
        """ 

`GetRowMinimalAcceptableHeight`(*self*)[¶](#wx.grid.Grid.GetRowMinimalAcceptableHeight "Permalink to this definition")
Returns the minimal size to which rows can be resized.


Use [`SetRowMinimalAcceptableHeight`](#wx.grid.Grid.SetRowMinimalAcceptableHeight "wx.grid.Grid.SetRowMinimalAcceptableHeight") to change this value globally or [`SetRowMinimalHeight`](#wx.grid.Grid.SetRowMinimalHeight "wx.grid.Grid.SetRowMinimalHeight") to do it for individual cells.



Return type
*int*





See also


[`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowMinimalHeight(self, col: int) -> int:
        """ 

`GetRowMinimalHeight`(*self*, *col*)[¶](#wx.grid.Grid.GetRowMinimalHeight "Permalink to this definition")
Returns the minimal size for the given column.


The value returned by this function may be different from that returned by [`GetRowMinimalAcceptableHeight`](#wx.grid.Grid.GetRowMinimalAcceptableHeight "wx.grid.Grid.GetRowMinimalAcceptableHeight") if [`SetRowMinimalHeight`](#wx.grid.Grid.SetRowMinimalHeight "wx.grid.Grid.SetRowMinimalHeight") had been called for this row.



Parameters
**col** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowPos(self, rowID: int) -> int:
        """ 

`GetRowPos`(*self*, *rowID*)[¶](#wx.grid.Grid.GetRowPos "Permalink to this definition")
Returns the position of the specified row.



Parameters
**rowID** (*int*) – 



Return type
*int*





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowSize(self, row: int) -> int:
        """ 

`GetRowSize`(*self*, *row*)[¶](#wx.grid.Grid.GetRowSize "Permalink to this definition")
Returns the height of the specified row.



Parameters
**row** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetRowSizes(self) -> 'GridSizesInfo':
        """ 

`GetRowSizes`(*self*)[¶](#wx.grid.Grid.GetRowSizes "Permalink to this definition")
Get size information for all row at once.



Return type
 [wx.grid.GridSizesInfo](wx.grid.GridSizesInfo.html#wx-grid-gridsizesinfo)





See also


 [wx.grid.GridSizesInfo](wx.grid.GridSizesInfo.html#wx-grid-gridsizesinfo), [`GetColSizes`](#wx.grid.Grid.GetColSizes "wx.grid.Grid.GetColSizes")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetScrollLineX(self) -> int:
        """ 

`GetScrollLineX`(*self*)[¶](#wx.grid.Grid.GetScrollLineX "Permalink to this definition")
Returns the number of pixels per horizontal scroll increment.


The default is 15.



Return type
*int*





See also


[`GetScrollLineY`](#wx.grid.Grid.GetScrollLineY "wx.grid.Grid.GetScrollLineY") , [`SetScrollLineX`](#wx.grid.Grid.SetScrollLineX "wx.grid.Grid.SetScrollLineX") , [`SetScrollLineY`](#wx.grid.Grid.SetScrollLineY "wx.grid.Grid.SetScrollLineY")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetScrollLineY(self) -> int:
        """ 

`GetScrollLineY`(*self*)[¶](#wx.grid.Grid.GetScrollLineY "Permalink to this definition")
Returns the number of pixels per vertical scroll increment.


The default is 15.



Return type
*int*





See also


[`GetScrollLineX`](#wx.grid.Grid.GetScrollLineX "wx.grid.Grid.GetScrollLineX") , [`SetScrollLineX`](#wx.grid.Grid.SetScrollLineX "wx.grid.Grid.SetScrollLineX") , [`SetScrollLineY`](#wx.grid.Grid.SetScrollLineY "wx.grid.Grid.SetScrollLineY")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedBlocks(self) -> 'GridBlocks':
        """ 

`GetSelectedBlocks`(*self*)[¶](#wx.grid.Grid.GetSelectedBlocks "Permalink to this definition")
Returns a range of grid selection blocks.


The returned range can be iterated over, e.g. with `C++11` range-for loop:



```
# For Python the returned GridBlocks object has a __iter__ method so iterating
# in the Python way is possible.

```



for block in self.grid.GetSelectedBlocks():do\_something(block)




Notice that the blocks returned by this method are not ordered in any particular way and may overlap. For grids using rows or columns-only selection modes, [`GetSelectedRowBlocks`](#wx.grid.Grid.GetSelectedRowBlocks "wx.grid.Grid.GetSelectedRowBlocks") or [`GetSelectedColBlocks`](#wx.grid.Grid.GetSelectedColBlocks "wx.grid.Grid.GetSelectedColBlocks") can be more convenient, as they return ordered and non-overlapping blocks.



Return type
 [wx.grid.GridBlocks](wx.grid.GridBlocks.html#wx-grid-gridblocks)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedCells(self) -> 'GridCellCoordsArray':
        """ 

`GetSelectedCells`(*self*)[¶](#wx.grid.Grid.GetSelectedCells "Permalink to this definition")
Returns an array of individually selected cells.


Notice that this array does *not* contain all the selected cells in general as it doesn’t include the cells selected as part of column, row or block selection. You must use this method, [`GetSelectedCols`](#wx.grid.Grid.GetSelectedCols "wx.grid.Grid.GetSelectedCols") , [`GetSelectedRows`](#wx.grid.Grid.GetSelectedRows "wx.grid.Grid.GetSelectedRows") and [`GetSelectionBlockTopLeft`](#wx.grid.Grid.GetSelectionBlockTopLeft "wx.grid.Grid.GetSelectionBlockTopLeft") and [`GetSelectionBlockBottomRight`](#wx.grid.Grid.GetSelectionBlockBottomRight "wx.grid.Grid.GetSelectionBlockBottomRight") methods to obtain the entire selection in general.


Please notice this behaviour is by design and is needed in order to support grids of arbitrary size (when an entire column is selected in a grid with a million of columns, we don’t want to create an array with a million of entries in this function, instead it returns an empty array and [`GetSelectedCols`](#wx.grid.Grid.GetSelectedCols "wx.grid.Grid.GetSelectedCols") returns an array containing one element).


The function can be slow for the big grids, use [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") in the new code.



Return type
*GridCellCoordsArray*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedColBlocks(self) -> Any:
        """ 

`GetSelectedColBlocks`(*self*)[¶](#wx.grid.Grid.GetSelectedColBlocks "Permalink to this definition")
Returns an ordered range of non-overlapping selected columns.


This method is symmetric to [`GetSelectedRowBlocks`](#wx.grid.Grid.GetSelectedRowBlocks "wx.grid.Grid.GetSelectedRowBlocks") , but is useful only in GridSelectColumns selection mode.



Return type
*PyObject*





New in version 4.1/wxWidgets-3.1.4.




See also


[`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedCols(self) -> int:
        """ 

`GetSelectedCols`(*self*)[¶](#wx.grid.Grid.GetSelectedCols "Permalink to this definition")
Returns an array of selected columns.


Please notice that this method alone is not sufficient to find all the selected columns as it contains only the columns which were individually selected but not those being part of the block selection or being selected in virtue of all of their cells being selected individually, please see [`GetSelectedCells`](#wx.grid.Grid.GetSelectedCells "wx.grid.Grid.GetSelectedCells") for more details.


The function can be slow for the big grids, use [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") in the new code.



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedRowBlocks(self) -> Any:
        """ 

`GetSelectedRowBlocks`(*self*)[¶](#wx.grid.Grid.GetSelectedRowBlocks "Permalink to this definition")
Returns an ordered range of non-overlapping selected rows.


For the grids using GridSelectRows selection mode, returns the possibly empty vector containing the coordinates of non-overlapping selected row blocks in the natural order, i.e. from smallest to the biggest row indices.


To see the difference between this method and [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") , consider the case when the user selects rows 2..4 in the grid and then also selects (using Ctrl/Shift keys) the rows 1..3. Iterating over the result of [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") would yield two blocks directly corresponding to the users selection, while this method returns a vector with a single element corresponding to the rows 1..4.


This method returns empty vector for the other selection modes.



Return type
*PyObject*





New in version 4.1/wxWidgets-3.1.4.




See also


[`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") , [`GetSelectedColBlocks`](#wx.grid.Grid.GetSelectedColBlocks "wx.grid.Grid.GetSelectedColBlocks")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectedRows(self) -> int:
        """ 

`GetSelectedRows`(*self*)[¶](#wx.grid.Grid.GetSelectedRows "Permalink to this definition")
Returns an array of selected rows.


Please notice that this method alone is not sufficient to find all the selected rows as it contains only the rows which were individually selected but not those being part of the block selection or being selected in virtue of all of their cells being selected individually, please see [`GetSelectedCells`](#wx.grid.Grid.GetSelectedCells "wx.grid.Grid.GetSelectedCells") for more details.


The function can be slow for the big grids, use [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") in the new code.



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBackground(self) -> 'Colour':
        """ 

`GetSelectionBackground`(*self*)[¶](#wx.grid.Grid.GetSelectionBackground "Permalink to this definition")
Returns the colour used for drawing the selection background.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBlockBottomRight(self) -> 'GridCellCoordsArray':
        """ 

`GetSelectionBlockBottomRight`(*self*)[¶](#wx.grid.Grid.GetSelectionBlockBottomRight "Permalink to this definition")
Returns an array of the bottom right corners of blocks of selected cells.


Please see [`GetSelectedCells`](#wx.grid.Grid.GetSelectedCells "wx.grid.Grid.GetSelectedCells") for more information about the selection representation in  [wx.grid.Grid](#wx-grid-grid).


The function can be slow for the big grids, use [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") in the new code.



Return type
*GridCellCoordsArray*





See also


[`GetSelectionBlockTopLeft`](#wx.grid.Grid.GetSelectionBlockTopLeft "wx.grid.Grid.GetSelectionBlockTopLeft")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionBlockTopLeft(self) -> 'GridCellCoordsArray':
        """ 

`GetSelectionBlockTopLeft`(*self*)[¶](#wx.grid.Grid.GetSelectionBlockTopLeft "Permalink to this definition")
Returns an array of the top left corners of blocks of selected cells.


Please see [`GetSelectedCells`](#wx.grid.Grid.GetSelectedCells "wx.grid.Grid.GetSelectedCells") for more information about the selection representation in  [wx.grid.Grid](#wx-grid-grid).


The function can be slow for the big grids, use [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks") in the new code.



Return type
*GridCellCoordsArray*





See also


[`GetSelectionBlockBottomRight`](#wx.grid.Grid.GetSelectionBlockBottomRight "wx.grid.Grid.GetSelectionBlockBottomRight")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionForeground(self) -> 'Colour':
        """ 

`GetSelectionForeground`(*self*)[¶](#wx.grid.Grid.GetSelectionForeground "Permalink to this definition")
Returns the colour used for drawing the selection foreground.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSelectionMode(self) -> 'GridSelectionModes':
        """ 

`GetSelectionMode`(*self*)[¶](#wx.grid.Grid.GetSelectionMode "Permalink to this definition")
Returns the current selection mode.



Return type
 [wx.grid.Grid.GridSelectionModes](wx.grid.Grid.GridSelectionModes.enumeration.html#wx-grid-grid-gridselectionmodes)





See also


[`SetSelectionMode`](#wx.grid.Grid.SetSelectionMode "wx.grid.Grid.SetSelectionMode") .





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetSortingColumn(self) -> int:
        """ 

`GetSortingColumn`(*self*)[¶](#wx.grid.Grid.GetSortingColumn "Permalink to this definition")
Return the column in which the sorting indicator is currently displayed.


Returns `NOT_FOUND` if sorting indicator is not currently displayed at all.



Return type
*int*





See also


[`SetSortingColumn`](#wx.grid.Grid.SetSortingColumn "wx.grid.Grid.SetSortingColumn")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GetTable(self) -> 'GridTableBase':
        """ 

`GetTable`(*self*)[¶](#wx.grid.Grid.GetTable "Permalink to this definition")
Returns a base pointer to the current table object.


The returned pointer is still owned by the grid.



Return type
 [wx.grid.GridTableBase](wx.grid.GridTableBase.html#wx-grid-gridtablebase)






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GoToCell(self, *args, **kw) -> None:
        """ 

`GoToCell`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.GoToCell "Permalink to this definition")
Make the given cell current and ensure it is visible.


This method is equivalent to calling [`MakeCellVisible`](#wx.grid.Grid.MakeCellVisible "wx.grid.Grid.MakeCellVisible") and [`SetGridCursor`](#wx.grid.Grid.SetGridCursor "wx.grid.Grid.SetGridCursor") and so, as with the latter, a `wxEVT_GRID_SELECT_CELL` event is generated by it and the selected cell doesn’t change if the event is vetoed.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GoToCell** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –






---

  



**GoToCell** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def GridLinesEnabled(self) -> bool:
        """ 

`GridLinesEnabled`(*self*)[¶](#wx.grid.Grid.GridLinesEnabled "Permalink to this definition")
Returns `True` if drawing of grid lines is turned on, `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideCellEditControl(self) -> None:
        """ 

`HideCellEditControl`(*self*)[¶](#wx.grid.Grid.HideCellEditControl "Permalink to this definition")
Hides the in-place cell edit control.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideCol(self, col: int) -> None:
        """ 

`HideCol`(*self*, *col*)[¶](#wx.grid.Grid.HideCol "Permalink to this definition")
Hides the specified column.


To show the column later you need to call [`SetColSize`](#wx.grid.Grid.SetColSize "wx.grid.Grid.SetColSize") with non-0 width or [`ShowCol`](#wx.grid.Grid.ShowCol "wx.grid.Grid.ShowCol") to restore the previous column width.


If the column is already hidden, this method doesn’t do anything.



Parameters
**col** (*int*) – The column index.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideColLabels(self) -> None:
        """ 

`HideColLabels`(*self*)[¶](#wx.grid.Grid.HideColLabels "Permalink to this definition")
Hides the column labels by calling [`SetColLabelSize`](#wx.grid.Grid.SetColLabelSize "wx.grid.Grid.SetColLabelSize") with a size of 0.


The labels can be shown again by calling [`SetColLabelSize`](#wx.grid.Grid.SetColLabelSize "wx.grid.Grid.SetColLabelSize") with a height greater than 0.


Note that when the column labels are hidden, the grid won’t have any visible border on the top side, which may result in a less than ideal appearance. Because of this, you may want to create the grid window with a border style, such as `BORDER_SIMPLE` , when you don’t plan to show the column labels for it.



See also


[`HideRowLabels`](#wx.grid.Grid.HideRowLabels "wx.grid.Grid.HideRowLabels")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideRow(self, col: int) -> None:
        """ 

`HideRow`(*self*, *col*)[¶](#wx.grid.Grid.HideRow "Permalink to this definition")
Hides the specified row.


To show the row later you need to call [`SetRowSize`](#wx.grid.Grid.SetRowSize "wx.grid.Grid.SetRowSize") with non-0 width or [`ShowRow`](#wx.grid.Grid.ShowRow "wx.grid.Grid.ShowRow") to restore its original height.


If the row is already hidden, this method doesn’t do anything.



Parameters
**col** (*int*) – The row index.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def HideRowLabels(self) -> None:
        """ 

`HideRowLabels`(*self*)[¶](#wx.grid.Grid.HideRowLabels "Permalink to this definition")
Hides the row labels by calling [`SetRowLabelSize`](#wx.grid.Grid.SetRowLabelSize "wx.grid.Grid.SetRowLabelSize") with a size of 0.


The labels can be shown again by calling [`SetRowLabelSize`](#wx.grid.Grid.SetRowLabelSize "wx.grid.Grid.SetRowLabelSize") with a width greater than 0.


See [`HideColLabels`](#wx.grid.Grid.HideColLabels "wx.grid.Grid.HideColLabels") for a note explaining why you may want to use a border with a grid without the row labels.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def InsertCols(self, pos=0, numCols=1, updateLabels=True) -> bool:
        """ 

`InsertCols`(*self*, *pos=0*, *numCols=1*, *updateLabels=True*)[¶](#wx.grid.Grid.InsertCols "Permalink to this definition")
Inserts one or more new columns into a grid with the first new column at the specified position.


Notice that inserting the columns in the grid requires grid table cooperation: when this method is called, grid object begins by requesting the underlying grid table to insert new columns. If this is successful the table notifies the grid and the grid updates the display. For a default grid (one where you have called [`CreateGrid`](#wx.grid.Grid.CreateGrid "wx.grid.Grid.CreateGrid") ) this process is automatic. If you are using a custom grid table (specified with [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable") or [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") ) then you must override [`wx.grid.GridTableBase.InsertCols`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.InsertCols "wx.grid.GridTableBase.InsertCols") in your derived table class.



Parameters
* **pos** (*int*) – The position which the first newly inserted column will have.
* **numCols** (*int*) – The number of columns to insert.
* **updateLabels** (*bool*) – Currently not used.



Return type
*bool*



Returns
`True` if the columns were successfully inserted, `False` if an error occurred (most likely the table couldn’t be updated).






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def InsertRows(self, pos=0, numRows=1, updateLabels=True) -> bool:
        """ 

`InsertRows`(*self*, *pos=0*, *numRows=1*, *updateLabels=True*)[¶](#wx.grid.Grid.InsertRows "Permalink to this definition")
Inserts one or more new rows into a grid with the first new row at the specified position.


Notice that you must implement [`wx.grid.GridTableBase.InsertRows`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.InsertRows "wx.grid.GridTableBase.InsertRows") if you use a grid with a custom table, please see [`InsertCols`](#wx.grid.Grid.InsertCols "wx.grid.Grid.InsertCols") for more information.



Parameters
* **pos** (*int*) – The position which the first newly inserted row will have.
* **numRows** (*int*) – The number of rows to insert.
* **updateLabels** (*bool*) – Currently not used.



Return type
*bool*



Returns
`True` if the rows were successfully inserted, `False` if an error occurred (most likely the table couldn’t be updated).






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCellEditControlEnabled(self) -> bool:
        """ 

`IsCellEditControlEnabled`(*self*)[¶](#wx.grid.Grid.IsCellEditControlEnabled "Permalink to this definition")
Returns `True` if the in-place edit control is currently enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCellEditControlShown(self) -> bool:
        """ 

`IsCellEditControlShown`(*self*)[¶](#wx.grid.Grid.IsCellEditControlShown "Permalink to this definition")
Returns `True` if the in-place edit control is currently shown.



Return type
*bool*





See also


[`HideCellEditControl`](#wx.grid.Grid.HideCellEditControl "wx.grid.Grid.HideCellEditControl")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsColShown(self, col: int) -> bool:
        """ 

`IsColShown`(*self*, *col*)[¶](#wx.grid.Grid.IsColShown "Permalink to this definition")
Returns `True` if the specified column is not currently hidden.



Parameters
**col** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsCurrentCellReadOnly(self) -> bool:
        """ 

`IsCurrentCellReadOnly`(*self*)[¶](#wx.grid.Grid.IsCurrentCellReadOnly "Permalink to this definition")
Returns `True` if the current cell is read-only.



Return type
*bool*





See also


[`SetReadOnly`](#wx.grid.Grid.SetReadOnly "wx.grid.Grid.SetReadOnly") , [`IsReadOnly`](#wx.grid.Grid.IsReadOnly "wx.grid.Grid.IsReadOnly")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsEditable(self) -> bool:
        """ 

`IsEditable`(*self*)[¶](#wx.grid.Grid.IsEditable "Permalink to this definition")
Returns `False` if the whole grid has been set as read-only or `True` otherwise.


See [`EnableEditing`](#wx.grid.Grid.EnableEditing "wx.grid.Grid.EnableEditing") for more information about controlling the editing status of grid cells.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsInSelection(self, *args, **kw) -> bool:
        """ 

`IsInSelection`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.IsInSelection "Permalink to this definition")
Returns `True` if the given cell is selected.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**IsInSelection** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






---

  



**IsInSelection** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsReadOnly(self, row, col) -> bool:
        """ 

`IsReadOnly`(*self*, *row*, *col*)[¶](#wx.grid.Grid.IsReadOnly "Permalink to this definition")
Returns `True` if the cell at the specified location can’t be edited.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*





See also


[`SetReadOnly`](#wx.grid.Grid.SetReadOnly "wx.grid.Grid.SetReadOnly") , [`IsCurrentCellReadOnly`](#wx.grid.Grid.IsCurrentCellReadOnly "wx.grid.Grid.IsCurrentCellReadOnly")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsRowShown(self, row: int) -> bool:
        """ 

`IsRowShown`(*self*, *row*)[¶](#wx.grid.Grid.IsRowShown "Permalink to this definition")
Returns `True` if the specified row is not currently hidden.



Parameters
**row** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSelection(self) -> bool:
        """ 

`IsSelection`(*self*)[¶](#wx.grid.Grid.IsSelection "Permalink to this definition")
Returns `True` if there are currently any selected cells, rows, columns or blocks.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSortOrderAscending(self) -> bool:
        """ 

`IsSortOrderAscending`(*self*)[¶](#wx.grid.Grid.IsSortOrderAscending "Permalink to this definition")
Return `True` if the current sorting order is ascending or `False` if it is descending.


It only makes sense to call this function if [`GetSortingColumn`](#wx.grid.Grid.GetSortingColumn "wx.grid.Grid.GetSortingColumn") returns a valid column index and not `NOT_FOUND` .



Return type
*bool*





See also


[`SetSortingColumn`](#wx.grid.Grid.SetSortingColumn "wx.grid.Grid.SetSortingColumn")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsSortingBy(self, col: int) -> bool:
        """ 

`IsSortingBy`(*self*, *col*)[¶](#wx.grid.Grid.IsSortingBy "Permalink to this definition")
Return `True` if this column is currently used for sorting.



Parameters
**col** (*int*) – 



Return type
*bool*





See also


[`GetSortingColumn`](#wx.grid.Grid.GetSortingColumn "wx.grid.Grid.GetSortingColumn")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsUsingNativeHeader(self) -> bool:
        """ 

`IsUsingNativeHeader`(*self*)[¶](#wx.grid.Grid.IsUsingNativeHeader "Permalink to this definition")
Return `True` if native header control is currently being used.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def IsVisible(self, *args, **kw) -> bool:
        """ 

`IsVisible`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.IsVisible "Permalink to this definition")
Returns `True` if a cell is either entirely or at least partially visible in the grid window.


By default, the cell must be entirely visible for this function to return `True` but if *wholeCellVisible* is `False`, the function returns `True` even if the cell is only partially visible.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**IsVisible** *(self, row, col, wholeCellVisible=True)*



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **wholeCellVisible** (*bool*) –



Return type
*bool*






---

  



**IsVisible** *(self, coords, wholeCellVisible=True)*



Parameters
* **coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **wholeCellVisible** (*bool*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MakeCellVisible(self, *args, **kw) -> None:
        """ 

`MakeCellVisible`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.MakeCellVisible "Permalink to this definition")
Brings the specified cell into the visible grid cell area with minimal scrolling.


Does nothing if the cell is already visible.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**MakeCellVisible** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –






---

  



**MakeCellVisible** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorDown(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorDown`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorDown "Permalink to this definition")
Moves the grid cursor down by one row.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorDownBlock(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorDownBlock`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorDownBlock "Permalink to this definition")
Moves the grid cursor down in the current column such that it skips to the beginning or end of a block of non-empty cells.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorLeft(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorLeft`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorLeft "Permalink to this definition")
Moves the grid cursor left by one column.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorLeftBlock(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorLeftBlock`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorLeftBlock "Permalink to this definition")
Moves the grid cursor left in the current row such that it skips to the beginning or end of a block of non-empty cells.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorRight(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorRight`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorRight "Permalink to this definition")
Moves the grid cursor right by one column.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorRightBlock(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorRightBlock`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorRightBlock "Permalink to this definition")
Moves the grid cursor right in the current row such that it skips to the beginning or end of a block of non-empty cells.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorUp(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorUp`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorUp "Permalink to this definition")
Moves the grid cursor up by one row.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MoveCursorUpBlock(self, expandSelection: bool) -> bool:
        """ 

`MoveCursorUpBlock`(*self*, *expandSelection*)[¶](#wx.grid.Grid.MoveCursorUpBlock "Permalink to this definition")
Moves the grid cursor up in the current column such that it skips to the beginning or end of a block of non-empty cells.


If a block of cells was previously selected it will expand if the argument is `True` or be cleared if the argument is `False`.



Parameters
**expandSelection** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MovePageDown(self) -> bool:
        """ 

`MovePageDown`(*self*)[¶](#wx.grid.Grid.MovePageDown "Permalink to this definition")
Moves the grid cursor down by some number of rows so that the previous bottom visible row becomes the top visible row.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def MovePageUp(self) -> bool:
        """ 

`MovePageUp`(*self*)[¶](#wx.grid.Grid.MovePageUp "Permalink to this definition")
Moves the grid cursor up by some number of rows so that the previous top visible row becomes the bottom visible row.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ProcessTableMessage(self, msg: 'grid.GridTableMessage') -> bool:
        """ 

`ProcessTableMessage`(*self*, *msg*)[¶](#wx.grid.Grid.ProcessTableMessage "Permalink to this definition")
Receive and handle a message from the table.



Parameters
**msg** ([*wx.grid.GridTableMessage*](wx.grid.GridTableMessage.html#wx.grid.GridTableMessage "wx.grid.GridTableMessage")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def RefreshAttr(self, row, col) -> None:
        """ 

`RefreshAttr`(*self*, *row*, *col*)[¶](#wx.grid.Grid.RefreshAttr "Permalink to this definition")
Invalidates the cached attribute for the given cell.


For efficiency reasons,  [wx.grid.Grid](#wx-grid-grid) may cache the recently used attributes (currently it caches only the single most recently used one, in fact) which can result in the cell appearance not being refreshed even when the attribute returned by your custom GridCellAttrProvider-derived class has changed. To force the grid to refresh the cell attribute, this function may be used. Notice that calling it will not result in actually redrawing the cell, you still need to call [`wx.Window.RefreshRect`](wx.Window.html#wx.Window.RefreshRect "wx.Window.RefreshRect") to invalidate the area occupied by the cell in the window to do this. Also note that you don’t need to call this function if you store the attributes in  [wx.grid.Grid](#wx-grid-grid) itself, i.e. use its [`SetAttr`](#wx.grid.Grid.SetAttr "wx.grid.Grid.SetAttr") and similar methods, it is only useful when using a separate custom attributes provider.



Parameters
* **row** (*int*) – The row of the cell whose attribute needs to be queried again.
* **col** (*int*) – The column of the cell whose attribute needs to be queried again.





New in version 2.9.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def RefreshBlock(self, *args, **kw) -> None:
        """ 

`RefreshBlock`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.RefreshBlock "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**RefreshBlock** *(self, topLeft, bottomRight)*


Redraw all the cells in the given block.


Refresh the block of cells with the given corners.


If the bottom right corner coordinates are invalid, i.e. set to `-1` , the top left corner coordinates are used for it, i.e. just a single cell is refreshed. If the top left corner coordinates are invalid as well, the function simply returns without doing anything. Note, however, that both coordinates need to be valid or invalid simultaneously, i.e. setting the top row to `-1` but using a valid value for the left column is unsupported and would result in an assertion failure.



Parameters
* **topLeft** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **bottomRight** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –





New in version 4.1/wxWidgets-3.1.3.





---

  



**RefreshBlock** *(self, topRow, leftCol, bottomRow, rightCol)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **topRow** (*int*) –
* **leftCol** (*int*) –
* **bottomRow** (*int*) –
* **rightCol** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def RegisterDataType(self, typeName, renderer, editor) -> None:
        """ 

`RegisterDataType`(*self*, *typeName*, *renderer*, *editor*)[¶](#wx.grid.Grid.RegisterDataType "Permalink to this definition")
Register a new data type.


The data types allow to naturally associate specific renderers and editors to the cells containing values of the given type. For example, the grid automatically registers a data type with the name `GRID_VALUE_STRING` which uses  [wx.grid.GridCellStringRenderer](wx.grid.GridCellStringRenderer.html#wx-grid-gridcellstringrenderer) and  [wx.grid.GridCellTextEditor](wx.grid.GridCellTextEditor.html#wx-grid-gridcelltexteditor) as its renderer and editor respectively – this is the data type used by all the cells of the default  [wx.grid.GridStringTable](wx.grid.GridStringTable.html#wx-grid-gridstringtable), so this renderer and editor are used by default for all grid cells.


However if a custom table returns `GRID_VALUE_BOOL` from its [`wx.grid.GridTableBase.GetTypeName`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.GetTypeName "wx.grid.GridTableBase.GetTypeName") method, then  [wx.grid.GridCellBoolRenderer](wx.grid.GridCellBoolRenderer.html#wx-grid-gridcellboolrenderer) and  [wx.grid.GridCellBoolEditor](wx.grid.GridCellBoolEditor.html#wx-grid-gridcellbooleditor) are used for it because the grid also registers a boolean data type with this name.


And as this mechanism is completely generic, you may register your own data types using your own custom renderers and editors. Just remember that the table must identify a cell as being of the given type for them to be used for this cell.



Parameters
* **typeName** (*string*) – Name of the new type. May be any string, but if the type name is the same as the name of an already registered type, including one of the standard ones (which are `GRID_VALUE_STRING` , `GRID_VALUE_BOOL` , `GRID_VALUE_NUMBER` , `GRID_VALUE_FLOAT` , `GRID_VALUE_CHOICE` and `GRID_VALUE_DATE` ), then the new registration information replaces the previously used renderer and editor.
* **renderer** ([*wx.grid.GridCellRenderer*](wx.grid.GridCellRenderer.html#wx.grid.GridCellRenderer "wx.grid.GridCellRenderer")) – The renderer to use for the cells of this type. Its ownership is taken by the grid, i.e. it will call DecRef() on this pointer when it doesn’t need it any longer.
* **editor** ([*wx.grid.GridCellEditor*](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor "wx.grid.GridCellEditor")) – The editor to use for the cells of this type. Its ownership is also taken by the grid.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def Render(*args, **kwargs) -> None:
        """ 

`Render`(*self*, *dc*, *pos=DefaultPosition*, *size=DefaultSize*, *topLeft=GridCellCoords(-1*, *-1)*, *bottomRight=GridCellCoords(-1*, *-1)*, *style=GRID\_DRAW\_DEFAULT*)[¶](#wx.grid.Grid.Render "Permalink to this definition")
Draws part or all of a  [wx.grid.Grid](#wx-grid-grid) on a  [wx.DC](wx.DC.html#wx-dc) for printing or display.


Pagination can be accomplished by using sequential [`Render`](#wx.grid.Grid.Render "wx.grid.Grid.Render") calls with appropriate values in  [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords) topLeft and bottomRight.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The  [wx.DC](wx.DC.html#wx-dc) to be drawn on.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The position on the  [wx.DC](wx.DC.html#wx-dc) where rendering should begin. If not specified drawing will begin at the  [wx.DC](wx.DC.html#wx-dc) MaxX() and MaxY().
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The size of the area on the  [wx.DC](wx.DC.html#wx-dc) that the rendered  [wx.grid.Grid](#wx-grid-grid) should occupy. If not specified the drawing will be scaled to fit the available dc width or height. The  [wx.grid.Grid](#wx-grid-grid)’s aspect ratio is maintained whether or not size is specified.
* **topLeft** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – The top left cell of the block to be drawn. Defaults to ( 0, 0 ).
* **bottomRight** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – The bottom right cell of the block to be drawn. Defaults to row and column counts.
* **style** (*int*) – A combination of values from GridRenderStyle.





New in version 2.9.4.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ResetColPos(self) -> None:
        """ 

`ResetColPos`(*self*)[¶](#wx.grid.Grid.ResetColPos "Permalink to this definition")
Resets the position of the columns to the default.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ResetRowPos(self) -> None:
        """ 

`ResetRowPos`(*self*)[¶](#wx.grid.Grid.ResetRowPos "Permalink to this definition")
Resets the position of the rows to the default.



New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SaveEditControlValue(self) -> None:
        """ 

`SaveEditControlValue`(*self*)[¶](#wx.grid.Grid.SaveEditControlValue "Permalink to this definition")
Sets the value of the current grid cell to the current in-place edit control value.


This is called automatically when the grid cursor moves from the current cell to a new cell. It is also a good idea to call this function when closing a grid since any edits to the final cell location will not be saved otherwise.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.grid.Grid.SelectAll "Permalink to this definition")
Selects all cells in the grid.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectBlock(self, *args, **kw) -> None:
        """ 

`SelectBlock`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.SelectBlock "Permalink to this definition")
Selects a rectangular block of cells.


If *addToSelected* is `False` then any existing selection will be deselected; if `True` the column will be added to the existing selection.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SelectBlock** *(self, topRow, leftCol, bottomRow, rightCol, addToSelected=False)*



Parameters
* **topRow** (*int*) –
* **leftCol** (*int*) –
* **bottomRow** (*int*) –
* **rightCol** (*int*) –
* **addToSelected** (*bool*) –






---

  



**SelectBlock** *(self, topLeft, bottomRight, addToSelected=False)*



Parameters
* **topLeft** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **bottomRight** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **addToSelected** (*bool*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectCol(self, col, addToSelected=False) -> None:
        """ 

`SelectCol`(*self*, *col*, *addToSelected=False*)[¶](#wx.grid.Grid.SelectCol "Permalink to this definition")
Selects the specified column.


If *addToSelected* is `False` then any existing selection will be deselected; if `True` the column will be added to the existing selection.


This method won’t select anything if the current selection mode is GridSelectRows.



Parameters
* **col** (*int*) –
* **addToSelected** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SelectRow(self, row, addToSelected=False) -> None:
        """ 

`SelectRow`(*self*, *row*, *addToSelected=False*)[¶](#wx.grid.Grid.SelectRow "Permalink to this definition")
Selects the specified row.


If *addToSelected* is `False` then any existing selection will be deselected; if `True` the row will be added to the existing selection.


This method won’t select anything if the current selection mode is GridSelectColumns.



Parameters
* **row** (*int*) –
* **addToSelected** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetAttr(self, row, col, attr) -> None:
        """ 

`SetAttr`(*self*, *row*, *col*, *attr*)[¶](#wx.grid.Grid.SetAttr "Permalink to this definition")
Sets the cell attributes for the specified cell.


The grid takes ownership of the attribute pointer.


See the  [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr) class for more information about controlling cell attributes.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellAlignment(self, row, col, horiz, vert) -> None:
        """ 

`SetCellAlignment`(*self*, *row*, *col*, *horiz*, *vert*)[¶](#wx.grid.Grid.SetCellAlignment "Permalink to this definition")
Sets the horizontal and vertical alignment for grid cell text at the specified location.


Horizontal alignment should be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` .


Vertical alignment should be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **horiz** (*int*) –
* **vert** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellBackgroundColour(self, row, col, colour) -> None:
        """ 

`SetCellBackgroundColour`(*self*, *row*, *col*, *colour*)[¶](#wx.grid.Grid.SetCellBackgroundColour "Permalink to this definition")
Set the background colour for the given cell or all cells by default.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellEditor(self, row, col, editor) -> None:
        """ 

`SetCellEditor`(*self*, *row*, *col*, *editor*)[¶](#wx.grid.Grid.SetCellEditor "Permalink to this definition")
Sets the editor for the grid cell at the specified location.


The grid will take ownership of the pointer.


See  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **editor** ([*wx.grid.GridCellEditor*](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor "wx.grid.GridCellEditor")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellFitMode(self, row, col, fitMode) -> None:
        """ 

`SetCellFitMode`(*self*, *row*, *col*, *fitMode*)[¶](#wx.grid.Grid.SetCellFitMode "Permalink to this definition")
Specifies the behaviour of the cell contents if it doesn’t fit into the available space.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **fitMode** ([*wx.grid.GridFitMode*](wx.grid.GridFitMode.html#wx.grid.GridFitMode "wx.grid.GridFitMode")) –





New in version 4.1/wxWidgets-3.1.4.




See also


 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellFont(self, row, col, font) -> None:
        """ 

`SetCellFont`(*self*, *row*, *col*, *font*)[¶](#wx.grid.Grid.SetCellFont "Permalink to this definition")
Sets the font for text in the grid cell at the specified location.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightColour(self) -> None:
        """ 

`SetCellHighlightColour`(*self*)[¶](#wx.grid.Grid.SetCellHighlightColour "Permalink to this definition")

Parameters
**``** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightPenWidth(self, width: int) -> None:
        """ 

`SetCellHighlightPenWidth`(*self*, *width*)[¶](#wx.grid.Grid.SetCellHighlightPenWidth "Permalink to this definition")

Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellHighlightROPenWidth(self, width: int) -> None:
        """ 

`SetCellHighlightROPenWidth`(*self*, *width*)[¶](#wx.grid.Grid.SetCellHighlightROPenWidth "Permalink to this definition")

Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellOverflow(self, row, col, allow) -> None:
        """ 

`SetCellOverflow`(*self*, *row*, *col*, *allow*)[¶](#wx.grid.Grid.SetCellOverflow "Permalink to this definition")
Sets the overflow permission of the cell.


Prefer using [`SetCellFitMode`](#wx.grid.Grid.SetCellFitMode "wx.grid.Grid.SetCellFitMode") in the new code.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **allow** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellRenderer(self, row, col, renderer) -> None:
        """ 

`SetCellRenderer`(*self*, *row*, *col*, *renderer*)[¶](#wx.grid.Grid.SetCellRenderer "Permalink to this definition")
Sets the renderer for the grid cell at the specified location.


The grid will take ownership of the pointer.


See  [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **renderer** ([*wx.grid.GridCellRenderer*](wx.grid.GridCellRenderer.html#wx.grid.GridCellRenderer "wx.grid.GridCellRenderer")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellSize(self, row, col, num_rows, num_cols) -> None:
        """ 

`SetCellSize`(*self*, *row*, *col*, *num\_rows*, *num\_cols*)[¶](#wx.grid.Grid.SetCellSize "Permalink to this definition")
Set the size of the cell.


Specifying a value of more than 1 in *num\_rows* or *num\_cols* will make the cell at (*row*, *col*) span the block of the specified size, covering the other cells which would be normally shown in it. Passing 1 for both arguments resets the cell to normal appearance.



Parameters
* **row** (*int*) – The row of the cell.
* **col** (*int*) – The column of the cell.
* **num\_rows** (*int*) – Number of rows to be occupied by this cell, must be >= 1.
* **num\_cols** (*int*) – Number of columns to be occupied by this cell, must be >= 1.





See also


[`GetCellSize`](#wx.grid.Grid.GetCellSize "wx.grid.Grid.GetCellSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellTextColour(self, row, col, colour) -> None:
        """ 

`SetCellTextColour`(*self*, *row*, *col*, *colour*)[¶](#wx.grid.Grid.SetCellTextColour "Permalink to this definition")
Sets the text colour for the given cell.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCellValue(self, *args, **kw) -> None:
        """ 

`SetCellValue`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.SetCellValue "Permalink to this definition")
Sets the string value for the cell at the specified location.


For simple applications where a grid object automatically uses a default grid table of string values you use this function together with [`GetCellValue`](#wx.grid.Grid.GetCellValue "wx.grid.Grid.GetCellValue") to access cell values. For more complex applications where you have derived your own grid table class that contains various data types (e.g. numeric, boolean or user-defined custom types) then you only use this function for those cells that contain string values.


See [`wx.grid.GridTableBase.CanSetValueAs`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.CanSetValueAs "wx.grid.GridTableBase.CanSetValueAs") and the [Grid Overview](grid_overview.html#grid-overview) for more information.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetCellValue** *(self, row, col, s)*



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **s** (*string*) –






---

  



**SetCellValue** *(self, coords, s)*



Parameters
* **coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **s** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColAttr(self, col, attr) -> None:
        """ 

`SetColAttr`(*self*, *col*, *attr*)[¶](#wx.grid.Grid.SetColAttr "Permalink to this definition")
Sets the cell attributes for all cells in the specified column.


For more information about controlling grid cell attributes see the  [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr) cell attribute class and the [Grid Overview](grid_overview.html#grid-overview).



Parameters
* **col** (*int*) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatBool(self, col: int) -> None:
        """ 

`SetColFormatBool`(*self*, *col*)[¶](#wx.grid.Grid.SetColFormatBool "Permalink to this definition")
Sets the specified column to display boolean values.



Parameters
**col** (*int*) – 





See also


[`SetColFormatCustom`](#wx.grid.Grid.SetColFormatCustom "wx.grid.Grid.SetColFormatCustom")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatCustom(self, col, typeName) -> None:
        """ 

`SetColFormatCustom`(*self*, *col*, *typeName*)[¶](#wx.grid.Grid.SetColFormatCustom "Permalink to this definition")
Sets the specified column to display data in a custom format.


This method provides an alternative to defining a custom grid table which would return *typeName* from its GetTypeName() method for the cells in this column: while it doesn’t really change the type of the cells in this column, it does associate the renderer and editor used for the cells of the specified type with them.


See the [Grid Overview](grid_overview.html#grid-overview) for more information on working with custom data types.



Parameters
* **col** (*int*) –
* **typeName** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatDate(self, col, format="") -> None:
        """ 

`SetColFormatDate`(*self*, *col*, *format=""*)[¶](#wx.grid.Grid.SetColFormatDate "Permalink to this definition")
Sets the specified column to display date values.


The *format* argument is used with  [wx.grid.GridCellDateRenderer](wx.grid.GridCellDateRenderer.html#wx-grid-gridcelldaterenderer) and allows to specify the strftime-like format string to use for displaying the dates in this column.



Parameters
* **col** (*int*) –
* **format** (*string*) –





New in version 4.1/wxWidgets-3.1.3.




See also


[`SetColFormatCustom`](#wx.grid.Grid.SetColFormatCustom "wx.grid.Grid.SetColFormatCustom")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatFloat(self, col, width=-1, precision=-1) -> None:
        """ 

`SetColFormatFloat`(*self*, *col*, *width=-1*, *precision=-1*)[¶](#wx.grid.Grid.SetColFormatFloat "Permalink to this definition")
Sets the specified column to display floating point values with the given width and precision.



Parameters
* **col** (*int*) –
* **width** (*int*) –
* **precision** (*int*) –





See also


[`SetColFormatCustom`](#wx.grid.Grid.SetColFormatCustom "wx.grid.Grid.SetColFormatCustom")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColFormatNumber(self, col: int) -> None:
        """ 

`SetColFormatNumber`(*self*, *col*)[¶](#wx.grid.Grid.SetColFormatNumber "Permalink to this definition")
Sets the specified column to display integer values.



Parameters
**col** (*int*) – 





See also


[`SetColFormatCustom`](#wx.grid.Grid.SetColFormatCustom "wx.grid.Grid.SetColFormatCustom")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelAlignment(self, horiz, vert) -> None:
        """ 

`SetColLabelAlignment`(*self*, *horiz*, *vert*)[¶](#wx.grid.Grid.SetColLabelAlignment "Permalink to this definition")
Sets the horizontal and vertical alignment of column label text.


Horizontal alignment should be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` . Vertical alignment should be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **horiz** (*int*) –
* **vert** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelSize(self, height: int) -> None:
        """ 

`SetColLabelSize`(*self*, *height*)[¶](#wx.grid.Grid.SetColLabelSize "Permalink to this definition")
Sets the height of the column labels.


If *height* equals to `GRID_AUTOSIZE` then height is calculated automatically so that no label is truncated. Note that this could be slow for a large table.



Parameters
**height** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelTextOrientation(self, textOrientation: int) -> None:
        """ 

`SetColLabelTextOrientation`(*self*, *textOrientation*)[¶](#wx.grid.Grid.SetColLabelTextOrientation "Permalink to this definition")
Sets the orientation of the column labels (either `HORIZONTAL` or `VERTICAL` ).



Parameters
**textOrientation** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColLabelValue(self, col, value) -> None:
        """ 

`SetColLabelValue`(*self*, *col*, *value*)[¶](#wx.grid.Grid.SetColLabelValue "Permalink to this definition")
Set the value for the given column label.


If you are using a custom grid table you must override [`wx.grid.GridTableBase.SetColLabelValue`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.SetColLabelValue "wx.grid.GridTableBase.SetColLabelValue") for this to have any effect.



Parameters
* **col** (*int*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColMinimalAcceptableWidth(self, width: int) -> None:
        """ 

`SetColMinimalAcceptableWidth`(*self*, *width*)[¶](#wx.grid.Grid.SetColMinimalAcceptableWidth "Permalink to this definition")
Sets the minimal *width* to which the user can resize columns.



Parameters
**width** (*int*) – 





See also


[`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColMinimalWidth(self, col, width) -> None:
        """ 

`SetColMinimalWidth`(*self*, *col*, *width*)[¶](#wx.grid.Grid.SetColMinimalWidth "Permalink to this definition")
Sets the minimal *width* for the specified column *col*.


It is usually best to call this method during grid creation as calling it later will not resize the column to the given minimal width even if it is currently narrower than it.


*width* must be greater than the minimal acceptable column width as returned by [`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth") .



Parameters
* **col** (*int*) –
* **width** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColPos(self, colID, newPos) -> None:
        """ 

`SetColPos`(*self*, *colID*, *newPos*)[¶](#wx.grid.Grid.SetColPos "Permalink to this definition")
Sets the position of the specified column.



Parameters
* **colID** (*int*) –
* **newPos** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColSize(self, col, width) -> None:
        """ 

`SetColSize`(*self*, *col*, *width*)[¶](#wx.grid.Grid.SetColSize "Permalink to this definition")
Sets the width of the specified column.



Parameters
* **col** (*int*) – The column index.
* **width** (*int*) – The new column width in pixels, 0 to hide the column or -1 to fit the column width to its label width.






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColSizes(self, sizeInfo: 'grid.GridSizesInfo') -> None:
        """ 

`SetColSizes`(*self*, *sizeInfo*)[¶](#wx.grid.Grid.SetColSizes "Permalink to this definition")
Restore all columns sizes.


This is usually called with  [wx.grid.GridSizesInfo](wx.grid.GridSizesInfo.html#wx-grid-gridsizesinfo) object previously returned by [`GetColSizes`](#wx.grid.Grid.GetColSizes "wx.grid.Grid.GetColSizes") .



Parameters
**sizeInfo** ([*wx.grid.GridSizesInfo*](wx.grid.GridSizesInfo.html#wx.grid.GridSizesInfo "wx.grid.GridSizesInfo")) – 





See also


[`SetRowSizes`](#wx.grid.Grid.SetRowSizes "wx.grid.Grid.SetRowSizes")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetColumnsOrder(self, order: int) -> None:
        """ 

`SetColumnsOrder`(*self*, *order*)[¶](#wx.grid.Grid.SetColumnsOrder "Permalink to this definition")
Sets the positions of all columns at once.


This method takes an array containing the indices of the columns in their display order, i.e. uses the same convention as [`wx.HeaderCtrl.SetColumnsOrder`](wx.HeaderCtrl.html#wx.HeaderCtrl.SetColumnsOrder "wx.HeaderCtrl.SetColumnsOrder") .



Parameters
**order** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelAlignment(self, horiz, vert) -> None:
        """ 

`SetCornerLabelAlignment`(*self*, *horiz*, *vert*)[¶](#wx.grid.Grid.SetCornerLabelAlignment "Permalink to this definition")
Sets the horizontal and vertical alignment of the (top-left) corner label text.


Horizontal alignment should be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` . Vertical alignment should be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **horiz** (*int*) –
* **vert** (*int*) –





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelTextOrientation(self, textOrientation: int) -> None:
        """ 

`SetCornerLabelTextOrientation`(*self*, *textOrientation*)[¶](#wx.grid.Grid.SetCornerLabelTextOrientation "Permalink to this definition")
Sets the orientation of the (top-left) corner label (either `HORIZONTAL` or `VERTICAL` ).



Parameters
**textOrientation** (*int*) – 





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetCornerLabelValue(self) -> None:
        """ 

`SetCornerLabelValue`(*self*)[¶](#wx.grid.Grid.SetCornerLabelValue "Permalink to this definition")
Set the value for the (top-left) corner label.


If you are using a custom grid table you must override [`wx.grid.GridTableBase.SetCornerLabelValue`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.SetCornerLabelValue "wx.grid.GridTableBase.SetCornerLabelValue") for this to have any effect.



Parameters
**``** (*string*) – 





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellAlignment(self, horiz, vert) -> None:
        """ 

`SetDefaultCellAlignment`(*self*, *horiz*, *vert*)[¶](#wx.grid.Grid.SetDefaultCellAlignment "Permalink to this definition")
Sets the default horizontal and vertical alignment for grid cell text.


Horizontal alignment should be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` . Vertical alignment should be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **horiz** (*int*) –
* **vert** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetDefaultCellBackgroundColour`(*self*, *colour*)[¶](#wx.grid.Grid.SetDefaultCellBackgroundColour "Permalink to this definition")
Sets the default background colour for grid cells.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellFitMode(self, fitMode: 'grid.GridFitMode') -> None:
        """ 

`SetDefaultCellFitMode`(*self*, *fitMode*)[¶](#wx.grid.Grid.SetDefaultCellFitMode "Permalink to this definition")
Specifies the default behaviour of the cell contents if it doesn’t fit into the available space.



Parameters
**fitMode** ([*wx.grid.GridFitMode*](wx.grid.GridFitMode.html#wx.grid.GridFitMode "wx.grid.GridFitMode")) – 





New in version 4.1/wxWidgets-3.1.4.




See also


 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellFont(self, font: 'Font') -> None:
        """ 

`SetDefaultCellFont`(*self*, *font*)[¶](#wx.grid.Grid.SetDefaultCellFont "Permalink to this definition")
Sets the default font to be used for grid cell text.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellOverflow(self, allow: bool) -> None:
        """ 

`SetDefaultCellOverflow`(*self*, *allow*)[¶](#wx.grid.Grid.SetDefaultCellOverflow "Permalink to this definition")
Sets the default overflow permission of the cells.


Prefer using [`SetDefaultCellFitMode`](#wx.grid.Grid.SetDefaultCellFitMode "wx.grid.Grid.SetDefaultCellFitMode") in the new code.



Parameters
**allow** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultCellTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetDefaultCellTextColour`(*self*, *colour*)[¶](#wx.grid.Grid.SetDefaultCellTextColour "Permalink to this definition")
Sets the current default colour for grid cell text.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultColSize(self, width, resizeExistingCols=False) -> None:
        """ 

`SetDefaultColSize`(*self*, *width*, *resizeExistingCols=False*)[¶](#wx.grid.Grid.SetDefaultColSize "Permalink to this definition")
Sets the default width for columns in the grid.


This will only affect columns subsequently added to the grid unless *resizeExistingCols* is `True`.


If *width* is less than [`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth") , then the minimal acceptable width is used instead of it.



Parameters
* **width** (*int*) –
* **resizeExistingCols** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultEditor(self, editor: 'grid.GridCellEditor') -> None:
        """ 

`SetDefaultEditor`(*self*, *editor*)[¶](#wx.grid.Grid.SetDefaultEditor "Permalink to this definition")
Sets the default editor for grid cells.


The grid will take ownership of the pointer.


See  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.



Parameters
**editor** ([*wx.grid.GridCellEditor*](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor "wx.grid.GridCellEditor")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultRenderer(self, renderer: 'grid.GridCellRenderer') -> None:
        """ 

`SetDefaultRenderer`(*self*, *renderer*)[¶](#wx.grid.Grid.SetDefaultRenderer "Permalink to this definition")
Sets the default renderer for grid cells.


The grid will take ownership of the pointer.


See  [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer) and the [Grid Overview](grid_overview.html#grid-overview) for more information about cell editors and renderers.



Parameters
**renderer** ([*wx.grid.GridCellRenderer*](wx.grid.GridCellRenderer.html#wx.grid.GridCellRenderer "wx.grid.GridCellRenderer")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetDefaultRowSize(self, height, resizeExistingRows=False) -> None:
        """ 

`SetDefaultRowSize`(*self*, *height*, *resizeExistingRows=False*)[¶](#wx.grid.Grid.SetDefaultRowSize "Permalink to this definition")
Sets the default height for rows in the grid.


This will only affect rows subsequently added to the grid unless *resizeExistingRows* is `True`.


If *height* is less than [`GetRowMinimalAcceptableHeight`](#wx.grid.Grid.GetRowMinimalAcceptableHeight "wx.grid.Grid.GetRowMinimalAcceptableHeight") , then the minimal acceptable height is used instead of it.



Parameters
* **height** (*int*) –
* **resizeExistingRows** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridCursor(self, *args, **kw) -> None:
        """ 

`SetGridCursor`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.SetGridCursor "Permalink to this definition")
Set the grid cursor to the specified cell.


The grid cursor indicates the current cell and can be moved by the user using the arrow keys or the mouse.


Calling this function generates a `wxEVT_GRID_SELECT_CELL` event and if the event handler vetoes this event, the cursor is not moved.


This function doesn’t make the target call visible, use [`GoToCell`](#wx.grid.Grid.GoToCell "wx.grid.Grid.GoToCell") to do this.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetGridCursor** *(self, row, col)*



Parameters
* **row** (*int*) –
* **col** (*int*) –






---

  



**SetGridCursor** *(self, coords)*



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridFrozenBorderColour(self) -> None:
        """ 

`SetGridFrozenBorderColour`(*self*)[¶](#wx.grid.Grid.SetGridFrozenBorderColour "Permalink to this definition")

Parameters
**``** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridFrozenBorderPenWidth(self, width: int) -> None:
        """ 

`SetGridFrozenBorderPenWidth`(*self*, *width*)[¶](#wx.grid.Grid.SetGridFrozenBorderPenWidth "Permalink to this definition")

Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetGridLineColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetGridLineColour`(*self*, *colour*)[¶](#wx.grid.Grid.SetGridLineColour "Permalink to this definition")
Sets the colour used to draw grid lines.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetLabelBackgroundColour`(*self*, *colour*)[¶](#wx.grid.Grid.SetLabelBackgroundColour "Permalink to this definition")
Sets the background colour for row and column labels.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelFont(self, font: 'Font') -> None:
        """ 

`SetLabelFont`(*self*, *font*)[¶](#wx.grid.Grid.SetLabelFont "Permalink to this definition")
Sets the font for row and column labels.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetLabelTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetLabelTextColour`(*self*, *colour*)[¶](#wx.grid.Grid.SetLabelTextColour "Permalink to this definition")
Sets the colour for row and column label text.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetMargins(self, extraWidth, extraHeight) -> None:
        """ 

`SetMargins`(*self*, *extraWidth*, *extraHeight*)[¶](#wx.grid.Grid.SetMargins "Permalink to this definition")
Sets the extra margins used around the grid area.


A grid may occupy more space than needed for its data display and this function allows setting how big this extra space is



Parameters
* **extraWidth** (*int*) –
* **extraHeight** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetReadOnly(self, row, col, isReadOnly=True) -> None:
        """ 

`SetReadOnly`(*self*, *row*, *col*, *isReadOnly=True*)[¶](#wx.grid.Grid.SetReadOnly "Permalink to this definition")
Makes the cell at the specified location read-only or editable.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **isReadOnly** (*bool*) –





See also


[`IsReadOnly`](#wx.grid.Grid.IsReadOnly "wx.grid.Grid.IsReadOnly")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowAttr(self, row, attr) -> None:
        """ 

`SetRowAttr`(*self*, *row*, *attr*)[¶](#wx.grid.Grid.SetRowAttr "Permalink to this definition")
Sets the cell attributes for all cells in the specified row.


The grid takes ownership of the attribute pointer.


See the  [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr) class for more information about controlling cell attributes.



Parameters
* **row** (*int*) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelAlignment(self, horiz, vert) -> None:
        """ 

`SetRowLabelAlignment`(*self*, *horiz*, *vert*)[¶](#wx.grid.Grid.SetRowLabelAlignment "Permalink to this definition")
Sets the horizontal and vertical alignment of row label text.


Horizontal alignment should be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` . Vertical alignment should be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **horiz** (*int*) –
* **vert** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelSize(self, width: int) -> None:
        """ 

`SetRowLabelSize`(*self*, *width*)[¶](#wx.grid.Grid.SetRowLabelSize "Permalink to this definition")
Sets the width of the row labels.


If *width* equals `GRID_AUTOSIZE` then width is calculated automatically so that no label is truncated. Note that this could be slow for a large table.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowLabelValue(self, row, value) -> None:
        """ 

`SetRowLabelValue`(*self*, *row*, *value*)[¶](#wx.grid.Grid.SetRowLabelValue "Permalink to this definition")
Sets the value for the given row label.


If you are using a derived grid table you must override [`wx.grid.GridTableBase.SetRowLabelValue`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.SetRowLabelValue "wx.grid.GridTableBase.SetRowLabelValue") for this to have any effect.



Parameters
* **row** (*int*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowMinimalAcceptableHeight(self, height: int) -> None:
        """ 

`SetRowMinimalAcceptableHeight`(*self*, *height*)[¶](#wx.grid.Grid.SetRowMinimalAcceptableHeight "Permalink to this definition")
Sets the minimal row *height* used by default.


See [`SetColMinimalAcceptableWidth`](#wx.grid.Grid.SetColMinimalAcceptableWidth "wx.grid.Grid.SetColMinimalAcceptableWidth") for more information.



Parameters
**height** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowMinimalHeight(self, row, height) -> None:
        """ 

`SetRowMinimalHeight`(*self*, *row*, *height*)[¶](#wx.grid.Grid.SetRowMinimalHeight "Permalink to this definition")
Sets the minimal *height* for the specified *row*.


See [`SetColMinimalWidth`](#wx.grid.Grid.SetColMinimalWidth "wx.grid.Grid.SetColMinimalWidth") for more information.



Parameters
* **row** (*int*) –
* **height** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowPos(self, rowID, newPos) -> None:
        """ 

`SetRowPos`(*self*, *rowID*, *newPos*)[¶](#wx.grid.Grid.SetRowPos "Permalink to this definition")
Sets the position of the specified row.



Parameters
* **rowID** (*int*) –
* **newPos** (*int*) –





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowSize(self, row, height) -> None:
        """ 

`SetRowSize`(*self*, *row*, *height*)[¶](#wx.grid.Grid.SetRowSize "Permalink to this definition")
Sets the height of the specified row.


See [`SetColSize`](#wx.grid.Grid.SetColSize "wx.grid.Grid.SetColSize") for more information.



Parameters
* **row** (*int*) –
* **height** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowSizes(self, sizeInfo: 'grid.GridSizesInfo') -> None:
        """ 

`SetRowSizes`(*self*, *sizeInfo*)[¶](#wx.grid.Grid.SetRowSizes "Permalink to this definition")
Restore all rows sizes.



Parameters
**sizeInfo** ([*wx.grid.GridSizesInfo*](wx.grid.GridSizesInfo.html#wx.grid.GridSizesInfo "wx.grid.GridSizesInfo")) – 





See also


[`SetColSizes`](#wx.grid.Grid.SetColSizes "wx.grid.Grid.SetColSizes")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetRowsOrder(self, order: int) -> None:
        """ 

`SetRowsOrder`(*self*, *order*)[¶](#wx.grid.Grid.SetRowsOrder "Permalink to this definition")
Sets the positions of all rows at once.


This method takes an array containing the indices of the rows in their display order.



Parameters
**order** (*list of integers*) – 





New in version 4.1/wxWidgets-3.1.7.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetScrollLineX(self, x: int) -> None:
        """ 

`SetScrollLineX`(*self*, *x*)[¶](#wx.grid.Grid.SetScrollLineX "Permalink to this definition")
Sets the number of pixels per horizontal scroll increment.


The default is 15.



Parameters
**x** (*int*) – 





See also


[`GetScrollLineX`](#wx.grid.Grid.GetScrollLineX "wx.grid.Grid.GetScrollLineX") , [`GetScrollLineY`](#wx.grid.Grid.GetScrollLineY "wx.grid.Grid.GetScrollLineY") , [`SetScrollLineY`](#wx.grid.Grid.SetScrollLineY "wx.grid.Grid.SetScrollLineY")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetScrollLineY(self, y: int) -> None:
        """ 

`SetScrollLineY`(*self*, *y*)[¶](#wx.grid.Grid.SetScrollLineY "Permalink to this definition")
Sets the number of pixels per vertical scroll increment.


The default is 15.



Parameters
**y** (*int*) – 





See also


[`GetScrollLineX`](#wx.grid.Grid.GetScrollLineX "wx.grid.Grid.GetScrollLineX") , [`GetScrollLineY`](#wx.grid.Grid.GetScrollLineY "wx.grid.Grid.GetScrollLineY") , [`SetScrollLineX`](#wx.grid.Grid.SetScrollLineX "wx.grid.Grid.SetScrollLineX")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionBackground(self, c: Union[int, str, 'Colour']) -> None:
        """ 

`SetSelectionBackground`(*self*, *c*)[¶](#wx.grid.Grid.SetSelectionBackground "Permalink to this definition")
Set the colour to be used for drawing the selection background.



Parameters
**c** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionForeground(self, c: Union[int, str, 'Colour']) -> None:
        """ 

`SetSelectionForeground`(*self*, *c*)[¶](#wx.grid.Grid.SetSelectionForeground "Permalink to this definition")
Set the colour to be used for drawing the selection foreground.



Parameters
**c** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSelectionMode(self, selmode: GridSelectionModes) -> None:
        """ 

`SetSelectionMode`(*self*, *selmode*)[¶](#wx.grid.Grid.SetSelectionMode "Permalink to this definition")
Set the selection behaviour of the grid.


The existing selection is converted to conform to the new mode if possible and discarded otherwise (e.g. any individual selected cells are deselected if the new mode allows only the selection of the entire rows or columns).



Parameters
**selmode** ([*GridSelectionModes*](wx.grid.Grid.GridSelectionModes.enumeration.html "GridSelectionModes")) – 






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetSortingColumn(self, col, ascending=True) -> None:
        """ 

`SetSortingColumn`(*self*, *col*, *ascending=True*)[¶](#wx.grid.Grid.SetSortingColumn "Permalink to this definition")
Set the column to display the sorting indicator in and its direction.



Parameters
* **col** (*int*) – The column to display the sorting indicator in or `NOT_FOUND` to remove any currently displayed sorting indicator.
* **ascending** (*bool*) – If `True`, display the ascending sort indicator, otherwise display the descending sort indicator.





See also


[`GetSortingColumn`](#wx.grid.Grid.GetSortingColumn "wx.grid.Grid.GetSortingColumn") , [`IsSortOrderAscending`](#wx.grid.Grid.IsSortOrderAscending "wx.grid.Grid.IsSortOrderAscending")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetTabBehaviour(self, behaviour: TabBehaviour) -> None:
        """ 

`SetTabBehaviour`(*self*, *behaviour*)[¶](#wx.grid.Grid.SetTabBehaviour "Permalink to this definition")
Set the grid’s behaviour when the user presses the `TAB` key.


Pressing the `TAB` key moves the grid cursor right in the current row, if there is a cell at the right and, similarly, Shift-TAB moves the cursor to the left in the current row if it’s not in the first column.


What happens if the cursor can’t be moved because it it’s already at the beginning or end of the row can be configured using this function, see  [wx.grid.Grid.TabBehaviour](wx.grid.Grid.TabBehaviour.enumeration.html#wx-grid-grid-tabbehaviour) documentation for the detailed description.


`IF` none of the standard behaviours is appropriate, you can always handle `wxEVT_GRID_TABBING` event directly to implement a custom TAB-handling logic.



Parameters
**behaviour** ([*TabBehaviour*](wx.grid.Grid.TabBehaviour.enumeration.html "TabBehaviour")) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def _SetTable(self, table, takeOwnership=False, selmode=GridSelectCells) -> bool:
        """ 

`_SetTable`(*self*, *table*, *takeOwnership=False*, *selmode=GridSelectCells*)[¶](#wx.grid.Grid._SetTable "Permalink to this definition")
Passes a pointer to a custom grid table to be used by the grid.


This should be called after the grid constructor and before using the grid object. If *takeOwnership* is set to `True` then the table will be deleted by the  [wx.grid.Grid](#wx-grid-grid) destructor.


Use this function instead of [`CreateGrid`](#wx.grid.Grid.CreateGrid "wx.grid.Grid.CreateGrid") when your application involves complex or non-string data or data sets that are too large to fit wholly in memory.


When the custom table should be owned by the grid, consider using the simpler [`AssignTable`](#wx.grid.Grid.AssignTable "wx.grid.Grid.AssignTable") function instead of this one with `True` value of *takeOwnership* parameter.



Parameters
* **table** ([*wx.grid.GridTableBase*](wx.grid.GridTableBase.html#wx.grid.GridTableBase "wx.grid.GridTableBase")) –
* **takeOwnership** (*bool*) –
* **selmode** ([*GridSelectionModes*](wx.grid.Grid.GridSelectionModes.enumeration.html "GridSelectionModes")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetTable(self, table, takeOwnership=False, selmode=Grid.GridSelectCells) -> None:
        """ 

`SetTable`(*self*, *table*, *takeOwnership=False*, *selmode=Grid.GridSelectCells*)[¶](#wx.grid.Grid.SetTable "Permalink to this definition")
Set the Grid Table to be used by this grid.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def SetUseNativeColLabels(self, native: bool=True) -> None:
        """ 

`SetUseNativeColLabels`(*self*, *native=True*)[¶](#wx.grid.Grid.SetUseNativeColLabels "Permalink to this definition")
Call this in order to make the column labels use a native look by using [`wx.RendererNative.DrawHeaderButton`](wx.RendererNative.html#wx.RendererNative.DrawHeaderButton "wx.RendererNative.DrawHeaderButton") internally.


There is no equivalent method for drawing row columns as there is not native look for that. This option is useful when using  [wx.grid.Grid](#wx-grid-grid) for displaying tables and not as a spread-sheet.



Parameters
**native** (*bool*) – 





See also


[`UseNativeColHeader`](#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowCellEditControl(self) -> None:
        """ 

`ShowCellEditControl`(*self*)[¶](#wx.grid.Grid.ShowCellEditControl "Permalink to this definition")
Displays the active in-place cell edit control for the current cell after it was hidden.


This method should only be called after calling [`HideCellEditControl`](#wx.grid.Grid.HideCellEditControl "wx.grid.Grid.HideCellEditControl") , to start editing the current grid cell use [`EnableCellEditControl`](#wx.grid.Grid.EnableCellEditControl "wx.grid.Grid.EnableCellEditControl") instead.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowCol(self, col: int) -> None:
        """ 

`ShowCol`(*self*, *col*)[¶](#wx.grid.Grid.ShowCol "Permalink to this definition")
Shows the previously hidden column by resizing it to non-0 size.


The column is shown again with the same width that it had before [`HideCol`](#wx.grid.Grid.HideCol "wx.grid.Grid.HideCol") call.


If the column is currently shown, this method doesn’t do anything.



Parameters
**col** (*int*) – 





See also


[`HideCol`](#wx.grid.Grid.HideCol "wx.grid.Grid.HideCol") , [`SetColSize`](#wx.grid.Grid.SetColSize "wx.grid.Grid.SetColSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def ShowRow(self, col: int) -> None:
        """ 

`ShowRow`(*self*, *col*)[¶](#wx.grid.Grid.ShowRow "Permalink to this definition")
Shows the previously hidden row.


The row is shown again with the same height that it had before [`HideRow`](#wx.grid.Grid.HideRow "wx.grid.Grid.HideRow") call.


If the row is currently shown, this method doesn’t do anything.



Parameters
**col** (*int*) – 





See also


[`HideRow`](#wx.grid.Grid.HideRow "wx.grid.Grid.HideRow") , [`SetRowSize`](#wx.grid.Grid.SetRowSize "wx.grid.Grid.SetRowSize")





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def UnsetSortingColumn(self) -> None:
        """ 

`UnsetSortingColumn`(*self*)[¶](#wx.grid.Grid.UnsetSortingColumn "Permalink to this definition")
Remove any currently shown sorting indicator.


This is equivalent to calling [`SetSortingColumn`](#wx.grid.Grid.SetSortingColumn "wx.grid.Grid.SetSortingColumn") with `NOT_FOUND` first argument.




            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def UseNativeColHeader(self, native: bool=True) -> bool:
        """ 

`UseNativeColHeader`(*self*, *native=True*)[¶](#wx.grid.Grid.UseNativeColHeader "Permalink to this definition")
Enable the use of native header window for column labels.


If this function is called with `True` argument, a  [wx.HeaderCtrl](wx.HeaderCtrl.html#wx-headerctrl) is used instead to display the column labels instead of drawing them in  [wx.grid.Grid](#wx-grid-grid) code itself. This has the advantage of making the grid look and feel perfectly the same as native applications (using [`SetUseNativeColLabels`](#wx.grid.Grid.SetUseNativeColLabels "wx.grid.Grid.SetUseNativeColLabels") the grid can be made to look more natively but it still doesn’t feel natively, notably the column resizing and dragging still works slightly differently as it is implemented in wxWidgets itself) but results in different behaviour for column and row headers, for which there is no equivalent function, and, most importantly, is unsuitable for grids with huge numbers of columns as  [wx.HeaderCtrl](wx.HeaderCtrl.html#wx-headerctrl) doesn’t support virtual mode. Because of this, by default the grid does not use the native header control but you should call this function to enable it if you are using the grid to display tabular data and don’t have thousands of columns in it.


Another difference between the default behaviour and the native header behaviour is that the latter provides the user with a context menu (which appears on right clicking the header) allowing to rearrange the grid columns if [`CanDragColMove`](#wx.grid.Grid.CanDragColMove "wx.grid.Grid.CanDragColMove") returns `True`. If you want to prevent this from happening for some reason, you need to define a handler for `wxEVT_GRID_LABEL_RIGHT_CLICK` event which simply does nothing (in particular doesn’t skip the event) as this will prevent the default right click handling from working.


Also note that currently `wxEVT_GRID_LABEL_RIGHT_DCLICK` event is not generated for the column labels if the native columns header is used (but this limitation could possibly be lifted in the future).


Finally, please note that using the native control is currently incompatible with freezing columns in the grid (see [`FreezeTo`](#wx.grid.Grid.FreezeTo "wx.grid.Grid.FreezeTo") ) and this function will return `False`, without doing anything, if it’s called on a grid in which any columns are frozen.



Parameters
**native** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XToCol(self, x, clipToMinMax=False, gridWindow=None) -> int:
        """ 

`XToCol`(*self*, *x*, *clipToMinMax=False*, *gridWindow=None*)[¶](#wx.grid.Grid.XToCol "Permalink to this definition")
Returns the column at the given pixel position depending on the window.



Parameters
* **x** (*int*) – The x position to evaluate.
* **clipToMinMax** (*bool*) – If `True`, rather than returning `NOT_FOUND` , it returns either the first or last column depending on whether *x* is too far to the left or right respectively.
* **gridWindow** (*wx.grid.GridWindow*) – The associated grid window that limits the search (note that this parameter is only available since wxWidgets 3.1.3). If *gridWindow* is `None`, it will consider all the cells, no matter which grid they belong to.



Return type
*int*



Returns
The column index or `NOT_FOUND` .






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XToEdgeOfCol(self, x: int) -> int:
        """ 

`XToEdgeOfCol`(*self*, *x*)[¶](#wx.grid.Grid.XToEdgeOfCol "Permalink to this definition")
Returns the column whose right hand edge is close to the given logical *x* position.


If no column edge is near to this position `NOT_FOUND` is returned.



Parameters
**x** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def XYToCell(self, *args, **kw) -> 'GridCellCoords':
        """ 

`XYToCell`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.Grid.XYToCell "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**XYToCell** *(self, x, y, gridWindow=None)*


Translates logical pixel coordinates to the grid cell coordinates.


Notice that this function expects logical coordinates on input so if you use this function in a mouse event handler you need to translate the mouse position, which is expressed in device coordinates, to logical ones.


The parameter *gridWindow* is new since wxWidgets 3.1.3. If it is specified, i.e. not `None`, the coordinates must be in this window coordinate system and only the cells of this window are considered, i.e. the function returns `NOT_FOUND` if the coordinates are out of bounds.


If *gridWindow* is `None`, coordinates are relative to the main grid window and all cells are considered.



Parameters
* **x** (*int*) –
* **y** (*int*) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
 [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords)





See also


[`XToCol`](#wx.grid.Grid.XToCol "wx.grid.Grid.XToCol") , [`YToRow`](#wx.grid.Grid.YToRow "wx.grid.Grid.YToRow")





---

  



**XYToCell** *(self, pos, gridWindow=None)*


This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.



Parameters
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
 [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords)






---

  





            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def YToEdgeOfRow(self, y: int) -> int:
        """ 

`YToEdgeOfRow`(*self*, *y*)[¶](#wx.grid.Grid.YToEdgeOfRow "Permalink to this definition")
Returns the row whose bottom edge is close to the given logical *y* position.


If no row edge is near to this position `NOT_FOUND` is returned.



Parameters
**y** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    def YToRow(self, y, clipToMinMax=False, gridWindow=None) -> int:
        """ 

`YToRow`(*self*, *y*, *clipToMinMax=False*, *gridWindow=None*)[¶](#wx.grid.Grid.YToRow "Permalink to this definition")
Returns the grid row that corresponds to the logical *y* coordinate.


The parameter *gridWindow* is new since wxWidgets 3.1.3. If it is specified, i.e. not `None`, only the cells of this window are considered, i.e. the function returns `NOT_FOUND` if *y* is out of bounds.


If *gridWindow* is `None`, the function returns `NOT_FOUND` only if there is no row at all at the *y* position.



Parameters
* **y** (*int*) –
* **clipToMinMax** (*bool*) –
* **gridWindow** (*wx.grid.GridWindow*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.Grid.html
        """

    BatchCount: int  # `BatchCount`[¶](#wx.grid.Grid.BatchCount "Permalink to this definition")See [`GetBatchCount`](#wx.grid.Grid.GetBatchCount "wx.grid.Grid.GetBatchCount")
    CellHighlightColour: 'Colour'  # `CellHighlightColour`[¶](#wx.grid.Grid.CellHighlightColour "Permalink to this definition")See [`GetCellHighlightColour`](#wx.grid.Grid.GetCellHighlightColour "wx.grid.Grid.GetCellHighlightColour") and [`SetCellHighlightColour`](#wx.grid.Grid.SetCellHighlightColour "wx.grid.Grid.SetCellHighlightColour")
    CellHighlightPenWidth: int  # `CellHighlightPenWidth`[¶](#wx.grid.Grid.CellHighlightPenWidth "Permalink to this definition")See [`GetCellHighlightPenWidth`](#wx.grid.Grid.GetCellHighlightPenWidth "wx.grid.Grid.GetCellHighlightPenWidth") and [`SetCellHighlightPenWidth`](#wx.grid.Grid.SetCellHighlightPenWidth "wx.grid.Grid.SetCellHighlightPenWidth")
    CellHighlightROPenWidth: int  # `CellHighlightROPenWidth`[¶](#wx.grid.Grid.CellHighlightROPenWidth "Permalink to this definition")See [`GetCellHighlightROPenWidth`](#wx.grid.Grid.GetCellHighlightROPenWidth "wx.grid.Grid.GetCellHighlightROPenWidth") and [`SetCellHighlightROPenWidth`](#wx.grid.Grid.SetCellHighlightROPenWidth "wx.grid.Grid.SetCellHighlightROPenWidth")
    ColLabelSize: int  # `ColLabelSize`[¶](#wx.grid.Grid.ColLabelSize "Permalink to this definition")See [`GetColLabelSize`](#wx.grid.Grid.GetColLabelSize "wx.grid.Grid.GetColLabelSize") and [`SetColLabelSize`](#wx.grid.Grid.SetColLabelSize "wx.grid.Grid.SetColLabelSize")
    ColLabelTextOrientation: int  # `ColLabelTextOrientation`[¶](#wx.grid.Grid.ColLabelTextOrientation "Permalink to this definition")See [`GetColLabelTextOrientation`](#wx.grid.Grid.GetColLabelTextOrientation "wx.grid.Grid.GetColLabelTextOrientation") and [`SetColLabelTextOrientation`](#wx.grid.Grid.SetColLabelTextOrientation "wx.grid.Grid.SetColLabelTextOrientation")
    ColMinimalAcceptableWidth: int  # `ColMinimalAcceptableWidth`[¶](#wx.grid.Grid.ColMinimalAcceptableWidth "Permalink to this definition")See [`GetColMinimalAcceptableWidth`](#wx.grid.Grid.GetColMinimalAcceptableWidth "wx.grid.Grid.GetColMinimalAcceptableWidth") and [`SetColMinimalAcceptableWidth`](#wx.grid.Grid.SetColMinimalAcceptableWidth "wx.grid.Grid.SetColMinimalAcceptableWidth")
    ColSizes: 'GridSizesInfo'  # `ColSizes`[¶](#wx.grid.Grid.ColSizes "Permalink to this definition")See [`GetColSizes`](#wx.grid.Grid.GetColSizes "wx.grid.Grid.GetColSizes") and [`SetColSizes`](#wx.grid.Grid.SetColSizes "wx.grid.Grid.SetColSizes")
    CornerLabelTextOrientation: int  # `CornerLabelTextOrientation`[¶](#wx.grid.Grid.CornerLabelTextOrientation "Permalink to this definition")See [`GetCornerLabelTextOrientation`](#wx.grid.Grid.GetCornerLabelTextOrientation "wx.grid.Grid.GetCornerLabelTextOrientation") and [`SetCornerLabelTextOrientation`](#wx.grid.Grid.SetCornerLabelTextOrientation "wx.grid.Grid.SetCornerLabelTextOrientation")
    CornerLabelValue: str  # `CornerLabelValue`[¶](#wx.grid.Grid.CornerLabelValue "Permalink to this definition")See [`GetCornerLabelValue`](#wx.grid.Grid.GetCornerLabelValue "wx.grid.Grid.GetCornerLabelValue") and [`SetCornerLabelValue`](#wx.grid.Grid.SetCornerLabelValue "wx.grid.Grid.SetCornerLabelValue")
    DefaultCellBackgroundColour: 'Colour'  # `DefaultCellBackgroundColour`[¶](#wx.grid.Grid.DefaultCellBackgroundColour "Permalink to this definition")See [`GetDefaultCellBackgroundColour`](#wx.grid.Grid.GetDefaultCellBackgroundColour "wx.grid.Grid.GetDefaultCellBackgroundColour") and [`SetDefaultCellBackgroundColour`](#wx.grid.Grid.SetDefaultCellBackgroundColour "wx.grid.Grid.SetDefaultCellBackgroundColour")
    DefaultCellFitMode: 'GridFitMode'  # `DefaultCellFitMode`[¶](#wx.grid.Grid.DefaultCellFitMode "Permalink to this definition")See [`GetDefaultCellFitMode`](#wx.grid.Grid.GetDefaultCellFitMode "wx.grid.Grid.GetDefaultCellFitMode") and [`SetDefaultCellFitMode`](#wx.grid.Grid.SetDefaultCellFitMode "wx.grid.Grid.SetDefaultCellFitMode")
    DefaultCellFont: 'Font'  # `DefaultCellFont`[¶](#wx.grid.Grid.DefaultCellFont "Permalink to this definition")See [`GetDefaultCellFont`](#wx.grid.Grid.GetDefaultCellFont "wx.grid.Grid.GetDefaultCellFont") and [`SetDefaultCellFont`](#wx.grid.Grid.SetDefaultCellFont "wx.grid.Grid.SetDefaultCellFont")
    DefaultCellOverflow: bool  # `DefaultCellOverflow`[¶](#wx.grid.Grid.DefaultCellOverflow "Permalink to this definition")See [`GetDefaultCellOverflow`](#wx.grid.Grid.GetDefaultCellOverflow "wx.grid.Grid.GetDefaultCellOverflow") and [`SetDefaultCellOverflow`](#wx.grid.Grid.SetDefaultCellOverflow "wx.grid.Grid.SetDefaultCellOverflow")
    DefaultCellTextColour: 'Colour'  # `DefaultCellTextColour`[¶](#wx.grid.Grid.DefaultCellTextColour "Permalink to this definition")See [`GetDefaultCellTextColour`](#wx.grid.Grid.GetDefaultCellTextColour "wx.grid.Grid.GetDefaultCellTextColour") and [`SetDefaultCellTextColour`](#wx.grid.Grid.SetDefaultCellTextColour "wx.grid.Grid.SetDefaultCellTextColour")
    DefaultColLabelSize: int  # `DefaultColLabelSize`[¶](#wx.grid.Grid.DefaultColLabelSize "Permalink to this definition")See [`GetDefaultColLabelSize`](#wx.grid.Grid.GetDefaultColLabelSize "wx.grid.Grid.GetDefaultColLabelSize")
    DefaultColSize: int  # `DefaultColSize`[¶](#wx.grid.Grid.DefaultColSize "Permalink to this definition")See [`GetDefaultColSize`](#wx.grid.Grid.GetDefaultColSize "wx.grid.Grid.GetDefaultColSize") and [`SetDefaultColSize`](#wx.grid.Grid.SetDefaultColSize "wx.grid.Grid.SetDefaultColSize")
    DefaultEditor: 'GridCellEditor'  # `DefaultEditor`[¶](#wx.grid.Grid.DefaultEditor "Permalink to this definition")See [`GetDefaultEditor`](#wx.grid.Grid.GetDefaultEditor "wx.grid.Grid.GetDefaultEditor") and [`SetDefaultEditor`](#wx.grid.Grid.SetDefaultEditor "wx.grid.Grid.SetDefaultEditor")
    DefaultGridLinePen: 'Pen'  # `DefaultGridLinePen`[¶](#wx.grid.Grid.DefaultGridLinePen "Permalink to this definition")See [`GetDefaultGridLinePen`](#wx.grid.Grid.GetDefaultGridLinePen "wx.grid.Grid.GetDefaultGridLinePen")
    DefaultRenderer: 'GridCellRenderer'  # `DefaultRenderer`[¶](#wx.grid.Grid.DefaultRenderer "Permalink to this definition")See [`GetDefaultRenderer`](#wx.grid.Grid.GetDefaultRenderer "wx.grid.Grid.GetDefaultRenderer") and [`SetDefaultRenderer`](#wx.grid.Grid.SetDefaultRenderer "wx.grid.Grid.SetDefaultRenderer")
    DefaultRowLabelSize: int  # `DefaultRowLabelSize`[¶](#wx.grid.Grid.DefaultRowLabelSize "Permalink to this definition")See [`GetDefaultRowLabelSize`](#wx.grid.Grid.GetDefaultRowLabelSize "wx.grid.Grid.GetDefaultRowLabelSize")
    DefaultRowSize: int  # `DefaultRowSize`[¶](#wx.grid.Grid.DefaultRowSize "Permalink to this definition")See [`GetDefaultRowSize`](#wx.grid.Grid.GetDefaultRowSize "wx.grid.Grid.GetDefaultRowSize") and [`SetDefaultRowSize`](#wx.grid.Grid.SetDefaultRowSize "wx.grid.Grid.SetDefaultRowSize")
    FirstFullyVisibleColumn: int  # `FirstFullyVisibleColumn`[¶](#wx.grid.Grid.FirstFullyVisibleColumn "Permalink to this definition")See [`GetFirstFullyVisibleColumn`](#wx.grid.Grid.GetFirstFullyVisibleColumn "wx.grid.Grid.GetFirstFullyVisibleColumn")
    FirstFullyVisibleRow: int  # `FirstFullyVisibleRow`[¶](#wx.grid.Grid.FirstFullyVisibleRow "Permalink to this definition")See [`GetFirstFullyVisibleRow`](#wx.grid.Grid.GetFirstFullyVisibleRow "wx.grid.Grid.GetFirstFullyVisibleRow")
    FrozenColGridWindow: 'Window'  # `FrozenColGridWindow`[¶](#wx.grid.Grid.FrozenColGridWindow "Permalink to this definition")See [`GetFrozenColGridWindow`](#wx.grid.Grid.GetFrozenColGridWindow "wx.grid.Grid.GetFrozenColGridWindow")
    FrozenCornerGridWindow: 'Window'  # `FrozenCornerGridWindow`[¶](#wx.grid.Grid.FrozenCornerGridWindow "Permalink to this definition")See [`GetFrozenCornerGridWindow`](#wx.grid.Grid.GetFrozenCornerGridWindow "wx.grid.Grid.GetFrozenCornerGridWindow")
    FrozenRowGridWindow: 'Window'  # `FrozenRowGridWindow`[¶](#wx.grid.Grid.FrozenRowGridWindow "Permalink to this definition")See [`GetFrozenRowGridWindow`](#wx.grid.Grid.GetFrozenRowGridWindow "wx.grid.Grid.GetFrozenRowGridWindow")
    GridColHeader: 'HeaderCtrl'  # `GridColHeader`[¶](#wx.grid.Grid.GridColHeader "Permalink to this definition")See [`GetGridColHeader`](#wx.grid.Grid.GetGridColHeader "wx.grid.Grid.GetGridColHeader")
    GridColLabelWindow: 'Window'  # `GridColLabelWindow`[¶](#wx.grid.Grid.GridColLabelWindow "Permalink to this definition")See [`GetGridColLabelWindow`](#wx.grid.Grid.GetGridColLabelWindow "wx.grid.Grid.GetGridColLabelWindow")
    GridCornerLabelWindow: 'Window'  # `GridCornerLabelWindow`[¶](#wx.grid.Grid.GridCornerLabelWindow "Permalink to this definition")See [`GetGridCornerLabelWindow`](#wx.grid.Grid.GetGridCornerLabelWindow "wx.grid.Grid.GetGridCornerLabelWindow")
    GridCursorCol: int  # `GridCursorCol`[¶](#wx.grid.Grid.GridCursorCol "Permalink to this definition")See [`GetGridCursorCol`](#wx.grid.Grid.GetGridCursorCol "wx.grid.Grid.GetGridCursorCol")
    GridCursorCoords: 'GridCellCoords'  # `GridCursorCoords`[¶](#wx.grid.Grid.GridCursorCoords "Permalink to this definition")See [`GetGridCursorCoords`](#wx.grid.Grid.GetGridCursorCoords "wx.grid.Grid.GetGridCursorCoords")
    GridCursorRow: int  # `GridCursorRow`[¶](#wx.grid.Grid.GridCursorRow "Permalink to this definition")See [`GetGridCursorRow`](#wx.grid.Grid.GetGridCursorRow "wx.grid.Grid.GetGridCursorRow")
    GridLineColour: 'Colour'  # `GridLineColour`[¶](#wx.grid.Grid.GridLineColour "Permalink to this definition")See [`GetGridLineColour`](#wx.grid.Grid.GetGridLineColour "wx.grid.Grid.GetGridLineColour") and [`SetGridLineColour`](#wx.grid.Grid.SetGridLineColour "wx.grid.Grid.SetGridLineColour")
    GridRowLabelWindow: 'Window'  # `GridRowLabelWindow`[¶](#wx.grid.Grid.GridRowLabelWindow "Permalink to this definition")See [`GetGridRowLabelWindow`](#wx.grid.Grid.GetGridRowLabelWindow "wx.grid.Grid.GetGridRowLabelWindow")
    GridWindow: 'Window'  # `GridWindow`[¶](#wx.grid.Grid.GridWindow "Permalink to this definition")See [`GetGridWindow`](#wx.grid.Grid.GetGridWindow "wx.grid.Grid.GetGridWindow")
    LabelBackgroundColour: 'Colour'  # `LabelBackgroundColour`[¶](#wx.grid.Grid.LabelBackgroundColour "Permalink to this definition")See [`GetLabelBackgroundColour`](#wx.grid.Grid.GetLabelBackgroundColour "wx.grid.Grid.GetLabelBackgroundColour") and [`SetLabelBackgroundColour`](#wx.grid.Grid.SetLabelBackgroundColour "wx.grid.Grid.SetLabelBackgroundColour")
    LabelFont: 'Font'  # `LabelFont`[¶](#wx.grid.Grid.LabelFont "Permalink to this definition")See [`GetLabelFont`](#wx.grid.Grid.GetLabelFont "wx.grid.Grid.GetLabelFont") and [`SetLabelFont`](#wx.grid.Grid.SetLabelFont "wx.grid.Grid.SetLabelFont")
    LabelTextColour: 'Colour'  # `LabelTextColour`[¶](#wx.grid.Grid.LabelTextColour "Permalink to this definition")See [`GetLabelTextColour`](#wx.grid.Grid.GetLabelTextColour "wx.grid.Grid.GetLabelTextColour") and [`SetLabelTextColour`](#wx.grid.Grid.SetLabelTextColour "wx.grid.Grid.SetLabelTextColour")
    NumberCols: int  # `NumberCols`[¶](#wx.grid.Grid.NumberCols "Permalink to this definition")See [`GetNumberCols`](#wx.grid.Grid.GetNumberCols "wx.grid.Grid.GetNumberCols")
    NumberFrozenCols: int  # `NumberFrozenCols`[¶](#wx.grid.Grid.NumberFrozenCols "Permalink to this definition")See [`GetNumberFrozenCols`](#wx.grid.Grid.GetNumberFrozenCols "wx.grid.Grid.GetNumberFrozenCols")
    NumberFrozenRows: int  # `NumberFrozenRows`[¶](#wx.grid.Grid.NumberFrozenRows "Permalink to this definition")See [`GetNumberFrozenRows`](#wx.grid.Grid.GetNumberFrozenRows "wx.grid.Grid.GetNumberFrozenRows")
    NumberRows: int  # `NumberRows`[¶](#wx.grid.Grid.NumberRows "Permalink to this definition")See [`GetNumberRows`](#wx.grid.Grid.GetNumberRows "wx.grid.Grid.GetNumberRows")
    RowLabelSize: int  # `RowLabelSize`[¶](#wx.grid.Grid.RowLabelSize "Permalink to this definition")See [`GetRowLabelSize`](#wx.grid.Grid.GetRowLabelSize "wx.grid.Grid.GetRowLabelSize") and [`SetRowLabelSize`](#wx.grid.Grid.SetRowLabelSize "wx.grid.Grid.SetRowLabelSize")
    RowMinimalAcceptableHeight: int  # `RowMinimalAcceptableHeight`[¶](#wx.grid.Grid.RowMinimalAcceptableHeight "Permalink to this definition")See [`GetRowMinimalAcceptableHeight`](#wx.grid.Grid.GetRowMinimalAcceptableHeight "wx.grid.Grid.GetRowMinimalAcceptableHeight") and [`SetRowMinimalAcceptableHeight`](#wx.grid.Grid.SetRowMinimalAcceptableHeight "wx.grid.Grid.SetRowMinimalAcceptableHeight")
    RowSizes: 'GridSizesInfo'  # `RowSizes`[¶](#wx.grid.Grid.RowSizes "Permalink to this definition")See [`GetRowSizes`](#wx.grid.Grid.GetRowSizes "wx.grid.Grid.GetRowSizes") and [`SetRowSizes`](#wx.grid.Grid.SetRowSizes "wx.grid.Grid.SetRowSizes")
    ScrollLineX: int  # `ScrollLineX`[¶](#wx.grid.Grid.ScrollLineX "Permalink to this definition")See [`GetScrollLineX`](#wx.grid.Grid.GetScrollLineX "wx.grid.Grid.GetScrollLineX") and [`SetScrollLineX`](#wx.grid.Grid.SetScrollLineX "wx.grid.Grid.SetScrollLineX")
    ScrollLineY: int  # `ScrollLineY`[¶](#wx.grid.Grid.ScrollLineY "Permalink to this definition")See [`GetScrollLineY`](#wx.grid.Grid.GetScrollLineY "wx.grid.Grid.GetScrollLineY") and [`SetScrollLineY`](#wx.grid.Grid.SetScrollLineY "wx.grid.Grid.SetScrollLineY")
    SelectedBlocks: 'GridBlocks'  # `SelectedBlocks`[¶](#wx.grid.Grid.SelectedBlocks "Permalink to this definition")See [`GetSelectedBlocks`](#wx.grid.Grid.GetSelectedBlocks "wx.grid.Grid.GetSelectedBlocks")
    SelectedCells: 'GridCellCoordsArray'  # `SelectedCells`[¶](#wx.grid.Grid.SelectedCells "Permalink to this definition")See [`GetSelectedCells`](#wx.grid.Grid.GetSelectedCells "wx.grid.Grid.GetSelectedCells")
    SelectedColBlocks: Any  # `SelectedColBlocks`[¶](#wx.grid.Grid.SelectedColBlocks "Permalink to this definition")See [`GetSelectedColBlocks`](#wx.grid.Grid.GetSelectedColBlocks "wx.grid.Grid.GetSelectedColBlocks")
    SelectedCols: int  # `SelectedCols`[¶](#wx.grid.Grid.SelectedCols "Permalink to this definition")See [`GetSelectedCols`](#wx.grid.Grid.GetSelectedCols "wx.grid.Grid.GetSelectedCols")
    SelectedRowBlocks: Any  # `SelectedRowBlocks`[¶](#wx.grid.Grid.SelectedRowBlocks "Permalink to this definition")See [`GetSelectedRowBlocks`](#wx.grid.Grid.GetSelectedRowBlocks "wx.grid.Grid.GetSelectedRowBlocks")
    SelectedRows: int  # `SelectedRows`[¶](#wx.grid.Grid.SelectedRows "Permalink to this definition")See [`GetSelectedRows`](#wx.grid.Grid.GetSelectedRows "wx.grid.Grid.GetSelectedRows")
    SelectionBackground: 'Colour'  # `SelectionBackground`[¶](#wx.grid.Grid.SelectionBackground "Permalink to this definition")See [`GetSelectionBackground`](#wx.grid.Grid.GetSelectionBackground "wx.grid.Grid.GetSelectionBackground") and [`SetSelectionBackground`](#wx.grid.Grid.SetSelectionBackground "wx.grid.Grid.SetSelectionBackground")
    SelectionBlockBottomRight: 'GridCellCoordsArray'  # `SelectionBlockBottomRight`[¶](#wx.grid.Grid.SelectionBlockBottomRight "Permalink to this definition")See [`GetSelectionBlockBottomRight`](#wx.grid.Grid.GetSelectionBlockBottomRight "wx.grid.Grid.GetSelectionBlockBottomRight")
    SelectionBlockTopLeft: 'GridCellCoordsArray'  # `SelectionBlockTopLeft`[¶](#wx.grid.Grid.SelectionBlockTopLeft "Permalink to this definition")See [`GetSelectionBlockTopLeft`](#wx.grid.Grid.GetSelectionBlockTopLeft "wx.grid.Grid.GetSelectionBlockTopLeft")
    SelectionForeground: 'Colour'  # `SelectionForeground`[¶](#wx.grid.Grid.SelectionForeground "Permalink to this definition")See [`GetSelectionForeground`](#wx.grid.Grid.GetSelectionForeground "wx.grid.Grid.GetSelectionForeground") and [`SetSelectionForeground`](#wx.grid.Grid.SetSelectionForeground "wx.grid.Grid.SetSelectionForeground")
    SelectionMode: 'GridSelectionModes'  # `SelectionMode`[¶](#wx.grid.Grid.SelectionMode "Permalink to this definition")See [`GetSelectionMode`](#wx.grid.Grid.GetSelectionMode "wx.grid.Grid.GetSelectionMode") and [`SetSelectionMode`](#wx.grid.Grid.SetSelectionMode "wx.grid.Grid.SetSelectionMode")
    SortingColumn: int  # `SortingColumn`[¶](#wx.grid.Grid.SortingColumn "Permalink to this definition")See [`GetSortingColumn`](#wx.grid.Grid.GetSortingColumn "wx.grid.Grid.GetSortingColumn") and [`SetSortingColumn`](#wx.grid.Grid.SetSortingColumn "wx.grid.Grid.SetSortingColumn")
    Table: 'GridTableBase'  # `Table`[¶](#wx.grid.Grid.Table "Permalink to this definition")See [`GetTable`](#wx.grid.Grid.GetTable "wx.grid.Grid.GetTable") and [`SetTable`](#wx.grid.Grid.SetTable "wx.grid.Grid.SetTable")



class GridCellAttrProvider(ClientDataContainer):
    """ **Possible constructors**:



```
GridCellAttrProvider()

```


Class providing attributes to be used for the grid cells.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellAttrProvider.__init__ "Permalink to this definition")
Trivial default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetAttr(self, row, col, kind) -> 'GridCellAttr':
        """ 

`GetAttr`(*self*, *row*, *col*, *kind*)[¶](#wx.grid.GridCellAttrProvider.GetAttr "Permalink to this definition")
Get the attribute to use for the specified cell.


If `wx.grid.GridCellAttr.Any` is used as *kind* value, this function combines the attributes set for this cell using [`SetAttr`](#wx.grid.GridCellAttrProvider.SetAttr "wx.grid.GridCellAttrProvider.SetAttr") and those for its row or column (set with [`SetRowAttr`](#wx.grid.GridCellAttrProvider.SetRowAttr "wx.grid.GridCellAttrProvider.SetRowAttr") or [`SetColAttr`](#wx.grid.GridCellAttrProvider.SetColAttr "wx.grid.GridCellAttrProvider.SetColAttr") respectively), with the cell attribute having the highest precedence.


Notice that the caller must call DecRef() on the returned pointer if it is not `None`. [`GetAttrPtr`](#wx.grid.GridCellAttrProvider.GetAttrPtr "wx.grid.GridCellAttrProvider.GetAttrPtr") method can be used to do this automatically.



Parameters
* **row** (*int*) – The row of the cell.
* **col** (*int*) – The column of the cell.
* **kind** (*GridCellAttr.wxAttrKind*) – The kind of the attribute to return.



Return type
 [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr)



Returns
The attribute to use which should be DecRef()’d by caller or `None` if no attributes are defined for this cell.






            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetAttrPtr(self, row, col, kind) -> 'GridCellAttrPtr':
        """ 

`GetAttrPtr`(*self*, *row*, *col*, *kind*)[¶](#wx.grid.GridCellAttrProvider.GetAttrPtr "Permalink to this definition")
Get the attribute to use for the specified cell.


This method is identical to [`GetAttr`](#wx.grid.GridCellAttrProvider.GetAttr "wx.grid.GridCellAttrProvider.GetAttr") , but returns a smart pointer, which frees the caller from the need to call DecRef() manually.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **kind** (*GridCellAttr.wxAttrKind*) –



Return type
`wx.grid.GridCellAttrPtr`





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetColumnHeaderRenderer(self, col: int) -> 'GridColumnHeaderRenderer':
        """ 

`GetColumnHeaderRenderer`(*self*, *col*)[¶](#wx.grid.GridCellAttrProvider.GetColumnHeaderRenderer "Permalink to this definition")
Return the renderer used for drawing column headers.


By default  [wx.grid.GridColumnHeaderRendererDefault](wx.grid.GridColumnHeaderRendererDefault.html#wx-grid-gridcolumnheaderrendererdefault) is returned.



Parameters
**col** (*int*) – 



Return type
 [wx.grid.GridColumnHeaderRenderer](wx.grid.GridColumnHeaderRenderer.html#wx-grid-gridcolumnheaderrenderer)





New in version 2.9.1.




See also


[`wx.grid.Grid.SetUseNativeColLabels`](wx.grid.Grid.html#wx.grid.Grid.SetUseNativeColLabels "wx.grid.Grid.SetUseNativeColLabels") , [`wx.grid.Grid.UseNativeColHeader`](wx.grid.Grid.html#wx.grid.Grid.UseNativeColHeader "wx.grid.Grid.UseNativeColHeader")





            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetCornerRenderer(self) -> 'GridCornerHeaderRenderer':
        """ 

`GetCornerRenderer`(*self*)[¶](#wx.grid.GridCellAttrProvider.GetCornerRenderer "Permalink to this definition")
Return the renderer used for drawing the corner window.


By default  [wx.grid.GridCornerHeaderRendererDefault](wx.grid.GridCornerHeaderRendererDefault.html#wx-grid-gridcornerheaderrendererdefault) is returned.



Return type
 [wx.grid.GridCornerHeaderRenderer](wx.grid.GridCornerHeaderRenderer.html#wx-grid-gridcornerheaderrenderer)





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def GetRowHeaderRenderer(self, row: int) -> 'GridRowHeaderRenderer':
        """ 

`GetRowHeaderRenderer`(*self*, *row*)[¶](#wx.grid.GridCellAttrProvider.GetRowHeaderRenderer "Permalink to this definition")
Return the renderer used for drawing row headers.


By default  [wx.grid.GridRowHeaderRendererDefault](wx.grid.GridRowHeaderRendererDefault.html#wx-grid-gridrowheaderrendererdefault) is returned.



Parameters
**row** (*int*) – 



Return type
 [wx.grid.GridRowHeaderRenderer](wx.grid.GridRowHeaderRenderer.html#wx-grid-gridrowheaderrenderer)





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetAttr(self, attr, row, col) -> None:
        """ 

`SetAttr`(*self*, *attr*, *row*, *col*)[¶](#wx.grid.GridCellAttrProvider.SetAttr "Permalink to this definition")
Set attribute for the specified cell.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetColAttr(self, attr, col) -> None:
        """ 

`SetColAttr`(*self*, *attr*, *col*)[¶](#wx.grid.GridCellAttrProvider.SetColAttr "Permalink to this definition")
Set attribute for the specified column.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    def SetRowAttr(self, attr, row) -> None:
        """ 

`SetRowAttr`(*self*, *attr*, *row*)[¶](#wx.grid.GridCellAttrProvider.SetRowAttr "Permalink to this definition")
Set attribute for the specified row.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **row** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellAttrProvider.html
        """

    CornerRenderer: 'GridCornerHeaderRenderer'  # `CornerRenderer`[¶](#wx.grid.GridCellAttrProvider.CornerRenderer "Permalink to this definition")See [`GetCornerRenderer`](#wx.grid.GridCellAttrProvider.GetCornerRenderer "wx.grid.GridCellAttrProvider.GetCornerRenderer")



class GridEditorCreatedEvent(CommandEvent):
    """ **Possible constructors**:



```
GridEditorCreatedEvent()

GridEditorCreatedEvent(id, type, obj, row, col, ctrl)

```


^^


  


        Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridEditorCreatedEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, id, type, obj, row, col, ctrl)*


Constructor for initializing all event attributes.



Parameters
* **id** (*int*) –
* **type** (*wx.EventType*) –
* **obj** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **row** (*int*) –
* **col** (*int*) –
* **ctrl** ([*wx.Control*](wx.Control.html#wx.Control "wx.Control")) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetCol(self) -> int:
        """ 

`GetCol`(*self*)[¶](#wx.grid.GridEditorCreatedEvent.GetCol "Permalink to this definition")
Returns the column at which the event occurred.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetControl(self) -> 'Control':
        """ 

`GetControl`(*self*)[¶](#wx.grid.GridEditorCreatedEvent.GetControl "Permalink to this definition")
Returns the edit control.


This function is preserved for compatibility, but [`GetWindow`](#wx.grid.GridEditorCreatedEvent.GetWindow "wx.grid.GridEditorCreatedEvent.GetWindow") should be preferred in the new code as the associated window doesn’t need to be of a Control-derived class.


Note that if [`SetWindow`](#wx.grid.GridEditorCreatedEvent.SetWindow "wx.grid.GridEditorCreatedEvent.SetWindow") had been called with an object not deriving from  [wx.Control](wx.Control.html#wx-control), this method will return `None`.



Return type
[`Control`](#wx.grid.GridEditorCreatedEvent.Control "wx.grid.GridEditorCreatedEvent.Control")






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetRow(self) -> int:
        """ 

`GetRow`(*self*)[¶](#wx.grid.GridEditorCreatedEvent.GetRow "Permalink to this definition")
Returns the row at which the event occurred.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def GetWindow(self) -> 'Window':
        """ 

`GetWindow`(*self*)[¶](#wx.grid.GridEditorCreatedEvent.GetWindow "Permalink to this definition")
Returns the edit window.



Return type
[`Window`](#wx.grid.GridEditorCreatedEvent.Window "wx.grid.GridEditorCreatedEvent.Window")





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetCol(self, col: int) -> None:
        """ 

`SetCol`(*self*, *col*)[¶](#wx.grid.GridEditorCreatedEvent.SetCol "Permalink to this definition")
Sets the column at which the event occurred.



Parameters
**col** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetControl(self, ctrl: 'Control') -> None:
        """ 

`SetControl`(*self*, *ctrl*)[¶](#wx.grid.GridEditorCreatedEvent.SetControl "Permalink to this definition")
Sets the edit control.


This function is preserved for compatibility, but [`SetWindow`](#wx.grid.GridEditorCreatedEvent.SetWindow "wx.grid.GridEditorCreatedEvent.SetWindow") should be preferred in the new code, see [`GetControl`](#wx.grid.GridEditorCreatedEvent.GetControl "wx.grid.GridEditorCreatedEvent.GetControl") .



Parameters
**ctrl** ([*wx.Control*](wx.Control.html#wx.Control "wx.Control")) – 






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetRow(self, row: int) -> None:
        """ 

`SetRow`(*self*, *row*)[¶](#wx.grid.GridEditorCreatedEvent.SetRow "Permalink to this definition")
Sets the row at which the event occurred.



Parameters
**row** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    def SetWindow(self, window: 'Window') -> None:
        """ 

`SetWindow`(*self*, *window*)[¶](#wx.grid.GridEditorCreatedEvent.SetWindow "Permalink to this definition")
Sets the edit window.



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.GridEditorCreatedEvent.html
        """

    Col: int  # `Col`[¶](#wx.grid.GridEditorCreatedEvent.Col "Permalink to this definition")See [`GetCol`](#wx.grid.GridEditorCreatedEvent.GetCol "wx.grid.GridEditorCreatedEvent.GetCol") and [`SetCol`](#wx.grid.GridEditorCreatedEvent.SetCol "wx.grid.GridEditorCreatedEvent.SetCol")
    Control: '_Control'  # `Control`[¶](#wx.grid.GridEditorCreatedEvent.Control "Permalink to this definition")See [`GetControl`](#wx.grid.GridEditorCreatedEvent.GetControl "wx.grid.GridEditorCreatedEvent.GetControl") and [`SetControl`](#wx.grid.GridEditorCreatedEvent.SetControl "wx.grid.GridEditorCreatedEvent.SetControl")
    Row: int  # `Row`[¶](#wx.grid.GridEditorCreatedEvent.Row "Permalink to this definition")See [`GetRow`](#wx.grid.GridEditorCreatedEvent.GetRow "wx.grid.GridEditorCreatedEvent.GetRow") and [`SetRow`](#wx.grid.GridEditorCreatedEvent.SetRow "wx.grid.GridEditorCreatedEvent.SetRow")
    Window: '_Window'  # `Window`[¶](#wx.grid.GridEditorCreatedEvent.Window "Permalink to this definition")See [`GetWindow`](#wx.grid.GridEditorCreatedEvent.GetWindow "wx.grid.GridEditorCreatedEvent.GetWindow") and [`SetWindow`](#wx.grid.GridEditorCreatedEvent.SetWindow "wx.grid.GridEditorCreatedEvent.SetWindow")



EVT_GRID_EDITOR_CREATED: int  # The editor for a cell was created. Processes a  wxEVT_GRID_EDITOR_CREATED   event type.

EVT_GRID_CMD_EDITOR_CREATED: int  # The editor for a cell was created; variant taking a window identifier. Processes a  wxEVT_GRID_EDITOR_CREATED   event type. ^^

class GridTableBase(Object):
    """ **Possible constructors**:



```
GridTableBase()

```


The almost abstract base class for grid tables.


  


        Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridTableBase.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def AppendCols(self, numCols: int=1) -> bool:
        """ 

`AppendCols`(*self*, *numCols=1*)[¶](#wx.grid.GridTableBase.AppendCols "Permalink to this definition")
Exactly the same as [`AppendRows`](#wx.grid.GridTableBase.AppendRows "wx.grid.GridTableBase.AppendRows") but for columns.



Parameters
**numCols** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def AppendRows(self, numRows: int=1) -> bool:
        """ 

`AppendRows`(*self*, *numRows=1*)[¶](#wx.grid.GridTableBase.AppendRows "Permalink to this definition")
Append additional rows at the end of the table.


This method is provided in addition to [`InsertRows`](#wx.grid.GridTableBase.InsertRows "wx.grid.GridTableBase.InsertRows") as some data models may only support appending rows to them but not inserting them at arbitrary locations. In such case you may implement this method only and leave [`InsertRows`](#wx.grid.GridTableBase.InsertRows "wx.grid.GridTableBase.InsertRows") unimplemented.



Parameters
**numRows** (*int*) – The number of rows to add.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanGetValueAs(self, row, col, typeName) -> bool:
        """ 

`CanGetValueAs`(*self*, *row*, *col*, *typeName*)[¶](#wx.grid.GridTableBase.CanGetValueAs "Permalink to this definition")
Returns `True` if the value of the given cell can be accessed as if it were of the specified type.


By default the cells can only be accessed as strings. Note that a cell could be accessible in different ways, e.g. a numeric cell may return `True` for `GRID_VALUE_NUMBER` but also for `GRID_VALUE_STRING` indicating that the value can be coerced to a string form.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **typeName** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanHaveAttributes(self) -> bool:
        """ 

`CanHaveAttributes`(*self*)[¶](#wx.grid.GridTableBase.CanHaveAttributes "Permalink to this definition")
Returns `True` if this table supports attributes or `False` otherwise.


By default, the table automatically creates a  [wx.grid.GridCellAttrProvider](wx.grid.GridCellAttrProvider.html#wx-grid-gridcellattrprovider) when this function is called if it had no attribute provider before and returns `True`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanMeasureColUsingSameAttr(self, col: int) -> bool:
        """ 

`CanMeasureColUsingSameAttr`(*self*, *col*)[¶](#wx.grid.GridTableBase.CanMeasureColUsingSameAttr "Permalink to this definition")
Override to return `True` if the same attribute can be used for measuring all cells in the given column.


This function is provided for optimization purposes: it returns `False` by default, but can be overridden to return `True` when all the cells in the same grid column use sensibly the same attribute, i.e. they use the same renderer (either explicitly, or implicitly, due to their type as returned by [`GetTypeName`](#wx.grid.GridTableBase.GetTypeName "wx.grid.GridTableBase.GetTypeName") ) and the font of the same size.


Returning `True` from this function allows AutoSizeColumns() to skip looking up the attribute and the renderer for each individual cell, which results in very noticeable performance improvements for the grids with many rows.



Parameters
**col** (*int*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def CanSetValueAs(self, row, col, typeName) -> bool:
        """ 

`CanSetValueAs`(*self*, *row*, *col*, *typeName*)[¶](#wx.grid.GridTableBase.CanSetValueAs "Permalink to this definition")
Returns `True` if the value of the given cell can be set as if it were of the specified type.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **typeName** (*string*) –



Return type
*bool*





See also


[`CanGetValueAs`](#wx.grid.GridTableBase.CanGetValueAs "wx.grid.GridTableBase.CanGetValueAs")





            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.grid.GridTableBase.Clear "Permalink to this definition")
Clear the table contents.


This method is used by [`wx.grid.Grid.ClearGrid`](wx.grid.Grid.html#wx.grid.Grid.ClearGrid "wx.grid.Grid.ClearGrid") .




            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def DeleteCols(self, pos=0, numCols=1) -> bool:
        """ 

`DeleteCols`(*self*, *pos=0*, *numCols=1*)[¶](#wx.grid.GridTableBase.DeleteCols "Permalink to this definition")
Exactly the same as [`DeleteRows`](#wx.grid.GridTableBase.DeleteRows "wx.grid.GridTableBase.DeleteRows") but for columns.



Parameters
* **pos** (*int*) –
* **numCols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def DeleteRows(self, pos=0, numRows=1) -> bool:
        """ 

`DeleteRows`(*self*, *pos=0*, *numRows=1*)[¶](#wx.grid.GridTableBase.DeleteRows "Permalink to this definition")
Delete rows from the table.



Parameters
* **pos** (*int*) – The first row to delete.
* **numRows** (*int*) – The number of rows to delete.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttr(self, row, col, kind) -> 'GridCellAttr':
        """ 

`GetAttr`(*self*, *row*, *col*, *kind*)[¶](#wx.grid.GridTableBase.GetAttr "Permalink to this definition")
Return the attribute for the given cell.


By default this function is simply forwarded to [`wx.grid.GridCellAttrProvider.GetAttr`](wx.grid.GridCellAttrProvider.html#wx.grid.GridCellAttrProvider.GetAttr "wx.grid.GridCellAttrProvider.GetAttr") but it may be overridden to handle attributes directly in the table.


Prefer to use [`GetAttrPtr`](#wx.grid.GridTableBase.GetAttrPtr "wx.grid.GridTableBase.GetAttrPtr") to avoid the need to call DecRef() on the returned pointer manually.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **kind** (*GridCellAttr.wxAttrKind*) –



Return type
 [wx.grid.GridCellAttr](wx.grid.GridCellAttr.html#wx-grid-gridcellattr)






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttrProvider(self) -> 'GridCellAttrProvider':
        """ 

`GetAttrProvider`(*self*)[¶](#wx.grid.GridTableBase.GetAttrProvider "Permalink to this definition")
Returns the attribute provider currently being used.


This function may return `None` if the attribute provider hasn’t been either associated with this table by [`SetAttrProvider`](#wx.grid.GridTableBase.SetAttrProvider "wx.grid.GridTableBase.SetAttrProvider") nor created on demand by any other methods.



Return type
 [wx.grid.GridCellAttrProvider](wx.grid.GridCellAttrProvider.html#wx-grid-gridcellattrprovider)






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetAttrPtr(self, row, col, kind) -> 'GridCellAttrPtr':
        """ 

`GetAttrPtr`(*self*, *row*, *col*, *kind*)[¶](#wx.grid.GridTableBase.GetAttrPtr "Permalink to this definition")
Return the attribute for the given cell.


This method is identical to [`GetAttr`](#wx.grid.GridTableBase.GetAttr "wx.grid.GridTableBase.GetAttr") , but returns a smart pointer, which frees the caller from the need to call DecRef() manually.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **kind** (*GridCellAttr.wxAttrKind*) –



Return type
`wx.grid.GridCellAttrPtr`





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ 

`GetColLabelValue`(*self*, *col*)[¶](#wx.grid.GridTableBase.GetColLabelValue "Permalink to this definition")
Return the label of the specified column.



Parameters
**col** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetColsCount(self) -> int:
        """ 

`GetColsCount`(*self*)[¶](#wx.grid.GridTableBase.GetColsCount "Permalink to this definition")
Return the number of columns in the table.


This method is not virtual and is only provided as a convenience for the derived classes which can’t call [`GetNumberCols`](#wx.grid.GridTableBase.GetNumberCols "wx.grid.GridTableBase.GetNumberCols") without a `const_cast` from their methods.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetCornerLabelValue(self) -> str:
        """ 

`GetCornerLabelValue`(*self*)[¶](#wx.grid.GridTableBase.GetCornerLabelValue "Permalink to this definition")
Return the label of the grid’s corner.



Return type
`string`





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetNumberCols(self) -> int:
        """ 

`GetNumberCols`(*self*)[¶](#wx.grid.GridTableBase.GetNumberCols "Permalink to this definition")
Must be overridden to return the number of columns in the table.


For backwards compatibility reasons, this method is not const. Use [`GetColsCount`](#wx.grid.GridTableBase.GetColsCount "wx.grid.GridTableBase.GetColsCount") instead of it in methods of derived table classes,



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetNumberRows(self) -> int:
        """ 

`GetNumberRows`(*self*)[¶](#wx.grid.GridTableBase.GetNumberRows "Permalink to this definition")
Must be overridden to return the number of rows in the table.


For backwards compatibility reasons, this method is not const. Use [`GetRowsCount`](#wx.grid.GridTableBase.GetRowsCount "wx.grid.GridTableBase.GetRowsCount") instead of it in methods of derived table classes.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ 

`GetRowLabelValue`(*self*, *row*)[¶](#wx.grid.GridTableBase.GetRowLabelValue "Permalink to this definition")
Return the label of the specified row.



Parameters
**row** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetRowsCount(self) -> int:
        """ 

`GetRowsCount`(*self*)[¶](#wx.grid.GridTableBase.GetRowsCount "Permalink to this definition")
Return the number of rows in the table.


This method is not virtual and is only provided as a convenience for the derived classes which can’t call [`GetNumberRows`](#wx.grid.GridTableBase.GetNumberRows "wx.grid.GridTableBase.GetNumberRows") without a `const_cast` from their methods.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetTypeName(self, row, col) -> str:
        """ 

`GetTypeName`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.GetTypeName "Permalink to this definition")
Returns the type of the value in the given cell.


By default all cells are strings and this method returns `GRID_VALUE_STRING` .



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValue(self, row, col) -> Any:
        """ 

`GetValue`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.GetValue "Permalink to this definition")
Must be overridden to implement accessing the table values as text.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsBool(self, row, col) -> bool:
        """ 

`GetValueAsBool`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.GetValueAsBool "Permalink to this definition")
Returns the value of the given cell as a boolean.


This should only be called if [`CanGetValueAs`](#wx.grid.GridTableBase.CanGetValueAs "wx.grid.GridTableBase.CanGetValueAs") returns `True` when called with `GRID_VALUE_BOOL` argument. Default implementation always return `False`.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsDouble(self, row, col) -> float:
        """ 

`GetValueAsDouble`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.GetValueAsDouble "Permalink to this definition")
Returns the value of the given cell as a double.


This should only be called if [`CanGetValueAs`](#wx.grid.GridTableBase.CanGetValueAs "wx.grid.GridTableBase.CanGetValueAs") returns `True` when called with `GRID_VALUE_FLOAT` argument. Default implementation always return 0.0.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*float*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetValueAsLong(self, row, col) -> int:
        """ 

`GetValueAsLong`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.GetValueAsLong "Permalink to this definition")
Returns the value of the given cell as a long.


This should only be called if [`CanGetValueAs`](#wx.grid.GridTableBase.CanGetValueAs "wx.grid.GridTableBase.CanGetValueAs") returns `True` when called with `GRID_VALUE_NUMBER` argument. Default implementation always return 0.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def GetView(self) -> 'Grid':
        """ 

`GetView`(*self*)[¶](#wx.grid.GridTableBase.GetView "Permalink to this definition")
Returns the last grid passed to [`SetView`](#wx.grid.GridTableBase.SetView "wx.grid.GridTableBase.SetView") .



Return type
 [wx.grid.Grid](wx.grid.Grid.html#wx-grid-grid)






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def InsertCols(self, pos=0, numCols=1) -> bool:
        """ 

`InsertCols`(*self*, *pos=0*, *numCols=1*)[¶](#wx.grid.GridTableBase.InsertCols "Permalink to this definition")
Exactly the same as [`InsertRows`](#wx.grid.GridTableBase.InsertRows "wx.grid.GridTableBase.InsertRows") but for columns.



Parameters
* **pos** (*int*) –
* **numCols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def InsertRows(self, pos=0, numRows=1) -> bool:
        """ 

`InsertRows`(*self*, *pos=0*, *numRows=1*)[¶](#wx.grid.GridTableBase.InsertRows "Permalink to this definition")
Insert additional rows into the table.



Parameters
* **pos** (*int*) – The position of the first new row.
* **numRows** (*int*) – The number of rows to insert.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def IsEmpty(self, coords: 'grid.GridCellCoords') -> bool:
        """ 

`IsEmpty`(*self*, *coords*)[¶](#wx.grid.GridTableBase.IsEmpty "Permalink to this definition")
Same as [`IsEmptyCell`](#wx.grid.GridTableBase.IsEmptyCell "wx.grid.GridTableBase.IsEmptyCell") but taking  [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords).


Notice that this method is not virtual, only [`IsEmptyCell`](#wx.grid.GridTableBase.IsEmptyCell "wx.grid.GridTableBase.IsEmptyCell") should be overridden.



Parameters
**coords** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def IsEmptyCell(self, row, col) -> bool:
        """ 

`IsEmptyCell`(*self*, *row*, *col*)[¶](#wx.grid.GridTableBase.IsEmptyCell "Permalink to this definition")
May be overridden to implement testing for empty cells.


This method is used by the grid to test if the given cell is not used and so whether a neighbouring cell may overflow into it. By default it only returns `True` if the value of the given cell, as returned by [`GetValue`](#wx.grid.GridTableBase.GetValue "wx.grid.GridTableBase.GetValue") , is empty.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetAttr(self, attr, row, col) -> None:
        """ 

`SetAttr`(*self*, *attr*, *row*, *col*)[¶](#wx.grid.GridTableBase.SetAttr "Permalink to this definition")
Set attribute of the specified cell.


By default this function is simply forwarded to [`wx.grid.GridCellAttrProvider.SetAttr`](wx.grid.GridCellAttrProvider.html#wx.grid.GridCellAttrProvider.SetAttr "wx.grid.GridCellAttrProvider.SetAttr") .


The table takes ownership of `attr`, i.e. will call DecRef() on it.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetAttrProvider(self, attrProvider: 'grid.GridCellAttrProvider') -> None:
        """ 

`SetAttrProvider`(*self*, *attrProvider*)[¶](#wx.grid.GridTableBase.SetAttrProvider "Permalink to this definition")
Associate this attributes provider with the table.


The table takes ownership of *attrProvider* pointer and will delete it when it doesn’t need it any more. The pointer can be `None`, however this won’t disable attributes management in the table but will just result in a default attributes being recreated the next time any of the other functions in this section is called. To completely disable the attributes support, should this be needed, you need to override [`CanHaveAttributes`](#wx.grid.GridTableBase.CanHaveAttributes "wx.grid.GridTableBase.CanHaveAttributes") to return `False`.



Parameters
**attrProvider** ([*wx.grid.GridCellAttrProvider*](wx.grid.GridCellAttrProvider.html#wx.grid.GridCellAttrProvider "wx.grid.GridCellAttrProvider")) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetColAttr(self, attr, col) -> None:
        """ 

`SetColAttr`(*self*, *attr*, *col*)[¶](#wx.grid.GridTableBase.SetColAttr "Permalink to this definition")
Set attribute of the specified column.


By default this function is simply forwarded to [`wx.grid.GridCellAttrProvider.SetColAttr`](wx.grid.GridCellAttrProvider.html#wx.grid.GridCellAttrProvider.SetColAttr "wx.grid.GridCellAttrProvider.SetColAttr") .


The table takes ownership of `attr`, i.e. will call DecRef() on it.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetColLabelValue(self, col, label) -> None:
        """ 

`SetColLabelValue`(*self*, *col*, *label*)[¶](#wx.grid.GridTableBase.SetColLabelValue "Permalink to this definition")
Exactly the same as [`SetRowLabelValue`](#wx.grid.GridTableBase.SetRowLabelValue "wx.grid.GridTableBase.SetRowLabelValue") but for columns.



Parameters
* **col** (*int*) –
* **label** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetCornerLabelValue(self) -> None:
        """ 

`SetCornerLabelValue`(*self*)[¶](#wx.grid.GridTableBase.SetCornerLabelValue "Permalink to this definition")
Set the given label for the grid’s corner.


The default version does nothing, i.e. the label is not stored. You must override this method in your derived class if you wish [`wx.grid.Grid.GetCornerLabelValue`](wx.grid.Grid.html#wx.grid.Grid.GetCornerLabelValue "wx.grid.Grid.GetCornerLabelValue") to work.



Parameters
**``** (*string*) – 





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetRowAttr(self, attr, row) -> None:
        """ 

`SetRowAttr`(*self*, *attr*, *row*)[¶](#wx.grid.GridTableBase.SetRowAttr "Permalink to this definition")
Set attribute of the specified row.


By default this function is simply forwarded to [`wx.grid.GridCellAttrProvider.SetRowAttr`](wx.grid.GridCellAttrProvider.html#wx.grid.GridCellAttrProvider.SetRowAttr "wx.grid.GridCellAttrProvider.SetRowAttr") .


The table takes ownership of `attr`, i.e. will call DecRef() on it.



Parameters
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **row** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetRowLabelValue(self, row, label) -> None:
        """ 

`SetRowLabelValue`(*self*, *row*, *label*)[¶](#wx.grid.GridTableBase.SetRowLabelValue "Permalink to this definition")
Set the given label for the specified row.


The default version does nothing, i.e. the label is not stored. You must override this method in your derived class if you wish [`wx.grid.Grid.SetRowLabelValue`](wx.grid.Grid.html#wx.grid.Grid.SetRowLabelValue "wx.grid.Grid.SetRowLabelValue") to work.



Parameters
* **row** (*int*) –
* **label** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValue(self, row, col, value) -> None:
        """ 

`SetValue`(*self*, *row*, *col*, *value*)[¶](#wx.grid.GridTableBase.SetValue "Permalink to this definition")
Must be overridden to implement setting the table values as text.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsBool(self, row, col, value) -> None:
        """ 

`SetValueAsBool`(*self*, *row*, *col*, *value*)[¶](#wx.grid.GridTableBase.SetValueAsBool "Permalink to this definition")
Sets the value of the given cell as a boolean.


This should only be called if [`CanSetValueAs`](#wx.grid.GridTableBase.CanSetValueAs "wx.grid.GridTableBase.CanSetValueAs") returns `True` when called with `GRID_VALUE_BOOL` argument. Default implementation doesn’t do anything.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **value** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsDouble(self, row, col, value) -> None:
        """ 

`SetValueAsDouble`(*self*, *row*, *col*, *value*)[¶](#wx.grid.GridTableBase.SetValueAsDouble "Permalink to this definition")
Sets the value of the given cell as a double.


This should only be called if [`CanSetValueAs`](#wx.grid.GridTableBase.CanSetValueAs "wx.grid.GridTableBase.CanSetValueAs") returns `True` when called with `GRID_VALUE_FLOAT` argument. Default implementation doesn’t do anything.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **value** (*float*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetValueAsLong(self, row, col, value) -> None:
        """ 

`SetValueAsLong`(*self*, *row*, *col*, *value*)[¶](#wx.grid.GridTableBase.SetValueAsLong "Permalink to this definition")
Sets the value of the given cell as a long.


This should only be called if [`CanSetValueAs`](#wx.grid.GridTableBase.CanSetValueAs "wx.grid.GridTableBase.CanSetValueAs") returns `True` when called with `GRID_VALUE_NUMBER` argument. Default implementation doesn’t do anything.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **value** (*long*) –






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    def SetView(self, grid: 'grid.Grid') -> None:
        """ 

`SetView`(*self*, *grid*)[¶](#wx.grid.GridTableBase.SetView "Permalink to this definition")
Called by the grid when the table is associated with it.


The default implementation stores the pointer and returns it from its [`GetView`](#wx.grid.GridTableBase.GetView "wx.grid.GridTableBase.GetView") and so only makes sense if the table cannot be associated with more than one grid at a time.



Parameters
**grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableBase.html
        """

    AttrProvider: 'GridCellAttrProvider'  # `AttrProvider`[¶](#wx.grid.GridTableBase.AttrProvider "Permalink to this definition")See [`GetAttrProvider`](#wx.grid.GridTableBase.GetAttrProvider "wx.grid.GridTableBase.GetAttrProvider") and [`SetAttrProvider`](#wx.grid.GridTableBase.SetAttrProvider "wx.grid.GridTableBase.SetAttrProvider")
    ColsCount: int  # `ColsCount`[¶](#wx.grid.GridTableBase.ColsCount "Permalink to this definition")See [`GetColsCount`](#wx.grid.GridTableBase.GetColsCount "wx.grid.GridTableBase.GetColsCount")
    CornerLabelValue: str  # `CornerLabelValue`[¶](#wx.grid.GridTableBase.CornerLabelValue "Permalink to this definition")See [`GetCornerLabelValue`](#wx.grid.GridTableBase.GetCornerLabelValue "wx.grid.GridTableBase.GetCornerLabelValue") and [`SetCornerLabelValue`](#wx.grid.GridTableBase.SetCornerLabelValue "wx.grid.GridTableBase.SetCornerLabelValue")
    NumberCols: int  # `NumberCols`[¶](#wx.grid.GridTableBase.NumberCols "Permalink to this definition")See [`GetNumberCols`](#wx.grid.GridTableBase.GetNumberCols "wx.grid.GridTableBase.GetNumberCols")
    NumberRows: int  # `NumberRows`[¶](#wx.grid.GridTableBase.NumberRows "Permalink to this definition")See [`GetNumberRows`](#wx.grid.GridTableBase.GetNumberRows "wx.grid.GridTableBase.GetNumberRows")
    RowsCount: int  # `RowsCount`[¶](#wx.grid.GridTableBase.RowsCount "Permalink to this definition")See [`GetRowsCount`](#wx.grid.GridTableBase.GetRowsCount "wx.grid.GridTableBase.GetRowsCount")
    View: 'Grid'  # `View`[¶](#wx.grid.GridTableBase.View "Permalink to this definition")See [`GetView`](#wx.grid.GridTableBase.GetView "wx.grid.GridTableBase.GetView") and [`SetView`](#wx.grid.GridTableBase.SetView "wx.grid.GridTableBase.SetView")



class GridStringTable(GridTableBase):
    """ **Possible constructors**:



```
GridStringTable()

GridStringTable(numRows, numCols)

```


Simplest type of data table for a grid for small tables of strings
that are stored in memory.


  


        Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridStringTable.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor creates an empty table.




---

  



**\_\_init\_\_** *(self, numRows, numCols)*


Constructor taking number of rows and columns.



Parameters
* **numRows** (*int*) –
* **numCols** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def AppendCols(self, numCols: int=1) -> bool:
        """ 

`AppendCols`(*self*, *numCols=1*)[¶](#wx.grid.GridStringTable.AppendCols "Permalink to this definition")
Exactly the same as [`AppendRows`](#wx.grid.GridStringTable.AppendRows "wx.grid.GridStringTable.AppendRows") but for columns.



Parameters
**numCols** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def AppendRows(self, numRows: int=1) -> bool:
        """ 

`AppendRows`(*self*, *numRows=1*)[¶](#wx.grid.GridStringTable.AppendRows "Permalink to this definition")
Append additional rows at the end of the table.


This method is provided in addition to [`InsertRows`](#wx.grid.GridStringTable.InsertRows "wx.grid.GridStringTable.InsertRows") as some data models may only support appending rows to them but not inserting them at arbitrary locations. In such case you may implement this method only and leave [`InsertRows`](#wx.grid.GridStringTable.InsertRows "wx.grid.GridStringTable.InsertRows") unimplemented.



Parameters
**numRows** (*int*) – The number of rows to add.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.grid.GridStringTable.Clear "Permalink to this definition")
Clear the table contents.


This method is used by [`wx.grid.Grid.ClearGrid`](wx.grid.Grid.html#wx.grid.Grid.ClearGrid "wx.grid.Grid.ClearGrid") .




            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def DeleteCols(self, pos=0, numCols=1) -> bool:
        """ 

`DeleteCols`(*self*, *pos=0*, *numCols=1*)[¶](#wx.grid.GridStringTable.DeleteCols "Permalink to this definition")
Exactly the same as [`DeleteRows`](#wx.grid.GridStringTable.DeleteRows "wx.grid.GridStringTable.DeleteRows") but for columns.



Parameters
* **pos** (*int*) –
* **numCols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def DeleteRows(self, pos=0, numRows=1) -> bool:
        """ 

`DeleteRows`(*self*, *pos=0*, *numRows=1*)[¶](#wx.grid.GridStringTable.DeleteRows "Permalink to this definition")
Delete rows from the table.



Parameters
* **pos** (*int*) – The first row to delete.
* **numRows** (*int*) – The number of rows to delete.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetColLabelValue(self, col: int) -> str:
        """ 

`GetColLabelValue`(*self*, *col*)[¶](#wx.grid.GridStringTable.GetColLabelValue "Permalink to this definition")
Return the label of the specified column.



Parameters
**col** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetCornerLabelValue(self) -> str:
        """ 

`GetCornerLabelValue`(*self*)[¶](#wx.grid.GridStringTable.GetCornerLabelValue "Permalink to this definition")
Return the label of the grid’s corner.



Return type
`string`





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetNumberCols(self) -> int:
        """ 

`GetNumberCols`(*self*)[¶](#wx.grid.GridStringTable.GetNumberCols "Permalink to this definition")
Must be overridden to return the number of columns in the table.


For backwards compatibility reasons, this method is not const. Use [`GetColsCount`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.GetColsCount "wx.grid.GridTableBase.GetColsCount") instead of it in methods of derived table classes,



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetNumberRows(self) -> int:
        """ 

`GetNumberRows`(*self*)[¶](#wx.grid.GridStringTable.GetNumberRows "Permalink to this definition")
Must be overridden to return the number of rows in the table.


For backwards compatibility reasons, this method is not const. Use [`GetRowsCount`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.GetRowsCount "wx.grid.GridTableBase.GetRowsCount") instead of it in methods of derived table classes.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetRowLabelValue(self, row: int) -> str:
        """ 

`GetRowLabelValue`(*self*, *row*)[¶](#wx.grid.GridStringTable.GetRowLabelValue "Permalink to this definition")
Return the label of the specified row.



Parameters
**row** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def GetValue(self, row, col) -> str:
        """ 

`GetValue`(*self*, *row*, *col*)[¶](#wx.grid.GridStringTable.GetValue "Permalink to this definition")
Must be overridden to implement accessing the table values as text.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def InsertCols(self, pos=0, numCols=1) -> bool:
        """ 

`InsertCols`(*self*, *pos=0*, *numCols=1*)[¶](#wx.grid.GridStringTable.InsertCols "Permalink to this definition")
Exactly the same as [`InsertRows`](#wx.grid.GridStringTable.InsertRows "wx.grid.GridStringTable.InsertRows") but for columns.



Parameters
* **pos** (*int*) –
* **numCols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def InsertRows(self, pos=0, numRows=1) -> bool:
        """ 

`InsertRows`(*self*, *pos=0*, *numRows=1*)[¶](#wx.grid.GridStringTable.InsertRows "Permalink to this definition")
Insert additional rows into the table.



Parameters
* **pos** (*int*) – The position of the first new row.
* **numRows** (*int*) – The number of rows to insert.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetColLabelValue(self, col, label) -> None:
        """ 

`SetColLabelValue`(*self*, *col*, *label*)[¶](#wx.grid.GridStringTable.SetColLabelValue "Permalink to this definition")
Exactly the same as [`SetRowLabelValue`](#wx.grid.GridStringTable.SetRowLabelValue "wx.grid.GridStringTable.SetRowLabelValue") but for columns.



Parameters
* **col** (*int*) –
* **label** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetCornerLabelValue(self) -> None:
        """ 

`SetCornerLabelValue`(*self*)[¶](#wx.grid.GridStringTable.SetCornerLabelValue "Permalink to this definition")
Set the given label for the grid’s corner.


The default version does nothing, i.e. the label is not stored. You must override this method in your derived class if you wish [`wx.grid.Grid.GetCornerLabelValue`](wx.grid.Grid.html#wx.grid.Grid.GetCornerLabelValue "wx.grid.Grid.GetCornerLabelValue") to work.



Parameters
**``** (*string*) – 





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetRowLabelValue(self, row, label) -> None:
        """ 

`SetRowLabelValue`(*self*, *row*, *label*)[¶](#wx.grid.GridStringTable.SetRowLabelValue "Permalink to this definition")
Set the given label for the specified row.


The default version does nothing, i.e. the label is not stored. You must override this method in your derived class if you wish [`wx.grid.Grid.SetRowLabelValue`](wx.grid.Grid.html#wx.grid.Grid.SetRowLabelValue "wx.grid.Grid.SetRowLabelValue") to work.



Parameters
* **row** (*int*) –
* **label** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    def SetValue(self, row, col, value) -> None:
        """ 

`SetValue`(*self*, *row*, *col*, *value*)[¶](#wx.grid.GridStringTable.SetValue "Permalink to this definition")
Must be overridden to implement setting the table values as text.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridStringTable.html
        """

    CornerLabelValue: str  # `CornerLabelValue`[¶](#wx.grid.GridStringTable.CornerLabelValue "Permalink to this definition")See [`GetCornerLabelValue`](#wx.grid.GridStringTable.GetCornerLabelValue "wx.grid.GridStringTable.GetCornerLabelValue") and [`SetCornerLabelValue`](#wx.grid.GridStringTable.SetCornerLabelValue "wx.grid.GridStringTable.SetCornerLabelValue")
    NumberCols: int  # `NumberCols`[¶](#wx.grid.GridStringTable.NumberCols "Permalink to this definition")See [`GetNumberCols`](#wx.grid.GridStringTable.GetNumberCols "wx.grid.GridStringTable.GetNumberCols")
    NumberRows: int  # `NumberRows`[¶](#wx.grid.GridStringTable.NumberRows "Permalink to this definition")See [`GetNumberRows`](#wx.grid.GridStringTable.GetNumberRows "wx.grid.GridStringTable.GetNumberRows")



class GridCellRenderer(SharedClientDataContainer,RefCounter):
    """ **Possible constructors**:



```
GridCellRenderer()

```


This class is responsible for actually drawing the cell in the grid.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellRenderer.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def Clone(self) -> 'GridCellRenderer':
        """ 

`Clone`(*self*)[¶](#wx.grid.GridCellRenderer.Clone "Permalink to this definition")
This function must be implemented in derived classes to return a copy of itself.



Return type
 [wx.grid.GridCellRenderer](#wx-grid-gridcellrenderer)






            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def Draw(self, grid, attr, dc, rect, row, col, isSelected) -> None:
        """ 

`Draw`(*self*, *grid*, *attr*, *dc*, *rect*, *row*, *col*, *isSelected*)[¶](#wx.grid.GridCellRenderer.Draw "Permalink to this definition")
Draw the given cell on the provided DC inside the given rectangle using the style specified by the attribute and the default or selected state corresponding to the isSelected value.


This pure virtual function has a default implementation which will prepare the DC using the given attribute: it will draw the rectangle with the background colour from attr and set the text colour and font.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **row** (*int*) –
* **col** (*int*) –
* **isSelected** (*bool*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestHeight(self, grid, attr, dc, row, col, width) -> int:
        """ 

`GetBestHeight`(*self*, *grid*, *attr*, *dc*, *row*, *col*, *width*)[¶](#wx.grid.GridCellRenderer.GetBestHeight "Permalink to this definition")
Get the preferred height of the cell at the given width.


Some renderers may not have a well-defined best size, but only be able to provide the best height at the given width, e.g. this is the case of the standard  [wx.grid.GridCellAutoWrapStringRenderer](wx.grid.GridCellAutoWrapStringRenderer.html#wx-grid-gridcellautowrapstringrenderer). In this case, they should override this method, in addition to [`GetBestSize`](#wx.grid.GridCellRenderer.GetBestSize "wx.grid.GridCellRenderer.GetBestSize") .



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **row** (*int*) –
* **col** (*int*) –
* **width** (*int*) –



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.




See also


[`GetBestWidth`](#wx.grid.GridCellRenderer.GetBestWidth "wx.grid.GridCellRenderer.GetBestWidth")





            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestSize(self, grid, attr, dc, row, col) -> 'Size':
        """ 

`GetBestSize`(*self*, *grid*, *attr*, *dc*, *row*, *col*)[¶](#wx.grid.GridCellRenderer.GetBestSize "Permalink to this definition")
Get the preferred size of the cell for its contents.


This method must be overridden in the derived classes to return the minimal fitting size for displaying the content of the given grid cell.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **row** (*int*) –
* **col** (*int*) –



Return type
*Size*





See also


[`GetBestHeight`](#wx.grid.GridCellRenderer.GetBestHeight "wx.grid.GridCellRenderer.GetBestHeight") , [`GetBestWidth`](#wx.grid.GridCellRenderer.GetBestWidth "wx.grid.GridCellRenderer.GetBestWidth")





            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetBestWidth(self, grid, attr, dc, row, col, height) -> int:
        """ 

`GetBestWidth`(*self*, *grid*, *attr*, *dc*, *row*, *col*, *height*)[¶](#wx.grid.GridCellRenderer.GetBestWidth "Permalink to this definition")
Get the preferred width of the cell at the given height.


See [`GetBestHeight`](#wx.grid.GridCellRenderer.GetBestHeight "wx.grid.GridCellRenderer.GetBestHeight") , this method is symmetric to it.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **row** (*int*) –
* **col** (*int*) –
* **height** (*int*) –



Return type
*int*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """

    def GetMaxBestSize(self, grid, attr, dc) -> 'Size':
        """ 

`GetMaxBestSize`(*self*, *grid*, *attr*, *dc*)[¶](#wx.grid.GridCellRenderer.GetMaxBestSize "Permalink to this definition")
Get the maximum possible size for a cell using this renderer, if possible.


This function may be overridden in the derived class if it can return the maximum size needed for displaying the cells rendered it without iterating over all cells. The base class version simply returns `wx.DefaultSize` , indicating that this is infeasible and that [`GetBestSize`](#wx.grid.GridCellRenderer.GetBestSize "wx.grid.GridCellRenderer.GetBestSize") should be called for each cell individually.


Note that this method will only be used if [`wx.grid.GridTableBase.CanMeasureColUsingSameAttr`](wx.grid.GridTableBase.html#wx.grid.GridTableBase.CanMeasureColUsingSameAttr "wx.grid.GridTableBase.CanMeasureColUsingSameAttr") is overridden to return `True`.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –



Return type
*Size*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellRenderer.html
        """



class GridCellBoolRenderer(GridCellRenderer):
    """ **Possible constructors**:



```
GridCellBoolRenderer()

```


This class may be used to format boolean data in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellBoolRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellBoolRenderer.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellBoolRenderer.html
        """



class GridCellFloatRenderer(GridCellStringRenderer):
    """ **Possible constructors**:



```
GridCellFloatRenderer(width=-1, precision=-1,
                      format=GRID_FLOAT_FORMAT_DEFAULT)

```


This class may be used to format floating point data in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
    """
    def __init__(self, width=-1, precision=-1, format=GRID_FLOAT_FORMAT_DEFAULT) -> None:
        """ 

`__init__`(*self*, *width=-1*, *precision=-1*, *format=GRID\_FLOAT\_FORMAT\_DEFAULT*)[¶](#wx.grid.GridCellFloatRenderer.__init__ "Permalink to this definition")
Float cell renderer constructor.



Parameters
* **width** (*int*) – Minimum number of characters to be shown.
* **precision** (*int*) – Number of digits after the decimal dot.
* **format** (*int*) – The format used to display the string, must be a combination of  [wx.grid.GridCellFloatFormat](wx.grid.GridCellFloatFormat.enumeration.html#wx-grid-gridcellfloatformat) enum elements. This parameter is only available since wxWidgets 2.9.3.






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetFormat(self) -> int:
        """ 

`GetFormat`(*self*)[¶](#wx.grid.GridCellFloatRenderer.GetFormat "Permalink to this definition")
Returns the specifier used to format the data to string.


The returned value is a combination of  [wx.grid.GridCellFloatFormat](wx.grid.GridCellFloatFormat.enumeration.html#wx-grid-gridcellfloatformat) elements.



Return type
*int*





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetPrecision(self) -> int:
        """ 

`GetPrecision`(*self*)[¶](#wx.grid.GridCellFloatRenderer.GetPrecision "Permalink to this definition")
Returns the precision.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def GetWidth(self) -> int:
        """ 

`GetWidth`(*self*)[¶](#wx.grid.GridCellFloatRenderer.GetWidth "Permalink to this definition")
Returns the width.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetFormat(self, format: int) -> None:
        """ 

`SetFormat`(*self*, *format*)[¶](#wx.grid.GridCellFloatRenderer.SetFormat "Permalink to this definition")
Set the format to use for display the number.



Parameters
**format** (*int*) – Must be a combination of  [wx.grid.GridCellFloatFormat](wx.grid.GridCellFloatFormat.enumeration.html#wx-grid-gridcellfloatformat) enum elements.





New in version 2.9.3.





            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellFloatRenderer.SetParameters "Permalink to this definition")
The parameters string format is “width[,precision[,format]]” where `format` should be chosen between f|e|g|E|G (f is used by default)



Parameters
**params** (*string*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetPrecision(self, precision: int) -> None:
        """ 

`SetPrecision`(*self*, *precision*)[¶](#wx.grid.GridCellFloatRenderer.SetPrecision "Permalink to this definition")
Sets the precision.



Parameters
**precision** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    def SetWidth(self, width: int) -> None:
        """ 

`SetWidth`(*self*, *width*)[¶](#wx.grid.GridCellFloatRenderer.SetWidth "Permalink to this definition")
Sets the width.



Parameters
**width** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatRenderer.html
        """

    Format: int  # `Format`[¶](#wx.grid.GridCellFloatRenderer.Format "Permalink to this definition")See [`GetFormat`](#wx.grid.GridCellFloatRenderer.GetFormat "wx.grid.GridCellFloatRenderer.GetFormat") and [`SetFormat`](#wx.grid.GridCellFloatRenderer.SetFormat "wx.grid.GridCellFloatRenderer.SetFormat")
    Precision: int  # `Precision`[¶](#wx.grid.GridCellFloatRenderer.Precision "Permalink to this definition")See [`GetPrecision`](#wx.grid.GridCellFloatRenderer.GetPrecision "wx.grid.GridCellFloatRenderer.GetPrecision") and [`SetPrecision`](#wx.grid.GridCellFloatRenderer.SetPrecision "wx.grid.GridCellFloatRenderer.SetPrecision")
    Width: int  # `Width`[¶](#wx.grid.GridCellFloatRenderer.Width "Permalink to this definition")See [`GetWidth`](#wx.grid.GridCellFloatRenderer.GetWidth "wx.grid.GridCellFloatRenderer.GetWidth") and [`SetWidth`](#wx.grid.GridCellFloatRenderer.SetWidth "wx.grid.GridCellFloatRenderer.SetWidth")



class GridCellNumberRenderer(GridCellStringRenderer):
    """ **Possible constructors**:



```
GridCellNumberRenderer()

```


This class may be used to format integer data in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellNumberRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellNumberRenderer.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellNumberRenderer.html
        """



class GridCellStringRenderer(GridCellRenderer):
    """ **Possible constructors**:



```
GridCellStringRenderer()

```


This class may be used to format string data in a cell; it is the
default for string cells.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellStringRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellStringRenderer.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellStringRenderer.html
        """



class GridCellDateRenderer(GridCellStringRenderer):
    """ **Possible constructors**:



```
GridCellDateRenderer(outformat="")

```


This class may be used to show a date, without time, in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
    """
    def __init__(self, outformat: str="") -> None:
        """ 

`__init__`(*self*, *outformat=""*)[¶](#wx.grid.GridCellDateRenderer.__init__ "Permalink to this definition")
Date renderer constructor.



Parameters
**outformat** (*string*) – strftime()-like format string used to render the output date. By default (or if provided format string is empty) localized date representation (“%x”) is used.






            Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellDateRenderer.SetParameters "Permalink to this definition")
Sets the strftime()-like format string which will be used to render the date.



Parameters
**params** (*string*) – strftime()-like format string used to render the date.






            Source: https://docs.wxpython.org/wx.grid.GridCellDateRenderer.html
        """



class GridCellDateTimeRenderer(GridCellDateRenderer):
    """ **Possible constructors**:



```
GridCellDateTimeRenderer(outformat=DefaultDateTimeFormat,
                         informat=DefaultDateTimeFormat)

```


This class may be used to format a date/time data in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellDateTimeRenderer.html
    """
    def __init__(self, outformat=DefaultDateTimeFormat, informat=DefaultDateTimeFormat) -> None:
        """ 

`__init__`(*self*, *outformat=DefaultDateTimeFormat*, *informat=DefaultDateTimeFormat*)[¶](#wx.grid.GridCellDateTimeRenderer.__init__ "Permalink to this definition")
Date/time renderer constructor.



Parameters
* **outformat** (*string*) – strptime()-like format string used the parse the output date/time.
* **informat** (*string*) – strptime()-like format string used to parse the string entered in the cell.






            Source: https://docs.wxpython.org/wx.grid.GridCellDateTimeRenderer.html
        """



class GridCellAttr(SharedClientDataContainer,RefCounter):
    """ **Possible constructors**:



```
GridCellAttr(attrDefault=None)

GridCellAttr(colText, colBack, font, hAlign, vAlign)

```


This class can be used to alter the cells’ appearance in the grid by
changing their attributes from the defaults.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridCellAttr.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, attrDefault=None)*


Default constructor.



Parameters
**attrDefault** ([*wx.grid.GridCellAttr*](#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) – 






---

  



**\_\_init\_\_** *(self, colText, colBack, font, hAlign, vAlign)*


Constructor specifying some of the often used attributes.



Parameters
* **colText** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **colBack** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) –
* **font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) –
* **hAlign** (*int*) –
* **vAlign** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def CanOverflow(self) -> bool:
        """ 

`CanOverflow`(*self*)[¶](#wx.grid.GridCellAttr.CanOverflow "Permalink to this definition")
Returns `True` if the cell will draw an overflowed text into the neighbouring cells.


Note that only left aligned cells currently can overflow. It means that [`GetFitMode`](#wx.grid.GridCellAttr.GetFitMode "wx.grid.GridCellAttr.GetFitMode") .IsOverflow() should returns `True` and GetAlignment should returns `wx.ALIGN_LEFT` for hAlign parameter.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def Clone(self) -> 'GridCellAttr':
        """ 

`Clone`(*self*)[¶](#wx.grid.GridCellAttr.Clone "Permalink to this definition")
Creates a new copy of this object.



Return type
 [wx.grid.GridCellAttr](#wx-grid-gridcellattr)






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def DecRef(self) -> None:
        """ 

`DecRef`(*self*)[¶](#wx.grid.GridCellAttr.DecRef "Permalink to this definition")
This class is reference counted: it is created with ref count of 1, so calling [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") once will delete it.


Calling [`IncRef`](#wx.grid.GridCellAttr.IncRef "wx.grid.GridCellAttr.IncRef") allows locking it until the matching [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") is called.




            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetAlignment(self) -> tuple:
        """ 

`GetAlignment`(*self*)[¶](#wx.grid.GridCellAttr.GetAlignment "Permalink to this definition")
Get the alignment to use for the cell with the given attribute.


If this attribute doesn’t specify any alignment, the default attribute alignment is used (which can be changed using [`wx.grid.Grid.SetDefaultCellAlignment`](wx.grid.Grid.html#wx.grid.Grid.SetDefaultCellAlignment "wx.grid.Grid.SetDefaultCellAlignment") but is left and top by default).


Notice that *hAlign* and *vAlign* values are always overwritten by this function, use [`GetNonDefaultAlignment`](#wx.grid.GridCellAttr.GetNonDefaultAlignment "wx.grid.GridCellAttr.GetNonDefaultAlignment") if this is not desirable.



Return type
*tuple*



Returns
( *hAlign*, *vAlign* )






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.grid.GridCellAttr.GetBackgroundColour "Permalink to this definition")
Returns the background colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetEditor(self, grid, row, col) -> 'GridCellEditor':
        """ 

`GetEditor`(*self*, *grid*, *row*, *col*)[¶](#wx.grid.GridCellAttr.GetEditor "Permalink to this definition")
Returns the cell editor.


The caller is responsible for calling [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") on the returned pointer, use [`GetEditorPtr`](#wx.grid.GridCellAttr.GetEditorPtr "wx.grid.GridCellAttr.GetEditorPtr") to do it automatically.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor)






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetEditorPtr(self, grid, row, col) -> 'GridCellEditor':
        """ 

`GetEditorPtr`(*self*, *grid*, *row*, *col*)[¶](#wx.grid.GridCellAttr.GetEditorPtr "Permalink to this definition")
Returns the cell editor.


This method is identical to [`GetEditor`](#wx.grid.GridCellAttr.GetEditor "wx.grid.GridCellAttr.GetEditor") , but returns a smart pointer, which frees the caller from the need to call [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") manually.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **row** (*int*) –
* **col** (*int*) –



Return type
`wx.grid.GridCellEditorPtr`





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetFitMode(self) -> 'GridFitMode':
        """ 

`GetFitMode`(*self*)[¶](#wx.grid.GridCellAttr.GetFitMode "Permalink to this definition")
Returns the fitting mode for the cells using this attribute.


The returned  [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode) is always specified, i.e. [`wx.grid.GridFitMode.IsSpecified`](wx.grid.GridFitMode.html#wx.grid.GridFitMode.IsSpecified "wx.grid.GridFitMode.IsSpecified") always returns `True`. The default value, if [`SetFitMode`](#wx.grid.GridCellAttr.SetFitMode "wx.grid.GridCellAttr.SetFitMode") hadn’t been called before, is “overflow”.



Return type
 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.grid.GridCellAttr.GetFont "Permalink to this definition")
Returns the font.



Return type
[`Font`](#wx.grid.GridCellAttr.Font "wx.grid.GridCellAttr.Font")






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetKind(self) -> 'AttrKind':
        """ 

`GetKind`(*self*)[¶](#wx.grid.GridCellAttr.GetKind "Permalink to this definition")

Return type
 [wx.grid.GridCellAttr.AttrKind](wx.grid.GridCellAttr.AttrKind.enumeration.html#wx-grid-gridcellattr-attrkind)






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetNonDefaultAlignment(self) -> tuple:
        """ 

`GetNonDefaultAlignment`(*self*)[¶](#wx.grid.GridCellAttr.GetNonDefaultAlignment "Permalink to this definition")
Get the alignment defined by this attribute.


Unlike [`GetAlignment`](#wx.grid.GridCellAttr.GetAlignment "wx.grid.GridCellAttr.GetAlignment") this function only modifies *hAlign* and *vAlign* if this attribute does define a non-default alignment. This means that they must be initialized before calling this function and that their values will be preserved unchanged if they are different from `wx.ALIGN_INVALID`.


For example, the following fragment can be used to use the cell alignment if one is defined but right-align its contents by default (instead of left-aligning it by default) while still using the default vertical alignment:



```
hAlign = wx.ALIGN_RIGHT
vAlign = wx.ALIGN_INVALID

hAlign, vAlign = attr.GetNonDefaultAlignment()

```



Return type
*tuple*



Returns
( *hAlign*, *vAlign* )





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetOverflow(self) -> bool:
        """ 

`GetOverflow`(*self*)[¶](#wx.grid.GridCellAttr.GetOverflow "Permalink to this definition")
Returns `True` if the cells using this attribute overflow into the neighbouring cells.


Prefer using [`GetFitMode`](#wx.grid.GridCellAttr.GetFitMode "wx.grid.GridCellAttr.GetFitMode") in the new code.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetRenderer(self, grid, row, col) -> 'GridCellRenderer':
        """ 

`GetRenderer`(*self*, *grid*, *row*, *col*)[¶](#wx.grid.GridCellAttr.GetRenderer "Permalink to this definition")
Returns the cell renderer.


The caller is responsible for calling [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") on the returned pointer, use `GetRendererPtr` to do it automatically.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.grid.GridCellRenderer](wx.grid.GridCellRenderer.html#wx-grid-gridcellrenderer)






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetSize(self) -> tuple:
        """ 

`GetSize`(*self*)[¶](#wx.grid.GridCellAttr.GetSize "Permalink to this definition")

Return type
*tuple*



Returns
( *num\_rows*, *num\_cols* )






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def GetTextColour(self) -> 'Colour':
        """ 

`GetTextColour`(*self*)[¶](#wx.grid.GridCellAttr.GetTextColour "Permalink to this definition")
Returns the text colour.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasAlignment(self) -> bool:
        """ 

`HasAlignment`(*self*)[¶](#wx.grid.GridCellAttr.HasAlignment "Permalink to this definition")
Returns `True` if this attribute has a valid alignment set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasBackgroundColour(self) -> bool:
        """ 

`HasBackgroundColour`(*self*)[¶](#wx.grid.GridCellAttr.HasBackgroundColour "Permalink to this definition")
Returns `True` if this attribute has a valid background colour set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasEditor(self) -> bool:
        """ 

`HasEditor`(*self*)[¶](#wx.grid.GridCellAttr.HasEditor "Permalink to this definition")
Returns `True` if this attribute has a valid cell editor set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasFont(self) -> bool:
        """ 

`HasFont`(*self*)[¶](#wx.grid.GridCellAttr.HasFont "Permalink to this definition")
Returns `True` if this attribute has a valid font set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasOverflowMode(self) -> bool:
        """ 

`HasOverflowMode`(*self*)[¶](#wx.grid.GridCellAttr.HasOverflowMode "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasReadWriteMode(self) -> bool:
        """ 

`HasReadWriteMode`(*self*)[¶](#wx.grid.GridCellAttr.HasReadWriteMode "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasRenderer(self) -> bool:
        """ 

`HasRenderer`(*self*)[¶](#wx.grid.GridCellAttr.HasRenderer "Permalink to this definition")
Returns `True` if this attribute has a valid cell renderer set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasSize(self) -> bool:
        """ 

`HasSize`(*self*)[¶](#wx.grid.GridCellAttr.HasSize "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def HasTextColour(self) -> bool:
        """ 

`HasTextColour`(*self*)[¶](#wx.grid.GridCellAttr.HasTextColour "Permalink to this definition")
Returns `True` if this attribute has a valid text colour set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def IncRef(self) -> None:
        """ 

`IncRef`(*self*)[¶](#wx.grid.GridCellAttr.IncRef "Permalink to this definition")
This class is reference counted: it is created with ref count of 1, so calling [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") once will delete it.


Calling [`IncRef`](#wx.grid.GridCellAttr.IncRef "wx.grid.GridCellAttr.IncRef") allows locking it until the matching [`DecRef`](#wx.grid.GridCellAttr.DecRef "wx.grid.GridCellAttr.DecRef") is called.




            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def IsReadOnly(self) -> bool:
        """ 

`IsReadOnly`(*self*)[¶](#wx.grid.GridCellAttr.IsReadOnly "Permalink to this definition")
Returns `True` if this cell is set as read-only.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def MergeWith(self, mergefrom: 'grid.GridCellAttr') -> None:
        """ 

`MergeWith`(*self*, *mergefrom*)[¶](#wx.grid.GridCellAttr.MergeWith "Permalink to this definition")

Parameters
**mergefrom** ([*wx.grid.GridCellAttr*](#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetAlignment(self, hAlign, vAlign) -> None:
        """ 

`SetAlignment`(*self*, *hAlign*, *vAlign*)[¶](#wx.grid.GridCellAttr.SetAlignment "Permalink to this definition")
Sets the alignment.


*hAlign* can be one of `ALIGN_LEFT` , `ALIGN_CENTRE` or `ALIGN_RIGHT` and *vAlign* can be one of `ALIGN_TOP` , `ALIGN_CENTRE` or `ALIGN_BOTTOM` .



Parameters
* **hAlign** (*int*) –
* **vAlign** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetBackgroundColour(self, colBack: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colBack*)[¶](#wx.grid.GridCellAttr.SetBackgroundColour "Permalink to this definition")
Sets the background colour.



Parameters
**colBack** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetDefAttr(self, defAttr: 'grid.GridCellAttr') -> None:
        """ 

`SetDefAttr`(*self*, *defAttr*)[¶](#wx.grid.GridCellAttr.SetDefAttr "Permalink to this definition")

Parameters
**defAttr** ([*wx.grid.GridCellAttr*](#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) – 





Todo


Needs documentation.





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetEditor(self, editor: 'grid.GridCellEditor') -> None:
        """ 

`SetEditor`(*self*, *editor*)[¶](#wx.grid.GridCellAttr.SetEditor "Permalink to this definition")
Sets the editor to be used with the cells with this attribute.



Parameters
**editor** ([*wx.grid.GridCellEditor*](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor "wx.grid.GridCellEditor")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetFitMode(self, fitMode: 'grid.GridFitMode') -> None:
        """ 

`SetFitMode`(*self*, *fitMode*)[¶](#wx.grid.GridCellAttr.SetFitMode "Permalink to this definition")
Specifies the behaviour of the cell contents if it doesn’t fit into the available space.



Parameters
**fitMode** ([*wx.grid.GridFitMode*](wx.grid.GridFitMode.html#wx.grid.GridFitMode "wx.grid.GridFitMode")) – 





New in version 4.1/wxWidgets-3.1.4.




See also


 [wx.grid.GridFitMode](wx.grid.GridFitMode.html#wx-grid-gridfitmode)





            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.grid.GridCellAttr.SetFont "Permalink to this definition")
Sets the font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetKind(self, kind: AttrKind) -> None:
        """ 

`SetKind`(*self*, *kind*)[¶](#wx.grid.GridCellAttr.SetKind "Permalink to this definition")

Parameters
**kind** ([*AttrKind*](wx.grid.GridCellAttr.AttrKind.enumeration.html "AttrKind")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetOverflow(self, allow: bool=True) -> None:
        """ 

`SetOverflow`(*self*, *allow=True*)[¶](#wx.grid.GridCellAttr.SetOverflow "Permalink to this definition")
Specifies if cells using this attribute should overflow or clip their contents.


This is the same as calling [`SetFitMode`](#wx.grid.GridCellAttr.SetFitMode "wx.grid.GridCellAttr.SetFitMode") with either [`wx.grid.GridFitMode.Overflow`](wx.grid.GridFitMode.html#wx.grid.GridFitMode.Overflow "wx.grid.GridFitMode.Overflow") or [`wx.grid.GridFitMode.Clip`](wx.grid.GridFitMode.html#wx.grid.GridFitMode.Clip "wx.grid.GridFitMode.Clip") argument depending on whether *allow* is `True` or `False`.


Prefer using [`SetFitMode`](#wx.grid.GridCellAttr.SetFitMode "wx.grid.GridCellAttr.SetFitMode") directly instead in the new code.



Parameters
**allow** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetReadOnly(self, isReadOnly: bool=True) -> None:
        """ 

`SetReadOnly`(*self*, *isReadOnly=True*)[¶](#wx.grid.GridCellAttr.SetReadOnly "Permalink to this definition")
Sets the cell as read-only.



Parameters
**isReadOnly** (*bool*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetRenderer(self, renderer: 'grid.GridCellRenderer') -> None:
        """ 

`SetRenderer`(*self*, *renderer*)[¶](#wx.grid.GridCellAttr.SetRenderer "Permalink to this definition")
Sets the renderer to be used for cells with this attribute.


Takes ownership of the pointer.



Parameters
**renderer** ([*wx.grid.GridCellRenderer*](wx.grid.GridCellRenderer.html#wx.grid.GridCellRenderer "wx.grid.GridCellRenderer")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetSize(self, num_rows, num_cols) -> None:
        """ 

`SetSize`(*self*, *num\_rows*, *num\_cols*)[¶](#wx.grid.GridCellAttr.SetSize "Permalink to this definition")

Parameters
* **num\_rows** (*int*) –
* **num\_cols** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    def SetTextColour(self, colText: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colText*)[¶](#wx.grid.GridCellAttr.SetTextColour "Permalink to this definition")
Sets the text colour.



Parameters
**colText** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellAttr.html
        """

    BackgroundColour: 'Colour'  # `BackgroundColour`[¶](#wx.grid.GridCellAttr.BackgroundColour "Permalink to this definition")See [`GetBackgroundColour`](#wx.grid.GridCellAttr.GetBackgroundColour "wx.grid.GridCellAttr.GetBackgroundColour") and [`SetBackgroundColour`](#wx.grid.GridCellAttr.SetBackgroundColour "wx.grid.GridCellAttr.SetBackgroundColour")
    FitMode: 'GridFitMode'  # `FitMode`[¶](#wx.grid.GridCellAttr.FitMode "Permalink to this definition")See [`GetFitMode`](#wx.grid.GridCellAttr.GetFitMode "wx.grid.GridCellAttr.GetFitMode") and [`SetFitMode`](#wx.grid.GridCellAttr.SetFitMode "wx.grid.GridCellAttr.SetFitMode")
    Font: '_Font'  # `Font`[¶](#wx.grid.GridCellAttr.Font "Permalink to this definition")See [`GetFont`](#wx.grid.GridCellAttr.GetFont "wx.grid.GridCellAttr.GetFont") and [`SetFont`](#wx.grid.GridCellAttr.SetFont "wx.grid.GridCellAttr.SetFont")
    Kind: 'AttrKind'  # `Kind`[¶](#wx.grid.GridCellAttr.Kind "Permalink to this definition")See [`GetKind`](#wx.grid.GridCellAttr.GetKind "wx.grid.GridCellAttr.GetKind") and [`SetKind`](#wx.grid.GridCellAttr.SetKind "wx.grid.GridCellAttr.SetKind")
    Overflow: bool  # `Overflow`[¶](#wx.grid.GridCellAttr.Overflow "Permalink to this definition")See [`GetOverflow`](#wx.grid.GridCellAttr.GetOverflow "wx.grid.GridCellAttr.GetOverflow") and [`SetOverflow`](#wx.grid.GridCellAttr.SetOverflow "wx.grid.GridCellAttr.SetOverflow")
    TextColour: 'Colour'  # `TextColour`[¶](#wx.grid.GridCellAttr.TextColour "Permalink to this definition")See [`GetTextColour`](#wx.grid.GridCellAttr.GetTextColour "wx.grid.GridCellAttr.GetTextColour") and [`SetTextColour`](#wx.grid.GridCellAttr.SetTextColour "wx.grid.GridCellAttr.SetTextColour")



ALIGN_LEFT: int

ALIGN_INVALID: int

class GridCellEditor(SharedClientDataContainer,RefCounter):
    """ **Possible constructors**:



```
GridCellEditor()

```


This class is responsible for providing and manipulating the in-place
edit controls for the grid.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellEditor.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def ApplyEdit(self, row, col, grid) -> None:
        """ 

`ApplyEdit`(*self*, *row*, *col*, *grid*)[¶](#wx.grid.GridCellEditor.ApplyEdit "Permalink to this definition")
Effectively save the changes in the grid.


This function should save the value of the control in the grid. It is called only after [`EndEdit`](#wx.grid.GridCellEditor.EndEdit "wx.grid.GridCellEditor.EndEdit") returns `True`.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def BeginEdit(self, row, col, grid) -> None:
        """ 

`BeginEdit`(*self*, *row*, *col*, *grid*)[¶](#wx.grid.GridCellEditor.BeginEdit "Permalink to this definition")
Fetch the value from the table and prepare the edit control to begin editing.


This function should save the original value of the grid cell at the given *row* and *col* and show the control allowing the user to change it.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –





See also


[`EndEdit`](#wx.grid.GridCellEditor.EndEdit "wx.grid.GridCellEditor.EndEdit")





            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Clone(self) -> 'GridCellEditor':
        """ 

`Clone`(*self*)[¶](#wx.grid.GridCellEditor.Clone "Permalink to this definition")
Create a new object which is the copy of this one.



Return type
 [wx.grid.GridCellEditor](#wx-grid-gridcelleditor)






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Create(self, parent, id, evtHandler) -> None:
        """ 

`Create`(*self*, *parent*, *id*, *evtHandler*)[¶](#wx.grid.GridCellEditor.Create "Permalink to this definition")
Creates the actual edit control.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **evtHandler** ([*wx.EvtHandler*](wx.EvtHandler.html#wx.EvtHandler "wx.EvtHandler")) –






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Destroy(self) -> None:
        """ 

`Destroy`(*self*)[¶](#wx.grid.GridCellEditor.Destroy "Permalink to this definition")
Final cleanup.




            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def DoActivate(self, row, col, grid) -> None:
        """ 

`DoActivate`(*self*, *row*, *col*, *grid*)[¶](#wx.grid.GridCellEditor.DoActivate "Permalink to this definition")
Function which must be overridden for “activatable” editors.


If [`TryActivate`](#wx.grid.GridCellEditor.TryActivate "wx.grid.GridCellEditor.TryActivate") is overridden to return “change” action, this function will be called to actually apply this change. Note that it is not passed the value to apply, as it is assumed that the editor class stores this value as a member variable anyhow.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetControl(self) -> 'Control':
        """ 

`GetControl`(*self*)[¶](#wx.grid.GridCellEditor.GetControl "Permalink to this definition")
Get the  [wx.Control](wx.Control.html#wx-control) used by this editor.


This function is preserved for compatibility, but [`GetWindow`](#wx.grid.GridCellEditor.GetWindow "wx.grid.GridCellEditor.GetWindow") should be preferred in the new code as the associated window doesn’t need to be of a Control-derived class.


Note that if [`SetWindow`](#wx.grid.GridCellEditor.SetWindow "wx.grid.GridCellEditor.SetWindow") had been called with an object not deriving from  [wx.Control](wx.Control.html#wx-control), this method will return `None`.



Return type
[`Control`](#wx.grid.GridCellEditor.Control "wx.grid.GridCellEditor.Control")






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetValue(self) -> str:
        """ 

`GetValue`(*self*)[¶](#wx.grid.GridCellEditor.GetValue "Permalink to this definition")
Returns the value currently in the editor control.



Return type
`string`






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def GetWindow(self) -> 'Window':
        """ 

`GetWindow`(*self*)[¶](#wx.grid.GridCellEditor.GetWindow "Permalink to this definition")
Get the edit window used by this editor.



Return type
[`Window`](#wx.grid.GridCellEditor.Window "wx.grid.GridCellEditor.Window")





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def HandleReturn(self, event: 'KeyEvent') -> None:
        """ 

`HandleReturn`(*self*, *event*)[¶](#wx.grid.GridCellEditor.HandleReturn "Permalink to this definition")
Some types of controls on some platforms may need some help with the Return key.



Parameters
**event** ([*wx.KeyEvent*](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def IsAcceptedKey(self, event: 'KeyEvent') -> bool:
        """ 

`IsAcceptedKey`(*self*, *event*)[¶](#wx.grid.GridCellEditor.IsAcceptedKey "Permalink to this definition")
Return `True` to allow the given key to start editing: the base class version only checks that the event has no modifiers.


If the key is `F2` (special), editing will always start and this method will not be called at all (but [`StartingKey`](#wx.grid.GridCellEditor.StartingKey "wx.grid.GridCellEditor.StartingKey") will)



Parameters
**event** ([*wx.KeyEvent*](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def IsCreated(self) -> bool:
        """ 

`IsCreated`(*self*)[¶](#wx.grid.GridCellEditor.IsCreated "Permalink to this definition")
Returns `True` if the edit control has been created.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def PaintBackground(self, dc, rectCell, attr) -> None:
        """ 

`PaintBackground`(*self*, *dc*, *rectCell*, *attr*)[¶](#wx.grid.GridCellEditor.PaintBackground "Permalink to this definition")
Draws the part of the cell not occupied by the control: the base class version just fills it with background colour from the attribute.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rectCell** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.grid.GridCellEditor.Reset "Permalink to this definition")
Reset the value in the control back to its starting value.




            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetControl(self, control: 'Control') -> None:
        """ 

`SetControl`(*self*, *control*)[¶](#wx.grid.GridCellEditor.SetControl "Permalink to this definition")
Set the  [wx.Control](wx.Control.html#wx-control) that will be used by this cell editor for editing the value.


This function is preserved for compatibility, but [`SetWindow`](#wx.grid.GridCellEditor.SetWindow "wx.grid.GridCellEditor.SetWindow") should be preferred in the new code, see [`GetControl`](#wx.grid.GridCellEditor.GetControl "wx.grid.GridCellEditor.GetControl") .



Parameters
**control** ([*wx.Control*](wx.Control.html#wx.Control "wx.Control")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetSize(self, rect: 'Rect') -> None:
        """ 

`SetSize`(*self*, *rect*)[¶](#wx.grid.GridCellEditor.SetSize "Permalink to this definition")
Size and position the edit control.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def SetWindow(self, window: 'Window') -> None:
        """ 

`SetWindow`(*self*, *window*)[¶](#wx.grid.GridCellEditor.SetWindow "Permalink to this definition")
Set the  [wx.Window](wx.Window.html#wx-window) that will be used by this cell editor for editing the value.



Parameters
**window** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def Show(self, show, attr=None) -> None:
        """ 

`Show`(*self*, *show*, *attr=None*)[¶](#wx.grid.GridCellEditor.Show "Permalink to this definition")
Show or hide the edit control, use the specified attributes to set colours/fonts for it.



Parameters
* **show** (*bool*) –
* **attr** ([*wx.grid.GridCellAttr*](wx.grid.GridCellAttr.html#wx.grid.GridCellAttr "wx.grid.GridCellAttr")) –






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def StartingClick(self) -> None:
        """ 

`StartingClick`(*self*)[¶](#wx.grid.GridCellEditor.StartingClick "Permalink to this definition")
If the editor is enabled by clicking on the cell, this method will be called.




            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def StartingKey(self, event: 'KeyEvent') -> None:
        """ 

`StartingKey`(*self*, *event*)[¶](#wx.grid.GridCellEditor.StartingKey "Permalink to this definition")
If the editor is enabled by pressing keys on the grid, this will be called to let the editor do something about that first key if desired.



Parameters
**event** ([*wx.KeyEvent*](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    def TryActivate(self, row, col, grid, actSource) -> 'GridActivationResult':
        """ 

`TryActivate`(*self*, *row*, *col*, *grid*, *actSource*)[¶](#wx.grid.GridCellEditor.TryActivate "Permalink to this definition")
Function allowing to create an “activatable” editor.


As explained in this class description, activatable editors don’t show any edit control but change the cell value directly, when it is activated (by any way described by  [wx.grid.GridActivationSource](wx.grid.GridActivationSource.html#wx-grid-gridactivationsource)).


To create such editor, this method must be overridden to return [`wx.grid.GridActivationResult.DoChange`](wx.grid.GridActivationResult.html#wx.grid.GridActivationResult.DoChange "wx.grid.GridActivationResult.DoChange") passing it the new value of the cell. If the change is not vetoed by wxEVT\_GRID\_CELL\_CHANGING handler, [`DoActivate`](#wx.grid.GridCellEditor.DoActivate "wx.grid.GridCellEditor.DoActivate") will be called to actually change the value, so it must be overridden as well if [`TryActivate`](#wx.grid.GridCellEditor.TryActivate "wx.grid.GridCellEditor.TryActivate") is overridden.


By default, [`wx.grid.GridActivationResult.DoEdit`](wx.grid.GridActivationResult.html#wx.grid.GridActivationResult.DoEdit "wx.grid.GridActivationResult.DoEdit") is returned, meaning that this is a normal editor, using an edit control for changing the cell value.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **actSource** ([*wx.grid.GridActivationSource*](wx.grid.GridActivationSource.html#wx.grid.GridActivationSource "wx.grid.GridActivationSource")) –



Return type
 [wx.grid.GridActivationResult](wx.grid.GridActivationResult.html#wx-grid-gridactivationresult)





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.grid.GridCellEditor.html
        """

    Control: '_Control'  # `Control`[¶](#wx.grid.GridCellEditor.Control "Permalink to this definition")See [`GetControl`](#wx.grid.GridCellEditor.GetControl "wx.grid.GridCellEditor.GetControl") and [`SetControl`](#wx.grid.GridCellEditor.SetControl "wx.grid.GridCellEditor.SetControl")
    Value: str  # `Value`[¶](#wx.grid.GridCellEditor.Value "Permalink to this definition")See [`GetValue`](#wx.grid.GridCellEditor.GetValue "wx.grid.GridCellEditor.GetValue")
    Window: '_Window'  # `Window`[¶](#wx.grid.GridCellEditor.Window "Permalink to this definition")See [`GetWindow`](#wx.grid.GridCellEditor.GetWindow "wx.grid.GridCellEditor.GetWindow") and [`SetWindow`](#wx.grid.GridCellEditor.SetWindow "wx.grid.GridCellEditor.SetWindow")



class GridCellBoolEditor(GridCellEditor):
    """ **Possible constructors**:



```
GridCellBoolEditor()

```


Grid cell editor for boolean data.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellBoolEditor.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellBoolEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    @staticmethod
    def IsTrueValue(value: str) -> bool:
        """ 

*static* `IsTrueValue`(*value*)[¶](#wx.grid.GridCellBoolEditor.IsTrueValue "Permalink to this definition")
Returns `True` if the given *value* is equal to the string representation of the truth value we currently use (see [`UseStringValues`](#wx.grid.GridCellBoolEditor.UseStringValues "wx.grid.GridCellBoolEditor.UseStringValues") ).



Parameters
**value** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """

    @staticmethod
    def UseStringValues(valueTrue="1", valueFalse="") -> None:
        """ 

*static* `UseStringValues`(*valueTrue="1"*, *valueFalse=""*)[¶](#wx.grid.GridCellBoolEditor.UseStringValues "Permalink to this definition")
This method allows you to customize the values returned by [`GetValue`](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor.GetValue "wx.grid.GridCellEditor.GetValue") for the cell using this editor.


By default, the default values of the arguments are used, i.e. `"1"` is returned if the cell is checked and an empty string otherwise.



Parameters
* **valueTrue** (*string*) –
* **valueFalse** (*string*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellBoolEditor.html
        """



class GridCellChoiceEditor(GridCellEditor):
    """ **Possible constructors**:



```
GridCellChoiceEditor(choices, allowOthers=False)

```


Grid cell editor for string data providing the user a choice from a
list of strings.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
    """
    def __init__(self, choices, allowOthers=False) -> None:
        """ 

`__init__`(*self*, *choices*, *allowOthers=False*)[¶](#wx.grid.GridCellChoiceEditor.__init__ "Permalink to this definition")
Choice cell renderer constructor.



Parameters
* **choices** (*list of strings*) – An array of strings from which the user can choose.
* **allowOthers** (*bool*) – If allowOthers is `True`, the user can type a string not in choices array.






            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellChoiceEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellChoiceEditor.SetParameters "Permalink to this definition")
Parameters string format is “item1[,item2[…,itemN]]”.


This method can be called before the editor is used for the first time, or later, in which case it replaces the previously specified strings with the new ones.



Parameters
**params** (*string*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellChoiceEditor.html
        """



class GridCellFloatEditor(GridCellTextEditor):
    """ **Possible constructors**:



```
GridCellFloatEditor(width=-1, precision=-1,
                    format=GRID_FLOAT_FORMAT_DEFAULT)

```


The editor for floating point numbers data.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
    """
    def __init__(self, width=-1, precision=-1, format=GRID_FLOAT_FORMAT_DEFAULT) -> None:
        """ 

`__init__`(*self*, *width=-1*, *precision=-1*, *format=GRID\_FLOAT\_FORMAT\_DEFAULT*)[¶](#wx.grid.GridCellFloatEditor.__init__ "Permalink to this definition")
Float cell editor constructor.



Parameters
* **width** (*int*) – Minimum number of characters to be shown.
* **precision** (*int*) – Number of digits after the decimal dot.
* **format** (*int*) – The format to use for displaying the number, a combination of  [wx.grid.GridCellFloatFormat](wx.grid.GridCellFloatFormat.enumeration.html#wx-grid-gridcellfloatformat) enum elements. This parameter is only available since wxWidgets 2.9.3.






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellFloatEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellFloatEditor.SetParameters "Permalink to this definition")
The parameters string format is “width[,precision[,format]]” where `format` should be chosen between f|e|g|E|G (f is used by default)



Parameters
**params** (*string*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellFloatEditor.html
        """



class GridCellNumberEditor(GridCellTextEditor):
    """ **Possible constructors**:



```
GridCellNumberEditor(min=-1, max=-1)

```


Grid cell editor for numeric integer data.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
    """
    def __init__(self, min=-1, max=-1) -> None:
        """ 

`__init__`(*self*, *min=-1*, *max=-1*)[¶](#wx.grid.GridCellNumberEditor.__init__ "Permalink to this definition")
Allows you to specify the range for acceptable data.


Values equal to -1 for both *min* and *max* indicate that no range checking should be done.



Parameters
* **min** (*int*) –
* **max** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellNumberEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellNumberEditor.SetParameters "Permalink to this definition")
Parameters string format is “min,max”.



Parameters
**params** (*string*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellNumberEditor.html
        """



class GridCellTextEditor(GridCellEditor):
    """ **Possible constructors**:



```
GridCellTextEditor(maxChars=0)

```


Grid cell editor for string/text data.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
    """
    def __init__(self, maxChars: int=0) -> None:
        """ 

`__init__`(*self*, *maxChars=0*)[¶](#wx.grid.GridCellTextEditor.__init__ "Permalink to this definition")
Text cell editor constructor.



Parameters
**maxChars** (*int*) – Maximum width of text (this parameter is supported starting since wxWidgets 2.9.5).






            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellTextEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellTextEditor.SetParameters "Permalink to this definition")
The parameters string format is “n” where n is a number representing the maximum width.



Parameters
**params** (*string*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """

    def SetValidator(self, validator: 'Validator') -> None:
        """ 

`SetValidator`(*self*, *validator*)[¶](#wx.grid.GridCellTextEditor.SetValidator "Permalink to this definition")
Set validator to validate user input.



Parameters
**validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.grid.GridCellTextEditor.html
        """



class GridCellDateEditor(GridCellEditor):
    """ **Possible constructors**:



```
GridCellDateEditor(format="")

```


Grid cell editor for dates.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
    """
    def __init__(self, format: str="") -> None:
        """ 

`__init__`(*self*, *format=""*)[¶](#wx.grid.GridCellDateEditor.__init__ "Permalink to this definition")
Date editor constructor.



Parameters
**format** (*string*) – Optional format for the date displayed in the associated cell. By default, the locale-specific date format (“%x”) is assumed. You would typically want to specify the same format as the one used with the cell renderer, if a non-default one is used. Note that this parameter is only available since wxWidgets 3.1.5.






            Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellDateEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellDateEditor.html
        """



class GridEvent(NotifyEvent):
    """ **Possible constructors**:



```
GridEvent()

GridEvent(id, type, obj, row=-1, col=-1, x=-1, y=-1, sel=True,
          kbd=KeyboardState())

```


This event class contains information about various grid events.


  


        Source: https://docs.wxpython.org/wx.grid.GridEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, id, type, obj, row=-1, col=-1, x=-1, y=-1, sel=True, kbd=KeyboardState())*


Constructor for initializing all event attributes.



Parameters
* **id** (*int*) –
* **type** (*wx.EventType*) –
* **obj** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **row** (*int*) –
* **col** (*int*) –
* **x** (*int*) –
* **y** (*int*) –
* **sel** (*bool*) –
* **kbd** ([*wx.KeyboardState*](wx.KeyboardState.html#wx.KeyboardState "wx.KeyboardState")) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def AltDown(self) -> bool:
        """ 

`AltDown`(*self*)[¶](#wx.grid.GridEvent.AltDown "Permalink to this definition")
Returns `True` if the Alt key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def ControlDown(self) -> bool:
        """ 

`ControlDown`(*self*)[¶](#wx.grid.GridEvent.ControlDown "Permalink to this definition")
Returns `True` if the Control key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetCol(self) -> int:
        """ 

`GetCol`(*self*)[¶](#wx.grid.GridEvent.GetCol "Permalink to this definition")
Column at which the event occurred.


Notice that for a `wxEVT_GRID_SELECT_CELL` event this column is the column of the newly selected cell while the previously selected cell can be retrieved using [`wx.grid.Grid.GetGridCursorCol`](wx.grid.Grid.html#wx.grid.Grid.GetGridCursorCol "wx.grid.Grid.GetGridCursorCol") .



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetPosition(self) -> 'Point':
        """ 

`GetPosition`(*self*)[¶](#wx.grid.GridEvent.GetPosition "Permalink to this definition")
Position in pixels at which the event occurred.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def GetRow(self) -> int:
        """ 

`GetRow`(*self*)[¶](#wx.grid.GridEvent.GetRow "Permalink to this definition")
Row at which the event occurred.


Notice that for a `wxEVT_GRID_SELECT_CELL` event this row is the row of the newly selected cell while the previously selected cell can be retrieved using [`wx.grid.Grid.GetGridCursorRow`](wx.grid.Grid.html#wx.grid.Grid.GetGridCursorRow "wx.grid.Grid.GetGridCursorRow") .



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def MetaDown(self) -> bool:
        """ 

`MetaDown`(*self*)[¶](#wx.grid.GridEvent.MetaDown "Permalink to this definition")
Returns `True` if the Meta key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def Selecting(self) -> bool:
        """ 

`Selecting`(*self*)[¶](#wx.grid.GridEvent.Selecting "Permalink to this definition")
Returns `True` if the user is selecting grid cells, or `False` if deselecting.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    def ShiftDown(self) -> bool:
        """ 

`ShiftDown`(*self*)[¶](#wx.grid.GridEvent.ShiftDown "Permalink to this definition")
Returns `True` if the Shift key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridEvent.html
        """

    Col: int  # `Col`[¶](#wx.grid.GridEvent.Col "Permalink to this definition")See [`GetCol`](#wx.grid.GridEvent.GetCol "wx.grid.GridEvent.GetCol")
    Position: 'Point'  # `Position`[¶](#wx.grid.GridEvent.Position "Permalink to this definition")See [`GetPosition`](#wx.grid.GridEvent.GetPosition "wx.grid.GridEvent.GetPosition")
    Row: int  # `Row`[¶](#wx.grid.GridEvent.Row "Permalink to this definition")See [`GetRow`](#wx.grid.GridEvent.GetRow "wx.grid.GridEvent.GetRow")



EVT_GRID_CELL_CHANGING: int  # The user is about to change the data in a cell. The new cell value as string is available from GetString  event object method. This event can be vetoed if the change is not allowed. Processes a  wxEVT_GRID_CELL_CHANGING   event type.

EVT_GRID_CELL_CHANGED: int  # The user changed the data in a cell. The old cell value as string is available from GetString  event object method. Notice that vetoing this event still works for backwards compatibility reasons but any new code should only veto EVT_GRID_CELL_CHANGING event and not this one. Processes a  wxEVT_GRID_CELL_CHANGED   event type.

EVT_GRID_CELL_LEFT_CLICK: int  # The user clicked a cell with the left mouse button. Processes a  wxEVT_GRID_CELL_LEFT_CLICK   event type.

EVT_GRID_CELL_LEFT_DCLICK: int  # The user double-clicked a cell with the left mouse button. Processes a  wxEVT_GRID_CELL_LEFT_DCLICK   event type.

EVT_GRID_CELL_RIGHT_CLICK: int  # The user clicked a cell with the right mouse button. Processes a  wxEVT_GRID_CELL_RIGHT_CLICK   event type.

EVT_GRID_CELL_RIGHT_DCLICK: int  # The user double-clicked a cell with the right mouse button. Processes a  wxEVT_GRID_CELL_RIGHT_DCLICK   event type.

EVT_GRID_EDITOR_HIDDEN: int  # The editor for a cell was hidden. Processes a  wxEVT_GRID_EDITOR_HIDDEN   event type.

EVT_GRID_EDITOR_SHOWN: int  # The editor for a cell was shown. Processes a  wxEVT_GRID_EDITOR_SHOWN   event type.

EVT_GRID_LABEL_LEFT_CLICK: int  # The user clicked a label with the left mouse button. Processes a  wxEVT_GRID_LABEL_LEFT_CLICK   event type.

EVT_GRID_LABEL_LEFT_DCLICK: int  # The user double-clicked a label with the left mouse button. Processes a  wxEVT_GRID_LABEL_LEFT_DCLICK   event type.

EVT_GRID_LABEL_RIGHT_CLICK: int  # The user clicked a label with the right mouse button. Processes a  wxEVT_GRID_LABEL_RIGHT_CLICK   event type.

EVT_GRID_LABEL_RIGHT_DCLICK: int  # The user double-clicked a label with the right mouse button. Processes a  wxEVT_GRID_LABEL_RIGHT_DCLICK   event type.

EVT_GRID_SELECT_CELL: int  # The given cell is about to be made current, either by user or by the program via a call to wx.grid.Grid.SetGridCursor   or wx.grid.Grid.GoToCell . The event can be vetoed to prevent this from happening and wx.grid.Grid.GetGridCursorCoords   still returns the previous current cell coordinates during the event handler execution, while the new ones are available via the event object GetRow  and GetCol  functions. Processes a  wxEVT_GRID_SELECT_CELL   event type.

EVT_GRID_ROW_MOVE: int  # The user tries to change the order of the rows in the grid by dragging the row specified by GetRow. This event can be vetoed to either prevent the user from reordering the row change completely (but notice that if you don’t want to allow it at all, you simply shouldn’t call wx.grid.Grid.EnableDragRowMove   in the first place), vetoed but handled in some way in the handler, e.g. by really moving the row to the new position at the associated table level, or allowed to proceed in which case wx.grid.Grid.SetRowPos   is used to reorder the rows display order without affecting the use of the row indices otherwise. This event macro corresponds to  wxEVT_GRID_ROW_MOVE   event type. It is only available since wxWidgets 3.1.7.

EVT_GRID_COL_MOVE: int  # The user tries to change the order of the columns in the grid by dragging the column specified by GetCol. This event can be vetoed to either prevent the user from reordering the column change completely (but notice that if you don’t want to allow it at all, you simply shouldn’t call wx.grid.Grid.EnableDragColMove   in the first place), vetoed but handled in some way in the handler, e.g. by really moving the column to the new position at the associated table level, or allowed to proceed in which case wx.grid.Grid.SetColPos   is used to reorder the columns display order without affecting the use of the column indices otherwise. This event macro corresponds to  wxEVT_GRID_COL_MOVE   event type.

EVT_GRID_COL_SORT: int  # This event is generated when a column is clicked by the user and its name is explained by the fact that the custom reaction to a click on a column is to sort the grid contents by this column. However the grid itself has no special support for sorting and it’s up to the handler of this event to update the associated table. But if the event is handled (and not vetoed) the grid supposes that the table was indeed resorted and updates the column to indicate the new sort order and refreshes itself. This event macro corresponds to  wxEVT_GRID_COL_SORT   event type.

EVT_GRID_TABBING: int  # This event is generated when the user presses TAB or Shift-TAB in the grid. It can be used to customize the simple default TAB handling logic, e.g. to go to the next non-empty cell instead of just the next cell. See also wx.grid.Grid.SetTabBehaviour . This event is new since wxWidgets 2.9.5. ^^

class GridSizeEvent(NotifyEvent):
    """ **Possible constructors**:



```
GridSizeEvent()

GridSizeEvent(id, type, obj, rowOrCol=-1, x=-1, y=-1,
              kbd=KeyboardState())

```


This event class contains information about a row/column resize event.


  


        Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridSizeEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, id, type, obj, rowOrCol=-1, x=-1, y=-1, kbd=KeyboardState())*


Constructor for initializing all event attributes.



Parameters
* **id** (*int*) –
* **type** (*wx.EventType*) –
* **obj** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **rowOrCol** (*int*) –
* **x** (*int*) –
* **y** (*int*) –
* **kbd** ([*wx.KeyboardState*](wx.KeyboardState.html#wx.KeyboardState "wx.KeyboardState")) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def AltDown(self) -> bool:
        """ 

`AltDown`(*self*)[¶](#wx.grid.GridSizeEvent.AltDown "Permalink to this definition")
Returns `True` if the Alt key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def ControlDown(self) -> bool:
        """ 

`ControlDown`(*self*)[¶](#wx.grid.GridSizeEvent.ControlDown "Permalink to this definition")
Returns `True` if the Control key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def GetPosition(self) -> 'Point':
        """ 

`GetPosition`(*self*)[¶](#wx.grid.GridSizeEvent.GetPosition "Permalink to this definition")
Position in pixels at which the event occurred.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def GetRowOrCol(self) -> int:
        """ 

`GetRowOrCol`(*self*)[¶](#wx.grid.GridSizeEvent.GetRowOrCol "Permalink to this definition")
Row or column at that was resized.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def MetaDown(self) -> bool:
        """ 

`MetaDown`(*self*)[¶](#wx.grid.GridSizeEvent.MetaDown "Permalink to this definition")
Returns `True` if the Meta key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    def ShiftDown(self) -> bool:
        """ 

`ShiftDown`(*self*)[¶](#wx.grid.GridSizeEvent.ShiftDown "Permalink to this definition")
Returns `True` if the Shift key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridSizeEvent.html
        """

    Position: 'Point'  # `Position`[¶](#wx.grid.GridSizeEvent.Position "Permalink to this definition")See [`GetPosition`](#wx.grid.GridSizeEvent.GetPosition "wx.grid.GridSizeEvent.GetPosition")
    RowOrCol: int  # `RowOrCol`[¶](#wx.grid.GridSizeEvent.RowOrCol "Permalink to this definition")See [`GetRowOrCol`](#wx.grid.GridSizeEvent.GetRowOrCol "wx.grid.GridSizeEvent.GetRowOrCol")



EVT_GRID_CMD_COL_SIZE: int  # The user resized a column, corresponds to  wxEVT_GRID_COL_SIZE   event type.

EVT_GRID_CMD_ROW_SIZE: int  # The user resized a row, corresponds to  wxEVT_GRID_ROW_SIZE   event type.

EVT_GRID_ROW_AUTO_SIZE: int  # This event is sent when a row must be resized to its best size, e.g. when the user double clicks the row divider. The default implementation simply resizes the row to fit the row label (but not its contents as this could be too slow for big grids). This macro corresponds to  wxEVT_GRID_ROW_AUTO_SIZE   event type and is new since wxWidgets 3.1.7.

EVT_GRID_COL_SIZE: int  # Same as EVT_GRID_CMD_COL_SIZE() but uses  ID_ANY   id.

EVT_GRID_COL_AUTO_SIZE: int  # This event is sent when a column must be resized to its best size, e.g. when the user double clicks the column divider. The default implementation simply resizes the column to fit the column label (but not its contents as this could be too slow for big grids). This macro corresponds to  wxEVT_GRID_COL_AUTO_SIZE   event type and is new since wxWidgets 2.9.5.

EVT_GRID_ROW_SIZE: int  # Same as EVT_GRID_CMD_ROW_SIZE() but uses  ID_ANY   id. ^^

class GridRangeSelectEvent(NotifyEvent):
    """ **Possible constructors**:



```
GridRangeSelectEvent()

GridRangeSelectEvent(id, type, obj, topLeft, bottomRight, sel=True,
                     kbd=KeyboardState())

```


Events of this class notify about a range of cells being selected.


  


        Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridRangeSelectEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, id, type, obj, topLeft, bottomRight, sel=True, kbd=KeyboardState())*


Constructor for initializing all event attributes.



Parameters
* **id** (*int*) –
* **type** (*wx.EventType*) –
* **obj** ([*wx.Object*](wx.Object.html#wx.Object "wx.Object")) –
* **topLeft** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **bottomRight** ([*wx.grid.GridCellCoords*](wx.grid.GridCellCoords.html#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) –
* **sel** (*bool*) –
* **kbd** ([*wx.KeyboardState*](wx.KeyboardState.html#wx.KeyboardState "wx.KeyboardState")) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def AltDown(self) -> bool:
        """ 

`AltDown`(*self*)[¶](#wx.grid.GridRangeSelectEvent.AltDown "Permalink to this definition")
Returns `True` if the Alt key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def ControlDown(self) -> bool:
        """ 

`ControlDown`(*self*)[¶](#wx.grid.GridRangeSelectEvent.ControlDown "Permalink to this definition")
Returns `True` if the Control key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetBottomRightCoords(self) -> 'GridCellCoords':
        """ 

`GetBottomRightCoords`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetBottomRightCoords "Permalink to this definition")
Top left corner of the rectangular area that was (de)selected.



Return type
 [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords)






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetBottomRow(self) -> int:
        """ 

`GetBottomRow`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetBottomRow "Permalink to this definition")
Bottom row of the rectangular area that was (de)selected.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetLeftCol(self) -> int:
        """ 

`GetLeftCol`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetLeftCol "Permalink to this definition")
Left column of the rectangular area that was (de)selected.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetRightCol(self) -> int:
        """ 

`GetRightCol`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetRightCol "Permalink to this definition")
Right column of the rectangular area that was (de)selected.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetTopLeftCoords(self) -> 'GridCellCoords':
        """ 

`GetTopLeftCoords`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetTopLeftCoords "Permalink to this definition")
Top left corner of the rectangular area that was (de)selected.



Return type
 [wx.grid.GridCellCoords](wx.grid.GridCellCoords.html#wx-grid-gridcellcoords)






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def GetTopRow(self) -> int:
        """ 

`GetTopRow`(*self*)[¶](#wx.grid.GridRangeSelectEvent.GetTopRow "Permalink to this definition")
Top row of the rectangular area that was (de)selected.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def MetaDown(self) -> bool:
        """ 

`MetaDown`(*self*)[¶](#wx.grid.GridRangeSelectEvent.MetaDown "Permalink to this definition")
Returns `True` if the Meta key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def Selecting(self) -> bool:
        """ 

`Selecting`(*self*)[¶](#wx.grid.GridRangeSelectEvent.Selecting "Permalink to this definition")
Returns `True` if the area was selected, `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    def ShiftDown(self) -> bool:
        """ 

`ShiftDown`(*self*)[¶](#wx.grid.GridRangeSelectEvent.ShiftDown "Permalink to this definition")
Returns `True` if the Shift key was down at the time of the event.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridRangeSelectEvent.html
        """

    BottomRightCoords: 'GridCellCoords'  # `BottomRightCoords`[¶](#wx.grid.GridRangeSelectEvent.BottomRightCoords "Permalink to this definition")See [`GetBottomRightCoords`](#wx.grid.GridRangeSelectEvent.GetBottomRightCoords "wx.grid.GridRangeSelectEvent.GetBottomRightCoords")
    BottomRow: int  # `BottomRow`[¶](#wx.grid.GridRangeSelectEvent.BottomRow "Permalink to this definition")See [`GetBottomRow`](#wx.grid.GridRangeSelectEvent.GetBottomRow "wx.grid.GridRangeSelectEvent.GetBottomRow")
    LeftCol: int  # `LeftCol`[¶](#wx.grid.GridRangeSelectEvent.LeftCol "Permalink to this definition")See [`GetLeftCol`](#wx.grid.GridRangeSelectEvent.GetLeftCol "wx.grid.GridRangeSelectEvent.GetLeftCol")
    RightCol: int  # `RightCol`[¶](#wx.grid.GridRangeSelectEvent.RightCol "Permalink to this definition")See [`GetRightCol`](#wx.grid.GridRangeSelectEvent.GetRightCol "wx.grid.GridRangeSelectEvent.GetRightCol")
    TopLeftCoords: 'GridCellCoords'  # `TopLeftCoords`[¶](#wx.grid.GridRangeSelectEvent.TopLeftCoords "Permalink to this definition")See [`GetTopLeftCoords`](#wx.grid.GridRangeSelectEvent.GetTopLeftCoords "wx.grid.GridRangeSelectEvent.GetTopLeftCoords")
    TopRow: int  # `TopRow`[¶](#wx.grid.GridRangeSelectEvent.TopRow "Permalink to this definition")See [`GetTopRow`](#wx.grid.GridRangeSelectEvent.GetTopRow "wx.grid.GridRangeSelectEvent.GetTopRow")



EVT_GRID_RANGE_SELECTING: int  # The user is selecting a group of contiguous cells. Processes a  wxEVT_GRID_RANGE_SELECTING   event type. This event is available in wxWidgets 3.1.5 and later only.

EVT_GRID_CMD_RANGE_SELECTING: int  # The user is selecting a group of contiguous cells; variant taking a window identifier. Processes a  wxEVT_GRID_RANGE_SELECTING   event type. This event is available in wxWidgets 3.1.5 and later only.

EVT_GRID_RANGE_SELECTED: int  # The user selected a group of contiguous cells. Processes a  wxEVT_GRID_RANGE_SELECTED   event type. This event is available in wxWidgets 3.1.5 and later only and was called   wxEVT_GRID_RANGE_SELECT   in the previous versions.

EVT_GRID_CMD_RANGE_SELECTED: int  # The user selected a group of contiguous cells; variant taking a window identifier. Processes a  wxEVT_GRID_RANGE_SELECTED   event type. This event is available in wxWidgets 3.1.5 and later only and was called   wxEVT_GRID_CMD_RANGE_SELECT   in the previous versions. ^^

class GridUpdateLocker:
    """ **Possible constructors**:



```
GridUpdateLocker(grid=None)

```


This small class can be used to prevent Grid from redrawing during
its lifetime by calling *Grid.BeginBatch()* in its constructor and
*Grid.EndBatch()* in its destructor.


  


        Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
    """
    def __init__(self, grid: Optional['grid.Grid']=None) -> None:
        """ 

`__init__`(*self*, *grid=None*)[¶](#wx.grid.GridUpdateLocker.__init__ "Permalink to this definition")
Creates an object preventing the updates of the specified *grid*.


The parameter could be `None` in which case nothing is done. If *grid* is not `None` then the grid must exist for longer than this  [wx.grid.GridUpdateLocker](#wx-grid-gridupdatelocker) object itself.


The default constructor could be followed by a call to [`Create`](#wx.grid.GridUpdateLocker.Create "wx.grid.GridUpdateLocker.Create") to set the grid object later.



Parameters
**grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) – 






            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def Create(self, grid: 'grid.Grid') -> None:
        """ 

`Create`(*self*, *grid*)[¶](#wx.grid.GridUpdateLocker.Create "Permalink to this definition")
This method can be called if the object had been constructed using the default constructor.


It must not be called more than once.



Parameters
**grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) – 






            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def __enter__(self) -> None:
        """ 

`__enter__`(*self*)[¶](#wx.grid.GridUpdateLocker.__enter__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ 

`__exit__`(*self*, *exc\_type*, *exc\_val*, *exc\_tb*)[¶](#wx.grid.GridUpdateLocker.__exit__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridUpdateLocker.html
        """



class GridCellCoords:
    """ **Possible constructors**:



```
GridCellCoords()

GridCellCoords(row, col)

```


Represents coordinates of a grid cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridCellCoords.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor initializes the object to invalid state.


Initially the row and column are both invalid (-1) and so `operator!` for an uninitialized  [wx.grid.GridCellCoords](#wx-grid-gridcellcoords) returns `False`.




---

  



**\_\_init\_\_** *(self, row, col)*


Constructor taking a row and a column.



Parameters
* **row** (*int*) –
* **col** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def Get(self) -> tuple:
        """ 

`Get`(*self*)[¶](#wx.grid.GridCellCoords.Get "Permalink to this definition")
Return the row and col properties as a tuple.



Return type
*tuple*



Returns
( *row*, *col* )






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetCol(self) -> int:
        """ 

`GetCol`(*self*)[¶](#wx.grid.GridCellCoords.GetCol "Permalink to this definition")
Return the column of the coordinate.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetIM(self) -> None:
        """ 

`GetIM`(*self*)[¶](#wx.grid.GridCellCoords.GetIM "Permalink to this definition")
Returns an immutable representation of the `wx.GridCellCoords` object, based on `namedtuple`.


This new object is hashable and can be used as a dictionary key,
be added to sets, etc. It can be converted back into a real `wx.GridCellCoords`
with a simple statement like this: `obj = wx.GridCellCoords(imObj)`.




            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def GetRow(self) -> int:
        """ 

`GetRow`(*self*)[¶](#wx.grid.GridCellCoords.GetRow "Permalink to this definition")
Return the row of the coordinate.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def Set(self, row, col) -> None:
        """ 

`Set`(*self*, *row*, *col*)[¶](#wx.grid.GridCellCoords.Set "Permalink to this definition")
Set the row and column of the coordinate.



Parameters
* **row** (*int*) –
* **col** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def SetCol(self, n: int) -> None:
        """ 

`SetCol`(*self*, *n*)[¶](#wx.grid.GridCellCoords.SetCol "Permalink to this definition")
Set the column of the coordinate.



Parameters
**n** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def SetRow(self, n: int) -> None:
        """ 

`SetRow`(*self*, *n*)[¶](#wx.grid.GridCellCoords.SetRow "Permalink to this definition")
Set the row of the coordinate.



Parameters
**n** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __bool__(self) -> None:
        """ 

`__bool__`(*self*)[¶](#wx.grid.GridCellCoords.__bool__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __getitem__(self, idx) -> None:
        """ 

`__getitem__`(*self*, *idx*)[¶](#wx.grid.GridCellCoords.__getitem__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __len__(self) -> None:
        """ 

`__len__`(*self*)[¶](#wx.grid.GridCellCoords.__len__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __nonzero__(self) -> None:
        """ 

`__nonzero__`(*self*)[¶](#wx.grid.GridCellCoords.__nonzero__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __reduce__(self) -> None:
        """ 

`__reduce__`(*self*)[¶](#wx.grid.GridCellCoords.__reduce__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __repr__(self) -> None:
        """ 

`__repr__`(*self*)[¶](#wx.grid.GridCellCoords.__repr__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __setitem__(self, idx, val) -> None:
        """ 

`__setitem__`(*self*, *idx*, *val*)[¶](#wx.grid.GridCellCoords.__setitem__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __str__(self) -> None:
        """ 

`__str__`(*self*)[¶](#wx.grid.GridCellCoords.__str__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __ne__(self, item: Any) -> bool:
        """ 

`__ne__`(*self*)[¶](#wx.grid.GridCellCoords.__ne__ "Permalink to this definition")
Inequality operator.



Parameters
**other** ([*wx.grid.GridCellCoords*](#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.grid.GridCellCoords.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**other** ([*wx.grid.GridCellCoords*](#wx.grid.GridCellCoords "wx.grid.GridCellCoords")) – 






            Source: https://docs.wxpython.org/wx.grid.GridCellCoords.html
        """

    Col: int  # `Col`[¶](#wx.grid.GridCellCoords.Col "Permalink to this definition")See [`GetCol`](#wx.grid.GridCellCoords.GetCol "wx.grid.GridCellCoords.GetCol") and [`SetCol`](#wx.grid.GridCellCoords.SetCol "wx.grid.GridCellCoords.SetCol")
    Row: int  # `Row`[¶](#wx.grid.GridCellCoords.Row "Permalink to this definition")See [`GetRow`](#wx.grid.GridCellCoords.GetRow "wx.grid.GridCellCoords.GetRow") and [`SetRow`](#wx.grid.GridCellCoords.SetRow "wx.grid.GridCellCoords.SetRow")



class GridFitMode:
    """ **Possible constructors**:



```
GridFitMode()

```


Allows to specify the behaviour when the cell contents doesn’t fit
into its allotted space.


  


        Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridFitMode.__init__ "Permalink to this definition")
Default constructor creates an object not specifying any behaviour.


This constructor is not very useful, use static methods [`Clip`](#wx.grid.GridFitMode.Clip "wx.grid.GridFitMode.Clip") and [`Overflow`](#wx.grid.GridFitMode.Overflow "wx.grid.GridFitMode.Overflow") below to create objects of this class instead.




            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Clip() -> 'GridFitMode':
        """ 

*static* `Clip`()[¶](#wx.grid.GridFitMode.Clip "Permalink to this definition")
Pseudo-constructor for object specifying clipping behaviour.



Return type
 [wx.grid.GridFitMode](#wx-grid-gridfitmode)






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Ellipsize(ellipsize: EllipsizeMode=ELLIPSIZE_END) -> 'GridFitMode':
        """ 

*static* `Ellipsize`(*ellipsize=ELLIPSIZE\_END*)[¶](#wx.grid.GridFitMode.Ellipsize "Permalink to this definition")
Pseudo-constructor for object specifying ellipsize behaviour.



Parameters
**ellipsize** ([*EllipsizeMode*](wx.EllipsizeMode.enumeration.html "EllipsizeMode")) – 



Return type
 [wx.grid.GridFitMode](#wx-grid-gridfitmode)






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def GetEllipsizeMode(self) -> 'EllipsizeMode':
        """ 

`GetEllipsizeMode`(*self*)[¶](#wx.grid.GridFitMode.GetEllipsizeMode "Permalink to this definition")
Return ellipsize mode, possibly `ELLIPSIZE_NONE` .


For the objects constructed using [`Ellipsize`](#wx.grid.GridFitMode.Ellipsize "wx.grid.GridFitMode.Ellipsize") , the same ellipsization mode as was passed to it is returned. For all the other objects, `ELLIPSIZE_NONE` is.



Return type
 [wx.EllipsizeMode](wx.EllipsizeMode.enumeration.html#wx-ellipsizemode)






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsClip(self) -> bool:
        """ 

`IsClip`(*self*)[¶](#wx.grid.GridFitMode.IsClip "Permalink to this definition")
Return `True` if the object specifies clipping behaviour.


This method returns `True` only for the objects returned by [`Clip`](#wx.grid.GridFitMode.Clip "wx.grid.GridFitMode.Clip") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsOverflow(self) -> bool:
        """ 

`IsOverflow`(*self*)[¶](#wx.grid.GridFitMode.IsOverflow "Permalink to this definition")
Return `True` if the object specifies overflow behaviour.


This method returns `True` only for the objects returned by [`Overflow`](#wx.grid.GridFitMode.Overflow "wx.grid.GridFitMode.Overflow") .



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    def IsSpecified(self) -> bool:
        """ 

`IsSpecified`(*self*)[¶](#wx.grid.GridFitMode.IsSpecified "Permalink to this definition")
Return `True` if the object specifies some particular behaviour.


This method returns `False` for default-constructed objects of this type only.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    @staticmethod
    def Overflow() -> 'GridFitMode':
        """ 

*static* `Overflow`()[¶](#wx.grid.GridFitMode.Overflow "Permalink to this definition")
Pseudo-constructor for object specifying overflow behaviour.



Return type
 [wx.grid.GridFitMode](#wx-grid-gridfitmode)






            Source: https://docs.wxpython.org/wx.grid.GridFitMode.html
        """

    EllipsizeMode: '_EllipsizeMode'  # `EllipsizeMode`[¶](#wx.grid.GridFitMode.EllipsizeMode "Permalink to this definition")See [`GetEllipsizeMode`](#wx.grid.GridFitMode.GetEllipsizeMode "wx.grid.GridFitMode.GetEllipsizeMode")



class GridSizesInfo:
    """ **Possible constructors**:



```
GridSizesInfo()

GridSizesInfo(defSize, allSizes)

```


GridSizesInfo stores information about sizes of all Grid rows or
columns.


  


        Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridSizesInfo.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.


m\_sizeDefault and m\_customSizes must be initialized later.




---

  



**\_\_init\_\_** *(self, defSize, allSizes)*


Constructor.


This constructor is used by [`wx.grid.Grid.GetRowSizes`](wx.grid.Grid.html#wx.grid.Grid.GetRowSizes "wx.grid.Grid.GetRowSizes") and GetColSizes() methods. User code will usually use the default constructor instead.



Parameters
* **defSize** (*int*) – The default element size.
* **allSizes** (*list of integers*) – Array containing the sizes of *all* elements, including those which have the default size.






---

  





            Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
        """

    def GetSize(self, pos: Any) -> int:
        """ 

`GetSize`(*self*, *pos*)[¶](#wx.grid.GridSizesInfo.GetSize "Permalink to this definition")
Get the element size.



Parameters
**pos** – The index of the element.



Return type
*int*



Returns
The size for this element, using m\_customSizes if *pos* is in it or m\_sizeDefault otherwise.






            Source: https://docs.wxpython.org/wx.grid.GridSizesInfo.html
        """

    m_sizeDefault: Any  # `m_sizeDefault`[¶](#wx.grid.GridSizesInfo.m_sizeDefault "Permalink to this definition")A public C++ attribute of type `int`. Default size.



class GridBlocks:
    """ Represents a collection of grid blocks that can be iterated over.


  


        Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
    """
    def __iter__(self) -> None:
        """ 

`__iter__`(*self*)[¶](#wx.grid.GridBlocks.__iter__ "Permalink to this definition")
Returns a Python iterator for accessing the collection of grid blocks.




            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """

    def begin(self) -> 'iterator':
        """ 

`begin`(*self*)[¶](#wx.grid.GridBlocks.begin "Permalink to this definition")
Return iterator corresponding to the beginning of the range.



Return type
 [wx.grid.GridBlocks.iterator](wx.grid.GridBlocks.iterator.html#wx-grid-gridblocks-iterator)






            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """

    def end(self) -> 'iterator':
        """ 

`end`(*self*)[¶](#wx.grid.GridBlocks.end "Permalink to this definition")
Return iterator corresponding to the end of the range.



Return type
 [wx.grid.GridBlocks.iterator](wx.grid.GridBlocks.iterator.html#wx-grid-gridblocks-iterator)






            Source: https://docs.wxpython.org/wx.grid.GridBlocks.html
        """



class GridTableMessage:
    """ **Possible constructors**:



```
GridTableMessage()

GridTableMessage(table, id, comInt1=-1, comInt2=-1)

```


Message class used by the grid table to send requests and
notifications to the grid view.


  


        Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.grid.GridTableMessage.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor initializes the object to invalid state.




---

  



**\_\_init\_\_** *(self, table, id, comInt1=-1, comInt2=-1)*


Constructor really initialize the message.



Parameters
* **table** ([*wx.grid.GridTableBase*](wx.grid.GridTableBase.html#wx.grid.GridTableBase "wx.grid.GridTableBase")) – Pointer to the grid table
* **id** (*int*) – One of GridTableRequest enum elements.
* **comInt1** (*int*) – For the insert/delete messages, position after which the rows or columns are inserted/deleted. For the append messages, the number of rows or columns that were appended.
* **comInt2** (*int*) – For the insert/deleted messages, number of rows or columns to be inserted/deleted. For the append messages, this parameter is not used.






---

  





            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetCommandInt(self) -> int:
        """ 

`GetCommandInt`(*self*)[¶](#wx.grid.GridTableMessage.GetCommandInt "Permalink to this definition")
Get the position after which the insertion/deletion occur.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetCommandInt2(self) -> int:
        """ 

`GetCommandInt2`(*self*)[¶](#wx.grid.GridTableMessage.GetCommandInt2 "Permalink to this definition")
Get the number of rows to be inserted/deleted.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetId(self) -> int:
        """ 

`GetId`(*self*)[¶](#wx.grid.GridTableMessage.GetId "Permalink to this definition")
Gets an id.



Return type
*int*






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def GetTableObject(self) -> 'GridTableBase':
        """ 

`GetTableObject`(*self*)[¶](#wx.grid.GridTableMessage.GetTableObject "Permalink to this definition")
Gets the table object.



Return type
 [wx.grid.GridTableBase](wx.grid.GridTableBase.html#wx-grid-gridtablebase)






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetCommandInt(self, comInt1: int) -> None:
        """ 

`SetCommandInt`(*self*, *comInt1*)[¶](#wx.grid.GridTableMessage.SetCommandInt "Permalink to this definition")
Set the position after which the insertion/deletion occur.



Parameters
**comInt1** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetCommandInt2(self, comInt2: int) -> None:
        """ 

`SetCommandInt2`(*self*, *comInt2*)[¶](#wx.grid.GridTableMessage.SetCommandInt2 "Permalink to this definition")
Set the number of rows to be inserted/deleted.



Parameters
**comInt2** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetId(self, id: int) -> None:
        """ 

`SetId`(*self*, *id*)[¶](#wx.grid.GridTableMessage.SetId "Permalink to this definition")
Sets an id.



Parameters
**id** (*int*) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    def SetTableObject(self, table: 'grid.GridTableBase') -> None:
        """ 

`SetTableObject`(*self*, *table*)[¶](#wx.grid.GridTableMessage.SetTableObject "Permalink to this definition")
Sets the table object.



Parameters
**table** ([*wx.grid.GridTableBase*](wx.grid.GridTableBase.html#wx.grid.GridTableBase "wx.grid.GridTableBase")) – 






            Source: https://docs.wxpython.org/wx.grid.GridTableMessage.html
        """

    CommandInt: int  # `CommandInt`[¶](#wx.grid.GridTableMessage.CommandInt "Permalink to this definition")See [`GetCommandInt`](#wx.grid.GridTableMessage.GetCommandInt "wx.grid.GridTableMessage.GetCommandInt") and [`SetCommandInt`](#wx.grid.GridTableMessage.SetCommandInt "wx.grid.GridTableMessage.SetCommandInt")
    CommandInt2: int  # `CommandInt2`[¶](#wx.grid.GridTableMessage.CommandInt2 "Permalink to this definition")See [`GetCommandInt2`](#wx.grid.GridTableMessage.GetCommandInt2 "wx.grid.GridTableMessage.GetCommandInt2") and [`SetCommandInt2`](#wx.grid.GridTableMessage.SetCommandInt2 "wx.grid.GridTableMessage.SetCommandInt2")
    Id: int  # `Id`[¶](#wx.grid.GridTableMessage.Id "Permalink to this definition")See [`GetId`](#wx.grid.GridTableMessage.GetId "wx.grid.GridTableMessage.GetId") and [`SetId`](#wx.grid.GridTableMessage.SetId "wx.grid.GridTableMessage.SetId")
    TableObject: 'GridTableBase'  # `TableObject`[¶](#wx.grid.GridTableMessage.TableObject "Permalink to this definition")See [`GetTableObject`](#wx.grid.GridTableMessage.GetTableObject "wx.grid.GridTableMessage.GetTableObject") and [`SetTableObject`](#wx.grid.GridTableMessage.SetTableObject "wx.grid.GridTableMessage.SetTableObject")



class GridColumnHeaderRendererDefault(GridColumnHeaderRenderer):
    """ Default column header renderer.


  


        Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ 

`DrawBorder`(*self*, *grid*, *dc*, *rect*)[¶](#wx.grid.GridColumnHeaderRendererDefault.DrawBorder "Permalink to this definition")
Implement border drawing for the column labels.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRendererDefault.html
        """



class GridColumnHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for column headers renderer.




        Source: https://docs.wxpython.org/wx.grid.GridColumnHeaderRenderer.html
    """


class GridCornerHeaderRendererDefault(GridCornerHeaderRenderer):
    """ Default corner window renderer.


  


        Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ 

`DrawBorder`(*self*, *grid*, *dc*, *rect*)[¶](#wx.grid.GridCornerHeaderRendererDefault.DrawBorder "Permalink to this definition")
Implement border drawing for the corner window.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRendererDefault.html
        """



class GridCornerHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for corner header renderer.




        Source: https://docs.wxpython.org/wx.grid.GridCornerHeaderRenderer.html
    """


class GridRowHeaderRendererDefault(GridRowHeaderRenderer):
    """ Default row header renderer.


  


        Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRendererDefault.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ 

`DrawBorder`(*self*, *grid*, *dc*, *rect*)[¶](#wx.grid.GridRowHeaderRendererDefault.DrawBorder "Permalink to this definition")
Implement border drawing for the row labels.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRendererDefault.html
        """



class GridRowHeaderRenderer(GridHeaderLabelsRenderer):
    """ Base class for row headers renderer.




        Source: https://docs.wxpython.org/wx.grid.GridRowHeaderRenderer.html
    """


class GridCellAutoWrapStringRenderer(GridCellStringRenderer):
    """ **Possible constructors**:



```
GridCellAutoWrapStringRenderer()

```


This class may be used to format string data in a cell.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellAutoWrapStringRenderer.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringRenderer.html
        """



class GridCellEnumRenderer(GridCellStringRenderer):
    """ **Possible constructors**:



```
GridCellEnumRenderer(choices="")

```


This class may be used to render in a cell a number as a textual
equivalent.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
    """
    def __init__(self, choices: str="") -> None:
        """ 

`__init__`(*self*, *choices=""*)[¶](#wx.grid.GridCellEnumRenderer.__init__ "Permalink to this definition")
Enum renderer constructor.



Parameters
**choices** (*string*) – Comma separated string parameters “item1[,item2[…,itemN]]”.






            Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
        """

    def SetParameters(self, params: str) -> None:
        """ 

`SetParameters`(*self*, *params*)[¶](#wx.grid.GridCellEnumRenderer.SetParameters "Permalink to this definition")
Sets the comma separated string content of the enum.



Parameters
**params** (*string*) – Comma separated string parameters “item1[,item2[…,itemN]]”.






            Source: https://docs.wxpython.org/wx.grid.GridCellEnumRenderer.html
        """



GridCellFloatFormat: TypeAlias = int  # Enumeration

GRID_FLOAT_FORMAT_FIXED: int

GRID_FLOAT_FORMAT_SCIENTIFIC: int

GRID_FLOAT_FORMAT_COMPACT: int

GRID_FLOAT_FORMAT_UPPER: int

GRID_FLOAT_FORMAT_DEFAULT: int

class GridCellActivatableEditor(GridCellEditor):
    """ Base class for activatable editors.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
    """
    def DoActivate(self, row, col, grid) -> None:
        """ 

`DoActivate`(*self*, *row*, *col*, *grid*)[¶](#wx.grid.GridCellActivatableEditor.DoActivate "Permalink to this definition")
Same method as in  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor), but pure virtual.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –






            Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
        """

    def TryActivate(self, row, col, grid, actSource) -> 'GridActivationResult':
        """ 

`TryActivate`(*self*, *row*, *col*, *grid*, *actSource*)[¶](#wx.grid.GridCellActivatableEditor.TryActivate "Permalink to this definition")
Same method as in  [wx.grid.GridCellEditor](wx.grid.GridCellEditor.html#wx-grid-gridcelleditor), but pure virtual.


Note that the implementation of this method must never return [`wx.grid.GridActivationResult.DoEdit`](wx.grid.GridActivationResult.html#wx.grid.GridActivationResult.DoEdit "wx.grid.GridActivationResult.DoEdit") for the editors inheriting from this class, as it doesn’t support normal editing.



Parameters
* **row** (*int*) –
* **col** (*int*) –
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **actSource** ([*wx.grid.GridActivationSource*](wx.grid.GridActivationSource.html#wx.grid.GridActivationSource "wx.grid.GridActivationSource")) –



Return type
 [wx.grid.GridActivationResult](wx.grid.GridActivationResult.html#wx-grid-gridactivationresult)






            Source: https://docs.wxpython.org/wx.grid.GridCellActivatableEditor.html
        """



class GridCellAutoWrapStringEditor(GridCellTextEditor):
    """ **Possible constructors**:



```
GridCellAutoWrapStringEditor()

```


Grid cell editor for wrappable string/text data.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.grid.GridCellAutoWrapStringEditor.__init__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellAutoWrapStringEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellAutoWrapStringEditor.html
        """



class GridCellEnumEditor(GridCellChoiceEditor):
    """ **Possible constructors**:



```
GridCellEnumEditor(choices="")

```


Grid cell editor which displays an enum number as a textual equivalent
(e.g.


  


        Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
    """
    def __init__(self, choices: str="") -> None:
        """ 

`__init__`(*self*, *choices=""*)[¶](#wx.grid.GridCellEnumEditor.__init__ "Permalink to this definition")
Enum cell editor constructor.



Parameters
**choices** (*string*) – Comma separated choice parameters “item1[,item2[…,itemN]]”.






            Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
        """

    def EndEdit(self, row, col, grid, oldval) -> None:
        """ 

`EndEdit`(*self*, *row*, *col*, *grid*, *oldval*)[¶](#wx.grid.GridCellEnumEditor.EndEdit "Permalink to this definition")
End editing the cell.


This function must check if the current value of the editing cell
is valid and different from the original value in its string
form. If not then simply return None. If it has changed then
this method should save the new value so that ApplyEdit can
apply it later and the string representation of the new value
should be returned.


Notice that this method shoiuld not modify the grid as the
change could still be vetoed.




            Source: https://docs.wxpython.org/wx.grid.GridCellEnumEditor.html
        """



class GridActivationSource:
    """ Represents a source of cell activation, which may be either a user
event (mouse or keyboard) or the program itself.


  


        Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
    """
    def GetKeyEvent(self) -> 'KeyEvent':
        """ 

`GetKeyEvent`(*self*)[¶](#wx.grid.GridActivationSource.GetKeyEvent "Permalink to this definition")
Get the key event corresponding to the key press activating the cell.


This method can be called for objects with Key origin only, use [`GetOrigin`](#wx.grid.GridActivationSource.GetOrigin "wx.grid.GridActivationSource.GetOrigin") to check for this first.



Return type
[`KeyEvent`](#wx.grid.GridActivationSource.KeyEvent "wx.grid.GridActivationSource.KeyEvent")






            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    def GetMouseEvent(self) -> 'MouseEvent':
        """ 

`GetMouseEvent`(*self*)[¶](#wx.grid.GridActivationSource.GetMouseEvent "Permalink to this definition")
Get the mouse event corresponding to the click activating the cell.


This method can be called for objects with Mouse origin only, use [`GetOrigin`](#wx.grid.GridActivationSource.GetOrigin "wx.grid.GridActivationSource.GetOrigin") to check for this first.



Return type
[`MouseEvent`](#wx.grid.GridActivationSource.MouseEvent "wx.grid.GridActivationSource.MouseEvent")






            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    def GetOrigin(self) -> 'Origin':
        """ 

`GetOrigin`(*self*)[¶](#wx.grid.GridActivationSource.GetOrigin "Permalink to this definition")
Get the origin of the activation.



Return type
 [wx.grid.GridActivationSource.Origin](wx.grid.GridActivationSource.Origin.enumeration.html#wx-grid-gridactivationsource-origin)






            Source: https://docs.wxpython.org/wx.grid.GridActivationSource.html
        """

    KeyEvent: '_KeyEvent'  # `KeyEvent`[¶](#wx.grid.GridActivationSource.KeyEvent "Permalink to this definition")See [`GetKeyEvent`](#wx.grid.GridActivationSource.GetKeyEvent "wx.grid.GridActivationSource.GetKeyEvent")
    MouseEvent: '_MouseEvent'  # `MouseEvent`[¶](#wx.grid.GridActivationSource.MouseEvent "Permalink to this definition")See [`GetMouseEvent`](#wx.grid.GridActivationSource.GetMouseEvent "wx.grid.GridActivationSource.GetMouseEvent")



class GridActivationResult:
    """ Represents the result of *GridCellEditor.TryActivate().*


  


        Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
    """
    @staticmethod
    def DoChange(newval: str) -> 'GridActivationResult':
        """ 

*static* `DoChange`(*newval*)[¶](#wx.grid.GridActivationResult.DoChange "Permalink to this definition")
Indicate that activating the cell is possible and would change its value to the given one.


This is the method to call for activatable editors, using it will result in changing the value of the cell to *newval* without showing the editor control at all.


Note that the change may still be vetoed by wxEVT\_GRID\_CELL\_CHANGING handler.



Parameters
**newval** (*string*) – 



Return type
 [wx.grid.GridActivationResult](#wx-grid-gridactivationresult)






            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """

    @staticmethod
    def DoEdit() -> 'GridActivationResult':
        """ 

*static* `DoEdit`()[¶](#wx.grid.GridActivationResult.DoEdit "Permalink to this definition")
Indicate that the editor control should be shown and the cell should be edited normally.


This is the default return value of [`wx.grid.GridCellEditor.TryActivate`](wx.grid.GridCellEditor.html#wx.grid.GridCellEditor.TryActivate "wx.grid.GridCellEditor.TryActivate") .



Return type
 [wx.grid.GridActivationResult](#wx-grid-gridactivationresult)






            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """

    @staticmethod
    def DoNothing() -> 'GridActivationResult':
        """ 

*static* `DoNothing`()[¶](#wx.grid.GridActivationResult.DoNothing "Permalink to this definition")
Indicate that nothing should be done and the cell shouldn’t be edited at all.


Note that this is different from [`DoEdit`](#wx.grid.GridActivationResult.DoEdit "wx.grid.GridActivationResult.DoEdit") and may be useful when the value of the cell wouldn’t change if it were activated anyhow, e.g. because the key or mouse event carried by  [wx.grid.GridActivationSource](wx.grid.GridActivationSource.html#wx-grid-gridactivationsource) would leave the cell value unchanged.



Return type
 [wx.grid.GridActivationResult](#wx-grid-gridactivationresult)






            Source: https://docs.wxpython.org/wx.grid.GridActivationResult.html
        """



class GridHeaderLabelsRenderer:
    """ Base class for header cells renderers.


  


        Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
    """
    def DrawBorder(self, grid, dc, rect) -> None:
        """ 

`DrawBorder`(*self*, *grid*, *dc*, *rect*)[¶](#wx.grid.GridHeaderLabelsRenderer.DrawBorder "Permalink to this definition")
Called by the grid to draw the border around the cell header.


This method is responsible for drawing the border inside the given *rect* and adjusting the rectangle size to correspond to the area inside the border, i.e. usually call [`wx.Rect.Deflate`](wx.Rect.html#wx.Rect.Deflate "wx.Rect.Deflate") to account for the border width.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) – The grid whose header cell window is being drawn.
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – The device context to use for drawing.
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – Input/output parameter which contains the border rectangle on input and should be updated to contain the area inside the border on function return.






            Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
        """

    def DrawLabel(self, grid, dc, value, rect, horizAlign, vertAlign, textOrientation) -> None:
        """ 

`DrawLabel`(*self*, *grid*, *dc*, *value*, *rect*, *horizAlign*, *vertAlign*, *textOrientation*)[¶](#wx.grid.GridHeaderLabelsRenderer.DrawLabel "Permalink to this definition")
Called by the grid to draw the specified label.


Notice that the [`DrawBorder`](#wx.grid.GridHeaderLabelsRenderer.DrawBorder "wx.grid.GridHeaderLabelsRenderer.DrawBorder") method is called before this one.


The default implementation uses [`wx.grid.Grid.GetLabelTextColour`](wx.grid.Grid.html#wx.grid.Grid.GetLabelTextColour "wx.grid.Grid.GetLabelTextColour") and [`wx.grid.Grid.GetLabelFont`](wx.grid.Grid.html#wx.grid.Grid.GetLabelFont "wx.grid.Grid.GetLabelFont") to draw the label.



Parameters
* **grid** ([*wx.grid.Grid*](wx.grid.Grid.html#wx.grid.Grid "wx.grid.Grid")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **value** (*string*) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **horizAlign** (*int*) –
* **vertAlign** (*int*) –
* **textOrientation** (*int*) –






            Source: https://docs.wxpython.org/wx.grid.GridHeaderLabelsRenderer.html
        """



GridCellCoordsArray: TypeAlias = list['GridCellCoords']

GridSelectionModes: TypeAlias = int

AttrKind: TypeAlias = int

GridWindow: TypeAlias = Any

GridCellAttrPtr: TypeAlias = Any

TabBehaviour: TypeAlias = int  # Enumeration

GRID_VALUE_STRING: str

GRID_VALUE_BOOL: str

GRID_VALUE_NUMBER: str

GRID_VALUE_FLOAT: str

GRID_VALUE_CHOICE: str

GRID_VALUE_DATE: str

GRID_VALUE_TEXT: str

GRID_VALUE_LONG: str

GRID_VALUE_CHOICEINT: str

GRID_VALUE_DATETIME: str

