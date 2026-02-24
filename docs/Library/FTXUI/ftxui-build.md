# FTXUI Build Lib

## Mô tả

- __FTXUI__ là viết tắt của __Functional Terminal & User interface__
- __FTXUI__ là thư viện `C++` đa nền tảng _(cross-platform)_ đơn giản cho các giao diện người dùng dựa trên thiết bị đầu cuối!
- Nói đơn giản thư viện này là tạo UI trên console bằng `C++`

## Tài liệu

Tài liệu được viết tại: [https://arthursonzogni.github.io/FTXUI/index.html](https://arthursonzogni.github.io/FTXUI/index.html)

## Install

Sử dụng 

=== "FTXUI"
    ```bash
    git clone --depth=1 https://github.com/ArthurSonzogni/FTXUI.git
    ```
=== "ftxui-starter"
    ```bash
    git clone --depth=1 https://github.com/ArthurSonzogni/ftxui-starter
    ```

- `--depth=1` nên được sử dụng để giảm thiểu dung lượng cần tải về, chỉ lấy source code.

## Build

- Tạo thư mục mới tên là `build` nằm trong `source-code`
- Dùng __Cmake__ để build ứng dụng.
- Giữa các hệ thống khác nhau thì cách dựng cũng có chút khác nhau.

### Build on Linux/Ubuntu

```bash
cd FTXUI
mkdir build
cd build
cmake ../
make all
sudo make install
```

Thường thì có thể _build_ lỗi do thiếu thư viện, có thể tải về bằng các lệnh sau:

```bash
sudo apt install libncurses-dev
```

Kiểm tra lại xem có thư viện chưa thường thì đường dẫn sẽ tại `/usr/lib/x86_64-linux-gnu/libncurses.a`. Trường hợp không chắc chắn có thể tìm bằng command:
```bash
find /usr/ -name libncurses.a
```

### Build on Windows

Trường hợp Windows thì mình chưa rõ cách dựng bằng cmd thế nào. Ở đây mình sẽ xây dựng ứng dụng bằng `msys2`

Đầu tiên có lẽ cần vài tệp phụ thuộc cần thiết để build. Tải về các gói:

```bash
pacman -S mingw-w64-x86_64-gcc
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-make
```

Nếu gặp lỗi hãy tải về gói `toolchain` trước:

```bash
pacman -S mingw-w64-x86_64-toolchain
```

Tải thư viện `ncurses`

```bash
pacman -S mingw-w64-x86_64-ncurses
```

Nếu tải thành công thì thường thư viện sẽ có tại: `/mingw64/lib/libncurses.a`

Chạy `cmake` cài đặt một số cờ:

```bash
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=../install -DDCMAKE_CXX_COMPILER=/mingw64/bin/x86_64-w64-mingw32-g++.exe
```
Run `cmake` for build

```bash
cmake --build . --config Release
cmake --install . --config Release
```

## Output

Trong cả hai trường hợp, kết quả sẽ được ba tệp thư viện:

- `libftxui-component.a`
- `libftxui-dom.a`
- `libftxui-screen.a`