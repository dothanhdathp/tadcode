# Pointer

## Định Nghĩa

__Pointer__ dịch ra nghĩa là con trỏ. Biến này là kiểu đặc thù của ngôn ngữ C/C++. Thay vì là biến thông thường, biến này có nghĩa chính là _địa chỉ_, có thể là biến, có thể là hàm, nhưng rõ ràng nhất nó là _địa chỉ_.

Địa chỉ rất khó hiểu. Lập trình viên lâu năm nắm vững hết các cách sử dụng con trỏ cũng chưa chắc hiểu được bản chất. Đại loại cách dùng là thế này:

```c
int main(int argc, char const *argv[])
{
    int a = 20;
    int* p = &a;
    printf("Address = %p\n", p);
    printf("Value   = %d\n", *p);
    return 0;
}
```
```text title="Kết Quả"
Address = 0x7fff8bfc6dfc
Value   = 20
```

- `*` là phương thức của con trỏ
- `&` là phương thức lấy địa chỉ

Có một mẹo rất đơn giản, chỉ cần hiểu cả `int*` là một kiểu biến và con trỏ là một kiểu biến thì dễ dàng hơn nhiều. Nếu `int* p = &a` thì trong `int (*p)`, `(*p)` có kiểu là int như thứ nguyên vậy.

## Địa Chỉ

Địa chỉ mà toán tử trả về là địa chỉ thực tế của biến. Thử:

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    int arr[] = {99,1,2,3,4,5,6,7,8,9};
    int* p0 = &arr[0];
    int* p1 = &arr[1];
    printf("p0 : %p;\n", p0);
    printf("p1 : %p;\n", p1);
    return 0;
}
```

Được rồi giờ chỉ cần chạy lại chương trình nhiều lần:

```text
dtdat@dtdat-desktop:~/Work/C$ ./main 
p0              : 0x7fff18539980;
p1              : 0x7fff18539984;
dtdat@dtdat-desktop:~/Work/C$ ./main 
p0              : 0x7fffcea0eb80;
p1              : 0x7fffcea0eb84;
dtdat@dtdat-desktop:~/Work/C$ ./main 
p0              : 0x7ffd68152060;
p1              : 0x7ffd68152064;
dtdat@dtdat-desktop:~/Work/C$ ./main 
p0              : 0x7fff0a630ab0;
p1              : 0x7fff0a630ab4;
dtdat@dtdat-desktop:~/Work/C$ ./main 
p0              : 0x7fffbb820ac0;
p1              : 0x7fffbb820ac4;
```

Có thể thấy trong kết quả:

- Địa chỉ của biến (`0x7fffbb820ac4`) là một số __64-bit__ vì mình đang dùng hệ điều hành __64-bit__
- Mỗi lần chạy địa chỉ bộ nhớ đều thay đổi, nên suy ra lưu ở đâu là do hệ điều hành điều phối.
- Khoảng cách địa chỉ là 4 vì độ rộng của biến int là `4 byte`

## Độ Lớn

### Kích Thước Con Trỏ

- Mỗi con trỏ có thể coi như một __*loại nhãn địa chỉ*__. Vì chỉ mang địa chỉ nên kích thước của mỗi con trỏ không khác nhau:

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    int*   pi;
    long*  pl;
    short* ps;
    printf("sizeof(pi) : %ld;\n", sizeof(pi));
    printf("sizeof(pl) : %ld;\n", sizeof(pl));
    printf("sizeof(ps) : %ld;\n", sizeof(ps));
    return 0;
}
```
```text title="Kết Quả"
sizeof(pi) : 8
sizeof(pl) : 8
sizeof(ps) : 8
```
_Việc kết quả ra 8 là do hệ điều hành 64-bit. Bộ nhớ cơ bản sẽ được đánh địa chỉ là **8**_. Ý tưởng ở đây là vùng nhớ được sử dụng để chứa con trỏ không hề mang kích thước khác nhau.

### Toán Tử

!!! danger "Danger"
    Các toán tử trên con trỏ từ `+/-` không được khuyến nghị.

Phép toán khả dụng đối với con trỏ là phép toán `+/-` mang ý nghĩa tăng/giảm bậc của thùng chứa trên nhãn dán. Thế nên mỗi lần `+/-` được thao tác trên con trỏ đều trỏ dến vị trí tiếp theo của _biến cùng loại_, tức là về mặt địa chỉ vật lý, nó nhảy một khoảng cách đúng bằng địa chỉ của biến.

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    short as[3] = {0,1,2};
    int   ai[3] = {3,4,5};
    long  al[3] = {6,7,8};
    short* ps = as;
    int*   pi = ai;
    long*  pl = &al[2];
    printf("ps : %d,%d,%d;\n"   , *ps, *(ps+1), *(ps+2));
    printf("pi : %d,%d,%d;\n"   , *pi, *(++pi), *(++pi));
    printf("pl : %ld,%ld,%ld;\n", *(pl--), *(pl--), *(pl--));
    return 0;
}```
```text
ps = 0,1,2;
pi = 3,4,5;
pl = 6,7,8;
```

### Void*

- `void` không được tính là kiểu biến. Thông thường chương trình biên dịch sẽ cấm các hành vi tham chiếu đến `void`. Nhưng `void*` lại có ý nghĩa.
- Trước khi có `byte` được định nghĩa, `void*` chính là kiểu này. `void*` thuần túy mang ý nghĩa của _chuỗi dữ liệu không hình dạng_.
- Như mọi kiểu con trỏ, `void*` mang địa chỉ dữ liệu, mỗi bước nhảy đúng `1 byte` trên các phép toán `+/-`
- Thêm nữa, bản chất của `void*` vô tình phù hợp với điều kiện phần cứng và truyền nhận tín hiệu. Nơi các gói và dữ liệu các gói được tính theo __tổng số bytes__, loại gói cũng khác nhau, tức là có thể dạng int, short, float, ... gì không quan trọng. Sau khi người nhận nhận được gói hàng sẽ dùng ép kiểu để lấy dữ liệu.
- Đồng thời void cũng mở ra thời đại mới cho các thuật toán __*nén từng bits*__, nơi họ sắp xếp lại các phần tử trong gói theo đúng từng byte để tiết kiệm chỗ cho băng truyền thông.