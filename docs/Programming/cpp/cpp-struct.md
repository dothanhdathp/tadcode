# \[C++\] Struct

__Struct__ là cấu trúc khối, gom nhiều giá trị lại với nhau đạt thành một ngữ nghĩa.

## Khai Báo

=== "Thông thường"
    ```cpp
    struct Pointer {
        int x = 1;
        int y = 1;
    };

    int main() {
        Pointer p;
        std::cout << p.x << ' ' << p.y << std::endl;
        return 0;
    }
    ```
=== "Không khởi tạo"
    ```cpp
    struct Pointer {
        int x = 1;
        int y = 1;
    };

    int main() {
        Pointer p;
        std::cout << p.x << ' ' << p.y << std::endl;
        return 0;
    }
    ```
    Không khởi tạo tuy không sao nhưng không nên. Trình biên dịch sẽ cảnh báo. Và đôi khi sẽ gây lỗi không xác định.
=== "Biến Độc Lập"
    ```cpp
    struct Pointer {
        int x = 1;
        int y = 1;
    } p;

    int main() {
        std::cout << p.x << ' ' << p.y << std::endl;
        return 0;
    }
    ```

## Căn chỉnh

### Hiện Tượng

__Data Structure Alignment__ (Căn chỉnh dữ liệu) và kết quả của nó là việc tạo ra các khoảng trống gọi là __Padding__ (Đệm dữ liệu) giữa các dữ liệu có kích thước khác nhau, thường là khi từ dữ liệu nhỏ bị đặt trước dữ liệu lớn.

Đây không phải là lỗi mà là tính năng. Vì máy tính đặt thường sẽ chỉ truy cập vào các vùng dữ liệu trên RAM theo các khối (block). Các khối này có đơn vị thấp nhất là một `size_t` theo kiến trúc phần cứng. Các giá trị nhỏ hơn ví dụ đến từng `bits` sẽ được CPU dịch bit, đọc và trả ra kết quả. Vì thế nếu dữ liệu khai báo ví dụ `short` nhỏ hơn một vùng nhớ cơ bản của RAM nó sẽ tự động được phân bổ vào một khu vực lớn hơn để tiện truy cập.

Cái này dễ hiểu vì các hệ thống máy tính lớn, việc thiếu hụt phần nhỏ như vậy tốn ít chi phí hơn tốc độ truy cập.

```cpp
struct Pointer1 {
    int x = 1;
    int y = 1;
};

struct Pointer2 {
    short x = 1;
    int y = 1;
};

struct Pointer3 {
    short x = 1;
    short y = 1;
};

int main() {
    std::cout << "Size of Pointer1: " << sizeof(Pointer1) << std::endl;
    std::cout << "Size of Pointer2: " << sizeof(Pointer2) << std::endl;
    std::cout << "Size of Pointer3: " << sizeof(Pointer3) << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Size of Pointer1: 8
Size of Pointer2: 8
Size of Pointer3: 4
```

## Tối Ưu hóa vùng nhớ

Tối ưu hóa vùng nhớ ta

```cpp
struct Pointer1 {
    int x = 1;
    int y = 1;
} __attribute__((packed));

struct Pointer2 {
    short x = 1;
    int y = 1;
} __attribute__((packed));

struct Pointer3 {
    short x = 1;
    short y = 1;
} __attribute__((packed));

int main() {
    std::cout << "Size of Pointer1: " << sizeof(Pointer1) << std::endl;
    std::cout << "Size of Pointer2: " << sizeof(Pointer2) << std::endl;
    std::cout << "Size of Pointer3: " << sizeof(Pointer3) << std::endl;
    return 0;
}
```
```text title="Kết Quả"
Size of Pointer1: 8
Size of Pointer2: 6
Size of Pointer3: 4
```

## Construct/Deconstruct

struct cũng có viết hàm tạo và hàm hủy giống như [class](cpp-class.md).

```cpp
struct Pointer {
    int x;
    int y;

    Pointer(int a, int b) {
        x = a;
        y = b;
    }

    ~Pointer() {
        std::cout << "Delete Pointer" << std::endl;
    }
};

void example_Point() {
    Pointer p(1, 2);
    std::cout << "p.x = " << p.x << std::endl;
    std::cout << "p.y = " << p.y << std::endl;
}

int main() {
    example_Point();
    return 0;
}
```
```text title="Kết Quả"
p.x = 1
p.y = 2
Delete Pointer
```

## Bit-field

__Bit-field__ là kỹ thuật khai báo số lượng bit chính xác cho từng biến thành phần __*struct*__ nhằm tối ưu hóa mạnh bộ nhớ, tối ưu dung lượng dữ liệu sử dụng tránh lãng phí.

Ví dụ tạo một __struct__ lưu trữ dữ liệu của một học sinh gồm các chỉ số như sau:
- __Cấp (Level)__: Một trường trung học ở VN chỉ có 4 cấp là 6,7,8,9.
- __Lớp (Class)__: Tiếp đến ở mỗi cấp chỉ có 10 lớp,đại loại 6-1, 6-2, ..., 6-10.
- __Số thứ tự trong lớp (Index)__: Mỗi lớp chỉ chứa được tối đa 40 học sinh.

Đánh giá:

- __Cấp (Level)__: Chỉ có 4 cấp lớn nhất là 9 chỉ cần 4 bits biểu diễn.
- __Lớp (Class)__: Số lớp lớn nhất là 10, cũng chỉ cần 4 bits biểu diễn.
- __Số thứ tự trong lớp (Index)__: Tối đa 40 học sinh cần, cần 6 bits biểu diễn.

```cpp
struct HS {
    int Level = 6;
    int Class = 1;
    int Index = 1;
};

struct HS_bit_field {
    int Level : 8  = 6;
    int Class : 8  = 1;
    int Index : 16 = 1;
};

int main() {
    std::cout << "Size of HS: "           << sizeof(HS) << std::endl;
    std::cout << "Size of HS_bit_field: " << sizeof(HS_bit_field) << std::endl;
    return 0;
}
```
```text title="Kết quả"
Size of HS: 12
Size of HS_bit_field: 4
```

Ở đây thay vì __*Bit-field*__ chính xác là `4:4:6`, chọn `8:8:16` vì máy tính có 3 độ chia đọc giá trị là:

- Đọc địa chỉ: Đọc địa chỉ của một thanh ghi cơ bản trong RAM, có thể 32 hoặc 64 bit.
- Đọc 1 WORD: đọc 1 WORD = 1 BYTES, đọc từng byte riêng, khối 8 bits
- Đọc 1 BIT: đọc từng bit

Thế nên tốt nhất nên chia thành các khối bội của `1 bytes` nếu không cần thiết tối giản về từng bits trong __bit-field__. Đọc từng bits đều tốn kém CPU hơn rất nhiều, nữa là đằng nào muốn hay không địa chỉ bộ nhớ đó cũng đã bị chiếm dụng nên cấp độ nhỏ nhất đã là 4 bytes cho tên 1 cấu trúc.

Cho nên chỉ cần tiết kiệm khi:

- Lập trình nhúng với bộ nhớ ít ỏi
- Một cấu trúc có bội nhân, số lượng phần tử độc lập lớn. Ví dụ như có đoạn khai báo một mảng 1.000.000 phần tử HS. Lúc này chỉa ra tốn `~11MB` nếu không __*bit-field*__, sau khi __*bit_field*__ dung lượng giảm xuống còn dưới `4MB`. Cho cả một đất nước hoặc thế giới, dung lượng tiết kiệm được càng đáng kể.

## Struct Access Specifiers

Đây chỉ là một fact vui. struct có thể sử dụng __Access Specifiers__. Điều này vì bản chất __class__ được xây dựng trên __struct__.

Các phương thức truy cập cũng tương tự. Chỉ là gây lú lẫn về ý nghĩa sử dụng nên chả ai dùng.

```cpp
#include <iostream>

struct struct_hs {
private:
    int Level : 8;
    int Class : 8;
    int Index : 16;
public:
    struct_hs(int v) {
        Level = v;
        Class = v;
        Index = v;
    }
};

int main() {
    struct_hs shs(4);
    void* d = &shs;
    char* arr = (char*)d;
    std::cout << static_cast<int>(arr[0]) << std::endl;
    std::cout << static_cast<int>(arr[1]) << std::endl;
    std::cout << static_cast<int>(arr[2]) << std::endl;
    std::cout << static_cast<int>(arr[3]) << std::endl;
    return 0;
}
```