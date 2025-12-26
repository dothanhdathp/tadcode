# \[C++\] Draw Loading

> Vẽ Loading Process bằng C++

Ví dụ này vẽ ra một đường loading như trong mấy cái ứng dụng khác, nhìn khá vui mắt.

## One Line

```cpp
#include <iostream>
#include <thread>
#include <unistd.h>

#define Loading(i) std::cout << "\rLoading: [" << std::string(i, '|') << std::string(100-i, ' ') << "]" << std::flush

void drawLoading(size_t pos) {
    std::cout << "\rLoading: [" << std::string(pos, '|') << std::string(100-pos, ' ') << "]" << std::flush;
}

int main() {
    // 1 Line
    for (size_t percents = 0; percents <= 100; percents++) {
        drawLoading(percents);
        usleep(10000);
    }
    std::cout << "\nDone!" << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Loading: [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]
Done!
```

## Multies Lines

Ví dụ này vẽ bao dòng chạy song song. Thực tế có thể nâng số dòng lên.

Số lượng task có thể tùy ý. Để lập lịch cho số lượng tiến trình chạy đồng thời, dùng biến __atomic__ để xử lý.

```cpp
#include <iostream>
#include <thread>
#include <unistd.h>

std::mutex print_lock;
void drawLoadingLine(std::atomic_size_t* proc, size_t numOfProc) {
    print_lock.lock();
    std::cout << "\033[" << numOfProc << 'F';
    while (numOfProc-- > 0)
        std::cout << "\rThread " << numOfProc << " : [" << std::string(proc[numOfProc], '|') << std::string(100-proc[numOfProc], ' ') << "]" << "]\033[K\n";
    std::cout << std::flush;
    print_lock.unlock();
}

void task(size_t id, std::atomic_size_t* proc) {
    for (size_t percents = 0; percents <= 100; percents++) {
        proc[id] = percents;
        drawLoadingLine(proc, 3);
        usleep(10000*(id+1));
    }
}

std::atomic_size_t process[3] = {0,0,0};

int main() {
    // Multies Line
    std::thread t0(task, 0, process);
    std::thread t1(task, 1, process);
    std::thread t2(task, 2, process);

    t0.join();
    t1.join();
    t2.join();

    std::cout << "\nDone!" << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Thread 2 : [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]]
Thread 1 : [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]]
Thread 0 : [||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]]

Done!
```