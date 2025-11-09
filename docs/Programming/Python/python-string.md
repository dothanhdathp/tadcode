# String

`string (str)` là phạm trù thuộc về một kiểu __chuỗi ký tự__, các thao tác cơ bản xoay quanh nó rất nhiều.

## Kích thước

```python
a = "This is example string"
print(len(a))
```
```txt
22
```

## Chuyển đổi

Mọi kiểu biến cơ bản đều có thể chuyển về `str` 👉 dẫn đến về mặt lý thuyết tất cả mọi kiểu đều có thể được chuyển thành `str` 👉 bạn có thể tạo chuỗi với bất kỳ kiểu dữ liệu nào.

```python
title = "Value of"
a = 10
b = 1.1
c = [1,2,3,4]
d = [1,'Q',3.14]
s = "Hello World"

print(title, "a = ", a)
print(title, "b = ", b)
print(title, "c = ", c)
print(title, "d = ", d)
print(title, "s = ", s)
```
```bash
Value of a =  10
Value of b =  1.1
Value of c =  [1, 2, 3, 4]
Value of d =  [1, 'Q', 3.14]
Value of s =  Hello World
```

## Nối chuỗi

- Để nối hai chuỗi với nhau dùng phép `+`. _(Các phép khác đương nhiên rồi, không có)_

```python
a = "This is first string"
b = "This is seconds string"

print(a, b)
```
```bash
This is first stringThis is seconds string
```

- Nếu đối tượng khác loại, chỉ cần dùng __*casting*__.

```python
a = "Value = "
b = 10

c = a + str(b)

print(c)
```
```bash
Value = 10
```

## Ký tự đặc biệt

__*Ký tự đặc biệt*__ trong chuỗi là các ký tự sẽ không được hiển thị theo cách mình nhìn thấy nó. Lý do cho việc này là vì nó lẫn lộn với các ký tự chức năng của lập trình nên người ta đã sáng tạo ra một vài cách khác nhau để khai báo chúng. Ví dụ dễ hiểu nhất là `"` được sử dụng để bắt đầu chuỗi, vậy làm sao để đưa `"` vào trong một chuỗi? Đó là:

| 1    | 2            | 3            |
| :--- | :----------- | :----------- |
| `\\` | Backslash    | In ký tự `\` |
| `\'` | Single Quote | In ký tự `'` |
| `\"` | Double Quote | In ký tự `"` |

Ngoài ra còn một số ký tự ẩn như sau:

| 1    | 2               | 3                                                                           |
| :--- | :-------------- | :-------------------------------------------------------------------------- |
| `\n` |                 | Xuống dòng                                                                  |
| `\t` |                 | Tab (cách một khoảng)                                                       |
| `\0` |                 | __*Null Character*__, thường được dùng để đánh dấu điểm kết thúc một chuỗi. |
| `\r` | Carriage Return | Chuyển con trỏ về đầu dòng bên phải                                         |
| `\v` | Vertical Tab    |                                                                             |

!!! quote "Ký tự `\0`"
    `\0` là ký tự đặc biệt được sử dụng để kết thúc chuỗi. Nó luôn tồn tại ở cuối chuỗi để xác định cho vị ký kết thúc và là quy ước cho hệ thống máy tính rồi (đến hiện tại là vậy). Ý nghĩa của nó tương tự dấu chấm câu.

## Một vài cách viết khác

- `\u{code}` → Truy cập vào UTF-8
- `\x{code}` → Truy cập vào UTF-16

Ví dụ:

```python
print("\x28\u25d5\u203f\u25d5\x29")
```
```text
(◕‿◕)
```

## Extract String

- Trích xuất ký tự bằng `[index]`
- Trích xuất đoạn bằng `[first:last]`
    - `first`: Vị trí đầu tiên
    - `last`: Vị trí đầu kết thúc
    - Nếu `first` == `last` thì không có gì xảy ra
    - Các giá trị âm cũng thoả mãn. Ví dụ như `-1` sẽ là quay ngược lại vị trí cuối cùng.

```python
a = "ABCDEF"

print(a[0], a[1], a[2], a[3], a[4], a[5])
print(a[0:1])
print(a[0:-1])
print(a[1:1]) # Nothing print out
```
```txt
A B C D E F
A
ABCDE
```

## Split String

Trích xuất chuỗi dùng `split()`. Sau hàm `split()` sẽ trả về một mảng các phần tử được phân tách bởi ký tự dùng để cắt.

Ví dụ phân tách một chuỗi ký tự bằng dấu cách ` `

```python
a = "This is example string"

for i in a.split(' '):
    print(i)
```
```txt
This
is
example
string
```

## Loại bỏ ký tự

- `lstrip([char])`: Loại bỏ ký tự lặp ở đầu
- `rstrip([char])`: Loại bỏ ký tự lặp ở cuối
- `strip([char])`: Loại bỏ ký tự lặp ở hai đầu

```python
a = "aaa-bbb-aaaaa"

print(a.lstrip('a'))
print(a.rstrip('a'))
print(a.strip('a'))
```
```txt
-bbb-aaaaa
aaa-bbb-
-bbb-
```

## Hàm xử lý khác

### isnumeric

- Kiểm tra có phải phải là chuỗi số hay không _(chắc để cho việc cast `str` thành `int`)_

```python
a = "10"
b = "AA"

print(a.isnumeric())
print(b.isnumeric())
```
```text
True
False
```

### lower & upper

- `lower()`: Chuyển _(tất cả các chữ)_ thành chữ thường
- `upper()`: Chuyển _(tất cả các chữ)_ thành chữ HOA

```text
a = "adAhdAFdDsADSd"

print(a.lower())
print(a.upper())
```
```text
adahdafddsadsd
ADAHDAFDDSADSD
```