# Đánh dấu #

* Tác giả: Noelia, Chris.

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

## Các phím lệnh: ##

*	control+shift+NVDA+f: mở hộp thoại với ô nhập liệu hiển thị tìm kiếm cuối
  cùng được lưu; trong hộp thoại này, bạn cũng có thể chọn các tìm kiếm đã
  được lưu trước đó  từ một hộp xổ hay xóa chuỗi văn bản được chọn khỏi lịch
  sử bằng một hộp kiểm. Bạn có thể chọn để lưu văn bản hiện tại trong ô nhập
  liệu vào lịch sử lưu văn bản của bạn. Cuối cùng, chọn một hoạt động từ
  nhóm radio buttons (tìm tiếp, tìm trước hay không tìm kiếm), và thiết lập
  nếu muốn NVDA tìm kiếm phân biệt chữ hoa  thường. Khi bạn bấm okay, NVDA
  sẽ tìm kiếm chuỗi văn bản.
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
*	Chưa gán lệnh: tìm văn bản tiếp theo có chứa nội dugn tìm kiếm gần nhất
  cho mọi tài liệu cụ thể.
*	Chưa gán lệnh: tìm văn bản trước đó có chứa nội dugn tìm kiếm gần nhất cho
  mọi tài liệu cụ thể.


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

## Các thay đổi cho phiên bản 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Đã hỗ trợ thay đổi vị trí đọc khi di chuyển đến dấu trang tạm thời.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Các thay đổi cho phiên bản 15.0 ##
* Khi đọc với chế độ đọc tất cả trong chế độ duyệt, các lệnh tìm trước và
  tìm tiếp không còn làm cho dừng đọc nữa nếu tùy chọn cho phép thay đổi vị
  trí khi đọc dược bật, dựa theo các lệnh tìm tiếp và tìm trước của NVDA
  2020.4.
* Nếu hộp thoại tìm kiếm cụ thể được mở sau khi gọi lệnh tìm trước, tùy chọn
  tìm kiếm trước sẽ được chọn.

## Các thay đổi cho phiên bản 14.0 ##
*	Lệnh chép tên của tập tin sẽ lưu dữ liệu của các điểm đánh dấu đã được
  thay thế bởi một lệnh để hiển thị tên này trong chế độ duyệt. Lệnh này
  không được gán thao tác.
*	Ô "Văn bản cần tìm" không còn bị tràn qua ô "Các văn bản đã lưu" nữa. (cảm
  ơn Cyrille Bougot).
*	Yêu cầu NVDA 2019.3 trở lên.

## Các thay đổi cho phiên bản 13.0 ##
*	Thêm các lệnh tìm kiếm văn bản kế và văn bản trước có chứa nội dugn tìm
  kiếm gần nhất cho mọi tài liệu cụ thể.
*	Tính năng tìm kiếm cụ thể hoạt động khi hộp thoại giới thiệu NVDA được mở.
*	Trong hộp thoại tìm kiếm cụ thể, hộp kiểm phân biệt chữ hoa thường sẽ được
  chọn nếu nó đã được chọn cho tìm kiếm trước đó.
*	Khi cập nhật add-on, các dấu trang và chuỗi tìm kiếm cụ thể đã lưu trong
  phiên bản trước đây sẽ được tự sao chép qua phiên bản mới, trừ khi bạn
  chọn nạp các dấu trang đã lưu trong thư mục cấu hình chính của NVDA.
*	Khi dùng hộp thoại để sao chép các dấu trang, nếu thư mục đã chọn không
  được đặt tên là placeMarkersBackup, một thư mục con với tên này sẽ được
  tạo để ngăn chạn việc xóa những thư mục chứa các dữ liệu quan trọng như
  Documents hay Downloads.

## Các thay đổi cho phiên bản 12.0 ##
*	Sửa một lỗi nghiêm trọng làm cho NVDA bị treo khi nỗ lực mở hộp thoại các
  ghi chú, nếu các kí tự tiếng Trung Quốc được chọn trước khi lưu các dấu
  trang.

## Các thay đổi cho phiên bản 11.0 ##
*	Tương thích với NVDA 2018.3 trở lên (yêu cầu).
*	Nếu cần, bạn có thể tải về [phiên bản cuối cùng tương thích với NVDA
  2017.3][3].

## Các thay đổi cho phiên bản 10.0 ##
*	Trong Edge, các thao tác liên quan đến chọn dấu trang như NVDA+k,
  NVDA+shift+k hay NVDA+alt+k sẽ gửi tới ứng dụng thay vì cố gắng chuyển con
  trỏ đến các dấu trang, nhằm tránh gây ra lỗi, đặc biệt là trong các tài
  liệu dài.
*	Giờ đây đã hỗ trợ tìm kiếm cụ thể trong Edge.

## Các thay đổi cho phiên bản 9.0
*	Khi chuyển đến một dấu trang từ hộp thoại ghi chú, con trỏ duyệt đi theo
  con trỏ hệ thống.
*	Phím lệnh chọn dấu trang trước đã hoạt động trở lại như mong muốn.
*	Có thể xóa các dấu trang thông qua hộp thoại ghi chú.
*	Giờ đây bạn có thể gán lệnh để lưu và di chuyển đến một dấu trang tạm thời
  cho mỗi tài liệu.

## Các thay đổi cho phiên bản 8.0 ##
*	Gỡ bỏ số nhận dạng phân đoạn từ tập tin các dấu trang, nhằm tránh gây ra
  lỗi trong VitalSource Bookshelf ePUB reader.
*	Đã thêm hộp thoại ghi chú để tích hợp chú thích cho các dấu trang đã lưu
  và di chuyển đến vị trí được chọn.

## Các thay đổi cho phiên bản 7.0 ##
*	Hộp thoại lưu chuỗi văn bản cho tìm kiếm cụ thể đã được gỡ bỏ. Tính năng
  này giờ đây được tích hợp trong hộp thoại tìm kiếm cụ thể, đã được thiết
  kế lại để cho phép thực hiện các hoạt động khác nhau khi bấm OK.
*	Trình bày trực quan của các hộp thoại đã được cải thiện, giống như cách
  xuất hiện các hộp thoại của NVDA.
*	Thực hiện lệnh tìm tiếp hay tìm trước trong chế độ duyệt giờ đây sẽ tìm
  kiếm phân biệt chữ hoa / thường một cách chính xác nếu tìm kiếm gốc là
  phân biệt chữ hoa / thường.
*	Yêu cầu NVDA 2016.4 trở lên.
*	Giờ bạn có thể  gán các thao tác để mở các hộp thoại sao chép và khôi phục
  các điểm đánh dấu.
*	NVDA sẽ phát một thông điệp để thông báo khi các điểm đánh dấu được sao
  chép hay khôi phục ở các hộp thoại tương ứng.

## Các thay đổi cho phiên bản 6.0 ##
* Khi không dùng được tính năng của add-on, các thao tác sẽ được gửi đến các
  ứng dụng tương ứng.

## Các thay đổi cho phiên bản 5.0 ##
* Thêm tính năng tìm kiếm phân biệt chữ hoa / thường.
* Gỡ bỏ tùy chọn mở tài liệu từ trình đơn đánh dấu.
* Thêm các phím lệnh trực quan.

## Các thay đổi cho phiên bản 4.0 ##
* Gỡ bỏ  số nhận dạng phân đoạn từ tên tập tin dấu trang nhằm tránh gây ra
  lỗi trong ePUBREADER Firefox add-on.
* Thông tin giúp đỡ cho add-on đã hiển thị trong phần quản lý add-on.

## Các thay đổi cho phiên bản 3.1 ##
* Cập nhất các bản dịch và ngôn ngữ mới.
* Vị trí dấu trang không được thông báo trong chế độ thay đổi vị trí đọc.

## Các thay đổi cho phiên bản 3.0 ##
* Thêm hỗ trợ cho thay đổi vị trí đọc.

## Các thay đổi cho phiên bản 2.0 ##
* Thêm các tùy chọn để lưu và xóa các tìm kiếm khác nhau cho mỗi tập tin.
* Sửa lỗi bị treo khi đường dẫn chứa các kí tự không phải chữ latin.
* Các phím tắt giờ đây có thể gán lại bằng hộp thoại quản lý thao tác của
  NVDA.

## Các thay đổi cho phiên bản 1.0 ##
* Phiên bản đầu tiên.
* Đã dịch sang các ngôn ngữ: Bồ Đào Nha brazi, Farsi, Phần Lan, Pháp,
  Galicia, Đức, Ý, Nhật, Hàn Quốc, Nepal, Bồ Đào Nha, Tây Ban Nha, Slovak,
  Slovenia, Nam Ấn Độ.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
