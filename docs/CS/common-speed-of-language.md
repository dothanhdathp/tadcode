# \[Common\] Tốc Độ Trong Ngôn Ngữ Lập Trình

## Thế giới xoay quanh C,C++ và Java

Có ba ngôn ngữ lập trình gần như điều hành mọi mặt của thế giới công nghệ là C/C++ và Java. Có lẽ nhiều người vẫn còn cho rằng đâu đó phải kể đến các ngôn ngữ như Ruby, PHP, Javascript, ... và nổi tiếng nhất phải kể đến là Python mới là chân lý thì ... không, mọi người đã lầm.

Hầu hết các ngôn ngữ đều dựa trên một thứ ngôn ngữ cơ bản nhất được gọi là __mã máy__.

Và thứ ngôn ngữ hỗ trợ cho __mã máy__ tốt nhất đều là __assembly__ đến __C__. Ở khu vực ngôn ngữ lập trình được nở rộ nhất đều là từ __C__ trở lên. Và thế là các ngôn ngữ khác đều cố gắng kế thừa thư viện, chức năng, ... từ ngôn ngữ này.

!!! quote "Quote"
    Chắc chắn rồi, không ai muốn phát minh lại bánh xe cả.

Và từ đó có ba ngôn ngữ lớn nhất thay đổi cuộc chơi là __C__, __C++__ và __Java__, tại sao à?

### C

C là ngôn ngữ cổ điển nhất. Nó đơn giản với những kiến trúc, khái niệm rất cơ bản và cân đối. Vừa khá dễ hiểu, lại đủ tính năng và hiệu quả. Thông thường người ta sẽ dùng ngôn ngữ này để viết các chương trình tương tác trực tiếp với máy tính và thanh ghi. Đã từng có nhiều ngôn ngữ khác cố gắng thay thế vị trí đó nhưng nó vẫn không thể thực sự hiệu quả hơn và __C__ vẫn tồn tại.

### C++

Ở lớp này, mặc dù có rất nhiều đối thủ cạnh tranh nhưng __C++__ vẫn là ngôn ngữ phổ biến vì __C__ tồn tại. __C++__ có một chức năng thú vị nhất ở giữa mà nhiều ngôn ngữ không có đó là thiết lập những bối cảnh đồng nhất với __C__ mà vẫn có nhiều giao thức hiện đại, thay đổi kết cấu kiến trúc đa dạng, linh hoạt.

### Java

Java đưa đến một cách tiếp cận khác và lâu đời. Nó chạy chương  trình thông qua máy ảo và nhờ đó hoạt động ổn định và tương đồng trên tất cả các thiết bị miễn là ... nó có thể chứa máy ảo. Tốn tài nguyên hơn, nhưng lại dễ tương thích và có khả năng __*tái sử dụng mã nguồn*__ hiệu quả hơn. Đặc biệt việc nâng cấp và sửa lỗi là tương đối đơn giản. Hầu hết công việc nặng nhọc nhất đều được gửi cho các bên tạo ra máy ảo Java. Nó mạnh, nó ổn định và hiệu quả đã thu hút một số lượng lớn những nhà đầu tư và phát triển khiến ngôn ngữ này mở rộng. Rất nhiều các ngôn ngữ sau này để kế thừa lại tiêu chí và phương thức của Java để tìm chỗ đứng.

## Tại sao Python và một số ngôn ngữ khác lại không được tính

Chỉ đơn giản phần lõi các ngôn ngữ khác hầu hết đều xoay quanh __C__ và mã máy. Chúng không độc lập và không có nhiều khái niệm mới mẻ và chỉ đi trong một cung đường rất nhỏ, nơi mà nó nổi tiếng ở một ngành con trong thế giới công nghệ. Còn lại thì ... tin tôi đi, nếu bạn có khả năng học đầy đủ về một lĩnh vực nào đó, tìm về nguồn gốc đều thấy dấu vết của những ngôn ngữ đã hình thành thế giới này.

## Tốc độ lạ kỳ

Thông thường, chúng ta có hai dạng phổ biến để nói về ngôn ngữ lập trình, chính là kết quả của chúng. __Biên Dịch__ và __Thông Dịch__

- __Biên Dịch__ tạo ra __mã máy__ chạy trực tiếp
- __Thông dịch__ tạo ra mã chạy trên máy ảo, hoặc phải thông qua một "phép thuật" nào đấy để thành __mã máy__

Chính thế nên nó cũng có hai chức năng thú vị

- Chương trình sau khi thông dịch chạy nhanh hơn, nhưng phải chạy toàn bộ và không thể phục hồi.
- Các chương trình thông dịch khởi động nhanh hơn, nhưng hiệu suất kém và có thể chạy được một phần.

Thế nên nhìn chung thì

- Càng gần mã máy thì ngôn ngữ càng nhanh.
- Càng được chạy trực tiếp thì chương trình viết bởi ngôn ngữ đó chạy càng nhanh.

!!! warning "Warning"
    Chà, điều đó thật sự chỉ đúng ở "bề nổi". Nơi mà nếu bạn bị ép phải chọn một trong hai thì đó là đúng. Nhưng thật sự, hoàn toàn mập mờ.

## C++ tiệm cận C

Điều đầu tiên mình từng nghĩ __C__ là ngôn ngữ nhanh hơn __C++__, bởi vì:

- __C__ gần mã máy
- __C__ có cú pháp đơn giản
- __C__ quản lý thanh ghi, bộ nhớ rõ ràng
- __C++__ có quá nhiều chức năng và hàm phức hợp. Việc gọi một hàm có sẵn của __C++__ luôn đi qua nhiều tầng hơn và kết thúc ở kết quả thường sẽ chậm hơn __C__

<mark class=red>Thực tế tôi đã nhầm</mark>

Về hiệu năng, nếu chương trình đủ đơn giản thì C có thể thắng. Thậm chí còn không hoàn toàn. Điều đó hoàn toàn phụ thuộc vào quá trình dựng của __Bộ Biên Dịch__. Nói thế có phần chung chung nhỉ?

So sánh đơn giản đi, nếu bạn viết cùng một thuật toán qua __C__ và __C++__ có một độ phức tạp vừa đủ thì:
- Người lập trình C phải tự tạo các khái niệm mới. Và điều này thường sẽ mất thời gian và hiệu quả tương đối.
- Người lập trình C++ thì có sẵn công cụ và sử dụng. Nhưng khác biệt ở chỗ __thư viện C++ có sẵn mã máy__ đã thực thi nó. Thế nên nó nhanh hơn. 

### Tại sao?

> Thế nếu C cũng làm vậy thì sao?

Hoá ra là không thể. Bạn biết đấy ngôn ngữ C++ đã mở rộng, và thế là có rất nhiều những khái niệm mới đã được "ảo hoá" và thế là để tối ưu người ta đã xây dựng trực tiếp khái niệm từ mã máy. C lại không thể, vì nó không đủ. Bạn biết đấy, nếu ngôn ngữ bạn sử dụng không có thì bạn nên dùng "từ mượn", hoặc không thì phải dùng những đoạn mô tả rất dài để mô tả chúng. Kể cả vậy thì nó vẫn gây khó hiểu.

Chính vì <mark>__C__ không phải ngôn ngữ cho ứng dụng người dùng</mark>, thế nên họ cứ để nguyên như vậy là đủ. Các khái niệm mở rộng sẽ được trình bày lên __C++__ và làm chúng trở nên đẹp đẽ hơn. Mà cũng bởi vậy nên __C++__ thực sự là một ngôn ngữ khó học.

## C++ < Java

Cái này cũng thật sự đau đầu. Hầu hết các trường hợp, __Java__ chịu thua. Nhưng cũng rất nhiều trường hợp, __C++__ chịu thua. Ê kỳ nha!

- Nè, theo lý thuyết, Java cần chạy qua máy ảo, làm sao có thể vượt mặt C++ được khi luôn phải thực thi hai tầng?

Nhưng không. Vì C++ là ngôn ngữ Biên Dịch, thế nên nó làm việc trực tiếp ra mã máy. Hay chính xác hơn kiểu như nó tạo ra một bản _prototype_ và chạy khi có đầu vào thực tế -> đầu ra. Nhưng Java thì lại có sự linh hoạt, __*prototype có thể linh hoạt để thích ứng*__. Hay nói cụ thể hơn:

- Trong một số trường hợp như __Sort__, __Search__, __Find__, ... Máy ảo Java khi cần tải lên một đoạn mã máy thực thi cho một tác vụ thì nó có thể trực tiếp xem xét phần nhỏ đó và "tối ưu" lại ngay trong quá trình thực thi. Thế nên các tác vụ đôi khi qua __C++__ cần lặp nhiều lần thì __Java__ lại chả cần.

Hiểu ví dụ này đi. Với bài toán kiểu như:

Đầu vào là một chuỗi các cá thể sinh vật. Và nhiệm vụ của người kiểm soát là:

- Xác định Sinh Vật mới nhận. Đồ Vật bị bỏ qua.
- Lấy Độ Tuổi và Giới Tính.
- Nếu Người thì lưu về Nghề Nghiệp.
- Nếu Động Vật thì lưu về Giống Loài.

Thường thì C++ sẽ thực hiện đầy đủ các bước. Nhưng ở Java, nó có thể biết trước chuỗi đầu vào luôn là Người, hoặc luôn là Vật _(Vì thường khi khai báo có dạng chuỗi luôn là đồng dạng)_. Thế là nó bỏ qua luôn một số bước kiểm tra không cần thiết -> kết quả nhanh hơn.

Cũng đồng thời, vì được biên dịch sang mã máy là một "dạng ngôn ngữ khác" nên có hai điểm:

- Ở một số mặt, ngữ cành __Java__ phục vụ mục đích tốt hơn __C++__
- Chính vì Java cắt nhỏ chương trình, nên nó có thể __tối ưu nhỏ từng phần__ tuỳ theo mà mà nó nhận được để thực thi. Cái này __C++__ chịu chết.

!!! quote "Ghi nhớ"
    Việc cho rằng ngôn ngữ lập trình $A$ luôn luôn hiệu quả hơn $B$ là một quan niệm cực kỳ sai lầm. Không nên đánh giá chúng theo cái cách nhìn nhận ban đầu. Hãy để ý đến mục đích chúng được sinh ra và cố gắng _"hiểu"_ để có thể _"lập trình hiệu quả trên ngôn ngữ"_.

    Ngôn ngữ không phế, chỉ có lập trình viên phế. Đừng đổ lỗi cho chương trình của bạn chạy chậm là do ngôn ngữ lập trình.