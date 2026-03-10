# FTXUI Note

> <mark>Đây không phải tài liệu, chỉ là ghi chú</mark>. Có rất nhiều thứ mà mình chưa hiểu rõ hoặc đang tìm hiểu sẽ để ở đây.

## FTXUI Button

### Gán một hàm ngoài cho button

Giải pháp không dùng _**lambda function**_

```cpp
void on_button_click(int &value, int diff) {
    value += diff;
}

int main() {
    int value = 50;
     // clang-format off
    auto btn_dec_01 = Button("-1",  std::bind(on_button_click, std::ref(value),  -1), Style());
    ... etc ...
    return 0;
}
```

- 