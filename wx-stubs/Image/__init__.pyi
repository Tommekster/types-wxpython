# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias


class HSVValue:
    """ **Possible constructors**:



```
HSVValue(h=0.0, s=0.0, v=0.0)

```


A simple class which stores hue, saturation and value as doubles in
the range 0.0-1.0.


  


        Source: https://docs.wxpython.org/wx.Image.HSVValue.html
    """
    def __init__(self, h=0.0, s=0.0, v=0.0) -> None:
        """ 

`__init__`(*self*, *h=0.0*, *s=0.0*, *v=0.0*)[¶](#wx.Image.HSVValue.__init__ "Permalink to this definition")
Constructor for  [wx.Image.HSVValue](#wx-image-hsvvalue), an object that contains values for hue, saturation and value which represent the value of a color.


It is used by [`wx.Image.HSVtoRGB`](wx.Image.html#wx.Image.HSVtoRGB "wx.Image.HSVtoRGB") and [`wx.Image.RGBtoHSV`](wx.Image.html#wx.Image.RGBtoHSV "wx.Image.RGBtoHSV") , which convert between `HSV` color space and `RGB` color space.



Parameters
* **h** (*float*) –
* **s** (*float*) –
* **v** (*float*) –






            Source: https://docs.wxpython.org/wx.Image.HSVValue.html
        """

    hue: Any  # `hue`[¶](#wx.Image.HSVValue.hue "Permalink to this definition")A public C++ attribute of type `float`.
    saturation: Any  # `saturation`[¶](#wx.Image.HSVValue.saturation "Permalink to this definition")A public C++ attribute of type `float`.
    value: Any  # `value`[¶](#wx.Image.HSVValue.value "Permalink to this definition")A public C++ attribute of type `float`.



class RGBValue:
    """ **Possible constructors**:



```
RGBValue(r=0, g=0, b=0)

```



A simple class which stores red, green and blue values as 8 bitintegers in the range of `0-255`.




  


        Source: https://docs.wxpython.org/wx.Image.RGBValue.html
    """
    def __init__(self, r=0, g=0, b=0) -> None:
        """ 

`__init__`(*self*, *r=0*, *g=0*, *b=0*)[¶](#wx.Image.RGBValue.__init__ "Permalink to this definition")
Constructor for  [wx.Image.RGBValue](#wx-image-rgbvalue), an object that contains values for red, green and blue which represent the value of a color.


It is used by [`wx.Image.HSVtoRGB`](wx.Image.html#wx.Image.HSVtoRGB "wx.Image.HSVtoRGB") and [`wx.Image.RGBtoHSV`](wx.Image.html#wx.Image.RGBtoHSV "wx.Image.RGBtoHSV") , which convert between `HSV` color space and `RGB` color space.



Parameters
* **r** (*int*) –
* **g** (*int*) –
* **b** (*int*) –






            Source: https://docs.wxpython.org/wx.Image.RGBValue.html
        """

    blue: Any  # `blue`[¶](#wx.Image.RGBValue.blue "Permalink to this definition")A public C++ attribute of type `int`.
    green: Any  # `green`[¶](#wx.Image.RGBValue.green "Permalink to this definition")A public C++ attribute of type `int`.
    red: Any  # `red`[¶](#wx.Image.RGBValue.red "Permalink to this definition")A public C++ attribute of type `int`.



