# \[Rust\] Match

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