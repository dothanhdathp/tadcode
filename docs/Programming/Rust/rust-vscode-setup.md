# Rust VSCode Setup

Cài đặt cho VSCode để lập trình Rust, lý do đơn giản là vì mình đang khá quen thuộc với IDE này.

## Thiết Lập Cài Đặt

- Mở phần cài đặt của VScode với tổ hợp phím `Ctrl+K` và `Ctrl+S`
- Tìm đến hai dạng lệnh sau **Run Build Task** và **Run Test Task**.
- Cài đặt tổ hợp phím cho hai chức năng, với mình thường là thế này:
	- _**Run Build Task**_ = `Ctrl+Shift+B`
	- _**Run Test Task**_ = `Ctrl+Shift+Q`

## Cài Đặt Task

Thiết lập cho mỗi Task được để trong tệp `.vscode/tasks.json`. Nội dung tệp đó như này:

```text
{
	// See https://go.microsoft.com/fwlink/?LinkId=733558
	// for the documentation about the tasks.json format
	"version": "2.0.0",
	"tasks": [
		{
			"label": "Rust Build",
			"type": "shell",
			"linux": {
				"command": "cargo build",
			},
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"isBackground": true,
		},
		{
			"label": "Run Project",
			"type": "shell",
			"command": "cargo run",
			"group": {
				"kind": "test",
				"isDefault": true
			},
			"presentation": {
				"reveal": "always",
				"panel": "new"
			}
		}
	],
}
```

Vì là cấu hình tùy chỉnh nên mình mới để thê