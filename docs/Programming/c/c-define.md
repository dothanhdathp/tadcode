# Define

- __Define__ là cách định nghĩa lại, hoặc kiểu như tự định danh một biến, hàm, hằng, ... nào đó.
- __Define__ cho phép người lập trình tự lập các công thức hoặc các biểu diễn theo ý cá nhân. Khá là mạnh trong lập trình bậc thấp.
- Về ý nghĩa, __Define__ cũng gần giống với [enum](c-enum.md), tránh cho việc viết tùy ý rườm rà và cung cấp thêm công cụ để dễ sửa đổi.

## Ví Dụ

Đầu tiên cần nói đến tính chất. Về căn bản cái `#define` sẽ <u>thay thế hẳn</u> một đoạn mã của bạn bằng cái đoạn được viết trong **define**:

```cpp
#include "stdio.h"

#define A (1)
#define FILE_PATH ("/usr/bin/temp")

int main() {
    printf("%d\n", A); // == printf("%d\n", 1);
    printf(FILE_PATH); // == printf("/usr/bin/temp");
}
```

Nghĩa là lệnh đó sẽ tìm kiếm và thay thế tất cả các đoạn mà đã được định danh lại để thay đổi. Ở trên là ví dụ đầu tiên về cách định nghĩa lại, nó cho phép thay đổi **FILE_PATH** thành một chuỗi `(const char*)"/usr/bin/temp"`. Chuỗi văn bản đó sẽ được thay thế trực tiếp ở **tất cả mọi nơi trong chương trình**.

Nghĩa là trong tất cả những lần sau, bạn không bao giờ cần thiết phải đi tìm từng đoạn và sửa từng cái **FILE_PATH** nào nữa.

## Định Danh Hàm

Nếu chỉ có vậy thì quá lãng phí. Define còn cho phép định danh hàm. Cái này thường dùng trong định danh cho các hàm in debug. Ví dụ:

```cpp
#include <cstdio>

#define debug(ftm, ...) printf("<%s:%d>  "#ftm"\n", __FUNCTION__, __LINE__, ##__VA_ARGS__);

int main(int argc, const char* args[]) {
    debug("Hello World. Number %d", 5);
    return 0;
}
```
```text title="Kết Quả"
<main:7> "Hello World. Number 5"
```

## println

```cpp
#include "stdio.h"

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);
```

- Tiễn xử lý __*__VA_ARGS__*__
- Cách định nghĩa này tự động thêm `\n` vào cuối chuỗi ký tự.
