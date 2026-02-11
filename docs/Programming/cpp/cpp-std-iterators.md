# Iterators

__*Iterators*__ là Là "keo dán" giữa các thành phần của [Container](cpp-std-container.md) (std::vector, std::list, ...) với các Algorithms (sort, find).

__*Iterators*__ định hình các cấu trúc dữ liệu theo một kiểu thống nhất giúp các thuật toán xử lý giữa chúng được đồng bộ, tối giản nhất có thể về mặt ngữ nghĩa.

Sau khi đồng nhất, các hàm chức năng, thuật toán sử dụng trên các thùng chứa đều có chung đầu vào và có thể thao tác tương đương. Chẳng hạn như hàm `std::sort` - sắp xếp lại sẽ thực hiện cùng một chức năng trên `std::vector` và `std::list` là như nhau.

std::iterators còn một tính năng ưu việt nữa là tối giản việc chuyển đổi. Chẳng hạn từ các cấu trúc dữ liệu tương đương như `std::vector`, `std::líst` có thể chuyển đổi qua lại với chi phí thấp nhất.

## 

std::distance
std::advance
std::next
std::move