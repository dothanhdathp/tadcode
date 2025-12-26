# \[Rust\] Tuples

> Nhiều dạng dữ liệu khác nhau được tập hợp lại với nhau gọi là __Tuples__

Tính chất:

- Tập hợp của các biến có kiểu dữ liệu. Chúng có thể cùng hoặc khác kiểu.
- Các phần tử được đánh thứ tự từ `0`.
- __Tuples__ có độ dài cố định. Không thể thêm hoặc bớt phần tử ra khỏi __Tuples__ trong quá trình chạy.
- Các giá trị của tuple được bao bọc trong dấu __ngoặc đơn__ và phân cách với nhau bằng __dấu phẩy__.
- __Tuples__ có thể được khai báo tự động. Tức là nếu không có thêm yêu cầu về kiểu, nó sẽ chạy theo hướng 

## Khai Báo

### Khai Báo Tự Động

Với cách khai báo tự động, các kiểu sẽ được tự động lựa chọn kiểu theo luật.

```rust
fn main() {
    let tup = (500, 6.4, 1);
}
```

### Khai Báo Thủ Công

Với cách khai báo thủ công sẽ phải thêm kiểu vào cho từng thành phần của __Tuples__. Khuyến nghị nên dùng cách khai báo này để tránh trường hợp bị vượt ngưỡng hoặc là vượt ngưỡng khoảng giá trị. Đồng thời làm rõ mục đích sử dụng của các phần tử của __Tuples__ hơn.

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

## Truy Vấn Giá Trị

### Truy Vấn Bằng Chỉ Số

Các phần tử trong __Tuples__ được đánh dấu với chỉ số bắt đầu từ `0` cho phần tử đầu tiên. Truy vấn giá trị của các phần tử qua chỉ số bằng dấu `.`.

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let x = tup.0;
    let y = tup.1;
    let z = tup.2;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```

### Truy Vấn Bằng Cụm Biến

Với một tập hợp các biến có cùng số lượng phần tử và được đặt trong dấu `()` có thể trực tiếp trích xuất giá trị các biến trong một __Tuples__ thông qua việc gán nó với giá trị của __Tuples__. Cụm biến sẽ có giá trị tương đương. Ví dụ:

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x,y,z) = tup;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```

## In Dữ Liệu

__Tuples__ vẫn là kiểu biến nguyên thủy thế nên các phương thức IO cơ bản có hoạt động với __Tuples__. Nhưng chú ý <mark>phương thức IO cơ bản không in được tuple quá 12 thành phần</mark>. _(Điều này thật là vớ vẩn, làm không đến nơi đến chốn)_.

Để có thể in thì thay vì sử dụng `{}` thì sẽ dùng `{:?}` với ý nghĩa là dạng dữ liệu tự do cần xác định.

```rust
let tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
println!("f = {:?}", tup);
```

Nếu muốn in đầy đủ, có thể sử dụng [Truy Vấn Giá Trị](#truy-van-gia-tri) và in từng thành phần.

## Tuple in Tuple

> Có thể lồng nhiều Tuples lại với nhau.

```rust
let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);
```

!!! danger "Số Lượng"
    __Tuple__ không có phương thức lấy về số lượng phần tử.