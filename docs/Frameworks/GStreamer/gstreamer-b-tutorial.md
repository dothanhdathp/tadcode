# GStreamer Tutorial

Tải về và chạy thử ví dụ

## Preset

__*Development Environment*__ duy nhất cần thiết là trình biên dịch `gcc` và trình soạn thảo văn bản. Để biên dịch mã yêu cầu _GStreamer_ và sử dụng thư viện lõi _GStreamer_, hãy nhớ thêm chuỗi này vào lệnh `gcc` của bạn:

```txt
pkg-config --cflags --libs gstreamer-1.0
```

- Nếu bạn đang sử dụng các thư viện GStreamer khác, ví dụ như thư viện __*video*__, bạn phải thêm các gói bổ sung sau `gstreamer-1.0` trong chuỗi trên _(ví dụ: `gstreamer-video-1.0` cho thư viện video)_.

- Nếu ứng dụng của bạn được xây dựng với sự trợ giúp của `libtool`, ví dụ khi sử dụng `automake/autoconf` làm hệ thống xây dựng, bạn phải chạy tệp lệnh `configure` từ bên trong môi trường `gst-sdk-shell`.

!!! abstract "Bình luận"
    Mình không biết cái này có cần thiết hay không luôn.

## Tutorial

Tải về mã nguồn từ đường dẫn sau

```bash
git clone https://gitlab.freedesktop.org/gstreamer/gstreamer
```

Bên trong đó có rất nhiều thư mục, sẽ nghiên cứu dần, trước tiên hãy thử vào đường dẫn sau:

```bash
cd gstreamer/subprojects/gst-docs/examples/tutorials/
```

Và `build` ứng dụng

```bash
gcc basic-tutorial-1.c -o basic-tutorial-1 `pkg-config --cflags --libs gstreamer-1.0`
```

Cuối cùng là chạy:

```bash
./basic-tutorial-1
```

!!! warning "Warning"
    - Không được chạy qua `ssh` vì nó sẽ gặp vấn đề với đầu ra của __*video*__.
    - Ví dụ sẽ khởi chạy ra một cửu sổ khác và __*video*__ được trình diễn trên đó.
    - Về code mẫu, tham khảo để sau.

## Lược qua hai loại hướng dẫn

Chia làm hai phần riêng biệt, gstreamer cung cấp hai loại 