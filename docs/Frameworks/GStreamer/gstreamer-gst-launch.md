# gst-launch-1.0

[gst-launch-1.0](https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html) là một công cụ xây dựng và chạy các đường dẫn GStreamer cơ bản.

## Công Thức

```bash
gst-launch-1.0 [OPTIONS] [PIPELINE-DESCRIPTION]
```

## Mô Tả

`gst-launch-1.0` là một công cụ xây dựng và chạy các đường dẫn GStreamer cơ bản.

Ở dạng đơn giản nhất, __PIPELINE-DESCRIPTION__ là danh sách các phần tử được phân tách bằng dấu chấm than (`!`). Các thuộc tính có thể được thêm vào các phần tử ở dạng `property=value`. Bạn cũng có thể đặt "đặt trước" bằng cú pháp `@preset=<preset name>`.

!!! note "Note"
    Xin lưu ý rằng `gst-launch-1.0` __*chủ yếu là một công cụ gỡ lỗi. Bạn không nên xây dựng các ứng dụng trên đó*__. Đối với các ứng dụng, hãy viết một tập lệnh python nhỏ hoặc ứng dụng Rust (hoặc sử dụng bất kỳ ngôn ngữ lập trình nào khác mà bạn thích) và sử dụng hàm `gst_parse_launch()` của __*API GStreamer*__ như một cách dễ dàng để xây dựng quy trình từ mô tả quy trình

## Tùy chọn (Options)

- `--help`: In bản tóm tắt trợ giúp và có sẵn __FLAGS__
- `-v`, `--verbose`: Thông tin trạng thái đầu ra và thông báo thuộc tính
- `-q`, `--quiet`: Không in bất kỳ thông tin tiến độ nào
- `-m`, `--messages`: Thông báo đầu ra được đăng trên __*pipeline's bus*__
- `-t`, `--tags`: Output tags _(còn được gọi là _*metadata*_)_
- `-e`, `--eos-on-shutdown`: Buộc một sự kiện EOS trên các nguồn trước khi tắt đường dẫn. Điều này rất hữu ích để đảm bảo các bộ chuyển đổi tạo các tệp có thể đọc được khi đường dẫn chuyển đổi bị tắt mạnh thông qua __Control-C__ (đặc biệt trong trường hợp `mp4mux` và `qtmux` trong đó tệp đã tạo sẽ không thể đọc được nếu tệp chưa được hoàn thiện đúng cách).
- `-f`, `--no_fault`: Không cài đặt trình xử lý segfault
- `--no-position`: Không in vị trí hiện tại của đường ống.<br>Nếu tùy chọn này không được chỉ định, vị trí sẽ được in khi thiết bị xuất chuẩn là TTY. Để bật vị trí in khi thiết bị xuất chuẩn không phải là TTY, hãy sử dụng tùy chọn `--force-position`.
- `--force-position`: Cho phép in vị trí hiện tại của đường ống ngay cả khi thiết bị xuất chuẩn không phải là TTY. <u>Tùy chọn này không có hiệu lực nếu tùy chọn `--no-position` được chỉ định.</u>

## GStreamer tùy chọn

`gst-launch-1.0` cũng chấp nhận các tùy chọn chung sau cho tất cả ứng dụng GStreamer:

- `--gst-version`: In chuỗi phiên bản của thư viện lõi GStreamer.
- `--gst-fatal-warnings`: Khiến GStreamer hủy bỏ nếu xuất hiện thông báo cảnh báo. Điều này tương đương với việc đặt biến môi trường G_DEBUG=fatal_warnings (xem phần biến môi trường bên dưới để biết thêm thông tin).

