# \[C++\] Bitset

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