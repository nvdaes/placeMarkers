# placeMarkers #

* Autores: Noelia, Chris.
* descarga [versión estable][1]
* descarga [versión de desenvolvemento][2]

Este complemento úsase para gardar e restaurar cadeas de texto específicas
ou marcas. Pode usarse en páxinas web ou en documentos no modo exploración
do NVDA. Tamén pode usarse para gardar ou procurar cadeas de texto en
controis multiliña; neste caso, se non é posible actualizar o cursor, a
cadea correspondente copiarase ao portapapeis, tal que se poda procurar
usando outras ferramentas.  O plugin garda as cadeas especificadas e marcas
en ficheiros con nombres baseados no título e URL do documento actual.  Este
complemento baséase en SpecificSearch y Bookmark&Search, desenvolvidos polo
mesmo autor. Deberías desinstalalos para usar este, xa que teñen as mesmas
combinacións de teclas e características.

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
*	control+shift+NVDA+k: garda a posición actual coma unha marca. Se queres
  proporcionar un nome para esta marca, seleciona algún texto desta posición
  antes de gardala.
*	control+shift+NVDA+suprimir: borra a marca correspondente a esta posición.
*	NVDA+k: Move á marca seguinte.
*	shift+NVDA+k: move á marca anterior.
*	control+shift+k: copia o nome do ficheiro onde se gardarán os datos dos
  marcadores ao portapapeis, sen unha extensión.
*	alt+NVDA+k: abre un diálogo coas marcas gardadas para este
  documento. Podes escreber unha nota para cada marca; preme Gardar Nota
  para guardar cambios. Pulsando Aceptar puedes moverte al a la posición
  seleccionada.
*	Sen asignar: garda a posición actual coma unha marca temporal.
*	Sen asignar: Móvese á marca temporal para o documento actual.


## Submenú Place markers (NVDA+N) ##

Usando o submenú Place markers no Menú Preferencias, podes acceder a

*	Cartafol de busca específica:abre un cartafol de buscas específicas
  gardadas anteriormente.
*	Cartafol de marcas: abre un cartafol de marcas gardadas.
*	Copiar cartafol de marcadores: podes gardar unha copia do cartafol de
  marcas.
*	Restaurar marcadores: Podes restaurar as túas marcas dende un cartafol de
  marcadores gardado anteriormente.

Nota: A posición da marca baséase no número de caracteres, polo tanto en
páxinas con contido dinámico é mellor usar a busca específica,e non as
marcas.


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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
