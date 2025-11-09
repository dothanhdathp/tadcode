# Variables

## Variables and Mutability

### let

<div class="note-red">
Có 2 điểm cực kỳ quan trọng trong việc khai báo biến ở Rust đó là:

1. Rust là ngôn ngữ bậc cao nên Rust cũng cho phép khai báo với kiểu biến ngầm định.
1. Nếu không có sửa đổi, thì biến trong Rust sẽ __mặc định ở chế độ không thể sửa__.
</div><br>

Nghĩa là __về mặc định, biến trong ngôn ngữ này sẽ được khai báo là <u>bất biến</u>__. Đó là điểm khác biệt với một số ngôn ngữ khác.

Để tạo một biến trong ngôn ngữ _rust_, sử dụng ký hiệu `let`.
Ví dụ, thử tạo biến và in ra với chương trình sau:
```rust
fn main()
{
    let x = 10;
    println!("main: x = {}", x);
}
```
Biên dịch và chạy thử, chương trình sẽ cho ra kết quả:
```bash
main: x = 10
```
👉 Không cần khai báo kiểu biến là ___interger___. Vì `x=10` nên trình biên dịch tự động cho phép nó là kiểu số nguyên.

Giờ hãy thử sửa đổi nhỏ như sau:

```rust
fn main()
{
    let x = 10;
    x = 20;
    println!("main: x = {}", x);
}
```

Chương trình biên dịch sẽ thông báo là:
```bash
error[E0384]: cannot assign twice to immutable variable `x`
 --> main.rs:4:5
  |
3 |     let x = 10;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
4 |     x = 20;
  |     ^^^^^^ cannot assign twice to immutable variable

error: aborting due to 1 previous error; 1 warning emitted
```
Như có thể thấy, chương trình không cho phép bạn gán giá trị khác vào biến đã sử dụng.

### let mut

Không thể khai báo biến có thể sửa đổi với `let`. Muốn sửa đổi được giá trị của biến thì dùng `let mut`.

```rust
fn main()
{
    let mut x = 10;
    x = 20;
    println!("main: x = {}", x);
}
```
Biên dịch thử và kết quả đây:
```bash
main: x = 20
```
Đương nhiên là không vấn đề nhưng vẫn có cảnh báo:
```bash
warning: value assigned to `x` is never read
 --> main.rs:3:13
  |
3 |     let mut x = 10;
  |             ^
  |
  = help: maybe it is overwritten before being read?
  = note: `#[warn(unused_assignments)]` on by default

warning: 1 warning emitted
```
Đấy là do khi khai báo đầu tiên `x` là `10` như bạn không sử dụng thôi, không có gì quan trọng cả.

## Variables Type

### Scalar Types
> Kiểu _vô hướng_

Kiểu vô hướng đại diện cho một giá trị duy nhất. Rust có bốn loại vô hướng chính: `integers` _(số nguyên)_, `floating-point numbers` _(số dấu phẩy động)_, `Booleans`, vả `characters` _(ký tự)_. Diều này cũng bắt gặp ở rất nhiều các ngôn ngữ lập trình khác.

#### Integer Types

| Length  | Signed |	Unsigned
|:-|:-|:-|
| 8-bit   | i8	  | u8    |
| 16-bit  | i16	  | u16   |
| 32-bit  | i32	  | u32   |
| 64-bit  | i64	  | u64   |
| 128-bit | i128  | u128  |
| arch    | isize | usize |

Ví dụ:

```rust
let x:i32 = 10;
```

Trong bảng trên, các số nguyên đều có kích thước rõ ràng  rồi trừ có `isize` và `usize` có độ dài là `arch`, tức là nó phụ thuộc vào kích thước thanh ghi. Nếu hệ điều hành là `32-bit` thì độ dài của nó sẽ là `32-bit`, tương tự với `64-bit`.

Ngoài việc có thể khai báo trực tiếp, các số nguyên còn có thể khai báo ở nhiều dạng khác nhau theo như bảng dưới đây:

| Chữ số | Ví dụ |
| :------------------------------ | :---------- |
| Số thập phân                    | 98_222      |
| lục giác                        | 0xff        |
| bát phân                        | 0o77        |
| nhị phân                        | 0b1111_0000 |
| Byte _(chỉ cho phép với `u8`)_  | b'A'        |

Ví dụ với dòng đầu - _số thập phân_ - có thể sử dụng dấu `_` để ngăn cách giữa các số mà không ảnh hưởng, việc này là để hỗ trợ viết các số quá dài, còn về bản chất số không đổi. Ví dụ:

```rust
let x:i64 = 100_000_000_000;
```

Lúc này giá trị của `x` sẽ là `100000000000`, có điều nếu để nguyên nhìn sẽ rất khó nhìn ra nó là 100 tỉ.

#### Floating-Point Types

Số thập phân chi có 2 dạng là `f32` và `f64`, khai báo tương tự.

#### The Boolean Type

Số thập phân chi có 1 dạng là `bool`.

#### The Character Type

Số thập phân chi có 1 dạng là `char`.

Và lưu ý là nó tương đương với `4 byte` ở dạng `UTF` bình thường, không phải dàng cho các ký tự đặc biệt. Vì thế không thể dùng để khai báo cho các ký tự đặc biệt. Chẳng hạn bộ chữ Trung Quốc sẽ cần một bộ ký tự mở rộng vì `4 byte` không đủ để địng nghĩa cho toàn bộ ký tự tiếng Trung.
