# Basic Operator

## Math Operator

### Tóm tắt

Các phép số học cơ bản bao gồm:
- `+`: Cộng
- `-`: Trừ
- `*`: Nhân
- `/`: Chia lấy nguyên
- `%`: Chia lấy dư

### Cộng, trừ và nhân

Cộng và trừ sẽ về cơ bản là giống như cũ trừ việc nó có thể  bị vượt ngưỡng. Ví dụ, giới hạn của số `int` là `2147483647` nếu cộng quá thì sao?

```c++
int main()
{
	int i = 2147483647;
	int over_int = i + 10;
	cout << over_int;
	return EXIT_SUCCESS;
}
```
Kết quả:
```bash
-2147483639
```
Đây là do tính chất quay vòng của số nên số `int` đã sai kết quả và quay vòng. Trong trường hợp này nên tăng thêm kích thước cho biến chẳng hạn dùng `long int`. Nhưng cái quan trọng cần đúc kết ở đây là:

!!! warning "Chú ý"
	Khi thực hiện phép tính nên đảm bảo phạm vi giá trị của biến. Bởi khi quá ngưỡng sẽ không có thông báo nào đâu, việc này tự bản thân người lập trình cần phải nắm.

Việc thực hiện phép nhân cũng tương tự nếu vượt quá kích thước sẽ xảy ra hiện tượng ___overflow___ như cũ.

### Phép Chia

Phép chia sẽ gồm 2 phép toán là <u>chia lấy nguyên</u> và <u>chia lấy dư</u>
#### Phép chia lấy nguyên

- Chia lấy nguyên tức là phép chi chỉ lấp phần nguyên. Ví dụ 5/2 được 2.5 nhưng phép chia không lấy phần thập phân mà chỉ lấy phần nguyên là `2`.
- Phép chia lấy nguyên trở thành phép chia bình thường nếu sử dụng số thực, ví dụ như là kiểu `double`.

```cpp
int main()
{
	int i = 5;
	float d = 5.0;
	
	cout << i / 2 << endl;
	cout << d / 2.0 << endl;
	return EXIT_SUCCESS;
}
```
Kết quả:
```bash
2
2.5
```
!!! note "Note"
	Thực ra trong phép tính trên không nhất thiết khi dùng `float` phải để là `5.0`, hoàn toàn có thể khai báo như là `float d = 5;`. Mục đích mình làm việc đó chỉ là để tạo thói quen không để chương trình dịch phải ngầm hiểu gây mất kiểm soát.

#### Phép chia lấy dư

- Phép chia lấy dư tức là lấy phần dư. Ví dụ như 5 chia 2 dư 1 thì `1` chính là kết quả.
- Phép chia lấy dư có thể thực hiện trên số nguyên.

```cpp
int main()
{
	int i = 5;
	cout << i % 2 << endl;
	return EXIT_SUCCESS;
}
```
Kết quả:
```bash
1
```

## Bitwise Operator

Các phép toán _bitwise_ là các phép toán <mark>trực tiếp thao tác các bit của một số</mark>. Các phép toán bitwise hữu ích cho nhiều mục đích khác nhau, chẳng hạn như tối ưu hóa thuật toán, thực hiện một số phép tính nhất định và thao tác bộ nhớ trong các ngôn ngữ lập trình cấp thấp hơn như C và C++.

Sau đây là tóm tắt nhanh về các phép toán bitwise phổ biến trong C++.

### Các phép toán logic với bits

#### AND (&)

Phép toán bitwise AND ( &) là phép toán nhị phân lấy hai số, so sánh từng bit một và trả về một số mới trong đó mỗi bit được đặt (1) nếu các bit tương ứng trong cả hai số đầu vào được đặt (1); nếu không, bit sẽ không được đặt (0).

|  A  |  B  | A & B |
| :-: | :-: | :---: |
|  0  |  0  |   0   |
|  0  |  1  |   0   |
|  1  |  0  |   0   |
|  1  |  1  |   1   |

Ví dụ:

```c++
int result = 5 & 3; // result will be 1 (0000 0101 & 0000 0011 = 0000 0001)
```

#### OR (|)

Phép toán bitwise OR ( |) là phép toán nhị phân lấy hai số, so sánh từng bit một và trả về một số mới trong đó mỗi bit được đặt (1) nếu ít nhất một trong các bit tương ứng trong một trong hai số đầu vào được đặt (1); nếu không, bit sẽ không được đặt (0).

|  A  |  B  | A\|B |
| :-: | :-: | :--: |
|  0  |  0  |  0   |
|  0  |  1  |  1   |
|  1  |  0  |  1   |
|  1  |  1  |  1   |

Ví dụ:

```c++
int result = 5 | 3; // result will be 7 (0000 0101 | 0000 0011 = 0000 0111
```

#### XOR (^)

Phép toán bitwise XOR (OR loại trừ) ( ^) là phép toán nhị phân lấy hai số, so sánh từng bit một và trả về một số mới trong đó mỗi bit được đặt (1) nếu các bit tương ứng trong các số đầu vào khác nhau; nếu không, bit sẽ không được đặt (0).

|  A  |  B  | A\|B |
| :-: | :-: | :--: |
|  0  |  0  |  0   |
|  0  |  1  |  1   |
|  1  |  0  |  1   |
|  1  |  1  |  0   |

Ví dụ:

```cpp
int result = 5 ^ 3; // result will be 6 (0000 0101 ^ 0000 0011 = 0000 0110)
```

#### NOT (~)

Phép toán bitwise NOT (~) là phép toán đơn ngôi lấy một số duy nhất và trả về một số mới trong đó mỗi bit được đảo ngược (1 thành 0 và 0 thành 1).

Ví dụ:

```cpp
int result = ~5; // result will be -6 (1111 1010)
```

### Dịch bit

#### Dịch bit sang trái (<<)

Phép dịch chuyển trái bitwise (`<<`) là phép toán nhị phân lấy hai số, một giá trị và một lượng dịch chuyển, và trả về một số mới bằng cách dịch chuyển các bit của giá trị sang trái theo lượng dịch chuyển đã chỉ định. Các bit bị bỏ trống được điền bằng số không.

Ví dụ:

```cpp
int result = 5 << 1; // result will be 10 (0000 0101 << 1 = 0000 1010
```

#### Dịch bit sang phải (>>)

Phép dịch chuyển bitwise sang phải (`>>`) là phép toán nhị phân lấy hai số, một giá trị và một lượng dịch chuyển, và trả về một số mới bằng cách dịch chuyển các bit của giá trị sang phải theo lượng dịch chuyển đã chỉ định. Các bit bị bỏ trống được điền bằng số không hoặc bit dấu tùy thuộc vào giá trị đầu vào có dấu hay không dấu.

Ví dụ:

```bash
int result = 5 >> 1; // result will be 2 (0000 0101 >> 1 = 0000 0010)
```