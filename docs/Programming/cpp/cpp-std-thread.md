# \[C++\] Thread

Theard là các phân luồng hoạt động trong __C++__. Đa luồng giúp chương trình thực thi nhiều tác vụ cùng một lúc giúp cho hệ thống trơn tru hơn. Mặc dù đánh đổi bởi sự an toàn cũng như việc quản lý tài nguyên nhưng thật sự đa luồng rất hữu dụng.

## Synchronous Thread

Thread là một tiến trình tách biệt với luồng chính của chương trình, nhưng vẫn sẽ sử dụng chung không gian bộ nhớ _(hệ điều hành quản lý)_. Thế nên việc sử dụng luồng ra sao là việc của hệ điều hành.

- Trong __C++__, một luồng - __thread__ được tạo ra bằng công thức: `std::thread __name(__function__)`
- Sau đó hàm được dùng khởi tạo sẽ ngay lập tức được khởi động.
- Trong khi luồng, luồng tại main sẽ không bị khóa.
- Luồng chính sẽ chờ tiến trình ở luồng con bằng hàm __join()__, tiến trình chờ này được gọi là đồng bộ luồng __*(Synchronous)*__.

### Ví Dụ

- Ví dụ dưới đây cho thấy sự hoạt động của hai luồng con trong một luồng chính.
- Luồng chính hoạt động sau mỗi 0.5 giây, các luồng con là một giây.
- Sau khi kết thúc hoạt động, luồng chính sẽ chờ tại __join()__ cho đến khi luồng kết thúc mới kết thúc chương trình.

```cpp
#include <cstdio>
#include <iostream>
#include <vector>
#include <thread>
#include <unistd.h>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

void task() {
    int cnt{10};
    while (cnt --> 0) {
        sleep(1);
        println("[task][", std::this_thread::get_id(), "] count down ", cnt);
    }
}

int main() {
    std::thread t1(task);
    std::thread t2(task);

    // Get thread IDs
    std::cout << "t1 ID: " << t1.get_id() << std::endl;
    std::cout << "t2 ID: " << t2.get_id() << std::endl;

    int cnt{10};

    while (cnt --> 0) {
        usleep(500000);
        println("[main][", std::this_thread::get_id(), "] count down ", cnt);
    }

    // Wait thread done.
    t1.join();
    t2.join();

    return 0;
}
```
```text title="Kết Quả"
t1 ID: 130044710090432
t2 ID: 130044701697728
[main][130044717029184] count down 9
[task][[task][130044701697728130044710090432] count down ] count down 99

[main][130044717029184] count down 8
[main][130044717029184] count down 7
[task][[task][130044701697728] count down 1300447100904328] count down 
8
[main][130044717029184] count down 6
[main][130044717029184] count down 5
[task][[task][130044710090432130044701697728] count down ] count down 77

[main][130044717029184] count down 4
[main][130044717029184] count down 3
[task][[task][130044710090432130044701697728] count down ] count down 66

[main][130044717029184] count down 2
[main][130044717029184] count down 1
[task][[task][130044701697728130044710090432] count down ] count down 55

[main][130044717029184] count down 0
[task][[task][130044701697728130044710090432] count down ] count down 44

[task][[task][130044701697728] count down 130044710090432] count down 33

[task][[task][130044710090432130044701697728] count down ] count down 22

[task][130044701697728] count down 1
[task][130044710090432] count down 1
[task][[task][130044710090432130044701697728] count down ] count down 00
```

Dễ thấy, các hàm in ra không có sự đồng bộ, các tiến trình được xen lận

## Asynchronous Thread
> Luồng không đồng bộ

- Luồng không đồng bộ là luồng được tách hoàn toàn khỏi __*main*__, hàm thực hiện việc đó là hàm __*detach()*__
- Qua việc __*detach()*__ luồng, luồng main sẽ không còn có thể chờ luồng thực thi và đồng bộ lại nữa. Tức là khi này __join()__ sẽ không còn tác dụng.
- Cách này không được khuyến nghị, bởi việc này nên khi thoát chương trình, toàn bộ dữ liệu từ luồng khi __*detach()*__ sẽ không được giải phóng.
- Nếu luồng này thực hiện sớm và kết thúc sớm hơn main sẽ không sao, nhưng nếu luồng kết thúc muộn hơn __*main()*__ hoặc __*main()*__ bị ép kết thúc sớm, bộ nhớ sẽ bị rò rỉ. Tài nguyên tại các luồng con được __*detach()*__ sẽ bị giải phóng tuần tự theo __Stack__. Tại điểm không thể giải quyết, bộ nhớ sẽ treo gây hiện tượng rò rỉ bộ nhớ.
- Thế nên để an toàn, nếu thực sự cần __*detach()*__, luồng này nên hoạt động như một __*daemon*__ _(tác vụ nền)_ độc lập. Các tài nguyên sẽ được sao chép lại và sử dụng độc lập so với tác vụ chính.
- Sau khi __*detach()*__, __*thread*__ sẽ mất quyền kiểm soát và việc hủy, trừ nó rất rất nguy hiểm.

=== "Detach After"
    ```cpp
    #include <cstdio>
    #include <iostream>
    #include <vector>
    #include <thread>
    #include <unistd.h>

    template <typename... Args>
    void println(Args... args) {
        (std::cout << ... << args) << std::endl; // C++17 Fold Expression
    }

    void task() {
        int cnt = 10;
        while (cnt --> 0) {
            usleep(100);
            println("[task][", std::this_thread::get_id(), "] count down ", cnt);
        }
    }

    int main() {
        std::thread t1(task);
        std::thread t2(task);
        
        // Get thread IDs
        std::cout << "t1 ID: " << t1.get_id() << std::endl;
        std::cout << "t2 ID: " << t2.get_id() << std::endl;
        t1.detach();
        t2.detach();

        int cnt{10};
        while (cnt --> 0) {
            println("[main][", std::this_thread::get_id(), "] count down ", cnt);
        }

        println("End Main!");
        return 0;
    }
    ```
    ```text title="Kết Quả"
    t1 ID: 139057290016448
    t2 ID: 139057281623744
    [main][139057297254208] count down 9
    [main][139057297254208] count down 8
    [main][139057297254208] count down 7
    [main][139057297254208] count down 6
    [main][139057297254208] count down 5
    [main][139057297254208] count down 4
    [main][139057297254208] count down 3
    [main][139057297254208] count down 2
    [main][139057297254208] count down 1
    [main][139057297254208] count down 0
    End Main!
    ```
=== "Detach Before"
    ```cpp
    #include <cstdio>
    #include <iostream>
    #include <vector>
    #include <thread>
    #include <unistd.h>

    template <typename... Args>
    void println(Args... args) {
        (std::cout << ... << args) << std::endl; // C++17 Fold Expression
    }

    void task() {
        int cnt = 10;
        while (cnt --> 0) {
            usleep(100);
            println("[task][", std::this_thread::get_id(), "] count down ", cnt);
        }
    }

    int main() {
        std::thread t1(task);
        std::thread t2(task);
        
        // Get thread IDs
        std::cout << "t1 ID: " << t1.get_id() << std::endl;
        std::cout << "t2 ID: " << t2.get_id() << std::endl;
        t1.detach();
        t2.detach();

        int cnt{10};
        while (cnt --> 0) {
            println("[main][", std::this_thread::get_id(), "] count down ", cnt);
        }

        println("End Main!");
        return 0;
    }
    ```
    ```text title="Kết Quả"
    t1 ID: thread::id of a non-executing thread
    t2 ID: thread::id of a non-executing thread
    [main][136640126654272] count down 9
    [main][136640126654272] count down 8
    [main][136640126654272] count down 7
    [main][136640126654272] count down 6
    [main][136640126654272] count down 5
    [main][136640126654272] count down 4
    [main][136640126654272] count down 3
    [main][136640126654272] count down 2
    [main][136640126654272] count down 1
    [main][136640126654272] count down 0
    End Main!
    ```
## Truyền tham số

Có thể truyền tham số vào cho __*thread*__. Giải sử hàm truyền vào nhận tham số là như này.

```cpp
void task(int id) {
    int cnt = 10;
    while (cnt --> 0) {
        sleep(1);
        println("[thread ",id,"] count down ", cnt);
    }
}
```

Thì khi khai báo tạo __*thread*__ có thể đưa vào tham số như này.

```cpp
std::thread t1(task, 1);
std::thread t2(task, 2);
```
```text title="Kết Quả"
[thread 1] count down 1
[thread 2] count down 1
```

## Tiếp Theo

- An toàn luồng với [Mutex](cpp-std-mutex.md)