# \[Com\] Dangling Pointers

!!! success "Tham Khảo"

## 

__Con trỏ lơ lửng__ _(Dangling Pointers)_ là con trỏ trỏ tới một vị trí bộ nhớ đã được giải phóng hoặc giải phóng. Điều này xảy ra khi một chương trình không còn cần một phần bộ nhớ nữa nên nó được giải phóng nhưng con trỏ vẫn giữ địa chỉ của bộ nhớ được giải phóng đó. Việc truy cập hoặc sửa đổi dữ liệu thông qua con trỏ lơ lửng sẽ dẫn đến hành vi không xác định và có thể khiến chương trình gặp sự cố hoặc dữ liệu bị hỏng.
