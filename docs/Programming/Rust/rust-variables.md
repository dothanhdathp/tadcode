# \[Rust\] Biến

> Biến là thành phần cơ bản trong mọi ngôn ngữ lập trình.

## Định Nghĩa

- __Biến__ là thành phần cơ bản trong mọi ngôn ngữ lập trình.

## Khai Báo Biến

- Là ngôn ngữ bậc cao, biến trong __Rust__ là biến tự động chọn kiểu.
- Biến khởi động với `let` và `let mut` với:
    - `let`: biến không sửa đổi
    - `let mut`: biến có thể sửa đổi. _(mut có nghĩa là __mutable__)_

```rust
let x = 10;
let mut y = 10;
```

## Tự Động

Biến trong Rust sẽ được tự động lựa chọn kiểu để phù hợp. Các kiểu tự động đầu tiên là các kiểu ngầm định có sẵn trong mọi ngôn ngữ lập trình.

1. Số tự nhiên
1. Số phẩy động
1. Boolean
1. Ký tự
1. Chuỗi ký tự

### Xác Định Loại Ngầm Định

Để xác định loại ngầm định, sử dụng hàm dưới đây:

```rust
use std::any::type_name;

fn print_type_of<T>(_: &T) {
    println!("Type is: {}", type_name::<T>());
}
```

Ví dụ:

```rust
use std::any::type_name;

// This prints the type name T is at runtime.
fn print_type_of<T>(_: &T) {
    println!("Type is: {}", type_name::<T>());
}

fn main() {
    let auto_int = 0;
    let auto_float = 0.1;
    let auto_bool = true;
    let auto_char = '0';
    let auto_string = "Hello World!";

    print_type_of(&auto_int);
    print_type_of(&auto_float);
    print_type_of(&auto_bool);
    print_type_of(&auto_char);
    print_type_of(&auto_string);
}
```
```text title="Kết Quả"
Type is: i32
Type is: f64
Type is: bool
Type is: char
Type is: &str
```

Các kiểu tự động được xác định:

- Số Nguyên (Interger): `i32`
- Số Thực (Float): `f64` _(Theo tiêu chuẩn IEEE-754)_
- Các kiểu còn lại đều đơn nhất nên không có gì so sánh.
- __Ngầm định không tự thay đổi__: với biến _interger_ có thể mở rộng phạm vi bằng `i64`, nhưng __*Rust*__ không làm thế, đơn giản là vượt ngưỡng. Nói chung thì nó không tự động hoàn toàn. Các giá trị tự động là mặc định và không đổi.
   
## Phân Loại

Các kiểu biến cơ bản gồm có ba phân loại chính loại

- [Scalar Types](rust-scalar-types.md): _(Biến Đơn Hướng)_
- Compound Types: _(Biến Phức Hợp)_
- Custom Types: _(Kiểu Tự Định Nghĩa)_

## Tương Tác

Các dạng thức tương tác với biến bao gồm:

- [Phương Thức - Operator](rust-operator.md) sẽ có thể thay đổi giá trị của các biến.
- [Điểu Khiển Luồng](rust-flow-control.md) sử dụng các biến dạng _boolean_ để xác định các luồng hoạt động cho chương trình.
- [Hàm](rust-function.md) sẽ sử dụng cả hai phương thức trên. Lấy biến làm đối số và thực hiện các tương tác đưa ra kết quả hoặc phục vụ mục địch nào đó.