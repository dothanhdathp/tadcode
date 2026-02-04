# \[C++\] Sort

- `std::sort` sắp xếp lại cấu trúc dữ liệu theo thứ tự.

## Mặc Định

Hàm này để sắp xếp một chuỗi các phần tử theo thứ tự. Dữ liệu đầu vào cần phải thuộc kiến trúc [STD Container](cpp-std-container.md) và đồng thời chúng cần phải thuộc dạng cấu trúc có thể sắp xếp.

Thường sẽ được sử dụng với `std::array`, `std::vector`, `std::list`. Các cấu trúc dữ liệu bảng chẳng hạn như `std::map`, `std::unordered_map` sẽ không có cơ chế _sắp xếp_ nên không sử dụng được.

Ở chế độ cơ bản, hàm này sẽ luôn sắp xếp từ bé đến lớn:

```cpp title="main.cpp"
#include <iostream>
#include <memory>
#include <algorithm>
#include <vector>

int main() {   
    // Pointer declaration
    std::vector<int> vec = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
    std::sort(vec.begin(), vec.end());
    for (auto i : vec)
        std::cout << i << ' ';
    std::cout << std::endl;

    return 0;
}
```
```text title="Kết Quả"
0 1 1 3 3 4 4 4 5 5 6 6 
```

## std::greater và std::less

- Thêm đối số `std::less<T>()` và `std::greater<T>()` vào đối số thứ ba sẽ thay đổi quy luật sắp xếp của hàm.
    - `std::less<T>()`: Xếp từ _nhỏ đến lớn_
    - `std::greater<T>()`: Xếp từ _lớn đến nhỏ_
- Mặc định theo cấu trúc sẽ chọn sắp xếp từ nhỏ đến lớn. Nên về cơ bản chỉ cần nhớ đến `std::greater`. Nếu muốn sắp xếp ngược lại trên các cơ sở dữ liệu chuẩn chung.

```cpp title="main.cpp"
#include <iostream>
#include <memory>
#include <algorithm>
#include <vector>

int main() {   
    // Pointer declaration
    std::vector<int> vec = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
    std::sort(vec.begin(), vec.end(), std::greater<int>());
    for (auto i : vec)
        std::cout << i << ' ';
    std::cout << std::endl;
    std::sort(vec.begin(), vec.end(), std::less<int>());
    for (auto i : vec)
        std::cout << i << ' ';
    std::cout << std::endl;

    return 0;
}
```
```text title="Kết Quả" 
6 6 5 5 4 4 4 3 3 1 1 0 
0 1 1 3 3 4 4 4 5 5 6 6
```

Còn nhiều cờ khác có thể sử dụng như là  `std::greater_equal`, `std::less_equal`, ... nhưng gần như chả ai dùng.

## Tự Định Nghĩa

Hàm sort cũng cho phép người dùng tự định nghĩa lại về phương thức so  sánh bàng [Lambd Function]().

```cpp
std::vector<int> vec = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
std::sort(vec.begin(), vec.end(), [](int a, int b){ return a > b; });
```
```text title="Kết Quả" 
6 6 5 5 4 4 4 3 3 1 1 0 
```