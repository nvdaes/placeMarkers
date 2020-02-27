# marcadores de lugar #
* Autores: Noelia, Chris.
* Compatibilidade com NVDA: 2019.3 ou posterior.
* baixe a [versão estável][1]
* baixe a [versão de desenvolvimento][2]

Este complemento é usado para salvar e procurar cadeias de texto ou
marcadores específicos. Ele pode ser usado em páginas de Internet ou
documentos no modo de navegação do NVDA. Pode-se também usá-lo para salvar
ou procurar cadeias de texto em controles multilinha; nesse caso, se não for
possível atualizar o cursor, a cadeia correspondente será copiada para a
área de transferência, para que possa ser buscada por outras ferramentas. O
plug-in salva as cadeias e marcadores especificados em arquivos cujos nomes
são baseados no título e no endereço do atual documento. Este complemento é
baseado nos complementos SpecificSearch e Bookmark&Search, desenvolvidos
pelo mesmo autor. Você deve desinstalá-los para usar este aqui, pois eles
têm teclas de atalho e recursos em comum.

## Teclas de comando: ##

*	control+shift+NVDA+f: Abre um diálogo com uma caixa de edição que mostra a
  última busca salva; nesse diálogo, você também pode selecionar numa caixa
  de combinação as buscas salvas anteriormente ou remover do histórico a
  cadeia selecionada usando uma caixa de seleção. Pode escolher se o texto
  contido na caixa de seleção será acrescentado ao histórico de textos
  salvos. Por mim, escolha uma ação no grupo seguinte de botões de opção
  (entre procurar próximo, procurar anterior ou não procurar) e especifique
  se o NVDA fará uma busca diferenciando maiúsculas. Quando pressionar OK, o
  NVDA buscará essa cadeia.
*	control+shift+NVDA+k: Salva a posição atual como marcador. Caso queira
  fornecer um nome para o marcador, selecione algum texto desta posição
  antes de salvar.
*	control+shift+NVDA+delete: Apaga o marcador correspondente a esta posição.
*	NVDA+k: Moves para o próximo marcador.
*	shift+NVDA+k: Moves para o marcador anterior.
*	Não atribuído: Mostra o nome do arquivo no qual serão salvos os dados de
  marcadores de lugar, sem a extensão.
*	alt+NVDA+k: Abre uma caixa de diálogo com os marcadores salvos para este
  documento. Você pode escrever uma nota para cada marcador; pressione
  Salvar nota para salvar as alterações. Pressionando Excluir você pode
  remover o marcador selecionado. Pressionando OK você pode se mover para a
  posição selecionada.
*	Não atribuído: salva uma posição como um marcador temporário.
*	Não atribuído: Move para o marcador temporário do documento atual.
*	Não atribuído: localiza a ocorrência seguinte do último texto buscado em
  qualquer documento específico.
*	Não atribuído: localiza a ocorrência anterior do último texto buscado em
  qualquer documento específico.


## Submenu Marcadores de lugar (NVDA+N) ##

Ao usar o submenu Marcadores de lugar no menu Preferências do NVDA, pode
acessar:

*	Pasta de busca específica: abre uma pasta com buscas específicas salvas
  anteriormente.
*	Pasta de marcadores: Abre uma pasta com os marcadores salvos.
*	Copiar pasta de marcadores de lugar: Pode salvar uma cópia da pasta de
  marcadores.
*	Restaurar marcadores de lugar: Pode restaurar os marcadores a partir de
  uma pasta de marcadores de lugar anteriormente salva.

Nota: A posição do marcador é baseada no número de caracteres; assim, em
páginas de conteúdo dinâmico, é melhor usar a busca específica e não
marcadores.

## Mudanças na 14.0 ##
*	O comando para copiar o nome do arquivo no qual os dados dos marcadores de
  lugar serão salvos foi substituído por um comando que mostra esse nome de
  arquivo no modo de navegação. Ele não está atribuído a um gesto.
*	O campo "Texto a buscar" não se sobrepõe mais ao campo "texto
  salvo". (Agradecimentos a Cyrille Bougot).
*	Requer NVDA 2019.3 ou posterior.

## Mudanças na 13.0 ##
*	Adicionado um comando não atribuído para localizar as ocorrências seguinte
  e anterior do último texto buscado em qualquer documento específico.
*	O recurso de busca específica funciona quando o diálogo Sobre o NVDA
  estiver aberto.
*	No diálogo de busca específica, a caixa de seleção diferenciar maiúsculas
  estará marcada se essa opção tiver sido selecionada na última busca.
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
*	O diálogo para salvar uma cadeia de texto para busca específica foi
  removido. Essa função está agora incluída no diálogo de busca específica,
  que foi remodelada para permitir ações diferentes ao pressionar o botão
  OK.
*	A apresentação visual dos diálogos foi melhorada, aderindo à aparência dos
  diálogos mostrados no NVDA.
*	Agora ao executar um comando Procurar Próximo ou Procurar Anterior no modo
  de navegação, será feita corretamente uma busca com diferenças de caixa se
  a procura original for com diferenças de caixa.
*	Requer NVDA 2016.4 ou posterior.
*	Agora você pode atribuir gestos para abrir os diálogos de copiar e
  restaurar marcadores de lugar.
*	O NVDA apresentará uma mensagem para notificar quando marcadores de lugar
  forem copiados ou restaurados, com os respectivos diálogos.

## Mudanças na 6.0 ##
* Quando não é possível usar os recursos do complemento, os gestos são
  enviados para o aplicativo correspondente.

## Mudanças na 5.0 ##
* Adicionada busca com diferenciação de maiúsculas.
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
* Adicionado opção de salvar e apagar diferentes buscas para um mesmo
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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
