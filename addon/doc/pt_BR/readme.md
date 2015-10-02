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

*	control+shift+NVDA+s; Abre um diálogo que possibilita salvar uma cadeia textual que se queira achar no documento atual. Por padrão, é mostrado o texto anteriormente salvo para este arquivo. Apague esse texto e pressione o botão OK se quiser remover o arquivo de texto correspondente à busca salva, ou digite um novo texto para adicionar outra busca.
*	control+shift+NVDA+f; Abre um diálogo com um campo de edição que mostra a última busca salva; nesse diálogo pode-se também selecionar buscas anteriormente salvas numa caixa de combinação e escolher uma ação noutra caixa de combinação. Caso não haja arquivos de buscas específicas para o documento atual, o NVDA vai alertá-lo que não foi encontrado qualquer arquivo de busca específica.
*	control+shift+NVDA+k; salva a posição atual como um marcador
*	control+shift+NVDA+delete; apaga o marcador que corresponde a esta posição.
*	NVDA+k; vai ao próximo marcador.
*	shift+NVDA+k; vai ao marcador anterior.
*	control+shift+k; Copia para a área de transferência o nome do arquivo, sem extensão, onde serão salvos os dados dos marcadores.

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
