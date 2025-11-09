# Basic Concept

Với những ngôn ngữ bậc cao, cú pháp đã tối giản hoá đến mức tối đa các phương thức được sử dụng rồi. Thế nên chỉ cần đi qua một lượt các ví dụ đơn giản là hòm hòm nắm được ngôn ngữ này.

Nhược điểm chính là về bản chất, các ngôn ngữ bậc cao là gói của các ngôn ngữ trước đó, thế nên hãy tập trung học kỹ thay vì học lướt.

Trong phần này trình bày bảy chủ đề chính:

1. Hello world
1. Basic types
1. Collections
1. Control flow
1. Functions
1. Classes
1. Null safety

## Hello World

Chương trình đầu tiên được viết bằng ngôn ngữ __Kotlin__.

```kotlin
fun main() {
    println("Hello, world!!!")
}
```

- Chương trình trên là chương trình in ra ngoài màn hình chữ `Hello, world!!!`
- Để in ra ngoài dòng chữ __*"Hello, world!!!"*__, cú pháp được sử dụng là `println()`

### Variables _(Biến)_

- `val` : Biến __*Read-only*__ _(chỉ đọc)_
- `var` : Biến __*Mutable*__ _(có thể thay đổi)_

```kotlin
fun main() {
    val popcorn = 5    // There are 5 boxes of popcorn
    val hotdog = 7     // There are 7 hotdogs
    var customers = 10 // There are 10 customers in the queue

    popcorn = 0
    hotdog = 0
    customers = 8
    println(popcorn)
    println(hotdog)
    println(customers)
}
```

Nếu cố tình gắn, sẽ bị lỗi:

```bash title="Kết quả"
fun main() {
    val popcorn = 5    // There are 5 boxes of popcorn
    val hotdog = 7     // There are 7 hotdogs

    popcorn = 0
    hotdog = 0

    println(popcorn)
    println(hotdog)
}
```

```bash title="Kết quả"
'val' cannot be reassigned.
'val' cannot be reassigned.
```

!!! warning "Warning"
    Chúng tôi khuyên bạn nên khai báo tất cả các biến là chỉ đọc __*read-only*__ (`val`) theo mặc định. Chỉ sử dụng các biến có thể thay đổi - __*mutable*__ (`var`) nếu bạn thực sự cần. Bằng cách đó, bạn ít có khả năng vô tình thay đổi thứ gì đó không có nghĩa là thay đổi.

### Mẫu String

Thật hữu ích khi biết cách in nội dung của các biến thành đầu ra tiêu chuẩn. Bạn có thể làm điều này với các mẫu chuỗi. Bạn có thể sử dụng các biểu thức mẫu để truy cập dữ liệu được lưu trữ trong các biến và các đối tượng khác và chuyển đổi chúng thành các chuỗi. Giá trị chuỗi là một chuỗi các ký tự trong dấu ngoặc kép `"`. Biểu thức mẫu luôn bắt đầu bằng dấu hiệu đô la `$`.

Để đánh giá một đoạn mã trong biểu thức mẫu, hãy đặt mã trong dấu ngoặc kép `{}` sau ký hiệu đô la `$`.

Ví dụ:

```bash
val customers = 10
println("There are $customers customers")
// There are 10 customers

println("There are ${customers + 1} customers")
// There are 11 customers
```

- Nễu `x` là một biến, giá trị của nó sẽ được lấy thông qua `$x`
- Nếu là một phép tính có thể lấy thông qua `${}`

## Basic types _(Các kiểu cơ bản)_

### Augmented assignments _(Nhiệm vụ tăng cường)_

| Sự biểu lộ | Dịch sang              |
| :--------- | :--------------------- |
| `a += b`   | __*a.plusAssign(b)*__  |
| `a -= b`   | __*a.minusAssign(b)*__ |
| `a *= b`   | __*a.timesAssign(b)*__ |
| `a /= b`   | __*a.divAssign(b)*__   |
| `a %= b`   | __*a.remAssign(b)*__   |

```kotlin
var customers = 10

// Some customers leave the queue
customers = 8

customers = customers + 3 // Example of addition: 11
customers += 7            // Example of addition: 18
customers -= 3            // Example of subtraction: 15
customers *= 2            // Example of multiplication: 30
customers /= 3            // Example of division: 10

println(customers) // 10
```

### Các kiểu

| Category                   | Basic types                        | Example code                                                |
| :------------------------- | :--------------------------------- | :---------------------------------------------------------- |
| __Integers__               | `Byte`, `Short`, `Int`, `Long`     | _val year: Int = 2020_                                      |
| __Unsigned integers__      | `UByte`, `UShort`, `UInt`, `ULong` | _val score: UInt = 100u_                                    |
| __Floating-point numbers__ | `Float`, `Double`                  | _val currentTemp: Float = 24.5f, val price: Double = 19.99_ |
| __Booleans__               | `Boolean`                          | _val isEnabled: Boolean = true_                             |
| __Characters__             | `Char`                             | _val separator: Char = ','_                                 |
| __Strings__                | `String`                           | _val message: String = "Hello, world!"_                     |

```kotlin
fun main() {
    val d: Int // Variable declared without initialization
    d = 3 // Variable initialized
    val e: String = "hello" // Variable explicitly typed and initialized

    // Variables can be read because they have been initialized
    println(d) // 3
    println(e) // hello
}
```

__*Code sai:*__

```kotlin
val d: Int
println(d)
```

__*Lỗi báo ra:*__

```txt
Variable 'd' must be initialized.
```

## Collections _(Bộ sưu tập)_

Các loại sưu tập

| Các loại sưu tập | Mô tả                                                                               |
| :--------------- | :---------------------------------------------------------------------------------- |
| `Lists`          | Bộ sưu tập các mặt hàng được đặt hàng                                               |
| `Sets`           | Bộ sưu tập các mặt hàng không có thứ tự độc đáo                                     |
| `Maps`           | Bộ các cặp giá trị khóa trong đó các phím là duy nhất và chỉ ánh xạ tới một giá trị |

### List

Danh sách các mục lưu trữ theo thứ tự chúng được thêm vào và cho phép các mục trùng lặp.

- `listOf()` là hàm tạo danh sách __*tĩnh*__, không thể sửa. Trả ra `List<Type>()`
- `mutableListOf()` là hàm tạo danh sách __*động*__, có thể sửa. Trả ra `MutableList<Type>()`

```kotlin
fun main() {
    // Read only list
    val readOnlyShapes = listOf("triangle", "square", "circle")
    println(readOnlyShapes)
    // [triangle, square, circle]

    // Mutable list with explicit type declaration
    val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
    println(shapes)
    // [triangle, square, circle]
}
```

- Danh sách có thể in ra ngoài như là `[triangle, square, circle]`

### Sets

Mô tả

### Maps

Mô tả
