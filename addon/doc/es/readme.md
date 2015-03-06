# placeMarkers #

* Autores: Noelia, Chris.
* descargar [versión estable][1]
* descarga [versión de desarrollo][2]

Este complemento se utiliza para guardar y buscar cadenas de texto
específicas o marcas, en páginas web o en documentos en el modo navegación
de NVDA.  El plugin guarda las cadenas especificadas y las marcas en
ficheros de texto y pickle. El nombre de estos ficheros se basa en el título
y en la dirección web del documento actual .

Este complemento se basó en SpecificSearch y Bookmark&Search, desarrollados
por el mismo autor. Deberías desinstalarlos para utilizarlo, ya que tienen
las pulsaciones de teclado y las características en común.

## Órdenes de teclado: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

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


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Cambios para  4.0 ##
* Eliminados fragmentos de identificadores de nombres de ficheros de
  marcador,  los cuales pueden evitar problemas en el complemento de Firefox
  ePUBREADER.
* La ayuda del complemento está disponible desde el Administrador de
  Complementos.

## Cambios para 3.1 ##
* Actualización de traducciones y nuevos idiomas.
* Ahora no se anuncia la posición del marcador en la lectura superficial.

## Cambios para 3.0 ##
* Añadido el soporte para lectura superficial.

## Cambios para 2.0 ##
* Añadidas opciones para guardar y eliminar diferentes búsquedas para cada
  archivo.
* Solucionado un problema que rompía cuando las rutas contenían caracteres
  no latinos.
* Los atajos de teclado ahora pueden reasignarse utilizando el diálogo de
  Entrada de gestos de NVDA.


## Cambios para 1.0 ##
* Versión inicial.
* Traducido a: Alemán, Coreano, Eslovaco, Esloveno, Español, Farsi,
  Finlandés, Francés, Gallego, Italiano, Japonés, Nepalí, Portugués,
  Portugués del Brasil, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
