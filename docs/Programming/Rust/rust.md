# \[Rust\] About Rust

Rust là một ngôn ngữ lập trình hệ thống hiện đại tập trung vào __tính an toàn__, __tốc độ__ và __tính đồng thời__. Ngôn ngữ này đạt được những mục tiêu này nhờ __*tính bảo mật bộ nhớ*__ mà không cần sử dụng cơ chế thu gom rác.

Rust mạnh mẽ nhất trong việc tạo ra các mã đơn giản mà an toàn. Hầu hết là nhờ bộ __quy tắc lặp trình chặt chẽ__ được sử dụng trong trình biên dịch. Mặc dù đã cố gắng áp dụng các __khái niệm tiên tiến__ mà an toàn từ những ngôn ngữ bậc cao như _tự động xác định kiểu biến an toàn_, nhưng dù vậy __*Rust*__ vẫn

- Khó học
- Build chậm
- Khó tiếp cận, cần có kiến thức đa điều từ cả ngôn ngữ lập trình lẫn kiến thức hệ thống.
- Không có nhiều các plugin hỗ trợ hoặc một tập đoàn hỗ trợ mạnh mẽ như __Kotlin__ của __Google__

## Roadmap

```puml
@startmindmap
skinparam backgroundcolor transparent
!$URL = "/Programming/Rust"

* [[$URL/rust/ Rust]]

left side
**_ [[/ Coder]]

right side
** Khởi Đầu
***_ What is Rust
***_ Why Rust
***_ C++ vs Rust
*** Cài Đặt
****_ Windows
****_ Linux
***_ Hello World
***_ [[$URL/rust-document Documents]]
***_ [[https://play.rust-lang.org/?version=stable&mode=debug&edition=2024 Playground]]

** [[$URL/rust-variables/ Variables]]
***_: [[$URL/rust-scalar-types Scalar Types]]
  ├─ i32, i64, u32, u64, ...
  ├─ f32, f64, ...
  └─ boolean, char, ...
;
***_ Compound Types
****_ [[$URL/rust-tuples/ Tuples]]
****_ [[$URL/rust-array/ Array]]
****_ [[$URL/rust-slices/ Slices]]
***_ [[$URL/rust-custom-types Custom Types]]
****_ Enum
****_ Struct
** Control
*** Flow Control
****_ [[$URL/rust-flow-control-if-else/ if/else]]
****_ [[$URL/rust-flow-control-loop/ loop]]
****_ [[$URL/rust-flow-control-while/ while]]
****_ [[$URL/rust-flow-control-for/ for]]
****_ [[$URL/rust-flow-control-match/ match]]
*** Operator

** System
*** IO

@endmindmap
```