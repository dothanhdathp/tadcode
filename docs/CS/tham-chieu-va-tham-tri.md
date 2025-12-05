# \[Common\] Tham Chiếu Và Tham Trị

> Tham Khảo: [Tham Chiếu Và Tham Trị trong C++](https://codelearn.io/sharing/tham-chieu-va-tham-tri-trong-cpp)

## Đôi Lời

Khái niệm này chỉ cách mà giá trị của một biến truy vấn được đưa vào một hàm và xử lý. Chức năng thì đã có từ ngôn ngữ C nhưng có lẽ đến C++ nó mới hình thành khái niệm và được sử dụng làm tiêu chuẩn.

## Tham Trị

__Truyền Tham Trị__ tức là chỉ truyền cho hàm một giá trị. Các phép tính và thay đổi của hàm lên giá trị đầu vào không làm thay đổi giá trị gốc của dữ liệu được truyền vào.

Ví dụ:

```cpp
void dosomething(int a) {
    // do something in here
}

int main() {
    int a = 0;
    dosomething(a);
    printf("a = %d\n", a);
    return 0;
}
```

Ở ví dụ trên, bất kể trong hàm `dosomething()` có làm gì thì cũng không tác động đến giá trị gốc của `a`.

## Tham Trị

__Truyền Tham Trị__ tức là truyền cho hàm địa chỉ. Hay hiểu rộng hơn đó là __*truyền chính xác bản thân biến a vào hàm*__. Lúc này khi hàm thực hiện các phép toán bên trong nếu có tác động thì sẽ trực tiếp tác động lên bản thân của biến `a`

```cpp
void dosomething(int &a) {
    // do something in here
    a = 10; // example
}

int main() {
    int a = 0;
    dosomething(a);
    printf("a = %d\n", a);
    return 0;
}
```
Như ví dụ trên, sau khi thoát khỏi hàm `dosomething(a)`, giá trị của `a` lên 10.