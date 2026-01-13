# \[C++\] Async Thread

__Async Thread__ là dạng khởi tạo một luồng thực thi một tác vụ nào đó trong khi luồng chính vẫn hoạt động. Đến một thời điểm nào đó luồng sẽ bắt đầu quay trở lại và lấy giá trị của biến đó.
- Nếu thực thi thành công thì giá trị sẽ được trả về.
- Nếu luồng chưa xong thì sẽ chờ

## Ví Dụ

=== "Từ C++20"
    ```cpp
    #include <iostream>
    #include <future>
    #include <chrono>

    int fetch_data() {
        std::this_thread::sleep_for(std::chrono::seconds(2));
        return 42;
    }

    int main() {
        // Start task asynchronously
        std::future<int> result = std::async(std::launch::async, fetch_data);

        std::cout << "Doing other work..." << std::endl;

        // .get() blocks until the value is ready (similar to "await")
        int value = result.get(); 
        std::cout << "Result: " << value << std::endl;

        return 0;
    }
    ```
=== "Nhỏ hơn C++20"
    ```cpp
    #include <iostream>
    #include <future>
    #include <chrono>
    #include <unistd.h>

    int fetch_data() {
        sleep(2);
        return 42;
    }

    int main() {
        // Start task asynchronously
        std::future<int> result = std::async(std::launch::async, fetch_data);

        std::cout << "Doing other work..." << std::endl;

        // .get() blocks until the value is ready (similar to "await")
        int value = result.get(); 
        std::cout << "Result: " << value << std::endl;

        return 0;
    }
    ```
    Thay hàm `sleep_for` bằng hàm sleep trong __*unistd.h*__

- Trong ví dụ trên một nhiệm vụ được thực hiện trong hàm __fetch_data()__, khởi tạo bằng __std::async__
- Sau đó thì luồng đó tiếp tục thực hiện đến khi gọi vào hàm __get()__ để lấy kết quả trả về. Lúc này vì hàm đang bị _nghỉ 2s_ trong luồng phụ nên chương trình được nghỉ mất một trước khi kết thúc.