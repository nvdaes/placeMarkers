# placeMarkers #

* Autores: Noelia, Chris.
* descarga [versión estable][1]
* descarga [versión de desenvolvemento][2]

Este complemento úsase para gardar e buscar cadeas de texto específicas ou
marcas, en páxinas web ou en documentos no modo navegación do NVDA.  O
plugin garda as cadeas especificadas e marcas en ficheiros de texto ou
pickle. O nome destes ficheiros baséase no título e no enderezo web do
documento actual.

Este complemento está baseado en SpecificSearch e Bookmark&Search,
desenvolvido polo mesmo autor. Debes desinstalalos para usar este, xa que
teñen os atallos de teclado e as características comúns.

## Ordes de teclado: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Submenú Place markers (NVDA+N) ##


Usando o submenú Place markers, no Menú Preferencias, podes acceder a

*	Cartafol de busca específica:abre un cartafol de buscas específicas
  gardadas anteriormente.
*	Cartafol de marcas, abre un cartafol de marcas gardadas.
*	Copiar cartafol marcas; podes gardar unha copia do cartafol de marcas.
*	Restaurar marcas; Podes restaurar as túas marcas dende un cartafol marcas
  gardado anteriormente.
*	Arquivo de documentación, no teu idioma escollido, se tes un, ou en inglés
  por defecto.

Nota: A posición da marca baséase no número de caracteres; en páxinas con
contido dinámico é mellor usar a busca específica,e non as marcas para
gardar unha posición precisa.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Cambios para 4.0 ##
* Elimináronse os identificadores de fragmentos dos nomes de ficheiro de
  marcadores , que poden evitar problemas no complemento de Firefox
  EPUBReader.
* A axuda do complemento está dispoñible no Administrador de Complementos.

## Cambios para 3.1 ##
* Actualizacións das traduccións e novas linguas.
* A posición do marcador non se anuncia na lectura superficial.

## Cambios para 3.0 ##
* Engadido o soporte para lectura superficial.

## Cambios para 2.0 ##
* Engadidas opcións para gardar e borrar diferentes buscas para cada
  ficheiro.
* Solucionado un problema que rompía cando as rutas contiñan caracteres non
  latinos.
* Os atallos de teclado agora pódense reasignar utilizando o diálogo xestos
  de entrada do NVDA.


## Cambios para 1.0 ##
* Versión inicial.
* Traducido ó: Alemán, Español, Eslovaco, Esloveno, Farsi, Finés, Francés,
  Galego, Italiano, Coreán, Nepalí, Portugués, Portugués do Brasil, Tamil,
  Xaponés.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
