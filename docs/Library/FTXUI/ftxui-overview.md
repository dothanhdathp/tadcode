# FTXUI Overview

## Định nghĩa và khái niệm

_Bỏ qua_

## Các Thành Phần

FTXUI được tổ chức thành ba _modules_, mỗi _modules_ được xây dựng dựa trên _modules_ trước đó:

- [__ftxui/screen__](ftxui-screen.md): Hiển thị cấp thấp,. Dùng để vẽ và tạo kiểu trực tiếp cho các đầu nối.
- [__ftxui/screen__](https://arthursonzogni.github.io/FTXUI/module-screen.html): Hiển thị cấp thấp,. Dùng để vẽ và tạo kiểu trực tiếp cho các đầu nối.
    - `ftxui::Screen`: một lưới 2D gồm các ký tự được tạo kiểu.
    - `ftxui::Pixel`: đơn vị hiển thị.
    - Các thư viện trợ giúp như `ftxui::Color` và `Dimension`.
- [__ftxui/dom__](https://arthursonzogni.github.io/FTXUI/module-dom.html): Bố cục và thành phần. Cung cấp lý tưởng cho giao diện người dùng có cấu trúc và kiểu dáng đẹp mắt.
    - `ftxui::Element`: Một cấu trúc dạng cây dùng để bố trí và thiết kế giao diện người dùng.
    - Các phần tử có thể kết hợp và đáp ứng.
    - __Render()__ để vẽ lên một __Screen__.
- [__ftxui/component__](https://arthursonzogni.github.io/FTXUI/module-component.html): Tương tác người dùng. Thêm vào đó, Hỗ trợ nhập liệu và soạn thảo bằng bàn phím/con trỏ. Sử dụng cho các ứng dụng tương tác.
    - `ftxui::Component`: Các widget tương tác, có trạng thái.
    - Tích hợp sẵn: __Checkbox__, __Input__, __Menu__ và __Button__.

