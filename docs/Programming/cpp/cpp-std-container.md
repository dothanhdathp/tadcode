# \[C++\] Container

Các __Container__ đại diện cho các thùng chứa, hay dễ hiểu hơn chính là tập hợp của các loại __dữ liệu (biến)__ theo một kiến trúc được đặt tên.

Dưới đây là một số dạng thức của _container_

## Các dạng _container_ cơ bản

Một khái niệm về _container_ phổ biến trong các ngôn ngữ lập trình gồm:

- __Sequence Container__: Là các dạng danh sách có thứ tự, một số đại diện phổ biến là
    - [Array (Chuỗi)](cpp-array.md): danh sách __tĩnh__. Không có khả năng mở rộng
    - [Vector](cpp-vector.md): Danh sách như Array nhưng cho phép mở rộng ở hai đầu
    - [Vector](cpp-vector.md): Danh sách như Array nhưng cho phép mở rộng ở hai đầu
Associative Containers
- __Vector__ cũng là chuỗi, nhưng nó cho phép thêm phần tử, tự do mở rộng
- Chuỗi là một danh sách __tĩnh__. Tức không thể thêm được phần tử.

Một số dạng container cần thoả mãn một số yêu cầu thiết kế trong [Named Requirements](cpp-named-requirements.md#container)

## 

gltestsrc ! glupload ! tee name=t t. ! queue name=t0 ! glcolorconvert ! glimagesink name="VSYNC_0" t. ! queue name=t1 ! glcolorconvert ! glimagesink name="VSYNC_1" t. ! queue name=t2 ! glcolorconvert ! gldownload ! video/x-raw,format=I420 ! x264enc tune=zerolatency ! rtph264pay ! multiudpsink name="MULTI_UDP_SINK" sync=true async=false androidaudiosrc ! audioconvert ! voaacenc ! rtpmp4gpay ! udpsink host=127.0.0.1 port=5002