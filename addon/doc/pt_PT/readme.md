# Marcadores de lugar #

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

## Comandos: ##

*	control+shift+NVDA+f: abre uma caixa de diálogo com uma caixa de edição
  que mostra a última pesquisa guardada; Nesta caixa de diálogo, também pode
  seleccionar as pesquisas guardadas anteriormente de uma caixa de
  combinação ou remover a cadeia seleccionada do histórico usando uma caixa
  de selecção. Pode escolher se o texto contido na caixa de edição será
  adicionado ao histórico dos seus textos guardados. Finalmente, escolha uma
  acção do próximo grupo de botões de rádio (entre Pesquisar próximo,
  Pesquisar anterior ou Não pesquisar) e especifique se o NVDA fará uma
  pesquisa sensível a maiúsculas e minúsculas. Quando pressiona ok, o NVDA
  procurará essa cadeia.
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
*	Não atribuído: Procura a próxima ocorrência do último texto procurado num
  documento específico.
*	Não atribuído: Procura a ocorrência anterior do último texto procurado num
  documento específico.


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

## Alterações para 24.0
* Y é utilizado em vez de k em atalhos como NVDA+k, NVDA+shift+k, NVDA+alt+k
  e NVDA+control+shift+k.
* Compatível com NVDA 2023.1.

## Alterações para 23.0
* O extra funciona novamente com o Microsoft Word.

## Alterações para 22.0
* Podemos mover-nos para os marcadores e apagá-los com a UIA activada,
  graças a Abdel.

## Alterações para 21.0
* Os marcadores podem ser guardados com a UIA activada em navegadores
  baseados no Chrome, graças ao Abdel.

## Alterações para 20.0
* Requer NVDA 2022.1 ou posterior.

## Alterações para 19.0 ##
* O extra não pode ser executado em ecrãs seguros.

## Alterações para 18.0 ##
* O comando para ver o caminho para placeMarkers mostra se existem
  marcadores permanentes, texto para pesquisa específica ou um marcador de
  página temporário para o documento actual.

## Alterações para 17.0 ##
* Corrigido um erro que não permitia guardar marcadores de lugar em alguns
  documentos.
* fixadas  algumas cadeias de tradução, fazendo as traduções funcionar
  correctamente.

## Alterações para 16.0 ##
* Compatibilidade com o NVDA 2021.1 ou superiores (obrigatório).
* A leitura rápida é suportada quando se muda para os marcadores
  temporários.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Alterações para 15.0 ##
* Ao ler seguidamente, no modo de navegação, os comandos específicos
  procurar seguinte e procurar anterior,  não param mais de ler se a opção
  "permitir leitura rápida" estiver activada, de acordo com procurar,
  procurar próximo e procurar anterior do NVDA 2020.4.
* Quando o diálogo de procura específica é aberto após a execução do comando
  procurar anterior, a opção procurar anterior será seleccionada.

## Alterações para 14.0 ##
*	O comando para copiar o nome do ficheiro onde os dados dos marcadores
  serão guardados foi substituído pelo comando que mostra o nome do ficheiro
  em modo de navegação. Este comando não tem tecla associada.
*	O campo "Texto a procurar" já não se sobrepõe ao campo "Textos
  guardados". (Agradecimentos a Cyrille Bougot).
*	Requer NVDA 2019.3 ou posterior.

## Alterações para 13.0 ##
*	Adicionado comandos não atribuídos para Procurar a próxima ou a nterior
  ocorrência da última expressão procurada para qualquer documento
  específico.
*	A procura específica funciona no diálogo Sobre o NVDA'.
*	No diálogo de Procura específica, a caixa de verificação "Ignorar
  maiúsculas/minúsculas" estará marcada, se esta opção estava marcada na
  última procura.
*	Quando o extra é actualizado, os marcadores e expressões para procuras
  específicas, guardados na versão anterior, são automaticamente copiados
  para a nova versão, a não ser que prefira importar os marcadores guardados
  na pasta principal de configurações do NVDA.
*	Quando se usa o diálogo para copiar marcadores de lugar, se a pasta
  selecionada não se chamar "placeMarkersBackup", será criada uma subpasta
  com este nome para prevenir a eventual eliminação de dados importantes,
  como documentos e transferências.

## Alterações para 12.0 ##
*	Corrigido um erro crítico que fazia com que o NVDA falhasse ao tentar
  abrir a caixa de diálogo de Notas, se os caracteres chineses fossem
  seleccionados antes de guardar os favoritos.

## Alterações para 11.0 ##
*	Compatível com o NVDA 2018.3 ou posterior (requerido).
*	Se necessário, pode fazer o download da [última versão compatível com o
  NVDA 2017.3] [3].

## Alterações para 10.0 ##
*	No Edge, os comandos associados à selecção de favoritos, como NVDA + k,
  NVDA + shift + k ou NVDA + alt + k, serão enviados para a aplicação em vez
  de tentar mover o cursor para marcadores, para evitar erros, especialmente
  em documentos longos.
*	Agora, a pesquisa específica é suportada no Edge.

## Alterações para 9.0
*	Ao mover-se para um marcador da caixa de diálogo Notas, o cursor de
  revisão segue o cursor do sistema.
*	O comando para seleccionar o marcador anterior funciona, novamente, de
  modo correcto.
*	Os marcadores podem ser excluídos a partir da caixa de diálogo de Notas.
*	Agora, pode atribuir comandos para guardar e mover para um marcador
  temporário para cada documento.

## Alterações para 8.0 ##
*	Foram removidos Identificadores de fragmentos de nomes de marcadores, que
  podem evitar problemas no leitor de ePUB VitalSource Bookshelf.
*	Adicionada uma caixa de diálogo Notas, para associar comentários para
  marcadores guardados e mover para a posição seleccionada.

## Alterações para 7.0 ##
*	A caixa de diálogo para guardar uma expressão para procura específica foi
  removida. Esta funcionalidade agora está incluída na caixa de diálogo
  Procura específica, que foi redesenhada para permitir diferentes acções ao
  pressionar o botão OK.
*	A apresentação visual dos diálogos foi aprimorada, seguindo a aparência
  dos diálogos mostrados no NVDA.
*	Executar um comando Procurar Próximo ou Procurar Anterior no Modo de
  Navegação agora irá fazer uma pesquisa sensível a maiúsculas e minúsculas,
  se a procura original for sensível a maiúsculas e minúsculas.
*	Requer NVDA 2016.4 ou posterior.
*	Agora, pode atribuir comandos para abrir as caixas de diálogo de copiar e
  restaurar Marcadores.
*	O NVDA apresentará uma mensagem para notificar quando os marcadores foram
  copiados ou restaurados com as caixas de diálogo correspondentes.

## Alterações para 6.0 ##
* Quando os recursos do extra não são utilizáveis, os comandos são enviados
  para o aplicativo correspondente.

## Alterações para 5.0 ##
* Adicionada procura sensível a maiúsculas e minúsculas.
* Removida a opção para abrir a documentação a partir do menu de marcadores.
* Comandos mais intuitivos.

## Alterações para 4.0 ##
* Foram removidos Identificadores de fragmentos de nomes de marcadores, que
  podem provocar problemas no extra ePUBREADER do Firefox.
* A ajuda do extra passa a estar disponível no gestor de extras.

## Alterações para 3.1 ##
* Actualização de traduções e um novo idioma.
* A posição dos marcadores não é anunciada na leitura rápida.

## Alterações para 3.0 ##
* Adicionado suporte para leitura rápida.

## Alterações para 2.0 ##
* Adicionadas opções para guardar e excluir pesquisas diferentes para cada
  ficheiro.
* Corrigido o erro que desactivava quando os caminhos continham caracteres
  não latinos.
* Os atalhos agora podem ser reatribuídos usando a caixa de diálogo de
  definição de comandos do NVDA.

## Alterações para 1.0 ##
* Versão inicial.
* Traduzido para: Português brasileiro, farsi, finlandês, francês, galego,
  alemão, italiano, japonês, coreano, nepalês, português, espanhol,
  eslovaco, esloveno, tamil.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
