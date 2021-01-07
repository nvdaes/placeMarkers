# eMule #

*	مطورو الإضافة: Noelia, Chris, Alberto
*	NVDA compatibility: 2019.3 or later.
*	تحميل [الإصدار النهائي][1]
*	تحميل [الإصدار التجريبي][3]
*	download [version compatible with NVDA 2017.3][4]

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

وقد تم تجربة الإضافة مع الإصدار  [eMule][2] 0.50a.

## الأوامر والمفاتيح المختصرة ##

*	control+shift+h: تحريك مؤشر الفأرة ومؤشر النظام تجاه شريط الأدوات
  الرئيسي. 
*	control+shift+t: لقراءة النافذة الحالية
*	control+shift+n: لتحريك مؤشر النظام إلى حقل الاسم في نافذة البحث.
*	control+shift+p: في نافذة البحث يحرك مؤشر الفأرة ومؤشر النظام تجاه قائمة
  معطيات البحث أو خيارات حقول التحرير. 
*	control+shift+b: لتحريك مؤشر النظام تجاه القائمة الموجودة بالنافذة
  الحالية. كالانتقال إلى قوائم نتائج البحث, أو التحميلات بنافذة نقل الملفات,
  وهكذا.
*	control+shift+o: لتحريك مؤشر النظام تجاه مربعات التحرير المخصصة للقراءة
  فقط في النافذة الحالية.  كمربعات تحرير استلام رسائل بروتوكول IRC, أو
  الخوادم المتاحة, وهكذا.
*	control+NVDA+f: If the caret is located in a read only edit box, opens a
  find dialog to use the commands for searching text available in NVDA.
*	control+shift+l: لتحريك مؤشر NVDA ومؤشر الفأرة تجاه رأس القائمة الحالية. 
*	control+shift+q: لقراءة أول كائن في شريط الحالة. يعطي معلومات عن أحدث أمر
  تم تنفيذه. 
*	control+shift+w: لقراءة الكائن الثاني في شريط الحالة. ويحتوي على معلومات
  عن الملفات والمستخدمين الحاليين على الخادم الحالي. 
*	control+shift+e: لقراءة الكائن الثالث في شريط الحالة. مفيد في معرفة سرعة
  الرفع والتنزيل. 
*	control+shift+r: لقراءة الكائن الرابع في شريط الحالة. يستخدم للإعلام عن
  الاتصال بشبكة eD2K و CAD

## إدارة العماويد ##

إذا كنت داخل القائمة يمكنك التنقل بين الصفوف والأعمدة باستخدام alt+control
مع الأسهم.  وفي هذه الإضافة تتوفر أيضا مفاتيح الاختصار التالية:

*	nvda+control+1-0: لقراءة الأعمدة العشر الأولى. 
*	nvda+shift+1-0: لقراءة الأعمدة من 11-20.
*	nvda+shift+C: لنسخ محتوى آخر عمود تمت قراءته إلى الحافظة.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Changes for 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## مستجدات الإصدار  1.0 ##
*	 إتاحة ملف المساعدة بمدير الإضافات البرمجية.

## مستجدات الإصدار 1.2 ##
*	 عند التحرك على رسائل ال IRC, فإنه سيتم الإعلان عنها بشكل صحيح
*	 لقد تم تعميم الاختصار الذي كان منوط بالانتقال إلى نتائج البحث حيث أصبح
   ينتقل لأي قائمة موجودة بالنافذة الحالية.
*	 لقد تم تعميم الأمر المخصص للانتقال للرسائل المستلمة ببروتوكول IRC حيث
   أصبح ينتقل إلى أي مربع تحرير للقراءة فقط, وذلك أدى إلى إمكانية مراجعة
   معلومات الاتصال بنافذة الخوادم.
*	 معالجة نطق شريط الأدوات مرتين في بعض الأحوال عند تحريك الفأرة أو مؤشر
   النظام إليه.

## تعديلات الإصدار  1.1 ##
*	 إصلاح خطأ برمجي بعنصر eMule بقائمة المساعدة ب NVDA, عندما يحتوي اسم ملف
   إعدادات المستخدم على أحرف غير لاتينية.
*	 يمكن إعادة تخصيص اختصارات الإضافة من خلال محاورة تخصيص اختصارات NVDA.

## تعديلات الإصدار  1.0 ##
*	 نسخة أولية


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
