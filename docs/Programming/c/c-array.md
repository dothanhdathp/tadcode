# Array

## Khái Niệm

- Chuỗi mô tả một tập hợp nhiều dữ liệu.
- Các biến dữ liệu trong chuỗi có tính liên tiếp, các phần tử nằm trên vùng bộ nhớ liền kề.
- Các dữ liệu chuỗi thường được mô tả bằng `type __name[__size]`

## Khai Báo

```c
int arr1[10] = {0,1,2,3,4,5,6,7,8,9}; // Have size
int arr2[] = {0,1,2,3,4,5,6,7,8,9};   // No size
int arr3[10];                         // Ok
// int arr4[];                        // Error
```

- Trường hợp tạo mảng không có khai báo ví dụ trường hợp `arr3` được vì có số lượng phần tử. `arr4` lỗi vì số lượng phần tử không được khai báo.
- `arr3` khi không có khai báo giá trị mặc định, thông thường nó sẽ là `0`, đôi khi nó sẽ là một vài giá trị rác tùy theo __*compiler*__ muốn biên dịch nó như thế nào.
- `arr4` vì không có số lượng, trình biên dịch không thể tạo ra được một mảng dữ liệu sẵn có dành cho nó. Thế nên lỗi.
- Mảng cũng cho phép sử dụng với nhiều dữ liệu kiểu mẫu, tự khai báo, ví dụ như tập hợp của nhiều __*pointer*__, __*struct*__, ... được trình bày ở các phần sau.

## Địa chỉ

Mỗi mảng được xác định như là một con trỏ. ví dụ với mảng `arr[]` thì `arr` chính là con trỏ đến địa chỉ bộ nhớ của phần tử đầu tiên:

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    int arr[10] = {99,1,2,3,4,5,6,7,8,9};
    printf("arr     = %p; Value: %d\n", arr, *arr);
    printf("&arr[0] = %p; Value: %d\n", &arr[0], arr[0]);
    return 0;
}
```
```text title="Kết Quả"
arr     = 0x7ffd6ecface0; Value: 99
&arr[0] = 0x7ffd6ecface0; Value: 99
```

## Tính Liền Kề

Các phần tử trong mảng liền kề nhau.

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    long long arr[] = {99,1,2,3,4,5,6,7,8,9};
    printf("Size of Int     : %ld\n", sizeof(long long));
    printf("arr[1] - arr[0] : %ld;\n", (&arr[1]) - (&arr[0]));
    return 0;
}
```
```text title="Kết Quả"
Size of Int     : 8
&arr[1] - &arr[0] : 1;
```