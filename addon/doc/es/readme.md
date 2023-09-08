# placeMarkers #

* Autores: Noelia, Chris.

Este complemento se utiliza para guardar y restaurar cadenas de texto
específicas o marcas. Puede utilizarse en páginas web o en documentos en el
modo exploración de NVDA. También puede utilizarse para guardar o buscar
cadenas de texto en controles multilínea; en este caso, si no es posible
actualizar el cursor, la cadena correspondiente se copiará al portapapeles,
tal que se pueda buscar utilizando otras herramientas.  El plugin guarda las
cadenas especificadas y marcas en ficheros cuyos nombres se basan en el
título y URL del documento actual.  Este complemento se basa en
SpecificSearch y Bookmark&Search, desarrollados por el mismo autor. Deberías
desinstalarlos para utilizar éste, ya que tienen las mismas combinaciones de
teclas y características.

## Órdenes de teclado: ##

*	control+shift+NVDA+f: abre un diálogo con un cuadro de edición que muestra
  la última búsqueda guardada; en este diálogo también puedes seleccionar
  las búsquedas anteriormente guardadas desde un cuadro combinado o eliminar
  la cadena seleccionada desde el historial utilizando una casilla de
  verificación. Puedes elegir si el texto contenido en el cuadro de edición
  se añadirá al histórico de textos guardados. Finalmente, elegir una acción
  del siguiente grupo de botones de opción (entre buscar siguiente, buscar
  anterior o no buscar), y especificar si NVDA hará una búsqueda sensible a
  las mayúsculas. Cuando pulses Aceptar, NVDA buscará esta cadena.
*	control+shift+NVDA+y: guarda la posición actual como una marca. Si quieres
  proporcionar un nombre para esta marca, selecciona algún texto de esta
  posición antes de guardarla.
*	control+shift+NVDA+suprimir: elimina la marca correspondiente a esta
  posición.
*	NVDA+y: se mueve al siguiente marcador.
*	shift+NVDA+y: se mueve al marcador anterior.
*	Sin asignar: muestra el nombre del archivo donde se guardarán los datos de
  marcas en modo exploración, sin extensión.
*	alt+NVDA+y: abre un diálogo con las marcas guardadas para este
  documento. Puedes escribir una nota para cada marca; pulsa Guardar Nota
  para guardar cambios. Pulsando suprimir se elimina la nota
  seleccionada. Pulsando Aceptar puedes moverte a la posición seleccionada.
*	Sin asignar: guarda la posición actual como una marca temporal.
*	Sin asignar: Se mueve a la marca temporal para el documento actual.
*	Sin asignar: encuentra la siguiente coincidencia del último texto buscado
  en cualquier documento específico.
*	Sin asignar: encuentra la coincidencia anterior del último texto buscado
  en cualquier documento específico.


## Submmenú Place markers (NVDA+N) ##

Utilizando el submenú Place markers en el menú Preferencias de NVDA, puedes
acceder a:

*	Carpeta de búsqueda específica: abre una carpeta de búsquedas específicas
  guardadas previamente.
*	Carpeta de marcas: abre una carpeta con las marcas guardadas.
*	Copiar carpeta de marcas: puedes guardar una copia de la carpeta de
  marcas.
*	Restaurar marcas: Puedes guardar tus marcas desde una carpeta de marcas
  guardada anteriormente.

Nota: La posición de la marca se basa en el número de caracteres; y por lo
tanto en páginas con contenido dinámico es mejor usar la búsqueda específica
y no las marcas.

## Cambios para 24.0
* Se usa Y en vez de K en gestos como NVDA+k, NVDA+shift+k, NVDA+alt+k y
  NVDA+control+shift+k.
* Compatible con NVDA 2023.1.

## Cambios para 23.0
* El complemento funciona otra vez con Microsoft Word.

## Cambios para 22.0
* Podemos desplazarnos a  los marcadores y eliminarlos con UIA activada,
  gracias a Abdel.

## Cambios para 21.0
* Se pueden guardar marcadores con UIA activada en navegadores basados en
  Chromium, gracias a Abdel.

## Cambios para 20.0
* Se requiere NVDA 2022.1 o posterior.

## Cambios para 19.0 ##
* El complemento no se puede ejecutar en pantallas seguras.

## Cambios para 18.0 ##
* La orden para ver la ruta de PlaceMarkers muestra si hay marcadores
  permanentes, texto para búsquedas específicas o un marcador temporal para
  el documento actual.

## Cambios para 17.0 ##
* Corregido un fallo que no permitía guardar marcadores de posición en
  algunos documentos.
* Corrección de cadenas traducidas para que las traducciones funcionen
  adecuadamente.

## Cambios para 16.0 ##
* Compatible con NVDA 2021.1 o posterior (requerido).
* Se soporta la lectura superficial al desplazarse a marcadores temporales.
* Si es necesario, puedes descargar [otras
  versiones](https://github.com/nvdaes/placeMarkers/releases).

## Cambios para 15.0 ##
* Al leer con verbalizar todo en modo exploración, las órdenes específicas
  de buscar siguiente y buscar anterior ya no dejan de leer si la lectura
  superficial está habilitada, al igual que las órdenes Buscar siguiente y
  Buscar anterior de NVDA 2020.4.
* Cuando se abra el diálogo de búsqueda específica tras ejecutar la orden de
  búsqueda específica anterior, se seleccionará la opción Buscar anterior.

## Cambios para 14.0 ##
*	La orden para copiar el nombre del archivo donde se guardarán los datos de
  Place Markers se ha sustituido por una orden que muestra el nombre de este
  archivo en modo exploración. Esta orden no tiene gesto asignado.
*	El campo "Texto a buscar" ya no se superpone al campo "Texto
  guardado". (Gracias a Cyrille Bougot).
*	Se requiere NVDA 2019.3 o posterior.

## Cambios para 13.0 ##
*	Se han añadido órdenes sin asignar para encontrar las coincidencias
  siguientes y anteriores del último texto buscado de cualquier documento
  específico.
*	La característica de búsqueda específica funciona cuando el diálogo Acerca
  de NVDA está abierto.
*	En el diálogo de búsqueda específica, la casilla sensible a mayúsculas
  estará marcada si se seleccionó esta opción en la última búsqueda.
*	Cuando el complemento se actualice, los marcadores y las cadenas de
  búsqueda específica guardadas en la versión anterior del complemento se
  copiarán automáticamente a la nueva versión, a menos que prefieras
  importar marcadores de la carpeta de configuración principal de NVDA.
*	Al usar el diálogo para copiar marcadores, si la carpeta elegida no se
  llama placeMarkersBackup, se creará una subcarpeta con este nombre para
  evitar la eliminación de directorios que contengan datos importantes,
  tales como Documentos o Descargas.

## Cambios para 12.0 ##
*	Solucionado un error crítico que causaba el cierre de NVDA al tratar de
  abrir el diálogo de notas si estaban seleccionados caracteres chinos antes
  de guardar marcadores.

## Cambios para 11.0 ##
*	Compatible con NVDA 2018.3 o posterior (requerido).
*	Si fuese necesario, puedes descargar la [última versión compatible con
  NVDA 2017.3][3].

## Cambios para 10.0 ##
*	En Edge, los gestos asociados con la selección de marcas, tales como
  NVDA+k, NVDA+shift+k o NVDA+alt+k, se enviarán a la aplicación en lugar de
  intentar mover el cursor a las marcas, para evitar errores, especialmente
  en documentos largos.
*	Ahora se admite la búsqueda específica en Edge.

## Cambios para 9.0
*	Al moverse a una marca desde el cuadro de diálogo Notas, El cursor de
  revisión sigue al cursor del sistema.
*	La orden para seleccionar la marca anterior funciona de nuevo
  adecuadamente.
*	Las marcas pueden eliminarse desde el cuadro de diálogo Notas.
*	Ahora puedes asignar gestos para guardar y moverte a una marca temporal
  para cada documento.

## Cambios para 8.0 ##
*	Eliminados fragmentos de identificadores de nombres de ficheros de marcas,
  los cuales pueden evitar problemas en VitalSource Bookshelf ePUB READER.
*	Se añadió un diálogo Notas, para asociar comentarios para marcas guardadas
  y para moverte a la posición seleccionada.

## Cambios para 7.0 ##
*	El diálogo para guardar una cadena de texto para una búsqueda específica
  se ha eliminado. Esta funcionalidad ahora se incluye el diálogo Búsqueda
  Específica, el cual se ha rediseñado para permitir acciones diferentes al
  pulsar el botón Aceptar.
*	Se ha mejorado la presentación visual del diálogo, adhiriéndose a la
  apariencia de los diálogos mostrados en NVDA.
*	Al realizar una orden Buscar siguiente o buscar anterior en Modo
  exploración ahora se hará correctamente una búsqueda sensible a las
  mayúsculas si la búsqueda original era sensible a las mayúsculas.
*	Se requiere de NVDA 2016.4 o posterior.
*	Ahora puedes asignar gestos para abrir los diálogos Copiar y Restaurar
  marcas.
*	NVDA presentará un mensaje para notificar cuando se hayan copiado o
  restaurado las marcas con los diálogos correspondientes.

## Cambios para 6.0 ##
* Cuando las características del complemento no sean usables, los gestos se
  envían a la aplicación correspondiente.

## Cambios para 5.0 ##
* Añadida la búsqueda sensible a las mayúsculas.
* Eliminada la opción para abrir documentación desde el menú Place markers.
* Órdenes de teclado más intuitivas.

## Cambios para  4.0 ##
* Eliminados fragmentos de identificadores de nombres de ficheros de marcas,
  los cuales pueden evitar problemas en el complemento de Firefox
  ePUBREADER.
* La ayuda del complemento está disponible desde el Administrador de
  Complementos.

## Cambios para 3.1 ##
* Actualización de traducciones y nuevos idiomas.
* Ahora no se anuncia la posición de la marca en la lectura superficial.

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
