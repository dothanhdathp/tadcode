# Tổng Quan

Trước khi có thể sử dụng _gstreamer_, điều kiện tiên quyết là phải hiểu cách thức hoạt động của nó.

## GStreamer là gì?

GStreamer là một framework để tạo ra các ứng dụng truyền phát đa phương tiện. Thiết kế cơ bản của nó xuất phát từ hệ thống xử lý video tại Viện Sau đại học Oregon, cũng như một số ý tưởng từ DirectShow.

Khung phát triển GStreamer cho phép viết bất kỳ loại ứng dụng đa phương tiện truyền phát nào. Khung GStreamer được thiết kế để dễ dàng viết các ứng dụng xử lý âm thanh, video hoặc cả hai. Nó không chỉ giới hạn ở âm thanh và video, mà còn có thể xử lý bất kỳ loại luồng dữ liệu nào. Thiết kế đường dẫn xử lý được tối ưu hóa để giảm thiểu chi phí phát sinh ngoài những gì các bộ lọc áp dụng tạo ra. Điều này làm cho GStreamer trở thành một khung tốt để thiết kế ngay cả các ứng dụng âm thanh cao cấp đòi hỏi độ trễ thấp.

Một trong những ứng dụng rõ ràng nhất của GStreamer là sử dụng nó để xây dựng trình phát đa phương tiện. GStreamer đã bao gồm các thành phần để xây dựng trình phát đa phương tiện có thể hỗ trợ rất nhiều định dạng, bao gồm MP3, Ogg/Vorbis, MPEG-1/2, AVI, Quicktime, mod, và nhiều hơn nữa. Tuy nhiên, GStreamer không chỉ đơn thuần là một trình phát đa phương tiện khác. Ưu điểm chính của nó là các thành phần có thể cắm thêm có thể được kết hợp và ghép nối thành các đường dẫn xử lý tùy ý, do đó có thể viết một ứng dụng chỉnh sửa video hoặc âm thanh hoàn chỉnh.

Khung phần mềm này dựa trên các plugin cung cấp nhiều codec và các chức năng khác. Các plugin có thể được liên kết và sắp xếp thành một đường dẫn xử lý dữ liệu (pipeline). Đường dẫn này xác định luồng dữ liệu. Các đường dẫn cũng có thể được chỉnh sửa bằng trình soạn thảo giao diện người dùng đồ họa (GUI) và lưu dưới dạng XML để có thể tạo thư viện đường dẫn với nỗ lực tối thiểu.

Chức năng cốt lõi của GStreamer là cung cấp một khung sườn cho các plugin, luồng dữ liệu và xử lý/đàm phán loại phương tiện. Nó cũng cung cấp một API để viết các ứng dụng sử dụng các plugin khác nhau.

## GStreamer Có Gì?

### Các Tính Năng

Cụ thể, GStreamer cung cấp:

- _**API dành cho các ứng dụng đa phương tiện**_
- _**Kiến trúc plugin (các bộ mở rộng)**_
- _**Kiến trúc đường ống**_
- _**Một cơ chế để xử lý/đàm phán loại phương tiện**_
- _**Một cơ chế đồng bộ hóa**_
- _**Hơn 250 <mark>plugin</mark> cung cấp hơn 1000 thành phần.**_
- _**Một bộ công cụ**_

### Plugins

Các <mark>plugin</mark> GStreamer có thể được phân loại thành:

- `protocols handling`: xử lý giao thức
- `sources`: Xử lý nguồn cho cả âm thanh và video (bao gồm các plugin giao thức)
- `formats` _(các định dạng)_:
    - __parsers__: _trình phân tích cú pháp_
    - __formaters__: _trình định dạng, bộ ghép kênh_
    - __muxers__: _bộ ghép kênh_
    - __demuxers__: _bộ tách kênh_
    - __metadata__: _siêu dữ liệu_
    - __subtitles__: _phụ đề_
- `codec`: bộ mã hóa và bộ giải mã
- `filters` _(các bộ lọc)_:  bộ chuyển đổi, bộ trộn, hiệu ứng, ...
- `sinks` _(sinks)_: dành cho âm thanh và video (liên quan đến các plugin giao thức)

### Thư Viện

GStreamer có các phần mở rộng _(plugins)_ được đóng gói trong các thư viện:

- `gstreamer`: các gói <u>cốt lõi</u>
- `gst-plugins-base`: tập hợp các gói <u>mẫu mực</u>, <u>thiết yếu</u> của các [Elements](gstreamer-gstreamer-concepts.md#element).
- `gst-plugins-good`: một bộ các gói chất lượng tốt theo LGPL
- `gst-plugins-ugly`: một bộ các gói chất lượng tốt có thể gây ra các vấn đề về phân phối
- `gst-plugins-bad`: một bộ các gói cần chất lượng hơn
- `gst-libav`: một bộ các gói bao bọc <mark>libav</mark> để giải mã và mã hóa
- _Một số gói khác sẽ không nằm trong các tập trên. Chúng thường được phát triển riêng cho một hệ thống chuyên biệt hoặc có thị phần khá nhỏ, đặc thù, không thuộc vào các phạm vi cơ bản_.

??? quote "Điều thú vị về thuật ngữ Sinks trong Gstreamer"
    __*Sinks*__ ở đây được dùng ở nghĩa là điểm tiêu thụ chất lỏng giống như nghĩa gốc của nó - __*bồn rửa*__. Vì _gstreamer_ con dữ liệu như dòng nước. Tại _bồn rửa_, dữ liệu được tiêu thụ theo bất kỳ cách gì nó muốn và về cơ bản thì dữ liệu đã đi ra khỏi đường ống nên không cần quan tâm nữa.

    Từ này không có nghĩa gốc ở tiếng việt vì nó là cách chơi chữ. Khá là được sử dụng nhiều trong các khái niệm về máy tính. __*Sink*__ sẽ là nơi hứng cuối cùng của một chuỗi dữ liệu, và thường sẽ có một số xử lý chung như này dành cho các bộ __*sinks*__ dữ liệu:

    - Nơi tiêu thụ chính của dữ liệu giống như loa, hoặc màn hình.
    - Tốc độ tiêu thụ có thể được cài đặt, gần giống như cách tiêu thụ nước.
    - Các đối tượng này ở thể vật lý thường sẽ có một thứ giống như "thùng chứa" hứng dữ liệu và đẩy dữ liệu từ từ ra thiết bị phần cứng (đầu ra) giống như loa hoặc màn hình.
    - Khi tốc độ dữ liệu _bị tiêu thụ_ lớn hơn tốc độ _được bơm vào_, hiện tượng sẽ là thiếu dữ liệu.
    - Khi tốc độ dữ liệu _bị tiêu thụ_ lớn hơn tốc độ _được bơm vào_, hiện tượng sẽ là _bị tràn_, lúc này thường là mất dữ liệu và yêu cầu đường ống hoặc bộ đẩy hạ thấp lưu lượng dòng chảy trong đường ống.

    Đây không phải thuật ngữ riêng của __*gstreamer*__, nó khá phổ biến trong các chuyên nghành xử lý dữ liệu như âm thanh hoặc hình ảnh.

## Nguyên tắc thiết kế

### Sạch sẽ và mạnh mẽ

GStreamer cung cấp một giao diện rõ ràng để:

- __Lập trình viên ứng dụng__ muốn xây dựng một hệ thống xử lý đa phương tiện. Lập trình viên có thể sử dụng một bộ công cụ mạnh mẽ để tạo ra các hệ thống xử lý đa phương tiện mà không cần viết một dòng mã nào. Việc thực hiện các thao tác xử lý đa phương tiện phức tạp trở nên rất dễ dàng.
- __Lập trình viên plugin__. Các lập trình viên plugin được cung cấp một API rõ ràng và đơn giản để tạo ra các plugin độc lập. Một cơ chế gỡ lỗi và theo dõi mở rộng đã được tích hợp. GStreamer cũng đi kèm với một bộ plugin thực tế phong phú, đóng vai trò như các ví dụ.

### Hướng đối tượng



## Tham Khảo

- [__*Nguồn - Giới thiệu về GStreamer*__](https://gstreamer.freedesktop.org/documentation/application-development/introduction/gstreamer.html?gi-language=c)