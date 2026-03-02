# FTXUI Example

!!! abstract "Abstract"
    Mục đích của bài này chính là chạy một ví dụ mẫu đầu tiên (Hello World)

## Các tệp cần thiết

Cấu trúc tệp như này:

```txt
.
├── Makefile
├── include
│   └── ftxui
│       ├── component
│       ├── dom
│       ├── screen
│       └── util
├── libs
│   ├── libftxui-component.a
│   ├── libftxui-dom.a
│   ├── libftxui-screen.a
│   └── libncurses.a
├── out
└── src
    └── main.cpp
```

Trong đó:

- `libs`: Thư mục này chứa các tệp thư viện được dựng ở trên là `libftxui-component.a`, `libftxui-dom.a` và `libftxui-screen.a`. Đó là ba thư viện gốc của __ftxui__. Ngoài ra còn có một thư viện `libncurses.a` để vẽ.
- `src`: Chứa các tệp lập trình chương trình.
- `include/ftxui`: Chứa các tệp ___header___ của thư viện __ftxui__
- `out`: Thư mục này được đưa ra để chứa các tệp kết xuất (tệp `main.exe`)

### Makefile

Tệp `Makefile`

```cmake title="Makefile"
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

## Ví dụ đầu tiên

### Code

```cpp title="main.cpp"
#include <ftxui/dom/elements.hpp>
#include <ftxui/screen/screen.hpp>
#include <iostream>
 
int main() {
  using namespace ftxui;
 
  Element document = hbox({
    text("Hello World"),
  });
 
  auto screen = Screen::Create(Dimension::Full(), Dimension::Fit(document));
  Render(screen, document);
  screen.Print();
}
```
```text title="Kết Quả"
Hello World
```

### Các Thành Phần

Trong ví dụ trên có ba thành phần đáng chú ý là:

- __Element__ document là bản đóng gói chung.
- `hbox({ text("Hello World"), })`