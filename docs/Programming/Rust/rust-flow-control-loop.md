# \[Rust\] Loop

## Cơ Bản

```rust
fn main() {
	let mut cond = 100;
	loop {
		cond -= 1;
		if cond == 0 {
			break;
		}
	};
	println!("cond: {}", cond);
}
```
```text title="Kết Quả"
cond: 0
```

- Khai báo vòng lặp với __*loop*__
- Vòng lặp sẽ liên tục cho đến khi có lệnh gọi __*break*__
- `cond -= 1` là bước hạ một đơn vị cho biến `cond`

## Break And Return

`loop` cũng hỗ trợ việc trả về kết quả nhanh chóng trong khi gọi __break__.

```rust
fn main() {
	let mut cond = 100;
	let ret = loop {
		cond -= 1;
		if cond == 0 {
			break 20;
		}
	};
	println!("ret = {}", ret);
}
```
```text title="Kết Quả"
ret = 20
```

- _`break` với giá trị nhưng không có gán biến nhận giá trị trả về cũng không sao._

## Nesting and labels

Đây là một tính năng rất hay. Rust cho phép gán nhãn vào mỗi vòng lặp `loop` và có thể thoát vòng lặp với nhãn của nó.


```rust
fn main() {
	let mut cond = 100;
    'outer: loop {
        cond -= 5;
        'inner: loop {
            cond -= 3;
            if(cond < 10) {
                break 'outer;
            }
        }
    }
	println!("cond = {}", cond);
}
```
```text title="Kết Quả"
ret = 8
```