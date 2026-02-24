# Gstreamer Graphs

Vẽ biểu đồi `pipeline` của __*GStreamer*__ bằng công cụ

Tham khảo  chương trình trong đường đẫn sau [generating-gstreamer-pipeline-graphs/](https://embeddedartistry.com/blog/2018/02/22/generating-gstreamer-pipeline-graphs/)

## Tải về công cụ

Đầu tiên cần tải về công cụ vẽ:

=== "Ubuntu/Linux"
    ```bash
    sudo apt-get install graphviz
    ```
=== "OSX"
    ```bash
    brew install graphviz
    ```

!!! warning "Lưu ý"
    - Mặc dù gói phần mềm tên `graphviz` là nhưng câu lệnh của nó gọi là `dot`
    - Tham khảo về phần mềm tại [graphviz.org](https://graphviz.org/about/)

## Cài đặt biến môi trường

### Cài đặt bằng dòng lệnh

Mặc định của __*gstreamer*__ sử dụng biến môi trường `GST_DEBUG_DUMP_DOT_DIR` làm địa chỉ debug đầu ra, để cài đặt biến môi trường này đơn giản dùng lệnh __*export*__:

=== "Ubuntu/Linux"
    ```bash
    export GST_DEBUG_DUMP_DOT_DIR=/tmp/
    ```
=== "Android"
    ```bash
    export GST_DEBUG_DUMP_DOT_DIR=/data/local/tmp/
    ```

### Cài đặt trong ứng dụng

Tham khảo hướng dẫn từ tài liệu gốc về hai marco:

- [GST_DEBUG_BIN_TO_DOT_FILE](https://gstreamer.freedesktop.org/documentation/gstreamer/debugutils.html?gi-language=c#GST_DEBUG_BIN_TO_DOT_FILE)
- [GST_DEBUG_BIN_TO_DOT_FILE_WITH_TS](https://gstreamer.freedesktop.org/documentation/gstreamer/debugutils.html?gi-language=c#GST_DEBUG_BIN_TO_DOT_FILE_WITH_TS)

Hai lệnh đó về cơ bản là __wrap__ lại hai lệnh __*gst_debug_bin_to_dot_file(...)*__ và __*gst_debug_bin_to_dot_file_with_ts(...)*__. Có lẽ việc in đậm lên như thế là để gây chú ý hơn về các câu lệnh / cài đặt khởi tạo thôi.

## Đầu ra đồ thị đường ống

Sau các bước trên thì hãy thử chạy bất kỳ một ứng dụng __*gstreamer*__ nào đó, hoặc không trở lại hướng dẫn [Hello World!](gstreamer-b-hello-world.md) và chạy thử.

Sau khi chạy thì tại thư mục được cài đặt tại biến môi trường `GST_DEBUG_DUMP_DOT_DIR` sẽ xuất hiện các tệp `*.dot` vẽ đồ thị các luồng hoạt động của __*gstreamer*__

## Chuyển đổi

Có thể dùng lệnh sau để chuyển đổi toàn bộ tệp `.dot` sang tệp nào đó như:

=== "PNG"
    ```bash
    for i in $(find -name "*.dot"); do dot -Tpng $i > ${i:2:-4}.png; done;
    ```
=== "PDF"
    ```bash
    for i in $(find -name "*.dot"); do dot -Tpng $i > ${i:2:-4}.pdf; done;
    ```
=== "BMP"
    ```bash
    for i in $(find -name "*.dot"); do dot -Tpng $i > ${i:2:-4}.bmp; done;
    ```
=== "SVG"
    ```bash
    for i in $(find -name "*.dot"); do dot -Tpng $i > ${i:2:-4}.svg; done;
    ```
