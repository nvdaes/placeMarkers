# placeMarkers #

* Авторы: Noelia, Chris.
* download [stable version][1] (compatible with NVDA 2022.1 and beyond)
* download [development version][2] (compatible with NVDA 2022.1 and beyond)

Это дополнение используется для сохранения и поиска определенных строк
текста или закладок. Оно может быть использовано на веб-страницах или
документах в режиме обзора NVDA. также оно может быть использовано для
сохранения или поиска строк текста в многострочных элементах управления, в
случае невозможности обновить курсор, соответствующая строка будет
скопирована в буфер обмена, так что она может быть найдена с помощью других
инструментов. Дополнение сохраняет указанные строки и закладки в файлах, чье
имя основано на названии и URL-адресе текущего документа. Это дополнение
основано на SpecificSearch и Bookmark&Search, разработанных тем же
автором. Вы должны удалить их, чтобы использовать его, поскольку они имеют
общие функции и комбинации клавиш.

## Клавиатурные Команды: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	Not assigned: Shows the file name where the place markers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


## Подменю Закладки (NVDA+N) ##

Используя подменю Закладки в меню Параметры NVDA, вы можете получить доступ
к следующим элементам:

*	Папка поисковых запросов; открывает папку сохранённых ранее поисковых
  запросов.
*	Папка закладок: открывает папку сохранённых закладок.
*	Копировать папку закладок: вы можете сохранить копию папки закладок.
*	Восстановить папку закладок: вы можете востановить ваши закладки из ранее
  сохранённой копии закладок.

Примечание: Положение закладки основано на количестве символов; и поэтому на
страницах с динамическим содержимым лучше использовать конкретный поиск, а
не закладки которые сохраняют чёткую позицию.

## Changes for 20.0
* Requires NVDA 2022.1 or later.

## Changes for 19.0 ##
* The add-on cannot be run on secure screens.

## Changes for 18.0 ##
* The command to see the path for placeMarkers shows if there are permanent
  bookmarks, text for specific search or a temporary bookmark for the
  current document.

## Changes for 17.0 ##
* Fixed a bug which didn't allow to save place markers in some documents.
* Fixed translated strings making translations to work properly.

## Changes for 16.0 ##
*	Compatible with NVDA 2021.1 or later (required).
* Skim reading is supported when moving to temporary bookmarks.
*	If needed, you can download [other versions](https://github.com/nvdaes/placeMarkers/releases).

## Changes for 15.0 ##
* When reading with say all in browse mode, the specific find next and
  specific find previous commands do not stop reading anymore if Allow skim
  reading option is enabled, according to find next and find previous
  commands from NVDA 2020.4.
* When the Specific search dialog is opened after running the Specific find
  previous command, the Search previous option will be selected.

## Changes for 14.0 ##
*	The command to copy the name of the file where place markers data will be
  saved has been replaced by a command which shows this file name in browse
  mode. This is not assigned to a gesture.
*	The "Text to search" field does not overlap the "Saved text" field
  anymore. (Thanks to Cyrille Bougot).
*	Requires NVDA 2019.3 or later.

## Changes for 13.0 ##
*	Added not assigned commands to find the next and previous occurrences of
  the last text searched for any specific document.
*	The specific search feature works when the NVDA's About dialog is open.
*	In the Specific search dialog, the case sensitive checkbox will be checked
  if this option was selected for the last search.
*	When the add-on is updated, bookmarks and strings for specific search
  saved in the previous version of the add-on will be automatically copied
  to the new version, unless you prefer to import place markers saved in the
  main configuration folder of NVDA.
*	When using the dialog to copy place markers, if the chosen folder is not
  named placeMarkersBackup, a subfolder with this name will be created to
  prevent the deletion of directories containing important data, such as
  Documents or Downloads.

## Changes for 12.0 ##
*	Fixed a critical bug which caused NVDA to crash when trying to open the
  Notes dialog, if chinese characters were selected before saving bookmarks.

## Changes for 11.0 ##
*	Compatible with NVDA 2018.3 or later (required).
*	If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 10.0 ##
*	In Edge, gestures associated with bookmarks selection, such as NVDA+k,
  NVDA+shift+k or NVDA+alt+k, will be sent to the application instead of
  trying to move the cursor to bookmarks, to avoid errors, especially in
  long documents.
*	Now specific search is supported in Edge.

## Changes for 9.0
*	When moving to a bookmark from the Notes dialog, the review cursor follows
  the system cursor.
*	The command to select the previous bookmark works properly again.
*	Bookmarks can be deleted from the Notes dialog.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

## Изменения для 8.0 ##
*	Removed fragment identifiers from bookmark filenames, which can avoid
  issues in the VitalSource Bookshelf ePUB reader.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

## Изменения для 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	Визуальное представление диалогов было модифицировано, придерживаясь
  внешнего вида диалогов, отображаемых в NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Требуется NVDA 2016.4 или позднее.
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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
