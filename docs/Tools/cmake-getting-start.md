# CMake Getting Start

## Chuẩn Bị

Chuẩn bị một một cấu trúc tệp thực thi như sau:

=== "Danh Sách Tệp"
    ```cmake
    .
    ├── CMakeLists.txt
    ├── include --> header file (.h, .hpp, ...)
    ├── src     --> source file (.c, .cpp, ...)
    ├── lib     --> lib extend (if need)
    └── main.cpp
    ```
=== "Tạo Danh Sách"
    Khi lười tạo thì có thể sao chép lệnh dưới dây
    ```text
    touch main.cpp CMakeLists.txt
    mkdir include src lib
    ```

Về căn bản không nhất định phải để các tệp thư mục như hướng dẫn. Nhưng nên làm thế vì đó là cấu trúc phổ biến cho các mã nguồn chương trình lập trình hiện đại.

## Nội Dung

Các tệp sẽ có nội dung như sau:

```cmake title="CMakeLists.txt"
cmake_minimum_required(VERSION 3.10)

set(CMAKE_PROJECT_NAME app-name)
project(${CMAKE_PROJECT_NAME})

# Ensure the compiler MUST support this version to continue
# Disable compiler-specific extensions (makes your code more portable)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

file(GLOB_RECURSE SOURCES "src/*.cpp")

# Create the executable
add_executable(${CMAKE_PROJECT_NAME} main.cpp ${SOURCES})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC include)
```

Giải thích ngắn gọn một số cấu hình như sau:

- `set(VAR_NAME {text})` dùng để cài đặt một giá trị nào đó vào `VAR_NAME` như một biến tạm. Các phần sau đó CMake sẽ tự thay thế chúng vào trong kịch bản build. Mục đích của việc này là để tránh việc khai báo một tên giống nhau nhiều lần hoặc gom tên các đối tượng thành một cụm để dựng dễ dàng hơn.
- `set(CMAKE_PROJECT_NAME app-name)`: Như đã trình bày, dòng này để lưu tên ứng dụng. Các phần tiếp theo sẽ có ít nhiều sử dụng lại cái tên này thế nên việc đặt tên như này giúp cho việc lần sau nếu muốn lập bản dựng chỉ cần sửa lại `app-name` thành tên ứng dụng kết xuất mong muốn.
- `project(${CMAKE_PROJECT_NAME})`: Bắt buộc. Cái này để định danh tên dự án. Và nó là tên được trình bày ở trên.
- `set(CMAKE_CXX_STANDARD 23)`, `set(CMAKE_CXX_STANDARD_REQUIRED ON)`, `set(CMAKE_CXX_EXTENSIONS OFF)` dùng để cài đặt các thông số chung. Các biến này thuộc phạm vi của CMake nên không thể đổi tên (trường `VAR_NAME` ấy).
- `file(GLOB_RECURSE SOURCES "src/*.cpp")` Thêm tất cả các tệp nguồn có đuôi là cpp trong thư mục **src**
- `add_executable(${CMAKE_PROJECT_NAME} main.cpp ${SOURCES})` Đâu là dòng định nghĩa kết xuất ra tệp thực thi. Ý nghĩa là _ứng dụng với tên là `${CMAKE_PROJECT_NAME}` sẽ được biên dịch từ `main.cpp` và các tệp trong `${SOURCES}` (được khai báo ở trên)_
- `target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC include)` Đưa vào các tệp _**hearder** (tệp khai báo prototype)_ nằm trong thư mục **include** vào.

Vì đây chỉ là ví dụ đầu tiên nên mã nguồn không cần thiết phải làm gì đặc biệt. Chỉ cần để như này.

```cpp title="main.cpp"
#include <iostream>

int main(int argc, const char* args[]) {
    std::cout << "Hello World" << std::endl;
    return 0;
}
```

Đây là _**HelloWorld**_ nên không có thêm các lớp khai báo thêm nào khác.

## Lập Bản Dựng

Là một hệ thống xây dựng, CMake sẽ sử dụng make để làm việc và các công cụ build. Chạy lệnh sau để bắt đầu biên dịch:

```bash
cmake -S . -B out
cmake --build out
```

Với:

- `-S .`: Nguồn nằm ở thư mục hiện tại
- `-B out`: Xuất file build/config vào thư mục **out** (tự động tạo nếu chưa có)
- `cmake --build out`: Biên dịch trong thư mục **out** mà không cần phải vào thư mục **out**

!!! quote "Quote"
    Trong một số dự án trên _**github**_ ví dụ [FTXUI](../Library/FTXUI/ftxui.md) có hướng dẫn biên dịch như là:

    ```text
    mkdir build
    cd build
    cmake ..
    ```

    Chính chính là như trên. Hướng dẫn phía trên là mình đã xem xét và rút gọn để có thể dựng trực tiếp từ gốc dự án.


## Mẹo

### Kết Hợp Với VSCode

Đầu tiên cần biết rằng lệnh build có hai lệnh, `cmake -S . -B out && cmake --build out`. Nếu mỗi lần dựng chương trình đều phải vào terminal và gõ hai lệnh sẽ rất phiền phức. Do đó có thể làm một _**script**_ _(đặt tên là `build.sh`)_:

```bash
touch build.sh
sudo chmod +x build.sh
```

Với nội dung như sau:

```bash title="build.sh"
#!/usr/bin/bash

# Uncommand dòng này nếu bạn muốn rebuild cho mỗi lần biên dịch
# rm -rf ./out

cmake -S . -B out
cmake --build out
```

Sau đó nối chúng vào phần _tasks_ của VSCode. Chạy lệnh sau để tạo Task mặc định:

```bash
mkdir .vscode
touch .vscode/tasks.json
```

Dán nội dung dưới đây vào tệp `.vscode/tasks.json`

```json title="tasks.json"
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build Project",
            "type": "shell",
            "linux": {
                "command": "/usr/bin/bash ./build.sh",
            },
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "isBackground": true
        },
        {
            "label": "Run Test",
            "type": "shell",
            "linux": {
                "command": "./out/app-name",
            },
            "group": {
                "kind": "test",
                "isDefault": true
            },
            "isBackground": true
        },
    ]
}
```

> **app-name** là tên của tệp thực thi trong ví dụ này. Thay nó thành tên ứng dụng của bạn khi tự cấu hình lại.