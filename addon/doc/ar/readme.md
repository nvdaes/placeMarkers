# placeMarkers #

* مطورو الإضافة: Noelia, Chris.
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

تستخدم هذه الإضافة في حفظ أو البحث عن الكلمات أو العلامات المرجعية, على
صفحات الإنترنت أو مستندات نمط التصفح ب NVDA. وتقوم الإضافة بحفظ الكلمات
والعلامات المرجعية التي يتم البحث عنها في كائنات متعددة الأسطر، وفي هذه
الحالة إذا تعذر عليك تحديث موضع مؤشر التحرير, فسيتم نسخ النص المتطابق إلى
الحافظة, حتى يمكن البحث عنها باستخدام أدوات أخرى. تقوم الإضافة بحفظ كلمات
البحث والعلامات المرجعية في ملفات نصية أو ملفات pickles.  وتتطابق أسماء
الملفات المحفوظة بهذه الكلمات والعلامات مع عناوين وروابط الصفحة أو المستند
الذي يتم البحث بداخله.

يجب على من يستخدم هذه الإضافة أن يقوم بإزالة الإضافتين SpecificSearch و
Bookmark إذا كان قد تم تنصيبهما, واللتان تم تطويرهما من قبل نفس مطور هذه
الإضافة, نظرا لاحتوائهما على خصائص ومفاتيح اختصار مشتركة.

## مفاتيح الاختصار: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## العلامات المرجعية قائمة فرعية (NVDA+N) ##


استخدام القائمة الفرعية علامات مرجعية, الموجودة بداخل قائمة التفضيلات والتي
تمكنك من الوصول إلى:

*	مجلد كلمات البحث: يقوم بفتح المجلد الخاص بكلمات البحث التي قمت بحفظها من
  قبل.
*	مجلد العلامات المرجعية, يقوم هذا الأمر بفتح المجلد الذي يحتوي على العلامات
  المرجعية التي قمت بحفظها.
*	نسخ مجلد العلامات المرجعية, يمكنك أخذ نسخة من المجلد الذي يحتوي على
  العلامات المرجعية التي قمت بحفظها.
*	استرجاع العلامات المرجعية, يمكنك استرجاع العلامات المرجعية التي قمت بحفظها
  من خلال مجلد قمت بحفظ العلامات المرجعية به مسبقا.
*	ملف اقرأني, باللغة التي تحددها إذا كان الملف مترجم إليها, أو قراءة الملف
  باللغة الإنجليزية.

ملحوظة: يعتمد مكان العلامة المرجعية على عدد الأحرف; لذا فإن الصفحات ذات
المحتوى المتغير يستحسن استخدام البحث, وليست العلامات المرجعية لحفظ مكان
دقيق.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## مستجدات الإصدار 4.0 ##
* إزالة معرف الجزيآت باسم ملف العلامة المرجعية, والتي كانت تتسبب في حدوث بعض
  المشكلات مع إضافة فيرفوكس ePUBREADER 
* إمكانية الوصول لملف المساعدة الخاص بالإضافة من مدير الإضافات البرمجية

## مستجدات الإصدار 3.1 ##
* تحديث ترجمة الإضافة وترجمتها لمزيد من اللغات
* لم يتم الإعلان عن موقع العلامة المرجعية أثناء القراءة المتصلة.

## مستجدات الإصدار 3.0 ##
* إضافة دعم للقراءة التصفحية السريعة

## مستجدات الإصدار 2.0 ##
* تم إضافات خيارات تسمح بحذف وحفظ كلمات بحث مختلفة لكل ملف على حدة.
* معالجة خطأ برمجي كان يتسبب في كسر المسارات التي تحتوي على أحرف غير لاتينية
* يمكن تخصيص اختصارات الإضافة باستخدام محاورة تخصيص اختصارات NVDA.


## مستجدات الإصدار 1.0 ##
* إصدار أولي
* هذه الإضافة مترجمة إلى: البرازيلية البرتغالية, والفنلندية, والفرنسية,
  والغالية, والألمانية, والإيطالية, واليابانية, والكورية, والبرتغالية,
  والإسبانية, والسلوفاكية, والسلوفينية, وتاميل.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm[1]:
http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
