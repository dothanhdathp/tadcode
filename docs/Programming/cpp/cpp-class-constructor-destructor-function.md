# Hàm tạo, hàm hủy

## Hàm Tạo

> Hàm Tạo được sử dụng như là cách để khởi tạo một class theo cách mình mong muốn. Nếu không có hàm tạo, lớp sẽ được khởi tạo như cách tạo __*struct*__ thông thường.

- Trong một lớp, hàm tạo sẽ được gọi đầu tiên để khởi tạo hàm.
- Hảm khởi tạo có thể nhiều hơn một.
- Lớp có thể không có hàm tạo. Khi không có lớp được khởi tạo như một struct đơn thuần.
- Hàm tạo không cần khai báo đối số trả về (bởi đối số đó chính là bản thân lớp)
- Nếu đã khai báo hàm tạo, nên khai báo ở lớp public. Bởi nếu không có, quyền truy cập sẽ tự nhiên cấm người dùng khai báo bởi khác với __*struct*__, __*class*__ tự động đánh dấu mọi phần tử là __*private*__.

## Hàm Tạo

### Một Hàm Tạo

```cpp
class Rectangle {
private:
    int height;
    int weight;
public:
    Rectangle() {};
};
```

### Nhiều Hàm Tạo

```cpp
class Rectangle {
private:
    int height;
    int weight;
public:
    Rectangle() {};
    Rectangle(int h, int w) {
        height = h;
        weight = w;
    };
};
```

### Cú Pháp Rút Gọn

```cpp
class Rectangle {
private:
    int height;
    int weight;
public:
    Rectangle() {};
    Rectangle(int h, int w) : height(h), weight(w) {};
};
```

## explicit

Từ khóa này dùng để chống khai báo ngầm định nhưng mình chưa hiểu lắm, để tạm đây đã.