# \[C++\] G++

## Example

```text
g++ main -std=c++11 -O2 -Wall
```

## Tùy Chọn

### Tùy Chọn STD Veriosn

#### Các tiêu chuẩn C++ chính thức (C++ Standard)

Danh sách các cờ -std khả dụng với GNU g++ rất đa dạng, phản ánh lịch sử phát triển của ngôn ngữ từ những ngày đầu cho đến các tiêu chuẩn đang được dự thảo.

Dưới đây là các cờ phổ biến nhất, được chia theo các nhóm tiêu chuẩn:

| Cờ           | Ý Nghĩa                                                                                     |
| :----------- | :------------------------------------------------------------------------------------------ |
| `-std=c++98` | Tiêu chuẩn ISO đầu tiên (bao gồm cả bản sửa đổi 2003).                                      |
| `-std=c++11` | Bước ngoặt lớn của C++ (tên mã cũ là C++0x).                                                |
| `-std=c++14` | Bản cập nhật hoàn thiện cho C++11 (tên mã cũ là C++1y).                                     |
| `-std=c++17` | Tiêu chuẩn năm 2017 (tên mã cũ là C++1z).                                                   |
| `-std=c++20` | Tiêu chuẩn năm 2020 với các tính năng lớn như Concepts, Coroutines (tên mã cũ là C++2a).    |
| `-std=c++23` | Tiêu chuẩn mới nhất hiện tại (tên mã cũ là C++2b).                                          |
| `-std=c++26` | Tiêu chuẩn đang trong quá trình phát triển (yêu cầu các phiên bản g++ rất mới như GCC 14+). |

#### Các biến thể GNU (GNU Extensions)

Các cờ này bao gồm tiêu chuẩn ISO tương ứng cộng với các phần mở rộng riêng của __GCC__ (như kiểu dữ liệu `__int128`, các hàm toán học bổ sung, v.v.).

| Cờ             | Ý Nghĩa                            |
| :------------- | :--------------------------------- |
| `-std=gnu++98` | Cờ biên dịch mở rộng cho `gnu++98` |
| `-std=gnu++11` | Cờ biên dịch mở rộng cho `gnu++11` |
| `-std=gnu++14` | Cờ biên dịch mở rộng cho `gnu++14` |
| `-std=gnu++17` | Cờ biên dịch mở rộng cho `gnu++17` |
| `-std=gnu++20` | Cờ biên dịch mở rộng cho `gnu++20` |
| `-std=gnu++23` | Cờ biên dịch mở rộng cho `gnu++23` |