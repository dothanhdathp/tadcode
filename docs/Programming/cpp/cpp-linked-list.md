# \[C++\] Linked List

__Linked List__ là dạng cơ sở dữ liệu cơ bản đầu tiên. Nó hoạt động the kiểu các thùng chứa đơn có một đầu liên tục. __Linked List__ có tốc độ cao, tính ổn định cũng cao và phân bổ bộ nhớ động nên khá được ưa dùng. Đây là cơ sở dữ liệu đầu tiên được học.

## Linked List 1 Chiều

Như tên gọi đây là một dạng chuỗi đơn có một chiều

### Code

#### Cấu Trúc

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

#### Triển Khai

```cpp
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int main() {
    ListNode* root = new ListNode(0);
    ListNode* runner = root;
    int cnt = 20;
    while (--cnt)
    {
        runner->next = new ListNode(runner->val + 1);
        runner = runner->next;
    }
    while (root != nullptr)
    {
        std::cout << "Node: " << root->val << std::endl;
        root = root->next;
    }
    return 0;
}
```

