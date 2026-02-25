# C++ Unordered Set

## Là

Thùng chứa này sử dụng để tạo một mảng **các phần tử không trùng lặp** và **không có thứ tự**.

## Các Ứng Dụng

### Tạo Mảng Độc Nhất

```cpp
std::unordered_set<int> uset;
for (int i : {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1}) {
    uset.insert(i);
}

for(
    std::unordered_set<int>::iterator ir = uset.begin();
    ir != uset.end();
    ++ir
) {
    std::cout << *ir << " ";
}
```
```text title="Kết Quả"
9 8 6 4 5 3 1 2
```

- Các phần tử ở bất kỳ vị trí nào nó muốn.
- Các phần tử sẽ không lặp lại.

### Chuyển Mảng Thành Vector

```cpp
std::unordered_set<int> uset;
for (int i : {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1}) {
    uset.insert(i);
}
std::vector<int> vec(uset.begin(), uset.end());
for(int i : vec) {
    std::cout << i << " ";
}
```
```text title="Kết Quả"
9 8 6 4 5 3 1 2
```

### Check Exited Value

```cpp
std::unordered_set<int> uset;
for (int i : {2,1,3,2,1,5,4,1,6,5,1,6,5,8,9,3,2,1,1}) {
    if(!uset.insert(i).second) {
        std::cout << "Duplicate value " << i << std::endl;
    };
}
```
```text title="Kết Quả"
Duplicate value 2
Duplicate value 1
Duplicate value 1
Duplicate value 5
Duplicate value 1
Duplicate value 6
Duplicate value 5
Duplicate value 3
Duplicate value 2
Duplicate value 1
Duplicate value 1
```