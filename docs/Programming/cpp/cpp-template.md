# Template

## Định Nghĩa

- __Template__ là tính lập trình khuôn mẫu trong C++

- Tác dụng của chức năng này là tạo ra một kiểu _hàm chức năng_, hoặc _lớp_ có thể tái sử dụng trên nhiều kiểu dữ liệu mà không cần phải sử dụng tính nạp chồng __*(overloading)*__ nhiều lần.
- __Template__ cho phép đặt bất kỳ một dạng biến nào đặt trong `<>` thành một dạng tên gọi. Tiến trình thay thế sẽ được hoạt động ở tiền trình biên dịch. Thế nên nếu phía hàm, hoặc lớp không thể thực hiện được một chức năng nào đó sẽ có lỗi thông báo.
- __Template__ cũng không có tính chất cục bộ. Tức là nếu bạn khai báo ở tập A, điều đó cũng không được đưa sang tập B, C, D, ... với cùng typename. __Template__ một biến gì chỉ có thể sử dụng được trong khu vực của lớp hoặc cấu trúc đó _(mình nghĩ có lẽ là giữa hai ký tự đóng ngoặc {})_
- Thông thường __template__ sẽ được dùng cho hàm hoặc là cho một lớp để khái quát hóa hàm/lớp đó cho nhiều kiến trúc.
- __C__ không có `template` 

## Template Function

```cpp title="Ví Dụ"
#include <iostream>
#include <vector>

template <typename T>
void printVector(std::vector<T> &vec, const char ftm[])
{
    for (auto i : vec) {
        printf(ftm, i);
    }
    putchar('\n');
}

// not recornize type T
// void printVector2(std::vector<T> &vec, const char ftm[]) {};
```

Trong hàm trên để in tất cả các giá trị bất kỳ của một __*vector*__ kèm theo một _fmt_ là chuỗi đầu vào nhằm có thể biểu diễn chính xác ý định của biến đó trên màn hình.

Sử dụng __*printf*__ vì __*printf*__ là một hàm C cơ bản, nó không có sử dụng <u>type safe</u> nên không có ảnh hưởng trong các kiểu dữ liệu khác nhau, và cả hỗ trợ __*C typecast*__. Không khuyến khích nhưng cấp độ ví dụ và ứng dụng đơn giản thì ổn.

__T__ có thể là bất cứ kiểu cơ bản nào, miễn là __*printf*__ có thể in được chúng là được.

Như đã nó T chỉ có tính chất cục bộ. Vì thế nếu có một hàm phía dưới _(dù ở ngay sau)_ nó cũng không được kế thừa kiểu thiết kế của __*template*__.

## Template Class

Nếu muốn có nhiều hàm có cùng kiến trúc được sử dụng __*template*__, có thể sử dụng __*template*__ cho __*class*__.

Như ví dụ dưới này:

```cpp title="Ví Dụ"
#include <iostream>
#include <vector>

template <typename T>
class VecPrinter
{
public:
    void printVector(std::vector<T> &vec, const char ftm[]) {
        for (auto i : vec) {
            printf(ftm, i);
        }
        putchar('\n');
    };
    void print2DVector(std::vector<std::vector<T>> &two_dimen_vector, const char ftm[]) {
        for (std::vector<T> vec : two_dimen_vector) {
            printVector(vec, ftm);
        }
        putchar('\n');
    };
};

int main(int argc, const char* args[])
{
    VecPrinter<size_t> printer;
    std::vector<std::vector<size_t>> sample = {
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
        {0,1,2,3,4,5,6,7,8,9},
    };
    printer.print2DVector(sample, "%ld ");
    return 0;
}
```

Cả __*printVector*__ và __*print2dVector*__ đều có thể kế thừa dạng thiết kế T của _class_.


### Tính Chất Cục Bộ

Khi viết `template` cho lớp cần đặc biệt cần lưu ý về tính chât cục bộ của nó.

Vấn đề, kiến trúc của một lớp đôi khi thường rất dài. Thường thì người ta chỉ khai báo nguyên mẫu hàm bên trong lớp để dễ quản lý các tính chất về [Access](). Và theo đó là các triển khai của lớp sẽ được viết ở tệp `.cpp`. Dạng như này:

```cpp title="VecPrinter.hpp"
#include <iostream>
#include <vector>

template <typename T>
class VecPrinter
{
public:
    void printVector(std::vector<T> &vec, const char ftm[]);
    void print2DVector(std::vector<std::vector<T>> &two_dimen_vector, const char ftm[]);
};
```

Nhưng nếu viết tách tệp, lúc này nguyên mẫu hàm bị lỗi, trên thực tế lúc này hàm của lớp và hàm cục bộ không còn có liên quan. Lỗi thường thấy nhất khi chạy chương trình là `undefined reference to ...` hoặc đôi khi là không thể tìm thấy hàm.

Để khắc phục tình trạng đó <mark>bắt buộc phải viết nội dung hàm bên dưới khai báo hàm.</mark>. Cách triển khai như sau:

```cpp title="VecPrinter.hpp"
#include <iostream>
#include <vector>

template <typename T>
class VecPrinter
{
public:
    // Khai báo nguyên mẫu hàm
    void printVector(std::vector<T> &vec, const char ftm[]);
    void print2DVector(std::vector<std::vector<T>> &two_dimen_vector, const char ftm[]);
};

// Viết nội dung hàm trên cùng một tệp
template <typename T>
void VecPrinter<T>::printVector(std::vector<T> &vec, const char ftm[]) {
    for (auto i : vec) {
        printf(ftm, i);
    }
    putchar('\n');
};

// Viết nội dung hàm trên cùng một tệp
template <typename T>
void VecPrinter<T>::print2DVector(std::vector<std::vector<T>> &two_dimen_vector, const char ftm[]) {
    for (std::vector<T> vec : two_dimen_vector) {
        printVector(vec, ftm);
    }
    putchar('\n');
};
```