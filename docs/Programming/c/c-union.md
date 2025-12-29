# \[C\] Union

__Union__ là dạng một vùng nhớ nhiều kiểu dữ liệu.

Tuy được khai báo giống __*struct*__, nhưng __*union*__ thì không mở rộng thêm phân vùng bộ nhớ nó sử dụng chung một bộ nhớ cho nhiều kiểu dữ liệu.

Độ lớn của vùng này là độ lớn của phần tử lớn nhất.

```c
#include "stdio.h"

union ascii {
    int  as_int;
    char as_char;
};

int main(int argc, char const *argv[])
{
    union ascii u1;
    u1.as_int = 97;
    union ascii u2;
    u2.as_int = 98;
    printf("[U1] %d = %c\n", u1.as_int, u1.as_char);
    printf("[U2] %d = %c\n", u2.as_int, u2.as_char);
    return 0;
}
```

Ứng dụng của Union được dùng nhiều nhất là trong ép kiểu trong truyền nhận thông tin. Kỹ thuật đó tên là __*serialize*__

```c
struct pointer
{
    int x;
    int y;
    int z;
};

union rectagle {
    struct pointer[4];
    char   data[12*4];
};
```