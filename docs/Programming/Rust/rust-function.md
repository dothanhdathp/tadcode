# \[Rust\] Hàm

## Định Nghĩa

- Hàm là khái niệm một tập hợp logic thực hiện một chức năng riêng biệt được đặt tên và có thể sử dụng lại.
- `main()` cũng là một hàm, __luôn được thực hiện đầu tiên__
- __Rust__ quy định hàm nên được viết bằng chữ thường, theo kiểu __Snake Case__, các từ được phân biệt bằng dấu _gạch dưới_ (`_`)
    - Nếu không thì cũng không sao, __Compiler__ chỉ đưa ra thông báo thôi.

## Khai Báo

### Một Hàm Thông Thường

```rust
fn say_hi() {
    println!("Hi!");
}

fn main() {
    println!("Hello!");
    say_hi();
}
```

### Đối Số Nguyên Thuỷ

Các loại dữ liệu nguyên thuỷ không có vấn đề gì

```rust
fn get_input_number(i: i32) {
    println!("Input Number:: {}", i);
}
```

### Đối Số Phức Hợp

#### Đối Số Tuple

Tuple và Mảng cũng có thể tương tác như các dữ liệu nguyên thuỷ mặc dù cấu tạo dữ liệu phức tạp hơn.

```rust title="Hàm đảo ngược giá trị của một Tuple dạng pair"
fn reverse_pair(pair: (i32, bool)) -> (bool, i32) {
    let (first, last) = pair;
    return (last, first);
}
```

> [Rust Example Primitives - Tuples](rust-example-primitives.md#tuples)


#### Đối Số Mảng

Ví dụ về việc đưa mảng làm đối số của một hàm.

```rust title="Hàm đọc giá trị đầu tiên và độ dài chuỗi"
fn analyze_array(slice: &[i32]) {
    println!("First element of the slice: {}", slice[0]);
    println!("The slice has {} elements", slice.len());
}
```

Khác với __Tuple__, bạn phải truy cập vào mảng thông qua tham vấn, tức là ở địa chỉ bộ nhớ gốc của mảng. Nếu ta tác động sửa đổi lên mảng là đã thay đổi mảng gốc.

```rust
fn main() {
    let a = [1,2,3,4,5];
    analyze_array(&a);
}
```

## Truyền Tham Chiếu & Truyền Tham Trị

Nếu chưa biết __Tham Trị & Tham Vấn__ là gì thì đọc bài này [Tham Chiếu Và Tham Trị](../../Common/tham-chieu-va-tham-tri.md)

### Truyền Tham Chiếu

```rust
fn dosomething(mut input: i32) -> i32 {
    input = 1000;
    return input;
}

fn main() {   
    let mut i = 0;
    let r = dosomething(i);
    println!("i = {}; result = {}", i, r);
}
```
```text title="Kết Quả"
i = 0; result = 1000
```

### Truyền Tham Trị

```rust
fn dosomething(input: &mut i32) {
    *input = 1000;
}

fn main() {
    let mut i = 0;
    dosomething(&mut i);
    println!("i = {}", i);
}
```
```text title="Kết Quả"
i = 1000;
```