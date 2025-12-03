# \[Cpp\] Smart Pointer

!!! abstract "Abstract"
    - [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr.html)
    - [shared_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr.html)
    - [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr.html)

## What is Smart Pointer?



## Shared Pointer

### Mục Đích

`shared_ptr` là một __*Smart Pointer*__ duy trì quyền sở hữu chung của một đối tượng thông qua một con trỏ.

Nhiều `shared_ptr` có thể sở hữu cùng một đối tượng. Đối tượng sẽ bị hủy và bộ nhớ của nó sẽ bị giải phóng khi một trong hai trường hợp sau xảy ra:

- `shared_ptr` cuối cùng sở hữu đối tượng bị phá hủy;
- `shared_ptr` cuối cùng sở hữu đối tượng bị gán cho một con trỏ khác thông qua toán tử `=` hoặc `reset()`.

### Lý Do

lỗi rò rỉ bộ nhớ (memory leaks) và các vấn đề về con trỏ treo ([dangling pointers](/Common/common-dangling-pointers)).

### Các Loại

### 