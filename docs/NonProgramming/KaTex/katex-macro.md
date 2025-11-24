# \[KaTex\] Macro

## Khai Báo Hàm

Tính năng này dùng để tạo một _alias_, hay nói rõ hơn là khi một biểu thức quá dài bạn có thể gói nó thành dạng một hàm tự định nghĩa và tái sử dụng để rút ngắn câu lệnh.

Hãy thử ví dụ với hàm sau:

$$
\sqrt{\cfrac{25}{x}} = \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}}
$$

Về cơ bản phải viết là:

```text
\sqrt{\cfrac{25}{x}} = \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}} + \cfrac{1}{\sqrt{x}}
```

Nhưng ta có thể rút gọn `x^2` lại bằng hàm `\def\foo{\cfrac{1}{\sqrt{x}}}`

```text
\def\foo{\cfrac{1}{\sqrt{x}}}
\sqrt{\cfrac{25}{x}} = \foo + \foo + \foo + \foo + \foo
```

Kết quả hiển nhiên vẫn là tương tự.

## Khai Báo Hàm Với Biến

Đôi khi, có một biểu thức cần xác minh thêm biến đầu vào để viết cho nhanh, hãy xem xét đoạn sau được trích ra từ công thức __Basel__:

$$
\displaystyle\sum_{N \rightarrow \infin}^{N=1} \cfrac{1}{N^2} = \cfrac{1}{1^2} + \cfrac{1}{2^2} + \cfrac{1}{3^2} + \cfrac{1}{4^2} + \cfrac{1}{5^2} + \dots = \cfrac{\pi^2}{6}
$$

Giờ ta sẽ gom biểu thức $\cfrac{1}{N^2}$ trở thành một phần của hàm `foo` bằng `\def\foo#1{\cfrac{1}{#1^2}}`

Giờ thì khai báo rồi sử dụng:

```text
\def\foo#1{\cfrac{1}{#1^2}}
\foo{1} + \foo{2} + \foo{3} + \foo{4} + \foo{5} + \foo{6} +  \dots = \cfrac{\pi^2}{6}
```

Xem hiệu quả này:

$$
\def\foo#1{\cfrac{1}{#1^2}}
\foo{1} + \foo{2} + \foo{3} + \foo{4} + \foo{5} + \foo{6} +  \dots = \cfrac{\pi^2}{6}
$$

Số lượng biến không hề cố định, hoàn toàn có thể nhiều hơn 1 biến:

```text
\def\foo#1#2{#1^2 - #2^2 = (#1 + #2)(#1 - #2)}
\foo{a}{b}
```

$$
\def\foo#1#2{#1^2 - #2^2 = (#1 + #2)(#1 - #2)}
\foo{a}{b}
$$