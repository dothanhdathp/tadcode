# Python Any Version

## Tải về

Trong đường dẫn này chứa [đầy đủ các phiên bản đã được Release](https://www.python.org/ftp/python/) của Python từ xưa đến nay. Hãy vào đó và tìm phiên bản bạn muốn xài.

- __Cho Windows__: Tải về bản cài đặt với đuôi `.msi` là được

## Ubuntu

Ubuntu mình biết một cách được sử dụng để dựng lại và cài đặt python lên hệ thống mà không lo về vấn đề tương thích hoặc mất thời gian đi tìm kiếm phiên bản Python phù hợp. Chính là tải về gói dựng và `build + install`trên chính thiết bị của mình.

Trước tiên nói qua lý do mình biết đến cái này và tại sao nó có, đơn giản là vì không phải tất cả các phần mềm đều tương thích với Python, đặc biệt là các hệ điều hành Linux phiên bản cũ.

Ở thời kỳ bùng nổ công nghệ, hàng loạt công nghệ mới nổi lên và hàng triệu phần mềm mới mỗi năm, các hệ điều hành có sự thay đổi chóng mặt và nhờ việc `open-soure` của ___Linux___, một hệ thống khổng lồ các loại phần mềm / ứng dụng / framework xịn sò đã được tạo ra.

Nhưng không phải tất cả đều ổn. Có nhiều dự án với thời gian phát triển lâu dài, họ khó có thể kịp xuất bản phần mềm theo bước tiến phiên bản của hệ điều hành hoặc phần mềm dựng như Python được nên họ yên lòng sử dụng các phiên bản cũ. Chính vì thế có một thời gian vượt quá ngưỡng thời gian hỗ trợ, 

### Cài đặt các gói phụ thuộc

Cài đặt các gói phụ thuộc sau:

```bash
sudo apt install
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

Hoặc có thể dùng lệnh này nếu muốn __Auto Selecte Yes__ trong lúc cài

```bash
sudo apt install
for i in {build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev};\
    do sudo apt install $i -y;\
done;
```

### Cài đặt biến môi trường

Việc cài đặt biến môi trường này chỉ là hỗ trợ thao tác. Hiểu đơn giản từ các câu lệnh sau, các biến sẽ được thay thế bằng các giá trị đúng.

Có thể cài đặt:

- `PYTHON_VERSION`: Số hiệu phiên bản đầy đủ
- `PYTHON_MAJOR`: Số hiệu phiên bản chính

Ví dụ nếu muốn cài đặt phiên bản `3.8.16` và đương nhiên tệp cục bộ của nó ở đường dẫn [https://www.python.org/ftp/python/3.8.16/](https://www.python.org/ftp/python/3.8.16/). Cài đặt biến môi trường như sau:

```txt
export PYTHON_VERSION=3.8.16
export PYTHON_MAJOR=3
```

### Tải về gói cài đặt

Tải về gói cài đặt bằng `wget`:

```txt
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
```

Giải nén:

```txt
tar -xvzf Python-${PYTHON_VERSION}.tgz
```

### Cài đặt

Điều hướng và tệp vừa được giải nén:

```txt
cd Python-${PYTHON_VERSION}
```

Cấu hình cài đặt:

```txt
./configure \
    --prefix=/opt/python/${PYTHON_VERSION} \
    --enable-shared \
    --enable-optimizations \
    --enable-ipv6 \
    LDFLAGS=-Wl,-rpath=/opt/python/${PYTHON_VERSION}/lib,--disable-new-dtags
```

Cài đặt:

- `make`: cài đặt đơn thuần
- `make install`: có thể dùng lệnh này nếu ___make___ không hoạt động
- `make -j 8 install`: thêm số luồng thực thi nếu máy bạn đủ khỏe.