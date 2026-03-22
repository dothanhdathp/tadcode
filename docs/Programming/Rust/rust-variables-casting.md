# Rust Casting

> Hướng dẫn chuyển đổi kiểu dữ liệu trong Rust

## Tóm Tắt

- Ép kiểu dùng as
	```text
	let var:u8 = 1000 as i32;
	```

## Giới Hạn

- Như mọi bài khác về giới hạn, độ dài bit các số giới hạn độ lớn mà một biến có thể chứa được. Ví dụ với các số dạng `1 byte` thường chỉ có giới hạn đến `255`, các số `2 byte` có giới hạn lên đến `65535`
- Như vậy phép biến đổi sau đây là bất hợp lệ vì số **1000** là vượt quá ngưỡng của của số `u8`.

```rust
fn main() {
    println!("1000 as a u16 is: {}", 1000 as u16);
}
```

Lúc này trình biên dịch sẽ có thông báo như sau:

```text
error: literal out of range for `u8`
 --> src/main.rs:5:35
  |
5 |     println!("1000 as a u8 is : {}", 1000 as u8);
  |                                      ^^^^
  |
  = note: the literal `1000` does not fit into the type `u8` whose range is `0..=255`
  = note: `#[deny(overflowing_literals)]` on by default

error: could not compile `hello-world` (bin "hello-world") due to previous error
```

## Ép Kiểu

Khi này nếu muốn ép chương trình phải thục thi hành động _**casting**_ nguy hiểm, sửa lại chương trình như sau:

```rust
// Suppress all errors from casts which overflow.
#![allow(overflowing_literals)]

fn main() {
	println!("1000 as a u8 is : {}", 1000 as u8);
}
```
```text title="Kết Quả"
1000 as a u8 is : 232
```

Tại sao lại vậy? Vì biểu diễn nhị phân của 1000 là `0000 0011 1110 1000`, khi rút gọn còn 1 byte (2 bit) thì sẽ thành `1110 1000` = 232.

Quá trình ép kiểu cũng thực hiện được với các quá trình khai báo như này, khi đó không có quá trình cảnh báo. Trình biên dịch của Rust mặc định lập trình viên hiểu mình đang làm gì và không đưa ra thông báo.

_Đây là điều mình đánh giá khá cao. Hầu hết các thông báo đều chỉ ra những lỗi mà người lập trình ít để ý. Bao phủ hết các cảnh báo sẽ giúp chương trình hoạt động ổn định._

```rust
fn main() {
	let var_i32:i32 = 1000;
	let var_u8:u8 = var_i32 as u8;

	println!("var_i32 : {}", var_i32);
	println!("var_u8  : {}", var_u8);
}
```
```text title="Kết Quả"
var_i32 : 1000
var_u8  : 232
```