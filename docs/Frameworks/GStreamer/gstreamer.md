# GStreamer

## Chung

- __GStreamer__ là một <u>__*framework*__ để tạo ra các ứng dụng truyền phát đa phương tiện</u>. Các ứng dụng mà nó hỗ trợ trải dài từ __Player__ _(phát lại)_ Ogg/Vorbis đơn giản, phát trực tuyến âm thanh/video đến xử lý âm thanh (mixing) và video (biên tập phi tuyến tính) phức tạp.
- Các ứng dụng có thể tận dụng những tiến bộ trong công nghệ codec và bộ lọc một cách minh bạch. Các nhà phát triển có thể thêm codec và bộ lọc mới bằng cách viết một plugin đơn giản với giao diện gọn gàng, ...
- __GStreamer__ được phát hành theo giấy phép LGPL. Phiên bản 1.x ổn định với API và ABI, thay thế cho phiên bản ổn định trước đó là 0.10. Cả hai đều có thể được cài đặt song song.

## Các Chủ Đề

```puml
@startmindmap
skinparam backgroundcolor transparent
!$URL = "/Frameworks/GStreamer"

* [[$URL/gstreamer GStreamer]]
**_ [[$URL/gstreamer-installing Tải về]]
**_ [[$URL/gstreamer-tools Gst Tools]]
***_ [[$URL/gstreamer-tools gst-launch-1.0]]
***_ [[$URL/gstreamer-tools gst-inspect-1.0]]
***_ [[$URL/gstreamer-tools ges-launch-1.0]]
**_ Khái Niệm
***_ [[$URL/gstreamer-gstreamer-concepts Concepts]]
***_ Elements
****_ Source
*****_ [[$URL/gstreamer-element-video-source Video]]
*****_ [[$URL/gstreamer-tools-stream-video Audio]]
*****_ [[$URL/gstreamer-tools-stream-video Playbin]]
****_ [[$URL/gstreamer-tools-stream-video Test]]
**_ [[$URL/gstreamer-notebook GStreamer Note]]
**_ Basic Tutorials
***_ [[$URL/gstreamer-b-tutorial Tutorial]]
***_ [[$URL/gstreamer-b-hello-world Hello world!]]
***_ [[$URL/gstreamer-b-dynamic-pipelines Đường Ống Động]]
***_ [[$URL/gstreamer-b-pipeline-graphs Pipeline Graphs]]
**_ [[$URL/gstreamer-tools-stream-video Stream Video]]
**_ Pipeline Samples (Self)
***_ [[$URL/gstreamer-pipeline-samples-simple Simple:]]
**_ Pipeline Samples
***_ [[$URL/gstreamer-pipeline-samples Intro:]]
***_ [[$URL/gstreamer-pipeline-samples-tips-for-debug Tips for Debug]]
***_ [[$URL/gstreamer-pipeline-samples-video Video]]
***_ [[$URL/gstreamer-pipeline-samples-audio Audio]]
***_ [[$URL/gstreamer-pipeline-samples-mux-video-and-audio Mux Video and Audio]]
***_ [[$URL/gstreamer-pipeline-samples-media-file Media File]]
***_ [[$URL/gstreamer-pipeline-samples-network-streaming Network Streaming]]
***_ [[$URL/gstreamer-pipeline-samples-mixing Mixing]]
***_ [[$URL/gstreamer-pipeline-samples-shm SHM (Shared Memory)]]
***_ [[$URL/gstreamer-pipeline-samples-fallbacksrc Fallbacksrc]]
***_ [[$URL/gstreamer-pipeline-samples-live-stream Live Stream, ..]]
***_ [[$URL/gstreamer-pipeline-samples-python-opencv Python Opencv]]
**_ Debug
***_ [[$URL/gstreamer-pipeline-graphs Graphs]]
**_ Ubuntu Tutorial
***_ [[$URL/gstreamer-ubuntu-tutorial-1 Tutorial 1]]
**_ Bắt đầu với Windows
***_ [[$URL/gstreamer-windows Geting Start]]
**_ Bắt đầu với Android
***_ [[$URL/gstreamer-android Geting Start]]
***_ [[$URL/gstreamer-android-build-gstreamer Dựng thư viện]]
***_ Android Tutorial
****_ [[$URL/gstreamer-android-tutorial-1 GStreamer 1]]
****_ [[$URL/gstreamer-android-tutorial-2 GStreamer 2]]
****_ [[$URL/gstreamer-android-tutorial-3 GStreamer 3]]
****_ [[$URL/gstreamer-android-tutorial-4 GStreamer 4]]
****_ NamiDtv2Example
*****_ [[$URL/gstreamer-android-nami-dtvbt2-example NamiDtv2Example]]
*****_ [[$URL/gstreamer-android-nami-dtvbt2-example-full-chart Full Chart]]
```

## Tham khảo

- Trang chủ: [https://gstreamer.freedesktop.org/](https://gstreamer.freedesktop.org/)
- Tài liệu API: [https://gstreamer.freedesktop.org/documentation/index.html](https://gstreamer.freedesktop.org/documentation/index.html)

??? note "Blog của NiklasJang"
    - [Blog của NiklasJang](https://niklasjang.github.io/)
    - [__NiklasJang Github__](https://github.com/niklasjang)
    - [Giới thiệu về NNStreamer](https://niklasjang.github.io/nnstreamer/Understanding-NNStreamer/)
    - [Cài đặt Gstreamer và chạy thử nghiệm](https://niklasjang.github.io/nnstreamer/Installing-Gstreamer/#gstreamer-%EC%84%A4%EC%B9%98)
    - [[NNStreamer] Style Transfer pipelie](https://niklasjang.github.io/nnstreamer/Style-Transfer-Pipeline/)
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer 1](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-GStreamer-1/)
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 2](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-GStreamer-2/)
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 3](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-GStreamer-3/)
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 4](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-GStreamer-4/)
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 5](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-GStreamer-5/)
    - _Missing_
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 7](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-Gstreaamer-7/)
    - _Missing_
    - _Missing_
    - [[NNStreamer] Hướng dẫn cơ bản về Gstreamer phần 10](https://niklasjang.github.io/nnstreamer/Basic-Tutorials-For-Gstreamer-10/)

## Ghi chú hôm nay

Có vẻ __*streaming*__ thông qua TCP có hiệu quả cao hơn hẳn so với udp. Đặc điểm là _ít lag_ và _không vỡ hình_.

```bash title="Server"
gst-launch-1.0 videotestsrc ! videoconvert ! x264enc tune=zerolatency ! "video/x-h264,stream-format=byte-stream" ! tcpserversink host=0.0.0.0 port=8000
```
```bash title="Clients"
gst-launch-1.0 tcpclientsrc host=192.168.100.184 port=8000 ! h264parse ! avdec_h264 ! autovideosink
```