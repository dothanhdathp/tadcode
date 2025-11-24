# \[Rust\] While

## Cơ Bản

- __*while*__ là lệnh lặp có điều kiện.
- Lệnh này tự động thoát không cần __*break*__
- Nếu điều kiện không được thỏa mãn, vòng `while` sẽ thoát.

```rust
fn main() {
	let mut cond = 100;
	while cond != 0 {
		cond -= 1;
	}
	println!("cond: {}", cond)
}
```
```text title="Kết Quả"
cond: 0
```

## Thoát Vòng Lặp

- Vòng __*while*__ cũng thoát khi có __*break*__

```rust
fn main() {
    let mut cond = 100;
    while cond != 0 {
        cond -= 1;
		if cond == 20 {
			break;
		}
    }
    println!("cond: {}", cond)
}
```
```text title="Kết Quả"
cond: 20
```

## Trả Về

__while__ không có tính năng trả về với __break__.