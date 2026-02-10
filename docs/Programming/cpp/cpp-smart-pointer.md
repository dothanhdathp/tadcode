# \[Cpp\] Smart Pointer

> [Smart Pointers in Geeksforgeeks](https://www.geeksforgeeks.org/cpp/smart-pointers-cpp/)

__Smart Pointer__ là một tập hợp, bộ các lớp đóng gói được sử dụng thay cho con trỏ truyền thồng __*(Raw Poniter)*__ nhằm đảm bảo hạn chế các vấn đề liên quan đến lỗi phần mềm gây lãng phí tài nguyên máy tính.

Các __Smart Pointer__ dần trở nên tiêu chuẩn và khá là phổ biến trong C++ và được khuyến nghị sử dụng trong những chương trình muốn tối ưu về chất lượng.

Đồng thời vì chúng được phát triển và đóng gói sẵn trong các công cụ xây dựng nên tốc độ sẽ nhỉnh hơn các hàm quản lý, hàm gọi thông thường khá nhiều.

## Các Loại Smart Pointer

- [Shared Pointer](cpp-shared-ptr.md)
- [Weak Pointer](cpp-weak-ptr.md)
- [Unique Pointer](cpp-unique-ptr.md)
    - [_Auto Pointer (Deprecated)_](cpp-unique-ptr.md#auto-pointer-deprecated)

<!-- - [Shared Pointer](https://en.cppreference.com/w/cpp/memory/shared_ptr.html) -->
<!-- - [Weak Pointer](https://en.cppreference.com/w/cpp/memory/weak_ptr.html) -->
<!-- - [Unique Pointer](https://en.cppreference.com/w/cpp/memory/unique_ptr.html) -->