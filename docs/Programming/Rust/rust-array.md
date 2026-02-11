# Mảng

Mảng là kiếu phức hợp thứ hai, là tập hợp các giá trị có cùng một kiểu được tập hợp lại thành một mảng với độ dài xác định.

- Tập các giá trị có cùng một kiểu.
- Kích thước xác định. Không thể thay đổi sau khi khai báo.
- Các giá trị của mảng được bao bọc trong dấu __ngoặc vuông__ và phân cách với nhau bằng __dấu phẩy__.
- Nhìn chung thì cách thức vận hành của __Mảng__ khá là giống với cách thức vận hàng của __Tuples__ với các phần tử có cùng kiểu.

## Khai Báo

### Khai Báo Tự Động

Khai báo tự do giống như cách khai báo với __Tuples__. Nếu các dữ liệu có cùng kiểu nó sẽ được chuyển về dạng __Array__ thông qua quá trình tự động xác định kiểu.

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];
}
```

### Khai Báo Thủ Công

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

## Truy Vấn Giá Trị

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

## Độ Dài Chuỗi

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

## In Dữ Liệu

Kết xuất dữ liệu ra cổng IO của chuỗi cũng được hỗ trợ tương tự như __Tuples__, đó là sử dụng `{:?}` là có thể in được toàn bộ chuỗi mà không cần thiết phải truy cập từng phẩn tử. Việc này cũng giúp ích khá nhiều.

__Array__ không có giới hạn về độ dài chuỗi nên không phải lo về số lượng.

```rust
fn main() {
    let arr_static = [1, 2, 3, 4, 5];
    println!("Auto: {:?}", arr_static);
}
```