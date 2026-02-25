# Casting

__Fundamental Cast__ nói về các chuyển đổi kiểu giữa các loại cơ bản.

Nhìn chung thì nó là các phương thức chuyển đổi kiểu theo phong cách C. Khi chuyển đổi các phương thức cơ bản này chủ yếu cần xem xét đến kích thước của kiểu biến.

Kích thước biến cần nhớ xem bài [(C++) Numeric Limits](cpp-std-numeric-limits.md).

Kích thước biến cơ bản chỉ có các kích thước chính là `1 bytes`, `2 bytes`, `4 bytes` và `8 bytes`. Theo đó có hai cách chuyển đổi cơ bản được gọi chung là down casting và up casting

## STD Casting

Thư viện cơ bản hỗ trợ nhiều phương thức chuyển đổi khác an toàn hơn.

1. [Static Cast](cpp-static_cast.md)
1. [Const Cast](cpp-const_cast.md)
1. [Dynamic Cast](cpp-dynamic_cast.md)
1. [Reinterpret Cast](cpp-reinterpret_cast.md)