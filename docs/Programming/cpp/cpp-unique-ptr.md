# \[C++\] Unique Pointer

## Unique Pointer

- `unique_ptr` <u>__*chỉ lưu trữ một con trỏ tại một thời điểm.*__</u>. Nghĩa là bạn không thể lấy địa chỉ từ con trỏ này sang một biến con trỏ khác và sử dụng ở cục bộ.
- `unique_ptr` <u>không thể sao chép</u>, chỉ chuyển quyền sở hữu đối tượng sang một `unique_ptr` khác bằng cách sử dụng phương thức `move()`.
- `unique_ptr` đảm bảo việc sử dụng con trỏ an toàn trong quyền sử dụng. Tại một thời điểm chỉ có một đối tượng được trao quyền mới được phép sử dụng. Khi đó, nếu các đối tượng khác truy cập, địa chỉ trả về sẽ là __*con trỏ null*__.

## Auto Pointer (Deprecated)

- `auto_ptr` là một con trỏ thông minh ban đầu tự động xóa đối tượng được quản lý khi nó vượt quá phạm vi.
- `auto_ptr` là tiền thân của `unique_ptr`.
- `auto_ptr` chỉ có thể biên dịch trong __C++14__.

<figure markdown="span">
    ![alt text](./img/auto-ptr.png)
    <figcaption>__auto_ptr__ trong C++</figcaption>
</figure>

```cpp
#include <iostream>
#include <memory>

int main() {
    std::auto_ptr<int> ptr1(new int(10));
    std::cout << *ptr1 << std::endl << std::endl;;

    std::auto_ptr<int> ptr2 = ptr1;  // ownership transfer

    // check ptr1
    if( ptr1.get() != nullptr ) {
        std::cout << *ptr1 << std::endl;
    } else {
        std::cout << "ptr1.get() = nullptr" << std::endl;
    };
    // check ptr2
    if( ptr2.get() != nullptr ) {
        std::cout << *ptr2 << std::endl;
    } else {
        std::cout << "ptr2.get() = nullptr" << std::endl;
    };
    return 0;
}
```
```text title="Kết Quả"
ptr1.get() = nullptr
10
```

!!! note "Note"
    `auto_ptr` không được dùng nữa sau __C++11__ và nó bị xóa sau phiên bản __C++17__. Nói đơn giản chỉ khả dụng trong __C++14_,  __C++17__.

    Sau đó, với sự thay thế của `unique_ptr`, `auto_ptr` đã bị loại bỏ.

    - _Để biết thêm chi tiết về lựa chọn phiên bản, đọc [GNU G++](/Programming/cpp/cpp-gnu-g-plus-plus/)_