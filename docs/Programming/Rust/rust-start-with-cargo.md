# Start With Cargo

> Sách tham khảo tại [The Cargo Book](https://doc.rust-lang.org/cargo/)

??? note "Tổng Kết"
	- Tạo dự án
	```text
	cargo new hello-world --bin
	```
	- Biên dịch
	```text
	cargo build
	```
	- Chạy tệp thực thi
	```text
	cargo run
	```

## Cài Đặt

### Bản cài đặt

Trên Linux hoặc macOS sử dụng lệnh sau để cài đặt:

```bash
curl https://sh.rustup.rs -sSf | sh
```

### Dựng Từ Source

**Cargo** cũng cung cấp giải pháp đưa ra từ source với mã nguồn mở tại [Cargo Github](https://github.com/rust-lang/cargo#compiling-from-source)

Về cách làm thế nào thì để bài khác viết.

## Bắt Đầu

### Mục Đich

Mục đích của bài này là tạo một dự án hello-world với Cargo và chạy thử.

### Thực Hành

Chạy lệnh sau là được, Cargo tự tạo dự án và các tệp cần thiết

```bash
cargo new hello-world --bin
```

Sau khi kết thúc sẽ có thư mục mới tên  `hello-world` với cấu trúc thư mục như sau:

```text
.
├── Cargo.toml
└── src
    └── main.rs
```

Với các tệp:

- `src/main.rs`: là tệp chứa mã gốc
- `Cargo.toml` là tệp chứa thông tin về phần mềm, cấu hình, phiên bản, etc, ...

Việc hiểu các tệp **Cargo.toml** xem bài tiếp theo [Cargo Toml](./rust-cargo-toml.md). Giờ Hãy chạy thử lệnh sau _(bên trong tệp dự án)_

```bash
cargo build
```

Và chạy thử dự án

```bash
cargo run
```

Kết Quả

```text
Hello, world!
```

### Kết Quả

Sau khi chạy thành công sẽ có thư mục mới được sinh ra  tên là **target**, với cấu trúc thư mục như sau:

```text
.
├── CACHEDIR.TAG
└── debug
    ├── build
    ├── deps
    │   ├── hello_world-72594be6e3adde6a
    │   └── hello_world-72594be6e3adde6a.d
    ├── examples
    ├── hello-world
    ├── hello-world.d
    └── incremental
        └── hello_world-2r0b0o30axhxa
            ├── s-hgw06antog-fmfdjt-2l2a3mwzsfr0fmq7rukmo6nf9
            │   ├── 2a3r3ov58y7sge3o.o
            │   ├── 2gt82fsgpnv7ctqc.o
            │   ├── 3q0fcewwr8qn7v1y.o
            │   ├── 4716n26icwzwav0r.o
            │   ├── 4hx1yy8osqtnl3gq.o
            │   ├── dep-graph.bin
            │   ├── query-cache.bin
            │   ├── work-products.bin
            │   └── zk7qewlc09aa2cc.o
            └── s-hgw06antog-fmfdjt.lock
```

- Trong đó có tệp `debug/hello-world` là tệp thực thi.
- Các tệp còn lại là các tệp tạm thời khi biên dịch, không quá quan trọng.