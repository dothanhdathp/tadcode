# Steady Clock

- __Steady Clock__ là đồng hồ với bộ đếm chính xác. Nó không đại diện hay phụ thuộc vào biến số đồng hồ của hệ điều hành.
- __Steady Clock__ thường được sử dụng để tính thời gian hoạt động của chương trình hoặc một đoạn chương trình.

## Tính tốc độ thực thi

```cpp
#include <iostream>
#include <chrono>
#include <thread>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

typedef std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<signed long, std::nano>> htime_t;

int main() {
    // Get time point start
    htime_t start = std::chrono::high_resolution_clock::now();
    
    println("Do something! ...");

    // Get time point stop
    htime_t end = std::chrono::high_resolution_clock::now();

    // Calculate the duration
    std::chrono::duration<double, std::milli> duration = end - start;

    // Output the time taken
    std::cout << "Time taken by program is : " << duration.count() << " milliseconds" << std::endl;

    return 0;
}
```
```text
Do something! ...
Time taken by program is : 0.017273 milliseconds
```

Ở dòng __std::chrono::duration<double, std::milli> duration = end - start;__, thẻ `std::milli` có thể thay bằng các trường khác với các độ chia khác nhau một chút:

|     | Tiền Tố      | Tỉ Lệ                |
| --: | :----------- | :------------------- |
|     | `std::atto`  | 000000000000000000.1 |
|     | `std::femto` | 000000000000000.1    |
|     | `std::pico`  | 000000000000.1       |
|   * | `std::nano`  | 000000000.1          |
|   * | `std::micro` | 000000.1             |
|   * | `std::milli` | 000.1                |
|     | `std::centi` | 00.1                 |
|     | `std::deci`  | 0.1                  |
|     | `std::deca`  | 10                   |
|     | `std::hecto` | 100                  |
|     | `std::kilo`  | 1000                 |
|     | `std::mega`  | 1000000              |
|     | `std::giga`  | 1000000000           |
|     | `std::tera`  | 1000000000000        |
|     | `std::peta`  | 1000000000000000     |
|     | `std::exa`   | 1000000000000000000  |

## 