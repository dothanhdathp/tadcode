# Cài Đặt

> Cài đặt các công cụ và môi trường cần thiết để lập trình C++

1. [Install for Windows](#install-for-windows)
1. [Install for Linux](#install-for-linux)

## Install for Windows

Cho Windows có nhiều cách để sử dụng như tải về. Một số công cụ sẵn có như:

- [Code::Blocks](https://www.codeblocks.org/)
- [Dev-C++](https://www.bloodshed.net/), ...

### Visual Studio
> [Downloads](https://visualstudio.microsoft.com/downloads/)

__Visual Studio__ Được khuến nghị rộng rãi trên hệ điều hành __Windows__. Công cụ xây dựng `mscv` là công cụ nhanh và mạnh nhất được dùng cho hệ thống này.

### MSYS2

`msys2` được khuyến nghị vì nó có vẻ được khuyến nghị bởi __VSCode__.

1. Tải msys và cài đặt từ trang chủ [MSYS2](https://www.msys2.org/)
1. Sau đó tải __VSCode__ để code C++
1. Theo hướng dẫn trong này [Using GCC with MinGW](https://code.visualstudio.com/docs/cpp/config-mingw) để tải về:
    - Tải về __MSYS2__
    - Dùng câu lệnh sau để tải về __g++ toolchain__:
        ```txt
        pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
        ```
1. Sau khi tải sẽ có:
    - `x86_64-w64-mingw32-g++.exe`
    - `x86_64-w64-mingw32-g++.exe`
    Dùng để build ứng dụng trên Windows.

Để kiểm tra dùng:

```bash
x86_64-w64-mingw32-g++.exe --version
```

Sẽ có kểt quả về phiên bản `g++` đang được dùng.

```bash
x86_64-w64-mingw32-g++ (GCC) 14.2.0
Copyright (C) 2024 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Khi cài đặt thông thường, các phiên bản `g++` sẽ thường nằm ở `C:\msys64\mingw32\bin` hoặc `C:\msys64\mingw64\bin`. Bình thường sẽ không thể dùng trực tiếp, muốn sử dụng trên cmd cần phải thêm đường dẫn vào `PATH`.

## Install for Linux

- Tải về `g++`

```cpp
sudo apt-get update
sudo apt-get install g++
```

- Kiểm tra _binary_

```cpp
$ which c++
/usr/bin/g++
```

- Kiểm tra số hiệu phiên bản

```bash
$ g++ --version
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```