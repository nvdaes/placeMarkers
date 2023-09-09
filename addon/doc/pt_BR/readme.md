# Marcadores de lugar (placeMarkers) #

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

## Teclas de comando: ##

*	control+shift+NVDA+f: Abre um diálogo com uma caixa de edição que mostra a
  última pesquisa salva; nesse diálogo, você também pode selecionar numa
  caixa de combinação as pesquisas salvas anteriormente ou remover do
  histórico a sequência de caracteres selecionada usando uma caixa de
  seleção. Pode escolher se o texto contido na caixa de edição será
  acrescentado ao histórico de textos salvos. Finalmente, escolha uma ação
  no grupo seguinte de botões de opção (entre pesquisar próximo, pesquisar
  anterior ou não pesquisar) e especifique se o NVDA fará uma pesquisa
  diferenciando maiúsculas. Quando pressionar OK, o NVDA pesquisará essa
  cadeia.
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
*	Não atribuído: localiza a ocorrência seguinte do último texto pesquisado
  em qualquer documento específico.
*	Não atribuído: localiza a ocorrência anterior do último texto pesquisado
  em qualquer documento específico.


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

## Mudanças na 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* A leitura dinâmica é suportada ao mover para marcadores temporários.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Mudanças na 15.0 ##
* Ao ler com leitura contínua no modo de navegação, os comandos específicos
  localizar próximo e localizar anterior não param de ler se a opção
  Permitir leitura dinâmica estiver habilitada, de acordo com comandos
  localizar próximo e localizar anteriores do NVDA 2020.4.
* Quando o diálogo Pesquisa específica for aberto após a execução do comando
  Localizar anterior específico, a opção Pesquisar anterior será
  selecionada.

## Mudanças na 14.0 ##
*	O comando para copiar o nome do arquivo no qual os dados dos marcadores de
  lugar serão salvos foi substituído por um comando que mostra esse nome de
  arquivo no modo de navegação. Ele não está atribuído a um gesto.
*	O campo "Texto a pesquisar" não se sobrepõe mais ao campo "texto
  salvo". (Agradecimentos a Cyrille Bougot).
*	Requer NVDA 2019.3 ou posterior.

## Mudanças na 13.0 ##
*	Adicionado um comando não atribuído para localizar as ocorrências seguinte
  e anterior do último texto buscado em qualquer documento específico.
*	O recurso de pesquisa específica funciona quando o diálogo Sobre o NVDA
  estiver aberto.
*	No diálogo de pesquisa específica, a caixa de seleção diferenciar
  maiúsculas estará marcada se essa opção tiver sido selecionada na última
  pesquisa.
*	Quando o complemento for atualizado, marcadores e cadeias de buscas
  específicas salvos na versão anterior do complemento serão automaticamente
  copiados para a nova versão, a não ser que você prefira importar
  marcadores salvos da pasta principal de configurações do NVDA.
*	Ao usar o diálogo de copiar marcadores, caso a pasta escolhida não seja
  nomeada placeMarkersBackup, será criada uma subpasta com esse nome para
  prevenir o apagamento de diretórios que contenham dados importantes, tais
  como Documentos ou Downloads.

## Mudanças na 12.0 ##
*	Corrigido um erro crítico que fazia com que o NVDA falhasse ao tentar
  abrir a caixa de diálogo do Notes, se os caracteres chineses fossem
  selecionados antes de salvar os favoritos.

## Mudanças na 11.0 ##
*	Compatível com o NVDA 2018.3 ou posterior (requerido).
*	Se necessário, você pode fazer o download da [última versão compatível com
  o NVDA 2017.3][3].

## Mudanças na 10.0 ##
*	No Edge, os gestos associados à seleção de favoritos, como NVDA+k,
  NVDA+shift+k ou NVDA+alt+k, serão enviados para o aplicativo em vez de
  tentar mover o cursor para marcadores, para evitar erros, especialmente em
  documentos longos.
*	Agora, a pesquisa específica é suportada no Edge.

## Mudanças na 9.0
*	Ao mover para um marcador da caixa de diálogo Notas, o cursor de
  exploração segue o cursor do sistema.
*	O comando para selecionar o marcador anterior funciona corretamente
  novamente.
*	Os marcadores podem ser excluídos da caixa de diálogo de Notas.
*	Agora você pode atribuir gestos para salvar e mover para um marcador
  temporário para cada documento.

## Mudanças na 8.0 ##
*	Removidos identificadores de fragmentos dos nomes dos arquivos de
  marcadores, o que pode evitar problemas no VitalSource Bookshelf ePUB
  reader.
*	Acrescentado diálogo Notas, para associar comentários a marcadores salvos
  e mover para a posição selecionada.

## Mudanças na 7.0 ##
*	O diálogo para salvar uma cadeia de texto para pesquisa específica foi
  removido. Essa função está agora incluída no diálogo de pesquisa
  específica, que foi remodelada para permitir ações diferentes ao
  pressionar o botão OK.
*	A apresentação visual dos diálogos foi melhorada, aderindo à aparência dos
  diálogos mostrados no NVDA.
*	Agora ao executar um comando Localizar Próximo ou Localizar Anterior no
  modo de navegação, será feita corretamente uma pesquisa com diferenças de
  maiúsculas se a pesquisa original for com diferenças de maiúsculas.
*	Requer NVDA 2016.4 ou posterior.
*	Agora você pode atribuir gestos para abrir os diálogos de copiar e
  restaurar marcadores de lugar.
*	O NVDA apresentará uma mensagem para notificar quando marcadores de lugar
  forem copiados ou restaurados, com os respectivos diálogos.

## Mudanças na 6.0 ##
* Quando não é possível usar os recursos do complemento, os gestos são
  enviados para o aplicativo correspondente.

## Mudanças na 5.0 ##
* Adicionada pesquisa com diferenciação de maiúsculas.
* Removida a opção de abrir a documentação a partir do menu de marcadores de
  lugar.
* Teclas de comandos mais intuitivas.

## Mudanças na 4.0 ##
* Removidos identificadores de fragmentos dos nomes dos arquivos de
  marcadores, o que pode evitar problemas no complemento ePUBREADER, do
  Firefox.
* A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 3.1 ##
* Atualização de traduções e novos idiomas.
* A posição do marcador não é anunciada na leitura dinâmica.

## Mudanças na 3.0 ##
* Adicionado suporte a leitura dinâmica.

## Mudanças na 2.0 ##
* Adicionado opção de salvar e apagar diferentes pesquisas para um mesmo
  arquivo.
* Corrigido falha que inviabilizava caminhos que contivessem caracteres
  não-latinos.
* Agora é possível atribuir outras teclas de atalho usando o diálogo de
  gestos de entrada do NVDA.

## Mudanças na 1.0 ##
* Versão inicial.
* Traduzido para: Alemão, Coreano, Eslovaco, Esloveno, Espanhol, Finlandês,
  Francês, Galego, Italiano, Japonês, Persa, Português, Português
  Brasileiro, Tâmil.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
