# \[C\] Callback Function

__Callback Function__ là cách truyền một hàm vào trong một hàm khác để hàm đó có thể gọi đến bất cứ lúc nào.

## Ví Dụ

```c
#include <stdio.h>
#include <stdbool.h>

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);

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

void do_action(void (*function)(int a, int b), int a, int b) {
    function(a,b);
}

int main() {
    do_action(add,4,2);
    do_action(sub,4,2);
    do_action(mul,4,2);
    do_action(divd,4,2);
    return 0;
}
```
```text title="Kết Quả"
4 + 2 = 6
4 - 2 = 2
4 * 2 = 8
4 / 2 = 2
```