# Bitset

> Source: [std::bitset](https://en.cppreference.com/w/cpp/utility/bitset.html)

## Định Nghĩa

- Mẫu lớp __bitset__ biểu diễn một chuỗi bit có kích thước cố định $N$.
- Các bitset có thể được thao tác bằng các toán tử _logic_ tiêu chuẩn và được chuyển đổi sang chuỗi hoặc số nguyên.
- Để biểu diễn chuỗi và đặt tên cho các phép dịch chuyển, chuỗi được coi là có các phần tử được lập chỉ mục thấp nhất nằm ở bên phải , như trong biểu diễn nhị phân của số nguyên.

### Kiến trúc

```cpp
template< std::size_t N >
class bitset;
```

## Khởi Tạo

`std::bitset` có thể khởi tạo từ nhiều nguồn khác nhau như:

```cpp
std::bitset<16> b0;         // construct with empty
std::bitset<16> b1(10);     // construct with interger
std::bitset<16> b2(0xA);    // construct with interger hex
std::bitset<16> b3(0b1010); // construct with interger bits
std::bitset<16> b4("1010"); // construct with bits strings
```
```text title="Giá Trị"
0000000000000000
0000000000001010
0000000000001010
0000000000001010
0000000000001010
```

## Function

### Operator

| Operator | Effect                                 |
| :------: | :------------------------------------- |
|   `[]`   | Truy cập vào phần tử theo _index_      |
|   `&=`   | Thực hiện toán tử __AND__ bit và gán   |
|   `|=`   | Thực hiện toán tử __OR__ bit và gán    |
|   `^=`   | Thực hiện toán tử __XOR__ bit và gán   |
|   `~=`   | Thực hiện toán tử __NOT__ bit và gán   |
|  `<<=`   | Thực hiện toán tử __dịch trái__ và gán |
|  `>>=`   | Thực hiện toán tử __dịch phải__ và gán |
|   `<<`   | Thực hiện toán tử __dịch trái__        |
|   `>>`   | Thực hiện toán tử __dịch phải__        |

### Member Operator

| Function Name                                                |       Return       | Desciption                                                                                                        | Throw                 |
| :----------------------------------------------------------- | :----------------: | :---------------------------------------------------------------------------------------------------------------- | :-------------------- |
| **all**()                                                    |      **bool**      | Kiểm tra nếu __*tất cả các bit*__ được set thành __True__                                                         |                       |
| **any**()                                                    |      **bool**      | Kiểm tra nếu __*có ít nhất một bit*__ được set thành __True__                                                     |                       |
| **none**()                                                   |      **bool**      | Kiểm tra nếu __*không có bit nào*__ được set thành __True__                                                       |                       |
| **test**(_std::size_t pos_) **const**;                       |      **bool**      | Trả về giá trị bit tại vị trí _pos_.                                                                              | **std::out_of_range** |
| **set**(_std::size_t pos_, _**bool**_ _value_ = **true**)    |  **std::bitset&**  | Đặt giá trị của một bit tại vị trí __*pos*__ thành giá trị `1`.                                                   |                       |
| **reset**( _std::size_t pos_, _**bool**_ _value_ = **true**) |  **std::bitset&**  | Đặt giá trị của một bit tại vị trí __*pos*__ thành giá trị `0`.                                                   |                       |
| **flip**( _std::size_t pos_ )                                |  **std::bitset&**  | Chuyển đổi, lật giá trị của bit tại vị trí __*pos*__/tất cả thành giá trị đối lập. _(`0` thành `1` và ngược lại)_ |                       |
| **to_string**()                                              |    std::string     |                                                                                                                   |                       |
| **to_ulong**()                                               |   unsigned long    |                                                                                                                   |                       |
| **to_ullong**()                                              | unsigned long long |                                                                                                                   |                       |

### Non-Member Operator

| Operator | Effect |
| :------: | :----- |
|   `&`    |        |
|   `|`    |        |
|   `^`    |        |
|   `<<`   |        |
|   `>>`   |        |
 
## Convert

`std::bitset` hỗ trợ ba kiểu chuyển đổi dữ liệu:

- `to_string()` : Chuyển đổi sang chuỗi __*string*__
- `to_ulong()` : Chuyển đổi sang dạng __*long int*__
- `to_string()` : Chuyển đổi sang chuỗi __*string*__

## hash

`std::bitset` cũng có thể được dùng với __*hash*__, ví dụ `std::hash<std::bitset<N>>`