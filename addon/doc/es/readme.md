[[!meta title="placeMarkers"]]

* Autores: Noelia, Chris.
* descarga [versión 1.0][1]

Este complemento se utiliza para guardar y buscar cadenas de texto
específicas o marcas, en páginas web o en documentos en el modo navegación
de NVDA.  El plugin guarda las cadenas especificadas y las marcas en
ficheros de texto y pickle. El nombre de estos ficheros se basa en el título
y en la dirección web del documento actual .

Este complemento se basó en SpecificSearch y Bookmark&Search, desarrollados
por el mismo autor. Deberías desinstalarlos para utilizarlo, ya que tienen
las pulsaciones de teclado y las características en común.

## Órdenes de teclado: ##

*	control+shift+NVDA+s; abre un diálogo para guardar una cadena de texto que
  es posible que desees encontrar en el documento actual. Por defecto se
  muestra el texto previamente guardado para este archivo. ;Si se elimina
  este texto, también se eliminará el archivo de texto que contenga la
  cadena correspondiente.
*	control+shift+NVDA+f; Si el documento actual tiene un fichero de texto
  para la búsqueda especificada, abre un diálogo que muestra la cadena de
  texto guardada. Cuando pulses Aceptar, NVDA busca. Si no se ha encontrado
  un fichero de texto para este documento, NVDA lo anuncia sin abrir el
  diálogo Búsqueda Específica.
*	control+shift+NVDA+k; Guarda la posición actual como una marca
*	control+shift+NVDA+Suprimir; Elimina la marca correspondiente a esta
  posición.
*	control+shift+k; Se mueve a la siguiente marca.
*	shift+NVDA+k; Se mueve a la marca anterior.
*	NVDA+k; Copia el nombre del fichero al portapapeles, sin extensión, donde
  se podrían guardar marcas de lugar(posiciones o una cadena para buscar).

## Submmenú Place markers (NVDA+N) ##

Utilizando el submenú Place markers, en el menú Preferencias, puedes acceder
a 

*	Carpeta de búsqueda específica: abre una carpeta de búsquedas específicas
  guardadas previamente.
*	Carpeta de marcas, se abre una carpeta con las marcas guardadas.
*	Copiar carpeta marcas; puedes guardar una copia de la carpeta de marcas.
*	Restaurar marcas; Puedes guardar tus marcas desde una carpeta marcas
  guardada anteriormente.
*	Archivo de documentación, en el idioma seleccionado, si está disponible, o
  en Inglés por defecto.

Nota: La posición de la marca se basa en el número de caracteres; en páginas
con contenido dinámico es mejor usar la búsqueda específica, y no las marcas
para guardar una posición precisa.

## Cambios para 1.0 ##
* Versión inicial.
* Translated into: Brazilian Portuguese, Farsi, Finnish, French, Galician,
  German, Italian, Japanese, Korean, Nepali, Portuguese, Spanish, Slovak,
  Slovenian, Tamil.

[1]: http://addons.nvda-project.org/files/get.php?file=pm
