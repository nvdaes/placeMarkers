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

*	control+shift+NVDA+s; Abre un diálogo que che permite gardar unha cadea de texto   que queres atopar no documento actual. De maneira predeterminada, amósase o texto gardado con anterioridade para este ficheiro. Elimina este texto e preme o botón Aceptar se desexas borrar o ficheiro de texto correspondente á busca gardada, ou teclea texto novo para engadir outra busca.
*	control+shift+NVDA+f; abre un diálogo cun cadro de edición que amosa a última busca gardada; neste diálogo tamén podes selecionar as buscas gardadas con anterioridade dende un cadro combinado e escoller unha  acción dende o seguinte cadro combinado. Se non hai ficheiros dispoñibles para buscas específicas no documento actual, NVDA advertiráche de que non se atopa ningún ficheiro para busca específica.
*	control+shift+NVDA+k; Garda a posición actual como unha marca
*	control+shift+NVDA+suprimir; borra a marca correspondente a esta posición.
*	control+shift+k; Móvese cara a seguinte marca.
*	shift+NVDA+k; Móvese cara a marca anterior.
*	NVDA+k; Copia ó portapapeis o nome do ficheiro, sin extensión, onde gardará os datos place marker.

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
