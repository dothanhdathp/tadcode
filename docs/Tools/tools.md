#

## Về Các Công Cụ

Trong phần này sẽ là nói về __*các công cụ liên quan đến việc xây dựng, hoặc thực thi, chạy giả lập, ... các chương trình máy tính*__.

Theo sự phát triển lớn mạnh hơn của ngôn ngữ lập trình thì các công cụ để xây dựng cũng được mở rộng không hề ít. Và nó cũng theo đó tạo nên một xã hội phần mềm bổ trợ vô cùng phức tạp và đau đầu luôn. Về cái nhìn tổng quan thì có:

- __Build Tools__: Công cụ xây dựng trực tiếp từ mã nguồn.
- __Meta-Build System__: Công cụ xây dựng gián tiếp bằng các __Build Tools__

## Build Tools

__Build Tools__ chỉ các công cụ có khả năng dịch trực tiếp từ mã nguồn thành các tệp thực thi *(hoặc là bytes code cho máy ảo như Java)*. Dễ phân biệt hơn thì có thể nói đây là những phần mềm sẽ _tương tác trực tiếp_ với mã nguồn để tạo ra một sản phẩm ở đầu ra, là các __complier__ cho các ngôn ngữ lập trình.

Kể các các ngôn ngữ __Interpreted__ _(Ngôn ngữ thông dịch)_, vẫn có các công cụ để dịch _một phần mã nguồn_ thành các mã máy, công cụ đó vẫn gọi là __công cụ biên dịch__.

Các công cụ biên dịch thường được tổng hợp lại thành một _bộ công cụ_ với nhiều chức năng khác nhau để phân tích mã nguồn và các đối số phụ thuộc theo mục đích của người sử dụng. Ví dụ:

- Xây dựng phiên bản __*debug*__ sẽ nặng và chứa các __*symbol*__, nếu không nghiên cứu chuyên sâu thì thường chúng ta sẽ xây dựng phần mềm ở dạng này.
- Để tạo phiên bản __*release*__ sẽ có thêm các cờ để tối ưu và loại bỏ các _ký hiệu phục vụ debug_ trong chương trình. Lúc này phần mềm xuất xưởng sẽ có dung lượng nhẹ hơn nhiều.

__Các bộ công cụ xây dựng ví dụ là:__

- Bộ công cụ của [GNU](tools-gnu.md)
- Bộ công cụ của [LLVM](tools-llvm.md)
- Bộ công cụ của [Clang](tools-clang.md)

## Build System và Meta-Build System

### Build System

Nói về hệ thống __Build System__, nó chính là một lớp phủ lên của lớp xây dựng. Tác dụng của nó là giúp lập trình viên tạo ra các _kịch bản xây dựng_ khác nhau trên cùng một mã nguồn và lợi ích tuỳ chỉnh thông số cho các _kịch bản khác nhau_, tạo ra nhiều phiên bản khác nhau của phần mềm dựa trên những đối số đó.

- Ví dụ như _bộ quy tắc_ cho hai phiên bản `debug` và `release` của phần mềm. Hoặc bộ quy tắc riêng cho các khu vực khác nhau như __*Asia*__, __*Arabic*__, __*China*__, ... bởi mỗi khu vực khác nhau cần đưa vào các cờ riêng để cấu hình lại các thư viện phụ thuộc cũng như áp dụng những phân vùng khác nhau trong mã nguồn.

Nhờ việc tuỳ chỉnh đó người phát triển còn có thể tuỳ ý __*xây dựng toàn bộ*__ hoặc __*xây dựng một phần*__ trên những mã nguồn lớn. Ví dụ như xây dựng một chương trình lớn cần xây dựng trước 10 thư viện nhỏ. Nếu cần dựng lại chương trình với một thay đổi nhỏ trong thư viện thứ 5 thì chỉ cần dựng lại thư viện số 5 và dựng lại chương trình tổng thôi. Việc này tiết kiệm được rất nhiều thời gian.

Hơn nữa các công cụ hỗ trợ xây dựng như này luôn có các tệp cấu hình trực quan, người phát triển sẽ đỡ vất vả hơn nhiều khi phải nhớ và lưu lại các câu lệnh xây dựng dài ngoằng, hoặc nhớ rõ các thứ tự xây dựng chương trình.

### Meta-Build System

__Meta-Build System__ về cơ bản nó cũng khá giống như hệ thống xây dựng truyền thống, có điều nó có phạm vi hoạt động rộng hơn, hỗ trợ việc xây dựng nhiều chương trình một lúc theo một kịch bản / cấu hình cài đặt. Chính vì thế nó mới có tên gọi là __Hệ Thống Xây Dựng Siêu Dữ Liệu__

Với công cụ __Build System__ xây dựng các chương trình có cấu trúc khá lớn, thì __Meta-Build System__ sẽ đảm nhận một số việc như:

Các hệ thống siêu xây dựng có thêm một số tính năng để có thể trực tiếp can thiệp vào hệ thống nhằm hỗ trợ đầy đủ cho các hệ thống dựng thông thường. Ví dụ như nó sẽ đọc các thông tin hệ điều hành rồi tuỳ chỉnh riêng và xây dựng lại các tệp cấu hình cho các hệ thống xây dựng mã nguồn. Ví dụ như xây dựng riêng cho hệ điều hành macOS, Windows, Linux. Thậm chí tải về các tệp phụ thuộc nếu cần, chuẩn bị tất cả mọi thứ rồi cuối cùng tạo ra tệp kịch bản xây dựng dành riêng cho thiết bị xây dựng. Hoặc là cho cả một hệ sinh thái khổng lồ bao gồm nhiều phần mềm khác nhau cần __đảm bảo được sự liên kết và chúng đang dùng chung__ một bộ các thư viện động.

Một số hệ thống xây dựng siêu dữ liêu như là:

1. [CMake](cmake.md)
1. Bazel

Sức mạnh tuyệt vời của các hệ thống xây dựng đó là ở AOSP trên Android. Nơi bạn sẽ tạo ra một bản __*image*__ cực kỳ nhỏ trên một khối mã nguồn đồ sộ hàng trăm __GB__. Các tệp xây dựng động tự động lồng ghép, chuyển đổi, xác minh thứ tự riêng trên một hệ thống chung. Ukm, ... nói đơn giản là rất mạnh.