# placeMarkers #

* 作者: Noelia, Chris.

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

## キーコマンド: ##

*	control+shift+NVDA+f:
  最後に保存された検索のエディットボックスのあるダイアログを開きます。このダイアログでは以前に保存した検索をコンボボックスから選択したり、選択した文字列をチェックボックスを使用して履歴から削除したり出来ます。エディットボックスに含まれる文字列を、保存した文字列の履歴に追加するかどうかを選択出来ます。最後に、次の組のラジオボタンから、動作を選択します（次を検索、前を検索、または検索しない）。OKを押すと、NVDAはその文字列を探します。
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
*	アサインなし: 特定のドキュメントで最後に検索された文字列について、次の物を見つけます。
*	アサインなし: 特定のドキュメントで最後に検索された文字列について、前の物を見つけます。


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

## 23.0の変更点
* このアドオンが再びMicrosoft Wordで動作するようになりました。

## 22.0の変更点
* ブックマークに移動し、有効化されたUIAから削除出来るようになりました。Abdelのおかげです。

## 21.0の変更点
* Chromiumベースのブラウザで有効化されたUIAで、ブックマークを保存出来るようになりました。Abdelのおかげです。

## 20.0の変更点
* NVDA 2022.1以降が必要です。

## 19.0の変更点 ##
* アドオンがセキュア画面で動作不能になりました。

## 18.0の変更点 ##
* placeMakerのパスを見るコマンドが、永久的なブックマークか、特定の検索の単語か、現在のドキュメントの一時的なブックマークかを表示するようになりました。

## バージョン 17.0 ##
* 一部のドキュメントでplace markerを保存出来ないバグを修正しました。
* 翻訳が適切に動作するように、翻訳された文字列を修正しました。

## バージョン 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* 一時的なブックマークに移動する時に、流し読みをサポートするようになりました。
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## 15.0の変更点 ##
* NVDA
  2020.4からの次を検索および前を検索コマンドに従い、ブラウズモードで全て読み上げで読み上げている時、流し読みの選択肢が有効化されていると、特定の次を検索および特定の前を検索コマンドにより、読み上げが停止しなくなりました。
* 特定の前を検索コマンドを実行後に特定の検索ダイアログが開いている時、前の選択肢を検索が選択されるようになりました。

## 14.0の変更点 ##
*	place
  markersのデータが保存されるファイル名のコピーのコマンドが、ブラウズモードでそのファイル名を表示するコマンドに変更されました。これはジェスチャーに割り当てされていません。
*	「検索文字列」フィールドが「保存された文字列」フィールドに重ならなくなりました（Cyrille Bougotのおかげです）。
*	NVDA2019.3以降が必要です。

## 13.0の変更点 ##
*	特定のドキュメントで最後に検索した文字列の次または前の物を見つける、アサインなしのコマンドを追加しました。
*	特定の検索機能は、NVDAのAboutダイアログが開いている時に動作します。
*	特定の検索のダイアログでは、最後に行った検索でチェックされていた場合、大文字と小文字の区別のチェックボックスはチェックされます。
*	アドオンがアップデートされた場合、アドオンの前のバージョンで保存されていたブックマークと特定の検索の文字列は、自動的に新しいバージョンにコピーされます。ただし、Place
  MarkersをNVDAのメインの設定フォルダに保存するようにしている場合を除きます。
*	Place
  Markersをコピーするダイアログを使用する時、選択されたフォルダの名前が、placeMarkersBackupでない場合は、この名前のサブフォルダが作られ、ドキュメントやダウンロードなどの重要なデータを含むディレクトリが消去されてしまうのを防ぎます。

## 12.0の変更点 ##
*	ノートダイアログを開こうとした時に、ブックマークの保存前に、中国の文字が選択されていると、NVDAのクラッシュの原因となる重大なバグを修正しました。

## 11.0の変更点 ##
*	NVDA 2018.3以降に互換します。（2018.3以降が必要）
*	必要な場合は、[NVDA 2017.3に互換する最後のバージョン][3]もダウンロード出来ます。

## 10.0の変更点 ##
*	Edgeでは、ブックマーク選択に関するジェスチャー、NVDA+k、NVDA+shift+kまたはNVDA+alt+kは、カーソルをブックマークに移動する代わりに、アプリケーションに送られます。これは、特に長いドキュメントにおいて、エラーを避けるためです。
*	現時点では、Edgeでは、特定の検索がサポートされています。

## 9.0の変更点
*	ノートダイアログからブックマークに移動する時に、レビューカーソルがシステムカーソルを追随します。
*	前のブックマークを選択するコマンドが、適切に動作するようになりました。
*	ブックマークをノートダイアログから削除出来ます。
*	それぞれのドキュメントに対して一時的なブックマークを保存したり移動したりするジェスチャーを保存出来ます。

## 8.0の変更点 ##
*	部分識別子をブックマークのファイル名から削除しました。これにより、VitalSource Bookshelf ePub
  Readerでの問題を回避出来ます。
*	ノートダイアログを追加して、保存されたブックマークにコメントを付けられるようにし、選択された位置に移動出来るようになりました。

## 7.0の変更点 ##
*	特定の検索の文字列を保存するダイアログが除かれました。この機能は現在、特定の検索のダイアログに含まれ、OKボタンを押した時に別の動作となるように再設計されました。
*	ダイアログの見た目が拡張され、NVDAで見られるダイアログの外見に似るようになりました。
*	元々の見つけるでの検索が、大文字と小文字を区別する物だった場合に、ブラウズモードでの、次を見つける、前を見つけるコマンドの実行が、正確に大文字と小文字を区別して行われるようになりました。
*	NVDA2016.4以降が必要です。
*	Place markersのコピーと復元ダイアログを開くジェスチャーを設定出来るようになりました。
*	Place markersがコピーまたは復元されると、NVDAは、対応するダイアログでメッセージを表示します。

## 6.0の変更点 ##
* ジェスチャーに対応するアドオンの機能が使用出来ない場合、そのジェスチャーは対応するアプリケーションに送られるようになりました。

## 5.0の変更点 ##
* 大文字と小文字を区別した検索が追加されました。
* プレイスマーカーのメニューから、説明を開く項目を削除しました。
* より直観的なキーコマンドになりました。

## 4.0の変更点 ##
* FirefoxのePUBREADERアドオンでの問題を避けるため、ブックマークのファイル名から、部分識別子を削除しました。
* アドオンヘルプはアドオンマネージャーから使用可能になりました。

## 3.1の変更点 ##
* 翻訳の更新と新しい言語。
* 流し読みでブックマーク位置が通知されないようになりました。

## 3.0の変更点 ##
* 流し読みのサポートが追加されました。

## 2.0の変更点 ##
* それぞれの検索を、別々のファイルに保存と削除をする選択肢が追加されました。
* ラテン文字以外の文字がパスに入っている場合に起きる不具合が修正されました。
* NVDAジェスチャー入力ダイアログを使用して、ショートカットを再設定できるようになりました。

## 1.0の変更点 ##
* 最初のバージョン。
* 次の言語に翻訳されました:
  ブラジルポルトガル語、ファルシ(ペルシア)語、フィンランド語、フランス語、ガリシア語、ドイツ語、イタリア語、日本語、韓国語、ネパール語、ポルトガル語、スペイン語、スロバキア語、スロベニア語、タミル語。

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
