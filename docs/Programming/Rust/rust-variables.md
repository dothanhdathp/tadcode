# \[Rust\] Biến

## Định Nghĩa

- Biến đại diện cho dữ liệu có thể sử dụng tính toán.

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

## Kiểu Nguyên Thuỷ

### Kiểu Nguyên Thuỷ

Như mọi ngôn ngữ, các kiểu biến nguyên thuỷ được hỗ trợ là số __*tự nhiên*__, __*số thực*__, __*boolean*__ _(logic so sánh)_ và kiểu __*ký tự*__.

__Các kiểu nguyên thuỷ và kích thước__:

|                   | 8-bit  | 16-bit | 32-bit | 64-bit | 128-bit |
| :---------------- | :----: | :----: | :----: | :----: | :-----: |
| Interger          |  `i8`  | `i16`  | `i32`  | `i64`  | `i128`  |
| Unsigned Interger |  `u8`  | `u16`  | `u32`  | `u64`  | `u128`  |
| Float             |        |        | `f32`  | `f64`  |         |
| Boolean           | `bool` |        |        |        |         |
| Character         |        |        | `char` |        |         |

- Ngoài các số nguyên kể trên còn có hai loại là `isize` và `usize`. Hai kiểu này không có kích thước cụ thể mà nó sẽ phụ thuộc vào kiến trúc vi xử lý _(`64-bit` hoặc `32-bit`)_
- Các số thực được sử dụng theo chuẩn __IEEE-754__, nghĩa __*số thập phân luôn là số có dấu*__.
- <mark>Kiểu ký tự trong Rust được mở rộng lên _4 bytes_</mark>, cho phép nó hiển thị được nhiều ký tự hơn so với bảng mã __ASCII__ thông thường.
- Ký tự trong __Rust__ yêu cầu khai báo trong dấu `'`, dấu `"` không chấp nhận.

### Khoảng Giá Trị

Cũng như các loại giá trị khác, thường __Số Nguyên Có Dấu__ sẽ có khoảng giá trị từ $[(-2^{N-1}) \to (2^{N-1}-1)]$, với $N$ là số `bits` mà biến đó có thể sử dụng. Ví dụ với `i32` (thường sử dụng nhất) sẽ có khoảng giá trị là $[(-2^{31}) \to (2^{31}-1)]$ hay cụ thể là từ $[-2,147,483,647 \to 2,147,483,646]$.

Với __Số Nguyên Không Dấu__, khoảng giá trị được mở rộng lên $[0 \to 2^{N}-1]$. Đại biểu với `u32` sẽ là $[0 \to 4,294,967,295]$

### Một Số Cách Viết Khác

Ngoài việc có thể khai báo trực tiếp, các số nguyên còn có thể <mark>khai báo ở nhiều dạng khác nhau</mark> theo như bảng dưới đây:

| Chữ số                         | Ví dụ         | Ví dụ                                                           |
| :----------------------------- | :------------ | :-------------------------------------------------------------- |
| Số thập phân                   | `98_222`      | *Các chữ số có thể dùng dấu _ để phân cách khi viết các số lớn* |
| Thập lục phân                  | `0xff`        |                                                                 |
| bát phân                       | `0o77`        |                                                                 |
| nhị phân                       | `0b1111_0000` |                                                                 |
| Byte _(chỉ cho phép với `u8`)_ | `b'A'`        |                                                                 |
| Float                          | `1e2`         |                                                                 |

```rust title "Ví dụ"
let x:i64 = 100_000_000_000; // 100000000000
```

## Tính Tự Động

Biến trong Rust sẽ được tự động lựa chọn kiểu phù hợp nếu không có khai báo kiểu từ đầu.

## Khai Báo Kiểu

Khai báo kiểu có thể sử dụng khai báo trước hoặc sau:

```rust
let x: u32 = 10;
let y = 10u32;
```

> Cả hai cách trên đều hợp lệ.
> - Cách 1 khai báo kiểu `u32` cho biến __x__
> - Cách 2 khai báo kiểu `u32` cho giá trị `10`. Lúc này giá trị của biến bị ép sang kiểu của biến.

Xem ví dụ: [Rust Example Primitives](rust-example-primitives.md#primitives)

## Tác Dụng

- Để thực hiện tính toán trên biến thường sử dụng các [Phương Thức](rust-operator.md) hoặc sử dụng để [Điểu Khiển Luồng](rust-flow-control.md)
- Khi các phép tính và điều khiển quá lớn cho một mục đích, các biến sẽ được sử dụng là các đối số cho [Hàm](rust-function.md)

> Bài Tiếp: [Biến Phức Hợp](rust-compound-variables.md)

