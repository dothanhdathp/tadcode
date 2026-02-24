# Heap & Stack

Ngăn xếp (__stack__) và vùng nhớ (__heap__) là hai vùng nhớ cơ bản được các chương trình sử dụng trong quá trình thực thi. Chúng phục vụ các mục đích khác nhau trong việc lưu trữ dữ liệu trong quá trình thực thi chương trình. __*Đây là kiến thức quan trọng đối với mọi lập trình viên nếu muốn viết chương trình hoạt động tốt và ổn định.*__

## Tổng quan về bộ nhớ

Bỏ qua vấn đề về công nghệ thì trong máy tính có 3 thiết bị có phân vùng lưu trữ dữ liệu chính như sau:

- CPU Cache: Phân vùng này về cơ bản chỉ lưu các giá trị ở phía mã lệnh rồi thực thi, phân vùng này toàn quyền do CPU quản lý để thực hiện các phép toán và đưa ra kết quả. Các bạn có thể thấy phân vùng này chỉ có vài MB và thường được nhà sản xuất đưa kèm với thông số chip. Về cơ bản bạn hiểu nó chỉ giống như hàng đợi lệnh cho CPU thực hiện, có nó nhiều thì chương trình ít khi bị treo hơn và ổn định hơn chứ không trông mong lưu trữ gì ở đây.
- Storage: Ổ cứng, hoặc ổ đĩa. Phân vùng này lưu dữ liệu tĩnh và không bị hỏng sau khi máy tính dừng hoạt động.
- RAM: Nơi lưu trữ "chương trình khi thực thi". Tức là mỗi khi có một __*chương trình nào đó chạy*__, nó sẽ được lưu lên phân vùng này.

!!! info "Đọc Thêm"
    Tại vì khái niệm khá nhập nhằng nên phải giải thích thêm về cái gọi là __*"Bỏ qua vấn đề về công nghệ..."*__. Tức là không nói đến loại RAM, tức là không nói đế công nghệ HDD hay SSD,...
    
    Các thiết bị phần cứng lúc đầu người ta tạo ra không hề có những phân chia đó. Nó chỉ đơn giản cái gì lưu và giữ được thì gọi là __Storage__, vv, .. RAM lúc đó chưa có ra đời và hề hết hoạt động được đặt trên _cache_ của con chip và hiển nhiên thời đó chương trình không hề quá phức tạp.

    Sau này khi có hệ điều hành và các chương trình hoạt động thông qua sự quản lý của hệ điều hành thì các chương trình chỉ cần biết đến 3 đơn vị chính - __*Storage*__, __*RAM*__ và __*CPU Cache*__. Chỉ có một vài chương trình đặc thì sử dụng cache còn lại hầu hết chỉ tác động với hai phân vùng còn lại.

    Storage thì quá đơn thuần. Phần lớn khi chương trình hoạt động, chúng chỉ loanh quanh ở RAM và hầu hết hiệu suất đều do cách người lập trình tổ chức và quản lý ở phân vùng này.

## Tải một chương trình

Một chương trình sẽ cần tải lên từ __Storage__. Chương trình khi được thực thi sẽ được tải từ Storage lên Ram và sau đó máy tính sẽ dùng RAM để thực hiện các hành động của chương trình. Chứng minh rất dễ, hãy viêt một __*chương trình đơn giản*__, thực thi nó trên hệ điều hành rồi xóa xem, nó vẫn hoạt động bình thường.

> __*chương trình đơn giản*__ ở đây là chương trình chỉ sử dụng những hàm cơ bản, không dùng thư viện động hay các tệp vật lý. Nó chết lúc này thì là vấn đề khác. Mục tiêu là nghiên cứu chứ không phải bắt bẻ ==!

## Memory Area

Được rồi chương trình sau khi được tải lên RAM thì nó sẽ như thế nào?

Khi chương trình được tải lên RAM nó sẽ được hệ điều hành cấp cho một vùng nhớ để sử dụng, và chương trình sẽ được phân thành 4 phân vùng như sau:

- __text__: Chứa các chuỗi văn bản nguyên bản, mã lệnh gốc hoặc dữ liệu thuẩn túy (dữ liệu được khai báo dạng const). Các hàm và tiến trình assembly cũng được phân vào vùng này.
- __static variables__: Chứa các biến cục bộ có tầm hoạt động xuyên suốt chương trình, luôn tồn tại. Chúng là dạng các biến static, các biến toàn cục, ...
- __heap__: dữ liệu cấp phát động. Nó là phân vùng dữ liệu được sử dụng để cấp phát cho các biến mà người lập trình muốn khởi tạo sử dụng lâu dài. Bộ nhớ này động và linh hoạt.
- __stack__s: vùng dữ liệu hoạt động của chương trình.

## Heap & Stack

Muốn hiểu rõ hơn hai dạng dữ liệu này cần xem video sẽ rõ hơn:

- Video 1
- Video 2
- Video 3

### Heap

- Lưu trữ bộ nhớ động, các khối bộ nhớ không liền kề.
- Bộ nhớ có thể thay đổi kích thước, không bị giới hạn sử dụng.
- Bộ nhớ này phải được lập trình viên quản lý thông qua toán tử dạng khởi tạo, yêu cầu cấp phát như __*new*__, hoặc các __*con trỏ*__, nó không được tự động cấp phát.
- Lâu hơn stack, vì mỗi lần truy xuất dữ liệu cần tìm kiếm lại vị trí bộ nhớ của biến.

### Stack

- Stack là bộ nhớ động, lưu dữ liệu khi chương trình khởi chạy, các tiến trình, biến cục bộ khi thực thi một chương trình sẽ được lưu vào đây.
- Chính vì cơ chế đó nên các giá trị của biến khởi tạo sẽ tự động được giải phóng sau khi ra khỏi phạm vi của hàm.
    - Muốn rõ hơn hãy xem video.
- Stack cho mỗi thread được cấp phát là khoảng 4MB. Chính vì thế nó có thể hết khi thực thi hàm và có thể dẫn tới lỗi __*"stack overflow"*__ khá là nổi tiếng. Lỗi này xảy ra khi các hàm thực hiện đệ quy nhiều lần không có kết thúc và vượt quá ngưỡng được hệ điều hành cấp. Hoặc các biến nội bộ được tạo nhiều lần, gọi lồng nhau, ...

## Tham Khảo

- [Understanding Stack and Heap Memory](https://towardsdev.com/understanding-stack-and-heap-memory-a96e90f9c982)