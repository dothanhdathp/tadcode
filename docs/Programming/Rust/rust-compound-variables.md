# \[Rust\] Biến Phức Hợp

Là kiểu dữ liệu được tạo nên từ nhiều biến khác nhau nhưng vẫn tồn tại như là một biến. Một kiểu tập hợp có thể chứa các loại biến có cùng kiểu, hoặc khác kiểu. Ứng với nó chính là hai kiểu cơ bản tên là __tuples__ and __arrays__.

## Tuples

### Khai Báo

__Tuple Là:__

- Một nhóm các biến có loại khác nhau.
- Có độ dài cố định _(kích thước không thể thay đổi)_
- Các giá trị của tuple được bao bọc trong dấu __ngoặc đơn__ và phân cách với nhau bằng __dấu phẩy__.

#### Khai Báo Tự Do

```rust
fn main() {
    let tup = (500, 6.4, 1);
}
```

#### Khai Báo Có Kiểu

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

### Truy Vấn Giá Trị

Sử dụng một cụm biến có dạng tương đương để khớp với các thành phần trong __Tuple__

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x,y,z) = tup;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```

Hoặc truy cập trực tiếp vào từng phần tử thông qua dấu `.` và chỉ số.

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let x = tup.0;
    let y = tup.1;
    let z = tup.2;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```
### Tuple Có Thể In

```rust
let tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
println!("f = {:?}", tup);
```

!!! warning "Chú ý"
    Phương thức In cơ bản không in được tuple quá 12 thành phần

### Tuple in Tuple

```rust
let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);
```

!!! danger "Số Lượng"
    __Tuple__ không có phương thức lấy về số lượng phần tử.

### Ví Dụ

- [Xem Rust Example Primitives : Tuples](rust-example-primitives.md#tuples)

## Mảng

### Khai Báo

Mảng là kiếu phức hợp thứ hai, là:

- Tập các giá trị có cùng một kiểu.
- Kích thước xác định. Không thể thay đổi sau khi khai báo.
- Các giá trị của mảng được bao bọc trong dấu __ngoặc vuông__ và phân cách với nhau bằng __dấu phẩy__.

#### Khai Báo Tự Do

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
}
```
#### Khai Báo Cụ Thể

- Tạo Mảng có kiểu là `i32` và có `5` phần tử.

```rust
fn main() {
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
}
```

- Kiểu là `i32` và có `5` phần tử.

#### Khai Báo Và Khởi Tạo

> Tạo mảng 500 phần tử có độ lớn bằng 0

```rust
fn main() {
    let arr: [i32; 500] = [0; 500];
}
```

```rust "Code Kiểm Tra"
fn main() {
    let arr: [i32; 500] = [0; 500];
    for i in arr {
        print!("{} ", i)
    }
}
```

### Ví Dụ

- [Xem Rust Example Primitives : Arrays and Slices](rust-example-primitives.md#arrays-and-slices)

!!! info "Info"
    - Cả __Tuple__ và __Mảng__ đều có thể làm đối số truyền vào cho [Hàm](rust-function.md)
    - [Rust Example Primitives](rust-example-primitives.md#tuples)