# placeMarkers (Маркери місць) #

* Автори: Noelia, Chris.

This add-on is used for saving and searching specific text strings or
placemarkers. It can be used on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
placemarkers to files whose name is based on the title and URL of the
current document.  This add-on is based on SpecificSearch and
Bookmark&Search, developed by the same author. You should uninstall them to
use this one, since they have common keystrokes and features.

## Комбінації клавіш: ##

*	control+shift+NVDA+f: Відкриває діалог із полем редагування, в якому
  відображається останній збережений пошук; в цьому діалозі ви також можете
  вибрати раніше збережені пошуки з комбінованого списку або видалити
  вибраний рядок з історії за допомогою прапорця. Ви можете вибрати, чи буде
  текст, що міститься у вікні редагування, додано до історії ваших
  збережених текстів. Нарешті, виберіть дію з наступної групи перемикачів
  (між «Шукати далі», «Шукати попереднє» або «Не шукати») і вкажіть, чи буде
  NVDA здійснювати пошук з урахуванням регістру. Коли ви натиснете кнопку
  «Гаразд», NVDA здійснить пошук цього рядка.
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
*	Не призначено: знаходить наступний фрагмент останнього шуканого тексту в
  будь-якому конкретному документі.
*	Не призначено: знаходить попередній фрагмент останнього шуканого тексту в
  будь-якому конкретному документі.


## PlaceMarkers Submenu (NVDA+N) ##

Using the PlaceMarkers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: Opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved placemarkers.
*	Copy placeMarkers folder: You can save a copy of the placeMarkers folder.
*	Restore placeMarkers: You can restore your placeMarkers from a previously
  saved placeMarkers folder.
*	Set default place markers folder: the default folder for place markers can
  be set from this dialog. It will be saved in the normal configuration
  profile.

Note: The placemarker position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
placemarkers.

## Changes for 45.0.0
* Added ability to set the default placeMarkers folder.
* If plugins are reloaded while this add-on is enabled, the last saved
  configuration will be applied.
* Added copy and close buttons to browseable message when showing the
  current file where bookmarks and specific search strings are saved.

## Changes for 35.0
* Removed URL parameters from file names, so that bookmarks are valid for
  specific websites in different sessions.

## Changes for 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Compatible with NVDA 2023.1.

## Зміни у версії 23.0
* Додаток знову працює з Microsoft Word.

## Зміни у версії 22.0
* Завдяки Абделю ми можемо переходити до закладок та видаляти їх з
  увімкненим UIA.

## Зміни у версії 21.0
* Завдяки Абделю можна зберігати закладки з увімкненою функцією UIA у
  браузерах на базі Chromium.

## Зміни у версії 20.0
* Потребує NVDA 2022.1 чи пізнішу.

## Зміни у версії 19.0 ##
* Додаток неможливо запустити на захищених екранах.

## Зміни у версії 18.0 ##
* Команда подивитися шлях для placeMarkers показує, чи є постійні закладки,
  текст для конкретного пошуку або тимчасова закладка для поточного
  документа.

## Зміни у версії 17.0 ##
* Виправлено помилку, яка не дозволяла зберігати маркери місць в деяких
  документах.
* Виправлено перекладені рядки, завдяки чому переклади працюють коректно.

## Зміни у версії 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Підтримується неперервне читання при переході на тимчасові закладки.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Зміни у версії 15.0 ##
* При читанні в режимі «Читати все» в режимі огляду, конкретні команди
  «Знайти далі» та «Знайти попереднє» більше не зупиняють читання, якщо
  увімкнено параметр «Дозволити неперервне читання», відповідно до команд
  «Знайти далі» і «Знайти попереднє» з NVDA 2020.4.
* При відкритті Конкретного пошуку після виконання команди конкретного
  пошуку «Знайти попереднє» буде вибрано параметр «Знайти попереднє».

## Зміни у версії 14.0 ##
*	Команду копіювання імені файлу, в якому будуть збережені дані про маркери
  місць, замінено на команду, яка показує це ім’я файлу в режимі
  огляду. Призначеного жесту немає..
*	Поле «Текст для пошуку» більше не перекриває поле «Збережений
  текст». (Подяка Cyrille Bougot).
*	Вимагає NVDA 2019.3 або новішу.

## Зміни у версії 13.0 ##
*	Додано непризначені жести для знаходження наступного й попереднього
  фрагменту останнього шуканого тексту для будь-якого конкретного документа.
*	Функція конкретного пошуку працює, коли відкрито діалог Про NVDA.
*	У діалозі «Конкретний пошук» буде позначено прапорець «Враховувати
  регістр», якщо ця опція була обрана для останнього пошуку.
*	При оновленні додатка закладки і рядки для конкретного пошуку, збережені в
  попередній версії додатка, буде автоматично скопійовано в нову версію,
  якщо тільки ви не віддасте перевагу імпорту маркерів місць, збережених в
  основній конфігураційній папці NVDA.
*	При використанні діалогу копіювання маркерів місць, якщо обрана папка не
  має імені placeMarkersBackup, буде створено підпапку з цим ім'ям, щоб
  запобігти видаленню каталогів, що містять важливі дані, такі як Документи
  або Завантаження.

## Зміни у версії 12.0 ##
*	Виправлено критичну помилку, яка призводила до аварійного завершення
  роботи NVDA при спробі відкрити діалог приміток, якщо перед збереженням
  закладок було виділено китайські ієрогліфи.

## Зміни у версії 11.0 ##
*	Сумісність з NVDA 2018.3 та новіші (необхідно).

## Зміни у версії 10.0 ##
*	В Edge жести, пов'язані з вибором закладок, такі як NVDA+k, NVDA+shift+k
  або NVDA+alt+k, будуть відправлятися в додаток замість того, щоб
  намагатися перемістити курсор на закладки, щоб уникнути помилок, особливо
  в довгих документах.
*	Тепер конкретний пошук підтримується й у Edge.

## Зміни у версії 9.0
*	При переході на закладку з діалогу примітки переглядовий курсор слідує за
  системним курсором.
*	Команда вибору попередньої закладки знову працює коректно.
*	Закладки можна видалити з діалогу приміток.
*	Тепер для кожного документа можна призначити жести для збереження та
  переміщення до тимчасової закладки.

## Зміни у версії 8.0 ##
*	Видалено ідентифікатори фрагментів з імен файлів закладок, що дозволяє
  уникнути проблем у програмі VitalSource Bookshelf ePUB reader.
*	Додано діалог приміток, щоб поєднати коментарі зі збереженими закладками й
  переходом до виділеної позиції.

## Зміни у версії 7.0 ##
*	Вилучено діалог збереження рядка тексту для конкретного пошуку. Цю функцію
  тепер включена в діалог «Конкретний пошук», який було перероблено таким
  чином, щоб забезпечити різні дії при натисканні кнопки «Гаразд».
*	Візуальне подання діалогів було покращено з дотриманням зовнішнього
  вигляду діалогів, показаних в NVDA.
*	Виконання команди «Знайти далі» або «Знайти попереднє» в режимі огляду
  тепер коректно виконуватиме пошук з урахуванням регістру, якщо початкова
  команда «Знайти» була з урахуванням регістру.
*	Потребує версію NVDA 2016.4 або новішу.
*	Тепер ви можете призначити жести для відкриття діалогів Копіювання й
  Відновлення маркерів місць.
*	NVDA надасть повідомлення, щоб сповістити, коли маркери місць були
  скопійовані або відновлені з відповідними діалогами.

## Зміни у версії 6.0 ##
* Коли функції додатка не використовуються, жести надсилаються до
  відповідного застосунку.

## Зміни у версії 5.0 ##
* Додано пошук, чутливий до регістру літер.
* Вилучено параметр відкриття документації з меню Place markers.
* Інтуїтивно зрозуміліші комбінації клавіш.

## Зміни у версії 4.0 ##
* Видалено ідентифікатори фрагментів з імен файлів закладок, що дозволяє
  уникнути проблем у роботі додатка ePUBREADER у Firefox.
* Довідка додатка доступна з менеджера додатків.

## Зміни у версії 3.1 ##
* Оновлено переклади й додано нові мови.
* Позиція закладки при неперервному читанні не оголошується.

## Зміни у версії 3.0 ##
* Додано підтримку неперервного читання.

## Зміни у версії 2.0 ##
* Додано параметри для збереження й видалення різних варіантів пошуку для
  кожного файлу.
* Виправлено помилку, яка виникала, коли шляхи містили нелатинські символи.
* Тепер комбінації можна перепризначити за допомогою діалогу жестів вводу
  NVDA.

## Зміни у версії 1.0 ##
* Перша версія.
* Перекладено  на: бразильську португальську, фарсі, фінську, французьку,
  галісійську, німецьку, італійську, японську, корейську, непальську,
  португальську, іспанську, словацьку, словенську, тамільську.

[[!tag dev stable]]

