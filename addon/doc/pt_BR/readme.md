# marcadores #

* Autores: Noelia, Chris.
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
*	control+shift+k: Copia para a área de transferência o nome do arquivo no
  qual serão salvos os dados dos marcadores, sem a extensão.
*	alt+NVDA+k: Abre um diálogo com os marcadores salvos para este
  documento. Pode escrever uma nota para cada marcador; pressione salvar
  notas para salvar as alterações. Pressionando OK você pode mover para a
  posição selecionada.


## Submenu Marcadores (NVDA+N) ##

Ao usar o submenu Marcadores no menu Preferências do NVDA, pode acessar:

*	Pasta de busca específica: abre uma pasta com buscas específicas salvas
  anteriormente.
*	Pasta de marcadores: Abre uma pasta com os marcadores salvos.
*	Copiar pasta de marcadores: Pode salvar uma cópia da pasta de marcadores.
*	Restaurar marcadores: Pode restaurar os marcadores a partir de uma pasta
  de marcadores anteriormente salva.

Nota: A posição do marcador é baseada no número de caracteres; assim, em
páginas de conteúdo dinâmico, é melhor usar a busca específica e não
marcadores.


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
  restaurar marcadores.
*	O NVDA apresentará uma mensagem para notificar quando marcadores forem
  copiados ou restaurados, com os respectivos diálogos.

## Mudanças na 6.0 ##
* Quando não é possível usar os recursos do complemento, os gestos são
  enviados para o aplicativo correspondente.

## Mudanças na 5.0 ##
* Adicionada busca com diferenciação de maiúsculas.
* Removida a opção de abrir a documentação a partir do menu dos marcadores.
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
  Francês, Galego, Italiano, Japonês, Persa, Português, Português do Brasil,
  Tâmil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
