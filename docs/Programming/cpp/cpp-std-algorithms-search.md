# \[C++\] Algorithms Search

## Min Max

- Thuật toán xác định giá trị lớn nhất / nhỏ nhất giữa hai hoặc nhiều phần tử.
- `std::min` và `std::max` nhận đầu vào là một cặp hoặc chuỗi số và trả về giá trị lớn nhất trong mảng.
- Cả hai hàm `std::min` và `std::max` thực sự có cấu trúc giống nhau,chỉ khác ở kết quả là __*lớn nhất / nhỏ nhất*__. Thế nên không có ví dụ cho trường hợp lớn nhất.

### Sử Dụng

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

## std::find