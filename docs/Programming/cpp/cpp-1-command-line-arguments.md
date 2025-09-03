# Command Line Arguments

## Chương trình

Đây là chương trình mẫu:

```c++ title="main.cpp"
#include <cstdlib>
#include <iostream>

using namespace std; 

int main (int argc, char *argv[] )
{
	printf("argc: %d\n", argc);
	for (size_t i = 0; i < argc; i++)
	{
		printf("%2u - %2s\n", i, argv[i]);
	}
	return EXIT_SUCCESS; 
}
```

Output:

```text title="output"
argc: 11
 0 - main
 1 -  1
 2 -  2
 3 -  3
 4 -  4
 5 -  5
 6 -  6
 7 -  7
 8 -  8
 9 -  9
10 - 10
```

- `argc`: là tổng số biến đầu vào.
- `argv`: là mảng các chuỗi ký tự đầu vào.
- Riêng chỉ số đầu tiên là ___0___ là dành riêng cho chuỗi ký tự ___"main"___