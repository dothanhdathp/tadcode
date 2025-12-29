# \[C\] Basic Data Types

## Data Types

Mỗi biến trong C có một kiểu dữ liệu liên quan. Nó chỉ định loại dữ liệu mà biến có thể lưu trữ như số nguyên, ký tự, float, double, v.v.

__C là ngôn ngữ kiểu tĩnh__ trong đó kiểu của mỗi biến phải được chỉ định khi khai báo và một khi đã được chỉ định thì không thể thay đổi được.

<figure markdown="span">
    ![](img/c-data-types.svg)
    <figcaption></figcaption>
</figure>

## Basic Data Types

### Basic

| Type     | Size (byte) | Mô tả        |
| :------- | ----------: | :----------- |
| `void`   |      0 byte | Hư vô        |
| `int`    |      4 byte | Số nguyên    |
| `long`   |      8 byte | Số nguyên    |
| `char`   |      1 byte | Ký tự        |
| `float`  |      4 byte | Số Thập Phân |
| `double` |      8 byte | Số Thập Phân |

#### int

- Dữ liệu kiểu số nguyên.

#### float

- Dữ liệu kiểu số thực (số có dấu phẩy động).
- Độ chính xác không quá cao. Sau dấu phẩy có giới hạn về số lượng số nên <mark>nhiều phép tính không thể chính xác</mark>
- Muốn chính xác thì nếu số khai báo là tĩnh thì nên để thêm ký tự `f` để xác minh. Ví dụ `30.5f`
    - Hành động này có tác dụng ép kiểu số _(làm tròn)_ về dạng số thập phân chính xác. Có thể tin tưởng vào các phép toán có làm tròn.
- <mark>Các số __*float*__ luôn là 2 chiều âm/dương. Không có `unsigned float`</mark>

#### double

- Dữ liệu kiểu số thực (số có dấu phẩy động) mở rộng.
- Độ chính xác và giới hạn tốt hơn nhiều, được sử dụng nhiều trong các ngành kỹ thuật.
- Các số __*double*__ luôn là 2 chiều âm/dương. Không có `unsigned double`

#### char

- Dữ liệu kiểu ký tự, chữ cơ bản.
- Các _ký tự_ được định nghĩa theo [bảng mã ASCII](/Common/common-ASCII)
- C không có __*câu, đoạn văn*__. char chỉ đại diện cho __*từng ký tự đơn lẻ*__. Muốn có một __*đoạn văn bản*__ cần sử dụng một kiểu khác là [chuỗi dữ liệu](c-array.md)


#### void

- Là kiểu dữ liệu độc đáo nhất, đại diện cho kiểu dữ liệu hư vô.
- Trung bình `void` sẽ có nhiều ý nghĩa hơn là quan tâm đến kiểu của nó, ví dụ:
    - Hàm không cần dùng dữ liệu trả về.
    - Một biến lơ lửng có thể chứa nhiều loại dữ liệu.
    - Loại biến không cần quan tâm, chỉ cần biết nó là một kiểu biến.
- Tác dụng và ý nghĩa của kiểu dữ liệu này thường gắn liền với kiến thức về [pointer]() nhiều hơn.

!!! danger "bool không phải kiểu thuần túy"
    - __bool__ không phải kiểu thuần túy trong __C__.
    - Khái niệm __true/false__ được người dùng tự định nghĩa thông qua define:
        ```text
        #define TRUE 1
        #define FALSE 0
        ```

### Tổng hợp

## Extend

Ngoài các loại trên, một số loại bổ sung ít dùng khác được sử dụng như

int8_t, int16_t

## Liên Kết

- [Giới Hạn Số](c-numeric-limits.md)
- [Derived Data Types](c-derived-data-types.md)
- [User Defined Data Types](c-user-defined-data-types.md)