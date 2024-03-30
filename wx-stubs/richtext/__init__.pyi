# -*- coding: utf-8 -*-
from typing import Any, ContextManager, Optional, Union, TypeAlias

from .. import Control, _CommandProcessor, Menu, Point, DateTime, TextPos, Cursor, Size, VisualAttributes, CommandProcessor, Rect, ComboCtrl, Command, Choice, DataObjectSimple, DataFormat, Char, Dialog, NotifyEvent, Event, Object, Font, Panel, _Font, Colour, BitmapType, _Rect, PageSetupDialogData, Window, _PrintData, PrintData, Printout, TextAttr, Position, _Size, _Bitmap, Bitmap, HtmlListBox, _ImageList, ColourData, ImageList, _Colour
from ...adv import PropertySheetDialog

class RichTextCtrl(Control):
    """ **Possible constructors**:



```
RichTextCtrl()

RichTextCtrl(parent, id=-1, value="", pos=DefaultPosition,
             size=DefaultSize, style=RE_MULTILINE, validator=DefaultValidator,
             name=TextCtrlNameStr)

```


RichTextCtrl provides a generic, ground-up implementation of a text
control capable of showing multiple styles and images.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, parent, id=-1, value=””, pos=DefaultPosition, size=DefaultSize, style=RE\_MULTILINE, validator=DefaultValidator, name=TextCtrlNameStr)*


Constructor, creating and showing a rich text control.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – Parent window. Must not be `None`.
* **id** (*wx.WindowID*) – Window identifier. The value `ID_ANY` indicates a default value.
* **value** (*string*) – Default string.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – Window position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – Window size.
* **style** (*long*) – Window style.
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) – Window validator.
* **name** (*string*) – Window name.





See also


[`Create`](#wx.richtext.RichTextCtrl.Create "wx.richtext.RichTextCtrl.Create") ,  [wx.Validator](wx.Validator.html#wx-validator)





---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AddImage(self, image: 'Image') -> 'RichTextRange':
        """ 

`AddImage`(*self*, *image*)[¶](#wx.richtext.RichTextCtrl.AddImage "Permalink to this definition")
Adds an image to the control’s buffer.



Parameters
**image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) – 



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AddParagraph(self, text: str) -> 'RichTextRange':
        """ 

`AddParagraph`(*self*, *text*)[¶](#wx.richtext.RichTextCtrl.AddParagraph "Permalink to this definition")
Adds a new paragraph of text to the end of the buffer.



Parameters
**text** (*string*) – 



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AppendText(self, text: str) -> None:
        """ 

`AppendText`(*self*, *text*)[¶](#wx.richtext.RichTextCtrl.AppendText "Permalink to this definition")
Sets the insertion point to the end of the buffer and writes the text.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyAlignmentToSelection(self, alignment: int) -> bool:
        """ 

`ApplyAlignmentToSelection`(*self*, *alignment*)[¶](#wx.richtext.RichTextCtrl.ApplyAlignmentToSelection "Permalink to this definition")
Applies the given alignment to the selection or the default style (undoable).


For alignment values, see  [wx.TextAttr](wx.TextAttr.html#wx-textattr).



Parameters
**alignment** ([*TextAttrAlignment*](wx.TextAttrAlignment.enumeration.html "TextAttrAlignment")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyBoldToSelection(self) -> bool:
        """ 

`ApplyBoldToSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.ApplyBoldToSelection "Permalink to this definition")
Apples bold to the selection or the default style (undoable).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyItalicToSelection(self) -> bool:
        """ 

`ApplyItalicToSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.ApplyItalicToSelection "Permalink to this definition")
Applies italic to the selection or the default style (undoable).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyStyle(self, styleDef: 'richtext.RichTextStyleDefinition') -> bool:
        """ 

`ApplyStyle`(*self*, *styleDef*)[¶](#wx.richtext.RichTextCtrl.ApplyStyle "Permalink to this definition")
Applies the style sheet to the buffer, matching paragraph styles in the sheet against named styles in the buffer.


This might be useful if the styles have changed. If *sheet* is `None`, the sheet set with [`SetStyleSheet`](#wx.richtext.RichTextCtrl.SetStyleSheet "wx.richtext.RichTextCtrl.SetStyleSheet") is used. Currently this applies paragraph styles only.



Parameters
**styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyStyleSheet(self, styleSheet: Optional['richtext.RichTextStyleSheet']=None) -> bool:
        """ 

`ApplyStyleSheet`(*self*, *styleSheet=None*)[¶](#wx.richtext.RichTextCtrl.ApplyStyleSheet "Permalink to this definition")
Applies the style sheet to the buffer, for example if the styles have changed.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyTextEffectToSelection(self, flags: int) -> bool:
        """ 

`ApplyTextEffectToSelection`(*self*, *flags*)[¶](#wx.richtext.RichTextCtrl.ApplyTextEffectToSelection "Permalink to this definition")
Applies one or more TextAttrEffects flags to the selection (undoable).


If there is no selection, it is applied to the default style.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ApplyUnderlineToSelection(self) -> bool:
        """ 

`ApplyUnderlineToSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.ApplyUnderlineToSelection "Permalink to this definition")
Applies underline to the selection or the default style (undoable).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoComplete(self, *args, **kw) -> bool:
        """ 

`AutoComplete`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.AutoComplete "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**AutoComplete** *(self, choices)*


Call this function to enable auto-completion of the text typed in a single-line text control using the given *choices*.



Parameters
**choices** (*list of strings*) – 



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.0.




See also


[`AutoCompleteFileNames`](#wx.richtext.RichTextCtrl.AutoCompleteFileNames "wx.richtext.RichTextCtrl.AutoCompleteFileNames")





---

  



**AutoComplete** *(self, completer)*


Enable auto-completion using the provided completer object.


This method should be used instead of [`AutoComplete`](#wx.richtext.RichTextCtrl.AutoComplete "wx.richtext.RichTextCtrl.AutoComplete") overload taking the array of possible completions if the total number of strings is too big as it allows returning the completions dynamically, depending on the text already entered by user and so is more efficient.


The specified *completer* object will be used to retrieve the list of possible completions for the already entered text and will be deleted by  [wx.TextEntry](wx.TextEntry.html#wx-textentry) itself when it’s not needed any longer.


Notice that you need to include */textcompleter.h* in order to define your class inheriting from  [wx.TextCompleter](wx.TextCompleter.html#wx-textcompleter).



Parameters
**completer** ([*wx.TextCompleter*](wx.TextCompleter.html#wx.TextCompleter "wx.TextCompleter")) – The object to be used for generating completions if not `None`. If it is `None`, auto-completion is disabled. The  [wx.TextEntry](wx.TextEntry.html#wx-textentry) object takes ownership of this pointer and will delete it in any case (i.e. even if this method returns `False`).



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.2.




See also


 [wx.TextCompleter](wx.TextCompleter.html#wx-textcompleter)





---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoCompleteDirectories(self) -> bool:
        """ 

`AutoCompleteDirectories`(*self*)[¶](#wx.richtext.RichTextCtrl.AutoCompleteDirectories "Permalink to this definition")
Call this function to enable auto-completion of the text using the file system directories.


Unlike [`AutoCompleteFileNames`](#wx.richtext.RichTextCtrl.AutoCompleteFileNames "wx.richtext.RichTextCtrl.AutoCompleteFileNames") which completes both file names and directories, this function only completes the directory names.


Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.3.




See also


[`AutoComplete`](#wx.richtext.RichTextCtrl.AutoComplete "wx.richtext.RichTextCtrl.AutoComplete")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def AutoCompleteFileNames(self) -> bool:
        """ 

`AutoCompleteFileNames`(*self*)[¶](#wx.richtext.RichTextCtrl.AutoCompleteFileNames "Permalink to this definition")
Call this function to enable auto-completion of the text typed in a single-line text control using all valid file system paths.


Notice that currently this function is only implemented in wxMSW port and does nothing under the other platforms.



Return type
*bool*



Returns
`True` if the auto-completion was enabled or `False` if the operation failed, typically because auto-completion is not supported by the current platform.





New in version 2.9.0.




See also


[`AutoComplete`](#wx.richtext.RichTextCtrl.AutoComplete "wx.richtext.RichTextCtrl.AutoComplete")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BatchingUndo(self) -> bool:
        """ 

`BatchingUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.BatchingUndo "Permalink to this definition")
Returns `True` if undo commands are being batched.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginAlignment(self, alignment: int) -> bool:
        """ 

`BeginAlignment`(*self*, *alignment*)[¶](#wx.richtext.RichTextCtrl.BeginAlignment "Permalink to this definition")
Begins using alignment.


For alignment values, see  [wx.TextAttr](wx.TextAttr.html#wx-textattr).



Parameters
**alignment** ([*TextAttrAlignment*](wx.TextAttrAlignment.enumeration.html "TextAttrAlignment")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginBatchUndo(self, cmdName: str) -> bool:
        """ 

`BeginBatchUndo`(*self*, *cmdName*)[¶](#wx.richtext.RichTextCtrl.BeginBatchUndo "Permalink to this definition")
Starts batching undo history for commands.



Parameters
**cmdName** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginBold(self) -> bool:
        """ 

`BeginBold`(*self*)[¶](#wx.richtext.RichTextCtrl.BeginBold "Permalink to this definition")
Begins using bold.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginCharacterStyle(self, characterStyle: str) -> bool:
        """ 

`BeginCharacterStyle`(*self*, *characterStyle*)[¶](#wx.richtext.RichTextCtrl.BeginCharacterStyle "Permalink to this definition")
Begins using the named character style.



Parameters
**characterStyle** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginFont(self, font: 'Font') -> bool:
        """ 

`BeginFont`(*self*, *font*)[¶](#wx.richtext.RichTextCtrl.BeginFont "Permalink to this definition")
Begins using this font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginFontSize(self, pointSize: int) -> bool:
        """ 

`BeginFontSize`(*self*, *pointSize*)[¶](#wx.richtext.RichTextCtrl.BeginFontSize "Permalink to this definition")
Begins using the given point size.



Parameters
**pointSize** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginItalic(self) -> bool:
        """ 

`BeginItalic`(*self*)[¶](#wx.richtext.RichTextCtrl.BeginItalic "Permalink to this definition")
Begins using italic.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginLeftIndent(self, leftIndent, leftSubIndent=0) -> bool:
        """ 

`BeginLeftIndent`(*self*, *leftIndent*, *leftSubIndent=0*)[¶](#wx.richtext.RichTextCtrl.BeginLeftIndent "Permalink to this definition")
Begins applying a left indent and subindent in tenths of a millimetre.


The subindent is an offset from the left edge of the paragraph, and is used for all but the first line in a paragraph. A positive value will cause the first line to appear to the left of the subsequent lines, and a negative value will cause the first line to be indented to the right of the subsequent lines.


 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer) uses indentation to render a bulleted item. The content of the paragraph, including the first line, starts at the *leftIndent* plus the *leftSubIndent*.



Parameters
* **leftIndent** (*int*) – The distance between the margin and the bullet.
* **leftSubIndent** (*int*) – The distance between the left edge of the bullet and the left edge of the actual paragraph.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginLineSpacing(self, lineSpacing: int) -> bool:
        """ 

`BeginLineSpacing`(*self*, *lineSpacing*)[¶](#wx.richtext.RichTextCtrl.BeginLineSpacing "Permalink to this definition")
Begins applying line spacing.


*spacing* is a multiple, where 10 means single-spacing, 15 means 1.5 spacing, and 20 means float spacing.


The  [wx.TextAttrLineSpacing](wx.TextAttrLineSpacing.enumeration.html#wx-textattrlinespacing) constants are defined for convenience.



Parameters
**lineSpacing** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginListStyle(self, listStyle, level=1, number=1) -> bool:
        """ 

`BeginListStyle`(*self*, *listStyle*, *level=1*, *number=1*)[¶](#wx.richtext.RichTextCtrl.BeginListStyle "Permalink to this definition")
Begins using a specified list style.


Optionally, you can also pass a level and a number.



Parameters
* **listStyle** (*string*) –
* **level** (*int*) –
* **number** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginNumberedBullet(self, bulletNumber, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_ARABIC|TEXT_ATTR_BULLET_STYLE_PERIOD) -> bool:
        """ 

`BeginNumberedBullet`(*self*, *bulletNumber*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_ARABIC|TEXT\_ATTR\_BULLET\_STYLE\_PERIOD*)[¶](#wx.richtext.RichTextCtrl.BeginNumberedBullet "Permalink to this definition")
Begins a numbered bullet.


This call will be needed for each item in the list, and the application should take care of incrementing the numbering.


*bulletNumber* is a number, usually starting with 1. *leftIndent* and *leftSubIndent* are values in tenths of a millimetre. *bulletStyle* is a bitlist of the  [wx.TextAttrBulletStyle](wx.TextAttrBulletStyle.enumeration.html#wx-textattrbulletstyle) values.


 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer) uses indentation to render a bulleted item. The left indent is the distance between the margin and the bullet. The content of the paragraph, including the first line, starts at leftMargin + leftSubIndent. So the distance between the left edge of the bullet and the left of the actual paragraph is leftSubIndent.



Parameters
* **bulletNumber** (*int*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginParagraphSpacing(self, before, after) -> bool:
        """ 

`BeginParagraphSpacing`(*self*, *before*, *after*)[¶](#wx.richtext.RichTextCtrl.BeginParagraphSpacing "Permalink to this definition")
Begins paragraph spacing; pass the before-paragraph and after-paragraph spacing in tenths of a millimetre.



Parameters
* **before** (*int*) –
* **after** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginParagraphStyle(self, paragraphStyle: str) -> bool:
        """ 

`BeginParagraphStyle`(*self*, *paragraphStyle*)[¶](#wx.richtext.RichTextCtrl.BeginParagraphStyle "Permalink to this definition")
Begins applying the named paragraph style.



Parameters
**paragraphStyle** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginRightIndent(self, rightIndent: int) -> bool:
        """ 

`BeginRightIndent`(*self*, *rightIndent*)[¶](#wx.richtext.RichTextCtrl.BeginRightIndent "Permalink to this definition")
Begins a right indent, specified in tenths of a millimetre.



Parameters
**rightIndent** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginStandardBullet(self, bulletName, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool:
        """ 

`BeginStandardBullet`(*self*, *bulletName*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_STANDARD*)[¶](#wx.richtext.RichTextCtrl.BeginStandardBullet "Permalink to this definition")
Begins applying a symbol bullet.



Parameters
* **bulletName** (*string*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ 

`BeginStyle`(*self*, *style*)[¶](#wx.richtext.RichTextCtrl.BeginStyle "Permalink to this definition")
Begins applying a style.



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginSuppressUndo(self) -> bool:
        """ 

`BeginSuppressUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.BeginSuppressUndo "Permalink to this definition")
Starts suppressing undo history for commands.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginSymbolBullet(self, symbol, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool:
        """ 

`BeginSymbolBullet`(*self*, *symbol*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_SYMBOL*)[¶](#wx.richtext.RichTextCtrl.BeginSymbolBullet "Permalink to this definition")
Begins applying a symbol bullet, using a character from the current font.


See [`BeginNumberedBullet`](#wx.richtext.RichTextCtrl.BeginNumberedBullet "wx.richtext.RichTextCtrl.BeginNumberedBullet") for an explanation of how indentation is used to render the bulleted paragraph.



Parameters
* **symbol** (*string*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginTextColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ 

`BeginTextColour`(*self*, *colour*)[¶](#wx.richtext.RichTextCtrl.BeginTextColour "Permalink to this definition")
Begins using this colour.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginURL(self, url, characterStyle="") -> bool:
        """ 

`BeginURL`(*self*, *url*, *characterStyle=""*)[¶](#wx.richtext.RichTextCtrl.BeginURL "Permalink to this definition")
Begins applying `wx.TEXT_ATTR_URL` to the content.


Pass a URL and optionally, a character style to apply, since it is common to mark a URL with a familiar style such as blue text with underlining.



Parameters
* **url** (*string*) –
* **characterStyle** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def BeginUnderline(self) -> bool:
        """ 

`BeginUnderline`(*self*)[¶](#wx.richtext.RichTextCtrl.BeginUnderline "Permalink to this definition")
Begins using underlining.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanCopy(self) -> bool:
        """ 

`CanCopy`(*self*)[¶](#wx.richtext.RichTextCtrl.CanCopy "Permalink to this definition")
Returns `True` if selected content can be copied to the clipboard.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanCut(self) -> bool:
        """ 

`CanCut`(*self*)[¶](#wx.richtext.RichTextCtrl.CanCut "Permalink to this definition")
Returns `True` if selected content can be copied to the clipboard and deleted.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanDeleteRange(self, container, range) -> bool:
        """ 

`CanDeleteRange`(*self*, *container*, *range*)[¶](#wx.richtext.RichTextCtrl.CanDeleteRange "Permalink to this definition")
Can we delete this range? Sends an event to the control.



Parameters
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanDeleteSelection(self) -> bool:
        """ 

`CanDeleteSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.CanDeleteSelection "Permalink to this definition")
Returns `True` if selected content can be deleted.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanEditProperties(self, obj: 'richtext.RichTextObject') -> bool:
        """ 

`CanEditProperties`(*self*, *obj*)[¶](#wx.richtext.RichTextCtrl.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanInsertContent(self, container, pos) -> bool:
        """ 

`CanInsertContent`(*self*, *container*, *pos*)[¶](#wx.richtext.RichTextCtrl.CanInsertContent "Permalink to this definition")
Can we insert content at this position? Sends an event to the control.



Parameters
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **pos** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanPaste(self) -> bool:
        """ 

`CanPaste`(*self*)[¶](#wx.richtext.RichTextCtrl.CanPaste "Permalink to this definition")
Returns `True` if the clipboard content can be pasted to the buffer.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanRedo(self) -> bool:
        """ 

`CanRedo`(*self*)[¶](#wx.richtext.RichTextCtrl.CanRedo "Permalink to this definition")
Returns `True` if there is a command in the command history that can be redone.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def CanUndo(self) -> bool:
        """ 

`CanUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.CanUndo "Permalink to this definition")
Returns `True` if there is a command in the command history that can be undone.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ChangeValue(self, value: str) -> None:
        """ 

`ChangeValue`(*self*, *value*)[¶](#wx.richtext.RichTextCtrl.ChangeValue "Permalink to this definition")
Sets the new text control value.


It also marks the control as not-modified which means that IsModified() would return `False` immediately after the call to [`ChangeValue`](#wx.richtext.RichTextCtrl.ChangeValue "wx.richtext.RichTextCtrl.ChangeValue") .


The insertion point is set to the start of the control (i.e. position 0) by this function.


This functions does not generate the `wxEVT_TEXT` event but otherwise is identical to [`SetValue`](#wx.richtext.RichTextCtrl.SetValue "wx.richtext.RichTextCtrl.SetValue") .


See [User Generated Events vs Programmatically Generated Events](events_overview.html#user-generated-events-vs-programmatically-generated-events) for more information.



Parameters
**value** (*string*) – The new value to set. It may contain newline characters if the text control is multi-line.





New in version 2.7.1.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextCtrl.Clear "Permalink to this definition")
Clears the buffer content, leaving a single empty paragraph.


Cannot be undone.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def ClearAvailableFontNames() -> None:
        """ 

*static* `ClearAvailableFontNames`()[¶](#wx.richtext.RichTextCtrl.ClearAvailableFontNames "Permalink to this definition")
Clears the cache of available font names.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ClearListStyle(self, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ 

`ClearListStyle`(*self*, *range*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO*)[¶](#wx.richtext.RichTextCtrl.ClearListStyle "Permalink to this definition")
Clears the list style from the given range, clearing list-related attributes and applying any named paragraph style associated with each paragraph.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **flags** (*int*) –



Return type
*bool*





See also


[`SetListStyle`](#wx.richtext.RichTextCtrl.SetListStyle "wx.richtext.RichTextCtrl.SetListStyle") , [`PromoteList`](#wx.richtext.RichTextCtrl.PromoteList "wx.richtext.RichTextCtrl.PromoteList") , [`NumberList`](#wx.richtext.RichTextCtrl.NumberList "wx.richtext.RichTextCtrl.NumberList") .





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Command(self, event: 'CommandEvent') -> None:
        """ 

`Command`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.Command "Permalink to this definition")
Sends the event to the control.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Copy(self) -> None:
        """ 

`Copy`(*self*)[¶](#wx.richtext.RichTextCtrl.Copy "Permalink to this definition")
Copies the selected content (if any) to the clipboard.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Create(self, parent, id=-1, value="", pos=DefaultPosition, size=DefaultSize, style=RE_MULTILINE, validator=DefaultValidator, name=TextCtrlNameStr) -> bool:
        """ 

`Create`(*self*, *parent*, *id=-1*, *value=""*, *pos=DefaultPosition*, *size=DefaultSize*, *style=RE\_MULTILINE*, *validator=DefaultValidator*, *name=TextCtrlNameStr*)[¶](#wx.richtext.RichTextCtrl.Create "Permalink to this definition")
Creates the underlying window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **value** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –
* **validator** ([*wx.Validator*](wx.Validator.html#wx.Validator "wx.Validator")) –
* **name** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Cut(self) -> None:
        """ 

`Cut`(*self*)[¶](#wx.richtext.RichTextCtrl.Cut "Permalink to this definition")
Copies the selected content (if any) to the clipboard and deletes the selection.


This is undoable.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Delete(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`Delete`(*self*, *range*)[¶](#wx.richtext.RichTextCtrl.Delete "Permalink to this definition")
Deletes the content within the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DeleteSelectedContent(self, newPos=None) -> None:
        """ 

`DeleteSelectedContent`(*self*, *newPos=None*)[¶](#wx.richtext.RichTextCtrl.DeleteSelectedContent "Permalink to this definition")
Deletes content if there is a selection, e.g.


when pressing a key. Returns the new caret position in *newPos*, or leaves it if there was no action. This is undoable.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DeleteSelection(self) -> None:
        """ 

`DeleteSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.DeleteSelection "Permalink to this definition")
Deletes the content in the selection, if any.


This is undoable.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DiscardEdits(self) -> None:
        """ 

`DiscardEdits`(*self*)[¶](#wx.richtext.RichTextCtrl.DiscardEdits "Permalink to this definition")
Sets the buffer’s modified status to `False`, and clears the buffer’s command history.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoGetBestSize(self) -> 'Size':
        """ 

`DoGetBestSize`(*self*)[¶](#wx.richtext.RichTextCtrl.DoGetBestSize "Permalink to this definition")
Currently this simply returns  [wx.Size](wx.Size.html#wx-size).



Return type
`Size`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoGetValue(self) -> str:
        """ 

`DoGetValue`(*self*)[¶](#wx.richtext.RichTextCtrl.DoGetValue "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoLayoutBuffer(self, buffer, dc, context, rect, parentRect, flags) -> None:
        """ 

`DoLayoutBuffer`(*self*, *buffer*, *dc*, *context*, *rect*, *parentRect*, *flags*)[¶](#wx.richtext.RichTextCtrl.DoLayoutBuffer "Permalink to this definition")
Implements layout.


An application may override this to perform operations before or after layout.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **flags** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoLoadFile(self, file, fileType) -> bool:
        """ 

`DoLoadFile`(*self*, *file*, *fileType*)[¶](#wx.richtext.RichTextCtrl.DoLoadFile "Permalink to this definition")
Helper function for [`LoadFile`](#wx.richtext.RichTextCtrl.LoadFile "wx.richtext.RichTextCtrl.LoadFile") .


Loads content into the control’s buffer using the given type.


If the specified type is `wx.richtext.RICHTEXT_TYPE_ANY`, the type is deduced from the filename extension.


This function looks for a suitable  [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler) object.



Parameters
* **file** (*string*) –
* **fileType** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoSaveFile(self, file="", fileType=RICHTEXT_TYPE_ANY) -> bool:
        """ 

`DoSaveFile`(*self*, *file=""*, *fileType=RICHTEXT\_TYPE\_ANY*)[¶](#wx.richtext.RichTextCtrl.DoSaveFile "Permalink to this definition")
Helper function for [`SaveFile`](#wx.richtext.RichTextCtrl.SaveFile "wx.richtext.RichTextCtrl.SaveFile") .


Saves the buffer content using the given type.


If the specified type is `wx.richtext.RICHTEXT_TYPE_ANY`, the type is deduced from the filename extension.


This function looks for a suitable  [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler) object.



Parameters
* **file** (*string*) –
* **fileType** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoThaw(self) -> None:
        """ 

`DoThaw`(*self*)[¶](#wx.richtext.RichTextCtrl.DoThaw "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoWriteText(self, value, flags=0) -> None:
        """ 

`DoWriteText`(*self*, *value*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.DoWriteText "Permalink to this definition")

Parameters
* **value** (*string*) –
* **flags** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def DoesSelectionHaveTextEffectFlag(self, flag: int) -> bool:
        """ 

`DoesSelectionHaveTextEffectFlag`(*self*, *flag*)[¶](#wx.richtext.RichTextCtrl.DoesSelectionHaveTextEffectFlag "Permalink to this definition")
Returns `True` if all of the selection, or the content at the current caret position, has the supplied TextAttrEffects flag(s).



Parameters
**flag** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EditProperties(self, obj, parent) -> bool:
        """ 

`EditProperties`(*self*, *obj*, *parent*)[¶](#wx.richtext.RichTextCtrl.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableDelayedImageLoading(self, b: bool) -> None:
        """ 

`EnableDelayedImageLoading`(*self*, *b*)[¶](#wx.richtext.RichTextCtrl.EnableDelayedImageLoading "Permalink to this definition")
Enable or disable delayed image loading.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableImages(self, b: bool) -> None:
        """ 

`EnableImages`(*self*, *b*)[¶](#wx.richtext.RichTextCtrl.EnableImages "Permalink to this definition")
Enable or disable images.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableVerticalScrollbar(self, enable: bool) -> None:
        """ 

`EnableVerticalScrollbar`(*self*, *enable*)[¶](#wx.richtext.RichTextCtrl.EnableVerticalScrollbar "Permalink to this definition")
Enable or disable the vertical scrollbar.



Parameters
**enable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EnableVirtualAttributes(self, b: bool) -> None:
        """ 

`EnableVirtualAttributes`(*self*, *b*)[¶](#wx.richtext.RichTextCtrl.EnableVirtualAttributes "Permalink to this definition")
Pass `True` to let the control use virtual attributes.


The default is `False`.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndAlignment(self) -> bool:
        """ 

`EndAlignment`(*self*)[¶](#wx.richtext.RichTextCtrl.EndAlignment "Permalink to this definition")
Ends alignment.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndAllStyles(self) -> bool:
        """ 

`EndAllStyles`(*self*)[¶](#wx.richtext.RichTextCtrl.EndAllStyles "Permalink to this definition")
Ends application of all styles in the current style stack.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndBatchUndo(self) -> bool:
        """ 

`EndBatchUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.EndBatchUndo "Permalink to this definition")
Ends batching undo command history.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndBold(self) -> bool:
        """ 

`EndBold`(*self*)[¶](#wx.richtext.RichTextCtrl.EndBold "Permalink to this definition")
Ends using bold.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndCharacterStyle(self) -> bool:
        """ 

`EndCharacterStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.EndCharacterStyle "Permalink to this definition")
Ends application of a named character style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndFont(self) -> bool:
        """ 

`EndFont`(*self*)[¶](#wx.richtext.RichTextCtrl.EndFont "Permalink to this definition")
Ends using a font.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndFontSize(self) -> bool:
        """ 

`EndFontSize`(*self*)[¶](#wx.richtext.RichTextCtrl.EndFontSize "Permalink to this definition")
Ends using a point size.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndItalic(self) -> bool:
        """ 

`EndItalic`(*self*)[¶](#wx.richtext.RichTextCtrl.EndItalic "Permalink to this definition")
Ends using italic.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndLeftIndent(self) -> bool:
        """ 

`EndLeftIndent`(*self*)[¶](#wx.richtext.RichTextCtrl.EndLeftIndent "Permalink to this definition")
Ends left indent.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndLineSpacing(self) -> bool:
        """ 

`EndLineSpacing`(*self*)[¶](#wx.richtext.RichTextCtrl.EndLineSpacing "Permalink to this definition")
Ends line spacing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndListStyle(self) -> bool:
        """ 

`EndListStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.EndListStyle "Permalink to this definition")
Ends using a specified list style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndNumberedBullet(self) -> bool:
        """ 

`EndNumberedBullet`(*self*)[¶](#wx.richtext.RichTextCtrl.EndNumberedBullet "Permalink to this definition")
Ends application of a numbered bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndParagraphSpacing(self) -> bool:
        """ 

`EndParagraphSpacing`(*self*)[¶](#wx.richtext.RichTextCtrl.EndParagraphSpacing "Permalink to this definition")
Ends paragraph spacing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndParagraphStyle(self) -> bool:
        """ 

`EndParagraphStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.EndParagraphStyle "Permalink to this definition")
Ends application of a named paragraph style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndRightIndent(self) -> bool:
        """ 

`EndRightIndent`(*self*)[¶](#wx.richtext.RichTextCtrl.EndRightIndent "Permalink to this definition")
Ends right indent.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndStandardBullet(self) -> bool:
        """ 

`EndStandardBullet`(*self*)[¶](#wx.richtext.RichTextCtrl.EndStandardBullet "Permalink to this definition")
Begins applying a standard bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndStyle(self) -> bool:
        """ 

`EndStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.EndStyle "Permalink to this definition")
Ends the current style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndSuppressUndo(self) -> bool:
        """ 

`EndSuppressUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.EndSuppressUndo "Permalink to this definition")
Ends suppressing undo command history.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndSymbolBullet(self) -> bool:
        """ 

`EndSymbolBullet`(*self*)[¶](#wx.richtext.RichTextCtrl.EndSymbolBullet "Permalink to this definition")
Ends applying a symbol bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndTextColour(self) -> bool:
        """ 

`EndTextColour`(*self*)[¶](#wx.richtext.RichTextCtrl.EndTextColour "Permalink to this definition")
Ends applying a text colour.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndURL(self) -> bool:
        """ 

`EndURL`(*self*)[¶](#wx.richtext.RichTextCtrl.EndURL "Permalink to this definition")
Ends applying a URL.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def EndUnderline(self) -> bool:
        """ 

`EndUnderline`(*self*)[¶](#wx.richtext.RichTextCtrl.EndUnderline "Permalink to this definition")
End applying underlining.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ExtendCellSelection(self, table, noRowSteps, noColSteps) -> bool:
        """ 

`ExtendCellSelection`(*self*, *table*, *noRowSteps*, *noColSteps*)[¶](#wx.richtext.RichTextCtrl.ExtendCellSelection "Permalink to this definition")
Extends a table selection in the given direction.



Parameters
* **table** ([*wx.richtext.RichTextTable*](wx.richtext.RichTextTable.html#wx.richtext.RichTextTable "wx.richtext.RichTextTable")) –
* **noRowSteps** (*int*) –
* **noColSteps** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ExtendSelection(self, oldPosition, newPosition, flags) -> bool:
        """ 

`ExtendSelection`(*self*, *oldPosition*, *newPosition*, *flags*)[¶](#wx.richtext.RichTextCtrl.ExtendSelection "Permalink to this definition")
Helper function for extending the selection, returning `True` if the selection was changed.


Selections are in caret positions.



Parameters
* **oldPosition** (*long*) –
* **newPosition** (*long*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindCaretPositionForCharacterPosition(self, position, hitTestFlags, container, caretLineStart) -> int:
        """ 

`FindCaretPositionForCharacterPosition`(*self*, *position*, *hitTestFlags*, *container*, *caretLineStart*)[¶](#wx.richtext.RichTextCtrl.FindCaretPositionForCharacterPosition "Permalink to this definition")
Find the caret position for the combination of hit-test flags and character position.


Returns the caret position and also an indication of where to place the caret (caretLineStart) since this is ambiguous (same position used for end of line and start of next).



Parameters
* **position** (*long*) –
* **hitTestFlags** (*int*) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **caretLineStart** (*bool*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindContainerAtPoint(self, pt, position, hit, hitObj, flags=0) -> 'RichTextParagraphLayoutBox':
        """ 

`FindContainerAtPoint`(*self*, *pt*, *position*, *hit*, *hitObj*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.FindContainerAtPoint "Permalink to this definition")
Finds the container at the given point, which is assumed to be in client coordinates.



Parameters
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **position** (*long*) –
* **hit** (*int*) –
* **hitObj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **flags** (*int*) –



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindNextWordPosition(self, direction: int=1) -> int:
        """ 

`FindNextWordPosition`(*self*, *direction=1*)[¶](#wx.richtext.RichTextCtrl.FindNextWordPosition "Permalink to this definition")
Helper function for finding the caret position for the next word.


Direction is 1 (forward) or -1 (backwards).



Parameters
**direction** (*int*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def FindRangeForList(self, pos, isNumberedList) -> 'RichTextRange':
        """ 

`FindRangeForList`(*self*, *pos*, *isNumberedList*)[¶](#wx.richtext.RichTextCtrl.FindRangeForList "Permalink to this definition")
Given a character position at which there is a list style, find the range encompassing the same list style by looking backwards and forwards.



Parameters
* **pos** (*long*) –
* **isNumberedList** (*bool*) –



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ForceDelayedLayout(self) -> None:
        """ 

`ForceDelayedLayout`(*self*)[¶](#wx.richtext.RichTextCtrl.ForceDelayedLayout "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ForceUpper(self) -> None:
        """ 

`ForceUpper`(*self*)[¶](#wx.richtext.RichTextCtrl.ForceUpper "Permalink to this definition")
Convert all text entered into the control to upper case.


Call this method to ensure that all text entered into the control is converted on the fly to upper case. If the control is not empty, its existing contents is also converted to upper case.



New in version 4.1/wxWidgets-3.1.0.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetAdjustedCaretPosition(self, caretPos: int) -> int:
        """ 

`GetAdjustedCaretPosition`(*self*, *caretPos*)[¶](#wx.richtext.RichTextCtrl.GetAdjustedCaretPosition "Permalink to this definition")
The adjusted caret position is the character position adjusted to take into account whether we’re at the start of a paragraph, in which case style information should be taken from the next position, not current one.



Parameters
**caretPos** (*long*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def GetAvailableFontNames() -> list[str]:
        """ 

*static* `GetAvailableFontNames`()[¶](#wx.richtext.RichTextCtrl.GetAvailableFontNames "Permalink to this definition")
Font names take a long time to retrieve, so cache them (on demand).



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetBasicStyle(self) -> 'RichTextAttr':
        """ 

`GetBasicStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.GetBasicStyle "Permalink to this definition")
Gets the basic (overall) style.


This is the style of the whole buffer before further styles are applied, unlike the default style, which only affects the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetBuffer(self) -> 'RichTextBuffer':
        """ 

`GetBuffer`(*self*)[¶](#wx.richtext.RichTextCtrl.GetBuffer "Permalink to this definition")
Returns the buffer associated with the control.



Return type
 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretAtLineStart(self) -> bool:
        """ 

`GetCaretAtLineStart`(*self*)[¶](#wx.richtext.RichTextCtrl.GetCaretAtLineStart "Permalink to this definition")
Returns `True` if we are showing the caret position at the start of a line instead of at the end of the previous one.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPosition(self) -> int:
        """ 

`GetCaretPosition`(*self*)[¶](#wx.richtext.RichTextCtrl.GetCaretPosition "Permalink to this definition")
Returns the current caret position.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPositionForDefaultStyle(self) -> int:
        """ 

`GetCaretPositionForDefaultStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.GetCaretPositionForDefaultStyle "Permalink to this definition")
Returns the caret position since the default formatting was changed.


As soon as this position changes, we no longer reflect the default style in the UI. A value of -2 means that we should only reflect the style of the content under the caret.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCaretPositionForIndex(self, position, rect, container=None) -> None:
        """ 

`GetCaretPositionForIndex`(*self*, *position*, *rect*, *container=None*)[¶](#wx.richtext.RichTextCtrl.GetCaretPositionForIndex "Permalink to this definition")
Returns the caret height and position for the given character position.


If container is null, the current focus object will be used.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetCommandProcessor(self) -> 'CommandProcessor':
        """ 

`GetCommandProcessor`(*self*)[¶](#wx.richtext.RichTextCtrl.GetCommandProcessor "Permalink to this definition")
Gets the command processor associated with the control’s buffer.



Return type
[`CommandProcessor`](#wx.richtext.RichTextCtrl.CommandProcessor "wx.richtext.RichTextCtrl.CommandProcessor")






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetContextMenu(self) -> 'Menu':
        """ 

`GetContextMenu`(*self*)[¶](#wx.richtext.RichTextCtrl.GetContextMenu "Permalink to this definition")
Returns the current context menu.



Return type
*Menu*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetContextMenuPropertiesInfo(self) -> 'RichTextContextMenuPropertiesInfo':
        """ 

`GetContextMenuPropertiesInfo`(*self*)[¶](#wx.richtext.RichTextCtrl.GetContextMenuPropertiesInfo "Permalink to this definition")
Returns an object that stores information about context menu property item(s), in order to communicate between the context menu event handler and the code that responds to it.


The  [wx.richtext.RichTextContextMenuPropertiesInfo](wx.richtext.RichTextContextMenuPropertiesInfo.html#wx-richtext-richtextcontextmenupropertiesinfo) stores one item for each object that could respond to a property-editing event. If objects are nested, several might be editable.



Return type
 [wx.richtext.RichTextContextMenuPropertiesInfo](wx.richtext.RichTextContextMenuPropertiesInfo.html#wx-richtext-richtextcontextmenupropertiesinfo)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDefaultStyleEx(self) -> 'RichTextAttr':
        """ 

`GetDefaultStyleEx`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDefaultStyleEx "Permalink to this definition")
Returns the current default style, which can be used to change how subsequently inserted text is displayed.



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageLoading(self) -> bool:
        """ 

`GetDelayedImageLoading`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDelayedImageLoading "Permalink to this definition")
Returns `True` if delayed image loading is enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageProcessingRequired(self) -> bool:
        """ 

`GetDelayedImageProcessingRequired`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDelayedImageProcessingRequired "Permalink to this definition")
Gets the flag indicating that delayed image processing is required.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedImageProcessingTime(self) -> int:
        """ 

`GetDelayedImageProcessingTime`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDelayedImageProcessingTime "Permalink to this definition")
Returns the last time delayed image processing was performed.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDelayedLayoutThreshold(self) -> int:
        """ 

`GetDelayedLayoutThreshold`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDelayedLayoutThreshold "Permalink to this definition")
Gets the size of the buffer beyond which layout is delayed during resizing.


This optimizes sizing for large buffers. The default is 20000.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDimensionScale(self) -> float:
        """ 

`GetDimensionScale`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDimensionScale "Permalink to this definition")
Returns the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragStartPoint(self) -> 'Point':
        """ 

`GetDragStartPoint`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDragStartPoint "Permalink to this definition")
Get the possible Drag’n’Drop start point.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragStartTime(self) -> 'DateTime':
        """ 

`GetDragStartTime`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDragStartTime "Permalink to this definition")
Get the possible Drag’n’Drop start time.



Return type
*DateTime*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetDragging(self) -> bool:
        """ 

`GetDragging`(*self*)[¶](#wx.richtext.RichTextCtrl.GetDragging "Permalink to this definition")
Returns `True` if we are extending a selection.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFilename(self) -> str:
        """ 

`GetFilename`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFilename "Permalink to this definition")
Gets the current filename associated with the control.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFirstVisiblePoint(self) -> 'Point':
        """ 

`GetFirstVisiblePoint`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFirstVisiblePoint "Permalink to this definition")
Returns the first visible point in the window.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFirstVisiblePosition(self) -> int:
        """ 

`GetFirstVisiblePosition`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFirstVisiblePosition "Permalink to this definition")
Returns the first visible position in the current view.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFocusObject(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetFocusObject`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFocusObject "Permalink to this definition")
Returns the  [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject) object that currently has the editing focus.


If there are no composite objects, this will be the top-level buffer.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFontScale(self) -> float:
        """ 

`GetFontScale`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFontScale "Permalink to this definition")
Returns the scale factor for displaying fonts, for example for more comfortable editing.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutRequired(self) -> bool:
        """ 

`GetFullLayoutRequired`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFullLayoutRequired "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutSavedPosition(self) -> int:
        """ 

`GetFullLayoutSavedPosition`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFullLayoutSavedPosition "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetFullLayoutTime(self) -> int:
        """ 

`GetFullLayoutTime`(*self*)[¶](#wx.richtext.RichTextCtrl.GetFullLayoutTime "Permalink to this definition")

Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetHandlerFlags(self) -> int:
        """ 

`GetHandlerFlags`(*self*)[¶](#wx.richtext.RichTextCtrl.GetHandlerFlags "Permalink to this definition")
Returns flags that change the behaviour of loading or saving.


See the documentation for each handler class to see what flags are relevant for each handler.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetHint(self) -> str:
        """ 

`GetHint`(*self*)[¶](#wx.richtext.RichTextCtrl.GetHint "Permalink to this definition")
Returns the current hint string.


See [`SetHint`](#wx.richtext.RichTextCtrl.SetHint "wx.richtext.RichTextCtrl.SetHint") for more information about hints.



Return type
`string`





New in version 2.9.0.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetImagesEnabled(self) -> bool:
        """ 

`GetImagesEnabled`(*self*)[¶](#wx.richtext.RichTextCtrl.GetImagesEnabled "Permalink to this definition")
Returns `True` if images are enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetInsertionPoint(self) -> int:
        """ 

`GetInsertionPoint`(*self*)[¶](#wx.richtext.RichTextCtrl.GetInsertionPoint "Permalink to this definition")
Returns the current insertion point.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetInternalSelectionRange(self) -> 'RichTextRange':
        """ 

`GetInternalSelectionRange`(*self*)[¶](#wx.richtext.RichTextCtrl.GetInternalSelectionRange "Permalink to this definition")
Returns the selection range in character positions.


-2, -2 means no selection -1, -1 means select everything. The range is in internal format, i.e. a single character selection is denoted by (n, n)



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLastPosition(self) -> 'TextPos':
        """ 

`GetLastPosition`(*self*)[¶](#wx.richtext.RichTextCtrl.GetLastPosition "Permalink to this definition")
Returns the last position in the buffer.



Return type
*wx.TextPos*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLineLength(self, lineNo: int) -> int:
        """ 

`GetLineLength`(*self*, *lineNo*)[¶](#wx.richtext.RichTextCtrl.GetLineLength "Permalink to this definition")
Returns the length of the specified line in characters.



Parameters
**lineNo** (*long*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLineText(self, lineNo: int) -> str:
        """ 

`GetLineText`(*self*, *lineNo*)[¶](#wx.richtext.RichTextCtrl.GetLineText "Permalink to this definition")
Returns the text for the given line.



Parameters
**lineNo** (*long*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetLogicalPoint(self, ptPhysical: Union[tuple[int, int], 'Point']) -> 'Point':
        """ 

`GetLogicalPoint`(*self*, *ptPhysical*)[¶](#wx.richtext.RichTextCtrl.GetLogicalPoint "Permalink to this definition")
Transforms physical window position to logical (unscrolled) position.



Parameters
**ptPhysical** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetMargins(self) -> 'Point':
        """ 

`GetMargins`(*self*)[¶](#wx.richtext.RichTextCtrl.GetMargins "Permalink to this definition")
Returns the margins used by the control.


The `x` field of the returned point is the horizontal margin and the `y` field is the vertical one.



Return type
 [wx.Point](wx.Point.html#wx-point)





New in version 2.9.1.




Note


If given margin cannot be accurately determined, its value will be set to -1. On some platforms you cannot obtain valid margin values until you have called [`SetMargins`](#wx.richtext.RichTextCtrl.SetMargins "wx.richtext.RichTextCtrl.SetMargins") .




See also


[`SetMargins`](#wx.richtext.RichTextCtrl.SetMargins "wx.richtext.RichTextCtrl.SetMargins")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetNumberOfLines(self) -> int:
        """ 

`GetNumberOfLines`(*self*)[¶](#wx.richtext.RichTextCtrl.GetNumberOfLines "Permalink to this definition")
Returns the number of lines in the buffer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPhysicalPoint(self, ptLogical: Union[tuple[int, int], 'Point']) -> 'Point':
        """ 

`GetPhysicalPoint`(*self*, *ptLogical*)[¶](#wx.richtext.RichTextCtrl.GetPhysicalPoint "Permalink to this definition")
Transforms logical (unscrolled) position to physical window position.



Parameters
**ptLogical** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPreDrag(self) -> bool:
        """ 

`GetPreDrag`(*self*)[¶](#wx.richtext.RichTextCtrl.GetPreDrag "Permalink to this definition")
Are we trying to start Drag’n’Drop?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetPropertiesMenuLabel(self, obj: 'richtext.RichTextObject') -> str:
        """ 

`GetPropertiesMenuLabel`(*self*, *obj*)[¶](#wx.richtext.RichTextCtrl.GetPropertiesMenuLabel "Permalink to this definition")
Gets the object’s properties menu label.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetRange(self, from_, to_) -> str:
        """ 

`GetRange`(*self*, *from\_*, *to\_*)[¶](#wx.richtext.RichTextCtrl.GetRange "Permalink to this definition")
Gets the text for the given range.


The end point of range is specified as the last character position of the span of text, plus one.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScale(self) -> float:
        """ 

`GetScale`(*self*)[¶](#wx.richtext.RichTextCtrl.GetScale "Permalink to this definition")
Returns an overall scale factor for displaying and editing the content.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledPoint(self, pt: Union[tuple[int, int], 'Point']) -> 'Point':
        """ 

`GetScaledPoint`(*self*, *pt*)[¶](#wx.richtext.RichTextCtrl.GetScaledPoint "Permalink to this definition")
Returns a scaled point.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledRect(self, rect: 'Rect') -> 'Rect':
        """ 

`GetScaledRect`(*self*, *rect*)[¶](#wx.richtext.RichTextCtrl.GetScaledRect "Permalink to this definition")
Returns a scaled rectangle.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 



Return type
`Rect`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetScaledSize(self, sz: Union[tuple[int, int], 'Size']) -> 'Size':
        """ 

`GetScaledSize`(*self*, *sz*)[¶](#wx.richtext.RichTextCtrl.GetScaledSize "Permalink to this definition")
Returns a scaled size.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
`Size`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelection(self) -> 'RichTextSelection':
        """ 

`GetSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.GetSelection "Permalink to this definition")
Returns the range of the current selection.


The end point of range is specified as the last character position of the span of text, plus one. If the return values *from* and *to* are the same, there is no selection.



Return type
 [wx.richtext.RichTextSelection](wx.richtext.RichTextSelection.html#wx-richtext-richtextselection)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionAnchor(self) -> int:
        """ 

`GetSelectionAnchor`(*self*)[¶](#wx.richtext.RichTextCtrl.GetSelectionAnchor "Permalink to this definition")
Returns an anchor so we know how to extend the selection.


It’s a caret position since it’s between two characters.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionAnchorObject(self) -> 'RichTextObject':
        """ 

`GetSelectionAnchorObject`(*self*)[¶](#wx.richtext.RichTextCtrl.GetSelectionAnchorObject "Permalink to this definition")
Returns the anchor object if selecting multiple containers.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetSelectionRange(self) -> 'RichTextRange':
        """ 

`GetSelectionRange`(*self*)[¶](#wx.richtext.RichTextCtrl.GetSelectionRange "Permalink to this definition")
Returns the selection range in character positions.


-1, -1 means no selection.


The range is in API convention, i.e. a single character selection is denoted by (n, n+1)



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStringSelection(self) -> str:
        """ 

`GetStringSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.GetStringSelection "Permalink to this definition")
Returns the text within the current selection range, if any.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyle(self, *args, **kw) -> None:
        """ 

`GetStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.GetStyle "Permalink to this definition")
Gets the attributes at the given position.


This function gets the combined style - that is, the style you see on the screen as a result of combining base style, paragraph style and character style attributes.


To get the character or paragraph style alone, use [`GetUncombinedStyle`](#wx.richtext.RichTextCtrl.GetUncombinedStyle "wx.richtext.RichTextCtrl.GetUncombinedStyle") .




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyleForRange(self, *args, **kw) -> None:
        """ 

`GetStyleForRange`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.GetStyleForRange "Permalink to this definition")
Gets the attributes common to the specified range.


Attributes that differ in value within the range will not be included in *style* flags.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextCtrl.GetStyleSheet "Permalink to this definition")
Returns the style sheet associated with the control, if any.


A style sheet allows named character and paragraph styles to be applied.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetTextCursor(self) -> 'Cursor':
        """ 

`GetTextCursor`(*self*)[¶](#wx.richtext.RichTextCtrl.GetTextCursor "Permalink to this definition")
Returns the text (normal) cursor.



Return type
`Cursor`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetURLCursor(self) -> 'Cursor':
        """ 

`GetURLCursor`(*self*)[¶](#wx.richtext.RichTextCtrl.GetURLCursor "Permalink to this definition")
Returns the cursor to be used over URLs.



Return type
`Cursor`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUncombinedStyle(self, *args, **kw) -> None:
        """ 

`GetUncombinedStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.GetUncombinedStyle "Permalink to this definition")
Gets the attributes at the given position.


This function gets the *uncombined* style - that is, the attributes associated with the paragraph or character content, and not necessarily the combined attributes you see on the screen. To get the combined attributes, use [`GetStyle`](#wx.richtext.RichTextCtrl.GetStyle "wx.richtext.RichTextCtrl.GetStyle") .


If you specify (any) paragraph attribute in *style’s* flags, this function will fetch the paragraph attributes. Otherwise, it will return the character attributes.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledPoint(self, pt: Union[tuple[int, int], 'Point']) -> 'Point':
        """ 

`GetUnscaledPoint`(*self*, *pt*)[¶](#wx.richtext.RichTextCtrl.GetUnscaledPoint "Permalink to this definition")
Returns an unscaled point.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledRect(self, rect: 'Rect') -> 'Rect':
        """ 

`GetUnscaledRect`(*self*, *rect*)[¶](#wx.richtext.RichTextCtrl.GetUnscaledRect "Permalink to this definition")
Returns an unscaled rectangle.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 



Return type
`Rect`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetUnscaledSize(self, sz: Union[tuple[int, int], 'Size']) -> 'Size':
        """ 

`GetUnscaledSize`(*self*, *sz*)[¶](#wx.richtext.RichTextCtrl.GetUnscaledSize "Permalink to this definition")
Returns an unscaled size.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 



Return type
`Size`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetValue(self) -> str:
        """ 

`GetValue`(*self*)[¶](#wx.richtext.RichTextCtrl.GetValue "Permalink to this definition")
Returns the content of the entire control as a string.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVerticalScrollbarEnabled(self) -> bool:
        """ 

`GetVerticalScrollbarEnabled`(*self*)[¶](#wx.richtext.RichTextCtrl.GetVerticalScrollbarEnabled "Permalink to this definition")
Returns `True` if the vertical scrollbar is enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVirtualAttributesEnabled(self) -> bool:
        """ 

`GetVirtualAttributesEnabled`(*self*)[¶](#wx.richtext.RichTextCtrl.GetVirtualAttributesEnabled "Permalink to this definition")
Returns `True` if this control can use virtual attributes and virtual text.


The default is `False`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def GetVisibleLineForCaretPosition(self, caretPosition: int) -> 'RichTextLine':
        """ 

`GetVisibleLineForCaretPosition`(*self*, *caretPosition*)[¶](#wx.richtext.RichTextCtrl.GetVisibleLineForCaretPosition "Permalink to this definition")
Internal helper function returning the line for the visible caret position.


If the caret is shown at the very end of the line, it means the next character is actually on the following line. So this function gets the line we’re expecting to find if this is the case.



Parameters
**caretPosition** (*long*) – 



Return type
 [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasCharacterAttributes(self, range, style) -> bool:
        """ 

`HasCharacterAttributes`(*self*, *range*, *style*)[¶](#wx.richtext.RichTextCtrl.HasCharacterAttributes "Permalink to this definition")
Test if this whole range has character attributes of the specified kind.


If any of the attributes are different within the range, the test fails.


You can use this to implement, for example, bold button updating. *style* must have flags indicating which attributes are of interest.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasParagraphAttributes(self, range, style) -> bool:
        """ 

`HasParagraphAttributes`(*self*, *range*, *style*)[¶](#wx.richtext.RichTextCtrl.HasParagraphAttributes "Permalink to this definition")
Test if this whole range has paragraph attributes of the specified kind.


If any of the attributes are different within the range, the test fails. You can use this to implement, for example, centering button updating. *style* must have flags indicating which attributes are of interest.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasSelection(self) -> bool:
        """ 

`HasSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.HasSelection "Permalink to this definition")
Returns `True` if there is a selection and the object containing the selection was the same as the current focus object.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HasUnfocusedSelection(self) -> bool:
        """ 

`HasUnfocusedSelection`(*self*)[¶](#wx.richtext.RichTextCtrl.HasUnfocusedSelection "Permalink to this definition")
Returns `True` if there was a selection, whether or not the current focus object is the same as the selection’s container object.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HitTest(self, pt: Union[tuple[int, int], 'Point']) -> tuple:
        """ 

`HitTest`(*self*, *pt*)[¶](#wx.richtext.RichTextCtrl.HitTest "Permalink to this definition")
Finds the character at the given position in pixels.


*pt* is in device coords (not adjusted for the client area origin nor for scrolling).



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*tuple*



Returns
(  [wx.TextCtrlHitTestResult](wx.TextCtrlHitTestResult.enumeration.html#wx-textctrlhittestresult), *pos* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def HitTestXY(self, pt: Union[tuple[int, int], 'Point']) -> tuple:
        """ 

`HitTestXY`(*self*, *pt*)[¶](#wx.richtext.RichTextCtrl.HitTestXY "Permalink to this definition")
Finds the character at the given position in pixels.


*pt* is in device coords (not adjusted for the client area origin nor for scrolling).



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*tuple*



Returns
(  [wx.TextCtrlHitTestResult](wx.TextCtrlHitTestResult.enumeration.html#wx-textctrlhittestresult), *col*, *row* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextCtrl.Init "Permalink to this definition")
Initialises the members of the control.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Invalidate(self) -> None:
        """ 

`Invalidate`(*self*)[¶](#wx.richtext.RichTextCtrl.Invalidate "Permalink to this definition")
Invalidates the whole buffer to trigger painting later.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsDefaultStyleShowing(self) -> bool:
        """ 

`IsDefaultStyleShowing`(*self*)[¶](#wx.richtext.RichTextCtrl.IsDefaultStyleShowing "Permalink to this definition")
Returns `True` if the user has recently set the default style without moving the caret, and therefore the UI needs to reflect the default style and not the style at the caret.


Below is an example of code that uses this function to determine whether the UI should show that the current style is bold.



Return type
*bool*





See also


[`SetAndShowDefaultStyle`](#wx.richtext.RichTextCtrl.SetAndShowDefaultStyle "wx.richtext.RichTextCtrl.SetAndShowDefaultStyle") .





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsEditable(self) -> bool:
        """ 

`IsEditable`(*self*)[¶](#wx.richtext.RichTextCtrl.IsEditable "Permalink to this definition")
Returns `True` if the control is editable.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextCtrl.IsEmpty "Permalink to this definition")
Returns `True` if the control is currently empty.


This is the same as [`GetValue`](#wx.richtext.RichTextCtrl.GetValue "wx.richtext.RichTextCtrl.GetValue") .empty() but can be much more efficient for the multiline controls containing big amounts of text.



Return type
*bool*





New in version 2.7.1.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsModified(self) -> bool:
        """ 

`IsModified`(*self*)[¶](#wx.richtext.RichTextCtrl.IsModified "Permalink to this definition")
Returns `True` if the buffer has been modified.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsMultiLine(self) -> bool:
        """ 

`IsMultiLine`(*self*)[¶](#wx.richtext.RichTextCtrl.IsMultiLine "Permalink to this definition")
Returns `True` if the control is multiline.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsPositionVisible(self, pos: int) -> bool:
        """ 

`IsPositionVisible`(*self*, *pos*)[¶](#wx.richtext.RichTextCtrl.IsPositionVisible "Permalink to this definition")
Returns `True` if the given position is visible on the screen.



Parameters
**pos** (*long*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionAligned(self, alignment: int) -> bool:
        """ 

`IsSelectionAligned`(*self*, *alignment*)[¶](#wx.richtext.RichTextCtrl.IsSelectionAligned "Permalink to this definition")
Returns `True` if all of the selection is aligned according to the specified flag.



Parameters
**alignment** ([*TextAttrAlignment*](wx.TextAttrAlignment.enumeration.html "TextAttrAlignment")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionBold(self) -> bool:
        """ 

`IsSelectionBold`(*self*)[¶](#wx.richtext.RichTextCtrl.IsSelectionBold "Permalink to this definition")
Returns `True` if all of the selection, or the content at the caret position, is bold.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionItalics(self) -> bool:
        """ 

`IsSelectionItalics`(*self*)[¶](#wx.richtext.RichTextCtrl.IsSelectionItalics "Permalink to this definition")
Returns `True` if all of the selection, or the content at the caret position, is italic.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSelectionUnderlined(self) -> bool:
        """ 

`IsSelectionUnderlined`(*self*)[¶](#wx.richtext.RichTextCtrl.IsSelectionUnderlined "Permalink to this definition")
Returns `True` if all of the selection, or the content at the caret position, is underlined.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def IsSingleLine(self) -> bool:
        """ 

`IsSingleLine`(*self*)[¶](#wx.richtext.RichTextCtrl.IsSingleLine "Permalink to this definition")
Returns `True` if the control is single-line.


Currently  [wx.richtext.RichTextCtrl](#wx-richtext-richtextctrl) does not support single-line editing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def KeyboardNavigate(self, keyCode, flags) -> bool:
        """ 

`KeyboardNavigate`(*self*, *keyCode*, *flags*)[¶](#wx.richtext.RichTextCtrl.KeyboardNavigate "Permalink to this definition")
Helper function implementing keyboard navigation.



Parameters
* **keyCode** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LayoutContent(self, onlyVisibleRect: bool=False) -> bool:
        """ 

`LayoutContent`(*self*, *onlyVisibleRect=False*)[¶](#wx.richtext.RichTextCtrl.LayoutContent "Permalink to this definition")
Lays out the buffer, which must be done before certain operations, such as setting the caret position.


This function should not normally be required by the application.



Parameters
**onlyVisibleRect** (*bool*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LineBreak(self) -> bool:
        """ 

`LineBreak`(*self*)[¶](#wx.richtext.RichTextCtrl.LineBreak "Permalink to this definition")
Inserts a line break at the current insertion point.


A line break forces wrapping within a paragraph, and can be introduced by using this function, by appending the Char value **RichTextLineBreakChar** to text content, or by typing Shift-Return.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def LoadFile(self, file, type=RICHTEXT_TYPE_ANY) -> bool:
        """ 

`LoadFile`(*self*, *file*, *type=RICHTEXT\_TYPE\_ANY*)[¶](#wx.richtext.RichTextCtrl.LoadFile "Permalink to this definition")
Loads content into the control’s buffer using the given type.


If the specified type is `wx.richtext.RICHTEXT_TYPE_ANY`, the type is deduced from the filename extension.


This function looks for a suitable  [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler) object.



Parameters
* **file** (*string*) –
* **type** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MarkDirty(self) -> None:
        """ 

`MarkDirty`(*self*)[¶](#wx.richtext.RichTextCtrl.MarkDirty "Permalink to this definition")
Marks the buffer as modified.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaret(self, pos, showAtLineStart=False, container=None) -> bool:
        """ 

`MoveCaret`(*self*, *pos*, *showAtLineStart=False*, *container=None*)[¶](#wx.richtext.RichTextCtrl.MoveCaret "Permalink to this definition")
Move the caret to the given character position.


Please note that this does not update the current editing style from the new position; to do that, call [`wx.richtext.RichTextCtrl.SetInsertionPoint`](#wx.richtext.RichTextCtrl.SetInsertionPoint "wx.richtext.RichTextCtrl.SetInsertionPoint") instead.



Parameters
* **pos** (*long*) –
* **showAtLineStart** (*bool*) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaretBack(self, oldPosition: int) -> None:
        """ 

`MoveCaretBack`(*self*, *oldPosition*)[¶](#wx.richtext.RichTextCtrl.MoveCaretBack "Permalink to this definition")
Move the caret one visual step forward: this may mean setting a flag and keeping the same position if we’re going from the end of one line to the start of the next, which may be the exact same caret position.



Parameters
**oldPosition** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveCaretForward(self, oldPosition: int) -> None:
        """ 

`MoveCaretForward`(*self*, *oldPosition*)[¶](#wx.richtext.RichTextCtrl.MoveCaretForward "Permalink to this definition")
Move the caret one visual step forward: this may mean setting a flag and keeping the same position if we’re going from the end of one line to the start of the next, which may be the exact same caret position.



Parameters
**oldPosition** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveDown(self, noLines=1, flags=0) -> bool:
        """ 

`MoveDown`(*self*, *noLines=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveDown "Permalink to this definition")
Moves the caret down.



Parameters
* **noLines** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveEnd(self, flags: int=0) -> bool:
        """ 

`MoveEnd`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveEnd "Permalink to this definition")
Moves to the end of the buffer.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveHome(self, flags: int=0) -> bool:
        """ 

`MoveHome`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveHome "Permalink to this definition")
Moves to the start of the buffer.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveLeft(self, noPositions=1, flags=0) -> bool:
        """ 

`MoveLeft`(*self*, *noPositions=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveLeft "Permalink to this definition")
Moves left.



Parameters
* **noPositions** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveRight(self, noPositions=1, flags=0) -> bool:
        """ 

`MoveRight`(*self*, *noPositions=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveRight "Permalink to this definition")
Moves right.



Parameters
* **noPositions** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToLineEnd(self, flags: int=0) -> bool:
        """ 

`MoveToLineEnd`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveToLineEnd "Permalink to this definition")
Moves to the end of the line.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToLineStart(self, flags: int=0) -> bool:
        """ 

`MoveToLineStart`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveToLineStart "Permalink to this definition")
Moves to the start of the line.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToParagraphEnd(self, flags: int=0) -> bool:
        """ 

`MoveToParagraphEnd`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveToParagraphEnd "Permalink to this definition")
Moves to the end of the paragraph.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveToParagraphStart(self, flags: int=0) -> bool:
        """ 

`MoveToParagraphStart`(*self*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveToParagraphStart "Permalink to this definition")
Moves to the start of the paragraph.



Parameters
**flags** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def MoveUp(self, noLines=1, flags=0) -> bool:
        """ 

`MoveUp`(*self*, *noLines=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.MoveUp "Permalink to this definition")
Moves to the start of the paragraph.



Parameters
* **noLines** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Newline(self) -> bool:
        """ 

`Newline`(*self*)[¶](#wx.richtext.RichTextCtrl.Newline "Permalink to this definition")
Inserts a new paragraph at the current insertion point.



Return type
*bool*





See also


[`LineBreak`](#wx.richtext.RichTextCtrl.LineBreak "wx.richtext.RichTextCtrl.LineBreak") .





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def NumberList(self, *args, **kw) -> bool:
        """ 

`NumberList`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.NumberList "Permalink to this definition")
Numbers the paragraphs in the given range.


Pass flags to determine how the attributes are set.


Either the style definition or the name of the style definition (in the current sheet) can be passed.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.



See also


[`SetListStyle`](#wx.richtext.RichTextCtrl.SetListStyle "wx.richtext.RichTextCtrl.SetListStyle") , [`PromoteList`](#wx.richtext.RichTextCtrl.PromoteList "wx.richtext.RichTextCtrl.PromoteList") , [`ClearListStyle`](#wx.richtext.RichTextCtrl.ClearListStyle "wx.richtext.RichTextCtrl.ClearListStyle") .



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**NumberList** *(self, range, def=None, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **def** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**NumberList** *(self, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCaptureLost(self, event: 'MouseCaptureLostEvent') -> None:
        """ 

`OnCaptureLost`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnCaptureLost "Permalink to this definition")

Parameters
**event** ([*wx.MouseCaptureLostEvent*](wx.MouseCaptureLostEvent.html#wx.MouseCaptureLostEvent "wx.MouseCaptureLostEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnChar(self, event: 'KeyEvent') -> None:
        """ 

`OnChar`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnChar "Permalink to this definition")

Parameters
**event** ([*wx.KeyEvent*](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnClear(self, event: 'CommandEvent') -> None:
        """ 

`OnClear`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnClear "Permalink to this definition")
Standard handler for the `wx.ID_CLEAR` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnContextMenu(self, event: 'ContextMenuEvent') -> None:
        """ 

`OnContextMenu`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnContextMenu "Permalink to this definition")
Shows a standard context menu with undo, redo, cut, copy, paste, clear, and select all commands.



Parameters
**event** ([*wx.ContextMenuEvent*](wx.ContextMenuEvent.html#wx.ContextMenuEvent "wx.ContextMenuEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCopy(self, event: 'CommandEvent') -> None:
        """ 

`OnCopy`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnCopy "Permalink to this definition")
Standard handler for the `wx.ID_COPY` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnCut(self, event: 'CommandEvent') -> None:
        """ 

`OnCut`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnCut "Permalink to this definition")
Standard handler for the `wx.ID_CUT` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnDropFiles(self, event: 'DropFilesEvent') -> None:
        """ 

`OnDropFiles`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnDropFiles "Permalink to this definition")
Loads the first dropped file.



Parameters
**event** ([*wx.DropFilesEvent*](wx.DropFilesEvent.html#wx.DropFilesEvent "wx.DropFilesEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnEraseBackground(self, event: 'EraseEvent') -> None:
        """ 

`OnEraseBackground`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnEraseBackground "Permalink to this definition")

Parameters
**event** ([*wx.EraseEvent*](wx.EraseEvent.html#wx.EraseEvent "wx.EraseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnIdle(self, event: 'IdleEvent') -> None:
        """ 

`OnIdle`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnIdle "Permalink to this definition")

Parameters
**event** ([*wx.IdleEvent*](wx.IdleEvent.html#wx.IdleEvent "wx.IdleEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnKillFocus(self, event: 'FocusEvent') -> None:
        """ 

`OnKillFocus`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnKillFocus "Permalink to this definition")

Parameters
**event** ([*wx.FocusEvent*](wx.FocusEvent.html#wx.FocusEvent "wx.FocusEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftClick(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftClick`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnLeftClick "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftDClick(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftDClick`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnLeftDClick "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnLeftUp(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftUp`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnLeftUp "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnMiddleClick(self, event: 'MouseEvent') -> None:
        """ 

`OnMiddleClick`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnMiddleClick "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnMoveMouse(self, event: 'MouseEvent') -> None:
        """ 

`OnMoveMouse`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnMoveMouse "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnPaint(self, event: 'PaintEvent') -> None:
        """ 

`OnPaint`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnPaint "Permalink to this definition")

Parameters
**event** ([*wx.PaintEvent*](wx.PaintEvent.html#wx.PaintEvent "wx.PaintEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnPaste(self, event: 'CommandEvent') -> None:
        """ 

`OnPaste`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnPaste "Permalink to this definition")
Standard handler for the `wx.ID_PASTE` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnProperties(self, event: 'CommandEvent') -> None:
        """ 

`OnProperties`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnProperties "Permalink to this definition")
Standard handler for property commands.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnRedo(self, event: 'CommandEvent') -> None:
        """ 

`OnRedo`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnRedo "Permalink to this definition")
Standard handler for the `wx.ID_REDO` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnRightClick(self, event: 'MouseEvent') -> None:
        """ 

`OnRightClick`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnRightClick "Permalink to this definition")

Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnScroll(self, event: 'ScrollWinEvent') -> None:
        """ 

`OnScroll`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnScroll "Permalink to this definition")

Parameters
**event** ([*wx.ScrollWinEvent*](wx.ScrollWinEvent.html#wx.ScrollWinEvent "wx.ScrollWinEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSelectAll(self, event: 'CommandEvent') -> None:
        """ 

`OnSelectAll`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnSelectAll "Permalink to this definition")
Standard handler for the `wx.ID_SELECTALL` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSetFocus(self, event: 'FocusEvent') -> None:
        """ 

`OnSetFocus`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnSetFocus "Permalink to this definition")

Parameters
**event** ([*wx.FocusEvent*](wx.FocusEvent.html#wx.FocusEvent "wx.FocusEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSize(self, event: 'SizeEvent') -> None:
        """ 

`OnSize`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnSize "Permalink to this definition")

Parameters
**event** ([*wx.SizeEvent*](wx.SizeEvent.html#wx.SizeEvent "wx.SizeEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnSysColourChanged(self, event: 'SysColourChangedEvent') -> None:
        """ 

`OnSysColourChanged`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnSysColourChanged "Permalink to this definition")

Parameters
**event** ([*wx.SysColourChangedEvent*](wx.SysColourChangedEvent.html#wx.SysColourChangedEvent "wx.SysColourChangedEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnTimer(self, event: 'TimerEvent') -> None:
        """ 

`OnTimer`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnTimer "Permalink to this definition")
Respond to timer events.



Parameters
**event** ([*wx.TimerEvent*](wx.TimerEvent.html#wx.TimerEvent "wx.TimerEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUndo(self, event: 'CommandEvent') -> None:
        """ 

`OnUndo`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUndo "Permalink to this definition")
Standard handler for the `wx.ID_UNDO` command.



Parameters
**event** ([*wx.CommandEvent*](wx.CommandEvent.html#wx.CommandEvent "wx.CommandEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateClear(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateClear`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateClear "Permalink to this definition")
Standard update handler for the `wx.ID_CLEAR` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateCopy(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateCopy`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateCopy "Permalink to this definition")
Standard update handler for the `wx.ID_COPY` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateCut(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateCut`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateCut "Permalink to this definition")
Standard update handler for the `wx.ID_CUT` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdatePaste(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdatePaste`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdatePaste "Permalink to this definition")
Standard update handler for the `wx.ID_PASTE` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateProperties(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateProperties`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateProperties "Permalink to this definition")
Standard update handler for property commands.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateRedo(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateRedo`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateRedo "Permalink to this definition")
Standard update handler for the `wx.ID_REDO` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateSelectAll(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateSelectAll`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateSelectAll "Permalink to this definition")
Standard update handler for the `wx.ID_SELECTALL` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def OnUpdateUndo(self, event: 'UpdateUIEvent') -> None:
        """ 

`OnUpdateUndo`(*self*, *event*)[¶](#wx.richtext.RichTextCtrl.OnUpdateUndo "Permalink to this definition")
Standard update handler for the `wx.ID_UNDO` command.



Parameters
**event** ([*wx.UpdateUIEvent*](wx.UpdateUIEvent.html#wx.UpdateUIEvent "wx.UpdateUIEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PageDown(self, noPages=1, flags=0) -> bool:
        """ 

`PageDown`(*self*, *noPages=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.PageDown "Permalink to this definition")
Moves one or more pages down.



Parameters
* **noPages** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PageUp(self, noPages=1, flags=0) -> bool:
        """ 

`PageUp`(*self*, *noPages=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.PageUp "Permalink to this definition")
Moves one or more pages up.



Parameters
* **noPages** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PaintAboveContent(self, WXUNUSED: 'DC') -> None:
        """ 

`PaintAboveContent`(*self*, *WXUNUSED*)[¶](#wx.richtext.RichTextCtrl.PaintAboveContent "Permalink to this definition")
Other user defined painting after everything else (i.e. all text) is painted.



Parameters
**WXUNUSED** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 





New in version 2.9.1.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PaintBackground(self, dc: 'DC') -> None:
        """ 

`PaintBackground`(*self*, *dc*)[¶](#wx.richtext.RichTextCtrl.PaintBackground "Permalink to this definition")
Paints the background.



Parameters
**dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Paste(self) -> None:
        """ 

`Paste`(*self*)[¶](#wx.richtext.RichTextCtrl.Paste "Permalink to this definition")
Pastes content from the clipboard to the buffer.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PopStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`PopStyleSheet`(*self*)[¶](#wx.richtext.RichTextCtrl.PopStyleSheet "Permalink to this definition")
Pops the style sheet from top of stack.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PositionCaret(self, container: Optional['richtext.RichTextParagraphLayoutBox']=None) -> None:
        """ 

`PositionCaret`(*self*, *container=None*)[¶](#wx.richtext.RichTextCtrl.PositionCaret "Permalink to this definition")
Internal function to position the visible caret according to the current caret position.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PositionToXY(self, pos: int) -> tuple:
        """ 

`PositionToXY`(*self*, *pos*)[¶](#wx.richtext.RichTextCtrl.PositionToXY "Permalink to this definition")
Converts a text position to zero-based column and line numbers.



Parameters
**pos** (*long*) – 



Return type
*tuple*



Returns
( *bool*, *x*, *y* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PrepareContent(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`PrepareContent`(*self*, *container*)[¶](#wx.richtext.RichTextCtrl.PrepareContent "Permalink to this definition")
Prepares the content just before insertion (or after buffer reset).


Called by the same function in  [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer). Currently is only called if undo mode is on.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PrepareContextMenu(self, menu, pt, addPropertyCommands) -> int:
        """ 

`PrepareContextMenu`(*self*, *menu*, *pt*, *addPropertyCommands*)[¶](#wx.richtext.RichTextCtrl.PrepareContextMenu "Permalink to this definition")
Prepares the context menu, optionally adding appropriate property-editing commands.


Returns the number of property commands added.



Parameters
* **menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **addPropertyCommands** (*bool*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessBackKey(self, event, flags) -> bool:
        """ 

`ProcessBackKey`(*self*, *event*, *flags*)[¶](#wx.richtext.RichTextCtrl.ProcessBackKey "Permalink to this definition")
Processes the back key.



Parameters
* **event** ([*wx.KeyEvent*](wx.KeyEvent.html#wx.KeyEvent "wx.KeyEvent")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessDelayedImageLoading(self, *args, **kw) -> bool:
        """ 

`ProcessDelayedImageLoading`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.ProcessDelayedImageLoading "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ProcessDelayedImageLoading** *(self, refresh)*


Do delayed image loading and garbage-collect other images.



Parameters
**refresh** (*bool*) – 



Return type
*bool*






---

  



**ProcessDelayedImageLoading** *(self, screenRect, box, loadCount)*



Parameters
* **screenRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **box** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **loadCount** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ProcessMouseMovement(self, container, obj, position, pos) -> bool:
        """ 

`ProcessMouseMovement`(*self*, *container*, *obj*, *position*, *pos*)[¶](#wx.richtext.RichTextCtrl.ProcessMouseMovement "Permalink to this definition")
Processes mouse movement in order to change the cursor.



Parameters
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **position** (*long*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PromoteList(self, *args, **kw) -> bool:
        """ 

`PromoteList`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.PromoteList "Permalink to this definition")
Promotes or demotes the paragraphs in the given range.


A positive *promoteBy* produces a smaller indent, and a negative number produces a larger indent. Pass flags to determine how the attributes are set. Either the style definition or the name of the style definition (in the current sheet) can be passed.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.



See also


[`SetListStyle`](#wx.richtext.RichTextCtrl.SetListStyle "wx.richtext.RichTextCtrl.SetListStyle") ,




See also


[`SetListStyle`](#wx.richtext.RichTextCtrl.SetListStyle "wx.richtext.RichTextCtrl.SetListStyle") , [`ClearListStyle`](#wx.richtext.RichTextCtrl.ClearListStyle "wx.richtext.RichTextCtrl.ClearListStyle") .



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PromoteList** *(self, promoteBy, range, def=None, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, specifiedLevel=-1)*



Parameters
* **promoteBy** (*int*) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **def** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**PromoteList** *(self, promoteBy, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, specifiedLevel=-1)*



Parameters
* **promoteBy** (*int*) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def PushStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ 

`PushStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextCtrl.PushStyleSheet "Permalink to this definition")
Push the style sheet to top of stack.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Redo(self) -> None:
        """ 

`Redo`(*self*)[¶](#wx.richtext.RichTextCtrl.Redo "Permalink to this definition")
Redoes the current command.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def RefreshForSelectionChange(self, oldSelection, newSelection) -> bool:
        """ 

`RefreshForSelectionChange`(*self*, *oldSelection*, *newSelection*)[¶](#wx.richtext.RichTextCtrl.RefreshForSelectionChange "Permalink to this definition")
Refreshes the area affected by a selection change.



Parameters
* **oldSelection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **newSelection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Remove(self, from_, to_) -> None:
        """ 

`Remove`(*self*, *from\_*, *to\_*)[¶](#wx.richtext.RichTextCtrl.Remove "Permalink to this definition")
Removes the content in the specified range.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Replace(self, from_, to_, value) -> None:
        """ 

`Replace`(*self*, *from\_*, *to\_*, *value*)[¶](#wx.richtext.RichTextCtrl.Replace "Permalink to this definition")
Replaces the content in the specified range with the string specified by *value*.



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –
* **value** (*string*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def RequestDelayedImageProcessing(self) -> None:
        """ 

`RequestDelayedImageProcessing`(*self*)[¶](#wx.richtext.RichTextCtrl.RequestDelayedImageProcessing "Permalink to this definition")
Request delayed image processing.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SaveFile(self, file="", type=RICHTEXT_TYPE_ANY) -> bool:
        """ 

`SaveFile`(*self*, *file=""*, *type=RICHTEXT\_TYPE\_ANY*)[¶](#wx.richtext.RichTextCtrl.SaveFile "Permalink to this definition")
Saves the buffer content using the given type.


If the specified type is `wx.richtext.RICHTEXT_TYPE_ANY`, the type is deduced from the filename extension.


This function looks for a suitable  [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler) object.



Parameters
* **file** (*string*) –
* **type** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ScrollIntoView(self, position, keyCode) -> bool:
        """ 

`ScrollIntoView`(*self*, *position*, *keyCode*)[¶](#wx.richtext.RichTextCtrl.ScrollIntoView "Permalink to this definition")
Scrolls *position* into view.


This function takes a caret position.



Parameters
* **position** (*long*) –
* **keyCode** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectAll(self) -> None:
        """ 

`SelectAll`(*self*)[¶](#wx.richtext.RichTextCtrl.SelectAll "Permalink to this definition")
Selects all the text in the buffer.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectNone(self) -> None:
        """ 

`SelectNone`(*self*)[¶](#wx.richtext.RichTextCtrl.SelectNone "Permalink to this definition")
Cancels any selection.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SelectWord(self, position: int) -> bool:
        """ 

`SelectWord`(*self*, *position*)[¶](#wx.richtext.RichTextCtrl.SelectWord "Permalink to this definition")
Selects the word at the given character position.



Parameters
**position** (*long*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetAndShowDefaultStyle(self, attr: 'richtext.RichTextAttr') -> None:
        """ 

`SetAndShowDefaultStyle`(*self*, *attr*)[¶](#wx.richtext.RichTextCtrl.SetAndShowDefaultStyle "Permalink to this definition")
Sets `attr` as the default style and tells the control that the UI should reflect this attribute until the user moves the caret.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 





See also


[`IsDefaultStyleShowing`](#wx.richtext.RichTextCtrl.IsDefaultStyleShowing "wx.richtext.RichTextCtrl.IsDefaultStyleShowing") .





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetBasicStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ 

`SetBasicStyle`(*self*, *style*)[¶](#wx.richtext.RichTextCtrl.SetBasicStyle "Permalink to this definition")
Sets the basic (overall) style.


This is the style of the whole buffer before further styles are applied, unlike the default style, which only affects the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretAtLineStart(self, atStart: bool) -> None:
        """ 

`SetCaretAtLineStart`(*self*, *atStart*)[¶](#wx.richtext.RichTextCtrl.SetCaretAtLineStart "Permalink to this definition")
Sets a flag to remember that we are showing the caret position at the start of a line instead of at the end of the previous one.



Parameters
**atStart** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPosition(self, position, showAtLineStart=False) -> None:
        """ 

`SetCaretPosition`(*self*, *position*, *showAtLineStart=False*)[¶](#wx.richtext.RichTextCtrl.SetCaretPosition "Permalink to this definition")
Sets the caret position.


The caret position is the character position just before the caret. A value of -1 means the caret is at the start of the buffer. Please note that this does not update the current editing style from the new position or cause the actual caret to be refreshed; to do that, call [`wx.richtext.RichTextCtrl.SetInsertionPoint`](#wx.richtext.RichTextCtrl.SetInsertionPoint "wx.richtext.RichTextCtrl.SetInsertionPoint") instead.



Parameters
* **position** (*long*) –
* **showAtLineStart** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPositionAfterClick(self, container, position, hitTestFlags, extendSelection=False) -> bool:
        """ 

`SetCaretPositionAfterClick`(*self*, *container*, *position*, *hitTestFlags*, *extendSelection=False*)[¶](#wx.richtext.RichTextCtrl.SetCaretPositionAfterClick "Permalink to this definition")
Sets up the caret for the given position and container, after a mouse click.



Parameters
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **position** (*long*) –
* **hitTestFlags** (*int*) –
* **extendSelection** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetCaretPositionForDefaultStyle(self, pos: int) -> None:
        """ 

`SetCaretPositionForDefaultStyle`(*self*, *pos*)[¶](#wx.richtext.RichTextCtrl.SetCaretPositionForDefaultStyle "Permalink to this definition")
Set the caret position for the default style that the user is selecting.



Parameters
**pos** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetContextMenu(self, menu: 'Menu') -> None:
        """ 

`SetContextMenu`(*self*, *menu*)[¶](#wx.richtext.RichTextCtrl.SetContextMenu "Permalink to this definition")
Sets the current context menu.



Parameters
**menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDefaultStyle(self, *args, **kw) -> bool:
        """ 

`SetDefaultStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.SetDefaultStyle "Permalink to this definition")
Sets the current default style, which can be used to change how subsequently inserted text is displayed.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetDefaultStyle** *(self, style)*



Parameters
**style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) – 



Return type
*bool*






---

  



**SetDefaultStyle** *(self, style)*



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDefaultStyleToCursorStyle(self) -> bool:
        """ 

`SetDefaultStyleToCursorStyle`(*self*)[¶](#wx.richtext.RichTextCtrl.SetDefaultStyleToCursorStyle "Permalink to this definition")
Sets the default style to the style under the cursor.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedImageProcessingRequired(self, b: bool) -> None:
        """ 

`SetDelayedImageProcessingRequired`(*self*, *b*)[¶](#wx.richtext.RichTextCtrl.SetDelayedImageProcessingRequired "Permalink to this definition")
Sets the flag indicating that delayed image processing is required.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedImageProcessingTime(self, t: int) -> None:
        """ 

`SetDelayedImageProcessingTime`(*self*, *t*)[¶](#wx.richtext.RichTextCtrl.SetDelayedImageProcessingTime "Permalink to this definition")
Sets the last time delayed image processing was performed.



Parameters
**t** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDelayedLayoutThreshold(self, threshold: int) -> None:
        """ 

`SetDelayedLayoutThreshold`(*self*, *threshold*)[¶](#wx.richtext.RichTextCtrl.SetDelayedLayoutThreshold "Permalink to this definition")
Sets the size of the buffer beyond which layout is delayed during resizing.


This optimizes sizing for large buffers. The default is 20000.



Parameters
**threshold** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDimensionScale(self, dimScale, refresh=False) -> None:
        """ 

`SetDimensionScale`(*self*, *dimScale*, *refresh=False*)[¶](#wx.richtext.RichTextCtrl.SetDimensionScale "Permalink to this definition")
Sets the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.


This can be useful when editing in a small control where you still want legible text, but a minimum of wasted white space.



Parameters
* **dimScale** (*float*) –
* **refresh** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragStartPoint(self, sp: Union[tuple[int, int], 'Point']) -> None:
        """ 

`SetDragStartPoint`(*self*, *sp*)[¶](#wx.richtext.RichTextCtrl.SetDragStartPoint "Permalink to this definition")
Set the possible Drag’n’Drop start point.



Parameters
**sp** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragStartTime(self, st: 'DateTime') -> None:
        """ 

`SetDragStartTime`(*self*, *st*)[¶](#wx.richtext.RichTextCtrl.SetDragStartTime "Permalink to this definition")
Set the possible Drag’n’Drop start time.



Parameters
**st** ([*wx.DateTime*](wx.DateTime.html#wx.DateTime "wx.DateTime")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetDragging(self, dragging: bool) -> None:
        """ 

`SetDragging`(*self*, *dragging*)[¶](#wx.richtext.RichTextCtrl.SetDragging "Permalink to this definition")
Sets a flag to remember if we are extending a selection.



Parameters
**dragging** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetEditable(self, editable: bool) -> None:
        """ 

`SetEditable`(*self*, *editable*)[¶](#wx.richtext.RichTextCtrl.SetEditable "Permalink to this definition")
Makes the control editable, or not.



Parameters
**editable** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFilename(self, filename: str) -> None:
        """ 

`SetFilename`(*self*, *filename*)[¶](#wx.richtext.RichTextCtrl.SetFilename "Permalink to this definition")
Sets the current filename.



Parameters
**filename** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFocusObject(self, obj, setCaretPosition=True) -> bool:
        """ 

`SetFocusObject`(*self*, *obj*, *setCaretPosition=True*)[¶](#wx.richtext.RichTextCtrl.SetFocusObject "Permalink to this definition")
Sets the  [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject) object that currently has the editing focus.



Parameters
* **obj** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – The  [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject) to set focus on.
* **setCaretPosition** (*bool*) – Optionally set the caret position.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFont(self, font: 'Font') -> bool:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.richtext.RichTextCtrl.SetFont "Permalink to this definition")
Sets the font, and also the basic and default attributes (see [`wx.richtext.RichTextCtrl.SetDefaultStyle`](#wx.richtext.RichTextCtrl.SetDefaultStyle "wx.richtext.RichTextCtrl.SetDefaultStyle") ).



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFontScale(self, fontScale, refresh=False) -> None:
        """ 

`SetFontScale`(*self*, *fontScale*, *refresh=False*)[¶](#wx.richtext.RichTextCtrl.SetFontScale "Permalink to this definition")
Sets the scale factor for displaying fonts, for example for more comfortable editing.



Parameters
* **fontScale** (*float*) –
* **refresh** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutRequired(self, b: bool) -> None:
        """ 

`SetFullLayoutRequired`(*self*, *b*)[¶](#wx.richtext.RichTextCtrl.SetFullLayoutRequired "Permalink to this definition")

Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutSavedPosition(self, p: int) -> None:
        """ 

`SetFullLayoutSavedPosition`(*self*, *p*)[¶](#wx.richtext.RichTextCtrl.SetFullLayoutSavedPosition "Permalink to this definition")

Parameters
**p** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetFullLayoutTime(self, t: int) -> None:
        """ 

`SetFullLayoutTime`(*self*, *t*)[¶](#wx.richtext.RichTextCtrl.SetFullLayoutTime "Permalink to this definition")

Parameters
**t** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetHandlerFlags(self, flags: int) -> None:
        """ 

`SetHandlerFlags`(*self*, *flags*)[¶](#wx.richtext.RichTextCtrl.SetHandlerFlags "Permalink to this definition")
Sets flags that change the behaviour of loading or saving.


See the documentation for each handler class to see what flags are relevant for each handler.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetHint(self, hint: str) -> bool:
        """ 

`SetHint`(*self*, *hint*)[¶](#wx.richtext.RichTextCtrl.SetHint "Permalink to this definition")
Sets a hint shown in an empty unfocused text control.


The hints are usually used to indicate to the user what is supposed to be entered into the given entry field, e.g. a common use of them is to show an explanation of what can be entered in a  [wx.SearchCtrl](wx.SearchCtrl.html#wx-searchctrl).


The hint is shown (usually greyed out) for an empty control until it gets focus and is shown again if the control loses it and remains empty. It won’t be shown once the control has a non-empty value, although it will be shown again if the control contents is cleared. Because of this, it generally only makes sense to use hints with the controls which are initially empty.


Notice that hints are known as *cue banners* under MSW or *placeholder strings* under macOS.


For the platforms without native hints support, the implementation has several known limitations. Notably, the hint display will not be properly updated if you change  [wx.TextEntry](wx.TextEntry.html#wx-textentry) contents programmatically when the hint is displayed using methods other than [`SetValue`](#wx.richtext.RichTextCtrl.SetValue "wx.richtext.RichTextCtrl.SetValue") or [`ChangeValue`](#wx.richtext.RichTextCtrl.ChangeValue "wx.richtext.RichTextCtrl.ChangeValue") or others which use them internally (e.g. [`Clear`](#wx.richtext.RichTextCtrl.Clear "wx.richtext.RichTextCtrl.Clear") ). In other words, currently you should avoid calling methods such as [`WriteText`](#wx.richtext.RichTextCtrl.WriteText "wx.richtext.RichTextCtrl.WriteText") or [`Replace`](#wx.richtext.RichTextCtrl.Replace "wx.richtext.RichTextCtrl.Replace") when using hints and the text control is empty. If you bind to the control’s focus and wxEVT\_TEXT events, you must call [`wx.Event.Skip`](wx.Event.html#wx.Event.Skip "wx.Event.Skip") on them so that the generic implementation works correctly.


Another limitation is that hints are ignored for the controls with `TE_PASSWORD` style.



Parameters
**hint** (*string*) – 



Return type
*bool*





New in version 2.9.0.




Note


Currently implemented natively on Windows (Vista and later only), macOS and GTK+ (3.2 and later).




Note


Hints can be used for single line text controls under all platforms, but only MSW and GTK+ 2 support them for multi-line text controls, they are ignored for them under the other platforms.





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInsertionPoint(self, pos: int) -> None:
        """ 

`SetInsertionPoint`(*self*, *pos*)[¶](#wx.richtext.RichTextCtrl.SetInsertionPoint "Permalink to this definition")
Sets the insertion point and causes the current editing style to be taken from the new position (unlike [`wx.richtext.RichTextCtrl.SetCaretPosition`](#wx.richtext.RichTextCtrl.SetCaretPosition "wx.richtext.RichTextCtrl.SetCaretPosition") ).



Parameters
**pos** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInsertionPointEnd(self) -> None:
        """ 

`SetInsertionPointEnd`(*self*)[¶](#wx.richtext.RichTextCtrl.SetInsertionPointEnd "Permalink to this definition")
Sets the insertion point to the end of the text control.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetInternalSelectionRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetInternalSelectionRange`(*self*, *range*)[¶](#wx.richtext.RichTextCtrl.SetInternalSelectionRange "Permalink to this definition")
Sets the selection range in character positions.


-2, -2 means no selection -1, -1 means select everything. The range is in internal format, i.e. a single character selection is denoted by (n, n)



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetListStyle(self, *args, **kw) -> bool:
        """ 

`SetListStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.SetListStyle "Permalink to this definition")
Sets the list attributes for the given range, passing flags to determine how the attributes are set.


Either the style definition or the name of the style definition (in the current sheet) can be passed. *flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.



See also


[`NumberList`](#wx.richtext.RichTextCtrl.NumberList "wx.richtext.RichTextCtrl.NumberList") , [`PromoteList`](#wx.richtext.RichTextCtrl.PromoteList "wx.richtext.RichTextCtrl.PromoteList") , [`ClearListStyle`](#wx.richtext.RichTextCtrl.ClearListStyle "wx.richtext.RichTextCtrl.ClearListStyle") .



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetListStyle** *(self, range, styleDef, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **styleDef** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**SetListStyle** *(self, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ 

`SetMargins`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.SetMargins "Permalink to this definition")
Attempts to set the control margins.


When margins are given as  [wx.Point](wx.Point.html#wx-point), x indicates the left and y the top margin. Use -1 to indicate that an existing value should be used.



Returns
`True` if setting of all requested margins was successful.





New in version 2.9.1.



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetMargins** *(self, pt)*



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 



Return type
*bool*






---

  



**SetMargins** *(self, left, top=-1)*



Parameters
* **left** (*int*) –
* **top** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetMaxLength(self, len: int) -> None:
        """ 

`SetMaxLength`(*self*, *len*)[¶](#wx.richtext.RichTextCtrl.SetMaxLength "Permalink to this definition")
Sets the maximum number of characters that may be entered in a single line text control.


For compatibility only; currently does nothing.



Parameters
**len** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetModified(self, modified: bool) -> None:
        """ 

`SetModified`(*self*, *modified*)[¶](#wx.richtext.RichTextCtrl.SetModified "Permalink to this definition")

Parameters
**modified** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetPreDrag(self, pd: bool) -> None:
        """ 

`SetPreDrag`(*self*, *pd*)[¶](#wx.richtext.RichTextCtrl.SetPreDrag "Permalink to this definition")
Set if we’re trying to start Drag’n’Drop.



Parameters
**pd** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetProperties(self, range, properties, flags=RICHTEXT_SETPROPERTIES_WITH_UNDO) -> bool:
        """ 

`SetProperties`(*self*, *range*, *properties*, *flags=RICHTEXT\_SETPROPERTIES\_WITH\_UNDO*)[¶](#wx.richtext.RichTextCtrl.SetProperties "Permalink to this definition")
Sets the properties for the given range, passing flags to determine how the attributes are set.


You can merge properties or replace them.


The end point of range is specified as the last character position of the span of text, plus one. So, for example, to set the properties for a character at position 5, use the range (5,6).


*flags* may contain a bit list of the following values:


* `RICHTEXT_SETSPROPERTIES_NONE`: no flag.
* `wx.richtext.RICHTEXT_SETPROPERTIES_WITH_UNDO`: specifies that this operation should be undoable.
* `wx.richtext.RICHTEXT_SETPROPERTIES_PARAGRAPHS_ONLY`: specifies that the properties should only be applied to paragraphs, and not the content.
* `wx.richtext.RICHTEXT_SETPROPERTIES_CHARACTERS_ONLY`: specifies that the properties should only be applied to characters, and not the paragraph.
* `wx.richtext.RICHTEXT_SETPROPERTIES_RESET`: resets (clears) the existing properties before applying the new properties.
* `wx.richtext.RICHTEXT_SETPROPERTIES_REMOVE`: removes the specified properties.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **properties** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetScale(self, scale, refresh=False) -> None:
        """ 

`SetScale`(*self*, *scale*, *refresh=False*)[¶](#wx.richtext.RichTextCtrl.SetScale "Permalink to this definition")
Sets an overall scale factor for displaying and editing the content.



Parameters
* **scale** (*float*) –
* **refresh** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelection(self, *args, **kw) -> None:
        """ 

`SetSelection`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.SetSelection "Permalink to this definition")
Sets the selection to the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the selection for a character at position 5, use the range (5,6).


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetSelection** *(self, from\_, to\_)*



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –






---

  



**SetSelection** *(self, sel)*



Parameters
**sel** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionAnchor(self, anchor: int) -> None:
        """ 

`SetSelectionAnchor`(*self*, *anchor*)[¶](#wx.richtext.RichTextCtrl.SetSelectionAnchor "Permalink to this definition")
Sets an anchor so we know how to extend the selection.


It’s a caret position since it’s between two characters.



Parameters
**anchor** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionAnchorObject(self, anchor: 'richtext.RichTextObject') -> None:
        """ 

`SetSelectionAnchorObject`(*self*, *anchor*)[¶](#wx.richtext.RichTextCtrl.SetSelectionAnchorObject "Permalink to this definition")
Sets the anchor object if selecting multiple containers.



Parameters
**anchor** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetSelectionRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetSelectionRange`(*self*, *range*)[¶](#wx.richtext.RichTextCtrl.SetSelectionRange "Permalink to this definition")
Sets the selection to the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the selection for a character at position 5, use the range (5,6).



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyle(self, *args, **kw) -> bool:
        """ 

`SetStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.SetStyle "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetStyle** *(self, start, end, style)*


Sets the attributes for the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the style for a character at position 5, use the range (5,6).



Parameters
* **start** (*long*) –
* **end** (*long*) –
* **style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) –



Return type
*bool*






---

  



**SetStyle** *(self, start, end, style)*


Sets the attributes for the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the style for a character at position 5, use the range (5,6).



Parameters
* **start** (*long*) –
* **end** (*long*) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  



**SetStyle** *(self, range, style)*


Sets the attributes for the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the style for a character at position 5, use the range (5,6).



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) –



Return type
*bool*






---

  



**SetStyle** *(self, range, style)*


Sets the attributes for the given range.


The end point of range is specified as the last character position of the span of text, plus one.


So, for example, to set the style for a character at position 5, use the range (5,6).



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  



**SetStyle** *(self, obj, textAttr, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO)*


Sets the attributes for a single object.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **flags** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyleEx(self, range, style, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ 

`SetStyleEx`(*self*, *range*, *style*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO*)[¶](#wx.richtext.RichTextCtrl.SetStyleEx "Permalink to this definition")
Sets the attributes for the given range, passing flags to determine how the attributes are set.


The end point of range is specified as the last character position of the span of text, plus one. So, for example, to set the style for a character at position 5, use the range (5,6).


*flags* may contain a bit list of the following values:


* `wx.richtext.RICHTEXT_SETSTYLE_NONE`: no style flag.
* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this operation should be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_OPTIMIZE`: specifies that the style should not be applied if the combined style at this point is already the style in question.
* `wx.richtext.RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY`: specifies that the style should only be applied to paragraphs, and not the content. This allows content styling to be preserved independently from that of e.g. a named paragraph style.
* `wx.richtext.RICHTEXT_SETSTYLE_CHARACTERS_ONLY`: specifies that the style should only be applied to characters, and not the paragraph. This allows content styling to be preserved independently from that of e.g. a named paragraph style.
* `wx.richtext.RICHTEXT_SETSTYLE_RESET`: resets (clears) the existing style before applying the new style.
* `wx.richtext.RICHTEXT_SETSTYLE_REMOVE`: removes the specified style. Only the style flags are used in this operation.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextCtrl.SetStyleSheet "Permalink to this definition")
Sets the style sheet associated with the control.


A style sheet allows named character and paragraph styles to be applied.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetTextCursor(self, cursor: 'Cursor') -> None:
        """ 

`SetTextCursor`(*self*, *cursor*)[¶](#wx.richtext.RichTextCtrl.SetTextCursor "Permalink to this definition")
Sets the text (normal) cursor.



Parameters
**cursor** ([*wx.Cursor*](wx.Cursor.html#wx.Cursor "wx.Cursor")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetURLCursor(self, cursor: 'Cursor') -> None:
        """ 

`SetURLCursor`(*self*, *cursor*)[¶](#wx.richtext.RichTextCtrl.SetURLCursor "Permalink to this definition")
Sets the cursor to be used over URLs.



Parameters
**cursor** ([*wx.Cursor*](wx.Cursor.html#wx.Cursor "wx.Cursor")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetValue(self, value: str) -> None:
        """ 

`SetValue`(*self*, *value*)[¶](#wx.richtext.RichTextCtrl.SetValue "Permalink to this definition")
Replaces existing content with the given text.



Parameters
**value** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SetupScrollbars(self, atTop: bool=False) -> None:
        """ 

`SetupScrollbars`(*self*, *atTop=False*)[¶](#wx.richtext.RichTextCtrl.SetupScrollbars "Permalink to this definition")
A helper function setting up scrollbars, for example after a resize.



Parameters
**atTop** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShouldInheritColours(self) -> bool:
        """ 

`ShouldInheritColours`(*self*)[¶](#wx.richtext.RichTextCtrl.ShouldInheritColours "Permalink to this definition")
Return `True` from here to allow the colours of this window to be changed by `InheritAttributes` .


Returning `False` forbids inheriting them from the parent window.


The base class version returns `False`, but this method is overridden in  [wx.Control](wx.Control.html#wx-control) where it returns `True`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShowContextMenu(self, menu, pt, addPropertyCommands) -> bool:
        """ 

`ShowContextMenu`(*self*, *menu*, *pt*, *addPropertyCommands*)[¶](#wx.richtext.RichTextCtrl.ShowContextMenu "Permalink to this definition")
Shows the given context menu, optionally adding appropriate property-editing commands for the current position in the object hierarchy.



Parameters
* **menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **addPropertyCommands** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def ShowPosition(self, pos: int) -> None:
        """ 

`ShowPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextCtrl.ShowPosition "Permalink to this definition")
Scrolls the buffer so that the given position is in view.



Parameters
**pos** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def StartCellSelection(self, table, newCell) -> bool:
        """ 

`StartCellSelection`(*self*, *table*, *newCell*)[¶](#wx.richtext.RichTextCtrl.StartCellSelection "Permalink to this definition")
Starts selecting table cells.



Parameters
* **table** ([*wx.richtext.RichTextTable*](wx.richtext.RichTextTable.html#wx.richtext.RichTextTable "wx.richtext.RichTextTable")) –
* **newCell** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def StoreFocusObject(self, obj: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`StoreFocusObject`(*self*, *obj*)[¶](#wx.richtext.RichTextCtrl.StoreFocusObject "Permalink to this definition")
Setter for m\_focusObject.



Parameters
**obj** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def SuppressingUndo(self) -> bool:
        """ 

`SuppressingUndo`(*self*)[¶](#wx.richtext.RichTextCtrl.SuppressingUndo "Permalink to this definition")
Returns `True` if undo history suppression is on.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def Undo(self) -> None:
        """ 

`Undo`(*self*)[¶](#wx.richtext.RichTextCtrl.Undo "Permalink to this definition")
Undoes the command at the top of the command history, if there is one.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WordLeft(self, noPages=1, flags=0) -> bool:
        """ 

`WordLeft`(*self*, *noPages=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.WordLeft "Permalink to this definition")
Moves a number of words to the left.



Parameters
* **noPages** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WordRight(self, noPages=1, flags=0) -> bool:
        """ 

`WordRight`(*self*, *noPages=1*, *flags=0*)[¶](#wx.richtext.RichTextCtrl.WordRight "Permalink to this definition")
Move a number of words to the right.



Parameters
* **noPages** (*int*) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteField(*args, **kwargs) -> 'RichTextField':
        """ 

`WriteField`(*self*, *fieldType*, *properties*, *textAttr=RichTextAttr()*)[¶](#wx.richtext.RichTextCtrl.WriteField "Permalink to this definition")
Writes a field at the current insertion point.



Parameters
* **fieldType** (*string*) – The field type, matching an existing field type definition.
* **properties** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – Extra data for the field.
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – Optional attributes.



Return type
 [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield)





See also


 [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield),  [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype),  [wx.richtext.RichTextFieldTypeStandard](wx.richtext.RichTextFieldTypeStandard.html#wx-richtext-richtextfieldtypestandard)





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteImage(self, *args, **kw) -> bool:
        """ 

`WriteImage`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCtrl.WriteImage "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**WriteImage** *(self, image, bitmapType=BITMAP\_TYPE\_PNG, textAttr=RichTextAttr())*


Write a bitmap or image at the current insertion point.


Supply an optional type to use for internal and file storage of the raw data.



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **bitmapType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  



**WriteImage** *(self, bitmap, bitmapType=BITMAP\_TYPE\_PNG, textAttr=RichTextAttr())*


Write a bitmap or image at the current insertion point.


Supply an optional type to use for internal and file storage of the raw data.



Parameters
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) –
* **bitmapType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  



**WriteImage** *(self, filename, bitmapType, textAttr=RichTextAttr())*


Loads an image from a file and writes it at the current insertion point.



Parameters
* **filename** (*string*) –
* **bitmapType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  



**WriteImage** *(self, imageBlock, textAttr=RichTextAttr())*


Writes an image block at the current insertion point.



Parameters
* **imageBlock** ([*wx.richtext.RichTextImageBlock*](wx.richtext.RichTextImageBlock.html#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteTable(*args, **kwargs) -> 'RichTextTable':
        """ 

`WriteTable`(*self*, *rows*, *cols*, *tableAttr=RichTextAttr()*, *cellAttr=RichTextAttr()*)[¶](#wx.richtext.RichTextCtrl.WriteTable "Permalink to this definition")
Write a table at the current insertion point, returning the table.


You can then call [`SetFocusObject`](#wx.richtext.RichTextCtrl.SetFocusObject "wx.richtext.RichTextCtrl.SetFocusObject") to set the focus to the new object.



Parameters
* **rows** (*int*) –
* **cols** (*int*) –
* **tableAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **cellAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextTable](wx.richtext.RichTextTable.html#wx-richtext-richtexttable)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteText(self, text: str) -> None:
        """ 

`WriteText`(*self*, *text*)[¶](#wx.richtext.RichTextCtrl.WriteText "Permalink to this definition")
Writes text at the current position.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def WriteTextBox(*args, **kwargs) -> 'RichTextBox':
        """ 

`WriteTextBox`(*self*, *textAttr=RichTextAttr()*)[¶](#wx.richtext.RichTextCtrl.WriteTextBox "Permalink to this definition")
Write a text box at the current insertion point, returning the text box.


You can then call [`SetFocusObject`](#wx.richtext.RichTextCtrl.SetFocusObject "wx.richtext.RichTextCtrl.SetFocusObject") to set the focus to the new object.



Parameters
**textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
 [wx.richtext.RichTextBox](wx.richtext.RichTextBox.html#wx-richtext-richtextbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    def XYToPosition(self, x, y) -> int:
        """ 

`XYToPosition`(*self*, *x*, *y*)[¶](#wx.richtext.RichTextCtrl.XYToPosition "Permalink to this definition")
Translates from column and line number to position.



Parameters
* **x** (*long*) –
* **y** (*long*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCtrl.html
        """

    BasicStyle: 'RichTextAttr'  # `BasicStyle`[¶](#wx.richtext.RichTextCtrl.BasicStyle "Permalink to this definition")See [`GetBasicStyle`](#wx.richtext.RichTextCtrl.GetBasicStyle "wx.richtext.RichTextCtrl.GetBasicStyle") and [`SetBasicStyle`](#wx.richtext.RichTextCtrl.SetBasicStyle "wx.richtext.RichTextCtrl.SetBasicStyle")
    Buffer: 'RichTextBuffer'  # `Buffer`[¶](#wx.richtext.RichTextCtrl.Buffer "Permalink to this definition")See [`GetBuffer`](#wx.richtext.RichTextCtrl.GetBuffer "wx.richtext.RichTextCtrl.GetBuffer")
    CaretAtLineStart: bool  # `CaretAtLineStart`[¶](#wx.richtext.RichTextCtrl.CaretAtLineStart "Permalink to this definition")See [`GetCaretAtLineStart`](#wx.richtext.RichTextCtrl.GetCaretAtLineStart "wx.richtext.RichTextCtrl.GetCaretAtLineStart") and [`SetCaretAtLineStart`](#wx.richtext.RichTextCtrl.SetCaretAtLineStart "wx.richtext.RichTextCtrl.SetCaretAtLineStart")
    CaretPosition: int  # `CaretPosition`[¶](#wx.richtext.RichTextCtrl.CaretPosition "Permalink to this definition")See [`GetCaretPosition`](#wx.richtext.RichTextCtrl.GetCaretPosition "wx.richtext.RichTextCtrl.GetCaretPosition") and [`SetCaretPosition`](#wx.richtext.RichTextCtrl.SetCaretPosition "wx.richtext.RichTextCtrl.SetCaretPosition")
    CaretPositionForDefaultStyle: int  # `CaretPositionForDefaultStyle`[¶](#wx.richtext.RichTextCtrl.CaretPositionForDefaultStyle "Permalink to this definition")See [`GetCaretPositionForDefaultStyle`](#wx.richtext.RichTextCtrl.GetCaretPositionForDefaultStyle "wx.richtext.RichTextCtrl.GetCaretPositionForDefaultStyle") and [`SetCaretPositionForDefaultStyle`](#wx.richtext.RichTextCtrl.SetCaretPositionForDefaultStyle "wx.richtext.RichTextCtrl.SetCaretPositionForDefaultStyle")
    CommandProcessor: '_CommandProcessor'  # `CommandProcessor`[¶](#wx.richtext.RichTextCtrl.CommandProcessor "Permalink to this definition")See [`GetCommandProcessor`](#wx.richtext.RichTextCtrl.GetCommandProcessor "wx.richtext.RichTextCtrl.GetCommandProcessor")
    ContextMenu: 'Menu'  # `ContextMenu`[¶](#wx.richtext.RichTextCtrl.ContextMenu "Permalink to this definition")See [`GetContextMenu`](#wx.richtext.RichTextCtrl.GetContextMenu "wx.richtext.RichTextCtrl.GetContextMenu") and [`SetContextMenu`](#wx.richtext.RichTextCtrl.SetContextMenu "wx.richtext.RichTextCtrl.SetContextMenu")
    ContextMenuPropertiesInfo: 'RichTextContextMenuPropertiesInfo'  # `ContextMenuPropertiesInfo`[¶](#wx.richtext.RichTextCtrl.ContextMenuPropertiesInfo "Permalink to this definition")See [`GetContextMenuPropertiesInfo`](#wx.richtext.RichTextCtrl.GetContextMenuPropertiesInfo "wx.richtext.RichTextCtrl.GetContextMenuPropertiesInfo")
    DefaultStyle: Any  # `DefaultStyle`[¶](#wx.richtext.RichTextCtrl.DefaultStyle "Permalink to this definition")See `GetDefaultStyle` and [`SetDefaultStyle`](#wx.richtext.RichTextCtrl.SetDefaultStyle "wx.richtext.RichTextCtrl.SetDefaultStyle")
    DefaultStyleEx: 'RichTextAttr'  # `DefaultStyleEx`[¶](#wx.richtext.RichTextCtrl.DefaultStyleEx "Permalink to this definition")See [`GetDefaultStyleEx`](#wx.richtext.RichTextCtrl.GetDefaultStyleEx "wx.richtext.RichTextCtrl.GetDefaultStyleEx")
    DelayedImageLoading: bool  # `DelayedImageLoading`[¶](#wx.richtext.RichTextCtrl.DelayedImageLoading "Permalink to this definition")See [`GetDelayedImageLoading`](#wx.richtext.RichTextCtrl.GetDelayedImageLoading "wx.richtext.RichTextCtrl.GetDelayedImageLoading")
    DelayedImageProcessingRequired: bool  # `DelayedImageProcessingRequired`[¶](#wx.richtext.RichTextCtrl.DelayedImageProcessingRequired "Permalink to this definition")See [`GetDelayedImageProcessingRequired`](#wx.richtext.RichTextCtrl.GetDelayedImageProcessingRequired "wx.richtext.RichTextCtrl.GetDelayedImageProcessingRequired") and [`SetDelayedImageProcessingRequired`](#wx.richtext.RichTextCtrl.SetDelayedImageProcessingRequired "wx.richtext.RichTextCtrl.SetDelayedImageProcessingRequired")
    DelayedImageProcessingTime: int  # `DelayedImageProcessingTime`[¶](#wx.richtext.RichTextCtrl.DelayedImageProcessingTime "Permalink to this definition")See [`GetDelayedImageProcessingTime`](#wx.richtext.RichTextCtrl.GetDelayedImageProcessingTime "wx.richtext.RichTextCtrl.GetDelayedImageProcessingTime") and [`SetDelayedImageProcessingTime`](#wx.richtext.RichTextCtrl.SetDelayedImageProcessingTime "wx.richtext.RichTextCtrl.SetDelayedImageProcessingTime")
    DelayedLayoutThreshold: int  # `DelayedLayoutThreshold`[¶](#wx.richtext.RichTextCtrl.DelayedLayoutThreshold "Permalink to this definition")See [`GetDelayedLayoutThreshold`](#wx.richtext.RichTextCtrl.GetDelayedLayoutThreshold "wx.richtext.RichTextCtrl.GetDelayedLayoutThreshold") and [`SetDelayedLayoutThreshold`](#wx.richtext.RichTextCtrl.SetDelayedLayoutThreshold "wx.richtext.RichTextCtrl.SetDelayedLayoutThreshold")
    DimensionScale: float  # `DimensionScale`[¶](#wx.richtext.RichTextCtrl.DimensionScale "Permalink to this definition")See [`GetDimensionScale`](#wx.richtext.RichTextCtrl.GetDimensionScale "wx.richtext.RichTextCtrl.GetDimensionScale") and [`SetDimensionScale`](#wx.richtext.RichTextCtrl.SetDimensionScale "wx.richtext.RichTextCtrl.SetDimensionScale")
    DragStartPoint: 'Point'  # `DragStartPoint`[¶](#wx.richtext.RichTextCtrl.DragStartPoint "Permalink to this definition")See [`GetDragStartPoint`](#wx.richtext.RichTextCtrl.GetDragStartPoint "wx.richtext.RichTextCtrl.GetDragStartPoint") and [`SetDragStartPoint`](#wx.richtext.RichTextCtrl.SetDragStartPoint "wx.richtext.RichTextCtrl.SetDragStartPoint")
    DragStartTime: 'DateTime'  # `DragStartTime`[¶](#wx.richtext.RichTextCtrl.DragStartTime "Permalink to this definition")See [`GetDragStartTime`](#wx.richtext.RichTextCtrl.GetDragStartTime "wx.richtext.RichTextCtrl.GetDragStartTime") and [`SetDragStartTime`](#wx.richtext.RichTextCtrl.SetDragStartTime "wx.richtext.RichTextCtrl.SetDragStartTime")
    Dragging: bool  # `Dragging`[¶](#wx.richtext.RichTextCtrl.Dragging "Permalink to this definition")See [`GetDragging`](#wx.richtext.RichTextCtrl.GetDragging "wx.richtext.RichTextCtrl.GetDragging") and [`SetDragging`](#wx.richtext.RichTextCtrl.SetDragging "wx.richtext.RichTextCtrl.SetDragging")
    Filename: str  # `Filename`[¶](#wx.richtext.RichTextCtrl.Filename "Permalink to this definition")See [`GetFilename`](#wx.richtext.RichTextCtrl.GetFilename "wx.richtext.RichTextCtrl.GetFilename") and [`SetFilename`](#wx.richtext.RichTextCtrl.SetFilename "wx.richtext.RichTextCtrl.SetFilename")
    FirstVisiblePoint: 'Point'  # `FirstVisiblePoint`[¶](#wx.richtext.RichTextCtrl.FirstVisiblePoint "Permalink to this definition")See [`GetFirstVisiblePoint`](#wx.richtext.RichTextCtrl.GetFirstVisiblePoint "wx.richtext.RichTextCtrl.GetFirstVisiblePoint")
    FirstVisiblePosition: int  # `FirstVisiblePosition`[¶](#wx.richtext.RichTextCtrl.FirstVisiblePosition "Permalink to this definition")See [`GetFirstVisiblePosition`](#wx.richtext.RichTextCtrl.GetFirstVisiblePosition "wx.richtext.RichTextCtrl.GetFirstVisiblePosition")
    FocusObject: 'RichTextParagraphLayoutBox'  # `FocusObject`[¶](#wx.richtext.RichTextCtrl.FocusObject "Permalink to this definition")See [`GetFocusObject`](#wx.richtext.RichTextCtrl.GetFocusObject "wx.richtext.RichTextCtrl.GetFocusObject") and [`SetFocusObject`](#wx.richtext.RichTextCtrl.SetFocusObject "wx.richtext.RichTextCtrl.SetFocusObject")
    FontScale: float  # `FontScale`[¶](#wx.richtext.RichTextCtrl.FontScale "Permalink to this definition")See [`GetFontScale`](#wx.richtext.RichTextCtrl.GetFontScale "wx.richtext.RichTextCtrl.GetFontScale") and [`SetFontScale`](#wx.richtext.RichTextCtrl.SetFontScale "wx.richtext.RichTextCtrl.SetFontScale")
    FullLayoutRequired: bool  # `FullLayoutRequired`[¶](#wx.richtext.RichTextCtrl.FullLayoutRequired "Permalink to this definition")See [`GetFullLayoutRequired`](#wx.richtext.RichTextCtrl.GetFullLayoutRequired "wx.richtext.RichTextCtrl.GetFullLayoutRequired") and [`SetFullLayoutRequired`](#wx.richtext.RichTextCtrl.SetFullLayoutRequired "wx.richtext.RichTextCtrl.SetFullLayoutRequired")
    FullLayoutSavedPosition: int  # `FullLayoutSavedPosition`[¶](#wx.richtext.RichTextCtrl.FullLayoutSavedPosition "Permalink to this definition")See [`GetFullLayoutSavedPosition`](#wx.richtext.RichTextCtrl.GetFullLayoutSavedPosition "wx.richtext.RichTextCtrl.GetFullLayoutSavedPosition") and [`SetFullLayoutSavedPosition`](#wx.richtext.RichTextCtrl.SetFullLayoutSavedPosition "wx.richtext.RichTextCtrl.SetFullLayoutSavedPosition")
    FullLayoutTime: int  # `FullLayoutTime`[¶](#wx.richtext.RichTextCtrl.FullLayoutTime "Permalink to this definition")See [`GetFullLayoutTime`](#wx.richtext.RichTextCtrl.GetFullLayoutTime "wx.richtext.RichTextCtrl.GetFullLayoutTime") and [`SetFullLayoutTime`](#wx.richtext.RichTextCtrl.SetFullLayoutTime "wx.richtext.RichTextCtrl.SetFullLayoutTime")
    HandlerFlags: int  # `HandlerFlags`[¶](#wx.richtext.RichTextCtrl.HandlerFlags "Permalink to this definition")See [`GetHandlerFlags`](#wx.richtext.RichTextCtrl.GetHandlerFlags "wx.richtext.RichTextCtrl.GetHandlerFlags") and [`SetHandlerFlags`](#wx.richtext.RichTextCtrl.SetHandlerFlags "wx.richtext.RichTextCtrl.SetHandlerFlags")
    Hint: str  # `Hint`[¶](#wx.richtext.RichTextCtrl.Hint "Permalink to this definition")See [`GetHint`](#wx.richtext.RichTextCtrl.GetHint "wx.richtext.RichTextCtrl.GetHint") and [`SetHint`](#wx.richtext.RichTextCtrl.SetHint "wx.richtext.RichTextCtrl.SetHint")
    ImagesEnabled: bool  # `ImagesEnabled`[¶](#wx.richtext.RichTextCtrl.ImagesEnabled "Permalink to this definition")See [`GetImagesEnabled`](#wx.richtext.RichTextCtrl.GetImagesEnabled "wx.richtext.RichTextCtrl.GetImagesEnabled")
    InsertionPoint: int  # `InsertionPoint`[¶](#wx.richtext.RichTextCtrl.InsertionPoint "Permalink to this definition")See [`GetInsertionPoint`](#wx.richtext.RichTextCtrl.GetInsertionPoint "wx.richtext.RichTextCtrl.GetInsertionPoint") and [`SetInsertionPoint`](#wx.richtext.RichTextCtrl.SetInsertionPoint "wx.richtext.RichTextCtrl.SetInsertionPoint")
    InternalSelectionRange: 'RichTextRange'  # `InternalSelectionRange`[¶](#wx.richtext.RichTextCtrl.InternalSelectionRange "Permalink to this definition")See [`GetInternalSelectionRange`](#wx.richtext.RichTextCtrl.GetInternalSelectionRange "wx.richtext.RichTextCtrl.GetInternalSelectionRange") and [`SetInternalSelectionRange`](#wx.richtext.RichTextCtrl.SetInternalSelectionRange "wx.richtext.RichTextCtrl.SetInternalSelectionRange")
    LastPosition: 'TextPos'  # `LastPosition`[¶](#wx.richtext.RichTextCtrl.LastPosition "Permalink to this definition")See [`GetLastPosition`](#wx.richtext.RichTextCtrl.GetLastPosition "wx.richtext.RichTextCtrl.GetLastPosition")
    Margins: 'Point'  # `Margins`[¶](#wx.richtext.RichTextCtrl.Margins "Permalink to this definition")See [`GetMargins`](#wx.richtext.RichTextCtrl.GetMargins "wx.richtext.RichTextCtrl.GetMargins") and [`SetMargins`](#wx.richtext.RichTextCtrl.SetMargins "wx.richtext.RichTextCtrl.SetMargins")
    NumberOfLines: int  # `NumberOfLines`[¶](#wx.richtext.RichTextCtrl.NumberOfLines "Permalink to this definition")See [`GetNumberOfLines`](#wx.richtext.RichTextCtrl.GetNumberOfLines "wx.richtext.RichTextCtrl.GetNumberOfLines")
    PreDrag: bool  # `PreDrag`[¶](#wx.richtext.RichTextCtrl.PreDrag "Permalink to this definition")See [`GetPreDrag`](#wx.richtext.RichTextCtrl.GetPreDrag "wx.richtext.RichTextCtrl.GetPreDrag") and [`SetPreDrag`](#wx.richtext.RichTextCtrl.SetPreDrag "wx.richtext.RichTextCtrl.SetPreDrag")
    Scale: float  # `Scale`[¶](#wx.richtext.RichTextCtrl.Scale "Permalink to this definition")See [`GetScale`](#wx.richtext.RichTextCtrl.GetScale "wx.richtext.RichTextCtrl.GetScale") and [`SetScale`](#wx.richtext.RichTextCtrl.SetScale "wx.richtext.RichTextCtrl.SetScale")
    Selection: 'RichTextSelection'  # `Selection`[¶](#wx.richtext.RichTextCtrl.Selection "Permalink to this definition")See [`GetSelection`](#wx.richtext.RichTextCtrl.GetSelection "wx.richtext.RichTextCtrl.GetSelection") and [`SetSelection`](#wx.richtext.RichTextCtrl.SetSelection "wx.richtext.RichTextCtrl.SetSelection")
    SelectionAnchor: int  # `SelectionAnchor`[¶](#wx.richtext.RichTextCtrl.SelectionAnchor "Permalink to this definition")See [`GetSelectionAnchor`](#wx.richtext.RichTextCtrl.GetSelectionAnchor "wx.richtext.RichTextCtrl.GetSelectionAnchor") and [`SetSelectionAnchor`](#wx.richtext.RichTextCtrl.SetSelectionAnchor "wx.richtext.RichTextCtrl.SetSelectionAnchor")
    SelectionAnchorObject: 'RichTextObject'  # `SelectionAnchorObject`[¶](#wx.richtext.RichTextCtrl.SelectionAnchorObject "Permalink to this definition")See [`GetSelectionAnchorObject`](#wx.richtext.RichTextCtrl.GetSelectionAnchorObject "wx.richtext.RichTextCtrl.GetSelectionAnchorObject") and [`SetSelectionAnchorObject`](#wx.richtext.RichTextCtrl.SetSelectionAnchorObject "wx.richtext.RichTextCtrl.SetSelectionAnchorObject")
    SelectionRange: 'RichTextRange'  # `SelectionRange`[¶](#wx.richtext.RichTextCtrl.SelectionRange "Permalink to this definition")See [`GetSelectionRange`](#wx.richtext.RichTextCtrl.GetSelectionRange "wx.richtext.RichTextCtrl.GetSelectionRange") and [`SetSelectionRange`](#wx.richtext.RichTextCtrl.SetSelectionRange "wx.richtext.RichTextCtrl.SetSelectionRange")
    StringSelection: str  # `StringSelection`[¶](#wx.richtext.RichTextCtrl.StringSelection "Permalink to this definition")See [`GetStringSelection`](#wx.richtext.RichTextCtrl.GetStringSelection "wx.richtext.RichTextCtrl.GetStringSelection")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextCtrl.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextCtrl.GetStyleSheet "wx.richtext.RichTextCtrl.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextCtrl.SetStyleSheet "wx.richtext.RichTextCtrl.SetStyleSheet")
    TextCursor: 'Cursor'  # `TextCursor`[¶](#wx.richtext.RichTextCtrl.TextCursor "Permalink to this definition")See [`GetTextCursor`](#wx.richtext.RichTextCtrl.GetTextCursor "wx.richtext.RichTextCtrl.GetTextCursor") and [`SetTextCursor`](#wx.richtext.RichTextCtrl.SetTextCursor "wx.richtext.RichTextCtrl.SetTextCursor")
    URLCursor: 'Cursor'  # `URLCursor`[¶](#wx.richtext.RichTextCtrl.URLCursor "Permalink to this definition")See [`GetURLCursor`](#wx.richtext.RichTextCtrl.GetURLCursor "wx.richtext.RichTextCtrl.GetURLCursor") and [`SetURLCursor`](#wx.richtext.RichTextCtrl.SetURLCursor "wx.richtext.RichTextCtrl.SetURLCursor")
    Value: str  # `Value`[¶](#wx.richtext.RichTextCtrl.Value "Permalink to this definition")See [`GetValue`](#wx.richtext.RichTextCtrl.GetValue "wx.richtext.RichTextCtrl.GetValue") and [`SetValue`](#wx.richtext.RichTextCtrl.SetValue "wx.richtext.RichTextCtrl.SetValue")
    VerticalScrollbarEnabled: bool  # `VerticalScrollbarEnabled`[¶](#wx.richtext.RichTextCtrl.VerticalScrollbarEnabled "Permalink to this definition")See [`GetVerticalScrollbarEnabled`](#wx.richtext.RichTextCtrl.GetVerticalScrollbarEnabled "wx.richtext.RichTextCtrl.GetVerticalScrollbarEnabled")
    VirtualAttributesEnabled: bool  # `VirtualAttributesEnabled`[¶](#wx.richtext.RichTextCtrl.VirtualAttributesEnabled "Permalink to this definition")See [`GetVirtualAttributesEnabled`](#wx.richtext.RichTextCtrl.GetVirtualAttributesEnabled "wx.richtext.RichTextCtrl.GetVirtualAttributesEnabled")



RE_CENTRE_CARET: int  # The control will try to keep the caret line centred vertically while editing. wx.richtext.RE_CENTER_CARET is a synonym for this style.

RE_MULTILINE: int  # The control will be multiline (mandatory).

RE_READONLY: int  # The control will not be editable. ^^

RE_CENTER_CARET: int

TEXT_ATTR_URL: int

ID_CLEAR: int

ID_COPY: int

ID_CUT: int

ID_PASTE: int

ID_REDO: int

ID_SELECTALL: int

ID_UNDO: int

RICHTEXT_SETSTYLE_WITH_UNDO: int

RICHTEXT_TYPE_ANY: int

RICHTEXT_SETSTYLE_RENUMBER: int

RICHTEXT_SETSTYLE_SPECIFY_LEVEL: int

RICHTEXT_SETPROPERTIES_WITH_UNDO: int

RICHTEXT_SETPROPERTIES_PARAGRAPHS_ONLY: int

RICHTEXT_SETPROPERTIES_CHARACTERS_ONLY: int

RICHTEXT_SETPROPERTIES_RESET: int

RICHTEXT_SETPROPERTIES_REMOVE: int

RICHTEXT_SETSTYLE_NONE: int

RICHTEXT_SETSTYLE_OPTIMIZE: int

RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY: int

RICHTEXT_SETSTYLE_CHARACTERS_ONLY: int

RICHTEXT_SETSTYLE_RESET: int

RICHTEXT_SETSTYLE_REMOVE: int

class RichTextStyleComboCtrl(ComboCtrl):
    """ **Possible constructors**:



```
RichTextStyleComboCtrl(parent, id=ID_ANY, pos=DefaultPosition,
                       size=DefaultSize, style=0)

RichTextStyleComboCtrl()

```


This is a combo control that can display the styles in a
RichTextStyleSheet, and apply the selection to an associated
RichTextCtrl.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextStyleComboCtrl.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*


Constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  



**\_\_init\_\_** *(self)*




---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.richtext.RichTextStyleComboCtrl.Create "Permalink to this definition")
Creates the windows.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextStyleComboCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ 

`GetRichTextCtrl`(*self*)[¶](#wx.richtext.RichTextStyleComboCtrl.GetRichTextCtrl "Permalink to this definition")
Returns the  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl) associated with this control.



Return type
 [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextStyleComboCtrl.GetStyleSheet "Permalink to this definition")
Returns the style sheet associated with this control.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ 

`SetRichTextCtrl`(*self*, *ctrl*)[¶](#wx.richtext.RichTextStyleComboCtrl.SetRichTextCtrl "Permalink to this definition")
Associates the control with a  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl).



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextStyleComboCtrl.SetStyleSheet "Permalink to this definition")
Associates the control with a style sheet.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    def UpdateStyles(self) -> None:
        """ 

`UpdateStyles`(*self*)[¶](#wx.richtext.RichTextStyleComboCtrl.UpdateStyles "Permalink to this definition")
Updates the combo control from the associated style sheet.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleComboCtrl.html
        """

    RichTextCtrl: 'RichTextCtrl'  # `RichTextCtrl`[¶](#wx.richtext.RichTextStyleComboCtrl.RichTextCtrl "Permalink to this definition")See [`GetRichTextCtrl`](#wx.richtext.RichTextStyleComboCtrl.GetRichTextCtrl "wx.richtext.RichTextStyleComboCtrl.GetRichTextCtrl") and [`SetRichTextCtrl`](#wx.richtext.RichTextStyleComboCtrl.SetRichTextCtrl "wx.richtext.RichTextStyleComboCtrl.SetRichTextCtrl")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextStyleComboCtrl.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextStyleComboCtrl.GetStyleSheet "wx.richtext.RichTextStyleComboCtrl.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextStyleComboCtrl.SetStyleSheet "wx.richtext.RichTextStyleComboCtrl.SetStyleSheet")



class RichTextCommand(Command):
    """ **Possible constructors**:



```
RichTextCommand(name, id, buffer, container, ctrl,
                ignoreFirstTime=False)

RichTextCommand(name)

```


Implements a command on the undo/redo stack.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCommand.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, name, id, buffer, container, ctrl, ignoreFirstTime=False)*


Constructor for one action.



Parameters
* **name** (*string*) –
* **id** ([*RichTextCommandId*](wx.richtext.RichTextCommandId.enumeration.html "RichTextCommandId")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **ignoreFirstTime** (*bool*) –






---

  



**\_\_init\_\_** *(self, name)*


Constructor for multiple actions.



Parameters
**name** (*string*) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def AddAction(self, action: 'richtext.RichTextAction') -> None:
        """ 

`AddAction`(*self*, *action*)[¶](#wx.richtext.RichTextCommand.AddAction "Permalink to this definition")
Adds an action to the action list.



Parameters
**action** ([*wx.richtext.RichTextAction*](wx.richtext.RichTextAction.html#wx.richtext.RichTextAction "wx.richtext.RichTextAction")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def ClearActions(self) -> None:
        """ 

`ClearActions`(*self*)[¶](#wx.richtext.RichTextCommand.ClearActions "Permalink to this definition")
Clears the action list.




            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def Do(self) -> bool:
        """ 

`Do`(*self*)[¶](#wx.richtext.RichTextCommand.Do "Permalink to this definition")
Performs the command.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def GetActions(self) -> 'RichTextActionList':
        """ 

`GetActions`(*self*)[¶](#wx.richtext.RichTextCommand.GetActions "Permalink to this definition")
Returns the action list.



Return type
*RichTextActionList*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    def Undo(self) -> bool:
        """ 

`Undo`(*self*)[¶](#wx.richtext.RichTextCommand.Undo "Permalink to this definition")
Undoes the command.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCommand.html
        """

    Actions: 'RichTextActionList'  # `Actions`[¶](#wx.richtext.RichTextCommand.Actions "Permalink to this definition")See [`GetActions`](#wx.richtext.RichTextCommand.GetActions "wx.richtext.RichTextCommand.GetActions")



class RichTextStyleListCtrl(Control):
    """ **Possible constructors**:



```
RichTextStyleListCtrl(parent, id=ID_ANY, pos=DefaultPosition,
                      size=DefaultSize, style=0)

RichTextStyleListCtrl()

```


This class incorporates a RichTextStyleListBox and a choice control
that allows the user to select the category of style to view.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextStyleListCtrl.__init__ "Permalink to this definition")
Constructors.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  



**\_\_init\_\_** *(self)*




---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.richtext.RichTextStyleListCtrl.Create "Permalink to this definition")
Creates the windows.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextStyleListCtrl.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ 

`GetRichTextCtrl`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.GetRichTextCtrl "Permalink to this definition")
Returns the associated rich text control, if any.



Return type
 [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleChoice(self) -> 'Choice':
        """ 

`GetStyleChoice`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.GetStyleChoice "Permalink to this definition")
Returns the  [wx.Choice](wx.Choice.html#wx-choice) control used for selecting the style category.



Return type
*Choice*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleListBox(self) -> 'RichTextStyleListBox':
        """ 

`GetStyleListBox`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.GetStyleListBox "Permalink to this definition")
Returns the  [wx.ListBox](wx.ListBox.html#wx-listbox) control used to view the style list.



Return type
 [wx.richtext.RichTextStyleListBox](wx.richtext.RichTextStyleListBox.html#wx-richtext-richtextstylelistbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.GetStyleSheet "Permalink to this definition")
Returns the associated style sheet, if any.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def GetStyleType(self) -> 'wxRichTextStyleType':
        """ 

`GetStyleType`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.GetStyleType "Permalink to this definition")
Returns the type of style to show in the list box.



Return type
*wx.richtext.RichTextStyleListBox.wxRichTextStyleType*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ 

`SetRichTextCtrl`(*self*, *ctrl*)[¶](#wx.richtext.RichTextStyleListCtrl.SetRichTextCtrl "Permalink to this definition")
Associates the control with a  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl).



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextStyleListCtrl.SetStyleSheet "Permalink to this definition")
Associates the control with a style sheet.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def SetStyleType(self, styleType: RichTextStyleListBox.wxRichTextStyleType) -> None:
        """ 

`SetStyleType`(*self*, *styleType*)[¶](#wx.richtext.RichTextStyleListCtrl.SetStyleType "Permalink to this definition")
Sets the style type to display.


One of


* `RichTextStyleListBox.__init__` ,
* `RichTextStyleListBox.__init__` ,
* `RichTextStyleListBox.__init__`
* `RichTextStyleListBox.__init__` .



Parameters
**styleType** (*RichTextStyleListBox.wxRichTextStyleType*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    def UpdateStyles(self) -> None:
        """ 

`UpdateStyles`(*self*)[¶](#wx.richtext.RichTextStyleListCtrl.UpdateStyles "Permalink to this definition")
Updates the style list box.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListCtrl.html
        """

    RichTextCtrl: 'RichTextCtrl'  # `RichTextCtrl`[¶](#wx.richtext.RichTextStyleListCtrl.RichTextCtrl "Permalink to this definition")See [`GetRichTextCtrl`](#wx.richtext.RichTextStyleListCtrl.GetRichTextCtrl "wx.richtext.RichTextStyleListCtrl.GetRichTextCtrl") and [`SetRichTextCtrl`](#wx.richtext.RichTextStyleListCtrl.SetRichTextCtrl "wx.richtext.RichTextStyleListCtrl.SetRichTextCtrl")
    StyleChoice: 'Choice'  # `StyleChoice`[¶](#wx.richtext.RichTextStyleListCtrl.StyleChoice "Permalink to this definition")See [`GetStyleChoice`](#wx.richtext.RichTextStyleListCtrl.GetStyleChoice "wx.richtext.RichTextStyleListCtrl.GetStyleChoice")
    StyleListBox: 'RichTextStyleListBox'  # `StyleListBox`[¶](#wx.richtext.RichTextStyleListCtrl.StyleListBox "Permalink to this definition")See [`GetStyleListBox`](#wx.richtext.RichTextStyleListCtrl.GetStyleListBox "wx.richtext.RichTextStyleListCtrl.GetStyleListBox")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextStyleListCtrl.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextStyleListCtrl.GetStyleSheet "wx.richtext.RichTextStyleListCtrl.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextStyleListCtrl.SetStyleSheet "wx.richtext.RichTextStyleListCtrl.SetStyleSheet")
    StyleType: 'wxRichTextStyleType'  # `StyleType`[¶](#wx.richtext.RichTextStyleListCtrl.StyleType "Permalink to this definition")See [`GetStyleType`](#wx.richtext.RichTextStyleListCtrl.GetStyleType "wx.richtext.RichTextStyleListCtrl.GetStyleType") and [`SetStyleType`](#wx.richtext.RichTextStyleListCtrl.SetStyleType "wx.richtext.RichTextStyleListCtrl.SetStyleType")



RICHTEXTSTYLELIST_HIDE_TYPE_SELECTOR: int  # This style hides the category selection control. ^^

class RichTextBufferDataObject(DataObjectSimple):
    """ **Possible constructors**:



```
RichTextBufferDataObject(richTextBuffer=None)

```


Implements a rich text data object for clipboard transfer.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
    """
    def __init__(self, richTextBuffer: Optional['richtext.RichTextBuffer']=None) -> None:
        """ 

`__init__`(*self*, *richTextBuffer=None*)[¶](#wx.richtext.RichTextBufferDataObject.__init__ "Permalink to this definition")
The constructor doesn’t copy the pointer, so it shouldn’t go away while this object is alive.



Parameters
**richTextBuffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetDataHere(self, *args, **kw) -> bool:
        """ 

`GetDataHere`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBufferDataObject.GetDataHere "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetDataHere** *(self, buf)*


Copy the data to the buffer, return `True` on success.


Must be implemented in the derived class if the object supports rendering its data.



Parameters
**buf** – 



Return type
*bool*






---

  



**GetDataHere** *(self, format, buf)*


The method will write the data of the format *format* to the buffer *buf*.


In other words, copy the data from this object in the given format to the supplied buffer. Returns `True` on success, `False` on failure.



Parameters
* **format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) –
* **buf** –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetDataSize(self, *args, **kw) -> int:
        """ 

`GetDataSize`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBufferDataObject.GetDataSize "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetDataSize** *(self)*


Gets the size of our data.


Must be implemented in the derived class if the object supports rendering its data.



Return type
*int*






---

  



**GetDataSize** *(self, format)*


Returns the data size of the given format *format*.



Parameters
**format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) – 



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetPreferredFormat(self, dir: int) -> 'DataFormat':
        """ 

`GetPreferredFormat`(*self*, *dir*)[¶](#wx.richtext.RichTextBufferDataObject.GetPreferredFormat "Permalink to this definition")
Returns the preferred format for either rendering the data (if *dir* is `Get` , its default value) or for setting it.


Usually this will be the native format of the  [wx.DataObject](wx.DataObject.html#wx-dataobject).



Parameters
**dir** ([*Direction*](wx.DataObject.Direction.enumeration.html "Direction")) – 



Return type
*DataFormat*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def GetRichTextBuffer(self) -> 'RichTextBuffer':
        """ 

`GetRichTextBuffer`(*self*)[¶](#wx.richtext.RichTextBufferDataObject.GetRichTextBuffer "Permalink to this definition")
After a call to this function, the buffer is owned by the caller and it is responsible for deleting it.



Return type
 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    @staticmethod
    def GetRichTextBufferFormatId() -> 'Char':
        """ 

*static* `GetRichTextBufferFormatId`()[¶](#wx.richtext.RichTextBufferDataObject.GetRichTextBufferFormatId "Permalink to this definition")
Returns the id for the new data format.



Return type
*wx.Char*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    def SetData(self, *args, **kw) -> bool:
        """ 

`SetData`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBufferDataObject.SetData "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetData** *(self, len, buf)*


Copy the data from the buffer, return `True` on success.


Must be implemented in the derived class if the object supports setting its data.



Parameters
* **len** (*int*) –
* **buf** –



Return type
*bool*






---

  



**SetData** *(self, format, len, buf)*


Set the data in the format *format* of the length *len* provided in the buffer *buf*.


In other words, copy length bytes of data from the buffer to this data object.



Parameters
* **format** ([*wx.DataFormat*](wx.DataFormat.html#wx.DataFormat "wx.DataFormat")) – The format for which to set the data.
* **len** (*int*) – The size of data in bytes.
* **buf** – Non-NULL pointer to the data.



Return type
*bool*



Returns
`True` on success, `False` on failure.






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBufferDataObject.html
        """

    DataSize: int  # `DataSize`[¶](#wx.richtext.RichTextBufferDataObject.DataSize "Permalink to this definition")See [`GetDataSize`](#wx.richtext.RichTextBufferDataObject.GetDataSize "wx.richtext.RichTextBufferDataObject.GetDataSize")
    RichTextBuffer: 'RichTextBuffer'  # `RichTextBuffer`[¶](#wx.richtext.RichTextBufferDataObject.RichTextBuffer "Permalink to this definition")See [`GetRichTextBuffer`](#wx.richtext.RichTextBufferDataObject.GetRichTextBuffer "wx.richtext.RichTextBufferDataObject.GetRichTextBuffer")



class RichTextStyleOrganiserDialog(Dialog):
    """ **Possible constructors**:



```
RichTextStyleOrganiserDialog()

RichTextStyleOrganiserDialog(flags, sheet, ctrl, parent, id=ID_ANY,
                             caption=_("StyleOrganiser"), pos=DefaultPosition, size=DefaultSize,
                             style=DEFAULT_DIALOG_STYLE|RESIZE_BORDER|SYSTEM_MENU|CLOSE_BOX)

```


This class shows a style sheet and allows the user to edit, add and
remove styles.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, flags, sheet, ctrl, parent, id=ID\_ANY, caption=\_(“StyleOrganiser”), pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_DIALOG\_STYLE|RESIZE\_BORDER|SYSTEM\_MENU|CLOSE\_BOX)*


Constructor.


To create a dialog, pass a bitlist of *flags* (see below), a style sheet, a text control to apply a selected style to (or `None`), followed by the usual window parameters.


To specify the operations available to the user, pass a combination of these values to *flags:*


* `wx.richtext.RICHTEXT_ORGANISER_DELETE_STYLES`: Provides a button for deleting styles.
* `wx.richtext.RICHTEXT_ORGANISER_CREATE_STYLES`: Provides buttons for creating styles.
* `wx.richtext.RICHTEXT_ORGANISER_APPLY_STYLES`: Provides a button for applying the currently selected style to the selection.
* `wx.richtext.RICHTEXT_ORGANISER_EDIT_STYLES`: Provides a button for editing styles.
* `wx.richtext.RICHTEXT_ORGANISER_RENAME_STYLES`: Provides a button for renaming styles.
* `wx.richtext.RICHTEXT_ORGANISER_OK_CANCEL`: Provides `wx.OK` and Cancel buttons.
* `wx.richtext.RICHTEXT_ORGANISER_RENUMBER`: Provides a checkbox for specifying that the selection should be renumbered.


The following flags determine what will be displayed in the style list:


* `wx.richtext.RICHTEXT_ORGANISER_SHOW_CHARACTER`: Displays character styles only.
* `wx.richtext.RICHTEXT_ORGANISER_SHOW_PARAGRAPH`: Displays paragraph styles only.
* `wx.richtext.RICHTEXT_ORGANISER_SHOW_LIST`: Displays list styles only.
* `wx.richtext.RICHTEXT_ORGANISER_SHOW_ALL`: Displays all styles.


The following symbols define commonly-used combinations of flags:


* `wx.richtext.RICHTEXT_ORGANISER_ORGANISE`: Enable all style editing operations so the dialog behaves as a style organiser.
* `wx.richtext.RICHTEXT_ORGANISER_BROWSE`: Show a list of all styles and their previews, but only allow application of a style or cancellation of the dialog. This makes the dialog behave as a style browser.
* `wx.richtext.RICHTEXT_ORGANISER_BROWSE_NUMBERING`: Enables only list style browsing, plus a control to specify renumbering. This allows the dialog to be used for applying list styles to the selection.



Parameters
* **flags** (*int*) –
* **sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **caption** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def ApplyStyle(self, ctrl: Optional['richtext.RichTextCtrl']=None) -> bool:
        """ 

`ApplyStyle`(*self*, *ctrl=None*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.ApplyStyle "Permalink to this definition")
Applies the selected style to selection in the given control or the control passed to the constructor.



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *flags*, *sheet*, *ctrl*, *parent*, *id=ID\_ANY*, *caption=GetTranslation("StyleOrganiser")*, *pos=DefaultPosition*, *size=Size(400*, *300)*, *style=DEFAULT\_DIALOG\_STYLE|RESIZE\_BORDER|SYSTEM\_MENU|CLOSE\_BOX*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.Create "Permalink to this definition")
Creates the dialog.


See the constructor.



Parameters
* **flags** (*int*) –
* **sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **caption** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetFlags "Permalink to this definition")
Returns the flags used to control the interface presented to the user.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetRestartNumbering(self) -> bool:
        """ 

`GetRestartNumbering`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetRestartNumbering "Permalink to this definition")
Returns `True` if the user has opted to restart numbering.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ 

`GetRichTextCtrl`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetRichTextCtrl "Permalink to this definition")
Returns the associated rich text control (if any).



Return type
 [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetSelectedStyle(self) -> str:
        """ 

`GetSelectedStyle`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyle "Permalink to this definition")
Returns selected style name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetSelectedStyleDefinition(self) -> 'RichTextStyleDefinition':
        """ 

`GetSelectedStyleDefinition`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyleDefinition "Permalink to this definition")
Returns selected style definition.



Return type
 [wx.richtext.RichTextStyleDefinition](wx.richtext.RichTextStyleDefinition.html#wx-richtext-richtextstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.GetStyleSheet "Permalink to this definition")
Returns the associated style sheet.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.SetFlags "Permalink to this definition")
Sets the flags used to control the interface presented to the user.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetRestartNumbering(self, restartNumbering: bool) -> None:
        """ 

`SetRestartNumbering`(*self*, *restartNumbering*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.SetRestartNumbering "Permalink to this definition")
Checks or unchecks the restart numbering checkbox.



Parameters
**restartNumbering** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ 

`SetRichTextCtrl`(*self*, *ctrl*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.SetRichTextCtrl "Permalink to this definition")
Sets the control to be associated with the dialog, for the purposes of applying a style to the selection.



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    @staticmethod
    def SetShowToolTips(show: bool) -> None:
        """ 

*static* `SetShowToolTips`(*show*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.SetShowToolTips "Permalink to this definition")
Determines whether tooltips will be shown.



Parameters
**show** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    def SetStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *sheet*)[¶](#wx.richtext.RichTextStyleOrganiserDialog.SetStyleSheet "Permalink to this definition")
Sets the associated style sheet.



Parameters
**sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleOrganiserDialog.html
        """

    Flags: int  # `Flags`[¶](#wx.richtext.RichTextStyleOrganiserDialog.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.RichTextStyleOrganiserDialog.GetFlags "wx.richtext.RichTextStyleOrganiserDialog.GetFlags") and [`SetFlags`](#wx.richtext.RichTextStyleOrganiserDialog.SetFlags "wx.richtext.RichTextStyleOrganiserDialog.SetFlags")
    RestartNumbering: bool  # `RestartNumbering`[¶](#wx.richtext.RichTextStyleOrganiserDialog.RestartNumbering "Permalink to this definition")See [`GetRestartNumbering`](#wx.richtext.RichTextStyleOrganiserDialog.GetRestartNumbering "wx.richtext.RichTextStyleOrganiserDialog.GetRestartNumbering") and [`SetRestartNumbering`](#wx.richtext.RichTextStyleOrganiserDialog.SetRestartNumbering "wx.richtext.RichTextStyleOrganiserDialog.SetRestartNumbering")
    RichTextCtrl: 'RichTextCtrl'  # `RichTextCtrl`[¶](#wx.richtext.RichTextStyleOrganiserDialog.RichTextCtrl "Permalink to this definition")See [`GetRichTextCtrl`](#wx.richtext.RichTextStyleOrganiserDialog.GetRichTextCtrl "wx.richtext.RichTextStyleOrganiserDialog.GetRichTextCtrl") and [`SetRichTextCtrl`](#wx.richtext.RichTextStyleOrganiserDialog.SetRichTextCtrl "wx.richtext.RichTextStyleOrganiserDialog.SetRichTextCtrl")
    SelectedStyle: str  # `SelectedStyle`[¶](#wx.richtext.RichTextStyleOrganiserDialog.SelectedStyle "Permalink to this definition")See [`GetSelectedStyle`](#wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyle "wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyle")
    SelectedStyleDefinition: 'RichTextStyleDefinition'  # `SelectedStyleDefinition`[¶](#wx.richtext.RichTextStyleOrganiserDialog.SelectedStyleDefinition "Permalink to this definition")See [`GetSelectedStyleDefinition`](#wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyleDefinition "wx.richtext.RichTextStyleOrganiserDialog.GetSelectedStyleDefinition")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextStyleOrganiserDialog.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextStyleOrganiserDialog.GetStyleSheet "wx.richtext.RichTextStyleOrganiserDialog.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextStyleOrganiserDialog.SetStyleSheet "wx.richtext.RichTextStyleOrganiserDialog.SetStyleSheet")



RICHTEXT_ORGANISER_DELETE_STYLES: int

RICHTEXT_ORGANISER_CREATE_STYLES: int

RICHTEXT_ORGANISER_APPLY_STYLES: int

RICHTEXT_ORGANISER_EDIT_STYLES: int

RICHTEXT_ORGANISER_RENAME_STYLES: int

RICHTEXT_ORGANISER_OK_CANCEL: int

OK: int

RICHTEXT_ORGANISER_RENUMBER: int

RICHTEXT_ORGANISER_SHOW_CHARACTER: int

RICHTEXT_ORGANISER_SHOW_PARAGRAPH: int

RICHTEXT_ORGANISER_SHOW_LIST: int

RICHTEXT_ORGANISER_SHOW_ALL: int

RICHTEXT_ORGANISER_ORGANISE: int

RICHTEXT_ORGANISER_BROWSE: int

RICHTEXT_ORGANISER_BROWSE_NUMBERING: int

class SymbolPickerDialog(Dialog):
    """ **Possible constructors**:



```
SymbolPickerDialog()

SymbolPickerDialog(symbol, initialFont, normalTextFont, parent,
                   id=ID_ANY, title=_("Symbols"), pos=DefaultPosition, size=DefaultSize,
                   style=DEFAULT_DIALOG_STYLE|RESIZE_BORDER|CLOSE_BOX)

```


SymbolPickerDialog presents the user with a choice of fonts and a
grid of available characters.


  


        Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.SymbolPickerDialog.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, symbol, initialFont, normalTextFont, parent, id=ID\_ANY, title=\_(“Symbols”), pos=DefaultPosition, size=DefaultSize, style=DEFAULT\_DIALOG\_STYLE|RESIZE\_BORDER|CLOSE\_BOX)*


Constructor.



Parameters
* **symbol** (*string*) – The initial symbol to show. Specify a single character in a string, or an empty string.
* **initialFont** (*string*) – The initial font to be displayed in the font list. If empty, the item normal text will be selected.
* **normalTextFont** (*string*) – The font the dialog will use to display the symbols if the initial font is empty.
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The dialog’s parent.
* **id** (*wx.WindowID*) – The dialog’s identifier.
* **title** (*string*) – The dialog’s caption.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The dialog’s position.
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The dialog’s size.
* **style** (*long*) – The dialog’s window style.






---

  





            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *symbol*, *initialFont*, *normalTextFont*, *parent*, *id=ID\_ANY*, *caption=GetTranslation("Symbols")*, *pos=DefaultPosition*, *size=Size(400*, *300)*, *style=DEFAULT\_DIALOG\_STYLE|RESIZE\_BORDER|CLOSE\_BOX*)[¶](#wx.richtext.SymbolPickerDialog.Create "Permalink to this definition")
Creation: see [the constructor](#wx-richtext-symbolpickerdialog) for details about the parameters.



Parameters
* **symbol** (*string*) –
* **initialFont** (*string*) –
* **normalTextFont** (*string*) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **caption** (*string*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.SymbolPickerDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetFontName(self) -> str:
        """ 

`GetFontName`(*self*)[¶](#wx.richtext.SymbolPickerDialog.GetFontName "Permalink to this definition")
Returns the font name (the font reflected in the font list).



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetFromUnicode(self) -> bool:
        """ 

`GetFromUnicode`(*self*)[¶](#wx.richtext.SymbolPickerDialog.GetFromUnicode "Permalink to this definition")
Returns `True` if the dialog is showing the full range of Unicode characters.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetNormalTextFontName(self) -> str:
        """ 

`GetNormalTextFontName`(*self*)[¶](#wx.richtext.SymbolPickerDialog.GetNormalTextFontName "Permalink to this definition")
Gets the font name used for displaying symbols in the absence of a selected font.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetSymbol(self) -> str:
        """ 

`GetSymbol`(*self*)[¶](#wx.richtext.SymbolPickerDialog.GetSymbol "Permalink to this definition")
Gets the current or initial symbol as a string.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def GetSymbolChar(self) -> int:
        """ 

`GetSymbolChar`(*self*)[¶](#wx.richtext.SymbolPickerDialog.GetSymbolChar "Permalink to this definition")
Gets the selected symbol character as an integer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def HasSelection(self) -> bool:
        """ 

`HasSelection`(*self*)[¶](#wx.richtext.SymbolPickerDialog.HasSelection "Permalink to this definition")
Returns `True` if a symbol is selected.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetFontName(self, value: str) -> None:
        """ 

`SetFontName`(*self*, *value*)[¶](#wx.richtext.SymbolPickerDialog.SetFontName "Permalink to this definition")
Sets the initial/selected font name.



Parameters
**value** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetFromUnicode(self, value: bool) -> None:
        """ 

`SetFromUnicode`(*self*, *value*)[¶](#wx.richtext.SymbolPickerDialog.SetFromUnicode "Permalink to this definition")
Sets the internal flag indicating that the full Unicode range should be displayed.



Parameters
**value** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetNormalTextFontName(self, value: str) -> None:
        """ 

`SetNormalTextFontName`(*self*, *value*)[¶](#wx.richtext.SymbolPickerDialog.SetNormalTextFontName "Permalink to this definition")
Sets the name of the font to be used in the absence of a selected font.



Parameters
**value** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetSymbol(self, value: str) -> None:
        """ 

`SetSymbol`(*self*, *value*)[¶](#wx.richtext.SymbolPickerDialog.SetSymbol "Permalink to this definition")
Sets the symbol as a one or zero character string.



Parameters
**value** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def SetUnicodeMode(self, unicodeMode: bool) -> None:
        """ 

`SetUnicodeMode`(*self*, *unicodeMode*)[¶](#wx.richtext.SymbolPickerDialog.SetUnicodeMode "Permalink to this definition")
Sets Unicode display mode.



Parameters
**unicodeMode** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    def UseNormalFont(self) -> bool:
        """ 

`UseNormalFont`(*self*)[¶](#wx.richtext.SymbolPickerDialog.UseNormalFont "Permalink to this definition")
Returns `True` if the has specified normal text - that is, there is no selected font.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.SymbolPickerDialog.html
        """

    FontName: str  # `FontName`[¶](#wx.richtext.SymbolPickerDialog.FontName "Permalink to this definition")See [`GetFontName`](#wx.richtext.SymbolPickerDialog.GetFontName "wx.richtext.SymbolPickerDialog.GetFontName") and [`SetFontName`](#wx.richtext.SymbolPickerDialog.SetFontName "wx.richtext.SymbolPickerDialog.SetFontName")
    FromUnicode: bool  # `FromUnicode`[¶](#wx.richtext.SymbolPickerDialog.FromUnicode "Permalink to this definition")See [`GetFromUnicode`](#wx.richtext.SymbolPickerDialog.GetFromUnicode "wx.richtext.SymbolPickerDialog.GetFromUnicode") and [`SetFromUnicode`](#wx.richtext.SymbolPickerDialog.SetFromUnicode "wx.richtext.SymbolPickerDialog.SetFromUnicode")
    NormalTextFontName: str  # `NormalTextFontName`[¶](#wx.richtext.SymbolPickerDialog.NormalTextFontName "Permalink to this definition")See [`GetNormalTextFontName`](#wx.richtext.SymbolPickerDialog.GetNormalTextFontName "wx.richtext.SymbolPickerDialog.GetNormalTextFontName") and [`SetNormalTextFontName`](#wx.richtext.SymbolPickerDialog.SetNormalTextFontName "wx.richtext.SymbolPickerDialog.SetNormalTextFontName")
    Symbol: str  # `Symbol`[¶](#wx.richtext.SymbolPickerDialog.Symbol "Permalink to this definition")See [`GetSymbol`](#wx.richtext.SymbolPickerDialog.GetSymbol "wx.richtext.SymbolPickerDialog.GetSymbol") and [`SetSymbol`](#wx.richtext.SymbolPickerDialog.SetSymbol "wx.richtext.SymbolPickerDialog.SetSymbol")
    SymbolChar: int  # `SymbolChar`[¶](#wx.richtext.SymbolPickerDialog.SymbolChar "Permalink to this definition")See [`GetSymbolChar`](#wx.richtext.SymbolPickerDialog.GetSymbolChar "wx.richtext.SymbolPickerDialog.GetSymbolChar")



class RichTextEvent(NotifyEvent):
    """ **Possible constructors**:



```
RichTextEvent(commandType=wxEVT_NULL, winid=0)

RichTextEvent(event)

```


This is the event class for RichTextCtrl notifications.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextEvent.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, commandType=wxEVT\_NULL, winid=0)*


Constructor.



Parameters
* **commandType** (*wx.EventType*) – The type of the event.
* **winid** (*int*) – Window identifier. The value `ID_ANY` indicates a default value.






---

  



**\_\_init\_\_** *(self, event)*


Copy constructor.



Parameters
**event** ([*wx.richtext.RichTextEvent*](#wx.richtext.RichTextEvent "wx.richtext.RichTextEvent")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def Clone(self) -> 'Event':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextEvent.Clone "Permalink to this definition")
Returns a copy of the event.


Any event that is posted to the wxWidgets event system for later action (via [`wx.EvtHandler.AddPendingEvent`](wx.EvtHandler.html#wx.EvtHandler.AddPendingEvent "wx.EvtHandler.AddPendingEvent") , [`wx.EvtHandler.QueueEvent`](wx.EvtHandler.html#wx.EvtHandler.QueueEvent "wx.EvtHandler.QueueEvent") or [`wx.PostEvent`](wx.functions.html#wx.PostEvent "wx.PostEvent") ) must implement this method.


All wxWidgets events fully implement this method, but any derived events implemented by the user should also implement this method just in case they (or some event derived from them) are ever posted.


All wxWidgets events implement a copy constructor, so the easiest way of implementing the Clone function is to implement a copy constructor for a new event (call it MyEvent) and then define the Clone function like this:



```
def Clone(self):

    return MyEvent()

```



Return type
*Event*






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetCharacter(self) -> 'Char':
        """ 

`GetCharacter`(*self*)[¶](#wx.richtext.RichTextEvent.GetCharacter "Permalink to this definition")
Returns the character pressed, within a `wxEVT_RICHTEXT_CHARACTER` event.



Return type
*wx.Char*






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetContainer`(*self*)[¶](#wx.richtext.RichTextEvent.GetContainer "Permalink to this definition")
Returns the container for which the event is relevant.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.RichTextEvent.GetFlags "Permalink to this definition")
Returns flags indicating modifier keys pressed.


Possible values are `RICHTEXT_CTRL_DOWN` , `RICHTEXT_SHIFT_DOWN` , and `RICHTEXT_ALT_DOWN` .



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetNewStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetNewStyleSheet`(*self*)[¶](#wx.richtext.RichTextEvent.GetNewStyleSheet "Permalink to this definition")
Returns the new style sheet.


Can be used in a `wxEVT_RICHTEXT_STYLESHEET_CHANGING` or `wxEVT_RICHTEXT_STYLESHEET_CHANGED` event handler.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetOldContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetOldContainer`(*self*)[¶](#wx.richtext.RichTextEvent.GetOldContainer "Permalink to this definition")
Returns the old container, for a focus change event.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetOldStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetOldStyleSheet`(*self*)[¶](#wx.richtext.RichTextEvent.GetOldStyleSheet "Permalink to this definition")
Returns the old style sheet.


Can be used in a `wxEVT_RICHTEXT_STYLESHEET_CHANGING` or `wxEVT_RICHTEXT_STYLESHEET_CHANGED` event handler.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetPosition(self) -> int:
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.RichTextEvent.GetPosition "Permalink to this definition")
Returns the buffer position at which the event occurred.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ 

`GetRange`(*self*)[¶](#wx.richtext.RichTextEvent.GetRange "Permalink to this definition")
Gets the range for the current operation.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetCharacter(self, ch: 'Char') -> None:
        """ 

`SetCharacter`(*self*, *ch*)[¶](#wx.richtext.RichTextEvent.SetCharacter "Permalink to this definition")
Sets the character variable.



Parameters
**ch** (*wx.Char*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`SetContainer`(*self*, *container*)[¶](#wx.richtext.RichTextEvent.SetContainer "Permalink to this definition")
Sets the container for which the event is relevant.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.RichTextEvent.SetFlags "Permalink to this definition")
Sets flags indicating modifier keys pressed.


Possible values are `RICHTEXT_CTRL_DOWN` , `RICHTEXT_SHIFT_DOWN` , and `RICHTEXT_ALT_DOWN` .



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetNewStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetNewStyleSheet`(*self*, *sheet*)[¶](#wx.richtext.RichTextEvent.SetNewStyleSheet "Permalink to this definition")
Sets the new style sheet variable.



Parameters
**sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetOldContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`SetOldContainer`(*self*, *container*)[¶](#wx.richtext.RichTextEvent.SetOldContainer "Permalink to this definition")
Sets the old container, for a focus change event.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetOldStyleSheet(self, sheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetOldStyleSheet`(*self*, *sheet*)[¶](#wx.richtext.RichTextEvent.SetOldStyleSheet "Permalink to this definition")
Sets the old style sheet variable.



Parameters
**sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetPosition(self, pos: int) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextEvent.SetPosition "Permalink to this definition")
Sets the buffer position variable.



Parameters
**pos** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetRange`(*self*, *range*)[¶](#wx.richtext.RichTextEvent.SetRange "Permalink to this definition")
Sets the range variable.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextEvent.html
        """

    Character: 'Char'  # `Character`[¶](#wx.richtext.RichTextEvent.Character "Permalink to this definition")See [`GetCharacter`](#wx.richtext.RichTextEvent.GetCharacter "wx.richtext.RichTextEvent.GetCharacter") and [`SetCharacter`](#wx.richtext.RichTextEvent.SetCharacter "wx.richtext.RichTextEvent.SetCharacter")
    Container: 'RichTextParagraphLayoutBox'  # `Container`[¶](#wx.richtext.RichTextEvent.Container "Permalink to this definition")See [`GetContainer`](#wx.richtext.RichTextEvent.GetContainer "wx.richtext.RichTextEvent.GetContainer") and [`SetContainer`](#wx.richtext.RichTextEvent.SetContainer "wx.richtext.RichTextEvent.SetContainer")
    Flags: int  # `Flags`[¶](#wx.richtext.RichTextEvent.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.RichTextEvent.GetFlags "wx.richtext.RichTextEvent.GetFlags") and [`SetFlags`](#wx.richtext.RichTextEvent.SetFlags "wx.richtext.RichTextEvent.SetFlags")
    NewStyleSheet: 'RichTextStyleSheet'  # `NewStyleSheet`[¶](#wx.richtext.RichTextEvent.NewStyleSheet "Permalink to this definition")See [`GetNewStyleSheet`](#wx.richtext.RichTextEvent.GetNewStyleSheet "wx.richtext.RichTextEvent.GetNewStyleSheet") and [`SetNewStyleSheet`](#wx.richtext.RichTextEvent.SetNewStyleSheet "wx.richtext.RichTextEvent.SetNewStyleSheet")
    OldContainer: 'RichTextParagraphLayoutBox'  # `OldContainer`[¶](#wx.richtext.RichTextEvent.OldContainer "Permalink to this definition")See [`GetOldContainer`](#wx.richtext.RichTextEvent.GetOldContainer "wx.richtext.RichTextEvent.GetOldContainer") and [`SetOldContainer`](#wx.richtext.RichTextEvent.SetOldContainer "wx.richtext.RichTextEvent.SetOldContainer")
    OldStyleSheet: 'RichTextStyleSheet'  # `OldStyleSheet`[¶](#wx.richtext.RichTextEvent.OldStyleSheet "Permalink to this definition")See [`GetOldStyleSheet`](#wx.richtext.RichTextEvent.GetOldStyleSheet "wx.richtext.RichTextEvent.GetOldStyleSheet") and [`SetOldStyleSheet`](#wx.richtext.RichTextEvent.SetOldStyleSheet "wx.richtext.RichTextEvent.SetOldStyleSheet")
    Position: int  # `Position`[¶](#wx.richtext.RichTextEvent.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.RichTextEvent.GetPosition "wx.richtext.RichTextEvent.GetPosition") and [`SetPosition`](#wx.richtext.RichTextEvent.SetPosition "wx.richtext.RichTextEvent.SetPosition")
    Range: 'RichTextRange'  # `Range`[¶](#wx.richtext.RichTextEvent.Range "Permalink to this definition")See [`GetRange`](#wx.richtext.RichTextEvent.GetRange "wx.richtext.RichTextEvent.GetRange") and [`SetRange`](#wx.richtext.RichTextEvent.SetRange "wx.richtext.RichTextEvent.SetRange")



EVT_RICHTEXT_LEFT_CLICK: int  # Process a  wxEVT_RICHTEXT_LEFT_CLICK   event, generated when the user releases the left mouse button over an object.

EVT_RICHTEXT_RIGHT_CLICK: int  # Process a  wxEVT_RICHTEXT_RIGHT_CLICK   event, generated when the user releases the right mouse button over an object.

EVT_RICHTEXT_MIDDLE_CLICK: int  # Process a  wxEVT_RICHTEXT_MIDDLE_CLICK   event, generated when the user releases the middle mouse button over an object.

EVT_RICHTEXT_LEFT_DCLICK: int  # Process a  wxEVT_RICHTEXT_LEFT_DCLICK   event, generated when the user double-clicks an object.

EVT_RICHTEXT_RETURN: int  # Process a  wxEVT_RICHTEXT_RETURN   event, generated when the user presses the return key. Valid event functions: GetFlags, GetPosition.

EVT_RICHTEXT_CHARACTER: int  # Process a  wxEVT_RICHTEXT_CHARACTER   event, generated when the user presses a character key. Valid event functions: GetFlags, GetPosition, GetCharacter.

EVT_RICHTEXT_CONSUMING_CHARACTER: int  # Process a  wxEVT_RICHTEXT_CONSUMING_CHARACTER   event, generated when the user presses a character key but before it is processed and inserted into the control. Call Veto to prevent normal processing. Valid event functions: GetFlags, GetPosition, GetCharacter, Veto.

EVT_RICHTEXT_DELETE: int  # Process a  wxEVT_RICHTEXT_DELETE   event, generated when the user presses the backspace or delete key. Valid event functions: GetFlags, GetPosition.

EVT_RICHTEXT_STYLE_CHANGED: int  # Process a  wxEVT_RICHTEXT_STYLE_CHANGED   event, generated when styling has been applied to the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_STYLESHEET_CHANGED: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_CHANGING   event, generated when the control’s stylesheet has changed, for example the user added, edited or deleted a style. Valid event functions: GetRange, GetPosition.

EVT_RICHTEXT_STYLESHEET_REPLACING: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_REPLACING   event, generated when the control’s stylesheet is about to be replaced, for example when a file is loaded into the control. Valid event functions: Veto, GetOldStyleSheet, GetNewStyleSheet.

EVT_RICHTEXT_STYLESHEET_REPLACED: int  # Process a  wxEVT_RICHTEXT_STYLESHEET_REPLACED   event, generated when the control’s stylesheet has been replaced, for example when a file is loaded into the control. Valid event functions: GetOldStyleSheet, GetNewStyleSheet.

EVT_RICHTEXT_PROPERTIES_CHANGED: int  # Process a  wxEVT_RICHTEXT_PROPERTIES_CHANGED   event, generated when properties have been applied to the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_CONTENT_INSERTED: int  # Process a  wxEVT_RICHTEXT_CONTENT_INSERTED   event, generated when content has been inserted into the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_CONTENT_DELETED: int  # Process a  wxEVT_RICHTEXT_CONTENT_DELETED   event, generated when content has been deleted from the control. Valid event functions: GetPosition, GetRange.

EVT_RICHTEXT_BUFFER_RESET: int  # Process a  wxEVT_RICHTEXT_BUFFER_RESET   event, generated when the buffer has been reset by deleting all content. You can use this to set a default style for the first new paragraph.

EVT_RICHTEXT_SELECTION_CHANGED: int  # Process a  wxEVT_RICHTEXT_SELECTION_CHANGED   event, generated when the selection range has changed.

EVT_RICHTEXT_FOCUS_OBJECT_CHANGED: int  # Process a  wxEVT_RICHTEXT_FOCUS_OBJECT_CHANGED   event, generated when the current focus object has changed. ^^

class RichTextAction(Object):
    """ **Possible constructors**:



```
RichTextAction(cmd, name, id, buffer, container, ctrl,
               ignoreFirstTime=False)

```


Implements a part of a command.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
    """
    def __init__(self, cmd, name, id, buffer, container, ctrl, ignoreFirstTime=False) -> None:
        """ 

`__init__`(*self*, *cmd*, *name*, *id*, *buffer*, *container*, *ctrl*, *ignoreFirstTime=False*)[¶](#wx.richtext.RichTextAction.__init__ "Permalink to this definition")
Constructor.


*buffer* is the top-level buffer, while *container* is the object within which the action is taking place. In the simplest case, they are the same.



Parameters
* **cmd** ([*wx.richtext.RichTextCommand*](wx.richtext.RichTextCommand.html#wx.richtext.RichTextCommand "wx.richtext.RichTextCommand")) –
* **name** (*string*) –
* **id** ([*RichTextCommandId*](wx.richtext.RichTextCommandId.enumeration.html "RichTextCommandId")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **ignoreFirstTime** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def ApplyParagraphs(self, fragment: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`ApplyParagraphs`(*self*, *fragment*)[¶](#wx.richtext.RichTextAction.ApplyParagraphs "Permalink to this definition")
Replaces the buffer paragraphs with the given fragment.



Parameters
**fragment** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def CalculateRefreshOptimizations(self, optimizationLineCharPositions, optimizationLineYPositions, oldFloatRect) -> None:
        """ 

`CalculateRefreshOptimizations`(*self*, *optimizationLineCharPositions*, *optimizationLineYPositions*, *oldFloatRect*)[¶](#wx.richtext.RichTextAction.CalculateRefreshOptimizations "Permalink to this definition")
Calculate arrays for refresh optimization.



Parameters
* **optimizationLineCharPositions** (*list of integers*) –
* **optimizationLineYPositions** (*list of integers*) –
* **oldFloatRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def Do(self) -> bool:
        """ 

`Do`(*self*)[¶](#wx.richtext.RichTextAction.Do "Permalink to this definition")
Performs the action.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetAttributes(self) -> 'RichTextAttr':
        """ 

`GetAttributes`(*self*)[¶](#wx.richtext.RichTextAction.GetAttributes "Permalink to this definition")
Returns the attributes, for single-object commands.



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetContainer`(*self*)[¶](#wx.richtext.RichTextAction.GetContainer "Permalink to this definition")
Returns the container that this action refers to, using the container address and top-level buffer.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetContainerAddress(self) -> 'RichTextObjectAddress':
        """ 

`GetContainerAddress`(*self*)[¶](#wx.richtext.RichTextAction.GetContainerAddress "Permalink to this definition")
Returns the address (nested position) of the container within the buffer being manipulated.



Return type
 [wx.richtext.RichTextObjectAddress](wx.richtext.RichTextObjectAddress.html#wx-richtext-richtextobjectaddress)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetIgnoreFirstTime(self) -> bool:
        """ 

`GetIgnoreFirstTime`(*self*)[¶](#wx.richtext.RichTextAction.GetIgnoreFirstTime "Permalink to this definition")
Returns `True` if the first [`Do`](#wx.richtext.RichTextAction.Do "wx.richtext.RichTextAction.Do") command should be skipped as it’s already been applied.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextAction.GetName "Permalink to this definition")
Returns the action name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetNewParagraphs(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetNewParagraphs`(*self*)[¶](#wx.richtext.RichTextAction.GetNewParagraphs "Permalink to this definition")
Returns the new fragments.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetObject(self) -> 'RichTextObject':
        """ 

`GetObject`(*self*)[¶](#wx.richtext.RichTextAction.GetObject "Permalink to this definition")
Returns the object to replace the one at the position defined by the container address and the action’s range start position.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetOldParagraphs(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetOldParagraphs`(*self*)[¶](#wx.richtext.RichTextAction.GetOldParagraphs "Permalink to this definition")
Returns the old fragments.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetPosition(self) -> int:
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.RichTextAction.GetPosition "Permalink to this definition")
Returns the position used for e.g.


insertion.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ 

`GetRange`(*self*)[¶](#wx.richtext.RichTextAction.GetRange "Permalink to this definition")
Returns the range for e.g.


deletion.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def MakeObject(self, obj: 'richtext.RichTextObject') -> None:
        """ 

`MakeObject`(*self*, *obj*)[¶](#wx.richtext.RichTextAction.MakeObject "Permalink to this definition")
Makes an address from the given object.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetContainerAddress(self, *args, **kw) -> None:
        """ 

`SetContainerAddress`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextAction.SetContainerAddress "Permalink to this definition")
Sets the address (nested position) of the container within the buffer being manipulated.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetContainerAddress** *(self, address)*



Parameters
**address** ([*wx.richtext.RichTextObjectAddress*](wx.richtext.RichTextObjectAddress.html#wx.richtext.RichTextObjectAddress "wx.richtext.RichTextObjectAddress")) – 






---

  



**SetContainerAddress** *(self, container, obj)*



Parameters
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetIgnoreFirstTime(self, b: bool) -> None:
        """ 

`SetIgnoreFirstTime`(*self*, *b*)[¶](#wx.richtext.RichTextAction.SetIgnoreFirstTime "Permalink to this definition")
Instructs the first [`Do`](#wx.richtext.RichTextAction.Do "wx.richtext.RichTextAction.Do") command should be skipped as it’s already been applied.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetObject(self, obj: 'richtext.RichTextObject') -> None:
        """ 

`SetObject`(*self*, *obj*)[¶](#wx.richtext.RichTextAction.SetObject "Permalink to this definition")
Sets the object to replace the one at the position defined by the container address and the action’s range start position.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetOldAndNewObjects(self, oldObj, newObj) -> None:
        """ 

`SetOldAndNewObjects`(*self*, *oldObj*, *newObj*)[¶](#wx.richtext.RichTextAction.SetOldAndNewObjects "Permalink to this definition")
Sets the existing and new objects, for use with `wx.richtext.RICHTEXT_CHANGE_OBJECT`.



Parameters
* **oldObj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **newObj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetPosition(self, pos: int) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextAction.SetPosition "Permalink to this definition")
Sets the position used for e.g.


insertion.



Parameters
**pos** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetRange`(*self*, *range*)[¶](#wx.richtext.RichTextAction.SetRange "Permalink to this definition")
Sets the range for e.g.


deletion.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def StoreObject(self, obj: 'richtext.RichTextObject') -> None:
        """ 

`StoreObject`(*self*, *obj*)[¶](#wx.richtext.RichTextAction.StoreObject "Permalink to this definition")
Stores the object to replace the one at the position defined by the container address without making an address for it.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 





See also


[`SetObject`](#wx.richtext.RichTextAction.SetObject "wx.richtext.RichTextAction.SetObject") , [`MakeObject`](#wx.richtext.RichTextAction.MakeObject "wx.richtext.RichTextAction.MakeObject") ).





            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def Undo(self) -> bool:
        """ 

`Undo`(*self*)[¶](#wx.richtext.RichTextAction.Undo "Permalink to this definition")
Undoes the action.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    def UpdateAppearance(*args, **kwargs) -> None:
        """ 

`UpdateAppearance`(*self*, *caretPosition*, *sendUpdateEvent=False*, *oldFloatRect=Rect()*, *optimizationLineCharPositions=None*, *optimizationLineYPositions=None*, *isDoCmd=True*)[¶](#wx.richtext.RichTextAction.UpdateAppearance "Permalink to this definition")
Updates the control appearance, optimizing if possible given information from the call to Layout.



Parameters
* **caretPosition** (*long*) –
* **sendUpdateEvent** (*bool*) –
* **oldFloatRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **optimizationLineCharPositions** (*list of integers*) –
* **optimizationLineYPositions** (*list of integers*) –
* **isDoCmd** (*bool*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextAction.html
        """

    Attributes: 'RichTextAttr'  # `Attributes`[¶](#wx.richtext.RichTextAction.Attributes "Permalink to this definition")See [`GetAttributes`](#wx.richtext.RichTextAction.GetAttributes "wx.richtext.RichTextAction.GetAttributes")
    Container: 'RichTextParagraphLayoutBox'  # `Container`[¶](#wx.richtext.RichTextAction.Container "Permalink to this definition")See [`GetContainer`](#wx.richtext.RichTextAction.GetContainer "wx.richtext.RichTextAction.GetContainer")
    ContainerAddress: 'RichTextObjectAddress'  # `ContainerAddress`[¶](#wx.richtext.RichTextAction.ContainerAddress "Permalink to this definition")See [`GetContainerAddress`](#wx.richtext.RichTextAction.GetContainerAddress "wx.richtext.RichTextAction.GetContainerAddress") and [`SetContainerAddress`](#wx.richtext.RichTextAction.SetContainerAddress "wx.richtext.RichTextAction.SetContainerAddress")
    IgnoreFirstTime: bool  # `IgnoreFirstTime`[¶](#wx.richtext.RichTextAction.IgnoreFirstTime "Permalink to this definition")See [`GetIgnoreFirstTime`](#wx.richtext.RichTextAction.GetIgnoreFirstTime "wx.richtext.RichTextAction.GetIgnoreFirstTime") and [`SetIgnoreFirstTime`](#wx.richtext.RichTextAction.SetIgnoreFirstTime "wx.richtext.RichTextAction.SetIgnoreFirstTime")
    Name: str  # `Name`[¶](#wx.richtext.RichTextAction.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextAction.GetName "wx.richtext.RichTextAction.GetName")
    NewParagraphs: 'RichTextParagraphLayoutBox'  # `NewParagraphs`[¶](#wx.richtext.RichTextAction.NewParagraphs "Permalink to this definition")See [`GetNewParagraphs`](#wx.richtext.RichTextAction.GetNewParagraphs "wx.richtext.RichTextAction.GetNewParagraphs")
    Object: 'RichTextObject'  # `Object`[¶](#wx.richtext.RichTextAction.Object "Permalink to this definition")See [`GetObject`](#wx.richtext.RichTextAction.GetObject "wx.richtext.RichTextAction.GetObject") and [`SetObject`](#wx.richtext.RichTextAction.SetObject "wx.richtext.RichTextAction.SetObject")
    OldParagraphs: 'RichTextParagraphLayoutBox'  # `OldParagraphs`[¶](#wx.richtext.RichTextAction.OldParagraphs "Permalink to this definition")See [`GetOldParagraphs`](#wx.richtext.RichTextAction.GetOldParagraphs "wx.richtext.RichTextAction.GetOldParagraphs")
    Position: int  # `Position`[¶](#wx.richtext.RichTextAction.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.RichTextAction.GetPosition "wx.richtext.RichTextAction.GetPosition") and [`SetPosition`](#wx.richtext.RichTextAction.SetPosition "wx.richtext.RichTextAction.SetPosition")
    Range: 'RichTextRange'  # `Range`[¶](#wx.richtext.RichTextAction.Range "Permalink to this definition")See [`GetRange`](#wx.richtext.RichTextAction.GetRange "wx.richtext.RichTextAction.GetRange") and [`SetRange`](#wx.richtext.RichTextAction.SetRange "wx.richtext.RichTextAction.SetRange")



RICHTEXT_CHANGE_OBJECT: int

class RichTextDrawingContext(Object):
    """ **Possible constructors**:



```
RichTextDrawingContext(buffer)

```


A class for passing information to drawing and measuring functions.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
    """
    def __init__(self, buffer: 'richtext.RichTextBuffer') -> None:
        """ 

`__init__`(*self*, *buffer*)[¶](#wx.richtext.RichTextDrawingContext.__init__ "Permalink to this definition")
Pass the buffer to the context so the context can retrieve information such as virtual attributes.



Parameters
**buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def ApplyVirtualAttributes(self, attr, obj) -> bool:
        """ 

`ApplyVirtualAttributes`(*self*, *attr*, *obj*)[¶](#wx.richtext.RichTextDrawingContext.ApplyVirtualAttributes "Permalink to this definition")
Applies any virtual attributes relevant to this object.



Parameters
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableDelayedImageLoading(self, b: bool) -> None:
        """ 

`EnableDelayedImageLoading`(*self*, *b*)[¶](#wx.richtext.RichTextDrawingContext.EnableDelayedImageLoading "Permalink to this definition")
Enable or disable delayed image loading.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableImages(self, b: bool) -> None:
        """ 

`EnableImages`(*self*, *b*)[¶](#wx.richtext.RichTextDrawingContext.EnableImages "Permalink to this definition")
Enable or disable images.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def EnableVirtualAttributes(self, b: bool) -> None:
        """ 

`EnableVirtualAttributes`(*self*, *b*)[¶](#wx.richtext.RichTextDrawingContext.EnableVirtualAttributes "Permalink to this definition")
Enables virtual attribute processing.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetDelayedImageLoading(self) -> bool:
        """ 

`GetDelayedImageLoading`(*self*)[¶](#wx.richtext.RichTextDrawingContext.GetDelayedImageLoading "Permalink to this definition")
Returns `True` if delayed image loading is enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetImagesEnabled(self) -> bool:
        """ 

`GetImagesEnabled`(*self*)[¶](#wx.richtext.RichTextDrawingContext.GetImagesEnabled "Permalink to this definition")
Returns `True` if images are enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetLayingOut(self) -> bool:
        """ 

`GetLayingOut`(*self*)[¶](#wx.richtext.RichTextDrawingContext.GetLayingOut "Permalink to this definition")
Returns `True` if laying out.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualAttributes(self, obj: 'richtext.RichTextObject') -> 'RichTextAttr':
        """ 

`GetVirtualAttributes`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingContext.GetVirtualAttributes "Permalink to this definition")
Returns the virtual attributes for this object.


Virtual attributes can be provided for visual cues without affecting the actual styling.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualAttributesEnabled(self) -> bool:
        """ 

`GetVirtualAttributesEnabled`(*self*)[¶](#wx.richtext.RichTextDrawingContext.GetVirtualAttributesEnabled "Permalink to this definition")
Returns `True` if virtual attribute processing is enabled.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualSubobjectAttributes(self, obj, positions, attributes) -> int:
        """ 

`GetVirtualSubobjectAttributes`(*self*, *obj*, *positions*, *attributes*)[¶](#wx.richtext.RichTextDrawingContext.GetVirtualSubobjectAttributes "Permalink to this definition")
Gets the mixed virtual attributes for individual positions within the object.


For example, individual characters within a text object may require special highlighting. The function is passed the count returned by GetVirtualSubobjectAttributesCount.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **positions** (*list of integers*) –
* **attributes** (*RichTextAttrArray*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualSubobjectAttributesCount(self, obj: 'richtext.RichTextObject') -> int:
        """ 

`GetVirtualSubobjectAttributesCount`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingContext.GetVirtualSubobjectAttributesCount "Permalink to this definition")
Gets the count for mixed virtual attributes for individual positions within the object.


For example, individual characters within a text object may require special highlighting.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def GetVirtualText(self, obj, text) -> bool:
        """ 

`GetVirtualText`(*self*, *obj*, *text*)[¶](#wx.richtext.RichTextDrawingContext.GetVirtualText "Permalink to this definition")
Gets the virtual text for this object.



Parameters
* **obj** ([*wx.richtext.RichTextPlainText*](wx.richtext.RichTextPlainText.html#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def HasVirtualAttributes(self, obj: 'richtext.RichTextObject') -> bool:
        """ 

`HasVirtualAttributes`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingContext.HasVirtualAttributes "Permalink to this definition")
Does this object have virtual attributes? Virtual attributes can be provided for visual cues without affecting the actual styling.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def HasVirtualText(self, obj: 'richtext.RichTextPlainText') -> bool:
        """ 

`HasVirtualText`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingContext.HasVirtualText "Permalink to this definition")
Do we have virtual text for this object? Virtual text allows an application to replace characters in an object for editing and display purposes, for example for highlighting special characters.



Parameters
**obj** ([*wx.richtext.RichTextPlainText*](wx.richtext.RichTextPlainText.html#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextDrawingContext.Init "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    def SetLayingOut(self, b: bool) -> None:
        """ 

`SetLayingOut`(*self*, *b*)[¶](#wx.richtext.RichTextDrawingContext.SetLayingOut "Permalink to this definition")
Set laying out flag.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingContext.html
        """

    DelayedImageLoading: bool  # `DelayedImageLoading`[¶](#wx.richtext.RichTextDrawingContext.DelayedImageLoading "Permalink to this definition")See [`GetDelayedImageLoading`](#wx.richtext.RichTextDrawingContext.GetDelayedImageLoading "wx.richtext.RichTextDrawingContext.GetDelayedImageLoading")
    ImagesEnabled: bool  # `ImagesEnabled`[¶](#wx.richtext.RichTextDrawingContext.ImagesEnabled "Permalink to this definition")See [`GetImagesEnabled`](#wx.richtext.RichTextDrawingContext.GetImagesEnabled "wx.richtext.RichTextDrawingContext.GetImagesEnabled")
    LayingOut: bool  # `LayingOut`[¶](#wx.richtext.RichTextDrawingContext.LayingOut "Permalink to this definition")See [`GetLayingOut`](#wx.richtext.RichTextDrawingContext.GetLayingOut "wx.richtext.RichTextDrawingContext.GetLayingOut") and [`SetLayingOut`](#wx.richtext.RichTextDrawingContext.SetLayingOut "wx.richtext.RichTextDrawingContext.SetLayingOut")
    VirtualAttributesEnabled: bool  # `VirtualAttributesEnabled`[¶](#wx.richtext.RichTextDrawingContext.VirtualAttributesEnabled "Permalink to this definition")See [`GetVirtualAttributesEnabled`](#wx.richtext.RichTextDrawingContext.GetVirtualAttributesEnabled "wx.richtext.RichTextDrawingContext.GetVirtualAttributesEnabled")
    m_buffer: Any  # `m_buffer`[¶](#wx.richtext.RichTextDrawingContext.m_buffer "Permalink to this definition")A public C++ attribute of type [`RichTextBuffer`](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer") .
    m_enableDelayedImageLoading: Any  # `m_enableDelayedImageLoading`[¶](#wx.richtext.RichTextDrawingContext.m_enableDelayedImageLoading "Permalink to this definition")A public C++ attribute of type `bool`.
    m_enableImages: Any  # `m_enableImages`[¶](#wx.richtext.RichTextDrawingContext.m_enableImages "Permalink to this definition")A public C++ attribute of type `bool`.
    m_enableVirtualAttributes: Any  # `m_enableVirtualAttributes`[¶](#wx.richtext.RichTextDrawingContext.m_enableVirtualAttributes "Permalink to this definition")A public C++ attribute of type `bool`.
    m_layingOut: Any  # `m_layingOut`[¶](#wx.richtext.RichTextDrawingContext.m_layingOut "Permalink to this definition")A public C++ attribute of type `bool`.



class RichTextDrawingHandler(Object):
    """ **Possible constructors**:



```
RichTextDrawingHandler(name="")

```


The base class for custom drawing handlers.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
    """
    def __init__(self, name: str="") -> None:
        """ 

`__init__`(*self*, *name=""*)[¶](#wx.richtext.RichTextDrawingHandler.__init__ "Permalink to this definition")
Creates a drawing handler object.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextDrawingHandler.GetName "Permalink to this definition")
Returns the name of the handler.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualAttributes(self, attr, obj) -> bool:
        """ 

`GetVirtualAttributes`(*self*, *attr*, *obj*)[¶](#wx.richtext.RichTextDrawingHandler.GetVirtualAttributes "Permalink to this definition")
Provides virtual attributes that we can provide.



Parameters
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualSubobjectAttributes(self, obj, positions, attributes) -> int:
        """ 

`GetVirtualSubobjectAttributes`(*self*, *obj*, *positions*, *attributes*)[¶](#wx.richtext.RichTextDrawingHandler.GetVirtualSubobjectAttributes "Permalink to this definition")
Gets the mixed virtual attributes for individual positions within the object.


For example, individual characters within a text object may require special highlighting. Returns the number of virtual attributes found.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **positions** (*list of integers*) –
* **attributes** (*RichTextAttrArray*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualSubobjectAttributesCount(self, obj: 'richtext.RichTextObject') -> int:
        """ 

`GetVirtualSubobjectAttributesCount`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingHandler.GetVirtualSubobjectAttributesCount "Permalink to this definition")
Gets the count for mixed virtual attributes for individual positions within the object.


For example, individual characters within a text object may require special highlighting.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def GetVirtualText(self, obj, text) -> bool:
        """ 

`GetVirtualText`(*self*, *obj*, *text*)[¶](#wx.richtext.RichTextDrawingHandler.GetVirtualText "Permalink to this definition")
Gets the virtual text for this object.



Parameters
* **obj** ([*wx.richtext.RichTextPlainText*](wx.richtext.RichTextPlainText.html#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def HasVirtualAttributes(self, obj: 'richtext.RichTextObject') -> bool:
        """ 

`HasVirtualAttributes`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingHandler.HasVirtualAttributes "Permalink to this definition")
Returns `True` if this object has virtual attributes that we can provide.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def HasVirtualText(self, obj: 'richtext.RichTextPlainText') -> bool:
        """ 

`HasVirtualText`(*self*, *obj*)[¶](#wx.richtext.RichTextDrawingHandler.HasVirtualText "Permalink to this definition")
Do we have virtual text for this object? Virtual text allows an application to replace characters in an object for editing and display purposes, for example for highlighting special characters.



Parameters
**obj** ([*wx.richtext.RichTextPlainText*](wx.richtext.RichTextPlainText.html#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextDrawingHandler.SetName "Permalink to this definition")
Sets the name of the handler.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextDrawingHandler.html
        """

    Name: str  # `Name`[¶](#wx.richtext.RichTextDrawingHandler.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextDrawingHandler.GetName "wx.richtext.RichTextDrawingHandler.GetName") and [`SetName`](#wx.richtext.RichTextDrawingHandler.SetName "wx.richtext.RichTextDrawingHandler.SetName")



class RichTextFieldType(Object):
    """ **Possible constructors**:



```
RichTextFieldType(name="")

RichTextFieldType(fieldType)

```


The base class for custom field types.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFieldType.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, name=””)*


Creates a field type definition.



Parameters
**name** (*string*) – 






---

  



**\_\_init\_\_** *(self, fieldType)*


Copy constructor.



Parameters
**fieldType** ([*wx.richtext.RichTextFieldType*](#wx.richtext.RichTextFieldType "wx.richtext.RichTextFieldType")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def CanEditProperties(self, obj: 'richtext.RichTextField') -> bool:
        """ 

`CanEditProperties`(*self*, *obj*)[¶](#wx.richtext.RichTextFieldType.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Parameters
**obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Copy(self, fieldType: 'richtext.RichTextFieldType') -> None:
        """ 

`Copy`(*self*, *fieldType*)[¶](#wx.richtext.RichTextFieldType.Copy "Permalink to this definition")

Parameters
**fieldType** ([*wx.richtext.RichTextFieldType*](#wx.richtext.RichTextFieldType "wx.richtext.RichTextFieldType")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Draw(self, obj, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *obj*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextFieldType.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def EditProperties(self, obj, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *obj*, *parent*, *buffer*)[¶](#wx.richtext.RichTextFieldType.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextFieldType.GetName "Permalink to this definition")
Returns the field type name.


There should be a unique name per field type object.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetPropertiesMenuLabel(self, obj: 'richtext.RichTextField') -> str:
        """ 

`GetPropertiesMenuLabel`(*self*, *obj*)[¶](#wx.richtext.RichTextFieldType.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Parameters
**obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *obj*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextFieldType.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def IsTopLevel(self, obj: 'richtext.RichTextField') -> bool:
        """ 

`IsTopLevel`(*self*, *obj*)[¶](#wx.richtext.RichTextFieldType.IsTopLevel "Permalink to this definition")
Returns `True` if this object is top-level, i.e. contains its own paragraphs, such as a text box.



Parameters
**obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def Layout(self, obj, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *obj*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextFieldType.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextFieldType.SetName "Permalink to this definition")
Sets the field type name.


There should be a unique name per field type object.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    def UpdateField(self, buffer, obj) -> bool:
        """ 

`UpdateField`(*self*, *buffer*, *obj*)[¶](#wx.richtext.RichTextFieldType.UpdateField "Permalink to this definition")
Update the field.


This would typically expand the field to its value, if this is a dynamically changing and/or composite field.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldType.html
        """

    Name: str  # `Name`[¶](#wx.richtext.RichTextFieldType.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextFieldType.GetName "wx.richtext.RichTextFieldType.GetName") and [`SetName`](#wx.richtext.RichTextFieldType.SetName "wx.richtext.RichTextFieldType.SetName")



class RichTextFileHandler(Object):
    """ **Possible constructors**:



```
RichTextFileHandler(name="", ext="", type=0)

```


The base class for file handlers.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
    """
    def __init__(self, name="", ext="", type=0) -> None:
        """ 

`__init__`(*self*, *name=""*, *ext=""*, *type=0*)[¶](#wx.richtext.RichTextFileHandler.__init__ "Permalink to this definition")
Creates a file handler object.



Parameters
* **name** (*string*) –
* **ext** (*string*) –
* **type** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanHandle(self, filename: str) -> bool:
        """ 

`CanHandle`(*self*, *filename*)[¶](#wx.richtext.RichTextFileHandler.CanHandle "Permalink to this definition")
Returns `True` if we handle this filename (if using files).


By default, checks the extension.



Parameters
**filename** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanLoad(self) -> bool:
        """ 

`CanLoad`(*self*)[¶](#wx.richtext.RichTextFileHandler.CanLoad "Permalink to this definition")
Returns `True` if we can load using this handler.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def CanSave(self) -> bool:
        """ 

`CanSave`(*self*)[¶](#wx.richtext.RichTextFileHandler.CanSave "Permalink to this definition")
Returns `True` if we can save using this handler.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def DoLoadFile(self, buffer, stream) -> bool:
        """ 

`DoLoadFile`(*self*, *buffer*, *stream*)[¶](#wx.richtext.RichTextFileHandler.DoLoadFile "Permalink to this definition")
Override to load content from *stream* into *buffer*.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def DoSaveFile(self, buffer, stream) -> bool:
        """ 

`DoSaveFile`(*self*, *buffer*, *stream*)[¶](#wx.richtext.RichTextFileHandler.DoSaveFile "Permalink to this definition")
Override to save content to *stream* from *buffer*.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetEncoding(self) -> str:
        """ 

`GetEncoding`(*self*)[¶](#wx.richtext.RichTextFileHandler.GetEncoding "Permalink to this definition")
Returns the encoding to use when saving a file.


If empty, a suitable encoding is chosen.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetExtension(self) -> str:
        """ 

`GetExtension`(*self*)[¶](#wx.richtext.RichTextFileHandler.GetExtension "Permalink to this definition")
Returns the default extension to recognise.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.RichTextFileHandler.GetFlags "Permalink to this definition")
Returns flags controlling how loading and saving is done.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextFileHandler.GetName "Permalink to this definition")
Returns the name of the handler.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def GetType(self) -> int:
        """ 

`GetType`(*self*)[¶](#wx.richtext.RichTextFileHandler.GetType "Permalink to this definition")
Returns the handler type.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def IsVisible(self) -> bool:
        """ 

`IsVisible`(*self*)[¶](#wx.richtext.RichTextFileHandler.IsVisible "Permalink to this definition")
Returns `True` if this handler should be visible to the user.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def LoadFile(self, *args, **kw) -> bool:
        """ 

`LoadFile`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFileHandler.LoadFile "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadFile** *(self, buffer, stream)*


Loads the buffer from a stream.


Not all handlers will implement file loading.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –



Return type
*bool*






---

  



**LoadFile** *(self, buffer, filename)*


Loads the buffer from a file.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **filename** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SaveFile(self, *args, **kw) -> bool:
        """ 

`SaveFile`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFileHandler.SaveFile "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SaveFile** *(self, buffer, stream)*


Saves the buffer to a stream.


Not all handlers will implement file saving.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –



Return type
*bool*






---

  



**SaveFile** *(self, buffer, filename)*


Saves the buffer to a file.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **filename** (*string*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetEncoding(self, encoding: str) -> None:
        """ 

`SetEncoding`(*self*, *encoding*)[¶](#wx.richtext.RichTextFileHandler.SetEncoding "Permalink to this definition")
Sets the encoding to use when saving a file.


If empty, a suitable encoding is chosen.



Parameters
**encoding** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetExtension(self, ext: str) -> None:
        """ 

`SetExtension`(*self*, *ext*)[¶](#wx.richtext.RichTextFileHandler.SetExtension "Permalink to this definition")
Sets the default extension to recognise.



Parameters
**ext** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.RichTextFileHandler.SetFlags "Permalink to this definition")
Sets flags that change the behaviour of loading or saving.


See the documentation for each handler class to see what flags are relevant for each handler.


You call this function directly if you are using a file handler explicitly (without going through the text control or buffer LoadFile/SaveFile API). Or, you can call the control or buffer’s SetHandlerFlags function to set the flags that will be used for subsequent load and save operations.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextFileHandler.SetName "Permalink to this definition")
Sets the name of the handler.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetType(self, type: int) -> None:
        """ 

`SetType`(*self*, *type*)[¶](#wx.richtext.RichTextFileHandler.SetType "Permalink to this definition")
Sets the handler type.



Parameters
**type** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    def SetVisible(self, visible: bool) -> None:
        """ 

`SetVisible`(*self*, *visible*)[¶](#wx.richtext.RichTextFileHandler.SetVisible "Permalink to this definition")
Sets whether the handler should be visible to the user (via the application’s load and save dialogs).



Parameters
**visible** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFileHandler.html
        """

    Encoding: str  # `Encoding`[¶](#wx.richtext.RichTextFileHandler.Encoding "Permalink to this definition")See [`GetEncoding`](#wx.richtext.RichTextFileHandler.GetEncoding "wx.richtext.RichTextFileHandler.GetEncoding") and [`SetEncoding`](#wx.richtext.RichTextFileHandler.SetEncoding "wx.richtext.RichTextFileHandler.SetEncoding")
    Extension: str  # `Extension`[¶](#wx.richtext.RichTextFileHandler.Extension "Permalink to this definition")See [`GetExtension`](#wx.richtext.RichTextFileHandler.GetExtension "wx.richtext.RichTextFileHandler.GetExtension") and [`SetExtension`](#wx.richtext.RichTextFileHandler.SetExtension "wx.richtext.RichTextFileHandler.SetExtension")
    Flags: int  # `Flags`[¶](#wx.richtext.RichTextFileHandler.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.RichTextFileHandler.GetFlags "wx.richtext.RichTextFileHandler.GetFlags") and [`SetFlags`](#wx.richtext.RichTextFileHandler.SetFlags "wx.richtext.RichTextFileHandler.SetFlags")
    Name: str  # `Name`[¶](#wx.richtext.RichTextFileHandler.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextFileHandler.GetName "wx.richtext.RichTextFileHandler.GetName") and [`SetName`](#wx.richtext.RichTextFileHandler.SetName "wx.richtext.RichTextFileHandler.SetName")
    Type: int  # `Type`[¶](#wx.richtext.RichTextFileHandler.Type "Permalink to this definition")See [`GetType`](#wx.richtext.RichTextFileHandler.GetType "wx.richtext.RichTextFileHandler.GetType") and [`SetType`](#wx.richtext.RichTextFileHandler.SetType "wx.richtext.RichTextFileHandler.SetType")



class RichTextFontTable(Object):
    """ **Possible constructors**:



```
RichTextFontTable()

RichTextFontTable(table)

```


Manages quick access to a pool of fonts for rendering rich text.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFontTable.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, table)*


Copy constructor.



Parameters
**table** ([*wx.richtext.RichTextFontTable*](#wx.richtext.RichTextFontTable "wx.richtext.RichTextFontTable")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextFontTable.Clear "Permalink to this definition")
Clears the font table.




            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def FindFont(self, fontSpec: 'richtext.RichTextAttr') -> 'Font':
        """ 

`FindFont`(*self*, *fontSpec*)[¶](#wx.richtext.RichTextFontTable.FindFont "Permalink to this definition")
Finds a font for the given attribute object.



Parameters
**fontSpec** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*Font*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.richtext.RichTextFontTable.IsOk "Permalink to this definition")
Returns `True` if the font table is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def SetFontScale(self, fontScale: float) -> None:
        """ 

`SetFontScale`(*self*, *fontScale*)[¶](#wx.richtext.RichTextFontTable.SetFontScale "Permalink to this definition")
Set the font scale factor.



Parameters
**fontScale** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def __ne__(self, item: Any) -> bool:
        """ 

`__ne__`(*self*)[¶](#wx.richtext.RichTextFontTable.__ne__ "Permalink to this definition")
Inequality operator.



Parameters
**table** ([*wx.richtext.RichTextFontTable*](#wx.richtext.RichTextFontTable "wx.richtext.RichTextFontTable")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.RichTextFontTable.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**table** ([*wx.richtext.RichTextFontTable*](#wx.richtext.RichTextFontTable "wx.richtext.RichTextFontTable")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFontTable.html
        """



class RichTextFormattingDialogFactory(Object):
    """ **Possible constructors**:



```
RichTextFormattingDialogFactory()

```


This class provides pages for RichTextFormattingDialog, and allows
other customization of the dialog.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.RichTextFormattingDialogFactory.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreateButtons(self, dialog: 'richtext.RichTextFormattingDialog') -> bool:
        """ 

`CreateButtons`(*self*, *dialog*)[¶](#wx.richtext.RichTextFormattingDialogFactory.CreateButtons "Permalink to this definition")
Creates the main dialog buttons.



Parameters
**dialog** ([*wx.richtext.RichTextFormattingDialog*](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog "wx.richtext.RichTextFormattingDialog")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreatePage(self, page, title, dialog) -> 'Panel':
        """ 

`CreatePage`(*self*, *page*, *title*, *dialog*)[¶](#wx.richtext.RichTextFormattingDialogFactory.CreatePage "Permalink to this definition")
Creates a page, given a page identifier.



Parameters
* **page** (*int*) –
* **title** (*string*) –
* **dialog** ([*wx.richtext.RichTextFormattingDialog*](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog "wx.richtext.RichTextFormattingDialog")) –



Return type
*Panel*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def CreatePages(self, pages, dialog) -> bool:
        """ 

`CreatePages`(*self*, *pages*, *dialog*)[¶](#wx.richtext.RichTextFormattingDialogFactory.CreatePages "Permalink to this definition")
Creates all pages under the dialog’s book control, also calling AddPage().



Parameters
* **pages** (*long*) –
* **dialog** ([*wx.richtext.RichTextFormattingDialog*](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog "wx.richtext.RichTextFormattingDialog")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageId(self, i: int) -> int:
        """ 

`GetPageId`(*self*, *i*)[¶](#wx.richtext.RichTextFormattingDialogFactory.GetPageId "Permalink to this definition")
Enumerate all available page identifiers.



Parameters
**i** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageIdCount(self) -> int:
        """ 

`GetPageIdCount`(*self*)[¶](#wx.richtext.RichTextFormattingDialogFactory.GetPageIdCount "Permalink to this definition")
Gets the number of available page identifiers.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def GetPageImage(self, id: int) -> int:
        """ 

`GetPageImage`(*self*, *id*)[¶](#wx.richtext.RichTextFormattingDialogFactory.GetPageImage "Permalink to this definition")
Gets the image index for the given page identifier.



Parameters
**id** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def SetSheetStyle(self, dialog: 'richtext.RichTextFormattingDialog') -> bool:
        """ 

`SetSheetStyle`(*self*, *dialog*)[¶](#wx.richtext.RichTextFormattingDialogFactory.SetSheetStyle "Permalink to this definition")
Set the property sheet style, called at the start of [`wx.richtext.RichTextFormattingDialog.Create`](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog.Create "wx.richtext.RichTextFormattingDialog.Create") .



Parameters
**dialog** ([*wx.richtext.RichTextFormattingDialog*](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog "wx.richtext.RichTextFormattingDialog")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    def ShowHelp(self, page, dialog) -> bool:
        """ 

`ShowHelp`(*self*, *page*, *dialog*)[¶](#wx.richtext.RichTextFormattingDialogFactory.ShowHelp "Permalink to this definition")
Invokes help for the dialog.



Parameters
* **page** (*int*) –
* **dialog** ([*wx.richtext.RichTextFormattingDialog*](wx.richtext.RichTextFormattingDialog.html#wx.richtext.RichTextFormattingDialog "wx.richtext.RichTextFormattingDialog")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialogFactory.html
        """

    PageIdCount: int  # `PageIdCount`[¶](#wx.richtext.RichTextFormattingDialogFactory.PageIdCount "Permalink to this definition")See [`GetPageIdCount`](#wx.richtext.RichTextFormattingDialogFactory.GetPageIdCount "wx.richtext.RichTextFormattingDialogFactory.GetPageIdCount")



class RichTextHeaderFooterData(Object):
    """ **Possible constructors**:



```
RichTextHeaderFooterData()

RichTextHeaderFooterData(data)

```


This class represents header and footer data to be passed to the
RichTextPrinting and RichTextPrintout classes.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextHeaderFooterData.__init__ "Permalink to this definition")
Constructors.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, data)*



Parameters
**data** ([*wx.richtext.RichTextHeaderFooterData*](#wx.richtext.RichTextHeaderFooterData "wx.richtext.RichTextHeaderFooterData")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.Clear "Permalink to this definition")
Clears all text.




            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Copy(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ 

`Copy`(*self*, *data*)[¶](#wx.richtext.RichTextHeaderFooterData.Copy "Permalink to this definition")
Copies the data.



Parameters
**data** ([*wx.richtext.RichTextHeaderFooterData*](#wx.richtext.RichTextHeaderFooterData "wx.richtext.RichTextHeaderFooterData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.GetFont "Permalink to this definition")
Returns the font specified for printing the header and footer.



Return type
[`Font`](#wx.richtext.RichTextHeaderFooterData.Font "wx.richtext.RichTextHeaderFooterData.Font")






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFooterMargin(self) -> int:
        """ 

`GetFooterMargin`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.GetFooterMargin "Permalink to this definition")
Returns the margin between the text and the footer.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetFooterText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ 

`GetFooterText`(*self*, *page=RICHTEXT\_PAGE\_EVEN*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextHeaderFooterData.GetFooterText "Permalink to this definition")
Returns the footer text on odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetHeaderMargin(self) -> int:
        """ 

`GetHeaderMargin`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.GetHeaderMargin "Permalink to this definition")
Returns the margin between the text and the header.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetHeaderText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ 

`GetHeaderText`(*self*, *page=RICHTEXT\_PAGE\_EVEN*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextHeaderFooterData.GetHeaderText "Permalink to this definition")
Returns the header text on odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetShowOnFirstPage(self) -> bool:
        """ 

`GetShowOnFirstPage`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.GetShowOnFirstPage "Permalink to this definition")
Returns `True` if the header and footer will be shown on the first page.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetText(self, headerFooter, page, location) -> str:
        """ 

`GetText`(*self*, *headerFooter*, *page*, *location*)[¶](#wx.richtext.RichTextHeaderFooterData.GetText "Permalink to this definition")
Helper function for getting the header or footer text, odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **headerFooter** (*int*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def GetTextColour(self) -> 'Colour':
        """ 

`GetTextColour`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.GetTextColour "Permalink to this definition")
Returns the text colour for drawing the header and footer.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextHeaderFooterData.Init "Permalink to this definition")
Initialises the object.




            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.richtext.RichTextHeaderFooterData.SetFont "Permalink to this definition")
Sets the font for drawing the header and footer.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetFooterText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ 

`SetFooterText`(*self*, *text*, *page=RICHTEXT\_PAGE\_ALL*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextHeaderFooterData.SetFooterText "Permalink to this definition")
Sets the footer text on odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **text** (*string*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetHeaderText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ 

`SetHeaderText`(*self*, *text*, *page=RICHTEXT\_PAGE\_ALL*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextHeaderFooterData.SetHeaderText "Permalink to this definition")
Sets the header text on odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **text** (*string*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetMargins(self, headerMargin, footerMargin) -> None:
        """ 

`SetMargins`(*self*, *headerMargin*, *footerMargin*)[¶](#wx.richtext.RichTextHeaderFooterData.SetMargins "Permalink to this definition")
Sets the margins between text and header or footer, in tenths of a millimeter.



Parameters
* **headerMargin** (*int*) –
* **footerMargin** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetShowOnFirstPage(self, showOnFirstPage: bool) -> None:
        """ 

`SetShowOnFirstPage`(*self*, *showOnFirstPage*)[¶](#wx.richtext.RichTextHeaderFooterData.SetShowOnFirstPage "Permalink to this definition")
Pass `True` to show the header or footer on first page (the default).



Parameters
**showOnFirstPage** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetText(self, text, headerFooter, page, location) -> None:
        """ 

`SetText`(*self*, *text*, *headerFooter*, *page*, *location*)[¶](#wx.richtext.RichTextHeaderFooterData.SetText "Permalink to this definition")
Helper function for setting the header or footer text, odd or even pages, and at a given position on the page (left, centre or right).



Parameters
* **text** (*string*) –
* **headerFooter** (*int*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    def SetTextColour(self, col: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *col*)[¶](#wx.richtext.RichTextHeaderFooterData.SetTextColour "Permalink to this definition")
Sets the text colour for drawing the header and footer.



Parameters
**col** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHeaderFooterData.html
        """

    Font: '_Font'  # `Font`[¶](#wx.richtext.RichTextHeaderFooterData.Font "Permalink to this definition")See [`GetFont`](#wx.richtext.RichTextHeaderFooterData.GetFont "wx.richtext.RichTextHeaderFooterData.GetFont") and [`SetFont`](#wx.richtext.RichTextHeaderFooterData.SetFont "wx.richtext.RichTextHeaderFooterData.SetFont")
    FooterMargin: int  # `FooterMargin`[¶](#wx.richtext.RichTextHeaderFooterData.FooterMargin "Permalink to this definition")See [`GetFooterMargin`](#wx.richtext.RichTextHeaderFooterData.GetFooterMargin "wx.richtext.RichTextHeaderFooterData.GetFooterMargin")
    FooterText: str  # `FooterText`[¶](#wx.richtext.RichTextHeaderFooterData.FooterText "Permalink to this definition")See [`GetFooterText`](#wx.richtext.RichTextHeaderFooterData.GetFooterText "wx.richtext.RichTextHeaderFooterData.GetFooterText") and [`SetFooterText`](#wx.richtext.RichTextHeaderFooterData.SetFooterText "wx.richtext.RichTextHeaderFooterData.SetFooterText")
    HeaderMargin: int  # `HeaderMargin`[¶](#wx.richtext.RichTextHeaderFooterData.HeaderMargin "Permalink to this definition")See [`GetHeaderMargin`](#wx.richtext.RichTextHeaderFooterData.GetHeaderMargin "wx.richtext.RichTextHeaderFooterData.GetHeaderMargin")
    HeaderText: str  # `HeaderText`[¶](#wx.richtext.RichTextHeaderFooterData.HeaderText "Permalink to this definition")See [`GetHeaderText`](#wx.richtext.RichTextHeaderFooterData.GetHeaderText "wx.richtext.RichTextHeaderFooterData.GetHeaderText") and [`SetHeaderText`](#wx.richtext.RichTextHeaderFooterData.SetHeaderText "wx.richtext.RichTextHeaderFooterData.SetHeaderText")
    ShowOnFirstPage: bool  # `ShowOnFirstPage`[¶](#wx.richtext.RichTextHeaderFooterData.ShowOnFirstPage "Permalink to this definition")See [`GetShowOnFirstPage`](#wx.richtext.RichTextHeaderFooterData.GetShowOnFirstPage "wx.richtext.RichTextHeaderFooterData.GetShowOnFirstPage") and [`SetShowOnFirstPage`](#wx.richtext.RichTextHeaderFooterData.SetShowOnFirstPage "wx.richtext.RichTextHeaderFooterData.SetShowOnFirstPage")
    TextColour: 'Colour'  # `TextColour`[¶](#wx.richtext.RichTextHeaderFooterData.TextColour "Permalink to this definition")See [`GetTextColour`](#wx.richtext.RichTextHeaderFooterData.GetTextColour "wx.richtext.RichTextHeaderFooterData.GetTextColour") and [`SetTextColour`](#wx.richtext.RichTextHeaderFooterData.SetTextColour "wx.richtext.RichTextHeaderFooterData.SetTextColour")



class RichTextImageBlock(Object):
    """ **Possible constructors**:



```
RichTextImageBlock()

RichTextImageBlock(block)

```


This class stores information about an image, in binary in-memory
form.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextImageBlock.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Constructor.




---

  



**\_\_init\_\_** *(self, block)*


Copy constructor.



Parameters
**block** ([*wx.richtext.RichTextImageBlock*](#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextImageBlock.Clear "Permalink to this definition")
Clears the block.




            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Copy(self, block: 'richtext.RichTextImageBlock') -> None:
        """ 

`Copy`(*self*, *block*)[¶](#wx.richtext.RichTextImageBlock.Copy "Permalink to this definition")
Copy from *block*.



Parameters
**block** ([*wx.richtext.RichTextImageBlock*](#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def DoMakeImageBlock(self, image, imageType) -> bool:
        """ 

`DoMakeImageBlock`(*self*, *image*, *imageType*)[¶](#wx.richtext.RichTextImageBlock.DoMakeImageBlock "Permalink to this definition")
Makes the image block.



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetData(self) -> int:
        """ 

`GetData`(*self*)[¶](#wx.richtext.RichTextImageBlock.GetData "Permalink to this definition")
Returns the raw data.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetDataSize(self) -> int:
        """ 

`GetDataSize`(*self*)[¶](#wx.richtext.RichTextImageBlock.GetDataSize "Permalink to this definition")
Returns the data size in bytes.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetExtension(self) -> str:
        """ 

`GetExtension`(*self*)[¶](#wx.richtext.RichTextImageBlock.GetExtension "Permalink to this definition")
Gets the extension for the block’s type.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def GetImageType(self) -> 'BitmapType':
        """ 

`GetImageType`(*self*)[¶](#wx.richtext.RichTextImageBlock.GetImageType "Permalink to this definition")
Returns the image type.



Return type
 [wx.BitmapType](wx.BitmapType.enumeration.html#wx-bitmaptype)






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextImageBlock.Init "Permalink to this definition")
Initialises the block.




            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def IsOk(self) -> bool:
        """ 

`IsOk`(*self*)[¶](#wx.richtext.RichTextImageBlock.IsOk "Permalink to this definition")
Returns `True` if the data is not `None`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Load(self, image: 'Image') -> bool:
        """ 

`Load`(*self*, *image*)[¶](#wx.richtext.RichTextImageBlock.Load "Permalink to this definition")

Parameters
**image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def MakeImageBlock(self, *args, **kw) -> bool:
        """ 

`MakeImageBlock`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextImageBlock.MakeImageBlock "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**MakeImageBlock** *(self, filename, imageType, image, convertToJPEG=True)*


Load the original image into a memory block.


If the image is not a `JPEG`, we must convert it into a `JPEG` to conserve space. If it’s not a `JPEG` we can make use of *image*, already scaled, so we don’t have to load the image a second time.



Parameters
* **filename** (*string*) –
* **imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **convertToJPEG** (*bool*) –



Return type
*bool*






---

  



**MakeImageBlock** *(self, image, imageType, quality=80)*


Make an image block from the  [wx.Image](wx.Image.html#wx-image) in the given format.



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –
* **quality** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def MakeImageBlockDefaultQuality(self, image, imageType) -> bool:
        """ 

`MakeImageBlockDefaultQuality`(*self*, *image*, *imageType*)[¶](#wx.richtext.RichTextImageBlock.MakeImageBlockDefaultQuality "Permalink to this definition")
Uses a  [wx.Image](wx.Image.html#wx-image) for efficiency, but can’t set quality (only relevant for `JPEG`)



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Ok(self) -> bool:
        """ 

`Ok`(*self*)[¶](#wx.richtext.RichTextImageBlock.Ok "Permalink to this definition")

Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    @staticmethod
    def ReadBlock(*args, **kw) -> int:
        """ 

*static* `ReadBlock`(*\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextImageBlock.ReadBlock "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ReadBlock** *(stream, size)*


Implementation.


Allocates and reads from a stream as a block of memory.



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **size** (*int*) –



Return type
*int*






---

  



**ReadBlock** *(filename, size)*


Allocates and reads from a file as a block of memory.



Parameters
* **filename** (*string*) –
* **size** (*int*) –



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def ReadHex(self, stream, length, imageType) -> bool:
        """ 

`ReadHex`(*self*, *stream*, *length*, *imageType*)[¶](#wx.richtext.RichTextImageBlock.ReadHex "Permalink to this definition")
Reads the data in hex from a stream.



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **length** (*int*) –
* **imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetData(self, image: int) -> None:
        """ 

`SetData`(*self*, *image*)[¶](#wx.richtext.RichTextImageBlock.SetData "Permalink to this definition")

Parameters
**image** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetDataSize(self, size: int) -> None:
        """ 

`SetDataSize`(*self*, *size*)[¶](#wx.richtext.RichTextImageBlock.SetDataSize "Permalink to this definition")
Sets the data size.



Parameters
**size** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def SetImageType(self, imageType: BitmapType) -> None:
        """ 

`SetImageType`(*self*, *imageType*)[¶](#wx.richtext.RichTextImageBlock.SetImageType "Permalink to this definition")
Sets the image type.



Parameters
**imageType** ([*BitmapType*](wx.BitmapType.enumeration.html "BitmapType")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def Write(self, filename: str) -> bool:
        """ 

`Write`(*self*, *filename*)[¶](#wx.richtext.RichTextImageBlock.Write "Permalink to this definition")
Writes the block to a file.



Parameters
**filename** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    @staticmethod
    def WriteBlock(*args, **kw) -> bool:
        """ 

*static* `WriteBlock`(*\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextImageBlock.WriteBlock "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**WriteBlock** *(stream, block, size)*


Writes a memory block to stream.



Parameters
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –
* **block** (*int*) –
* **size** (*int*) –



Return type
*bool*






---

  



**WriteBlock** *(filename, block, size)*


Writes a memory block to a file.



Parameters
* **filename** (*string*) –
* **block** (*int*) –
* **size** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    def WriteHex(self, stream: 'OutputStream') -> bool:
        """ 

`WriteHex`(*self*, *stream*)[¶](#wx.richtext.RichTextImageBlock.WriteHex "Permalink to this definition")
Writes the data in hex to a stream.



Parameters
**stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImageBlock.html
        """

    Data: int  # `Data`[¶](#wx.richtext.RichTextImageBlock.Data "Permalink to this definition")See [`GetData`](#wx.richtext.RichTextImageBlock.GetData "wx.richtext.RichTextImageBlock.GetData") and [`SetData`](#wx.richtext.RichTextImageBlock.SetData "wx.richtext.RichTextImageBlock.SetData")
    DataSize: int  # `DataSize`[¶](#wx.richtext.RichTextImageBlock.DataSize "Permalink to this definition")See [`GetDataSize`](#wx.richtext.RichTextImageBlock.GetDataSize "wx.richtext.RichTextImageBlock.GetDataSize") and [`SetDataSize`](#wx.richtext.RichTextImageBlock.SetDataSize "wx.richtext.RichTextImageBlock.SetDataSize")
    Extension: str  # `Extension`[¶](#wx.richtext.RichTextImageBlock.Extension "Permalink to this definition")See [`GetExtension`](#wx.richtext.RichTextImageBlock.GetExtension "wx.richtext.RichTextImageBlock.GetExtension")
    ImageType: 'BitmapType'  # `ImageType`[¶](#wx.richtext.RichTextImageBlock.ImageType "Permalink to this definition")See [`GetImageType`](#wx.richtext.RichTextImageBlock.GetImageType "wx.richtext.RichTextImageBlock.GetImageType") and [`SetImageType`](#wx.richtext.RichTextImageBlock.SetImageType "wx.richtext.RichTextImageBlock.SetImageType")



class RichTextObject(Object):
    """ **Possible constructors**:



```
RichTextObject(parent=None)

```


This is the base for drawable rich text objects.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
    """
    def __init__(self, parent: Optional['richtext.RichTextObject']=None) -> None:
        """ 

`__init__`(*self*, *parent=None*)[¶](#wx.richtext.RichTextObject.__init__ "Permalink to this definition")
Constructor, taking an optional parent pointer.



Parameters
**parent** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def AcceptsFocus(self) -> bool:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.richtext.RichTextObject.AcceptsFocus "Permalink to this definition")
Returns `True` if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.


For example, containers supporting text, such as a text box object, can accept the focus, but a table can’t (set the focus to individual cells instead).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def AdjustAttributes(self, attr, context) -> bool:
        """ 

`AdjustAttributes`(*self*, *attr*, *context*)[¶](#wx.richtext.RichTextObject.AdjustAttributes "Permalink to this definition")
Adjusts the attributes for virtual attribute provision, collapsed borders, etc.



Parameters
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def AdjustAvailableSpace(dc, buffer, parentAttr, childAttr, availableParentSpace, availableContainerSpace) -> 'Rect':
        """ 

*static* `AdjustAvailableSpace`(*dc*, *buffer*, *parentAttr*, *childAttr*, *availableParentSpace*, *availableContainerSpace*)[¶](#wx.richtext.RichTextObject.AdjustAvailableSpace "Permalink to this definition")
Returns the rectangle which the child has available to it given restrictions specified in the child attribute, e.g.


50% width of the parent, 400 pixels, x position 20% of the parent, etc. availableContainerSpace might be a parent that the cell has to compute its width relative to. E.g. a cell that’s 50% of its parent.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **parentAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **childAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **availableParentSpace** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **availableContainerSpace** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
[`Rect`](#wx.richtext.RichTextObject.Rect "wx.richtext.RichTextObject.Rect")






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextObject.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextObject.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanMerge(self, object, context) -> bool:
        """ 

`CanMerge`(*self*, *object*, *context*)[¶](#wx.richtext.RichTextObject.CanMerge "Permalink to this definition")
Returns `True` if this object can merge itself with the given one.



Parameters
* **object** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def CanSplit(self, context: 'richtext.RichTextDrawingContext') -> bool:
        """ 

`CanSplit`(*self*, *context*)[¶](#wx.richtext.RichTextObject.CanSplit "Permalink to this definition")
Returns `True` if this object can potentially be split, by virtue of having different virtual attributes for individual sub-objects.



Parameters
**context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextObject.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ConvertPixelsToTenthsMM(self, *args, **kw) -> int:
        """ 

`ConvertPixelsToTenthsMM`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextObject.ConvertPixelsToTenthsMM "Permalink to this definition")
Convert units in pixels to tenths of a millimetre.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ConvertPixelsToTenthsMM** *(self, dc, pixels)*



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **pixels** (*int*) –



Return type
*int*






---

  



**ConvertPixelsToTenthsMM** *(ppi, pixels, scale=1.0)*



Parameters
* **ppi** (*int*) –
* **pixels** (*int*) –
* **scale** (*float*) –



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ConvertTenthsMMToPixels(self, *args, **kw) -> int:
        """ 

`ConvertTenthsMMToPixels`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextObject.ConvertTenthsMMToPixels "Permalink to this definition")
Converts units in tenths of a millimetre to device units.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**ConvertTenthsMMToPixels** *(self, dc, units)*



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **units** (*int*) –



Return type
*int*






---

  



**ConvertTenthsMMToPixels** *(ppi, units, scale=1.0)*



Parameters
* **ppi** (*int*) –
* **units** (*int*) –
* **scale** (*float*) –



Return type
*int*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Copy(self, obj: 'richtext.RichTextObject') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextObject.Copy "Permalink to this definition")
Copies the object.



Parameters
**obj** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`DeleteRange`(*self*, *range*)[¶](#wx.richtext.RichTextObject.DeleteRange "Permalink to this definition")
Deletes the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Dereference(self) -> None:
        """ 

`Dereference`(*self*)[¶](#wx.richtext.RichTextObject.Dereference "Permalink to this definition")
Reference-counting allows us to use the same object in multiple lists (not yet used).




            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def DoSplit(self, pos: int) -> 'RichTextObject':
        """ 

`DoSplit`(*self*, *pos*)[¶](#wx.richtext.RichTextObject.DoSplit "Permalink to this definition")
Do a split from *pos*, returning an object containing the second part, and setting the first part in ‘this’.



Parameters
**pos** (*long*) – 



Return type
 [wx.richtext.RichTextObject](#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextObject.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def DrawBorder(dc, buffer, attr, borders, rect, flags=0) -> bool:
        """ 

*static* `DrawBorder`(*dc*, *buffer*, *attr*, *borders*, *rect*, *flags=0*)[¶](#wx.richtext.RichTextObject.DrawBorder "Permalink to this definition")
Draws a border.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **borders** ([*wx.richtext.TextAttrBorders*](wx.richtext.TextAttrBorders.html#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def DrawBoxAttributes(dc, buffer, attr, boxRect, flags=0, obj=None) -> bool:
        """ 

*static* `DrawBoxAttributes`(*dc*, *buffer*, *attr*, *boxRect*, *flags=0*, *obj=None*)[¶](#wx.richtext.RichTextObject.DrawBoxAttributes "Permalink to this definition")
Draws the borders and background for the given rectangle and attributes.


*boxRect* is taken to be the outer margin box, not the box around the content.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **boxRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **flags** (*int*) –
* **obj** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextObject.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ 

`FindPosition`(*self*, *dc*, *context*, *index*, *forceLineStart*)[¶](#wx.richtext.RichTextObject.FindPosition "Permalink to this definition")
Finds the absolute position and row height for the given character position.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **index** (*long*) –
* **forceLineStart** (*bool*) –



Return type
*tuple*



Returns
( *bool*, *pt*, *height* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAbsolutePosition(self) -> 'Point':
        """ 

`GetAbsolutePosition`(*self*)[¶](#wx.richtext.RichTextObject.GetAbsolutePosition "Permalink to this definition")
Returns the absolute object position, by traversing up the child/parent hierarchy.


`TODO`: may not be needed, if all object positions are in fact relative to the top of the coordinate space.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAttributes(self) -> 'RichTextAttr':
        """ 

`GetAttributes`(*self*)[¶](#wx.richtext.RichTextObject.GetAttributes "Permalink to this definition")
Returns the object’s attributes.



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetAvailableContentArea(self, dc, context, outerRect) -> 'Rect':
        """ 

`GetAvailableContentArea`(*self*, *dc*, *context*, *outerRect*)[¶](#wx.richtext.RichTextObject.GetAvailableContentArea "Permalink to this definition")
Calculates the available content space in the given rectangle, given the margins, border and padding specified in the object’s attributes.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **outerRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
[`Rect`](#wx.richtext.RichTextObject.Rect "wx.richtext.RichTextObject.Rect")






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBestSize(self) -> 'Size':
        """ 

`GetBestSize`(*self*)[¶](#wx.richtext.RichTextObject.GetBestSize "Permalink to this definition")
Returns the best size, i.e. the ideal starting size for this object irrespective of available space.


For a short text string, it will be the size that exactly encloses the text. For a longer string, it might use the parent width for example.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBottomMargin(self) -> int:
        """ 

`GetBottomMargin`(*self*)[¶](#wx.richtext.RichTextObject.GetBottomMargin "Permalink to this definition")
Returns the bottom margin of the object, in pixels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def GetBoxRects(dc, buffer, attr) -> tuple:
        """ 

*static* `GetBoxRects`(*dc*, *buffer*, *attr*)[¶](#wx.richtext.RichTextObject.GetBoxRects "Permalink to this definition")
Returns the various rectangles of the box model in pixels.


You can either specify *contentRect* (inner) or *marginRect* (outer), and the other must be the default rectangle (no width or height). Note that the outline doesn’t affect the position of the rectangle, it’s drawn in whatever space is available.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*tuple*



Returns
( *bool*, *marginRect*, *borderRect*, *contentRect*, *paddingRect*, *outlineRect* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetBuffer(self) -> 'RichTextBuffer':
        """ 

`GetBuffer`(*self*)[¶](#wx.richtext.RichTextObject.GetBuffer "Permalink to this definition")
Returns the containing buffer.



Return type
 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetCachedSize(self) -> 'Size':
        """ 

`GetCachedSize`(*self*)[¶](#wx.richtext.RichTextObject.GetCachedSize "Permalink to this definition")
Gets the cached object size as calculated by Layout.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetContainer`(*self*)[¶](#wx.richtext.RichTextObject.GetContainer "Permalink to this definition")
Returns the top-level container of this object.


May return itself if it’s a container; use GetParentContainer to return a different container.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetDescent(self) -> int:
        """ 

`GetDescent`(*self*)[¶](#wx.richtext.RichTextObject.GetDescent "Permalink to this definition")
Returns the stored descent value.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetFloatDirection(self) -> int:
        """ 

`GetFloatDirection`(*self*)[¶](#wx.richtext.RichTextObject.GetFloatDirection "Permalink to this definition")
Returns the floating direction.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetLeftMargin(self) -> int:
        """ 

`GetLeftMargin`(*self*)[¶](#wx.richtext.RichTextObject.GetLeftMargin "Permalink to this definition")
Returns the left margin of the object, in pixels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetMaxSize(self) -> 'Size':
        """ 

`GetMaxSize`(*self*)[¶](#wx.richtext.RichTextObject.GetMaxSize "Permalink to this definition")
Gets the maximum object size as calculated by Layout.


This allows us to fit an object to its contents or allocate extra space if required.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetMinSize(self) -> 'Size':
        """ 

`GetMinSize`(*self*)[¶](#wx.richtext.RichTextObject.GetMinSize "Permalink to this definition")
Gets the minimum object size as calculated by Layout.


This allows us to constrain an object to its absolute minimum size if necessary.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextObject.GetName "Permalink to this definition")
Returns the identifying name for this object from the properties, using the “name” key.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetNaturalSize(self) -> 'TextAttrSize':
        """ 

`GetNaturalSize`(*self*)[¶](#wx.richtext.RichTextObject.GetNaturalSize "Permalink to this definition")
Gets the ‘natural’ size for an object.


For an image, it would be the image size.



Return type
 [wx.richtext.TextAttrSize](wx.richtext.TextAttrSize.html#wx-richtext-textattrsize)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetOwnRange(self) -> 'RichTextRange':
        """ 

`GetOwnRange`(*self*)[¶](#wx.richtext.RichTextObject.GetOwnRange "Permalink to this definition")
Returns the object’s own range (valid if top-level).



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetOwnRangeIfTopLevel(self) -> 'RichTextRange':
        """ 

`GetOwnRangeIfTopLevel`(*self*)[¶](#wx.richtext.RichTextObject.GetOwnRangeIfTopLevel "Permalink to this definition")
Returns the object’s own range only if a top-level object.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetParent(self) -> 'RichTextObject':
        """ 

`GetParent`(*self*)[¶](#wx.richtext.RichTextObject.GetParent "Permalink to this definition")
Returns a pointer to the parent object.



Return type
 [wx.richtext.RichTextObject](#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetParentContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetParentContainer`(*self*)[¶](#wx.richtext.RichTextObject.GetParentContainer "Permalink to this definition")
Returns the top-level container of this object.


Returns a different container than itself, unless there’s no parent, in which case it will return `None`.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetPosition(self) -> 'Point':
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.RichTextObject.GetPosition "Permalink to this definition")
Returns the object position in pixels.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ 

`GetProperties`(*self*)[¶](#wx.richtext.RichTextObject.GetProperties "Permalink to this definition")
Returns the object’s properties.



Return type
 [wx.richtext.RichTextProperties](wx.richtext.RichTextProperties.html#wx-richtext-richtextproperties)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextObject.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ 

`GetRange`(*self*)[¶](#wx.richtext.RichTextObject.GetRange "Permalink to this definition")
Returns the object’s range.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextObject.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRect(self) -> 'Rect':
        """ 

`GetRect`(*self*)[¶](#wx.richtext.RichTextObject.GetRect "Permalink to this definition")
Returns the rectangle enclosing the object.



Return type
[`Rect`](#wx.richtext.RichTextObject.Rect "wx.richtext.RichTextObject.Rect")






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetRightMargin(self) -> int:
        """ 

`GetRightMargin`(*self*)[¶](#wx.richtext.RichTextObject.GetRightMargin "Permalink to this definition")
Returns the right margin of the object, in pixels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetSelection(self, start, end) -> 'RichTextSelection':
        """ 

`GetSelection`(*self*, *start*, *end*)[¶](#wx.richtext.RichTextObject.GetSelection "Permalink to this definition")
Returns a selection object specifying the selections between start and end character positions.


For example, a table would deduce what cells (of range length 1) are selected when dragging across the table.



Parameters
* **start** (*long*) –
* **end** (*long*) –



Return type
 [wx.richtext.RichTextSelection](wx.richtext.RichTextSelection.html#wx-richtext-richtextselection)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ 

`GetTextForRange`(*self*, *range*)[¶](#wx.richtext.RichTextObject.GetTextForRange "Permalink to this definition")
Returns any text in this object for the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetTopMargin(self) -> int:
        """ 

`GetTopMargin`(*self*)[¶](#wx.richtext.RichTextObject.GetTopMargin "Permalink to this definition")
Returns the top margin of the object, in pixels.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    @staticmethod
    def GetTotalMargin(dc, buffer, attr) -> tuple:
        """ 

*static* `GetTotalMargin`(*dc*, *buffer*, *attr*)[¶](#wx.richtext.RichTextObject.GetTotalMargin "Permalink to this definition")
Returns the total margin for the object in pixels, taking into account margin, padding and border size.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*tuple*



Returns
( *bool*, *leftMargin*, *rightMargin*, *topMargin*, *bottomMargin* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextObject.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def HandlesChildSelections(self) -> bool:
        """ 

`HandlesChildSelections`(*self*)[¶](#wx.richtext.RichTextObject.HandlesChildSelections "Permalink to this definition")
Returns `True` if this object can handle the selections of its children, fOr example a table.


Required for composite selection handling to work.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextObject.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ 

`ImportFromXML`(*self*, *buffer*, *node*, *handler*, *recurse*)[¶](#wx.richtext.RichTextObject.ImportFromXML "Permalink to this definition")
Imports this object from `XML`.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **handler** ([*wx.richtext.RichTextXMLHandler*](wx.richtext.RichTextXMLHandler.html#wx.richtext.RichTextXMLHandler "wx.richtext.RichTextXMLHandler")) –
* **recurse** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ 

`Invalidate`(*self*, *invalidRange=RICHTEXT\_ALL*)[¶](#wx.richtext.RichTextObject.Invalidate "Permalink to this definition")
Invalidates the object at the given range.


With no argument, invalidates the whole object.



Parameters
**invalidRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsAtomic(self) -> bool:
        """ 

`IsAtomic`(*self*)[¶](#wx.richtext.RichTextObject.IsAtomic "Permalink to this definition")
Returns `True` if no user editing can be done inside the object.


This returns `True` for simple objects, `False` for most composite objects, but `True` for fields, which if composite, should not be user-edited.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsComposite(self) -> bool:
        """ 

`IsComposite`(*self*)[¶](#wx.richtext.RichTextObject.IsComposite "Permalink to this definition")
Returns `True` if this object is composite.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextObject.IsEmpty "Permalink to this definition")
Returns `True` if the object is empty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsFloatable(self) -> bool:
        """ 

`IsFloatable`(*self*)[¶](#wx.richtext.RichTextObject.IsFloatable "Permalink to this definition")
Returns `True` if this class of object is floatable.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsFloating(self) -> bool:
        """ 

`IsFloating`(*self*)[¶](#wx.richtext.RichTextObject.IsFloating "Permalink to this definition")
Returns `True` if this object is currently floating.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsShown(self) -> bool:
        """ 

`IsShown`(*self*)[¶](#wx.richtext.RichTextObject.IsShown "Permalink to this definition")
Returns `True` if the object will be shown, `False` otherwise.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def IsTopLevel(self) -> bool:
        """ 

`IsTopLevel`(*self*)[¶](#wx.richtext.RichTextObject.IsTopLevel "Permalink to this definition")
Returns `True` if this object is top-level, i.e. contains its own paragraphs, such as a text box.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextObject.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def LayoutToBestSize(self, dc, context, buffer, parentAttr, attr, availableParentSpace, availableContainerSpace, style) -> bool:
        """ 

`LayoutToBestSize`(*self*, *dc*, *context*, *buffer*, *parentAttr*, *attr*, *availableParentSpace*, *availableContainerSpace*, *style*)[¶](#wx.richtext.RichTextObject.LayoutToBestSize "Permalink to this definition")
Lays out the object first with a given amount of space, and then if no width was specified in attr, lays out the object again using the minimum size.


*availableParentSpace* is the maximum space for the object, whereas *availableContainerSpace* is the container with which relative positions and sizes should be computed. For example, a text box whose space has already been constrained in a previous layout pass to *availableParentSpace*, but should have a width of 50% of *availableContainerSpace*. (If these two rects were the same, a 2nd pass could see the object getting too small.)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **parentAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **availableParentSpace** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **availableContainerSpace** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Merge(self, object, context) -> bool:
        """ 

`Merge`(*self*, *object*, *context*)[¶](#wx.richtext.RichTextObject.Merge "Permalink to this definition")
Returns `True` if this object merged itself with the given one.


The calling code will then delete the given object.



Parameters
* **object** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Move(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`Move`(*self*, *pt*)[¶](#wx.richtext.RichTextObject.Move "Permalink to this definition")
Moves the object recursively, by adding the offset from old to new.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Reference(self) -> None:
        """ 

`Reference`(*self*)[¶](#wx.richtext.RichTextObject.Reference "Permalink to this definition")
Reference-counting allows us to use the same object in multiple lists (not yet used).




            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetAttributes(self, attr: 'richtext.RichTextAttr') -> None:
        """ 

`SetAttributes`(*self*, *attr*)[¶](#wx.richtext.RichTextObject.SetAttributes "Permalink to this definition")
Sets the object’s attributes.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetCachedSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetCachedSize`(*self*, *sz*)[¶](#wx.richtext.RichTextObject.SetCachedSize "Permalink to this definition")
Sets the cached object size as calculated by Layout.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetDescent(self, descent: int) -> None:
        """ 

`SetDescent`(*self*, *descent*)[¶](#wx.richtext.RichTextObject.SetDescent "Permalink to this definition")
Sets the stored descent value.



Parameters
**descent** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMargins(self, *args, **kw) -> None:
        """ 

`SetMargins`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextObject.SetMargins "Permalink to this definition")
Set the margin around the object, in pixels.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetMargins** *(self, margin)*



Parameters
**margin** (*int*) – 






---

  



**SetMargins** *(self, leftMargin, rightMargin, topMargin, bottomMargin)*



Parameters
* **leftMargin** (*int*) –
* **rightMargin** (*int*) –
* **topMargin** (*int*) –
* **bottomMargin** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMaxSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetMaxSize`(*self*, *sz*)[¶](#wx.richtext.RichTextObject.SetMaxSize "Permalink to this definition")
Sets the maximum object size as calculated by Layout.


This allows us to fit an object to its contents or allocate extra space if required.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetMinSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetMinSize`(*self*, *sz*)[¶](#wx.richtext.RichTextObject.SetMinSize "Permalink to this definition")
Sets the minimum object size as calculated by Layout.


This allows us to constrain an object to its absolute minimum size if necessary.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextObject.SetName "Permalink to this definition")
Sets the identifying name for this object as a property using the “name” key.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetOwnRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetOwnRange`(*self*, *range*)[¶](#wx.richtext.RichTextObject.SetOwnRange "Permalink to this definition")
Set the object’s own range, for a top-level object with its own position space.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetParent(self, parent: 'richtext.RichTextObject') -> None:
        """ 

`SetParent`(*self*, *parent*)[¶](#wx.richtext.RichTextObject.SetParent "Permalink to this definition")
Sets the pointer to the parent object.



Parameters
**parent** ([*wx.richtext.RichTextObject*](#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextObject.SetPosition "Permalink to this definition")
Sets the object position in pixels.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ 

`SetProperties`(*self*, *props*)[¶](#wx.richtext.RichTextObject.SetProperties "Permalink to this definition")
Sets the object’s properties.



Parameters
**props** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetRange`(*self*, *range*)[¶](#wx.richtext.RichTextObject.SetRange "Permalink to this definition")
Sets the object’s range within its container.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Show(self, show: bool) -> None:
        """ 

`Show`(*self*, *show*)[¶](#wx.richtext.RichTextObject.Show "Permalink to this definition")
Call to show or hide this object.


This function does not cause the content to be laid out or redrawn.



Parameters
**show** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def Split(self, context: 'richtext.RichTextDrawingContext') -> 'RichTextObject':
        """ 

`Split`(*self*, *context*)[¶](#wx.richtext.RichTextObject.Split "Permalink to this definition")
Returns the final object in the split objects if this object was split due to differences between sub-object virtual attributes.


Returns itself if it was not split.



Parameters
**context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) – 



Return type
 [wx.richtext.RichTextObject](#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ 

`UsesParagraphAttributes`(*self*)[¶](#wx.richtext.RichTextObject.UsesParagraphAttributes "Permalink to this definition")
Returns `True` if this object takes note of paragraph attributes (text and image objects don’t).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObject.html
        """

    AbsolutePosition: 'Point'  # `AbsolutePosition`[¶](#wx.richtext.RichTextObject.AbsolutePosition "Permalink to this definition")See [`GetAbsolutePosition`](#wx.richtext.RichTextObject.GetAbsolutePosition "wx.richtext.RichTextObject.GetAbsolutePosition")
    Attributes: 'RichTextAttr'  # `Attributes`[¶](#wx.richtext.RichTextObject.Attributes "Permalink to this definition")See [`GetAttributes`](#wx.richtext.RichTextObject.GetAttributes "wx.richtext.RichTextObject.GetAttributes") and [`SetAttributes`](#wx.richtext.RichTextObject.SetAttributes "wx.richtext.RichTextObject.SetAttributes")
    BestSize: 'Size'  # `BestSize`[¶](#wx.richtext.RichTextObject.BestSize "Permalink to this definition")See [`GetBestSize`](#wx.richtext.RichTextObject.GetBestSize "wx.richtext.RichTextObject.GetBestSize")
    BottomMargin: int  # `BottomMargin`[¶](#wx.richtext.RichTextObject.BottomMargin "Permalink to this definition")See [`GetBottomMargin`](#wx.richtext.RichTextObject.GetBottomMargin "wx.richtext.RichTextObject.GetBottomMargin")
    Buffer: 'RichTextBuffer'  # `Buffer`[¶](#wx.richtext.RichTextObject.Buffer "Permalink to this definition")See [`GetBuffer`](#wx.richtext.RichTextObject.GetBuffer "wx.richtext.RichTextObject.GetBuffer")
    CachedSize: 'Size'  # `CachedSize`[¶](#wx.richtext.RichTextObject.CachedSize "Permalink to this definition")See [`GetCachedSize`](#wx.richtext.RichTextObject.GetCachedSize "wx.richtext.RichTextObject.GetCachedSize") and [`SetCachedSize`](#wx.richtext.RichTextObject.SetCachedSize "wx.richtext.RichTextObject.SetCachedSize")
    Container: 'RichTextParagraphLayoutBox'  # `Container`[¶](#wx.richtext.RichTextObject.Container "Permalink to this definition")See [`GetContainer`](#wx.richtext.RichTextObject.GetContainer "wx.richtext.RichTextObject.GetContainer")
    Descent: int  # `Descent`[¶](#wx.richtext.RichTextObject.Descent "Permalink to this definition")See [`GetDescent`](#wx.richtext.RichTextObject.GetDescent "wx.richtext.RichTextObject.GetDescent") and [`SetDescent`](#wx.richtext.RichTextObject.SetDescent "wx.richtext.RichTextObject.SetDescent")
    FloatDirection: int  # `FloatDirection`[¶](#wx.richtext.RichTextObject.FloatDirection "Permalink to this definition")See [`GetFloatDirection`](#wx.richtext.RichTextObject.GetFloatDirection "wx.richtext.RichTextObject.GetFloatDirection")
    LeftMargin: int  # `LeftMargin`[¶](#wx.richtext.RichTextObject.LeftMargin "Permalink to this definition")See [`GetLeftMargin`](#wx.richtext.RichTextObject.GetLeftMargin "wx.richtext.RichTextObject.GetLeftMargin")
    MaxSize: 'Size'  # `MaxSize`[¶](#wx.richtext.RichTextObject.MaxSize "Permalink to this definition")See [`GetMaxSize`](#wx.richtext.RichTextObject.GetMaxSize "wx.richtext.RichTextObject.GetMaxSize") and [`SetMaxSize`](#wx.richtext.RichTextObject.SetMaxSize "wx.richtext.RichTextObject.SetMaxSize")
    MinSize: 'Size'  # `MinSize`[¶](#wx.richtext.RichTextObject.MinSize "Permalink to this definition")See [`GetMinSize`](#wx.richtext.RichTextObject.GetMinSize "wx.richtext.RichTextObject.GetMinSize") and [`SetMinSize`](#wx.richtext.RichTextObject.SetMinSize "wx.richtext.RichTextObject.SetMinSize")
    Name: str  # `Name`[¶](#wx.richtext.RichTextObject.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextObject.GetName "wx.richtext.RichTextObject.GetName") and [`SetName`](#wx.richtext.RichTextObject.SetName "wx.richtext.RichTextObject.SetName")
    NaturalSize: 'TextAttrSize'  # `NaturalSize`[¶](#wx.richtext.RichTextObject.NaturalSize "Permalink to this definition")See [`GetNaturalSize`](#wx.richtext.RichTextObject.GetNaturalSize "wx.richtext.RichTextObject.GetNaturalSize")
    OwnRange: 'RichTextRange'  # `OwnRange`[¶](#wx.richtext.RichTextObject.OwnRange "Permalink to this definition")See [`GetOwnRange`](#wx.richtext.RichTextObject.GetOwnRange "wx.richtext.RichTextObject.GetOwnRange") and [`SetOwnRange`](#wx.richtext.RichTextObject.SetOwnRange "wx.richtext.RichTextObject.SetOwnRange")
    OwnRangeIfTopLevel: 'RichTextRange'  # `OwnRangeIfTopLevel`[¶](#wx.richtext.RichTextObject.OwnRangeIfTopLevel "Permalink to this definition")See [`GetOwnRangeIfTopLevel`](#wx.richtext.RichTextObject.GetOwnRangeIfTopLevel "wx.richtext.RichTextObject.GetOwnRangeIfTopLevel")
    Parent: 'RichTextObject'  # `Parent`[¶](#wx.richtext.RichTextObject.Parent "Permalink to this definition")See [`GetParent`](#wx.richtext.RichTextObject.GetParent "wx.richtext.RichTextObject.GetParent") and [`SetParent`](#wx.richtext.RichTextObject.SetParent "wx.richtext.RichTextObject.SetParent")
    ParentContainer: 'RichTextParagraphLayoutBox'  # `ParentContainer`[¶](#wx.richtext.RichTextObject.ParentContainer "Permalink to this definition")See [`GetParentContainer`](#wx.richtext.RichTextObject.GetParentContainer "wx.richtext.RichTextObject.GetParentContainer")
    Position: 'Point'  # `Position`[¶](#wx.richtext.RichTextObject.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.RichTextObject.GetPosition "wx.richtext.RichTextObject.GetPosition") and [`SetPosition`](#wx.richtext.RichTextObject.SetPosition "wx.richtext.RichTextObject.SetPosition")
    Properties: 'RichTextProperties'  # `Properties`[¶](#wx.richtext.RichTextObject.Properties "Permalink to this definition")See [`GetProperties`](#wx.richtext.RichTextObject.GetProperties "wx.richtext.RichTextObject.GetProperties") and [`SetProperties`](#wx.richtext.RichTextObject.SetProperties "wx.richtext.RichTextObject.SetProperties")
    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextObject.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextObject.GetPropertiesMenuLabel "wx.richtext.RichTextObject.GetPropertiesMenuLabel")
    Range: 'RichTextRange'  # `Range`[¶](#wx.richtext.RichTextObject.Range "Permalink to this definition")See [`GetRange`](#wx.richtext.RichTextObject.GetRange "wx.richtext.RichTextObject.GetRange") and [`SetRange`](#wx.richtext.RichTextObject.SetRange "wx.richtext.RichTextObject.SetRange")
    Rect: '_Rect'  # `Rect`[¶](#wx.richtext.RichTextObject.Rect "Permalink to this definition")See [`GetRect`](#wx.richtext.RichTextObject.GetRect "wx.richtext.RichTextObject.GetRect")
    RightMargin: int  # `RightMargin`[¶](#wx.richtext.RichTextObject.RightMargin "Permalink to this definition")See [`GetRightMargin`](#wx.richtext.RichTextObject.GetRightMargin "wx.richtext.RichTextObject.GetRightMargin")
    TopMargin: int  # `TopMargin`[¶](#wx.richtext.RichTextObject.TopMargin "Permalink to this definition")See [`GetTopMargin`](#wx.richtext.RichTextObject.GetTopMargin "wx.richtext.RichTextObject.GetTopMargin")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextObject.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextObject.GetXMLNodeName "wx.richtext.RichTextObject.GetXMLNodeName")



class RichTextPrinting(Object):
    """ **Possible constructors**:



```
RichTextPrinting(name="Printing", parentWindow=None)

```


This class provides a simple interface for performing RichTextBuffer
printing and previewing.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
    """
    def __init__(self, name="Printing", parentWindow=None) -> None:
        """ 

`__init__`(*self*, *name="Printing"*, *parentWindow=None*)[¶](#wx.richtext.RichTextPrinting.__init__ "Permalink to this definition")
Constructor.


Optionally pass a title to be used in the preview frame and printing wait dialog, and also a parent window for these windows.



Parameters
* **name** (*string*) –
* **parentWindow** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetFooterText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ 

`GetFooterText`(*self*, *page=RICHTEXT\_PAGE\_EVEN*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextPrinting.GetFooterText "Permalink to this definition")
A convenience function to get the footer text.


See  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) for details.



Parameters
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetHeaderFooterData(self) -> 'RichTextHeaderFooterData':
        """ 

`GetHeaderFooterData`(*self*)[¶](#wx.richtext.RichTextPrinting.GetHeaderFooterData "Permalink to this definition")
Returns the internal  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) object.



Return type
 [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetHeaderText(self, page=RICHTEXT_PAGE_EVEN, location=RICHTEXT_PAGE_CENTRE) -> str:
        """ 

`GetHeaderText`(*self*, *page=RICHTEXT\_PAGE\_EVEN*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextPrinting.GetHeaderText "Permalink to this definition")
A convenience function to get the header text.


See  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) for details.



Parameters
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPageSetupData(self) -> 'PageSetupDialogData':
        """ 

`GetPageSetupData`(*self*)[¶](#wx.richtext.RichTextPrinting.GetPageSetupData "Permalink to this definition")
Returns a pointer to the internal page setup data.



Return type
*PageSetupDialogData*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetParentWindow(self) -> 'Window':
        """ 

`GetParentWindow`(*self*)[¶](#wx.richtext.RichTextPrinting.GetParentWindow "Permalink to this definition")
Returns the parent window to be used for the preview window and printing wait dialog.



Return type
*Window*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPreviewRect(self) -> 'Rect':
        """ 

`GetPreviewRect`(*self*)[¶](#wx.richtext.RichTextPrinting.GetPreviewRect "Permalink to this definition")
Returns the dimensions to be used for the preview window.



Return type
*Rect*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetPrintData(self) -> 'PrintData':
        """ 

`GetPrintData`(*self*)[¶](#wx.richtext.RichTextPrinting.GetPrintData "Permalink to this definition")
Returns a pointer to the internal print data.



Return type
[`PrintData`](#wx.richtext.RichTextPrinting.PrintData "wx.richtext.RichTextPrinting.PrintData")






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def GetTitle(self) -> str:
        """ 

`GetTitle`(*self*)[¶](#wx.richtext.RichTextPrinting.GetTitle "Permalink to this definition")
Returns the title of the preview window or printing wait caption.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PageSetup(self) -> None:
        """ 

`PageSetup`(*self*)[¶](#wx.richtext.RichTextPrinting.PageSetup "Permalink to this definition")
Shows the page setup dialog.




            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PreviewBuffer(self, buffer: 'richtext.RichTextBuffer') -> bool:
        """ 

`PreviewBuffer`(*self*, *buffer*)[¶](#wx.richtext.RichTextPrinting.PreviewBuffer "Permalink to this definition")
Shows a preview window for the given buffer.


The function takes its own copy of *buffer*.



Parameters
**buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PreviewFile(self, richTextFile: str) -> bool:
        """ 

`PreviewFile`(*self*, *richTextFile*)[¶](#wx.richtext.RichTextPrinting.PreviewFile "Permalink to this definition")
Shows a preview window for the given file.


*richTextFile* can be a text file or `XML` file, or other file depending on the available file handlers.



Parameters
**richTextFile** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PrintBuffer(self, buffer, showPrintDialog=True) -> bool:
        """ 

`PrintBuffer`(*self*, *buffer*, *showPrintDialog=True*)[¶](#wx.richtext.RichTextPrinting.PrintBuffer "Permalink to this definition")
Prints the given buffer.


The function takes its own copy of *buffer*. *showPrintDialog* can be `True` to show the print dialog, or `False` to print quietly.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **showPrintDialog** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def PrintFile(self, richTextFile, showPrintDialog=True) -> bool:
        """ 

`PrintFile`(*self*, *richTextFile*, *showPrintDialog=True*)[¶](#wx.richtext.RichTextPrinting.PrintFile "Permalink to this definition")
Prints the given file.


*richTextFile* can be a text file or `XML` file, or other file depending on the available file handlers. *showPrintDialog* can be `True` to show the print dialog, or `False` to print quietly.



Parameters
* **richTextFile** (*string*) –
* **showPrintDialog** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetFooterText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ 

`SetFooterText`(*self*, *text*, *page=RICHTEXT\_PAGE\_ALL*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextPrinting.SetFooterText "Permalink to this definition")
A convenience function to set the footer text.


See  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) for details.



Parameters
* **text** (*string*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterData(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ 

`SetHeaderFooterData`(*self*, *data*)[¶](#wx.richtext.RichTextPrinting.SetHeaderFooterData "Permalink to this definition")
Sets the internal  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) object.



Parameters
**data** ([*wx.richtext.RichTextHeaderFooterData*](wx.richtext.RichTextHeaderFooterData.html#wx.richtext.RichTextHeaderFooterData "wx.richtext.RichTextHeaderFooterData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterFont(self, font: 'Font') -> None:
        """ 

`SetHeaderFooterFont`(*self*, *font*)[¶](#wx.richtext.RichTextPrinting.SetHeaderFooterFont "Permalink to this definition")
Sets the  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderFooterTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetHeaderFooterTextColour`(*self*, *colour*)[¶](#wx.richtext.RichTextPrinting.SetHeaderFooterTextColour "Permalink to this definition")
Sets the  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) text colour.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetHeaderText(self, text, page=RICHTEXT_PAGE_ALL, location=RICHTEXT_PAGE_CENTRE) -> None:
        """ 

`SetHeaderText`(*self*, *text*, *page=RICHTEXT\_PAGE\_ALL*, *location=RICHTEXT\_PAGE\_CENTRE*)[¶](#wx.richtext.RichTextPrinting.SetHeaderText "Permalink to this definition")
A convenience function to set the header text.


See  [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata) for details.



Parameters
* **text** (*string*) –
* **page** ([*RichTextOddEvenPage*](wx.richtext.RichTextOddEvenPage.enumeration.html "RichTextOddEvenPage")) –
* **location** ([*RichTextPageLocation*](wx.richtext.RichTextPageLocation.enumeration.html "RichTextPageLocation")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPageSetupData(self, pageSetupData: 'PageSetupDialogData') -> None:
        """ 

`SetPageSetupData`(*self*, *pageSetupData*)[¶](#wx.richtext.RichTextPrinting.SetPageSetupData "Permalink to this definition")
Sets the page setup data.



Parameters
**pageSetupData** ([*wx.PageSetupDialogData*](wx.PageSetupDialogData.html#wx.PageSetupDialogData "wx.PageSetupDialogData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetParentWindow(self, parent: 'Window') -> None:
        """ 

`SetParentWindow`(*self*, *parent*)[¶](#wx.richtext.RichTextPrinting.SetParentWindow "Permalink to this definition")
Sets the parent window to be used for the preview window and printing wait dialog.



Parameters
**parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPreviewRect(self, rect: 'Rect') -> None:
        """ 

`SetPreviewRect`(*self*, *rect*)[¶](#wx.richtext.RichTextPrinting.SetPreviewRect "Permalink to this definition")
Sets the dimensions to be used for the preview window.



Parameters
**rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetPrintData(self, printData: 'PrintData') -> None:
        """ 

`SetPrintData`(*self*, *printData*)[¶](#wx.richtext.RichTextPrinting.SetPrintData "Permalink to this definition")
Sets the print data.



Parameters
**printData** ([*wx.PrintData*](wx.PrintData.html#wx.PrintData "wx.PrintData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetShowOnFirstPage(self, show: bool) -> None:
        """ 

`SetShowOnFirstPage`(*self*, *show*)[¶](#wx.richtext.RichTextPrinting.SetShowOnFirstPage "Permalink to this definition")
Pass `True` to show the header and footer on the first page.



Parameters
**show** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    def SetTitle(self, title: str) -> None:
        """ 

`SetTitle`(*self*, *title*)[¶](#wx.richtext.RichTextPrinting.SetTitle "Permalink to this definition")
Pass the title of the preview window or printing wait caption.



Parameters
**title** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrinting.html
        """

    FooterText: str  # `FooterText`[¶](#wx.richtext.RichTextPrinting.FooterText "Permalink to this definition")See [`GetFooterText`](#wx.richtext.RichTextPrinting.GetFooterText "wx.richtext.RichTextPrinting.GetFooterText") and [`SetFooterText`](#wx.richtext.RichTextPrinting.SetFooterText "wx.richtext.RichTextPrinting.SetFooterText")
    HeaderFooterData: 'RichTextHeaderFooterData'  # `HeaderFooterData`[¶](#wx.richtext.RichTextPrinting.HeaderFooterData "Permalink to this definition")See [`GetHeaderFooterData`](#wx.richtext.RichTextPrinting.GetHeaderFooterData "wx.richtext.RichTextPrinting.GetHeaderFooterData") and [`SetHeaderFooterData`](#wx.richtext.RichTextPrinting.SetHeaderFooterData "wx.richtext.RichTextPrinting.SetHeaderFooterData")
    HeaderText: str  # `HeaderText`[¶](#wx.richtext.RichTextPrinting.HeaderText "Permalink to this definition")See [`GetHeaderText`](#wx.richtext.RichTextPrinting.GetHeaderText "wx.richtext.RichTextPrinting.GetHeaderText") and [`SetHeaderText`](#wx.richtext.RichTextPrinting.SetHeaderText "wx.richtext.RichTextPrinting.SetHeaderText")
    PageSetupData: 'PageSetupDialogData'  # `PageSetupData`[¶](#wx.richtext.RichTextPrinting.PageSetupData "Permalink to this definition")See [`GetPageSetupData`](#wx.richtext.RichTextPrinting.GetPageSetupData "wx.richtext.RichTextPrinting.GetPageSetupData") and [`SetPageSetupData`](#wx.richtext.RichTextPrinting.SetPageSetupData "wx.richtext.RichTextPrinting.SetPageSetupData")
    ParentWindow: 'Window'  # `ParentWindow`[¶](#wx.richtext.RichTextPrinting.ParentWindow "Permalink to this definition")See [`GetParentWindow`](#wx.richtext.RichTextPrinting.GetParentWindow "wx.richtext.RichTextPrinting.GetParentWindow") and [`SetParentWindow`](#wx.richtext.RichTextPrinting.SetParentWindow "wx.richtext.RichTextPrinting.SetParentWindow")
    PreviewRect: 'Rect'  # `PreviewRect`[¶](#wx.richtext.RichTextPrinting.PreviewRect "Permalink to this definition")See [`GetPreviewRect`](#wx.richtext.RichTextPrinting.GetPreviewRect "wx.richtext.RichTextPrinting.GetPreviewRect") and [`SetPreviewRect`](#wx.richtext.RichTextPrinting.SetPreviewRect "wx.richtext.RichTextPrinting.SetPreviewRect")
    PrintData: '_PrintData'  # `PrintData`[¶](#wx.richtext.RichTextPrinting.PrintData "Permalink to this definition")See [`GetPrintData`](#wx.richtext.RichTextPrinting.GetPrintData "wx.richtext.RichTextPrinting.GetPrintData") and [`SetPrintData`](#wx.richtext.RichTextPrinting.SetPrintData "wx.richtext.RichTextPrinting.SetPrintData")
    Title: str  # `Title`[¶](#wx.richtext.RichTextPrinting.Title "Permalink to this definition")See [`GetTitle`](#wx.richtext.RichTextPrinting.GetTitle "wx.richtext.RichTextPrinting.GetTitle") and [`SetTitle`](#wx.richtext.RichTextPrinting.SetTitle "wx.richtext.RichTextPrinting.SetTitle")



class RichTextProperties(Object):
    """ **Possible constructors**:



```
RichTextProperties()

RichTextProperties(props)

```


A simple property class using Variants.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextProperties.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, props)*


Copy constructor.



Parameters
**props** ([*wx.richtext.RichTextProperties*](#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextProperties.Clear "Permalink to this definition")
Clears the properties.




            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Copy(self, props: 'richtext.RichTextProperties') -> None:
        """ 

`Copy`(*self*, *props*)[¶](#wx.richtext.RichTextProperties.Copy "Permalink to this definition")
Copies from *props*.



Parameters
**props** ([*wx.richtext.RichTextProperties*](#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Find(self, name: str) -> int:
        """ 

`Find`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.Find "Permalink to this definition")
Finds the given property.



Parameters
**name** (*string*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def FindOrCreateProperty(self, name: str) -> Any:
        """ 

`FindOrCreateProperty`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.FindOrCreateProperty "Permalink to this definition")
Finds or creates a property with the given name, returning a pointer to the variant.



Parameters
**name** (*string*) – 



Return type
*Variant*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.richtext.RichTextProperties.GetCount "Permalink to this definition")
Returns a count of the properties.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetProperties(self) -> 'RichTextVariantArray':
        """ 

`GetProperties`(*self*)[¶](#wx.richtext.RichTextProperties.GetProperties "Permalink to this definition")
Returns the array of variants implementing the properties.



Return type
*RichTextVariantArray*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetProperty(self, name: str) -> Any:
        """ 

`GetProperty`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.GetProperty "Permalink to this definition")
Gets the property variant by name.



Parameters
**name** (*string*) – 



Return type
*Variant*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyBool(self, name: str) -> bool:
        """ 

`GetPropertyBool`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.GetPropertyBool "Permalink to this definition")
Gets the value of the named property as a boolean.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyDouble(self, name: str) -> float:
        """ 

`GetPropertyDouble`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.GetPropertyDouble "Permalink to this definition")
Gets the value of the named property as a double.



Parameters
**name** (*string*) – 



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyLong(self, name: str) -> int:
        """ 

`GetPropertyLong`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.GetPropertyLong "Permalink to this definition")
Gets the value of the named property as a long integer.



Parameters
**name** (*string*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyNames(self) -> list[str]:
        """ 

`GetPropertyNames`(*self*)[¶](#wx.richtext.RichTextProperties.GetPropertyNames "Permalink to this definition")
Returns all the property names.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def GetPropertyString(self, name: str) -> str:
        """ 

`GetPropertyString`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.GetPropertyString "Permalink to this definition")
Gets the value of the named property as a string.



Parameters
**name** (*string*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def HasProperty(self, name: str) -> bool:
        """ 

`HasProperty`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.HasProperty "Permalink to this definition")
Returns `True` if the given property is found.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def MergeProperties(self, properties: 'richtext.RichTextProperties') -> None:
        """ 

`MergeProperties`(*self*, *properties*)[¶](#wx.richtext.RichTextProperties.MergeProperties "Permalink to this definition")
Merges the given properties with these properties.



Parameters
**properties** ([*wx.richtext.RichTextProperties*](#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def Remove(self, name: str) -> bool:
        """ 

`Remove`(*self*, *name*)[¶](#wx.richtext.RichTextProperties.Remove "Permalink to this definition")
Removes the given property.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def RemoveProperties(self, properties: 'richtext.RichTextProperties') -> None:
        """ 

`RemoveProperties`(*self*, *properties*)[¶](#wx.richtext.RichTextProperties.RemoveProperties "Permalink to this definition")
Removes the given properties from these properties.



Parameters
**properties** ([*wx.richtext.RichTextProperties*](#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def SetProperties(self, props: RichTextVariantArray) -> None:
        """ 

`SetProperties`(*self*, *props*)[¶](#wx.richtext.RichTextProperties.SetProperties "Permalink to this definition")
Sets the array of variants.



Parameters
**props** (*RichTextVariantArray*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def SetProperty(self, props: Any) -> None:
        """ 

`SetProperty`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextProperties.SetProperty "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetProperty** *(self, variant)*


Sets the property by passing a variant which contains a name and value.



Parameters
**variant** (*Variant*) – 






---

  



**SetProperty** *(self, name, variant)*


Sets a property by name and variant.



Parameters
* **name** (*string*) –
* **variant** (*Variant*) –






---

  



**SetProperty** *(self, name, value)*


Sets a property by name and string value.



Parameters
* **name** (*string*) –
* **value** (*string*) –






---

  



**SetProperty** *(self, name, value)*


Sets a property by name and Char value.



Parameters
* **name** (*string*) –
* **value** (*wx.Char*) –






---

  



**SetProperty** *(self, name, value)*


Sets property by name and long integer value.



Parameters
* **name** (*string*) –
* **value** (*long*) –






---

  



**SetProperty** *(self, name, value)*


Sets property by name and float value.



Parameters
* **name** (*string*) –
* **value** (*float*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.RichTextProperties.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**props** ([*wx.richtext.RichTextProperties*](#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextProperties.html
        """

    Count: int  # `Count`[¶](#wx.richtext.RichTextProperties.Count "Permalink to this definition")See [`GetCount`](#wx.richtext.RichTextProperties.GetCount "wx.richtext.RichTextProperties.GetCount")
    Properties: 'RichTextVariantArray'  # `Properties`[¶](#wx.richtext.RichTextProperties.Properties "Permalink to this definition")See [`GetProperties`](#wx.richtext.RichTextProperties.GetProperties "wx.richtext.RichTextProperties.GetProperties") and [`SetProperties`](#wx.richtext.RichTextProperties.SetProperties "wx.richtext.RichTextProperties.SetProperties")
    PropertyNames: list[str]  # `PropertyNames`[¶](#wx.richtext.RichTextProperties.PropertyNames "Permalink to this definition")See [`GetPropertyNames`](#wx.richtext.RichTextProperties.GetPropertyNames "wx.richtext.RichTextProperties.GetPropertyNames")



class RichTextRenderer(Object):
    """ **Possible constructors**:



```
RichTextRenderer()

```


This class isolates some common drawing functionality.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.RichTextRenderer.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawBitmapBullet(self, paragraph, dc, attr, rect) -> bool:
        """ 

`DrawBitmapBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*)[¶](#wx.richtext.RichTextRenderer.DrawBitmapBullet "Permalink to this definition")
Draws a bitmap bullet, where the bullet bitmap is specified by the value of GetBulletName.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawStandardBullet(self, paragraph, dc, attr, rect) -> bool:
        """ 

`DrawStandardBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*)[¶](#wx.richtext.RichTextRenderer.DrawStandardBullet "Permalink to this definition")
Draws a standard bullet, as specified by the value of GetBulletName.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def DrawTextBullet(self, paragraph, dc, attr, rect, text) -> bool:
        """ 

`DrawTextBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*, *text*)[¶](#wx.richtext.RichTextRenderer.DrawTextBullet "Permalink to this definition")
Draws a bullet that can be described by text, such as numbered or symbol bullets.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def EnumerateStandardBulletNames(self, bulletNames: list[str]) -> bool:
        """ 

`EnumerateStandardBulletNames`(*self*, *bulletNames*)[¶](#wx.richtext.RichTextRenderer.EnumerateStandardBulletNames "Permalink to this definition")
Enumerate the standard bullet names currently supported.


This function should be overridden.



Parameters
**bulletNames** (*list of strings*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """

    def MeasureBullet(self, paragraph, dc, attr, sz) -> bool:
        """ 

`MeasureBullet`(*self*, *paragraph*, *dc*, *attr*, *sz*)[¶](#wx.richtext.RichTextRenderer.MeasureBullet "Permalink to this definition")
Measure the bullet.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRenderer.html
        """



class RichTextStyleDefinition(Object):
    """ **Possible constructors**:



```
RichTextStyleDefinition(name="")

```


This is a base class for paragraph and character styles.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ 

`__init__`(*self*, *name=""*)[¶](#wx.richtext.RichTextStyleDefinition.__init__ "Permalink to this definition")
Constructor.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetBaseStyle(self) -> str:
        """ 

`GetBaseStyle`(*self*)[¶](#wx.richtext.RichTextStyleDefinition.GetBaseStyle "Permalink to this definition")
Returns the style on which this style is based.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetDescription(self) -> str:
        """ 

`GetDescription`(*self*)[¶](#wx.richtext.RichTextStyleDefinition.GetDescription "Permalink to this definition")
Returns the style’s description.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextStyleDefinition.GetName "Permalink to this definition")
Returns the style name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ 

`GetProperties`(*self*)[¶](#wx.richtext.RichTextStyleDefinition.GetProperties "Permalink to this definition")
Returns the definition’s properties.



Return type
 [wx.richtext.RichTextProperties](wx.richtext.RichTextProperties.html#wx-richtext-richtextproperties)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetStyle(self) -> 'RichTextAttr':
        """ 

`GetStyle`(*self*)[¶](#wx.richtext.RichTextStyleDefinition.GetStyle "Permalink to this definition")
Returns the attributes associated with this style.



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def GetStyleMergedWithBase(self, sheet: 'richtext.RichTextStyleSheet') -> 'RichTextAttr':
        """ 

`GetStyleMergedWithBase`(*self*, *sheet*)[¶](#wx.richtext.RichTextStyleDefinition.GetStyleMergedWithBase "Permalink to this definition")
Returns the style attributes combined with the attributes of the specified base style, if any.


This function works recursively.



Parameters
**sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetBaseStyle(self, name: str) -> None:
        """ 

`SetBaseStyle`(*self*, *name*)[¶](#wx.richtext.RichTextStyleDefinition.SetBaseStyle "Permalink to this definition")
Sets the name of the style that this style is based on.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetDescription(self, descr: str) -> None:
        """ 

`SetDescription`(*self*, *descr*)[¶](#wx.richtext.RichTextStyleDefinition.SetDescription "Permalink to this definition")
Sets the style description.



Parameters
**descr** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextStyleDefinition.SetName "Permalink to this definition")
Sets the name of the style.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ 

`SetProperties`(*self*, *props*)[¶](#wx.richtext.RichTextStyleDefinition.SetProperties "Permalink to this definition")
Sets the definition’s properties.



Parameters
**props** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    def SetStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ 

`SetStyle`(*self*, *style*)[¶](#wx.richtext.RichTextStyleDefinition.SetStyle "Permalink to this definition")
Sets the attributes for this style.



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleDefinition.html
        """

    BaseStyle: str  # `BaseStyle`[¶](#wx.richtext.RichTextStyleDefinition.BaseStyle "Permalink to this definition")See [`GetBaseStyle`](#wx.richtext.RichTextStyleDefinition.GetBaseStyle "wx.richtext.RichTextStyleDefinition.GetBaseStyle") and [`SetBaseStyle`](#wx.richtext.RichTextStyleDefinition.SetBaseStyle "wx.richtext.RichTextStyleDefinition.SetBaseStyle")
    Description: str  # `Description`[¶](#wx.richtext.RichTextStyleDefinition.Description "Permalink to this definition")See [`GetDescription`](#wx.richtext.RichTextStyleDefinition.GetDescription "wx.richtext.RichTextStyleDefinition.GetDescription") and [`SetDescription`](#wx.richtext.RichTextStyleDefinition.SetDescription "wx.richtext.RichTextStyleDefinition.SetDescription")
    Name: str  # `Name`[¶](#wx.richtext.RichTextStyleDefinition.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextStyleDefinition.GetName "wx.richtext.RichTextStyleDefinition.GetName") and [`SetName`](#wx.richtext.RichTextStyleDefinition.SetName "wx.richtext.RichTextStyleDefinition.SetName")
    Properties: 'RichTextProperties'  # `Properties`[¶](#wx.richtext.RichTextStyleDefinition.Properties "Permalink to this definition")See [`GetProperties`](#wx.richtext.RichTextStyleDefinition.GetProperties "wx.richtext.RichTextStyleDefinition.GetProperties") and [`SetProperties`](#wx.richtext.RichTextStyleDefinition.SetProperties "wx.richtext.RichTextStyleDefinition.SetProperties")
    Style: 'RichTextAttr'  # `Style`[¶](#wx.richtext.RichTextStyleDefinition.Style "Permalink to this definition")See [`GetStyle`](#wx.richtext.RichTextStyleDefinition.GetStyle "wx.richtext.RichTextStyleDefinition.GetStyle") and [`SetStyle`](#wx.richtext.RichTextStyleDefinition.SetStyle "wx.richtext.RichTextStyleDefinition.SetStyle")



class RichTextStyleSheet(Object):
    """ **Possible constructors**:



```
RichTextStyleSheet()

```


A style sheet contains named paragraph and character styles that make
it easy for a user to apply combinations of attributes to a
RichTextCtrl.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.RichTextStyleSheet.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddCharacterStyle(self, styleDef: 'richtext.RichTextCharacterStyleDefinition') -> bool:
        """ 

`AddCharacterStyle`(*self*, *styleDef*)[¶](#wx.richtext.RichTextStyleSheet.AddCharacterStyle "Permalink to this definition")
Adds a definition to the character style list.



Parameters
**styleDef** ([*wx.richtext.RichTextCharacterStyleDefinition*](wx.richtext.RichTextCharacterStyleDefinition.html#wx.richtext.RichTextCharacterStyleDefinition "wx.richtext.RichTextCharacterStyleDefinition")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddListStyle(self, styleDef: 'richtext.RichTextListStyleDefinition') -> bool:
        """ 

`AddListStyle`(*self*, *styleDef*)[¶](#wx.richtext.RichTextStyleSheet.AddListStyle "Permalink to this definition")
Adds a definition to the list style list.



Parameters
**styleDef** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddParagraphStyle(self, styleDef: 'richtext.RichTextParagraphStyleDefinition') -> bool:
        """ 

`AddParagraphStyle`(*self*, *styleDef*)[¶](#wx.richtext.RichTextStyleSheet.AddParagraphStyle "Permalink to this definition")
Adds a definition to the paragraph style list.



Parameters
**styleDef** ([*wx.richtext.RichTextParagraphStyleDefinition*](wx.richtext.RichTextParagraphStyleDefinition.html#wx.richtext.RichTextParagraphStyleDefinition "wx.richtext.RichTextParagraphStyleDefinition")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def AddStyle(self, styleDef: 'richtext.RichTextStyleDefinition') -> bool:
        """ 

`AddStyle`(*self*, *styleDef*)[¶](#wx.richtext.RichTextStyleSheet.AddStyle "Permalink to this definition")
Adds a definition to the appropriate style list.



Parameters
**styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def DeleteStyles(self) -> None:
        """ 

`DeleteStyles`(*self*)[¶](#wx.richtext.RichTextStyleSheet.DeleteStyles "Permalink to this definition")
Deletes all styles.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindCharacterStyle(self, name, recurse=True) -> 'RichTextCharacterStyleDefinition':
        """ 

`FindCharacterStyle`(*self*, *name*, *recurse=True*)[¶](#wx.richtext.RichTextStyleSheet.FindCharacterStyle "Permalink to this definition")
Finds a character definition by name.



Parameters
* **name** (*string*) –
* **recurse** (*bool*) –



Return type
 [wx.richtext.RichTextCharacterStyleDefinition](wx.richtext.RichTextCharacterStyleDefinition.html#wx-richtext-richtextcharacterstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindListStyle(self, name, recurse=True) -> 'RichTextListStyleDefinition':
        """ 

`FindListStyle`(*self*, *name*, *recurse=True*)[¶](#wx.richtext.RichTextStyleSheet.FindListStyle "Permalink to this definition")
Finds a list definition by name.



Parameters
* **name** (*string*) –
* **recurse** (*bool*) –



Return type
 [wx.richtext.RichTextListStyleDefinition](wx.richtext.RichTextListStyleDefinition.html#wx-richtext-richtextliststyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindParagraphStyle(self, name, recurse=True) -> 'RichTextParagraphStyleDefinition':
        """ 

`FindParagraphStyle`(*self*, *name*, *recurse=True*)[¶](#wx.richtext.RichTextStyleSheet.FindParagraphStyle "Permalink to this definition")
Finds a paragraph definition by name.



Parameters
* **name** (*string*) –
* **recurse** (*bool*) –



Return type
 [wx.richtext.RichTextParagraphStyleDefinition](wx.richtext.RichTextParagraphStyleDefinition.html#wx-richtext-richtextparagraphstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def FindStyle(self, name: str) -> 'RichTextStyleDefinition':
        """ 

`FindStyle`(*self*, *name*)[¶](#wx.richtext.RichTextStyleSheet.FindStyle "Permalink to this definition")
Finds a style definition by name.



Parameters
**name** (*string*) – 



Return type
 [wx.richtext.RichTextStyleDefinition](wx.richtext.RichTextStyleDefinition.html#wx-richtext-richtextstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetCharacterStyle(self, n: int) -> 'RichTextCharacterStyleDefinition':
        """ 

`GetCharacterStyle`(*self*, *n*)[¶](#wx.richtext.RichTextStyleSheet.GetCharacterStyle "Permalink to this definition")
Returns the *nth* character style.



Parameters
**n** (*int*) – 



Return type
 [wx.richtext.RichTextCharacterStyleDefinition](wx.richtext.RichTextCharacterStyleDefinition.html#wx-richtext-richtextcharacterstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetCharacterStyleCount(self) -> int:
        """ 

`GetCharacterStyleCount`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetCharacterStyleCount "Permalink to this definition")
Returns the number of character styles.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetDescription(self) -> str:
        """ 

`GetDescription`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetDescription "Permalink to this definition")
Returns the style sheet’s description.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetListStyle(self, n: int) -> 'RichTextListStyleDefinition':
        """ 

`GetListStyle`(*self*, *n*)[¶](#wx.richtext.RichTextStyleSheet.GetListStyle "Permalink to this definition")
Returns the *nth* list style.



Parameters
**n** (*int*) – 



Return type
 [wx.richtext.RichTextListStyleDefinition](wx.richtext.RichTextListStyleDefinition.html#wx-richtext-richtextliststyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetListStyleCount(self) -> int:
        """ 

`GetListStyleCount`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetListStyleCount "Permalink to this definition")
Returns the number of list styles.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetName(self) -> str:
        """ 

`GetName`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetName "Permalink to this definition")
Returns the style sheet’s name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetParagraphStyle(self, n: int) -> 'RichTextParagraphStyleDefinition':
        """ 

`GetParagraphStyle`(*self*, *n*)[¶](#wx.richtext.RichTextStyleSheet.GetParagraphStyle "Permalink to this definition")
Returns the *nth* paragraph style.



Parameters
**n** (*int*) – 



Return type
 [wx.richtext.RichTextParagraphStyleDefinition](wx.richtext.RichTextParagraphStyleDefinition.html#wx-richtext-richtextparagraphstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetParagraphStyleCount(self) -> int:
        """ 

`GetParagraphStyleCount`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetParagraphStyleCount "Permalink to this definition")
Returns the number of paragraph styles.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def GetProperties(self) -> 'RichTextProperties':
        """ 

`GetProperties`(*self*)[¶](#wx.richtext.RichTextStyleSheet.GetProperties "Permalink to this definition")
Returns the sheet’s properties.



Return type
 [wx.richtext.RichTextProperties](wx.richtext.RichTextProperties.html#wx-richtext-richtextproperties)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveCharacterStyle(self, styleDef, deleteStyle=False) -> bool:
        """ 

`RemoveCharacterStyle`(*self*, *styleDef*, *deleteStyle=False*)[¶](#wx.richtext.RichTextStyleSheet.RemoveCharacterStyle "Permalink to this definition")
Removes a character style.



Parameters
* **styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) –
* **deleteStyle** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveListStyle(self, styleDef, deleteStyle=False) -> bool:
        """ 

`RemoveListStyle`(*self*, *styleDef*, *deleteStyle=False*)[¶](#wx.richtext.RichTextStyleSheet.RemoveListStyle "Permalink to this definition")
Removes a list style.



Parameters
* **styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) –
* **deleteStyle** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveParagraphStyle(self, styleDef, deleteStyle=False) -> bool:
        """ 

`RemoveParagraphStyle`(*self*, *styleDef*, *deleteStyle=False*)[¶](#wx.richtext.RichTextStyleSheet.RemoveParagraphStyle "Permalink to this definition")
Removes a paragraph style.



Parameters
* **styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) –
* **deleteStyle** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def RemoveStyle(self, styleDef, deleteStyle=False) -> bool:
        """ 

`RemoveStyle`(*self*, *styleDef*, *deleteStyle=False*)[¶](#wx.richtext.RichTextStyleSheet.RemoveStyle "Permalink to this definition")
Removes a style.



Parameters
* **styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) –
* **deleteStyle** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetDescription(self, descr: str) -> None:
        """ 

`SetDescription`(*self*, *descr*)[¶](#wx.richtext.RichTextStyleSheet.SetDescription "Permalink to this definition")
Sets the style sheet’s description.



Parameters
**descr** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetName(self, name: str) -> None:
        """ 

`SetName`(*self*, *name*)[¶](#wx.richtext.RichTextStyleSheet.SetName "Permalink to this definition")
Sets the style sheet’s name.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    def SetProperties(self, props: 'richtext.RichTextProperties') -> None:
        """ 

`SetProperties`(*self*, *props*)[¶](#wx.richtext.RichTextStyleSheet.SetProperties "Permalink to this definition")
Sets the sheet’s properties.



Parameters
**props** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleSheet.html
        """

    CharacterStyleCount: int  # `CharacterStyleCount`[¶](#wx.richtext.RichTextStyleSheet.CharacterStyleCount "Permalink to this definition")See [`GetCharacterStyleCount`](#wx.richtext.RichTextStyleSheet.GetCharacterStyleCount "wx.richtext.RichTextStyleSheet.GetCharacterStyleCount")
    Description: str  # `Description`[¶](#wx.richtext.RichTextStyleSheet.Description "Permalink to this definition")See [`GetDescription`](#wx.richtext.RichTextStyleSheet.GetDescription "wx.richtext.RichTextStyleSheet.GetDescription") and [`SetDescription`](#wx.richtext.RichTextStyleSheet.SetDescription "wx.richtext.RichTextStyleSheet.SetDescription")
    ListStyleCount: int  # `ListStyleCount`[¶](#wx.richtext.RichTextStyleSheet.ListStyleCount "Permalink to this definition")See [`GetListStyleCount`](#wx.richtext.RichTextStyleSheet.GetListStyleCount "wx.richtext.RichTextStyleSheet.GetListStyleCount")
    Name: str  # `Name`[¶](#wx.richtext.RichTextStyleSheet.Name "Permalink to this definition")See [`GetName`](#wx.richtext.RichTextStyleSheet.GetName "wx.richtext.RichTextStyleSheet.GetName") and [`SetName`](#wx.richtext.RichTextStyleSheet.SetName "wx.richtext.RichTextStyleSheet.SetName")
    ParagraphStyleCount: int  # `ParagraphStyleCount`[¶](#wx.richtext.RichTextStyleSheet.ParagraphStyleCount "Permalink to this definition")See [`GetParagraphStyleCount`](#wx.richtext.RichTextStyleSheet.GetParagraphStyleCount "wx.richtext.RichTextStyleSheet.GetParagraphStyleCount")
    Properties: 'RichTextProperties'  # `Properties`[¶](#wx.richtext.RichTextStyleSheet.Properties "Permalink to this definition")See [`GetProperties`](#wx.richtext.RichTextStyleSheet.GetProperties "wx.richtext.RichTextStyleSheet.GetProperties") and [`SetProperties`](#wx.richtext.RichTextStyleSheet.SetProperties "wx.richtext.RichTextStyleSheet.SetProperties")



class RichTextPrintout(Printout):
    """ **Possible constructors**:



```
RichTextPrintout(title="Printout")

```


This class implements print layout for RichTextBuffer.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
    """
    def __init__(self, title: str="Printout") -> None:
        """ 

`__init__`(*self*, *title="Printout"*)[¶](#wx.richtext.RichTextPrintout.__init__ "Permalink to this definition")
Constructor.



Parameters
**title** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def CalculateScaling(self, dc, textRect, headerRect, footerRect) -> None:
        """ 

`CalculateScaling`(*self*, *dc*, *textRect*, *headerRect*, *footerRect*)[¶](#wx.richtext.RichTextPrintout.CalculateScaling "Permalink to this definition")
Calculates scaling and text, header and footer rectangles.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **textRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **headerRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **footerRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetHeaderFooterData(self) -> 'RichTextHeaderFooterData':
        """ 

`GetHeaderFooterData`(*self*)[¶](#wx.richtext.RichTextPrintout.GetHeaderFooterData "Permalink to this definition")
Returns the header and footer data associated with the printout.



Return type
 [wx.richtext.RichTextHeaderFooterData](wx.richtext.RichTextHeaderFooterData.html#wx-richtext-richtextheaderfooterdata)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetPageInfo(self) -> tuple:
        """ 

`GetPageInfo`(*self*)[¶](#wx.richtext.RichTextPrintout.GetPageInfo "Permalink to this definition")
Gets the page information.



Return type
*tuple*



Returns
( *minPage*, *maxPage*, *selPageFrom*, *selPageTo* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def GetRichTextBuffer(self) -> 'RichTextBuffer':
        """ 

`GetRichTextBuffer`(*self*)[¶](#wx.richtext.RichTextPrintout.GetRichTextBuffer "Permalink to this definition")
Returns a pointer to the buffer being rendered.



Return type
 [wx.richtext.RichTextBuffer](wx.richtext.RichTextBuffer.html#wx-richtext-richtextbuffer)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def HasPage(self, page: int) -> bool:
        """ 

`HasPage`(*self*, *page*)[¶](#wx.richtext.RichTextPrintout.HasPage "Permalink to this definition")
Returns `True` if the given page exists in the printout.



Parameters
**page** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def OnPreparePrinting(self) -> None:
        """ 

`OnPreparePrinting`(*self*)[¶](#wx.richtext.RichTextPrintout.OnPreparePrinting "Permalink to this definition")
Prepares for printing, laying out the buffer and calculating pagination.




            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def OnPrintPage(self, page: int) -> bool:
        """ 

`OnPrintPage`(*self*, *page*)[¶](#wx.richtext.RichTextPrintout.OnPrintPage "Permalink to this definition")
Does the actual printing for this page.



Parameters
**page** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetHeaderFooterData(self, data: 'richtext.RichTextHeaderFooterData') -> None:
        """ 

`SetHeaderFooterData`(*self*, *data*)[¶](#wx.richtext.RichTextPrintout.SetHeaderFooterData "Permalink to this definition")
Sets the header and footer data associated with the printout.



Parameters
**data** ([*wx.richtext.RichTextHeaderFooterData*](wx.richtext.RichTextHeaderFooterData.html#wx.richtext.RichTextHeaderFooterData "wx.richtext.RichTextHeaderFooterData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetMargins(self, top=254, bottom=254, left=254, right=254) -> None:
        """ 

`SetMargins`(*self*, *top=254*, *bottom=254*, *left=254*, *right=254*)[¶](#wx.richtext.RichTextPrintout.SetMargins "Permalink to this definition")
Sets margins in 10ths of millimetre.


Defaults to 1 inch for margins.



Parameters
* **top** (*int*) –
* **bottom** (*int*) –
* **left** (*int*) –
* **right** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    def SetRichTextBuffer(self, buffer: 'richtext.RichTextBuffer') -> None:
        """ 

`SetRichTextBuffer`(*self*, *buffer*)[¶](#wx.richtext.RichTextPrintout.SetRichTextBuffer "Permalink to this definition")
Sets the buffer to print.


 [wx.richtext.RichTextPrintout](#wx-richtext-richtextprintout) does not manage this pointer; it should be managed by the calling code, such as  [wx.richtext.RichTextPrinting](wx.richtext.RichTextPrinting.html#wx-richtext-richtextprinting).



Parameters
**buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPrintout.html
        """

    HeaderFooterData: 'RichTextHeaderFooterData'  # `HeaderFooterData`[¶](#wx.richtext.RichTextPrintout.HeaderFooterData "Permalink to this definition")See [`GetHeaderFooterData`](#wx.richtext.RichTextPrintout.GetHeaderFooterData "wx.richtext.RichTextPrintout.GetHeaderFooterData") and [`SetHeaderFooterData`](#wx.richtext.RichTextPrintout.SetHeaderFooterData "wx.richtext.RichTextPrintout.SetHeaderFooterData")
    RichTextBuffer: 'RichTextBuffer'  # `RichTextBuffer`[¶](#wx.richtext.RichTextPrintout.RichTextBuffer "Permalink to this definition")See [`GetRichTextBuffer`](#wx.richtext.RichTextPrintout.GetRichTextBuffer "wx.richtext.RichTextPrintout.GetRichTextBuffer") and [`SetRichTextBuffer`](#wx.richtext.RichTextPrintout.SetRichTextBuffer "wx.richtext.RichTextPrintout.SetRichTextBuffer")



class RichTextAttr(TextAttr):
    """ **Possible constructors**:



```
RichTextAttr(attr)

RichTextAttr(attr)

RichTextAttr()

```


A class representing enhanced attributes for rich text objects.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextAttr.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, attr)*


Constructor taking a  [wx.TextAttr](wx.TextAttr.html#wx-textattr).



Parameters
**attr** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) – 






---

  



**\_\_init\_\_** *(self, attr)*


Copy constructor.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def Apply(self, style, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *style*, *compareWith=None*)[¶](#wx.richtext.RichTextAttr.Apply "Permalink to this definition")
Merges the given attributes.


If *compareWith* is not `None`, then it will be used to mask out those attributes that are the same in style and *compareWith*, for situations where we don’t want to explicitly set inherited attributes.



Parameters
* **style** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **compareWith** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.RichTextAttr.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **clashingAttr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **absentAttr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def Copy(self, attr: 'richtext.RichTextAttr') -> None:
        """ 

`Copy`(*self*, *attr*)[¶](#wx.richtext.RichTextAttr.Copy "Permalink to this definition")
Copy function.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def EqPartial(self, attr, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *attr*, *weakTest=True*)[¶](#wx.richtext.RichTextAttr.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of `attr` are present. If *weakTest* is `False`, the function will fail if an attribute is present in `attr` but not in this object.



Parameters
* **attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def GetTextBoxAttr(self) -> 'TextBoxAttr':
        """ 

`GetTextBoxAttr`(*self*)[¶](#wx.richtext.RichTextAttr.GetTextBoxAttr "Permalink to this definition")
Returns the text box attributes.



Return type
 [wx.richtext.TextBoxAttr](wx.richtext.TextBoxAttr.html#wx-richtext-textboxattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def IsDefault(self) -> bool:
        """ 

`IsDefault`(*self*)[¶](#wx.richtext.RichTextAttr.IsDefault "Permalink to this definition")
Returns `True` if no attributes are set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def RemoveStyle(self, attr: 'richtext.RichTextAttr') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.RichTextAttr.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def SetTextBoxAttr(self, attr: 'richtext.TextBoxAttr') -> None:
        """ 

`SetTextBoxAttr`(*self*, *attr*)[¶](#wx.richtext.RichTextAttr.SetTextBoxAttr "Permalink to this definition")
Set the text box attributes.



Parameters
**attr** ([*wx.richtext.TextBoxAttr*](wx.richtext.TextBoxAttr.html#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.RichTextAttr.__eq__ "Permalink to this definition")
Equality test.



Parameters
**attr** ([*wx.richtext.RichTextAttr*](#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextAttr.html
        """

    TextBoxAttr: 'TextBoxAttr'  # `TextBoxAttr`[¶](#wx.richtext.RichTextAttr.TextBoxAttr "Permalink to this definition")See [`GetTextBoxAttr`](#wx.richtext.RichTextAttr.GetTextBoxAttr "wx.richtext.RichTextAttr.GetTextBoxAttr") and [`SetTextBoxAttr`](#wx.richtext.RichTextAttr.SetTextBoxAttr "wx.richtext.RichTextAttr.SetTextBoxAttr")
    m_textBoxAttr: Any  # `m_textBoxAttr`[¶](#wx.richtext.RichTextAttr.m_textBoxAttr "Permalink to this definition")A public C++ attribute of type [`TextBoxAttr`](wx.richtext.TextBoxAttr.html#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr") .



class RichTextStdRenderer(RichTextRenderer):
    """ **Possible constructors**:



```
RichTextStdRenderer()

```


The standard renderer for drawing bullets.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.RichTextStdRenderer.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawBitmapBullet(self, paragraph, dc, attr, rect) -> bool:
        """ 

`DrawBitmapBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*)[¶](#wx.richtext.RichTextStdRenderer.DrawBitmapBullet "Permalink to this definition")
Draws a bitmap bullet, where the bullet bitmap is specified by the value of GetBulletName.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawStandardBullet(self, paragraph, dc, attr, rect) -> bool:
        """ 

`DrawStandardBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*)[¶](#wx.richtext.RichTextStdRenderer.DrawStandardBullet "Permalink to this definition")
Draws a standard bullet, as specified by the value of GetBulletName.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def DrawTextBullet(self, paragraph, dc, attr, rect, text) -> bool:
        """ 

`DrawTextBullet`(*self*, *paragraph*, *dc*, *attr*, *rect*, *text*)[¶](#wx.richtext.RichTextStdRenderer.DrawTextBullet "Permalink to this definition")
Draws a bullet that can be described by text, such as numbered or symbol bullets.


This function should be overridden.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def EnumerateStandardBulletNames(self, bulletNames: list[str]) -> bool:
        """ 

`EnumerateStandardBulletNames`(*self*, *bulletNames*)[¶](#wx.richtext.RichTextStdRenderer.EnumerateStandardBulletNames "Permalink to this definition")
Enumerate the standard bullet names currently supported.


This function should be overridden.



Parameters
**bulletNames** (*list of strings*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """

    def MeasureBullet(self, paragraph, dc, attr, sz) -> bool:
        """ 

`MeasureBullet`(*self*, *paragraph*, *dc*, *attr*, *sz*)[¶](#wx.richtext.RichTextStdRenderer.MeasureBullet "Permalink to this definition")
Measure the bullet.



Parameters
* **paragraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStdRenderer.html
        """



class RichTextBuffer(RichTextParagraphLayoutBox):
    """ **Possible constructors**:



```
RichTextBuffer()

RichTextBuffer(obj)

```


This is a kind of paragraph layout box, used to represent the whole
buffer.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBuffer.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextBuffer*](#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddDrawingHandler(handler: 'richtext.RichTextDrawingHandler') -> None:
        """ 

*static* `AddDrawingHandler`(*handler*)[¶](#wx.richtext.RichTextBuffer.AddDrawingHandler "Permalink to this definition")
Adds a drawing handler to the end.



Parameters
**handler** ([*wx.richtext.RichTextDrawingHandler*](wx.richtext.RichTextDrawingHandler.html#wx.richtext.RichTextDrawingHandler "wx.richtext.RichTextDrawingHandler")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def AddEventHandler(self, handler: 'EvtHandler') -> bool:
        """ 

`AddEventHandler`(*self*, *handler*)[¶](#wx.richtext.RichTextBuffer.AddEventHandler "Permalink to this definition")
Adds an event handler.


A buffer associated with a control has the control as the only event handler, but the application is free to add more if further notification is required. All handlers are notified of an event originating from the buffer, such as the replacement of a style sheet during loading.


The buffer never deletes any of the event handlers, unless [`RemoveEventHandler`](#wx.richtext.RichTextBuffer.RemoveEventHandler "wx.richtext.RichTextBuffer.RemoveEventHandler") is called with `True` as the second argument.



Parameters
**handler** ([*wx.EvtHandler*](wx.EvtHandler.html#wx.EvtHandler "wx.EvtHandler")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddFieldType(fieldType: 'richtext.RichTextFieldType') -> None:
        """ 

*static* `AddFieldType`(*fieldType*)[¶](#wx.richtext.RichTextBuffer.AddFieldType "Permalink to this definition")
Adds a field type.



Parameters
**fieldType** ([*wx.richtext.RichTextFieldType*](wx.richtext.RichTextFieldType.html#wx.richtext.RichTextFieldType "wx.richtext.RichTextFieldType")) – 





See also


[`RemoveFieldType`](#wx.richtext.RichTextBuffer.RemoveFieldType "wx.richtext.RichTextBuffer.RemoveFieldType") , [`FindFieldType`](#wx.richtext.RichTextBuffer.FindFieldType "wx.richtext.RichTextBuffer.FindFieldType") ,  [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield),  [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype),  [wx.richtext.RichTextFieldTypeStandard](wx.richtext.RichTextFieldTypeStandard.html#wx-richtext-richtextfieldtypestandard)





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def AddHandler(handler: 'richtext.RichTextFileHandler') -> None:
        """ 

*static* `AddHandler`(*handler*)[¶](#wx.richtext.RichTextBuffer.AddHandler "Permalink to this definition")
Adds a file handler to the end.



Parameters
**handler** ([*wx.richtext.RichTextFileHandler*](wx.richtext.RichTextFileHandler.html#wx.richtext.RichTextFileHandler "wx.richtext.RichTextFileHandler")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def AddParagraph(self, text, paraStyle=None) -> 'RichTextRange':
        """ 

`AddParagraph`(*self*, *text*, *paraStyle=None*)[¶](#wx.richtext.RichTextBuffer.AddParagraph "Permalink to this definition")
Convenience function to add a paragraph of text.



Parameters
* **text** (*string*) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BatchingUndo(self) -> bool:
        """ 

`BatchingUndo`(*self*)[¶](#wx.richtext.RichTextBuffer.BatchingUndo "Permalink to this definition")
Returns `True` if we are collapsing commands.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginAlignment(self, alignment: int) -> bool:
        """ 

`BeginAlignment`(*self*, *alignment*)[¶](#wx.richtext.RichTextBuffer.BeginAlignment "Permalink to this definition")
Begins using alignment.



Parameters
**alignment** ([*TextAttrAlignment*](wx.TextAttrAlignment.enumeration.html "TextAttrAlignment")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginBatchUndo(self, cmdName: str) -> bool:
        """ 

`BeginBatchUndo`(*self*, *cmdName*)[¶](#wx.richtext.RichTextBuffer.BeginBatchUndo "Permalink to this definition")
Begin collapsing undo/redo commands.


Note that this may not work properly if combining commands that delete or insert content, changing ranges for subsequent actions.


*cmdName* should be the name of the combined command that will appear next to Undo and Redo in the edit menu.



Parameters
**cmdName** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginBold(self) -> bool:
        """ 

`BeginBold`(*self*)[¶](#wx.richtext.RichTextBuffer.BeginBold "Permalink to this definition")
Begins using bold.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginCharacterStyle(self, characterStyle: str) -> bool:
        """ 

`BeginCharacterStyle`(*self*, *characterStyle*)[¶](#wx.richtext.RichTextBuffer.BeginCharacterStyle "Permalink to this definition")
Begins named character style.



Parameters
**characterStyle** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginFont(self, font: 'Font') -> bool:
        """ 

`BeginFont`(*self*, *font*)[¶](#wx.richtext.RichTextBuffer.BeginFont "Permalink to this definition")
Begins using this font.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginFontSize(self, pointSize: int) -> bool:
        """ 

`BeginFontSize`(*self*, *pointSize*)[¶](#wx.richtext.RichTextBuffer.BeginFontSize "Permalink to this definition")
Begins using point size.



Parameters
**pointSize** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginItalic(self) -> bool:
        """ 

`BeginItalic`(*self*)[¶](#wx.richtext.RichTextBuffer.BeginItalic "Permalink to this definition")
Begins using italic.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginLeftIndent(self, leftIndent, leftSubIndent=0) -> bool:
        """ 

`BeginLeftIndent`(*self*, *leftIndent*, *leftSubIndent=0*)[¶](#wx.richtext.RichTextBuffer.BeginLeftIndent "Permalink to this definition")
Begins using *leftIndent* for the left indent, and optionally *leftSubIndent* for the sub-indent.


Both are expressed in tenths of a millimetre.


The sub-indent is an offset from the left of the paragraph, and is used for all but the first line in a paragraph. A positive value will cause the first line to appear to the left of the subsequent lines, and a negative value will cause the first line to be indented relative to the subsequent lines.



Parameters
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginLineSpacing(self, lineSpacing: int) -> bool:
        """ 

`BeginLineSpacing`(*self*, *lineSpacing*)[¶](#wx.richtext.RichTextBuffer.BeginLineSpacing "Permalink to this definition")
Begins line spacing using the specified value.


*spacing* is a multiple, where 10 means single-spacing, 15 means 1.5 spacing, and 20 means float spacing.


The  [wx.TextAttrLineSpacing](wx.TextAttrLineSpacing.enumeration.html#wx-textattrlinespacing) enumeration values are defined for convenience.



Parameters
**lineSpacing** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginListStyle(self, listStyle, level=1, number=1) -> bool:
        """ 

`BeginListStyle`(*self*, *listStyle*, *level=1*, *number=1*)[¶](#wx.richtext.RichTextBuffer.BeginListStyle "Permalink to this definition")
Begins named list style.


Optionally, you can also pass a level and a number.



Parameters
* **listStyle** (*string*) –
* **level** (*int*) –
* **number** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginNumberedBullet(self, bulletNumber, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_ARABIC|TEXT_ATTR_BULLET_STYLE_PERIOD) -> bool:
        """ 

`BeginNumberedBullet`(*self*, *bulletNumber*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_ARABIC|TEXT\_ATTR\_BULLET\_STYLE\_PERIOD*)[¶](#wx.richtext.RichTextBuffer.BeginNumberedBullet "Permalink to this definition")
Begins numbered bullet.


This call will be needed for each item in the list, and the application should take care of incrementing the numbering.


*bulletNumber* is a number, usually starting with 1. *leftIndent* and *leftSubIndent* are values in tenths of a millimetre. *bulletStyle* is a bitlist of the following values:


 [wx.richtext.RichTextBuffer](#wx-richtext-richtextbuffer) uses indentation to render a bulleted item. The left indent is the distance between the margin and the bullet. The content of the paragraph, including the first line, starts at leftMargin + leftSubIndent. So the distance between the left edge of the bullet and the left of the actual paragraph is leftSubIndent.



Parameters
* **bulletNumber** (*int*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginParagraphSpacing(self, before, after) -> bool:
        """ 

`BeginParagraphSpacing`(*self*, *before*, *after*)[¶](#wx.richtext.RichTextBuffer.BeginParagraphSpacing "Permalink to this definition")
Begins paragraph spacing; pass the before-paragraph and after-paragraph spacing in tenths of a millimetre.



Parameters
* **before** (*int*) –
* **after** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginParagraphStyle(self, paragraphStyle: str) -> bool:
        """ 

`BeginParagraphStyle`(*self*, *paragraphStyle*)[¶](#wx.richtext.RichTextBuffer.BeginParagraphStyle "Permalink to this definition")
Begins named paragraph style.



Parameters
**paragraphStyle** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginRightIndent(self, rightIndent: int) -> bool:
        """ 

`BeginRightIndent`(*self*, *rightIndent*)[¶](#wx.richtext.RichTextBuffer.BeginRightIndent "Permalink to this definition")
Begins a right indent, specified in tenths of a millimetre.



Parameters
**rightIndent** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginStandardBullet(self, bulletName, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_STANDARD) -> bool:
        """ 

`BeginStandardBullet`(*self*, *bulletName*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_STANDARD*)[¶](#wx.richtext.RichTextBuffer.BeginStandardBullet "Permalink to this definition")
Begins applying a standard bullet, using one of the standard bullet names (currently `standard/circle` or `standard/square` .


See [`BeginNumberedBullet`](#wx.richtext.RichTextBuffer.BeginNumberedBullet "wx.richtext.RichTextBuffer.BeginNumberedBullet") for an explanation of how indentation is used to render the bulleted paragraph.



Parameters
* **bulletName** (*string*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ 

`BeginStyle`(*self*, *style*)[¶](#wx.richtext.RichTextBuffer.BeginStyle "Permalink to this definition")
Begin using a style.



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginSuppressUndo(self) -> bool:
        """ 

`BeginSuppressUndo`(*self*)[¶](#wx.richtext.RichTextBuffer.BeginSuppressUndo "Permalink to this definition")
Begin suppressing undo/redo commands.


The way undo is suppressed may be implemented differently by each command. If not dealt with by a command implementation, then it will be implemented automatically by not storing the command in the undo history when the action is submitted to the command processor.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginSymbolBullet(self, symbol, leftIndent, leftSubIndent, bulletStyle=TEXT_ATTR_BULLET_STYLE_SYMBOL) -> bool:
        """ 

`BeginSymbolBullet`(*self*, *symbol*, *leftIndent*, *leftSubIndent*, *bulletStyle=TEXT\_ATTR\_BULLET\_STYLE\_SYMBOL*)[¶](#wx.richtext.RichTextBuffer.BeginSymbolBullet "Permalink to this definition")
Begins applying a symbol bullet, using a character from the current font.


See [`BeginNumberedBullet`](#wx.richtext.RichTextBuffer.BeginNumberedBullet "wx.richtext.RichTextBuffer.BeginNumberedBullet") for an explanation of how indentation is used to render the bulleted paragraph.



Parameters
* **symbol** (*string*) –
* **leftIndent** (*int*) –
* **leftSubIndent** (*int*) –
* **bulletStyle** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginTextColour(self, colour: Union[int, str, 'Colour']) -> bool:
        """ 

`BeginTextColour`(*self*, *colour*)[¶](#wx.richtext.RichTextBuffer.BeginTextColour "Permalink to this definition")
Begins using this colour.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginURL(self, url, characterStyle="") -> bool:
        """ 

`BeginURL`(*self*, *url*, *characterStyle=""*)[¶](#wx.richtext.RichTextBuffer.BeginURL "Permalink to this definition")
Begins applying `wx.TEXT_ATTR_URL` to the content.


Pass a URL and optionally, a character style to apply, since it is common to mark a URL with a familiar style such as blue text with underlining.



Parameters
* **url** (*string*) –
* **characterStyle** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def BeginUnderline(self) -> bool:
        """ 

`BeginUnderline`(*self*)[¶](#wx.richtext.RichTextBuffer.BeginUnderline "Permalink to this definition")
Begins using underline.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def CanPasteFromClipboard(self) -> bool:
        """ 

`CanPasteFromClipboard`(*self*)[¶](#wx.richtext.RichTextBuffer.CanPasteFromClipboard "Permalink to this definition")
Returns `True` if we can paste from the clipboard.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpDrawingHandlers() -> None:
        """ 

*static* `CleanUpDrawingHandlers`()[¶](#wx.richtext.RichTextBuffer.CleanUpDrawingHandlers "Permalink to this definition")
Clean up drawing handlers.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpFieldTypes() -> None:
        """ 

*static* `CleanUpFieldTypes`()[¶](#wx.richtext.RichTextBuffer.CleanUpFieldTypes "Permalink to this definition")
Cleans up field types.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def CleanUpHandlers() -> None:
        """ 

*static* `CleanUpHandlers`()[¶](#wx.richtext.RichTextBuffer.CleanUpHandlers "Permalink to this definition")
Clean up file handlers.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ClearEventHandlers(self) -> None:
        """ 

`ClearEventHandlers`(*self*)[¶](#wx.richtext.RichTextBuffer.ClearEventHandlers "Permalink to this definition")
Clear event handlers.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ClearStyleStack(self) -> None:
        """ 

`ClearStyleStack`(*self*)[¶](#wx.richtext.RichTextBuffer.ClearStyleStack "Permalink to this definition")
Clears the style stack.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextBuffer.Clone "Permalink to this definition")
Clones the buffer.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Copy(self, obj: 'richtext.RichTextBuffer') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextBuffer.Copy "Permalink to this definition")
Copies the buffer.



Parameters
**obj** ([*wx.richtext.RichTextBuffer*](#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def CopyToClipboard(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`CopyToClipboard`(*self*, *range*)[¶](#wx.richtext.RichTextBuffer.CopyToClipboard "Permalink to this definition")
Copy the range to the clipboard.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def DeleteRangeWithUndo(self, range, ctrl) -> bool:
        """ 

`DeleteRangeWithUndo`(*self*, *range*, *ctrl*)[¶](#wx.richtext.RichTextBuffer.DeleteRangeWithUndo "Permalink to this definition")
Submits a command to delete this range.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndAlignment(self) -> bool:
        """ 

`EndAlignment`(*self*)[¶](#wx.richtext.RichTextBuffer.EndAlignment "Permalink to this definition")
Ends alignment.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndAllStyles(self) -> bool:
        """ 

`EndAllStyles`(*self*)[¶](#wx.richtext.RichTextBuffer.EndAllStyles "Permalink to this definition")
End all styles.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndBatchUndo(self) -> bool:
        """ 

`EndBatchUndo`(*self*)[¶](#wx.richtext.RichTextBuffer.EndBatchUndo "Permalink to this definition")
End collapsing undo/redo commands.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndBold(self) -> bool:
        """ 

`EndBold`(*self*)[¶](#wx.richtext.RichTextBuffer.EndBold "Permalink to this definition")
Ends using bold.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndCharacterStyle(self) -> bool:
        """ 

`EndCharacterStyle`(*self*)[¶](#wx.richtext.RichTextBuffer.EndCharacterStyle "Permalink to this definition")
Ends named character style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndFont(self) -> bool:
        """ 

`EndFont`(*self*)[¶](#wx.richtext.RichTextBuffer.EndFont "Permalink to this definition")
Ends using a font.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndFontSize(self) -> bool:
        """ 

`EndFontSize`(*self*)[¶](#wx.richtext.RichTextBuffer.EndFontSize "Permalink to this definition")
Ends using point size.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndItalic(self) -> bool:
        """ 

`EndItalic`(*self*)[¶](#wx.richtext.RichTextBuffer.EndItalic "Permalink to this definition")
Ends using italic.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndLeftIndent(self) -> bool:
        """ 

`EndLeftIndent`(*self*)[¶](#wx.richtext.RichTextBuffer.EndLeftIndent "Permalink to this definition")
Ends left indent.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndLineSpacing(self) -> bool:
        """ 

`EndLineSpacing`(*self*)[¶](#wx.richtext.RichTextBuffer.EndLineSpacing "Permalink to this definition")
Ends line spacing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndListStyle(self) -> bool:
        """ 

`EndListStyle`(*self*)[¶](#wx.richtext.RichTextBuffer.EndListStyle "Permalink to this definition")
Ends named character style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndNumberedBullet(self) -> bool:
        """ 

`EndNumberedBullet`(*self*)[¶](#wx.richtext.RichTextBuffer.EndNumberedBullet "Permalink to this definition")
Ends numbered bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndParagraphSpacing(self) -> bool:
        """ 

`EndParagraphSpacing`(*self*)[¶](#wx.richtext.RichTextBuffer.EndParagraphSpacing "Permalink to this definition")
Ends paragraph spacing.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndParagraphStyle(self) -> bool:
        """ 

`EndParagraphStyle`(*self*)[¶](#wx.richtext.RichTextBuffer.EndParagraphStyle "Permalink to this definition")
Ends named character style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndRightIndent(self) -> bool:
        """ 

`EndRightIndent`(*self*)[¶](#wx.richtext.RichTextBuffer.EndRightIndent "Permalink to this definition")
Ends right indent.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndStandardBullet(self) -> bool:
        """ 

`EndStandardBullet`(*self*)[¶](#wx.richtext.RichTextBuffer.EndStandardBullet "Permalink to this definition")
Ends standard bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndStyle(self) -> bool:
        """ 

`EndStyle`(*self*)[¶](#wx.richtext.RichTextBuffer.EndStyle "Permalink to this definition")
End the style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndSuppressUndo(self) -> bool:
        """ 

`EndSuppressUndo`(*self*)[¶](#wx.richtext.RichTextBuffer.EndSuppressUndo "Permalink to this definition")
End suppressing undo/redo commands.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndSymbolBullet(self) -> bool:
        """ 

`EndSymbolBullet`(*self*)[¶](#wx.richtext.RichTextBuffer.EndSymbolBullet "Permalink to this definition")
Ends symbol bullet.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndTextColour(self) -> bool:
        """ 

`EndTextColour`(*self*)[¶](#wx.richtext.RichTextBuffer.EndTextColour "Permalink to this definition")
Ends using a colour.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndURL(self) -> bool:
        """ 

`EndURL`(*self*)[¶](#wx.richtext.RichTextBuffer.EndURL "Permalink to this definition")
Ends URL.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def EndUnderline(self) -> bool:
        """ 

`EndUnderline`(*self*)[¶](#wx.richtext.RichTextBuffer.EndUnderline "Permalink to this definition")
Ends using underline.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindDrawingHandler(name: str) -> 'RichTextDrawingHandler':
        """ 

*static* `FindDrawingHandler`(*name*)[¶](#wx.richtext.RichTextBuffer.FindDrawingHandler "Permalink to this definition")
Finds a drawing handler by name.



Parameters
**name** (*string*) – 



Return type
 [wx.richtext.RichTextDrawingHandler](wx.richtext.RichTextDrawingHandler.html#wx-richtext-richtextdrawinghandler)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindFieldType(name: str) -> 'RichTextFieldType':
        """ 

*static* `FindFieldType`(*name*)[¶](#wx.richtext.RichTextBuffer.FindFieldType "Permalink to this definition")
Finds a field type by name.



Parameters
**name** (*string*) – 



Return type
 [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype)





See also


[`RemoveFieldType`](#wx.richtext.RichTextBuffer.RemoveFieldType "wx.richtext.RichTextBuffer.RemoveFieldType") , [`AddFieldType`](#wx.richtext.RichTextBuffer.AddFieldType "wx.richtext.RichTextBuffer.AddFieldType") ,  [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield),  [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype),  [wx.richtext.RichTextFieldTypeStandard](wx.richtext.RichTextFieldTypeStandard.html#wx-richtext-richtextfieldtypestandard)





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByType(imageType: RichTextFileType) -> 'RichTextFileHandler':
        """ 

*static* `FindHandlerByType`(*imageType*)[¶](#wx.richtext.RichTextBuffer.FindHandlerByType "Permalink to this definition")
Finds a handler by type.



Parameters
**imageType** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) – 



Return type
 [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByExtension(extension, imageType) -> 'RichTextFileHandler':
        """ 

*static* `FindHandlerByExtension`(*extension*, *imageType*)[¶](#wx.richtext.RichTextBuffer.FindHandlerByExtension "Permalink to this definition")
Finds a file handler by extension and type.



Parameters
* **extension** (*string*) –
* **imageType** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
 [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByName(name: str) -> 'RichTextFileHandler':
        """ 

*static* `FindHandlerByName`(*name*)[¶](#wx.richtext.RichTextBuffer.FindHandlerByName "Permalink to this definition")
Finds a file handler by name.



Parameters
**name** (*string*) – 



Return type
 [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def FindHandlerByFilename(filename, imageType) -> 'RichTextFileHandler':
        """ 

*static* `FindHandlerByFilename`(*filename*, *imageType*)[¶](#wx.richtext.RichTextBuffer.FindHandlerByFilename "Permalink to this definition")
Finds a handler by filename or, if supplied, type.



Parameters
* **filename** (*string*) –
* **imageType** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
 [wx.richtext.RichTextFileHandler](wx.richtext.RichTextFileHandler.html#wx-richtext-richtextfilehandler)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetBatchedCommand(self) -> 'RichTextCommand':
        """ 

`GetBatchedCommand`(*self*)[¶](#wx.richtext.RichTextBuffer.GetBatchedCommand "Permalink to this definition")
Returns the collapsed command.



Return type
 [wx.richtext.RichTextCommand](wx.richtext.RichTextCommand.html#wx-richtext-richtextcommand)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetBulletProportion() -> float:
        """ 

*static* `GetBulletProportion`()[¶](#wx.richtext.RichTextBuffer.GetBulletProportion "Permalink to this definition")
Returns the factor to multiply by character height to get a reasonable bullet size.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetBulletRightMargin() -> int:
        """ 

*static* `GetBulletRightMargin`()[¶](#wx.richtext.RichTextBuffer.GetBulletRightMargin "Permalink to this definition")
Returns the minimum margin between bullet and paragraph in 10ths of a mm.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetCommandProcessor(self) -> 'CommandProcessor':
        """ 

`GetCommandProcessor`(*self*)[¶](#wx.richtext.RichTextBuffer.GetCommandProcessor "Permalink to this definition")
Returns the command processor.


A text buffer always creates its own command processor when it is initialized.



Return type
[`CommandProcessor`](#wx.richtext.RichTextBuffer.CommandProcessor "wx.richtext.RichTextBuffer.CommandProcessor")






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetDimensionScale(self) -> float:
        """ 

`GetDimensionScale`(*self*)[¶](#wx.richtext.RichTextBuffer.GetDimensionScale "Permalink to this definition")
Returns the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetDrawingHandlers() -> list['richtext.RichTextDrawingHandler']:
        """ 

*static* `GetDrawingHandlers`()[¶](#wx.richtext.RichTextBuffer.GetDrawingHandlers "Permalink to this definition")
Returns the drawing handlers.



Return type
*RichTextDrawingHandlerList*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetExtWildcard(combine=False, save=False) -> Any:
        """ 

*static* `GetExtWildcard`(*combine=False*, *save=False*)[¶](#wx.richtext.RichTextBuffer.GetExtWildcard "Permalink to this definition")

> Gets a wildcard string for the file dialog based on all the currently
> loaded richtext file handlers, and a list that can be used to map
> those filter types to the file handler type.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetFloatingLayoutMode() -> bool:
        """ 

*static* `GetFloatingLayoutMode`()[¶](#wx.richtext.RichTextBuffer.GetFloatingLayoutMode "Permalink to this definition")
Returns the floating layout mode.


The default is `True`, where objects are laid out according to their floating status.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetFontScale(self) -> float:
        """ 

`GetFontScale`(*self*)[¶](#wx.richtext.RichTextBuffer.GetFontScale "Permalink to this definition")
Returns the scale factor for displaying fonts, for example for more comfortable editing.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetFontTable(self) -> 'RichTextFontTable':
        """ 

`GetFontTable`(*self*)[¶](#wx.richtext.RichTextBuffer.GetFontTable "Permalink to this definition")
Returns the table storing fonts, for quick access and font reuse.



Return type
 [wx.richtext.RichTextFontTable](wx.richtext.RichTextFontTable.html#wx-richtext-richtextfonttable)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetHandlerFlags(self) -> int:
        """ 

`GetHandlerFlags`(*self*)[¶](#wx.richtext.RichTextBuffer.GetHandlerFlags "Permalink to this definition")
Gets the handler flags, controlling loading and saving.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetHandlers() -> list['richtext.RichTextFileHandler']:
        """ 

*static* `GetHandlers`()[¶](#wx.richtext.RichTextBuffer.GetHandlers "Permalink to this definition")
Returns the file handlers.



Return type
*RichTextFileHandlerList*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def GetRenderer() -> 'RichTextRenderer':
        """ 

*static* `GetRenderer`()[¶](#wx.richtext.RichTextBuffer.GetRenderer "Permalink to this definition")
Returns the renderer object.



Return type
 [wx.richtext.RichTextRenderer](wx.richtext.RichTextRenderer.html#wx-richtext-richtextrenderer)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetScale(self) -> float:
        """ 

`GetScale`(*self*)[¶](#wx.richtext.RichTextBuffer.GetScale "Permalink to this definition")
Returns the scale factor for calculating dimensions.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextBuffer.GetStyleSheet "Permalink to this definition")
Returns the style sheet.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def GetStyleStackSize(self) -> int:
        """ 

`GetStyleStackSize`(*self*)[¶](#wx.richtext.RichTextBuffer.GetStyleStackSize "Permalink to this definition")
Returns the size of the style stack, for example to check correct nesting.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextBuffer.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextBuffer.Init "Permalink to this definition")
Initialisation.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InitStandardHandlers() -> None:
        """ 

*static* `InitStandardHandlers`()[¶](#wx.richtext.RichTextBuffer.InitStandardHandlers "Permalink to this definition")
Initialise the standard file handlers.


Currently, only the plain text loading/saving handler is initialised by default.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InsertDrawingHandler(handler: 'richtext.RichTextDrawingHandler') -> None:
        """ 

*static* `InsertDrawingHandler`(*handler*)[¶](#wx.richtext.RichTextBuffer.InsertDrawingHandler "Permalink to this definition")
Inserts a drawing handler at the front.



Parameters
**handler** ([*wx.richtext.RichTextDrawingHandler*](wx.richtext.RichTextDrawingHandler.html#wx.richtext.RichTextDrawingHandler "wx.richtext.RichTextDrawingHandler")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def InsertHandler(handler: 'richtext.RichTextFileHandler') -> None:
        """ 

*static* `InsertHandler`(*handler*)[¶](#wx.richtext.RichTextBuffer.InsertHandler "Permalink to this definition")
Inserts a file handler at the front.



Parameters
**handler** ([*wx.richtext.RichTextFileHandler*](wx.richtext.RichTextFileHandler.html#wx.richtext.RichTextFileHandler "wx.richtext.RichTextFileHandler")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertImageWithUndo(*args, **kwargs) -> bool:
        """ 

`InsertImageWithUndo`(*self*, *pos*, *imageBlock*, *ctrl*, *flags=0*, *textAttr=RichTextAttr()*)[¶](#wx.richtext.RichTextBuffer.InsertImageWithUndo "Permalink to this definition")
Submits a command to insert the given image.



Parameters
* **pos** (*long*) –
* **imageBlock** ([*wx.richtext.RichTextImageBlock*](wx.richtext.RichTextImageBlock.html#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertNewlineWithUndo(self, pos, ctrl, flags=0) -> bool:
        """ 

`InsertNewlineWithUndo`(*self*, *pos*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextBuffer.InsertNewlineWithUndo "Permalink to this definition")
Submits a command to insert a newline.



Parameters
* **pos** (*long*) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertObjectWithUndo(self, pos, object, ctrl, flags) -> 'RichTextObject':
        """ 

`InsertObjectWithUndo`(*self*, *pos*, *object*, *ctrl*, *flags*)[¶](#wx.richtext.RichTextBuffer.InsertObjectWithUndo "Permalink to this definition")
Submits a command to insert an object.



Parameters
* **pos** (*long*) –
* **object** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertParagraphsWithUndo(self, pos, paragraphs, ctrl, flags=0) -> bool:
        """ 

`InsertParagraphsWithUndo`(*self*, *pos*, *paragraphs*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextBuffer.InsertParagraphsWithUndo "Permalink to this definition")
Submits a command to insert paragraphs.



Parameters
* **pos** (*long*) –
* **paragraphs** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def InsertTextWithUndo(self, pos, text, ctrl, flags=0) -> bool:
        """ 

`InsertTextWithUndo`(*self*, *pos*, *text*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextBuffer.InsertTextWithUndo "Permalink to this definition")
Submits a command to insert the given text.



Parameters
* **pos** (*long*) –
* **text** (*string*) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def IsModified(self) -> bool:
        """ 

`IsModified`(*self*)[¶](#wx.richtext.RichTextBuffer.IsModified "Permalink to this definition")
Returns `True` if the buffer was modified.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def LoadFile(self, *args, **kw) -> bool:
        """ 

`LoadFile`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBuffer.LoadFile "Permalink to this definition")
Loads content from a stream or file.


Not all handlers will implement file loading.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**LoadFile** *(self, filename, type=RICHTEXT\_TYPE\_ANY)*



Parameters
* **filename** (*string*) –
* **type** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
*bool*






---

  



**LoadFile** *(self, stream, type=RICHTEXT\_TYPE\_ANY)*



Parameters
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –
* **type** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def Modify(self, modify: bool=True) -> None:
        """ 

`Modify`(*self*, *modify=True*)[¶](#wx.richtext.RichTextBuffer.Modify "Permalink to this definition")
Mark modified.



Parameters
**modify** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PasteFromClipboard(self, position: int) -> bool:
        """ 

`PasteFromClipboard`(*self*, *position*)[¶](#wx.richtext.RichTextBuffer.PasteFromClipboard "Permalink to this definition")
Paste the clipboard content to the buffer.



Parameters
**position** (*long*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PopStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`PopStyleSheet`(*self*)[¶](#wx.richtext.RichTextBuffer.PopStyleSheet "Permalink to this definition")
Pops the style sheet from the top of the style sheet stack.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def PushStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ 

`PushStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextBuffer.PushStyleSheet "Permalink to this definition")
Pushes the style sheet to the top of the style sheet stack.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveDrawingHandler(name: str) -> bool:
        """ 

*static* `RemoveDrawingHandler`(*name*)[¶](#wx.richtext.RichTextBuffer.RemoveDrawingHandler "Permalink to this definition")
Removes a drawing handler.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def RemoveEventHandler(self, handler, deleteHandler=False) -> bool:
        """ 

`RemoveEventHandler`(*self*, *handler*, *deleteHandler=False*)[¶](#wx.richtext.RichTextBuffer.RemoveEventHandler "Permalink to this definition")
Removes an event handler from the buffer’s list of handlers, deleting the object if *deleteHandler* is `True`.



Parameters
* **handler** ([*wx.EvtHandler*](wx.EvtHandler.html#wx.EvtHandler "wx.EvtHandler")) –
* **deleteHandler** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveFieldType(name: str) -> bool:
        """ 

*static* `RemoveFieldType`(*name*)[¶](#wx.richtext.RichTextBuffer.RemoveFieldType "Permalink to this definition")
Removes a field type by name.



Parameters
**name** (*string*) – 



Return type
*bool*





See also


[`AddFieldType`](#wx.richtext.RichTextBuffer.AddFieldType "wx.richtext.RichTextBuffer.AddFieldType") , [`FindFieldType`](#wx.richtext.RichTextBuffer.FindFieldType "wx.richtext.RichTextBuffer.FindFieldType") ,  [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield),  [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype),  [wx.richtext.RichTextFieldTypeStandard](wx.richtext.RichTextFieldTypeStandard.html#wx-richtext-richtextfieldtypestandard)





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def RemoveHandler(name: str) -> bool:
        """ 

*static* `RemoveHandler`(*name*)[¶](#wx.richtext.RichTextBuffer.RemoveHandler "Permalink to this definition")
Removes a file handler.



Parameters
**name** (*string*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def ResetAndClearCommands(self) -> None:
        """ 

`ResetAndClearCommands`(*self*)[¶](#wx.richtext.RichTextBuffer.ResetAndClearCommands "Permalink to this definition")
Clears the buffer, adds an empty paragraph, and clears the command processor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SaveFile(self, *args, **kw) -> bool:
        """ 

`SaveFile`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBuffer.SaveFile "Permalink to this definition")
Saves content to a stream or file.


Not all handlers will implement file saving.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SaveFile** *(self, filename, type=RICHTEXT\_TYPE\_ANY)*



Parameters
* **filename** (*string*) –
* **type** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
*bool*






---

  



**SaveFile** *(self, stream, type=RICHTEXT\_TYPE\_ANY)*



Parameters
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –
* **type** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SendEvent(self, event, sendToAll=True) -> bool:
        """ 

`SendEvent`(*self*, *event*, *sendToAll=True*)[¶](#wx.richtext.RichTextBuffer.SendEvent "Permalink to this definition")
Send event to event handlers.


If sendToAll is `True`, will send to all event handlers, otherwise will stop at the first successful one.



Parameters
* **event** ([*wx.Event*](wx.Event.html#wx.Event "wx.Event")) –
* **sendToAll** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetBulletProportion(prop: float) -> None:
        """ 

*static* `SetBulletProportion`(*prop*)[¶](#wx.richtext.RichTextBuffer.SetBulletProportion "Permalink to this definition")
Sets the factor to multiply by character height to get a reasonable bullet size.



Parameters
**prop** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetBulletRightMargin(margin: int) -> None:
        """ 

*static* `SetBulletRightMargin`(*margin*)[¶](#wx.richtext.RichTextBuffer.SetBulletRightMargin "Permalink to this definition")
Sets the minimum margin between bullet and paragraph in 10ths of a mm.



Parameters
**margin** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetDimensionScale(self, dimScale: float) -> None:
        """ 

`SetDimensionScale`(*self*, *dimScale*)[¶](#wx.richtext.RichTextBuffer.SetDimensionScale "Permalink to this definition")
Sets the scale factor for displaying certain dimensions such as indentation and inter-paragraph spacing.


This can be useful when editing in a small control where you still want legible text, but a minimum of wasted white space.



Parameters
**dimScale** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetFloatingLayoutMode(mode: bool) -> None:
        """ 

*static* `SetFloatingLayoutMode`(*mode*)[¶](#wx.richtext.RichTextBuffer.SetFloatingLayoutMode "Permalink to this definition")
Sets the floating layout mode.


Pass `False` to speed up editing by not performing floating layout. This setting affects all buffers.



Parameters
**mode** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetFontScale(self, fontScale: float) -> None:
        """ 

`SetFontScale`(*self*, *fontScale*)[¶](#wx.richtext.RichTextBuffer.SetFontScale "Permalink to this definition")
Sets the scale factor for displaying fonts, for example for more comfortable editing.



Parameters
**fontScale** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetFontTable(self, table: 'richtext.RichTextFontTable') -> None:
        """ 

`SetFontTable`(*self*, *table*)[¶](#wx.richtext.RichTextBuffer.SetFontTable "Permalink to this definition")
Sets table storing fonts, for quick access and font reuse.



Parameters
**table** ([*wx.richtext.RichTextFontTable*](wx.richtext.RichTextFontTable.html#wx.richtext.RichTextFontTable "wx.richtext.RichTextFontTable")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetHandlerFlags(self, flags: int) -> None:
        """ 

`SetHandlerFlags`(*self*, *flags*)[¶](#wx.richtext.RichTextBuffer.SetHandlerFlags "Permalink to this definition")
Sets the handler flags, controlling loading and saving.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    @staticmethod
    def SetRenderer(renderer: 'richtext.RichTextRenderer') -> None:
        """ 

*static* `SetRenderer`(*renderer*)[¶](#wx.richtext.RichTextBuffer.SetRenderer "Permalink to this definition")
Sets *renderer* as the object to be used to render certain aspects of the content, such as bullets.


You can override default rendering by deriving a new class from  [wx.richtext.RichTextRenderer](wx.richtext.RichTextRenderer.html#wx-richtext-richtextrenderer) or  [wx.richtext.RichTextStdRenderer](wx.richtext.RichTextStdRenderer.html#wx-richtext-richtextstdrenderer), overriding one or more virtual functions, and setting an instance of the class using this function.



Parameters
**renderer** ([*wx.richtext.RichTextRenderer*](wx.richtext.RichTextRenderer.html#wx.richtext.RichTextRenderer "wx.richtext.RichTextRenderer")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetScale(self, scale: float) -> None:
        """ 

`SetScale`(*self*, *scale*)[¶](#wx.richtext.RichTextBuffer.SetScale "Permalink to this definition")
Sets the scale factor for calculating dimensions.



Parameters
**scale** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextBuffer.SetStyleSheet "Permalink to this definition")
Sets style sheet, if any.


This will allow the application to use named character and paragraph styles found in the style sheet.


Neither the buffer nor the control owns the style sheet so must be deleted by the application.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SetStyleSheetAndNotify(self, sheet: 'richtext.RichTextStyleSheet') -> bool:
        """ 

`SetStyleSheetAndNotify`(*self*, *sheet*)[¶](#wx.richtext.RichTextBuffer.SetStyleSheetAndNotify "Permalink to this definition")
Sets the style sheet and sends a notification of the change.



Parameters
**sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SubmitAction(self, action: 'richtext.RichTextAction') -> bool:
        """ 

`SubmitAction`(*self*, *action*)[¶](#wx.richtext.RichTextBuffer.SubmitAction "Permalink to this definition")
Submit the action immediately, or delay according to whether collapsing is on.



Parameters
**action** ([*wx.richtext.RichTextAction*](wx.richtext.RichTextAction.html#wx.richtext.RichTextAction "wx.richtext.RichTextAction")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    def SuppressingUndo(self) -> bool:
        """ 

`SuppressingUndo`(*self*)[¶](#wx.richtext.RichTextBuffer.SuppressingUndo "Permalink to this definition")
Are we suppressing undo??



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBuffer.html
        """

    BatchedCommand: 'RichTextCommand'  # `BatchedCommand`[¶](#wx.richtext.RichTextBuffer.BatchedCommand "Permalink to this definition")See [`GetBatchedCommand`](#wx.richtext.RichTextBuffer.GetBatchedCommand "wx.richtext.RichTextBuffer.GetBatchedCommand")
    CommandProcessor: '_CommandProcessor'  # `CommandProcessor`[¶](#wx.richtext.RichTextBuffer.CommandProcessor "Permalink to this definition")See [`GetCommandProcessor`](#wx.richtext.RichTextBuffer.GetCommandProcessor "wx.richtext.RichTextBuffer.GetCommandProcessor")
    DimensionScale: float  # `DimensionScale`[¶](#wx.richtext.RichTextBuffer.DimensionScale "Permalink to this definition")See [`GetDimensionScale`](#wx.richtext.RichTextBuffer.GetDimensionScale "wx.richtext.RichTextBuffer.GetDimensionScale") and [`SetDimensionScale`](#wx.richtext.RichTextBuffer.SetDimensionScale "wx.richtext.RichTextBuffer.SetDimensionScale")
    FontScale: float  # `FontScale`[¶](#wx.richtext.RichTextBuffer.FontScale "Permalink to this definition")See [`GetFontScale`](#wx.richtext.RichTextBuffer.GetFontScale "wx.richtext.RichTextBuffer.GetFontScale") and [`SetFontScale`](#wx.richtext.RichTextBuffer.SetFontScale "wx.richtext.RichTextBuffer.SetFontScale")
    FontTable: 'RichTextFontTable'  # `FontTable`[¶](#wx.richtext.RichTextBuffer.FontTable "Permalink to this definition")See [`GetFontTable`](#wx.richtext.RichTextBuffer.GetFontTable "wx.richtext.RichTextBuffer.GetFontTable") and [`SetFontTable`](#wx.richtext.RichTextBuffer.SetFontTable "wx.richtext.RichTextBuffer.SetFontTable")
    HandlerFlags: int  # `HandlerFlags`[¶](#wx.richtext.RichTextBuffer.HandlerFlags "Permalink to this definition")See [`GetHandlerFlags`](#wx.richtext.RichTextBuffer.GetHandlerFlags "wx.richtext.RichTextBuffer.GetHandlerFlags") and [`SetHandlerFlags`](#wx.richtext.RichTextBuffer.SetHandlerFlags "wx.richtext.RichTextBuffer.SetHandlerFlags")
    Scale: float  # `Scale`[¶](#wx.richtext.RichTextBuffer.Scale "Permalink to this definition")See [`GetScale`](#wx.richtext.RichTextBuffer.GetScale "wx.richtext.RichTextBuffer.GetScale") and [`SetScale`](#wx.richtext.RichTextBuffer.SetScale "wx.richtext.RichTextBuffer.SetScale")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextBuffer.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextBuffer.GetStyleSheet "wx.richtext.RichTextBuffer.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextBuffer.SetStyleSheet "wx.richtext.RichTextBuffer.SetStyleSheet")
    StyleStackSize: int  # `StyleStackSize`[¶](#wx.richtext.RichTextBuffer.StyleStackSize "Permalink to this definition")See [`GetStyleStackSize`](#wx.richtext.RichTextBuffer.GetStyleStackSize "wx.richtext.RichTextBuffer.GetStyleStackSize")



class RichTextRange:
    """ **Possible constructors**:



```
RichTextRange()

RichTextRange(start, end)

RichTextRange(range)

```


This stores beginning and end positions for a range of data.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextRange.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, start, end)*


Constructor taking start and end positions.



Parameters
* **start** (*long*) –
* **end** (*long*) –






---

  



**\_\_init\_\_** *(self, range)*


Copy constructor.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Contains(self, pos: int) -> bool:
        """ 

`Contains`(*self*, *pos*)[¶](#wx.richtext.RichTextRange.Contains "Permalink to this definition")
Returns `True` if *pos* was within the range.


Does not match if the range is empty.



Parameters
**pos** (*long*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def FromInternal(self) -> 'RichTextRange':
        """ 

`FromInternal`(*self*)[¶](#wx.richtext.RichTextRange.FromInternal "Permalink to this definition")
Converts the internal range, which uses the first and last character positions of the range, to the API-standard range, whose end is one past the last character in the range.


In other words, one is added to the end position. (n, n+1) is the range of a single character.



Return type
 [wx.richtext.RichTextRange](#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Get(self) -> tuple:
        """ 

`Get`(*self*)[¶](#wx.richtext.RichTextRange.Get "Permalink to this definition")
Return the start and end properties as a tuple.



Return type
*tuple*



Returns
( *start*, *end* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetEnd(self) -> int:
        """ 

`GetEnd`(*self*)[¶](#wx.richtext.RichTextRange.GetEnd "Permalink to this definition")
Gets the end position.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetIM(self) -> None:
        """ 

`GetIM`(*self*)[¶](#wx.richtext.RichTextRange.GetIM "Permalink to this definition")
Returns an immutable representation of the `wx.RichTextRange` object, based on `namedtuple`.


This new object is hashable and can be used as a dictionary key,
be added to sets, etc. It can be converted back into a real `wx.RichTextRange`
with a simple statement like this: `obj = wx.RichTextRange(imObj)`.




            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetLength(self) -> int:
        """ 

`GetLength`(*self*)[¶](#wx.richtext.RichTextRange.GetLength "Permalink to this definition")
Gets the length of the range.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def GetStart(self) -> int:
        """ 

`GetStart`(*self*)[¶](#wx.richtext.RichTextRange.GetStart "Permalink to this definition")
Returns the start position.



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def IsOutside(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`IsOutside`(*self*, *range*)[¶](#wx.richtext.RichTextRange.IsOutside "Permalink to this definition")
Returns `True` if this range is completely outside *range*.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def IsWithin(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`IsWithin`(*self*, *range*)[¶](#wx.richtext.RichTextRange.IsWithin "Permalink to this definition")
Returns `True` if this range is completely within *range*.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def LimitTo(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`LimitTo`(*self*, *range*)[¶](#wx.richtext.RichTextRange.LimitTo "Permalink to this definition")
Limit this range to be within *range*.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetEnd(self, end: int) -> None:
        """ 

`SetEnd`(*self*, *end*)[¶](#wx.richtext.RichTextRange.SetEnd "Permalink to this definition")
Sets the end position.



Parameters
**end** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetRange(self, start, end) -> None:
        """ 

`SetRange`(*self*, *start*, *end*)[¶](#wx.richtext.RichTextRange.SetRange "Permalink to this definition")
Sets the range start and end positions.



Parameters
* **start** (*long*) –
* **end** (*long*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def SetStart(self, start: int) -> None:
        """ 

`SetStart`(*self*, *start*)[¶](#wx.richtext.RichTextRange.SetStart "Permalink to this definition")
Sets the start position.



Parameters
**start** (*long*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def Swap(self) -> None:
        """ 

`Swap`(*self*)[¶](#wx.richtext.RichTextRange.Swap "Permalink to this definition")
Swaps the start and end.




            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def ToInternal(self) -> 'RichTextRange':
        """ 

`ToInternal`(*self*)[¶](#wx.richtext.RichTextRange.ToInternal "Permalink to this definition")
Converts the API-standard range, whose end is one past the last character in the range, to the internal form, which uses the first and last character positions of the range.


In other words, one is subtracted from the end position. (n, n) is the range of a single character.



Return type
 [wx.richtext.RichTextRange](#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __bool__(self) -> None:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.RichTextRange.__bool__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __getitem__(self, idx) -> None:
        """ 

`__getitem__`(*self*, *idx*)[¶](#wx.richtext.RichTextRange.__getitem__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __len__(self) -> None:
        """ 

`__len__`(*self*)[¶](#wx.richtext.RichTextRange.__len__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __nonzero__(self) -> None:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.RichTextRange.__nonzero__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __reduce__(self) -> None:
        """ 

`__reduce__`(*self*)[¶](#wx.richtext.RichTextRange.__reduce__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __repr__(self) -> None:
        """ 

`__repr__`(*self*)[¶](#wx.richtext.RichTextRange.__repr__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __setitem__(self, idx, val) -> None:
        """ 

`__setitem__`(*self*, *idx*, *val*)[¶](#wx.richtext.RichTextRange.__setitem__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __str__(self) -> None:
        """ 

`__str__`(*self*)[¶](#wx.richtext.RichTextRange.__str__ "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __ne__(self, item: Any) -> bool:
        """ 

`__ne__`(*self*)[¶](#wx.richtext.RichTextRange.__ne__ "Permalink to this definition")
Inequality operator.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __add__(self) -> None:
        """ 

`__add__`(*self*)[¶](#wx.richtext.RichTextRange.__add__ "Permalink to this definition")
Adds a range to this range.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __sub__(self) -> None:
        """ 

`__sub__`(*self*)[¶](#wx.richtext.RichTextRange.__sub__ "Permalink to this definition")
Subtracts a range from this range.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.RichTextRange.__eq__ "Permalink to this definition")
Equality operator.


Returns `True` if *range* is the same as this range.



Parameters
**range** ([*wx.richtext.RichTextRange*](#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextRange.html
        """

    End: int  # `End`[¶](#wx.richtext.RichTextRange.End "Permalink to this definition")See [`GetEnd`](#wx.richtext.RichTextRange.GetEnd "wx.richtext.RichTextRange.GetEnd") and [`SetEnd`](#wx.richtext.RichTextRange.SetEnd "wx.richtext.RichTextRange.SetEnd")
    Length: int  # `Length`[¶](#wx.richtext.RichTextRange.Length "Permalink to this definition")See [`GetLength`](#wx.richtext.RichTextRange.GetLength "wx.richtext.RichTextRange.GetLength")
    Start: int  # `Start`[¶](#wx.richtext.RichTextRange.Start "Permalink to this definition")See [`GetStart`](#wx.richtext.RichTextRange.GetStart "wx.richtext.RichTextRange.GetStart") and [`SetStart`](#wx.richtext.RichTextRange.SetStart "wx.richtext.RichTextRange.SetStart")



class RichTextParagraphLayoutBox(RichTextCompositeObject):
    """ **Possible constructors**:



```
RichTextParagraphLayoutBox(parent=None)

RichTextParagraphLayoutBox(obj)

```


This class knows how to lay out paragraphs.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraphLayoutBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None)*



Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






---

  



**\_\_init\_\_** *(self, obj)*



Parameters
**obj** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AcceptsFocus(self) -> bool:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.AcceptsFocus "Permalink to this definition")
Returns `True` if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.


For example, containers supporting text, such as a text box object, can accept the focus, but a table can’t (set the focus to individual cells instead).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddImage(self, image, paraStyle=None) -> 'RichTextRange':
        """ 

`AddImage`(*self*, *image*, *paraStyle=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.AddImage "Permalink to this definition")
Convenience function to add an image.



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddParagraph(self, text, paraStyle=None) -> 'RichTextRange':
        """ 

`AddParagraph`(*self*, *text*, *paraStyle=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.AddParagraph "Permalink to this definition")
Convenience function to add a paragraph of text.



Parameters
* **text** (*string*) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def AddParagraphs(self, text, paraStyle=None) -> 'RichTextRange':
        """ 

`AddParagraphs`(*self*, *text*, *paraStyle=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.AddParagraphs "Permalink to this definition")
Adds multiple paragraphs, based on newlines.



Parameters
* **text** (*string*) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ApplyStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> bool:
        """ 

`ApplyStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextParagraphLayoutBox.ApplyStyleSheet "Permalink to this definition")
Apply the style sheet to the buffer, for example if the styles have changed.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Clear "Permalink to this definition")
Clears all the children.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ClearListStyle(self, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ 

`ClearListStyle`(*self*, *range*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO*)[¶](#wx.richtext.RichTextParagraphLayoutBox.ClearListStyle "Permalink to this definition")
Clears the list style from the given range, clearing list-related attributes and applying any named paragraph style associated with each paragraph.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **flags** (*int*) –



Return type
*bool*





See also


[`SetListStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetListStyle "wx.richtext.RichTextParagraphLayoutBox.SetListStyle") , [`PromoteList`](#wx.richtext.RichTextParagraphLayoutBox.PromoteList "wx.richtext.RichTextParagraphLayoutBox.PromoteList") , [`NumberList`](#wx.richtext.RichTextParagraphLayoutBox.NumberList "wx.richtext.RichTextParagraphLayoutBox.NumberList")





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def CollectStyle(self, currentStyle, style, clashingAttr, absentAttr) -> bool:
        """ 

`CollectStyle`(*self*, *currentStyle*, *style*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.RichTextParagraphLayoutBox.CollectStyle "Permalink to this definition")
Combines *style* with *currentStyle* for the purpose of summarising the attributes of a range of content.



Parameters
* **currentStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **clashingAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **absentAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Copy(self, obj: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def CopyFragment(self, range, fragment) -> bool:
        """ 

`CopyFragment`(*self*, *range*, *fragment*)[¶](#wx.richtext.RichTextParagraphLayoutBox.CopyFragment "Permalink to this definition")
Make a copy of the fragment corresponding to the given range, putting it in *fragment*.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **fragment** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`DeleteRange`(*self*, *range*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DeleteRange "Permalink to this definition")
Deletes the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DeleteRangeWithUndo(self, range, ctrl, buffer) -> bool:
        """ 

`DeleteRangeWithUndo`(*self*, *range*, *ctrl*, *buffer*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DeleteRangeWithUndo "Permalink to this definition")
Submits a command to delete this range.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoGetStyle(self, position, style, combineStyles=True) -> bool:
        """ 

`DoGetStyle`(*self*, *position*, *style*, *combineStyles=True*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DoGetStyle "Permalink to this definition")
Implementation helper for GetStyle.


If combineStyles is `True`, combine base, paragraph and context attributes.



Parameters
* **position** (*long*) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **combineStyles** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoInvalidate(self, invalidRange: 'richtext.RichTextRange') -> None:
        """ 

`DoInvalidate`(*self*, *invalidRange*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DoInvalidate "Permalink to this definition")
Do the (in)validation for this object only.



Parameters
**invalidRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DoNumberList(self, range, promotionRange, promoteBy, styleDef, flags=RICHTEXT_SETSTYLE_WITH_UNDO, startFrom=1, specifiedLevel=-1) -> bool:
        """ 

`DoNumberList`(*self*, *range*, *promotionRange*, *promoteBy*, *styleDef*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO*, *startFrom=1*, *specifiedLevel=-1*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DoNumberList "Permalink to this definition")
Helper for NumberList and PromoteList, that does renumbering and promotion simultaneously *def* can be NULL/empty to indicate that the existing list style should be used.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **promotionRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **promoteBy** (*int*) –
* **styleDef** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def DrawFloats(self, dc, context, range, selection, rect, descent, style) -> None:
        """ 

`DrawFloats`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.DrawFloats "Permalink to this definition")
Draws the floating objects in this buffer.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def FindNextParagraphNumber(self, previousParagraph, attr) -> bool:
        """ 

`FindNextParagraphNumber`(*self*, *previousParagraph*, *attr*)[¶](#wx.richtext.RichTextParagraphLayoutBox.FindNextParagraphNumber "Permalink to this definition")
Fills in the attributes for numbering a paragraph after previousParagraph.



Parameters
* **previousParagraph** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetBasicStyle(self) -> 'RichTextAttr':
        """ 

`GetBasicStyle`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetBasicStyle "Permalink to this definition")
Returns the basic (overall) style.


This is the style of the whole buffer before further styles are applied, unlike the default style, which only affects the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetDefaultStyle(self) -> 'RichTextAttr':
        """ 

`GetDefaultStyle`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetDefaultStyle "Permalink to this definition")
Returns the current default style, affecting the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatCollector(self) -> 'RichTextFloatCollector':
        """ 

`GetFloatCollector`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetFloatCollector "Permalink to this definition")
Returns the RichTextFloatCollector of this object.



Return type
*RichTextFloatCollector*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatingObjectCount(self) -> int:
        """ 

`GetFloatingObjectCount`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetFloatingObjectCount "Permalink to this definition")
Returns the number of floating objects at this level.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetFloatingObjects(self, objects: RichTextObjectList) -> bool:
        """ 

`GetFloatingObjects`(*self*, *objects*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetFloatingObjects "Permalink to this definition")
Returns a list of floating objects.



Parameters
**objects** (*RichTextObjectList*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetInvalidRange(self, wholeParagraphs: bool=False) -> 'RichTextRange':
        """ 

`GetInvalidRange`(*self*, *wholeParagraphs=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetInvalidRange "Permalink to this definition")
Get invalid range, rounding to entire paragraphs if argument is `True`.



Parameters
**wholeParagraphs** (*bool*) – 



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLeafObjectAtPosition(self, position: int) -> 'RichTextObject':
        """ 

`GetLeafObjectAtPosition`(*self*, *position*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLeafObjectAtPosition "Permalink to this definition")
Returns the leaf object in a paragraph at this position.



Parameters
**position** (*long*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineAtPosition(self, pos, caretPosition=False) -> 'RichTextLine':
        """ 

`GetLineAtPosition`(*self*, *pos*, *caretPosition=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLineAtPosition "Permalink to this definition")
Returns the line at the given position.


If *caretPosition* is `True`, the position is a caret position, which is normally a smaller number.



Parameters
* **pos** (*long*) –
* **caretPosition** (*bool*) –



Return type
 [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineAtYPosition(self, y: int) -> 'RichTextLine':
        """ 

`GetLineAtYPosition`(*self*, *y*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLineAtYPosition "Permalink to this definition")
Returns the line at the given y pixel position, or the last line.



Parameters
**y** (*int*) – 



Return type
 [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineCount(self) -> int:
        """ 

`GetLineCount`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLineCount "Permalink to this definition")
Returns the number of visible lines.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineForVisibleLineNumber(self, lineNumber: int) -> 'RichTextLine':
        """ 

`GetLineForVisibleLineNumber`(*self*, *lineNumber*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLineForVisibleLineNumber "Permalink to this definition")
Given a line number, returns the corresponding  [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline) object.



Parameters
**lineNumber** (*long*) – 



Return type
 [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetLineSizeAtPosition(self, pos, caretPosition=False) -> 'Size':
        """ 

`GetLineSizeAtPosition`(*self*, *pos*, *caretPosition=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetLineSizeAtPosition "Permalink to this definition")
Returns the line size at the given position.



Parameters
* **pos** (*long*) –
* **caretPosition** (*bool*) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphAtLine(self, paragraphNumber: int) -> 'RichTextParagraph':
        """ 

`GetParagraphAtLine`(*self*, *paragraphNumber*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphAtLine "Permalink to this definition")
Returns the paragraph by number.



Parameters
**paragraphNumber** (*long*) – 



Return type
 [wx.richtext.RichTextParagraph](wx.richtext.RichTextParagraph.html#wx-richtext-richtextparagraph)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphAtPosition(self, pos, caretPosition=False) -> 'RichTextParagraph':
        """ 

`GetParagraphAtPosition`(*self*, *pos*, *caretPosition=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphAtPosition "Permalink to this definition")
Returns the paragraph at the given character or caret position.



Parameters
* **pos** (*long*) –
* **caretPosition** (*bool*) –



Return type
 [wx.richtext.RichTextParagraph](wx.richtext.RichTextParagraph.html#wx-richtext-richtextparagraph)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphCount(self) -> int:
        """ 

`GetParagraphCount`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphCount "Permalink to this definition")
Returns the number of paragraphs.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphForLine(self, line: 'richtext.RichTextLine') -> 'RichTextParagraph':
        """ 

`GetParagraphForLine`(*self*, *line*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphForLine "Permalink to this definition")
Returns the paragraph for a given line.



Parameters
**line** ([*wx.richtext.RichTextLine*](wx.richtext.RichTextLine.html#wx.richtext.RichTextLine "wx.richtext.RichTextLine")) – 



Return type
 [wx.richtext.RichTextParagraph](wx.richtext.RichTextParagraph.html#wx-richtext-richtextparagraph)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphLength(self, paragraphNumber: int) -> int:
        """ 

`GetParagraphLength`(*self*, *paragraphNumber*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphLength "Permalink to this definition")
Returns the length of the paragraph.



Parameters
**paragraphNumber** (*long*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetParagraphText(self, paragraphNumber: int) -> str:
        """ 

`GetParagraphText`(*self*, *paragraphNumber*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphText "Permalink to this definition")
Returns the text of the paragraph.



Parameters
**paragraphNumber** (*long*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetPartialParagraph(self) -> bool:
        """ 

`GetPartialParagraph`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetPartialParagraph "Permalink to this definition")
Returns a flag indicating whether the last paragraph is partial or complete.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ 

`GetRichTextCtrl`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetRichTextCtrl "Permalink to this definition")
Returns the associated control.



Return type
 [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyle(self, position, style) -> bool:
        """ 

`GetStyle`(*self*, *position*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetStyle "Permalink to this definition")
Returns the combined text attributes for this position.


This function gets the *uncombined* style - that is, the attributes associated with the paragraph or character content, and not necessarily the combined attributes you see on the screen. To get the combined attributes, use [`GetStyle`](#wx.richtext.RichTextParagraphLayoutBox.GetStyle "wx.richtext.RichTextParagraphLayoutBox.GetStyle") . If you specify (any) paragraph attribute in *style’s* flags, this function will fetch the paragraph attributes. Otherwise, it will return the character attributes.



Parameters
* **position** (*long*) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleForNewParagraph(self, buffer, pos, caretPosition=False, lookUpNewParaStyle=False) -> 'RichTextAttr':
        """ 

`GetStyleForNewParagraph`(*self*, *buffer*, *pos*, *caretPosition=False*, *lookUpNewParaStyle=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetStyleForNewParagraph "Permalink to this definition")
Returns the style that is appropriate for a new paragraph at this position.


If the previous paragraph has a paragraph style name, looks up the next-paragraph style.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **caretPosition** (*bool*) –
* **lookUpNewParaStyle** (*bool*) –



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleForRange(self, range, style) -> bool:
        """ 

`GetStyleForRange`(*self*, *range*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetStyleForRange "Permalink to this definition")
This function gets a style representing the common, combined attributes in the given range.


Attributes which have different values within the specified range will not be included the style flags.


The function is used to get the attributes to display in the formatting dialog: the user can edit the attributes common to the selection, and optionally specify the values of further attributes to be applied uniformly.


To apply the edited attributes, you can use [`SetStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetStyle "wx.richtext.RichTextParagraphLayoutBox.SetStyle") specifying the `wx.richtext.RICHTEXT_SETSTYLE_OPTIMIZE` flag, which will only apply attributes that are different from the *combined* attributes within the range. So, the user edits the effective, displayed attributes for the range, but his choice won’t be applied unnecessarily to content. As an example, say the style for a paragraph specifies bold, but the paragraph text doesn’t specify a weight. The combined style is bold, and this is what the user will see on-screen and in the formatting dialog. The user now specifies red text, in addition to bold. When applying with [`SetStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetStyle "wx.richtext.RichTextParagraphLayoutBox.SetStyle") , the content font weight attributes won’t be changed to bold because this is already specified by the paragraph. However the text colour attributes *will* be changed to show red.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetStyleSheet "Permalink to this definition")
Returns the style sheet associated with the overall buffer.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetText "Permalink to this definition")
Get all the text.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ 

`GetTextForRange`(*self*, *range*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetTextForRange "Permalink to this definition")
Returns any text in this object for the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetUncombinedStyle(self, position, style) -> bool:
        """ 

`GetUncombinedStyle`(*self*, *position*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetUncombinedStyle "Permalink to this definition")
Returns the content (uncombined) attributes for this position.



Parameters
* **position** (*long*) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetVisibleLineNumber(self, pos, caretPosition=False, startOfLine=False) -> int:
        """ 

`GetVisibleLineNumber`(*self*, *pos*, *caretPosition=False*, *startOfLine=False*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetVisibleLineNumber "Permalink to this definition")
Given a position, returns the number of the visible line (potentially many to a paragraph), starting from zero at the start of the buffer.


We also have to pass a bool (*startOfLine*) that indicates whether the caret is being shown at the end of the previous line or at the start of the next, since the caret can be shown at two visible positions for the same underlying position.



Parameters
* **pos** (*long*) –
* **caretPosition** (*bool*) –
* **startOfLine** (*bool*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HasCharacterAttributes(self, range, style) -> bool:
        """ 

`HasCharacterAttributes`(*self*, *range*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.HasCharacterAttributes "Permalink to this definition")
Test if this whole range has character attributes of the specified kind.


If any of the attributes are different within the range, the test fails. You can use this to implement, for example, bold button updating. style must have flags indicating which attributes are of interest.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HasParagraphAttributes(self, range, style) -> bool:
        """ 

`HasParagraphAttributes`(*self*, *range*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.HasParagraphAttributes "Permalink to this definition")
Test if this whole range has paragraph attributes of the specified kind.


If any of the attributes are different within the range, the test fails. You can use this to implement, for example, centering button updating. style must have flags indicating which attributes are of interest.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextParagraphLayoutBox.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ 

`ImportFromXML`(*self*, *buffer*, *node*, *handler*, *recurse*)[¶](#wx.richtext.RichTextParagraphLayoutBox.ImportFromXML "Permalink to this definition")
Imports this object from `XML`.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **handler** ([*wx.richtext.RichTextXMLHandler*](wx.richtext.RichTextXMLHandler.html#wx.richtext.RichTextXMLHandler "wx.richtext.RichTextXMLHandler")) –
* **recurse** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Init "Permalink to this definition")
Initializes the object.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertFieldWithUndo(self, buffer, pos, fieldType, properties, ctrl, flags, textAttr) -> 'RichTextField':
        """ 

`InsertFieldWithUndo`(*self*, *buffer*, *pos*, *fieldType*, *properties*, *ctrl*, *flags*, *textAttr*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertFieldWithUndo "Permalink to this definition")
Submits a command to insert the given field.


Field data can be included in properties.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **fieldType** (*string*) –
* **properties** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
 [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield)





See also


 [wx.richtext.RichTextField](wx.richtext.RichTextField.html#wx-richtext-richtextfield),  [wx.richtext.RichTextFieldType](wx.richtext.RichTextFieldType.html#wx-richtext-richtextfieldtype),  [wx.richtext.RichTextFieldTypeStandard](wx.richtext.RichTextFieldTypeStandard.html#wx-richtext-richtextfieldtypestandard)





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertFragment(self, position, fragment) -> bool:
        """ 

`InsertFragment`(*self*, *position*, *fragment*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertFragment "Permalink to this definition")
Insert fragment into this box at the given position.


If partialParagraph is `True`, it is assumed that the last (or only) paragraph is just a piece of data with no paragraph marker.



Parameters
* **position** (*long*) –
* **fragment** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertImageWithUndo(self, buffer, pos, imageBlock, ctrl, flags, textAttr) -> bool:
        """ 

`InsertImageWithUndo`(*self*, *buffer*, *pos*, *imageBlock*, *ctrl*, *flags*, *textAttr*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertImageWithUndo "Permalink to this definition")
Submits a command to insert the given image.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **imageBlock** ([*wx.richtext.RichTextImageBlock*](wx.richtext.RichTextImageBlock.html#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertNewlineWithUndo(self, buffer, pos, ctrl, flags=0) -> bool:
        """ 

`InsertNewlineWithUndo`(*self*, *buffer*, *pos*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertNewlineWithUndo "Permalink to this definition")
Submits a command to insert the given text.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertObjectWithUndo(self, buffer, pos, object, ctrl, flags=0) -> 'RichTextObject':
        """ 

`InsertObjectWithUndo`(*self*, *buffer*, *pos*, *object*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertObjectWithUndo "Permalink to this definition")
Inserts an object.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **object** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertParagraphsWithUndo(self, buffer, pos, paragraphs, ctrl, flags=0) -> bool:
        """ 

`InsertParagraphsWithUndo`(*self*, *buffer*, *pos*, *paragraphs*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertParagraphsWithUndo "Permalink to this definition")
Submits a command to insert paragraphs.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **paragraphs** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InsertTextWithUndo(self, buffer, pos, text, ctrl, flags=0) -> bool:
        """ 

`InsertTextWithUndo`(*self*, *buffer*, *pos*, *text*, *ctrl*, *flags=0*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InsertTextWithUndo "Permalink to this definition")
Submits a command to insert the given text.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **pos** (*long*) –
* **text** (*string*) –
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ 

`Invalidate`(*self*, *invalidRange=RICHTEXT\_ALL*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Invalidate "Permalink to this definition")
Invalidates the buffer.


With no argument, invalidates whole buffer.



Parameters
**invalidRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def InvalidateHierarchy(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ 

`InvalidateHierarchy`(*self*, *invalidRange=RICHTEXT\_ALL*)[¶](#wx.richtext.RichTextParagraphLayoutBox.InvalidateHierarchy "Permalink to this definition")
Do the (in)validation both up and down the hierarchy.



Parameters
**invalidRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def IsDirty(self) -> bool:
        """ 

`IsDirty`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.IsDirty "Permalink to this definition")
Returns `True` if this object needs layout.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def IsTopLevel(self) -> bool:
        """ 

`IsTopLevel`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.IsTopLevel "Permalink to this definition")
Returns `True` if this object is top-level, i.e. contains its own paragraphs, such as a text box.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def MoveAnchoredObjectToParagraph(self, from_, to_, obj) -> None:
        """ 

`MoveAnchoredObjectToParagraph`(*self*, *from\_*, *to\_*, *obj*)[¶](#wx.richtext.RichTextParagraphLayoutBox.MoveAnchoredObjectToParagraph "Permalink to this definition")
Moves an anchored object to another paragraph.



Parameters
* **from\_** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **to\_** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def NumberList(self, *args, **kw) -> bool:
        """ 

`NumberList`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraphLayoutBox.NumberList "Permalink to this definition")
Numbers the paragraphs in the given range.


Pass flags to determine how the attributes are set. Either the style definition or the name of the style definition (in the current sheet) can be passed.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.


*def* can be `None` to indicate that the existing list style should be used.



See also


[`SetListStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetListStyle "wx.richtext.RichTextParagraphLayoutBox.SetListStyle") , [`PromoteList`](#wx.richtext.RichTextParagraphLayoutBox.PromoteList "wx.richtext.RichTextParagraphLayoutBox.PromoteList") , [`ClearListStyle`](#wx.richtext.RichTextParagraphLayoutBox.ClearListStyle "wx.richtext.RichTextParagraphLayoutBox.ClearListStyle")



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**NumberList** *(self, range, def=None, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **def** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**NumberList** *(self, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PositionToXY(self, pos, x, y) -> bool:
        """ 

`PositionToXY`(*self*, *pos*, *x*, *y*)[¶](#wx.richtext.RichTextParagraphLayoutBox.PositionToXY "Permalink to this definition")
Converts a zero-based position to line column and paragraph number.



Parameters
* **pos** (*long*) –
* **x** (*long*) –
* **y** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PrepareContent(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`PrepareContent`(*self*, *container*)[¶](#wx.richtext.RichTextParagraphLayoutBox.PrepareContent "Permalink to this definition")
Prepares the content just before insertion (or after buffer reset).


Currently is only called if undo mode is on.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def PromoteList(self, *args, **kw) -> bool:
        """ 

`PromoteList`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraphLayoutBox.PromoteList "Permalink to this definition")
Promotes the list items within the given range.


A positive *promoteBy* produces a smaller indent, and a negative number produces a larger indent. Pass flags to determine how the attributes are set. Either the style definition or the name of the style definition (in the current sheet) can be passed.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.



See also


[`SetListStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetListStyle "wx.richtext.RichTextParagraphLayoutBox.SetListStyle") , [`SetListStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetListStyle "wx.richtext.RichTextParagraphLayoutBox.SetListStyle") , [`ClearListStyle`](#wx.richtext.RichTextParagraphLayoutBox.ClearListStyle "wx.richtext.RichTextParagraphLayoutBox.ClearListStyle")



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**PromoteList** *(self, promoteBy, range, def=None, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, specifiedLevel=-1)*



Parameters
* **promoteBy** (*int*) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **def** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**PromoteList** *(self, promoteBy, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, specifiedLevel=-1)*



Parameters
* **promoteBy** (*int*) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.Reset "Permalink to this definition")
Clears and initializes with one blank paragraph.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetBasicStyle(self, style: 'richtext.RichTextAttr') -> None:
        """ 

`SetBasicStyle`(*self*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetBasicStyle "Permalink to this definition")
Sets the basic (overall) style.


This is the style of the whole buffer before further styles are applied, unlike the default style, which only affects the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetDefaultStyle(self, style: 'richtext.RichTextAttr') -> bool:
        """ 

`SetDefaultStyle`(*self*, *style*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetDefaultStyle "Permalink to this definition")
Sets the default style, affecting the style currently being applied (for example, setting the default style to bold will cause subsequently inserted text to be bold).


This is not cumulative - setting the default style will replace the previous default style.


Setting it to a default attribute object makes new content take on the ‘basic’ style.



Parameters
**style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetListStyle(self, *args, **kw) -> bool:
        """ 

`SetListStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetListStyle "Permalink to this definition")
Sets the list attributes for the given range, passing flags to determine how the attributes are set.


Either the style definition or the name of the style definition (in the current sheet) can be passed.


*flags* is a bit list of the following:


* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this command will be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_RENUMBER`: specifies that numbering should start from *startFrom*, otherwise existing attributes are used.
* `wx.richtext.RICHTEXT_SETSTYLE_SPECIFY_LEVEL`: specifies that *listLevel* should be used as the level for all paragraphs, otherwise the current indentation will be used.



See also


[`NumberList`](#wx.richtext.RichTextParagraphLayoutBox.NumberList "wx.richtext.RichTextParagraphLayoutBox.NumberList") , [`PromoteList`](#wx.richtext.RichTextParagraphLayoutBox.PromoteList "wx.richtext.RichTextParagraphLayoutBox.PromoteList") , [`ClearListStyle`](#wx.richtext.RichTextParagraphLayoutBox.ClearListStyle "wx.richtext.RichTextParagraphLayoutBox.ClearListStyle") .



[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetListStyle** *(self, range, styleDef, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **styleDef** ([*wx.richtext.RichTextListStyleDefinition*](wx.richtext.RichTextListStyleDefinition.html#wx.richtext.RichTextListStyleDefinition "wx.richtext.RichTextListStyleDefinition")) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  



**SetListStyle** *(self, range, defName, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO, startFrom=1, specifiedLevel=-1)*



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **defName** (*string*) –
* **flags** (*int*) –
* **startFrom** (*int*) –
* **specifiedLevel** (*int*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetObjectPropertiesWithUndo(self, obj, properties, objToSet=None) -> bool:
        """ 

`SetObjectPropertiesWithUndo`(*self*, *obj*, *properties*, *objToSet=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetObjectPropertiesWithUndo "Permalink to this definition")
Sets with undo the properties for the given object.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **properties** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) –
* **objToSet** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetPartialParagraph(self, partialPara: bool) -> None:
        """ 

`SetPartialParagraph`(*self*, *partialPara*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetPartialParagraph "Permalink to this definition")
Sets a flag indicating whether the last paragraph is partial or complete.



Parameters
**partialPara** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetProperties(self, range, properties, flags=RICHTEXT_SETPROPERTIES_WITH_UNDO) -> bool:
        """ 

`SetProperties`(*self*, *range*, *properties*, *flags=RICHTEXT\_SETPROPERTIES\_WITH\_UNDO*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetProperties "Permalink to this definition")
Sets the properties for the given range, passing flags to determine how the attributes are set.


You can merge properties or replace them.


The end point of range is specified as the last character position of the span of text, plus one. So, for example, to set the properties for a character at position 5, use the range (5,6).


*flags* may contain a bit list of the following values:


* `wx.richtext.RICHTEXT_SETPROPERTIES_NONE`: no flag.
* `wx.richtext.RICHTEXT_SETPROPERTIES_WITH_UNDO`: specifies that this operation should be undoable.
* `wx.richtext.RICHTEXT_SETPROPERTIES_PARAGRAPHS_ONLY`: specifies that the properties should only be applied to paragraphs, and not the content.
* `wx.richtext.RICHTEXT_SETPROPERTIES_CHARACTERS_ONLY`: specifies that the properties should only be applied to characters, and not the paragraph.
* `wx.richtext.RICHTEXT_SETPROPERTIES_RESET`: resets (clears) the existing properties before applying the new properties.
* `wx.richtext.RICHTEXT_SETPROPERTIES_REMOVE`: removes the specified properties.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **properties** ([*wx.richtext.RichTextProperties*](wx.richtext.RichTextProperties.html#wx.richtext.RichTextProperties "wx.richtext.RichTextProperties")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ 

`SetRichTextCtrl`(*self*, *ctrl*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetRichTextCtrl "Permalink to this definition")
Associates a control with the buffer, for operations that for example require refreshing the window.



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def SetStyle(self, *args, **kw) -> bool:
        """ 

`SetStyle`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraphLayoutBox.SetStyle "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetStyle** *(self, range, style, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO)*


Sets the attributes for the given range.


Pass flags to determine how the attributes are set.


The end point of range is specified as the last character position of the span of text. So, for example, to set the style for a character at position 5, use the range (5,5). This differs from the  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl) API, where you would specify (5,6).


*flags* may contain a bit list of the following values:


* `wx.richtext.RICHTEXT_SETSTYLE_NONE`: no style flag.
* `wx.richtext.RICHTEXT_SETSTYLE_WITH_UNDO`: specifies that this operation should be undoable.
* `wx.richtext.RICHTEXT_SETSTYLE_OPTIMIZE`: specifies that the style should not be applied if the combined style at this point is already the style in question.
* `wx.richtext.RICHTEXT_SETSTYLE_PARAGRAPHS_ONLY`: specifies that the style should only be applied to paragraphs, and not the content. This allows content styling to be preserved independently from that of e.g. a named paragraph style.
* `wx.richtext.RICHTEXT_SETSTYLE_CHARACTERS_ONLY`: specifies that the style should only be applied to characters, and not the paragraph. This allows content styling to be preserved independently from that of e.g. a named paragraph style.
* `wx.richtext.RICHTEXT_SETSTYLE_RESET`: resets (clears) the existing style before applying the new style.
* `wx.richtext.RICHTEXT_SETSTYLE_REMOVE`: removes the specified style. Only the style flags are used in this operation.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **flags** (*int*) –



Return type
*bool*






---

  



**SetStyle** *(self, obj, textAttr, flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO)*


Sets the attributes for the given object only, for example the box attributes for a text box.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **textAttr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **flags** (*int*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def UpdateFloatingObjects(self, availableRect, untilObj=None) -> bool:
        """ 

`UpdateFloatingObjects`(*self*, *availableRect*, *untilObj=None*)[¶](#wx.richtext.RichTextParagraphLayoutBox.UpdateFloatingObjects "Permalink to this definition")
Gather information about floating objects.


If untilObj is not `None`, will stop getting information if the current object is this, since we will collect the rest later.



Parameters
* **availableRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **untilObj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def UpdateRanges(self) -> None:
        """ 

`UpdateRanges`(*self*)[¶](#wx.richtext.RichTextParagraphLayoutBox.UpdateRanges "Permalink to this definition")
Calculate ranges.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    def XYToPosition(self, x, y) -> int:
        """ 

`XYToPosition`(*self*, *x*, *y*)[¶](#wx.richtext.RichTextParagraphLayoutBox.XYToPosition "Permalink to this definition")
Converts zero-based line column and paragraph number to a position.



Parameters
* **x** (*long*) –
* **y** (*long*) –



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphLayoutBox.html
        """

    BasicStyle: 'RichTextAttr'  # `BasicStyle`[¶](#wx.richtext.RichTextParagraphLayoutBox.BasicStyle "Permalink to this definition")See [`GetBasicStyle`](#wx.richtext.RichTextParagraphLayoutBox.GetBasicStyle "wx.richtext.RichTextParagraphLayoutBox.GetBasicStyle") and [`SetBasicStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetBasicStyle "wx.richtext.RichTextParagraphLayoutBox.SetBasicStyle")
    DefaultStyle: 'RichTextAttr'  # `DefaultStyle`[¶](#wx.richtext.RichTextParagraphLayoutBox.DefaultStyle "Permalink to this definition")See [`GetDefaultStyle`](#wx.richtext.RichTextParagraphLayoutBox.GetDefaultStyle "wx.richtext.RichTextParagraphLayoutBox.GetDefaultStyle") and [`SetDefaultStyle`](#wx.richtext.RichTextParagraphLayoutBox.SetDefaultStyle "wx.richtext.RichTextParagraphLayoutBox.SetDefaultStyle")
    FloatCollector: 'RichTextFloatCollector'  # `FloatCollector`[¶](#wx.richtext.RichTextParagraphLayoutBox.FloatCollector "Permalink to this definition")See [`GetFloatCollector`](#wx.richtext.RichTextParagraphLayoutBox.GetFloatCollector "wx.richtext.RichTextParagraphLayoutBox.GetFloatCollector")
    FloatingObjectCount: int  # `FloatingObjectCount`[¶](#wx.richtext.RichTextParagraphLayoutBox.FloatingObjectCount "Permalink to this definition")See [`GetFloatingObjectCount`](#wx.richtext.RichTextParagraphLayoutBox.GetFloatingObjectCount "wx.richtext.RichTextParagraphLayoutBox.GetFloatingObjectCount")
    InvalidRange: 'RichTextRange'  # `InvalidRange`[¶](#wx.richtext.RichTextParagraphLayoutBox.InvalidRange "Permalink to this definition")See [`GetInvalidRange`](#wx.richtext.RichTextParagraphLayoutBox.GetInvalidRange "wx.richtext.RichTextParagraphLayoutBox.GetInvalidRange")
    LineCount: int  # `LineCount`[¶](#wx.richtext.RichTextParagraphLayoutBox.LineCount "Permalink to this definition")See [`GetLineCount`](#wx.richtext.RichTextParagraphLayoutBox.GetLineCount "wx.richtext.RichTextParagraphLayoutBox.GetLineCount")
    ParagraphCount: int  # `ParagraphCount`[¶](#wx.richtext.RichTextParagraphLayoutBox.ParagraphCount "Permalink to this definition")See [`GetParagraphCount`](#wx.richtext.RichTextParagraphLayoutBox.GetParagraphCount "wx.richtext.RichTextParagraphLayoutBox.GetParagraphCount")
    PartialParagraph: bool  # `PartialParagraph`[¶](#wx.richtext.RichTextParagraphLayoutBox.PartialParagraph "Permalink to this definition")See [`GetPartialParagraph`](#wx.richtext.RichTextParagraphLayoutBox.GetPartialParagraph "wx.richtext.RichTextParagraphLayoutBox.GetPartialParagraph") and [`SetPartialParagraph`](#wx.richtext.RichTextParagraphLayoutBox.SetPartialParagraph "wx.richtext.RichTextParagraphLayoutBox.SetPartialParagraph")
    RichTextCtrl: 'RichTextCtrl'  # `RichTextCtrl`[¶](#wx.richtext.RichTextParagraphLayoutBox.RichTextCtrl "Permalink to this definition")See [`GetRichTextCtrl`](#wx.richtext.RichTextParagraphLayoutBox.GetRichTextCtrl "wx.richtext.RichTextParagraphLayoutBox.GetRichTextCtrl") and [`SetRichTextCtrl`](#wx.richtext.RichTextParagraphLayoutBox.SetRichTextCtrl "wx.richtext.RichTextParagraphLayoutBox.SetRichTextCtrl")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextParagraphLayoutBox.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextParagraphLayoutBox.GetStyleSheet "wx.richtext.RichTextParagraphLayoutBox.GetStyleSheet")
    Text: str  # `Text`[¶](#wx.richtext.RichTextParagraphLayoutBox.Text "Permalink to this definition")See [`GetText`](#wx.richtext.RichTextParagraphLayoutBox.GetText "wx.richtext.RichTextParagraphLayoutBox.GetText")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextParagraphLayoutBox.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextParagraphLayoutBox.GetXMLNodeName "wx.richtext.RichTextParagraphLayoutBox.GetXMLNodeName")



RICHTEXT_SETPROPERTIES_NONE: int

class RichTextTable(RichTextBox):
    """ **Possible constructors**:



```
RichTextTable(parent=None)

RichTextTable(obj)

```


RichTextTable represents a table with arbitrary columns and rows.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextTable.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None)*


Default constructor; optionally pass the parent object.



Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextTable*](#wx.richtext.RichTextTable "wx.richtext.RichTextTable")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AcceptsFocus(self) -> bool:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.richtext.RichTextTable.AcceptsFocus "Permalink to this definition")
Returns `True` if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.


For example, containers supporting text, such as a text box object, can accept the focus, but a table can’t (set the focus to individual cells instead).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AddColumns(*args, **kwargs) -> bool:
        """ 

`AddColumns`(*self*, *startCol*, *noCols=1*, *attr=RichTextAttr()*)[¶](#wx.richtext.RichTextTable.AddColumns "Permalink to this definition")
Adds columns from the given column position.



Parameters
* **startCol** (*int*) –
* **noCols** (*int*) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def AddRows(*args, **kwargs) -> bool:
        """ 

`AddRows`(*self*, *startRow*, *noRows=1*, *attr=RichTextAttr()*)[¶](#wx.richtext.RichTextTable.AddRows "Permalink to this definition")
Adds rows from the given row position.



Parameters
* **startRow** (*int*) –
* **noRows** (*int*) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextTable.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextTable.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def ClearTable(self) -> None:
        """ 

`ClearTable`(*self*)[¶](#wx.richtext.RichTextTable.ClearTable "Permalink to this definition")
Clears the table.




            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextTable.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Copy(self, obj: 'richtext.RichTextTable') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextTable.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextTable*](#wx.richtext.RichTextTable "wx.richtext.RichTextTable")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def CreateTable(self, rows, cols) -> bool:
        """ 

`CreateTable`(*self*, *rows*, *cols*)[¶](#wx.richtext.RichTextTable.CreateTable "Permalink to this definition")
Creates a table of the given dimensions.



Parameters
* **rows** (*int*) –
* **cols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteColumns(self, startCol, noCols=1) -> bool:
        """ 

`DeleteColumns`(*self*, *startCol*, *noCols=1*)[¶](#wx.richtext.RichTextTable.DeleteColumns "Permalink to this definition")
Deletes columns from the given column position.



Parameters
* **startCol** (*int*) –
* **noCols** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`DeleteRange`(*self*, *range*)[¶](#wx.richtext.RichTextTable.DeleteRange "Permalink to this definition")
Deletes the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def DeleteRows(self, startRow, noRows=1) -> bool:
        """ 

`DeleteRows`(*self*, *startRow*, *noRows=1*)[¶](#wx.richtext.RichTextTable.DeleteRows "Permalink to this definition")
Deletes rows from the given row position.



Parameters
* **startRow** (*int*) –
* **noRows** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextTable.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextTable.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ 

`FindPosition`(*self*, *dc*, *context*, *index*, *forceLineStart*)[¶](#wx.richtext.RichTextTable.FindPosition "Permalink to this definition")
Finds the absolute position and row height for the given character position.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **index** (*long*) –
* **forceLineStart** (*bool*) –



Return type
*tuple*



Returns
( *bool*, *pt*, *height* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCell(self, *args, **kw) -> 'RichTextCell':
        """ 

`GetCell`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextTable.GetCell "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetCell** *(self, row, col)*


Returns the cell at the given row/column position.



Parameters
* **row** (*int*) –
* **col** (*int*) –



Return type
 [wx.richtext.RichTextCell](wx.richtext.RichTextCell.html#wx-richtext-richtextcell)






---

  



**GetCell** *(self, pos)*


Returns the cell at the given character position (in the range of the table).



Parameters
**pos** (*long*) – 



Return type
 [wx.richtext.RichTextCell](wx.richtext.RichTextCell.html#wx-richtext-richtextcell)






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCellRowColumnPosition(self, pos, row, col) -> bool:
        """ 

`GetCellRowColumnPosition`(*self*, *pos*, *row*, *col*)[¶](#wx.richtext.RichTextTable.GetCellRowColumnPosition "Permalink to this definition")
Returns the row/column for a given character position.



Parameters
* **pos** (*long*) –
* **row** (*int*) –
* **col** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetCells(self) -> 'RichTextObjectPtrArrayArray':
        """ 

`GetCells`(*self*)[¶](#wx.richtext.RichTextTable.GetCells "Permalink to this definition")
Returns the cells array.



Return type
*RichTextObjectPtrArrayArray*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetColumnCount(self) -> int:
        """ 

`GetColumnCount`(*self*)[¶](#wx.richtext.RichTextTable.GetColumnCount "Permalink to this definition")
Returns the column count.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetFocusedCell(self) -> 'Position':
        """ 

`GetFocusedCell`(*self*)[¶](#wx.richtext.RichTextTable.GetFocusedCell "Permalink to this definition")
Returns the coordinates of the cell with keyboard focus, or (-1,-1) if none.



Return type
`Position`






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextTable.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextTable.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetRowCount(self) -> int:
        """ 

`GetRowCount`(*self*)[¶](#wx.richtext.RichTextTable.GetRowCount "Permalink to this definition")
Returns the row count.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetSelection(self, start, end) -> 'RichTextSelection':
        """ 

`GetSelection`(*self*, *start*, *end*)[¶](#wx.richtext.RichTextTable.GetSelection "Permalink to this definition")
Returns a selection object specifying the selections between start and end character positions.


For example, a table would deduce what cells (of range length 1) are selected when dragging across the table.



Parameters
* **start** (*long*) –
* **end** (*long*) –



Return type
 [wx.richtext.RichTextSelection](wx.richtext.RichTextSelection.html#wx-richtext-richtextselection)






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ 

`GetTextForRange`(*self*, *range*)[¶](#wx.richtext.RichTextTable.GetTextForRange "Permalink to this definition")
Returns any text in this object for the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextTable.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def HandlesChildSelections(self) -> bool:
        """ 

`HandlesChildSelections`(*self*)[¶](#wx.richtext.RichTextTable.HandlesChildSelections "Permalink to this definition")
Returns `True` if this object can handle the selections of its children, fOr example a table.


Required for composite selection handling to work.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextTable.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ 

`ImportFromXML`(*self*, *buffer*, *node*, *handler*, *recurse*)[¶](#wx.richtext.RichTextTable.ImportFromXML "Permalink to this definition")
Imports this object from `XML`.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **handler** ([*wx.richtext.RichTextXMLHandler*](wx.richtext.RichTextXMLHandler.html#wx.richtext.RichTextXMLHandler "wx.richtext.RichTextXMLHandler")) –
* **recurse** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextTable.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    def SetCellStyle(self, selection, style, flags=RICHTEXT_SETSTYLE_WITH_UNDO) -> bool:
        """ 

`SetCellStyle`(*self*, *selection*, *style*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO*)[¶](#wx.richtext.RichTextTable.SetCellStyle "Permalink to this definition")
Sets the attributes for the cells specified by the selection.



Parameters
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextTable.html
        """

    Cells: 'RichTextObjectPtrArrayArray'  # `Cells`[¶](#wx.richtext.RichTextTable.Cells "Permalink to this definition")See [`GetCells`](#wx.richtext.RichTextTable.GetCells "wx.richtext.RichTextTable.GetCells")
    ColumnCount: int  # `ColumnCount`[¶](#wx.richtext.RichTextTable.ColumnCount "Permalink to this definition")See [`GetColumnCount`](#wx.richtext.RichTextTable.GetColumnCount "wx.richtext.RichTextTable.GetColumnCount")
    FocusedCell: 'Position'  # `FocusedCell`[¶](#wx.richtext.RichTextTable.FocusedCell "Permalink to this definition")See [`GetFocusedCell`](#wx.richtext.RichTextTable.GetFocusedCell "wx.richtext.RichTextTable.GetFocusedCell")
    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextTable.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextTable.GetPropertiesMenuLabel "wx.richtext.RichTextTable.GetPropertiesMenuLabel")
    RowCount: int  # `RowCount`[¶](#wx.richtext.RichTextTable.RowCount "Permalink to this definition")See [`GetRowCount`](#wx.richtext.RichTextTable.GetRowCount "wx.richtext.RichTextTable.GetRowCount")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextTable.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextTable.GetXMLNodeName "wx.richtext.RichTextTable.GetXMLNodeName")



class RichTextContextMenuPropertiesInfo:
    """ **Possible constructors**:



```
RichTextContextMenuPropertiesInfo()

```


RichTextContextMenuPropertiesInfo keeps track of objects that appear
in the context menu, whose properties are available to be edited.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.__init__ "Permalink to this definition")
Constructor.




            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddItem(self, label, obj) -> bool:
        """ 

`AddItem`(*self*, *label*, *obj*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.AddItem "Permalink to this definition")
Adds an item.



Parameters
* **label** (*string*) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddItems(self, ctrl, container, obj) -> int:
        """ 

`AddItems`(*self*, *ctrl*, *container*, *obj*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.AddItems "Permalink to this definition")
Adds appropriate menu items for the current container and clicked on object (and container’s parent, if appropriate).



Parameters
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **container** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def AddMenuItems(self, menu, startCmd=ID_RICHTEXT_PROPERTIES1) -> int:
        """ 

`AddMenuItems`(*self*, *menu*, *startCmd=ID\_RICHTEXT\_PROPERTIES1*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.AddMenuItems "Permalink to this definition")
Returns the number of menu items that were added.



Parameters
* **menu** ([*wx.Menu*](wx.Menu.html#wx.Menu "wx.Menu")) –
* **startCmd** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def Clear(self) -> None:
        """ 

`Clear`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.Clear "Permalink to this definition")
Clears the items.




            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.GetCount "Permalink to this definition")
Returns the number of items.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetLabel(self, n: int) -> str:
        """ 

`GetLabel`(*self*, *n*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.GetLabel "Permalink to this definition")
Returns the nth label.



Parameters
**n** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetLabels(self) -> list[str]:
        """ 

`GetLabels`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.GetLabels "Permalink to this definition")
Returns the array of labels.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetObject(self, n: int) -> 'RichTextObject':
        """ 

`GetObject`(*self*, *n*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.GetObject "Permalink to this definition")
Returns the nth object.



Parameters
**n** (*int*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def GetObjects(self) -> 'RichTextObjectPtrArray':
        """ 

`GetObjects`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.GetObjects "Permalink to this definition")
Returns the array of objects.



Return type
*RichTextObjectPtrArray*






            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.Init "Permalink to this definition")
Initialisation.




            Source: https://docs.wxpython.org/wx.richtext.RichTextContextMenuPropertiesInfo.html
        """

    Count: int  # `Count`[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.Count "Permalink to this definition")See [`GetCount`](#wx.richtext.RichTextContextMenuPropertiesInfo.GetCount "wx.richtext.RichTextContextMenuPropertiesInfo.GetCount")
    Labels: list[str]  # `Labels`[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.Labels "Permalink to this definition")See [`GetLabels`](#wx.richtext.RichTextContextMenuPropertiesInfo.GetLabels "wx.richtext.RichTextContextMenuPropertiesInfo.GetLabels")
    Objects: 'RichTextObjectPtrArray'  # `Objects`[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.Objects "Permalink to this definition")See [`GetObjects`](#wx.richtext.RichTextContextMenuPropertiesInfo.GetObjects "wx.richtext.RichTextContextMenuPropertiesInfo.GetObjects")
    m_labels: Any  # `m_labels`[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.m_labels "Permalink to this definition")A public C++ attribute of type `list of strings`.
    m_objects: Any  # `m_objects`[¶](#wx.richtext.RichTextContextMenuPropertiesInfo.m_objects "Permalink to this definition")A public C++ attribute of type `RichTextObjectPtrArray`.



class RichTextSelection:
    """ **Possible constructors**:



```
RichTextSelection(sel)

RichTextSelection(range, container)

RichTextSelection()

```


Stores selection information.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextSelection.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, sel)*


Copy constructor.



Parameters
**sel** ([*wx.richtext.RichTextSelection*](#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) – 






---

  



**\_\_init\_\_** *(self, range, container)*


Creates a selection from a range and a container.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –






---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Add(self, range: 'richtext.RichTextRange') -> None:
        """ 

`Add`(*self*, *range*)[¶](#wx.richtext.RichTextSelection.Add "Permalink to this definition")
Adds a range to the selection.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Copy(self, sel: 'richtext.RichTextSelection') -> None:
        """ 

`Copy`(*self*, *sel*)[¶](#wx.richtext.RichTextSelection.Copy "Permalink to this definition")
Copies from *sel*.



Parameters
**sel** ([*wx.richtext.RichTextSelection*](#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetContainer(self) -> 'RichTextParagraphLayoutBox':
        """ 

`GetContainer`(*self*)[¶](#wx.richtext.RichTextSelection.GetContainer "Permalink to this definition")
Returns the container for which the selection is valid.



Return type
 [wx.richtext.RichTextParagraphLayoutBox](wx.richtext.RichTextParagraphLayoutBox.html#wx-richtext-richtextparagraphlayoutbox)






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetCount(self) -> int:
        """ 

`GetCount`(*self*)[¶](#wx.richtext.RichTextSelection.GetCount "Permalink to this definition")
Returns the number of ranges in the selection.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetRange(self, *args, **kw) -> 'RichTextRange':
        """ 

`GetRange`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextSelection.GetRange "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetRange** *(self, i)*


Returns the range at the given index.



Parameters
**i** (*int*) – 



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






---

  



**GetRange** *(self)*


Returns the first range if there is one, otherwise `wx.richtext.RICHTEXT_NO_SELECTION`.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetRanges(self) -> 'RichTextRangeArray':
        """ 

`GetRanges`(*self*)[¶](#wx.richtext.RichTextSelection.GetRanges "Permalink to this definition")
Returns the selection ranges.



Return type
*RichTextRangeArray*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def GetSelectionForObject(self, obj: 'richtext.RichTextObject') -> 'RichTextRangeArray':
        """ 

`GetSelectionForObject`(*self*, *obj*)[¶](#wx.richtext.RichTextSelection.GetSelectionForObject "Permalink to this definition")
Returns the selection appropriate to the specified object, if any; returns an empty array if none at the level of the object’s container.



Parameters
**obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*RichTextRangeArray*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.RichTextSelection.IsValid "Permalink to this definition")
Returns `True` if the selection is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.RichTextSelection.Reset "Permalink to this definition")
Resets the selection.




            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def Set(self, *args, **kw) -> None:
        """ 

`Set`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextSelection.Set "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**Set** *(self, range, container)*


Sets the selection.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –






---

  



**Set** *(self, ranges, container)*


Sets the selections from an array of ranges and a container object.



Parameters
* **ranges** (*RichTextRangeArray*) –
* **container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetContainer(self, container: 'richtext.RichTextParagraphLayoutBox') -> None:
        """ 

`SetContainer`(*self*, *container*)[¶](#wx.richtext.RichTextSelection.SetContainer "Permalink to this definition")
Sets the container for which the selection is valid.



Parameters
**container** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetRange(self, range: 'richtext.RichTextRange') -> None:
        """ 

`SetRange`(*self*, *range*)[¶](#wx.richtext.RichTextSelection.SetRange "Permalink to this definition")
Sets a single range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def SetRanges(self, ranges: RichTextRangeArray) -> None:
        """ 

`SetRanges`(*self*, *ranges*)[¶](#wx.richtext.RichTextSelection.SetRanges "Permalink to this definition")
Sets the selection ranges.



Parameters
**ranges** (*RichTextRangeArray*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def WithinSelection(self, *args, **kw) -> bool:
        """ 

`WithinSelection`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextSelection.WithinSelection "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**WithinSelection** *(self, pos, obj)*


Returns `True` if the given position is within the selection.



Parameters
* **pos** (*long*) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






---

  



**WithinSelection** *(self, pos)*


Returns `True` if the given position is within the selection.



Parameters
**pos** (*long*) – 



Return type
*bool*






---

  



**WithinSelection** *(pos, ranges)*


Returns `True` if the given position is within the selection range.



Parameters
* **pos** (*long*) –
* **ranges** (*RichTextRangeArray*) –



Return type
*bool*






---

  



**WithinSelection** *(range, ranges)*


Returns `True` if the given range is within the selection range.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **ranges** (*RichTextRangeArray*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.RichTextSelection.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.RichTextSelection.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.RichTextSelection.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**sel** ([*wx.richtext.RichTextSelection*](#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextSelection.html
        """

    Container: 'RichTextParagraphLayoutBox'  # `Container`[¶](#wx.richtext.RichTextSelection.Container "Permalink to this definition")See [`GetContainer`](#wx.richtext.RichTextSelection.GetContainer "wx.richtext.RichTextSelection.GetContainer") and [`SetContainer`](#wx.richtext.RichTextSelection.SetContainer "wx.richtext.RichTextSelection.SetContainer")
    Count: int  # `Count`[¶](#wx.richtext.RichTextSelection.Count "Permalink to this definition")See [`GetCount`](#wx.richtext.RichTextSelection.GetCount "wx.richtext.RichTextSelection.GetCount")
    Range: 'RichTextRange'  # `Range`[¶](#wx.richtext.RichTextSelection.Range "Permalink to this definition")See [`GetRange`](#wx.richtext.RichTextSelection.GetRange "wx.richtext.RichTextSelection.GetRange") and [`SetRange`](#wx.richtext.RichTextSelection.SetRange "wx.richtext.RichTextSelection.SetRange")
    Ranges: 'RichTextRangeArray'  # `Ranges`[¶](#wx.richtext.RichTextSelection.Ranges "Permalink to this definition")See [`GetRanges`](#wx.richtext.RichTextSelection.GetRanges "wx.richtext.RichTextSelection.GetRanges") and [`SetRanges`](#wx.richtext.RichTextSelection.SetRanges "wx.richtext.RichTextSelection.SetRanges")
    m_container: Any  # `m_container`[¶](#wx.richtext.RichTextSelection.m_container "Permalink to this definition")A public C++ attribute of type [`RichTextParagraphLayoutBox`](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox") .
    m_ranges: Any  # `m_ranges`[¶](#wx.richtext.RichTextSelection.m_ranges "Permalink to this definition")A public C++ attribute of type `RichTextRangeArray`.



RICHTEXT_NO_SELECTION: int

class RichTextLine:
    """ **Possible constructors**:



```
RichTextLine(parent)

RichTextLine(obj)

```


This object represents a line in a paragraph, and stores offsets from
the start of the paragraph representing the start and end positions of
the line.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextLine.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent)*



Parameters
**parent** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) – 






---

  



**\_\_init\_\_** *(self, obj)*



Parameters
**obj** ([*wx.richtext.RichTextLine*](#wx.richtext.RichTextLine "wx.richtext.RichTextLine")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Clone(self) -> 'RichTextLine':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextLine.Clone "Permalink to this definition")

Return type
 [wx.richtext.RichTextLine](#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Copy(self, obj: 'richtext.RichTextLine') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextLine.Copy "Permalink to this definition")
Copies from *obj*.



Parameters
**obj** ([*wx.richtext.RichTextLine*](#wx.richtext.RichTextLine "wx.richtext.RichTextLine")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetAbsolutePosition(self) -> 'Point':
        """ 

`GetAbsolutePosition`(*self*)[¶](#wx.richtext.RichTextLine.GetAbsolutePosition "Permalink to this definition")
Returns the absolute object position.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetAbsoluteRange(self) -> 'RichTextRange':
        """ 

`GetAbsoluteRange`(*self*)[¶](#wx.richtext.RichTextLine.GetAbsoluteRange "Permalink to this definition")
Returns the absolute range.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetDescent(self) -> int:
        """ 

`GetDescent`(*self*)[¶](#wx.richtext.RichTextLine.GetDescent "Permalink to this definition")
Returns the stored descent.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetParent(self) -> 'RichTextParagraph':
        """ 

`GetParent`(*self*)[¶](#wx.richtext.RichTextLine.GetParent "Permalink to this definition")
Returns the parent paragraph.



Return type
 [wx.richtext.RichTextParagraph](wx.richtext.RichTextParagraph.html#wx-richtext-richtextparagraph)






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetPosition(self) -> 'Point':
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.RichTextLine.GetPosition "Permalink to this definition")
Returns the object position relative to the parent.



Return type
*Point*






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetRange(self) -> 'RichTextRange':
        """ 

`GetRange`(*self*)[¶](#wx.richtext.RichTextLine.GetRange "Permalink to this definition")
Returns the range.



Return type
 [wx.richtext.RichTextRange](wx.richtext.RichTextRange.html#wx-richtext-richtextrange)






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetRect(self) -> 'Rect':
        """ 

`GetRect`(*self*)[¶](#wx.richtext.RichTextLine.GetRect "Permalink to this definition")
Returns the rectangle enclosing the line.



Return type
[`Rect`](#wx.richtext.RichTextLine.Rect "wx.richtext.RichTextLine.Rect")






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def GetSize(self) -> 'Size':
        """ 

`GetSize`(*self*)[¶](#wx.richtext.RichTextLine.GetSize "Permalink to this definition")
Returns the line size as calculated by Layout.



Return type
[`Size`](#wx.richtext.RichTextLine.Size "wx.richtext.RichTextLine.Size")






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def Init(self, parent: 'richtext.RichTextParagraph') -> None:
        """ 

`Init`(*self*, *parent*)[¶](#wx.richtext.RichTextLine.Init "Permalink to this definition")
Initialises the object.



Parameters
**parent** ([*wx.richtext.RichTextParagraph*](wx.richtext.RichTextParagraph.html#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetDescent(self, descent: int) -> None:
        """ 

`SetDescent`(*self*, *descent*)[¶](#wx.richtext.RichTextLine.SetDescent "Permalink to this definition")
Sets the stored descent.



Parameters
**descent** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetPosition(self, pos: Union[tuple[int, int], 'Point']) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextLine.SetPosition "Permalink to this definition")
Sets the object position relative to the parent.



Parameters
**pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetRange(self, *args, **kw) -> None:
        """ 

`SetRange`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextLine.SetRange "Permalink to this definition")
Sets the range associated with this line.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetRange** *(self, range)*



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






---

  



**SetRange** *(self, from\_, to\_)*



Parameters
* **from\_** (*long*) –
* **to\_** (*long*) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    def SetSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetSize`(*self*, *sz*)[¶](#wx.richtext.RichTextLine.SetSize "Permalink to this definition")
Sets the line size as calculated by Layout.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextLine.html
        """

    AbsolutePosition: 'Point'  # `AbsolutePosition`[¶](#wx.richtext.RichTextLine.AbsolutePosition "Permalink to this definition")See [`GetAbsolutePosition`](#wx.richtext.RichTextLine.GetAbsolutePosition "wx.richtext.RichTextLine.GetAbsolutePosition")
    AbsoluteRange: 'RichTextRange'  # `AbsoluteRange`[¶](#wx.richtext.RichTextLine.AbsoluteRange "Permalink to this definition")See [`GetAbsoluteRange`](#wx.richtext.RichTextLine.GetAbsoluteRange "wx.richtext.RichTextLine.GetAbsoluteRange")
    Descent: int  # `Descent`[¶](#wx.richtext.RichTextLine.Descent "Permalink to this definition")See [`GetDescent`](#wx.richtext.RichTextLine.GetDescent "wx.richtext.RichTextLine.GetDescent") and [`SetDescent`](#wx.richtext.RichTextLine.SetDescent "wx.richtext.RichTextLine.SetDescent")
    Parent: 'RichTextParagraph'  # `Parent`[¶](#wx.richtext.RichTextLine.Parent "Permalink to this definition")See [`GetParent`](#wx.richtext.RichTextLine.GetParent "wx.richtext.RichTextLine.GetParent")
    Position: 'Point'  # `Position`[¶](#wx.richtext.RichTextLine.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.RichTextLine.GetPosition "wx.richtext.RichTextLine.GetPosition") and [`SetPosition`](#wx.richtext.RichTextLine.SetPosition "wx.richtext.RichTextLine.SetPosition")
    Range: 'RichTextRange'  # `Range`[¶](#wx.richtext.RichTextLine.Range "Permalink to this definition")See [`GetRange`](#wx.richtext.RichTextLine.GetRange "wx.richtext.RichTextLine.GetRange") and [`SetRange`](#wx.richtext.RichTextLine.SetRange "wx.richtext.RichTextLine.SetRange")
    Rect: '_Rect'  # `Rect`[¶](#wx.richtext.RichTextLine.Rect "Permalink to this definition")See [`GetRect`](#wx.richtext.RichTextLine.GetRect "wx.richtext.RichTextLine.GetRect")
    Size: '_Size'  # `Size`[¶](#wx.richtext.RichTextLine.Size "Permalink to this definition")See [`GetSize`](#wx.richtext.RichTextLine.GetSize "wx.richtext.RichTextLine.GetSize") and [`SetSize`](#wx.richtext.RichTextLine.SetSize "wx.richtext.RichTextLine.SetSize")



class RichTextListStyleDefinition(RichTextParagraphStyleDefinition):
    """ **Possible constructors**:



```
RichTextListStyleDefinition(name="")

```


This class represents a list style definition, usually added to a
RichTextStyleSheet.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ 

`__init__`(*self*, *name=""*)[¶](#wx.richtext.RichTextListStyleDefinition.__init__ "Permalink to this definition")
Constructor.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def CombineWithParagraphStyle(self, indent, paraStyle, styleSheet=None) -> 'RichTextAttr':
        """ 

`CombineWithParagraphStyle`(*self*, *indent*, *paraStyle*, *styleSheet=None*)[¶](#wx.richtext.RichTextListStyleDefinition.CombineWithParagraphStyle "Permalink to this definition")
This function combines the given paragraph style with the list style’s base attributes and level style matching the given indent, returning the combined attributes.


If *styleSheet* is specified, the base style for this definition will also be included in the result.



Parameters
* **indent** (*int*) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def FindLevelForIndent(self, indent: int) -> int:
        """ 

`FindLevelForIndent`(*self*, *indent*)[¶](#wx.richtext.RichTextListStyleDefinition.FindLevelForIndent "Permalink to this definition")
This function finds the level (from 0 to 9) whose indentation attribute mostly closely matches *indent* (expressed in tenths of a millimetre).



Parameters
**indent** (*int*) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetCombinedStyle(self, indent, styleSheet=None) -> 'RichTextAttr':
        """ 

`GetCombinedStyle`(*self*, *indent*, *styleSheet=None*)[¶](#wx.richtext.RichTextListStyleDefinition.GetCombinedStyle "Permalink to this definition")
This function combines the list style’s base attributes and the level style matching the given indent, returning the combined attributes.


If *styleSheet* is specified, the base style for this definition will also be included in the result.



Parameters
* **indent** (*int*) –
* **styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetCombinedStyleForLevel(self, level, styleSheet=None) -> 'RichTextAttr':
        """ 

`GetCombinedStyleForLevel`(*self*, *level*, *styleSheet=None*)[¶](#wx.richtext.RichTextListStyleDefinition.GetCombinedStyleForLevel "Permalink to this definition")
This function combines the list style’s base attributes and the style for the specified level, returning the combined attributes.


If *styleSheet* is specified, the base style for this definition will also be included in the result.



Parameters
* **level** (*int*) –
* **styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetLevelAttributes(self, level: int) -> 'RichTextAttr':
        """ 

`GetLevelAttributes`(*self*, *level*)[¶](#wx.richtext.RichTextListStyleDefinition.GetLevelAttributes "Permalink to this definition")
Returns the style for the given level.


*level* is a number between 0 and 9.



Parameters
**level** (*int*) – 



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def GetLevelCount(self) -> int:
        """ 

`GetLevelCount`(*self*)[¶](#wx.richtext.RichTextListStyleDefinition.GetLevelCount "Permalink to this definition")
Returns the number of levels.


This is hard-wired to 10. Returns the style for the given level. *level* is a number between 0 and 9.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def IsNumbered(self, level: int) -> bool:
        """ 

`IsNumbered`(*self*, *level*)[¶](#wx.richtext.RichTextListStyleDefinition.IsNumbered "Permalink to this definition")
Returns `True` if the given level has numbered list attributes.



Parameters
**level** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    def SetLevelAttributes(self, level, attr) -> None:
        """ 

`SetLevelAttributes`(*self*, *level*, *attr*)[¶](#wx.richtext.RichTextListStyleDefinition.SetLevelAttributes "Permalink to this definition")
Sets the style for the given level.


*level* is a number between 0 and 9. The first and most flexible form uses a  [wx.TextAttr](wx.TextAttr.html#wx-textattr) object, while the second form is for convenient setting of the most commonly-used attributes.



Parameters
* **level** (*int*) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextListStyleDefinition.html
        """

    LevelCount: int  # `LevelCount`[¶](#wx.richtext.RichTextListStyleDefinition.LevelCount "Permalink to this definition")See [`GetLevelCount`](#wx.richtext.RichTextListStyleDefinition.GetLevelCount "wx.richtext.RichTextListStyleDefinition.GetLevelCount")



class RichTextField(RichTextParagraphLayoutBox):
    """ **Possible constructors**:



```
RichTextField(fieldType="", parent=None)

RichTextField(obj)

```


This class implements the general concept of a field, an object that
represents additional functionality such as a footnote, a bookmark, a
page number, a table of contents, and so on.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextField.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, fieldType=””, parent=None)*


Default constructor; optionally pass the parent object.



Parameters
* **fieldType** (*string*) –
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextField*](#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def AcceptsFocus(self) -> bool:
        """ 

`AcceptsFocus`(*self*)[¶](#wx.richtext.RichTextField.AcceptsFocus "Permalink to this definition")
Returns `True` if objects of this class can accept the focus, i.e. a call to SetFocusObject is possible.


For example, containers supporting text, such as a text box object, can accept the focus, but a table can’t (set the focus to individual cells instead).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextField.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextField.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextField.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Copy(self, obj: 'richtext.RichTextField') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextField.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextField*](#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextField.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextField.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetFieldType(self) -> str:
        """ 

`GetFieldType`(*self*)[¶](#wx.richtext.RichTextField.GetFieldType "Permalink to this definition")

Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextField.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextField.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextField.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsAtomic(self) -> bool:
        """ 

`IsAtomic`(*self*)[¶](#wx.richtext.RichTextField.IsAtomic "Permalink to this definition")
If a field has children, we don’t want the user to be able to edit it.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextField.IsEmpty "Permalink to this definition")
Returns `True` if the buffer is empty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def IsTopLevel(self) -> bool:
        """ 

`IsTopLevel`(*self*)[¶](#wx.richtext.RichTextField.IsTopLevel "Permalink to this definition")
Returns `True` if this object is top-level, i.e. contains its own paragraphs, such as a text box.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextField.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def SetFieldType(self, fieldType: str) -> None:
        """ 

`SetFieldType`(*self*, *fieldType*)[¶](#wx.richtext.RichTextField.SetFieldType "Permalink to this definition")

Parameters
**fieldType** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    def UpdateField(self, buffer: 'richtext.RichTextBuffer') -> bool:
        """ 

`UpdateField`(*self*, *buffer*)[¶](#wx.richtext.RichTextField.UpdateField "Permalink to this definition")
Update the field; delegated to the associated field type.


This would typically expand the field to its value, if this is a dynamically changing and/or composite field.



Parameters
**buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextField.html
        """

    FieldType: str  # `FieldType`[¶](#wx.richtext.RichTextField.FieldType "Permalink to this definition")See [`GetFieldType`](#wx.richtext.RichTextField.GetFieldType "wx.richtext.RichTextField.GetFieldType") and [`SetFieldType`](#wx.richtext.RichTextField.SetFieldType "wx.richtext.RichTextField.SetFieldType")
    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextField.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextField.GetPropertiesMenuLabel "wx.richtext.RichTextField.GetPropertiesMenuLabel")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextField.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextField.GetXMLNodeName "wx.richtext.RichTextField.GetXMLNodeName")



class RichTextFieldTypeStandard(RichTextFieldType):
    """ **Possible constructors**:



```
RichTextFieldTypeStandard(name, label,
                          displayStyle=RICHTEXT_FIELD_STYLE_RECTANGLE)

RichTextFieldTypeStandard(name, bitmap,
                          displayStyle=RICHTEXT_FIELD_STYLE_NO_BORDER)

RichTextFieldTypeStandard()

RichTextFieldTypeStandard(field)

```


A field type that can handle fields with text or bitmap labels, with a
small range of styles for implementing rectangular fields and fields
that can be used for start and end tags.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFieldTypeStandard.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, name, label, displayStyle=RICHTEXT\_FIELD\_STYLE\_RECTANGLE)*


Constructor, creating a field type definition with a text label.



Parameters
* **name** (*string*) – The name of the type definition. This must be unique, and is the type name used when adding a field to a control.
* **label** (*string*) – The text label to be shown on the field.
* **displayStyle** (*int*) – The display style: one of `RICHTEXT_FIELD_STYLE_RECTANGLE`, `RICHTEXT_FIELD_STYLE_NO_BORDER`, `RICHTEXT_FIELD_STYLE_START_TAG`, `RICHTEXT_FIELD_STYLE_END_TAG`.






---

  



**\_\_init\_\_** *(self, name, bitmap, displayStyle=RICHTEXT\_FIELD\_STYLE\_NO\_BORDER)*


Constructor, creating a field type definition with a bitmap label.



Parameters
* **name** (*string*) – The name of the type definition. This must be unique, and is the type name used when adding a field to a control.
* **bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – The bitmap label to be shown on the field.
* **displayStyle** (*int*) – The display style: one of `RICHTEXT_FIELD_STYLE_RECTANGLE`, `RICHTEXT_FIELD_STYLE_NO_BORDER`, `RICHTEXT_FIELD_STYLE_START_TAG`, `RICHTEXT_FIELD_STYLE_END_TAG`.






---

  



**\_\_init\_\_** *(self)*


The default constructor.




---

  



**\_\_init\_\_** *(self, field)*


The copy constructor.



Parameters
**field** ([*wx.richtext.RichTextFieldTypeStandard*](#wx.richtext.RichTextFieldTypeStandard "wx.richtext.RichTextFieldTypeStandard")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Copy(self, field: 'richtext.RichTextFieldTypeStandard') -> None:
        """ 

`Copy`(*self*, *field*)[¶](#wx.richtext.RichTextFieldTypeStandard.Copy "Permalink to this definition")
Copies the object.



Parameters
**field** ([*wx.richtext.RichTextFieldTypeStandard*](#wx.richtext.RichTextFieldTypeStandard "wx.richtext.RichTextFieldTypeStandard")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Draw(self, obj, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *obj*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextFieldTypeStandard.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBackgroundColour(self) -> 'Colour':
        """ 

`GetBackgroundColour`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetBackgroundColour "Permalink to this definition")
Gets the colour used for drawing the field background.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBitmap(self) -> 'Bitmap':
        """ 

`GetBitmap`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetBitmap "Permalink to this definition")
Gets the bitmap label for fields of this type.



Return type
[`Bitmap`](#wx.richtext.RichTextFieldTypeStandard.Bitmap "wx.richtext.RichTextFieldTypeStandard.Bitmap")






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetBorderColour(self) -> 'Colour':
        """ 

`GetBorderColour`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetBorderColour "Permalink to this definition")
Gets the colour used for drawing the field border.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetDisplayStyle(self) -> int:
        """ 

`GetDisplayStyle`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetDisplayStyle "Permalink to this definition")
Gets the display style for fields of this type.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetFont(self) -> 'Font':
        """ 

`GetFont`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetFont "Permalink to this definition")
Gets the font used for drawing the text label.



Return type
[`Font`](#wx.richtext.RichTextFieldTypeStandard.Font "wx.richtext.RichTextFieldTypeStandard.Font")






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetHorizontalMargin(self) -> int:
        """ 

`GetHorizontalMargin`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetHorizontalMargin "Permalink to this definition")
Gets the horizontal margin surrounding the field object.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetHorizontalPadding(self) -> int:
        """ 

`GetHorizontalPadding`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetHorizontalPadding "Permalink to this definition")
Sets the horizontal padding (the distance between the border and the text).



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetLabel(self) -> str:
        """ 

`GetLabel`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetLabel "Permalink to this definition")
Returns the text label for fields of this type.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *obj*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetSize(self, obj, dc, context, style) -> 'Size':
        """ 

`GetSize`(*self*, *obj*, *dc*, *context*, *style*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetSize "Permalink to this definition")
Get the size of the field, given the label, font size, and so on.



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **style** (*int*) –



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetTextColour(self) -> 'Colour':
        """ 

`GetTextColour`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetTextColour "Permalink to this definition")
Gets the colour used for drawing the text label.



Return type
*Colour*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetVerticalMargin(self) -> int:
        """ 

`GetVerticalMargin`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetVerticalMargin "Permalink to this definition")
Gets the vertical margin surrounding the field object.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def GetVerticalPadding(self) -> int:
        """ 

`GetVerticalPadding`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.GetVerticalPadding "Permalink to this definition")
Gets the vertical padding (the distance between the border and the text).



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextFieldTypeStandard.Init "Permalink to this definition")
Initialises the object.




            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def IsTopLevel(self, obj: 'richtext.RichTextField') -> bool:
        """ 

`IsTopLevel`(*self*, *obj*)[¶](#wx.richtext.RichTextFieldTypeStandard.IsTopLevel "Permalink to this definition")
Returns `True` if the display type is `RICHTEXT_FIELD_STYLE_COMPOSITE`, `False` otherwise.



Parameters
**obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def Layout(self, obj, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *obj*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextFieldTypeStandard.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **obj** ([*wx.richtext.RichTextField*](wx.richtext.RichTextField.html#wx.richtext.RichTextField "wx.richtext.RichTextField")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBackgroundColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBackgroundColour`(*self*, *colour*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetBackgroundColour "Permalink to this definition")
Sets the colour used for drawing the field background.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBitmap(self, bitmap: 'Bitmap') -> None:
        """ 

`SetBitmap`(*self*, *bitmap*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetBitmap "Permalink to this definition")
Sets the bitmap label for fields of this type.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetBorderColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetBorderColour`(*self*, *colour*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetBorderColour "Permalink to this definition")
Sets the colour used for drawing the field border.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetDisplayStyle(self, displayStyle: int) -> None:
        """ 

`SetDisplayStyle`(*self*, *displayStyle*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetDisplayStyle "Permalink to this definition")
Sets the display style for fields of this type.



Parameters
**displayStyle** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetFont(self, font: 'Font') -> None:
        """ 

`SetFont`(*self*, *font*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetFont "Permalink to this definition")
Sets the font used for drawing the text label.



Parameters
**font** ([*wx.Font*](wx.Font.html#wx.Font "wx.Font")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetHorizontalMargin(self, margin: int) -> None:
        """ 

`SetHorizontalMargin`(*self*, *margin*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetHorizontalMargin "Permalink to this definition")
Sets the horizontal margin surrounding the field object.



Parameters
**margin** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetHorizontalPadding(self, padding: int) -> None:
        """ 

`SetHorizontalPadding`(*self*, *padding*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetHorizontalPadding "Permalink to this definition")
Sets the horizontal padding (the distance between the border and the text).



Parameters
**padding** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetLabel(self, label: str) -> None:
        """ 

`SetLabel`(*self*, *label*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetLabel "Permalink to this definition")
Sets the text label for fields of this type.



Parameters
**label** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetTextColour(self, colour: Union[int, str, 'Colour']) -> None:
        """ 

`SetTextColour`(*self*, *colour*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetTextColour "Permalink to this definition")
Sets the colour used for drawing the text label.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetVerticalMargin(self, margin: int) -> None:
        """ 

`SetVerticalMargin`(*self*, *margin*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetVerticalMargin "Permalink to this definition")
Sets the vertical margin surrounding the field object.



Parameters
**margin** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    def SetVerticalPadding(self, padding: int) -> None:
        """ 

`SetVerticalPadding`(*self*, *padding*)[¶](#wx.richtext.RichTextFieldTypeStandard.SetVerticalPadding "Permalink to this definition")
Sets the vertical padding (the distance between the border and the text).



Parameters
**padding** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFieldTypeStandard.html
        """

    BackgroundColour: 'Colour'  # `BackgroundColour`[¶](#wx.richtext.RichTextFieldTypeStandard.BackgroundColour "Permalink to this definition")See [`GetBackgroundColour`](#wx.richtext.RichTextFieldTypeStandard.GetBackgroundColour "wx.richtext.RichTextFieldTypeStandard.GetBackgroundColour") and [`SetBackgroundColour`](#wx.richtext.RichTextFieldTypeStandard.SetBackgroundColour "wx.richtext.RichTextFieldTypeStandard.SetBackgroundColour")
    Bitmap: '_Bitmap'  # `Bitmap`[¶](#wx.richtext.RichTextFieldTypeStandard.Bitmap "Permalink to this definition")See [`GetBitmap`](#wx.richtext.RichTextFieldTypeStandard.GetBitmap "wx.richtext.RichTextFieldTypeStandard.GetBitmap") and [`SetBitmap`](#wx.richtext.RichTextFieldTypeStandard.SetBitmap "wx.richtext.RichTextFieldTypeStandard.SetBitmap")
    BorderColour: 'Colour'  # `BorderColour`[¶](#wx.richtext.RichTextFieldTypeStandard.BorderColour "Permalink to this definition")See [`GetBorderColour`](#wx.richtext.RichTextFieldTypeStandard.GetBorderColour "wx.richtext.RichTextFieldTypeStandard.GetBorderColour") and [`SetBorderColour`](#wx.richtext.RichTextFieldTypeStandard.SetBorderColour "wx.richtext.RichTextFieldTypeStandard.SetBorderColour")
    DisplayStyle: int  # `DisplayStyle`[¶](#wx.richtext.RichTextFieldTypeStandard.DisplayStyle "Permalink to this definition")See [`GetDisplayStyle`](#wx.richtext.RichTextFieldTypeStandard.GetDisplayStyle "wx.richtext.RichTextFieldTypeStandard.GetDisplayStyle") and [`SetDisplayStyle`](#wx.richtext.RichTextFieldTypeStandard.SetDisplayStyle "wx.richtext.RichTextFieldTypeStandard.SetDisplayStyle")
    Font: '_Font'  # `Font`[¶](#wx.richtext.RichTextFieldTypeStandard.Font "Permalink to this definition")See [`GetFont`](#wx.richtext.RichTextFieldTypeStandard.GetFont "wx.richtext.RichTextFieldTypeStandard.GetFont") and [`SetFont`](#wx.richtext.RichTextFieldTypeStandard.SetFont "wx.richtext.RichTextFieldTypeStandard.SetFont")
    HorizontalMargin: int  # `HorizontalMargin`[¶](#wx.richtext.RichTextFieldTypeStandard.HorizontalMargin "Permalink to this definition")See [`GetHorizontalMargin`](#wx.richtext.RichTextFieldTypeStandard.GetHorizontalMargin "wx.richtext.RichTextFieldTypeStandard.GetHorizontalMargin") and [`SetHorizontalMargin`](#wx.richtext.RichTextFieldTypeStandard.SetHorizontalMargin "wx.richtext.RichTextFieldTypeStandard.SetHorizontalMargin")
    HorizontalPadding: int  # `HorizontalPadding`[¶](#wx.richtext.RichTextFieldTypeStandard.HorizontalPadding "Permalink to this definition")See [`GetHorizontalPadding`](#wx.richtext.RichTextFieldTypeStandard.GetHorizontalPadding "wx.richtext.RichTextFieldTypeStandard.GetHorizontalPadding") and [`SetHorizontalPadding`](#wx.richtext.RichTextFieldTypeStandard.SetHorizontalPadding "wx.richtext.RichTextFieldTypeStandard.SetHorizontalPadding")
    Label: str  # `Label`[¶](#wx.richtext.RichTextFieldTypeStandard.Label "Permalink to this definition")See [`GetLabel`](#wx.richtext.RichTextFieldTypeStandard.GetLabel "wx.richtext.RichTextFieldTypeStandard.GetLabel") and [`SetLabel`](#wx.richtext.RichTextFieldTypeStandard.SetLabel "wx.richtext.RichTextFieldTypeStandard.SetLabel")
    TextColour: 'Colour'  # `TextColour`[¶](#wx.richtext.RichTextFieldTypeStandard.TextColour "Permalink to this definition")See [`GetTextColour`](#wx.richtext.RichTextFieldTypeStandard.GetTextColour "wx.richtext.RichTextFieldTypeStandard.GetTextColour") and [`SetTextColour`](#wx.richtext.RichTextFieldTypeStandard.SetTextColour "wx.richtext.RichTextFieldTypeStandard.SetTextColour")
    VerticalMargin: int  # `VerticalMargin`[¶](#wx.richtext.RichTextFieldTypeStandard.VerticalMargin "Permalink to this definition")See [`GetVerticalMargin`](#wx.richtext.RichTextFieldTypeStandard.GetVerticalMargin "wx.richtext.RichTextFieldTypeStandard.GetVerticalMargin") and [`SetVerticalMargin`](#wx.richtext.RichTextFieldTypeStandard.SetVerticalMargin "wx.richtext.RichTextFieldTypeStandard.SetVerticalMargin")
    VerticalPadding: int  # `VerticalPadding`[¶](#wx.richtext.RichTextFieldTypeStandard.VerticalPadding "Permalink to this definition")See [`GetVerticalPadding`](#wx.richtext.RichTextFieldTypeStandard.GetVerticalPadding "wx.richtext.RichTextFieldTypeStandard.GetVerticalPadding") and [`SetVerticalPadding`](#wx.richtext.RichTextFieldTypeStandard.SetVerticalPadding "wx.richtext.RichTextFieldTypeStandard.SetVerticalPadding")



RICHTEXT_FIELD_STYLE_COMPOSITE: int  # Creates a composite field; you will probably need to derive a new class to implement UpdateField.

RICHTEXT_FIELD_STYLE_RECTANGLE: int  # Shows a rounded rectangle background.

RICHTEXT_FIELD_STYLE_NO_BORDER: int  # Suppresses the background and border; mostly used with a bitmap label.

RICHTEXT_FIELD_STYLE_START_TAG: int  # Shows a start tag background, with the pointy end facing right.

RICHTEXT_FIELD_STYLE_END_TAG: int  # Shows an end tag background, with the pointy end facing left. ^^

class RichTextBox(RichTextParagraphLayoutBox):
    """ **Possible constructors**:



```
RichTextBox(parent=None)

RichTextBox(obj)

```


This class implements a floating or inline text box, containing
paragraphs.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None)*


Default constructor; optionally pass the parent object.



Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextBox*](#wx.richtext.RichTextBox "wx.richtext.RichTextBox")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextBox.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextBox.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Copy(self, obj: 'richtext.RichTextBox') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextBox.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextBox*](#wx.richtext.RichTextBox "wx.richtext.RichTextBox")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextBox.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextBox.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextBox.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextBox.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextBox.html
        """

    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextBox.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextBox.GetPropertiesMenuLabel "wx.richtext.RichTextBox.GetPropertiesMenuLabel")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextBox.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextBox.GetXMLNodeName "wx.richtext.RichTextBox.GetXMLNodeName")



class RichTextStyleListBox(HtmlListBox):
    """ **Possible constructors**:



```
RichTextStyleListBox(parent, id=ID_ANY, pos=DefaultPosition,
                     size=DefaultSize, style=0)

RichTextStyleListBox()

```


This is a listbox that can display the styles in a
RichTextStyleSheet, and apply the selection to an associated
RichTextCtrl.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextStyleListBox.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent, id=ID\_ANY, pos=DefaultPosition, size=DefaultSize, style=0)*


Constructor.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –






---

  



**\_\_init\_\_** *(self)*




---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def ApplyStyle(self, i: int) -> None:
        """ 

`ApplyStyle`(*self*, *i*)[¶](#wx.richtext.RichTextStyleListBox.ApplyStyle "Permalink to this definition")
Applies the *ith* style to the associated rich text control.



Parameters
**i** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def ConvertTenthsMMToPixels(self, dc, units) -> int:
        """ 

`ConvertTenthsMMToPixels`(*self*, *dc*, *units*)[¶](#wx.richtext.RichTextStyleListBox.ConvertTenthsMMToPixels "Permalink to this definition")
Converts units in tenths of a millimetre to device units.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **units** (*int*) –



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0) -> bool:
        """ 

`Create`(*self*, *parent*, *id=ID\_ANY*, *pos=DefaultPosition*, *size=DefaultSize*, *style=0*)[¶](#wx.richtext.RichTextStyleListBox.Create "Permalink to this definition")
Creates the window.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def CreateHTML(self, styleDef: 'richtext.RichTextStyleDefinition') -> str:
        """ 

`CreateHTML`(*self*, *styleDef*)[¶](#wx.richtext.RichTextStyleListBox.CreateHTML "Permalink to this definition")
Creates a suitable HTML fragment for a definition.



Parameters
**styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetApplyOnSelection(self) -> bool:
        """ 

`GetApplyOnSelection`(*self*)[¶](#wx.richtext.RichTextStyleListBox.GetApplyOnSelection "Permalink to this definition")
If the return value is `True`, clicking on a style name in the list will immediately apply the style to the associated rich text control.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextStyleListBox.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetRichTextCtrl(self) -> 'RichTextCtrl':
        """ 

`GetRichTextCtrl`(*self*)[¶](#wx.richtext.RichTextStyleListBox.GetRichTextCtrl "Permalink to this definition")
Returns the  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl) associated with this listbox.



Return type
 [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyle(self, i: int) -> 'RichTextStyleDefinition':
        """ 

`GetStyle`(*self*, *i*)[¶](#wx.richtext.RichTextStyleListBox.GetStyle "Permalink to this definition")
Gets a style for a listbox index.



Parameters
**i** (*int*) – 



Return type
 [wx.richtext.RichTextStyleDefinition](wx.richtext.RichTextStyleDefinition.html#wx-richtext-richtextstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextStyleListBox.GetStyleSheet "Permalink to this definition")
Returns the style sheet associated with this listbox.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def GetStyleType(self) -> 'wxRichTextStyleType':
        """ 

`GetStyleType`(*self*)[¶](#wx.richtext.RichTextStyleListBox.GetStyleType "Permalink to this definition")
Returns the type of style to show in the list box.



Return type
*wx.richtext.RichTextStyleListBox.wxRichTextStyleType*






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def OnGetItem(self, n: int) -> str:
        """ 

`OnGetItem`(*self*, *n*)[¶](#wx.richtext.RichTextStyleListBox.OnGetItem "Permalink to this definition")
Returns the HTML for this item.



Parameters
**n** (*int*) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def OnLeftDown(self, event: 'MouseEvent') -> None:
        """ 

`OnLeftDown`(*self*, *event*)[¶](#wx.richtext.RichTextStyleListBox.OnLeftDown "Permalink to this definition")
Implements left click behaviour, applying the clicked style to the  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl).



Parameters
**event** ([*wx.MouseEvent*](wx.MouseEvent.html#wx.MouseEvent "wx.MouseEvent")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetApplyOnSelection(self, applyOnSelection: bool) -> None:
        """ 

`SetApplyOnSelection`(*self*, *applyOnSelection*)[¶](#wx.richtext.RichTextStyleListBox.SetApplyOnSelection "Permalink to this definition")
If *applyOnSelection* is `True`, clicking on a style name in the list will immediately apply the style to the associated rich text control.



Parameters
**applyOnSelection** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetRichTextCtrl(self, ctrl: 'richtext.RichTextCtrl') -> None:
        """ 

`SetRichTextCtrl`(*self*, *ctrl*)[¶](#wx.richtext.RichTextStyleListBox.SetRichTextCtrl "Permalink to this definition")
Associates the listbox with a  [wx.richtext.RichTextCtrl](wx.richtext.RichTextCtrl.html#wx-richtext-richtextctrl).



Parameters
**ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetStyleSheet(self, styleSheet: 'richtext.RichTextStyleSheet') -> None:
        """ 

`SetStyleSheet`(*self*, *styleSheet*)[¶](#wx.richtext.RichTextStyleListBox.SetStyleSheet "Permalink to this definition")
Associates the control with a style sheet.



Parameters
**styleSheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def SetStyleType(self, styleType: RichTextStyleListBox.wxRichTextStyleType) -> None:
        """ 

`SetStyleType`(*self*, *styleType*)[¶](#wx.richtext.RichTextStyleListBox.SetStyleType "Permalink to this definition")
Sets the style type to display.


One of


* `RichTextStyleListBox.__init__` ,
* `RichTextStyleListBox.__init__` ,
* `RichTextStyleListBox.__init__`
* `RichTextStyleListBox.__init__` .



Parameters
**styleType** (*RichTextStyleListBox.wxRichTextStyleType*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    def UpdateStyles(self) -> None:
        """ 

`UpdateStyles`(*self*)[¶](#wx.richtext.RichTextStyleListBox.UpdateStyles "Permalink to this definition")
Updates the list from the associated style sheet.




            Source: https://docs.wxpython.org/wx.richtext.RichTextStyleListBox.html
        """

    ApplyOnSelection: bool  # `ApplyOnSelection`[¶](#wx.richtext.RichTextStyleListBox.ApplyOnSelection "Permalink to this definition")See [`GetApplyOnSelection`](#wx.richtext.RichTextStyleListBox.GetApplyOnSelection "wx.richtext.RichTextStyleListBox.GetApplyOnSelection") and [`SetApplyOnSelection`](#wx.richtext.RichTextStyleListBox.SetApplyOnSelection "wx.richtext.RichTextStyleListBox.SetApplyOnSelection")
    RichTextCtrl: 'RichTextCtrl'  # `RichTextCtrl`[¶](#wx.richtext.RichTextStyleListBox.RichTextCtrl "Permalink to this definition")See [`GetRichTextCtrl`](#wx.richtext.RichTextStyleListBox.GetRichTextCtrl "wx.richtext.RichTextStyleListBox.GetRichTextCtrl") and [`SetRichTextCtrl`](#wx.richtext.RichTextStyleListBox.SetRichTextCtrl "wx.richtext.RichTextStyleListBox.SetRichTextCtrl")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextStyleListBox.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextStyleListBox.GetStyleSheet "wx.richtext.RichTextStyleListBox.GetStyleSheet") and [`SetStyleSheet`](#wx.richtext.RichTextStyleListBox.SetStyleSheet "wx.richtext.RichTextStyleListBox.SetStyleSheet")
    StyleType: 'wxRichTextStyleType'  # `StyleType`[¶](#wx.richtext.RichTextStyleListBox.StyleType "Permalink to this definition")See [`GetStyleType`](#wx.richtext.RichTextStyleListBox.GetStyleType "wx.richtext.RichTextStyleListBox.GetStyleType") and [`SetStyleType`](#wx.richtext.RichTextStyleListBox.SetStyleType "wx.richtext.RichTextStyleListBox.SetStyleType")



RichTextCommandId: TypeAlias = int  # Enumeration

RICHTEXT_INSERT: int

RICHTEXT_DELETE: int

RICHTEXT_CHANGE_ATTRIBUTES: int

RICHTEXT_CHANGE_STYLE: int

class RichTextFormattingDialog(PropertySheetDialog):
    """ **Possible constructors**:



```
RichTextFormattingDialog()

RichTextFormattingDialog(flags, parent, title="Formatting", id=ID_ANY,
                         pos=DefaultPosition, sz=DefaultSize, style=DEFAULT_DIALOG_STYLE)

```


This dialog allows the user to edit a character and/or paragraph
style.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextFormattingDialog.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, flags, parent, title=”Formatting”, id=ID\_ANY, pos=DefaultPosition, sz=DefaultSize, style=DEFAULT\_DIALOG\_STYLE)*


Constructors.



Parameters
* **flags** (*long*) – The pages to show.
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – The dialog’s parent.
* **title** (*string*) – The dialog’s title.
* **id** (*wx.WindowID*) – The dialog’s `ID`.
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – The dialog’s position.
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – The dialog’s size.
* **style** (*long*) – The dialog’s window style.






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def ApplyStyle(self, ctrl, range, flags=RICHTEXT_SETSTYLE_WITH_UNDO|RICHTEXT_SETSTYLE_OPTIMIZE) -> bool:
        """ 

`ApplyStyle`(*self*, *ctrl*, *range*, *flags=RICHTEXT\_SETSTYLE\_WITH\_UNDO|RICHTEXT\_SETSTYLE\_OPTIMIZE*)[¶](#wx.richtext.RichTextFormattingDialog.ApplyStyle "Permalink to this definition")
Apply attributes to the given range, only changing attributes that need to be changed.



Parameters
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **flags** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def Create(*args, **kwargs) -> bool:
        """ 

`Create`(*self*, *flags*, *parent*, *title=GetTranslation("Formatting")*, *id=ID\_ANY*, *pos=DefaultPosition*, *sz=DefaultSize*, *style=DEFAULT\_DIALOG\_STYLE*)[¶](#wx.richtext.RichTextFormattingDialog.Create "Permalink to this definition")
Creation: see  [wx.richtext.RichTextFormattingDialog](#wx-richtext-richtextformattingdialog) “the constructor” for details about the parameters.



Parameters
* **flags** (*long*) –
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **title** (*string*) –
* **id** (*wx.WindowID*) –
* **pos** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **style** (*long*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetAttributes(self) -> 'TextAttr':
        """ 

`GetAttributes`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.GetAttributes "Permalink to this definition")
Gets the attributes being edited.



Return type
*TextAttr*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetClassDefaultAttributes(variant: int=WINDOW_VARIANT_NORMAL) -> 'VisualAttributes':
        """ 

*static* `GetClassDefaultAttributes`(*variant=WINDOW\_VARIANT\_NORMAL*)[¶](#wx.richtext.RichTextFormattingDialog.GetClassDefaultAttributes "Permalink to this definition")

Parameters
**variant** ([*WindowVariant*](wx.WindowVariant.enumeration.html "WindowVariant")) – 



Return type
*VisualAttributes*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetColourData() -> 'ColourData':
        """ 

*static* `GetColourData`()[¶](#wx.richtext.RichTextFormattingDialog.GetColourData "Permalink to this definition")
Returns the custom colour data for use by the colour dialog.



Return type
*ColourData*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialog(win: 'Window') -> 'RichTextFormattingDialog':
        """ 

*static* `GetDialog`(*win*)[¶](#wx.richtext.RichTextFormattingDialog.GetDialog "Permalink to this definition")
Helper for pages to get the top-level dialog.



Parameters
**win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
 [wx.richtext.RichTextFormattingDialog](#wx-richtext-richtextformattingdialog)






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialogAttributes(win: 'Window') -> 'TextAttr':
        """ 

*static* `GetDialogAttributes`(*win*)[¶](#wx.richtext.RichTextFormattingDialog.GetDialogAttributes "Permalink to this definition")
Helper for pages to get the attributes.



Parameters
**win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
*TextAttr*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetDialogStyleDefinition(win: 'Window') -> 'RichTextStyleDefinition':
        """ 

*static* `GetDialogStyleDefinition`(*win*)[¶](#wx.richtext.RichTextFormattingDialog.GetDialogStyleDefinition "Permalink to this definition")
Helper for pages to get the style.



Parameters
**win** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) – 



Return type
 [wx.richtext.RichTextStyleDefinition](wx.richtext.RichTextStyleDefinition.html#wx-richtext-richtextstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetFormattingDialogFactory() -> 'RichTextFormattingDialogFactory':
        """ 

*static* `GetFormattingDialogFactory`()[¶](#wx.richtext.RichTextFormattingDialog.GetFormattingDialogFactory "Permalink to this definition")
Returns the object to be used to customize the dialog and provide pages.



Return type
 [wx.richtext.RichTextFormattingDialogFactory](wx.richtext.RichTextFormattingDialogFactory.html#wx-richtext-richtextformattingdialogfactory)






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetImageList(self) -> 'ImageList':
        """ 

`GetImageList`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.GetImageList "Permalink to this definition")
Returns the image list associated with the dialog, used for example if showing the dialog as a toolbook.



Return type
[`ImageList`](#wx.richtext.RichTextFormattingDialog.ImageList "wx.richtext.RichTextFormattingDialog.ImageList")






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetLastPage() -> int:
        """ 

*static* `GetLastPage`()[¶](#wx.richtext.RichTextFormattingDialog.GetLastPage "Permalink to this definition")
Returns the page identifier of the last page selected (not the control id).



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetOptions(self) -> int:
        """ 

`GetOptions`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.GetOptions "Permalink to this definition")
Gets the dialog options, determining what the interface presents to the user.


Currently the only option is Option\_AllowPixelFontSize.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def GetRestoreLastPage() -> bool:
        """ 

*static* `GetRestoreLastPage`()[¶](#wx.richtext.RichTextFormattingDialog.GetRestoreLastPage "Permalink to this definition")
Returns `True` if the dialog will restore the last-selected page.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyle(self, ctrl, range) -> bool:
        """ 

`GetStyle`(*self*, *ctrl*, *range*)[¶](#wx.richtext.RichTextFormattingDialog.GetStyle "Permalink to this definition")
Gets common attributes from the given range and calls [`SetAttributes`](#wx.richtext.RichTextFormattingDialog.SetAttributes "wx.richtext.RichTextFormattingDialog.SetAttributes") .


Attributes that do not have common values in the given range will be omitted from the style’s flags.



Parameters
* **ctrl** ([*wx.richtext.RichTextCtrl*](wx.richtext.RichTextCtrl.html#wx.richtext.RichTextCtrl "wx.richtext.RichTextCtrl")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyleDefinition(self) -> 'RichTextStyleDefinition':
        """ 

`GetStyleDefinition`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.GetStyleDefinition "Permalink to this definition")
Gets the associated style definition, if any.



Return type
 [wx.richtext.RichTextStyleDefinition](wx.richtext.RichTextStyleDefinition.html#wx-richtext-richtextstyledefinition)






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def GetStyleSheet(self) -> 'RichTextStyleSheet':
        """ 

`GetStyleSheet`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.GetStyleSheet "Permalink to this definition")
Gets the associated style sheet, if any.



Return type
 [wx.richtext.RichTextStyleSheet](wx.richtext.RichTextStyleSheet.html#wx-richtext-richtextstylesheet)






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def HasOption(self, option: int) -> bool:
        """ 

`HasOption`(*self*, *option*)[¶](#wx.richtext.RichTextFormattingDialog.HasOption "Permalink to this definition")
Returns `True` if the given option is present.



Parameters
**option** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetAttributes(self, attr: 'TextAttr') -> None:
        """ 

`SetAttributes`(*self*, *attr*)[¶](#wx.richtext.RichTextFormattingDialog.SetAttributes "Permalink to this definition")
Sets the attributes to be edited.



Parameters
**attr** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetColourData(colourData: 'ColourData') -> None:
        """ 

*static* `SetColourData`(*colourData*)[¶](#wx.richtext.RichTextFormattingDialog.SetColourData "Permalink to this definition")
Sets the custom colour data for use by the colour dialog.



Parameters
**colourData** ([*wx.ColourData*](wx.ColourData.html#wx.ColourData "wx.ColourData")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetFormattingDialogFactory(factory: 'richtext.RichTextFormattingDialogFactory') -> None:
        """ 

*static* `SetFormattingDialogFactory`(*factory*)[¶](#wx.richtext.RichTextFormattingDialog.SetFormattingDialogFactory "Permalink to this definition")
Sets the formatting factory object to be used for customization and page creation.


It deletes the existing factory object.



Parameters
**factory** ([*wx.richtext.RichTextFormattingDialogFactory*](wx.richtext.RichTextFormattingDialogFactory.html#wx.richtext.RichTextFormattingDialogFactory "wx.richtext.RichTextFormattingDialogFactory")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetImageList(self, imageList: 'ImageList') -> None:
        """ 

`SetImageList`(*self*, *imageList*)[¶](#wx.richtext.RichTextFormattingDialog.SetImageList "Permalink to this definition")
Sets the image list associated with the dialog’s property sheet.



Parameters
**imageList** ([*wx.ImageList*](wx.ImageList.html#wx.ImageList "wx.ImageList")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetLastPage(lastPage: int) -> None:
        """ 

*static* `SetLastPage`(*lastPage*)[¶](#wx.richtext.RichTextFormattingDialog.SetLastPage "Permalink to this definition")
Sets the page identifier of the last page selected (not the control id).



Parameters
**lastPage** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetOptions(self, options: int) -> None:
        """ 

`SetOptions`(*self*, *options*)[¶](#wx.richtext.RichTextFormattingDialog.SetOptions "Permalink to this definition")
Sets the dialog options, determining what the interface presents to the user.


Currently the only option is Option\_AllowPixelFontSize.



Parameters
**options** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    @staticmethod
    def SetRestoreLastPage(b: bool) -> None:
        """ 

*static* `SetRestoreLastPage`(*b*)[¶](#wx.richtext.RichTextFormattingDialog.SetRestoreLastPage "Permalink to this definition")
Pass `True` if the dialog should restore the last-selected page.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetStyle(self, style, update=True) -> bool:
        """ 

`SetStyle`(*self*, *style*, *update=True*)[¶](#wx.richtext.RichTextFormattingDialog.SetStyle "Permalink to this definition")
Sets the attributes and optionally updates the display, if *update* is `True`.



Parameters
* **style** ([*wx.TextAttr*](wx.TextAttr.html#wx.TextAttr "wx.TextAttr")) –
* **update** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def SetStyleDefinition(self, styleDef, sheet, update=True) -> bool:
        """ 

`SetStyleDefinition`(*self*, *styleDef*, *sheet*, *update=True*)[¶](#wx.richtext.RichTextFormattingDialog.SetStyleDefinition "Permalink to this definition")
Sets the style definition and optionally update the display, if *update* is `True`.



Parameters
* **styleDef** ([*wx.richtext.RichTextStyleDefinition*](wx.richtext.RichTextStyleDefinition.html#wx.richtext.RichTextStyleDefinition "wx.richtext.RichTextStyleDefinition")) –
* **sheet** ([*wx.richtext.RichTextStyleSheet*](wx.richtext.RichTextStyleSheet.html#wx.richtext.RichTextStyleSheet "wx.richtext.RichTextStyleSheet")) –
* **update** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    def UpdateDisplay(self) -> bool:
        """ 

`UpdateDisplay`(*self*)[¶](#wx.richtext.RichTextFormattingDialog.UpdateDisplay "Permalink to this definition")
Updates the display.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextFormattingDialog.html
        """

    Attributes: 'TextAttr'  # `Attributes`[¶](#wx.richtext.RichTextFormattingDialog.Attributes "Permalink to this definition")See [`GetAttributes`](#wx.richtext.RichTextFormattingDialog.GetAttributes "wx.richtext.RichTextFormattingDialog.GetAttributes") and [`SetAttributes`](#wx.richtext.RichTextFormattingDialog.SetAttributes "wx.richtext.RichTextFormattingDialog.SetAttributes")
    ImageList: '_ImageList'  # `ImageList`[¶](#wx.richtext.RichTextFormattingDialog.ImageList "Permalink to this definition")See [`GetImageList`](#wx.richtext.RichTextFormattingDialog.GetImageList "wx.richtext.RichTextFormattingDialog.GetImageList") and [`SetImageList`](#wx.richtext.RichTextFormattingDialog.SetImageList "wx.richtext.RichTextFormattingDialog.SetImageList")
    Options: int  # `Options`[¶](#wx.richtext.RichTextFormattingDialog.Options "Permalink to this definition")See [`GetOptions`](#wx.richtext.RichTextFormattingDialog.GetOptions "wx.richtext.RichTextFormattingDialog.GetOptions") and [`SetOptions`](#wx.richtext.RichTextFormattingDialog.SetOptions "wx.richtext.RichTextFormattingDialog.SetOptions")
    StyleDefinition: 'RichTextStyleDefinition'  # `StyleDefinition`[¶](#wx.richtext.RichTextFormattingDialog.StyleDefinition "Permalink to this definition")See [`GetStyleDefinition`](#wx.richtext.RichTextFormattingDialog.GetStyleDefinition "wx.richtext.RichTextFormattingDialog.GetStyleDefinition") and [`SetStyleDefinition`](#wx.richtext.RichTextFormattingDialog.SetStyleDefinition "wx.richtext.RichTextFormattingDialog.SetStyleDefinition")
    StyleSheet: 'RichTextStyleSheet'  # `StyleSheet`[¶](#wx.richtext.RichTextFormattingDialog.StyleSheet "Permalink to this definition")See [`GetStyleSheet`](#wx.richtext.RichTextFormattingDialog.GetStyleSheet "wx.richtext.RichTextFormattingDialog.GetStyleSheet")



class RichTextObjectAddress:
    """ **Possible constructors**:



```
RichTextObjectAddress(topLevelContainer, obj)

RichTextObjectAddress()

RichTextObjectAddress(address)

```


A class for specifying an object anywhere in an object hierarchy,
without using a pointer, necessary since `RTC` commands may delete and
recreate sub-objects so physical object addresses change.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextObjectAddress.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, topLevelContainer, obj)*


Creates the address given a container and an object.



Parameters
* **topLevelContainer** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –






---

  



**\_\_init\_\_** *(self)*




---

  



**\_\_init\_\_** *(self, address)*



Parameters
**address** ([*wx.richtext.RichTextObjectAddress*](#wx.richtext.RichTextObjectAddress "wx.richtext.RichTextObjectAddress")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Copy(self, address: 'richtext.RichTextObjectAddress') -> None:
        """ 

`Copy`(*self*, *address*)[¶](#wx.richtext.RichTextObjectAddress.Copy "Permalink to this definition")
Copies the address.



Parameters
**address** ([*wx.richtext.RichTextObjectAddress*](#wx.richtext.RichTextObjectAddress "wx.richtext.RichTextObjectAddress")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Create(self, topLevelContainer, obj) -> bool:
        """ 

`Create`(*self*, *topLevelContainer*, *obj*)[¶](#wx.richtext.RichTextObjectAddress.Create "Permalink to this definition")
Creates the address given a container and an object.



Parameters
* **topLevelContainer** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def GetAddress(self) -> int:
        """ 

`GetAddress`(*self*)[¶](#wx.richtext.RichTextObjectAddress.GetAddress "Permalink to this definition")
Returns the array of integers representing the object address.



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def GetObject(self, topLevelContainer: 'richtext.RichTextParagraphLayoutBox') -> 'RichTextObject':
        """ 

`GetObject`(*self*, *topLevelContainer*)[¶](#wx.richtext.RichTextObjectAddress.GetObject "Permalink to this definition")
Returns the object specified by the address, given a top level container.



Parameters
**topLevelContainer** ([*wx.richtext.RichTextParagraphLayoutBox*](wx.richtext.RichTextParagraphLayoutBox.html#wx.richtext.RichTextParagraphLayoutBox "wx.richtext.RichTextParagraphLayoutBox")) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextObjectAddress.Init "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    def SetAddress(self, address: int) -> None:
        """ 

`SetAddress`(*self*, *address*)[¶](#wx.richtext.RichTextObjectAddress.SetAddress "Permalink to this definition")
Sets the address from an array of integers.



Parameters
**address** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextObjectAddress.html
        """

    Address: int  # `Address`[¶](#wx.richtext.RichTextObjectAddress.Address "Permalink to this definition")See [`GetAddress`](#wx.richtext.RichTextObjectAddress.GetAddress "wx.richtext.RichTextObjectAddress.GetAddress") and [`SetAddress`](#wx.richtext.RichTextObjectAddress.SetAddress "wx.richtext.RichTextObjectAddress.SetAddress")



class RichTextPlainText(RichTextObject):
    """ **Possible constructors**:



```
RichTextPlainText(text="", parent=None, style=None)

RichTextPlainText(obj)

```


This object represents a single piece of text.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextPlainText.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, text=””, parent=None, style=None)*


Constructor.



Parameters
* **text** (*string*) –
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextPlainText*](#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextPlainText.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CanMerge(self, object, context) -> bool:
        """ 

`CanMerge`(*self*, *object*, *context*)[¶](#wx.richtext.RichTextPlainText.CanMerge "Permalink to this definition")
Returns `True` if this object can merge itself with the given one.



Parameters
* **object** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def CanSplit(self, context: 'richtext.RichTextDrawingContext') -> bool:
        """ 

`CanSplit`(*self*, *context*)[¶](#wx.richtext.RichTextPlainText.CanSplit "Permalink to this definition")
Returns `True` if this object can potentially be split, by virtue of having different virtual attributes for individual sub-objects.



Parameters
**context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextPlainText.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Copy(self, obj: 'richtext.RichTextPlainText') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextPlainText.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextPlainText*](#wx.richtext.RichTextPlainText "wx.richtext.RichTextPlainText")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`DeleteRange`(*self*, *range*)[¶](#wx.richtext.RichTextPlainText.DeleteRange "Permalink to this definition")
Deletes the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def DoSplit(self, pos: int) -> 'RichTextObject':
        """ 

`DoSplit`(*self*, *pos*)[¶](#wx.richtext.RichTextPlainText.DoSplit "Permalink to this definition")
Do a split from *pos*, returning an object containing the second part, and setting the first part in ‘this’.



Parameters
**pos** (*long*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextPlainText.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetFirstLineBreakPosition(self, pos: int) -> int:
        """ 

`GetFirstLineBreakPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextPlainText.GetFirstLineBreakPosition "Permalink to this definition")
Get the first position from pos that has a line break character.



Parameters
**pos** (*long*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextPlainText.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetText(self) -> str:
        """ 

`GetText`(*self*)[¶](#wx.richtext.RichTextPlainText.GetText "Permalink to this definition")
Returns the text.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ 

`GetTextForRange`(*self*, *range*)[¶](#wx.richtext.RichTextPlainText.GetTextForRange "Permalink to this definition")
Returns any text in this object for the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextPlainText.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ 

`ImportFromXML`(*self*, *buffer*, *node*, *handler*, *recurse*)[¶](#wx.richtext.RichTextPlainText.ImportFromXML "Permalink to this definition")
Imports this object from `XML`.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **handler** ([*wx.richtext.RichTextXMLHandler*](wx.richtext.RichTextXMLHandler.html#wx.richtext.RichTextXMLHandler "wx.richtext.RichTextXMLHandler")) –
* **recurse** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextPlainText.IsEmpty "Permalink to this definition")
Returns `True` if the object is empty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextPlainText.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Merge(self, object, context) -> bool:
        """ 

`Merge`(*self*, *object*, *context*)[¶](#wx.richtext.RichTextPlainText.Merge "Permalink to this definition")
Returns `True` if this object merged itself with the given one.


The calling code will then delete the given object.



Parameters
* **object** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def SetText(self, text: str) -> None:
        """ 

`SetText`(*self*, *text*)[¶](#wx.richtext.RichTextPlainText.SetText "Permalink to this definition")
Sets the text.



Parameters
**text** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def Split(self, context: 'richtext.RichTextDrawingContext') -> 'RichTextObject':
        """ 

`Split`(*self*, *context*)[¶](#wx.richtext.RichTextPlainText.Split "Permalink to this definition")
Returns the final object in the split objects if this object was split due to differences between sub-object virtual attributes.


Returns itself if it was not split.



Parameters
**context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ 

`UsesParagraphAttributes`(*self*)[¶](#wx.richtext.RichTextPlainText.UsesParagraphAttributes "Permalink to this definition")
Does this object take note of paragraph attributes? Text and image objects don’t.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainText.html
        """

    Text: str  # `Text`[¶](#wx.richtext.RichTextPlainText.Text "Permalink to this definition")See [`GetText`](#wx.richtext.RichTextPlainText.GetText "wx.richtext.RichTextPlainText.GetText") and [`SetText`](#wx.richtext.RichTextPlainText.SetText "wx.richtext.RichTextPlainText.SetText")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextPlainText.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextPlainText.GetXMLNodeName "wx.richtext.RichTextPlainText.GetXMLNodeName")



class RichTextHTMLHandler(RichTextFileHandler):
    """ **Possible constructors**:



```
RichTextHTMLHandler(name="HTML", ext="html", type=RICHTEXT_TYPE_HTML)

```


Handles HTML output (only) for RichTextCtrl content.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
    """
    def __init__(self, name="HTML", ext="html", type=RICHTEXT_TYPE_HTML) -> None:
        """ 

`__init__`(*self*, *name="HTML"*, *ext="html"*, *type=RICHTEXT\_TYPE\_HTML*)[¶](#wx.richtext.RichTextHTMLHandler.__init__ "Permalink to this definition")
Constructor.



Parameters
* **name** (*string*) –
* **ext** (*string*) –
* **type** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def ClearTemporaryImageLocations(self) -> None:
        """ 

`ClearTemporaryImageLocations`(*self*)[¶](#wx.richtext.RichTextHTMLHandler.ClearTemporaryImageLocations "Permalink to this definition")
Clears the image locations generated by the last operation.




            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def DeleteTemporaryImages(self, *args, **kw) -> bool:
        """ 

`DeleteTemporaryImages`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextHTMLHandler.DeleteTemporaryImages "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**DeleteTemporaryImages** *(self)*


Deletes the in-memory or temporary files generated by the last operation.



Return type
*bool*






---

  



**DeleteTemporaryImages** *(flags, imageLocations)*


Delete the in-memory or temporary files generated by the last operation.


This is a static function that can be used to delete the saved locations from an earlier operation, for example after the user has viewed the HTML file.



Parameters
* **flags** (*int*) –
* **imageLocations** (*list of strings*) –



Return type
*bool*






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetFontSizeMapping(self) -> int:
        """ 

`GetFontSizeMapping`(*self*)[¶](#wx.richtext.RichTextHTMLHandler.GetFontSizeMapping "Permalink to this definition")
Returns the mapping for converting point sizes to HTML font sizes.



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetTempDir(self) -> str:
        """ 

`GetTempDir`(*self*)[¶](#wx.richtext.RichTextHTMLHandler.GetTempDir "Permalink to this definition")
Returns the directory used to store temporary image files.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def GetTemporaryImageLocations(self) -> list[str]:
        """ 

`GetTemporaryImageLocations`(*self*)[¶](#wx.richtext.RichTextHTMLHandler.GetTemporaryImageLocations "Permalink to this definition")
Returns the image locations for the last operation.



Return type
*list of strings*






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    @staticmethod
    def SetFileCounter(counter: int) -> None:
        """ 

*static* `SetFileCounter`(*counter*)[¶](#wx.richtext.RichTextHTMLHandler.SetFileCounter "Permalink to this definition")
Reset the file counter, in case, for example, the same names are required each time.



Parameters
**counter** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetFontSizeMapping(self, fontSizeMapping: int) -> None:
        """ 

`SetFontSizeMapping`(*self*, *fontSizeMapping*)[¶](#wx.richtext.RichTextHTMLHandler.SetFontSizeMapping "Permalink to this definition")
Sets the mapping for converting point sizes to HTML font sizes.


There should be 7 elements, one for each HTML font size, each element specifying the maximum point size for that HTML font size. For example:



```
fontSizeMapping = [7, 9, 11, 12, 14, 22, 100]
htmlHandler.SetFontSizeMapping(fontSizeMapping)

```



Parameters
**fontSizeMapping** (*list of integers*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetTempDir(self, tempDir: str) -> None:
        """ 

`SetTempDir`(*self*, *tempDir*)[¶](#wx.richtext.RichTextHTMLHandler.SetTempDir "Permalink to this definition")
Sets the directory for storing temporary files.


If empty, the system temporary directory will be used.



Parameters
**tempDir** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    def SetTemporaryImageLocations(self, locations: list[str]) -> None:
        """ 

`SetTemporaryImageLocations`(*self*, *locations*)[¶](#wx.richtext.RichTextHTMLHandler.SetTemporaryImageLocations "Permalink to this definition")
Sets the list of image locations generated by the last operation.



Parameters
**locations** (*list of strings*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextHTMLHandler.html
        """

    FontSizeMapping: int  # `FontSizeMapping`[¶](#wx.richtext.RichTextHTMLHandler.FontSizeMapping "Permalink to this definition")See [`GetFontSizeMapping`](#wx.richtext.RichTextHTMLHandler.GetFontSizeMapping "wx.richtext.RichTextHTMLHandler.GetFontSizeMapping") and [`SetFontSizeMapping`](#wx.richtext.RichTextHTMLHandler.SetFontSizeMapping "wx.richtext.RichTextHTMLHandler.SetFontSizeMapping")
    TempDir: str  # `TempDir`[¶](#wx.richtext.RichTextHTMLHandler.TempDir "Permalink to this definition")See [`GetTempDir`](#wx.richtext.RichTextHTMLHandler.GetTempDir "wx.richtext.RichTextHTMLHandler.GetTempDir") and [`SetTempDir`](#wx.richtext.RichTextHTMLHandler.SetTempDir "wx.richtext.RichTextHTMLHandler.SetTempDir")
    TemporaryImageLocations: list[str]  # `TemporaryImageLocations`[¶](#wx.richtext.RichTextHTMLHandler.TemporaryImageLocations "Permalink to this definition")See [`GetTemporaryImageLocations`](#wx.richtext.RichTextHTMLHandler.GetTemporaryImageLocations "wx.richtext.RichTextHTMLHandler.GetTemporaryImageLocations") and [`SetTemporaryImageLocations`](#wx.richtext.RichTextHTMLHandler.SetTemporaryImageLocations "wx.richtext.RichTextHTMLHandler.SetTemporaryImageLocations")



RICHTEXT_HANDLER_SAVE_IMAGES_TO_BASE64: int

RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY: int

RICHTEXT_HANDLER_SAVE_IMAGES_TO_FILES: int

RICHTEXT_HANDLER_NO_HEADER_FOOTER: int

RICHTEXT_HANDLER_USE_CSS: int

class RichTextPlainTextHandler(RichTextFileHandler):
    """ **Possible constructors**:



```
RichTextPlainTextHandler(name="Text", ext="txt",
                         type=RICHTEXT_TYPE_TEXT)

```


Implements saving a buffer to plain text.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
    """
    def __init__(self, name="Text", ext="txt", type=RICHTEXT_TYPE_TEXT) -> None:
        """ 

`__init__`(*self*, *name="Text"*, *ext="txt"*, *type=RICHTEXT\_TYPE\_TEXT*)[¶](#wx.richtext.RichTextPlainTextHandler.__init__ "Permalink to this definition")

Parameters
* **name** (*string*) –
* **ext** (*string*) –
* **type** ([*RichTextFileType*](wx.richtext.RichTextFileType.enumeration.html "RichTextFileType")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def CanLoad(self) -> bool:
        """ 

`CanLoad`(*self*)[¶](#wx.richtext.RichTextPlainTextHandler.CanLoad "Permalink to this definition")
Returns `True` if we can load using this handler.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def CanSave(self) -> bool:
        """ 

`CanSave`(*self*)[¶](#wx.richtext.RichTextPlainTextHandler.CanSave "Permalink to this definition")
Returns `True` if we can save using this handler.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def DoLoadFile(self, buffer, stream) -> bool:
        """ 

`DoLoadFile`(*self*, *buffer*, *stream*)[¶](#wx.richtext.RichTextPlainTextHandler.DoLoadFile "Permalink to this definition")
Override to load content from *stream* into *buffer*.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.InputStream*](wx.InputStream.html#wx.InputStream "wx.InputStream")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """

    def DoSaveFile(self, buffer, stream) -> bool:
        """ 

`DoSaveFile`(*self*, *buffer*, *stream*)[¶](#wx.richtext.RichTextPlainTextHandler.DoSaveFile "Permalink to this definition")
Override to save content to *stream* from *buffer*.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextPlainTextHandler.html
        """



class RichTextXMLHandler(RichTextFileHandler):
    """ **Possible constructors**:



```
RichTextXMLHandler(name="XML", ext="xml", type=RICHTEXT_TYPE_XML)

```


A handler for loading and saving content in an `XML` format specific to
RichTextBuffer.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
    """
    def __init__(self, name="XML", ext="xml", type=RICHTEXT_TYPE_XML) -> None:
        """ 

`__init__`(*self*, *name="XML"*, *ext="xml"*, *type=RICHTEXT\_TYPE\_XML*)[¶](#wx.richtext.RichTextXMLHandler.__init__ "Permalink to this definition")
Constructor.



Parameters
* **name** (*string*) –
* **ext** (*string*) –
* **type** (*int*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def CanLoad(self) -> bool:
        """ 

`CanLoad`(*self*)[¶](#wx.richtext.RichTextXMLHandler.CanLoad "Permalink to this definition")
Returns `True`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def CanSave(self) -> bool:
        """ 

`CanSave`(*self*)[¶](#wx.richtext.RichTextXMLHandler.CanSave "Permalink to this definition")
Returns `True`.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    @staticmethod
    def ClearNodeToClassMap() -> None:
        """ 

*static* `ClearNodeToClassMap`()[¶](#wx.richtext.RichTextXMLHandler.ClearNodeToClassMap "Permalink to this definition")
Cleans up the mapping between node name and C++ class.




            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def ExportXML(self, stream, obj, level) -> bool:
        """ 

`ExportXML`(*self*, *stream*, *obj*, *level*)[¶](#wx.richtext.RichTextXMLHandler.ExportXML "Permalink to this definition")
Recursively exports an object to the stream.



Parameters
* **stream** ([*wx.OutputStream*](wx.OutputStream.html#wx.OutputStream "wx.OutputStream")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **level** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    def ImportXML(self, buffer, obj, node) -> bool:
        """ 

`ImportXML`(*self*, *buffer*, *obj*, *node*)[¶](#wx.richtext.RichTextXMLHandler.ImportXML "Permalink to this definition")
Recursively imports an object.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """

    @staticmethod
    def RegisterNodeName(nodeName, className) -> None:
        """ 

*static* `RegisterNodeName`(*nodeName*, *className*)[¶](#wx.richtext.RichTextXMLHandler.RegisterNodeName "Permalink to this definition")
Call with `XML` node name, C++ class name so that `RTC` can read in the node.


If you add a custom object, call this.



Parameters
* **nodeName** (*string*) –
* **className** (*string*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextXMLHandler.html
        """



RICHTEXT_HANDLER_INCLUDE_STYLESHEET: int

RichTextOddEvenPage: TypeAlias = int  # Enumeration

RICHTEXT_PAGE_ODD: int

RICHTEXT_PAGE_EVEN: int

RICHTEXT_PAGE_ALL: int

RichTextPageLocation: TypeAlias = int  # Enumeration

RICHTEXT_PAGE_LEFT: int

RICHTEXT_PAGE_CENTRE: int

RICHTEXT_PAGE_RIGHT: int

class RichTextCompositeObject(RichTextObject):
    """ **Possible constructors**:



```
RichTextCompositeObject(parent=None)

```


Objects of this class can contain other objects.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
    """
    def __init__(self, parent: Optional['richtext.RichTextObject']=None) -> None:
        """ 

`__init__`(*self*, *parent=None*)[¶](#wx.richtext.RichTextCompositeObject.__init__ "Permalink to this definition")

Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def AppendChild(self, child: 'richtext.RichTextObject') -> int:
        """ 

`AppendChild`(*self*, *child*)[¶](#wx.richtext.RichTextCompositeObject.AppendChild "Permalink to this definition")
Appends a child, returning the position.



Parameters
**child** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextCompositeObject.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Copy(self, obj: 'richtext.RichTextCompositeObject') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextCompositeObject.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextCompositeObject*](#wx.richtext.RichTextCompositeObject "wx.richtext.RichTextCompositeObject")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Defragment(self, context, range=RICHTEXT_ALL) -> bool:
        """ 

`Defragment`(*self*, *context*, *range=RICHTEXT\_ALL*)[¶](#wx.richtext.RichTextCompositeObject.Defragment "Permalink to this definition")
Recursively merges all pieces that can be merged.



Parameters
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def DeleteChildren(self) -> bool:
        """ 

`DeleteChildren`(*self*)[¶](#wx.richtext.RichTextCompositeObject.DeleteChildren "Permalink to this definition")
Deletes all the children.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def DeleteRange(self, range: 'richtext.RichTextRange') -> bool:
        """ 

`DeleteRange`(*self*, *range*)[¶](#wx.richtext.RichTextCompositeObject.DeleteRange "Permalink to this definition")
Deletes the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ 

`FindPosition`(*self*, *dc*, *context*, *index*, *forceLineStart*)[¶](#wx.richtext.RichTextCompositeObject.FindPosition "Permalink to this definition")
Finds the absolute position and row height for the given character position.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **index** (*long*) –
* **forceLineStart** (*bool*) –



Return type
*tuple*



Returns
( *bool*, *pt*, *height* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChild(self, n: int) -> 'RichTextObject':
        """ 

`GetChild`(*self*, *n*)[¶](#wx.richtext.RichTextCompositeObject.GetChild "Permalink to this definition")
Returns the nth child.



Parameters
**n** (*int*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildAtPosition(self, pos: int) -> 'RichTextObject':
        """ 

`GetChildAtPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextCompositeObject.GetChildAtPosition "Permalink to this definition")
Returns the child object at the given character position.



Parameters
**pos** (*long*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildCount(self) -> int:
        """ 

`GetChildCount`(*self*)[¶](#wx.richtext.RichTextCompositeObject.GetChildCount "Permalink to this definition")
Returns the number of children.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetChildren(self) -> 'RichTextObjectList':
        """ 

`GetChildren`(*self*)[¶](#wx.richtext.RichTextCompositeObject.GetChildren "Permalink to this definition")
Returns the children.



Return type
*RichTextObjectList*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextCompositeObject.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def GetTextForRange(self, range: 'richtext.RichTextRange') -> str:
        """ 

`GetTextForRange`(*self*, *range*)[¶](#wx.richtext.RichTextCompositeObject.GetTextForRange "Permalink to this definition")
Returns any text in this object for the given range.



Parameters
**range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextCompositeObject.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def InsertChild(self, child, inFrontOf) -> bool:
        """ 

`InsertChild`(*self*, *child*, *inFrontOf*)[¶](#wx.richtext.RichTextCompositeObject.InsertChild "Permalink to this definition")
Inserts the child in front of the given object, or at the beginning.



Parameters
* **child** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **inFrontOf** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Invalidate(self, invalidRange: 'richtext.RichTextRange'=RICHTEXT_ALL) -> None:
        """ 

`Invalidate`(*self*, *invalidRange=RICHTEXT\_ALL*)[¶](#wx.richtext.RichTextCompositeObject.Invalidate "Permalink to this definition")
Invalidates the object at the given range.


With no argument, invalidates the whole object.



Parameters
**invalidRange** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsAtomic(self) -> bool:
        """ 

`IsAtomic`(*self*)[¶](#wx.richtext.RichTextCompositeObject.IsAtomic "Permalink to this definition")
Returns `True` if no user editing can be done inside the object.


This returns `True` for simple objects, `False` for most composite objects, but `True` for fields, which if composite, should not be user-edited.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsComposite(self) -> bool:
        """ 

`IsComposite`(*self*)[¶](#wx.richtext.RichTextCompositeObject.IsComposite "Permalink to this definition")
Returns `True` if this object is composite.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextCompositeObject.IsEmpty "Permalink to this definition")
Returns `True` if the buffer is empty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def Move(self, pt: Union[tuple[int, int], 'Point']) -> None:
        """ 

`Move`(*self*, *pt*)[¶](#wx.richtext.RichTextCompositeObject.Move "Permalink to this definition")
Moves the object recursively, by adding the offset from old to new.



Parameters
**pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    def RemoveChild(self, child, deleteChild=False) -> bool:
        """ 

`RemoveChild`(*self*, *child*, *deleteChild=False*)[¶](#wx.richtext.RichTextCompositeObject.RemoveChild "Permalink to this definition")
Removes and optionally deletes the specified child.



Parameters
* **child** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **deleteChild** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCompositeObject.html
        """

    ChildCount: int  # `ChildCount`[¶](#wx.richtext.RichTextCompositeObject.ChildCount "Permalink to this definition")See [`GetChildCount`](#wx.richtext.RichTextCompositeObject.GetChildCount "wx.richtext.RichTextCompositeObject.GetChildCount")
    Children: 'RichTextObjectList'  # `Children`[¶](#wx.richtext.RichTextCompositeObject.Children "Permalink to this definition")See [`GetChildren`](#wx.richtext.RichTextCompositeObject.GetChildren "wx.richtext.RichTextCompositeObject.GetChildren")



class RichTextImage(RichTextObject):
    """ **Possible constructors**:



```
RichTextImage(parent=None)

RichTextImage(image, parent=None, charStyle=None)

RichTextImage(imageBlock, parent=None, charStyle=None)

RichTextImage(obj)

```


This class implements a graphic object.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextImage.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None)*


Default constructor.



Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






---

  



**\_\_init\_\_** *(self, image, parent=None, charStyle=None)*


Creates a  [wx.richtext.RichTextImage](#wx-richtext-richtextimage) from a  [wx.Image](wx.Image.html#wx-image).



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **charStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






---

  



**\_\_init\_\_** *(self, imageBlock, parent=None, charStyle=None)*


Creates a  [wx.richtext.RichTextImage](#wx-richtext-richtextimage) from an image block.



Parameters
* **imageBlock** ([*wx.richtext.RichTextImageBlock*](wx.richtext.RichTextImageBlock.html#wx.richtext.RichTextImageBlock "wx.richtext.RichTextImageBlock")) –
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **charStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextImage*](#wx.richtext.RichTextImage "wx.richtext.RichTextImage")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextImage.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextImage.Clone "Permalink to this definition")
Clones the image object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Copy(self, obj: 'richtext.RichTextImage') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextImage.Copy "Permalink to this definition")
Copies the image object.



Parameters
**obj** ([*wx.richtext.RichTextImage*](#wx.richtext.RichTextImage "wx.richtext.RichTextImage")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextImage.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextImage.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageBlock(self) -> 'RichTextImageBlock':
        """ 

`GetImageBlock`(*self*)[¶](#wx.richtext.RichTextImage.GetImageBlock "Permalink to this definition")
Returns the image block containing the raw data.



Return type
 [wx.richtext.RichTextImageBlock](wx.richtext.RichTextImageBlock.html#wx-richtext-richtextimageblock)






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageCache(self) -> 'Bitmap':
        """ 

`GetImageCache`(*self*)[¶](#wx.richtext.RichTextImage.GetImageCache "Permalink to this definition")
Returns the image cache (a scaled bitmap).



Return type
*Bitmap*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetImageState(self) -> int:
        """ 

`GetImageState`(*self*)[¶](#wx.richtext.RichTextImage.GetImageState "Permalink to this definition")
Gets the image state.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetNaturalSize(self) -> 'TextAttrSize':
        """ 

`GetNaturalSize`(*self*)[¶](#wx.richtext.RichTextImage.GetNaturalSize "Permalink to this definition")
Returns the ‘natural’ size for this object - the image size.



Return type
 [wx.richtext.TextAttrSize](wx.richtext.TextAttrSize.html#wx-richtext-textattrsize)






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetOriginalImageSize(self) -> 'Size':
        """ 

`GetOriginalImageSize`(*self*)[¶](#wx.richtext.RichTextImage.GetOriginalImageSize "Permalink to this definition")
Gets the original image size.



Return type
*Size*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextImage.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextImage.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextImage.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def ImportFromXML(self, buffer, node, handler, recurse) -> bool:
        """ 

`ImportFromXML`(*self*, *buffer*, *node*, *handler*, *recurse*)[¶](#wx.richtext.RichTextImage.ImportFromXML "Permalink to this definition")
Imports this object from `XML`.



Parameters
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –
* **node** ([*wx.xml.XmlNode*](wx.xml.XmlNode.html#wx.xml.XmlNode "wx.xml.XmlNode")) –
* **handler** ([*wx.richtext.RichTextXMLHandler*](wx.richtext.RichTextXMLHandler.html#wx.richtext.RichTextXMLHandler "wx.richtext.RichTextXMLHandler")) –
* **recurse** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def IsEmpty(self) -> bool:
        """ 

`IsEmpty`(*self*)[¶](#wx.richtext.RichTextImage.IsEmpty "Permalink to this definition")
Returns `True` if the object is empty.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def IsFloatable(self) -> bool:
        """ 

`IsFloatable`(*self*)[¶](#wx.richtext.RichTextImage.IsFloatable "Permalink to this definition")
Returns `True` if this class of object is floatable.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextImage.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def LoadAndScaleImageCache(self, image, sz, context, changed) -> tuple:
        """ 

`LoadAndScaleImageCache`(*self*, *image*, *sz*, *context*, *changed*)[¶](#wx.richtext.RichTextImage.LoadAndScaleImageCache "Permalink to this definition")
Do the loading and scaling.



Parameters
* **image** ([*wx.Image*](wx.Image.html#wx.Image "wx.Image")) –
* **sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **changed** (*bool*) –



Return type
*tuple*



Returns
( *bool*, *changed* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def LoadImageCache(self, dc, context, retImageSize, resetCache=False, parentSize=DefaultSize) -> bool:
        """ 

`LoadImageCache`(*self*, *dc*, *context*, *retImageSize*, *resetCache=False*, *parentSize=DefaultSize*)[¶](#wx.richtext.RichTextImage.LoadImageCache "Permalink to this definition")
Creates a cached image at the required size.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **retImageSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **resetCache** (*bool*) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def ResetImageCache(self) -> None:
        """ 

`ResetImageCache`(*self*)[¶](#wx.richtext.RichTextImage.ResetImageCache "Permalink to this definition")
Resets the image cache.




            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetImageCache(self, bitmap: 'Bitmap') -> None:
        """ 

`SetImageCache`(*self*, *bitmap*)[¶](#wx.richtext.RichTextImage.SetImageCache "Permalink to this definition")
Sets the image cache.



Parameters
**bitmap** ([*wx.Bitmap*](wx.Bitmap.html#wx.Bitmap "wx.Bitmap")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetImageState(self, state: int) -> None:
        """ 

`SetImageState`(*self*, *state*)[¶](#wx.richtext.RichTextImage.SetImageState "Permalink to this definition")
Sets the image state.



Parameters
**state** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def SetOriginalImageSize(self, sz: Union[tuple[int, int], 'Size']) -> None:
        """ 

`SetOriginalImageSize`(*self*, *sz*)[¶](#wx.richtext.RichTextImage.SetOriginalImageSize "Permalink to this definition")
Sets the original image size.



Parameters
**sz** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    def UsesParagraphAttributes(self) -> bool:
        """ 

`UsesParagraphAttributes`(*self*)[¶](#wx.richtext.RichTextImage.UsesParagraphAttributes "Permalink to this definition")
Returns `True` if this object takes note of paragraph attributes (text and image objects don’t).



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextImage.html
        """

    ImageBlock: 'RichTextImageBlock'  # `ImageBlock`[¶](#wx.richtext.RichTextImage.ImageBlock "Permalink to this definition")See [`GetImageBlock`](#wx.richtext.RichTextImage.GetImageBlock "wx.richtext.RichTextImage.GetImageBlock")
    ImageCache: 'Bitmap'  # `ImageCache`[¶](#wx.richtext.RichTextImage.ImageCache "Permalink to this definition")See [`GetImageCache`](#wx.richtext.RichTextImage.GetImageCache "wx.richtext.RichTextImage.GetImageCache") and [`SetImageCache`](#wx.richtext.RichTextImage.SetImageCache "wx.richtext.RichTextImage.SetImageCache")
    ImageState: int  # `ImageState`[¶](#wx.richtext.RichTextImage.ImageState "Permalink to this definition")See [`GetImageState`](#wx.richtext.RichTextImage.GetImageState "wx.richtext.RichTextImage.GetImageState") and [`SetImageState`](#wx.richtext.RichTextImage.SetImageState "wx.richtext.RichTextImage.SetImageState")
    NaturalSize: 'TextAttrSize'  # `NaturalSize`[¶](#wx.richtext.RichTextImage.NaturalSize "Permalink to this definition")See [`GetNaturalSize`](#wx.richtext.RichTextImage.GetNaturalSize "wx.richtext.RichTextImage.GetNaturalSize")
    OriginalImageSize: 'Size'  # `OriginalImageSize`[¶](#wx.richtext.RichTextImage.OriginalImageSize "Permalink to this definition")See [`GetOriginalImageSize`](#wx.richtext.RichTextImage.GetOriginalImageSize "wx.richtext.RichTextImage.GetOriginalImageSize") and [`SetOriginalImageSize`](#wx.richtext.RichTextImage.SetOriginalImageSize "wx.richtext.RichTextImage.SetOriginalImageSize")
    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextImage.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextImage.GetPropertiesMenuLabel "wx.richtext.RichTextImage.GetPropertiesMenuLabel")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextImage.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextImage.GetXMLNodeName "wx.richtext.RichTextImage.GetXMLNodeName")



class TextAttrBorders:
    """ **Possible constructors**:



```
TextAttrBorders()

```


A class representing a rich text object’s borders.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.TextAttrBorders.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def Apply(self, borders, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *borders*, *compareWith=None*)[¶](#wx.richtext.TextAttrBorders.Apply "Permalink to this definition")
Applies border to this object, but not if the same as *compareWith*.



Parameters
* **borders** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –
* **compareWith** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrBorders.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –
* **clashingAttr** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –
* **absentAttr** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def EqPartial(self, borders, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *borders*, *weakTest=True*)[¶](#wx.richtext.TextAttrBorders.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *borders* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *borders* but not in this object.



Parameters
* **borders** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetBottom(self) -> 'TextAttrBorder':
        """ 

`GetBottom`(*self*)[¶](#wx.richtext.TextAttrBorders.GetBottom "Permalink to this definition")

Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetLeft(self) -> 'TextAttrBorder':
        """ 

`GetLeft`(*self*)[¶](#wx.richtext.TextAttrBorders.GetLeft "Permalink to this definition")

Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetRight(self) -> 'TextAttrBorder':
        """ 

`GetRight`(*self*)[¶](#wx.richtext.TextAttrBorders.GetRight "Permalink to this definition")

Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def GetTop(self) -> 'TextAttrBorder':
        """ 

`GetTop`(*self*)[¶](#wx.richtext.TextAttrBorders.GetTop "Permalink to this definition")

Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrBorders.IsValid "Permalink to this definition")
Returns `True` if at least one border is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrBorders') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextAttrBorders.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrBorders.Reset "Permalink to this definition")
Resets all borders.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ 

`SetColour`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrBorders.SetColour "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetColour** *(self, colour)*


Sets colour of all borders.



Parameters
**colour** (*long*) – 






---

  



**SetColour** *(self, colour)*


Sets the colour for all borders.



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetStyle(self, style: int) -> None:
        """ 

`SetStyle`(*self*, *style*)[¶](#wx.richtext.TextAttrBorders.SetStyle "Permalink to this definition")
Sets the style of all borders.



Parameters
**style** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ 

`SetWidth`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrBorders.SetWidth "Permalink to this definition")
Sets the width of all borders.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetWidth** *(self, width)*



Parameters
**width** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






---

  



**SetWidth** *(self, value, units=TEXT\_ATTR\_UNITS\_TENTHS\_MM)*



Parameters
* **value** (*int*) –
* **units** ([*TextAttrUnits*](wx.richtext.TextAttrUnits.enumeration.html "TextAttrUnits")) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.TextAttrBorders.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.TextAttrBorders.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrBorders.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**borders** ([*wx.richtext.TextAttrBorders*](#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorders.html
        """

    Bottom: 'TextAttrBorder'  # `Bottom`[¶](#wx.richtext.TextAttrBorders.Bottom "Permalink to this definition")See [`GetBottom`](#wx.richtext.TextAttrBorders.GetBottom "wx.richtext.TextAttrBorders.GetBottom")
    Left: 'TextAttrBorder'  # `Left`[¶](#wx.richtext.TextAttrBorders.Left "Permalink to this definition")See [`GetLeft`](#wx.richtext.TextAttrBorders.GetLeft "wx.richtext.TextAttrBorders.GetLeft")
    Right: 'TextAttrBorder'  # `Right`[¶](#wx.richtext.TextAttrBorders.Right "Permalink to this definition")See [`GetRight`](#wx.richtext.TextAttrBorders.GetRight "wx.richtext.TextAttrBorders.GetRight")
    Top: 'TextAttrBorder'  # `Top`[¶](#wx.richtext.TextAttrBorders.Top "Permalink to this definition")See [`GetTop`](#wx.richtext.TextAttrBorders.GetTop "wx.richtext.TextAttrBorders.GetTop")
    m_bottom: Any  # `m_bottom`[¶](#wx.richtext.TextAttrBorders.m_bottom "Permalink to this definition")A public C++ attribute of type [`TextAttrBorder`](wx.richtext.TextAttrBorder.html#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder") .
    m_left: Any  # `m_left`[¶](#wx.richtext.TextAttrBorders.m_left "Permalink to this definition")A public C++ attribute of type [`TextAttrBorder`](wx.richtext.TextAttrBorder.html#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder") .
    m_right: Any  # `m_right`[¶](#wx.richtext.TextAttrBorders.m_right "Permalink to this definition")A public C++ attribute of type [`TextAttrBorder`](wx.richtext.TextAttrBorder.html#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder") .
    m_top: Any  # `m_top`[¶](#wx.richtext.TextAttrBorders.m_top "Permalink to this definition")A public C++ attribute of type [`TextAttrBorder`](wx.richtext.TextAttrBorder.html#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder") .



class TextAttrSize:
    """ **Possible constructors**:



```
TextAttrSize()

```


A class for representing width and height.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.TextAttrSize.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def Apply(self, dims, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *dims*, *compareWith=None*)[¶](#wx.richtext.TextAttrSize.Apply "Permalink to this definition")
Apply to this object, but not if the same as *compareWith*.



Parameters
* **dims** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –
* **compareWith** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrSize.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –
* **clashingAttr** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –
* **absentAttr** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def EqPartial(self, size, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *size*, *weakTest=True*)[¶](#wx.richtext.TextAttrSize.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *size* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *size* but not in this object.



Parameters
* **size** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def GetHeight(self) -> 'TextAttrDimension':
        """ 

`GetHeight`(*self*)[¶](#wx.richtext.TextAttrSize.GetHeight "Permalink to this definition")
Gets the height.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ 

`GetWidth`(*self*)[¶](#wx.richtext.TextAttrSize.GetWidth "Permalink to this definition")
Returns the width.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrSize.IsValid "Permalink to this definition")
Is the size valid?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrSize') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextAttrSize.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrSize.Reset "Permalink to this definition")
Resets the width and height dimensions.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def SetHeight(self, *args, **kw) -> None:
        """ 

`SetHeight`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrSize.SetHeight "Permalink to this definition")
Sets the height.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetHeight** *(self, value, flags)*



Parameters
* **value** (*int*) –
* **flags** (*wx.richtext.TextAttrDimensionFlags*) –






---

  



**SetHeight** *(self, dim)*



Parameters
**dim** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ 

`SetWidth`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrSize.SetWidth "Permalink to this definition")
Sets the width.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetWidth** *(self, value, flags)*



Parameters
* **value** (*int*) –
* **flags** (*wx.richtext.TextAttrDimensionFlags*) –






---

  



**SetWidth** *(self, dim)*



Parameters
**dim** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.TextAttrSize.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.TextAttrSize.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrSize.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**size** ([*wx.richtext.TextAttrSize*](#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrSize.html
        """

    Height: 'TextAttrDimension'  # `Height`[¶](#wx.richtext.TextAttrSize.Height "Permalink to this definition")See [`GetHeight`](#wx.richtext.TextAttrSize.GetHeight "wx.richtext.TextAttrSize.GetHeight") and [`SetHeight`](#wx.richtext.TextAttrSize.SetHeight "wx.richtext.TextAttrSize.SetHeight")
    Width: 'TextAttrDimension'  # `Width`[¶](#wx.richtext.TextAttrSize.Width "Permalink to this definition")See [`GetWidth`](#wx.richtext.TextAttrSize.GetWidth "wx.richtext.TextAttrSize.GetWidth") and [`SetWidth`](#wx.richtext.TextAttrSize.SetWidth "wx.richtext.TextAttrSize.SetWidth")
    m_height: Any  # `m_height`[¶](#wx.richtext.TextAttrSize.m_height "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_width: Any  # `m_width`[¶](#wx.richtext.TextAttrSize.m_width "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .



class RichTextParagraph(RichTextCompositeObject):
    """ **Possible constructors**:



```
RichTextParagraph(parent=None, style=None)

RichTextParagraph(text, parent=None, paraStyle=None, charStyle=None)

RichTextParagraph(obj)

```


This object represents a single paragraph containing various objects
such as text content, images, and further paragraph layout objects.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraph.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None, style=None)*


Constructor taking a parent and style.



Parameters
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **style** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






---

  



**\_\_init\_\_** *(self, text, parent=None, paraStyle=None, charStyle=None)*


Constructor taking a text string, a parent and paragraph and character attributes.



Parameters
* **text** (*string*) –
* **parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **paraStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **charStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –






---

  



**\_\_init\_\_** *(self, obj)*



Parameters
**obj** ([*wx.richtext.RichTextParagraph*](#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def AllocateLine(self, pos: int) -> 'RichTextLine':
        """ 

`AllocateLine`(*self*, *pos*)[¶](#wx.richtext.RichTextParagraph.AllocateLine "Permalink to this definition")
Allocates or reuses a line object.



Parameters
**pos** (*int*) – 



Return type
 [wx.richtext.RichTextLine](wx.richtext.RichTextLine.html#wx-richtext-richtextline)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ApplyParagraphStyle(self, line, attr, rect, dc) -> None:
        """ 

`ApplyParagraphStyle`(*self*, *line*, *attr*, *rect*, *dc*)[¶](#wx.richtext.RichTextParagraph.ApplyParagraphStyle "Permalink to this definition")
Applies paragraph styles such as centering to the wrapped lines.



Parameters
* **line** ([*wx.richtext.RichTextLine*](wx.richtext.RichTextLine.html#wx.richtext.RichTextLine "wx.richtext.RichTextLine")) –
* **attr** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def CalculateRange(self, start: int) -> None:
        """ 

`CalculateRange`(*self*, *start*)[¶](#wx.richtext.RichTextParagraph.CalculateRange "Permalink to this definition")
Calculates the range of the object.


By default, guess that the object is 1 unit long.



Parameters
**start** (*long*) – 



Return type
*end*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def ClearDefaultTabs() -> None:
        """ 

*static* `ClearDefaultTabs`()[¶](#wx.richtext.RichTextParagraph.ClearDefaultTabs "Permalink to this definition")
Clears the default tabstop array.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ClearLines(self) -> None:
        """ 

`ClearLines`(*self*)[¶](#wx.richtext.RichTextParagraph.ClearLines "Permalink to this definition")
Clears the cached lines.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def ClearUnusedLines(self, lineCount: int) -> bool:
        """ 

`ClearUnusedLines`(*self*, *lineCount*)[¶](#wx.richtext.RichTextParagraph.ClearUnusedLines "Permalink to this definition")
Clears remaining unused line objects, if any.



Parameters
**lineCount** (*int*) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextParagraph.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Copy(self, obj: 'richtext.RichTextParagraph') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextParagraph.Copy "Permalink to this definition")
Copies the object.



Parameters
**obj** ([*wx.richtext.RichTextParagraph*](#wx.richtext.RichTextParagraph "wx.richtext.RichTextParagraph")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextParagraph.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindObjectAtPosition(self, position: int) -> 'RichTextObject':
        """ 

`FindObjectAtPosition`(*self*, *position*)[¶](#wx.richtext.RichTextParagraph.FindObjectAtPosition "Permalink to this definition")
Finds the object at the given position.



Parameters
**position** (*long*) – 



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindPosition(self, dc, context, index, forceLineStart) -> tuple:
        """ 

`FindPosition`(*self*, *dc*, *context*, *index*, *forceLineStart*)[¶](#wx.richtext.RichTextParagraph.FindPosition "Permalink to this definition")
Finds the absolute position and row height for the given character position.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **index** (*long*) –
* **forceLineStart** (*bool*) –



Return type
*tuple*



Returns
( *bool*, *pt*, *height* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def FindWrapPosition(self, range, dc, context, availableSpace, wrapPosition, partialExtents) -> bool:
        """ 

`FindWrapPosition`(*self*, *range*, *dc*, *context*, *availableSpace*, *wrapPosition*, *partialExtents*)[¶](#wx.richtext.RichTextParagraph.FindWrapPosition "Permalink to this definition")
Finds a suitable wrap position.


*wrapPosition* is the last position in the line to the left of the split.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **availableSpace** (*int*) –
* **wrapPosition** (*long*) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetBulletText(self) -> str:
        """ 

`GetBulletText`(*self*)[¶](#wx.richtext.RichTextParagraph.GetBulletText "Permalink to this definition")
Returns the bullet text for this paragraph.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetCombinedAttributes(self, *args, **kw) -> 'RichTextAttr':
        """ 

`GetCombinedAttributes`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextParagraph.GetCombinedAttributes "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**GetCombinedAttributes** *(self, contentStyle, includingBoxAttr=False)*


Returns combined attributes of the base style, paragraph style and character style.


We use this to dynamically retrieve the actual style.



Parameters
* **contentStyle** ([*wx.richtext.RichTextAttr*](wx.richtext.RichTextAttr.html#wx.richtext.RichTextAttr "wx.richtext.RichTextAttr")) –
* **includingBoxAttr** (*bool*) –



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






---

  



**GetCombinedAttributes** *(self, includingBoxAttr=False)*


Returns the combined attributes of the base style and paragraph style.



Parameters
**includingBoxAttr** (*bool*) – 



Return type
 [wx.richtext.RichTextAttr](wx.richtext.RichTextAttr.html#wx-richtext-richtextattr)






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetContiguousPlainText(self, text, range, fromStart=True) -> bool:
        """ 

`GetContiguousPlainText`(*self*, *text*, *range*, *fromStart=True*)[¶](#wx.richtext.RichTextParagraph.GetContiguousPlainText "Permalink to this definition")
Returns the plain text searching from the start or end of the range.


The resulting string may be shorter than the range given.



Parameters
* **text** (*string*) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **fromStart** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def GetDefaultTabs() -> int:
        """ 

*static* `GetDefaultTabs`()[¶](#wx.richtext.RichTextParagraph.GetDefaultTabs "Permalink to this definition")
Returns the default tabstop array.



Return type
*list of integers*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetFirstLineBreakPosition(self, pos: int) -> int:
        """ 

`GetFirstLineBreakPosition`(*self*, *pos*)[¶](#wx.richtext.RichTextParagraph.GetFirstLineBreakPosition "Permalink to this definition")
Returns the first position from pos that has a line break character.



Parameters
**pos** (*long*) – 



Return type
*long*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetImpactedByFloatingObjects(self) -> int:
        """ 

`GetImpactedByFloatingObjects`(*self*)[¶](#wx.richtext.RichTextParagraph.GetImpactedByFloatingObjects "Permalink to this definition")
Whether the paragraph is impacted by floating objects from above.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetLines(self) -> Any:
        """ 

`GetLines`(*self*)[¶](#wx.richtext.RichTextParagraph.GetLines "Permalink to this definition")
Returns the cached lines.



Return type
*PyObject*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetRangeSize(*args, **kwargs) -> bool:
        """ 

`GetRangeSize`(*self*, *range*, *size*, *descent*, *dc*, *context*, *flags*, *position=Point(0*, *0)*, *parentSize=DefaultSize*, *partialExtents=None*)[¶](#wx.richtext.RichTextParagraph.GetRangeSize "Permalink to this definition")
Returns the object size for the given range.


Returns `False` if the range is invalid for this object.



Parameters
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **size** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **descent** (*int*) –
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **flags** (*int*) –
* **position** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **parentSize** ([*wx.Size*](wx.Size.html#wx.Size "wx.Size")) –
* **partialExtents** (*list of integers*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextParagraph.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextParagraph.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.RichTextParagraph.Init "Permalink to this definition")


            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    @staticmethod
    def InitDefaultTabs() -> None:
        """ 

*static* `InitDefaultTabs`()[¶](#wx.richtext.RichTextParagraph.InitDefaultTabs "Permalink to this definition")
Creates a default tabstop array.




            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def InsertText(self, pos, text) -> bool:
        """ 

`InsertText`(*self*, *pos*, *text*)[¶](#wx.richtext.RichTextParagraph.InsertText "Permalink to this definition")
Inserts text at the given position.



Parameters
* **pos** (*long*) –
* **text** (*string*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def Layout(self, dc, context, rect, parentRect, style) -> bool:
        """ 

`Layout`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*)[¶](#wx.richtext.RichTextParagraph.Layout "Permalink to this definition")
Lay the item out at the specified position with the given size constraint.


Layout must set the cached size. *rect* is the available space for the object, and *parentRect* is the container that is used to determine a relative size or position (for example if a text box must be 50% of the parent text box).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def LayoutFloat(self, dc, context, rect, parentRect, style, floatCollector) -> None:
        """ 

`LayoutFloat`(*self*, *dc*, *context*, *rect*, *parentRect*, *style*, *floatCollector*)[¶](#wx.richtext.RichTextParagraph.LayoutFloat "Permalink to this definition")
Lays out the floating objects.



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **parentRect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **style** (*int*) –
* **floatCollector** (*RichTextFloatCollector*) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def MoveFromList(self, list: list['richtext.RichTextList']) -> None:
        """ 

`MoveFromList`(*self*, *list*)[¶](#wx.richtext.RichTextParagraph.MoveFromList "Permalink to this definition")
Adds content back from a list.



Parameters
**list** (`RichTextObjectList_`) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def MoveToList(self, obj, list) -> None:
        """ 

`MoveToList`(*self*, *obj*, *list*)[¶](#wx.richtext.RichTextParagraph.MoveToList "Permalink to this definition")
Moves content to a list from this point.



Parameters
* **obj** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –
* **list** (`RichTextObjectList_`) –






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def SetImpactedByFloatingObjects(self, i: int) -> None:
        """ 

`SetImpactedByFloatingObjects`(*self*, *i*)[¶](#wx.richtext.RichTextParagraph.SetImpactedByFloatingObjects "Permalink to this definition")
Sets whether the paragraph is impacted by floating objects from above.



Parameters
**i** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    def SplitAt(self, pos, previousObject=None) -> 'RichTextObject':
        """ 

`SplitAt`(*self*, *pos*, *previousObject=None*)[¶](#wx.richtext.RichTextParagraph.SplitAt "Permalink to this definition")
Splits an object at this position if necessary, and returns the previous object, or `None` if inserting at the beginning.



Parameters
* **pos** (*long*) –
* **previousObject** ([*RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) –



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraph.html
        """

    BulletText: str  # `BulletText`[¶](#wx.richtext.RichTextParagraph.BulletText "Permalink to this definition")See [`GetBulletText`](#wx.richtext.RichTextParagraph.GetBulletText "wx.richtext.RichTextParagraph.GetBulletText")
    CombinedAttributes: 'RichTextAttr'  # `CombinedAttributes`[¶](#wx.richtext.RichTextParagraph.CombinedAttributes "Permalink to this definition")See [`GetCombinedAttributes`](#wx.richtext.RichTextParagraph.GetCombinedAttributes "wx.richtext.RichTextParagraph.GetCombinedAttributes")
    ImpactedByFloatingObjects: int  # `ImpactedByFloatingObjects`[¶](#wx.richtext.RichTextParagraph.ImpactedByFloatingObjects "Permalink to this definition")See [`GetImpactedByFloatingObjects`](#wx.richtext.RichTextParagraph.GetImpactedByFloatingObjects "wx.richtext.RichTextParagraph.GetImpactedByFloatingObjects") and [`SetImpactedByFloatingObjects`](#wx.richtext.RichTextParagraph.SetImpactedByFloatingObjects "wx.richtext.RichTextParagraph.SetImpactedByFloatingObjects")
    Lines: Any  # `Lines`[¶](#wx.richtext.RichTextParagraph.Lines "Permalink to this definition")See [`GetLines`](#wx.richtext.RichTextParagraph.GetLines "wx.richtext.RichTextParagraph.GetLines")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextParagraph.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextParagraph.GetXMLNodeName "wx.richtext.RichTextParagraph.GetXMLNodeName")



class RichTextCharacterStyleDefinition(RichTextStyleDefinition):
    """ **Possible constructors**:



```
RichTextCharacterStyleDefinition(name="")

```


This class represents a character style definition, usually added to a
RichTextStyleSheet.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextCharacterStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ 

`__init__`(*self*, *name=""*)[¶](#wx.richtext.RichTextCharacterStyleDefinition.__init__ "Permalink to this definition")
Constructor.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCharacterStyleDefinition.html
        """



class RichTextParagraphStyleDefinition(RichTextStyleDefinition):
    """ **Possible constructors**:



```
RichTextParagraphStyleDefinition(name="")

```


This class represents a paragraph style definition, usually added to a
RichTextStyleSheet.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
    """
    def __init__(self, name: str="") -> None:
        """ 

`__init__`(*self*, *name=""*)[¶](#wx.richtext.RichTextParagraphStyleDefinition.__init__ "Permalink to this definition")
Constructor.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    def GetNextStyle(self) -> str:
        """ 

`GetNextStyle`(*self*)[¶](#wx.richtext.RichTextParagraphStyleDefinition.GetNextStyle "Permalink to this definition")
Returns the style that should normally follow this style.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    def SetNextStyle(self, name: str) -> None:
        """ 

`SetNextStyle`(*self*, *name*)[¶](#wx.richtext.RichTextParagraphStyleDefinition.SetNextStyle "Permalink to this definition")
Sets the style that should normally follow this style.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextParagraphStyleDefinition.html
        """

    NextStyle: str  # `NextStyle`[¶](#wx.richtext.RichTextParagraphStyleDefinition.NextStyle "Permalink to this definition")See [`GetNextStyle`](#wx.richtext.RichTextParagraphStyleDefinition.GetNextStyle "wx.richtext.RichTextParagraphStyleDefinition.GetNextStyle") and [`SetNextStyle`](#wx.richtext.RichTextParagraphStyleDefinition.SetNextStyle "wx.richtext.RichTextParagraphStyleDefinition.SetNextStyle")



class TextBoxAttr:
    """ **Possible constructors**:



```
TextBoxAttr()

TextBoxAttr(attr)

```


A class representing the box attributes of a rich text object.


  


        Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextBoxAttr.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, attr)*


Copy constructor.



Parameters
**attr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def AddFlag(self, flag: TextBoxAttrFlags) -> None:
        """ 

`AddFlag`(*self*, *flag*)[¶](#wx.richtext.TextBoxAttr.AddFlag "Permalink to this definition")
Adds this flag.



Parameters
**flag** ([*TextBoxAttrFlags*](wx.richtext.TextBoxAttrFlags.enumeration.html "TextBoxAttrFlags")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Apply(self, style, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *style*, *compareWith=None*)[¶](#wx.richtext.TextBoxAttr.Apply "Permalink to this definition")
Merges the given attributes.


If *compareWith* is not `None`, then it will be used to mask out those attributes that are the same in style and *compareWith*, for situations where we don’t want to explicitly set inherited attributes.



Parameters
* **style** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –
* **compareWith** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextBoxAttr.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –
* **clashingAttr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –
* **absentAttr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def EqPartial(self, attr, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *attr*, *weakTest=True*)[¶](#wx.richtext.TextBoxAttr.EqPartial "Permalink to this definition")
Partial equality test, ignoring unset attributes.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of `attr` are present. If *weakTest* is `False`, the function will fail if an attribute is present in `attr` but not in this object.



Parameters
* **attr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBorder(self) -> 'TextAttrBorders':
        """ 

`GetBorder`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBorder "Permalink to this definition")
Returns the borders.



Return type
 [wx.richtext.TextAttrBorders](wx.richtext.TextAttrBorders.html#wx-richtext-textattrborders)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottom(self) -> 'TextAttrDimension':
        """ 

`GetBottom`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBottom "Permalink to this definition")
Returns the bottom position.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomBorder(self) -> 'TextAttrBorder':
        """ 

`GetBottomBorder`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBottomBorder "Permalink to this definition")
Returns the bottom border.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomMargin(self) -> 'TextAttrDimension':
        """ 

`GetBottomMargin`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBottomMargin "Permalink to this definition")
Returns the bottom margin.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomOutline(self) -> 'TextAttrBorder':
        """ 

`GetBottomOutline`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBottomOutline "Permalink to this definition")
Returns the bottom outline.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBottomPadding(self) -> 'TextAttrDimension':
        """ 

`GetBottomPadding`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBottomPadding "Permalink to this definition")
Returns the bottom padding value.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetBoxStyleName(self) -> str:
        """ 

`GetBoxStyleName`(*self*)[¶](#wx.richtext.TextBoxAttr.GetBoxStyleName "Permalink to this definition")
Returns the box style name.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetClearMode(self) -> 'TextBoxAttrClearStyle':
        """ 

`GetClearMode`(*self*)[¶](#wx.richtext.TextBoxAttr.GetClearMode "Permalink to this definition")
Returns the clear mode - whether to wrap text after object.


Currently unimplemented.



Return type
 [wx.richtext.TextBoxAttrClearStyle](wx.richtext.TextBoxAttrClearStyle.enumeration.html#wx-richtext-textboxattrclearstyle)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetCollapseBorders(self) -> 'TextBoxAttrCollapseMode':
        """ 

`GetCollapseBorders`(*self*)[¶](#wx.richtext.TextBoxAttr.GetCollapseBorders "Permalink to this definition")
Returns the collapse mode - whether to collapse borders.



Return type
 [wx.richtext.TextBoxAttrCollapseMode](wx.richtext.TextBoxAttrCollapseMode.enumeration.html#wx-richtext-textboxattrcollapsemode)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetCornerRadius(self) -> 'TextAttrDimension':
        """ 

`GetCornerRadius`(*self*)[¶](#wx.richtext.TextBoxAttr.GetCornerRadius "Permalink to this definition")

Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.TextBoxAttr.GetFlags "Permalink to this definition")
Returns the flags.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetFloatMode(self) -> 'TextBoxAttrFloatStyle':
        """ 

`GetFloatMode`(*self*)[¶](#wx.richtext.TextBoxAttr.GetFloatMode "Permalink to this definition")
Returns the float mode.



Return type
 [wx.richtext.TextBoxAttrFloatStyle](wx.richtext.TextBoxAttrFloatStyle.enumeration.html#wx-richtext-textboxattrfloatstyle)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetHeight(self) -> 'TextAttrDimension':
        """ 

`GetHeight`(*self*)[¶](#wx.richtext.TextBoxAttr.GetHeight "Permalink to this definition")
Returns the object height.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeft(self) -> 'TextAttrDimension':
        """ 

`GetLeft`(*self*)[¶](#wx.richtext.TextBoxAttr.GetLeft "Permalink to this definition")
Returns the left position.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftBorder(self) -> 'TextAttrBorder':
        """ 

`GetLeftBorder`(*self*)[¶](#wx.richtext.TextBoxAttr.GetLeftBorder "Permalink to this definition")
Returns the left border.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftMargin(self) -> 'TextAttrDimension':
        """ 

`GetLeftMargin`(*self*)[¶](#wx.richtext.TextBoxAttr.GetLeftMargin "Permalink to this definition")
Returns the left margin.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftOutline(self) -> 'TextAttrBorder':
        """ 

`GetLeftOutline`(*self*)[¶](#wx.richtext.TextBoxAttr.GetLeftOutline "Permalink to this definition")
Returns the left outline.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetLeftPadding(self) -> 'TextAttrDimension':
        """ 

`GetLeftPadding`(*self*)[¶](#wx.richtext.TextBoxAttr.GetLeftPadding "Permalink to this definition")
Returns the left padding value.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMargins(self) -> 'TextAttrDimensions':
        """ 

`GetMargins`(*self*)[¶](#wx.richtext.TextBoxAttr.GetMargins "Permalink to this definition")
Returns the margin values.



Return type
 [wx.richtext.TextAttrDimensions](wx.richtext.TextAttrDimensions.html#wx-richtext-textattrdimensions)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMaxSize(self) -> 'TextAttrSize':
        """ 

`GetMaxSize`(*self*)[¶](#wx.richtext.TextBoxAttr.GetMaxSize "Permalink to this definition")
Returns the object maximum size.



Return type
 [wx.richtext.TextAttrSize](wx.richtext.TextAttrSize.html#wx-richtext-textattrsize)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetMinSize(self) -> 'TextAttrSize':
        """ 

`GetMinSize`(*self*)[¶](#wx.richtext.TextBoxAttr.GetMinSize "Permalink to this definition")
Returns the object minimum size.



Return type
 [wx.richtext.TextAttrSize](wx.richtext.TextAttrSize.html#wx-richtext-textattrsize)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetOutline(self) -> 'TextAttrBorders':
        """ 

`GetOutline`(*self*)[¶](#wx.richtext.TextBoxAttr.GetOutline "Permalink to this definition")
Returns the outline.



Return type
 [wx.richtext.TextAttrBorders](wx.richtext.TextAttrBorders.html#wx-richtext-textattrborders)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetPadding(self) -> 'TextAttrDimensions':
        """ 

`GetPadding`(*self*)[¶](#wx.richtext.TextBoxAttr.GetPadding "Permalink to this definition")
Returns the padding values.



Return type
 [wx.richtext.TextAttrDimensions](wx.richtext.TextAttrDimensions.html#wx-richtext-textattrdimensions)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetPosition(self) -> 'TextAttrDimensions':
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.TextBoxAttr.GetPosition "Permalink to this definition")
Returns the position.



Return type
 [wx.richtext.TextAttrDimensions](wx.richtext.TextAttrDimensions.html#wx-richtext-textattrdimensions)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRight(self) -> 'TextAttrDimension':
        """ 

`GetRight`(*self*)[¶](#wx.richtext.TextBoxAttr.GetRight "Permalink to this definition")
Returns the right position.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightBorder(self) -> 'TextAttrBorder':
        """ 

`GetRightBorder`(*self*)[¶](#wx.richtext.TextBoxAttr.GetRightBorder "Permalink to this definition")
Returns the right border.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightMargin(self) -> 'TextAttrDimension':
        """ 

`GetRightMargin`(*self*)[¶](#wx.richtext.TextBoxAttr.GetRightMargin "Permalink to this definition")
Returns the right margin.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightOutline(self) -> 'TextAttrBorder':
        """ 

`GetRightOutline`(*self*)[¶](#wx.richtext.TextBoxAttr.GetRightOutline "Permalink to this definition")
Returns the right outline.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetRightPadding(self) -> 'TextAttrDimension':
        """ 

`GetRightPadding`(*self*)[¶](#wx.richtext.TextBoxAttr.GetRightPadding "Permalink to this definition")
Returns the right padding value.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetShadow(self) -> 'TextAttrShadow':
        """ 

`GetShadow`(*self*)[¶](#wx.richtext.TextBoxAttr.GetShadow "Permalink to this definition")
Returns the box shadow attributes.



Return type
 [wx.richtext.TextAttrShadow](wx.richtext.TextAttrShadow.html#wx-richtext-textattrshadow)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetSize(self) -> 'TextAttrSize':
        """ 

`GetSize`(*self*)[¶](#wx.richtext.TextBoxAttr.GetSize "Permalink to this definition")
Returns the object size.



Return type
 [wx.richtext.TextAttrSize](wx.richtext.TextAttrSize.html#wx-richtext-textattrsize)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTop(self) -> 'TextAttrDimension':
        """ 

`GetTop`(*self*)[¶](#wx.richtext.TextBoxAttr.GetTop "Permalink to this definition")
Returns the top position.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopBorder(self) -> 'TextAttrBorder':
        """ 

`GetTopBorder`(*self*)[¶](#wx.richtext.TextBoxAttr.GetTopBorder "Permalink to this definition")
Returns the top border.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopMargin(self) -> 'TextAttrDimension':
        """ 

`GetTopMargin`(*self*)[¶](#wx.richtext.TextBoxAttr.GetTopMargin "Permalink to this definition")
Returns the top margin.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopOutline(self) -> 'TextAttrBorder':
        """ 

`GetTopOutline`(*self*)[¶](#wx.richtext.TextBoxAttr.GetTopOutline "Permalink to this definition")
Returns the top outline.



Return type
 [wx.richtext.TextAttrBorder](wx.richtext.TextAttrBorder.html#wx-richtext-textattrborder)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetTopPadding(self) -> 'TextAttrDimension':
        """ 

`GetTopPadding`(*self*)[¶](#wx.richtext.TextBoxAttr.GetTopPadding "Permalink to this definition")
Returns the top padding value.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetVerticalAlignment(self) -> int:
        """ 

`GetVerticalAlignment`(*self*)[¶](#wx.richtext.TextBoxAttr.GetVerticalAlignment "Permalink to this definition")
Returns the vertical alignment.



Return type
 [wx.richtext.TextBoxAttrVerticalAlignment](wx.richtext.TextBoxAttrVerticalAlignment.enumeration.html#wx-richtext-textboxattrverticalalignment)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetWhitespaceMode(self) -> 'TextBoxAttrWhitespaceMode':
        """ 

`GetWhitespaceMode`(*self*)[¶](#wx.richtext.TextBoxAttr.GetWhitespaceMode "Permalink to this definition")
Returns the whitespace mode.



Return type
 [wx.richtext.TextBoxAttrWhitespaceMode](wx.richtext.TextBoxAttrWhitespaceMode.enumeration.html#wx-richtext-textboxattrwhitespacemode)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ 

`GetWidth`(*self*)[¶](#wx.richtext.TextBoxAttr.GetWidth "Permalink to this definition")
Returns the object width.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasBoxStyleName(self) -> bool:
        """ 

`HasBoxStyleName`(*self*)[¶](#wx.richtext.TextBoxAttr.HasBoxStyleName "Permalink to this definition")
Returns `True` if the box style name is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasClearMode(self) -> bool:
        """ 

`HasClearMode`(*self*)[¶](#wx.richtext.TextBoxAttr.HasClearMode "Permalink to this definition")
Returns `True` if we have a clear flag.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasCollapseBorders(self) -> bool:
        """ 

`HasCollapseBorders`(*self*)[¶](#wx.richtext.TextBoxAttr.HasCollapseBorders "Permalink to this definition")
Returns `True` if the collapse borders flag is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasCornerRadius(self) -> bool:
        """ 

`HasCornerRadius`(*self*)[¶](#wx.richtext.TextBoxAttr.HasCornerRadius "Permalink to this definition")
Returns `True` if the corner radius flag is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasFlag(self, flag: TextBoxAttrFlags) -> bool:
        """ 

`HasFlag`(*self*, *flag*)[¶](#wx.richtext.TextBoxAttr.HasFlag "Permalink to this definition")
Is this flag present?



Parameters
**flag** ([*TextBoxAttrFlags*](wx.richtext.TextBoxAttrFlags.enumeration.html "TextBoxAttrFlags")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasFloatMode(self) -> bool:
        """ 

`HasFloatMode`(*self*)[¶](#wx.richtext.TextBoxAttr.HasFloatMode "Permalink to this definition")
Returns `True` if float mode is active.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasVerticalAlignment(self) -> bool:
        """ 

`HasVerticalAlignment`(*self*)[¶](#wx.richtext.TextBoxAttr.HasVerticalAlignment "Permalink to this definition")
Returns `True` if a vertical alignment flag is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def HasWhitespaceMode(self) -> bool:
        """ 

`HasWhitespaceMode`(*self*)[¶](#wx.richtext.TextBoxAttr.HasWhitespaceMode "Permalink to this definition")
Returns `True` if the whitespace flag is present.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Init(self) -> None:
        """ 

`Init`(*self*)[¶](#wx.richtext.TextBoxAttr.Init "Permalink to this definition")
Initialises this object.




            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def IsDefault(self) -> bool:
        """ 

`IsDefault`(*self*)[¶](#wx.richtext.TextBoxAttr.IsDefault "Permalink to this definition")
Returns `True` if no attributes are set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def IsFloating(self) -> bool:
        """ 

`IsFloating`(*self*)[¶](#wx.richtext.TextBoxAttr.IsFloating "Permalink to this definition")
Returns `True` if this object is floating.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def RemoveFlag(self, flag: TextBoxAttrFlags) -> None:
        """ 

`RemoveFlag`(*self*, *flag*)[¶](#wx.richtext.TextBoxAttr.RemoveFlag "Permalink to this definition")
Removes this flag.



Parameters
**flag** ([*TextBoxAttrFlags*](wx.richtext.TextBoxAttrFlags.enumeration.html "TextBoxAttrFlags")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def RemoveStyle(self, attr: 'richtext.TextBoxAttr') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextBoxAttr.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextBoxAttr.Reset "Permalink to this definition")
Resets this object.




            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetBoxStyleName(self, name: str) -> None:
        """ 

`SetBoxStyleName`(*self*, *name*)[¶](#wx.richtext.TextBoxAttr.SetBoxStyleName "Permalink to this definition")
Sets the box style name.



Parameters
**name** (*string*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetClearMode(self, mode: TextBoxAttrClearStyle) -> None:
        """ 

`SetClearMode`(*self*, *mode*)[¶](#wx.richtext.TextBoxAttr.SetClearMode "Permalink to this definition")
Set the clear mode.


Currently unimplemented.



Parameters
**mode** ([*TextBoxAttrClearStyle*](wx.richtext.TextBoxAttrClearStyle.enumeration.html "TextBoxAttrClearStyle")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetCollapseBorders(self, collapse: TextBoxAttrCollapseMode) -> None:
        """ 

`SetCollapseBorders`(*self*, *collapse*)[¶](#wx.richtext.TextBoxAttr.SetCollapseBorders "Permalink to this definition")
Sets the collapse mode - whether to collapse borders.



Parameters
**collapse** ([*TextBoxAttrCollapseMode*](wx.richtext.TextBoxAttrCollapseMode.enumeration.html "TextBoxAttrCollapseMode")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetCornerRadius(self, dim: 'richtext.TextAttrDimension') -> None:
        """ 

`SetCornerRadius`(*self*, *dim*)[¶](#wx.richtext.TextBoxAttr.SetCornerRadius "Permalink to this definition")
Sets the corner radius value.



Parameters
**dim** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.TextBoxAttr.SetFlags "Permalink to this definition")
Sets the flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetFloatMode(self, mode: TextBoxAttrFloatStyle) -> None:
        """ 

`SetFloatMode`(*self*, *mode*)[¶](#wx.richtext.TextBoxAttr.SetFloatMode "Permalink to this definition")
Sets the float mode.



Parameters
**mode** ([*TextBoxAttrFloatStyle*](wx.richtext.TextBoxAttrFloatStyle.enumeration.html "TextBoxAttrFloatStyle")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetMaxSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ 

`SetMaxSize`(*self*, *sz*)[¶](#wx.richtext.TextBoxAttr.SetMaxSize "Permalink to this definition")
Sets the object maximum size.



Parameters
**sz** ([*wx.richtext.TextAttrSize*](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetMinSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ 

`SetMinSize`(*self*, *sz*)[¶](#wx.richtext.TextBoxAttr.SetMinSize "Permalink to this definition")
Sets the object minimum size.



Parameters
**sz** ([*wx.richtext.TextAttrSize*](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetSize(self, sz: 'richtext.TextAttrSize') -> None:
        """ 

`SetSize`(*self*, *sz*)[¶](#wx.richtext.TextBoxAttr.SetSize "Permalink to this definition")
Sets the object size.



Parameters
**sz** ([*wx.richtext.TextAttrSize*](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetVerticalAlignment(self, verticalAlignment: int) -> None:
        """ 

`SetVerticalAlignment`(*self*, *verticalAlignment*)[¶](#wx.richtext.TextBoxAttr.SetVerticalAlignment "Permalink to this definition")
Sets the vertical alignment.



Parameters
**verticalAlignment** ([*TextBoxAttrVerticalAlignment*](wx.richtext.TextBoxAttrVerticalAlignment.enumeration.html "TextBoxAttrVerticalAlignment")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def SetWhitespaceMode(self, whitespace: TextBoxAttrWhitespaceMode) -> None:
        """ 

`SetWhitespaceMode`(*self*, *whitespace*)[¶](#wx.richtext.TextBoxAttr.SetWhitespaceMode "Permalink to this definition")
Sets the whitespace mode.



Parameters
**whitespace** ([*TextBoxAttrWhitespaceMode*](wx.richtext.TextBoxAttrWhitespaceMode.enumeration.html "TextBoxAttrWhitespaceMode")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextBoxAttr.__eq__ "Permalink to this definition")
Equality test.



Parameters
**attr** ([*wx.richtext.TextBoxAttr*](#wx.richtext.TextBoxAttr "wx.richtext.TextBoxAttr")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextBoxAttr.html
        """

    Border: 'TextAttrBorders'  # `Border`[¶](#wx.richtext.TextBoxAttr.Border "Permalink to this definition")See [`GetBorder`](#wx.richtext.TextBoxAttr.GetBorder "wx.richtext.TextBoxAttr.GetBorder")
    Bottom: 'TextAttrDimension'  # `Bottom`[¶](#wx.richtext.TextBoxAttr.Bottom "Permalink to this definition")See [`GetBottom`](#wx.richtext.TextBoxAttr.GetBottom "wx.richtext.TextBoxAttr.GetBottom")
    BottomBorder: 'TextAttrBorder'  # `BottomBorder`[¶](#wx.richtext.TextBoxAttr.BottomBorder "Permalink to this definition")See [`GetBottomBorder`](#wx.richtext.TextBoxAttr.GetBottomBorder "wx.richtext.TextBoxAttr.GetBottomBorder")
    BottomMargin: 'TextAttrDimension'  # `BottomMargin`[¶](#wx.richtext.TextBoxAttr.BottomMargin "Permalink to this definition")See [`GetBottomMargin`](#wx.richtext.TextBoxAttr.GetBottomMargin "wx.richtext.TextBoxAttr.GetBottomMargin")
    BottomOutline: 'TextAttrBorder'  # `BottomOutline`[¶](#wx.richtext.TextBoxAttr.BottomOutline "Permalink to this definition")See [`GetBottomOutline`](#wx.richtext.TextBoxAttr.GetBottomOutline "wx.richtext.TextBoxAttr.GetBottomOutline")
    BottomPadding: 'TextAttrDimension'  # `BottomPadding`[¶](#wx.richtext.TextBoxAttr.BottomPadding "Permalink to this definition")See [`GetBottomPadding`](#wx.richtext.TextBoxAttr.GetBottomPadding "wx.richtext.TextBoxAttr.GetBottomPadding")
    BoxStyleName: str  # `BoxStyleName`[¶](#wx.richtext.TextBoxAttr.BoxStyleName "Permalink to this definition")See [`GetBoxStyleName`](#wx.richtext.TextBoxAttr.GetBoxStyleName "wx.richtext.TextBoxAttr.GetBoxStyleName") and [`SetBoxStyleName`](#wx.richtext.TextBoxAttr.SetBoxStyleName "wx.richtext.TextBoxAttr.SetBoxStyleName")
    ClearMode: 'TextBoxAttrClearStyle'  # `ClearMode`[¶](#wx.richtext.TextBoxAttr.ClearMode "Permalink to this definition")See [`GetClearMode`](#wx.richtext.TextBoxAttr.GetClearMode "wx.richtext.TextBoxAttr.GetClearMode") and [`SetClearMode`](#wx.richtext.TextBoxAttr.SetClearMode "wx.richtext.TextBoxAttr.SetClearMode")
    CollapseBorders: 'TextBoxAttrCollapseMode'  # `CollapseBorders`[¶](#wx.richtext.TextBoxAttr.CollapseBorders "Permalink to this definition")See [`GetCollapseBorders`](#wx.richtext.TextBoxAttr.GetCollapseBorders "wx.richtext.TextBoxAttr.GetCollapseBorders") and [`SetCollapseBorders`](#wx.richtext.TextBoxAttr.SetCollapseBorders "wx.richtext.TextBoxAttr.SetCollapseBorders")
    CornerRadius: 'TextAttrDimension'  # `CornerRadius`[¶](#wx.richtext.TextBoxAttr.CornerRadius "Permalink to this definition")See [`GetCornerRadius`](#wx.richtext.TextBoxAttr.GetCornerRadius "wx.richtext.TextBoxAttr.GetCornerRadius") and [`SetCornerRadius`](#wx.richtext.TextBoxAttr.SetCornerRadius "wx.richtext.TextBoxAttr.SetCornerRadius")
    Flags: int  # `Flags`[¶](#wx.richtext.TextBoxAttr.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.TextBoxAttr.GetFlags "wx.richtext.TextBoxAttr.GetFlags") and [`SetFlags`](#wx.richtext.TextBoxAttr.SetFlags "wx.richtext.TextBoxAttr.SetFlags")
    FloatMode: 'TextBoxAttrFloatStyle'  # `FloatMode`[¶](#wx.richtext.TextBoxAttr.FloatMode "Permalink to this definition")See [`GetFloatMode`](#wx.richtext.TextBoxAttr.GetFloatMode "wx.richtext.TextBoxAttr.GetFloatMode") and [`SetFloatMode`](#wx.richtext.TextBoxAttr.SetFloatMode "wx.richtext.TextBoxAttr.SetFloatMode")
    Height: 'TextAttrDimension'  # `Height`[¶](#wx.richtext.TextBoxAttr.Height "Permalink to this definition")See [`GetHeight`](#wx.richtext.TextBoxAttr.GetHeight "wx.richtext.TextBoxAttr.GetHeight")
    Left: 'TextAttrDimension'  # `Left`[¶](#wx.richtext.TextBoxAttr.Left "Permalink to this definition")See [`GetLeft`](#wx.richtext.TextBoxAttr.GetLeft "wx.richtext.TextBoxAttr.GetLeft")
    LeftBorder: 'TextAttrBorder'  # `LeftBorder`[¶](#wx.richtext.TextBoxAttr.LeftBorder "Permalink to this definition")See [`GetLeftBorder`](#wx.richtext.TextBoxAttr.GetLeftBorder "wx.richtext.TextBoxAttr.GetLeftBorder")
    LeftMargin: 'TextAttrDimension'  # `LeftMargin`[¶](#wx.richtext.TextBoxAttr.LeftMargin "Permalink to this definition")See [`GetLeftMargin`](#wx.richtext.TextBoxAttr.GetLeftMargin "wx.richtext.TextBoxAttr.GetLeftMargin")
    LeftOutline: 'TextAttrBorder'  # `LeftOutline`[¶](#wx.richtext.TextBoxAttr.LeftOutline "Permalink to this definition")See [`GetLeftOutline`](#wx.richtext.TextBoxAttr.GetLeftOutline "wx.richtext.TextBoxAttr.GetLeftOutline")
    LeftPadding: 'TextAttrDimension'  # `LeftPadding`[¶](#wx.richtext.TextBoxAttr.LeftPadding "Permalink to this definition")See [`GetLeftPadding`](#wx.richtext.TextBoxAttr.GetLeftPadding "wx.richtext.TextBoxAttr.GetLeftPadding")
    Margins: 'TextAttrDimensions'  # `Margins`[¶](#wx.richtext.TextBoxAttr.Margins "Permalink to this definition")See [`GetMargins`](#wx.richtext.TextBoxAttr.GetMargins "wx.richtext.TextBoxAttr.GetMargins")
    MaxSize: 'TextAttrSize'  # `MaxSize`[¶](#wx.richtext.TextBoxAttr.MaxSize "Permalink to this definition")See [`GetMaxSize`](#wx.richtext.TextBoxAttr.GetMaxSize "wx.richtext.TextBoxAttr.GetMaxSize") and [`SetMaxSize`](#wx.richtext.TextBoxAttr.SetMaxSize "wx.richtext.TextBoxAttr.SetMaxSize")
    MinSize: 'TextAttrSize'  # `MinSize`[¶](#wx.richtext.TextBoxAttr.MinSize "Permalink to this definition")See [`GetMinSize`](#wx.richtext.TextBoxAttr.GetMinSize "wx.richtext.TextBoxAttr.GetMinSize") and [`SetMinSize`](#wx.richtext.TextBoxAttr.SetMinSize "wx.richtext.TextBoxAttr.SetMinSize")
    Outline: 'TextAttrBorders'  # `Outline`[¶](#wx.richtext.TextBoxAttr.Outline "Permalink to this definition")See [`GetOutline`](#wx.richtext.TextBoxAttr.GetOutline "wx.richtext.TextBoxAttr.GetOutline")
    Padding: 'TextAttrDimensions'  # `Padding`[¶](#wx.richtext.TextBoxAttr.Padding "Permalink to this definition")See [`GetPadding`](#wx.richtext.TextBoxAttr.GetPadding "wx.richtext.TextBoxAttr.GetPadding")
    Position: 'TextAttrDimensions'  # `Position`[¶](#wx.richtext.TextBoxAttr.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.TextBoxAttr.GetPosition "wx.richtext.TextBoxAttr.GetPosition")
    Right: 'TextAttrDimension'  # `Right`[¶](#wx.richtext.TextBoxAttr.Right "Permalink to this definition")See [`GetRight`](#wx.richtext.TextBoxAttr.GetRight "wx.richtext.TextBoxAttr.GetRight")
    RightBorder: 'TextAttrBorder'  # `RightBorder`[¶](#wx.richtext.TextBoxAttr.RightBorder "Permalink to this definition")See [`GetRightBorder`](#wx.richtext.TextBoxAttr.GetRightBorder "wx.richtext.TextBoxAttr.GetRightBorder")
    RightMargin: 'TextAttrDimension'  # `RightMargin`[¶](#wx.richtext.TextBoxAttr.RightMargin "Permalink to this definition")See [`GetRightMargin`](#wx.richtext.TextBoxAttr.GetRightMargin "wx.richtext.TextBoxAttr.GetRightMargin")
    RightOutline: 'TextAttrBorder'  # `RightOutline`[¶](#wx.richtext.TextBoxAttr.RightOutline "Permalink to this definition")See [`GetRightOutline`](#wx.richtext.TextBoxAttr.GetRightOutline "wx.richtext.TextBoxAttr.GetRightOutline")
    RightPadding: 'TextAttrDimension'  # `RightPadding`[¶](#wx.richtext.TextBoxAttr.RightPadding "Permalink to this definition")See [`GetRightPadding`](#wx.richtext.TextBoxAttr.GetRightPadding "wx.richtext.TextBoxAttr.GetRightPadding")
    Shadow: 'TextAttrShadow'  # `Shadow`[¶](#wx.richtext.TextBoxAttr.Shadow "Permalink to this definition")See [`GetShadow`](#wx.richtext.TextBoxAttr.GetShadow "wx.richtext.TextBoxAttr.GetShadow")
    Size: 'TextAttrSize'  # `Size`[¶](#wx.richtext.TextBoxAttr.Size "Permalink to this definition")See [`GetSize`](#wx.richtext.TextBoxAttr.GetSize "wx.richtext.TextBoxAttr.GetSize") and [`SetSize`](#wx.richtext.TextBoxAttr.SetSize "wx.richtext.TextBoxAttr.SetSize")
    Top: 'TextAttrDimension'  # `Top`[¶](#wx.richtext.TextBoxAttr.Top "Permalink to this definition")See [`GetTop`](#wx.richtext.TextBoxAttr.GetTop "wx.richtext.TextBoxAttr.GetTop")
    TopBorder: 'TextAttrBorder'  # `TopBorder`[¶](#wx.richtext.TextBoxAttr.TopBorder "Permalink to this definition")See [`GetTopBorder`](#wx.richtext.TextBoxAttr.GetTopBorder "wx.richtext.TextBoxAttr.GetTopBorder")
    TopMargin: 'TextAttrDimension'  # `TopMargin`[¶](#wx.richtext.TextBoxAttr.TopMargin "Permalink to this definition")See [`GetTopMargin`](#wx.richtext.TextBoxAttr.GetTopMargin "wx.richtext.TextBoxAttr.GetTopMargin")
    TopOutline: 'TextAttrBorder'  # `TopOutline`[¶](#wx.richtext.TextBoxAttr.TopOutline "Permalink to this definition")See [`GetTopOutline`](#wx.richtext.TextBoxAttr.GetTopOutline "wx.richtext.TextBoxAttr.GetTopOutline")
    TopPadding: 'TextAttrDimension'  # `TopPadding`[¶](#wx.richtext.TextBoxAttr.TopPadding "Permalink to this definition")See [`GetTopPadding`](#wx.richtext.TextBoxAttr.GetTopPadding "wx.richtext.TextBoxAttr.GetTopPadding")
    VerticalAlignment: int  # `VerticalAlignment`[¶](#wx.richtext.TextBoxAttr.VerticalAlignment "Permalink to this definition")See [`GetVerticalAlignment`](#wx.richtext.TextBoxAttr.GetVerticalAlignment "wx.richtext.TextBoxAttr.GetVerticalAlignment") and [`SetVerticalAlignment`](#wx.richtext.TextBoxAttr.SetVerticalAlignment "wx.richtext.TextBoxAttr.SetVerticalAlignment")
    WhitespaceMode: 'TextBoxAttrWhitespaceMode'  # `WhitespaceMode`[¶](#wx.richtext.TextBoxAttr.WhitespaceMode "Permalink to this definition")See [`GetWhitespaceMode`](#wx.richtext.TextBoxAttr.GetWhitespaceMode "wx.richtext.TextBoxAttr.GetWhitespaceMode") and [`SetWhitespaceMode`](#wx.richtext.TextBoxAttr.SetWhitespaceMode "wx.richtext.TextBoxAttr.SetWhitespaceMode")
    Width: 'TextAttrDimension'  # `Width`[¶](#wx.richtext.TextBoxAttr.Width "Permalink to this definition")See [`GetWidth`](#wx.richtext.TextBoxAttr.GetWidth "wx.richtext.TextBoxAttr.GetWidth")
    m_border: Any  # `m_border`[¶](#wx.richtext.TextBoxAttr.m_border "Permalink to this definition")A public C++ attribute of type [`TextAttrBorders`](wx.richtext.TextAttrBorders.html#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders") .
    m_boxStyleName: Any  # `m_boxStyleName`[¶](#wx.richtext.TextBoxAttr.m_boxStyleName "Permalink to this definition")A public C++ attribute of type `string`.
    m_clearMode: Any  # `m_clearMode`[¶](#wx.richtext.TextBoxAttr.m_clearMode "Permalink to this definition")A public C++ attribute of type `TextBoxAttrClearStyle` .
    m_collapseMode: Any  # `m_collapseMode`[¶](#wx.richtext.TextBoxAttr.m_collapseMode "Permalink to this definition")A public C++ attribute of type `TextBoxAttrCollapseMode` .
    m_cornerRadius: Any  # `m_cornerRadius`[¶](#wx.richtext.TextBoxAttr.m_cornerRadius "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_flags: Any  # `m_flags`[¶](#wx.richtext.TextBoxAttr.m_flags "Permalink to this definition")A public C++ attribute of type `int`.
    m_floatMode: Any  # `m_floatMode`[¶](#wx.richtext.TextBoxAttr.m_floatMode "Permalink to this definition")A public C++ attribute of type `TextBoxAttrFloatStyle` .
    m_margins: Any  # `m_margins`[¶](#wx.richtext.TextBoxAttr.m_margins "Permalink to this definition")A public C++ attribute of type [`TextAttrDimensions`](wx.richtext.TextAttrDimensions.html#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions") .
    m_maxSize: Any  # `m_maxSize`[¶](#wx.richtext.TextBoxAttr.m_maxSize "Permalink to this definition")A public C++ attribute of type [`TextAttrSize`](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize") .
    m_minSize: Any  # `m_minSize`[¶](#wx.richtext.TextBoxAttr.m_minSize "Permalink to this definition")A public C++ attribute of type [`TextAttrSize`](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize") .
    m_outline: Any  # `m_outline`[¶](#wx.richtext.TextBoxAttr.m_outline "Permalink to this definition")A public C++ attribute of type [`TextAttrBorders`](wx.richtext.TextAttrBorders.html#wx.richtext.TextAttrBorders "wx.richtext.TextAttrBorders") .
    m_padding: Any  # `m_padding`[¶](#wx.richtext.TextBoxAttr.m_padding "Permalink to this definition")A public C++ attribute of type [`TextAttrDimensions`](wx.richtext.TextAttrDimensions.html#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions") .
    m_position: Any  # `m_position`[¶](#wx.richtext.TextBoxAttr.m_position "Permalink to this definition")A public C++ attribute of type [`TextAttrDimensions`](wx.richtext.TextAttrDimensions.html#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions") .
    m_shadow: Any  # `m_shadow`[¶](#wx.richtext.TextBoxAttr.m_shadow "Permalink to this definition")A public C++ attribute of type [`TextAttrShadow`](wx.richtext.TextAttrShadow.html#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow") .
    m_size: Any  # `m_size`[¶](#wx.richtext.TextBoxAttr.m_size "Permalink to this definition")A public C++ attribute of type [`TextAttrSize`](wx.richtext.TextAttrSize.html#wx.richtext.TextAttrSize "wx.richtext.TextAttrSize") .
    m_verticalAlignment: Any  # `m_verticalAlignment`[¶](#wx.richtext.TextBoxAttr.m_verticalAlignment "Permalink to this definition")A public C++ attribute of type `TextBoxAttrVerticalAlignment` .
    m_whitespaceMode: Any  # `m_whitespaceMode`[¶](#wx.richtext.TextBoxAttr.m_whitespaceMode "Permalink to this definition")A public C++ attribute of type `TextBoxAttrWhitespaceMode` .



RichTextFileType: TypeAlias = int  # Enumeration

RICHTEXT_TYPE_TEXT: int

RICHTEXT_TYPE_XML: int

RICHTEXT_TYPE_HTML: int

RICHTEXT_TYPE_RTF: int

RICHTEXT_TYPE_PDF: int

class RichTextCell(RichTextBox):
    """ **Possible constructors**:



```
RichTextCell(parent=None)

RichTextCell(obj)

```


RichTextCell is the cell in a table, in which the user can type.


  


        Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.RichTextCell.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self, parent=None)*


Default constructor; optionally pass the parent object.



Parameters
**parent** ([*wx.richtext.RichTextObject*](wx.richtext.RichTextObject.html#wx.richtext.RichTextObject "wx.richtext.RichTextObject")) – 






---

  



**\_\_init\_\_** *(self, obj)*


Copy constructor.



Parameters
**obj** ([*wx.richtext.RichTextCell*](#wx.richtext.RichTextCell "wx.richtext.RichTextCell")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def CanEditProperties(self) -> bool:
        """ 

`CanEditProperties`(*self*)[¶](#wx.richtext.RichTextCell.CanEditProperties "Permalink to this definition")
Returns `True` if we can edit the object’s properties via a GUI.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Clone(self) -> 'RichTextObject':
        """ 

`Clone`(*self*)[¶](#wx.richtext.RichTextCell.Clone "Permalink to this definition")
Clones the object.



Return type
 [wx.richtext.RichTextObject](wx.richtext.RichTextObject.html#wx-richtext-richtextobject)






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Copy(self, obj: 'richtext.RichTextCell') -> None:
        """ 

`Copy`(*self*, *obj*)[¶](#wx.richtext.RichTextCell.Copy "Permalink to this definition")

Parameters
**obj** ([*wx.richtext.RichTextCell*](#wx.richtext.RichTextCell "wx.richtext.RichTextCell")) – 






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def Draw(self, dc, context, range, selection, rect, descent, style) -> bool:
        """ 

`Draw`(*self*, *dc*, *context*, *range*, *selection*, *rect*, *descent*, *style*)[¶](#wx.richtext.RichTextCell.Draw "Permalink to this definition")
Draw the item, within the given range.


Some objects may ignore the range (for example paragraphs) while others must obey it (lines, to implement wrapping)



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **range** ([*wx.richtext.RichTextRange*](wx.richtext.RichTextRange.html#wx.richtext.RichTextRange "wx.richtext.RichTextRange")) –
* **selection** ([*wx.richtext.RichTextSelection*](wx.richtext.RichTextSelection.html#wx.richtext.RichTextSelection "wx.richtext.RichTextSelection")) –
* **rect** ([*wx.Rect*](wx.Rect.html#wx.Rect "wx.Rect")) –
* **descent** (*int*) –
* **style** (*int*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def EditProperties(self, parent, buffer) -> bool:
        """ 

`EditProperties`(*self*, *parent*, *buffer*)[¶](#wx.richtext.RichTextCell.EditProperties "Permalink to this definition")
Edits the object’s properties via a GUI.



Parameters
* **parent** ([*wx.Window*](wx.Window.html#wx.Window "wx.Window")) –
* **buffer** ([*wx.richtext.RichTextBuffer*](wx.richtext.RichTextBuffer.html#wx.richtext.RichTextBuffer "wx.richtext.RichTextBuffer")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetColSpan(self) -> int:
        """ 

`GetColSpan`(*self*)[¶](#wx.richtext.RichTextCell.GetColSpan "Permalink to this definition")
Returns the number of columns spanned by the cell.


By default a cell doesn’t span extra columns, so this function returns 1.



Return type
*int*





New in version 2.9.5.




See also


[`SetColSpan`](#wx.richtext.RichTextCell.SetColSpan "wx.richtext.RichTextCell.SetColSpan") , [`GetRowSpan`](#wx.richtext.RichTextCell.GetRowSpan "wx.richtext.RichTextCell.GetRowSpan")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetPropertiesMenuLabel(self) -> str:
        """ 

`GetPropertiesMenuLabel`(*self*)[¶](#wx.richtext.RichTextCell.GetPropertiesMenuLabel "Permalink to this definition")
Returns the label to be used for the properties context menu item.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetRowSpan(self) -> int:
        """ 

`GetRowSpan`(*self*)[¶](#wx.richtext.RichTextCell.GetRowSpan "Permalink to this definition")
Returns the number of rows spanned by the cell.


By default a cell doesn’t span extra rows, so this function returns 1.



Return type
*int*





New in version 2.9.5.




See also


[`SetRowSpan`](#wx.richtext.RichTextCell.SetRowSpan "wx.richtext.RichTextCell.SetRowSpan") , [`GetColSpan`](#wx.richtext.RichTextCell.GetColSpan "wx.richtext.RichTextCell.GetColSpan")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def GetXMLNodeName(self) -> str:
        """ 

`GetXMLNodeName`(*self*)[¶](#wx.richtext.RichTextCell.GetXMLNodeName "Permalink to this definition")
Returns the `XML` node name of this object.


This must be overridden for XmlNode-base `XML` export to work.



Return type
`string`






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def HitTest(self, dc, context, pt, flags=0) -> tuple:
        """ 

`HitTest`(*self*, *dc*, *context*, *pt*, *flags=0*)[¶](#wx.richtext.RichTextCell.HitTest "Permalink to this definition")
Hit-testing: returns a flag indicating hit test details, plus information about position.


*contextObj* is returned to specify what object position is relevant to, since otherwise there’s an ambiguity. @ obj might not be a child of *contextObj*, since we may be referring to the container itself if we have no hit on a child - for example if we click outside an object.


The function puts the position in *textPosition* if one is found. *pt* is in logical units (a zero y position is at the beginning of the buffer).



Parameters
* **dc** ([*wx.DC*](wx.DC.html#wx.DC "wx.DC")) –
* **context** ([*wx.richtext.RichTextDrawingContext*](wx.richtext.RichTextDrawingContext.html#wx.richtext.RichTextDrawingContext "wx.richtext.RichTextDrawingContext")) –
* **pt** ([*wx.Point*](wx.Point.html#wx.Point "wx.Point")) –
* **flags** (*int*) –



Return type
*tuple*



Returns
( *int*, *textPosition*, *obj*, *contextObj* )






            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def SetColSpan(self, span: int) -> None:
        """ 

`SetColSpan`(*self*, *span*)[¶](#wx.richtext.RichTextCell.SetColSpan "Permalink to this definition")
Set the number of columns spanned by the cell.


By default colspan is 1 i.e. a cell doesn’t span extra columns. Pass a value >1 to change this. Attempting to set a colspan <1 will assert and be ignored.



Parameters
**span** (*long*) – 





New in version 2.9.5.




See also


[`GetColSpan`](#wx.richtext.RichTextCell.GetColSpan "wx.richtext.RichTextCell.GetColSpan") , [`SetRowSpan`](#wx.richtext.RichTextCell.SetRowSpan "wx.richtext.RichTextCell.SetRowSpan")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    def SetRowSpan(self, span: int) -> None:
        """ 

`SetRowSpan`(*self*, *span*)[¶](#wx.richtext.RichTextCell.SetRowSpan "Permalink to this definition")
Set the number of rows spanned by the cell.


By default colspan is 1 i.e. a cell doesn’t span extra rows. Pass a value >1 to change this. Attempting to set a rowspan <1 will assert and be ignored.



Parameters
**span** (*long*) – 





New in version 2.9.5.




See also


[`GetRowSpan`](#wx.richtext.RichTextCell.GetRowSpan "wx.richtext.RichTextCell.GetRowSpan") , [`SetColSpan`](#wx.richtext.RichTextCell.SetColSpan "wx.richtext.RichTextCell.SetColSpan")





            Source: https://docs.wxpython.org/wx.richtext.RichTextCell.html
        """

    ColSpan: int  # `ColSpan`[¶](#wx.richtext.RichTextCell.ColSpan "Permalink to this definition")See [`GetColSpan`](#wx.richtext.RichTextCell.GetColSpan "wx.richtext.RichTextCell.GetColSpan") and [`SetColSpan`](#wx.richtext.RichTextCell.SetColSpan "wx.richtext.RichTextCell.SetColSpan")
    PropertiesMenuLabel: str  # `PropertiesMenuLabel`[¶](#wx.richtext.RichTextCell.PropertiesMenuLabel "Permalink to this definition")See [`GetPropertiesMenuLabel`](#wx.richtext.RichTextCell.GetPropertiesMenuLabel "wx.richtext.RichTextCell.GetPropertiesMenuLabel")
    RowSpan: int  # `RowSpan`[¶](#wx.richtext.RichTextCell.RowSpan "Permalink to this definition")See [`GetRowSpan`](#wx.richtext.RichTextCell.GetRowSpan "wx.richtext.RichTextCell.GetRowSpan") and [`SetRowSpan`](#wx.richtext.RichTextCell.SetRowSpan "wx.richtext.RichTextCell.SetRowSpan")
    XMLNodeName: str  # `XMLNodeName`[¶](#wx.richtext.RichTextCell.XMLNodeName "Permalink to this definition")See [`GetXMLNodeName`](#wx.richtext.RichTextCell.GetXMLNodeName "wx.richtext.RichTextCell.GetXMLNodeName")



class TextAttrBorder:
    """ **Possible constructors**:



```
TextAttrBorder()

```


A class representing a rich text object border.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.TextAttrBorder.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def AddFlag(self, flag: int) -> None:
        """ 

`AddFlag`(*self*, *flag*)[¶](#wx.richtext.TextAttrBorder.AddFlag "Permalink to this definition")
Adds a border flag.



Parameters
**flag** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def Apply(self, border, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *border*, *compareWith=None*)[¶](#wx.richtext.TextAttrBorder.Apply "Permalink to this definition")
Applies the border to this object, but not if the same as *compareWith*.



Parameters
* **border** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –
* **compareWith** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrBorder.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –
* **clashingAttr** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –
* **absentAttr** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def EqPartial(self, border, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *border*, *weakTest=True*)[¶](#wx.richtext.TextAttrBorder.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *border* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *border* but not in this object.



Parameters
* **border** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetColour(self) -> 'Colour':
        """ 

`GetColour`(*self*)[¶](#wx.richtext.TextAttrBorder.GetColour "Permalink to this definition")
Gets the colour.



Return type
[`Colour`](#wx.richtext.TextAttrBorder.Colour "wx.richtext.TextAttrBorder.Colour")






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetColourLong(self) -> int:
        """ 

`GetColourLong`(*self*)[¶](#wx.richtext.TextAttrBorder.GetColourLong "Permalink to this definition")
Gets the colour as a long.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.TextAttrBorder.GetFlags "Permalink to this definition")
Returns the border flags.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetStyle(self) -> int:
        """ 

`GetStyle`(*self*)[¶](#wx.richtext.TextAttrBorder.GetStyle "Permalink to this definition")
Gets the border style.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def GetWidth(self) -> 'TextAttrDimension':
        """ 

`GetWidth`(*self*)[¶](#wx.richtext.TextAttrBorder.GetWidth "Permalink to this definition")
Gets the border width.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasColour(self) -> bool:
        """ 

`HasColour`(*self*)[¶](#wx.richtext.TextAttrBorder.HasColour "Permalink to this definition")
True if the border has a valid colour.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasStyle(self) -> bool:
        """ 

`HasStyle`(*self*)[¶](#wx.richtext.TextAttrBorder.HasStyle "Permalink to this definition")
True if the border has a valid style.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def HasWidth(self) -> bool:
        """ 

`HasWidth`(*self*)[¶](#wx.richtext.TextAttrBorder.HasWidth "Permalink to this definition")
True if the border has a valid width.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def IsDefault(self) -> bool:
        """ 

`IsDefault`(*self*)[¶](#wx.richtext.TextAttrBorder.IsDefault "Permalink to this definition")
True if the border has no attributes set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrBorder.IsValid "Permalink to this definition")
True if the border is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def MakeValid(self) -> None:
        """ 

`MakeValid`(*self*)[¶](#wx.richtext.TextAttrBorder.MakeValid "Permalink to this definition")
Set the valid flag for this border.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def RemoveFlag(self, flag: int) -> None:
        """ 

`RemoveFlag`(*self*, *flag*)[¶](#wx.richtext.TextAttrBorder.RemoveFlag "Permalink to this definition")
Removes a border flag.



Parameters
**flag** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrBorder') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextAttrBorder.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrBorder.Reset "Permalink to this definition")
Resets the border style, colour, width and flags.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ 

`SetColour`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrBorder.SetColour "Permalink to this definition")
Sets the border colour.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetColour** *(self, colour)*



Parameters
**colour** (*long*) – 






---

  



**SetColour** *(self, colour)*



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.TextAttrBorder.SetFlags "Permalink to this definition")
Sets the border flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetStyle(self, style: int) -> None:
        """ 

`SetStyle`(*self*, *style*)[¶](#wx.richtext.TextAttrBorder.SetStyle "Permalink to this definition")
Sets the border style.



Parameters
**style** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def SetWidth(self, *args, **kw) -> None:
        """ 

`SetWidth`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrBorder.SetWidth "Permalink to this definition")
Sets the border width.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetWidth** *(self, width)*



Parameters
**width** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






---

  



**SetWidth** *(self, value, units=TEXT\_ATTR\_UNITS\_TENTHS\_MM)*



Parameters
* **value** (*int*) –
* **units** ([*TextAttrUnits*](wx.richtext.TextAttrUnits.enumeration.html "TextAttrUnits")) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.TextAttrBorder.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.TextAttrBorder.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrBorder.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**border** ([*wx.richtext.TextAttrBorder*](#wx.richtext.TextAttrBorder "wx.richtext.TextAttrBorder")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrBorder.html
        """

    Colour: '_Colour'  # `Colour`[¶](#wx.richtext.TextAttrBorder.Colour "Permalink to this definition")See [`GetColour`](#wx.richtext.TextAttrBorder.GetColour "wx.richtext.TextAttrBorder.GetColour") and [`SetColour`](#wx.richtext.TextAttrBorder.SetColour "wx.richtext.TextAttrBorder.SetColour")
    ColourLong: int  # `ColourLong`[¶](#wx.richtext.TextAttrBorder.ColourLong "Permalink to this definition")See [`GetColourLong`](#wx.richtext.TextAttrBorder.GetColourLong "wx.richtext.TextAttrBorder.GetColourLong")
    Flags: int  # `Flags`[¶](#wx.richtext.TextAttrBorder.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.TextAttrBorder.GetFlags "wx.richtext.TextAttrBorder.GetFlags") and [`SetFlags`](#wx.richtext.TextAttrBorder.SetFlags "wx.richtext.TextAttrBorder.SetFlags")
    Style: int  # `Style`[¶](#wx.richtext.TextAttrBorder.Style "Permalink to this definition")See [`GetStyle`](#wx.richtext.TextAttrBorder.GetStyle "wx.richtext.TextAttrBorder.GetStyle") and [`SetStyle`](#wx.richtext.TextAttrBorder.SetStyle "wx.richtext.TextAttrBorder.SetStyle")
    Width: 'TextAttrDimension'  # `Width`[¶](#wx.richtext.TextAttrBorder.Width "Permalink to this definition")See [`GetWidth`](#wx.richtext.TextAttrBorder.GetWidth "wx.richtext.TextAttrBorder.GetWidth") and [`SetWidth`](#wx.richtext.TextAttrBorder.SetWidth "wx.richtext.TextAttrBorder.SetWidth")
    m_borderColour: Any  # `m_borderColour`[¶](#wx.richtext.TextAttrBorder.m_borderColour "Permalink to this definition")A public C++ attribute of type `long`.
    m_borderStyle: Any  # `m_borderStyle`[¶](#wx.richtext.TextAttrBorder.m_borderStyle "Permalink to this definition")A public C++ attribute of type `int`.
    m_borderWidth: Any  # `m_borderWidth`[¶](#wx.richtext.TextAttrBorder.m_borderWidth "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_flags: Any  # `m_flags`[¶](#wx.richtext.TextAttrBorder.m_flags "Permalink to this definition")A public C++ attribute of type `int`.



class TextAttrDimension:
    """ **Possible constructors**:



```
TextAttrDimension()

TextAttrDimension(value, units=TEXT_ATTR_UNITS_TENTHS_MM)

```


A class representing a rich text dimension, including units and
position.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
    """
    def __init__(self, *args, **kw) -> None:
        """ 

`__init__`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrDimension.__init__ "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**\_\_init\_\_** *(self)*


Default constructor.




---

  



**\_\_init\_\_** *(self, value, units=TEXT\_ATTR\_UNITS\_TENTHS\_MM)*


Constructor taking value and units flag.



Parameters
* **value** (*int*) –
* **units** ([*TextAttrUnits*](wx.richtext.TextAttrUnits.enumeration.html "TextAttrUnits")) –






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def Apply(self, dim, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *dim*, *compareWith=None*)[¶](#wx.richtext.TextAttrDimension.Apply "Permalink to this definition")
Apply the dimension, but not those identical to *compareWith* if present.



Parameters
* **dim** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –
* **compareWith** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrDimension.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –
* **clashingAttr** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –
* **absentAttr** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def EqPartial(self, dim, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *dim*, *weakTest=True*)[¶](#wx.richtext.TextAttrDimension.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *dim* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *dim* but not in this object.



Parameters
* **dim** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetFlags(self) -> 'TextAttrDimensionFlags':
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.TextAttrDimension.GetFlags "Permalink to this definition")
Gets the dimension flags.



Return type
*wx.richtext.TextAttrDimensionFlags*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetPosition(self) -> 'TextBoxAttrPosition':
        """ 

`GetPosition`(*self*)[¶](#wx.richtext.TextAttrDimension.GetPosition "Permalink to this definition")
Gets the position flags.



Return type
 [wx.richtext.TextBoxAttrPosition](wx.richtext.TextBoxAttrPosition.enumeration.html#wx-richtext-textboxattrposition)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetUnits(self) -> 'TextAttrUnits':
        """ 

`GetUnits`(*self*)[¶](#wx.richtext.TextAttrDimension.GetUnits "Permalink to this definition")
Gets the units of the dimension.



Return type
 [wx.richtext.TextAttrUnits](wx.richtext.TextAttrUnits.enumeration.html#wx-richtext-textattrunits)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetValue(self) -> int:
        """ 

`GetValue`(*self*)[¶](#wx.richtext.TextAttrDimension.GetValue "Permalink to this definition")
Returns the integer value of the dimension.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def GetValueMM(self) -> float:
        """ 

`GetValueMM`(*self*)[¶](#wx.richtext.TextAttrDimension.GetValueMM "Permalink to this definition")
Returns the floating-pointing value of the dimension in mm.



Return type
*float*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrDimension.IsValid "Permalink to this definition")
Returns `True` if the dimension is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrDimension.Reset "Permalink to this definition")
Resets the dimension value and flags.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetFlags(self, flags: 'richtext.TextAttrDimensionFlags') -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.TextAttrDimension.SetFlags "Permalink to this definition")
Sets the dimension flags.



Parameters
**flags** (*wx.richtext.TextAttrDimensionFlags*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetPosition(self, pos: TextBoxAttrPosition) -> None:
        """ 

`SetPosition`(*self*, *pos*)[¶](#wx.richtext.TextAttrDimension.SetPosition "Permalink to this definition")
Sets the position flags.



Parameters
**pos** ([*TextBoxAttrPosition*](wx.richtext.TextBoxAttrPosition.enumeration.html "TextBoxAttrPosition")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetUnits(self, units: TextAttrUnits) -> None:
        """ 

`SetUnits`(*self*, *units*)[¶](#wx.richtext.TextAttrDimension.SetUnits "Permalink to this definition")
Sets the units of the dimension.



Parameters
**units** ([*TextAttrUnits*](wx.richtext.TextAttrUnits.enumeration.html "TextAttrUnits")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValid(self, b: bool) -> None:
        """ 

`SetValid`(*self*, *b*)[¶](#wx.richtext.TextAttrDimension.SetValid "Permalink to this definition")
Sets the valid flag.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValue(self, *args, **kw) -> None:
        """ 

`SetValue`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrDimension.SetValue "Permalink to this definition")
[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetValue** *(self, value)*


Sets the integer value of the dimension.



Parameters
**value** (*int*) – 






---

  



**SetValue** *(self, value, flags)*


Sets the integer value of the dimension, passing dimension flags.



Parameters
* **value** (*int*) –
* **flags** (*wx.richtext.TextAttrDimensionFlags*) –






---

  



**SetValue** *(self, dim)*


Sets the dimension.



Parameters
**dim** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def SetValueMM(self, value: float) -> None:
        """ 

`SetValueMM`(*self*, *value*)[¶](#wx.richtext.TextAttrDimension.SetValueMM "Permalink to this definition")
Sets the value of the dimension in mm.



Parameters
**value** (*float*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.TextAttrDimension.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.TextAttrDimension.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrDimension.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**dim** ([*wx.richtext.TextAttrDimension*](#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimension.html
        """

    Flags: 'TextAttrDimensionFlags'  # `Flags`[¶](#wx.richtext.TextAttrDimension.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.TextAttrDimension.GetFlags "wx.richtext.TextAttrDimension.GetFlags") and [`SetFlags`](#wx.richtext.TextAttrDimension.SetFlags "wx.richtext.TextAttrDimension.SetFlags")
    Position: 'TextBoxAttrPosition'  # `Position`[¶](#wx.richtext.TextAttrDimension.Position "Permalink to this definition")See [`GetPosition`](#wx.richtext.TextAttrDimension.GetPosition "wx.richtext.TextAttrDimension.GetPosition") and [`SetPosition`](#wx.richtext.TextAttrDimension.SetPosition "wx.richtext.TextAttrDimension.SetPosition")
    Units: 'TextAttrUnits'  # `Units`[¶](#wx.richtext.TextAttrDimension.Units "Permalink to this definition")See [`GetUnits`](#wx.richtext.TextAttrDimension.GetUnits "wx.richtext.TextAttrDimension.GetUnits") and [`SetUnits`](#wx.richtext.TextAttrDimension.SetUnits "wx.richtext.TextAttrDimension.SetUnits")
    Value: int  # `Value`[¶](#wx.richtext.TextAttrDimension.Value "Permalink to this definition")See [`GetValue`](#wx.richtext.TextAttrDimension.GetValue "wx.richtext.TextAttrDimension.GetValue") and [`SetValue`](#wx.richtext.TextAttrDimension.SetValue "wx.richtext.TextAttrDimension.SetValue")
    ValueMM: float  # `ValueMM`[¶](#wx.richtext.TextAttrDimension.ValueMM "Permalink to this definition")See [`GetValueMM`](#wx.richtext.TextAttrDimension.GetValueMM "wx.richtext.TextAttrDimension.GetValueMM") and [`SetValueMM`](#wx.richtext.TextAttrDimension.SetValueMM "wx.richtext.TextAttrDimension.SetValueMM")
    m_flags: Any  # `m_flags`[¶](#wx.richtext.TextAttrDimension.m_flags "Permalink to this definition")A public C++ attribute of type *TextAttrDimensionFlags* .
    m_value: Any  # `m_value`[¶](#wx.richtext.TextAttrDimension.m_value "Permalink to this definition")A public C++ attribute of type `int`.



TextAttrUnits: TypeAlias = int  # Enumeration

TEXT_ATTR_UNITS_TENTHS_MM: int

TEXT_ATTR_UNITS_PIXELS: int

TEXT_ATTR_UNITS_PERCENTAGE: int

TEXT_ATTR_UNITS_POINTS: int

TEXT_ATTR_UNITS_HUNDREDTHS_POINT: int

TEXT_ATTR_UNITS_MASK: int

class TextAttrDimensions:
    """ **Possible constructors**:



```
TextAttrDimensions()

```


A class for left, right, top and bottom dimensions.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.TextAttrDimensions.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def Apply(self, dims, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *dims*, *compareWith=None*)[¶](#wx.richtext.TextAttrDimensions.Apply "Permalink to this definition")
Apply to ‘this’, but not if the same as *compareWith*.



Parameters
* **dims** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –
* **compareWith** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrDimensions.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –
* **clashingAttr** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –
* **absentAttr** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def EqPartial(self, dims, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *dims*, *weakTest=True*)[¶](#wx.richtext.TextAttrDimensions.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *dims* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *dims* but not in this object.



Parameters
* **dims** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetBottom(self) -> 'TextAttrDimension':
        """ 

`GetBottom`(*self*)[¶](#wx.richtext.TextAttrDimensions.GetBottom "Permalink to this definition")

Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetLeft(self) -> 'TextAttrDimension':
        """ 

`GetLeft`(*self*)[¶](#wx.richtext.TextAttrDimensions.GetLeft "Permalink to this definition")

Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetRight(self) -> 'TextAttrDimension':
        """ 

`GetRight`(*self*)[¶](#wx.richtext.TextAttrDimensions.GetRight "Permalink to this definition")

Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def GetTop(self) -> 'TextAttrDimension':
        """ 

`GetTop`(*self*)[¶](#wx.richtext.TextAttrDimensions.GetTop "Permalink to this definition")

Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrDimensions.IsValid "Permalink to this definition")
Are all dimensions valid?



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrDimensions') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextAttrDimensions.RemoveStyle "Permalink to this definition")
Remove specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrDimensions.Reset "Permalink to this definition")
Resets the value and flags for all dimensions.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __bool__(self) -> int:
        """ 

`__bool__`(*self*)[¶](#wx.richtext.TextAttrDimensions.__bool__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __nonzero__(self) -> int:
        """ 

`__nonzero__`(*self*)[¶](#wx.richtext.TextAttrDimensions.__nonzero__ "Permalink to this definition")

Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrDimensions.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**dims** ([*wx.richtext.TextAttrDimensions*](#wx.richtext.TextAttrDimensions "wx.richtext.TextAttrDimensions")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrDimensions.html
        """

    Bottom: 'TextAttrDimension'  # `Bottom`[¶](#wx.richtext.TextAttrDimensions.Bottom "Permalink to this definition")See [`GetBottom`](#wx.richtext.TextAttrDimensions.GetBottom "wx.richtext.TextAttrDimensions.GetBottom")
    Left: 'TextAttrDimension'  # `Left`[¶](#wx.richtext.TextAttrDimensions.Left "Permalink to this definition")See [`GetLeft`](#wx.richtext.TextAttrDimensions.GetLeft "wx.richtext.TextAttrDimensions.GetLeft")
    Right: 'TextAttrDimension'  # `Right`[¶](#wx.richtext.TextAttrDimensions.Right "Permalink to this definition")See [`GetRight`](#wx.richtext.TextAttrDimensions.GetRight "wx.richtext.TextAttrDimensions.GetRight")
    Top: 'TextAttrDimension'  # `Top`[¶](#wx.richtext.TextAttrDimensions.Top "Permalink to this definition")See [`GetTop`](#wx.richtext.TextAttrDimensions.GetTop "wx.richtext.TextAttrDimensions.GetTop")
    m_bottom: Any  # `m_bottom`[¶](#wx.richtext.TextAttrDimensions.m_bottom "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_left: Any  # `m_left`[¶](#wx.richtext.TextAttrDimensions.m_left "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_right: Any  # `m_right`[¶](#wx.richtext.TextAttrDimensions.m_right "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_top: Any  # `m_top`[¶](#wx.richtext.TextAttrDimensions.m_top "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .



class TextAttrShadow:
    """ **Possible constructors**:



```
TextAttrShadow()

```


A class representing a shadow.


  


        Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
    """
    def __init__(self) -> None:
        """ 

`__init__`(*self*)[¶](#wx.richtext.TextAttrShadow.__init__ "Permalink to this definition")
Default constructor.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def AddFlag(self, flag: int) -> None:
        """ 

`AddFlag`(*self*, *flag*)[¶](#wx.richtext.TextAttrShadow.AddFlag "Permalink to this definition")
Adds a border flag.



Parameters
**flag** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def Apply(self, shadow, compareWith=None) -> bool:
        """ 

`Apply`(*self*, *shadow*, *compareWith=None*)[¶](#wx.richtext.TextAttrShadow.Apply "Permalink to this definition")
Applies the border to this object, but not if the same as *compareWith*.



Parameters
* **shadow** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –
* **compareWith** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def CollectCommonAttributes(self, attr, clashingAttr, absentAttr) -> None:
        """ 

`CollectCommonAttributes`(*self*, *attr*, *clashingAttr*, *absentAttr*)[¶](#wx.richtext.TextAttrShadow.CollectCommonAttributes "Permalink to this definition")
Collects the attributes that are common to a range of content, building up a note of which attributes are absent in some objects and which clash in some objects.



Parameters
* **attr** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –
* **clashingAttr** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –
* **absentAttr** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def EqPartial(self, shadow, weakTest=True) -> bool:
        """ 

`EqPartial`(*self*, *shadow*, *weakTest=True*)[¶](#wx.richtext.TextAttrShadow.EqPartial "Permalink to this definition")
Partial equality test.


If *weakTest* is `True`, attributes of this object do not have to be present if those attributes of *border* are present. If *weakTest* is `False`, the function will fail if an attribute is present in *border* but not in this object.



Parameters
* **shadow** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) –
* **weakTest** (*bool*) –



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetBlurDistance(self) -> 'TextAttrDimension':
        """ 

`GetBlurDistance`(*self*)[¶](#wx.richtext.TextAttrShadow.GetBlurDistance "Permalink to this definition")
Gets the shadow blur distance.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetColour(self) -> 'Colour':
        """ 

`GetColour`(*self*)[¶](#wx.richtext.TextAttrShadow.GetColour "Permalink to this definition")
Gets the colour.



Return type
[`Colour`](#wx.richtext.TextAttrShadow.Colour "wx.richtext.TextAttrShadow.Colour")






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetColourLong(self) -> int:
        """ 

`GetColourLong`(*self*)[¶](#wx.richtext.TextAttrShadow.GetColourLong "Permalink to this definition")
Gets the colour as a long.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetFlags(self) -> int:
        """ 

`GetFlags`(*self*)[¶](#wx.richtext.TextAttrShadow.GetFlags "Permalink to this definition")
Returns the border flags.



Return type
*int*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOffsetX(self) -> 'TextAttrDimension':
        """ 

`GetOffsetX`(*self*)[¶](#wx.richtext.TextAttrShadow.GetOffsetX "Permalink to this definition")
Gets the shadow horizontal offset.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOffsetY(self) -> 'TextAttrDimension':
        """ 

`GetOffsetY`(*self*)[¶](#wx.richtext.TextAttrShadow.GetOffsetY "Permalink to this definition")
Gets the shadow vertical offset.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetOpacity(self) -> 'TextAttrDimension':
        """ 

`GetOpacity`(*self*)[¶](#wx.richtext.TextAttrShadow.GetOpacity "Permalink to this definition")
Gets the shadow opacity.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def GetSpread(self) -> 'TextAttrDimension':
        """ 

`GetSpread`(*self*)[¶](#wx.richtext.TextAttrShadow.GetSpread "Permalink to this definition")
Gets the shadow spread size.



Return type
 [wx.richtext.TextAttrDimension](wx.richtext.TextAttrDimension.html#wx-richtext-textattrdimension)






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def HasColour(self) -> bool:
        """ 

`HasColour`(*self*)[¶](#wx.richtext.TextAttrShadow.HasColour "Permalink to this definition")
True if the shadow has a valid colour.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def IsDefault(self) -> bool:
        """ 

`IsDefault`(*self*)[¶](#wx.richtext.TextAttrShadow.IsDefault "Permalink to this definition")
True if the shadow has no attributes set.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def IsValid(self) -> bool:
        """ 

`IsValid`(*self*)[¶](#wx.richtext.TextAttrShadow.IsValid "Permalink to this definition")
Returns `True` if the dimension is valid.



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def RemoveFlag(self, flag: int) -> None:
        """ 

`RemoveFlag`(*self*, *flag*)[¶](#wx.richtext.TextAttrShadow.RemoveFlag "Permalink to this definition")
Removes a border flag.



Parameters
**flag** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def RemoveStyle(self, attr: 'richtext.TextAttrShadow') -> bool:
        """ 

`RemoveStyle`(*self*, *attr*)[¶](#wx.richtext.TextAttrShadow.RemoveStyle "Permalink to this definition")
Removes the specified attributes from this object.



Parameters
**attr** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) – 



Return type
*bool*






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def Reset(self) -> None:
        """ 

`Reset`(*self*)[¶](#wx.richtext.TextAttrShadow.Reset "Permalink to this definition")
Resets the shadow.




            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetBlurDistance(self, blur: 'richtext.TextAttrDimension') -> None:
        """ 

`SetBlurDistance`(*self*, *blur*)[¶](#wx.richtext.TextAttrShadow.SetBlurDistance "Permalink to this definition")
Sets the shadow blur distance.



Parameters
**blur** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetColour(self, *args, **kw) -> None:
        """ 

`SetColour`(*self*, *\*args*, *\*\*kw*)[¶](#wx.richtext.TextAttrShadow.SetColour "Permalink to this definition")
Sets the shadow colour.


[![overload](_images/overload.png)](_images/overload.png) **Overloaded Implementations:**




---

  



**SetColour** *(self, colour)*



Parameters
**colour** (*long*) – 






---

  



**SetColour** *(self, colour)*



Parameters
**colour** ([*wx.Colour*](wx.Colour.html#wx.Colour "wx.Colour")) – 






---

  





            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetFlags(self, flags: int) -> None:
        """ 

`SetFlags`(*self*, *flags*)[¶](#wx.richtext.TextAttrShadow.SetFlags "Permalink to this definition")
Sets the border flags.



Parameters
**flags** (*int*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOffsetX(self, offset: 'richtext.TextAttrDimension') -> None:
        """ 

`SetOffsetX`(*self*, *offset*)[¶](#wx.richtext.TextAttrShadow.SetOffsetX "Permalink to this definition")
Sets the shadow horizontal offset.



Parameters
**offset** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOffsetY(self, offset: 'richtext.TextAttrDimension') -> None:
        """ 

`SetOffsetY`(*self*, *offset*)[¶](#wx.richtext.TextAttrShadow.SetOffsetY "Permalink to this definition")
Sets the shadow vertical offset.



Parameters
**offset** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetOpacity(self, opacity: 'richtext.TextAttrDimension') -> None:
        """ 

`SetOpacity`(*self*, *opacity*)[¶](#wx.richtext.TextAttrShadow.SetOpacity "Permalink to this definition")
Sets the shadow opacity.



Parameters
**opacity** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetSpread(self, spread: 'richtext.TextAttrDimension') -> None:
        """ 

`SetSpread`(*self*, *spread*)[¶](#wx.richtext.TextAttrShadow.SetSpread "Permalink to this definition")
Sets the shadow spread size.



Parameters
**spread** ([*wx.richtext.TextAttrDimension*](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def SetValid(self, b: bool) -> None:
        """ 

`SetValid`(*self*, *b*)[¶](#wx.richtext.TextAttrShadow.SetValid "Permalink to this definition")
Sets the valid flag.



Parameters
**b** (*bool*) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    def __eq__(self, item: Any) -> bool:
        """ 

`__eq__`(*self*)[¶](#wx.richtext.TextAttrShadow.__eq__ "Permalink to this definition")
Equality operator.



Parameters
**shadow** ([*wx.richtext.TextAttrShadow*](#wx.richtext.TextAttrShadow "wx.richtext.TextAttrShadow")) – 






            Source: https://docs.wxpython.org/wx.richtext.TextAttrShadow.html
        """

    BlurDistance: 'TextAttrDimension'  # `BlurDistance`[¶](#wx.richtext.TextAttrShadow.BlurDistance "Permalink to this definition")See [`GetBlurDistance`](#wx.richtext.TextAttrShadow.GetBlurDistance "wx.richtext.TextAttrShadow.GetBlurDistance") and [`SetBlurDistance`](#wx.richtext.TextAttrShadow.SetBlurDistance "wx.richtext.TextAttrShadow.SetBlurDistance")
    Colour: '_Colour'  # `Colour`[¶](#wx.richtext.TextAttrShadow.Colour "Permalink to this definition")See [`GetColour`](#wx.richtext.TextAttrShadow.GetColour "wx.richtext.TextAttrShadow.GetColour") and [`SetColour`](#wx.richtext.TextAttrShadow.SetColour "wx.richtext.TextAttrShadow.SetColour")
    ColourLong: int  # `ColourLong`[¶](#wx.richtext.TextAttrShadow.ColourLong "Permalink to this definition")See [`GetColourLong`](#wx.richtext.TextAttrShadow.GetColourLong "wx.richtext.TextAttrShadow.GetColourLong")
    Flags: int  # `Flags`[¶](#wx.richtext.TextAttrShadow.Flags "Permalink to this definition")See [`GetFlags`](#wx.richtext.TextAttrShadow.GetFlags "wx.richtext.TextAttrShadow.GetFlags") and [`SetFlags`](#wx.richtext.TextAttrShadow.SetFlags "wx.richtext.TextAttrShadow.SetFlags")
    OffsetX: 'TextAttrDimension'  # `OffsetX`[¶](#wx.richtext.TextAttrShadow.OffsetX "Permalink to this definition")See [`GetOffsetX`](#wx.richtext.TextAttrShadow.GetOffsetX "wx.richtext.TextAttrShadow.GetOffsetX") and [`SetOffsetX`](#wx.richtext.TextAttrShadow.SetOffsetX "wx.richtext.TextAttrShadow.SetOffsetX")
    OffsetY: 'TextAttrDimension'  # `OffsetY`[¶](#wx.richtext.TextAttrShadow.OffsetY "Permalink to this definition")See [`GetOffsetY`](#wx.richtext.TextAttrShadow.GetOffsetY "wx.richtext.TextAttrShadow.GetOffsetY") and [`SetOffsetY`](#wx.richtext.TextAttrShadow.SetOffsetY "wx.richtext.TextAttrShadow.SetOffsetY")
    Opacity: 'TextAttrDimension'  # `Opacity`[¶](#wx.richtext.TextAttrShadow.Opacity "Permalink to this definition")See [`GetOpacity`](#wx.richtext.TextAttrShadow.GetOpacity "wx.richtext.TextAttrShadow.GetOpacity") and [`SetOpacity`](#wx.richtext.TextAttrShadow.SetOpacity "wx.richtext.TextAttrShadow.SetOpacity")
    Spread: 'TextAttrDimension'  # `Spread`[¶](#wx.richtext.TextAttrShadow.Spread "Permalink to this definition")See [`GetSpread`](#wx.richtext.TextAttrShadow.GetSpread "wx.richtext.TextAttrShadow.GetSpread") and [`SetSpread`](#wx.richtext.TextAttrShadow.SetSpread "wx.richtext.TextAttrShadow.SetSpread")
    m_blurDistance: Any  # `m_blurDistance`[¶](#wx.richtext.TextAttrShadow.m_blurDistance "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_flags: Any  # `m_flags`[¶](#wx.richtext.TextAttrShadow.m_flags "Permalink to this definition")A public C++ attribute of type `int`.
    m_offsetX: Any  # `m_offsetX`[¶](#wx.richtext.TextAttrShadow.m_offsetX "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_offsetY: Any  # `m_offsetY`[¶](#wx.richtext.TextAttrShadow.m_offsetY "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_opacity: Any  # `m_opacity`[¶](#wx.richtext.TextAttrShadow.m_opacity "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .
    m_shadowColour: Any  # `m_shadowColour`[¶](#wx.richtext.TextAttrShadow.m_shadowColour "Permalink to this definition")A public C++ attribute of type `long`.
    m_spread: Any  # `m_spread`[¶](#wx.richtext.TextAttrShadow.m_spread "Permalink to this definition")A public C++ attribute of type [`TextAttrDimension`](wx.richtext.TextAttrDimension.html#wx.richtext.TextAttrDimension "wx.richtext.TextAttrDimension") .



TextBoxAttrFlags: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_FLOAT: int

TEXT_BOX_ATTR_CLEAR: int

TEXT_BOX_ATTR_COLLAPSE_BORDERS: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT: int

TEXT_BOX_ATTR_BOX_STYLE_NAME: int

TEXT_BOX_ATTR_WHITESPACE: int

TEXT_BOX_ATTR_CORNER_RADIUS: int

TextBoxAttrClearStyle: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_CLEAR_NONE: int

TEXT_BOX_ATTR_CLEAR_LEFT: int

TEXT_BOX_ATTR_CLEAR_RIGHT: int

TEXT_BOX_ATTR_CLEAR_BOTH: int

TextBoxAttrCollapseMode: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_COLLAPSE_NONE: int

TEXT_BOX_ATTR_COLLAPSE_FULL: int

TextBoxAttrFloatStyle: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_FLOAT_NONE: int

TEXT_BOX_ATTR_FLOAT_LEFT: int

TEXT_BOX_ATTR_FLOAT_RIGHT: int

TextBoxAttrVerticalAlignment: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_NONE: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_TOP: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_CENTRE: int

TEXT_BOX_ATTR_VERTICAL_ALIGNMENT_BOTTOM: int

TextBoxAttrWhitespaceMode: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_WHITESPACE_NONE: int

TEXT_BOX_ATTR_WHITESPACE_NORMAL: int

TEXT_BOX_ATTR_WHITESPACE_NO_WRAP: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_LINE: int

TEXT_BOX_ATTR_WHITESPACE_PREFORMATTED_WRAP: int

TextBoxAttrPosition: TypeAlias = int  # Enumeration

TEXT_BOX_ATTR_POSITION_STATIC: int

TEXT_BOX_ATTR_POSITION_RELATIVE: int

TEXT_BOX_ATTR_POSITION_ABSOLUTE: int

TEXT_BOX_ATTR_POSITION_FIXED: int

TEXT_BOX_ATTR_POSITION_MASK: int

RichTextActionList: TypeAlias = list['RichTextAction']

wxRichTextStyleType: TypeAlias = int

RichTextVariantArray: TypeAlias = list[Any]

RichTextFloatCollector: TypeAlias = Any

RichTextObjectPtrArrayArray: TypeAlias = list[Any]

RichTextObjectPtrArray: TypeAlias = list[Any]

RichTextRangeArray: TypeAlias = list['RichTextRange']

RichTextObjectList: TypeAlias = list['RichTextObject']

TextAttrDimensionFlags: TypeAlias = int

