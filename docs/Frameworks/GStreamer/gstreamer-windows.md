# GStreamer Windows

_Hướng dẫn tải về chạy gstreammer trên **Windows**_

## Tải về

- __MSVC 64-bit (VS 2019, Release CRT):__
    - [1.26.5 runtime installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-msvc-x86_64-1.26.5.msi)
    - [1.26.5 development installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-devel-msvc-x86_64-1.26.5.msi)
- __MSVC 32-bit (VS 2019, Release CRT):__
    - [1.26.5 runtime installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-msvc-x86-1.26.5.msi)
    - [1.26.5 development installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-devel-msvc-x86-1.26.5.msi)
- __MinGW 64-bit:__
    - [1.26.5 runtime installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/mingw/gstreamer-1.0-mingw-x86_64-1.26.5.msi)
    - [1.26.5 development installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/mingw/gstreamer-1.0-devel-mingw-x86_64-1.26.5.msi)
- __MinGW 32-bit:__
    - [1.26.5 runtime installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/mingw/gstreamer-1.0-mingw-x86-1.26.5.msi)
    - [1.26.5 development installer](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/mingw/gstreamer-1.0-devel-mingw-x86-1.26.5.msi)

Tải về __MSVC 64-bit (VS 2019, Release CRT)__ _(vì hầu hết máy tính bây giờ là chạy trên hệ thống Win 64-bit)_

Cài đặt xong thì thường sẽ có gói ở đây `%PROGRAMFILES%\gstreamer` và các tệp thực thi nó sẽ nằm ở trong thư mục `gstreamer\1.0\msvc_x86_64\bin`

Nên cài đặt __PATH__ cho `gstreamer\1.0\msvc_x86_64\bin`

Và cuối cùng là kiểm tra với lệnh __gst-launch-1.0__