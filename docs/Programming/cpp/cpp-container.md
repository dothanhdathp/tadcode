# \[C++\] Thùng Chứa

__*Thùng Chứa*__ hay __*Container*__ là khái niệm chỉ một tập hợp của nhiều dữ liệu nguyên thủy lại với nhau. Nó có thể có/hoặc không có cấu trúc

Các thùng chứa là một phần trong tập khái niệm về __*Cơ Sở Dữ Liệu*__, là kiến trúc cực kỳ quan trọng, những viên gạch cơ bản nhất trong nghành lập trình.

## Phân Loại

- Theo chức năng có hai dạng là _có trật tự_ và _không có trật tự_
- Theo cấu trúc có các dạng như Liner và Non-Liner, ý là dữ liệu được sắp xếp theo một chuỗi liên tục giống như sợi dây. Dạng còn lại không có dạng chuỗi thì có thể là có dạng cây __*(tree)*__ hoặc dạng bản đồ __*(map)*__, ...
- Phân loại theo nhà xuất bản, có dạng thùng chứa là mặc định, một dạng khác là tự tạo và cuối cùng là các thùng chứa trong thư viện cơ bản `std`

## Thùng chứa trong lập trình.

### Thùng Chứa Cổ Điển

Thùng chứa cổ điển hoặc có thể gọi là những cơ sở dữ liệu nguyên bản. Nó đơn giản có nghĩa là __*gom một đống dữ liệu lại*__ và đặt tên là ta đã có thùng chứa. Các thùng chứa cổ điển cơ bản là:

- [array](cpp-array.md)
- [struct](cpp-struct.md)
- [union](cpp-union.md)

### [STD Cotainer](cpp-std-container.md)

Các thùng chứa ở đây là những thùng chứa được hỗ trợ bởi trình biên dịch trong bộ thư viện cơ bản. Nó được xây dựng dựa trên kiến thức về cơ sở dữ liệu và được chuẩn hóa, có tầm phủ sóng rộng rãi trong nhiều lĩnh vực.

### Tự Định Nghĩa

Đây là các loại thùng chứa nâng cao được tự do phát triển tùy theo nhu cầu. Nó có thể phổ biến trong một lĩnh vực nào đó hoặc là được người dùng cảm thấy thú vị và tự tạo ra.

- [Linked List](cpp-linked-list.md)