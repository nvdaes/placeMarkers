# Marcadores de lugar (placeMarkers) #

* Autores: Noelia, Chris.

Esse complemento é usado para salvar e pesquisar sequências de texto ou
marcadores de local específicos. Ele pode ser usado em páginas da Web ou
documentos no modo de navegação do NVDA. Também pode ser usado para salvar
ou pesquisar cadeias de texto em controles de várias linhas; nesse caso, se
não for possível atualizar o cursor, a cadeia de caracteres correspondente
será copiada para a área de transferência, para que possa ser pesquisada
usando outras ferramentas.  O plug-in salva as cadeias de caracteres e os
marcadores de local especificados em arquivos cujo nome é baseado no título
e no URL do documento atual.  Esse complemento é baseado no SpecificSearch e
no Bookmark&Search, desenvolvidos pelo mesmo autor. Você deve desinstalá-los
para usar este, pois eles têm teclas e recursos comuns.

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
*	control+shift+NVDA+y: Salva a posição atual como um marcador de
  posição. Se você quiser fornecer um nome para esse marcador de posição,
  selecione algum texto dessa posição antes de salvá-lo.
*	control+shift+NVDA+delete: Exclui o marcador de posição correspondente a
  essa posição.
*	NVDA+y: Passa para o próximo marcador de posição.
*	shift+NVDA+y: Move-se para o marcador de posição anterior.
*	Não atribuído: Mostra o nome do arquivo em que os dados dos marcadores de
  posição serão salvos no modo de navegação, sem uma extensão.
*	alt+NVDA+y: Abre uma caixa de diálogo com os marcadores de posição salvos
  para este documento. Você pode escrever uma nota para cada marcador;
  pressione Salvar nota para salvar as alterações. Ao pressionar Excluir,
  você pode remover o marcador selecionado. Ao pressionar OK, você pode ir
  para a posição selecionada.
*	Não atribuído: Salva uma posição como um marcador de posição temporário.
*	Não atribuído: Move-se para o marcador de posição temporário do documento
  atual.
*	Não atribuído: localiza a ocorrência seguinte do último texto pesquisado
  em qualquer documento específico.
*	Não atribuído: localiza a ocorrência anterior do último texto pesquisado
  em qualquer documento específico.


## Submenu PlaceMarkers (NVDA+N) ##

Usando o submenu PlaceMarkers no menu Preferências do NVDA, você pode
acessar:

*	Pasta de pesquisa específica: Abre uma pasta de pesquisas específicas
  salvas anteriormente.
*	Pasta de marcadores: Abre uma pasta com os marcadores de local salvos.
*	Copia a pasta placeMarkers: Você pode salvar uma cópia da pasta
  placeMarkers.
*	Restaurar placeMarkers: Você pode restaurar seus placeMarkers de uma pasta
  placeMarkers salva anteriormente.
*	Set default place markers folder: the default folder for place markers can
  be set from this dialog. It will be saved in the normal configuration
  profile.

Nota: A posição do marcador de posição se baseia no número de caracteres;
portanto, em páginas dinâmicas, é melhor usar a pesquisa específica, não
marcadores de posição.

## Changes for 45.0.0
* Added ability to set the default placeMarkers folder.
* If plugins are reloaded while this add-on is enabled, the last saved
  configuration will be applied.
* Added copy and close buttons to browseable message when showing the
  current file where bookmarks and specific search strings are saved.

## Mudanças na 35.0
* Remoção dos parâmetros de URL dos nomes de arquivos, para que os
  marcadores sejam válidos para sites específicos em sessões diferentes.

## Mudanças na 24.0
* Y é usado em vez de k em gestos como NVDA+k, NVDA+shift+k, NVDA+alt+k e
  NVDA+control+shift+k.
* Compatível com o NVDA 2023.1.

## Mudanças na 23.0
* O complemento trabalha novamente com o Microsoft Word.

## Mudanças na 22.0
* Podemos mover para os marcadores e excluí-los com o UIA ativado, obrigado
  a Abdel.

## Mudanças na 21.0
* Os marcadores podem ser salvos com o UIA habilitado em navegadores
  baseados no Chromium, graças a Abdel.

## Mudanças na 20.0
* Requer o NVDA 2022.1 ou posterior.

## Mudanças na 19.0 ##
* O complemento não pode ser executado em telas seguras.

## Mudanças na 18.0 ##
* O comando para ver o caminho para placeMarkers mostra se há marcadores
  permanentes, texto para pesquisa específica ou um marcador temporário para
  o documento atual.

## Mudanças na 17.0 ##
* Corrigido um erro que não permitia salvar marcadores de local em alguns
  documentos.
* Corrigido cadeias de caracteres traduzidas para que as traduções funcionem
  corretamente.

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

