# \[C++\] Coroutine

__Coroutine__ là chế độ chạy xen kẽ giả thread. Chúng được sinh ra để chia sẻ tài nguyên trên một luồng để tối ưu hóa tài nguyên máy một cách triệt để.

## C++23

```cpp
#include <iostream>
#include <generator> // C++23 feature

// This is a coroutine
std::generator<int> count_up(int start, int end) {
    for (int i = start; i <= end; ++i) {
        co_yield i; // Execution PAUSES here and returns 'i'
    }
    // Execution ends here
}

int main() {
    auto numbers = count_up(1, 3);

    for (int n : numbers) {
        std::cout << n << " "; // Prints 1 2 3
    }
}
```

!!! danger "Không chạy"
    Việc thực hiện dựng trên các cờ bản bị lỗi.

## C++20

Ở các bản cũ hơn, cấu trúc struct được được phát triển, thế nên cần khai báo tay:

```cpp
#include <iostream>
#include <coroutine>

struct Generator {
    // 1. The Promise Object: Defines the behavior
    struct promise_type {
        int current_value;
        Generator get_return_object() { return Generator{std::coroutine_handle<promise_type>::from_promise(*this)}; }
        std::suspend_always initial_suspend() { return {}; }
        std::suspend_always final_suspend() noexcept { return {}; }
        void unhandled_exception() { std::terminate(); }
        void return_void() {}
        std::suspend_always yield_value(int value) {
            current_value = value;
            return {};
        }
    };

    // 2. The Handle: Used to resume the coroutine
    std::coroutine_handle<promise_type> handle;

    Generator(std::coroutine_handle<promise_type> h) : handle(h) {}
    ~Generator() { if (handle) handle.destroy(); }

    bool next() {
        if (!handle || handle.done()) return false;
        handle.resume();
        return !handle.done();
    }

    int value() { return handle.promise().current_value; }
};

// Simple usage
Generator simple_count() {
    for (int i = 1; i <= 3; ++i) {
        co_yield i; 
    }
}

int main() {
    auto gen = simple_count();
    while (gen.next()) {
        std::cout << gen.value() << " "; // Output: 1 2 3
    }
}
```
```text
1 2 3
```