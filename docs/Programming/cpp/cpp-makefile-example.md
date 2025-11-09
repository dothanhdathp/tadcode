# \[C++\] Makefile Example

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