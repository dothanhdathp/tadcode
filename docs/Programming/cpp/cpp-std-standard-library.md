# Standard Library

## Định Nghĩa

Như tên gọi __*(thư viện cơ bản)*__

Thư viện cơ bản của mọi loại ngôn ngữ đều chung một mục đích, cung cấp những công cụ cơ bản, trực quan nhất cho lập trình viên thao tác và đồng nhất trên mọi hệ thống lập trình.

Các thư viện cơ bản này thường sẽ cung cấp nhiều các công cụ chung, phổ biến trong giới lập trình ví dụ như các thao tác tìm kiếm, sắp xếp, xử lý với tệp, ... Tùy thuộc vào loại ngôn ngữ mà thư viện này sẽ có các chức năng khác nhau.

Lớp thư viện này thường được tối ưu rất tốt, có hiệu năng siêu cao. Đây là bộ công cụ cơ bản nhất cho lập trình viên, bắt buộc phải thành thạo.

## Phân Loại

Thư viện cơ sở chia làm bốn phần chính:

1. [⚙️ Iterator](cpp-std-iterator.md): Lớp cầu nối, lớp này chứa lõi như các kiến trúc xử lý chung, phần sụn cho lớn [⚙️ Container](cpp-std-container.md). Hầu như bình thường không dùng trừ khi cần can thiệp sâu vào cấu trúc dữ liệu trên thư viện của **C++**
1. [⚙️ Utility](cpp-std-utility.md): Lớp này chứa các công cụ trung gian như **std::reverser** dùng để xoay ngược lại một chuỗi, hoặc là **std::hash** để băm dữ liệu ...
1. [⚙️ Container](cpp-std-container.md): Phần này gồm các cấu trúc dữ liệu chung, những cấu trúc dữ liệu thường dùng trong các giải thuật sẽ được khai báo ở đây.
1. [⚙️ Algorithms](cpp-std-algorithms.md): Lớp này chứa các hàm giải thuật mạnh mẽ như sắp xếp, phân phối cây nhị phân, ...