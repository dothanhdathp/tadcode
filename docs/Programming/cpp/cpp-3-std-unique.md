# std::unique

> Link tham khảo: [https://en.cppreference.com/w/cpp/algorithm/unique](https://en.cppreference.com/w/cpp/algorithm/unique)

## Mô tả

Thuật toán này để xoá những phần tử giống nhau có trong một mảng.

## Chuẩn bị

Trước tiên để thuận tiện sẽ chuẩn bị hàm `printvec` dùng để in `vector`

```cpp
template <typename T>
void printvec(std::vector<T> &v) {
    std::cout << "{ ";
    for (T i : v) {
        std::cout << i << ", ";
    }
    std::cout << " }" << std::endl;
}
```

## Sử dụng

### Loại bỏ phần tử liền kề giống nhau

```cpp
#include <iostream>     // std::cout
#include <algorithm>    // std::unique, std::distance
#include <vector>       // std::vector

template <typename T>
void printvec(std::vector<T> &v) {
    std::cout << "{ ";
    for (T i : v) {
        std::cout << i << ", ";
    }
    std::cout << " }" << std::endl;
}

int main () {
    std::vector<int> vec = {1,2,2,3,3,5,4,6,4,5,9,5,6};
    std::cout << "Origin: ";
    printvec<int>(vec);

    std::vector<int>::iterator it;
    it = std::unique (vec.begin(), vec.end());
    std::cout << "Vec:    ";
    printvec<int>(vec);

    return 0;
}
```

Kết quả:

```txt
Origin: { 1, 2, 2, 3, 3, 5, 4, 6, 4, 5, 9, 5, 6,  }
Vec:    { 1, 2, 3, 5, 4, 6, 4, 5, 9, 5, 6, 5, 6,  }
```

Có thể thấy các phần tử ___không thỏa mãn___ sẽ bị đẩy dần dần xuống phía dưới.

#### Loại bỏ phần thừa

Trong ví dụ trên, con trỏ `it` được trả ra là con trỏ đến phần tử cuối cùng không bị loại bỏ. Nói ngắn gọn hơn, từ `[vec.begin(), it]` là độ dài chuỗi hợp lệ của chuỗi `vector`. Có thể dùng `std::resize` để loại bỏ các phần tử bị loại bỏ ở cuối.

```cpp
int main () {
    std::vector<int> vec = {1,2,2,3,3,5,4,6,4,5,9,5,6};
    std::cout << "Origin: ";
    printvec<int>(vec);

    std::vector<int>::iterator it;
    it = std::unique (vec.begin(), vec.end());
    // Remove garbage Value
    vec.resize( std::distance(vec.begin(),it) );
    std::cout << "Vec:    ";
    printvec<int>(vec);

    return 0;
}
```

Kết quả:

```txt
Origin: { 1, 2, 2, 3, 3, 5, 4, 6, 4, 5, 9, 5, 6,  }
Vec:    { 1, 2, 3, 5, 4, 6, 4, 5, 9, 5, 6,  }
```

Giải thích:

- Các cặp `2,2`,`3,3` là hai phần tử giống nhau liền kề đã bị loại bỏ.

### Tạo chuỗi với phần tử độc nhất

Để có thể tạo chuỗi thành phần tử mà mỗi phần tử hoàn toàn khác nhau thì cần dùng thêm hàm `std::sort`

```cpp
int main () {
    std::vector<int> vec = {1,2,2,3,3,5,4,6,4,5,9,5,6};
    std::cout << "Origin: ";
    printvec<int>(vec);

    // Sort
    std::sort(vec.begin(), vec.end());

    std::vector<int>::iterator it;
    it = std::unique (vec.begin(), vec.end());
    // Remove garbage Value
    vec.resize( std::distance(vec.begin(),it) );
    std::cout << "Vec:    ";
    printvec<int>(vec);

    return 0;
}
```

Lúc này kết quả giảm đi khá nhiều.

```txt
Origin: { 1, 2, 2, 3, 3, 5, 4, 6, 4, 5, 9, 5, 6,  }
Vec:    { 1, 2, 3, 4, 5, 6, 9,  }
```

### Tùy biến với Lambda

Dùng ___lambda function___ để tùy biến cách thức hoạt động của hàm `std::unique`

#### Xem xét nguyên bản

Trước tiên thì xem xét tính năng nguyên bản. Hàm truyền vào so sánh hai số `a` và `b` và trả ra kết quả so sánh `==`.

```cpp
bool compare (int a, int b) {
    return (a==b);
}
```

Dưa hàm vào trong `std::unique`

```cpp
std::unique (vec.begin(), vec.end(), compare);
```

#### Lambda function

```cpp
std::unique (vec.begin(), vec.end(), [](int a, int b) {return a==b;});
```