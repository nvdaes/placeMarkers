# placeMarkers #

* Autores: Noelia, Chris.

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

## Ordes de teclado: ##

*	control+shift+NVDA+f: abre un diálogo cunha caixa de edición que amosa a
  última procura gardada; neste diálogo tamén podes selecionar as procuras
  anteriormente gardadas dende unha Caixa combinada ou borrar a cadea
  selecionada dende o historial utilizando unha caixa de verificación. Podes
  escoller se o texto contido na caixa de edición se engadirá ao histórico
  de textos gardados. Finalmente, escoller unha acción do seguinte grupo de
  botóns de opción (entre procurar seguinte, procurar anterior ou non
  procurar), e especificar se NVDA fará unha procura sensible ás
  maiúsculas. Cando premas Aceptar, NVDA procurará esta cadea.
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
*	Sen asignar: Buscar seguinte ocorrencia do último texto procurado en
  calquera documento específico.
*	Sen asignar: Buscar ocorrencia anterior do último texto procurado en
  calquera documento específico.


## PlaceMarkers Submenu (NVDA+N) ##

Using the PlaceMarkers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: Opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved placemarkers.
*	Copy placeMarkers folder: You can save a copy of the placeMarkers folder.
*	Restore placeMarkers: You can restore your placeMarkers from a previously
  saved placeMarkers folder.

Note: The placemarker position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
placemarkers.

## Changes for 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Compatible with NVDA 2023.1.

## Cambios para 23.0
* O complemento volve a funcionar con Microsoft Word.

## Cambios para 22.0
* Podemos movernos a marcadores e eliminalos con UIA activado, grazas a
  Abdel.

## Cambios para 21.0
* Pódense gardar os marcadores con UIA activado en navegadores baseados en
  Chromium, grazas a Abdel.

## Cambios para 20.0
* Require NVDA 2022.1 ou posterior.

## Cambios para 19.0 ##
* O complemento non se pode executar en pantallas seguras.

## Cambios para 18.0 ##
* O atallo para amosar a ruta de placeMarkers amosa se hai marcas
  permanentes, texto para busca específica ou unha marca temporal para o
  documento actual.

## Cambios para 17.0 ##
* Arranxado un erro que non permitía gardar marcas de posición nalgúns
  documentos.
* Arranxadas as cadeas traducidas facendo funcionar correctamente as
  traducións.

## Cambios para 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Sopórtase a lectura superficial ao moverse a unha marca temporal.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Cambios para 15.0 ##
* Ó ler con ler todo en modo exploración, os atallos específico buscar
  anterior e específico buscar seguinte xa non deteñen a lectura se a opción
  Permitir lectura superficial está habilitada, en consoancia cos atallos
  buscar seguinte e buscar anterior de NVDA 2020.4.
* Cando o diálogo de busca específico se abre despois de executar o atallo
  específico buscar anterior, seleccionarase a opción buscar anterior.

## Cambios para 14.0 ##
*	O atallo para copiar o nome do arquivo onde se gardarán os datos dos
  marcadores de ubicación reemprazouse por un atallo que amosa este nome de
  arquivo en modo exploración. Está sen asignar a ningún xesto.
*	O campo "Texto a buscar" xa non solapa ao campo "Texto gardado". (Grazas a
  Cyrille Bougot).
*	Require NVDA 2019.3 ou posterior.

## Cambios para 13.0 ##
*	Engadidas ordes sen asignar para buscar a próxima e anterior ocorrencia do
  último texto procurado en calquera documento específico.
*	A característica de busca específica funciona cando o diálogo Acerca de
  NVDA está aberto.
*	No diálogo Busca específica, a caixa de verificación sensible ás
  maiúsculas estará verificada se esta opción se seleccionou na busca
  anterior.
*	Cando o complemento se actualice, os marcadores e as cadeas da busca
  específica gardadas na versión anterior do complemento copiaranse
  automaticamente á nova versión, a menos que prefiras importar os
  marcadores de lugar gardados no cartafol principal de configuración de
  NVDA.
*	Ao utilizar o diálogo para copiar marcadores de lugar, se o cartafol
  escollido non se chama placeMarkersBackup, crearase un subcartafol co
  mesmo nome para previr a eliminación de directorios que conteñan datos
  importantes, como Documentos ou Descargas.

## Cambios para 12.0 ##
*	Solucionado un erro crítico que causaba o peche de NVDA ao tratar de abrir
  o diálogo de notas cando estaban seleccionados caracteres chinos antes de
  gardar marcadores.

## Cambios para 11.0 ##
*	Compatible co NVDA 2018.3 ou posterior (requerido).
*	Se fora necesario, podes descargar a [última versión compatible co NVDA
  2017.3][3].

## Cambios para 10.0 ##
*	En Edge, os xestos asociados coa seleción de marcas, como NVDA+k,
  NVDA+shift+k ou NVDA+alt+k, enviaranse á aplicación en lugar de tentar
  mover o cursor ás marcas, para evitar erros, especialmente en documentos
  longos.
*	Agora admítese a procura específica en Edge.

## Cambios para 9.0
*	Ao se mover a unha marca dende a Caixa de diálogo Notas, o cursor de
  revisión segue ao cursor do sistema.
*	A orde para selecionar a marca anterior funciona de novo adecuadamente.
*	As marcas poden borrarse dende a Caixa de diálogo Notas.
*	Agora podes asignar xestos para gardar e moverte a unha marca temporal
  para cada documento.

## Cambios para 8.0 ##
*	Elimináronse os identificadores de fragmentos dos nomes de ficheiro de
  marcadores , que poden evitar problemas no VitalSource Bookshelf
  EPUBReader.
*	Engadiuse un diálogo Notas, para asociar comentarios para marcas gardadas
  e para moverte cara a posición selecionada.

## Cambios para 7.0 ##
*	O diálogo para gardar unha cadea de texto para unha procura específica
  eliminouse. Esta funcionalidade agora inclúese no diálogo Procura
  Específica, o que se rediseñou para permitir accións diferentes ao se
  premer o botón Aceptar.
*	Mellorouse a presentación visual do diálogo, adheríndose á apariencia dos
  diálogos amosados no NVDA.
*	Ao se realizar unha orde procurar seguinte ou procurar anterior en Modo
  exploración agora farase correctamente unha procura sensible ás maiúsculas
  se a procura orixinal era sensible ás maiúsculas.
*	Requírese do NVDA 2016.4 ou posterior.
*	Agora podes asignar xestos para abrir os diálogos Copiar e Restaurar
  marcadores.
*	NVDA presentará unha mensaxe para notificar cando se copiaran ou
  restauraran os marcadores cos diálogos correspondentes.

## Cambios para 6.0 ##
* Cando as características do complemento non son usables, os xestos
  envíanse á aplicación correspondente.

## Cambios para 5.0 ##
* Engadida busca sensible ás maiúsculas.
* Eliminada a opción para abrir documentación dende o menú Place markers.
* Ordes de teclado máis intuitivas.

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
