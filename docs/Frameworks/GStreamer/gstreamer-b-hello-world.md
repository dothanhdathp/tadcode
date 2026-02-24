# Hello world!

## Mục tiêu

- Không gì tốt hơn để có ấn tượng đầu tiên về một thư viện phần mềm hơn là in dòng chữ "Hello World" trên màn hình! Nhưng vì chúng ta đang xử lý các khuôn khổ đa phương tiện nên chúng ta sẽ phát video thay thế.
- Đừng lo lắng về lượng code bên dưới: <mark class=red>chỉ có 4 dòng thực sự hoạt động</mark>. Phần còn lại là code dọn dẹp, và trong C, code này luôn hơi dài dòng.
- Không cần phải nói thêm nữa, hãy sẵn sàng cho ứng dụng GStreamer đầu tiên của bạn...

## Ví dụ

Sau bài trước và chạy thành công thì bài này sẽ bắt đầu ví dụ đầu tiên với __*gstreamer*__ _(mặc dù chưa hiểu gì hết.)_

- Tạo thư mục `1-hello-world` để chạy ví dụ.
- Trong thư mục khởi tạo tệp `main.c`
- Dán nội dung code dưới đây vào

```c title="main.c"
#include <gst/gst.h>

#ifdef __APPLE__
#include <TargetConditionals.h>
#endif

int tutorial_main (int argc, char *argv[]) {
    GstElement *pipeline;
    GstBus *bus;
    GstMessage *msg;

    /* Initialize GStreamer */
    gst_init(&argc, &argv);

    /* Build the pipeline */
    pipeline = gst_parse_launch ("playbin uri=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm", NULL);

    /* Start playing */
    gst_element_set_state (pipeline, GST_STATE_PLAYING);

    /* Wait until error or EOS */
    bus = gst_element_get_bus (pipeline);
    msg = gst_bus_timed_pop_filtered (bus, GST_CLOCK_TIME_NONE, GST_MESSAGE_ERROR | GST_MESSAGE_EOS);

    /* See next tutorial for proper error message handling/parsing */
    if (GST_MESSAGE_TYPE (msg) == GST_MESSAGE_ERROR) {
        g_printerr ("An error occurred! Re-run with the GST_DEBUG=*:WARN environment variable set for more details.\n");
    }

    /* Free resources */
    gst_message_unref (msg);
    gst_object_unref (bus);
    gst_element_set_state (pipeline, GST_STATE_NULL);
    gst_object_unref (pipeline);
    return 0;
}

int main (int argc, char *argv[]) {
#if defined(__APPLE__) && TARGET_OS_MAC && !TARGET_OS_IPHONE
    return gst_macos_main ((GstMainFunc) tutorial_main, argc, argv, NULL);
#else
    return tutorial_main (argc, argv);
#endif
}
```

Sau đó chạy lệnh sau để __build__:

```bash
gcc main.c -o main `pkg-config --cflags --libs gstreamer-1.0`
```

Ta được tệp thực thi tên là `main`, chạy thử chương trình:

```bash
./main
```

Kết quả y hệ code mẫu đầu tiên `basic-tutorial-1`

- Chương trình ví dụ này sẽ mở một cửa sổ và hiển thị một bộ phim, kèm theo âm thanh.
- Nội dung được __tải từ Internet__, vì vậy cửa sổ có thể mất vài giây để xuất hiện, tùy thuộc vào tốc độ kết nối của bạn.
- Ngoài ra, <mark class=red>không có tính năng quản lý độ trễ (đệm), vì vậy trên các kết nối chậm, bộ phim có thể dừng phát sau vài giây</mark>.

## Phân tích

### Thư viện

Ngay dòng đầu tiên bắt buộc phải thêm vào thư viện `<gst/gst.h>`

```c
#include <gst/gst.h>
```

### gst_init

```c
/* Initialize GStreamer */
gst_init(&argc, &argv);
```

- Đây luôn là lệnh __*GStreamer*__ đầu tiên, nó sẽ thực hiện:
    - Khởi tạo tất cả các cấu trúc bên trong
    - Kiểm tra các __plug-in__ có sẵn
    - Thực hiện bất kỳ tùy chọn dòng lệnh nào dành cho __*GStreamer*__

### Xây dựng pipeline

Dòng này được sử dụng để xây dựng __*pipeline*__

```c
/* Build the pipeline */
pipeline = gst_parse_launch("playbin uri=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm", NULL);
```

Dòng đó tương đương với lệnh gọi __*command-line*__ như sau:

```bash
gst-launch-1.0 playbin uri=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm
```

!!! abstract "Abstract"
    Liệu `gst_parse_launch()` có phải chạy đến `gst-launch-1.0` không?

### playbin

Vậy, pipeline nào? Điểm mấu chốt ở đây: Chúng ta đang xây dựng một pipeline bao gồm một phần tử duy nhất gọi là `playbin`.

__Playbin__ là một thành phần đặc biệt, vừa đóng vai trò là nguồn phát, vừa là bồn chứa, và là một đường ống hoàn chỉnh. Về mặt nội bộ, nó tạo ra và kết nối tất cả các thành phần cần thiết để phát nội dung đa phương tiện của bạn, vì vậy không cần phải lo lắng về điều đó.

<mark class=red>Nó không cho phép kiểm soát chi tiết như đường ống thủ công, nhưng vẫn cho phép tùy chỉnh</mark> đủ để đáp ứng nhiều ứng dụng khác nhau.

Trong ví dụ này, chúng ta chỉ truyền một tham số cho playbin , đó là URI của phương tiện chúng ta muốn phát. Hãy thử thay đổi nó thành một tham số khác! Cho dù đó là URI `http://` hay `file://` __URI__, playbin sẽ khởi tạo nguồn GStreamer phù hợp một cách minh bạch!

