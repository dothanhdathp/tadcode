# Dangling Pointers

Trong C++, con trỏ cho phép quản lý bộ nhớ trực tiếp, nhưng chúng cũng có thể dẫn đến các vấn đề như con trỏ treo lơ lửng. Con trỏ lơ lửng xảy ra khi con trỏ tiếp tục tham chiếu đến bộ nhớ đã được giải phóng hoặc không còn hợp lệ. Điều này có thể gây ra hành vi không thể đoán trước, sự cố và rủi ro bảo mật. Trong bài viết này, chúng tôi sẽ giải thích con trỏ lơ lửng là gì, cung cấp ví dụ và thảo luận về các phương pháp hiệu quả để ngăn chặn chúng, giúp bạn viết mã C++ an toàn và đáng tin cậy hơn.

## 1. What is a Dangling Pointer?

__Con trỏ lơ lửng__ _(Dangling Pointers)_ là con trỏ trỏ tới một vị trí bộ nhớ đã được giải phóng hoặc giải phóng. Điều này xảy ra khi một chương trình không còn cần một phần bộ nhớ nữa nên nó được giải phóng nhưng con trỏ vẫn giữ địa chỉ của bộ nhớ được giải phóng đó. Việc truy cập hoặc sửa đổi dữ liệu thông qua con trỏ lơ lửng sẽ dẫn đến hành vi không xác định và có thể khiến chương trình gặp sự cố hoặc dữ liệu bị hỏng.

Con trỏ lơ lửng đề cập đến con trỏ không còn trỏ đến vị trí bộ nhớ hợp lệ nhưng vẫn giữ địa chỉ bộ nhớ. Điều này thường xảy ra khi bộ nhớ được trỏ tới bị giải phóng hoặc nằm ngoài phạm vi, khiến con trỏ __*"dangling"*__.

Ví dụ, trong C++, nếu một con trỏ tham chiếu đến bộ nhớ được cấp phát động đã được giải phóng bằng cách sử dụng `delete`, thì con trỏ sẽ không tự động đặt lại về `nullptr`. Nó vẫn chứa địa chỉ bộ nhớ cũ, dẫn đến khả năng truy cập vào bộ nhớ không hợp lệ.

## 2. Dangling Pointer Examples in C++

Con trỏ lơ lửng là một vấn đề phổ biến trong C++ khi con trỏ tiếp tục tham chiếu đến một vị trí bộ nhớ đã bị giải phóng hoặc không còn hợp lệ. Hãy xem xét ba trường hợp phổ biến xảy ra con trỏ lơ lửng, cùng với các giải thích chi tiết và ví dụ về mã.

Hãy xem xét một số tình huống phổ biến khi con trỏ lơ lửng xảy ra:

### 2.1 Memory Deallocation

Một con trỏ lơ lửng phát sinh khi một con trỏ trỏ tới bộ nhớ đã được giải phóng bằng cách sử dụng `delete`. Con trỏ vẫn giữ địa chỉ của bộ nhớ đã giải phóng nhưng không thể truy cập nó một cách an toàn.

#### 2.1.1 Example

Hãy tưởng tượng bạn cấp phát bộ nhớ để lưu trữ một giá trị và sau đó xóa nó đi. Con trỏ vẫn giữ địa chỉ nhưng trỏ đến bộ nhớ không hợp lệ _(invalid memory)_.

```cpp
#include <iostream>
using namespace std;

void memoryDeallocationExample() {
    int* ptr = new int(10);  // Step 1: Allocate memory
    delete ptr;              // Step 2: Deallocate memory
    cout << *ptr << endl;    // Step 3: Access deallocated memory (undefined behavior)
}

int main() {
    memoryDeallocationExample();
    return 0;
}
```

!!! warning "Kết Luận"
    Sau khi giải phóng bộ nhớ bằng `delete`, luôn đặt con trỏ thành `nullptr` để đảm bảo nó không còn trỏ đến bộ nhớ không hợp lệ nữa.

    ```cpp
    delete ptr;
    ptr = nullptr;  // Safe practice
    ```

### 2.1.2 Returning Local Variables

Con trỏ lơ lửng xảy ra khi hàm trả về địa chỉ của biến cục bộ. Khi hàm kết thúc, biến cục bộ sẽ nằm ngoài phạm vi, khiến con trỏ không hợp lệ.

#### Example

Giả sử một hàm tạo một biến cục bộ và trả về địa chỉ của nó. Biến bị hủy khi hàm kết thúc, làm cho con trỏ không hợp lệ.

```cpp
#include <iostream>
using namespace std;

int* returnLocalVariable() {
    int localVar = 42;  // Step 1: Create a local variable
    return &localVar;   // Step 2: Return its address
}

int main() {
    int* dangling = returnLocalVariable();  // Step 3: Use the returned pointer
    cout << *dangling << endl;  // Step 4: Access invalid memory (undefined behavior)
    return 0;
}
```

!!! warning "Kết Luận"
    Không bao giờ trả về địa chỉ của một biến cục bộ. Thay vào đó:

    - Sử dụng bộ nhớ được cấp phát động nếu cần thiết.
    - Truyền biến theo tham chiếu hoặc giá trị để tránh tạo con trỏ lơ lửng.

### 2.1.3 Memory Overwriting

Một _dangling pointer_ xảy ra khi nhiều con trỏ tham chiếu cùng một bộ nhớ và một trong số chúng sẽ giải phóng bộ nhớ. Các con trỏ khác vẫn giữ địa chỉ không hợp lệ.


#### Example

If two pointers share the same memory and one pointer deletes it, the other becomes dangling.

```cpp
#include <iostream>
using namespace std;

void overwriteMemoryExample() {
    int* ptr = new int(5);   // Step 1: Allocate memory
    int* otherPtr = ptr;     // Step 2: Share the same memory
    delete ptr;              // Step 3: Deallocate memory using one pointer
    cout << *otherPtr << endl;  // Step 4: Access invalid memory (undefined behavior)
}

int main() {
    overwriteMemoryExample();
    return 0;
}
```

!!! warning "Kết Luận"
    Khi nhiều con trỏ chia sẻ cùng một bộ nhớ, hãy đảm bảo tất cả được đặt thành `nullptr` sau khi phân bổ để tránh các _con trỏ lơ lửng_. Tốt hơn hết, hãy sử dụng các con trỏ thông minh như `std::shared_ptr` hoặc `std::unique_ptr` để xử lý bộ nhớ một cách an toàn.

## 3. Problems Caused by Dangling Pointers

Sử dụng con trỏ lơ lửng trong chương trình có thể dẫn đến các vấn đề nghiêm trọng. Dưới đây là lời giải thích chi tiết về những vấn đề chúng gây ra:

### 3.1 Undefined Behavior (Trạng thái vô định)

Khi một con trỏ lơ lửng bị hủy đăng ký _(tức là khi bạn cố truy cập vào bộ nhớ mà nó trỏ tới)_, hoạt động của chương trình sẽ trở nên không thể đoán trước được. Điều này có thể có nghĩa là bất cứ điều gì từ việc tạo ra kết quả không chính xác đến gây ra sự cố.

#### 3.1.1 Why It Happens

Vị trí bộ nhớ mà các tham chiếu con trỏ lơ lửng có thể đã được phân bổ lại hoặc không còn nằm trong tầm kiểm soát của chương trình. Việc truy cập bộ nhớ như vậy không được xác định theo tiêu chuẩn C++.

```cpp
#include <iostream>
using namespace std;

void undefinedBehaviorExample() {
    int* ptr = new int(10);  // Dynamically allocate memory
    delete ptr;              // Deallocate memory
    cout << *ptr << endl;    // Undefined behavior: accessing invalid memory
}
```

#### 3.1.2 Effect

Đầu ra là không thể đoán trước. Đôi khi, chương trình có thể hoạt động nhưng không đáng tin cậy và không an toàn.

### 3.2 Program Crashes

Việc hủy tham chiếu một con trỏ lơ lửng có thể dẫn đến lỗi phân đoạn, lỗi chương trình do cố gắng truy cập vào bộ nhớ mà chương trình không có quyền sử dụng.

#### 3.2.1 Why It Happens

Khi bộ nhớ bị giải phóng, hệ điều hành có thể thu hồi quyền truy cập của chương trình. Mọi nỗ lực truy cập tiếp theo đều dẫn đến sự cố.

```cpp
#include <iostream>
using namespace std;

void programCrashExample() {
    int* ptr = new int(20);  // Allocate memory
    delete ptr;              // Deallocate memory
    cout << *ptr << endl;    // Likely causes a segmentation fault
}
```

#### 3.2.1 Effect

Chương trình kết thúc đột ngột với một lỗi như lỗi phân đoạn hoặc vi phạm quyền truy cập.

### 3.3 Security Vulnerabilities

Attackers can exploit dangling pointers to execute malicious code by injecting their payload into the memory the pointer references.

#### 3.3.1 Why It Happens

Khi một con trỏ tham chiếu đến bộ nhớ đã được giải phóng, bộ nhớ đó sau đó có thể được cấp phát cho một phần khác của chương trình hoặc một nguồn bên ngoài. Những kẻ tấn công có thể thao túng quá trình này để giành quyền kiểm soát hành vi của chương trình.

Hãy tưởng tượng một hệ thống nơi dữ liệu nhạy cảm (như mật khẩu) được lưu trữ trong bộ nhớ. Nếu một con trỏ lơ lửng truy cập vào bộ nhớ đã được giải phóng, kẻ tấn công có thể chiếm quyền điều khiển nó để truy xuất hoặc ghi đè dữ liệu nhạy cảm.

#### 3.3.2 Effect

- Truy cập trái phép vào dữ liệu nhạy cảm.
- Thực thi mã tùy ý, cho phép kẻ tấn công giành quyền kiểm soát hệ thống.

Đây là một kỹ thuật phổ biến trong các hoạt động khai thác bảo mật, chẳng hạn như các cuộc tấn công __Use-After-Free (UAF)__.

<!--  -->

## 4. How to Overcome Dangling Pointer?

Việc tránh các con trỏ lơ lửng là điều cần thiết để viết các chương trình C++ mạnh mẽ và không có lỗi. Con trỏ lơ lửng xảy ra khi con trỏ vẫn giữ địa chỉ của bộ nhớ đã bị giải phóng hoặc không còn hợp lệ. Dưới đây là các phương pháp chi tiết để ngăn chặn và quản lý con trỏ lơ lửng một cách hiệu quả:

### 4.1. Nullify Pointers After Deallocation

Khi bộ nhớ được giải phóng bằng từ khóa delete, con trỏ vẫn giữ địa chỉ bộ nhớ. Điều này dẫn đến một con trỏ lơ lửng vì bộ nhớ không còn hợp lệ. Bằng cách đặt con trỏ thành nullptr, bạn đảm bảo rằng nó không còn tham chiếu đến bộ nhớ không hợp lệ nữa. Truy cập nullptr an toàn hơn vì nó tạo ra lỗi thời gian chạy rõ ràng thay vì hành vi không thể đoán trước.

```cpp
#include <iostream>
using namespace std;

void nullifyPointerExample() {
    int* ptr = new int(10);  // Dynamically allocate memory
    delete ptr;              // Deallocate memory
    ptr = nullptr;           // Nullify pointer

    if (ptr == nullptr) {
        cout << "Pointer is nullified and safe." << endl;
    }
}
```

!!! warning "Kết Luận"
    Luôn đặt lại con trỏ về `nullptr` sau khi cấp phát bộ nhớ để ngăn chúng giữ địa chỉ không hợp lệ. Điều này đảm bảo mọi truy cập ngẫu nhiên vào con trỏ đều có thể được xác định ngay lập tức là lỗi.

### 4.2. Use Smart Pointers

Các con trỏ thông minh, chẳng hạn như `std::unique_ptr` và `std::shared_ptr` trong Thư viện chuẩn C++, tự động quản lý bộ nhớ. Chúng đảm bảo bộ nhớ được giải phóng khi con trỏ thông minh vượt quá phạm vi. Điều này giúp loại bỏ nhu cầu phân bổ thủ công, giảm nguy cơ con trỏ bị treo.

```cpp
#include <memory>
#include <iostream>
using namespace std;

void smartPointerExample() {
    std::unique_ptr<int> smartPtr = std::make_unique<int>(20);  // Smart pointer
    cout << "Smart pointer value: " << *smartPtr << endl;
    // Memory is automatically released when smartPtr goes out of scope
}
```

!!! warning "Kết Luận"
    Sử dụng các tính năng C++ hiện đại như std::unique_ptr và std::shared_ptr để tự động quản lý bộ nhớ. Con trỏ thông minh xử lý việc phân bổ và phân bổ một cách liền mạch, loại bỏ nguy cơ lỗi của con người.

### 4.3. Avoid Returning Local Variables

Trả về địa chỉ của một biến cục bộ từ một hàm là nguồn phổ biến của các con trỏ lơ lửng. Các biến cục bộ được lưu trữ trên ngăn xếp và bị hủy khi hàm thoát. Thay vào đó, hãy phân bổ bộ nhớ trên heap hoặc chuyển biến theo tham chiếu để tránh vấn đề này.

```cpp
#include <iostream>
using namespace std;

int* safeFunction() {
    int* heapVar = new int(50);  // Allocate memory on the heap
    return heapVar;              // Return valid pointer
}

void avoidReturningLocalVariable() {
    int* ptr = safeFunction();
    cout << "Valid pointer value: " << *ptr << endl;
    delete ptr;  // Free allocated memory
}
```
!!! warning "Kết Luận"
    Không bao giờ trả về địa chỉ của biến cục bộ từ một hàm, vì các biến cục bộ sẽ bị hủy khi phạm vi hàm kết thúc. Thay vào đó, hãy sử dụng phân bổ vùng heap hoặc tham chiếu để duy trì tính hợp lệ.

### 4.4 Use Static Analysis Tools

Các công cụ phân tích tĩnh giúp xác định các vấn đề liên quan đến bộ nhớ như con trỏ lơ lửng trong giai đoạn phát triển. Những công cụ này có thể xác định chính xác nơi xảy ra truy cập bộ nhớ không hợp lệ, cho phép bạn khắc phục sự cố trước khi chạy chương trình.

Dưới đây là một số công cụ phổ biến:

1. __Valgrind__: Phát hiện rò rỉ bộ nhớ và truy cập bộ nhớ không hợp lệ
    ```bash
    valgrind ./program
    ```
2. __AddressSanitizer__: Biên dịch mã có bật tính năng kiểm tra bộ nhớ.
    ```bash
    g++ -fsanitize=address -g program.cpp -o program ./program
    ```

!!! warning "Kết Luận"
    Thường xuyên chạy các công cụ như __*Valgrind*__ hoặc __*AddressSanitizer*__ để xác định và giải quyết các vấn đề về con trỏ lơ lửng trong quá trình phát triển. Những công cụ này có thể xác định chính xác các vấn đề khó phát hiện.

## Conclusion

Hiểu con trỏ lơ lửng là gì và rủi ro của nó là rất quan trọng để phát triển các ứng dụng mạnh mẽ. Bằng cách áp dụng các kỹ thuật quản lý bộ nhớ hiện đại trong C++, chẳng hạn như con trỏ thông minh và bằng cách làm theo các phương pháp hay nhất, các nhà phát triển có thể khắc phục một cách hiệu quả các vấn đề về con trỏ lơ lửng. Hãy nhớ rằng, quản lý con trỏ sạch sẽ và an toàn không chỉ đảm bảo tính ổn định của chương trình mà còn bảo vệ khỏi các lỗ hổng tiềm ẩn.

## Tham Khảo

- [[stackoverflow] What is a dangling pointer?](https://stackoverflow.com/questions/17997228/what-is-a-dangling-pointer)
- [[medium.com] What is a Dangling Pointer? How Can It Be Avoided?](https://medium.com/@sofiasondh/what-is-a-dangling-pointer-how-can-it-be-avoided-e72321e1fdf3)