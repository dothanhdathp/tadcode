# \[C\] File

## Mode

| Mode | Mô Tả                      |
| :--: | :------------------------- |
| `w`  | Writes to a file           |
| `a`  | Appends new data to a file |
| `r`  | Reads from a file          |

## Create File

```c
#include <stdio.h>

int main() {
    FILE *fptr;
    // Create a file
    fptr = fopen("example", "w");
    // Close the file
    fclose(fptr);
    return 0;
}
```

## Write To File

```c
#include <stdio.h>

int main() {
    FILE *fptr;

    // Open a file in writing mode
    fptr = fopen("filename.txt", "w");

    // Write some text to the file
    fprintf(fptr, "Some text");

    // Close the file
    fclose(fptr);
}
```

## Read File

```c
#include <stdio.h>

int main() {
    FILE *fptr;

    // Open a file in read mode
    fptr = fopen("filename.txt", "r");

    // Store the content of the file
    char myString[100];

    // Read the content and store it inside myString
    fgets(myString, 100, fptr);

    // Print the file content
    printf("%s", myString);

    // Close the file
    fclose(fptr);
}
```