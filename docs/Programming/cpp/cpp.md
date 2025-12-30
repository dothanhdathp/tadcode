# \[C++\] Overview

Tìm cách đặt tên các cấp bậc Basic, Begin, ... mệt vl nên đổi cấp bậc này xài cho dễ hiểu

- Nhập Môn
- Luyện Khí
- Trúc Cơ
- Kim Đan
- Nguyên Anh
- Hóa Thần

```puml
@startwbs
* Road Map C++

** Nhập Môn
***_ What is C++
***_ Why C++
***_ C++ vs C
***_ Cài Đặt Môi Trường
***_ Editor
***_ Hello World

** Luyện Khí
*** Biến
****_ Biến nguyên thủy
****_ enum
****_ Con trỏ
**** Tập Hợp
*****_ array
*****_ struct
*****_ union
***_ Operator
****_ Math
****_ Bit
***_ Điều khiển luồng
*** Hàm
****_ main
****_ hàm chức năng
*** Thư viện STD
***_:=== Khái niệm về thùng chứa
 Linked List
 Stack, Queue
;
***_:=== Chuỗi
 std::string
;
***_:=== Class
 OOP
 Class
 Access Specifiers
;

** Trúc Cơ
*** Smart Pointer
****_ Raw Pointer
****_:== Smart Pointer
 - std::weak_ptr
 - std::shared_ptr
 - std::unique_ptr
;
*** STD Container
****_:== sequence
  **std::array**
  **std::vector**
  **std::list**
  **std::deque**
;
****_:== associative
  **std::set**
  **std::map**
  std::multiset
  std::multimap
;
****_:== u_associative
  **std::unordered_set**
  **std::unordered_map**
  std::unordered_multiset
  std::unordered_multimap
;
****_:== adaptors
  **std::stack**
  **std::queue**
  std::priority_queue
  std::flat_set
  std::flat_map
  std::flat_multiset
  std::flat_multimap
;
*** Pre Processing
****_ Define
****_ Namespace
***_ Thread
****_ std::thread
*****_ std::jthread
****_ std::mutex
****_ std::coroutine
*** Function
****_ Lambda Function
****_ Function as Parameter
****_ Function Pointer

** Kim Đan
*+*_ Template
*+*_ System
**+*_ IO


@endwbs
```

<!--
[[/Programming/cpp/cpp-linear-types/ std::linear Types]]
-->niệm