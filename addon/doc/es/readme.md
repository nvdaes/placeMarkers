# eMule #

*	Autores: Noelia, Chris, Alberto.
*	Compatibilidad con NVDA: 2019.3 o posterior.
*	descarga [versión estable][1]
*	descargar [versión de desarrollo][3]
*	descargar [versión compatible con NVDA 2017.3][4]

Este complemento te ayuda a mejorar la accesibilidad de eMule con
NVDA. También proporciona comandos de teclado adicionales para moverse en
diferentes ventanas y da información útil de eMule.

Se basa en el complemento eMuleNVDASupport, desarrollado por el mismo
autor. Debes desinstalar el viejo complemento para usar este, ya que ambos
tienen atajos de teclado y características en común.

Probado en [eMule] [2] 0.50A.

## Órdenes de teclado: ##

*	control+shift+h: mueve el foco y el ratón a la barra de herramientas
  principal.
*	control+shift+t: lee la ventana actual.
*	control+shift+n: Mueve el foco al campo nombre en la ventana de Búsqueda.
*	control+shift+p: En la ventana de Búsqueda, mueve el foco y el ratón a la
  lista de parámetros de búscqueda, o al campo de edición de opciones .
*	control+shift+b: Mueve el foco a la lista en la ventana actual. Por
  ejemplo útil en la ventana Buscar, Descargas en ventana de Transferencia,
  etc.
*	control+shift+o: Mueve el foco a los cuadros de edición de sólo lectura en
  la ventana actual. Por ejemplo, mensajes recibidos de IRC , Servidores
  disponibles, etc.
*	control+NVDA+f: si el cursor está colocado en un cuadro de edición de sólo
  lectura, abre un diálogo de búsqueda para utilizar las órdenes para
  encontrar texto disponibles en NVDA.
*	control+shift+l: Mueve el navegador de objetos y el ratón a los
  encabezados de la lista actual.
*	control+shift+q: Lee el primer objeto en la barra de estado; proporciona
  información acerca de la actividad reciente.
*	control+shift+w: Lee el segundo objeto de la barra de estado; contiene
  información acerca de ficheros y usuarios en el servidor actual.
*	control+shift+e: Lee el tercer objeto de la barra de estado; útil para
  saber la velocidad de subida y bajada.
*	control+shift+r: Lee el cuarto objeto de la barra de estado; informa sobre
  la conexión de las redes Kad y eD2K.

## Administrando columnas. ##

Cuando estés dentro de una lista, puedes mover el cursor  entre las filas y
las columnas utilizando alt+control+Flechas.  En este complemento también
están disponibles las siguientes órdenes de teclado:

*	nvda+control+1-0: Lee las primeras 10 columnas.
*	nvda+shift+1-0: Lee las columnas 11 a 20.
*	nvda+shift+C: Copia el contenido de la última columna leída al
  portapapeles.

## Cambios para 4.0 ##
*	Se requiere NVDA 2019.3 o posterior.

## Cambios para 3.0 ##
*	 Para buscar texto en cuadros de edición de sólo lectura, se puede usar el
   diálogo Buscar, por ejemplo pulsando NVDA+control+f para activarlo.

## Cambios para 2.0 ##
*	 La ayuda del complemento está disponible en el Administrador de
   Complementos.

## Cambios para 1.2 ##
*	 Al moverse a los mensajes del IRC, el texto seleccionado se anuncia
   apropiadamente.
*	 La combinación de teclas usada para mover a la lista de resultados de la
   búsqueda se ha generalizado para ser capaz de mover el foco a cualquier
   lista disponible en la ventana actual.
*	 La orden usada para enfocar los mensajes de IRC se ha generalizado para
   moverse a cualquier casilla de edición de sólo lectura, por lo que es
   posible revisar la información de conexión en la ventana Servidores.
*	 Al mover el ratón y el foco a la barra de herramientas, en algunos casos
   se anunciaba dos veces. Esto ha sido corregido.

## Cambios para 1.1 ##
*	 Solucionado un problema en el elemento eMule en el menú Ayuda de NVDA,
   cuando el nombre de la carpeta de configuración de usuario contiene
   caracteres no latinos.
*	 Los atajos ahora pueden reasignarse utilizando el diálogo gestos de
   entrada de NVDA.

## Cambios para 1.0 ##
*	 Versión inicial.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
