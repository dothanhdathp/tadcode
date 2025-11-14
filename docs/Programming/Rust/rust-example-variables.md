# \[Rust\] Example<br>Variables

## Các Loại Biến Nguyên Thuỷ

### Tự Động

```rust
let x = 42; // i32
let y = 6.24; // f64
let z = false; // bool
```
### Kê Khai Kiểu

```rust
let x:i32 = 42;
let y:f64 = 6.24;
let z:bool = false;
```

### Kích Thước Bộ Nhớ

```rust
fn main() {
    let x = 42;
    let y = 6.24;
    let z:bool = false;
    let x_size = mem::size_of_val(&x);
    let y_size = mem::size_of_val(&y);
    let z_size = mem::size_of_val(&z);
    println!("Size of x is {} bytes", x_size);
    println!("Size of y is {} bytes", y_size);
    println!("Size of z is {} bytes", z_size);
}
```

```text title='Kết Quả'
Size of x is 4 bytes
Size of y is 8 bytes
Size of z is 1 bytes
```

## Biến Phức Hợp

```rust
fn main() {
    let tup = (5, 10.22, true);
    let (x, y, z) = tup;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```

```text title="Kết Quả"
x = 5, y = 10.22, z = true
```