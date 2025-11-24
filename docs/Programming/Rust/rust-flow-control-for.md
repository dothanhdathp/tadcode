# \[Rust\] For

- __*for*__ là lệnh lặp trong một chuỗi số. Từ `a..b` thì nó sẽ từ `a` đến `b-1`. Ví dụ:

```rust
fn main() {
	for n in 1..10 {
		print!("{} ", n);
	}
}
```
```text title="Kết Quả"
1 2 3 4 5 6 7 8 9 
```

- __*for*__ cũng tương tác với mảng, có thể dùng để dượt một lượt tất cả thành phần trong màng.

```rust
fn main() {
	let arr = [1, 4, 12, 3, 11, 5, 1];
	for n in arr {
		print!("{} ", n);
	}
}
```
```text title="Kết Quả"
1 4 12 3 11 5 1 
```