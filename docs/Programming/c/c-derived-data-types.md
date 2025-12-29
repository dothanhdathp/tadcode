## Derived Data Types

## array

Chuỗi mô tả một tập hợp nhiều dữ liệu. Các dữ liệu chuỗi thường được mô tả bằng `type __name[__size]`

Ví dụ:

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

## pointer

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

Con trỏ là một vấn đề khó, khai thác nó sẽ đọc thêm ở bài [Pointer](c-pointer.md)

## function