# placeMarkers (Позиционни маркери) #

* Автори: Noelia, Chris.
* Изтегляне [стабилна версия][1]
* Изтегляне [работна версия][2]

Тази добавка се използва за запазване и търсене на определен текст или
отметка в уеб страници или други документи в режим на разглеждане с
NVDA. Може също да бъде използвана за запазване или търсене на текстове в
многоредови контроли; в този случай опресняването на каретката не е
възможно, затова отговарящият низ ще бъде копиран в клипборда, така че да
може да бъде намерен с други инструменти.  Добавката записва низовете и
отметките в текстови и pickle файлове. Имената на тези файлове са базирани
на името и URL адреса на текущия документ.

Тази добавка е базирана на SpecificSearch и Bookmark&Search, разработени от
същия автор. Ако смятате да използвате тази добавка, трябва първо да
премахнете горните две, тъй като те имат сходни клавишни команди и
възможности.

## Клавишни команди: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Подменю Позиционни маркери (NVDA+N) ##


Използвайки подменю Позиционни маркери, намиращо се в подменю Настройки от
главното меню на NVDA, имате достъп до:

*	Папка за конкретно търсене: отваря папката, където са записани предишните
  конкретни търсения.
*	Папка с отметки; отваря папката със запазените отметки.
*	Копиране на папката с позиционни маркери; можете да копирате папката с
  позиционни маркери на друго място на твърдия диск.
*	Възстановяване на позиционните маркери; може да възстановите вашите
  позиционни маркери от предишно съхранено копие на папката с вашите
  позиционни маркери.
*	Файл с документация, на вашия майчин език (ако е наличен), или на
  английски (по подразбиране).

Забележка: позицията на отметките се базира на броя на знаците; поради това
в страници с динамично съдържание е по-добре да използвате конкретното
търсене вместо отметките, които запазват точно определена позиция.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Промени във версия 4.0 ##
* Премахнати са идентификатори на фрагменти от имената на отметките, с което
  може да се избегнат проблеми в добавката ePUBREADER за Firefox.
* Помощта за добавката е достъпна от мениджъра на добавките.

## Промени във версия 3.1 ##
* Обновени преводи и нов език.
* Позицията на маркерите не бива съобщавана при бегло четене.

## Промени във версия 3.0 ##
* Добавена е поддръжка за бегло четене.

## Промени във версия 2.0 ##
* Добавени са опции за запазване и изтриване на различните търсения за всеки
  файл.
* Отстранен е проблем с пътищата на файловата система, които съдържат
  символи, различни от латиница.
* Бързите клавиши вече могат да бъдат преназначавани с използване на диалога
  Жестове на въвеждане на NVDA.


## Промени във версия 1.0 ##
* Първоначално издание.
* Добавката е преведена на: бразилски португалски, фарси, фински, френски,
  галицийски, немски, италиански, японски, корейски, непалски, португалски,
  испански, словашки, словенски, Тамил.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
