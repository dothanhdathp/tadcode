# std::makeshare

## Overview

Xây dựng một đối tượng thuộc loại Tvà gói nó trong std::shared_ptr bằng cách sử dụng ___args___ làm danh sách tham số cho hàm tạo của T.
 
In header `<memory>`
```c++
template< class T, class... Args >
shared_ptr<T> make_shared( Args&&... args );
```
_Hàm này sẽ trả ra một biến con trỏ loại `std::shared_ptr` của đối tượng loại `T` sau khi khởi tạo đối tượng bằng các biến đầu vào trong chuỗi `Args&&... args`._

## Detail

### Parameters
&emsp;_args: Chuỗi các giá trị đầu vào để tạo ra 1 đối tượng theo dạng template `T`_

### Return value
&emsp; Trả ra `std::shared_ptr` của một đối tượng loại `T` _duy nhất_. (Khá giống ___singleton___)

##### Exceptions
Hàm này sẽ trả ra `std::bad_alloc` hoặc một trong những loại khác nếu trong hàm __construct__  của lớp `T` định nghĩa.

### Notes

> Hàm này được tạo ra để thay thế việc xây dựng `std::shared_ptr<T>(T new(args...))` của một con trỏ dùng chung từ con trỏ gốc nhưng lại được trả về bởi lệnh gọi `new`.\
Cách gọi nguy hiểm đó khiến hàm `std::shared_ptr` sẽ phải thực hiện ít nhất hai lần khởi tạo bộ nhớ. Hơn nữa nếu có trả về exceptions thì cách gọi cũ rất dễ gây ra lỗi rò rỉ bộ nhớ.\
→ `std::make_shared` ra đời nhằm khắc phục hai điểm yếu trên.

Tham khảo: _[link](https://www.enseignement.polytechnique.fr/informatique/INF478/docs/Cpp/en/cpp/memory/shared_ptr/make_shared.html#:~:text=Constructs%20an%20object%20of%20type,for%20the%20constructor%20of%20T%20.)_