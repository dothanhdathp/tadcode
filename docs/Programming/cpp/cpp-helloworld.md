# HelloWorld

## Nội dung

Chương trình cơ bản đầu tiên của C++ được viết như này.

```cpp title="main.cpp"
#include "stdio.h"

int main() {
    printf("Hello World!");
    return 0;
}
```

## Chạy thử trên Windows

Sau đó có thể dùng MSYS2 để biên dịch:

```bash
g++ -std=c++11 -O2 -Wall main.cpp -o main
```

và chạy tệp __main.exe__ được xuất bản.

```bash
main.exe
```

## Chạy thử trên Linux

Nếu sử  dụng Ubuntu hoặc Linux thì mọi chuyện đơn giản hơn, trực tiếp bằng `g++` trên Linux

```bash
g++ -std=c++11 -O2 -Wall main.cpp -o main
```

Sau đó chạy bẳng lệnh:

```text
./main
```

!!! info "Info"
    Nếu không chạy được lệnh trên có thể bạn chưa cài đặt tệp dưới dạng có thể thực thi. Dùng lệnh sau:

    ```text
    sudo chmod +x ./main
    ```

## Makefile

Trên hệ thống __Linux__ hoặc trên __Msys__, có thể dùng tệp __*Makefile*__ sau:

```text title="Makefile"
CXX = g++

TARGETS = main
CLFLAG = -std=c++11 -O2 -Wall

$(TARGETS): %: %.cpp
	$(CXX) $(CLFLAG) $< -o $@

all: $(TARGETS)
	echo Done!

remake_%:
	rm -rf $*
	$(CXX) $(CLFLAG) $*.cpp -o $*

.PHONY: clean
clean: $(TARGETS)
	@echo "Cleaning all targets..."
	rm -f $(TARGETS)

.PHONY: clean_%
clean_%:
	@echo "Cleaning target: $*"
	rm -f $*
```