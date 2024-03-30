# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import WeekDay

class TimeZone:
    """ **Possible constructors**:



```
TimeZone(tz)

TimeZone(offset=0)

```


Class representing a time zone.


  


        Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.DateTime.TimeZone.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, tz)*


Constructor for a named time zone.



Parameters
**tz** (*DateTime.TZ*) – 






---

  



**\_\_init\_\_** *(self, offset=0)*


Constructor for the given offset in seconds.



Parameters
**offset** (*long*) – 






---

  





            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    def GetOffset(self) -> int:
        """ 

`GetOffset`(*self*)[¶](#wx.DateTime.TimeZone.GetOffset "Permalink to this definition")
Return the offset of this time zone from `UTC`, in seconds.



Return type
*long*






            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    def IsLocal(self) -> bool:
        """ 

`IsLocal`(*self*)[¶](#wx.DateTime.TimeZone.IsLocal "Permalink to this definition")
Return `True` if this is the local time zone.


This method can be useful for distinguishing between `UTC` time zone and local time zone in Great Britain, which use the same offset as `UTC` (i.e. 0), but do use `DST`.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.1.





            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    @staticmethod
    def Make(offset: int) -> 'TimeZone':
        """ 

*static* `Make`(*offset*)[¶](#wx.DateTime.TimeZone.Make "Permalink to this definition")
Create a time zone with the given offset in seconds.



Parameters
**offset** (*long*) – 



Return type
 [wx.DateTime.TimeZone](#wx-datetime-timezone)






            Source: https://docs.wxpython.org/wx.DateTime.TimeZone.html
        """

    Offset: int  # `Offset`[¶](#wx.DateTime.TimeZone.Offset "Permalink to this definition")See [`GetOffset`](#wx.DateTime.TimeZone.GetOffset "wx.DateTime.TimeZone.GetOffset")



class Tm:
    """ Contains broken down date-time representation.


  


        Source: https://docs.wxpython.org/wx.DateTime.Tm.html
    """
    def GetWeekDay(self) -> 'WeekDay':
        """ 

`GetWeekDay`(*self*)[¶](#wx.DateTime.Tm.GetWeekDay "Permalink to this definition")
Return the week day corresponding to this date.


Unlike the other fields, the week day is not always available and so must be accessed using this method as it is computed on demand when it is called.



Return type
 [wx.DateTime.WeekDay](wx.DateTime.WeekDay.enumeration.html#wx-datetime-weekday)






            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.DateTime.Tm.IsValid "Permalink to this definition")
Check if the given date/time is valid (in Gregorian calendar).


Return `False` if the components don’t correspond to a correct date.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.DateTime.Tm.html
        """

    WeekDay: 'WeekDay'  # `WeekDay`[¶](#wx.DateTime.Tm.WeekDay "Permalink to this definition")See [`GetWeekDay`](#wx.DateTime.Tm.GetWeekDay "wx.DateTime.Tm.GetWeekDay")
    hour: Any  # `hour`[¶](#wx.DateTime.Tm.hour "Permalink to this definition")A public C++ attribute of type `int`. Hours since midnight in 0..23 range.
    mday: Any  # `mday`[¶](#wx.DateTime.Tm.mday "Permalink to this definition")A public C++ attribute of type `int`. Day of the month in 1..31 range.
    min: Any  # `min`[¶](#wx.DateTime.Tm.min "Permalink to this definition")A public C++ attribute of type `int`. Minutes in 0..59 range.
    mon: Any  # `mon`[¶](#wx.DateTime.Tm.mon "Permalink to this definition")A public C++ attribute of type `DateTime.Month`. Month, as an enumerated constant.
    msec: Any  # `msec`[¶](#wx.DateTime.Tm.msec "Permalink to this definition")A public C++ attribute of type `int`. Number of milliseconds.
    sec: Any  # `sec`[¶](#wx.DateTime.Tm.sec "Permalink to this definition")A public C++ attribute of type `int`. Seconds in 0..59 (60 with leap seconds) range.
    yday: Any  # `yday`[¶](#wx.DateTime.Tm.yday "Permalink to this definition")A public C++ attribute of type `int`. Day of the year in 0..365 range.
    year: Any  # `year`[¶](#wx.DateTime.Tm.year "Permalink to this definition")A public C++ attribute of type `int`. Year.



Country: TypeAlias = int  # Enumeration

WeekFlags: TypeAlias = int  # Enumeration

Month: TypeAlias = Any  # Enumeration

TZ: TypeAlias = Any

