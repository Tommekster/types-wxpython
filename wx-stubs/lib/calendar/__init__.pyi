# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class CalDraw:
    """ A class to draw a calendar.


  


        Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
    """
    def __init__(self, parent: 'Window') -> None:
        """ 

`__init__`(*self*, *parent*)[¶](#wx.lib.calendar.CalDraw.__init__ "Permalink to this definition")
Default class constructor



Parameters
**parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def AddSelect(self, list, cfont=None, cbackgrd=None) -> None:
        """ 

`AddSelect`(*self*, *list*, *cfont=None*, *cbackgrd=None*)[¶](#wx.lib.calendar.CalDraw.AddSelect "Permalink to this definition")
Add a selection of days.



Parameters
* **list** – a list of days to select
* **cfont** – the font color to use
* **cbackgrd** – the background color to use






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def Center(self) -> None:
        """ 

`Center`(*self*)[¶](#wx.lib.calendar.CalDraw.Center "Permalink to this definition")
Calculate the dimensions in the center of the drawing area.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DefParms(self) -> None:
        """ 

`DefParms`(*self*)[¶](#wx.lib.calendar.CalDraw.DefParms "Permalink to this definition")
Setup the default parameters.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawBorder(self, DC, transparent=False) -> None:
        """ 

`DrawBorder`(*self*, *DC*, *transparent=False*)[¶](#wx.lib.calendar.CalDraw.DrawBorder "Permalink to this definition")
Draw a border around the outside of the main display rectangle.



Parameters
* **DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use
* **transparent** – use a transparent brush, default is `False`.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawCal(self, DC, sel_lst=[]) -> None:
        """ 

`DrawCal`(*self*, *DC*, *sel\_lst=[]*)[¶](#wx.lib.calendar.CalDraw.DrawCal "Permalink to this definition")
Draw the calendar.



Parameters
* **DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use to draw upon.
* **sel\_list** – a list of days to override the weekend highlight.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawDayText(self, DC, key) -> None:
        """ 

`DrawDayText`(*self*, *DC*, *key*)[¶](#wx.lib.calendar.CalDraw.DrawDayText "Permalink to this definition")
Draw the day text.



Parameters
* **DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use.
* **key** – the day to draw






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawFocusIndicator(self, DC: 'DC') -> None:
        """ 

`DrawFocusIndicator`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawFocusIndicator "Permalink to this definition")
Draw the focus indicator



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawGrid(self, DC: 'DC') -> None:
        """ 

`DrawGrid`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawGrid "Permalink to this definition")
Calculate and draw the grid lines.



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawMonth(self, DC: 'DC') -> None:
        """ 

`DrawMonth`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawMonth "Permalink to this definition")
Draw the month and year titles.



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawNum(self, DC: 'DC') -> None:
        """ 

`DrawNum`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawNum "Permalink to this definition")
Draw the day numbers



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawNumVal(self) -> None:
        """ 

`DrawNumVal`(*self*)[¶](#wx.lib.calendar.CalDraw.DrawNumVal "Permalink to this definition")
Draw the numeric values.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawSel(self, DC: 'DC') -> None:
        """ 

`DrawSel`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawSel "Permalink to this definition")
Highlight selected days.



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def DrawWeek(self, DC: 'DC') -> None:
        """ 

`DrawWeek`(*self*, *DC*)[¶](#wx.lib.calendar.CalDraw.DrawWeek "Permalink to this definition")
Draw the week days.



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to use.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetCal(self) -> None:
        """ 

`GetCal`(*self*)[¶](#wx.lib.calendar.CalDraw.GetCal "Permalink to this definition")
Get the calendar days.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetColor(self, name: Any) -> None:
        """ 

`GetColor`(*self*, *name*)[¶](#wx.lib.calendar.CalDraw.GetColor "Permalink to this definition")
Get a color.



Parameters
**name** – one of the defined color names.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetOffset(self) -> None:
        """ 

`GetOffset`(*self*)[¶](#wx.lib.calendar.CalDraw.GetOffset "Permalink to this definition")
Get the offset position.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def GetRect(self) -> None:
        """ 

`GetRect`(*self*)[¶](#wx.lib.calendar.CalDraw.GetRect "Permalink to this definition")
Get the display rectangle list of the day grid.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def InitScale(self) -> None:
        """ 

`InitScale`(*self*)[¶](#wx.lib.calendar.CalDraw.InitScale "Permalink to this definition")
Set the default scale values.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def InitValues(self) -> None:
        """ 

`InitValues`(*self*)[¶](#wx.lib.calendar.CalDraw.InitValues "Permalink to this definition")
Default dimensions of various elements of the calendar.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetCal(self, year, month) -> None:
        """ 

`SetCal`(*self*, *year*, *month*)[¶](#wx.lib.calendar.CalDraw.SetCal "Permalink to this definition")
Calculate the calendar days and offset position.



Parameters
* **year** (*int*) – the year to calculate.
* **month** (*int*) – the month to calculate.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetColor(self, name, value) -> None:
        """ 

`SetColor`(*self*, *name*, *value*)[¶](#wx.lib.calendar.CalDraw.SetColor "Permalink to this definition")
Set a color.



Parameters
* **name** – the name to assign the color too.
* **value** – the color to use, see [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetMarg(self, xmarg, ymarg) -> None:
        """ 

`SetMarg`(*self*, *xmarg*, *ymarg*)[¶](#wx.lib.calendar.CalDraw.SetMarg "Permalink to this definition")
Set the margins.



Parameters
* **xmarg** – the x margin
* **ymarg** – the y margin, also used for the end margin






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetPos(self, xpos, ypos) -> None:
        """ 

`SetPos`(*self*, *xpos*, *ypos*)[¶](#wx.lib.calendar.CalDraw.SetPos "Permalink to this definition")
Set the position.



Parameters
* **xpos** (*int*) – the x position
* **ypos** (*int*) – the y position






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetSize(self, size: Any) -> None:
        """ 

`SetSize`(*self*, *size*)[¶](#wx.lib.calendar.CalDraw.SetSize "Permalink to this definition")
Set the size.



Parameters
**size** – a tuple/list with width and height






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetWeekColor(self, font_color, week_color) -> None:
        """ 

`SetWeekColor`(*self*, *font\_color*, *week\_color*)[¶](#wx.lib.calendar.CalDraw.SetWeekColor "Permalink to this definition")
Set the font and background color of the week title.



Parameters
* **font\_color** – the font color, a value as is accepted by [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")
* **week\_color** – the week color, a value as is accepted by [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour")






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """

    def SetWeekEnd(self, font_color=None, backgrd=None) -> None:
        """ 

`SetWeekEnd`(*self*, *font\_color=None*, *backgrd=None*)[¶](#wx.lib.calendar.CalDraw.SetWeekEnd "Permalink to this definition")
Set the weekend backgrounds.



Parameters
* **font\_color** – the font color to use, if `None` the default is used.
* **backgrd** – the background color to use, if `None` the default is used.






            Source: https://docs.wxpython.org/wx.lib.calendar.CalDraw.html
        """



class Calendar(Control):
    """ A calendar control class.


  


        Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
    """
    def __init__(*args, **kwargs) -> None:
        """ 

`__init__`(*self*, *parent*, *id=-1*, *pos=wx.DefaultPosition*, *size=wx.Size(200*, *200)*, *style=0*, *validator=wx.DefaultValidator*, *name="calendar"*)[¶](#wx.lib.calendar.Calendar.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **id** (*integer*) – window identifier. A value of -1 indicates a default value;
* **pos** (tuple or [`wx.Point`](wx.Point.html#wx.Point "wx.Point")) – the control position. A value of (-1, -1) indicates a default position,
chosen by either the windowing system or wxPython, depending on platform;
* **size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;
* **style** (*integer*) – the button style (unused);
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – the validator associated to the button;
* **name** (*string*) – the calendar name.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def AcceptsFocus(self) -> None:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.lib.calendar.Calendar.AcceptsFocus "Permalink to this definition")
Can it accept focus?




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def AddSelect(self, list, font_color, back_color) -> None:
        """ 

`AddSelect`(*self*, *list*, *font\_color*, *back\_color*)[¶](#wx.lib.calendar.Calendar.AddSelect "Permalink to this definition")
Add a selection.



Parameters
* **list** – list of days to select
* **font\_color** – the font color to use
* **back\_color** – the back color to use






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DecMonth(self) -> None:
        """ 

`DecMonth`(*self*)[¶](#wx.lib.calendar.Calendar.DecMonth "Permalink to this definition")
Decrement the month by 1.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DecYear(self) -> None:
        """ 

`DecYear`(*self*)[¶](#wx.lib.calendar.Calendar.DecYear "Permalink to this definition")
Decrement the year by 1.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DoDrawing(self, DC: 'DC') -> None:
        """ 

`DoDrawing`(*self*, *DC*)[¶](#wx.lib.calendar.Calendar.DoDrawing "Permalink to this definition")
Do the drawing.



Parameters
**DC** – the [`wx.DC`](wx.DC.html#wx.DC "wx.DC") to draw






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawFocusIndicator(self, draw: bool) -> None:
        """ 

`DrawFocusIndicator`(*self*, *draw*)[¶](#wx.lib.calendar.Calendar.DrawFocusIndicator "Permalink to this definition")
Draw the focus indicator or a border.



Parameters
**draw** – `True` draws the focus indicator, `False` a border






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawRect(self, key, bgcolor='WHITE', fgcolor='PINK', width=0) -> None:
        """ 

`DrawRect`(*self*, *key*, *bgcolor='WHITE'*, *fgcolor='PINK'*, *width=0*)[¶](#wx.lib.calendar.Calendar.DrawRect "Permalink to this definition")
Draw a rectangle.



Parameters
* **key** – the day to draw the rectangle on
* **bgcolor** – the background color






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def DrawRectOrg(self, key, fgcolor='BLACK', width=0) -> None:
        """ 

`DrawRectOrg`(*self*, *key*, *fgcolor='BLACK'*, *width=0*)[¶](#wx.lib.calendar.Calendar.DrawRectOrg "Permalink to this definition")
Draw a rectangle.



Parameters
* **key** – the day to draw the rectangle on
* **fgcolor** – the color for the pen
* **width** – the width for the pen






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetColor(self, color: str) -> None:
        """ 

`GetColor`(*self*, *name*)[¶](#wx.lib.calendar.Calendar.GetColor "Permalink to this definition")
Get a color.



Parameters
**name** – a valid color name, can be defined using [`SetColor`](#wx.lib.calendar.Calendar.SetColor "wx.lib.calendar.Calendar.SetColor")






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDate(self) -> None:
        """ 

`GetDate`(*self*)[¶](#wx.lib.calendar.Calendar.GetDate "Permalink to this definition")
Get the set calendar date.



Returns
the day, the month and the year






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDay(self) -> None:
        """ 

`GetDay`(*self*)[¶](#wx.lib.calendar.Calendar.GetDay "Permalink to this definition")
Get the set calendar day.



Returns
the day






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetDayHit(self, mx, my) -> None:
        """ 

`GetDayHit`(*self*, *mx*, *my*)[¶](#wx.lib.calendar.Calendar.GetDayHit "Permalink to this definition")
Find the clicked area rectangle.



Parameters
* **mx** – the x position
* **my** – the y position






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetMonth(self) -> None:
        """ 

`GetMonth`(*self*)[¶](#wx.lib.calendar.Calendar.GetMonth "Permalink to this definition")
Get the set calendar month.



Returns
the month






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def GetYear(self) -> None:
        """ 

`GetYear`(*self*)[¶](#wx.lib.calendar.Calendar.GetYear "Permalink to this definition")
Get the set calendar year.



Returns
the year






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def HideGrid(self) -> None:
        """ 

`HideGrid`(*self*)[¶](#wx.lib.calendar.Calendar.HideGrid "Permalink to this definition")
Hide the calendar grid.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def HideTitle(self) -> None:
        """ 

`HideTitle`(*self*)[¶](#wx.lib.calendar.Calendar.HideTitle "Permalink to this definition")
Hide the calendar title.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IncMonth(self) -> None:
        """ 

`IncMonth`(*self*)[¶](#wx.lib.calendar.Calendar.IncMonth "Permalink to this definition")
Increment the month by 1.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IncYear(self) -> None:
        """ 

`IncYear`(*self*)[¶](#wx.lib.calendar.Calendar.IncYear "Permalink to this definition")
Increment the year by 1.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def IsDayInWeekend(self, key: Any) -> None:
        """ 

`IsDayInWeekend`(*self*, *key*)[¶](#wx.lib.calendar.Calendar.IsDayInWeekend "Permalink to this definition")
Is the day in the weekend



Parameters
**key** – the day to check






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def MoveDate(self, months=0, years=0) -> None:
        """ 

`MoveDate`(*self*, *months=0*, *years=0*)[¶](#wx.lib.calendar.Calendar.MoveDate "Permalink to this definition")
Move the current date by a given interval of months/years.



Parameters
* **months** (*int*) – months to add (can be negative)
* **years** (*int*) – years to add (can be negative)



Returns
the new date set.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnKeyDown(self, event) -> None:
        """ 

`OnKeyDown`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnKeyDown "Permalink to this definition")
Key down event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnKillFocus(self, event) -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnKillFocus "Permalink to this definition")
Kill focus event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnLeftDEvent(self, event) -> None:
        """ 

`OnLeftDEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnLeftDEvent "Permalink to this definition")
Left double mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnLeftEvent(self, event) -> None:
        """ 

`OnLeftEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnLeftEvent "Permalink to this definition")
Left mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnMiddleDEvent(self, event) -> None:
        """ 

`OnMiddleDEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnMiddleDEvent "Permalink to this definition")
Middle double mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnMiddleEvent(self, event) -> None:
        """ 

`OnMiddleEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnMiddleEvent "Permalink to this definition")
Middle mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnPaint(self, event) -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnPaint "Permalink to this definition")
The on paint event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnRightDEvent(self, event) -> None:
        """ 

`OnRightDEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnRightDEvent "Permalink to this definition")
Right double mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnRightEvent(self, event) -> None:
        """ 

`OnRightEvent`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnRightEvent "Permalink to this definition")
Right mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnSetFocus(self, event) -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.OnSetFocus "Permalink to this definition")
Set focus event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def OnSize(self, evt) -> None:
        """ 

`OnSize`(*self*, *evt*)[¶](#wx.lib.calendar.Calendar.OnSize "Permalink to this definition")
The on size event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def ProcessClick(self, event) -> None:
        """ 

`ProcessClick`(*self*, *event*)[¶](#wx.lib.calendar.Calendar.ProcessClick "Permalink to this definition")
Determine the calendar rectangle click area and draw a selection.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SelectDay(self, key: Any) -> None:
        """ 

`SelectDay`(*self*, *key*)[¶](#wx.lib.calendar.Calendar.SelectDay "Permalink to this definition")
Select the day.



Parameters
**key** – The day to select






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetBusType(self) -> None:
        """ 

`SetBusType`(*self*)[¶](#wx.lib.calendar.Calendar.SetBusType "Permalink to this definition")
Set the calendar type to ‘BUS’.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetColor(self, name, value) -> None:
        """ 

`SetColor`(*self*, *name*, *value*)[¶](#wx.lib.calendar.Calendar.SetColor "Permalink to this definition")
Set a color.



Parameters
* **name** – the name to be assigned to the color.
* **value** – the color value, see [`wx.Colour`](wx.Colour.html#wx.Colour "wx.Colour") for valid values






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetCurrentDay(self) -> None:
        """ 

`SetCurrentDay`(*self*)[¶](#wx.lib.calendar.Calendar.SetCurrentDay "Permalink to this definition")
Set the current day to today.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDate(self, day, month, year) -> None:
        """ 

`SetDate`(*self*, *day*, *month*, *year*)[¶](#wx.lib.calendar.Calendar.SetDate "Permalink to this definition")
Set a calendar date.



Parameters
* **day** (*int*) – the day
* **month** (*int*) – the month
* **year** (*int*) – the year



Raises
*ValueError* when setting an invalid month/year



Returns
the new date set.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDay(self, day: Any) -> None:
        """ 

`SetDay`(*self*, *day*)[¶](#wx.lib.calendar.Calendar.SetDay "Permalink to this definition")
Set the day.



Parameters
**day** – the day to select






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetDayValue(self, day: int) -> None:
        """ 

`SetDayValue`(*self*, *day*)[¶](#wx.lib.calendar.Calendar.SetDayValue "Permalink to this definition")
Set the day.



Parameters
**day** (*int*) – the day



Raises
*ValueError* if the resulting date is invalid.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetMargin(self, xmarg, ymarg) -> None:
        """ 

`SetMargin`(*self*, *xmarg*, *ymarg*)[¶](#wx.lib.calendar.Calendar.SetMargin "Permalink to this definition")
Set the margins



Parameters
* **xmarg** – the ‘x’ margin
* **ymarg** – the ‘y’ margin






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetMonth(self, month: int) -> None:
        """ 

`SetMonth`(*self*, *month*)[¶](#wx.lib.calendar.Calendar.SetMonth "Permalink to this definition")
Set the Month.



Parameters
**month** (*int*) – the month



Raises
*ValueError* if the resulting date is invalid.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetNow(self) -> None:
        """ 

`SetNow`(*self*)[¶](#wx.lib.calendar.Calendar.SetNow "Permalink to this definition")
Set the current day.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetSelDay(self, sel: list) -> None:
        """ 

`SetSelDay`(*self*, *sel*)[¶](#wx.lib.calendar.Calendar.SetSelDay "Permalink to this definition")
Set the days to highlight.



Parameters
**sel** (*list*) – the list of days to highlight






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetSize(self, set_size: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetSize`(*self*, *set\_size*)[¶](#wx.lib.calendar.Calendar.SetSize "Permalink to this definition")
Set the size.



Parameters
**set\_size** (tuple or [`wx.Size`](wx.Size.html#wx.Size "wx.Size")) – the control size. A value of (-1, -1) indicates a default size,
chosen by either the windowing system or wxPython, depending on platform;






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetTextAlign(self, vert, horz) -> None:
        """ 

`SetTextAlign`(*self*, *vert*, *horz*)[¶](#wx.lib.calendar.Calendar.SetTextAlign "Permalink to this definition")
Set the text alignment.



Parameters
* **vert** – the vertical alignment
* **horz** – the horizontal alignment






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetWeekColor(self, font_color, week_color) -> None:
        """ 

`SetWeekColor`(*self*, *font\_color*, *week\_color*)[¶](#wx.lib.calendar.Calendar.SetWeekColor "Permalink to this definition")
Set the week title color.



Parameters
* **font\_color** – the font color to use.
* **week\_color** – the week color to use for the background.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def SetYear(self, year: int) -> None:
        """ 

`SetYear`(*self*, *year*)[¶](#wx.lib.calendar.Calendar.SetYear "Permalink to this definition")
Set the year.



Parameters
**year** (*int*) – the year



Raises
*ValueError* if the resulting date is invalid.






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def ShowWeekEnd(self) -> None:
        """ 

`ShowWeekEnd`(*self*)[¶](#wx.lib.calendar.Calendar.ShowWeekEnd "Permalink to this definition")
Highlight the weekend.




            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """

    def TestDay(self, key: Any) -> None:
        """ 

`TestDay`(*self*, *key*)[¶](#wx.lib.calendar.Calendar.TestDay "Permalink to this definition")
Test to see if the selection has a date and create event.



Parameters
**key** – the day to test






            Source: https://docs.wxpython.org/wx.lib.calendar.Calendar.html
        """



class CalenDlg(Dialog):
    """ A dialog with a calendar control.


  


        Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
    """
    def __init__(self, parent, month=None, day=None, year=None) -> None:
        """ 

`__init__`(*self*, *parent*, *month=None*, *day=None*, *year=None*)[¶](#wx.lib.calendar.CalenDlg.__init__ "Permalink to this definition")
Default class constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent window. Must not be `None`;
* **month** (*integer*) – the month, if None the current day will be used
* **day** (*integer*) – the day
* **year** (*integer*) – the year






            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def EvtComboBox(self, event) -> None:
        """ 

`EvtComboBox`(*self*, *event*)[¶](#wx.lib.calendar.CalenDlg.EvtComboBox "Permalink to this definition")
The month combobox event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def MouseClick(self, evt) -> None:
        """ 

`MouseClick`(*self*, *evt*)[¶](#wx.lib.calendar.CalenDlg.MouseClick "Permalink to this definition")
The mouse click event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnCancel(self, event) -> None:
        """ 

`OnCancel`(*self*, *event*)[¶](#wx.lib.calendar.CalenDlg.OnCancel "Permalink to this definition")
The Cancel event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnMonthSpin(self, event) -> None:
        """ 

`OnMonthSpin`(*self*, *event*)[¶](#wx.lib.calendar.CalenDlg.OnMonthSpin "Permalink to this definition")
The month spin control event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnOk(self, evt) -> None:
        """ 

`OnOk`(*self*, *evt*)[¶](#wx.lib.calendar.CalenDlg.OnOk "Permalink to this definition")
The OK event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def OnYrSpin(self, event) -> None:
        """ 

`OnYrSpin`(*self*, *event*)[¶](#wx.lib.calendar.CalenDlg.OnYrSpin "Permalink to this definition")
The year spin control event handler.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """

    def ResetDisplay(self) -> None:
        """ 

`ResetDisplay`(*self*)[¶](#wx.lib.calendar.CalenDlg.ResetDisplay "Permalink to this definition")
Reset the display.




            Source: https://docs.wxpython.org/wx.lib.calendar.CalenDlg.html
        """



class PrtCalDraw(CalDraw):
    """ A class to optimize [`CalDraw`](wx.lib.calendar.CalDraw.html#wx.lib.calendar.CalDraw "wx.lib.calendar.CalDraw") for printing.


  


        Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
    """
    def InitValues(self) -> None:
        """ 

`InitValues`(*self*)[¶](#wx.lib.calendar.PrtCalDraw.InitValues "Permalink to this definition")
Set initial values.




            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """

    def SetPreview(self, preview: Any) -> None:
        """ 

`SetPreview`(*self*, *preview*)[¶](#wx.lib.calendar.PrtCalDraw.SetPreview "Permalink to this definition")
Set the preview.



Parameters
**preview** – set the preview state???






            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """

    def SetPSize(self, pwidth, pheight) -> None:
        """ 

`SetPSize`(*self*, *pwidth*, *pheight*)[¶](#wx.lib.calendar.PrtCalDraw.SetPSize "Permalink to this definition")
Calculate the dimensions in the center of the drawing area.




            Source: https://docs.wxpython.org/wx.lib.calendar.PrtCalDraw.html
        """



