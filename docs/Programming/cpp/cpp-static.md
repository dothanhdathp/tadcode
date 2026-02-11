# Static

## Khái Niệm

`static` là từ khóa khai báo rằng một biến chỉ khởi tạo một lần và tái sử dụng lại giá trị đó trong phạm vi của hàm, tệp, ẩn giấu với phần còn lại. Xem ví dụ sau:

```cpp
#include <iostream>

void tick() {
    static int counter_value;
    counter_value++;
    std::cout << counter_value << std::endl;
}

int main(int argc, const char* args[]) {
    for (int i{0}; i < 10; ++i)
        tick();
    return 0;
}
```

- Nếu không có `static`, giá trị in ra sẽ luôn là 1. 
    ```text
    1 1 1 1 1 1 1 1 1 1
    ```
- Nếu có `static`, giá trị in ra sẽ luôn là
    ```text
    1 2 3 4 5 6 7 8 9 10
    ```

Từ khóa `static` _giới hạn phạm vi_ của biến trong  