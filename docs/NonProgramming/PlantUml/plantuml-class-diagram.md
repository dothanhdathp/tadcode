# \[PlantUml\] Class Diagram

## I. Mục đích

__Class Diagram__ được sử dụng để mô tả tương tác giữa các tác nhân hệ thống và bản thân hệ thống nhằm xác định các yêu cầu chức năng và nắm bắt hành vi.

Tham khảo chi tiết tại: [https://plantuml.com/use-case-diagram](https://plantuml.com/use-case-diagram)

## I. Class

=== "Các Loại Class"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
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
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
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
        </div>
    </div>
=== "Các Thực Thể Khác"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        scale 200*200
        circle  circle
        ()      circle_short_form
        diamond diamond
        <>      diamond_short_form
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        circle  circle
        ()      circle_short_form
        diamond diamond
        <>      diamond_short_form
        @enduml
        ```
        </div>
    </div>

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

## III. Visibility

| Ký Tự | Icon for Field | Icon for Method | Khả Năng Hiển Thị |
| :---: | :------------: | :-------------: | :---------------- |
|  `-`  |       □        |        ■        | private           |
|  `#`  |       ⬦       |       ⬥        | protected         |
|  `~`  |       △        |        ▲        | package private   |
|  `+`  |       ○        |        ●        | public            |

=== "Field Visibility"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Dummy {
            - field
            # field
            ~ field
            + field
        }
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Dummy {
            - field
            # field
            ~ field
            + field
        }
        @enduml
        ```
        </div>
    </div>
=== "Method Visibility"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Dummy {
            - method()
            # method()
            ~ method()
            + method()
        }
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Dummy {
            - method()
            # method()
            ~ method()
            + method()
        }
        @enduml
        ```
        </div>
    </div>
=== "Class Visibility"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        -class DummyA {
        }
        #class DummyB {
        }
        ~class DummyC {
        }
        +class DummyD {
        }
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        -class DummyA {
        }
        #class DummyB {
        }
        ~class DummyC {
        }
        +class DummyD {
        }
        @enduml
        ```
        </div>
    </div>

!!! info "package private"
    Thường dùng trong __Java__. Nó có ý nghĩa là độ phân bổ chỉ được thể hiện trong bố cục nội bộ. Mọi thành phần nội bộ trong cùng một __*package*__ có quyền truy cập vào thành phần này. Các thành phần bên ngoài __*package*__ không có quyền truy cập.

## IV. Relations

> Thể hiện mối quan hệ giữa các đối tượng.

### 4.1 Association

__*Sự liên kết*__ thể hiện mối quan hệ chung giữa hai lớp trong đó các đối tượng của một lớp tương tác với các đối tượng của lớp khác. Nó giống như nói, "hai thứ này được kết nối theo một cách nào đó.", hoặc đối tượng này sử dụng một đối tượng nào đó khác.

__*Sự liên kết*__ hiếm khi được thể hiện trong kiến trúc của mô hình __Class__, hầu hết nó có nhiều tác dụng ở một số mô hình khác lớn.

Trong ví dụ bên dưới, có thể chưa thực sự chính xác ứng với mọi mô hình, nhưng ba dịch vụ con __*PhoneSerive*__, __*MediaSerive*__, __*SensorSerive*__ đều có sự liên kết mạnh đến __*MasterSerive*__. __*MasterSerive*__ có quyền khởi động, dừng, hoặc yêu cầu điều khiển đến các __*Service*__ con. Liên kết dạng này có thể coi là liên kết mạnh.

<div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
    ```puml
    @startuml
    <style>
        document { BackGroundColor #00000000 }
    </style>
    class MasterSerive
    class PhoneSerive
    class MediaSerive
    class SensorSerive
    MasterSerive --> PhoneSerive
    MasterSerive --> MediaSerive
    MasterSerive --> SensorSerive
    @enduml
    ```
    </div>
    <div style="flex: 1;">
    ```text
    @startuml
    class MasterSerive
    class PhoneSerive
    class MediaSerive
    class SensorSerive
    MasterSerive --> PhoneSerive
    MasterSerive --> MediaSerive
    MasterSerive --> SensorSerive
    @enduml
    ```
    </div>
</div>

### 4.2 Dependency
> phụ thuộc

Mối quan hệ phụ thuộc là mối quan hệ trong đó <mark>một lớp dựa vào một lớp khác để hoạt động</mark>. Nó thường là tạm thời, nghĩa là sự phụ thuộc chỉ tồn tại khi hoạt động đang diễn ra và không tạo thành mối quan hệ lâu dài giữa các lớp.

Về mặt ý nghĩa như trên có thể hiểu mối liên lết này có tính nhất thời. Nó chỉ đơn giản là tạo ra một sự hạn chế hoặc ràng buộc phụ. Ở đây lấy ví dụ về ba tác vụ __*BluetoothSerive*__, __*WifiSerive*__, __*LightService*__ đều liên hệ đế __*PowerServive*__ trong mô hình điện thoại di động. Ba chức năng trên nếu không có ràng buộc sẽ làm việc liên tục đến khi hết năng lượng. Nhưng nếu có một tiến trình quản lý, nó có thể điều phối lại năng lượng và yêu cầu liên kết mềm đến các tác vụ nền. Tức là PowerService không có quyền ảnh hưởng trực tiếp đến các tác vụ kia nhưng vẫn có sự liên kết phụ thuộc nhẹ. Khi năng lượng xuống dưới ngưỡng, có thể một số tác vụ khác sẽ __*bị ép*__ dừng tiến trình tùy theo thiết kế.

Mối liên kết như vậy có thể gọi là liên kết phụ thuộc, liên kết mềm.

<div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
    ```puml
    @startuml
    <style>
        document { BackGroundColor #00000000 }
    </style>
    class PowerServive
    class BluetoothSerive
    class WifiSerive
    class LightService
    PowerServive ..> BluetoothSerive
    PowerServive ..> WifiSerive
    PowerServive ..> LightService
    @enduml
    ```
    </div>
    <div style="flex: 1;">
    ```text
    @startuml
    class PowerServive
    class BluetoothSerive
    class WifiSerive
    class LightService
    PowerServive ..> BluetoothSerive
    PowerServive ..> WifiSerive
    PowerServive ..> LightService
    @enduml
    ```
    </div>
</div>


### 4.3 Inheritance
> Kế thừa

__*Implementation*__ là mối quan hệ giữa một lớp và một giao diện. Một giao diện định nghĩa các phương thức trừu tượng mà một lớp phải triển khai, nhưng <mark>nó không cung cấp mã thực tế</mark>. Khi một lớp triển khai một giao diện, nó đồng ý cung cấp chức năng cụ thể được xác định bởi giao diện đó. Khi được kế thừa, các chức năng của nó cũng được sử dụng như một phương thức.

Triển khai của kế thừa sử dụng dấu `--|>` hoặc _keywords_ `extends`

Ví dụ thể hiện quan hệ kế thừa. __Dog__, __Cat__ và __Duck__ được kế thừa từ lớp __Animal__. Duck được kế thừa từ lớp Bird nên nó _có cánh_ và có thể _bay_ như một chức năng.

=== "Inheritance"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        Animal <|-- Dog
        Animal <|-- Cat
        Animal <|-- Duck
        Bird   <|-- Duck
        Animal <|-- Bird
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        Animal <|-- Dog
        Animal <|-- Cat
        Animal <|-- Duck
        Bird   <|-- Duck
        Animal <|-- Bird
        @enduml
        ```
        </div>
    </div>
=== "Extends"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Dog  extends Animal
        class Cat  extends Animal
        class Duck extends Animal
        class Bird extends Animal
        class Duck extends Bird
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        Ký hiệu `--|>` có thể viết một cách đơn giản hơn bằng `extends`
        ```text
        @startuml
        class Dog  extends Animal
        class Cat  extends Animal
        class Duck extends Animal
        class Bird extends Animal
        class Duck extends Bird
        @enduml
        ```
        </div>
    </div>
=== "Multies Extends"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Duck extends Bird,Animal,Poultry
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        `extends` cũng hỗ trợ việc kế thừa nhiều đối tượng một lúc.
        ```text
        @startuml
        class Duck extends Bird,Animal,Poultry
        @enduml
        ```
        </div>
    </div>

### 4.3 Implementation
> Thực hiện

__Implementation__ là mối quan hệ giữa một lớp và một giao diện. Một giao diện định nghĩa các phương thức trừu tượng mà một lớp phải triển khai, <mark>nhưng nó không cung cấp mã thực tế. Khi một lớp triển khai một giao diện, nó đồng ý cung cấp chức năng cụ thể được xác định bởi giao diện đó</mark> __*(interface)*__.

Mã này được lập luận từ __Java__. Java có một thực thể là __*interface*__ cái mà chỉ mang các phương thức và đối số cần thiết bên trong. Nó cho phép một __*module*__ có thể tương tác với các loại module khác nhau như mội loại thực thể xác định có các chức năng đã được định nghĩa nhưng không quan tâm cách thức triển khai, chỉ quan tâm kết quả.

Triển khai của _implement_ sử dụng dấu `..|>` hoặc _keywords_ `implements`

Ví dụ ba lớp __*Car*__, __*Board*__, __*Plane*__ đều kế thừa một _interface_ là __*Verhical*__. Chúng đều có hàm `move()` để thực hiện việc di chuyển nhưng Car thì chỉ chạy được trên mặt đất, thuyền chỉ chạy được ở duới nước còn máy bay thì không thể bơi. Do đó trong các trường hợp không thể thực hiện nó sẽ đều trả về false ứng với môi trường. Còn mặc định __*Verhical*__ không phải là một thực thể (dạng như Class), nó chỉ mang bản thiết kế chung.

=== "Inheritance"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Vehical {
            move()
        }
        Car ..|> Vehical
        Board ..|> Vehical
        Plane ..|> Vehical
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Vehical {
            move()
        }
        Car ..|> Vehical
        Board ..|> Vehical
        @enduml
        ```
        </div>
    </div>
=== "Implements"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Car implements Vehical
        class Board implements Vehical
        class Plane implements Vehical
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        Ký hiệu `--|>` có thể viết một cách đơn giản hơn bằng `implements`
        ```text
        @startuml
        class Car implements Vehical
        class Board implements Vehical
        class Plane implements Vehical
        @enduml
        ```
        </div>
    </div>
=== "Multies Implements"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Subway implements Vehical, Train, ElectronicsMachine
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        `implements` cũng hỗ trợ việc kế thừa nhiều đối tượng một lúc. Ví dụ như sử dụng Tàu Điện Ngầm kế thừa lại từ __Phương Tiện Giao Thông__, __Tàu Hỏa__, và __Thiết Bị Chạy Điện__
        ```text
        @startuml
        class Subway implements Vehical, Train, ElectronicsMachine
        @enduml
        ```
        </div>
    </div>



### 4.4 Aggregation
> Tổng hợp

__Tổng hợp__ là một loại liên kết đặc biệt biểu thị mối quan hệ "toàn thể - bộ phận". Nó được sử dụng khi một lớp (toàn thể) được tạo thành từ các lớp khác (các bộ phận) có thể tồn tại độc lập . Nói cách khác, các bộ phận (các lớp khác) <mark>có thể tồn tại mà không cần toàn thể (lớp đó), vì vậy việc loại bỏ toàn thể không phá hủy các bộ phận</mark>.

Theo ý kiến cá nhân, mối quan hệ này được hiểu như là _"sự hình thành của một đối tượng tổng được tạo nên từ các thành phần độc lập"_. Bởi vậy __tổng hợp__ có thể thêm, bớt các thành phần tùy theo nhu cầu, và ngay cả khi __tổng hợp__ bị phá hủy, các thành phần cũng không bị phá hủy. Mối quan hệ tổng hợp được diễn tả bằng dấu `o--`

Ví dụ __Shopee__ quản lý một hệ thống nhiều cửa hàng __Store__, kể cả khi Shopee bị sụp đổ, hệ thống các cửa hàng vẫn hoạt động bình thường vì nó là các thực thể độc lập.

=== "Strong Aggregation"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Shopee
        class StoreA
        class StoreB
        class StoreC
        StoreA --o Shopee
        StoreB --o Shopee
        StoreC --o Shopee
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Shopee
        class StoreA
        class StoreB
        class StoreC
        StoreA --o Shopee
        StoreB --o Shopee
        StoreC --o Shopee
        @enduml
        ```
        </div>
    </div>
=== "Weak Aggregation"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Shopee
        class StoreA
        class StoreB
        class StoreC
        StoreA ..o Shopee
        StoreB ..o Shopee
        StoreC ..o Shopee
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Shopee
        class StoreA
        class StoreB
        class StoreC
        StoreA ..o Shopee
        StoreB ..o Shopee
        StoreC ..o Shopee
        @enduml
        ```
        </div>
    </div>

### 4.5 Composition
> Thành phần

__Composition__ là một dạng tổng hợp mạnh mẽ hơn và cũng thể hiện mối quan hệ "toàn bộ". Tuy nhiên, trong bố cục, <mark>các bộ phận không thể tồn tại nếu không có tổng thể</mark>. Điều này có nghĩa là nếu tổng thể bị xóa bỏ thì các bộ phận cũng bị xóa bỏ vì chúng phụ thuộc vào tổng thể để tồn tại.

Thực sự mình không biết thể hiện liên kết mạnh yếu ở đây có nghĩa gì, nhưng có lẽ chỉ cần có liên kết mạnh.

Trong ví dụ, giả sử người dùng khởi tạo một thiết bị Xe và bắt đầu khởi tạo các thành phần cho nó phụ thuộc bởi chiếc xe. Nếu cả chiếc xe bị phá hủy, mọi thành phần liên quan cũng sẽ bị phá hủy theo.

=== "Strong Composition"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Car
        class Wheels
        class Engine
        class Navigation
        Wheels --* Car
        Engine --* Car
        Navigation --* Car
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Car
        class Wheels
        class Engine
        class Navigation
        Wheels --* Car
        Engine --* Car
        Navigation --* Car
        @enduml
        ```
        </div>
    </div>
=== "Weak Composition"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
        ```puml
        @startuml
        <style>
            document { BackGroundColor #00000000 }
        </style>
        class Car
        class Wheels
        class Engine
        class Navigation
        Wheels ..* Car
        Engine ..* Car
        Navigation ..* Car
        @enduml
        ```
        </div>
        <div style="flex: 1;">
        ```text
        @startuml
        class Car
        class Wheels
        class Engine
        class Navigation
        Wheels ..* Car
        Engine ..* Car
        Navigation ..* Car
        @enduml
        ```
        </div>
    </div>

## V. Theme

### Line

Một số kết nối vào jack cắm khác.

```text title="Cái này chưa biết chạy hay không"
<div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
    ```puml
    @startuml
    <style>
        document { BackGroundColor #00000000 }
    </style>
    @startuml
    Class0 <--> Class1
    Class0 <..> Class1
    Class1 <|--|> Class2
    Class1 <|..|> Class2
    Class2 o--o Class3
    Class2 o..o Class3
    Class4 *--* Class5
    Class4 *..* Class5
    Class5 #--# Class6
    Class5 #..# Class6
    Class6 x--x Class7
    Class6 x..x Class7
    Class8 }-- Class9
    Class8 }.. Class9
    Class9 +--+ Class10
    Class9 +..+ Class10
    Class10 ^--^ Class11
    Class10 ^..^ Class11
    @enduml
    ```
    </div>
    <div style="flex: 1;">
    ```text
    @startuml
    <style>
        document { BackGroundColor #00000000 }
    </style>
    @startuml
    Class0 <--> Class1
    Class0 <..> Class1
    Class1 <|--|> Class2
    Class1 <|..|> Class2
    Class2 o--o Class3
    Class2 o..o Class3
    Class4 *--* Class5
    Class4 *..* Class5
    Class5 #--# Class6
    Class5 #..# Class6
    Class6 x--x Class7
    Class6 x..x Class7
    Class8 }-- Class9
    Class8 }.. Class9
    Class9 +--+ Class10
    Class9 +..+ Class10
    Class10 ^--^ Class11
    Class10 ^..^ Class11
    @enduml
    ```
    </div>
</div>
```

## VI. Tham Khảo

- [Understanding Uml Class Diagrams A Beginners Guide](https://dev.to/krishna-nayak/understanding-uml-class-diagrams-a-beginners-guide-2omj)
- [Class Diagram Plantuml](https://plantuml.com/class-diagram)
- [Plantuml Commons Command](https://plantuml.com/commons)