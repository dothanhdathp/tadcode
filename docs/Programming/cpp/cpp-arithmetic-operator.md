# \[C++\] Toán Tử Toán Học

Các phép toán số học căn bản đề cập đến các phương thức thực hiện các phép toán thông thường __Cộng__, __Trừ__, __Nhân__, __Chia lấy nguyên__ và __Chia lấy dư__

## Với Số

### Cộng, Trừ, Nhân

Các phép toán __Cộng__, __Trừ__ và __Nhân__ về cơ bản là giống như các phép toán thông thường. Các phép toán này thực hiện công việc duy nhất trên các phép toán số học.

```cpp
int a = 1;
int b = 2;
std::cout << b + a << std::cendl; // 3
std::cout << b - a << std::cendl; // 1
std::cout << b * a << std::cendl; // 2
```
### Tràn Số

Trong các phép toán này rất dễ bị tràn số. Ví dự như sau:

```c++
int main()
{
	int i = 2147483647;
	int over_int = i + 10;
	cout << over_int;
	return EXIT_SUCCESS;
}
```
```txt title="Kết Quả"
-2147483639
```

Đây là do tính chất quay vòng của số nên số `int` đã sai kết quả và quay vòng. Trong trường hợp này nên tăng thêm kích thước cho biến chẳng hạn dùng `long int`. Nhưng cái quan trọng cần đúc kết ở đây là nên nắm chắc về khoảng giới hạn của các số để tránh sai sót.

Việc thực hiện các phép toán gây tràn số không hề có thông báo, hãy hết sức cẩn thận.

### Phép Chia

- Riêng phép chia có phân thành hai là __Chia lấy nguyên__ và __Chia lấy dư__
- Phép chia khá quan trọng vì các số trong lập trình sẽ giữ nguyên bản chất nên không có các trường hợp như số thực. Nó không phải là phép toán số học thật sự.

#### Chia lấy nguyên

- Chia lấy nguyên như tên gọi là phép toán chỉ lấy phần nguyên. Ví dụ như phép toán sau:

```cpp
int a = 2;
int b = 5;
std::cout << b/a << std::cendl; // 2
```

- Kết quả được 2 vì phép tính ta được 2 dư một, phần dư không được tính.
- Muốn kết quả lấy được phần thập phân cần phải để dữ liệu ở dạng `float` hoặc `double`. Dù vậy các số vẫn phải chịu giới hạn số ở phần thập phân.

```cpp
int main()
{
	float i = 5;
	float d = 5.0;
	cout << i / 2 << endl;
	cout << d / 2.0 << endl;
	return EXIT_SUCCESS;
}
```
```txt title="Kết Quả"
2
2.5
```

!!! note "Note"
	Thực ra trong phép tính trên không nhất thiết khi dùng `float` phải để là `5.0`, hoàn toàn có thể khai báo như là `float d = 5;`. Mục đích mình làm việc đó chỉ là để tạo thói quen không để chương trình dịch phải ngầm hiểu gây mất kiểm soát.

#### Phép chia lấy dư

- Phép chia lấy dư tức là lấy phần dư. Ví dụ như 5 chia 2 dư 1 thì `1` chính là kết quả.
- Phép <mark>chia lấy dư chỉ có thể thực hiện trên số nguyên</mark>.

```cpp
int main()
{
	int i = 5;
	cout << i % 2 << endl;
	return EXIT_SUCCESS;
}
```
```txt title="Kết Quả"
1
```
