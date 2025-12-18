# \[C++\] Linked List

__Linked List__ là dạng cơ sở dữ liệu cơ bản đầu tiên. Nó hoạt động the kiểu các thùng chứa đơn có một đầu liên tục. __Linked List__ có tốc độ cao, tính ổn định cũng cao và phân bổ bộ nhớ động nên khá được ưa dùng. Đây là cơ sở dữ liệu đầu tiên được học.

## Linked List 1 Chiều

Như tên gọi đây là một dạng chuỗi đơn có một chiều

### Cấu Trúc

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
```

### Triển Khai

```cpp
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
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

## Linked List 2 Chiều

### Cấu Trúc

Cấu trúc con trỏ hai chiều cực đơn giản. Nó chỉ đơn giản là tạo thêm một con trỏ về chiều back nữa.

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode *back;
    ListNode(int x) : val(x), next(nullptr), back(nullptr) {}
};
```

### Triển Khai

```cpp
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode *back;
    ListNode(int x) : val(x), next(nullptr), back(nullptr) {}
};

int main() {
    ListNode* root = new ListNode(0);
    ListNode* last = nullptr;

    ListNode* current = root;
    int cnt = 20;
    while (--cnt)
    {
        // create new ListNode
        current->next = new ListNode(current->val + 1);
        current->next->back = current;
        current = current->next;
    }
    
    current = root;
    std::cout << ">>> Node: ";
    while (true)
    {
        std::cout << current->val << " --> ";
        if(current->next == nullptr) {
            break;
        } else {
            current = current->next;
        }
    }
    std::cout << "{};" << std::endl;
    std::cout << "<<< Node: ";
    while (true)
    {
        std::cout << current->val << " --> ";
        if(current->back == nullptr) {
            break;
        } else {
            current = current->back;
        }
    }
    std::cout << "{};" << std::endl;
    return 0;
}
```

_Nếu mà sử dụng đầu ra với hai đầu left/right ta có cấu trúc dữ liệu thứ hai là *tree*_

__*TO_DO*__