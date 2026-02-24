# std::function<br>Function As Parameter

## Mô Tả

-  Sử dụng hàm như là biến đầu vào
- Thay thế cho tham số đầu vào của một hàm bằng một con trỏ hàm.
- Thư viện: `<functional>`

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