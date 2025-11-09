# Rust Setup

## Tải về bản cài đặt

- Cài đặt Rust từ [trang chủ](https://www.rust-lang.org/).
- Tải rust từ trang [Install](https://www.rust-lang.org/tools/install) của họ.

## Cài đặt cho Windows

### Windows Install Normal

Với hệ điều hành windows thì chỉ cần tải xuống bản cài đặt phù hợp với hệ điều hành _([64-bit](https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe) hoặc [32-bit](https://www.rust-lang.org/tools/install))_.

Chương trình sẽ chạy trên `terminal` giống như này:

```text
Rust requires a linker and Windows API libraries but they don't seem to be
available.

These components can be acquired through a Visual Studio installer.

1) Quick install via the Visual Studio Community installer
   (free for individuals, academic uses, and open source).

2) Manually install the prerequisites
   (for enterprise and advanced users).

3) Don't install the prerequisites
    (if you're targeting the GNU ABI).
```

Chọn `1` nếu không hiểu lắm về môi trường hoặc yêu cầu.

Chương trình sẽ đưa thêm câu hỏi về cài đặt __Visual Studio__, cái đó là môi trường để chạy chương trình rust trên windows thôi nên không vấn đề, chọn `Continue`.

Yêu cầu cài đặt MSVC, vẫn đồng ý cài đặt.

<figure markdown="span">
    ![installer-msvc](img/rust-setup.png)
    <figcaption>MSVC Install</figcaption>
</figure>


Xong việc rồi chỉ còn chờ cài đặt xong là được.

Rồi xong việc thì kiểm tra với lệnh sau:

```bash
rustc --version
```

Nếu kết quả trả về dạng như này là thành công rồi:

```bash
rustc 1.79.0 (129f3b996 2024-06-10)
```

### Install for MSYS2

Cách này mình thoải mái hơn vì nó hoạt động được cả với __Makefile__

```bash
pacman -S mingw-w64-x86_64-rust
```

## Cài đặt cho Linux

### Cách 1: Install Rust Using

- Tải về qua `curl`

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

- Nhấn Enter để tiến hành cài đặt mặc định.
- Cài đặt `source`

```bash
source "$HOME/.cargo/env"
```

- Cuối cùng là kiểm tra phiên bản:

```bash
rustc --version
```

### Cách 2: Install Rust Using APT

```bash
sudo apt update
sudo apt install rustc
rustc --version
```