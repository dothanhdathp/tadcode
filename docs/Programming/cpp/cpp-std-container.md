# \[C++\] STD Container

Các __Container__ đại diện cho các thùng chứa, hay dễ hiểu hơn chính là tập hợp của các loại __dữ liệu (biến)__ theo một kiến trúc được đặt tên.

Dưới đây là một số dạng thức của _container_

## Các dạng _container_ cơ bản

Một khái niệm về _container_ phổ biến trong các ngôn ngữ lập trình gồm:

### Sequence containers
> Các container tuần tự

Các thùng chứa trình tự triển khai các cấu trúc dữ liệu có thể được truy cập tuần tự.

| Tên                              | Phiên Bản | Mô Tả                                                            |
| :------------------------------- | :-------: | :--------------------------------------------------------------- |
| [std::vector](cpp-std-vector.md) |           | mảng liền kề có thể thay đổi kích thước                          |
| std::deque                       |           | hàng đợi hai đầu                                                 |
| [std::list](cpp-std-list.md)     |           | danh sách liên kết đôi                                           |
| [std::array](cpp-std-array.md)   |  (C++11)  | mảng liền kề tại chỗ có kích thước cố định                       |
| std::forward_list                |  (C++11)  | danh sách liên kết đơn                                           |
| std::hive                        |  (C++26)  | bộ sưu tập tái sử dụng bộ nhớ của các phần tử đã bị xóa          |
| std::inplace_vector              |  (C++26)  | có thể thay đổi kích thước, dung lượng cố định, đặt mảng liền kề |

### Associative containers
> thùng chứa kết hợp

Các vùng chứa kết hợp triển khai các cấu trúc dữ liệu được sắp xếp có thể tìm kiếm nhanh chóng (độ phức tạp O(log n)).

| Tên                        | Phiên Bản | Mô Tả                                                                  |
| :------------------------- | :-------: | :--------------------------------------------------------------------- |
| [std::set](cpp-std-set.md) |           | bộ sưu tập các khóa độc đáo, được sắp xếp theo khóa                    |
| [std::map](cpp-std-map.md) |           | tập hợp các cặp khóa-giá trị, được sắp xếp theo khóa, khóa là duy nhất |
| std::multiset              |           | tập hợp các phím, được sắp xếp theo phím                               |
| std::multimap              |           | tập hợp các cặp khóa-giá trị, được sắp xếp theo khóa                   |

### Unordered associative containers (since C++11)
> Vùng chứa kết hợp không có thứ tự

Các vùng chứa kết hợp không có thứ tự triển khai các cấu trúc dữ liệu chưa được sắp xếp (băm) có thể được tìm kiếm nhanh chóng ($O(1)$ trung bình, $O(n)$ độ phức tạp trong trường hợp xấu nhất).

| Tên                                       | Phiên Bản | Mô Tả                                                              |
| :---------------------------------------- | :-------: | :----------------------------------------------------------------- |
| [unordered_set](cpp-std-unordered-set.md) |  (C++11)  | tập hợp các khóa duy nhất, được băm theo khóa                      |
| [unordered_map](cpp-std-unordered-map.md) |  (C++11)  | tập hợp các cặp khóa-giá trị, được băm theo khóa, khóa là duy nhất |
| unordered_multiset                        |  (C++11)  | tập hợp các khóa, được băm theo khóa                               |
| unordered_multimap                        |  (C++11)  | tập hợp các cặp khóa-giá trị, được băm theo khóa                   |

### Container adaptors
> Bộ điều hợp container

Bộ điều hợp vùng chứa cung cấp giao diện khác cho vùng chứa tuần tự.

| Tên                            | Phiên Bản | Mô Tả                                                                                                      |
| :----------------------------- | :-------: | :--------------------------------------------------------------------------------------------------------- |
| [std::stack](cpp-std-stack.md) |           | điều chỉnh một thùng chứa để cung cấp ngăn xếp (cấu trúc dữ liệu LIFO)                                     |
| [std::queue](cpp-std-queue.md) |           | điều chỉnh một vùng chứa để cung cấp hàng đợi (cấu trúc dữ liệu FIFO)                                      |
| std::priority_queue            |           | điều chỉnh một container để cung cấp hàng đợi ưu tiên                                                      |
| std::flat_set                  |  (C++23)  | điều chỉnh một vùng chứa để cung cấp một tập hợp các khóa duy nhất, được sắp xếp theo khóa                 |
| std::flat_map                  |  (C++23)  | điều chỉnh hai vùng chứa để cung cấp một tập hợp các cặp khóa-giá trị, được sắp xếp theo các khóa duy nhất |
| std::flat_multiset             |  (C++23)  | điều chỉnh một vùng chứa để cung cấp một tập hợp các khóa, được sắp xếp theo các khóa                      |
| std::flat_multimap             |  (C++23)  | điều chỉnh hai vùng chứa để cung cấp tập hợp các cặp khóa-giá trị, được sắp xếp theo khóa                  |

Một số dạng container cần thoả mãn một số yêu cầu thiết kế trong [Named Requirements](cpp-named-requirements.md#container)

## Tham Khảo

- [Cppreference::Container](https://en.cppreference.com/w/cpp/container.html)