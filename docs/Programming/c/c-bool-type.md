# \[C\] Boolean

Dạng `bool` không có sẵn, nó được định nghĩa trong thư viện __stdbool.h__. Về cơ bản nó vẫn theo _logic_ cũ xử lý __*if/else*__ case. Sai với không và đúng với các trường hợp còn lại. Nó được định nghĩa như sau:

```c
#define true 1
#define false 0
```

Ví dụ dùng như này.

```c
#include <stdio.h>
#include <stdbool.h>

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);

int main() {
    bool t_value = true;
    bool f_value = false;

    if(t_value == 1) println("True Case");
    if(f_value == 0) println("False Case");
    return 0;
}
```