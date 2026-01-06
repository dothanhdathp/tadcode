# \[C++\] Kiểu biến Fundamental

## Định nghĩa

- Các loại biến cơ bản bao gồm _bool_, _char_, _short_, _int_, _long_, _float_, _double_
- Biến cơ bản nghĩa là các loại biến có sẵn _(không thông qua lớp gói ghém nào cả)_
- Biến cơ bản thụ động, không có chức năng phụ gì cả.

## Danh sách

| Type   | 32–bit Size | 64–bit Size | Min                        | Max                       | Unsigned (Min=0)          |
| :----- | :---------: | :---------: | :------------------------: | :-----------------------: | :-----------------------: |
| bool   | 1 byte      | 1 byte      | NA                         | NA                        | NA                        |
| char   | 1 byte      | 1 byte      | -128                       | 127                       | 255                       |
| short  | 2 byte      | 2 byte      | -32768                     | 32767                     | 65535                     |
| int    | 4 byte      | 4 byte      | -2147483648                | 2147483647                | 4294967295 = $2^{32}-1$   |
| long   | 4 byte      | 8 byte      | (tự tính)                  | (tự tính)                 | (tự tính)                 |
| float  | 4 byte      | 4 byte      | $-3.40282 \times 10^{38}$  | $3.40282 \times 10^{38}$  | TO_DO                     |
| double | 8 byte      | 8 byte      | $−1,79769 \times 10^{308}$ | $1,79769 \times 10^{308}$ | TO_DO                     |

## Integer (short, int)

Số nguyên là các số thực nguyên bản thường dùng, không có dấu phẩy.

Tập các số nguyên trong C++ có rất nhiều loại khác nhau như `short`, `int`, `long`, `long long`. Chúng giống nhau về bản chất, khác nhau về khối lượng lưu trữ

Số nguyên là số duy nhất chia thành số nguyên có dấu và không dấu. Mặc định là số có dấu.

### Số nguyên dạng có dấu

Về cơ bản nếu không có khai báo gì thêm thì số nguyên sẽ là __dạng số nguyên có dấu__.

| Type        |  Size   |          Min           |          Max          | Max as bit `0xF..F` |
| :---------- | :-----: | :--------------------: | :-------------------: | :-----------------: |
| `short`     | 2 bytes |        `-32768`        |        `32767`        |        `-1`         |
| `int`       | 4 bytes |     `-2147483648`      |     `2147483647`      |        `-1`         |
| `long`      | 8 bytes |     `-2147483648`      |     `2147483647`      |        `-1`         |
| `long long` | 8 bytes | `-9223372036854775808` | `9223372036854775807` |        `-1`         |

### Số nguyên không dấu

Nếu là __dạng số nguyên không dấu__, cần thêm biến `unsigned`.

| Type                 |  Size   | Min |          Max           |  Max as bit `0xF..F`   |
| :------------------- | :-----: | :-: | :--------------------: | :--------------------: |
| `unsigned short`     | 2 bytes | `0` |        `65535`         |        `65535`         |
| `unsigned int`       | 4 bytes | `0` |      `4294967295`      |      `4294967295`      |
| `unsigned long`      | 8 bytes | `0` |      `4294967295`      |      `4294967295`      |
| `unsigned long long` | 8 bytes | `0` | `18446744073709551615` | `18446744073709551615` |

## Floating-Point (float, double)

Các loại ___floating-point___ đại diện cho các số thực, tức là, các số có điểm thập phân. Có hai loại ___floating-point___ chính:

- `float`: __Float__ Cung cấp số dấu nổi chính xác đơn. Nó thường chiếm `4 bytes` bộ nhớ.
    ```c++
    float pi = 3.14f;
    ```
- `double`: __Double__ Cung cấp các số điểm nổi độ chính xác kép. Nó tiêu thụ nhiều bộ nhớ hơn (thường là `8 bytes`) nhưng có độ chính xác cao hơn `float`.
    ```c++
    double pi_high_precision = 3.1415926535;
    ```
## Character (char)

Các ký tự đại diện cho một ký tự duy nhất, chẳng hạn như chữ cái, chữ số hoặc ký hiệu. Chúng được lưu trữ bằng cách sử dụng giá trị ASCII của biểu tượng và thường chiếm 1 byte bộ nhớ.

```c++
char letter = 'A';
```

## Boolean (bool)

Booleans đại diện cho các giá trị logic: __Đúng__ (`true`) hoặc __Sai__ (`false`). bool thường chiếm 1 byte bộ nhớ.

```c++
bool is_cpp_great = true;
```

## Ví dụ các loại biến cơ bản

Tổ hợp biến cơ bản của C++ gồm có:

- `int`, `short`, `long`: số tự nhiên (bao gồm cả số âm)
- `float` hoặc `double`: số thập phân, ví dụ như là 19.99 hoặc 19.99
- `char` : ký tự, kiểu chữ cái đơn lẻ `a`, `b` hay `c` hoặc `+` ...
- `bool` : giá trị logic đúng sai (`true`/`false`)

```c++
int main()
{
	int    i = 10;
	float  f1 = 0.5;
	double f2 = 1.5;
	char   c = 'f';
	std::cout << i << std::endl;
	std::cout << f1 << std::endl;
	std::cout << f2 << std::endl;
	std::cout << c << std::endl;
	return EXIT_SUCCESS;
}
```
```txt title="Kết quả"
10
0.5
1.5
f
```
> `std::endl` để kết thúc công việc `cout` và xuống dòng.

## Thay đổi biến

Biến có thể được gắn lại cho giá trị khác sau khi khai báo, ví dụ:

```c++
int main() {
    int i = 0;
    i = 10; // Sau lần khai báo đầu tiên, không cần phải gọi lại int để định dạng kiểu biến.
    cout << i << endl; // Kết quả là 10
    return EXIT_SUCCESS;
}
```

## Hằng số

- __Hằng số__ là dạng biến không thể sửa đổi nội dung sau khi khai báo.
- __Hằng số__ khai báo bằng `const`

```c++ title="main"
int main() {
    unsigned int ui = -1; // Sẽ bị chuyển đổi
    const int ci = 10;
    // ci = 20; // Sẽ gây ra lỗi khi build
    cout << ui << endl; // Kết quả là 10
    return EXIT_SUCCESS;
}
```
```txt title="Kết quả"
4294967295
```

<div style="display: none;">

Link to:

- [Pointer](cpp-pointer.md)
- [Array](cpp-array.md)
- [Struct](cpp-struct.md)
- [Union](cpp-union.md)
- [String](cpp-std-string.md)

</div>