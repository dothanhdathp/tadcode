# STD Map

- __std::map__ là cấu trúc dữ liệu dạng bản đồ theo cặp __*key-value*__, nghĩa là mỗi phần tử của _std::map_ chính là một phần tử _std::pair_ và được xếp vào thành _std::set_, thế nên:

## Tính chất

- Các phần tử tồn tại theo một cặp _"khóa - giá trị"_
- Các phần tử trong _std::set_ tự động sắp xếp và là duy nhất.
    - Nghĩa là không thể tồn tại hai phần tử có cùng khóa.

## Khởi Tạo


## Truy Cập

Vì được phát triển lên từ [std::pair](cpp-std-pair.md) nên 

```cpp
#include <iostream>
#include <map>
#include <string>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

int main(int argc, const char* args[]) {

    std::map<std::string, int> mmap;
    mmap["Tad"] = 8;
    mmap["Doom"] = 7;
    mmap["Zinasu"] = 10;
    mmap["Ohalo"] = 9;

    for (auto ir = mmap.begin(); ir != mmap.end(); ++ir) {
        println(ir->first, " = ", ir->second);
    }
    return 0;
}
```
```text title="Kết Quả"
Doom = 7
Ohalo = 9
Tad = 8
Zinasu = 10
```

Các __key__ trong `std::map` được sắp xếp mặc định theo thứ tự từ lớn đến nhỏ, cấu trúc mặc định giống `std::set`, nghĩa là nó cũng cấm luôn các giá trị lặp lại.

!!! quote "Quote"
    Các __*key*__ của `std::map` là duy nhất. Trong một `std::map` không thể có hai __*key*__ giống nhau.

```cpp
#include <iostream>
#include <map>
#include <string>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

int main(int argc, const char* args[]) {
    std::map<std::string, int> mmap;
    mmap["Tad"] = 8;
    mmap["Doom"] = 7;
    mmap["Zinasu"] = 10;
    mmap["Ohalo"] = 9;
    mmap["Tad"] = 11;
    mmap["Tad"] = 21;

    for (auto ir = mmap.begin(); ir != mmap.end(); ++ir) {
        println(ir->first, " = ", ir->second);
    }
    return 0;
}
```
```text title="Kết Quả"
Doom = 7
Ohalo = 9
Tad = 21
Zinasu = 10
```

## Khởi Tạo

Các cách khởi tạo một `std::map`

```cpp
// Normally construct, empty map
std::map<int, int> mmap;

// Construt by array
std::map<std::string, int> mmap = {
    {"Chicken", 0},
    {"Rabit",   1},
    {"Cat",     2},
    {"Dog",     3},
    {"Bird",    4}
};

```