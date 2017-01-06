# placeMarkers #

* Авторы: Noelia, Chris.
* загрузить [стабильную версию][1]
* загрузить [разрабатываемую версию][2]

This addon is used for saving and searching specific text strings or
bookmarks. It can be used  on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
bookmarks to files whose name is based on the title and URL of the current
document.  This addon is based on SpecificSearch and Bookmark&Search,
developed by the same author. You should uninstall them to use this one,
since they have common keystrokes and features.

## Клавиатурные Команды: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.


## Подменю Закладки (NVDA+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Папка поисковых запросов; открывает папку сохранённых ранее поисковых
  запросов.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.

## Changes for 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Requires NVDA 2016.4 or later.
*	Now you can assign gestures to open the Copy and Restore place markers
  dialogs.
*	NVDA will present a message to notify when place markers have been copied
  or restored with the corresponding dialogs.

## Изменения для 6.0 ##
* Когда дополнительные функции не могут использоваться, жесты посылаются в
  соответствующее приложение.

## Изменения для 5.0 ##
* Добавлен поиск с учётом регистра.
* Удалена возможность открыть документацию из меню Закладки.
* Более интуитивные комбинации клавиш.

## Изменения для 4.0 ##
* Удалены идентификаторы фрагментов из имён файлов закладок, что позволяет
  избежать проблем в EPUBReader - дополнении для FireFox.
* Справка по дополнению теперь доступна из менеджера дополнений.

## Изменения для 3.1 ##
* Обновлены переводы и новые языки.
* Позиция закладки теперь не сообщается при беглом чтении.

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
* Первый публичный релиз.
* Переведено на: бразильский португальский, фарси, финский, французский,
  галисийский, немецкий, итальянский, японский, корейский, непальский,
  португальский, испанский, словацкий, словенский, тамильский.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
