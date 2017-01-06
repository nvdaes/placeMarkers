# placeMarkers #

* 作者: Noelia, Chris.
* ダウンロード [安定版][1]
* ダウンロード [開発版][2]

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

## キー操作: ##

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


## プレイスマーカーのサブメニュー(NVDA+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	検索保存フォルダー: 検索保存フォルダーを開きます。
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

## 6.0の変更点 ##
* ジェスチャーに対応するアドオンの機能が使用出来ない場合、そのジェスチャーは対応するアプリケーションに送られるようになりました。

## 5.0の変更点 ##
* 大文字と小文字を区別した検索が追加されました
* プレイスマーカーのメニューから、説明を開く項目を削除しました
* より直観的なキーコマンドになりました

## 4.0の変更点 ##
* FirefoxのePUBREADERアドオンでの問題を避けるため、ブックマークのファイル名から、部分識別子を削除しました
* アドオン　ヘルプはアドオン　マネージャーから使用可能になりました

## 3.1の変更点 ##
* 翻訳の更新と新しい言語
* 流し読みでブックマーク位置が通知されないようになりました

## 3.0の変更点 ##
* 流し読みのサポートが追加されました

## 2.0の変更点 ##
* それぞれの検索を、別々のファイルに保存と削除をする選択肢が追加されました
* ラテン文字以外の文字がパスに入っている場合に起きる不具合が修正されました
* NVDAジェスチャー入力ダイアログを使用して、ショートカットを再設定できるようになりました

## バージョン 1.0 ##
* 最初のバージョン
* 次の言語に翻訳されました:
  ブラジルポルトガル語、ファルシ(ペルシア)語、フィンランド語、フランス語、ガリシア語、ドイツ語、イタリア語、日本語、韓国語、ネパール語、ポルトガル語、スペイン語、スロバキア語、スロベニア語、タミル語

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
