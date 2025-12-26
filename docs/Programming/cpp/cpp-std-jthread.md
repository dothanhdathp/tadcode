# \[C++\] JThread

> (since C++20) `std::jthread` được phát triển từ sau __C++20__

## Mô Tả

`std::jthread` giống như luồng cũ nhưng nó theo đúng luật an toàn luồng. Các tính năng sau đã được xác thực:

- Luồng sau khi thoát không cần thiết phải __join()__. Nó trở thành chức năng tự động.
    - Nếu hàm main kết thúc khi luồng còn hoạt động, sẽ tự động đợi luồng như khi gọi tới __*join()*__
- Kể cả sau trở thành luồng an toàn, việc __*detach()*__ luồng vẫn cực kỳ nguy hiểm. Hãy cố gắng đảm bảo quy tắc trong luồng __*detach()*__ tất cả các tài nguyên cần phải sao chép, hoạt động duy nhất trên luồng. Không nên __*detach()*__ luồng có chia sẻ chung dữ liệu.

## Thành Viên

### Member types
| Member types       | Definition                      |
| :----------------- | :------------------------------ |
| id                 | std::thread::id                 |
| native_handle_type | std::thread::native_handle_type |