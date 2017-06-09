# marcadores #

* Autores: Noelia, Chris.
* baixe a [versão estável][1]
* baixe a [versão de desenvolvimento][2]

This addon is used for saving and searching specific text strings or
bookmarks. It can be used  on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
bookmarks to files whose name is based on the title and URL of the current
document.  This addon is based on SpecificSearch and Bookmark&Search,
developed by the same author. You should uninstall them to use this one,
since they have common keystrokes and features.

## Teclas de comando: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.


## Submenu Marcadores (NVDA+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Pasta de busca específica: abre uma pasta com buscas específicas salvas
  anteriormente.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.

## Changes for 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Requires NVDA 2016.4 or later.
*	Now you can assign gestures to open the Copy and Restore place markers
  dialogs.
*	NVDA will present a message to notify when place markers have been copied
  or restored with the corresponding dialogs.

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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev
