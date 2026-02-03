# \[Cpp\] Unordered Map

- Là dạng cấu trúc dữ liệu dạng __*key-value*__ giống như __std::map__ trừ trường _key_ là trường sẽ sử dụng __*hash table*__ để phát triển.
- Vì thuật toán _hash_ cơ bản không hoạt động với các dạng dữ liệu phức tạp, do đó chỉ có các dữ liệu kiểu [fundamental](cpp-fundamental-datatypes.md) mới có thể sử dụng.

## Constructor

```cpp
// default constructor: empty map
std::unordered_map<std::string, std::string> m1;

// list constructor
std::unordered_map<int, std::string> m2 =
{
    {1, "foo"},
    {3, "bar"},
    {2, "baz"}
};
```

### Copy Ceonstructor

```cpp
std::unordered_map<int, std::string> m3 = m2;
```
 
### Move Constructor

```cpp
std::unordered_map<int, std::string> m4 = std::move(m2);
```
 
### Range Constructor

Tái tạo lại bản đồ dựa trên 

```cpp
std::vector<std::pair<std::bitset<8>, int>> v = {{0x12, 1}, {0x01,-1}};
std::unordered_map<std::bitset<8>, double> m5(v.begin(), v.end());
```

## Duyệt Mảng

```cpp
std::unordered_map<int, float> umap;
for(auto ir : umap) {
    println("(first, second) = (", ir.first, ", ", ir.second, ")");
}
```

## Thông số

- `umap.size()`: trả về số lượng phần tử.

## Truy cập phần tử