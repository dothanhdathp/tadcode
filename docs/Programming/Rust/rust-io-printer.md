# \[Rust\] Print

## Các hàm output

Các hàm in kết quả ra màn hình:

- `format!`: Viết văn bản được định dạng vào __String__
- `print!`: tương tự `format!` nhưng văn bản được in vào bảng điều khiển (`io::stdout`).
- `println!`: tương tự `print!` nhưng một dòng mới được nối thêm.
- `eprint!`: tương tự `print!` nhưng văn bản được in ra lỗi tiêu chuẩn (`io::stderr`).
- `eprintln!`: tương tự `eprint!` nhưng một dòng mới được nối thêm.

Ví dụ:

```rust
fn main() {
    println!("<< Line 0 >>");
    format!("<< Line 1 >>");
    print!("<< Line 2 >>");
    println!("<< Line 3 >>");
    eprint!("<< Line 4 >>"); // Print to port error
    eprintln!("<< Line 5 >>"); // Print to port error
}
```

Kết quả:

```txt
<< Line 0 >>
<< Line 2 >><< Line 3 >>
<< Line 4 >><< Line 5 >>
```

## Thứ tự in

Có các cách sau để in kết quả ra ngoài màn hình bằng `println!` _(các hàm khác như `print!`, `println!`, `eprint!`, `eprintln!`)_ cũng có cách xài tương tự.

- __*Cách 1*__: Giá trị của các biến sẽ được thay thế lần lượt bằng `{}`.
- __*Cách 2*__: Trong dấu `{index}` có thể được lựa chọn bằng _index_ được để trong đấu `{}`. Và nó sẽ chọn đúng vị trí được đánh theo số. Với vị trí được để sau trong mỗi dáu `{}` sẽ theo sau đúng với vị trí của biến theo sau chuỗi __*prompt*__.
- __*Cách 3*__: Có một cách khác là đưa vào theo tên và giá trị in ra tự động theo đúng như tên của biến được đặt.

```rust
fn main() {
    // Cách 1: Normal print
    println!("Output: {}", 0);
    // Cách 2: Print with index
    println!("Output: {1}, {0}, {2}, {1}", 0, 1, 2);
    // Cách 2: Print with object-name
    println!("Output: {var1}, {var0}, {var2}, {var1}", var0=0, var1=1, var2=2);
}
```

Kết quả:

```text
Output: 0
Output: 10, 0, 20, 10
Output: 10, 0, 20, 10
```

## Formatted Print

