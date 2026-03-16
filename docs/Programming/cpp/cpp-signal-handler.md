# C++ Signal Handler

## Signal là gì?

**Signal** là các tín hiệu được đưa lên trực tiếp từ hệ điều hành nhằm thông báo một mã lỗi cục bộ xảy ra trong quá trình phần mềm thực thi.
Thư viện này kế thừa từ C nên có thể xem mẫu ở đây [C Signal Handler](../c/c-signal-handler.md)

Ý nghĩa của các thư viện này có thể tham khảo tại [OS Posix Signal](http://localhost:65000/OS/os-posix-signal/)/[(public)](https://dothanhdathp.github.io/taddev/OS/os-posix-signal/)


```cpp
#include <iostream>
#include <csignal>
#include <atomic>
#include <support.h>

std::atomic<bool> main_loop = true;

void function_handler_signal(int sig) {
    std::cout << "Handle signal: " << sig << ". Do not interupt software." << std::endl;
    main_loop = false;
}

int main(int argc, const char* args[]) {
    std::cout << "Start " << args[0] << std::endl;
    std::signal(SIGINT,  function_handler_signal);
    std::signal(SIGILL,  function_handler_signal);
    std::signal(SIGABRT, function_handler_signal);
    std::signal(SIGFPE,  function_handler_signal);
    std::signal(SIGSEGV, function_handler_signal);
    std::signal(SIGTERM, function_handler_signal);
    std::signal(SIGHUP,  function_handler_signal);
    std::signal(SIGQUIT, function_handler_signal);
    std::signal(SIGTRAP, function_handler_signal);
    std::signal(SIGKILL, function_handler_signal);
    std::signal(SIGPIPE, function_handler_signal);
    std::signal(SIGALRM, function_handler_signal);

    std::cout << "Sleeping on 10s" << std::endl;
    int* cnt = new int(10);
    while (main_loop)
    {
        std::cout << "Count " << (*cnt)-- << std::endl;
        sleep_for_sec(1);
        if((*cnt) < 0) {
            // Access wrong index!
            cnt = nullptr;
            delete(cnt);
        }
    }
    
    std::cout << "Stop " << args[0] << std::endl;
    return 0;
}
```


## Tham Khảo

- OS Posix Signal
    - online
    - [local](http://localhost:65000/OS/os-posix-signal/)