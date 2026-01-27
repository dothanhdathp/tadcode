# \[C++\] Mẩu Thử

__Mẩu Thử__ chứa các thành phần cơ bản để bắt đầu thử nghiện code C++ một cách nhanh với tiện nhất. Yêu cầu đơn giản chỉ cần một tệp `main.cpp` thuần chứa mã gốc và cài đặt `g++`, `make` để chạy.

## main.cpp

### Không đối số

```cpp
#include <iostream>

int main() {
	return 0;
}
```
### Có đối số

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
#include <unorderedmap>

int main(int argc, const char* args[]) {
	println("argc: ", argc);
	for(auto i = 0; i < argc; ++i) {
		println("args[",i,"] ", args[i]);
	}
	return 0;
}
```

## Makefile

```makefile title="Makefile"
CXX = g++

TARGETS = main
CLFLAG = -std=c++23 -O2 -Wall

$(TARGETS): %: %.cpp
	$(CXX) $(CLFLAG) $< -o $@

all: $(TARGETS)
	echo Done!

r%:
	rm -rf $*
	$(CXX) $(CLFLAG) $*.cpp -o $*

t%:
	rm -rf $*
	$(CXX) $(CLFLAG) $*.cpp -o $*
	./main

.PHONY: clean
clean: $(TARGETS)
	@echo "Cleaning all targets..."
	rm -f $(TARGETS)

.PHONY: clean_%
clean_%:
	@echo "Cleaning target: $*"
	rm -f $*
```

## common

Một số hàm bổ trợ được viết sẵn chỉ cần thêm vào chương trình thôi. Nên hạn chế trên các thư viện có sẵn, không nên sử dụng trong các mẫu thử.

```cpp
#include <iostream>
#include <algorithm>
#include <chrono>
#include <thread>
#include <array>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>

#include <stdio.h>

typedef std::chrono::_V2::system_clock::time_point stime_p;
typedef std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<signed long, std::nano>> htime_p;

#define thread_sleep_s()  std::this_thread::sleep_for(std::chrono::seconds(value));
#define thread_sleep_ms() std::this_thread::sleep_for(std::chrono::milliseconds(value));
#define thread_sleep_ns() std::this_thread::sleep_for(std::chrono::nano(value));

#define htime_now(t) htime_p t = std::chrono::high_resolution_clock::now()
#define time_now(t)  stime_p t = std::chrono::system_clock::now()

template <typename T>
inline double time_duration(htime_p t_start, htime_p t_end) {
    return static_cast<std::chrono::duration<double, T>>(t_end - t_start).count();
}

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}
```
