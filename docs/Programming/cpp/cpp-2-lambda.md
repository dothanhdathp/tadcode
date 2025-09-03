## Định nghĩa

Hàm _lambda_, hay đơn giản là “lambda”, là một <u>hàm ẩn danh</u> (không có tên) được định nghĩa tại chỗ, trong mã nguồn của bạn và với cú pháp ngắn gọn. Hàm _lambda_ được giới thiệu trong C++11 và kể từ đó đã trở thành một tính năng được sử dụng rộng rãi, đặc biệt là khi kết hợp với các thuật toán __Thư viện chuẩn (std)__.

## Cú pháp

Sau đây là cú pháp cơ bản của hàm lambda trong C++:

```cpp
[capture-list](parameters) -> return_type {
    // function body
};
```

- `capture-list` : Danh sách các biến từ phạm vi xung quanh mà hàm lambda có thể truy cập.
- `parameters (tham số)` : Danh sách các tham số đầu vào, giống như trong một hàm thông thường. Tùy chọn.
- `return_type (kiểu trả về)` : Kiểu giá trị mà hàm lambda sẽ trả về. Phần này là tùy chọn và trình biên dịch có thể suy ra trong nhiều trường hợp.
- `function body (thân hàm)` : Mã định nghĩa hoạt động của hàm lambda.

### Ví dụ

Sau đây là một số ví dụ để chứng minh việc sử dụng hàm lambda trong C++:

- Hàm Lambda không có tham số, kiểu dữ liệu hoặc kiểu trả về.

```c++
auto printHello = []() {
    std::cout << "Hello, World!" << std::endl;
};
printHello(); // Output: Hello, World!
```

- Hàm Lambda có tham số.

```c++
auto add = [](int a, int b) {
    return a + b;
};
int result = add(3, 4); // result = 7
```

- Hàm Lambda với phương pháp nắm bắt theo giá trị.

```cpp
int multiplier = 3;
auto times = [multiplier](int a) {
    return a * multiplier;
};
int result = times(5); // result = 15 
```

- Hàm Lambda với tham chiếu.

```cpp
int expiresInDays = 45;
auto updateDays = [&expiresInDays](int newDays) {
    expiresInDays = newDays;
};
updateDays(30); // expiresInDays = 30
```

!!! note "Note"
    Lưu ý rằng, khi sử dụng __capture by reference__, bất kỳ thay đổi nào được thực hiện đối với biến được __capture__ bên trong hàm __lambda__ sẽ ảnh hưởng đến giá trị của biến đó trong phạm vi xung quanh.

## Tìm hiểu thêm

#### 💚 Tài nguyên miễn phí

1. [Biểu thức Lambda](https://en.cppreference.com/w/cpp/language/lambda)
1. [Lambda trong C++](https://youtu.be/MH8mLFqj-n8)
1. [Khám phá các bài đăng hàng đầu về AWS Lambda](https://app.daily.dev/tags/aws-lambda?ref=roadmapsh)