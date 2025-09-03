# Basic Bit Operator

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