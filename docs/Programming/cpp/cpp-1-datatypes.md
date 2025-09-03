# Data Type (Kiểu Biến)

## Primitive Data Types (Các loại biến cơ bản)

### Định nghĩa

- Các loại biến cơ bản bao gồm _bool_, _char_, _short_, _int_, _long_, _float_, _double_
- Biến cơ bản nghĩa là các loại biến có sẵn _(không thông qua lớp gói ghém nào cả)_
- Biến cơ bản thụ động, không có chức năng phụ gì cả.

### Danh sách

| Type   | 32–bit Size | 64–bit Size | Min                        | Max                       | Unsigned (Min=0)          |
| :----- | :---------: | :---------: | :------------------------: | :-----------------------: | :-----------------------: |
| bool   | 1 byte      | 1 byte      | NA                         | NA                        | NA                        |
| char   | 1 byte      | 1 byte      | -128                       | 127                       | 255                       |
| short  | 2 byte      | 2 byte      | -32768                     | 32767                     | 65535                     |
| int    | 4 byte      | 4 byte      | -2147483648                | 2147483647                | 4294967295 = $2^{32}-1$   |
| long   | 4 byte      | 8 byte      | (tự tính)                  | (tự tính)                 | (tự tính)                 |
| float  | 4 byte      | 4 byte      | $-3.40282 \times 10^{38}$  | $3.40282 \times 10^{38}$  | TO_DO                     |
| double | 8 byte      | 8 byte      | $−1,79769 \times 10^{308}$ | $1,79769 \times 10^{308}$ | TO_DO                     |

### Integer (short, int)

Số nguyên là các số toàn bộ có thể lưu trữ cả giá trị tích cực và âm. Kích thước của INT phụ thuộc vào kiến ​​trúc hệ thống (thường là 4 byte). Có các biến thể của int có thể chứa các phạm vi số khác nhau:

```cpp
int num = 42;
```

Có các biến thể của `int` có thể chứa các phạm vi số khác nhau:

- `short` (`short int`): Phạm vi nhỏ hơn `int`.
- `long` (`long int`): phạm vi lớn hơn `int`.
- `long long` (`long int`): thậm chí phạm vi lớn hơn so với `long int`.


Tập các số nguyên trong C++ có rất nhiều loại khác nhau như `short`, `int`, `long`, `long long`.

#### Số nguyên dạng có dấu

Về cơ bản nếu không có khai báo gì thêm thì số nguyên sẽ là __dạng số nguyên có dấu__.

| Type        |  Size   |          Min           |          Max          | Max as bit `0xF..F` |
| :---------- | :-----: | :--------------------: | :-------------------: | :-----------------: |
| `short`     | 2 bytes |        `-32768`        |        `32767`        |        `-1`         |
| `int`       | 4 bytes |     `-2147483648`      |     `2147483647`      |        `-1`         |
| `long`      | 8 bytes |     `-2147483648`      |     `2147483647`      |        `-1`         |
| `long long` | 8 bytes | `-9223372036854775808` | `9223372036854775807` |        `-1`         |

#### Số nguyên không dấu

Nếu là __dạng số nguyên không dấu__, cần thêm biến `unsigned`.

| Type                 |  Size   | Min |          Max           |  Max as bit `0xF..F`   |
| :------------------- | :-----: | :-: | :--------------------: | :--------------------: |
| `unsigned short`     | 2 bytes | `0` |        `65535`         |        `65535`         |
| `unsigned int`       | 4 bytes | `0` |      `4294967295`      |      `4294967295`      |
| `unsigned long`      | 8 bytes | `0` |      `4294967295`      |      `4294967295`      |
| `unsigned long long` | 8 bytes | `0` | `18446744073709551615` | `18446744073709551615` |

### Floating-Point (float, double)

Các loại ___floating-point___ đại diện cho các số thực, tức là, các số có điểm thập phân. Có hai loại ___floating-point___ chính:

- `float`: __Float__ Cung cấp số dấu nổi chính xác đơn. Nó thường chiếm `4 bytes` bộ nhớ.
    ```c++
    float pi = 3.14f;
    ```
- `double`: __Double__ Cung cấp các số điểm nổi độ chính xác kép. Nó tiêu thụ nhiều bộ nhớ hơn (thường là `8 bytes`) nhưng có độ chính xác cao hơn `float`.
    ```c++
    double pi_high_precision = 3.1415926535;
    ```
### Character (char)

Các ký tự đại diện cho một ký tự duy nhất, chẳng hạn như chữ cái, chữ số hoặc ký hiệu. Chúng được lưu trữ bằng cách sử dụng giá trị ASCII của biểu tượng và thường chiếm 1 byte bộ nhớ.

```c++
char letter = 'A';
```

### Boolean (bool)

Booleans đại diện cho các giá trị logic: __Đúng__ (`true`) hoặc __Sai__ (`false`). bool thường chiếm 1 byte bộ nhớ.

```c++
bool is_cpp_great = true;
```

### Ví dụ các loại biến cơ bản

Tổ hợp biến cơ bản của C++ gồm có:

- `int`, `short`, `long`: số tự nhiên (bao gồm cả số âm)
- `float` hoặc `double`: số thập phân, ví dụ như là 19.99 hoặc 19.99
- `char` : ký tự, kiểu chữ cái đơn lẻ `a`, `b` hay `c` hoặc `+` ...
- `bool` : giá trị logic đúng sai (`true`/`false`)

Hãy thử
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
Kết quả:
```bash
10
0.5
1.5
f
```
> `std::endl` để kết thúc công việc `cout` và xuống dòng.

## Array - Chuỗi

Chuỗi là một tập hợp có nhiều của biến, có thể là biến cơ bản hoặc không. Chuỗi được xác định bằng cách thêm `[]` đằng sau tên biến. Giữa hai dấu ngoặc sẽ là số lượng. Có thể không cần điền số lượng, nhưng để sử dụng nó tốt phải có kiến thức về con trỏ nên sẽ đề cập sau.

Truy cập phần tử của chuỗi chỉ cần dùng `tên_biến[vị_trí]` với vị trí là số thứ tự của phần tử trong chuỗi, <mark>nhưng nó sẽ bắt đầu từ `0`, không phải `1`</mark>

Xem ví dụ sau:
```c++
int main()
{
	int    i[5] = {1,2,3,4,5}; 
	char   c[5] = {'H', 'e', 'l', 'l', 'o'};
	string str = "Hello World";
	cout << i[0] << endl; // Trả về số đầu tiên
	cout << i[1] << endl; // Trả về số tiếp theo
	cout << c[0] << c[1] << c[2] << c[3] << c[4] << endl; // Đầy đủ
	cout << str << endl;  // Chuỗi ký tự
	return EXIT_SUCCESS;
}
```
Kết quả:
```bash
1
2
Hello
Hello World
```

!!! warning "Chú ý"
	Bạn không thể gọi đến vị trí vượt quá giới hạn của chuỗi. Ví dụ như `i[6]`

### string

- `string` về cơ bản là một chuỗi `char` đặc biệt được phát triển dành riêng cho ngôn ngữ `C++` cần thư viện __standard library c++__, cần sử dụng __std::string__. Mà thực tế là chả ai rảnh để viết từng ký tự cho một văn bản cả nên việc có nó là bắt buộc.
- `string` được coi là một trong những dạng biến cơ bản bằt đầu từ `C++`. Nhưng về bản chất nó vẫn là một chuỗi những ký tự `char` nên mình để đây. Xung quanh `string` còn có rất nhiều thư viện vệ tinh hỗ trợ nên riêng kiểu biến này sẽ được tách ra làm một chương riêng.

### Thay đổi biến

Biến có thể được gắn lại cho giá trị khác sau khi khai báo, ví dụ:
```c++
int main() {
    int i = 0;
    i = 10; // Sau lần khai báo đầu tiên, không cần phải gọi lại int để định dạng kiểu biến.
    cout << i << endl; // Kết quả là 10
    return EXIT_SUCCESS;
}
```
### Khai báo mở rộng

Biến có thể được khai báo thêm một số ràng buộc điều kiện như:

- `unsigned` : ràng buộc là số dương
- `const` : không thể đổi

```c++
int main() {
    unsigned int ui = -1; // Sẽ bị chuyển đổi
    const int ci = 10;
    // ci = 20; // Sẽ gây ra lỗi khi build
    cout << ui << endl; // Kết quả là 10
    return EXIT_SUCCESS;
}
```
Kết quả:
```bash
4294967295
```

## Ép kiểu

Biến có thể ép kiểu từ loại này sang loại khác. Ép kiểu cũng có 2 kiểu:

- Ép kiểu an toàn là ép kiểu từ dữ liệu thấp lên cao hoặc bằng nhau.
- Ép kiểu dữ liệu từ cao xuống thấp là không an toàn.

Xem kích thước kiểu dữ liệu ở bảng [Danh sách]( #danh-sach), cụ thể là:

- Ví dụ ép kiểu an toàn là từ _bool_, _char_, _..._, kiểu dữ liệu nhỏ thành _int_, _float_, _double_ là ép kiểu an toàn.
- Ví dụ ép kiểu không an toàn là từ kích thước lớn như _int_, _float_, _double_, _..._ sang kiểu an toàn là _bool_, _char_, _..._

```c++
int main()
{
	int a = 2000000000;
	short s0 = 97;

	short s1 = a;
	long  l = a;
	char c = s0;
	cout << s1 << endl; // Hight -> low
	cout << l << endl;
	cout << c << endl;
	return EXIT_SUCCESS; 
}
```
Kết quả:
```bash
-27648
2000000000
```
