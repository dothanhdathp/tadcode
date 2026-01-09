# \[C++\] thread_local

- `thread_local` là một loại _keyword_ trong C++.
- `thread_local` khai báo một biến trở thành một biến độc lập trên luồng.
- Khác với biến bản thân được tạo trong hàm sẽ khai báo trên __Stack__, biến độc lập trên luồng chạy trên __Heap__.
- Biến `thread_local`:
    - Khởi tạo khi luồng được khởi tạo
    - Tự đông giải phóng khi luồng kết thúc

```cpp
#include <iostream>
#include <vector>
#include <thread>

thread_local int i = 10;

void task(std::string task_name) {
    std::cout << "Addresss of i on " << task_name << &i << std::endl;
    while (i --> 0) {
        std::cout << task_name << i << std::endl;
        using namespace std::literals::chrono_literals;
        std::this_thread::sleep_for(1ms);
    }
}

int main() {
    std::cout << "Addresss of i on main: " << &i << std::endl;
    std::jthread task0(task, std::string("Task 0: "));
    std::jthread task1(task, std::string("Task 1: "));

    task0.join();
    task1.join();
    return 0;
}
```
```text title="Kết Quả"
Addresss of i on main: 0x72aeed09d73c
Addresss of i on Task 0: 0x72aeec9ff6bc
Task 0: 9
Addresss of i on Task 1: 0x72aeec1fe6bc
Task 1: 9
Task 0: 8
Task 1: 8
Task 0: 7
Task 1: 7
Task 0: 6
Task 1: 6
Task 0: 5
Task 1: 5
Task 0: 4
Task 1: 4
Task 0: 3
Task 1: 3
Task 0: 2
Task 1: 2
Task 0: 1
Task 1: 1
Task 0: 0
Task 1: 0
```

- Xét về luồng thì ở đây có 3 luồng.
Như có thể thấy, trên mỗi luồng biến i có một địa chỉ khác nhau.