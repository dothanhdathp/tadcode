# \[C++\] Class Access Specifiers

> Phân bổ quyền truy cập

__Access Specifiers__ là cơ chế bảo vệ dữ liệu của C++. Việc này được sử dụng trong C++ nhằm bảo vệ vùng dữ liệu trong một lớp, cấu trúc nhằm nghiêm cấm tác động trực tiếp từ bên ngoài. Nói ngắn gọn là nó chỉ cấm người khác sử dụng các hành vi không mong muốn lên các đối tượng bạn khai báo trong lớp.

__Access Specifiers__ thật ra chỉ cấm được ở giai đoạn __*biên dịch*__. Tức là các thao tác này chỉ compiler hiểu. Trong chương trình thực thi, nó không hiểu, và thường được bỏ qua về nguyên bản.

Điều đó sẽ được giải thích sau, trước mắt thì có các cấp độ sau `public`, `private` và `protected`. Xét theo mức độ `public`, `private` và `protected`

## Public

Không có gì quá đặc biệt. Khi khai báo `public`, các tham số và hàm có thể truy cập tự do từ hàm ngoài.

## Private

- Với khai báo `private`, chỉ các phương thức con bên trong lớp mới có thể truy cập.
- `private` cấm kế thừa. Các lớp kế thừa không thể sử dụng các phần tử này.

## Protected

Với khai báo `protected`, các lớp con sau khi kế thừa có thể sử dụng các phương thức này. Nhưng hoạt động giống với `private`. Nói ngắn gọn nếu bạn muốn một phần tử có thể kế thừa _(tái sử dụng)_ đồng thời cũng che giấu thì dùng phương thức này.

Xem ví dụ:

```cpp
#include <iostream>

class Father {
public:
    int  height = 180;
    int  weight = 80;
    int  age = 40;
private:
    bool have_wife = true;
protected:
    int hidden_power = 2;
    
public:
    Father() {};
    int getSize() {
        return height*weight;
    };
    int getPower() {
        return hidden_power*age;
    };
};

class Child : public Father {
public:
    Child() {
        height = 160;
        weight = 50;
        age = 16;
    };

    int getHiddenPower() {
        return hidden_power;
    };
    // int getWife() {
    //     return have_wife;
    // };
};


int main() {
    Child c;

    std::cout << "[C] *height       : " << c.height << std::endl;
    std::cout << "[C] *weight       : " << c.weight << std::endl;
    std::cout << "[C] *age          : " << c.age << std::endl;
    // std::cout << "[C] *hidden_power : " << c.hidden_power << std::endl;
    std::cout << "[C] Size          : " << c.getSize() << std::endl;
    std::cout << "[C] Power         : " << c.getPower() << std::endl;
    std::cout << "[C] Hidden Power  : " << c.getHiddenPower() << std::endl;
    return 0;
}
```
```text title="Kết Quả"
[C] *height       : 160
[C] *weight       : 50
[C] *age          : 16
[C] Size          : 8000
[C] Power         : 32
[C] Hidden Power  : 2
```

- __*public*__ chắc chắn vẫn được kế thừa và truy cập trực tiếp
- `hidden_power` được kế thừa như __*protected*__. Về hoạt động hành xử trong lớp con như một biến __*private*__, cấm truy cập từ ngoài nhưng vẫn cho phép gọi đến từ các phương thức.
- `have_wife` là __*private*__, không thể kế thừa luôn rồi.