# \[C++\] Hàm Đệ Quy

## Định nghĩa

- Hàm đệ quy hay hàm gọi hàm là một cách viết hàm gọi lại chính nó sử dụng phương pháp đệ quy.
- Hàm đệ quy có tốc độ ưu việc nhờ việc thực hiện các tác vụ trên chính bộ nhớ stack
- Hàm đệ quy cần phải đảm bảo việc thực thi cần có:
    - Phải có điểm kết thúc (điểm trả về)
    - Tiến trình vừa phải, không quá nhiều lần chồng chập tránh hiện tượng __*stack over flow*__

## Ví dụ



## Ứng dụng

### Chuỗi Fibonancy

Hàm đệ quy có nhiều ứng dụng trong đó một số ứng dụng phổ biến là ứng dụng cho phần tử thứ n của chuỗi fibonacci

```c++
int fibonanci(int n) {
    if(n <= 1) return n;
    return fibonanci(n-1) + fibonanci(n-2);
}
```