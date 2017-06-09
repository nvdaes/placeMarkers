# placeMarkers #

* Авторы: Noelia, Chris.
* загрузить [стабильную версию][1]
* загрузить [разрабатываемую версию][2]

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
*	control+shift+NVDA+k: Saves the current position as a bookmark.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.


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
