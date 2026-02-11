# The Wavefunction Collapse

> Tạm dịch là __Mô Hình Hàm Sóng Sụp Đổ__

Đây là một thuật toán rất thú vị cái mà hay dùng để tạo ra những bản đồ ngẫu nhiên trên những trò chơi điện tử dựa trên một tập mẫu về __hạt giống__ và __quy luật__ được đưa ra.

Về hoạt động nghe rất kinh khủng nhưng thật ra cách vận hành của nó khá đơn giản.

## Vận Hành

Việc đầu tiên bạn cần xác định một __bộ quy luật__ và các điểm. Ví dụ như nếu như trò chơi **Đế Chế _(AOE)_** muốn tạo ra một bản đồ tự nhiên nhất có thể thì nó nên là:

1. Tạo ra các đơn vị và đánh cho chúng  thuộc tính:
    - __Nhà__ và __Dân__, __Quân Lính__ là các __Đơn Vị Bộ__
    - __Thuyền__ và __Cá__ là đơn vị __Nước__
    - __Cây Dừa__, __Cây Cọ__ ở __Hoang Mạc__
2. Thiết lập một số bộ _quy tắc mở_. Nên tránh quá chặt chẽ sẽ dễ gây chồng chập vi phạm.
    - __Nhà__ và các __Đơn Vị Bộ__ không thể xây trên khu vực __Nước__. Chỉ có thể trên __Đất__.
    - __Cây Cọ__ phải ở khi __Đất Hoang Mạc__
    - __Cây Sồi__ và __Cây Dẻ__ xuất hiện nhiều ở các khu vực đất xanh. Hoang mạc tỉ lệ `5%`
    - Nước cách đất khoảng 2 ô sẽ thành __Nước Sâu__ và có màu tối hơn.
    - ...
3. Sau bước trên, thuật toán sẽ tạo ra một bản đồ ảo ở mỗi điểm sẽ là __Bất Kỳ Thứ Gì__ đề chờ đến khi __Hạt Giống__ được đặt vào bản đồ.
3. Nếu muốn __Hạt Giống__ được tự nhiên. Có thể theo một số quy tắc.
    - Các quân đội khác nhau sẽ không ở gần. Ví Dụ __Quân Đỏ__ và __Xanh__ nếu có trên bản đồ sẽ cách nhau ít nhất 20 ô.
    - Để người chơi không thua thiệt thì gần các đơn vị quân các Tài Nguyên như _gỗ_, _vàng_, _thịt_, ... sẽ được đặt cố dịnh một lượng luôn có. Các yếu tố còn lại sẽ được tuỳ biến.
4. Đặt __Hạt Giống__ vào __Bản Đồ__ và thuật toán sẽ hoạt động như sau:
    - Vì các đơn vị quân đều là quân bộ nên dưới chân sẽ luôn là __Đất__.
    - Các phân vùng có sẵn như cây, quả, đá vàng cũng đặt là __Đất__
    - Dựa theo luật thì khu vực ít nhất xung quanh mỗi đơn vị phải qua 20 bước mới có thể là nước. Sau 20 bước chạy thuật toán _random_ theo tỉ lệ đê xác định nước hoặc đất.
    - Xong lại kiểm tra các đơn vị xung quanh có thoả mãn luật không, lặp lại, ...

Nói chung thì tuy hơi đần nhưng thật toán rất hay. Nó ví dụ như một điều gì đó được phản hồi lại từ tự nhiên theo quy luật. Những điều còn lại nếu không vi phạm mà còn nhiều lựa chọn sẽ được _chọn ngẫu nhiên_.

Chính điều thú vị này dẫn đến chế độ random bản đồ ở các trò chơi bậc cao.


Mình có thể đọc thêm về thuật toán này ở đây: [https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/)

> Cái thuật toán này mình thấy khi xem về bài giải thuật của __Sudoku__