# Buikd Qt Source

## Tải Về

Tải về nguồn tại [kho lưu trữ **official_releases**, thư mục **qt**](https://download.qt.io/official_releases/qt/). Sau đó tại phiên bản mong muốn tìm đến thư mục **single**, tìm tệp binary tải về  có dạng _**qt-everywhere-src-{version}.zip**_ hoặc _**qt-everywhere-src-{version}.tar.xz**_.

## Build

### Yêu Cầu
> [Tham khảo tại](https://doc.qt.io/qt-6/linux-requirements.html)

- Theo trang chủ, các tệp dưới này là yêu cầu cần thiết.
- Thêm cờ `-y` để các gói tải về luôn _(thay cho câu trả lời **yes**)_

```text
apt install \
    libfontconfig1-dev \
    libfreetype-dev \
    libgtk-3-dev \
    libx11-dev \
    libx11-xcb-dev \
    libxcb-cursor-dev \
    libxcb-glx0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-shape0-dev \
    libxcb-shm0-dev \
    libxcb-sync-dev \
    libxcb-util-dev \
    libxcb-xfixes0-dev \
    libxcb-xkb-dev \
    libxcb1-dev \
    libxext-dev \
    libxfixes-dev \
    libxi-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxrender-dev -y
```

### Build

- Trước tiên giải nén tệp vừa tải về - tệp tar.xz. Ở đây ví dụ nó là tệp `qt-everywhere-src-6.10.2` và tôi giải nên ở `/tmp/` để sau khi kết thúc, máy tính sẽ dọn dẹp các tệp đó.
    ```bash
    tar -xvf ./qt-everywhere-src-6.10.2.tar.xz -C /tmp/
    ```
- Tạo một thư mục khác để cấu hình và các biên dịch sẽ được tải vào đó. Ở đây với mong muốn hiểu hệ thống nên mình sẽ sử dụng thư mục riêng được đặt ở `~/.local/`, nơi chứa các biến và thành phần cục bộ. Có nghĩa là, ở cấp độ hệ thống sẽ không có Qt tránh gây rác, xung đột.
    - Tạo thư mục mới như sau
        ```bash
        mkdir ~/.local/lib
        mkdir ~/.local/lib/qt
        mkdir ~/.local/lib/qt/6.10.2
        cd ~/.local/lib/qt/6.10.2
        
        ```
- Theo mặc định, Qt được cấu hình để cài đặt trong đường dẫn `/usr/local/Qt-6.10.2`. Khi đó chạy lệnh cấu hình ở chế độ mặc định với lệnh `/tmp/qt-everywhere-src-6.10.2/configure`. Điều này có thể được thay đổi bằng cách sử dụng tùy chọn `-prefix`. Xem danh sách các tùy chọn cấu hình để điều chỉnh thêm. Vì mình muốn cài đặt Qt cho user nên mình dùng lệnh dưới này:
    ```bash
    /tmp/qt-everywhere-src-6.10.2/configure -prefix /home/tad/.local/lib/qt/6.10.2
    ```
- Một cách khác, khi mà cờ `-prefix` không hoạt động hoặc lỗi, có thể đưa trực tiếp cờ vào hệ thống như này:
    ```text
    /tmp/qt-everywhere-src-6.10.2/qtbase/configure -- -DCMAKE_INSTALL_PREFIX=/home/tad/.local/lib/qt/6.10.2
    ```
- Sau khi _configure_ hoàn thành. Tiến hành xây dựng thư viện và công cụ:
    ```bash
    cmake --build . --parallel
    ```
- Cài đặt cho Qt
    ```bash
    cmake --install .
    ```

### Kiểm Tra

Sau khi thành công, lệnh `cmake --install .` sẽ đưa các tệp cần thiết vào trong `/home/tad/.local/lib/qt/6.10.2`. Nó có dạng như này khi dùng `ls -la`

```text
drwxrwxr-x   2 tad tad  4096 Thg 3  20 11:09 bin/
drwxrwxr-x   4 tad tad  4096 Thg 3  20 11:09 doc/
drwxrwxr-x 188 tad tad 12288 Thg 3  20 11:09 include/
drwxrwxr-x   5 tad tad 36864 Thg 3  20 11:09 lib/
drwxrwxr-x   2 tad tad  4096 Thg 3  20 11:09 libexec/
drwxrwxr-x   2 tad tad 12288 Thg 3  20 11:09 metatypes/
drwxr-xr-x  66 tad tad  4096 Thg 3  20 11:09 mkspecs/
drwxrwxr-x   2 tad tad 12288 Thg 3  20 11:09 modules/
drwxrwxr-x   2 tad tad  4096 Thg 3  20 11:09 phrasebooks/
drwxrwxr-x  36 tad tad  4096 Thg 3  20 11:09 plugins/
drwxrwxr-x  31 tad tad  4096 Thg 3  20 11:09 qml/
drwxrwxr-x   2 tad tad  4096 Thg 3  20 11:09 sbom/
drwxrwxr-x   3 tad tad  4096 Thg 3  20 11:09 share/
drwxrwxr-x   2 tad tad 12288 Thg 3  20 11:09 translations/
```

### Sử Dụng

#### Các tệp cần thiết

Tạo thử một Project chạy Qt bao gồm hai tệp:

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

#### Biên Dịch

- Chạy command dưới này để biên dịch.
- Kết quả đầu ra được kết xuất trong thư mục `./out`
- Vì tự xây dựng nên phải sử dụng cờ `-DCMAKE_PREFIX_PATH` để đưa vào địa chỉ của thư viện qt tự build.

```bash
cmake -S . -B ./out -DCMAKE_PREFIX_PATH=/home/tad/.local/lib/qt/6.10.2
cmake --build ./out --parallel $(nproc)
```

- Kết quả như này

<figure markdown="span">
    ![alt text](img/qt-build-qt-source.png)
    <figcaption>Chương trình đầu tiên</figcaption>
</figure>

#### Một số cách khác

Việc trỏ cờ `-DCMAKE_PREFIX_PATH` đôi khi khá là bất tiện, buộc phải ghi nhớ câu lệnh. Để tránh cách này có thể.

1. Viết _script_ thực thi _(không khuyến nghị)_
1. Viết luôn cấu hình vào tệp **CMakeList.txt**
    - Trong tệp ___ thêm dòng này vào đầu:
        ```cmake
        cmake_minimum_required(VERSION 3.16)
        project(HelloWorld LANGUAGES CXX)

        # Thiết lập đường dẫn đến bộ thư viện Qt tự build
        # Lưu ý: Phải đặt trước find_package
        set(CMAKE_PREFIX_PATH "/home/tad/.local/lib/qt/qt6.10.2")
        ```
1. Cách cuối là sử dụng cờ cục bộ bằng
    ```bash
    export CMAKE_PREFIX_PATH=$HOME/.local/lib/qt/6.10.2:$CMAKE_PREFIX_PATH
    ```
    Khi này các câu lệnh biên dịch chỉ còn:
    ```bash
    cmake -S . -B ./out
    cmake --build ./out --parallel $(nproc)
    ```

    !!! warning "Warning"
        - Các biến môi trường được cài đặt qua `export` khá an toàn, chỉ làm việc trong phiên làm việc _(terminal)_.
        - Thoát khỏi phiên các biến môi trường sẽ về như cũ và lần khác lại cần tái kích hoạt.
        - Phương pháp này tốt cho nhiều dự án khi có thể yêu cầu cấu hình từ đầu và rõ ràng lý do cấu hình cho từng dự án.

## Sửa Lỗi

!!! failure "Could not find a package configuration file provided by \"Qt6\" with any of the following names:"
    Nếu bạn gặp lỗi như thế này:

    ```text
    CMake Error at CMakeLists.txt:9 (find_package):
    By not providing "FindQt6.cmake" in CMAKE_MODULE_PATH this project has
    asked CMake to find a package configuration file provided by "Qt6", but
    CMake did not find one.

    Could not find a package configuration file provided by "Qt6" with any of
    the following names:

        Qt6Config.cmake  
        qt6-config.cmake

    Add the installation prefix of "Qt6" to CMAKE_PREFIX_PATH or set "Qt6_DIR"
    to a directory containing one of the above files.  If "Qt6" provides a
    separate development package or SDK, be sure it has been installed.
    ```

    Thì phải kiểm tra lại xem cấu hình môi trường ở `-DCMAKE_PREFIX_PATH` hoặc đường dẫn đúng chưa.

## Tham Khảo

### Phiên Bản Qt

etc.
