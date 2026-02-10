# Class

- __class__ về cơ bản giống như [struct](cpp-struct.md), nó thường được biết đến nhiều hơn với vai trò trong lập trình hướng đối tượng.
- __class__ và __struct__ giống nhau đến 99% trong cấu trúc bộ nhớ. Hầu hết sự khác biệt đến từ cách sử dụng. Về cơ bản class giống như struct có thêm _plugin_, một số thay đổi đáng kể như:
    - Truy cập phần tử mặc định của struct là public, class là private
    - class hỗ trợ thêm về các method kế thừa, ảo hóa, ... của cpp

## Các Thành Phần

Một lớp gồm 4 thành phần chính:

- __Thuộc tính (Attributes/Fields/Variables)__: là các biến nằm trong cấu trúc. Các biến đại diện cho các đặc điểm, thành phần con nằm trong đối tượng. Cụ thể hóa nó gọi như các thành phần của một cấu trúc lớn. Ví dụ như trong cấu trúc __Point__ ở bài [struct](cpp-struct.md), tọa độ __x, y__ chính là các thuộc tính.
- __Hàm (2)__:
    - __Hàm chức năng__: Hàm chức năng là các hàm thực thi nhiệm vụ. Nói đơn giản nó là __hàm trong một Class__. Các hàm này sẽ thực thi các nhiệm vụ liên quan đến lớp.
    - __Hàm Khởi Tạo/ Hàm Hủy__: Đây là hai loại hàm khác đặc biệt dành cho quá trình khởi tạo, hoặc hủy của một lớp. Xem thêm [Class Hàm Tạo, Hàm Hủy](cpp-class-constructor-destructor-function.md)
- __Access Specifiers__: Quyền truy cập vào các phần tử như hàm hoặc thuộc tính. Xem kỹ hơn tại [Class Access Specifiers](cpp-class-access-specifiers.md)

## Khai báo

Không khác lắm với struct ở kết cấu đầu tiên. Trừ việc các phần tử trong class là __*private*__ (xem qua [Class Access Specifiers](cpp-class-access-specifiers.md)).

## Hàm Tạo Hàm Hủy

```cpp
class ExampleClass {
    ExampleClass() {};
    virtual ~Example() {};
};
```

```cpp
class ExampleClass {
public:
    ExampleClass() {};
    virtual ~Example() {};
private:
    int id = 10;
};
```

```cpp
class ExampleClass {
public:
    ExampleClass(int id) : private_id(id) {

    };
    virtual ~Example() {};
    int getId() {
        return private_id;
    };
private:
    int private_id;
};
```