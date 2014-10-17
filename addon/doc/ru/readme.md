# placeMarkers #

* Авторы: Noelia, Chris.
* загрузить [стабильную версию][1]
* загрузить [разрабатываемую версию][2]

This addon is used for saving and searching specific text strings or
bookmarks, on web pages or documents in NVDA's browse mode. It can also be
used for saving or searching strings of text in multi-line controls; in this
case, if it's not possible to update the caret, the corresponding string
will be copied to the clipboard, so that it can be searched using other
tools.  The plugin saves the specified strings and bookmarks to text and
pickle files. The name of these files is based on the title and URL of the
current document.

This addon is based on SpecificSearch and Bookmark&Search, developed by the
same author. You should uninstall them to use this one, since they have
common keystrokes and features.

## Клавиатурные Команды: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	control+shift+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	NVDA+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Place markers Submenu (NVDA+N) ##


Using Place markers submenu, under Preferences menu, you can access:

*	Specific search folder: opens a folder of specific searches previously
  saved.
*	Bookmarks folder; opens a folder of the saved bookmarks.
*	Copy placeMarkers folder; you can save a copy of the bookmarks folder.
*	Restore placeMarkers; you can restore your bookmarks from a previously
  saved placeMarkers folder .
*	Файл документации, на выбранном языке, если есть, или английском - по
  умолчанию.

Примечание: Положение закладки основано на количестве символов, и поэтому на
страницах с динамическим содержимым лучше использовать конкретный поиск, а
не закладки которые сохраняют чёткую позицию.

## Changes for 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Add-on help is available from the Add-ons Manager.

## Изменения для 3.1 ##
* Обновлены переводы и новые языки.
* Bookmark position is not announced in skim reading.

## Изменения для 3.0 ##
* Добавлена поддержка беглого чтения.

## Изменения для 2.0 ##
* Добавлены опции для сохранения и удаления различных поисков для каждого
  файла.
* Исправлена ошибка, вызывающая крах, когда пути содержат не латинские
  буквы.
* Горячие клавиши теперь могут быть переназначены в диалоге жестов ввода
  NVDA.


## Изменения для 1.0 ##
* Первый Публичный Релиз
* Переведено на: бразильский португальский, фарси, финский, французский,
  галисийский, немецкий, итальянский, японский, корейский, непальский,
  португальский, испанский, словацкий, словенский, тамильский.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
