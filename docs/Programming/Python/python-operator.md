# [Python] Toán tử

## Toán tử số học

- Có bốn loại toán tử số học đầu tiên mà ai cũng biết là cộng (`+`), trừ (`-`), nhân (`*`) và chia (`/`).
- Ngoài ra bên python còn bổ sung thêm hai toán tử nữa là luỹ thừa (`**`) và __*chia lấy phần nguyên*__ (`//`)

Điểm khác biệt của Python so với các ngôn ngữ khác là phép chia trong đây được tính gần giống phép tính số học ngoài đời. Nếu muốn phép chia lấy nguyên như __C/C++__, bạn cần sử dụng `//`

```python
print(63/2)
print(63//2)
```
```text
31.5
31
```

Bảng tóm tắt

| Toán tử | Mô tả       |
| :------ | :---------- |
| `+`     | Cộng        |
| `-`     | Trừ         |
| `*`     | Nhân        |
| `/`     | Chia        |
| `**`    | Luỹ thừa    |
| `//`    | Chia lấy dư |

## Toán tử Bit

| Toán tử | Mô tả         |
| :------ | :------------ |
| `<<`    | Dịch trái     |
| `>>`    | Dịch phải     |
| `&`     | AND           |
| `|`     | OR            |
| `^`     | XOR           |
| `~`     | NOT (đảo bit) |

```python
A = 3 # 3 = 0011
B = 12 # 3 = 1100

print("A<<1 = ", A<<1) # 0011 << 1 = 0110 = 6
print("A<<1 = ", A<<1) # 0011 << 1 = 0110 = 6
print("A&B  = ",  A&B) # 0011 & 1100 = 0000 (AND)
print("A|B  = ",  A|B) # 0011 | 1100 = 1111 (OR)
print("A^2  = ",  A^2) # 0011 ^ 0010 = 0001 (XOR)
print("~A   = ",  ~A)  # ~0011 = 1..11100 = -4
```
```text
A<<1 =  6
A<<1 =  6
A&B  =  0
A|B  =  15
A^2  =  1
~A   =  -4
```

## Gán động

Các phép đặt ký hiệu toán tử đằng trước dấu bằng và một đối số sẽ trực tiếp thực thi và gán ngược lại cho biến. Đấy đơn giản chỉ là cách viết rút gọn nhằm tối ưu hoá dòng cho việc thực thi. Ví dụ:

```python
a = 1
print(a)
a += 1 # a = a + 1
print(a)
```
```text
1
2
```

- Trước đó `a = 1`
- Sau đó `a += 1` sẽ thực hiện là `a = a + 1`
- Kết quả giá trị của `a` vừa được nâng lên và gán trở lại, khác với `a + 1` sẽ thực thi ở biến tạm nào đó, thường nếu không có yêu cầu sẽ không được gán ngược lại cho `a`

Một số phép toán gán động như sau:

| Toán tử | Mô tả           | Ví dụ                 |
| :------ | :-------------- | :-------------------- |
| `+=`    | `x += 3`        | `x = x + 3`           |
| `-=`    | `x -= 3`        | `x = x - 3`           |
| `*=`    | `x *= 3`        | `x = x * 3`           |
| `/=`    | `x /= 3`        | `x = x / 3`           |
| `%=`    | `x %= 3`        | `x = x % 3`           |
| `//=`   | `x //= 3`       | `x = x // 3`          |
| `**=`   | `x **= 3`       | `x = x ** 3`          |
| `&=`    | `x &= 3`        | `x = x & 3`           |
| `|=`    | `x |= 3`        | `x = x | 3`           |
| `^=`    | `x ^= 3`        | `x = x ^ 3`           |
| `>>=`   | `x >>= 3`       | `x = x >> 3`          |
| `<<=`   | `x <<= 3`       | `x = x << 3`          |
| `:=`    | `print(x := 3)` | `x = 3`<br>`print(x)` |

## Toán tử logic

### Toán tử so sánh

| Toán tử | Mô tả             | Ví dụ  |
| :------ | :---------------- | :----- |
| ==      | Bình đẳng         | x == y |
| !=      | Không bằng nhau   | x != y |
| >       | Lớn hơn           | x > y  |
| <       | Ít hơn            | x < y  |
| >=      | Lớn hơn hoặc bằng | x >= y |
| <=      | Nhỏ hơn hoặc bằng | x <= y |

### Toán tử so sánh logic

| Toán tử | Mô tả                                             | Ví dụ                 |
| :------ | :------------------------------------------------ | :-------------------- |
| and     | Trả về đúng nếu cả hai câu đều đúng               | x < 5 and  x < 10     |
| or      | Trả về đúng nếu một trong các tuyên bố là đúng    | x < 5 or x < 4        |
| not     | Đảo ngược kết quả, trả về sai nếu kết quả là đúng | not(x < 5 and x < 10) |

## Xác định kiểu

Sử dụng `in` hoặc `not in` để xác minh hai đối tượng có phải là toán tử hay không. Ví dụ:

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
```
```text
False
True
False
```