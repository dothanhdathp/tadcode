# \[C++\] STD Algorithms

## About

Thư viện __Algorithms__ sử dụng

```cpp
#include <algorithm>
```

## std::min / std::max

### Sử Dụng

Thuật toán xác định giá trị lớn nhất / nhỏ nhất giữa hai hoặc nhiều phần tử. Cả hai hàm `std::min` và `std::max` thực sự có cấu trúc giống nhau,chỉ khác ở kết quả là __*lớn nhất / nhỏ nhất*__. Thế nên không có ví dụ cho trường hợp lớn nhất.

=== "2 Phần Tử"
    ```cpp
    int a = 2;
    int b = 2;
    std::cout << std::min(a, b) << std::endl;
    ```
    ```text title="Kết Quả"
    1
    ```
=== "Nhiều Phần Tử"
    ```cpp
    std::cout << std::min({2,1,3,7,8,9}) << std::endl;
    ```
    ```text title="Kết Quả"
    1
    ```
=== "Với std::initializer_list"
    ```cpp
    const std::initializer_list<int> l = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
    std::cout << std::min(l) << std::endl;
    ```
    ```text title="Kết Quả"
    0
    ```

### Tự Định Nghĩa

Bạn cũng có thể tái định nghĩa lại thuật so sánh để thay đổi kết quả trả về hoặc sử dụng với các chuỗi có cấu trúc dạng đặc biệt kiểu `std::string`. Dưới đây là ví dụ cho trường hợp so sánh các số nguyên nhưng thay đổi hàm so sánh để `std::min` trả lại kết quả lớn nhất:

```cpp title="Ví Dụ"
const std::initializer_list<int> l = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
std::cout << std::min(l, [](int a, int b){
    return a > b;
}) << std::endl;
```
```text title="Kết Quả"
6
```

## std::sort

### Mặc Định

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

### GREATER, LESS

Chắc chắn có nhỏ hơn thì có lớn hơn. Trường hợp muốn sắp xếp có chiều thì có thể dùng các cờ như `std::greater`, `std::less` để chuyển đổi thuật toán sắp xếp:

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

### Tự Định Nghĩa

Hàm sort cũng cho phép người dùng tự định nghĩa lại về phương thức só sánh bàng [Lambd Function]().

```cpp
std::vector<int> vec = { 3, 1, 6, 5, 4, 6, 4, 3, 0, 1, 5, 4 };
std::sort(vec.begin(), vec.end(), [](int a, int b){ return a > b; });
```
```text title="Kết Quả" 
6 6 5 5 4 4 4 3 3 1 1 0 
```

## std::find

## std::copy