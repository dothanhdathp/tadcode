# C Volatile

Toán tử **volatile** định nghĩa rằng biến này là biến dễ bị sửa đổi và không nằm hoàn toàn trong sự kiểm soát của chương trình. Ví dụ như đối với các hàm ngắt, hàm sửa đổi giá trị trực tiếp trên ram trong các hệ thống nhúng cấp thấp.

Mục đích của nó là tránh trình biên dịch áp dụng các thuật toán tối ưu lệnh nhằm bỏ qua các bước kiểm tra vì các biến này **hầu như sẽ không thay đổi hoặc hoàn toàn không thay đổi** trong phạm vi chương trình gốc.

## Tham Khảo

- [c volatile](https://en.cppreference.com/w/c/language/volatile.html)