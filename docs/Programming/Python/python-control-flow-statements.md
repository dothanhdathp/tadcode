# Điều khiển luồng

> Thật kỳ lạ là những cái này tồn tại ở trong hầu hết tất cả các ngôn ngữ lập trình nhưng lại chưa có ai đặt tên cho chúng.

Luôn có nhiều cách khai thác mạnh mẽ hơn ở các ngôn ngữ bậc cao nhưng điều thú vị là cơ chế điều khiển luồng hầu như chưa từng thay đổi. Bất kỳ một ngôn ngữ lập trình nào đều cần có chúng như những bộ công cụ căn bản bậc nhất. Nó có thể thêm nhưng hầu như không ai quyết định loại bỏ chúng cả. Đã có nhiều trường hợp có gắng bỏ cơ chế `switch/case` chẳng hạn nhưng rồi thì nó vẫn trở lại và tốt hơn.

Nào cùng đi qua các chức năng căn bản này.

## IF / ELSE

### IF

Đây là cơ chế đầu tiên và căn bản nhất. Ở cấp độ đầu nó có nghĩa là nếu đúng thì _(làm gì đó)_. Ví dụ:

```python
a = 100
b = 10

if a > b:
    print("a > b là đúng")
```
```text
a > b là đúng
```

### IF / ELSE

Tiếp đến là mở rộng hơn, nếu đúng thì _(làm gì đó)_ và ngược lại, nếu sai thì ta _(làm gì đó)_. Ví dụ:

Tức là trong đoạn trên, phần code thực thi nằm trong nhánh còn lại đã không được đi qua chỉ thực hiện nội dung trong trường hợp đúng. Đây là một trong những cơ chế cơ bản của lập trình. __*Nếu đúng thì làm gì và sai thì làm gì.*__

Mở rộng hơn cho trường hợp kiểm tra nhiều lần lại cần đổ xuống theo thứ bậc, thì có cách viết như này:

```python
a = 100
b = 10

if b > a:
    print("b > a là đúng")
else:
    print("b > a là sai")
```
```text
b > a là sai
```

### 