# Function As Parameter

## Sử dụng hàm như là biến đầu vào

- Tương đương với lamda và có thể dùng hàm như biến truyền đầu vào (gần giống hàm `std::sort`).
- Đây là một ý tưởng khá thú vị. Trong một số trường hợp, biến truyền đầu vào sẽ không nằm trong một số kiểu biến cơ bản hoặc là chúng sẽ cần __điều kiện__ gì đó thêm để thay đổi nội dung logic bên trong. Ví dụ như:
    - `1.1` và `1.11`, nếu hiểu là số thì `1.11` > `1.1` nhưng xếp hạng theo dạng chuỗi (string) thì `1.11` < `1.1` vì `1.1` ngắn và tổng quát hơn.
- Dạng điều kiện này cần thiết và được ưa chuộng gần giống như `lambda` vì tính tiện lợi, nhiều phần logic nhỏ không cần thiết phải tạo hàm ra ngoài nhưng vẫn có thể thay đổi / sửa đổi tử ngoài như một tham số có thể truyền vào.

### Thư viện cần thiết

- `#include <functional>`

### Ví dụ

```cpp
#include <cstdlib>
#include <iostream>
#include <functional>

void test_functional(int x, int y, std::function<bool(int)> fn = nullptr) {
    if(fn==nullptr)
        return;
    if(fn(x) && fn(y)) {
        printf("both x & y is valid!\n");
    } else if(fn(x)) {
        printf("x valid!\n");
    } else {
        printf("y valid!\n");
    }
    return;
}

bool functional(int x) {
    return x > 10;
}

int main() {
    int a = 10;
    int b = 20;
    test_functional(a, b, functional); // y valid!
    test_functional(a, b, [](int x) {return x > 4;}); // both x & y is valid!
    return 0;
}
```

- `functional` là một hàm, và nó cũng được truyền vào như một biến, nó giúp hàm `test_functional` có thể linh hoạt xử lý hơn với hai biến đầu vào ví dụ như a và b trong việc xử lý logic nội hàm.
- Cách thứ hai được viết bên dưới là một kiểu viết bằng lambda thuần túy.