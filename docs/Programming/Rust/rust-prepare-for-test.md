# Prepare for Test

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

### Với VSCode

Cách khác là có thể cài trực tiếp lệnh vào dự án riêng tạo bởi **VS Code**. Cách này khá tiện để thử cho các dự án nhỏ.

Trong dự án tạo một thư mục ngoài cùng tên là `.vscode`. Trong đó tạo một tệp là `tasks.json`.

Dán nội dung dưới này vào:

```json
{
	// See https://go.microsoft.com/fwlink/?LinkId=733558
	// for the documentation about the tasks.json format
	"version": "2.0.0",
	"tasks": [
		{
			"label": "Rust Build",
			"type": "shell",
			"linux": {
				"command": "rustc main.rs",
			},
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"isBackground": true,
		}
	]
}
```

Trong trường hợp muốn sửa gì đó có thể thay lệnh trong **command** là được.