# DataTypes & Variables

## Java Variables

Trong Java, có nhiều loại biến khác nhau, ví dụ:

- `String` - Lưu trữ văn bản, chẳng hạn như "Xin chào". Giá trị chuỗi được bao quanh bởi các báo giá kép
- `int` - lưu trữ số nguyên (số nguyên), không có số thập phân, chẳng hạn như 123 hoặc -123
- `float` - Cửa hàng số điểm nổi, với số thập phân, chẳng hạn như 19,99 hoặc -19,99
- `char` - Lưu trữ các ký tự đơn, chẳng hạn như 'A' hoặc 'B'. Giá trị char được bao quanh bởi các trích dẫn đơn lẻ
- `boolean` - Lưu trữ các giá trị với hai trạng thái: Đúng hoặc Sai

Và __Java__ tồn tại 2 kiểu biến là ___Primitive___ và ___Wrapper Class___.

| ___Primitive___ | ___Wrapper Class___ |
| :-------------: | :-----------------: |
|    __byte__     |      __Byte__       |
|    __short__    |      __Short__      |
|    __char__     |    __Character__    |
|     __int__     |     __Integer__     |
|    __long__     |      __Long__       |
|    __float__    |      __Float__      |
|   __double__    |     __Double__      |
|                 |     __String__      |

### Primitive Data

___Primitive Data___ là những loại như _byte_, _short_, _char_, _int_, _long_, _float_ và _double_. Đây là những dữ liệu ở dạng nguyên bản nhất có giới hạn _(có giới hạn về kích thước rõ ràng)_ và không bao gồm thêm các tính năng phụ.

```java
byte b = 0;
short s = 0;
char c = '0';
int i = 0;
long l = 0;
float f = 0;
double d = 0.0;
System.out.println("byte   : " + b);
System.out.println("short  : " + s);
System.out.println("char   : " + c);
System.out.println("int    : " + i);
System.out.println("long   : " + l);
System.out.println("float  : " + f);
System.out.println("double : " + d);
```

```txt
byte   : 0
short  : 0
char   : 0
int    : 0
long   : 0
float  : 0.0
double : 0.0
```

### Wrapper Class

Ngoài dạng dữ liệu nguyên thủy, __Java__ cung cấp thêm một số dạng dữ liệu mở rộng như __Byte__, __Integer__, __String__, ... Những dạng này có cấu trúc phức tạo hơn xoay quanh dữ liệu nguyên bản. Ví dụ như kiểu __interger__ dùng để biểu diễn số tự nhiên có thể dùng cả `int` và `Interger` để khai báo, nhưng `Interger` an toàn hơn khi chuyển kiểu, kiểm tra, tính âm dương, ... tốt hơn. Có thể nói tiện dụng hơn nhưng nặng nề hơn về bộ nhớ đến mức không cần thiết.

Phần lớn cái lớp này có lẽ được tạo ra để cho `String` và `Byte`. Hai kiểu dữ liệu này bản thân mang nhiều ý nghĩa và nhiều tính năng quan trọng biến đổi dữ liệu khá phổ biến. Việc hỗ trợ cho chúng đem lại nhiều lợi ích cho lập trình viên hơn nhiều so với `Interger`.

Đi sâu hơn về từng loại sẽ đề cập ở các chương sau.

## Syntax

```txt
type variableName = value;
```

Trong đó `type` là một trong các loại của Java (như int hoặc chuỗi) và `variablename` là tên của biến (như X hoặc tên).
Dấu bằng được sử dụng để gán các giá trị cho biến.

Để tạo một biến nên lưu trữ văn bản, hãy xem ví dụ sau:

Để tạo một biến, bạn phải chỉ định loại và gán cho nó một giá trị:
Các _dữ liệu cơ bản trong tất cả các ngôn ngữ lập trình_ nhìn chung bao gồm số nguyên __Interger__, số thực __Float__, chữ số __Char__ và chuối __String__.

Ví dụ:

```java
public class Main {
    public static void main(String[] args) {
        int     i   = 100000;
        long    l   = 10000000000L;
        float   f   = 123.123456789f;
        double  d   = 456.123456789d;
        byte    by  = 100;
        short   s   = 10000;
        char    c   = 'A';
        boolean bl  = true;
        String  str = "Hello World";

        System.out.println("Int     : " + i);
        System.out.println("Long    : " + l);
        System.out.println("Float   : " + f);
        System.out.println("Double  : " + d);
        System.out.println("Byte    : " + by);
        System.out.println("Short   : " + s);
        System.out.println("Char    : " + c);
        System.out.println("Boolean : " + bl);
        System.out.println("String  : " + str);
    }
}
```

Kết quả:

```txt
Int     : 100000
Long    : 10000000000
Float   : 123.12346
Double  : 456.123456789
Byte    : 100
Short   : 10000
Char    : A
Boolean : true
String  : Hello World
```
## Mô tả các kiểu cơ bản

### Các kiểu số nguyên int, long, byte, short và Interger

Có tới 5 loại để biểu diễn số nguyên là `int`, `byte`, `short`, `long` và một kiểu riêng của Java cũng là số nguyên là __Interger__.

Trong đó 4 kiểu đầu `int`, `byte`, `short`, `long` chỉ khác về mặt kích thước bộ nhớ, tương được là về dải giá trị mà chúng có thể biểu diễn.

|  Loại   | Kích thước |
| :-----: | :--------: |
| `byte`  |  1 bytes   |
| `short` |  2 bytes   |
|  `int`  |  4 bytes   |
| `long`  |  8 bytes   |

> Các phép toán cơ bản như cộng trừ nhân chia và so sánh cũng đều hoạt động tốt với kiểu số nguyên này.

### Integer

Integer là một lớp nguyên thủy trong Java, được sử dụng để biểu diễn các số nguyên. Nó có thể được sử dụng để biểu diễn các số nguyên trong một phạm vi rộng lớn hơn so với các kiểu số nguyên khác.

Các chức năng cơ bản của Interger là:

```java
Integer a = 10, b = 20;
System.out.println("The value of a is: " + a);
System.out.println("The value of b is: " + b);
```

__Kết quả:__
```bash
The value of a is: 10
The value of b is: 20
```

Lớp Interger có sẵn các biến ___enum___ `MIN_VALUE`, `MAX_VALUE`:

| `MIN_VALUE` | `MAX_VALUE` |
| :---------: | :---------: |
| -2147483648 | 2147483647  |

> Về các thành phần khác nên tham khảo riêng.

### float, double

`float` là kiểu số thực. Còn một kiểu biến tương tự khác là `double`, điểm khác biệt duy nhất là `double` có khoảng biểu diễn số lớn hơn. Cụ thể là:

#### So sánh float với double

##### Kích thước và độ chính xác
|              |       float        |       double        |
| :----------- | :----------------: | :-----------------: |
| Kích thước   | 4 bytes (32 bits)  |  8 bytes (64 bits)  |
| Độ chính xác | ~7 số sau dấu phẩy | ~15 số sau dấu phây |

#### Sử dụng

- `float` được sử dụng khi muốn tiết kiệm bộ nhớ hơn sự chính xác mức độ cao (thông thường với con người chỉ cần khoảng 3-6 độ chính xác sau dấu phẩy là đáng tin cậy rồi).
    - `float` được sử dụng phổ thông trong các lĩnh vực liên quan đến đồ hoạ và hiển thị UI/UX
- `double` được sử dụng trong những trường hợp yêu cầu độ chính xác ví dụ như những lĩnh vực liên quan đến toán học.
    - `double` mạnh mẽ hơn trong toán học, khoa học, khoa học máy tính.

Về sử dụng `float` và `double` không có gì khác nhau nhiều, ví dụ:

```java
public class Main {
    public static void main(String[] args) {
        float  f = 123.123456789f;
        double d = 456.123456789d;
        System.out.println(f);
        System.out.println(d);
    }
}
```

Kết quả:
```txt
123.12346
456.123456789
```
### Char

`char` trong Java là một kiểu dữ liệu đặc biệt, nó được sử dụng để lưu trữ một ký tự. `char` có thể được sử dụng để lưu trữ một ký tự trong một ngôn ngữ nào đó , hoặc một ký tự đặc biệt trong một ứng dụng nào đó. Hầu hết trường hợp thì `char` được sử dụng để lược/duyệt từng chữ có trong một chuỗi (`String`). Ngoài ra thì kiểu biến này cũng hay được sử dụng để đại diện cho một `word` trong máy tính. (nếu ai chưa biết thì đơn vị thuận tiện nhất cho máy tính là `int` và `char`, hai kiểu này sẽ được ưu tiên tính toán hơn các loại còn lại.)

### String

`String` trong Java là một kiểu dữ liệu đặc biệt, nó được sử dụng để lưu trữ một chuỗi các ký tự . `String` có thể được sử dụng để lưu trữ một chuỗi các ký tự trong một ngôn ngữ nào đó , hoặc một chuỗi các ký tự đặc biệt trong một ứng dụng nào đó . `String` được sử dụng rộng rãi trong các ứng dụng Java, từ các ứng dụng đơn giản đến các ứng dụng phức tạp. `String` có thể được sử dụng để lưu trữ một chuỗi các ký tự, và có thể được sử dụng để thực hiện các hoạt động như so sánh, tìm kiếm, thay thế, cắt xén, nối chuỗi, v.v. `String` là một trong những kiểu dữ liệu quan trọng nhất trong Java.

Khác biệt của String trong Java với các ngôn ngữ khác là:

1. `String` trong Java có thể được sử dụng để lưu trữ một chuỗi các ký tự
1. `String` trong Java là một đối tượng, không phải là một chuỗi các ký tự
1. `String` trong Java có thể được sử dụng để thực hiện các hoạt động như so sánh
1. `String` trong Java có thể được sử dụng để thực hiện các hoạt động như tìm kiếm
1. `String` trong Java có thể được sử dụng để thực hiện các hoạt động như thay thế

## Variables

Có ba loại biến (`Variables`) trong Java, đó là ___local___ (biến cục bộ), ___instance___ (ví dụ) và ___static___ (biến tĩnh). Một biến là tên của một khu vực dành riêng được phân bổ trong bộ nhớ. Nói cách khác, nó là một tên của vị trí bộ nhớ. Nó là sự kết hợp của "Vary + có thể" có nghĩa là giá trị của nó có thể được thay đổi.

### Local Variable

Một biến được khai báo bên trong phần thân của phương pháp được gọi là biến cục bộ. Bạn chỉ có thể sử dụng biến này trong phương thức đó và các phương thức khác trong lớp thậm chí không nhận thức được rằng biến tồn tại.

```java
public class LocalVariableExample {  
    public static void main(String[] args)  
    {  
        //defining a Local Variable  
        int num = 10;  
        System.out.println(" Variable: " + num);  
    }  
}  
```

Kết quả:

```txt
Variable: 10
```

### Instance Variable

Một biến được khai báo bên trong lớp nhưng bên ngoài phần thân của phương pháp, được gọi là một biến thể hiện. Nó không được tuyên bố là tĩnh.

Nó được gọi là một biến thể hiện vì giá trị của nó là cụ thể về thể hiện và không được chia sẻ giữa các trường hợp.

```java
import java.io.*;  
public class InstanceVariableDemo {  
    //Defining Instance Variables  
    public String name;  
    public int age=19;  
 //Creadting a default Constructor initializing Instance Variable  
    public InstanceVariableDemo()  
    {  
        this.name = "Deepak";  
    }  
    public static void main(String[] args)  
    {  
        // Object Creation  
        InstanceVariableDemo obj = new InstanceVariableDemo();  
        System.out.println("Student Name is: " + obj.name);  
        System.out.println("Age: "+ obj.age);  
    }  
}  
```

Kết quả:

```txt
Student Name is: Deepak
Age: 19
```

### Static variable

Một biến được khai báo là tĩnh được gọi là biến tĩnh. <mark>Nó không thể là địa phương</mark>. Bạn có thể tạo một bản sao duy nhất của biến tĩnh và chia sẻ nó trong số tất cả các trường hợp của lớp. Phân bổ bộ nhớ cho các biến tĩnh chỉ xảy ra một lần khi lớp được tải trong bộ nhớ.

```java
class Student{  
    //static variable  
   static int age;  
}  
public class StaticVariableExample{  
   public static void main(String args[]){  
       Student s1 = new Student();  
       Student s2 = new Student();  
       s1.age = 24;  
       s2.age = 21;  
       Student.age = 23;  
       System.out.println("S1\'s age is: " + s1.age);  
       System.out.println("S2\'s age is: " + s2.age);  
   }  
}   
```

Kết quả:

```txt
S1's age is: 23
S2's age is: 23
```

## Tóm tắt

!!! note "Note"
    - Biến có ___8 kiểu___ cơ bản được kế thừa là `int`, `long`, `float`, `double`, `byte`, `short`, `char` và `boolean`
    - Loại biến có ___3 loại___ chính là __Local__, __Instance__ và __Static__