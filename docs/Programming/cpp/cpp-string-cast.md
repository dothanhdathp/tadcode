# String Cast
> Chuyển đổi string thành các dạng khác nhau và ngược lại

## Cast To String

Hầu hết mọi dữ liệu nguyên thủy đều có thể chuyển đổi thành string bằng hàm `std::to_string()` _(cần thư viện `<string>`)_

```cpp
#include <iostream>
#include <string>

int main() {
    int i = 23242;
    char c = 'g';
    float f = 1.24161;
    double d = 1321.563241;

    std::cout << std::to_string(i) << std::endl;
    std::cout << std::to_string(c) << std::endl;
    std::cout << std::to_string(f) << std::endl;
    std::cout << std::to_string(d) << std::endl;
    return 0;
}
```
```text title="Kết Quả"
23242
103
1.241610
1321.563241
```

## Cast From String

Khi chuyển từ chuỗi thành một giá trị, sẽ có nhiều trường hợp chuyển đổi thất bại. Khi đó hàm sẽ trả về _exeption_ 

- `std::invalid_argument` nếu không thể thực hiện chuyển đổi.
- `std::out_of_range` nếu giá trị được chuyển đổi sẽ giảm

### Các Hàm Chuyển Đổi

| Function   | From String To | Version |
| :--------- | :------------- | :------ |
| std::stoi  | int            |         |
| std::stoul | unsigned int   |         |
| std::stol  | long           |         |
| std::stoll | long long      |         |
| std::stof  | float          |         |
| std::stod  | double         |         |
| std::stold | long double    |         |
|            |                |         |

### Trường Hợp Thành Công

```cpp
#include <iostream>
#include <string>

int main() {
    std::string i = "23242";
    std::string f = "1.24161";
    std::string d = "1321.563241";

    std::cout << std::stoi(i) << std::endl;
    std::cout << std::stof(f) << std::endl;
    std::cout << std::stod(d) << std::endl;
    return 0;
}
```

### Trường Hợp Thất Bại

```cpp title="std::invalid_argument"
std::string str = "*&#$@^";
std::cout << std::stoi(str) << std::endl;
```
```text title="Kết Quả"
terminate called after throwing an instance of 'std::invalid_argument'
  what():  stoi
```

```cpp title="std::out_of_range"
std::string str = "4000000000";
std::cout << std::stoi(str) << std::endl;
```
```text title="Kết Quả"
terminate called after throwing an instance of 'std::out_of_range'
  what():  stoi
```

## Xử Lý 