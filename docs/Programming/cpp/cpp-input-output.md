# Input/Output

> Theo [iolibrary](https://cplusplus.com/reference/iolibrary/)

## Thư viện đầu vào/đầu ra

__iostream library__ là một thư viện hướng đối tượng cung cấp chức năng đầu vào và đầu ra bằng cách sử dụng các luồng.

<figure markdown="span">
    ![](img/input-output.gif)
    <figcaption></figcaption>
</figure>

`stream` là một sự trừu tượng hóa đại diện cho một thiết bị mà trên đó các hoạt động đầu vào và đầu ra được thực hiện. Về cơ bản, một `luồng` có thể được biểu diễn dưới dạng nguồn hoặc đích của các ký tự có độ dài không xác định.

Các luồng thường được liên kết với nguồn hoặc đích vật lý của các ký tự, như tệp đĩa, bàn phím hoặc bảng điều khiển, do đó, các ký tự được nhận hoặc ghi vào/từ phần trừu tượng của chúng tôi được gọi là `stream` là đầu vào/đầu ra vật lý cho thiết bị vật lý. Ví dụ: luồng tệp là đối tượng C++ để thao tác và tương tác với tệp; Khi một tệp `stream` được sử dụng để mở một tệp, mọi thao tác đầu vào hoặc đầu ra được thực hiện trên `luồng` đó đều được phản ánh vật lý trong tệp.

Để hoạt động với các luồng, C++ cung cấp thư viện __*iostream*__ tiêu chuẩn, chứa các phần tử sau:

- __Basic class templates__
    - Cơ sở của thư viện __*iostream*__ là hệ thống phân cấp của các mẫu lớp. Các mẫu lớp cung cấp hầu hết các chức năng của thư viện theo kiểu độc lập với kiểu.
    - Đây là một tập hợp các mẫu lớp, mỗi mẫu có hai tham số mẫu: tham số loại `char(charT)`, xác định loại phần tử sẽ được thao tác và tham số đặc điểm, cung cấp các đặc điểm bổ sung cụ thể cho một loại phần tử cụ thể.
    - Các mẫu lớp trong hệ thống phân cấp lớp này có cùng tên với các phiên bản kiểu `char` của chúng nhưng có tiền tố `basic_`. Ví dụ: mẫu lớp mà __*istream*__ được khởi tạo từ đó được gọi là `basic_istream`, mẫu lớp mà từ đó __*fstream*__ được gọi là `basic_fstream`, v.v... Ngoại lệ duy nhất là __ios_base__, bản thân nó không phụ thuộc vào loại và do đó không dựa trên một mẫu mà là một lớp thông thường.
- __Class template instantiations__
    - Thư viện kết hợp hai bộ phiên bản tiêu chuẩn của toàn bộ hệ thống phân cấp mẫu lớp __*iostream*__: một bộ có hướng hẹp để thao tác các phần tử kiểu `char` và một bộ khác có hướng rộng để thao tác các phần tử kiểu `wchar_t`.
    - Việc khởi tạo theo định hướng hẹp (kiểu `char`) có lẽ là phần được biết đến nhiều hơn của thư viện __*iostream*__. Các lớp như __*ios*__, __*istream*__ và __*ofstream*__ có định hướng hẹp. Sơ đồ ở đầu trang này hiển thị tên và mối quan hệ của các lớp có định hướng hẹp.
    - Các lớp của quá trình khởi tạo định hướng rộng (`wchar_t`) tuân theo các quy ước đặt tên giống như khởi tạo định hướng hẹp nhưng với tên của mỗi lớp và đối tượng có tiền tố là ký tự `w`, tạo thành __*wios*__, __*wistream*__ và __*wofstream*__, làm ví dụ.
- __Standard objects__
    - Là một phần của thư viện __*iostream*__, tệp tiêu đề `<iostream>` khai báo một số đối tượng nhất định được sử dụng để thực hiện các thao tác đầu vào và đầu ra trên đầu vào và đầu ra tiêu chuẩn.
    - Chúng được chia thành hai bộ: các đối tượng có định hướng hẹp, là các đối tượng phổ biến là `cin`, `cout`, `cerr` và `clog` và các đối tượng có định hướng rộng, được khai báo là `wcin`, `wcout`, `wcerr` và `wclog`.
- __Types__
    - Các lớp __*iostream*__ hầu như không sử dụng các kiểu cơ bản trên nguyên mẫu của thành viên. Họ thường sử dụng các loại được xác định phụ thuộc vào các đặc điểm được sử dụng trong quá trình khởi tạo của chúng. Đối với các phiên bản char và wchar_t mặc định, các loại luồng, luồng và luồng được sử dụng để thể hiện vị trí, độ lệch và kích thước tương ứng.y.
- __Manipulators__
    - Trình thao tác là các hàm toàn cục được thiết kế để sử dụng cùng với các toán tử chèn (`<<`) và trích xuất (`>>`) được thực hiện trên các đối tượng `stream` __*iostream*__. Họ thường sửa đổi các thuộc tính và cài đặt định dạng của luồng. `endl`, `hex` và `scientific` là một số ví dụ về _manipulators_.

## Tổ chức

Thư viện và hệ thống phân cấp các lớp của nó được chia thành nhiều tập tin khác nhau:

- Các thẻ `<ios>` , `<istream>` , `<ostream>` , `<streambuf> ` và `<iosfwd>` thường không được đưa trực tiếp vào hầu hết các chương trình C++. Chúng mô tả các lớp cơ sở của hệ thống phân cấp và được tự động đưa vào bởi các tệp tiêu đề khác của thư viện chứa các lớp dẫn xuất.
- `<iostream>` khai báo các đối tượng được sử dụng để giao tiếp thông qua đầu vào và đầu ra chuẩn (bao gồm cin và cout ).
- `<fstream>` định nghĩa các lớp luồng tệp (như mẫu basic_ifstream hoặc lớp ofstream ) cũng như các đối tượng bộ đệm nội bộ được sử dụng với chúng (__*basic_filebuf*__). Các lớp này được sử dụng để thao tác với các tệp bằng cách sử dụng luồng.
- `<sstream>` : Các lớp được định nghĩa trong tệp này được sử dụng để thao tác với các đối tượng chuỗi như thể chúng là các luồng.
- `<iomanip>` khai báo một số bộ điều khiển tiêu chuẩn với các tham số được sử dụng với các toán tử trích xuất và chèn để sửa đổi các cờ nội bộ và các tùy chọn định dạng.

