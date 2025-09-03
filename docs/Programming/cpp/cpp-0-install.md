# Tải về và cài đặt

## Cài đặt cho Windows

Cho Windows có nhiều cách để sử dụng như tải về và công cụ sẵn có như:
- [Code::Blocks](https://www.codeblocks.org/)
- [Dev-C++](https://www.bloodshed.net/), ...

Nhưng tôi nghĩ tốt nhất nên dùng `msys2` vì nó có vẻ được khuyến nghị bởi [Visual Studio Code](../../Software/VSCode/software-vscode-install.md).

1. Tải msys và cài đặt từ trang chủ [MSYS2](https://www.msys2.org/)
1. Sau đó tải [VSCode](../../Software/VSCode/software-vscode-install.md) để code C++
1. Theo hướng dẫn trong này [Using GCC with MinGW](https://code.visualstudio.com/docs/cpp/config-mingw) để tải về 
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

## Cài đặt cho Linux/Ubuntu

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
## Cài đặt cho IOS

_Chưa có tiền mua máy Mac_