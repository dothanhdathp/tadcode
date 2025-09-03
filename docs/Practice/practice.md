# Practice

!!! abstract "Abstract"
    Tôi có đại ý cho phần này là thay vì dán tên lên trên từng trang ___leetcode___ một thì có thể làm một trang khác và lập danh sách các bài leetcode. Lúc này `extension` set sẽ có hiệu quả.

Để chuẩn bị cho việc lập trình cạnh tranh cùng nhiều test case có thể dùng như sau:

## Chuẩn bị chương trình

Chương trình chạy thử cho ___leetcode___ đơn giản sẽ được viết bằng hàm `main.exe` và nhận các giá trị đầu vào qua tệp. Bài này khá thích hợp khi đầu vào là một chuỗi, và có nhiều `testcase`.

Ý tưởng này đại loại là sẽ chuyển dữ liệu test thành tệp đầu vào `input` và lần lượt đưa vào 

### Hàm đọc đầu vào và chuyển thành vector

```cpp
template <typename T>
std::vector<T> input_vector()
{
    size_t vector_size;
    std::cin >> vector_size;
    std::vector<T> r_vec;
    while(vector_size--) {
        T ref;
        std::cin >> ref;
        r_vec.push_back(ref);
    }
    return r_vec;
}
```

Trong hàm trên có tác dụng lấy đầu vào theo cấu trúc `[Kích thước]` + `[{các giá trị}]`

Ví dụ đầu vào là `3 4 5 6` thì sẽ kết xuất được `std::vector` là `{4,5,6}` với kích thước là `3`.

### Để sau hãy nói 

## Thao tác kiểm thử

Ở đây lấy bài `leetcode-1486` làm ví dụ:

```cpp title="main.cpp"
#include <iostream>
#include <ostream>
#include <stdlib.h>
#include <limits>
#include <cstdint>
#include <vector>
#include <string>
#include <bitset>

#define N (10000)

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"

int xorOperation(int n, int start) {
    if(1==n)
        return start;

    return (start + 2*(n-1))^xorOperation(n-1, start);
}

// int main(int argc, char *argv[]) {
int main() {
    int total_testcase;
    std::cin >> total_testcase;
    int buff = total_testcase;
    while (buff--)
    {
        int n;
        int start;
        int expected;
        std::cin >> n;
        std::cin >> start;
        std::cin >> expected;
        int answer = xorOperation(n, start);
        // Check the test
        if(expected==answer) {
            printf(ANSI_COLOR_GREEN "[Case %d] PASS!\n", (total_testcase - buff));
        } else {
            printf(ANSI_COLOR_RED "[Case %d] FALSE\n", (total_testcase - buff));
            printf(ANSI_COLOR_RESET "\tAnswer   : %d\n", answer);
            printf(ANSI_COLOR_RESET "\tExpected : %d\n", expected);
        }
    }
    return 0;
}
```

Tổng thể bài này không có gì đáng xem, chủ yếu chính là việc thực hiện kiểm thử chương trình với tệp đầu vào `input`. Tệp đó nội dung như này:

```txt title="input"
2
5 0
8
4 3
8
```

Với:

- `2` là tổng số ___test case___
- `5 0`  là đầu vào cho ___test case___ đầu tiên
- `8`  là kết quả đúng cho test case này.
- `4 3` và `8` thì tương tự ...

!!! note "Note"
    Chủ yếu mình lưu lại phần này để xem mẫu viết chương trình kiểm thử nhiều phương án. Lưu lại nó và sử dụng sau này cho nhiều chương trình khác. ... Nếu có dịp quay lại hãy bổ sung hoặc tái cấu trúc điều này vào mục tốt hơn.