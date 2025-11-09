# Hello World!

## Tạo tệp

1. Tạo một thư mục tuỳ ý.
2. Trong đó tạo một tệp tên là Hello.java
1. Trong đó đưa đoạn code này vào.
    ```java
    public class Hello {
      public static void main(String args[]) {
        System.out.println("Hello World");
      }
    }
    ```
4. Chạy command sau:
    ```bash
    javac Hello.java
    java Hello
    ```
5. Kết quả:
    ```text
    Hello World
    ```

📌 Ghim ...
- Tên tệp bắt buộc phải trùng với tên class.
- Hàm `main` sẽ được thực thi ngoài cùng nên bắt buộc phải gọi dạng `static`
- `main(String args[])` Là cú pháp bắt buộc với `args[]` là đầu vào tiêu chuẩn.
- `System.out.println` in ra màn hình.

## Xử lý với biến đầu vào

Đổi tên tệp `Hello.java` bằng `Main.java` và sử dụng đoạn code sau:
```java
public class Main {
  public static void main(String[] args) {
    for (int i = 0; i < args.length; ++i) {
      System.out.println("[" + i + "]" + args[i]);
    }
  }
}
```
- `args` là các biến đầu vào theo sau chương trình ngăn cách bởi dấu _"cách (space)"_
- `args.length` là tính độ dài chuỗi `args`.
- `args[i]` là giá trị của phần tử tại vị trí thứ `i`

Ví dụ kiểm thử chương trình:

```bash
java Main.java string_1 string_2 string_3 string_4 string_5 string_6 string_7 string_8 string_9 string_10
[0]string_1
[1]string_2
[2]string_3
[3]string_4
[4]string_5
[5]string_6
[6]string_7
[7]string_8
[8]string_9
[9]string_10
```