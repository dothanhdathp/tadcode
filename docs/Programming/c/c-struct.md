# Struct

- __struct__ là cấu trúc để hợp một nhóm các giá trị vào một nhóm.
- Việc thực thi có thế tương tác với từng thành phần trong __struct__
- __struct__ giúp tối giản việc đặt tên và cấu trúc hóa một số thực thể đa chiều.

## Ví dụ

Ví dụ với một dạng điểm ảnh hai chiều:

```c
#include "stdio.h"

struct point {   // Structure declaration
    int  x;           // Member (int variable)
    int y;       // Member (char variable)
}; // End

int main(int argc, char const *argv[])
{
    struct point p0;
    p0.x = 0;
    p0.y = 1;
    struct point p1 = {1,1};

    printf("Position of p0 [ %d, %d ]\n", p0.x, p0.y);
    printf("Position of p1 [ %d, %d ]\n", p1.x, p1.y);
    return 0;
}
```

Trong __*struct*__, con trỏ cũng có thể sử dụng và khai báo bình thường.

## Kích thước

### __Data Alignment__ & __Padding__

Kích thước của struct __*thường không bằng kích thước*__ các phần tử trong mảng. Thông thường trình biên dịch sẽ cố gắng chuyển nó thành các phần bằng nhau.

```c
#include "stdio.h"

struct point1 {
    int    x;
    int    y;
    int    z;
};

struct point2 {
    int    y;
    int    z;
    short  x;
};

int main(int argc, char const *argv[])
{
    struct point1 p1;
    struct point2 p2;
    printf("Size of short : %ld\n", sizeof(short));
    printf("Size of int : %ld\n", sizeof(int));
    printf("Size of p1 : %ld\n", sizeof(p1));
    printf("Size of p2 : %ld\n", sizeof(p2));
    return 0;
}
```
```text title="Kết Quả"
Size of short : 2
Size of int : 4
Size of p1 : 12
Size of p2 : 12
```

### Remove Padding

```c
#include "stdio.h"

struct point1 {
    int    x;
    int    y;
    int    z;
};

struct point2 {
    int    y;
    int    z;
    short  x;
} __attribute__((packed));

int main(int argc, char const *argv[])
{
    struct point1 p1;
    struct point2 p2;
    printf("Size of short : %ld\n", sizeof(short));
    printf("Size of int : %ld\n", sizeof(int));
    printf("Size of p1 : %ld\n", sizeof(p1));
    printf("Size of p2 : %ld\n", sizeof(p2));
    return 0;
}
```
```text title="Kết Quả"
Size of short : 2
Size of int : 4
Size of p1 : 12
Size of p2 : 12
```