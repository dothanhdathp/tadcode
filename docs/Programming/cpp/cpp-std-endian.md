# \[C++\] std::endian

Công cụ này sử dụng để kiểm tra endian hệ thống đang sử dụng.

Tham khảo endian tại bài [Endianness](http://localhost:65001/OS/os-endianness/)

```c++
#include <iostream>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

int main() {
    println("std::endian::native : ", static_cast<size_t>(std::endian::native));
    println("std::endian::little : ", static_cast<size_t>(std::endian::little));
    println("std::endian::big    : ", static_cast<size_t>(std::endian::big));

    if constexpr (std::endian::native == std::endian::little) {
        println("This system is little-endian.");
    } else if constexpr (std::endian::native == std::endian::big) {
        println("This system is big-endian.");
    } else {
        println("This a mixed endian system.");
    }
}
```
```text
std::endian::native : 1234
std::endian::little : 1234
std::endian::big    : 4321
This system is little-endian.
```