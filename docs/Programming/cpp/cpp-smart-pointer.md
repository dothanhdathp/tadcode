# \[Cpp\] Smart Pointer

__Smart Pointer__ là một tập hợp, bộ các lớp đóng gói được sử dụng thay cho con trỏ truyền thồng nhằm đảm bảo hạn chế các vấn đề liên quan đến lỗi phần mềm gây lãng phí tài nguyên máy tính.

Các __Smart Pointer__ dần trở nên tiêu chuẩn và khá là phổ biến trong C++ và được khuyến nghị sử dụng trong những chương trình muốn tối ưu về chất lượng.

Đồng thời vì chúng được phát triển và đóng gói sẵn trong các công cụ xây dựng nên tốc độ sẽ nhỉnh hơn các hàm quản lý, hàm gọi thông thường khá nhiều.

## Shared Pointer

__Shared Pointer__ là một con trỏ thông minh _sở hữu quyền sử dụng một đối tượng_ và _đảm bảo an toàn cho khả năng chia sẻ quyền sở hữu của đối tượng_ đến các đối tượng khác.

`shared_ptr` là một __*Smart Pointer*__ duy trì quyền sở hữu chung của một đối tượng thông qua một con trỏ.

### Tính chất

Nhiều `shared_ptr` có thể sở hữu cùng một đối tượng. Đối tượng sẽ bị hủy và bộ nhớ của nó sẽ bị giải phóng khi một trong hai trường hợp sau xảy ra:

- `shared_ptr` cuối cùng sở hữu đối tượng bị phá hủy;
- `shared_ptr` cuối cùng sở hữu đối tượng bị gán cho một con trỏ khác thông qua toán tử `=` hoặc `reset()`.

### Lý Do

lỗi rò rỉ bộ nhớ (memory leaks) và các vấn đề về con trỏ treo ([dangling pointers](../../CS/common-dangling-pointers.md)). Lỗi này hay xảy ra khi hai hoặc nhiều lớp cùng tạo và sở hữu con trỏ để truy cập vào một vùng dữ liệu chung.

- Bởi vì các lớp không có thông tin về nhau nên sau khi kết thúc 

Nhưng sau khi vòng đời của lớp kết thúc, nó không thể biết khi nào để giải phóng vùng nhớ mà con trỏ đang sử dụng. Thế nên 

### Các Loại

Các loại shared_ointer 

### 

## Tham Khảo

- [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr.html)
- [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr.html)
- [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr.html)