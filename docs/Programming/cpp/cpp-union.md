# \[C++\] Union

## Định nghĩa

- __union__ là định nghĩa dữ liệu đặc biệt, nó có nghĩa là nhiều kiểu dữ liệu khác nhau trên cùng một địa chỉ bộ nhớ.
- Kích thước của union phụ thuộc vào kiểu dữ liệu lớn nhất mà nó chứa.
- Nói dễ hiểu hơn, các phần tử của __*union*__ chỉ là các cách biểu diễn của nó cho cùng một giá trị, giống như __type_cast__
- Nếu các phần tử khác kích thước, phần tử bé hơn sẽ lấy đúng phần kích thước của mình thôi, phần dư còn lại không sử dụng. Lấy phần tử nào thì phải xem xét kiến trúc bộ nhớ.
- Thay đổi giá trị một phần tử sẽ thay đổi cách thức biểu diễn của các phần tử khác. Ví dụ nếu phần tử interger = 97 thì khi đọc dưới giá trị char nó tự động là `a`.

Ví dụ

```cpp
#include <iostream>

union un {
    int   as_int;
    float as_float;
    char  as_char;
};

int main() {
    un u;
    std::cout << "size of int : " << sizeof(int) << std::endl;
    std::cout << "size of float : " << sizeof(float) << std::endl;
    std::cout << "size of char : " << sizeof(char) << std::endl;
    std::cout << "size of un : " << sizeof(un) << std::endl;
    std::cout << "as_int   : " << u.as_int << std::endl;
    std::cout << "as_float : " << u.as_float << std::endl;
    std::cout << "as_char  : " << u.as_char << std::endl;
    return 0;
}
```
```text title="Kết Quả"
size of int : 4
size of float : 4
size of char : 1
size of un : 4
as_int   : 0
as_float : 0
as_char  : 
```

### Phần tử nhỏ hơn.

## Construct/Destruct

Giống struct, union cũng có thể tạo các hàm khai báo và hủy. Chỉ có điều cần đặc biệt ghi nhớ, là xóa 1 phần tử vì các phần tử chia sẻ chung bộ nhớ.

```cpp
#include <iostream>

union un {
    int   as_int;
    float as_float;
    char  as_char;

    un(int v) { as_int = v; }
    un(float v) { as_float = v; }
    un(char v) { as_char = v; }
    ~un() {};
};

int main() {
    un u(97);
    std::cout << "as_float : " << u.as_float << std::endl;
    std::cout << "as_char  : " << u.as_char << std::endl;
    return 0;
}
```
```text title="Kết Quả"
as_float : 1.35926e-43
as_char  : a
```

## Ứng Dụng

Ứng dụng thực tế và nhiều nhất của __union__ chính là trong các giao thức trao đổi dữ liệu. Ví dụ bên A muốn gửi đi một bản tin có "cấu trúc" thì bên B khi nhận về sẽ chuyển đổi ngược về "cấu trúc" để đọc. Cách này vừa tận dụng được __*bit-field*__ của __struct__, vừa tiêu chuẩn hóa được quy trình.

Cách sử dụng rất đơn giản, đó là đóng gói [struct](cpp-struct.md) bên trong một __union__. Lúc này toàn bộ dữ liệu của __struct__ sẽ được đọc ra giống như dữ liệu của phần tử còn lại của __union__. Ví dụ

```cpp
#include <iostream>

struct struct_hs {
    int Level : 4;
    int Class : 4;
    int Index : 16;
};

union union_hs {
    int as_int;
    struct_hs hs;
};

int wrap(int l, int c, int i) {
    struct_hs hs;
    hs.Level = l;
    hs.Class = c;
    hs.Index = i;
    union_hs uhs;
    uhs.hs = hs;
    return uhs.as_int;
}

void unwrap(int value) {
    union_hs u;
    u.as_int = value;
    std::cout << "Level = " << u.hs.Level << std::endl;
    std::cout << "Class = " << u.hs.Class << std::endl;
    std::cout << "Index = " << u.hs.Index << std::endl;
}

int main() {
    int ret = wrap(1,2,3);
    unwrap(ret);
    return 0;
}
```
```text title="Kết Quả"
Level = 1
Class = 2
Index = 3
```