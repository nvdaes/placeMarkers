# eMule #

*	Tác giả: Noelia, Chris, Alberto.
*	NVDA tương thích: 2019.3 trở lên.
*	tải về [phiên bản chính thức][1]
*	tải về [phiên bản thử nghiệm][3]
*	tải về [phiên bản tương thích với NVDA 2017.3][4]

Add-on này giúp cải thiện khả năng tiếp cận của eMule với NVDA.  Đồng thời
cung cấp thêm các phím lệnh để chuyển đến các cửa sổ khác nhau và cung cấp
các thông tin hữu ích của eMule.

Add-on này dựa trên add-on eMuleNVDASupport, phát triển bởi cùng tác
giả. Bạn nên gỡ bỏ add-on đó để dùng add-on này vì chúng có cùng các phím
tắt và tính năng phổ biến.

Đã thử nghiệm trên [eMule][2] 0.50a.

## Các phím lệnh: ##

*	control+shift+h: chuyển focus hệ thống và chuột đến thanh công cụ chính.
*	control+shift+t: thông báo cửa sổ hiện tại.
*	control+shift+n: chuyển focus hệ thống đến trường Name (tên) trong cửa sổ
  tìm kiếm.
*	control+shift+p: trong cửa sổ tìm kiếm, chuyển focus hệ thống và  chuột
  đến danh sách các tham số tìm kiếm hoặc trường nhập liệu cho mỗi tùy chọn
  trong cửa sổ tìm kiếm.
*	control+shift+b: chuyển focus đến danh sách trong cửa sổ hiện tại. Ví dụ
  trong cửa sổ tìm kiếm, cửa sổ các dữ liệu đang tải về, v...v...
*	control+shift+o: chuyển focus hệ thống đến các hộp có thuộc tính chỉ đọc
  trong cửa sổ hiện tại. Ví dụ như các thông điệp IRC, các máy chủ đang hoạt
  động, v...v...
*	control+NVDA+f: nếu dấu nháy hệ thống đứng tại một trường nhập liệu có
  thuộc tính chỉ đọc, mở một hộp thoại tìm kiếm để dùng các phím lệnh của
  NVDA cho việc tìm kiếm văn bản.
*	control+shift+l: chuyển đối tượng điều hướng và chuột đến các tiêu đề của
  danh sách hiện tại.
*	control+shift+q: Thông báo đối tượng thứ nhất của thanh trạng thái; cung
  cấp thông tin về các hoạt động gần đây.
*	control+shift+w: thông báo đối tượng thứ hai của thanh trạng thái; bao gồm
  thông tin về những tập tin và người dùng trên máy chủ hiện tại.
*	control+shift+e: Thông báo đối tượng thứ ba của thanh trạng thái; hữu ích
  khi muốn biết tốc độ tải lên / tải xuống.
*	control+shift+r: thông báo đối tượng thứ tư của thanh trạng thái; thông
  báo kết nối của mạng eD2K và Kad.

## Quản lý các cột. ##

Khi ở trong một danh sách, bạn có thể di chuyển dấu nháy giữa các dòng và
cột bằng alt+control+ các phím mũi tên.  Trong Add-on này cũng có các lệnh
sau:

*	nvda+control+1-0: thông báo các cột từ 1 đến 10..
*	nvda+shift+1-0: thông báo các cột từ 11 đến 20.
*	nvda+shift+C: chép cột cuối cùng được đọc vào bộ nhớ tạm.

## Các thay đổi cho phiên bản 4.0 ##
*	Yêu cầu NVDA 2019.3 trở lên.

## Các thay đổi cho phiên bản 3.0 ##
*	 Để tìm kiếm văn bản trong các trường nhập liệu có thuộc tính chỉ đọc, có
   thể dùng hộp thoại tìm kiếm. Chẳng hạn như nvda+control+f để kích hoạt
   hộp thoại này.

## Các thay đổi cho phiên bản 2.0 ##
*	 Đã có trợ giúp cho add-on trong trình quản lý add-on.

## Các thay đổi cho phiên bản 1.2 ##
*	 Khi di chuyển đến các thông điệp IRC, văn bản được chọn is được thông báo
   chính xác.
*	 Phím tắt để di chuyển đến danh sách kết quả tìm kiếm đã được thiết kế lại
   để di chuyển focus đến bất cứ danh sách nào đang có trong cửa sổ hiện
   tại.
*	 Lệnh để đưa focus đến các thông điệp IRC đã được thiết kế lại để chuyển
   đến trường nhập liệu bất kì có thuộc tính chỉ đọc, làm cho có thể xem lại
   thông tin kết nối trong cửa sổ các máy chủ.
*	 Khi di chuyển chuột hay focus đến các thanh công cụ, trong vài trường
   hợp, thông tin bị đọc lại hai lần. Lỗi này đã được sửa.

## Các thay đổi cho phiên bản 1.1 ##
*	 Sửa lỗi cho mục eMule trong trình đơn trợ giúp của NVDA, khi tên của thư
   mục user config có chứa các kí tự không phải kí tự latin.
*	 Có thể gán lại các phím tắt thông qua hộp thoại quản lý các cử chỉ của
   NVDA.

## Các thay đổi cho phiên bản 1.0 ##
*	 Phiên bản đầu tiên.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
