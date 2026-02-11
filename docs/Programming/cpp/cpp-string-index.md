# String Index

## Iterators

Đây là các con trỏ [Iterators](/Common/iterators) đến các vị trí phần tử nằm trong chuỗi. Chúng gồm

| Tên Hàm     | Tác dụng                     |
| :---------- | :--------------------------- |
| `begin()`   | Con trỏ đến vị trí đầu tiên  |
| `end()`     | Con trỏ đến vị trí cuối cùng |
| `rbegin()`  |                              |
| `rend()`    |                              |
| `cbegin()`  |                              |
| `cend()`    |                              |
| `crbegin()` |                              |
| `crend()`,  |                              |

- __*begin()*__ trả về địa chỉ của ký tự đầu tiên của chuỗi.
- __*end()*__ hàm trả về địa chỉ của ký tự cuối cùng của chuỗi. Ví là chuỗi __*string*__ nên nó sẽ luôn là ký tự __NULL__ (`\0`)

```cpp
#include <iostream>

int main() {
    std::string a("abcdefgh");
    for (auto ir = a.begin(); ir != a.end(); ++ir) {
        std::cout << *ir << std::endl;
    }
    if('\0' == (*a.end())) {
        std::cout << "True" << std::endl;
    } else {
        std::cout << "False" << std::endl;
    }
    return 0;
}
```
```text title="Kết Quả"
a
b
c
d
e
f
g
h
True
```

## Truy cập vị trí

Có hai cách truy cập vị trí vào một `std::string str_example` à dùng `[index]` hoặc hàm `at(index)`. Hai cách đi đến chung kết quả nhưng khác tác dụng.

- `[index]` đối __*string*__ như một chuỗi __*char array*__. Truy cập trực tiếp đến vùng nhớ và đưa ra giá trị.
- `at(index)` cùng tác dụng nhưng an toàn hơn. Nếu _index_ vượt ngưỡi sẽ có __throw__ chương trình xảy ra.