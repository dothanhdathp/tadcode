# std::hash

## Intro

- Hàm băm để băm dữ liệu thành dữ liệu __băm__.
- Dữ liệu sau khi băm không thể hoàn nguyên

## Example

Ví dụ sau về cách sử dụng `std::hash` trong __C++__

```cpp
#include <iostream>
#include <functional>
#include <string>

int main ()
{
  char nts[] = "Test";
  std::string str ("Test");

  std::hash<char*>       ptr_hash;
  std::hash<std::string> str_hash;
  
  std::cout << "nts1:  " << nts << std::endl;
  std::cout << "str:   "  << str << std::endl;
  std::cout << "hash:  " << ptr_hash(nts) << std::endl;
  std::cout << "hash:  " << str_hash(str) << std::endl;
  printf("printf hass:  %zu", str_hash(str));

return 0;
}
```

Kết quả:

```txt
nts1:  Test
str:   Test
hash:  140727073925123
hash:  1631790366531532337
```

## Tóm tắt

- `std::hash` là một kiểu, được khai báo bằng dạng `std::hash<type>`
- Hàm `std::hash` sẽ băm dữ liệu thành một số nguyên không dấu có kích thước là `size_t` _(tương đương với mỗi hệ điều hành)_