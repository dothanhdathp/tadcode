# \[C\] Preprocessor

## Định Nghĩa

- __Tiền xử lý__ là quá trình thao tác một số cấu hình, đặt định nghĩa trước khi bắt đầu biên dịch mà nguồn.
- Các tiến trình tiền xử lý thông thường sẽ được có dấu `#` ở đằng trước, không hoàn toàn nhưng thường là vậy.
- Tiến trình _tiền xử lý_ đầu tiên được biết đến chính là tiến trình thêm thư viện hoặc thêm khai báo thư viện với `#include`.
- Bộ tiền xử lý được thực hiện tại [Giai Đoạn 4 của Trình Biên Dịch](c-translation-phases.md#giai-oan-4-phase-4), trước khi biên soạn. Kết quả của quá trình tiền xử lý là một tệp duy nhất sau đó được chuyển đến trình biên dịch thực tế.

## Chức Năng

### Biên dịch điều kiện

Các cờ biên dịch có điều kiện xác định một khối điều kiện có được thực thi hoặc không dựa vào điều kiện của cờ được bật hoặc tắt theo cơ chế __*nếu - thì (if - else)*__.

Các cờ biên dịch điều kiện bao gồm:

| Cờ          | Version |
| :---------- | :------ |
| `#if`       |         |
| `#ifdef`    |         |
| `#ifndef`   |         |
| `#elif`     |         |
| `#elifdef`  | (C23)   |
| `#elifndef` | (C23)   |
| `#else`     |         |
| `#endif`    |         |

Về cơ bản nhất nó chỉ đơn giản là

- Xác định cờ điều kiện.
- Nếu có thì biên dịch mã theo đó.
- Nếu không có thì không biên dịch đoạn mã đó.

Ví dụ:

=== "HIGH_PRECISION"
    ```c title="main.h"
    #define HIGH_PRECISION

    #define PI (3.14159265359f)
    #else
    #define PI (3.14)
    #endif
    ```
    ```c title="main.c"
    #include "stdio.h"
    #include "main.h"

    int main(int argc, char const *argv[])
    {
        printf ("Pi: (%f)\n", PI);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    Pi: (3.141593)
    ```
=== "No HIGH_PRECISION"
    ```c title="main.h"
    // #define HIGH_PRECISION

    #define PI (3.14159265359f)
    #else
    #define PI (3.14)
    #endif
    ```
    ```c title="main.c"
    #include "stdio.h"
    #include "main.h"

    int main(int argc, char const *argv[])
    {
        printf ("Pi: (%f)\n", PI);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    Pi: (3.140000)
    ```

!!! danger "Chú Ý"
    Hai cờ `#elifdef` và `#elifndef` chỉ có thể sử dụng từ phiên bản __C23__

## Replace Text Macros

[Thay thế macro văn bản](c-replacing-text-macros.md) trong khi có thể nối hoặc trích dẫn các mã định danh (được điều khiển bởi các lệnh `#define` và `#undef` cũng như các toán tử `#` và `##`)