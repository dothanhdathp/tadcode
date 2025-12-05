# \[C++\] Container

Các __Container__ đại diện cho các thùng chứa, hay dễ hiểu hơn chính là tập hợp của các loại __dữ liệu (biến)__ theo một kiến trúc được đặt tên.

Dưới đây là một số dạng thức của _container_

## Các dạng _container_ cơ bản

Một khái niệm về _container_ phổ biến trong các ngôn ngữ lập trình gồm:

- __Sequence Container__: Là các dạng danh sách có thứ tự, một số đại diện phổ biến là
    - [Array (Chuỗi)](cpp-array.md): danh sách __tĩnh__. Không có khả năng mở rộng
    - [Vector](cpp-vector.md): Danh sách như Array nhưng cho phép mở rộng ở hai đầu
    - [Vector](cpp-vector.md): Danh sách như Array nhưng cho phép mở rộng ở hai đầu
- __Associative Containers__:
    - [Map](cpp-map.md)
    - [Unordered Map‼](cpp-unordered-map.md)
- Một số kiểu khác:
    - [Set](cpp-set.md)
    - [Unordered Set](cpp-unordered-set.md)

- __Vector__ cũng là chuỗi, nhưng nó cho phép thêm phần tử, tự do mở rộng
- Chuỗi là một danh sách __tĩnh__. Tức không thể thêm được phần tử.

Một số dạng container cần thoả mãn một số yêu cầu thiết kế trong [Named Requirements](cpp-named-requirements.md#container)

## 