# Rust Variable Binding

## Mutability

Biến trong Rust mặc định là kiểu _immutable (không cho phép sửa sau khi khai báo)_. Để sửa được biến phải thêm `mut`

```rust
fn main() {
	let a = 0;
	let mut b = 0;
	// a = 2; // Trình biên dịch sẽ báo lỗi ở dòng này
	b = 2;
	println!("a = {}; b = {}", a, b);
}
```
```text title="Kết Quả"
a = 0; b = 2
```

## Variable Binding
> Ràng buộc biến

Chương này giải thích về phân vùng của biến và cách Rust tổ chức phạm vi của biến.

- Trong Rust, các khu vực được đánh dấu bằng `{}`, mỗi phân vùng sẽ có khu vực và phạm vi biến riêng không liên quan đến nhau

Trong ví dụ này, cùng một tên biến là _**scope**_, khi được đặt ở trong `{}` sẽ được coi như ở phần vùng khác, không còn trong phạm vi dù trong cùng một hàm.

```rust
fn main() {
	let scope = 1;
	{
		let scope = "Another Value";
		println!("[inner] scope  = {}", scope);
	}
	println!("[outer] scope  = {}", scope);
}
```
```text title="Kết Quả"
[inner] scope  = Another Value
[outer] scope  = 1
```

## Declare first
> Khai báo trước

Có thể khai báo các liên kết biến trước và khởi tạo chúng sau, nhưng tất cả các liên kết biến phải được khởi tạo trước khi chúng được sử dụng: trình biên dịch cấm sử dụng các liên kết biến chưa được khởi tạo, vì nó sẽ dẫn đến hành vi không xác định.

Việc khai báo một liên kết biến và khởi tạo nó sau này trong hàm là điều không phổ biến. Người đọc sẽ khó tìm thấy phần khởi tạo hơn khi phần khởi tạo được tách khỏi phần khai báo. Người ta thường khai báo và khởi tạo một liên kết biến gần nơi biến sẽ được sử dụng.

```rust
fn main() {
    let a; // Create a
    {
        let x = 2;
        // Initialize a
        a = x * x;
    }
    println!("a binding: {}", a);
}
```

## Đóng Băng

Một biến _mutable_ của nó sẽ bị đóng băng khi bước vào một phạm vi khác và được ghi đè thành let. Khi này tính chất của biến thay đổi.

```rust
fn main() {
    let mut _mutable_integer = 7i32;
    {
        let _mutable_integer = _mutable_integer; // "_mutable_integer" bị thay đổi bản chất
        // _mutable_integer = 50; // "_mutable_integer" --> bị cấm sửa đổi. Mở dòng này trình biên dịch sẽ báo lỗi.
        println!("_mutable_integer = {}", _mutable_integer);
    }
    _mutable_integer = 3;
}
```
```text title="Kết Quả"
_mutable_integer = 7
```