# Build System

## Build System

Nói về hệ thống xây dựng, có nhiều cái tên tiếng anh nhưng thôi ở đây mình xài tiếng Việt thôi vì nó chẳng quan trọng đâu. Nhưng nhìn chung câu chuyện là thế này.

Để xây dựng nên một chương trình máy tính 

Giải thích cụ thể hơn như sau:

- Để __*mã nguồn*__ thành được __*chương trình*__, cần sử dụng các công cụ xây dựng

- Mục đích công cụ __*siêu xây dựng*__ là dựa trên các tệp __*siêu xây dựng*__ để tạo các __*tệp xây dựng*__ _(Build Tools)_ như `gcc`, `g++` của __GNU__/__Clang__, `rustc` cho __Rust__ hay `javac` cho __Java__, ...
- Các công cụ xây dựng yêu cầu rất nhiều đối số để hoạt động. Chẳng hạn như các cờ quy định về 