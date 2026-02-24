# FNV1a
   
## Giới thiệu

> Bài viết tham khảo của [wikipedia]()

__FNV1a__ is __Fowler–Noll–Vo hash function__ _(hay FNV)_ là một hàm băm phi mật mã được _Glenn Fowler_, _Landon Curt Noll_ và _Kiem-Phong Vo_ tạo ra.

Cơ sở của thuật toán băm __FNV__ được lấy từ một ý tưởng được gửi dưới dạng bình luận của người đánh giá tới ủy ban __IEEE POSIX P1003.2__ của __Glenn Fowler__ và __Phong Vo__ vào năm `1991`. Trong vòng bỏ phiếu tiếp theo, __Landon Curt Noll__ đã cải thiện thuật toán của họ. Trong một email gửi __Landon__, họ đặt tên cho nó là băm ___Fowler/Noll/Vo___ hoặc ___FNV___.

## Phát triển

### C/C++

#### Hàm băm cho số 32-bit

=== "C"
    ```c
    #include <stdint.h>

    #define FNV_OFFSET_BASIS_32 2166136261u
    #define FNV_PRIME_32 16777619u

    uint32_t fnv1a_32(const char *data, size_t length) {
        uint32_t hash = FNV_OFFSET_BASIS_32;
        for (size_t i = 0; i < length; ++i) {
            hash ^= (uint32_t)data[i];
            hash *= FNV_PRIME_32;
        }
        return hash;
    }
    ```

=== "C++"
    ```cpp
    inline uint32_t fnv1a_32(std::string const & text) {
        // 32 bit params
        uint32_t constexpr fnv_prime = 16777619U;
        uint32_t constexpr fnv_offset_basis = 2166136261U;
    
        uint32_t hash = fnv_offset_basis;
        
        for(auto c: text) {
            hash ^= c;
            hash *= fnv_prime;
        }

        return hash;
    }
    ```

### Hàm băm cho số 64-bit

=== "C++"
    ```cpp
    inline uint64_t fnv1a_64(std::string const & text) {
        // 64 bit params
        uint64_t constexpr fnv_prime = 1099511628211ULL;
        uint64_t constexpr fnv_offset_basis = 14695981039346656037ULL;
        
        uint64_t hash = fnv_offset_basis;
        
        for(auto c: text) {
            hash ^= c;
            hash *= fnv_prime;
        }

        return hash;
    }
    ```