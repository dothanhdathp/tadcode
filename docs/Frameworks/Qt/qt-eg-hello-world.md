# Qt Hello World

## Source

- **main.cpp**: Chứa mã nguồn.
- **CMakeList**: Tệp CMake đơn giản.

```cpp title="main.cpp"
#include <QApplication>
#include <QLabel>
#include <QWidget>

int main(int argc, char *argv[]) {
    // Khởi tạo đối tượng quản lý vòng lặp sự kiện của ứng dụng
    QApplication app(argc, argv);

    // Tạo một cửa sổ chính (widget)
    QWidget window;
    window.setWindowTitle("My First Application");
    window.resize(300, 100);

    // Tạo một nhãn dán hiển thị văn bản
    QLabel *label = new QLabel("Hello World!", &window);
    label->setAlignment(Qt::AlignCenter);
    label->setGeometry(0, 0, 300, 100);

    // Hiển thị cửa sổ
    window.show();

    // Chạy vòng lặp sự kiện
    return app.exec();
}
```
```cmake title="CMakeList.txt"
cmake_minimum_required(VERSION 3.16)

project(HelloWorld LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Tìm các gói Qt cần thiết
find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_executable(HelloWorld main.cpp)

# Liên kết với thư viện Widgets của Qt
target_link_libraries(HelloWorld PRIVATE Qt6::Widgets)
```

## Build

### Build With Prefix

- Cài đặt `-DCMAKE_PREFIX_PATH` với địa chỉ đường dẫn trực tiếp đến thư viện Qt tự build

```text
cmake -S . -B ./out -DCMAKE_PREFIX_PATH=/home/tad/.local/lib/qt/6.10.2
cmake --build ./out --parallel $(nproc)
```