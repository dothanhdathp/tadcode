# \[Rust\] Phương Thức

## Các Phương Thức Cơ Bản

- `+`: Cộng
- `-`: Trừ
- `*`: Nhân
- `/`: Chia _(lấy nguyên)_
- `%`: Chia _(lấy dư)_

```rust
fn main() {
    let a = 5;
    let b = 2;

	println!("a + b: {}", a + b);
	println!("a - b: {}", a - b);
	println!("a * b: {}", a * b);
	println!("a / b: {}", a / b);
	println!("a % b: {}", a % b);
}
```

## Phương Thức Rút Gọn

```rust
fn main() {
    let mut val = 10;
	val += 1;
	println!("val: {}", val); // val = 11
	val -= 1;
	println!("val: {}", val); // val = 10
	val *= 2;
	println!("val: {}", val); // val = 20
	val /= 2;
	println!("val: {}", val); // val = 10
}
```
```text title="Kết Quả"
val: 11
val: 10
val: 20
val: 10
```