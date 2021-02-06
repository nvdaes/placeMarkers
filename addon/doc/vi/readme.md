# Đánh dấu #
* Tác giả: Noelia, Chris.
* NVDA tương thích: 2019.3 trở lên.
* tải về [phiên bản chính thức][1]
* tải về [phiên bản thử nghiệm][2]

Addon này dùng để lưu lại và tìm kiếm một chuỗi văn bản hay dấu trang cụ
thể. nó có thể được dùng trên các trang web hay tài liệu trong chế độ duyệt
của NVDA. Nó cũng có thể được dùng để lưu lại hoặc tìm kiếm các chuỗi văn
bản trong các điều khiển nhập liệu nhiều dòng; trường hợp này, nếu không thể
cập nhật dấu trang, chuỗi văn bản tương ứng sẽ được chép vào bộ nhớ tạm nên
có thể tìm kiếm bằng những công cụ khác. Plugin này lưu các chuỗi văn bản và
dấu trang được chỉ định vào các tập tin được đặt tên dựa trên tựa đề và URL
của tài liệu hiện tại. Addon này dựa trên addon SpecificSearch và
Bookmark&Search, phát triển bởi cùng tác giả. Bạn nên gỡ bỏ chúng để dùng
addon này vì chúng có những tính năng và phím lệnh trùng nhau.

## Các phím lệnh: ##

*	control+shift+NVDA+f: mở hộp thoại với ô nhập liệu hiển thị tìm kiếm cuối
  cùng được lưu; trong hộp thoại này, bạn cũng có thể chọn các tìm kiếm đã
  được lưu trước đó  từ một hộp xổ hay xóa chuỗi văn bản được chọn khỏi lịch
  sử bằng một hộp kiểm. Bạn có thể chọn để lưu văn bản hiện tại trong ô nhập
  liệu vào lịch sử lưu văn bản của bạn. Cuối cùng, chọn một hoạt động từ
  nhóm radio buttons (tìm tiếp, tìm trước hay không tìm kiếm), và thiết lập
  nếu muốn NVDA tìm kiếm phân biệt chữ hoa  thường. Khi bạn bấm okay, NVDA
  sẽ tìm kiếm chuỗi văn bản.
*	control+shift+NVDA+k: Lưu vị trí hiện tại thành một dấu trang. Nếu muốn
  đặt tên dấu trang, hãy chọn vài từ tại vị trí con trỏ trước khi lưu nó.
*	control+shift+NVDA+delete: Xóa dấu trang tại vị trí tương ứng.
*	NVDA+k: Chuyển đến dấu trang kế tiếp.
*	shift+NVDA+k: Chuyển đến dấu trang trước.
*	Chưa gán: Hiển thị tên tập tin dùng để lưu dữ liệu của các điểm đánh dấu ở
  chế độ duyệt mà không có phần mở rộng.
*	alt+NVDA+k: Mở hộp thoại với các dấu trang đã lưu cho tài liệu hiện
  tại. Bạn có thể viết ghi chú cho mỗi dấu trang; bấm Lưu ghi chú để lưu các
  thay đổi. Có thể xóa dấu trang hiện tại bằng cách bấm Delete. Bấm OK để di
  chuyển đến vị trí đã được chọn.
*	Chưa gán lệnh: Lưu một vị trí thành dấu trang tạm thời.
*	Chưa gán lệnh: Chuyển đến dấu trang tạm thời của tài liệu hiện thời.
*	Chưa gán lệnh: tìm văn bản tiếp theo có chứa nội dugn tìm kiếm gần nhất
  cho mọi tài liệu cụ thể.
*	Chưa gán lệnh: tìm văn bản trước đó có chứa nội dugn tìm kiếm gần nhất cho
  mọi tài liệu cụ thể.


## Đánh dấu thực đơn con (NVDA+N) ##

Dùng đánh dấu trình đơn con trong trình đơn Tùy Chọn, bạn có thể truy cập:

*	Thư mục tìm kiếm cụ thể: mở thư mục của những tìm kiếm cụ thể đã được lưu
  trước đó.
*	Thư mục dấu trang: mở thư mục các dấu trang đã lưu.
*	Sao chép thư mục các điểm đánh dấu: Bạn có thể tạo một bản sao của thư mục
  các điểm đánh dấu.
*	Khôi phục các điểm đánh dấu: Bạn có thể khôi phục các điểm đánh dấu từ thư
  mục các điểm đánh dấu đã lưu trước đó.

Lưu ý: vị trí dấu trang dựa trên số lượng kí tự; vậy nên trong các trang web
động thì dùng tìm kiếm cụ thể tốt hơn dấu trang.

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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
