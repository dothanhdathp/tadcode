# Hàm

## Định Nghĩa Hàm

> Hàm là một nhóm __các__ câu lệnh thực hiện một nhiệm vụ cụ thể, được tổ chức như một đơn vị riêng biệt trong một chương trình. Hàm giúp chia nhỏ mã thành các khối nhỏ hơn, dễ quản lý và có thể tái sử dụng.

## Khai Báo

Định dạng chung để định nghĩa hàm trong C++ là:
```cpp
<return_type> function_name(<parameter list>) {
    // function body
}
```

Trong đó:

- `return_type`: Kiểu dữ liệu của đầu ra do hàm tạo ra. Có thể là void, biểu thị rằng hàm không trả về bất kỳ giá trị nào.
- `function_name`: Tên được đặt cho hàm, theo quy ước đặt tên C++.
- `parameter list`: Danh sách các tham số/đối số đầu vào cần thiết để thực hiện tác vụ. Đây là tùy chọn, bạn có thể để trống khi không cần tham số nào.
    - Các thành phần của __*parameter list*__ yêu cầu loại biến. Đôi khi, tên biến lại không cần thiết.e

### Ví dụ

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

## Nguyên Mẫu Hàm

> Khai báo cấu trúc hàm trước rồi mới viết nội dung.

- Nguyên mẫu chức năng của hàm có thể được khai báo trước mà không cần nội dung hàm. Trong ví dụ này hàm `multiplyNumbers` được khai báo trước cấu trúc với hai đối số đầu vào là _interger_ trước khi nội dung của hàm được khai báo.
- Sau khi khai báo nguyên mẫu, nội dung của hàm có thể được viết ở bất kỳ đâu trong mã. Điều này khá là khác biệt so với ngôn ngữ C khi bắt buộc các hàm phải khai báo tuần tự.
- Cách này cũng thường được dùng khi các hàm có thứ tự sử dụng chồng chéo.

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

### Lỗi Chồng Chéo

Một ví dụ vui về việc hai hàm gọi chéo nhau đẫn đến __deadlock__. Hai hàm khóa với nhau không thể thoát.

```cpp
#include <iostream>

int funtion_a();
int funtion_b();

int funtion_a () {
    std::cout << "Call: " << __func__ << std::endl;
    return funtion_b();
}

int funtion_b () {
    std::cout << "Call: " << __func__ << std::endl;
    return funtion_a();
}

int main() {
    funtion_a();
    return 0;
}
```

Trong ví dụ trên, hàm __*funtion_a*__ gọi đến __*funtion_b*__ và ngược lại, dẫn đến vòng lặp gọi chéo nhau vô tận.

## Hàm và Tham Số

### Tham Số Mặc Định

Các tham số của hàm có thể được khai báo mặc định. Khi đó nếu tham số đầu vào không được khai báo, hàm sẽ sử dụng tham số mặc định để thực thi.

```cpp
#include <iostream>

int sum(int a=0, int b=0) {
    std::cout << "a = " << a << std::endl;
    std::cout << "b = " << b << std::endl;
    int ans = a + b;
    std::cout << "Sum of a + b = " << ans << std::endl;
    return ans;
}

int main() {
    sum();
    return 0;
}
```

```text title="Kết Quả"
a = 0
b = 0
Sum of a + b = 0
```

### Pass By Reference

Khi sử dụng dấu `&` trước tên của tham số được truyền vào hàm thì nó có nghĩa là truyền tham trị, hay chính bản thân biến đó được đưa vào làm tham số. Nếu tham số bị thay đổi, nó sẽ thay đổi giá trị được truyền vào sau khi thoát hàm.

```cpp
#include <iostream>

void plus_one(int & input) {
    ++input;
}

int main() {
    int a = 1;
    plus_one(a);
    std::cout << a << std::endl;
    return 0;
}
```
```text title="Kết Quả"
2
```

Nó cũng khá dễ hiểu khi `&var` có nghĩa là lấy địa của biến, thế nên nó khá giống với ý nghĩa truyền con trỏ vào để thực thi. Đoạn code trên cũng tương đương với đoạn sau:

```cpp
#include <iostream>

void plus_one(int* input) {
    *input += 1;
}

int main() {
    int a=1;
    plus_one(&a);
    std::cout << a << std::endl;
    return 0;
}
```
```text title="Kết Quả"
2
```

### Truyền Chuỗi

Chuỗi là một chuỗi dữ liệu gốc được khai báo trong Heap thế nên nó hoàn toàn không được lưu trong stack, khi này để truyền vào một chuỗi, bắt buộc phải truyền dưới dạng tham trị, hoặc con trỏ.

=== "Cách 1"
    ```cpp
    void show_arr(int arr[]) {
        for (int i=0; i<10; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }

    int main() {
        int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        show_arr(arr);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    0 1 2 3 4 5 6 7 8 9 
    ```
=== "Cách 2"
    ```cpp
    void show_arr(int *arr) {
        for (int i=0; i<10; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }

    int main() {
        int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        show_arr(arr);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    0 1 2 3 4 5 6 7 8 9 
    ```

Mặc dù cả hai cách trên đều hoạt động nhưng dễ nhận thấy một điều là nó không an toàn. Tốt nhất khi đưa vào một chuỗi nên, phải có kèm thêm kích thước bởi __*complier*__ không thể biết được giới hạn trong chuỗi cơ bản.

=== "Cách 1 _(improved)_"
    ```cpp
    void show_arr(int arr[], size_t _size) {
        for (int i=0; i<_size; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }

    int main() {
        int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        show_arr(arr);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    0 1 2 3 4 5 6 7 8 9 
    ```
=== "Cách 2 _(improved)_"
    ```cpp
    void show_arr(int *arr, size_t _size) {
        for (int i=0; i<_size; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    }

    int main() {
        int arr[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        show_arr(arr, 10);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    0 1 2 3 4 5 6 7 8 9 
    ```

### Truyền Struct

Về cơ bản _struct_ cũng hoạt động cũng giống như các biến thông thường, nó vẫn có hai phương thức là truyền tham chiếu và tham trị. Tham trị thì thay đổi giá trị của biến bị truyền vào.

=== "Tham Chiếu"
    ```cpp
    #include <iostream>

    struct pos {
        int x;
        int y;
    };

    void change_p(pos p) {
        p.x = 10;
        p.y = 10;
        std::cout << "~ p.x = " << p.x << std::endl;
        std::cout << "~ p.y = " << p.y << std::endl;
    }

    void show_p(pos p) {
        std::cout << "! p.x = " << p.x << std::endl;
        std::cout << "! p.y = " << p.y << std::endl;
    }

    int main() {
        pos p = {1, 2};
        change_p(p);
        show_p(p);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    ~ p.x = 10
    ~ p.y = 10
    ! p.x = 1
    ! p.y = 2
    ```
=== "Tham Trị"
    ```cpp
    #include <iostream>

    struct pos {
        int x;
        int y;
    };

    void change_p(pos &p) {
        p.x = 10;
        p.y = 10;
        std::cout << "~ p.x = " << p.x << std::endl;
        std::cout << "~ p.y = " << p.y << std::endl;
    }

    void show_p(pos p) {
        std::cout << "! p.x = " << p.x << std::endl;
        std::cout << "! p.y = " << p.y << std::endl;
    }

    int main() {
        pos p = {1, 2};
        change_p(p);
        show_p(p);
        return 0;
    }
    ```
    ```text title="Kết Quả"
    ~ p.x = 10
    ~ p.y = 10
    ! p.x = 10
    ! p.y = 10
    ```

## Function Overload

Các hàm có thể trùng tên và khác `prototype`. Sử dụng hàm theo các `prototype` khác nhau đưa ra kết quả khác nhau.

```cpp
#include <iostream>

int unix_function(int a, int b) {
    return a + b;
}

std::string unix_function(std::string a, std::string b) {
    return std::string(a + std::string(" ") + b);
}

int main() {
    int a=1, b=4;
    std::string str_a = "Hello";
    std::string str_b = "World";
    std::cout << unix_function(a, b) << std::endl;
    std::cout << unix_function(str_a, str_b) << std::endl;
    return 0;
}
```
```text title="Kết Quả"
5
Hello World
```

## Auto Type Cast

Một điều quan trọng cần phải chú ý là hàm có tính chất tự động ép kiểu cho cả đầu vào và đầu ra. Nghĩa là giả sử bạn đưa vào sai kiểu được khai báo thì biến sẽ tự động bị ép kiểu về đúng với __*prototype*__

```cpp
#include <iostream>

int function(int a, int b) {
    return a + b;
}

int main() {
    char a = 'A'; // 65
    char b = 'B'; // 66
    std::cout << function(a, b) << std::endl;
    return 0;
}
```
```text title="Kết Quả"
131
```

__*Compiler*__ chỉ báo lỗi khi không thể thực hiện được ép kiểu ngầm định.

```cpp
#include <iostream>

std::string function(std::string a, std::string b) {
    return a + b;
}

int main() {
    char a = 'A'; // 101
    char b = 'B'; // 102
    std::cout << function(a, b) << std::endl;
    return 0;
}
```
```text
Lỗi không thể build vì không thể cast từ char thành std::string
```

## Tham Khảo

- [(w3schools) Functions](https://www.w3schools.com/cpp/cpp_functions.asp)

<!-- Hidding -->
<div style="display: none;">

- [Lambda Function](cpp-lambda-function.md)
- [Function as Parameter](cpp-function-as-parameter.md)

</div>