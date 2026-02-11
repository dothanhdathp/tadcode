# Function Pointer

__Con trỏ hàm__ _(Function Pointer)_

## Con Trỏ Hàm

Ví dụ đơn giản con trỏ hàm đầu tiên.

```c
#include <stdio.h>
#include <stdbool.h>

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);

void add(int a, int b) {
    println("%d + %d = %d",a,b,a+b);
}

int main() {
    void (*fn)(int, int) = &add;
    fn(2,3);

    return 0;
}
```
```text title="Kết Quả"
4 + 2 = 6
```

## Chuỗi Con Trỏ Hàm

Tạo một mảng con trỏ hàm và chức năng.

```c
#include <stdio.h>
#include <stdbool.h>

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);

enum function_name {
    ADD,
    SUB,
    MUL,
    DIV,
    FN_MAX
};

void add(int a, int b) {
    println("%d + %d = %d",a,b,a+b);
}
void sub(int a, int b) {
    println("%d - %d = %d",a,b,a-b);
}
void mul(int a, int b) {
    println("%d * %d = %d",a,b,a*b);
}
void divd(int a, int b) {
    println("%d / %d = %d",a,b,a/b);
}

int main() {
    void (*function_array[FN_MAX])(int, int) = {add, sub, mul, divd};

    function_array[ADD](4,2);
    function_array[SUB](4,2);
    function_array[MUL](4,2);
    function_array[DIV](4,2);

    return 0;
}
```
```text title="Kết Quả"
4 + 2 = 6
4 - 2 = 2
4 * 2 = 8
4 / 2 = 2
```
