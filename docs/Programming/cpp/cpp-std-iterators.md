# Iterators

__*Iterators*__ là Là "keo dán" giữa các thành phần của [Container](cpp-std-container.md) (std::vector, std::list, ...) với các Algorithms (sort, find).

__*Iterators*__ định hình các cấu trúc dữ liệu theo một kiểu thống nhất giúp các thuật toán xử lý giữa chúng được đồng bộ, tối giản nhất có thể về mặt ngữ nghĩa.

Sau khi đồng nhất, các hàm chức năng, thuật toán sử dụng trên các thùng chứa đều có chung đầu vào và có thể thao tác tương đương. Chẳng hạn như hàm `std::sort` - sắp xếp lại sẽ thực hiện cùng một chức năng trên `std::vector` và `std::list` là như nhau.

std::iterators còn một tính năng ưu việt nữa là tối giản việc chuyển đổi. Chẳng hạn từ các cấu trúc dữ liệu tương đương như `std::vector`, `std::líst` có thể chuyển đổi qua lại với chi phí thấp nhất.

## Con Trỏ Iterator

Hầu hết các cấu trúc dữ liệu trong [STD Container](cpp-std-container.md) đều sẽ có các thành phần sau. Chúng được sinh ra để thống nhất cấu tạo của các thùng chứa, giúp mã hoạt động trơn tru hơn khi bạn muốn đổi một cấu trúc dữ liệu này sang cấu trúc dữ liệu khác.

| Tên       | Ý nghĩa              | Ý nghĩa                                                         |
| :-------- | :------------------- | :-------------------------------------------------------------- |
| begin()   | _begin_              | con trỏ trỏ đến phần tử đầu tiên                                |
| end()     | _end_                | con trỏ trỏ đến vị trí sau phần tử cuối cùng                    |
| rbegin()  | _revert_begin_       | con trỏ trỏ đến vị trí sau phần tử cuối cùng _(ngược)_          |
| rend()    | _revert_end_         | con trỏ trỏ đến phần tử đầu tiên _(ngược)_                      |
| cbegin()  | _const_begin_        | con trỏ __hằng__ trỏ đến phần tử đầu tiên                       |
| cend()    | _const_end_          | con trỏ __hằng__ trỏ đến vị trí sau phần tử cuối cùng           |
| crbegin() | _const_revert_begin_ | con trỏ __hằng__ trỏ đến vị trí sau phần tử cuối cùng _(ngược)_ |
| crend()   | _const_revert_end_   | con trỏ __hằng__ trỏ đến phần tử đầu tiên _(ngược)_             |

Các chức năng không phải lúc nào cũng có, còn phụ thuộc vào:

- bản thân cấu trúc dữ liệu. Ví dụ __*std::initializer_list*__ thì thiếu hết, giữ lạ mỗi __begin()__, __end()__.
- phiên bản GNU bạn đang sử dụng và

## Chức Năng Chung 

### std::distance
> https://en.cppreference.com/w/cpp/iterator/distance.html

Trả về <u>số bước nhảy</u> từ phần tử đầu tiên _(first)_ đến phần tử cuối cùng _(last)_.

```cpp title="Ví Dụ"
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vec = { 1,2,3,4,5,6,7,8,9 };
    std::cout << std::distance(vec.begin(), vec.end()) << std::endl;
    return 0;
}
```

!!! failure "Failure"
    Yêu cầu con trỏ truyền vào thuộc về một cấu trúc dữ liệu thỏa mãn yêu cầu của [LegacyRandomAccessIterator](cpp-named-requirements.md). Nếu không, hành vi sẽ không được xác định vì không thể truy cập phần từ.

### std::advance

```text

```

### std::next

```text

```

### std::move

```text

```

