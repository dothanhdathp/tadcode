# Match

> Giải pháp thay thế cho `switch/case`

## Match

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

## Match and Tuple

```rust
fn main() {
    let triple = (0, -2, 3);
    // TODO ^ Try different values for `triple`

    println!("Tell me about {:?}", triple);
    // Match can be used to destructure a tuple
    match triple {
        // Destructure the second and third elements
        (0, y, z) => println!("First is `0`, `y` is {:?}, and `z` is {:?}", y, z),
        (1, ..)  => println!("First is `1` and the rest doesn't matter"),
        (.., 2)  => println!("last is `2` and the rest doesn't matter"),
        (3, .., 4)  => println!("First is `3`, last is `4`, and the rest doesn't matter"),
        // `..` can be used to ignore the rest of the tuple
        _      => println!("It doesn't matter what they are"),
        // `_` means don't bind the value to a variable
    }
}
```