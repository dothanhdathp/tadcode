# std::rotate

## Mô tả

`std::rotate` dùng để xoay một chuỗi theo chiều ⬅

## Ví dụ

```cpp
// rotate algorithm example
#include <iostream>     // std::cout
#include <algorithm>    // std::rotate
#include <vector>       // std::vector

int main () {
    std::vector<int> vec = {1,2,3,4,5,6,7,8,9};

    std::rotate(vec.begin(),vec.begin()+3,vec.end()); // 4 5 6 7 8 9 1 2 3

    // print out content:
    for (std::vector<int>::iterator it=vec.begin(); it!=vec.end(); ++it)
    std::cout << ' ' << *it;
    std::cout << '\n';

    return 0;
}
```

Kết quả:

```txt
4 5 6 7 8 9 1 2 3
```