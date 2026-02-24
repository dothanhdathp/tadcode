# Constexpr

> https://en.cppreference.com/w/cpp/language/constexpr.html
> Từ __C++11__

## Định Nghĩa và Tác Dụng

__constexpr__ là khai báo cho biết một <mark>biến</mark> hoặc <mark>hàm</mark> sẽ <mark>có cấu trúc tĩnh</mark> và có thể xử lý ở tiến trình biên dịch _(pre-prcessing)_.

Nói đơn giản,khi bạn khai báo hàm, hoặc biến với cờ này thì trình biên dịch sẽ <mark>trực tiếp biên dịch kết quả cuối cùng cho hàm, hoặc biến đó rồi lưu lại</mark> trong quá trình biên dịch thay vì tạo lập các mã lệnh tính toán để chạy trong quá trình thực thi.

Việc này đem lại lợi ích lớn trong các tệp <u>cấu hình</u> khi các giá trị liên đới được tạo ra từ một vài giá trị ban đầu.

!!! quote "Ví dụ thực tế"
    Ví dụ như trong phần mềm quản lý hàng hóa tại một siêu thị chẳng hạn. Giả sử mỗi kệ hàng hóa chứa được dung tích là X. Mỗi tầng cửa hàng chứa được số hàng _R (row)_ và _C (columns)_ là số cột, số tầng là N thì dung tích tối đa hàng hóa chứa được của siêu thị đó $(V)$ là:

    $$
    V = R \times C \times N \times X
    $$

    Trong ví dụ trên, nếu khai báo:

    ```cpp
    constexpr int V = R*C*N*X;
    ```

    Thì trình biên dịch sẽ biên dịch đoạn mã, chạy và lưu lại kết quả cho $V$ luôn. Khi chương trình chạy sẽ không bao giờ phải tính toán lại giá trị này nữa. Với yêu cầu là $R,C,N,X$ đều phải là __*hằng số*__ hoặc là __*hằng số có thể tính*__ như $V$.


Trong thực tế cờ này khuyến khích nhiều ở các tầng dưới khi mà việc cấu hình cho một hệ thống nào đó khá là lớn, các giá trị tính toán phụ thuộc vào nhau. Nếu mỗi lần sửa một thông số phải sửa tay lại cấu hình cho toàn bộ các thông số khác rất là lớn. Chức năng này cực kỳ giá trị.

## Ví dụ

Ví dụ sau là ví dụ cơ bản cho việc sử dụng `const`

