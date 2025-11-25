# \[C\] Phases of translation

Tệp nguồn C được trình biên dịch xử lý như thể các giai đoạn sau diễn ra theo thứ tự chính xác này. Việc triển khai thực tế có thể kết hợp các hành động này hoặc xử lý chúng theo cách khác nhau miễn là hành vi đó giống nhau.

## Giai đoạn 1 (Phase 1)

1. Các byte riêng lẻ của tệp mã nguồn (thường là tệp văn bản trong một số mã hóa nhiều byte như __UTF-8__) được ánh xạ, theo cách xác định khi triển khai, tới các ký tự của bộ ký tự nguồn. Đặc biệt, các chỉ báo cuối dòng phụ thuộc vào hệ điều hành được thay thế bằng các ký tự dòng mới.
    Bộ ký tự nguồn là bộ ký tự nhiều byte bao gồm bộ ký tự nguồn cơ bản dưới dạng tập hợp con một byte, bao gồm 96 ký tự sau:
    1. 5 ký tự khoảng trắng _(space, horizontal tab, vertical tab, form feed, new-line)_
    1. 10 ký tự chữ số từ `0` tới `9`
    1. 52 ký tự chữ cái từ `a` tớ `z` và từ `A` tới `Z`
    1. 29 ký tự dấu chấm câu: `_ { } [ ] # ( ) < > % : ; . ? * + - / ^ & | ~ ! = , \ " '`
1. [*__Trigraph sequences__ (Biểu diễn toán tử thay thế)*]() được thay thế bằng các biểu diễn ký tự đơn tương ứng. (cho đến C23)
    - _Tiến trình này là thay thế một số ký tự đặc biệt thành cấu trúc khác giúp hỗ trợ hiểu sâu cú pháp, tăng tốc phân tích biên dịch và tương thích với nhiều hệ thống nhưng đã bị lược bỏ._

## Giai đoạn 2 (Phase 2)

1. Bất cứ khi nào dấu gạch chéo ngược xuất hiện ở cuối dòng (ngay sau ký tự dòng mới), cả dấu gạch chéo ngược và dòng mới đều bị xóa, kết hợp hai dòng nguồn vật lý thành một dòng nguồn logic. Đây là thao tác một lần: một dòng kết thúc bằng hai dấu gạch chéo ngược theo sau là một dòng trống không kết hợp ba dòng thành một.
1. Nếu tệp nguồn không trống không kết thúc bằng ký tự dòng mới sau bước này (cho dù ban đầu nó không có dòng mới hay kết thúc bằng dấu gạch chéo ngược), thì hành vi đó không được xác định.

!!! note "Note"
    Nối các dòng __*marco-defined*__ thành một.

    Việc dùng dấu `\` đặt ở cuối dòng có tác dụng nối nhiều dòng thành một cho các định nghĩa [tiền xử lý](c-preprocessor.md).

## Giai đoạn 3 (Phase 3)

- Tệp nguồn được phân tách thành nhận xét, chuỗi ký tự khoảng trắng (dấu cách, tab ngang, dòng mới, tab dọc và nguồn cấp dữ liệu biểu mẫu) và mã thông báo tiền xử lý, như sau:
    1. Tệp tiêu đề: `<stdio.h>` hoặc `"myfile.h"`
    1. Số nhận dạng
    1. Số tiền xử lý, bao gồm các hằng số nguyên và hằng số động, nhưng cũng bao gồm một số mã thông báo không hợp lệ như `1..E+3.foo` hoặc `0JBK`
    1. Hằng ký tự và chuỗi ký tự
    1. Toán tử và dấu chấm câu, chẳng hạn như `+`, `<<=`, `<%`, hoặc `##`.
    1. Các ký tự không phải khoảng trắng riêng lẻ không phù hợp với bất kỳ danh mục nào khác
- Mỗi bình luận được thay thế bằng một ký tự khoảng trắng
- Các dòng mới được giữ lại và được xác định bằng cách triển khai liệu các chuỗi khoảng trắng không phải dòng mới có thể được thu gọn thành các ký tự khoảng trắng đơn hay không.

Nếu đầu vào đã được phân tích cú pháp thành các mã thông báo tiền xử lý có tối đa một ký tự nhất định thì mã thông báo tiền xử lý tiếp theo thường được coi là chuỗi ký tự dài nhất có thể tạo thành mã thông báo tiền xử lý, ngay cả khi điều đó có thể khiến phân tích tiếp theo không thành công. Điều này thường được gọi là nhai tối đa.

## Giai đoạn 4 (Phase 4)

1. [Bộ tiền xử lý](c-preprocessor.md) được thực thi.
1. Mỗi tệp được thêm vào bằng lệnh `#include` sẽ trải qua các giai đoạn từ 1 đến 4 theo cách đệ quy.
1. Vào cuối giai đoạn này, tất cả các chỉ thị tiền xử lý sẽ bị xóa khỏi nguồn.

## Giai đoạn 5 (Phase 5)

Tất cả các ký tự và chuỗi thoát trong hằng ký tự và chuỗi ký tự đều được chuyển đổi từ bộ ký tự nguồn sang bộ ký tự thực thi (có thể là bộ ký tự nhiều byte như UTF-8, miễn là tất cả 96 ký tự từ bộ ký tự nguồn cơ bản được liệt kê trong giai đoạn 1 đều có biểu diễn một byte). Nếu ký tự được chỉ định bởi chuỗi thoát không phải là thành viên của bộ ký tự thực thi thì kết quả được xác định theo cách triển khai nhưng được đảm bảo không phải là ký tự rỗng (rộng).

!!! note "Note"
    Việc chuyển đổi được thực hiện ở giai đoạn này có thể được kiểm soát bằng các tùy chọn dòng lệnh trong một số triển khai: __gcc__ và __clang__ sử dụng `-finput-charset` để chỉ định _mã hóa bộ ký tự nguồn_, `-fexec-charset` và `-fwide-exec-charset` để _chỉ định mã hóa của bộ ký tự thực thi_ trong chuỗi ký tự chuỗi và hằng ký tự không có tiền tố mã hóa __*(kể từ C11)*__.

### Giải thích

_Đọc bước này có hơi lú lú cái đầu nên phải tìm hiểu thêm tý_

Bước này về cơ bản có nghĩa là chuyển đổi ký tự của tệp nguồn `.c`, `.h`, ... thành bộ ký tự thực thi. Dựa theo chương trình được sử dụng để lập trình là chương trình gì và có ứng dụng như nào ảnh hưởng đến tệp nguồn.

Lấy ví dụ đơn giản về mẫu tiếng Trung hoặc Hàn đều sử dụng bộ ký tự khác ký tự cơ bản UTF-8. Trình soạn thảo văn bản có thể đọc và biểu diễn chúng nhưng chương trình biên dịch thì không vì nó không biết tệp nguồn được mã hoá theo định dạng gì.

Vì thế chức năng này sẽ nói cho trình biên dịch biết định dạng của __*(bộ ký tự nguồn)*__ bạn đang sử dụng và chỉ định **_(bộ ký thực thi)_**

## Giai đoạn 6 (Phase 6)

Các chuỗi ký tự liền kề được nối với nhau.

## Giai đoạn 7 (Phase 7)

Quá trình biên dịch diễn ra: các mã thông báo được phân tích về mặt cú pháp và ngữ nghĩa và được dịch dưới dạng đơn vị dịch thuật.

## Giai đoạn 8 (Phase 8)

Liên kết diễn ra: Các đơn vị dịch và các thành phần thư viện cần thiết để đáp ứng các tham chiếu bên ngoài được thu thập thành hình ảnh chương trình chứa thông tin cần thiết để thực thi trong môi trường thực thi của nó (HĐH).