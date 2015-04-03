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

*	control+shift+NVDA+s; Abre un diálogo que  te permite guardar una cadena de texto   que quieras encontrar en el documento actual. De forma predeterminada, se muestra el  texto guardado anteriormente para este fichero. Elimina este texto y pulsa el botón Aceptar si deseas borrar el fichero de texto correspondiente a la búsqueda guardada, o escribe texto nuevo para añadir otra búsqueda.
*	control+shift+NVDA+f; Abre un diálogo con un cuadro de edición que muestra la última búsqeuda guardada; en este diálogo también puedes seleccionar las búsquedas guardadas anteriormente desde un cuadro combinado y elegir una acción desde el siguiente cuadro combinado. Si no hay archivos disponibles para la búsqueda específica en el documento actual, NVDA te advertirá de que no se encuentra ningún archivo para la búsqueda específica.
*	control+shift+NVDA+k; Guarda la posición actual como una marca
*	control+shift+NVDA+suprimir; Elimina la marca correspondiente a esta posición.
*	NVDA+k; Se desplaza a la siguiente marca.
*	shift+NVDA+k; Se desplaza a la marca anterior.
*	control+shift+k; Copia al portapaqpeles el nombre del fichero, sin extensión, donde guardará sus datos el place marker.

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


## Cambios para 5.0 ##
* Añadida búsqueda sensible a las mayúsculas.
* Eliminada la opción para abrir documentación desde el menú Place markers.
* Órdenes de teclado más intuitivas.

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
