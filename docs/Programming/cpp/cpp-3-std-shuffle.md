# Shuffle

Hàm này là hàm dùng để xáo trộn các phần tử nằm trong mảng.

## Ví dụ mẫu

```cpp
#include <iostream>     // std::cout
#include <algorithm>    // std::shuffle
#include <array>        // std::array
#include <random>       // std::default_random_engine
#include <chrono>       // std::chrono::system_clock

template <typename T>
void printvec(std::vector<T> &v) {
    std::cout << "{ ";
    for (T i : v) {
        std::cout << i << ", ";
    }
    std::cout << " }" << std::endl;
}

int main () {
    std::vector<int> vec {1,2,3,4,5};
    // obtain a time-based seed:
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    shuffle (vec.begin(), vec.end(), std::default_random_engine(seed));
    printvec(vec);
    return 0;
}
```

- `seed`: Có thể thay bừa bằng một số nào đó. Nhưng đặc điểm thú vị là nếu cùng `seed` thì giá trị sau ___shuffle___ sẽ là như nhau. Việc đưa vào giá trị của thời gian chủ yếu để tạo sự độc nhất, với mọi lần gọi thì kết quả đưa ra luôn khác nhau.

Ngoài ra thì cái này không còn gì thêm nữa. Xin cám ơn!