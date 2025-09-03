> Hàm là một nhóm __các__ câu lệnh thực hiện một nhiệm vụ cụ thể, được tổ chức như một đơn vị riêng biệt trong một chương trình. Hàm giúp chia nhỏ mã thành các khối nhỏ hơn, dễ quản lý và có thể tái sử dụng.

## Định nghĩa một hàm

Về cơ bản có hai loại hàm trong C++:

- __Các hàm thư viện chuẩn__: Các hàm được định nghĩa trước có trong thư viện chuẩn C++, chẳng hạn như sort(), strlen(), sqrt(), và nhiều hàm khác nữa. Các hàm này là một phần của thư viện chuẩn, do đó bạn cần đưa vào tệp tiêu đề thích hợp để sử dụng chúng.
- __Hàm do người dùng định nghĩa__: Hàm do lập trình viên tạo ra để thực hiện một tác vụ cụ thể. Để tạo hàm do người dùng định nghĩa, bạn cần định nghĩa hàm và gọi hàm đó trong mã của mình.

## Định nghĩa một hàm

Định dạng chung để định nghĩa hàm trong C++ là:
```cpp
return_type function_name(parameter list) {
    // function body
}
```

Trong đó:

- `return_type`: Kiểu dữ liệu của đầu ra do hàm tạo ra. Có thể là void, biểu thị rằng hàm không trả về bất kỳ giá trị nào.
- `function_name`: Tên được đặt cho hàm, theo quy ước đặt tên C++.
- `parameter list`: Danh sách các tham số/đối số đầu vào cần thiết để thực hiện tác vụ. Đây là tùy chọn, bạn có thể để trống khi không cần tham số nào.

## Ví dụ

```cpp
#include <iostream>

// Function to add two numbers
int addNumbers(int a, int b) {
    int sum = a + b;
    return sum;
}

int main() {
    int num1 = 5, num2 = 10;
    int result = addNumbers(num1, num2); // Calling the function
    std::cout << "The sum is: " << result << std::endl;
    return 0;
}
```

Trong ví dụ này, hàm `addNumbers` lấy hai tham số nguyên `a` và `b`, và trả về tổng của các số. Sau đó, chúng ta gọi hàm này từ hàm ___main()___  và hiển thị kết quả.

## Nguyên mẫu chức năng

Trong một số trường hợp, bạn có thể muốn sử dụng một hàm trước khi <u>thực sự định nghĩa nó</u>. Để làm như vậy, bạn cần khai báo một ___nguyên mẫu hàm___ ở đầu mã của mình.

Nguyên mẫu hàm là một khai báo hàm không có phần thân và thông báo cho trình biên dịch về tên hàm, kiểu trả về và các tham số.

```cpp
#include <iostream>

// Function prototype
int multiplyNumbers(int x, int y);

int main() {
    int num1 = 3, num2 = 7;
    int result = multiplyNumbers(num1, num2); // Calling the function
    std::cout << "The product is: " << result << std::endl;
    return 0;
}

// Function definition
int multiplyNumbers(int x, int y) {
    int product = x * y;
    return product;
}
```

Trong ví dụ này, chúng ta sử dụng một nguyên mẫu hàm `multiplyNumbers()` trước khi định nghĩa nó. Theo cách này, chúng ta có thể gọi hàm từ hàm `main()` mặc dù nó chưa được định nghĩa trong mã.

Tìm hiểu thêm từ các nguồn sau: [Introduction to functions](https://www.learncpp.com/cpp-tutorial/introduction-to-functions/)