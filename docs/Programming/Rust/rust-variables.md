# \[Rust\] Biến

> Biến là thành phần cơ bản trong mọi ngôn ngữ lập trình.

## Định Nghĩa

- __Biến__ là thành phần cơ bản trong mọi ngôn ngữ lập trình.

## Phân Loại

Các kiểu biến chia làm hai loại chính là __*Primitives*__ _(tức kiểu biến nguyên thuỷ sẽ được hỗ trợ trực tiếp từ **complier** mà không cần thiết phải thêm thư viện ngoài)_ và __*Non Primitives*__ là các kiểu còn lại, có thể do người dùng tự định nghĩa hoặc thư viện sẽ hỗ trợ.

__Primitives__ cũng chia làm hai loại:

- [Scalar Types](rust-scalar-types.md) _(Biến Đơn Hướng)_
- [Compound Types](rust-compound-types.md) _(Biến Phức Hợp)_

!!! warning "Chú Ý"
    Các phần tiếp theo cần nghiên cứu một chút ở kiểu biến [Scalar Types](rust-scalar-types.md). Hãy đọc qua nếu khó hiểu.

## Khai Báo Biến

Để tạo một biến sử dụng `let`:

```rust
let x = 10;
```

* Biến được khởi tạo nhưng không thể thay đổi tức là nếu cố gán lại giá trị khác vào `x` sẽ gây ra lỗi. Muốn biến có khả năng sửa đổi, khai  báo thêm với `mut` tượng trưng cho __*mutable*__

```rust
let x = 10;
x = 20; // complie error
```

```rust
let mut x = 10;
x = 20; // ok
```

## Tính Tự Động

### Tự Động Chọn Kiểu

Biến trong Rust sẽ được tự động lựa chọn kiểu phù hợp nếu không được khai báo mặc định. Tiến trình này cũng khá là giống __Python__. Ví dụ như:

```rust
let x = 10;
let y:i32 = 10;
```

Cả hai biến __*x*__ và __*y*__ sẽ đều có cùng kiểu là __*interger 32 bits*__ `i32`. Có thể dùng chương trình dưới đây để kiểm tra loại của biến

```rust
use std::any::type_name;

fn print_type_of<T>(_: &T) {
    // This prints the type name T is at runtime.
    println!("Type is: {}", type_name::<T>());
}

fn main() {
    let x = 10;
    let y:i32 = 10;
    print_type_of(&x);
    print_type_of(&y);
}
```
```text title="Kết Quả"
Type is: i32
Type is: i32
```

### Kiểu Tự Động Mặc Định

Các kiểu biến tự động cũng có __mặc định__.

- Số Nguyên (Interger): `i32`
- Số Thực (Float): `f64` _(Theo tiêu chuẩn IEEE-754)_
- _Các kiểu **bool** và **char** thì không có kiểu dữ liệu mở rộng nào khác nên bỏ qua._

!!! question "Câu hỏi"
    - ❓ Khi đầu vào khai báo vượt ngưỡng dữ liệu cơ bản thì sao?
        - Lúc đó trình biên dịch sẽ có thông báo cảnh báo viết khai báo rõ ràng cho loại dữ liệu. __Rust__ không có kiểu _ngầm hiểu_ trong trường hợp này. Với các kiểu dữ liệu khi đã thoát khỏi quy chuẩn thì sẽ để người dùng tự định nghĩa.
    - ❓ Nếu các phép toán gây vượt quá ngưỡng đầu vào thì sao?
        - Trình biên dịch không biết, tự làm thôi.
    
## Tương Tác

Các dạng thức tương tác với biến bao gồm:
- [Phương Thức - Operator](rust-operator.md) sẽ có thể thay đổi giá trị của các biến.
- [Điểu Khiển Luồng](rust-flow-control.md) sử dụng các biến dạng _boolean_ để xác định các luồng hoạt động cho chương trình.
- [Hàm](rust-function.md) sẽ sử dụng cả hai phương thức trên. Lấy biến làm đối số và thực hiện các tương tác đưa ra kết quả hoặc phục vụ mục địch nào đó.
