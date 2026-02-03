# \[C++\] Exampler Printer

> Các hàm viết sẵn đẩy kết quả ra ngoài màn hình hỗ trợ cho việc debug/lập trình.


## print & println

> Yêu cầu __C++17__. Sau __C++21__ không còn cần các hàm này nữa vì hàm được tích hợp sẵn rồi.

```cpp
template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}
template <typename... Args>
void print(Args... args) {
    (std::cout << ... << args);
}
```

## Vector Print

### Normal Vector

```cpp
template<typename T>
void printf_vector(std::vector<T> &vec, const char* mnt)
{
    for(T var : vec) {
        printf(mnt, var);
    }
    printf("\n");
}
```
### 2D Vector

```cpp
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