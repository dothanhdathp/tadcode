# Basic Concept

Một số bài tập đầu tiên làm quen với ngôn ngữ Python

## Hello World

Giới thiệu đầu tiên về một chương trình __Python__.

```python
print("Hello World")
```

Kết quả:

```txt
Hello World
```

## Syntax (cú pháp)

### Chung

1. Python không cần `;` để kết thúc câu
1. Các khối của Python được xác định bằng cách lùi đầu dòng (`TAB`).

### Bình luận

```python
# This is line comment
""" This is
multi lines
comments"""

print("Hello World")
```

- Các dòng bắt đầu với `#` sẽ là các dòng _bình luận_
- Câu bình luận chỉ có tác dụng viết chú thích, hoặc ghi chú, ... và nó không có tác dụng gì với chương trình. Nói đơn giản là khi thực thi, chương trình luôn tự động bỏ qua nó.
- Các câu bình luận chủ yếu để làm sáng tỏ ý của người viết chương trình, hoặc viết lời nhắc nhở, nó có ý nghĩa với lập trình viên hơn với chương trình.
- Để bình luận trên nhiều dòng _(đôi khi bình luận sẽ dài hơn bình thường, có thể là cả một đoạn)_ sẽ cần ký tự `"""` để bắt đầu và kết thúc.

## Biến

Là ngôn ngữ bậc cao, các biến của trong __*Python*__ tự động xác định kiểu. Và __Python__ cực kỳ linh động trong việc này. Về mặt xác định kiểu biến, mình thấy Python mạnh mẽ hơn _javascript_ nhiều.

```python
a = "Version"
b = 1
c = 0.1
d = 'E'

print(a,b,c,d)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
```
```txt
Version 1 0.1 E
Version <class 'str'>
1 <class 'int'>
0.1 <class 'float'>
E <class 'str'>
```

- Ở ví dụ trên có thể thấy kiểu biến được Python tự động quyết định dựa trên cách biến được tạo, hoặc sử dụng.
- `type(var)` là cách để xác định kiểu biến.
- Python không phân biệt `char` và `str` như __C++__

## Số học

### Không giới hạn

Trong số học, python gần như không có giới hạn về số lớn _(các ngôn ngữ như C, C++, Java đều có giới hạn này)_. Bởi vậy đây là ngôn ngữ dễ học hơn nhiều vì không sợ vướng phải lỗi tràn số. Ngoài ra chính điều này nên ngôn ngữ này thường được ưu tiên để phục vụ cho nghiên cứu toán học là vì thế.


```python
a = 2147483000
b = 2147483000

print(a*b)
```
```txt
4611683235289000000
```

!!! warning "Warning"
    Không có giới hạn tràn số tuy tốt cho người sử dụng nhưng không tốt cho máy tính! Bởi vì phải xử lý ở phạm vi lớn không xác định nên python thường không có kết quả trả về tốt nếu được so sánh với các ngôn ngữ cấp thấp.
    
    Gì cũng có hai mặt, đừng thần thánh hoá tính năng này! Nếu nó "lỗi khó xác định", rất khó sửa.

### Phân tách số

Python cũng cho phép viết số như này với các số lớn, tránh cho việc nhầm lẫn số:

```txt
a = 2_147_483_000
b = 2_147_483_000

print(a*b)
```

__*Kết quả vẫn như cũ*__

### Tự động ép kiểu

```txt
a = 1
b = 1.1
c = a+b

print(a, '+', b, '=', c)

print("a = ", type(a))
print("b = ", type(b))
print("c = ", type(c))
```

Trong phép toán trên tự động ép kiểu __a__ thành `1.0` để có thể tính toán với số `float` __b__

### Số lớn e

- Một số số lớn __*(số mũ của 10)*__ sẽ được rút gọn thành `e` để việc biểu diễn dễ dàng hơn.
- `e` hay `E` đều được chấp nhận, cách sử dụng xem dưới đây:

```txt
a = 1e9
b = 1e10
c = 1E30

print("a =", a)
print("b =", b)
print("c =", c)

print("Type of a: ", type(a))
print("Type of b: ", type(b))
print("Type of c: ", type(c))
```

### Số phức

- Lần đầu tiên biết đến việc Python mặc định hỗ trợ cả số phức 😂. Không biết được phát triển từ bao giờ nhưng phiên bản hiện tại mình đang dùng là `Python 3.13.5`
- Trước đó, số phức được xác định qua thư viện `cmath` giờ đã thành mặc định.

Số phức của Python được ví dụ như này:

```python
a = 5 + 3j # basic complex number
b = a*a

print("a =", a, a*a, a.real, a.imag)
print("b =", b, b.real, b.imag)
```
```txt
a = (5+3j) (16+30j) 5.0 3.0
b = (16+30j) 16.0 30.0
```

## Primative Casting (Ép kiểu cơ bản)

- Ép kiểu cơ bản là ép kiểu xoay xung quanh những kiểu thông dụng trong ngôn ngữ __Python__, một số kiểu phức tạp hơn sẽ trình bày ở phần khác.
- Có ba kiểu chuyển đổi phổ biến và thông dụng là: `Interger`, `Float` và `String`.
- <mark>Trừ kiểu ép sang `String` là khá an toàn thì các kiểu còn lại khi chuyển đổi đều không an toàn. Ví dụ như không phải đoạn văn bản nào cũng có thể ép thành _số tự nhiên_, nhưng mọi số tự nhiên đều có thể biểu diễn trên văn bản.</mark>

Một số ví dụ như sau:

### Interger Casting

```python
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
```

### Float Casting

```python
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
```

### String Casting

```python
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
```