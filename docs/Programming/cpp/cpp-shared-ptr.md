# Shared Pointer

> [Shared Pointer](https://en.cppreference.com/w/cpp/memory/shared_ptr.html)

## Shared Pointer

- `shared_ptr` là một con trỏ thông minh tạo ra với mục đích <u>chia sẻ quyền sở hữu quyền sử dụng một đối tượng</u> và <u>đảm bảo an toàn cho khả năng chia sẻ quyền sở hữu của đối tượng</u> đến các đối tượng khác.
- `shared_ptr` vẫn quản lý các đối tượng thông qua con trỏ.
- <mark>`shared_ptr` khả dụng từ __C++11__</mark>

## Cơ Chế

- Mỗi khi có một đối tượng mới tham gia truy cập vào đối tượng chia sẻ, lớp này sẽ trả ra một con trỏ mới cho đối tượng đó sử dụng.
- Con trỏ đó sẽ được lưu lại kèm đối tượng trong suốt vòng đời của các đối tượng nơi nó được chia sẻ. Con trỏ này sẽ tự động giải phóng khi tất cả các đối tượng sử dụng nó được giải phóng.

!!! note "Note"
    - `shared_ptr` cuối cùng sở hữu đối tượng bị phá hủy.
    - `shared_ptr` cuối cùng sở hữu đối tượng bị gán cho một con trỏ khác thông qua toán tử `=` hoặc `reset()`.

## Phương thức



## Lý Do

lỗi rò rỉ bộ nhớ (memory leaks) và các vấn đề về con trỏ treo ([dangling pointers](../../CS/common-dangling-pointers.md)). Lỗi này hay xảy ra khi hai hoặc nhiều lớp cùng tạo và sở hữu con trỏ để truy cập vào một vùng dữ liệu chung.

- Bởi vì các lớp không có thông tin về nhau nên sau khi kết thúc 

Nhưng sau khi vòng đời của lớp kết thúc, nó không thể biết khi nào để giải phóng vùng nhớ mà con trỏ đang sử dụng. Thế nên 