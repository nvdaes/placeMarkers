# Marcadores de lugar (placeMarkers) #

* Autores: Noelia, Chris.
* download [stable version][1] (compatible with NVDA 2022.1 and beyond)

Este complemento é usado para salvar e pesquisar cadeias de texto ou
marcadores específicos. Ele pode ser usado em páginas de Internet ou
documentos no modo de navegação do NVDA. Pode-se também usá-lo para salvar
ou pesquisar cadeias de texto em controles multilinha; nesse caso, se não
for possível atualizar o cursor, a cadeia correspondente será copiada para a
área de transferência, para que possa ser pesquisada por outras
ferramentas. O plug-in salva as cadeias e marcadores especificados em
arquivos cujos nomes são baseados no título e no endereço do documento
atual. Este complemento é baseado nos complementos SpecificSearch e
Bookmark&Search, desenvolvidos pelo mesmo autor. Você deve desinstalá-los
para usar este aqui, pois eles têm teclas de atalho e recursos em comum.

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
*	control+shift+NVDA+k: Salva a posição atual como marcador. Caso queira
  fornecer um nome para o marcador, selecione algum texto desta posição
  antes de salvar.
*	control+shift+NVDA+delete: Exclue o marcador correspondente a esta
  posição.
*	NVDA+k: Passa para o próximo marcador.
*	shift+NVDA+k: Passa para o marcador anterior.
*	Não atribuído: Mostra o nome do arquivo no qual serão salvos os dados de
  marcadores de lugar, sem a extensão.
*	alt+NVDA+k: Abre uma caixa de diálogo com os marcadores salvos para este
  documento. Você pode escrever uma nota para cada marcador; pressione
  Salvar nota para salvar as alterações. Pressionando Excluir você pode
  remover o marcador selecionado. Pressionando OK você pode se mover para a
  posição selecionada.
*	Não atribuído: salva uma posição como um marcador temporário.
*	Não atribuído: Move para o marcador temporário do documento atual.
*	Não atribuído: localiza a ocorrência seguinte do último texto pesquisado
  em qualquer documento específico.
*	Não atribuído: localiza a ocorrência anterior do último texto pesquisado
  em qualquer documento específico.


## Submenu Marcadores de lugar (NVDA+N) ##

Ao usar o submenu Marcadores de lugar no menu Preferências do NVDA, pode
acessar:

*	Pasta de pesquisa específica: abre uma pasta com pesquisas específicas
  salvas anteriormente.
*	Pasta de marcadores: Abre uma pasta com os marcadores salvos.
*	Copiar pasta de marcadores de lugar: Pode salvar uma cópia da pasta de
  marcadores.
*	Restaurar marcadores de lugar: Pode restaurar os marcadores a partir de
  uma pasta de marcadores de lugar anteriormente salva.

Nota: A posição do marcador é baseada no número de caracteres; assim, em
páginas de conteúdo dinâmico, é melhor usar a pesquisa específica e não
marcadores.

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
* Compatível com o NVDA 2021.1 ou posterior (requerido).
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=placeMarkers

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
