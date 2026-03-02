# Make

## Luật Chung

### Build g++ cho C++

- `CXX`: chỉ định công cụ dựng, có thể là __gcc__ hoặc __g++__
- `TARGETS`: định danh cho tên cách thành phần xây dựng. Thường có thể là __main__ hoặc các tên khác để tạo các tệp `.o`
- `BFLAGS`: Các cờ xây dựng kiểu như `-std=c++17`,`-std=c++23`, ... chỉ định phương pháp xây dựng.
- `CFLAGS`: Cờ này dùng để khai báo thư mục đầu vào của các tệp thư viện vào __-I./include__. Sau đó các đường dẫn không cần phải để trong dấu __""__ nữa.
- `LDLIBS`: Trong này đưa vào các cờ liên quan đến thư viện __-L./libs -lncurses -lftxui-component -letc__
    - Cái này đặt khai báo __-l(name_lib)__, sẽ có tên tương tự với tệp `.so`. Thêm chúng vào tệp `.so` sẽ tự động được tải.


```text
CXX = g++

TARGETS = main
BFLAGS = -std=c++17 -O2 -Wall
CFLAGS = -I./include
LDLIBS =  -L./libs -lncurses -lftxui-component -lftxui-dom -lftxui-screen

$(TARGETS): %: %.cpp
	$(CXX) $(BFLAGS) $(CFLAGS) $< -o $@ $(LDLIBS) $(LDLIBS)

all: $(TARGETS)
	echo Done!

remake_%:
	rm -rf $*
	$(CXX) $(BFLAGS) $(CFLAGS) $*.cpp -o $* $(LDLIBS)

.PHONY: clean
clean: $(TARGETS)
	@echo "Cleaning all targets..."
	rm -f $(TARGETS)

.PHONY: clean_%
clean_%:
	@echo "Cleaning target: $*"
	rm -f $*
```