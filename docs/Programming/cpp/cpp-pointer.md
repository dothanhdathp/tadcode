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

## Tìm Hiểu Thêm

Con trỏ nên coi là một __kiểu biến__, nó giống như dạng biến `int`, hay `long`, điều đó sẽ dễ dàng hơn nhiều trong việc hiểu cách thức mã của bạn hoạt động.

Con trỏ vốn là một khái niệm mơ hồ. Khác với các kiểu biến khác nó sẽ _không thực sự lưu giá trị_. Nó chỉ có đúng một thành phần là __địa chỉ__. Các thành phần khác như kích thước và kiểu được _trình biên dịch_ làm. Chính thế nên nếu bạn có thể lấy chính xác địa chỉ đến một hàm hoặc là biến nào đó của chương trình trong __*runtime*__ hoặc trên chính __*tệp nhị phân*__, mọi ngữ nghĩa đều không có ý nghĩa.

Các kiểu biến nguyên thủy mới có `++`, `--` đối với con trỏ để nhảy đến địa chỉ liền kề. Việc xác định kích thước của dạng dữ liệu hay kiểu dữ liệu hoàn toàn do trình biên dịch. Chính thế nên mỗi khi viết một lớp tự định nghĩa, tốt nhất nên tự viết riêng toán tử nhảy địa chỉ.

- Con trỏ cơ bản trong C++ kế thừa trực tiếp từ [Con trỏ trong C](/Programming/c/c-pointer/)

## Smart Pointer

Con trỏ thông thường còn gọi là __Raw Pointer__ nhằm phân biệt với lớp các con trỏ mới được đóng gói trong lớp thư viện tiêu chuẩn là [__Smart Pointer__](cpp-smart-pointer.md).