# Tổ Hợp, Chỉnh Hợp, Giai Thừa

- __Permutation__: _Tổ Hợp_
- __Compination__: _Chỉnh Hợp_
- __Factorial__: _Giai Thừa_

## Compination _(Chỉnh Hợp)_

### Công Thức Chỉnh Hợp

Sử dụng ba công thức sau để giải bài toán chỉnh hợp.

- $C^{1}_N = N$
- $C^{0}_N = C^{N}_N = 1$
- $C^{k}_N = C^{k}_{N-1} + C^{k-1}_{N-1}$

Trường hợp đệ quy đơn giản có mẫu thế này:

```cpp
// simple compination
size_t compination(size_t k, size_t N) {
    if(k==1)
        return N;
    if(k==0 || k==N)
        return 1;

    return compination(k, N-1) + compination(k-1, N-1);
}
```

## Factorial _(Giai Thừa)_

__Giai thừa__ đơn giản chỉ là bộ nhân của các số.

$N! = 1 \cdot 2 \cdot ... \cdot N$

Sử dụng đệ quy:

```cpp
// simple factorial
size_t factorial(size_t N) {
    if(N<2) return 1;
    return N * factorial(N-1);
}
```

## Permutation _(Tổ Hợp)_

__Tổ hợp__ hơi phức tạp một chút. Theo công thức:

$P^{k}_N = k! \cdot C^{k}_N$

Vậy nên nếu muốn đơn giản thì:

```cpp
// simple factorial
size_t permutation(size_t k, size_t N) {
    return factorial(k) * compination(k, N);
}
```

## Thư Viện

Cả ba cách trên đều khá là tốn dữ liệu trên stack và dễ _overfllow_. Bên cạnh đó thiếu 2 thứ quan trọng:

!!! danger "Kiểm Giới Hạn"
    Mặc dù size_t khá là lớn nhưng hàm số của tổ hợp vẫn tăng theo cấp số nhân đáng kể mỗi lần biến số thay đổi. Đến khoảng N với giá trị 68, chương trình sẽ bị quá tải. Nếu không có kiểm tra nó sẽ quá tải và vượt khỏi giá trị ban đầu.

!!! danger "Chậm"
    Nếu với bộ số nhỏ (dưới 10) thì có thể vì sai khác không quá lớn. Trên 10 sẽ cần cân nhắc đến tốc độ chương trình, đổi hướng sang lập trình động đem lại kết quả tốt hơn nhiều về tốc độ.

    Đánh đổi, cần mảng khá lớn để lưu trữ các số.

!!! danger "Stack Overflow"
    Lỗi kinh điển khi sử dụng đệ quy.

### Ví Dụ Phát Triển

- Dựa vào mẫu dưới này, phát triển thêm các tính năng khác cho thư viện tự làm. Bộ thư viện này có thêm khả năng hỗ trợ mở rộng cho số __*interger 128 bits*__. Với số lớn vậy có thể tính đến các số chỉnh hợp dưới 100 trước khi tràn bộ nhớ.
- Tốc độ gẫn đặt đến $log(N)$ khi N tăng đần, đã thử nghiệm với tính toán vòng for và kết quả trả về luôn dưới 1s _(cỡ vài ms thôi)_. Trong khi nếu đệ quy, tốc độ chương trình nhanh chóng bị quá tải ở mức độ tổ hợp cấp 100.
- Đồng thời nó cũng linh động với các loại biến đầu vào luôn.

```cpp title="Compination.hpp"
#include <iostream>
#include <algorithm>
#include <string>
#include <unordered_map>

// global function
std::string uint128_to_string(unsigned __int128 value) {
    // 0 case
    if (value == 0)
        return "0";
    
    // Another
    std::string ans = "";
    while (value > 0) {
        // Convert last number in value to character and put it string return
        ans += (char)('0' + (value % 10));
        value /= 10; // value reduce 10
    }

    // reverse string
    std::reverse(ans.begin(), ans.end());
    return ans;
}

template <typename T>
class Compination {
private:
    const size_t maxN;
    const unsigned __int128 __max_128b = (static_cast<unsigned __int128>(0xFFFFFFFFFFFFFFFFULL) << 64) | 0xFFFFFFFFFFFFFFFFULL;
    const T __max_val = static_cast<T>(__max_128b);
    std::unordered_map<size_t, std::vector<T>> CompinationMap;

    // Check Overflow
    T CheckAddUnsignedOverflow(T __argl, T __argr);
    // Recursion Style
    T RecursionCompination(size_t k, size_t N);
    // Dynamic Recursion Style
    T DynamicCompination(size_t k, size_t N);
public:
    Compination(size_t n) : maxN(n) {};
    virtual ~Compination() {
        CompinationMap.clear();
    };

    size_t getMaxN() { return maxN; };
    T RecursionCompination(size_t k); // --> RecursionCompination(k, maxN)
    T DynamicCompination(size_t k);   // --> DynamicCompination(k, maxN)
};

// Check overflow
template <typename T>
T Compination<T>::CheckAddUnsignedOverflow(T __argl, T __argr) {
    if(sizeof(T) > 16)
        throw std::runtime_error("Type of size overflow");

    T __remain = __max_val - __argl;
    if(__remain < __argr) {
        throw std::runtime_error("Numberic limit");
    }
    return __argl + __argr;
}

template <typename T>
T Compination<T>::RecursionCompination(size_t k) {
    return RecursionCompination(k, maxN);
}

template <typename T>
T Compination<T>::RecursionCompination(size_t k, size_t N) {
    if(k==1)
        return static_cast<T>(N);
    if(k==0 || k==N)
        return static_cast<T>(1);

    return CheckAddUnsignedOverflow(RecursionCompination(k, N-1), RecursionCompination(k-1, N-1));
}

template <typename T>
T Compination<T>::DynamicCompination(size_t k) {
    return DynamicCompination(k, maxN);
}

template <typename T>
T Compination<T>::DynamicCompination(size_t k, size_t N) {
    if(k==1)
        return static_cast<T>(N);
    if(k==0 || k==N)
        return static_cast<T>(1);
        
    if(CompinationMap[N-1].empty()) {
        CompinationMap[N-1] = std::vector<T>(N, T(0));
    }
    if(!CompinationMap[N-1][k]) {
        CompinationMap[N-1][k] = DynamicCompination(k, N-1);
    }
    if(!CompinationMap[N-1][k-1]) {
        CompinationMap[N-1][k-1] = DynamicCompination(k-1, N-1);
    }
        
    return CheckAddUnsignedOverflow(CompinationMap[N-1][k], CompinationMap[N-1][k-1]);
}
```
```cpp title="main.cpp"
#include <iostream>
#include "Common.hpp"
#include "Compination.hpp"

int main(int argc, const char* args[])
{
    size_t k = 13; // Set max value of N in C(k,N)
    size_t N = 25; // Set max value of N in C(k,N)
    Compination<size_t>      short_comp = Compination<size_t>(N);
    Compination<__uint128_t> max_comp   = Compination<__uint128_t>(N);

    println("Result C(",k,",",N,") :", short_comp.RecursionCompination(k));
    println("Result C(",k,",",N,") :", short_comp.DynamicCompination(k));
    println("Result C(",k,",",N,") :", uint128_to_string(max_comp.RecursionCompination(k)));
    println("Result C(",k,",",N,") :", uint128_to_string(max_comp.DynamicCompination(k)));

    return 0;
}
```

- __RecursionCompination__: Tính bằng cách đệ quy cổ điển.
- __DynamicCompination__: Tính bằng cách quy hoạch động.