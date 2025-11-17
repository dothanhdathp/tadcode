# \[C++\] String Init

## Yêu Cầu

- Yêu cầu khai báo [namespace](cpp-namespace.md) của [thư viện std](cpp-std-standard-library.md).

## Định Nghĩa

=== "C98"
    |         Khái niệm | Khai Báo                                                                             |                                     Khái niệm |
    | ----------------: | :----------------------------------------------------------------------------------- | --------------------------------------------: |
    |       default (1) | `string();`                                                                          |   [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi) |
    |          copy (2) | `string (const string& str);`                                                        |   [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi) |
    |     substring (3) | `string (const string& str, size_t pos, size_t len = npos);`                         |                       [Cắt Chuỗi](#cat-chuoi) |
    | from c-string (4) | `string (const char* s);`                                                            |   [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi) |
    | from sequence (5) | `string (const char* s, size_t n);`                                                  |                       [Cắt Chuỗi](#cat-chuoi) |
    |          fill (6) | `string (size_t n, char c);`                                                         | [Khởi Tạo Chuỗi Ký Tự](#khoi-tao-chuoi-ky-tu) |
    |         range (7) | `template <class InputIterator>  string  (InputIterator first, InputIterator last);` |                    [Khởi Tạo Từ Thùng Chứa]() |
=== "C++11"
    |            Khái niệm | Khai Báo                                                                             | Khái niệm                                     |
    | -------------------: | :----------------------------------------------------------------------------------- | :-------------------------------------------- |
    |          default (1) | `string();`                                                                          | [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi)   |
    |             copy (2) | `string (const string& str);`                                                        | [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi)   |
    |        substring (3) | `string (const string& str, size_t pos, size_t len = npos);`                         | [Cắt Chuỗi](#cat-chuoi)                       |
    |    from c-string (4) | `string (const char* s);`                                                            | [Khởi tạo bằng chuỗi](#khoi-tao-bang-chuoi)   |
    |      from buffer (5) | `string (const char* s, size_t n);`                                                  | [Cắt Chuỗi](#cat-chuoi)                       |
    |             fill (6) | `string (size_t n, char c);`                                                         | [Khởi Tạo Chuỗi Ký Tự](#khoi-tao-chuoi-ky-tu) |
    |            range (7) | `template <class InputIterator>  string  (InputIterator first, InputIterator last);` | [Khởi Tạo Từ Thùng Chứa]()                    |
    | initializer list (8) | `string (initializer_list<char> il);`                                                | [Khởi Tạo Từ Thùng Chứa]()                    |
    |             move (9) | `string (string&& str) noexcept;`                                                    | ???                                           |

## Khởi Tạo (Construct)

### Khởi Tạo Bằng Chuỗi

```cpp
#include <iostream>

int main() {
    std::string a = "Hello World"; // From org string
    std::string b("Hello World");  // From org string
    std::string c = a; // From another string
    std::string d(a);  // From another string
    const char* temp = "Hello World";
    std::string e = temp; // From const char
    std::string f(temp);  // From const char
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << c << std::endl;
    std::cout << d << std::endl;
    std::cout << e << std::endl;
    std::cout << f << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
```

### Khởi Tạo Chuỗi Ký Tự

Cách dưới đây khởi tạo một chuỗi với `10` ký tự `a`

```cpp
#include <iostream>

int main() {
    std::string a (10, 'a');      // Từ ký tự
    std::string b (10, 97);       // Từ mã ASCII
    // std::string c (10, 15321); // Lỗi vì quá ngưỡng mã ASCII
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    return 0;
}
```
```text title="Kết Quả"
aaaaaaaaaa
aaaaaaaaaa
```

### Cắt chuỗi

Hàm khởi tạo cũng có thể cắt chuỗi.

```cpp
#include <iostream>

int main() {
    std::string a(10, 'a');
    std::string b(a, 5); // Lấy 5 ký tự từ chuỗi a
    std::string c("aaaaaaaaaa", 5); // Lấy 5 ký tự từ chuỗi gốc
    std::string d("abcdefgh", 3, 3); // Lấy 5 ký tự từ chuỗi gốc
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << c << std::endl;
    std::cout << d << std::endl;
    return 0;
}
```
```text title="Kết Quả"
aaaaaaaaaa
aaaaa
aaaaa
def
```

### Khởi Tạo Từ Thùng Chứa

Chuỗi từ thư viện `std::string` cũng có thể khởi tạo từ các thùng chứa như [Array](), [List](), [Vector](), [Initializer List](cpp-initializer-list.md), ... miễn là chúng có cấu trúc của 


```cpp
#include <iostream>
#include <vector>
#include <list>
#include <initializer_list>

int main() {
    std::vector v = { 'H','e','l','l','o',' ','W','o','r','l','d'};
    std::list l = { 'H','e','l','l','o',' ','W','o','r','l','d'};
    std::initializer_list il = { 'H','e','l','l','o',' ','W','o','r','l','d'};
    std::string str_v(v.begin(), v.end());
    std::string str_l(l.begin(), l.end());
    std::string str_il(il.begin(), il.end());
    std::cout << str_v << std::endl;
    std::cout << str_l << std::endl;
    std::cout << str_il << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Hello World
Hello World
Hello World
```

## Tham khảo

- [cplusplus - string](https://cplusplus.com/reference/string/string/)