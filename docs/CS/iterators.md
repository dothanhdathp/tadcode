# Iterators

Trình vòng lặp là một đối tượng cung cấp một cách tiêu chuẩn để truy cập và duyệt qua từng phần tử của vùng chứa hoặc bộ sưu tập (như danh sách hoặc mảng) mà không cần biết cấu trúc bên trong bên dưới của vùng chứa. Nó hoạt động giống như một con trỏ trỏ đến một phần tử tại một thời điểm.

Mẫu thiết kế này tách thuật toán duyệt dữ liệu khỏi chính cấu trúc dữ liệu, cho phép bạn viết các thuật toán chung có thể hoạt động với bất kỳ bộ sưu tập nào cung cấp trình vòng lặp.

## Core concepts

Tách riêng vùng chứa và thuật toán: Trình vòng lặp phân tách cách bạn thực hiện từng bước trong một bộ sưu tập với cách triển khai bộ sưu tập đó. Điều này có nghĩa là bạn có thể sử dụng cùng một vòng lặp for để lặp qua danh sách, mảng hoặc bản đồ băm, bất kể mỗi cấu trúc dữ liệu đó được lưu trữ trong bộ nhớ như thế nào.

Đóng gói logic truyền tải: Bản thân đối tượng iterator giữ trạng thái cần thiết để theo dõi vị trí của nó trong bộ sưu tập. Nhiều trình vòng lặp có thể duyệt cùng một bộ sưu tập một cách đồng thời và độc lập.

Xác định một giao diện: Để một bộ sưu tập có thể "lặp lại được", nó phải cung cấp cách tạo một đối tượng lặp. Bản thân trình lặp phải triển khai một bộ phương thức tiêu chuẩn (thường là next()) để truy xuất phần tử tiếp theo và báo hiệu khi đã đạt đến điểm cuối.

## Iterator vs. iterable

Các thuật ngữ "iterator" và "iterable" có liên quan chặt chẽ nhưng là những khái niệm khác biệt, đặc biệt là trong các ngôn ngữ như Python.
Iterable: Một đối tượng có thể được lặp lại. Nó là nơi chứa dữ liệu mà bạn có thể lấy một trình vòng lặp từ đó. Ví dụ bao gồm danh sách, bộ dữ liệu và chuỗi.

Iterator: Một đối tượng tạo ra mục tiếp theo trong một chuỗi. Nó được tạo từ một iterable và thực hiện công việc lặp lại thực tế.

## Lợi ích của iterators

- __Memory efficiency__: Iteratorscho phép bạn xử lý các bộ sưu tập lớn từng mục một mà không cần tải toàn bộ bộ sưu tập vào bộ nhớ.
- __Abstracts Complexity__: Chúng cung cấp một giao diện đơn giản, nhất quán để duyệt qua một bộ sưu tập, ẩn các cấu trúc dữ liệu cơ bản phức tạp như cây hoặc danh sách được liên kết.
- __Code Reusability__: Các thuật toán chung có thể được viết để chấp nhận bất kỳ loại trình vòng lặp nào, làm cho mã linh hoạt hơn và có thể tái sử dụng với các kiểu và cấu trúc dữ liệu khác nhau.