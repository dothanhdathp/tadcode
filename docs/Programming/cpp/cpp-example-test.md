# \[C++\] Example Test

__Example Test__ là kết cấu chương trình mẫu dành cho việc chạy kiểm thử nhanh và tiện hơn.

```cpp title="main.cpp"
#include <iostream>

int main() {
    return 0;
}
```
```text title="Makefile"
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