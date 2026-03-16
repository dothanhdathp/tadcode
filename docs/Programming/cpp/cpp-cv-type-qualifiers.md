# cv type qualifiers

**cv** là viết tắt của _**(const and volatile)**_. Nó kế thừa hai _keyword_ gốc của C là:

- [const](../c/c-const.md): Biến tĩnh, mô tả tính chất không thể sửa đổi của giá trị.
- [volatile](../c/c-volatile.md) Biến cục bộ, tính chất _**dễ bay hơi**_, nó thường dùng để khai báo giá trị găn với các chân mạch cục bộ (jum) hoặc các biến xử lý ngắt, ... Ý nghĩa của nó đơn giản là đánh dấu một biến mà giá trị của nó không phụ thuộc vào logic của chương trình, cái này giúp cho các compiler sẽ không cố gắng xử lý nó như một biến thông thường mà như là một đối tượng độc lập. Trên thực tế nếu là một đối số không có thay đổi trong nội hàm của chương trình, các trình biên dịch đôi khi loại bỏ nó ra khỏi chương trình hoặc tối ưu nó khiến chương trình lỗi.

## mutable specifier

`mutable` - khai bái biến thành viên này là có thể được sửa đổi trong thành viên đã được khai báo là _**const**_.

Ví dụ nổi tiếng nhất của từ khóa này là **M&M Rule**


### M&M Rule

**M&M Rule** là luật khai báo `mutable std::mutex` với nhau trong lập trình đa luồng.

```cpp
class ThreadsafeCounter
{
    mutable std::mutex m; // The "M&M rule": mutable and mutex go together
    int data = 0;
public:
    int get() const
    {
        std::lock_guard<std::mutex> lk(m);
        return data;
    }
 
    void inc()
    {
        std::lock_guard<std::mutex> lk(m);
        ++data;
    }
};
```

Trong ví dụ này, **mutex** cần được khai báo nhưng nó không được lập trình viên sửa đổi, nó được sử dụng bên trong thư viện và thay đổi biến thành viên mỗi khi khóa luồng. Nhưng vì hàm get là hàm const nên việc sử dụng biến có khả năng thay đổi là bị ngăn cấm bởi trình biên dịch.

Khai báo **mutable** cho phép **std::mutex** được sử dụng bên trong hàm **const** - các hàm không có sự can thiệp sửa đổi từ bên ngoài.