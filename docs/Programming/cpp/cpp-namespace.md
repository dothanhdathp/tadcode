# \[C++\] Namespace

__namespace__ chia cách các chức năng code, hàm,... hay nói đơn giản là nó sẽ phân vùng các chức năng có trong ngôn ngữ thành các thành phần khác nhau.

Muốn truy cập vào một phân vùng chứa `namespace` có hai cách.
1. Khai báo nó
1. Sử dụng trực tiếp với `NAMESPACE::NAME`

## Namespace STD

`std` là một namespace cơ bản nhất. Và khá là quen mắt trong các dự án __C++__ với dòng:

```c++
using namespace std;
```

Dòng đó có nghĩa là nó cho phép code của bạn được quyền truy cập vào tất cả các hàm chứ năng có trong thư viện cơ bản [Standard Library](cpp-std-standard-library.md). Các thư viện cơ bản là một trong những thành phần không thể thiếu của bất kỳ ngôn ngữ nào và là phần chính yếu góp phần đưa giá trị của một ngôn ngữ lên.

Việc khai báo như trên sẽ giúp mã nguồn tự động truy cập vào thư viện cơ bản khi các hàm đã được khai báo có trong __*namespace*__ của __C++__.