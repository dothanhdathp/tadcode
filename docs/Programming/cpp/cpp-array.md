# \[Cpp\] Array - Chuỗi Cổ Điển

Chuỗi là cấu trúc đơn giản nhất. Nó gồm các dữ liệu được xếp liên tục nhau có __số lượng phần tử__ khai báo sẵn. Tức là sau khi chuỗi đã được tạo, nó không có khả năng mở rộng bộ nhớ đã có. Để hiểu được tại sao hãy đọc về cách máy tính phân bổ bộ nhớ cho __Heap__ và __Stack__.

Chuỗi không nhất thiết phải là các dữ liệu nguyên thủy. Chuỗi có thể là tất cả các loại miễn là nó có tính chất có thể đóng gói.

Chuỗi của chuỗi được gọi là __chuỗi hai chiều__. Nếu mở rộng thêm thì ta có chuỗi ba, bốn chiều, ...

Phần tử của chuỗi không nhất thiết phải là các kiểu nguyên thủy.

## Khai Báo Mảng

### Khai Báo Tĩnh

Mảng được khai báo với `type name[amount]`.

Danh sách có thể được khai báo theo hai kiểu, __khai báo mặc định__ với __khai báo + giá trị khởi tạo__. Nếu khai báo với giá trị khởi tạo thì nó sẽ được đặt trong một mảng `{ danh_sách }`.

Trong cả hai trường hợp, bắt buộc đều phải có số lượng phần tử trong mảng.

=== "Khai Báo Mặc Định"
    ```cpp
    int    list_of_int[10];
    bool   list_of_bool[10];
    float  list_of_float[10];
    size_t list_of_size_t[10];
    ```
=== "Khai Báo _+ Giá Trị Khởi Tạo_"
    ```cpp
    int    list_of_int[10]    = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    bool   list_of_bool[10]   = { false, true, false, true, false, true, false, true, false, true };
    float  list_of_float[10]  = { 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 };
    size_t list_of_size_t[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    ```

### Khai Báo Động

Khai báo động là cách thức khai báo mảng trong khi chương trình chạy. Cách thức này sẽ tiết kiệm bộ nhớ trong những bài toán yêu cầu lượng bộ nhớ không rõ ràng cho mảng và có sự dao động lớn.

Xem xét đây là ví dụ khi khai báo mảng động với giá trị mặc định ngược lại so với __*index*__.

```cpp
#include <iostream>

struct Pointer {
    int x = 0;
    int y = 0;
};

int main() {
    int _size = 0;
    
    std::cout << "Tạo mảng với ? phần tử: ";
    std::cin >> _size;
    std::cout << std::endl;

    int* list_of_int = new int[_size];

    for(int i=0; i<_size; ++i) {
        list_of_int[i] = _size - i;
    }

    // In
    std::cout << "Mảng vừa nhập là: { ";
    for(int i=0; i<_size; ++i) {
        std::cout << list_of_int[i] << " ";
    }
    std::cout << "}" << std::endl;
    return 0;
}
```

!!! danger "Chú Ý"
    Khai báo động khá là nguy hiểm. Ở ví dụ trên con trỏ `list_of_int` chẳng hạn đã khai báo một mảng mới qua __*new*__. Sau đó hãy đảm bảo việc quản lý mảng đó một cách cẩn thận tránh trường hợp __*khai báo lại trước khi xóa*__, còn gọi là __Memory Leak__. Tức là code chạy đến `int* list_of_int = new int[_size];` một lần nữa trước khi gọi `delete list_of_int;`. Bởi vì lúc đó dữ liệu cũ của mảng sẽ bị mất liên kết, trở thành bộ nhớ không được quản lý, không thể xóa trên RAM. Gây lãng phí tài nguyên.

## Tính Liên Tục Của Mảng

Để chứng minh một mảng là một bộ các dữ liệu liên tục trong bộ nhớ có thể tham khảo ví dụ sau:

```cpp
#include <iostream>

int arr[2] = {0, 0};

/*
[[7FFFFFFF__FFFFFFFF]]
[[7FFFFFFF][FFFFFFFF]]
[[       1][       0]]
*/
int main() {
    long long* d = (long long*)arr;
    *d = 0x7FFFFFFFFFFFFFFF;
    std::cout << *d << std::endl;
    std::cout << arr[0] << std::endl;
    std::cout << arr[1] << std::endl;
    return 0;
}
```

Ở ví dụ trên:

- Dữ liệu kiểu `int` chiếm __4 byte__, dữ liệu kiểu `long long` chiếm __8 byte__
- Con trỏ __d__ tham chiếu đến mảng __*arr[]*__ tại vị trí đầu tiên, điều dễ nhận thấy nhất là nó sẽ can thiệp vào cả vùng nhớ của mảng __*arr[]*__.
- Để chứng minh, phủ toàn bộ dữ liệu của vùng nhớ `long long` mà con trỏ d tham chiếu tới bằng một số cực lớn. Nếu làm vậy kết quả các tham số trong mảng __*arr[]*__ sẽ bị thay đổi.
    - Ở đây đối số đầu tiên là `0x7` không phải `0xF` để phân biệt hai số interger được khai báo. Một số là `0x7FFFFFFF` là số nguyên cố dấu lớn nhất, `0xFFFFFFFF` là số nguyên không dấu lớn nhất. Khi đặt ở trường hợp số có dấu, `0xFFFFFFFF` có giá trị là `-1`
- Kết quả như có thể thấy đấy là:
    1. Giá trị của `arr[0]` và `arr[1]` bị thay đổi.
    1. Mỗi giá trị tương ứng với một nửa giá trị của `long long`
    1. Nhưng có vẻ như bị __*ngược*__? Đọc thêm về [Endianness](http://localhost:65001/OS/os-endianness/)


## Sử Dụng

Điểm đầu tiên cần nhớ là nên khai báo chuỗi ở __*global*__ và tái sử dụng mảng là cách an toàn nhất. Tư duy đúng đắn là tạo ra một phân vùng dữ liệu gốc và tái sử dụng chúng để tránh việc khai báo và khởi tạo lặp gây __Memory Leak__.

Cách thứ hai đó là nên sử dụng các cơ sở dữ liệu sẵn có như `std::array` hoặc `std::vector` thay cho việc sử dụng các mảng cổ điển. Bạn đang lập trình trên ngôn ngữ bậc cao nên dùng các công cụ phù hợp với ngôn ngữ.

## STD Array

Mảng thuần C khá là nguy hiểm, nó liên quan trực tiếp đến địa chỉ của dữ liệu. Tránh trường hợp đó C++ cung cấp một thư viện hệ thống [std::array](cpp-std-array.md) cho mảng. Về bản chất nó vẫn giống như mảng nguyên thủy, chỉ khác duy nhất là đã được đóng gói và mở rộng nhiều giao thức an toàn để tương tác với mảng hơn lối sử dụng như mảng C thuần.