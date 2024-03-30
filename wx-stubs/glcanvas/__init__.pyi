# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Window, VisualAttributes, Object

class GLCanvas(Window):
    """ **Possible constructors**:



```
GLCanvas(parent, dispAttrs, id=ID_ANY, pos=DefaultPosition,
         size=DefaultSize, style=0, name=GLCanvasName, palette=NullPalette)

GLCanvas(parent, id=ID_ANY, attribList=None, pos=DefaultPosition,
         size=DefaultSize, style=0, name='GLCanvas', palette=NullPalette)

```


GLCanvas is a class for displaying OpenGL graphics.


  


        Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.glcanvas.GLCanvas.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, dispAttrs, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=GLCanvasName, palette=NullPalette)*


Creates a window with the given parameters.


Notice that you need to create and use a  [wx.glcanvas.GLContext](wx.glcanvas.GLContext.html#wx-glcanvas-glcontext) to output to this window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Pointer to a parent window.
* **dispAttrs** ([*wx.glcanvas.GLAttributes*](wx.glcanvas.GLAttributes.html#wx.glcanvas.GLAttributes "wx.glcanvas.GLAttributes")) – The  [wx.glcanvas.GLAttributes](wx.glcanvas.GLAttributes.html#wx-glcanvas-glattributes) used for setting display attributes (not for rendering context attributes).
* **id** (*wx.WindowID*) – Window identifier. If -1, will automatically create an identifier.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position. DefaultPosition is (-1, -1) which indicates that wxWidgets should generate a default position for the window.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size. DefaultSize is (-1, -1) which indicates that wxWidgets should generate a default size for the window. If no suitable size can be found, the window will be sized to 20x20 pixels so that the window is visible but obviously not correctly sized.
* **style** (*long*) – Window style.
* **name** (*string*) – Window name.
* **palette** ([*wx.Palette*](wx.Palette.html#wx.Palette "wx.Palette")) – Palette for indexed colour (i.e. non `wx.glcanvas.WX_GL_RGBA`) mode. Ignored under most platforms.





New in version 4.1/wxWidgets-3.1.0.





---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, attribList=None, pos=DefaultPosition, size=DefaultSize, style=0, name=’GLCanvas’, palette=NullPalette)*




---

  





            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.glcanvas.GLCanvas.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
 [wx.VisualAttributes](wx.VisualAttributes.html#wx-visualattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def IsDisplaySupported(*args, **kw) -> bool:
        """ 

*static* `IsDisplaySupported`(*\*args*, *\*\*kw*)[¶](#wx.glcanvas.GLCanvas.IsDisplaySupported "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**IsDisplaySupported** *(dispAttrs)*


Determines if a canvas having the specified attributes is available.


This only applies for visual attributes, not rendering context attributes.



Parameters
**dispAttrs** ([*wx.glcanvas.GLAttributes*](wx.glcanvas.GLAttributes.html#wx.glcanvas.GLAttributes "wx.glcanvas.GLAttributes")) – The requested attributes.



Return type
*bool*



Returns
`True` if attributes are supported.





New in version 4.1/wxWidgets-3.1.0.





---

  



**IsDisplaySupported** *(attribList)*


Determines if a canvas having the specified attributes is available.


This only applies for visual attributes, not rendering context attributes. Please, use the new form of this method, using  [wx.glcanvas.GLAttributes](wx.glcanvas.GLAttributes.html#wx-glcanvas-glattributes).



Parameters
**attribList** (*list of integers*) – See *attribList* for  [wx.glcanvas.GLCanvas](#wx-glcanvas-glcanvas).



Return type
*bool*



Returns
`True` if attributes are supported.






---

  





            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    @staticmethod
    def IsExtensionSupported(extension: int) -> bool:
        """ 

*static* `IsExtensionSupported`(*extension*)[¶](#wx.glcanvas.GLCanvas.IsExtensionSupported "Permalink to this definition")
Returns `True` if the extension with given name is supported.


Notice that while this function is implemented for all of `GLX`, `WGL` and NSOpenGL the extensions names are usually not the same for different platforms and so the code using it still usually uses conditional compilation.



Parameters
**extension** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SetColour(self, colour: str) -> bool:
        """ 

`SetColour`(*self*, *colour*)[¶](#wx.glcanvas.GLCanvas.SetColour "Permalink to this definition")
Sets the current colour for this window (using `glcolor3f()` ), using the wxWidgets colour database to find a named colour.



Parameters
**colour** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SetCurrent(self, context: 'glcanvas.GLContext') -> bool:
        """ 

`SetCurrent`(*self*, *context*)[¶](#wx.glcanvas.GLCanvas.SetCurrent "Permalink to this definition")
Makes the OpenGL state that is represented by the OpenGL rendering context *context* current, i.e.


it will be used by all subsequent OpenGL calls.


This is equivalent to [`wx.glcanvas.GLContext.SetCurrent`](wx.glcanvas.GLContext.html#wx.glcanvas.GLContext.SetCurrent "wx.glcanvas.GLContext.SetCurrent") called with this window as parameter.



Parameters
**context** ([*wx.glcanvas.GLContext*](wx.glcanvas.GLContext.html#wx.glcanvas.GLContext "wx.glcanvas.GLContext")) – 



Return type
*bool*



Returns
`False` if an error occurred.





Note


This function may only be called when the window is shown on screen, in particular it can’t usually be called from the constructor as the window isn’t yet shown at this moment.





            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """

    def SwapBuffers(self) -> bool:
        """ 

`SwapBuffers`(*self*)[¶](#wx.glcanvas.GLCanvas.SwapBuffers "Permalink to this definition")
Swaps the double-buffer of this window, making the back-buffer the front-buffer and vice versa, so that the output of the previous OpenGL commands is displayed on the window.



Return type
*bool*



Returns
`False` if an error occurred.






            Source: https://docs.wxpython.org/wx.glcanvas.GLCanvas.html
        """



WX_GL_RGBA: int

class GLContext(Object):
    """ **Possible constructors**:



```
GLContext(win, other=None, ctxAttrs=None)

```


An instance of a GLContext represents the state of an OpenGL state
machine and the connection between OpenGL and the system.


  


        Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
    """
    def __init__(self, win, other=None, ctxAttrs=None) -> None:
        """ 

`__init__`(*self*, *win*, *other=None*, *ctxAttrs=None*)[¶](#wx.glcanvas.GLContext.__init__ "Permalink to this definition")
Constructor.



Parameters
* **win** ([*wx.glcanvas.GLCanvas*](wx.glcanvas.GLCanvas.html#wx.glcanvas.GLCanvas "wx.glcanvas.GLCanvas")) – The canvas that is used to initialize this context. This parameter is needed only temporarily, and the caller may do anything with it (e.g. destroy the window) after the constructor returned.
It will be possible to bind (make current) this context to any other  [wx.glcanvas.GLCanvas](wx.glcanvas.GLCanvas.html#wx-glcanvas-glcanvas) that has been created with equivalent attributes as win.
* **other** ([*wx.glcanvas.GLContext*](#wx.glcanvas.GLContext "wx.glcanvas.GLContext")) – Context to share some data with or `None` (the default) for no sharing.
* **ctxAttrs** ([*wx.glcanvas.GLContextAttrs*](wx.glcanvas.GLContextAttrs.html#wx.glcanvas.GLContextAttrs "wx.glcanvas.GLContextAttrs")) – A  [wx.glcanvas.GLContextAttrs](wx.glcanvas.GLContextAttrs.html#wx-glcanvas-glcontextattrs) pointer to the attributes used for defining the flags when `OGL` >= 3.2 is requested. This is the preferred method since wxWidgets 3.1.0. The previous method (still available for backwards compatibility) is to define the attributes at  [wx.glcanvas.GLCanvas](wx.glcanvas.GLCanvas.html#wx-glcanvas-glcanvas) constructor. If this parameter is `None` (the default) then that previous method is taken. If no attributes are defined at all, then those provided by the `GPU` driver defaults will be used.






            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """

    def IsOK(self) -> bool:
        """ 

`IsOK`(*self*)[¶](#wx.glcanvas.GLContext.IsOK "Permalink to this definition")
Checks if the underlying OpenGL rendering context was correctly created by the system with the requested attributes.


If this function returns `False` then the  [wx.glcanvas.GLContext](#wx-glcanvas-glcontext) object is useless and should be deleted and recreated with different attributes.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """

    def SetCurrent(self, win: 'glcanvas.GLCanvas') -> bool:
        """ 

`SetCurrent`(*self*, *win*)[¶](#wx.glcanvas.GLContext.SetCurrent "Permalink to this definition")
Makes the OpenGL state that is represented by this rendering context current with the  [wx.glcanvas.GLCanvas](wx.glcanvas.GLCanvas.html#wx-glcanvas-glcanvas) *win*.



Parameters
**win** ([*wx.glcanvas.GLCanvas*](wx.glcanvas.GLCanvas.html#wx.glcanvas.GLCanvas "wx.glcanvas.GLCanvas")) – 



Return type
*bool*





Note


*win* can be a different  [wx.glcanvas.GLCanvas](wx.glcanvas.GLCanvas.html#wx-glcanvas-glcanvas) window than the one that was passed to the constructor of this rendering context. If `RC` is an object of type  [wx.glcanvas.GLContext](#wx-glcanvas-glcontext), the statements *“RC.SetCurrent(win);”* and *“win.SetCurrent(RC);”* are equivalent, see [`wx.glcanvas.GLCanvas.SetCurrent`](wx.glcanvas.GLCanvas.html#wx.glcanvas.GLCanvas.SetCurrent "wx.glcanvas.GLCanvas.SetCurrent") .





            Source: https://docs.wxpython.org/wx.glcanvas.GLContext.html
        """



class GLAttributes(GLAttribsBase):
    """ This class is used for setting display attributes when drawing through
OpenGL (“Pixel format” in MSW and OSX parlance, “Configs” in X11).


  


        Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
    """
    def AuxBuffers(self, val: int) -> 'GLAttributes':
        """ 

`AuxBuffers`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.AuxBuffers "Permalink to this definition")
Specifies the number of auxiliary buffers.



Parameters
**val** (*int*) – The number of auxiliary buffers.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def BufferSize(self, val: int) -> 'GLAttributes':
        """ 

`BufferSize`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.BufferSize "Permalink to this definition")
Specifies the number of bits for colour buffer.


For `RGBA` it’s normally the sum of the bits per each component.



Parameters
**val** (*int*) – The number of bits.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Defaults(self) -> 'GLAttributes':
        """ 

`Defaults`(*self*)[¶](#wx.glcanvas.GLAttributes.Defaults "Permalink to this definition")
wxWidgets defaults: `RGBA`, Z-depth 16 bits, double buffering, 1 sample buffer, 4 samplers.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)





See also


[`PlatformDefaults`](#wx.glcanvas.GLAttributes.PlatformDefaults "wx.glcanvas.GLAttributes.PlatformDefaults")





            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Depth(self, val: int) -> 'GLAttributes':
        """ 

`Depth`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.Depth "Permalink to this definition")
Specifies number of bits for Z-buffer.



Parameters
**val** (*int*) – Number of bits for Z-buffer (typically 0, 16 or 32).



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def DoubleBuffer(self) -> 'GLAttributes':
        """ 

`DoubleBuffer`(*self*)[¶](#wx.glcanvas.GLAttributes.DoubleBuffer "Permalink to this definition")
Requests using double buffering.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def EndList(self) -> None:
        """ 

`EndList`(*self*)[¶](#wx.glcanvas.GLAttributes.EndList "Permalink to this definition")
The set of attributes must end with this one; otherwise, the `GPU` may display nothing at all.




            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def FrameBuffersRGB(self) -> 'GLAttributes':
        """ 

`FrameBuffersRGB`(*self*)[¶](#wx.glcanvas.GLAttributes.FrameBuffersRGB "Permalink to this definition")
Used to request a frame buffer sRGB capable.


It makes no effect for macOS.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Level(self, val: int) -> 'GLAttributes':
        """ 

`Level`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.Level "Permalink to this definition")
Specifies the framebuffer level.


It makes no effect for macOS.



Parameters
**val** (*int*) – 0 for main buffer, >0 for overlay, <0 for underlay.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def MinAcumRGBA(self, mRed, mGreen, mBlue, mAlpha) -> 'GLAttributes':
        """ 

`MinAcumRGBA`(*self*, *mRed*, *mGreen*, *mBlue*, *mAlpha*)[¶](#wx.glcanvas.GLAttributes.MinAcumRGBA "Permalink to this definition")
Specifies the minimal number of bits for each accumulator channel.


On MSW and OSX this function also sets the size of the accumulation buffer.



Parameters
* **mRed** (*int*) – The minimal number of bits for red accumulator.
* **mGreen** (*int*) – The minimal number of bits for green accumulator.
* **mBlue** (*int*) – The minimal number of bits for blue accumulator.
* **mAlpha** (*int*) – The minimal number of bits for alpha accumulator.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def MinRGBA(self, mRed, mGreen, mBlue, mAlpha) -> 'GLAttributes':
        """ 

`MinRGBA`(*self*, *mRed*, *mGreen*, *mBlue*, *mAlpha*)[¶](#wx.glcanvas.GLAttributes.MinRGBA "Permalink to this definition")
Specifies the minimal number of bits for each colour and alpha.


On MSW and OSX this function also sets the size of the colour buffer.



Parameters
* **mRed** (*int*) – The minimal number of bits for colour red.
* **mGreen** (*int*) – The minimal number of bits for colour green.
* **mBlue** (*int*) – The minimal number of bits for colour blue.
* **mAlpha** (*int*) – The minimal number of bits for alpha channel.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def PlatformDefaults(self) -> 'GLAttributes':
        """ 

`PlatformDefaults`(*self*)[¶](#wx.glcanvas.GLAttributes.PlatformDefaults "Permalink to this definition")
Set some typically needed attributes.


E.g. full-acceleration on MSW.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)





See also


[`Defaults`](#wx.glcanvas.GLAttributes.Defaults "wx.glcanvas.GLAttributes.Defaults")





            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def RGBA(self) -> 'GLAttributes':
        """ 

`RGBA`(*self*)[¶](#wx.glcanvas.GLAttributes.RGBA "Permalink to this definition")
Use `True` colour instead of colour index rendering for each pixel.


It makes no effect for macOS.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def SampleBuffers(self, val: int) -> 'GLAttributes':
        """ 

`SampleBuffers`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.SampleBuffers "Permalink to this definition")
Use multi-sampling support (antialiasing).



Parameters
**val** (*int*) – Number of sample buffers, usually 1.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Samplers(self, val: int) -> 'GLAttributes':
        """ 

`Samplers`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.Samplers "Permalink to this definition")
Specifies the number of samplers per pixel.



Parameters
**val** (*int*) – Number of samplers, e.g. 4 for 2x2 antialiasing.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Stencil(self, val: int) -> 'GLAttributes':
        """ 

`Stencil`(*self*, *val*)[¶](#wx.glcanvas.GLAttributes.Stencil "Permalink to this definition")
Specifies number of bits for stencil buffer.



Parameters
**val** (*int*) – Number of bits.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """

    def Stereo(self) -> 'GLAttributes':
        """ 

`Stereo`(*self*)[¶](#wx.glcanvas.GLAttributes.Stereo "Permalink to this definition")
Use stereoscopic display.



Return type
 [wx.glcanvas.GLAttributes](#wx-glcanvas-glattributes)






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttributes.html
        """



class GLContextAttrs(GLAttribsBase):
    """ This class is used for setting context attributes.


  


        Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
    """
    def CompatibilityProfile(self) -> 'GLContextAttrs':
        """ 

`CompatibilityProfile`(*self*)[¶](#wx.glcanvas.GLContextAttrs.CompatibilityProfile "Permalink to this definition")
Request a type of context with all OpenGL features from version 1.0 to the newest available by the `GPU` driver.


In this mode the `GPU` may be some slower than it would be without this compatibility attribute.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def CoreProfile(self) -> 'GLContextAttrs':
        """ 

`CoreProfile`(*self*)[¶](#wx.glcanvas.GLContextAttrs.CoreProfile "Permalink to this definition")
Request an OpenGL core profile for the context.


If the requested OpenGL version is less than 3.2, this attribute is ignored and the functionality of the context is determined solely by the requested version.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def DebugCtx(self) -> 'GLContextAttrs':
        """ 

`DebugCtx`(*self*)[¶](#wx.glcanvas.GLContextAttrs.DebugCtx "Permalink to this definition")
Request debugging functionality.


This tells OpenGL to prepare a set where some logs are enabled and also allows `OGL` to send debug messages through a callback function.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ES2(self) -> 'GLContextAttrs':
        """ 

`ES2`(*self*)[¶](#wx.glcanvas.GLContextAttrs.ES2 "Permalink to this definition")
Request an `ES` or `ES2` (“Embedded Subsystem”) context.


These are special subsets of OpenGL, lacking some features of the full specification. Used mainly in embedded devices such as mobile phones.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def EndList(self) -> None:
        """ 

`EndList`(*self*)[¶](#wx.glcanvas.GLContextAttrs.EndList "Permalink to this definition")
The set of attributes must end with this one; otherwise, the `GPU` may display nothing at all.




            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ForwardCompatible(self) -> 'GLContextAttrs':
        """ 

`ForwardCompatible`(*self*)[¶](#wx.glcanvas.GLContextAttrs.ForwardCompatible "Permalink to this definition")
Request a forward-compatible context.


Forward-compatible contexts are defined only for OpenGL versions 3.0 and later. They must not support functionality marked as deprecated or removed by the requested version of the OpenGL API.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def LoseOnReset(self) -> 'GLContextAttrs':
        """ 

`LoseOnReset`(*self*)[¶](#wx.glcanvas.GLContextAttrs.LoseOnReset "Permalink to this definition")
With robustness enabled, if graphics reset happens, all context state is lost.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def MajorVersion(self, val: int) -> 'GLContextAttrs':
        """ 

`MajorVersion`(*self*, *val*)[¶](#wx.glcanvas.GLContextAttrs.MajorVersion "Permalink to this definition")
Request specific OpenGL core major version number (>= 3).



Parameters
**val** (*int*) – The major version number requested.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)




[`CoreProfile`](#wx.glcanvas.GLContextAttrs.CoreProfile "wx.glcanvas.GLContextAttrs.CoreProfile") will result in using OpenGL version at least 3.2.




            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def MinorVersion(self, val: int) -> 'GLContextAttrs':
        """ 

`MinorVersion`(*self*, *val*)[¶](#wx.glcanvas.GLContextAttrs.MinorVersion "Permalink to this definition")
Request specific OpenGL core minor version number.



Parameters
**val** (*int*) – The minor version number requested, e.g. 2 if OpenGL 3.2 is requested.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)




[`CoreProfile`](#wx.glcanvas.GLContextAttrs.CoreProfile "wx.glcanvas.GLContextAttrs.CoreProfile") will result in using OpenGL version at least 3.2.




            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def NoResetNotify(self) -> 'GLContextAttrs':
        """ 

`NoResetNotify`(*self*)[¶](#wx.glcanvas.GLContextAttrs.NoResetNotify "Permalink to this definition")
With robustness enabled, never deliver notification of reset events.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def OGLVersion(self, vmayor, vminor) -> 'GLContextAttrs':
        """ 

`OGLVersion`(*self*, *vmayor*, *vminor*)[¶](#wx.glcanvas.GLContextAttrs.OGLVersion "Permalink to this definition")
An easy way of requesting an OpenGL version.



Parameters
* **vmayor** (*int*) – The major version number requested, e.g. 4 if OpenGL 4.5 is requested.
* **vminor** (*int*) – The minor version number requested, e.g. 5 if OpenGL 4.5 is requested.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)




[`CoreProfile`](#wx.glcanvas.GLContextAttrs.CoreProfile "wx.glcanvas.GLContextAttrs.CoreProfile") will result in using OpenGL version at least 3.2.




            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def PlatformDefaults(self) -> 'GLContextAttrs':
        """ 

`PlatformDefaults`(*self*)[¶](#wx.glcanvas.GLContextAttrs.PlatformDefaults "Permalink to this definition")
Set platform specific defaults.


Currently only Unix defaults are implemented: use X11 direct rendering and use X11 `RGBA` type.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ReleaseFlush(self, val: int=1) -> 'GLContextAttrs':
        """ 

`ReleaseFlush`(*self*, *val=1*)[¶](#wx.glcanvas.GLContextAttrs.ReleaseFlush "Permalink to this definition")
Request OpenGL to avoid or not flushing pending commands when the context is made no longer current (released).


If you don’t specify this attribute, the `GPU` driver default is ‘flushing’.



Parameters
**val** (*int*) – 0 for not flushing, 1 (wxWidgets default) for flushing pending commands.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def ResetIsolation(self) -> 'GLContextAttrs':
        """ 

`ResetIsolation`(*self*)[¶](#wx.glcanvas.GLContextAttrs.ResetIsolation "Permalink to this definition")
Request OpenGL to protect other applications or shared contexts from reset side-effects.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """

    def Robust(self) -> 'GLContextAttrs':
        """ 

`Robust`(*self*)[¶](#wx.glcanvas.GLContextAttrs.Robust "Permalink to this definition")
Request robustness, or how OpenGL handles out-of-bounds buffer object accesses and graphics reset notification behaviours.


It has no effect under macOS.



Return type
 [wx.glcanvas.GLContextAttrs](#wx-glcanvas-glcontextattrs)






            Source: https://docs.wxpython.org/wx.glcanvas.GLContextAttrs.html
        """



class GLAttribsBase:
    """ **Possible constructors**:



```
GLAttribsBase()

```


This is the base class for GLAttributes and GLContextAttrs.


  


        Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.glcanvas.GLAttribsBase.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def AddAttribBits(self, searchVal, combineVal) -> None:
        """ 

`AddAttribBits`(*self*, *searchVal*, *combineVal*)[¶](#wx.glcanvas.GLAttribsBase.AddAttribBits "Permalink to this definition")
Combine (bitwise `wx.OR`) a given value with the existing one, if any.


This function first searches for an identifier and then combines the given value with the value right after the identifier. If the identifier is not found, two new values (i.e. the identifier and the given value) are added to the list.



Parameters
* **searchVal** (*int*) – The identifier to search for.
* **combineVal** (*int*) – The value to combine with the existing one.






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def AddAttribute(self, attribute: int) -> None:
        """ 

`AddAttribute`(*self*, *attribute*)[¶](#wx.glcanvas.GLAttribsBase.AddAttribute "Permalink to this definition")
Adds an integer value to the list of attributes.



Parameters
**attribute** (*int*) – The value to add.






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def GetSize(self) -> int:
        """ 

`GetSize`(*self*)[¶](#wx.glcanvas.GLAttribsBase.GetSize "Permalink to this definition")
Returns the size of the internal list of attributes.


Remember that the last value in the list must be a ‘0’ (zero). So, a minimal list is of size = 2, the first value is meaningful and the last is ‘0’.



Return type
*int*






            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def NeedsARB(self) -> bool:
        """ 

`NeedsARB`(*self*)[¶](#wx.glcanvas.GLAttribsBase.NeedsARB "Permalink to this definition")
Returns the current value of the ARB-flag.



Return type
*bool*





See also


[`SetNeedsARB`](#wx.glcanvas.GLAttribsBase.SetNeedsARB "wx.glcanvas.GLAttribsBase.SetNeedsARB")





            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.glcanvas.GLAttribsBase.Reset "Permalink to this definition")
Delete contents and sets ARB-flag to `False`.




            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    def SetNeedsARB(self, needsARB: bool=True) -> None:
        """ 

`SetNeedsARB`(*self*, *needsARB=True*)[¶](#wx.glcanvas.GLAttribsBase.SetNeedsARB "Permalink to this definition")
Sets the necessity of using special ARB-functions (e.g.


wglCreateContextAttribsARB in MSW) for some of the attributes of the list. Multi-sampling and modern context require these ARB-functions.



Parameters
**needsARB** (*bool*) – `True` if an ARB-function is needed for any of the attributes.





See also


[`NeedsARB`](#wx.glcanvas.GLAttribsBase.NeedsARB "wx.glcanvas.GLAttribsBase.NeedsARB")





            Source: https://docs.wxpython.org/wx.glcanvas.GLAttribsBase.html
        """

    Size: int  # `Size`[¶](#wx.glcanvas.GLAttribsBase.Size "Permalink to this definition")See [`GetSize`](#wx.glcanvas.GLAttribsBase.GetSize "wx.glcanvas.GLAttribsBase.GetSize")



OR: int

