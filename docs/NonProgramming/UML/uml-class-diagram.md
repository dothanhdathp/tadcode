# \[UML\] Class diagram

## Class

| Loại Class     | Tác Dụng                                                                                                                                                                   |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __abstract__   | lớp trừu tượng, gần giống như _interface_ nhưng sẽ giấu code phần dưới và các hàm không thể thay thế.                                                                      |
| __annotation__ | Thực thể để chú thích???                                                                                                                                                   |
| __class__      | Lớp                                                                                                                                                                        |
| __dataclass__  | Lớp dữ liệu, đặc tả cho đối tượng sử dụng để mô tả về khối mang dữ liệu                                                                                                    |
| __entity__     | Đại diện cho thực thể cái mình cũng không biết để làm gì                                                                                                                   |
| __enum__       | Đại diện cho khối __*enum*__, chắc dùng để đặc tả chi tiết                                                                                                                 |
| __exception__  | exception _(ngoại lệ)_, chắc khối này để đặc tả cho hành vi __*throw*__ mỗi khi chương trình chết. Hoặc __*try()/catch()*__                                                |
| __interface__  | Thường trong Java, mô tả các đặc điểm của một interface, về các đại diện chức năng                                                                                         |
| __metaclass__  | Là các siêu class dạng như __*factory*__, nó tạo ra các class và quy định hành vi cho bản thân nó theo cấu hình. Khái niệm này chỉ có trên các ngôn ngữ lập trình bậc cao. |
| __struct__     | Đặc tả cho __struct__. Cái này đặc trưng riêng cho mỗi ngôn ngữ.                                                                                                           |
| __protocol__   | Đặc tả cho __protocol__. Cái này đặc trưng riêng cho mỗi ngôn ngữ.                                                                                                         |
| __record__     | Đặc tả cho __record__. Cái này đặc trưng riêng cho mỗi ngôn ngữ.                                                                                                           |
| __stereotype__ | Đặc tả cho __stereotype__. Cái này đặc trưng riêng cho mỗi ngôn ngữ.                                                                                                       |

```puml
@startuml
<style>
    document { BackGroundColor #00000000 }
</style>
abstract        abstract
annotation      annotation
class           class
dataclass       dataclass
entity          entity
enum            enum
exception       exception
interface       interface
metaclass       metaclass
protocol        protocol
record          record
stereotype      stereotype
struct          struct
@enduml
```

## Relationship

### Association
> Sự liên kết

- __*Sự liên kết*__ thể hiện mối quan hệ chung giữa hai lớp trong đó các đối tượng của một lớp tương tác với các đối tượng của lớp khác. Nó giống như nói, "hai thứ này được kết nối theo một cách nào đó.", hoặc đối tượng này sử dụng một đối tượng nào đó khác.
- __*Sự liên kết*__ sử dụng mũi tên nét liền để thể hiện mối quan liên kết.

### Aggregation
> Tổng hợp

Tập hợp là một loại liên kết đặc biệt đại diện cho mối quan hệ "toàn bộ". Điều này được sử dụng khi một lớp (toàn bộ) được tạo thành từ các lớp khác (các bộ phận) có thể tồn tại độc lập. Nói cách khác, các bộ phận (các lớp khác) có thể tồn tại mà không có cái toàn thể (một lớp đó), nên việc loại bỏ cái toàn thể không làm mất đi các bộ phận.

### Composition
> Thành phần

Thành phần là một hình thức tổng hợp mạnh mẽ hơn và cũng thể hiện mối quan hệ "toàn bộ". Tuy nhiên, trong bố cục, các bộ phận không thể tồn tại nếu không có tổng thể. Điều này có nghĩa là nếu tổng thể bị xóa bỏ thì các bộ phận cũng bị xóa bỏ vì chúng phụ thuộc vào tổng thể để tồn tại.

### Inheritance (Generalization)
> Kế thừa (Tổng quát hóa)

Kế thừa hay còn gọi là Generalization, giống như mối quan hệ “cha-con” giữa hai lớp. Trong mối quan hệ này, một lớp (lớp con hoặc lớp con) kế thừa các thuộc tính và hành vi từ lớp khác (lớp cha hoặc lớp cha). Điều này giúp tái sử dụng mã và tránh trùng lặp vì lớp con tự động lấy các đặc điểm của lớp cha.

### Implementation
> Thực hiện

Việc triển khai là mối quan hệ giữa một lớp và một giao diện. Một giao diện định nghĩa các phương thức trừu tượng mà một lớp phải triển khai, nhưng nó không cung cấp mã thực tế. Khi một lớp triển khai một giao diện, nó đồng ý cung cấp chức năng cụ thể được xác định bởi giao diện đó.

### Dependency
> phụ thuộc

Sự phụ thuộc là mối quan hệ trong đó một lớp dựa vào lớp khác để hoạt động. Nó thường là tạm thời, có nghĩa là sự phụ thuộc chỉ tồn tại khi hoạt động đang diễn ra và không hình thành mối quan hệ lâu dài giữa các lớp.

