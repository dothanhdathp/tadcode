# Basic Synctax

## Target
Hiểu được những điều cơ bản là chìa khóa cho một nền tảng vững chắc. Trong phần này, hãy tìm hiểu các thuật ngữ cơ bản, quy ước đặt tên, từ khóa dành riêng, biểu thức, câu lệnh, cấu trúc dữ liệu, OOP, gói, v.v.

Để in kết quả sử dụng —> System.out.println();
Để lấy dữ liệu đầu vào từ người dùng —> Có thể sử dụng lớp Scanner hoặc BufferedReader

## Hello World

- Trước tiên tạo một tệp tên là `HelloWorld.java`
- Sao chép nội dung như sau vào trong tệp:
    ```java
    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
    ```
- Chạy thử với lệnh `javac HelloWorld.java` để dựng chương trình thành `byte code`.
- Khi thành công sẽ có một tệp là `HelloWorld.class`
- Chạy thử chương trình bằng `java HelloWorld`
- Kết quả sẽ có trên màn hình là:
    ```bash
    Hello World!
    ```

__Giải thích:__
- `public class HelloWorld` là tên của lớp, và tên này sẽ <mark>phải luôn trùng với tên của lớp</mark>.
    - Ví dụ tên lớp là `HelloWorld` thì tên tệp tương ứng cũng phải là `HelloWorld.java`
- `public static void main(String[] args)` là hàm bắt buộc phải có và sẽ luôn chạy đầu tiên.
- `System.out.println` là hàm in kết quả ra màn hình.

## Đọc đầu vào

Có hai cách đọc dữ liệu đầu vào là __Scanner__ và __BufferedReader__.

### Scanner

Để đọc đầu vào có hai cách:
1. Đọc từ _parameter_ đầu vào.
1. Là đọc từ lớp __Scanner__
    ```java
    import java.util.Scanner;

    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter a string: ");
            String stringInput = scanner.nextLine();
            System.out.println("You entered: " + stringInput);
        }
    }
    ```

### BufferedReader

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.println("Enter your input: ");
            String input = reader.readLine();
            System.out.println("You entered: " + input);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## Input Parameter

Với cách này thì đọc đầu vào dữ liệu qua chuỗi __args__ nên cách chạy nó hơi khác một chút, chương trình như sau:

- `Main.java`
    ```java
    public class Main {
        public static void main(String[] args) {
            for (String string : args) {
                System.out.println(string);
            }
        }
    }
    ```
- Chạy như sau:
    - Dùng `java Main A B C D E F`
    - Kết quả:
        ```bash
        A
        B
        C
        D
        E
        F
        ```
    - `for (String string : args)` là hàm gọi sẽ duyệt qua tất cả các phần tử có trong chuỗi `args`

### Cách khác

Một cách khác, nếu muốn dượt qua một lượt các phần tử dựa trên chỉ số như sau:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Number of arguments: " + args.length);
        for (int i = 0; i < args.length; i++) {
            System.out.println("Argument " + i + ": " + args[i]);
        }
    }
}
```