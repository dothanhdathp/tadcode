# STD Set

> `std::set` là tập hợp các phần tử **duy nhất** và **có thử tự**.

## Khởi Tạo

```cpp
std::set<int> mset = {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1};
for (std::set<int>::iterator ir = mset.begin(); ir != mset.end(); ++ir) {
    std::cout << *ir << ", ";
}
```
```text
1, 2, 3, 4, 5, 6, 8, 9, 
```

## Ứng Dụng

### Set And Vector

#### std::vector → std::set

```cpp
std::vector<int> mvec = {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1};
std::set<int> mset(mvec.begin(), mvec.end());
for (auto ir : mset) {
    std::cout << ir << ", ";
}
```
```text
1, 2, 3, 4, 5, 6, 8, 9, 
```

#### std::set → std::vector

```cpp
std::set<int> mset = {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1};
std::vector<int> mvec(mset.begin(), mset.end());
for (auto ir : mvec) {
    std::cout << ir << ", ";
}
```
```text
1, 2, 3, 4, 5, 6, 8, 9, 
```

## Đôi Lời

Nói chung chỉ có thế. Thư viện này không có nhiều thứ.