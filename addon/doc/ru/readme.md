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

Это дополнение основано на SpecificSearch и Bookmark&Search, разработаными
тем же автором. Вы должны удалить их, чтобы использовать placeMarkers, так
как они имеют общие горячие клавиши и возможности.

## Клавиатурные Команды: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Подменю Закладки (NVDA+N) ##


Используя подменю Закладки в меню Параметры, вы можете получить доступ к
следующим элементам:

*	Папка поисковых запросов; открывает папку сохранённых ранее поисковых
  запросов.
*	Папка закладок; открывает папку сохранённых закладок.
*	Копировать папку закладок; вы можете сохранить копию папки закладок.
*	Востановить папку закладок; вы можете востановить ваши закладки из ранее
  сохранённой копии закладок.
*	Файл документации, на выбранном языке, если есть, или английском - по
  умолчанию.

Примечание: Положение закладки основано на количестве символов, и поэтому на
страницах с динамическим содержимым лучше использовать конкретный поиск, а
не закладки которые сохраняют чёткую позицию.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

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
