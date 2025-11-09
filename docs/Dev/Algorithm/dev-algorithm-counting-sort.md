# Counting Sort

## Mô tả

__Ưu điểm:__
- Là một trong những cách tối ưu nhất về tốc độ khi phải sắp xếp với mảng lớn các phần tử có độ lặp lại cao.
- __Counting Sort__ trả ra kết quả nhanh và có độ ổn định khá là cao.

__Nhược điểm:__
- Tốn nhiều bộ nhớ
- Cần chú ý giới hạn.

## Code mẫu

=== "C++"
    ```cpp
    int main()
    {
        std::vector<int> v = {11,22,34,5,21,6,9,4,3,1,4,5,65,10};
        int count[100] = {0};
        for(auto x : v) {
            count[x] += 1;
        }
        v.clear();
        for(int i=0; i<100; ++i) {
            while (count[i]--)
            {
                v.push_back(i);
            }
        }
        for(auto x : v) {
            std::cout << x << ' ';
        }
        return 0;
    }
    ```