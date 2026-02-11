# Chrono library

Thư viện __Chrono__ xử lý các vấn đề liên quan đến thời gian gồm ba dạng đồng hồ chính là:

- __System Clock__: Xử lý thời gian thực, thời gian đồng hồ về các bộ đếm thời gian hiển thị trên máy tính.
- __Steady Clock__: Xử lý thời gian số học liên quan đến bộ đếm máy tính, có bộ đếm lớn và độ chính xác cao. Thường được sử dụng trong các bài làm về thuật toán.
- __File Clock__: Liên quan đến xử lý về các dâu thời gian nằm trên các tệp.

## Time Type

- `std::time_t` là cấu hình chuẩn thời gian theo hệ [POSIX](/OS/os-posix-and-win32/)

