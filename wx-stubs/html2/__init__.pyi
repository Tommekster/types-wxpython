# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Control, VersionInfo, VisualAttributes, NotifyEvent, Object, _VersionInfo, FSFile

class WebView(Control):
    """ This control may be used to render web (HTML / CSS / javascript)
documents.


  


        Source: https://docs.wxpython.org/wx.html2.WebView.html
    """
    def AddScriptMessageHandler(self, name: str) -> bool:
        """ 

`AddScriptMessageHandler`(*self*, *name*)[¶](#wx.html2.WebView.AddScriptMessageHandler "Permalink to this definition")
Add a script message handler with the given name.


To use the script message handler from javascript use `window` .<name>.postMessage(<messageBody>) where `<name>` corresponds the value of the name parameter. The `<messageBody>` will be available to the application via a `wxEVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED` event.


Sample C++ code receiving a script message:



```
# Install message handler with the name wx_msg
self.webView.AddScriptMessageHandler('wx_msg')
# Bind an event handler to receive those messages
self.webView.Bind(wx.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, self.handleMessage)

```


Sample javascript sending a script message:



```
# Send sample message body
window.wx_msg.postMessage('This is a message body')

```



Parameters
**name** (*string*) – Name of the message handler that can be used from javascript



Return type
*bool*



Returns
`True` if the handler could be added, `False` if it could not be added.





New in version 4.1/wxWidgets-3.1.5.




Note


The Edge backend only supports a single message handler and the IE backend does not support script message handlers.




See also


[`RemoveScriptMessageHandler`](#wx.html2.WebView.RemoveScriptMessageHandler "wx.html2.WebView.RemoveScriptMessageHandler")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def AddUserScript(self, javascript, injectionTime=WEBVIEW_INJECT_AT_DOCUMENT_START) -> bool:
        """ 

`AddUserScript`(*self*, *javascript*, *injectionTime=WEBVIEW\_INJECT\_AT\_DOCUMENT\_START*)[¶](#wx.html2.WebView.AddUserScript "Permalink to this definition")
Injects the specified script into the webpage’s content.



Parameters
* **javascript** (*string*) – The javascript code to add.
* **injectionTime** ([*WebViewUserScriptInjectionTime*](wx.html2.WebViewUserScriptInjectionTime.enumeration.html "WebViewUserScriptInjectionTime")) – Specifies when the script will be executed.



Return type
*bool*



Returns
Returns `True` if the script was added successfully.





New in version 4.1/wxWidgets-3.1.5.




Note


Please note that this is unsupported by the IE backend and the Edge backend does only support `wx.html2.WEBVIEW_INJECT_AT_DOCUMENT_START`.




See also


[`RemoveAllUserScripts`](#wx.html2.WebView.RemoveAllUserScripts "wx.html2.WebView.RemoveAllUserScripts")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanCopy(self) -> bool:
        """ 

`CanCopy`(*self*)[¶](#wx.html2.WebView.CanCopy "Permalink to this definition")
Returns `True` if the current selection can be copied.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanCut(self) -> bool:
        """ 

`CanCut`(*self*)[¶](#wx.html2.WebView.CanCut "Permalink to this definition")
Returns `True` if the current selection can be cut.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanGoBack(self) -> bool:
        """ 

`CanGoBack`(*self*)[¶](#wx.html2.WebView.CanGoBack "Permalink to this definition")
Returns `True` if it is possible to navigate backward in the history of visited pages.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanGoForward(self) -> bool:
        """ 

`CanGoForward`(*self*)[¶](#wx.html2.WebView.CanGoForward "Permalink to this definition")
Returns `True` if it is possible to navigate forward in the history of visited pages.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanPaste(self) -> bool:
        """ 

`CanPaste`(*self*)[¶](#wx.html2.WebView.CanPaste "Permalink to this definition")
Returns `True` if data can be pasted.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanRedo(self) -> bool:
        """ 

`CanRedo`(*self*)[¶](#wx.html2.WebView.CanRedo "Permalink to this definition")
Returns `True` if there is an action to redo.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanSetZoomType(self, type: WebViewZoomType) -> bool:
        """ 

`CanSetZoomType`(*self*, *type*)[¶](#wx.html2.WebView.CanSetZoomType "Permalink to this definition")
Retrieve whether the current HTML engine supports a zoom type.



Parameters
**type** ([*WebViewZoomType*](wx.html2.WebViewZoomType.enumeration.html "WebViewZoomType")) – The zoom type to test.



Return type
*bool*



Returns
Whether this type of zoom is supported by this HTML engine (and thus can be set through [`SetZoomType`](#wx.html2.WebView.SetZoomType "wx.html2.WebView.SetZoomType") ).






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def CanUndo(self) -> bool:
        """ 

`CanUndo`(*self*)[¶](#wx.html2.WebView.CanUndo "Permalink to this definition")
Returns `True` if there is an action to undo.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def ClearHistory(self) -> None:
        """ 

`ClearHistory`(*self*)[¶](#wx.html2.WebView.ClearHistory "Permalink to this definition")
Clear the history, this will also remove the visible page.



Note


This is not implemented on the WebKit2GTK+ backend and macOS.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def ClearSelection(self) -> None:
        """ 

`ClearSelection`(*self*)[¶](#wx.html2.WebView.ClearSelection "Permalink to this definition")
Clears the current selection.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Copy(self) -> None:
        """ 

`Copy`(*self*)[¶](#wx.html2.WebView.Copy "Permalink to this definition")
Copies the current selection.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Create(self, parent, id=ID_ANY, url=WebViewDefaultURLStr, pos=DefaultPosition, size=DefaultSize, style=0, name=WebViewNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *url=WebViewDefaultURLStr*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*, *name=WebViewNameStr*)[¶](#wx.html2.WebView.Create "Permalink to this definition")
Creation function for two-step creation.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **url** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.html2.WebView.Cut "Permalink to this definition")
Cuts the current selection.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def DeleteSelection(self) -> None:
        """ 

`DeleteSelection`(*self*)[¶](#wx.html2.WebView.DeleteSelection "Permalink to this definition")
Deletes the current selection.


Note that for `WEBVIEW_BACKEND_WEBKIT` the selection must be editable, either through SetEditable or the correct HTML attribute.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableAccessToDevTools(self, enable: bool=True) -> None:
        """ 

`EnableAccessToDevTools`(*self*, *enable=True*)[¶](#wx.html2.WebView.EnableAccessToDevTools "Permalink to this definition")
Enable or disable access to dev tools for the user.


Dev tools are disabled by default.



Parameters
**enable** (*bool*) – 





New in version 4.1/wxWidgets-3.1.4.




Note


This is not implemented for the IE backend.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableContextMenu(self, enable: bool=True) -> None:
        """ 

`EnableContextMenu`(*self*, *enable=True*)[¶](#wx.html2.WebView.EnableContextMenu "Permalink to this definition")
Enable or disable the right click context menu.


By default the standard context menu is enabled, this method can be used to disable it or re-enable it later.



Parameters
**enable** (*bool*) – 





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def EnableHistory(self, enable: bool=True) -> None:
        """ 

`EnableHistory`(*self*, *enable=True*)[¶](#wx.html2.WebView.EnableHistory "Permalink to this definition")
Enable or disable the history.


This will also clear the history.



Parameters
**enable** (*bool*) – 





Note


This is not implemented on the WebKit2GTK+ backend and macOS.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Find(self, text, flags=WEBVIEW_FIND_DEFAULT) -> int:
        """ 

`Find`(*self*, *text*, *flags=WEBVIEW\_FIND\_DEFAULT*)[¶](#wx.html2.WebView.Find "Permalink to this definition")
Finds a phrase on the current page and if found, the control will scroll the phrase into view and select it.



Parameters
* **text** (*string*) – The phrase to search for.
* **flags** ([*WebViewFindFlags*](wx.html2.WebViewFindFlags.enumeration.html "WebViewFindFlags")) – The flags for the search.



Return type
*long*



Returns
If search phrase was not found in combination with the flags then `NOT_FOUND` is returned. If called for the first time with search phrase then the total number of results will be returned. Then for every time its called with the same search phrase it will return the number of the current match.





New in version 2.9.5.




Note


This function will restart the search if the flags `WEBVIEW_FIND_ENTIRE_WORD` or `WEBVIEW_FIND_MATCH_CASE` are changed, since this will require a new search. To reset the search, for example resetting the highlights call the function with an empty search phrase.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def GetBackendVersionInfo(backend: str=WebViewBackendDefault) -> 'VersionInfo':
        """ 

*static* `GetBackendVersionInfo`(*backend=WebViewBackendDefault*)[¶](#wx.html2.WebView.GetBackendVersionInfo "Permalink to this definition")
Retrieve the version information about the backend implementation.



Parameters
**backend** (*string*) – 



Return type
*VersionInfo*





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetBackwardHistory(self) -> Any:
        """ 

`GetBackwardHistory`(*self*)[¶](#wx.html2.WebView.GetBackwardHistory "Permalink to this definition")
Returns a list of items in the back history.


The first item in the vector is the first page that was loaded by the control.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.html2.WebView.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetCurrentTitle(self) -> str:
        """ 

`GetCurrentTitle`(*self*)[¶](#wx.html2.WebView.GetCurrentTitle "Permalink to this definition")
Get the title of the current web page, or its URL/path if title is not available.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetCurrentURL(self) -> str:
        """ 

`GetCurrentURL`(*self*)[¶](#wx.html2.WebView.GetCurrentURL "Permalink to this definition")
Get the URL of the currently displayed document.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetForwardHistory(self) -> Any:
        """ 

`GetForwardHistory`(*self*)[¶](#wx.html2.WebView.GetForwardHistory "Permalink to this definition")
Returns a list of items in the forward history.


The first item in the vector is the next item in the history with respect to the currently loaded page.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetNativeBackend(self) -> None:
        """ 

`GetNativeBackend`(*self*)[¶](#wx.html2.WebView.GetNativeBackend "Permalink to this definition")
Return the pointer to the native backend used by this control.


This method can be used to retrieve the pointer to the native rendering engine used by this control. The return value needs to be down-casted to the appropriate type depending on the platform: under Windows, it’s a pointer to IWebBrowser2 interface, under macOS it’s a WebView pointer and under GTK it’s a WebKitWebView.


For example, you could set the WebKit options using this method:



```
# In Python the value returned will be a sip wrapper around a void* type,
# and it can be converted to the address being pointed to with int().
webview_ptr = self.webview.GetNativeBackend()

# Assuming you are able to get a ctypes, cffi or similar access to the
# webview library, you can use that pointer value to give it access to the
# WebView backend to operate upon.
theWebViewLib.doSomething(int(webview_ptr))

```



New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetPageSource(self) -> str:
        """ 

`GetPageSource`(*self*)[¶](#wx.html2.WebView.GetPageSource "Permalink to this definition")
Get the HTML source code of the currently displayed document.



Return type
`string`



Returns
The HTML source code, or an empty string if no page is currently shown.






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetPageText(self) -> str:
        """ 

`GetPageText`(*self*)[¶](#wx.html2.WebView.GetPageText "Permalink to this definition")
Get the text of the current page.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetSelectedSource(self) -> str:
        """ 

`GetSelectedSource`(*self*)[¶](#wx.html2.WebView.GetSelectedSource "Permalink to this definition")
Returns the currently selected source, if any.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetSelectedText(self) -> str:
        """ 

`GetSelectedText`(*self*)[¶](#wx.html2.WebView.GetSelectedText "Permalink to this definition")
Returns the currently selected text, if any.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetUserAgent(self) -> str:
        """ 

`GetUserAgent`(*self*)[¶](#wx.html2.WebView.GetUserAgent "Permalink to this definition")
Returns the current user agent string for the web view.



Return type
`string`





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoom(self) -> 'WebViewZoom':
        """ 

`GetZoom`(*self*)[¶](#wx.html2.WebView.GetZoom "Permalink to this definition")
Get the zoom level of the page.


See [`GetZoomFactor`](#wx.html2.WebView.GetZoomFactor "wx.html2.WebView.GetZoomFactor") to get more precise zoom scale value other than as provided by `WebViewZoom` .



Return type
 [wx.html2.WebViewZoom](wx.html2.WebViewZoom.enumeration.html#wx-html2-webviewzoom)



Returns
The current level of zoom.






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoomFactor(self) -> float:
        """ 

`GetZoomFactor`(*self*)[¶](#wx.html2.WebView.GetZoomFactor "Permalink to this definition")
Get the zoom factor of the page.



Return type
*float*



Returns
The current factor of zoom.





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GetZoomType(self) -> 'WebViewZoomType':
        """ 

`GetZoomType`(*self*)[¶](#wx.html2.WebView.GetZoomType "Permalink to this definition")
Get how the zoom factor is currently interpreted.



Return type
 [wx.html2.WebViewZoomType](wx.html2.WebViewZoomType.enumeration.html#wx-html2-webviewzoomtype)



Returns
How the zoom factor is currently interpreted by the HTML engine.






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GoBack(self) -> None:
        """ 

`GoBack`(*self*)[¶](#wx.html2.WebView.GoBack "Permalink to this definition")
Navigate back in the history of visited pages.


Only valid if [`CanGoBack`](#wx.html2.WebView.CanGoBack "wx.html2.WebView.CanGoBack") returns `True`.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def GoForward(self) -> None:
        """ 

`GoForward`(*self*)[¶](#wx.html2.WebView.GoForward "Permalink to this definition")
Navigate forward in the history of visited pages.


Only valid if [`CanGoForward`](#wx.html2.WebView.CanGoForward "wx.html2.WebView.CanGoForward") returns `True`.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def HasSelection(self) -> bool:
        """ 

`HasSelection`(*self*)[¶](#wx.html2.WebView.HasSelection "Permalink to this definition")
Returns `True` if there is a current selection.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsAccessToDevToolsEnabled(self) -> bool:
        """ 

`IsAccessToDevToolsEnabled`(*self*)[¶](#wx.html2.WebView.IsAccessToDevToolsEnabled "Permalink to this definition")
Returns `True` if dev tools are available to the user.



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def IsBackendAvailable(backend: str) -> bool:
        """ 

*static* `IsBackendAvailable`(*backend*)[¶](#wx.html2.WebView.IsBackendAvailable "Permalink to this definition")
Allows to check if a specific backend is currently available.


For example, to check for Edge backend availability:



```
if wx.html2.WebView.IsBackendAvailable(wx.html2.WebViewBackendEdge):
    # Do whatever you need to do when the Edge backend is available

```



Parameters
**backend** (*string*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.4.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsBusy(self) -> bool:
        """ 

`IsBusy`(*self*)[¶](#wx.html2.WebView.IsBusy "Permalink to this definition")
Returns whether the web control is currently busy (e.g. loading a page).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsContextMenuEnabled(self) -> bool:
        """ 

`IsContextMenuEnabled`(*self*)[¶](#wx.html2.WebView.IsContextMenuEnabled "Permalink to this definition")
Returns `True` if a context menu will be shown on right click.



Return type
*bool*





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def IsEditable(self) -> bool:
        """ 

`IsEditable`(*self*)[¶](#wx.html2.WebView.IsEditable "Permalink to this definition")
Returns whether the web control is currently editable.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def LoadURL(self, url: str) -> None:
        """ 

`LoadURL`(*self*, *url*)[¶](#wx.html2.WebView.LoadURL "Permalink to this definition")
Load a web page from a URL.



Parameters
**url** (*string*) – The URL of the page to be loaded.





Note


Web engines generally report errors asynchronously, so if you wish to know whether loading the URL was successful, register to receive navigation error events.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def MSWSetEmulationLevel(level: WebViewIE_EmulationLevel=WEBVIEWIE_EMU_IE11) -> bool:
        """ 

*static* `MSWSetEmulationLevel`(*level=WEBVIEWIE\_EMU\_IE11*)[¶](#wx.html2.WebView.MSWSetEmulationLevel "Permalink to this definition")
Sets emulation level.


This function is useful to change the emulation level of the system browser control used for  [wx.html2.WebView](#wx-html2-webview) implementation under MSW, rather than using the currently default, IE7-compatible, level.


Please notice that this function works by modifying the per-user part of MSW registry, which has several implications: first, it is sufficient to call it only once (per user) as the changes done by it are persistent and, second, if you do not want them to be persistent, you need to call it with `WEBVIEWIE_EMU_DEFAULT` argument explicitly.


In particular, this function should be called to allow [`RunScript`](#wx.html2.WebView.RunScript "wx.html2.WebView.RunScript") to work for JavaScript code returning arbitrary objects, which is not supported at the default emulation level.


If set to a level higher than installed version, the highest available level will be used instead. `WEBVIEWIE_EMU_IE11` is recommended for best performance and experience.


This function is MSW-specific and doesn’t exist under other platforms.


See <https://msdn.microsoft.com/en-us/library/ee330730#browser_emulation> for more information about browser control emulation levels.



Parameters
**level** ([*WebViewIE\_EmulationLevel*](wx.html2.WebViewIE_EmulationLevel.enumeration.html "WebViewIE_EmulationLevel")) – the target emulation level



Return type
*bool*



Returns
`True` on success, `False` on failure (a warning message is also logged in the latter case).





New in version 4.1/wxWidgets-3.1.3.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def MSWSetModernEmulationLevel(modernLevel: bool=True) -> bool:
        """ 

*static* `MSWSetModernEmulationLevel`(*modernLevel=True*)[¶](#wx.html2.WebView.MSWSetModernEmulationLevel "Permalink to this definition")
Please explicitly specify emulation level with [`MSWSetEmulationLevel`](#wx.html2.WebView.MSWSetEmulationLevel "wx.html2.WebView.MSWSetEmulationLevel") .



Parameters
**modernLevel** (*bool*) – `True` to set level to `IE8`, synonym for `WEBVIEWIE_EMU_IE8` . `False` to reset the emulation level to its default, synonym for `WEBVIEWIE_EMU_DEFAULT` .



Return type
*bool*



Returns
`True` on success, `False` on failure (a warning message is also logged in the latter case).





New in version 4.1/wxWidgets-3.1.1.




Deprecated


This function is kept mostly for backwards compatibility.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def New(*args, **kw) -> 'WebView':
        """ 

*static* `New`(*\*args*, *\*\*kw*)[¶](#wx.html2.WebView.New "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**New** *(backend=WebViewBackendDefault)*


Factory function to create a new  [wx.html2.WebView](#wx-html2-webview) with two-step creation, [`wx.html2.WebView.Create`](#wx.html2.WebView.Create "wx.html2.WebView.Create") should be called on the returned object.



Parameters
**backend** (*string*) – The backend web rendering engine to use. `WebViewBackendDefault` , `WebViewBackendIE` and `WebViewBackendWebKit` are predefined where appropriate.



Return type
 [wx.html2.WebView](#wx-html2-webview)



Returns
The created  [wx.html2.WebView](#wx-html2-webview)





New in version 2.9.5.





---

  



**New** *(parent, id=ID\_ANY, url=WebViewDefaultURLStr, pos=DefaultPosition, size=DefaultSize, backend=WebViewBackendDefault, style=0, name=WebViewNameStr)*


Factory function to create a new  [wx.html2.WebView](#wx-html2-webview) using a  [wx.html2.WebViewFactory](wx.html2.WebViewFactory.html#wx-html2-webviewfactory).



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window for the control
* **id** (*wx.WindowID*) – `ID` of this control
* **url** (*string*) – Initial URL to load
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position of the control
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Size of the control
* **backend** (*string*) – The backend web rendering engine to use. `WebViewBackendDefault` , `WebViewBackendIE` and `WebViewBackendWebKit` are predefined where appropriate.
* **style** (*long*) – Window style. For generic window styles, please see  [wx.Window](wx.Window.html#wx-window).
* **name** (*string*) – Window name.



Return type
 [wx.html2.WebView](#wx-html2-webview)



Returns
The created  [wx.html2.WebView](#wx-html2-webview), or `NULL` if the requested backend is not available





New in version 2.9.5.





---

  





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.html2.WebView.Paste "Permalink to this definition")
Pastes the current data.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Print(self) -> None:
        """ 

`Print`(*self*)[¶](#wx.html2.WebView.Print "Permalink to this definition")
Opens a print dialog so that the user may print the currently displayed page.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Redo(self) -> None:
        """ 

`Redo`(*self*)[¶](#wx.html2.WebView.Redo "Permalink to this definition")
Redos the last action.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    @staticmethod
    def RegisterFactory(backend, factory) -> None:
        """ 

*static* `RegisterFactory`(*backend*, *factory*)[¶](#wx.html2.WebView.RegisterFactory "Permalink to this definition")
Allows the registering of new backend for  [wx.html2.WebView](#wx-html2-webview).


*backend* can be used as an argument to [`New`](#wx.html2.WebView.New "wx.html2.WebView.New") .



Parameters
* **backend** (*string*) – The name for the new backend to be registered under
* **factory** ([*wx.html2.WebViewFactory*](wx.html2.WebViewFactory.html#wx.html2.WebViewFactory "wx.html2.WebViewFactory")) – A shared pointer to the factory which creates the appropriate backend.





New in version 2.9.5.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RegisterHandler(self, handler: 'html2.WebViewHandler') -> None:
        """ 

`RegisterHandler`(*self*, *handler*)[¶](#wx.html2.WebView.RegisterHandler "Permalink to this definition")
Registers a custom scheme handler.



Parameters
**handler** ([*wx.html2.WebViewHandler*](wx.html2.WebViewHandler.html#wx.html2.WebViewHandler "wx.html2.WebViewHandler")) – A shared pointer to a WebHandler.





Note


On macOS in order to use handlers two-step creation has to be used and [`RegisterHandler`](#wx.html2.WebView.RegisterHandler "wx.html2.WebView.RegisterHandler") has to be called before [`Create`](#wx.html2.WebView.Create "wx.html2.WebView.Create") . With the other backends it has to be called after [`Create`](#wx.html2.WebView.Create "wx.html2.WebView.Create") .





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Reload(self, flags: WebViewReloadFlags=WEBVIEW_RELOAD_DEFAULT) -> None:
        """ 

`Reload`(*self*, *flags=WEBVIEW\_RELOAD\_DEFAULT*)[¶](#wx.html2.WebView.Reload "Permalink to this definition")
Reload the currently displayed URL.



Parameters
**flags** ([*WebViewReloadFlags*](wx.html2.WebViewReloadFlags.enumeration.html "WebViewReloadFlags")) – A bit array that may optionally contain reload options.





Note


The flags are ignored by the Edge backend.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RemoveAllUserScripts(self) -> None:
        """ 

`RemoveAllUserScripts`(*self*)[¶](#wx.html2.WebView.RemoveAllUserScripts "Permalink to this definition")
Removes all user scripts from the web view.



New in version 4.1/wxWidgets-3.1.5.




See also


[`AddUserScript`](#wx.html2.WebView.AddUserScript "wx.html2.WebView.AddUserScript")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RemoveScriptMessageHandler(self, name: str) -> bool:
        """ 

`RemoveScriptMessageHandler`(*self*, *name*)[¶](#wx.html2.WebView.RemoveScriptMessageHandler "Permalink to this definition")
Remove a script message handler with the given name that was previously added via [`AddScriptMessageHandler`](#wx.html2.WebView.AddScriptMessageHandler "wx.html2.WebView.AddScriptMessageHandler") .



Parameters
**name** (*string*) – 



Return type
*bool*



Returns
`True` if the handler could be removed, `False` if it could not be removed.





New in version 4.1/wxWidgets-3.1.5.




See also


[`AddScriptMessageHandler`](#wx.html2.WebView.AddScriptMessageHandler "wx.html2.WebView.AddScriptMessageHandler")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RunScript(self, javascript: str) -> tuple:
        """ 

`RunScript`(*self*, *javascript*)[¶](#wx.html2.WebView.RunScript "Permalink to this definition")
Runs the given JavaScript code.


JavaScript code is executed inside the browser control and has full access to `DOM` and other browser-provided functionality. For example, this code



```
webview.RunScript("document.write('Hello from wx.Widgets!')")

```


will replace the current page contents with the provided string.


If *output* is non-null, it is filled with the result of executing this code on success, e.g. a JavaScript value such as a string, a number (integer or floating point), a boolean or `JSON` representation for non-primitive types such as arrays and objects. For example:



```
success, result = webview.RunScript(
    "document.getElementById('some_id').innderHTML")

if success:
    ... result contains the contents of the given element ...

else:
    ... the element with self ID probably doesn't exist ...

```


This function has a few platform-specific limitations:


* When using WebKit v1 in wxGTK2, retrieving the result of JavaScript execution is unsupported and this function will always return `False` if *output* is non-null to indicate this. This functionality is fully supported when using WebKit v2 or later in `GTK3`.
* When using WebKit under macOS, code execution is limited to at most 10MiB of memory and 10 seconds of execution time.
* When using IE backend under MSW, scripts can only be executed when the current page is fully loaded (i.e. `wxEVT_WEBVIEW_LOADED` event was received). A script tag inside the page HTML is required in order to run JavaScript.


Also notice that under MSW converting JavaScript objects to `JSON` is not supported in the default emulation mode.  [wx.html2.WebView](#wx-html2-webview) implements its own object-to-JSON conversion as a fallback for this case, however it is not as full-featured, well-tested or performing as the implementation of this functionality in the browser control itself, so it is recommended to use MSWSetEmulationLevel() to change emulation level to a more modern one in which `JSON` conversion is done by the control itself.



Parameters
**javascript** (*string*) – JavaScript code to execute.



Return type
*tuple*



Returns
( *bool*, *output* )





Note


Because of various potential issues it’s recommended to use [`RunScriptAsync`](#wx.html2.WebView.RunScriptAsync "wx.html2.WebView.RunScriptAsync") instead of this method. This is especially `True` if you plan to run code from a webview event and will also prevent unintended side effects on the UI outside of the webview.




See also


[`RunScriptAsync`](#wx.html2.WebView.RunScriptAsync "wx.html2.WebView.RunScriptAsync")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def RunScriptAsync(self, javascript, clientData=None) -> None:
        """ 

`RunScriptAsync`(*self*, *javascript*, *clientData=None*)[¶](#wx.html2.WebView.RunScriptAsync "Permalink to this definition")
Runs the given JavaScript code asynchronously and returns the result via a `wxEVT_WEBVIEW_SCRIPT_RESULT` .


The script result value can be retrieved via `wx.html2.WebViewEvent.GetString` . If the execution fails [`wx.html2.WebViewEvent.IsError`](wx.html2.WebViewEvent.html#wx.html2.WebViewEvent.IsError "wx.html2.WebViewEvent.IsError") will return `True`. In this case additional script execution error information maybe available via `wx.html2.WebViewEvent.GetString` .



Parameters
* **javascript** (*string*) – JavaScript code to execute.
* **clientData** – Arbirary pointer to data that can be retrieved from the result event.





New in version 4.1/wxWidgets-3.1.6.




Note


The IE backend does not support async script execution.




See also


[`RunScript`](#wx.html2.WebView.RunScript "wx.html2.WebView.RunScript")





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.html2.WebView.SelectAll "Permalink to this definition")
Selects the entire page.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetEditable(self, enable: bool=True) -> None:
        """ 

`SetEditable`(*self*, *enable=True*)[¶](#wx.html2.WebView.SetEditable "Permalink to this definition")
Set the editable property of the web control.


Enabling allows the user to edit the page even if the `contenteditable` attribute is not set. The exact capabilities vary with the backend being used.



Parameters
**enable** (*bool*) – 





Note


This is not implemented for macOS and the Edge backend.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetPage(self, *args, **kw) -> None:
        """ 

`SetPage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.html2.WebView.SetPage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetPage** *(self, html, baseUrl)*


Set the displayed page source to the contents of the given string.



Parameters
* **html** (*string*) – The string that contains the HTML data to display.
* **baseUrl** (*string*) – URL assigned to the HTML data, to be used to resolve relative paths, for instance.





Note


When using `WEBVIEW_BACKEND_IE` you must wait for the current page to finish loading before calling [`SetPage`](#wx.html2.WebView.SetPage "wx.html2.WebView.SetPage") . The baseURL parameter is not used in this backend and the Edge backend.





---

  



**SetPage** *(self, html, baseUrl)*


Set the displayed page source to the contents of the given stream.



Parameters
* **html** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) – The stream to read HTML data from.
* **baseUrl** (*string*) – URL assigned to the HTML data, to be used to resolve relative paths, for instance.






---

  





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetUserAgent(self, userAgent: str) -> bool:
        """ 

`SetUserAgent`(*self*, *userAgent*)[¶](#wx.html2.WebView.SetUserAgent "Permalink to this definition")
Specify a custom user agent string for the web view.


Returns `True` the user agent could be set.


If your first request should already use the custom user agent please use two step creation and call [`SetUserAgent`](#wx.html2.WebView.SetUserAgent "wx.html2.WebView.SetUserAgent") before [`Create`](#wx.html2.WebView.Create "wx.html2.WebView.Create") .



Parameters
**userAgent** (*string*) – 



Return type
*bool*





New in version 4.1/wxWidgets-3.1.5.




Note


This is not implemented for IE. For Edge [`SetUserAgent`](#wx.html2.WebView.SetUserAgent "wx.html2.WebView.SetUserAgent") `MUST` be called before [`Create`](#wx.html2.WebView.Create "wx.html2.WebView.Create") .





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoom(self, zoom: WebViewZoom) -> None:
        """ 

`SetZoom`(*self*, *zoom*)[¶](#wx.html2.WebView.SetZoom "Permalink to this definition")
Set the zoom level of the page.


See [`SetZoomFactor`](#wx.html2.WebView.SetZoomFactor "wx.html2.WebView.SetZoomFactor") for more precise scaling other than the measured steps provided by `WebViewZoom` .



Parameters
**zoom** ([*WebViewZoom*](wx.html2.WebViewZoom.enumeration.html "WebViewZoom")) – How much to zoom (scale) the HTML document.






            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoomFactor(self, zoom: float) -> None:
        """ 

`SetZoomFactor`(*self*, *zoom*)[¶](#wx.html2.WebView.SetZoomFactor "Permalink to this definition")
Set the zoom factor of the page.



Parameters
**zoom** (*float*) – How much to zoom (scale) the HTML document in arbitrary number.





New in version 4.1/wxWidgets-3.1.4.




Note


zoom scale in IE will be converted into `WebViewZoom` levels for `WebViewZoomType` of `WEBVIEW_ZOOM_TYPE_TEXT` .





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def SetZoomType(self, zoomType: WebViewZoomType) -> None:
        """ 

`SetZoomType`(*self*, *zoomType*)[¶](#wx.html2.WebView.SetZoomType "Permalink to this definition")
Set how to interpret the zoom factor.



Parameters
**zoomType** ([*WebViewZoomType*](wx.html2.WebViewZoomType.enumeration.html "WebViewZoomType")) – How the zoom factor should be interpreted by the HTML engine.





Note


invoke [`CanSetZoomType`](#wx.html2.WebView.CanSetZoomType "wx.html2.WebView.CanSetZoomType") first, some HTML renderers may not support all zoom types.





            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Stop(self) -> None:
        """ 

`Stop`(*self*)[¶](#wx.html2.WebView.Stop "Permalink to this definition")
Stop the current page loading process, if any.


May trigger an error event of type `WEBVIEW_NAV_ERR_USER_CANCELLED` . `TODO`: make `WEBVIEW_NAV_ERR_USER_CANCELLED` errors uniform across ports.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    def Undo(self) -> None:
        """ 

`Undo`(*self*)[¶](#wx.html2.WebView.Undo "Permalink to this definition")
Undos the last action.




            Source: https://docs.wxpython.org/wx.html2.WebView.html
        """

    BackwardHistory: Any  # `BackwardHistory`[¶](#wx.html2.WebView.BackwardHistory "Permalink to this definition")See [`GetBackwardHistory`](#wx.html2.WebView.GetBackwardHistory "wx.html2.WebView.GetBackwardHistory")
    CurrentTitle: str  # `CurrentTitle`[¶](#wx.html2.WebView.CurrentTitle "Permalink to this definition")See [`GetCurrentTitle`](#wx.html2.WebView.GetCurrentTitle "wx.html2.WebView.GetCurrentTitle")
    CurrentURL: str  # `CurrentURL`[¶](#wx.html2.WebView.CurrentURL "Permalink to this definition")See [`GetCurrentURL`](#wx.html2.WebView.GetCurrentURL "wx.html2.WebView.GetCurrentURL")
    ForwardHistory: Any  # `ForwardHistory`[¶](#wx.html2.WebView.ForwardHistory "Permalink to this definition")See [`GetForwardHistory`](#wx.html2.WebView.GetForwardHistory "wx.html2.WebView.GetForwardHistory")
    NativeBackend: None  # `NativeBackend`[¶](#wx.html2.WebView.NativeBackend "Permalink to this definition")See [`GetNativeBackend`](#wx.html2.WebView.GetNativeBackend "wx.html2.WebView.GetNativeBackend")
    PageSource: str  # `PageSource`[¶](#wx.html2.WebView.PageSource "Permalink to this definition")See [`GetPageSource`](#wx.html2.WebView.GetPageSource "wx.html2.WebView.GetPageSource")
    PageText: str  # `PageText`[¶](#wx.html2.WebView.PageText "Permalink to this definition")See [`GetPageText`](#wx.html2.WebView.GetPageText "wx.html2.WebView.GetPageText")
    SelectedSource: str  # `SelectedSource`[¶](#wx.html2.WebView.SelectedSource "Permalink to this definition")See [`GetSelectedSource`](#wx.html2.WebView.GetSelectedSource "wx.html2.WebView.GetSelectedSource")
    SelectedText: str  # `SelectedText`[¶](#wx.html2.WebView.SelectedText "Permalink to this definition")See [`GetSelectedText`](#wx.html2.WebView.GetSelectedText "wx.html2.WebView.GetSelectedText")
    UserAgent: str  # `UserAgent`[¶](#wx.html2.WebView.UserAgent "Permalink to this definition")See [`GetUserAgent`](#wx.html2.WebView.GetUserAgent "wx.html2.WebView.GetUserAgent") and [`SetUserAgent`](#wx.html2.WebView.SetUserAgent "wx.html2.WebView.SetUserAgent")
    Zoom: 'WebViewZoom'  # `Zoom`[¶](#wx.html2.WebView.Zoom "Permalink to this definition")See [`GetZoom`](#wx.html2.WebView.GetZoom "wx.html2.WebView.GetZoom") and [`SetZoom`](#wx.html2.WebView.SetZoom "wx.html2.WebView.SetZoom")
    ZoomFactor: float  # `ZoomFactor`[¶](#wx.html2.WebView.ZoomFactor "Permalink to this definition")See [`GetZoomFactor`](#wx.html2.WebView.GetZoomFactor "wx.html2.WebView.GetZoomFactor") and [`SetZoomFactor`](#wx.html2.WebView.SetZoomFactor "wx.html2.WebView.SetZoomFactor")
    ZoomType: 'WebViewZoomType'  # `ZoomType`[¶](#wx.html2.WebView.ZoomType "Permalink to this definition")See [`GetZoomType`](#wx.html2.WebView.GetZoomType "wx.html2.WebView.GetZoomType") and [`SetZoomType`](#wx.html2.WebView.SetZoomType "wx.html2.WebView.SetZoomType")



EVT_WEBVIEW_NAVIGATING: int  # Process a  wxEVT_WEBVIEW_NAVIGATING   event, generated before trying to get a resource. This event may be vetoed to prevent navigating to this resource. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_NAVIGATED: int  # Process a  wxEVT_WEBVIEW_NAVIGATED   event generated after it was confirmed that a resource would be requested. This event may not be vetoed. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_LOADED: int  # Process a  wxEVT_WEBVIEW_LOADED   event generated when the document is fully loaded and displayed. Note that if the displayed HTML document has several frames, one such event will be generated per frame.

EVT_WEBVIEW_ERROR: int  # Process a  wxEVT_WEBVIEW_ERROR   event generated when a navigation error occurs. The integer associated with this event will be a WebNavigationError item. The string associated with this event may contain a backend-specific more precise error message/code.

EVT_WEBVIEW_NEWWINDOW: int  # Process a  wxEVT_WEBVIEW_NEWWINDOW   event, generated when a new window is created. You must handle this event if you want anything to happen, for example to load the page in a new window or tab.

EVT_WEBVIEW_TITLE_CHANGED: int  # Process a  wxEVT_WEBVIEW_TITLE_CHANGED   event, generated when the page title changes. Use GetString to get the title.

EVT_WEBVIEW_FULLSCREEN_CHANGED: int  # Process a  wxEVT_WEBVIEW_FULLSCREEN_CHANGED   event, generated when the page wants to enter or leave fullscreen. Use GetInt to get the status. Not implemented for the IE backend and is only available in wxWidgets 3.1.5 or later.

EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED: int  # Process a  wxEVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED   event only available in wxWidgets 3.1.5 or later. For usage details see  AddScriptMessageHandler.

wxEVT_WEBVIEW_SCRIPT_RESULT: int  # Process a  wxEVT_WEBVIEW_SCRIPT_RESULT   event only available in wxWidgets 3.1.6 or later. For usage details see  RunScriptAsync. ^^

WEBVIEW_INJECT_AT_DOCUMENT_START: int

class WebViewEvent(NotifyEvent):
    """ **Possible constructors**:



```
WebViewEvent()

WebViewEvent(type, id, href, target, flags=WEBVIEW_NAV_ACTION_NONE,
             messageHandler="")

```


A navigation event holds information about events associated with
WebView objects.


  


        Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.html2.WebViewEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, type, id, href, target, flags=WEBVIEW\_NAV\_ACTION\_NONE, messageHandler=””)*



Parameters
* **type** (*wx.EventType*) –
* **id** (*int*) –
* **href** (*string*) –
* **target** (*string*) –
* **flags** ([*WebViewNavigationActionFlags*](wx.html2.WebViewNavigationActionFlags.enumeration.html "WebViewNavigationActionFlags")) –
* **messageHandler** (*string*) –






---

  





            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetMessageHandler(self) -> str:
        """ 

`GetMessageHandler`(*self*)[¶](#wx.html2.WebViewEvent.GetMessageHandler "Permalink to this definition")
Get the name of the script handler.


Only valid for events of type `wxEVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED`



Return type
`string`





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetNavigationAction(self) -> 'WebViewNavigationActionFlags':
        """ 

`GetNavigationAction`(*self*)[¶](#wx.html2.WebViewEvent.GetNavigationAction "Permalink to this definition")
Get the type of navigation action.


Only valid for events of type `wxEVT_WEBVIEW_NEWWINDOW`



Return type
 [wx.html2.WebViewNavigationActionFlags](wx.html2.WebViewNavigationActionFlags.enumeration.html#wx-html2-webviewnavigationactionflags)





New in version 4.1/wxWidgets-3.1.2.





            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetTarget(self) -> str:
        """ 

`GetTarget`(*self*)[¶](#wx.html2.WebViewEvent.GetTarget "Permalink to this definition")
Get the name of the target frame which the url of this event has been or will be loaded into.


This may return an empty string if the frame is not available.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def GetURL(self) -> str:
        """ 

`GetURL`(*self*)[¶](#wx.html2.WebViewEvent.GetURL "Permalink to this definition")
Get the URL being visited.



Return type
`string`






            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    def IsError(self) -> bool:
        """ 

`IsError`(*self*)[¶](#wx.html2.WebViewEvent.IsError "Permalink to this definition")
Returns `True` the script execution failed.


Only valid for events of type `wxEVT_WEBVIEW_SCRIPT_RESULT`



Return type
*bool*





New in version 4.1/wxWidgets-3.1.6.





            Source: https://docs.wxpython.org/wx.html2.WebViewEvent.html
        """

    MessageHandler: str  # `MessageHandler`[¶](#wx.html2.WebViewEvent.MessageHandler "Permalink to this definition")See [`GetMessageHandler`](#wx.html2.WebViewEvent.GetMessageHandler "wx.html2.WebViewEvent.GetMessageHandler")
    NavigationAction: 'WebViewNavigationActionFlags'  # `NavigationAction`[¶](#wx.html2.WebViewEvent.NavigationAction "Permalink to this definition")See [`GetNavigationAction`](#wx.html2.WebViewEvent.GetNavigationAction "wx.html2.WebViewEvent.GetNavigationAction")
    Target: str  # `Target`[¶](#wx.html2.WebViewEvent.Target "Permalink to this definition")See [`GetTarget`](#wx.html2.WebViewEvent.GetTarget "wx.html2.WebViewEvent.GetTarget")
    URL: str  # `URL`[¶](#wx.html2.WebViewEvent.URL "Permalink to this definition")See [`GetURL`](#wx.html2.WebViewEvent.GetURL "wx.html2.WebViewEvent.GetURL")



class WebViewFactory(Object):
    """ An abstract factory class for creating WebView backends.


  


        Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
    """
    def Create(self, *args, **kw) -> 'WebView':
        """ 

`Create`(*self*, *\*args*, *\*\*kw*)[¶](#wx.html2.WebViewFactory.Create "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Create** *(self)*


Function to create a new  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview) with two-step creation, [`wx.html2.WebView.Create`](wx.html2.WebView.html#wx.html2.WebView.Create "wx.html2.WebView.Create") should be called on the returned object.



Return type
 [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview)



Returns
the created  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview)






---

  



**Create** *(self, parent, id, url=WebViewDefaultURLStr, pos=DefaultPosition, size=DefaultSize, style=0, name=WebViewNameStr)*


Function to create a new  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview) with parameters.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window for the control
* **id** (*wx.WindowID*) – `ID` of this control
* **url** (*string*) – Initial URL to load
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Position of the control
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Size of the control
* **style** (*long*) – Window style. For generic window styles, please see  [wx.Window](wx.Window.html#wx-window).
* **name** (*string*) – Window name.



Return type
 [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview)



Returns
the created  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview)






---

  





            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    def GetVersionInfo(self) -> 'VersionInfo':
        """ 

`GetVersionInfo`(*self*)[¶](#wx.html2.WebViewFactory.GetVersionInfo "Permalink to this definition")
Retrieve the version information about this backend implementation.



Return type
[`VersionInfo`](#wx.html2.WebViewFactory.VersionInfo "wx.html2.WebViewFactory.VersionInfo")





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    def IsAvailable(self) -> bool:
        """ 

`IsAvailable`(*self*)[¶](#wx.html2.WebViewFactory.IsAvailable "Permalink to this definition")
Function to check if the backend is available at runtime.


The  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview) implementation can use this function to check all runtime requirements without trying to create a  [wx.html2.WebView](wx.html2.WebView.html#wx-html2-webview).



Return type
*bool*



Returns
returns `True` if the backend can be used or `False` if it is not available during runtime.





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebViewFactory.html
        """

    VersionInfo: '_VersionInfo'  # `VersionInfo`[¶](#wx.html2.WebViewFactory.VersionInfo "Permalink to this definition")See [`GetVersionInfo`](#wx.html2.WebViewFactory.GetVersionInfo "wx.html2.WebViewFactory.GetVersionInfo")



class WebViewHandler:
    """ **Possible constructors**:



```
WebViewHandler(scheme)

```


The base class for handling custom schemes in WebView, for example
to allow virtual file system support.


  


        Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
    """
    def __init__(self, scheme: str) -> None:
        """ 

`__init__`(*self*, *scheme*)[¶](#wx.html2.WebViewHandler.__init__ "Permalink to this definition")
Constructor.


Takes the name of the scheme that will be handled by this class for example `file` or `zip` .



Parameters
**scheme** (*string*) – 






            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetFile(self, uri: str) -> 'FSFile':
        """ 

`GetFile`(*self*, *uri*)[¶](#wx.html2.WebViewHandler.GetFile "Permalink to this definition")

Parameters
**uri** (*string*) – 



Return type
*FSFile*



Returns
A pointer to the file represented by `uri` .






            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.html2.WebViewHandler.GetName "Permalink to this definition")

Return type
`string`



Returns
The name of the scheme, as passed to the constructor.






            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def GetSecurityURL(self) -> str:
        """ 

`GetSecurityURL`(*self*)[¶](#wx.html2.WebViewHandler.GetSecurityURL "Permalink to this definition")

Return type
`string`



Returns
The custom security URL. Only used by *WebViewIE* .





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    def SetSecurityURL(self, url: str) -> None:
        """ 

`SetSecurityURL`(*self*, *url*)[¶](#wx.html2.WebViewHandler.SetSecurityURL "Permalink to this definition")
Sets a custom security URL.


Only used by *WebViewIE* .



Parameters
**url** (*string*) – 





New in version 4.1/wxWidgets-3.1.5.





            Source: https://docs.wxpython.org/wx.html2.WebViewHandler.html
        """

    Name: str  # `Name`[¶](#wx.html2.WebViewHandler.Name "Permalink to this definition")See [`GetName`](#wx.html2.WebViewHandler.GetName "wx.html2.WebViewHandler.GetName")
    SecurityURL: str  # `SecurityURL`[¶](#wx.html2.WebViewHandler.SecurityURL "Permalink to this definition")See [`GetSecurityURL`](#wx.html2.WebViewHandler.GetSecurityURL "wx.html2.WebViewHandler.GetSecurityURL") and [`SetSecurityURL`](#wx.html2.WebViewHandler.SetSecurityURL "wx.html2.WebViewHandler.SetSecurityURL")



class WebViewFSHandler(WebViewHandler):
    """ **Possible constructors**:



```
WebViewFSHandler(scheme)

```


A WebView file system handler to support standard FileSystem
protocols of the form example:page.htm The handler allows WebView
to use FileSystem in a similar fashion to its use with Html.


  


        Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
    """
    def __init__(self, scheme: str) -> None:
        """ 

`__init__`(*self*, *scheme*)[¶](#wx.html2.WebViewFSHandler.__init__ "Permalink to this definition")
Constructor.



Parameters
**scheme** (*string*) – 






            Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
        """

    def GetFile(self, uri: str) -> 'FSFile':
        """ 

`GetFile`(*self*, *uri*)[¶](#wx.html2.WebViewFSHandler.GetFile "Permalink to this definition")

Parameters
**uri** (*string*) – 



Return type
*FSFile*



Returns
A pointer to the file represented by `uri` .






            Source: https://docs.wxpython.org/wx.html2.WebViewFSHandler.html
        """



class WebViewArchiveHandler(WebViewHandler):
    """ **Possible constructors**:



```
WebViewArchiveHandler(scheme)

```


A custom handler for the file scheme which also supports loading from
archives.


  


        Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
    """
    def __init__(self, scheme: str) -> None:
        """ 

`__init__`(*self*, *scheme*)[¶](#wx.html2.WebViewArchiveHandler.__init__ "Permalink to this definition")
Constructor.



Parameters
**scheme** (*string*) – 






            Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
        """

    def GetFile(self, uri: str) -> 'FSFile':
        """ 

`GetFile`(*self*, *uri*)[¶](#wx.html2.WebViewArchiveHandler.GetFile "Permalink to this definition")

Parameters
**uri** (*string*) – 



Return type
*FSFile*



Returns
A pointer to the file represented by `uri` .






            Source: https://docs.wxpython.org/wx.html2.WebViewArchiveHandler.html
        """



WebViewUserScriptInjectionTime: TypeAlias = int  # Enumeration

WEBVIEW_INJECT_AT_DOCUMENT_END: int

WebViewZoomType: TypeAlias = int  # Enumeration

WEBVIEW_ZOOM_TYPE_LAYOUT: int

WEBVIEW_ZOOM_TYPE_TEXT: int

WebViewFindFlags: TypeAlias = int  # Enumeration

WEBVIEW_FIND_WRAP: int

WEBVIEW_FIND_ENTIRE_WORD: int

WEBVIEW_FIND_MATCH_CASE: int

WEBVIEW_FIND_HIGHLIGHT_RESULT: int

WEBVIEW_FIND_BACKWARDS: int

WEBVIEW_FIND_DEFAULT: int

WebViewZoom: TypeAlias = int  # Enumeration

WEBVIEW_ZOOM_TINY: int

WEBVIEW_ZOOM_SMALL: int

WEBVIEW_ZOOM_MEDIUM: int

WEBVIEW_ZOOM_LARGE: int

WEBVIEW_ZOOM_LARGEST: int

WEBVIEWIE_EMU_DEFAULT: int

WEBVIEWIE_EMU_IE7: int

WEBVIEWIE_EMU_IE8: int

WEBVIEWIE_EMU_IE8_FORCE: int

WEBVIEWIE_EMU_IE9: int

WEBVIEWIE_EMU_IE9_FORCE: int

WEBVIEWIE_EMU_IE10: int

WEBVIEWIE_EMU_IE10_FORCE: int

WEBVIEWIE_EMU_IE11: int

WEBVIEWIE_EMU_IE11_FORCE: int

WebViewReloadFlags: TypeAlias = int  # Enumeration

WEBVIEW_RELOAD_DEFAULT: int

WEBVIEW_RELOAD_NO_CACHE: int

WebViewNavigationError: TypeAlias = int  # Enumeration

WEBVIEW_NAV_ERR_CONNECTION: int

WEBVIEW_NAV_ERR_CERTIFICATE: int

WEBVIEW_NAV_ERR_AUTH: int

WEBVIEW_NAV_ERR_SECURITY: int

WEBVIEW_NAV_ERR_NOT_FOUND: int

WEBVIEW_NAV_ERR_REQUEST: int

WEBVIEW_NAV_ERR_USER_CANCELLED: int

WEBVIEW_NAV_ERR_OTHER: int

WebViewNavigationActionFlags: TypeAlias = int  # Enumeration

WEBVIEW_NAV_ACTION_NONE: int

WEBVIEW_NAV_ACTION_USER: int

WEBVIEW_NAV_ACTION_OTHER: int

WebViewIE_EmulationLevel: TypeAlias = int

