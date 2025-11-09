# Rust HelloWorld

## Bắt đầu với rustc

Đầu tiên là tạo một tệp `main.rs` có nội dung như này:

```bash title="main.rs"
fn main() {
    println!("Hello World!");
}
```

Sau đó biên dịch với `rustc` như sau:

```bash
rustc main.rs
```

Kết quả đầu ra được tệp thực thi `main.exe` chạy tệp tin này được kết quả như sau:

```txt
Hello World!
```

## Bắt đầu với Cargo

### Tạo dự án

__Cargo__ là bộ quản lý gói của __Rust__ và nó rất mạnh. Hầu hết mọi người có lý do sử dụng __Rust__ là do nó.

Bắt đầu một dự án mới như sau:

```bash
cargo new HelloWorld
```

Sau lệnh đó sẽ tạo được một tệp mới tên là `HelloWorld`. Kiến trúc tệp của nó như này:

```bash
.
├── Cargo.lock
├── Cargo.toml
└── src
    └── main.rs
```

- `Cargo.toml` : tệp này chứa thông tin dự án. __Cargo__ sẽ tự động thêm thông tin ở đây vào nội dung của gói phát hành.
    ```bash title="Cargo.toml"
    [package]
    name = "HelloWorld"
    version = "0.1.0"
    edition = "2024"

    [dependencies]
    ```
- `main.rs` : tệp nguồn. _Code_ vào đây.
    ```rust
    fn main() {
        println!("Hello, world!");
    }
    ```

### Chạy dự án

Vào trong tệp `HelloWorld` và chạy lệnh sau:

```bash
cargo run
```

Kết quả như này:

```bash
   Compiling HelloWorld v0.1.0 (D:\Code\rust\HelloWorld)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.37s
     Running `target\debug\HelloWorld.exe`
Hello, world!
```

## Makefile

Nhưng mà vì __Cargo__ chạy hơi chậm nên mình thích dùng __Makefile__ hơn. Để chạy nò thì đơn giản là sử dụng __Msys2__ để chạy với `make`. Trước đó thì cần tải gói cài đặt của `rustc` từ bài trước.

Đây là tệp __Makefile__ mẫu:

```make title="Makefile"
RSC = rustc

SRC = main.rs
TARGET = main.exe

$(TARGET): $(SRCS)
	$(RSC) $(SRC)
```

Để tệp `main.rs` bên cạnh __Makefile__, kiến trúc như này

```txt
Makefile
main.rs
```

Rồi sau đó chạy lệnh dưới này để _build_ và _run_

```bash
make clean && make main && ./main.exe
```