# Python

## I. Tổng quan

Python trải qua nhiều phiên bản đã có python2 và python3. Mặc dù python2 mới là đỉnh cao đem lại sự phát triển lớn mạnh dành cho ngôn ngữ này nhưng qua thời gian python2 đã không còn phù hợp với nhiều công nghệ mới. Vì vậy nếu không thực sự phải làm việc với những hệ thống cao tuổi thì khuyến khích nên cài đặt python3 với nhiều hỗ trợ đầy đủ hơn và tốt hơn.

## II. Cài đặt cho windows

1. Tải tệp cài đặt Python trực tiếp từ [trang chủ](https://www.python.org/).
    * ![alt text](img/python-0.png)
1. Sau đó chỉ cần cài đặt. Ở bước này nếu không thông thạo thì cứ cài đặt như bình thường vào ổ Win(C:) không sao cả vì python khá là nhẹ. Nhưng nên chọn `Add python.exe to PATH` để có thể dùng các lệnh python ở `command console (cmd)`.
    * ![alt text](img/python-1.png)
1. Nếu không muốn gặp vấn đề với đường dẫn thì nên chọn lựa chọn này! Chủ yếu hệ thông Windows thi thoảng sẽ có đường dẫn rất rất dài do windows không hạn chế về dir-lenght + filename-length dựa trên số lượng `ascii` mà trên `số lượng ký tự`. Điều này nếu không mở ra có thể chạy code python sẽ lỗi. Còn nếu có thể bỏ được thì cũng tốt nếu bạn tự tin và khả năng quản lý và xử lý lỗi của mình.
    * ![alt text](img/python-2.png)

Vậy là xong rồi đó!

## III. Cài đặt cho Ubuntu

### Phiên bản tiêu chuẩn

Ở Linux thì chỉ cần dùng lệnh `Terminal`.
```bash
sudo apt-get update
sudo apt-get install python3
```

## Cài các phiên bản khác của Python

Nhiều hệ thống cũ vẫn dùng Python phiên bản cũ cái mà theo thời gian không còn được hỗ trợ nữa. Nhưng vì dự án còn chạy nên đôi khi, có thể gọi là đôi khi sẽ cần Python cũ để chạy những chương trình đó. Cụ thể và trực tiếp nhất chính là giai đoạn bùng nổ của 

### Nguồn tải

Các phiên bản đã được xuất bản của python được tải lên ở đây [link](https://www.python.org/ftp/python/)

### Windows

Cài đặt cho windows rất dễ, chỉ cần chọn 1 phiên bản và chọn tệp dạng `.msi` hoặc `.exe` và cài đặt như bình thường.

### Linux hoặc Ubuntu

- Lựa chọn đúng phiên bản xem hướng dẫn tại (TO_DO)
- Sau đó là tải gói cài đặt xuống, thường đuôi là `.tgz`. Tải xuống bằng trình duyệt web hoặc là chọn phiên bản và tải về với `wget`. Ví dụ với version 3.12.3:

```
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
```

- Trước khi làm gì thì nên cập nhật hệ thống để tải các gói mới nhất về:

```bash
sudo apt install
```

- Xong rồi thì giải nén gói vừa cài

```bash
tar -xf Python-3.11.3.tgz
```
!!! warning "Chú ý"
    Nếu chưa cài đặt các gói phụ thuộc dưới đây thì nên chạy lệnh dưới đây để cài đặt các gói cần thiết


```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```
- Rồi thì thực hiện các bước cài đặt, ví dụ với python 3.12.3

```bash
cd Python-3.12.3
```

- Cấu hình cài đặt

```bash
./configure --enable-optimizations
```

- Với cờ được thêm vào là:
    - `--enable-optimizations` hữu ích và nên thêm
    - `--with-ensurepip=install` có thể có hoặc không

- Rồi cuối cùng là chạy `make` để build. Hoặc `make -j 4` nếu chỉ muốn chạy build trên 4 luồng để tiết kiệm tài nguyên cho các tác vụ khác

```bash
make
```

Hoặc

```bash
make -j 4
```

Vậy là hoàn thành bước cài đặt, cuối cùng là lựa chọn sử dụng gói `python2` hay `python3` nào bởi hầu hết các hệ thống đều có thể tồn tại 2 gói độc lập. Bạn cũng có thể dùng một trong 2 cách dưới đây để cài mặc định cho hệ thống là sử dụng `python3` thay vì `python2`.
Chạy lệnh này nếu muốn cài đặt bản mới riêng biệt mà không phải là phiên bản nâng cấp của python cũ đã có trên máy.

```bash
sudo make altinstall
```

Dùng soft-link để gán tệp thực thi từ `python2` -> `python3`. Chuyển `python3` thành mặc định. Nói đơn giản, mỗi lần dùng `python` tức là `python3`

```bash
ln -s /usr/bin/python /usr/bin/python3.12.3
```

## Cài đặt biến môi trường

Với hệ điều hành Windows thì đó gần như là điều bắt buộc vì các phần mềm hệ thống có vẻ chẳng bao giờ nằm gọn ở một chỗ, thế nên có một số cài đặt sau nên được thêm vào biến môi trường trên Windows. Các biến môi trường cần thêm là:

```bash
%USERPROFILE%\AppData\Local\Programs\Python\Python$\
%USERPROFILE%\AppData\Local\Programs\Python\Python$\Scripts
```

_Thay `$` bằng phiên bản Python tương ứng_

!!! warning "Lưu ý:"
    - `Python313` là phiên bản python hiện tại sử dụng, sẽ thay đổi đường dẫn dựa trên phiên bản mà bạn cài đặt.
    - Hai thư mục đó là chứa tệp `py.exe` và `pip.exe` (có thể là `py3.exe` hoặc `pip3.exe`)