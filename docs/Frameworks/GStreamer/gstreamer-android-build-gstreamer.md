# Gstreamer Android Application

__Mục tiêu:__ Tạo ứng dụng chạy trên Android bằng Android Studio

Ở ví dụ này, để đơn giản thì chưa dùng đến __*Surface*__ để xem gì cả, việc đầu tiên chỉ đơn giản là liên kết đến thư viện __*gstreamer*__ và gọi sang các hàm.

## Chú ý

### Yêu cầu về phiên bản

__Bảng này yêu cầu chính xác NDK phân bản nào sẽ được dùng để dựng cho thư viện NDK tương ứng__

| GStreamer version | NDK Version |
| :---------------: | :---------: |
|      1.26.x       |    r25c     |
|      1.24.x       |    r25c     |
|      1.22.x       |     r21     |
|      1.20.x       |     r21     |
|      1.18.x       |     r21     |
|      1.16.x       |    r18b     |

### Yêu cầu về kiến trúc

__Bảng này lại đưa ra yêu cầu về phiên bản API của Android sẽ phù hợp thế nào với thư viện gstreamer__

| Architecture | API Targeted<br>_(GStreamer <= 1.20)_ | API Targeted<br>_(GStreamer >= 1.22)_ |
| :----------: | :-----------------------------------: | :-----------------------------------: |
|    armv7     |           v16 (Jelly Bean)            |            v21 (Lollipop)             |
|     x86      |           v16 (Jelly Bean)            |            v21 (Lollipop)             |
|    arm64     |            v21 (Lollipop)             |            v21 (Lollipop)             |
|    x86_64    |            v21 (Lollipop)             |            v21 (Lollipop)             |