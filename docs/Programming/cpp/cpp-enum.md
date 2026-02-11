# Enum

> Giống với ngôn ngữ [\[C Enum\]](/Programming/c/c-enum/)

__Enum__ là dạng một vùng nhớ nhiều dữ liệu dạng __interger__. Nó chỉ có một tác dụng là định nghĩa dạng __*const*__, gán cho số một cái tên nào đó để định danh.

Ví dụ một dạng định danh đơn giản sau:

```cpp
#include <iostream>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

enum e_music_state {
    STATE_IDLE,
    STATE_PLAY,
    STATE_PAUSE,
    STATE_STOP,
    STATE_FAST_FORWARD,
    STATE_FAST_REWIND,
    STATE_MAX
};

int main() {
    println("STATE_IDLE         : ", STATE_IDLE);
    println("STATE_PLAY         : ", STATE_PLAY);
    println("STATE_PAUSE        : ", STATE_PAUSE);
    println("STATE_STOP         : ", STATE_STOP);
    println("STATE_FAST_FORWARD : ", STATE_FAST_FORWARD);
    println("STATE_FAST_REWIND  : ", STATE_FAST_REWIND);
    println("STATE_MAX          : ", STATE_MAX);
    return 0;
}
```
```text title="Kết Quả"
STATE_IDLE         : 0
STATE_PLAY         : 1
STATE_PAUSE        : 2
STATE_STOP         : 3
STATE_FAST_FORWARD : 4
STATE_FAST_REWIND  : 5
STATE_MAX          : 6
```

Nếu các giá trị không có định nghĩa đặc biệt thì nó sẽ tự động chạy liên tục từ `0`.

Nhưng trong môi trường thực tế thì thường không như vậy. Nếu __*enum*__ chỉ có tác dụng vậy thì thật sự là tính năng vớ vẩn. Cái hay của nó chính là gán ý nghĩa cho một giá trị. Giá trị đó sẽ mặc định được thay bằng số nguyên. Và nó chấp nhận các kiểu biển diễn khác nhau của số, ví dụ như sau:

```cpp
#include <iostream>

template <typename... Args>
void println(Args... args) {
    (std::cout << ... << args) << std::endl;
}

enum e_music_state {
    STATE_IDLE         = 0x00000001,
    STATE_PLAY         = 0x00000010,
    STATE_PAUSE        = 0x00000100,
    STATE_STOP         = 0x00001000,
    STATE_FAST_FORWARD = 0x00010000,
    STATE_FAST_REWIND  = 0x00100000,
    STATE_MAX          = 0xFFFFFFFF
};

int main() {
    println("STATE_IDLE         : ", STATE_IDLE);
    println("STATE_PLAY         : ", STATE_PLAY);
    println("STATE_PAUSE        : ", STATE_PAUSE);
    println("STATE_STOP         : ", STATE_STOP);
    println("STATE_FAST_FORWARD : ", STATE_FAST_FORWARD);
    println("STATE_FAST_REWIND  : ", STATE_FAST_REWIND);
    println("STATE_MAX          : ", STATE_MAX);

    int state_play_and_pause = (STATE_PLAY|STATE_PAUSE);
    if(state_play_and_pause & STATE_PLAY)
        println("Have state Play");
    if(state_play_and_pause & STATE_PAUSE)
        println("Have state Pause");
    return 0;
}
```
```text title="Kết Quả"
STATE_IDLE         : 1
STATE_PLAY         : 16
STATE_PAUSE        : 256
STATE_STOP         : 4096
STATE_FAST_FORWARD : 65536
STATE_FAST_REWIND  : 1048576
STATE_MAX          : -1
Have state Play
Have state Pause
```

Nhờ thế mà có thể định nghĩa lại các giá trị để xác định các trạng thái chồng chập.

Điểm thú vị là nó sử dụng trong quá trình biên dịch không ảnh hưởng đến chương trình. Tức là nếu bạn sử dụng một số __*enum*__ trong mã thì sau khi thành mã máy nó sẽ trực tiếp được thay đổi thành số nguyên trực tiếp.