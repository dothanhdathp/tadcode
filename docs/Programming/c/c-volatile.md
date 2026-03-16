# C Volatile

## Định Nghĩa

Toán tử **volatile** định nghĩa rằng biến này là biến dễ bị sửa đổi và không nằm hoàn toàn trong sự kiểm soát của chương trình. Ví dụ như đối với các hàm ngắt, hàm sửa đổi giá trị trực tiếp trên ram trong các hệ thống nhúng cấp thấp.

Mục đích của nó là tránh trình biên dịch áp dụng các thuật toán tối ưu lệnh nhằm bỏ qua các bước kiểm tra vì các biến này **hầu như sẽ không thay đổi hoặc hoàn toàn không thay đổi** trong phạm vi chương trình gốc.

## Chức Năng

1. [static](c-static.md) volatile mô hình đối tượng **memory-mapped I/O ports**, và `static const volatile` mô hình hóa đối tượng của **memory-mapped input ports**, như là _**real-time clock**_:
2) _**static volatile**_ các đối tượng thuộc loại **sig_atomic_t** được sử dụng để liên lạc với bộ xử lý tín hiệu.
3) Các biến loại `volatile` được đặt trong các hàm cái mà chứa các hàm gọi tới các hàm **setjmp macro** là các biến cục bộ duy nhất được đảm bảo giữ lại giá trị của chúng sau khi `longjmp` trả về.
4) In addition, volatile variables can be used to disable certain forms of optimization, e.g. to disable dead store elimination or constant folding for micro-benchmarks. _(Ngoài ra, các biến **volatile** có thể được sử dụng để vô hiệu hóa một số hình thức tối ưu hóa nhất định, ví dụ: để vô hiệu hóa việc loại bỏ cửa hàng chết hoặc gấp liên tục đối với các điểm chuẩn vi mô. ??)_

Lưu ý rằng <mark>các biến **volatile** không phù hợp để liên lạc giữa các luồng; chúng không cung cấp tính nguyên tử, đồng bộ hóa hoặc sắp xếp bộ nhớ.</mark> Việc đọc từ một biến dễ thay đổi được sửa đổi bởi một luồng khác mà không đồng bộ hóa hoặc sửa đổi đồng thời từ hai luồng không đồng bộ là hành vi không xác định do cuộc đua dữ liệu.

## Tham Khảo

- Bài viết này tham khảo từ [C volatile](https://en.cppreference.com/w/c/language/volatile.html)