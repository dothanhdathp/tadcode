# System Clock

__System Clock__ chính là đồng hồ của hệ thống.

## Đọc System Clock

Thư viện yêu cầu `chrono`

=== "Normal"
    ```cpp
    #include <iostream>
    #include <chrono>

    int main()
    {
        // Get current time
        const auto now = std::chrono::system_clock::now();
        
        // Convert to (std::chrono::system_clock) to POSIX time type (std::time_t)
        const std::time_t now_2_time_t = std::chrono::system_clock::to_time_t(now);

        // Read time
        std::cout << "The system clock is currently at " << std::ctime(&now_2_time_t);
    }
    ```
=== "Namespace"
    ```cpp
    #include <iostream>
    #include <chrono>

    template <typename... Args>
    void println(Args... args) {
        (std::cout << ... << args) << std::endl; // C++17 Fold Expression
    }

    using namespace std;
    using namespace std::chrono;

    int main()
    {
        // Get current time
        const auto now = system_clock::now();
        
        // Convert to (std::chrono::system_clock) to POSIX time type (std::time_t)
        const time_t now_2_time_t = system_clock::to_time_t(now);

        // Read time
        cout << "The system clock is currently at " << ctime(&now_2_time_t);
    }
    ```

```text title="Kết Quả"
The system clock is currently at Mon Jan 12 18:44:17 2026
```

Trong dòng đầu tiên, `std::chrono::system_clock::now();` trả về thời gian dấu mốc thời gian được tính theo dạng dấu thời gian `system_clock::time_point` đầy đủ là `std::chrono::_V2::system_clock::time_point`

Độ dài này là bởi vì trong các hệ thống khác nhau __*(POSIX or NON_POSIX)*__ sử dụng những phương thức khác nhau để đánh dấu mốc thời gian kèm theo đó là mối quan hệ về các thư viện hỗ trợ khác.

```cpp title="No Auto Type"
#include <iostream>
#include <chrono>

void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

typedef std::chrono::_V2::system_clock::time_point time_point_t;

int main()
{
    // Get current time
    time_point_t now = std::chrono::system_clock::now();
    
    // Convert to (std::chrono::system_clock) to POSIX time type (std::time_t)
    const std::time_t now_2_time_t = std::chrono::system_clock::to_time_t(now);

    // Read time
    std::cout << "The system clock is currently at " << std::ctime(&now_2_time_t);
}
```

## Tính Thời Gian Thực Thi Bằng System Clock

```cpp
#include <iostream>
#include <chrono>
#include <thread>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

typedef std::chrono::_V2::system_clock::time_point stime_t;

int main() {
    // Get time point start
    stime_t start = std::chrono::system_clock::now();
    
    println("Do something! ...");

    // Get time point stop
    stime_t end = std::chrono::system_clock::now();

    // Calculate the duration
    std::chrono::duration<double, std::milli> duration = end - start;

    // Output the time taken
    std::cout << "Time taken by program is : " << duration.count() << " milliseconds" << std::endl;

    return 0;
}
```

!!! note "Note"
    Ở cấp đô mili giây thì phương pháp này có thể, nếu đòi hỏi sử tính toán đồng hồ chính xác ở cấp độ cao hơn khuyến cáo sử dụng [Steady Clock](cpp-system-steady-clock.md)