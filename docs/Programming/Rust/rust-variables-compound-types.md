# \[Rust\] Biến Phức Hợp

> Kiểu dữ liệu tập hợp của nhiêu kiểu biến dạng [Scalar](rust-variables-scalar-types.md)

## Định Nghĩa

- Dạng phức hợp có thể hiểu chính xác là tập hợp của các kiểu  __Scalar__.
- Nó sẽ hành xử và có tính chất như một tâpj hợp cấu trúc.
- Để so sánh với các ngôn ngữ bậc thấp và trung khác thì nó kiểu như __*array*__ hoặc __*struct*__. Việc dữ liệu này được đưa vào làm một trong các dạng nguyên thủy làm mình có phần bối rối. Các dạng thức tập hợp hơi khó để thực hiện với các phương thức tính toán cơ bản.

## Kiểu Phức Hợp

Có ba kiểu phức hợp chính là:

- [Tuples](rust-variables-compound-types-tuples.md): Là dạng _cấu trúc_ gồm nhiều loại dữ liệu khác nhau được tập hợp với nhau. Nó có phần giống với __*struct*__ của C++.
- [Array](rust-variables-compound-types-array.md): Dạng chuỗi cơ bản có yêu cầu về độ dài. Tương tự với các kiểu chuỗi cơ bản trong các ngôn ngữ lập trình khác.
- [Slices](rust-variables-compound-types-slices.md): Giống như chuỗi nhưng không có yêu cầu về độ dài. Việc hoạt động của chuỗi này có lẽ giống kiểu __*vector*__ trong C++.