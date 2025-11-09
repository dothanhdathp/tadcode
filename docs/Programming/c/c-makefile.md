# Makefile

## Nội dung

```text title="main.c"
#include "stdio.h"

int main(int argc, char const *argv[])
{
    printf("Hello World\n");
    return 0;
}
```

```text title="Makefile"
CC = gcc
TARGETS = main
CLFLAG =

$(TARGETS): %: %.c
	$(CC) $(CLFLAG) $< -o $@

all: $(TARGETS)
	echo Done!

remake_%:
	rm -rf $*
	$(CC) $(CLFLAG) $*.c -o $*

.PHONY: clean
clean: $(TARGETS)
	@echo "Cleaning all targets..."
	rm -f $(TARGETS)

.PHONY: clean_%
clean_%:
	@echo "Cleaning target: $*"
	rm -f $*
```