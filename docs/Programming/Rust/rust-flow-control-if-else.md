# If/Else

## Mặc Định

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

!!! danger "Danger"
	Khác với __C/C++__, <u>điều kiện không được là số</u>, phải là dạng nhị phân để đảm bảo tính logic.
	Nếu thay `let cond = 1` thì chắc công cụ dựng sẽ báo lỗi. (Không được mập mờ trong loại dữ liệu như C/C++).

## Trả Về

Rust cho phép if/else trả về trực tiếp như sau:

```rust
fn main() {
    let cond = true;
    let res = if cond {
        println!("True");
        // return
        123456789
    } else {
        println!("False");
        // return
        987654321
    };
    println!("res: {}", res);
}
```
```text title="Kết Quả"
True
res: 123456789
```

!!! warning "Warning"
	- Không có dấu `;` trong phần trả về. Đây là điều mình thấy khá là .. không thích.

## Short Return

Thay cho cơ chế `cond ? true : false` vốn tuy tiện dụng nhưng khá là khó đọc trong __C__ thì __Rust__ có:

```rust
fn main() {
    let cond = true;
    let res = if cond {1} else {0};
    println!("res: {}", res);
}
```
```text title="Kết Quả"
res: 1
```