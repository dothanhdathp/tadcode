# \[C++\] JThread

> (since C++20) `std::jthread` được phát triển từ sau __C++20__

## Mô Tả

`std::jthread` giống như luồng cũ nhưng nó theo đúng luật an toàn luồng. Các tính năng sau đã được xác thực:

- Luồng sau khi thoát không cần thiết phải `join()`. Nó trở thành chức năng tự động.
- Luồng khi `detach()` mà kết thúc cũng 


## Thành Viên

### Member types
| Member types       | Definition                      |
| :----------------- | :------------------------------ |
| id                 | std::thread::id                 |
| native_handle_type | std::thread::native_handle_type |
|                    |                                 |

__TEMP__: Một chương trình phụ chạy loading khá là vui mắt.

```cpp
#include <iostream>
#include <thread>
#include <thread>

#define Loading(i) std::cout << "\rLoading: [" << std::string(i, '|') << std::string(100-i, ' ') << "]" << std::flush

int main() {
    for (int i = 0; i <= 100; ++i) {
        std::cout << "\rLoading: [" << std::string(i, '|') << std::string(100-i, ' ') << "]" << "]\033[K\n"
                  << "\rLoading: [" << std::string(i, '|') << std::string(100-i, ' ') << "]" << "]\033[K\n"
                  << "\rLoading: [" << std::string(i, '|') << std::string(100-i, ' ') << "]" << std::flush;
            std::cout << "\033[2F";
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
    std::cout << "\nDone!" << std::endl;
    return 0;
}
```
