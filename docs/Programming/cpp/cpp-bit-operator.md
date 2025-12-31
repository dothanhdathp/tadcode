# \[C++\] Bit Operator

## Bit Operator?

Nghĩa là các thuật toán liên quan đến `bit`. Máy tính thực hiện các phép tính này nhanh hơn nhiều so với khi tính toán các phép tính số học.

## Operator

### Logic

!!! warning "Chú ý"
	Các phép tính với bit bằng cách nào đó chỉ thực hiện với các số nguyên kiểu như `int`, `short` ...

#### AND

Phép __AND__ được biểu diễn bằng dấu `&`. __AND__ hai `bit` chỉ trả về `1` khi cả hai đều là `1`.

<div class="center-table" markdown>

|a/b | 0 | 1 |
|:--:|:-:|:-:|
| 0  | 0 | 0 |
| 1  | 0 | 1 |
</div>

#### OR

Phép __OR__ được biểu diễn bằng dấu `|`. __OR__ hai `bit` chỉ trả về `0` khi cả hai đều là `0`.

<div class="center-table" markdown>

|a/b | 0 | 1 |
|:--:|:-:|:-:|
| 0  | 0 | 1 |
| 1  | 1 | 1 |
</div>

#### XOR

Phép __XOR__ được biểu diễn bằng dấu `^`. __XOR__ hai `bit` trả về `0` khi giống nhau, `1` nếu khác nhau.

<div class="center-table" markdown>

|a/b | 0 | 1 |
|:--:|:-:|:-:|
| 0  | 0 | 1 |
| 1  | 1 | 0 |
</div>

#### NOT

__NOT__ là phép đảo bit. Từ `1` thành `0` và ngược lại. Phép đảo sử dụng dấu `~`.

#### Ví dụ

```c++ title="main.cpp"
int main()
{
	int a = 8; // 0x0100
	int b = 9; // 0x0101

	cout << (a&b) << endl; // 0x0100 & 0x0101 = 8
	cout << (a|b) << endl; // 0x0100 | 0x0101 = 9
	cout << (a^b) << endl; // 0x0100 ^ 0x0101 = 1
	cout << (~a) << endl;  // Thy đổi bit dấu (bit đầu tiên) và trở thành số âm
	return EXIT_SUCCESS;
}
```
Kết quả:
```text title="output"
8
9
1
-9
```

### Dịch

#### Dịch trái
#### Dịch phải

## Temp

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

```c++
int result = 5 >> 1; // result will be 2 (0000 0101 >> 1 = 0000 0010)
```