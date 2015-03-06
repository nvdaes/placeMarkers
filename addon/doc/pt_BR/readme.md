# marcadores #

* Autores: Noelia, Chris.
* baixe a [versão estável][1]
* baixe a [versão de desenvolvimento][2]

Este complemento é usado para salvar e procurar cadeias de texto ou
marcadores específicos, em páginas de Internet ou documentos no modo de
navegação do NVDA. Pode ser usado também para salvar ou procurar cadeias de
texto em controles multilinha; Nesse caso, se não for possível atualizar o
cursor, a cadeia correspondente será copiada para a área de transferência,
por forma a poder ser buscada por outras ferramentas. O plug-in salva as
cadeias e marcadores especificados em arquivos de texto e pickle. O nome
desses arquivos baseia-se no título e no endereço do documento atual.

Este complemento é baseado nos complementos SpecificSearch e
Bookmark&Search, desenvolvidos pelo mesmo autor. Você tem que desinstalá-los
para usar este aqui, visto que eles possuem recursos e teclas de atalho em
comum.

## Teclas de comando: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Submenu Marcadores (NVDA+N) ##


Ao usar o submenu Marcadores, no menu Preferências, pode acessar:

*	Pasta de busca específica: abre uma pasta com buscas específicas salvas
  anteriormente.
*	Pasta de marcadores; abre uma pasta de marcadores salvos.
*	Copiar pasta do complemento de marcadores: pode salvar uma cópia da pasta
  do complemento de marcadores.
*	Restaurar marcadores; pode restaurar os marcadores a partir de uma pasta
  anteriormente salva do complemento de marcadores.
*	Arquivo de documentação, no idioma escolhido se disponível ou Inglês por
  padrão.

Nota: A posição do marcador é baseada no número de caracteres; assim, em
páginas de conteúdo dinâmico é melhor usar a busca específica e não
marcadores, que salvam uma posição precisa.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

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
