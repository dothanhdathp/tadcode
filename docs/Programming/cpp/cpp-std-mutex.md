# \[C++\] Mutex

Lớp `mutex` là một lớp nguyên thủy đồng bộ hóa có thể được sử dụng để bảo vệ dữ liệu được chia sẻ khỏi bị nhiều luồng truy cập đồng thời.

`mutex` cung cấp ngữ nghĩa quyền sở hữu độc quyền, không đệ quy:

Một luồng gọi sở hữu một `mutex` kể từ thời điểm nó gọi thành công `lock` hoặc `try_lock` cho đến khi nó gọi `unlock`.

Khi một __*thread*__ sở hữu một __*mutex*__, tất cả các __*thread*__ khác sẽ chặn (đối với các cuộc gọi đến `lock`) hoặc nhận giá trị trả về sai (đối với`try_lock`) nếu họ cố gắng đòi quyền sở hữu `mutex`.

Chuỗi cuộc gọi không được sở hữu `mutex` trước khi gọi `lock` hoặc `try_lock`.

Hành vi của một chương trình là không xác định nếu một `mutex` bị hủy trong khi vẫn thuộc sở hữu của bất kỳ luồng nào hoặc một luồng chấm dứt khi sở hữu một `mutex`. Lớp `mutex` đáp ứng mọi yêu cầu của __Mutex__ và __StandardLayoutType__.

`std::mutex` không thể sao chép và di chuyển được.

!!! note "Note"
    Nói ngắn gọn, khi gọi đến mutex nó sẽ khóa luồng và cấm các luồng khác tiếp tục thực thi để đảm bảo luồng đó được hoạt động ổn định

## Sử dụng

### Ổn Định Luồng Với Mutex

=== "Không Mutex"
    Các luồng chạy chồng chéo khiến tín hiệu bị lẫn.

    ```cpp
    #include <iostream>
    #include <thread>
    #include <mutex>
    #include <unistd.h>

    template <typename... Args>
    void println(Args... args) {
        (std::cout << ... << args) << std::endl; // C++17 Fold Expression
    }

    void task(int id) {
        int cnt = 10;
        while (cnt --> 0) {
            sleep(1);
            println("[thread ",id,"] count down ", cnt);
        }
        println("[thread ",id,"] FINISH!");
    }

    int main() {
        std::thread t1(task, 0);
        std::thread t2(task, 1);

        t1.join();
        t2.join();
        return 0;
    }
    ```
    ```text title="Kết Quả"
    [thread 0] count down 9[thread 
    [thread 0] count down 8
    1[thread ] count down 09] count down 
    [thread 1] count down 8
    [thread 1] count down 7
    [thread 1] count down 6
    [thread 1] count down 5
    [thread 1] count down 4
    7[thread 1] count down 3

    [thread 0] count down 6
    [thread 0] count down 5
    [thread 0] count down 4
    [thread 0] count down 3[thread 1] count down 2
    [thread 1] count down 1

    [thread 0] count down 2
    [thread 0] count down 1
    [thread 0] count down 0
    [thread 0] FINISH!
    [thread 1] count down 0
    [thread 1] FINISH!
    ```
=== "Có Mutex"
    Thêm mutex, khóa lại luồng khi đang thực thi quá trình in kết quả ra ngoài màn hành sau đó nhả khóa. Kết quả các luồng được thi thi tuần tự đẹp đẽ.

    ```cpp
    #include <iostream>
    #include <thread>
    #include <mutex>
    #include <unistd.h>

    template <typename... Args>
    void println(Args... args) {
        (std::cout << ... << args) << std::endl; // C++17 Fold Expression
    }

    std::mutex global_mutex;

    void task(int id) {
        int cnt = 10;
        while (cnt --> 0) {
            sleep(1);
            global_mutex.lock();
            println("[thread ",id,"] count down ", cnt);
            global_mutex.unlock();
        }
        println("[thread ",id,"] FINISH!");
    }

    int main() {
        std::thread t1(task, 0);
        std::thread t2(task, 1);

        t1.join();
        t2.join();
        return 0;
    }
    ```
    ```text title="Kết Quả"
    [thread 1] count down 9
    [thread 0] count down 9
    [thread 0] count down 8
    [thread 1] count down 8
    [thread 0] count down 7
    [thread 1] count down 7
    [thread 1] count down 6
    [thread 0] count down 6
    [thread 1] count down 5
    [thread 0] count down 5
    [thread 1] count down 4
    [thread 0] count down 4
    [thread 0] count down 3
    [thread 1] count down 3
    [thread 0] count down 2
    [thread 1] count down 2
    [thread 0] count down 1
    [thread 1] count down 1
    [thread 1] count down 0
    [thread 1] FINISH!
    [thread 0] count down 0
    [thread 0] FINISH!
    ```

## Death Lock

__Death Lock__ là trường hợp mà hai __*thread*__ sử dụng và khóa chéo nhau. ThreadA giữ khóa cuả ThreadB và ngược lại khiến hai __*thread*__ rơi chung vào trạng thái _khóa chéo hành vi của nhau_ và đều _chờ nhau mở khóa_. Trường hợp này rất dễ xảy ra khi lạm dụng các khóa __*mutex*__, đây là một ví dụ điển hình:

```cpp title="Death Lock"
#include <iostream>
#include <thread>
#include <mutex>
#include <unistd.h>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

void task(int id, std::mutex* lock_a, std::mutex* lock_b) {
    int cnt = 100;
    while (cnt --> 0) {
        lock_a->lock();
        lock_b->lock();
        println("[thread ",id,"] count down ", cnt);
        lock_b->unlock();
        lock_a->unlock();
    }
    println("[thread ",id,"] FINISH!");
}

int main() {
    std::mutex locker_A;
    std::mutex locker_B;
    std::thread t1(task, 20, &locker_A, &locker_B);
    std::thread t2(task, 10, &locker_B, &locker_A);

    t1.join();
    t2.join();
    return 0;
}
```
```text title="Kết Quả"
[thread 20] count down 99
[thread 20] count down 98
[thread 20] count down 97
[thread 20] count down 96
[thread 20] count down 95
[thread 20] count down 94
[thread 20] count down 93
[thread 20] count down 92
[thread 20] count down 91
[thread 20] count down 90
[thread 20] count down 89
[thread 20] count down 88
[thread 20] count down 87
[thread 20] count down 86
[thread 20] count down 85
[thread 20] count down 84
[thread 20] count down 83
[thread 20] count down 82
[thread 20] count down 81
[thread 20] count down 80
[thread 20] count down 79
[thread 20] count down 78
[thread 20] count down 77
[thread 20] count down 76
[thread 20] count down 75
[thread 20] count down 74
[thread 20] count down 73





(blocking and not work)
```

Như ở trên việc mỗi luồng đang sử dụng khóa để khóa chéo nhau. Lúc đầu thì chương trình vẫn hoạt động, lúc sau thì bị treo. Đây chỉ là ví dụ nên tốc độ luồng đã được đẩy nhanh và nhất quán chứ ở những hệ thống lớn, việc có hàng trăm luồng cùng hoạt động và khóa chéo nhau như này là rất dễ xảy ra và một khi xảy ra ... rất khó __debug__.

## Tốn Kém

- `mutex` khá là tốn kém. Việc sử dụng nó cũng nhiều vấn đề như khóa chéo ()

## Tham Khảo

- [Cppreference - Mutex](https://en.cppreference.com/w/cpp/thread/mutex.html)
- _Phân Cấp Khóa_ : __Lock Hierarchy__