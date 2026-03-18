# Mảng
> [Nguồn](https://doc.rust-lang.org/std/primitive.array.html)

Mảng là kiếu phức hợp thứ hai, là tập hợp các giá trị có cùng một kiểu được tập hợp lại thành một mảng với độ dài xác định.

!!! abstract "Ghi Chú"
    - Tập các giá trị có cùng một kiểu.
    - Kích thước xác định. Không thể thay đổi sau khi khai báo.
    - Khai báo dùng `x:[T;S] = [A,B,C,...]`
    - Nếu dùng `[T;S] = [D;S]` _(`D` là giá trị mặc định)_
    - Có thể bỏ qua kiểu, lúc này hệ thống sẽ tự ép kiểu mặc định.
    - Truy cập phần tử dùng `[index]`

## Khai Báo

- Khai báo tự do giống như cách khai báo với __Tuples__. Nếu các dữ liệu có cùng kiểu nó sẽ được chuyển về dạng __Array__ thông qua quá trình tự động xác định kiểu.
- Khai báo thủ công với cấu trúc `[T; length]` với `T` là kiểu là `length` là độ dài của chuỗi.
- Có thể rút gọn khai báo như cách ba với, lúc này tất cả các phần tử của mảng sẽ có cùng một giá trị mặc định.

```rust
fn main() {
    let arr = [1, 2, 3, 4, 5];           // Khai báo tự do
    let arr: [i32; 5] = [1, 2, 3, 4, 5]; // Khai báo với số lượng phần tử
    let arr: [i32; 500] = [0; 500];      // Khai báo với số lượng phần tử + giá trị mặc định
}
```

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