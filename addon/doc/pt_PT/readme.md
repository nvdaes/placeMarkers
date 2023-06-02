# Marcadores de lugar #

* Autores: Noelia, Chris.
* download [stable version][1] (compatible with NVDA 2022.1 and beyond)

Este extra é usado para guardar e procurar expressões ou marcadores de texto
específicos. Pode ser usado em páginas da Web ou documentos no modo de
navegação do NVDA. Também pode ser usado para guardar ou procurar expressões
em controlos de múltiplas linhas; neste caso, se não for possível actualizar
o cursor, a expressão será copiada para a área de transferência, para que
possa ser pesquisada usando outras ferramentas. O extra guarda as expressões
e marcadores específicos em ficheiros cujo nome se baseia no título e URL do
documento actual. Este extra é baseado em "SpecificSearch" e
"Bookmark&Search", desenvolvidos pelo mesmo autor. Deve desinstalá-los para
usar este, uma vez que têm comandos e recursos comuns.

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
*	control+shift+NVDA+y: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Apaga o marcador correspondente a esta posição.
*	NVDA+y: Moves to the next bookmark.
*	shift+NVDA+y: Moves to the previous bookmark.
*	Não atribuído: Mostra o nome do ficheiro onde os dados dos marcadores de
  lugar serão guardados em modo de navegação, sem uma extensão.
*	alt+NVDA+y: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Não atribuído: salva uma posição como um marcador temporário.
*	Não atribuído: Move para o marcador temporário do documento actual.
*	Não atribuído: Procura a próxima ocorrência do último texto procurado num
  documento específico.
*	Não atribuído: Procura a ocorrência anterior do último texto procurado num
  documento específico.


## Submenu marcadores de lugar(NVDA + N) ##

Usando o submenu de Marcadores de lugar, no menu Preferências do NVDA, pode
aceder a:

*	Pasta de procuras específicas: abre uma pasta de buscas específicas
  anteriormente guardadas.
*	Pasta de marcadores: abre uma pasta dos marcadores guardados.
*	Copiar pasta de marcadores: pode guardar uma cópia da pasta de marcadores
  de lugar.
*	Restaurar marcadores: Pode restaurar os seus marcadores a partir de uma
  cópia da pasta de Marcadores de lugar.

Nota: A posição do marcador é baseada no número de caracteres; e, portanto,
em páginas dinâmicas, é melhor usar a Procura específica, não os marcadores.

## Changes for 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Compatible with NVDA 2023.1.

## Changes for 23.0
* The add-on works again with Microsoft Word.

## Changes for 22.0
* We can move to bookmarks and delete them with UIA enabled, thanks to
  Abdel.

## Changes for 21.0
* Bookmarks can be saved with UIA enabled in browsers based on Chromium,
  thanks to Abdel.

## Changes for 20.0
* Requires NVDA 2022.1 or later.

## Changes for 19.0 ##
* The add-on cannot be run on secure screens.

## Changes for 18.0 ##
* The command to see the path for placeMarkers shows if there are permanent
  bookmarks, text for specific search or a temporary bookmark for the
  current document.

## Changes for 17.0 ##
* Fixed a bug which didn't allow to save place markers in some documents.
* Fixed translated strings making translations to work properly.

## Alterações para 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=placeMarkers

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
