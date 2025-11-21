# \[C++\] My Stack

Tự viết lại một lớp stack theo ý của mình bằng con trỏ và áp dụng __*template*__

Lớp này có thể phát triển cực kỳ đơn giản mà không cần thêm một lớp nào khác bổ sung để làm rõ ý nghĩa:

## Lớp

```cpp title="Class TStack"
template <typename T>
struct TListNode {
    T val;
    TListNode *next;
    TListNode(T x) : val(x), next(nullptr) {}
};

template <typename T>
class TStack {
public:
    TListNode<T>* head;

    TStack() {
        head = nullptr;
    }

    void push(T val) {
        TListNode<T>* new_node = new TListNode<T>(val);
        new_node->next = head;
        head = new_node;
    }

    void pop() {
        if(nullptr == head)
            return; // should be throw in here.

        TListNode<T>* top = head;
        head = head->next;
        delete top;
    }

    T top() {
        T res = head->val;
        return res;
    }

    bool empty() {
        return (nullptr == head);
    }
};
```
- __TListNode__: Là một lớp con tương đương một đối tượng được sử dụng để làm nơi chứa thành phần tương đương một phần tử của __Stack__.
- __TStack__: Đóng gói lớp __TListNode__, sử dụng con trỏ để phát triển. Tôi muốn kiểm tra về tính an toàn luồng và đảm báo mức độ tiêu thụ thấp.

## Chương Trình

```cpp title="main.cpp"
#include "stdio.h"
#include <math.h>
#include <float.h>

using namespace std;

// Implement Stack by C
template <typename T>
struct TListNode {
    T val;
    TListNode *next;
    TListNode(T x) : val(x), next(nullptr) {}
};

template <typename T>
class TStack {
public:
    TListNode<T>* head;

    TStack() {
        head = nullptr;
    }

    void push(T val) {
        TListNode<T>* new_node = new TListNode<T>(val);
        new_node->next = head;
        head = new_node;
    }

    void pop() {
        if(nullptr == head)
            return; // should be throw in here.

        TListNode<T>* top = head;
        head = head->next;
        delete top;
    }

    T top() {
        T res = head->val;
        return res;
    }

    bool empty() {
        return (nullptr == head);
    }
};

int main(int argc, char const *argv[]) {
    TStack<int> my_stack;
    for (int i = 0; i < 100; ++i) {
        
    }
    my_stack.push(10);
    my_stack.push(20);
    my_stack.push(30);
    my_stack.push(30);
    my_stack.push(30);
    my_stack.push(30);
    while (!my_stack.empty())
    {
        printf("%d\n", my_stack.top()); my_stack.pop();
    }
    return 0; // Return success
}
```