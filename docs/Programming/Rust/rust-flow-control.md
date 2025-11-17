# \[Rust\] Điều Khiển Luồng

## If/Else

```rust
fn main() {
	let cond = true;
	if cond {
		println!("True")
	} else {
		println!("False")
	}
}
```
```text title="Kết Quả"
True
```

!!! failure "Failure"
	Khác với __C/C++__, điều kiện không được là số, phải là dạng nhị phân. Nếu thay `let cond = 1` thì chắc công cụ dựng sẽ báo lỗi.

## Vòng Lặp

### Loop

```rust
fn main() {
	let mut cond = 100;
	loop {
		cond -= 1;
		if cond == 0 {
			break;
		}
	}
	println!("cond: {}", cond)
}
```
```text title="Kết Quả"
cond: 0
```

- Khai báo vòng lặp với __*loop*__
- Vòng lặp sẽ liên tục cho đến khi có lệnh gọi __*break*__
- `cond -= 1` là bước hạ một đơn vị cho biến `cond`

### While

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

## For

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

## Match

Giải pháp thay thế cho `switch/case`

```rust
fn main() {
	for number in 0..20 {
		print!("number = {} --> ", number);
		match number {
			1 => println!("One"),
			2 => println!("Two"),
			3 => println!("Three"),
			4 | 5 | 6 | 7 | 8 | 9 | 10 => println!("Four to Ten"),
			_ => println!("Another Number!"),
		}
	}
}
```
```text title="Kết Quả"
number = 0 --> Another Number!
number = 1 --> One
number = 2 --> Two
number = 3 --> Three
number = 4 --> Four to Ten
number = 5 --> Four to Ten
number = 6 --> Four to Ten
number = 7 --> Four to Ten
number = 8 --> Four to Ten
number = 9 --> Four to Ten
number = 10 --> Four to Ten
number = 11 --> Another Number!
number = 12 --> Another Number!
number = 13 --> Another Number!
number = 14 --> Another Number!
number = 15 --> Another Number!
number = 16 --> Another Number!
number = 17 --> Another Number!
number = 18 --> Another Number!
number = 19 --> Another Number!
```