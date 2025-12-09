# \[Rust\] Biến Phức Hợp

> Kiểu dữ liệu tập hợp của nhiêu kiểu biến dạng [Scalar](rust-variables-scalar-types.md)

## Định Nghĩa

- Dạng phức hợp có thể hiểu chính xác là tập hợp của các kiểu  __Scalar__.
- Nó sẽ hành xử và có tính chất như một tâpj hợp cấu trúc.
- Để so sánh với các ngôn ngữ bậc thấp và trung khác thì nó kiểu như __*array*__ hoặc __*struct*__. Việc dữ liệu này được đưa vào làm một trong các dạng nguyên thủy làm mình có phần bối rối. Các dạng thức tập hợp hơi khó để thực hiện với các phương thức tính toán cơ bản.

## Kiểu Phức Hợp

Có ba kiểu phức hợp chính là:

- [Tuples](#Tuples): Là dạng _cấu trúc_ gồm nhiều loại dữ liệu khác nhau được tập hợp với nhau. Nó có phần giống với __*struct*__ của C++.
- [Array](#Array): Dạng chuỗi cơ bản có yêu cầu về độ dài. Tương tự với các kiểu chuỗi cơ bản trong các ngôn ngữ lập trình khác.
- [Slices](#Slices): Giống như chuỗi nhưng không có yêu cầu về độ dài. Việc hoạt động của chuỗi này có lẽ giống kiểu __*vector*__ trong C++.

## Tuples

> Nhiều dạng dữ liệu khác nhau được tập hợp lại với nhau gọi là __Tuples__

Tính chất:

- Tập hợp của các biến có kiểu dữ liệu. Chúng có thể cùng hoặc khác kiểu.
- Các phần tử được đánh thứ tự từ `0`.
- __Tuples__ có độ dài cố định. Không thể thêm hoặc bớt phần tử ra khỏi __Tuples__ trong quá trình chạy.
- Các giá trị của tuple được bao bọc trong dấu __ngoặc đơn__ và phân cách với nhau bằng __dấu phẩy__.
- __Tuples__ có thể được khai báo tự động. Tức là nếu không có thêm yêu cầu về kiểu, nó sẽ chạy theo hướng 

### Khai Báo

#### Khai Báo Tự Động

Với cách khai báo tự động, các kiểu sẽ được tự động lựa chọn kiểu theo luật.

```rust
fn main() {
    let tup = (500, 6.4, 1);
}
```

#### Khai Báo Thủ Công

Với cách khai báo thủ công sẽ phải thêm kiểu vào cho từng thành phần của __Tuples__. Khuyến nghị nên dùng cách khai báo này để tránh trường hợp bị vượt ngưỡng hoặc là vượt ngưỡng khoảng giá trị. Đồng thời làm rõ mục đích sử dụng của các phần tử của __Tuples__ hơn.

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

### Truy Vấn Giá Trị

#### Truy Vấn Bằng Chỉ Số

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

#### Truy Vấn Bằng Cụm Biến

Với một tập hợp các biến có cùng số lượng phần tử và được đặt trong dấu `()` có thể trực tiếp trích xuất giá trị các biến trong một __Tuples__ thông qua việc gán nó với giá trị của __Tuples__. Cụm biến sẽ có giá trị tương đương. Ví dụ:

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x,y,z) = tup;
    println!("x = {}, y = {}, z = {}", x,y,z);
}
```

### In Dữ Liệu

__Tuples__ vẫn là kiểu biến nguyên thủy thế nên các phương thức IO cơ bản có hoạt động với __Tuples__. Nhưng chú ý <mark>phương thức IO cơ bản không in được tuple quá 12 thành phần</mark>. _(Điều này thật là vớ vẩn, làm không đến nơi đến chốn)_.

Để có thể in thì thay vì sử dụng `{}` thì sẽ dùng `{:?}` với ý nghĩa là dạng dữ liệu tự do cần xác định.

```rust
let tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
println!("f = {:?}", tup);
```

Nếu muốn in đầy đủ, có thể sử dụng [Truy Vấn Giá Trị](#truy-van-gia-tri) và in từng thành phần.

### Tuple in Tuple

> Có thể lồng nhiều Tuples lại với nhau.

```rust
let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);
```

!!! danger "Số Lượng"
    __Tuple__ không có phương thức lấy về số lượng phần tử.

## Mảng

Mảng là kiếu phức hợp thứ hai, là tập hợp các giá trị có cùng một kiểu được tập hợp lại thành một mảng với độ dài xác định.

- Tập các giá trị có cùng một kiểu.
- Kích thước xác định. Không thể thay đổi sau khi khai báo.
- Các giá trị của mảng được bao bọc trong dấu __ngoặc vuông__ và phân cách với nhau bằng __dấu phẩy__.
- Nhìn chung thì cách thức vận hành của __Mảng__ khá là giống với cách thức vận hàng của __Tuples__ với các phần tử có cùng kiểu.

### Khai Báo

#### Khai Báo Tự Động

Khai báo tự do giống như cách khai báo với __Tuples__. Nếu các dữ liệu có cùng kiểu nó sẽ được chuyển về dạng __Array__ thông qua quá trình tự động xác định kiểu.

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
}
```

#### Khai Báo Thủ Công

Khai báo thủ công với cấu trúc `[T; length]` với `T` là kiểu là `length` là độ dài của chuỗi. Ví dụ này là khai báo một chuỗi có 5 phần tử với dạng số nguyên __32-bít__.

```rust
fn main() {
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
}
```

Nếu muốn khởi tạo mảng với các giá trị mặc định giống nhau thì làm như dưới đây:

```rust
fn main() {
    let arr: [i32; 500] = [0; 500];
}
```

- _Mảng trên có 500 phần tử với giá trị là `0`_

### Truy Vấn Giá Trị

Truy vấn giá trị trong Array có điển khác với __Tuples__. Về việc khác nhau này có thể hiểu nó gần giống như cách thức truy vấn ở các ngôn ngữ cổ điển như __C/C++__, đó là truy vấn địa chỉ bằng dấu `[i]` với __*i*__ là _index_ bắt đầu từ `0`


```rust
fn main() {
    let arr_static = [1, 2, 3, 4, 5];
    println!("By hand: {}, {}, {}, {}, {}",
        arr_static[0],
        arr_static[1],
        arr_static[2],
        arr_static[3],
        arr_static[4]
    );
}
```

### Độ Dài Chuỗi

Lấy độ dài của chuỗi với `len()`

```rust
fn main() {
    let arr: [i32; 1000] = [0; 1000];
    println!("Length of array: {}", arr.len());
}
```
```text title="Kết Quả"
Length of array: 1000
```

### In Dữ Liệu

Kết xuất dữ liệu ra cổng IO của chuỗi cũng được hỗ trợ tương tự như __Tuples__, đó là sử dụng `{:?}` là có thể in được toàn bộ chuỗi mà không cần thiết phải truy cập từng phẩn tử. Việc này cũng giúp ích khá nhiều.

__Array__ không có giới hạn về độ dài chuỗi nên không phải lo về số lượng.

```rust
fn main() {
    let arr_static = [1, 2, 3, 4, 5];
    println!("Auto: {:?}", arr_static);
}
```

