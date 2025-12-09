# \[Rust\] Prepare for Test

> Chuẩn bị một số thứ cần thiết để chạy thử

## Simple Source Code

Code mẫu lấy từ [Hello World](rust-example-helloworld.md). Lưu và __main.rs__

```rust title="main.rc"
fn main() {
    println!("Hello World!");
}
```

## Makefile

Tạo một tệp __*Makefile*__ đơn giản.

```makefile
RCC=rustc

main:
	rustc main.rs
mainr:
	rm -rf main
	rustc main.rs
mainre:
	rm -rf main
	rustc main.rs
	./main
```

- `make main`: Build
- `make mainr`: Rebuild
- `make mainre`: Rebuild + Test