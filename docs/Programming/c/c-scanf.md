# \[C\] Scanf

## Mô Tả

> Read formatted data from stdin

```text
int scanf ( const char * format, ... );
```

Đọc dữ liệu đầu vào và ép chúng thành một định dạng gần tương tự như hàm [printf](c-printf.md).

## Định Dạng

Về định dạng thì nó như này:

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

Một điểm khác biệt cần nhớ, khi truyền tham số vào để đọc dữ liệu đầu vào, phải truyền địa chỉ biến.

## Ví Dụ

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    char str[100];
    int i;
    float f;
    printf ("Input String: ");
    scanf ("%d", str);
    printf ("Input Interger: ");
    scanf ("%d", &i);
    printf ("Input Double: ");
    scanf ("%d", &f);
    printf ("You Have Input:\n- %s\n- %d\n- %f", str, i, f);
    return 0;
}
```
```text title="Kết Quả"
Input String: ádadasdadasd
Input Interger: 123
Input Double: 111.222    
You Have Input:
- ádadasdadasd
- 123
- 111.222000
```

## gets

Hàm này dễ dùng hơn, đùng dể đọc một đoạn văn bản đầu vào.

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    char str[100];
    gets(str);
    printf ("You Have Input: %s\n", str);
    return 0;
}
```
```text title="Kết Quả"
ádadasdadasd
You Have Input: ádadasdadasd
```

## getchar

Đọc __chỉ một ký tự__ từ đầu vào và đưa vào biến `char`

```c
#include "stdio.h"

int main(int argc, char const *argv[])
{
    char c = getchar();
    printf ("You Have Input: %c\n", c);
    return 0;
}
```
```text title="Kết Quả"
c
You Have Input: c
```
