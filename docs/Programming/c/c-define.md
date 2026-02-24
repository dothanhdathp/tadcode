# Define

__Define__ là cách định nghĩa lại 

## println

```cpp
#include "stdio.h"

#define println(ftm, ...) printf(ftm"\n", ##__VA_ARGS__);
```

Tiễn xử lý __*__VA_ARGS__*__

Cách định nghĩa này tự động thêm `\n` vào cuối chuỗi ký tự.
