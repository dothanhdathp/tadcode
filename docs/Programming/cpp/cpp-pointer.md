# \[C++\] Con trỏ (Pointer)

## Khái niệm

### Định nghĩa 

Con trỏ là một biến lưu trữ địa chỉ bộ nhớ của một biến khác. Thay vì giữ một giá trị trực tiếp, nó giữ địa chỉ nơi giá trị được lưu trong bộ nhớ. Nó là xương sống của thao tác bộ nhớ cấp thấp trong C.

- Con trỏ được khai báo bằng cách chỉ định kiểu dữ liệu và tên của nó, với dấu hoa thị (*) trước tên. Cú pháp : data_type *pointer_name;
- Kiểu dữ liệu cho biết loại biến mà con trỏ có thể trỏ đến. Ví dụ: "int *ptr;" khai báo một con trỏ trỏ đến một số nguyên.
- Truy cập trực tiếp con trỏ sẽ chỉ cung cấp cho chúng ta địa chỉ được lưu trữ trong con trỏ. Để lấy giá trị tại địa chỉ được lưu trữ trong biến con trỏ, chúng ta sử dụng toán tử *, gọi là toán tử hủy tham chiếu trong C.
- Lưu ý rằng chúng ta sử dụng * cho hai mục đích khác nhau trong con trỏ. Một là để khai báo một biến con trỏ và mục đích còn lại là trong một toán tử để lấy giá trị được lưu trữ tại địa chỉ được lưu trữ trong con trỏ.

### Ý nghĩa

> Con trỏ rất hữu dụng nên nó được kế thừa lại từ C. Không có sự khác biệt giữa hai ngôn ngữ.

!!! example "Mục đích"
    Nói về mục đích, con trỏ sinh ra chính là để có thể gọi đến trực tiếp __*một biến rõ ràng*__ nào đó thay vì __là biến tự do__. Hãy tưởng tượng giống như một quản lý có hai nhiệm vụ như sau:

    - Nhiệm vụ 1 cần 4 công nhân bất kỳ
    - Nhiệm vụ 1 cần 4 công nhân bắt buộc phải có tên là A,B,C,D

    _**biến tự do** là một kiểu biến sẽ bị giải phóng sau khi hàm kết thúc_ 

Như vậy, việc kiểm soát của con trỏ sinh ra là cho vấn dề đó. Chính xác là khả năng __kiểm soát biến__

Con trỏ cực kỳ hữu dụng, và nó cũng mạnh mẽ trong C/C++. Đối với người thực hành lập trình nhúng hoặc tối ưu bộ nhớ đều khá là yêu thích con trỏ trong ngôn ngữ này.

## Ví dụ

### Ví dụ 1

Ví dụ đơn giản về việc khai báo con trỏ.

- `int var = 10;` Tạo ra một biến có giá trị là __10__
- `int* ptr = &var;` Con trỏ kiểu số nguyên được khai báo, và gán nó vào 

```cpp
#include <stdio.h>
​
int main()
{
    // Biến bình thường
    int var = 10;
    // Biến con trỏ ptr lưu trữ địa chỉ của var
    int* ptr = &var;
    // Truy cập trực tiếp ptr sẽ cung cấp cho chúng ta một địa chỉ
    printf ( "%d" , ptr );
​    return  0 ;
}
```


## Ghi chú

!!! tip "Tip"
    - Con trỏ cũng là một __kiểu biến__, nó giống như dạng biến `int`, hay `long`.
        - Kiểu biến của con trỏ sẽ mang theo kiểu biến và kích thước.

## Liên kết

- Con trỏ trong C

- [Smart Pointer](cpp-3-smart-pointer.md)
- [Raw Pointer](cpp-3-raw-pointer.md)