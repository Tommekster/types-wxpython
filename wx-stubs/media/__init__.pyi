# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Control, Size, FileOffset, NotifyEvent

class MediaCtrl(Control):
    """ **Possible constructors**:



```
MediaCtrl()

MediaCtrl(parent, id=-1, fileName="", pos=DefaultPosition,
          size=DefaultSize, style=0, szBackend="", validator=DefaultValidator,
          name="mediaCtrl")

```


MediaCtrl is a class for displaying various types of media, such as
videos, audio files, natively through native codecs.


  


        Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.media.MediaCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor - you `MUST` call [`Create`](#wx.media.MediaCtrl.Create "wx.media.MediaCtrl.Create") before calling any other methods of  [wx.media.MediaCtrl](#wx-media-mediactrl).




---

  



**\_\_init\_\_** *(self, parent, id=-1, fileName=””, pos=DefaultPosition, size=DefaultSize, style=0, szBackend=””, validator=DefaultValidator, name=”mediaCtrl”)*


Constructor that calls [`Create`](#wx.media.MediaCtrl.Create "wx.media.MediaCtrl.Create") .


You may prefer to call [`Create`](#wx.media.MediaCtrl.Create "wx.media.MediaCtrl.Create") directly to check to see if  [wx.media.MediaCtrl](#wx-media-mediactrl) is available on the system.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent of this control. Must not be `None`.
* **id** (*wx.WindowID*) – id to use for events
* **fileName** (*string*) – If not empty, the path of a file to open.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position to put control at.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Size to put the control at and to stretch movie to.
* **style** (*long*) – Optional styles. It is recommended to use `MC_NO_AUTORESIZE`, although it is not used by default for compatibility reasons.
* **szBackend** (*string*) – Name of backend you want to use, leave blank to make  [wx.media.MediaCtrl](#wx-media-mediactrl) figure it out.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – validator to use.
* **name** (*string*) – Window name.






---

  





            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Create(self, parent, id=-1, fileName="", pos=DefaultPosition, size=DefaultSize, style=0, szBackend="", validator=DefaultValidator, name="mediaCtrl") -> bool:
        """ 

`Create`(*self*, *parent*, *id=-1*, *fileName=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *szBackend=""*, *validator=DefaultValidator*, *name="mediaCtrl"*)[¶](#wx.media.MediaCtrl.Create "Permalink to this definition")
Creates this control.


Returns `False` if it can’t load the media located at *fileName* or it can’t create a backend.


If you specify a file to open via *fileName* and you don’t specify a backend to use,  [wx.media.MediaCtrl](#wx-media-mediactrl) tries each of its backends until one that can render the path referred to by *fileName* can be found.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – parent of this control. Must not be `None`.
* **id** (*wx.WindowID*) – id to use for events
* **fileName** (*string*) – If not empty, the path of a file to open.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position to put control at.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Size to put the control at and to stretch movie to.
* **style** (*long*) – Optional styles. It is recommended to use `MC_NO_AUTORESIZE`, although it is not used by default for compatibility reasons.
* **szBackend** (*string*) – Name of backend you want to use, leave blank to make  [wx.media.MediaCtrl](#wx-media-mediactrl) figure it out.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – validator to use.
* **name** (*string*) – Window name.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetBestSize(self) -> 'Size':
        """ 

`GetBestSize`(*self*)[¶](#wx.media.MediaCtrl.GetBestSize "Permalink to this definition")
Obtains the best size relative to the original/natural size of the video, if there is any.


See [Video size](#wx-media-mediactrl) for more information.



Return type
`Size`






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetPlaybackRate(self) -> float:
        """ 

`GetPlaybackRate`(*self*)[¶](#wx.media.MediaCtrl.GetPlaybackRate "Permalink to this definition")
Obtains the playback rate, or speed of the media.



> `1.0` represents normal speed, while `2.0` represents twice the normal speed of the media, for example. Not supported on the GStreamer (Unix) backend.



Return type
*float*



Returns
zero on failure.






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetState(self) -> 'MediaState':
        """ 

`GetState`(*self*)[¶](#wx.media.MediaCtrl.GetState "Permalink to this definition")
Obtains the state the playback of the media is in.







| `wx.media.MEDIASTATE_STOPPED` | The media has stopped. |
| --- | --- |
| `wx.media.MEDIASTATE_PAUSED` | The media is paused. |
| `wx.media.MEDIASTATE_PLAYING` | The media is currently playing. |



  



Return type
 [wx.media.MediaState](wx.media.MediaState.enumeration.html#wx-media-mediastate)






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def GetVolume(self) -> float:
        """ 

`GetVolume`(*self*)[¶](#wx.media.MediaCtrl.GetVolume "Permalink to this definition")
Gets the volume of the media from a 0.0 to 1.0 range.



Return type
*float*





Note


Due to rounding and other errors the value returned may not be the exact value sent to [`SetVolume`](#wx.media.MediaCtrl.SetVolume "wx.media.MediaCtrl.SetVolume") .





            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Length(self) -> 'FileOffset':
        """ 

`Length`(*self*)[¶](#wx.media.MediaCtrl.Length "Permalink to this definition")
Obtains the length - the total amount of time the media has in milliseconds.



Return type
*wx.FileOffset*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Load(self, fileName: str) -> bool:
        """ 

`Load`(*self*, *fileName*)[¶](#wx.media.MediaCtrl.Load "Permalink to this definition")
Loads the file that fileName refers to.


Returns `False` if loading fails.



Parameters
**fileName** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def LoadURI(self, uri: str) -> bool:
        """ 

`LoadURI`(*self*, *uri*)[¶](#wx.media.MediaCtrl.LoadURI "Permalink to this definition")
Loads the location that uri refers to.


Note that this is very implementation-dependent, although `HTTP` URI/URLs are generally supported, for example. Returns `False` if loading fails.



Parameters
**uri** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def LoadURIWithProxy(self, uri, proxy) -> bool:
        """ 

`LoadURIWithProxy`(*self*, *uri*, *proxy*)[¶](#wx.media.MediaCtrl.LoadURIWithProxy "Permalink to this definition")
Loads the location that `uri` refers to with the proxy `proxy` .


Not implemented on most backends so it should be called with caution. Returns `False` if loading fails.



Parameters
* **uri** (*string*) –
* **proxy** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Pause(self) -> bool:
        """ 

`Pause`(*self*)[¶](#wx.media.MediaCtrl.Pause "Permalink to this definition")
Pauses playback of the media.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Play(self) -> bool:
        """ 

`Play`(*self*)[¶](#wx.media.MediaCtrl.Play "Permalink to this definition")
Resumes playback of the media.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Seek(self, where, mode=FromStart) -> 'FileOffset':
        """ 

`Seek`(*self*, *where*, *mode=FromStart*)[¶](#wx.media.MediaCtrl.Seek "Permalink to this definition")
Seeks to a position within the media.



Parameters
* **where** (*wx.FileOffset*) –
* **mode** ([*SeekMode*](wx.SeekMode.enumeration.html "SeekMode")) –



Return type
*wx.FileOffset*





Todo


Document the SeekMode parameter *mode*, and perhaps also the FileOffset and SeekMode themselves.





            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def SetPlaybackRate(self, dRate: float) -> bool:
        """ 

`SetPlaybackRate`(*self*, *dRate*)[¶](#wx.media.MediaCtrl.SetPlaybackRate "Permalink to this definition")
Sets the playback rate, or speed of the media, to that referred by *dRate*.



> `1.0` represents normal speed, while `2.0` represents twice the normal speed of the media, for example. Not supported on the GStreamer (Unix) backend. Returns `True` if successful.



Parameters
**dRate** (*float*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def SetVolume(self, dVolume: float) -> bool:
        """ 

`SetVolume`(*self*, *dVolume*)[¶](#wx.media.MediaCtrl.SetVolume "Permalink to this definition")
Sets the volume of the media from a 0.0 to 1.0 range to that referred by `dVolume` .



> `1.0` represents full volume, while `0.5` represents half (50 percent) volume, for example.



Parameters
**dVolume** (*float*) – 



Return type
*bool*





Note


The volume may not be exact due to conversion and rounding errors, although setting the volume to full or none is always exact. Returns `True` if successful.





            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def ShowPlayerControls(self, flags: MediaCtrlPlayerControls=MEDIACTRLPLAYERCONTROLS_DEFAULT) -> bool:
        """ 

`ShowPlayerControls`(*self*, *flags=MEDIACTRLPLAYERCONTROLS\_DEFAULT*)[¶](#wx.media.MediaCtrl.ShowPlayerControls "Permalink to this definition")
A special feature to  [wx.media.MediaCtrl](#wx-media-mediactrl).


Applications using native toolkits such as QuickTime usually have a scrollbar, play button, and more provided to them by the toolkit. By default  [wx.media.MediaCtrl](#wx-media-mediactrl) does not do this. However, on the DirectShow and QuickTime backends you can show or hide the native controls provided by the underlying toolkit at will using [`ShowPlayerControls`](#wx.media.MediaCtrl.ShowPlayerControls "wx.media.MediaCtrl.ShowPlayerControls") . Simply calling the function with default parameters tells  [wx.media.MediaCtrl](#wx-media-mediactrl) to use the default controls provided by the toolkit. The function takes a MediaCtrlPlayerControls enumeration, please see available show modes there.


For more info see [Player controls](#wx-media-mediactrl).


Currently only implemented on the QuickTime and DirectShow backends. The function returns `True` on success.



Parameters
**flags** ([*MediaCtrlPlayerControls*](wx.media.MediaCtrlPlayerControls.enumeration.html "MediaCtrlPlayerControls")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Stop(self) -> bool:
        """ 

`Stop`(*self*)[¶](#wx.media.MediaCtrl.Stop "Permalink to this definition")
Stops the media.


See *Operation* for an overview of how stopping works.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    def Tell(self) -> 'FileOffset':
        """ 

`Tell`(*self*)[¶](#wx.media.MediaCtrl.Tell "Permalink to this definition")
Obtains the current position in time within the media in milliseconds.



Return type
*wx.FileOffset*






            Source: https://docs.wxpython.org/wx.media.MediaCtrl.html
        """

    BestSize: 'Size'  # `BestSize`[¶](#wx.media.MediaCtrl.BestSize "Permalink to this definition")See [`GetBestSize`](#wx.media.MediaCtrl.GetBestSize "wx.media.MediaCtrl.GetBestSize")
    PlaybackRate: float  # `PlaybackRate`[¶](#wx.media.MediaCtrl.PlaybackRate "Permalink to this definition")See [`GetPlaybackRate`](#wx.media.MediaCtrl.GetPlaybackRate "wx.media.MediaCtrl.GetPlaybackRate") and [`SetPlaybackRate`](#wx.media.MediaCtrl.SetPlaybackRate "wx.media.MediaCtrl.SetPlaybackRate")
    State: 'MediaState'  # `State`[¶](#wx.media.MediaCtrl.State "Permalink to this definition")See [`GetState`](#wx.media.MediaCtrl.GetState "wx.media.MediaCtrl.GetState")
    Volume: float  # `Volume`[¶](#wx.media.MediaCtrl.Volume "Permalink to this definition")See [`GetVolume`](#wx.media.MediaCtrl.GetVolume "wx.media.MediaCtrl.GetVolume") and [`SetVolume`](#wx.media.MediaCtrl.SetVolume "wx.media.MediaCtrl.SetVolume")



MC_NO_AUTORESIZE: int  # By default, the control will automatically adjust its size to exactly fit the size of a loaded video as soon as a video is loaded. If this flag is given, the control will not change its size automatically and it must be done manually (if desired) using Layout. It is strongly recommended to use this flag and handle control resizing manually (note that this style is only available in wxWidgets 3.1.6, so it is only possible to do it when using this or later version). ^^

MEDIASTATE_STOPPED: int

MEDIASTATE_PAUSED: int

MEDIASTATE_PLAYING: int

class MediaEvent(NotifyEvent):
    """ **Possible constructors**:



```
MediaEvent(commandType=wxEVT_NULL, winid=0)

```


Event MediaCtrl uses.


  


        Source: https://docs.wxpython.org/wx.media.MediaEvent.html
    """
    def __init__(self, commandType=wxEVT_NULL, winid=0) -> None:
        """ 

`__init__`(*self*, *commandType=wxEVT\_NULL*, *winid=0*)[¶](#wx.media.MediaEvent.__init__ "Permalink to this definition")
Default constructor.



Parameters
* **commandType** (*wx.EventType*) –
* **winid** (*int*) –






            Source: https://docs.wxpython.org/wx.media.MediaEvent.html
        """



EVT_MEDIA_LOADED: int  # Sent when a media has loaded enough data that it can start playing. Processes a  wxEVT_MEDIA_LOADED   event type.

EVT_MEDIA_STOP: int  # Sent when a media has switched to the  MEDIASTATE_STOPPED   state. You may be able to Veto this event to prevent it from stopping, causing it to continue playing - even if it has reached that end of the media (note that this may not have the desired effect - if you want to loop the media, for example, catch the   EVT_MEDIA_FINISHED   and play there instead). Processes a   wxEVT_MEDIA_STOP   event type.

EVT_MEDIA_FINISHED: int  # Sent when a media has finished playing in a   wx.media.MediaCtrl. Processes a  wxEVT_MEDIA_FINISHED   event type.

EVT_MEDIA_STATECHANGED: int  # Sent when a media has switched its state (from any media state). Processes a  wxEVT_MEDIA_STATECHANGED   event type.

EVT_MEDIA_PLAY: int  # Sent when a media has switched to the  MEDIASTATE_PLAYING   state. Processes a   wxEVT_MEDIA_PLAY   event type.

EVT_MEDIA_PAUSE: int  # Sent when a media has switched to the  MEDIASTATE_PAUSED   state. Processes a   wxEVT_MEDIA_PAUSE   event type. ^^

MediaState: TypeAlias = int  # Enumeration

MediaCtrlPlayerControls: TypeAlias = int  # Enumeration

MEDIACTRLPLAYERCONTROLS_NONE: int

MEDIACTRLPLAYERCONTROLS_STEP: int

MEDIACTRLPLAYERCONTROLS_VOLUME: int

MEDIACTRLPLAYERCONTROLS_DEFAULT: int

