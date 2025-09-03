# Input and Output

## Mô tả

Có hai kiểu để xuất ra ngoài là dùng hàm kiểu ___C___ là ___printf()___ và ___cin___. Và kiểu xuất động từ thư viện `std`.

##  Thao tác nguyên thủy
### putchar/puts

- Thao tác đơn giản, đẩy một chuỗi ký tự ra ngoài màn hình.
- Phụ thuộc thư viện `stdio.h`

| 1       | 2                                | 3                           |
| :------ | :------------------------------- | :-------------------------- |
| putchar | `int putchar(int character)`     | Viết một ký tự vào `stdout` |
| puts    | `int puts ( const char * str );` | Viết chuỗi vào `stdout`     |

### printf

- Thư viện kiểu C được kế thừa từ jngoon
- Cấu trúc hàm: `int printf ( const char * format, ... );`
    - Hàm này có giá trị trả về, là số ký tự được xuất ra ngoài.

| Specifier  | Output                                                                                                                                                  | Example      |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------- |
| `d` or `i` | Số nguyên thập phân có dấu                                                                                                                              | 392          |
| `u`        | Số nguyên thập phân không dấu                                                                                                                           | 7235         |
| `o`        | Bát phân không dấu                                                                                                                                      | 610          |
| `x`        | Số nguyên thập lục phân không dấu                                                                                                                       | 7ngày        |
| `X`        | Số nguyên thập lục phân không dấu (viết hoa)                                                                                                            | 7FA          |
| `f`        | Số thập phân dấu phẩy động, chữ thường                                                                                                                  | 392,65       |
| `F`        | Số thập phân dấu phẩy động, chữ hoa                                                                                                                     | 392,65       |
| `e`        | Ký hiệu khoa học (mantissa/mũ), chữ thường                                                                                                              | 3.9265e+2    |
| `E`        | Ký hiệu khoa học (mantissa/mũ), chữ hoa                                                                                                                 | 3.9265E+2    |
| `g`        | Sử dụng biểu diễn ngắn nhất: %e hoặc %f                                                                                                                 | 392,65       |
| `G`        | Sử dụng biểu diễn ngắn nhất: %E hoặc %F                                                                                                                 | 392,65       |
| `a`        | Dấu phẩy động thập lục phân, chữ thường                                                                                                                 | -0xc.90fep-2 |
| `A`        | Dấu phẩy động thập lục phân, chữ hoa                                                                                                                    | -0XC.90FEP-2 |
| `c`        | Tính cách                                                                                                                                               | Một          |
| `S`        | Chuỗi ký tự                                                                                                                                             | vật mẫu      |
| `P`        | Địa chỉ con trỏ                                                                                                                                         | b8000000     |
| `N`        | Không có gì được in ra. Đối số tương ứng phải là một con trỏ đến một số nguyên có dấu. Số ký tự đã viết cho đến nay được lưu trữ ở vị trí được trỏ tới. |              |
| `%`        | Ký tự % theo sau là một ký tự % khác sẽ ghi một ký tự % duy nhất vào luồng.                                                                             | %            |

Flag

| flags   | description                                                                                                                                                                                                                                                                                                                                                                      |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-`       | Căn trái trong phạm vi chiều rộng được chỉ định; Căn phải là mặc định (xem thông số phụ về chiều rộng ).                                                                                                                                                                                                                                                                         |
| `+`       | Buộc phải thêm dấu cộng hoặc dấu trừ ( + hoặc - ) vào trước kết quả ngay cả đối với số dương.                                                                                                                                                                                                                                                                                    |
| `(space)` | Nếu không có dấu hiệu nào được viết, một khoảng trắng sẽ được chèn vào trước giá trị.                                                                                                                                                                                                                                                                                            |
| `#`       | Được sử dụng với các chỉ định `o, x hoặc X`, giá trị được đặt trước bằng `0, 0x hoặc 0X` tương ứng cho các giá trị khác không.<br>Được sử dụng với `a, A, e, E, f, F, g hoặc G`, nó buộc đầu ra được viết phải chứa dấu thập phân ngay cả khi không có thêm chữ số nào theo sau.<br>_Theo mặc định, nếu không có chữ số nào theo sau, thì không có dấu thập phân nào được viết._ |
| `0`       | Thêm số bên trái bằng số không.                                                                                                                                                                                                                                                                                                                                                  |


### std::cout

## cin

## Reference (tham khảo)