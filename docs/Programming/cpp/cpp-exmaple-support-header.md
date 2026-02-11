# Support Header

Mình không biết thế nào nhưng cái này để hỗ trợ viết code làm bài leetcode cho tiện.

```cpp title="support.h"
#include "stdio.h"
#include <algorithm>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
#include <bitset>
#include <vector>

#define plog(mnt, ...) printf("%s:%d: "#mnt"\n", __FILE__, __LINE__, ##__VA_ARGS__);

#define time_stamp(f) auto f = std::chrono::high_resolution_clock::now()

#define time_as_milliseconds(time_start, time_end) std::cout << "Milliseconds: " << std::chrono::duration_cast<std::chrono::milliseconds>(time_end - time_start).count() << " (ms)" << std::endl;
#define time_as_microseconds(time_start, time_end) std::cout << "Microseconds: " << std::chrono::duration_cast<std::chrono::microseconds>(time_end - time_start).count() << " (µs)" << std::endl;
#define time_as_seconds(time_start, time_end) std::cout << "Seconds:      " << std::chrono::duration<double>(time_end - time_start).count()                         << " (s)" << std::endl;

template<typename T>
std::vector<T> get_input_vector()
{
    std::vector<T> ans;
    T size_of_array;
    std::cin >> size_of_array;
    while(size_of_array--) {
        T var;
        std::cin >> var;
        ans.push_back(var);
    }
    return ans;
}

template<typename T>
void printf_vector(std::vector<T> &vec, const char* mnt)
{
    for(T var : vec) {
        printf(mnt, var);
    }
    printf("\n");
}

template<typename T>
void printf_2d_vector(std::vector<std::vector<T>> &vec, const char* mnt)
{
    for(auto V : vec) {
        for(T var : V) {
            printf(mnt, var);
        }
        printf("\n");
    }
    printf("\n");
}
```

Còn cái này là dành để đọc đầu vào liên tục mà không cần phải sửa code.

```cpp
int main(int argc, char *argv[]) {
    int idx_i = argc;
    std::vector<int> input;
    while (--idx_i)
    {
        int var = stoi(argv[argc - idx_i]);
        input.push_back(var);
    }
    return 0;
}
```

```bash
./main $(cat input_x)
```

Cách này dựa vào số lượng input, chuyển đổi thành dạng số và lưu vào vector