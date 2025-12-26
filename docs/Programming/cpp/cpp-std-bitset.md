# \[C++\] Bitset

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

## Operator

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

## Function

- `bool all()` : Kiểm tra nếu __*tất cả các bit*__ được set thành __True__
- `bool any()` : Kiểm tra nếu __*có ít nhất một bit*__ được set thành __True__
- `bool none()` : Kiểm tra nếu __*không có bit nào*__ được set thành __True__
- `bool test( std::size_t pos ) const;`: Trả về giá trị bit tại vị trí _pos_.
    - Hàm này khác `[]` là có  thực hiện hành vi <u>kiểm tra giới hạn</u>.
    - Khi vượt quá giới hạn hàm này sẽ văng ra __*throw*__ `std::out_of_range`
- `bitset& set( std::size_t pos, bool value = true);`: Đặt giá trị của một bit tại vị trí __*pos*__ thành giá trị `1`.
    - Hàm này trả về địa chỉ của __*bitset*__ được dùng
    - Nếu dùng độc lập _(không đưa vào tham số pos)_, hàm này sẽ đặt lại tất cả giá trị của __*bitset*__ thành `1`
    - Khi vượt quá giới hạn hàm này sẽ văng ra __*throw*__ `std::out_of_range`
- `bitset& reset( std::size_t pos, bool value = true);`: Đặt giá trị của một bit tại vị trí __*pos*__ thành giá trị `0`.
    - Hàm này trả về địa chỉ của __*bitset*__ được dùng
    - Nếu dùng độc lập _(không đưa vào tham số pos)_, hàm này sẽ đặt lại tất cả giá trị của __*bitset*__ thành `0`
    - Khi vượt quá giới hạn hàm này sẽ văng ra __*throw*__ `std::out_of_range`
- `bitset& flip( std::size_t pos);`: Chuyển đổi giá trị của bit tại vị trí __*pos*__ thành giá trị đối lập. _(`0` thành `1` và ngược lại)_
    - Hàm này trả về địa chỉ của __*bitset*__ được dùng
    - Nếu dùng độc lập _(không đưa vào tham số pos)_, hàm này đảo bit tất cả các bit có trong __*bitset*__
    - Khi vượt quá giới hạn hàm này sẽ văng ra __*throw*__ `std::out_of_range`

## Convert

`std::bitset` hỗ trợ ba kiểu chuyển đổi dữ liệu:

- `to_string()` : Chuyển đổi sang chuỗi __*string*__
- `to_ulong()` : Chuyển đổi sang dạng __*long int*__
- `to_string()` : Chuyển đổi sang chuỗi __*string*__

## hash

`std::bitset` cũng có thể được dùng với __*hash*__, ví dụ `std::hash<std::bitset<N>>`