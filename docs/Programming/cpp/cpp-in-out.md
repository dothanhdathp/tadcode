# \[C++\] Input & Output
> Chương này nói về các hoạt động đầu vào đầu ra của C++

## C Type

Kế thừa từ C nên C++ cũng có thể dùng các hàm in cơ bản của C như `printf()`, `putc()`, `scanf()`, ...

```cpp title="Ví Dụ Tham Khảo"
#include <cstdio>

int main() {
    // print string
    printf("Hello World!\n");
    // print char
    putchar('H');
    // get input
    char str_input[20];
    scanf("%s", str_input);
    printf("Input: %s\n", str_input);
    return 0;
}
```

Để biết chi tiết hơn đọc thêm ở [C printf](../c/c-printf.md), [C scanf](../c/c-scanf.md).

## STD CIN/COUT

`std::cin` và `std::cout` là một phần cuả thư viện _iostream_. Trong đó định nghĩa. Thư viện __*iostream*__

```cpp
#include <ios> 
#include <streambuf> 
#include <istream> 
#include <ostream>
 
namespace std { 
    extern istream cin ; 
    extern ostream cout ; 
    extern ostream cerr ; 
    extern ostream clog ;

    extern wistream wcin ; 
    extern wostream wcout ; 
    extern wostream wcerr ; 
    extern wostream wclog ; 
}
```

Thư viện này chứa các hàm cơ bản điều khiển đầu ra __*in/out*__. Các hàm thường dùng nhất là `std::cin` và `std::cout`.

Thư viện __*iostream*__ mới là thư viện chuẩn đầu ra vào cho C++ bởi nó an toàn luồng, nhưng hầu hết mọi người thích dùng _printf()_ của C hơn vì nó nhanh hơn.

```cpp
#include <iostream>

int main() {
    // Output
    std::cout << "Hello World" << std::endl;

    // Input
    int input;
    std::cout << "Input Number: ";
    std::cin >> input;
    std::cout << "Input: " << input << std::endl;
}
```

## \[C++17\] Wrap in Println

Nhưng việc sử dụng std::cout khá là phiền. Ở C++17 có thể sử dụng hàm sau:

```cpp
#include <iostream>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl; // C++17 Fold Expression
}

int main() {
    println("Hello World!");
    return 0;
}
```

Hàm này đóng gói lại lệnh gọi hàm `std::cout` từ __C++__, cung cấp một hàm với giao thức khác dễ dùng, dễ đọc hơn.

!!! danger "print và println (C++23)"
    Có hai hàm __print__ và __println__ được phát triển từ __*C++23*__. Các hàm này phát triển khá là giống __Rust__, thay vì sử dụng `%s`, `%d`, ... như C, hàm này thay các đối số vào các vị trị `{}`:

    Nhưng khi dựng thử nghiệm hàm đó có vẻ chưa được phổ biến cho lắn nên để sau đi.