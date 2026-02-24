# STD Pair

- Pair tạo ra một cặp các giá trị được liên kết với nhau (khá là giống với dạng __*struct*__). Chỉ khác là vì nó được định nghĩa chung trong thư viện chuẩn nên các thao tác với con trỏ dạng __*interator*__ có thể được kế thừa sử dụng.
- Muốn sử dụng `std::pair`, cần sử dụng thư viện `<utility>`
- `std::pair` cũng tương tác được với các lớp thư viện khác như `std::vector` hay `std::list`

## Construct

Cách để tạo một biến `std::pair` theo ba cách như này

```cpp title="Khai Báo"
std::pair<int, float> p0(1, 1.11);                  // Cách 1
std::pair<int, float> p1 = {1, 1.11};               // Cách 2
std::pair<int, float> p2 = std::make_pair(1, 1.11); // Cách 3
```
```text title="Kết Quả"
First  : 1
Second : 1.11
```

## Truy Vấn

Trong phương pháp truy vấn, có thể dùng khá là nhiều cách

- Dùng `first` và `second`
- Dùng `std::get` và `std::get` với
    - `<0>` và `<1>` để truy vấn vào vị trí
    - `<type_t>` và `<type_t>` để truy vấn dựa vào loại biến.

```cpp
#include <iostream>
#include <algorithm>
#include <utility>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

int main(int argc, const char* args[]) {
    std::pair<int, float> p = std::make_pair(1, 1.11);

    println(p.first,          ", ", p.second);
    println(std::get<0>(p),   ", ", std::get<1>(p));
    println(std::get<int>(p), ", ", std::get<float>(p));
    return 0;
}
```
```text title="Kết Quả"
1, 1.11
1, 1.11
1, 1.11
```

## Swap (Trao Đổi)

`std::pair` tương tác với cả _swap_

```cpp
#include <iostream>
#include <algorithm>
#include <utility>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

int main(int argc, const char* args[]) {
    std::pair<int, float> p1 = {1, 2.34};
    std::pair<int, float> p2 = {2, 4.78};

    println("p1<", p1.first, ',', p1.second, "> ; p2<", p2.first, ',', p2.second, '>');

    // swap 1 <--->
    std::swap(p1, p2);
    println("p1<", p1.first, ',', p1.second, "> ; p2<", p2.first, ',', p2.second, '>');

    // swap 2 <--->
    p1.swap(p2);
    println("p1<", p1.first, ',', p1.second, "> ; p2<", p2.first, ',', p2.second, '>');

    return 0;
}
```
```text
p1<1,2.34> ; p2<2,4.78>
p1<2,4.78> ; p2<1,2.34>
p1<1,2.34> ; p2<2,4.78>
```