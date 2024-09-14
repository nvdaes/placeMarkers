# placeMarkers #

* Авторы: Noelia, Chris.

Это дополнение используется для сохранения и поиска определённых текстовых
строк или меток размещения. Его можно использовать на веб-страницах или в
документах в режиме обзора NVDA. Его также можно использовать для сохранения
или поиска строк текста в многострочных элементах управления; в этом случае,
если невозможно обновить курсор, соответствующая строка будет скопирована в
буфер обмена, чтобы её можно было искать с помощью других инструментов.
Дополнение сохраняет указанные строки и метки размещения в файлах, название
которых основано на заголовке и URL-адресе текущего документа.  В основе
дополнения лежат такие плагины для NVDA, как SpecificSearch и
Bookmark&Search, разработанных тем же автором. Чтобы использовать это
дополнение, вам следует удалить их, поскольку они имеют общие сочитания
клавиш и функции.

## Клавиатурные Команды: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+y: Saves the current position as a placemarker. If you
  want to provide a name for this placemarker, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the placemarker corresponding to this
  position.
*	NVDA+y: Moves to the next placemarker.
*	shift+NVDA+y: Moves to the previous placemarker.
*	Not assigned: Shows the file name where the placemarkers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+y: Opens a dialog with the placemarkers saved for this
  document. You can write a note for each placemarker; press Save note to
  save changes. Pressing Delete you can remove the selected
  placemarker. Pressing OK you can move to the selected position.
*	Not assigned: Saves a position as a temporary placemarker.
*	Not assigned: Moves to the temporary placemarker for the current document.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


## PlaceMarkers Submenu (NVDA+N) ##

Using the PlaceMarkers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: Opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved placemarkers.
*	Copy placeMarkers folder: You can save a copy of the placeMarkers folder.
*	Restore placeMarkers: You can restore your placeMarkers from a previously
  saved placeMarkers folder.

Примечание: Позиция placemarker зависит от количества символов, и поэтому на
динамических страницах лучше использовать конкретный поиск, а не
placemarkers.

## Изменения для 35.0
* Removed URL parameters from file names, so that bookmarks are valid for
  specific websites in different sessions.

## Изменения для 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Совместимо с NVDA 2023.1.

## Изменения для 23.0
* The add-on works again with Microsoft Word.

## Изменения для 22.0
* We can move to bookmarks and delete them with UIA enabled, thanks to
  Abdel.

## Изменения для 21.0
* Bookmarks can be saved with UIA enabled in browsers based on Chromium,
  thanks to Abdel.

## Изменения для 20.0
* Требуется NVDA 2022.1 или позднее.

## Изменения для 19.0 ##
* The add-on cannot be run on secure screens.

## Изменения для 18.0 ##
* The command to see the path for placeMarkers shows if there are permanent
  bookmarks, text for specific search or a temporary bookmark for the
  current document.

## Изменения для 17.0 ##
* Fixed a bug which didn't allow to save place markers in some documents.
* Исправлены переведённые строки, чтобы правильно работали переводы.

## Изменения для 16.0 ##
* Совместимо с NVDA 2021.1 или выше (требуется).
* Skim reading is supported when moving to temporary bookmarks.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Изменения для 15.0 ##
* When reading with say all in browse mode, the specific find next and
  specific find previous commands do not stop reading anymore if Allow skim
  reading option is enabled, according to find next and find previous
  commands from NVDA 2020.4.
* When the Specific search dialog is opened after running the Specific find
  previous command, the Search previous option will be selected.

## Изменения для 14.0 ##
*	The command to copy the name of the file where place markers data will be
  saved has been replaced by a command which shows this file name in browse
  mode. This is not assigned to a gesture.
*	The "Text to search" field does not overlap the "Saved text" field
  anymore. (Thanks to Cyrille Bougot).
*	Требуется NVDA 2019.3 или позднее.

## Изменения для 13.0 ##
*	Добавлены не назначенные команды для поиска следующего и предыдущего
  вхождений последнего искомого текста для любого конкретного документа.
*	Конкретная функция поиска работает, когда открыто диалоговое окно NVDA "О
  программе".
*	В диалоге "Конкретный поиск" будет установлен флажок "Учитывать регистр",
  если этот параметр был выбран для последнего поиска.
*	When the add-on is updated, bookmarks and strings for specific search
  saved in the previous version of the add-on will be automatically copied
  to the new version, unless you prefer to import place markers saved in the
  main configuration folder of NVDA.
*	When using the dialog to copy place markers, if the chosen folder is not
  named placeMarkersBackup, a subfolder with this name will be created to
  prevent the deletion of directories containing important data, such as
  Documents or Downloads.

## Изменения для 12.0 ##
*	Исправлена критическая ошибка, приводившая к сбою NVDA при попытке открыть
  диалог заметок, если перед сохранением закладок были выбраны китайские
  иероглифы.

## Изменения для 11.0 ##
*	Совместимо с NVDA 2018.3 или позднее (обязательно).
*	При необходимости вы можете загрузить [последнюю версию, совместимую с
  NVDA 2017.3][3].

## Изменения для 10.0 ##
*	В Edge жесты, связанные с выбором закладок, такие как NVDA+k, NVDA+shift+k
  или NVDA+alt+k, будут отправляться в приложение вместо попыток навести
  курсор на закладки, чтобы избежать ошибок, особенно в длинных документах.
*	Теперь в Edge поддерживается специальный поиск.

## Изменения для 9.0
*	При переходе к закладке в диалоге "Заметки" просмотровый курсор следует за
  системным курсором.
*	Команда для выбора предыдущей закладки снова работает корректно.
*	Закладки можно удалить из диалога Заметок.
*	Теперь вы можете назначать жесты для сохранения и перемещения во временную
  закладку для каждого документа.

## Изменения для 8.0 ##
*	Удалены идентификаторы фрагментов из имен файлов закладок, что позволяет
  избежать проблем в программе чтения ePUB VitalSource Bookshelf.
*	Добавлен диалог заметок, позволяющий привязывать комментарии к сохранённым
  закладкам и перемещаться в выбранную позицию.

## Изменения для 7.0 ##
*	Диалог для сохранения текстовой строки для конкретного поиска был
  удалён. Эта функция теперь включена в диалог конкретного поиска, дизайн
  которого был изменён таким образом, чтобы при нажатии кнопки OK можно было
  выполнять другие действия.
*	Визуальное представление диалогов было модифицировано, придерживаясь
  внешнего вида диалогов, отображаемых в NVDA.
*	Выполнение команды "Найти следующее" или "Найти предыдущее" в режиме
  обзора теперь будет корректно выполнять поиск с учётом регистра, если
  исходный поиск был выполнен с учётом регистра.
*	Требуется NVDA 2016.4 или позднее.
*	Теперь вы можете назначать жесты для открытия диалогов Копирования и
  восстановления маркеров.
*	NVDA выдаст сообщение с уведомлением о копировании или восстановлении
  маркеров местоположения с помощью соответствующих диалогов.

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
