# Replacing text macros

> Nguồn: [https://en.cppreference.com/w/c/preprocessor/replace.html](https://en.cppreference.com/w/c/preprocessor/replace.html)

## Định Nghĩa

- [Bộ tiền xử lý](c-preprocessor.md) sẽ thực thi các câu lệnh này trước để __*xác định một số định mới*__ do người dùng cài đặt. Các định danh này về cơ bản là các đoạn xử lý đơn giản thay cho các hàm, hoặc chỉ đơn giản là đổi tên một thành phần để làm rõ ngữ nghĩa.
- Định danh được khai báo bằng `#define`

Ví dụ: Định nghĩa giá trị cho hằng số $\pi$ để tính điện tích hình tròn.

```c
#include "stdio.h"

#define PI (3.14159265359f)

int main(int argc, char const *argv[])
{
    printf ("Area of Circle R = 5 is: (%f)\n", PI*PI*5.00);
    return 0;
}
```

## Macros Có Sẵn

### Function-like Macros

