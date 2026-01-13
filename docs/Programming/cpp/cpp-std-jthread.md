# \[C++\] JThread

> (since C++20) `std::jthread` được phát triển từ sau __C++20__

## Mô Tả

`std::jthread` giống như luồng cũ nhưng nó theo đúng luật an toàn luồng. Các tính năng sau đã được xác thực:

- Luồng sau khi thoát không cần thiết phải __join()__. Nó trở thành chức năng tự động.
    - Nếu hàm main kết thúc khi luồng còn hoạt động, sẽ tự động đợi luồng như khi gọi tới __*join()*__
- Kể cả sau trở thành luồng an toàn, việc __*detach()*__ luồng vẫn cực kỳ nguy hiểm. Luồng chính vẫn không đợi được luồng con bằng __*join()*__ như trường hợp luồng thông thường.
- Hãy cố gắng đảm bảo quy tắc trong luồng __*detach()*__ tất cả các tài nguyên cần phải sao chép, hoạt động duy nhất trên luồng. Không nên __*detach()*__ luồng có chia sẻ chung dữ liệu.

## Thành Viên

### Member types

| Member types       | Definition                      |
| :----------------- | :------------------------------ |
| id                 | std::thread::id                 |
| native_handle_type | std::thread::native_handle_type |

## Ví dụ

### Auto Join

```cpp
#include <iostream>
#include <chrono>
#include <thread>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

void task(int count) {
    while(count --> 0)  {
        println("Countdown: ", count);
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
}

int main() {
    std::jthread t1(task, 10);
    return 0;
}
```
```text title="Kết Quả"
Countdown: 9
Countdown: 8
Countdown: 7
Countdown: 6
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Countdown: 0
```

Như có thể thấy, không cần thực hiện __*join()*__ để chờ luồng kết thúc. Luồng chính sẽ tự chờ luồng con hoạt động thành công.

### Detach

Trong trường hợp bạn gọi đến _detach()_ thì luồng sẽ ngay lập tức kết thúc vì luồng chính mất khả năng điều khiển luồng đơn.

```cpp
#include <iostream>
#include <chrono>
#include <thread>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

void task(int count) {
    while(count --> 0)  {
        println("Countdown: ", count);
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
}

int main() {
    std::jthread thread(task, 10);
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    thread.detach();
    return 0;
}
```
```text title="Kết Quả"
Countdown: 9
Countdown: 8
Countdown: 7
```