# \[C\] Printf

## Thư viện

```c
#include "stdio.h"
```

## Syntax

```text title="Syntax"
printf("format_string", args...);
```

## Example

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    printf("Hello World!");
    return 0;
}
```
```text title="Kết Quả"
Hello World!
```

## Format Specifier

```text title="Syntax"
%[flags][width][.precision][length]specifier
```

- Trong chuỗi __*format_string*__, các đối số được thay đổi sẽ được bắt đầu bằng ký tự `%`
- Sau ký tự `%` sẽ là __*flags*__, là một _ký tự_. Ký tự đó được gọi là __*specifier character*__ như bảng dưới đây:

Ví dụ như sau:

```c
int a = 10;
printf("%s %o %d %x %p\n", "string", a, a, a, &a);
```
```text
string 12 10 a 0x7ffc19a1ca04
```

Tác dụng của %s `%o`, `%d`, `%x`, `%p` như bảng dưới đây:

| Specifier |      Type       | Number System |   Sign   | Case  | Present For                                      |   Example    |
| :-------- | :-------------: | :-----------: | :------: | :---: | :----------------------------------------------- | :----------: |
| `%d`      |    Interger     |    Decimal    |  Signed  |       | `short`, `int`, `long`                           |     392      |
| `%i`      |    Interger     |    Decimal    |  Signed  |       | `short`, `int`, `long`                           |     392      |
| `%u`      |    Interger     |    Decimal    | Unsigned |       | `unsigned int`, `unsigned long`, `u_int64_t`,... |     7235     |
| `%o`      |    Interger     |     Octal     | Unsigned |       | `int`, `unsigned int`, ...                       |     610      |
| `%x`      |    Interger     |  Hexadecimal  | Unsigned | Lower | `int`, `unsigned int`, ...                       |     7fa      |
| `%X`      |    Interger     |  Hexadecimal  | Unsigned | Upper | `int`, `unsigned int`, ...                       |     7FA      |
| `%f`      | Floating Point  |    Decimal    |  Signed  | Lower | `float`, `double`                                |    392.65    |
| `%F`      | Floating Point  |    Decimal    |  Signed  | Upper | `float`, `double`                                |    392.65    |
| `%e`      | Floating Point  |  Decimal + E  |  Signed  | Lower | `float`, `double`                                |  3.9265e+2   |
| `%E`      | Floating Point  |  Decimal + E  |  Signed  | Upper | `float`, `double`                                |  3.9265E+2   |
| `%g`      | Floating Point  |    Decimal    |  Signed  | Lower | `float`, `double`                                |    392.65    |
| `%G`      | Floating Point  |    Decimal    |  Signed  | Upper | `float`, `double`                                |    392.65    |
| `%a`      | Floating Point  |  Hexadecimal  |  Signed  | Lower | `float`, `double`                                | -0xc.90fep-2 |
| `%A`      | Floating Point  |  Hexadecimal  |  Signed  | Upper | `float`, `double`                                | -0XC.90FEP-2 |
| `%c`      |    Character    |               |          |       | `char`                                           |      a       |
| `%s`      |     String      |               |          |       | `chat*`, `const chat*`                           |    sample    |
| `%p`      | Pointer Address |               |          |       | Address of __Object__                            |   b8000000   |



## Format Specifier

### Flags

| `[flags]` | Description                                                                                                                                                                                                                                               |
| :-------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    `-`    | Căn lề sang __*trái*__                                                                                                                                                                                                                                    |
|    `+`    | Căn lề sang __*phải*__ _(mặc định)_                                                                                                                                                                                                                       |
|    `#`    | Khi sử dụng với các cờ `o`, `x` hoặc `X`, các số được biểu diễn thành `0x`, `0X` thay vì số thuần.<br>Khi sử dụng với `a`, `A`,`e` ,`E` ,`f` ,`F` ,`g` hoặc `G`, nó buộc đầu ra được ghi phải chứa dấu thập phân ngay cả khi không có chữ số nào theo sau |
|    `0`    | Điền tất cả các phần trống còn lại với ký tự 0. Sử dụng với [Width](#width)                                                                                                                                                                               |

### Width

- `[width]` là một số chỉ định số ký tự tối thiểu cần in. Nếu giá trị cần in ngắn hơn số này, kết quả sẽ được thêm khoảng trắng. Giá trị không bị cắt bớt ngay cả khi kết quả lớn hơn.
- Khi chiều rộng không được chỉ định trong chuỗi định dạng mà là một đối số giá trị số nguyên bổ sung đứng trước đối số cần được định dạng. Giá trị của nó có thể đặt thành `*`

### Precision

- Đối với các chỉ định số nguyên (`d` ,`i` ,`o` ,`u` ,`x` ,`X` ): `[precision]` sẽ đặt trước dấu phẩy, chỉ định số chữ số tối thiểu cần ghi. Nếu giá trị cần ghi ngắn hơn số này, kết quả sẽ được thêm số không đứng đầu. Giá trị không bị cắt bớt ngay cả khi kết quả dài hơn. Độ chính xác bằng 0 nghĩa là không có ký tự nào được ghi cho giá trị 0.
- Đối với các chỉ định `a`, `A`, `e`, `E`, `f` và `F` : đây là số chữ số cần in sau dấu thập phân (theo mặc định là 6).
- Đối với các chỉ định g và G : Đây là số chữ số có nghĩa tối đa cần in.
- Đối với `s`: đây là số ký tự tối đa cần in. Theo mặc định, tất cả các ký tự được in cho đến khi gặp ký tự __null__ kết thúc.
- Nếu dấu chấm được chỉ định mà không có giá trị rõ ràng cho độ chính xác , thì giá trị 0 được coi là đúng.
- Khi chiều rộng không được chỉ định trong chuỗi định dạng mà là một đối số giá trị số nguyên bổ sung đứng trước đối số cần được định dạng. Giá trị của nó có thể đặt thành `*`


### Modifiers Length

Bộ xác định phụ độ dài sửa đổi độ dài của kiểu dữ liệu. Đây là biểu đồ hiển thị các loại được sử dụng để diễn giải các đối số tương ứng có và không có bộ xác định độ dài (nếu sử dụng một loại khác, việc quảng bá hoặc chuyển đổi loại thích hợp sẽ được thực hiện, nếu được phép):

| length | d i           | u o x X                | f F e E g G a A | c      | s        | p     | n              |
| :----- | :------------ | :--------------------- | :-------------- | :----- | :------- | :---- | :------------- |
| (none) | int           | unsigned int           | double          | int    | char*    | void* | int*           |
| hh     | signed char   | unsigned char          |                 |        |          |       | signed char*   |
| h      | short int     | unsigned short int     |                 |        |          |       | short int*     |
| l      | long int      | unsigned long int      |                 | wint_t | wchar_t* |       | long int*      |
| ll     | long long int | unsigned long long int |                 |        |          |       | long long int* |
| j      | intmax_t      | uintmax_t              |                 |        |          |       | intmax_t*      |
| z      | size_t        | size_t                 |                 |        |          |       | size_t*        |
| t      | ptrdiff_t     | ptrdiff_t              |                 |        |          |       | ptrdiff_t*     |
| L      |               |                        | long double     |        |          |       |                |		

!!! note "Note"
    Thật ra cái chức năng này mình cũng chả hiểu gì lắm chỉ chép cho có thôi.

## Ký Tự Đặc Biệt

Một số ký tự đặc biệt giống trên bảng mã [bảng mã ASCII](/Common/common-ASCII) không phải một ký tự thuần như ký tự trên bàn phím. Các ký tự đó được gọi là các __*ký tự đặt biệt*__. Các ký tự ngoài khả năng biểu diễn một hình gì đó còn có tác dụng:

- `\n`: Xuống dòng
- `\t`: Tab, tạo khoảng trắng

## Ghi nhớ

- Hàm __*printf*__ sẽ tự động chuyển đổi để phù hợp đầu ra. Ví dụ ở ký tự `'A'` nếu ép hiển thị dưới dạng số nguyên thập phân thì nó sẽ in ra giá trị của ký tự đó trên [bảng mã ASCII](/Common/common-ASCII)
- Trường hợp không thể chuyển đổi, ví dụ như `%s` với con trỏ __NULL__ sẽ gây lỗi và chết chương trình.
- Trường hợp không có đầu và sẽ thường bị rơi vào trường hợp __*con trỏ không xác định*__. Ví dự như sau:
    ```c
    #include "stdio.h"

    int main(int argc, char const *argv[])
    {
        int a = 10;
        printf("%s %c %d %o %f %p\n");
        return 0;
    }
    ```
    ```text title="Kết Quả Không Xác Định"
    ��      H� ( 1012198848 0 0.000000 0x74ba30b7a380
    ```
    Thên tính năng tự chuyển đổi nữa nên giá trị sẽ không rõ ràng, phải thật cẩn thận khi sử dụng.

## puts, putchar

Khác với __*printf*__, hai hàm __*puts*__, __*putchar*__ chỉ đơn giản đẩy một chuỗi, một ký tự ra ngoài. Không có sử dụng _format_ hoặc biến, ...

Hai hàm này chỉ có tác dụng đơn điệu:
- `puts`: Đẩy một chuỗi thuần ra ngoài
- `putchar`: Đẩy một chuỗi thuần ra ngoài

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    puts("%s %c %d %o %f %p\n");
    putchar('c');
}
```
```text title="Kết Quả"
%s %c %d %o %f %p
c
```

## See also

- [scanf](c-scanf.md)
- [fprintf](c-fprintf.md)
- [fwrite]()