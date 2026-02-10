# \[C++\] Exampler Printer

> Các hàm viết sẵn đẩy kết quả ra ngoài màn hình hỗ trợ cho việc debug/lập trình.


## Overwrite Print & Println

> Trước __C++17__ không hoạt động.
> Yêu cầu ít nhất __C++17__. Sau __C++21__ không còn cần các hàm này nữa vì hàm được tích hợp sẵn rồi.

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

## Vector

### Print 1D Vector

```cpp
template<typename T>
void print_vector(std::vector<T> &vec, const char* mnt)
{
    for(T var : vec) {
        printf(mnt, var);
    }
    printf("\n");
}
```
### Print 2D Vector

```cpp
template<typename T>
void print_2d_vector(std::vector<std::vector<T>> &vec, const char* mnt)
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

## Define DEBUG_PRINT_VALUE

```cpp title="Hàm debug_print_value"
#define debug(...) debug_print_value(__LINE__, #__VA_ARGS__, __VA_ARGS__)
template <typename... Args>
void debug_print_value(size_t line_number, std::string names, Args... args) {
    size_t pos = 0;
    std::cout << "[ line " << line_number << " ] ";
    // Fold expression that handles the name parsing and printing
    ([&](auto& val) {
        size_t next_comma = names.find(',', pos);
        std::string name = names.substr(pos, next_comma - pos);
        std::cout << name << " = " << val << "; ";
        pos = next_comma + 1;
        // Skip space after comma if it exists
        if (pos < names.size() && names[pos] == ' ') pos++;
    }(args), ...);
    std::cout << std::endl;
}
```

Hàm này dùng để nhanh chóng __*debug*__ các giá trị của biến theo mẫu: `<val_0> = <value>, <val_1> = <value>, ...`.