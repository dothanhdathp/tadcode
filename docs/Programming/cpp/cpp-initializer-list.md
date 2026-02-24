# Initializer List

## Mục Đích

Một đối tượng thuộc kiểu `std::initializer_list<T>` là một đối tượng proxy nhẹ cung cấp quyền truy cập vào một mảng các đối tượng thuộc kiểu const T (có thể được cấp phát trong bộ nhớ chỉ đọc).

Mục đích của lớp này khá là củ chuối. Nó chỉ đơn giản là khởi tạo một chuỗi __*tĩnh*__ và là một chuỗi __*nhẹ*__. Mục đích chính của nó chỉ đơn giản là:

- Mục đích chính cho __khởi tạo__ một hệ cơ sở dữ liệu. Với:
    - Mục đích chỉ đọc - các phần tử trong mảng này là hằng số (_**const**, không thể thay đổi_)
    - Và cuối cùng nó vẫn là một thành phần của thư viện chuẩn nên kế thừa các tính chất của cơ sở dữ liệu chung.
- Vì để khởi tạo nên nó <u>nhẹ hơn __std::vector__</u>

## Khởi Tạo

```cpp
#include <iostream>
#include <initializer_list>

int main() {
    std::initializer_list<int> init_list = { 1,2,3,4,5,6,7,8,9 };
    for (auto it = init_list.begin(); it != init_list.end(); ++it) {
        std::cout << *it << std::endl;
    }
    return 0;
}
```

## Functions (Chức Năng)

Trong phần này chỉ nói đơn giản và ngắn gọn. Để sử dụng vui lòng đọc trong các tài liệu chuẩn.

### Member functions

Vì là một hàm nhẹ nên nó chỉ có ba chức năng

|           |                                                        |
| :-------- | :----------------------------------------------------- |
| `begin()` | _Trả về con trỏ trỏ đến phần tử đầu tiên_              |
| `end()`   | _Trả về con trỏ trỏ đến vị trí sau phần tử cuối cùng._ |
| `size()`  | _Trả về kích thước mảng_                               |

### Non-member functions

Hai chức năng chính không thuộc lớp chỉ có

|                                  |                                                                      |
| :------------------------------- | :------------------------------------------------------------------- |
| `std::data(<initializer_list>)`  | _Trả về con trỏ trỏ đến địa chỉ đầu tiên của bộ nhớ tĩnh trong mảng_ |
| `std::empty(<initializer_list>)` | _Kiểm tra xem danh sách có rỗng hoặc không_                          |

## Tham Khảo

1. [https://en.cppreference.com/w/cpp/utility/initializer_list.html](https://en.cppreference.com/w/cpp/utility/initializer_list.html)