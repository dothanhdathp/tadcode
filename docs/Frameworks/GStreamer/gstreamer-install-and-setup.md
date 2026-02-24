# Installing GStreamer

> [Trang chủ hướng dẫn tải __*GStreamer*__](https://gstreamer.freedesktop.org/documentation/installing/index.html)

Các Hệ Điều Hành Hỗ Trợ Là

- [Windows](#windows)
- [Linux](#linux)
- iOS
- Mac OS
- Android

## Windows

- [Đưởng dẫn tải về cho Windows](https://gstreamer.freedesktop.org/download/#windows)

- Hoặc có thể tải xuống trực tiếp bản cài đặt ở đây: 
    - [gstreamer-1.0-msvc-x86_64-1.26.5.msi](https://gstreamer.freedesktop.org/data/pkg/windows/1.26.5/msvc/gstreamer-1.0-msvc-x86_64-1.26.5.msi)

## Linux

!!! quote "Note"
    __GStreamer__ được tích hợp sẵn trong tất cả các bản phân phối Linux. Chúng tôi khuyên bạn nên sử dụng phiên bản mới nhất của một bản phân phối có tốc độ phát triển nhanh như __Fedora__, __Ubuntu__ _(không phải LTS)_, __Debian__ sid hoặc __OpenSuse__ để nhận bản phát hành __GStreamer__ mới nhất.

=== "Ubuntu/Debian"
    ```bash
    sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y
    ```

=== "Fedora"
    ```bash
    dnf install gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-doc gstreamer1-plugins-base-devel \
    gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly gstreamer1-plugins-bad-free \
    gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras
    ```

## Mac OS X

_Không có thiết bị nên làm sau_

## Android

Tải về __*tarball*__ của GStream và giải nén __*(trên các máy Linux)*__.

Xem phiên bản ổn định trên [trang chủ của gstreamer](https://gstreamer.freedesktop.org/download/#android) và tải về gỏi __*tar-ball*__. Sau đó giải nén là đã có thể sử dụng.

Theo dõi [hướng dẫn cho Android](gstreamer-android-tutorial-1.md) để biết rõ các bước.

Các phiên bản khác có thể xem ở [_đường dẫn_](https://gstreamer.freedesktop.org/data/pkg/android/). Vào thư mục và tải về tệp `gstreamer-1.0-android-universal-1.xx.x.tar.xz` tương ứng.

Nên tải về cái phiên bản ổn định _(stable)_, tránh những phiên bản đang phát triển:

- [Bản 1.28.0.tar.xz](https://gstreamer.freedesktop.org/data/pkg/android/1.28.0/gstreamer-1.0-android-universal-1.28.0.tar.xz)
- [Bản 1.26.10.tar.xz](https://gstreamer.freedesktop.org/data/pkg/android/1.26.10/gstreamer-1.0-android-universal-1.26.10.tar.xz)

Hai tệp còn lại mình không rõ, có lẽ để `checksum`, dùng để kiểm tra xem các tệp nguồn có bị chỉnh sửa gì chưa.