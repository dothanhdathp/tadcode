# Qt Hello World Qml

> Ứng dụng Qt kèm Qml

Từ ví dụ [Hello World](qt-eg-hello-world.md) trước đó, phát triển thêm để sử dụng các tệp mô tả giao diện qml.

## Source

### Cấu Trúc Cây

Cấu trúc thư mục như này

```text
.
├── build.sh
├── CMakeLists.txt
├── main.cpp
├── qml
│   └── main.qml
└── qml.qrc
```

Các tệp bổ sung ở đây là 

- `qml.qrc` dùng để khai báo các tệp tài nguyên.
- `main.qml` là tệp mới để render hình ảnh

### Nội Dung

#### Qml

Qml chỉ là tệp khai báo giao diện đơn giản. Trong đây chứa tệp mô tả màn hình đơn giản.

```cpp title="main.qml"
import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Hello QML"

    Rectangle {
        anchors.fill: parent
        color: "#2c3e50"

        Text {
            anchors.centerIn: parent
            text: "Hello from QML!"
            color: "white"
            font.pixelSize: 24
        }
    }
}
```

#### Qrc

- Tệp này chỉ đơn giản là khai báo các tệp tài nguyên.

```cpp title="qml.qrc"
<RCC>
    <qresource prefix="/">
        <file>qml/main.qml</file>
    </qresource>
</RCC>
```

#### Main

- `main` không còn gọi trực tiếp các đối tượng nữa mà nó sẽ sử dụng **QApplication** và **QQmlApplicationEngine** để tải và tạo giao diện qua các tệp `qml`.
- Nội dung tệp mới như sau:

```cpp title="main.cpp"
#include <QtWidgets/QApplication>
#include <QtQml/QQmlApplicationEngine>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QQmlApplicationEngine engine;
    
    // Nạp file QML từ resource hệ thống (đường dẫn bắt đầu bằng qrc:/)
    const QUrl url("qrc:qml/main.qml");
    
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreated,
        &app,
        [url](QObject *obj, const QUrl &objUrl) {
            if (!obj && url == objUrl)
                QCoreApplication::exit(-1);
        },
        Qt::QueuedConnection
    );
    engine.load(url);

    return app.exec();
}
```

#### CMakeList

Tệp **CMakeList** cũng cần thay đổi một chút. Yêu cầu khai báo thêm các khối mới ở

- `find_package()` 
- `add_executable()`
- `target_link_libraries()`


```cmake title="CMakeList.txt"
cmake_minimum_required(VERSION 3.16)
project(HelloWorld LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON) # Quan trọng để đóng gói file .qml vào binary

# Thêm Quick và Qml vào danh sách tìm kiếm
find_package(Qt6 REQUIRED COMPONENTS Widgets Quick Qml)

add_executable(HelloWorld main.cpp qml.qrc) # Thêm file resource ở đây

target_link_libraries(HelloWorld PRIVATE Qt6::Widgets Qt6::Quick Qt6::Qml)
```