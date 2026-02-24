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
├── lib
│   ├── libftxui-component.a
│   ├── libftxui-dom.a
│   ├── libftxui-screen.a
│   └── libncurses.a
├── out
└── src
    └── main.cpp
```

Trong đó:

- `lib`: Thư mục này chứa các tệp thư viện được dựng ở trên là `libftxui-component.a`, `libftxui-dom.a` và `libftxui-screen.a`. Đó là ba thư viện gốc của __ftxui__. Ngoài ra còn có một thư viện `libncurses.a` để vẽ.
- `src`: Chứa các tệp lập trình chương trình.
- `include/ftxui`: Chứa các tệp ___header___ của thư viện __ftxui__
- `out`: Thư mục này được đưa ra để chứa các tệp kết xuất (tệp `main.exe`)

### Makefile

Tệp `Makefile`

```cmake title="Makefile"
# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra -static -static-libgcc -static-libstdc++ -I./include/

# Linker flags
LDFLAGS = -L./lib/ -lftxui-component -lftxui-dom -lftxui-screen -lncurses

# Source files
SRCS = ./src/main.cpp

# Output executable
TARGET = ./out/main

# Default target
all: $(TARGET)

# Build the target
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRCS) $(LDFLAGS)

# Clean up build files
clean:
	rm -f $(TARGET)

# Phony targets
.PHONY: all clean
```

### Ví dụ đầu tiên

```cpp title="main.cpp"
#include <ftxui/dom/elements.hpp>
#include <ftxui/screen/screen.hpp>
#include <iostream>
 
int main() {
  using namespace ftxui;
 
  // Create a simple document with three text elements.
  Element document = hbox({
    text("left")   | border,
    text("middle") | border | flex,
    text("right")  | border,
  });
 
  // Create a screen with full width and height fitting the document.
  auto screen = Screen::Create(
    Dimension::Full(),       // Width
    Dimension::Fit(document) // Height
  );
 
  // Render the document onto the screen.
  Render(screen, document);
 
  // Print the screen to the console.
  screen.Print();
}
```