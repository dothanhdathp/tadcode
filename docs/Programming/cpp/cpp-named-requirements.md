# \[C++\] Named Requirements

> Tham khảo: [https://en.cppreference.com/w/cpp/iterator/concepts.html](https://en.cppreference.com/w/cpp/iterator/concepts.html)

## Định nghĩa

Các yêu cầu được đặt tên được liệt kê trên trang này là các yêu cầu được đặt tên được sử dụng trong văn bản quy chuẩn của tiêu chuẩn C++ để xác định những kỳ vọng của thư viện tiêu chuẩn.

Lập trình viên có trách nhiệm đảm bảo rằng các mẫu thư viện được khởi tạo với các đối số mẫu đáp ứng các yêu cầu này. Nếu không làm như vậy có thể dẫn đến chẩn đoán trình biên dịch rất phức tạp.

Một số yêu cầu này được chính thức hóa trong __C++20__ bằng cách sử dụng tính năng ngôn ngữ khái niệm _(concepts language)_.

## Basic

| Tên                      | Phiên bản | Ý nghĩa                                                                 |
| :----------------------- | :-------- | :---------------------------------------------------------------------- |
| __DefaultConstructible__ |           | Chỉ định rằng một đối tượng thuộc loại có thể được xây dựng mặc định    |
| __MoveConstructible__    | (C++11)   | Chỉ định rằng một đối tượng thuộc loại có thể được xây dựng từ giá trị  |
| __CopyConstructible__    |           | Chỉ định rằng một đối tượng thuộc loại có thể được xây dựng từ `lvalue` |
| __MoveAssignable__       | (C++11)   | Chỉ định rằng một đối tượng thuộc loại có thể được gán từ giá trị       |
| __CopyAssignable__       |           | Chỉ định rằng một đối tượng thuộc loại có thể được gán từ `lvalue`      |
| __Destructible__         |           | Chỉ định rằng một đối tượng thuộc loại có thể bị phá hủy                |

## Type properties

!!! note "Note"
    - Tiêu chuẩn không xác định các yêu cầu được đặt tên với các tên được chỉ định trong danh mục con này.
    - Đây là các loại loại được xác định bởi ngôn ngữ cốt lõi. Chúng được đưa vào đây dưới dạng các yêu cầu được đặt tên chỉ để đảm bảo tính nhất quán.

| Tên                      | Phiên bản                          | Ý nghĩa                                                                                                      |
| :----------------------- | :--------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| __ScalarType__           |                                    | Các kiểu đối tượng không phải là kiểu mảng hoặc kiểu lớp                                                     |
| __PODType__              | (không dùng nữa `C++20`)           | Các loại POD (Dữ liệu cũ đơn giản), tương thích với cấu trúc C                                               |
| __TriviallyCopyable__    | (C++11)                            | __Các đối tượng thuộc loại này có thể duy trì giá trị của chúng sau khi sao chép các byte cơ bản của chúng__ |
| __TrivialType__          | (C++11)(không dùng nữa từ `C++26`) | Các đối tượng thuộc loại này có thể được xây dựng và sao chép một cách tầm thường                            |
| __StandardLayoutType__   | (C++11)                            | Những loại này rất hữu ích để giao tiếp với mã được viết bằng các ngôn ngữ lập trình khác                    |
| __ImplicitLifetimeType__ |                                    | Các đối tượng thuộc loại này có thể được tạo ngầm và vòng đời của chúng có thể được bắt đầu ngầm             |
 
## Library-wide

| Tên                    | Phiên bản | Ý nghĩa                                                                                                   |
| :--------------------- | :-------- | :-------------------------------------------------------------------------------------------------------- |
| __BooleanTestable__    |           | Các toán tử __Boolean__ _(đúng sai)_ (toán tử `&&`, `|` và `!`) có ngữ nghĩa thông thường                 |
| __EqualityComparable__ |           | Toán tử `==` là một quan hệ tương đương                                                                   |
| __LessThanComparable__ |           | Toán tử `<` là quan hệ thứ tự yếu nghiêm ngặt                                                             |
| __Swappable__          |           | Có thể được hoán đổi bằng lệnh gọi hàm không phải thành viên không đủ tiêu chuẩn swap()                   |
| __ValueSwappabl__      | (C++11)   | Một LegacyIterator tham chiếu đến loại Có thể hoán đổi                                                    |
| __NullablePointer__    | (C++11)   | Kiểu giống con trỏ hỗ trợ giá trị null                                                                    |
| __Hash__               | (C++11)   | Một FunctionObject dành cho các đầu vào có giá trị khác nhau có xác suất thấp cho cùng một đầu ra         |
| __Allocator__          |           | Loại lớp chứa thông tin phân bổ                                                                           |
| __FunctionObject__     |           | Một đối tượng có thể được gọi bằng cú pháp gọi hàm                                                        |
| __Callable__           |           | Loại mà hoạt động gọi được xác định                                                                       |
| __Predicate__          |           | Một FunctionObject trả về một giá trị có thể chuyển đổi thành bool cho một đối số mà không sửa đổi nó     |
| __BinaryPredicate__    |           | Một FunctionObject trả về một giá trị có thể chuyển đổi thành bool cho hai đối số mà không sửa đổi chúng  |
| __Compare__            |           | Một BinaryPredicate thiết lập quan hệ thứ tự                                                              |

## Container

| Tên                               | Phiên bản | Ý nghĩa                                                                                      |
| :-------------------------------- | :-------- | :------------------------------------------------------------------------------------------- |
| __Container__                     |           | cấu trúc dữ liệu cho phép truy cập phần tử bằng cách sử dụng các trình vòng lặp              |
| __ReversibleContainer__           |           | thùng chứa sử dụng vòng lặp hai chiều                                                        |
| __AllocatorAwareContainer__       | (C++11)   | thùng chứa sử dụng bộ cấp phát                                                               |
| __SequenceContainer__             |           | thùng chứa các phần tử được lưu trữ tuyến tính                                               |
| __ContiguousContainer__           | (C++17)   | thùng chứa các phần tử được lưu trữ tại các địa chỉ bộ nhớ liền kề                           |
| __AssociativeContainer__          |           | thùng chứa các phần tử bằng cách liên kết chúng với các khóa                                 |
| __UnorderedAssociativeContainer__ | (C++11)   | thùng chứa lưu trữ các phần tử được lưu trữ trong nhóm bằng cách liên kết chúng với các khóa |

### Container element

| Tên                      | Phiên bản | Ý nghĩa                                                                    |
| :----------------------- | :-------- | :------------------------------------------------------------------------- |
| __DefaultInsertable__    | (C++11)   | phần tử có thể được xây dựng mặc định trong bộ lưu trữ chưa được khởi tạo  |
| __CopyInsertable__       | (C++11)   | phần tử có thể được sao chép trong bộ lưu trữ chưa được khởi tạo           |
| __MoveInsertable__       | (C++11)   | phần tử có thể được xây dựng di chuyển trong bộ lưu trữ chưa được khởi tạo |
| __EmplaceConstructible__ | (C++11)   | phần tử có thể được xây dựng trong bộ lưu trữ chưa được khởi tạo           |
| __Erasable__             | (C++11)   | phần tử có thể bị hủy bằng cách sử dụng bộ cấp phát                        |

## Iterator

| Tên                             | Phiên bản | Ý nghĩa                                                              |
| :------------------------------ | :-------- | :------------------------------------------------------------------- |
| __LegacyIterator__              |           | khái niệm chung để truy cập dữ liệu trong một số cấu trúc dữ liệu    |
| __LegacyInputIterator__         |           | iterator có thể được sử dụng để đọc dữ liệu                          |
| __LegacyOutputIterator__        |           | iterator có thể được sử dụng để ghi dữ liệu                          |
| __LegacyForwardIterator__       |           | iterator có thể được sử dụng để đọc dữ liệu nhiều lần                |
| __LegacyBidirectionalIterator__ |           | iterator có thể tăng và giảm                                         |
| __LegacyRandomAccessIterator__  |           | iterator có thể được nâng cao theo thời gian không đổi               |
| __LegacyContiguousIterator__    | (C++17)   | iterator tới các phần tử được phân bổ liền kề                        |
| __ConstexprIterator__           | (C++20)   | iterator có thể được sử dụng trong quá trình đánh giá biểu thức hằng |

## Stream I/O functions

| Tên                       | Phiên bản | Ý nghĩa                                                                                           |
| :------------------------ | :-------- | :------------------------------------------------------------------------------------------------ |
| UnformattedInputFunction  |           | Hàm nhập luồng không bỏ qua khoảng trắng ở đầu và đếm các ký tự được xử lý|
| FormattedInputFunction    |           | Chức năng nhập luồng bỏ qua khoảng trắng ở đầu|
| UnformattedOutputFunction |           | Chức năng đầu ra luồng cơ bản|
| FormattedOutputFunction   |           | Hàm đầu ra luồng đặt lỗi lỗi và trả về tham chiếu đến luồng|

## Formatters

| Tên            | Phiên bản | Ý nghĩa                                                                                 |
| :------------- | :-------- | :-------------------------------------------------------------------------------------- |
| BasicFormatter | (C++20)   | tóm tắt các hoạt động định dạng cho một kiểu đối số định dạng và kiểu ký tự nhất định |
| Formatter      | (C++20)   | định nghĩa các hàm được sử dụng bởi thư viện định dạng |

## Random Number Generation

| Tên                       | Phiên bản | Ý nghĩa                                                                             |
| :------------------------ | :-------- | :---------------------------------------------------------------------------------- |
| SeedSequence              | (C++11)   | Tiêu thụ một chuỗi các số nguyên và tạo ra một chuỗi các giá trị không dấu 32 bit   |
| UniformRandomBitGenerator | (C++11)   | Trả về các số nguyên không dấu ngẫu nhiên được phân bố đồng đều                     |
| RandomNumberEngine        | (C++11)   | Một UnityRandomBitGenerator xác định, được xác định bởi hạt giống                   |
| RandomNumberEngineAdaptor | (C++11)   | Một RandomNumberEngine biến đổi đầu ra của một RandomNumberEngine khác              |
| RandomNumberDistribution  | (C++11)   | Trả về các số ngẫu nhiên được phân phối theo hàm mật độ xác suất toán học nhất định |

## Concurrency

| Tên                 | Phiên bản | Ý nghĩa                                                                                |
| :------------------ | :-------- | :------------------------------------------------------------------------------------- |
| BasicLockable       | (C++11)   | Cung cấp ngữ nghĩa quyền sở hữu độc quyền cho các tác nhân thực thi (tức là các luồng) |
| Lockable            | (C++11)   | BasicLockable hỗ trợ việc cố gắng lấy lại khóa                                         |
| TimedLockable       | (C++11)   | Một Lockable hỗ trợ việc thu thập khóa theo thời gian                                  |
| SharedLockable      | (C++14)   | Cung cấp ngữ nghĩa quyền sở hữu chung cho các tác nhân thực thi (tức là các luồng)     |
| SharedTimedLockable | (C++14)   | Một SharedLockable hỗ trợ việc thu thập khóa theo thời gian                            |
| Mutex               | (C++11)   | Có thể khóa để bảo vệ chống lại các cuộc đua dữ liệu và đồng bộ hóa nhất quán tuần tự  |
| TimedMutex          | (C++11)   | TimedLockable bảo vệ chống lại các cuộc đua dữ liệu và đồng bộ hóa nhất quán tuần tự   |
| SharedMutex         | (C++17)   | Một Mutex hỗ trợ ngữ nghĩa quyền sở hữu chung                                          |
| SharedTimedMutex    | (C++14)   | Một TimedMutex hỗ trợ ngữ nghĩa quyền sở hữu chung                                     |

## Ranges

| Tên                       | Phiên bản | Ý nghĩa                                                                        |
| :------------------------ | :-------- | :----------------------------------------------------------------------------- |
| RangeAdaptorObject        | (C++20)   | FunctionObject tạo bộ điều hợp phạm vi từ viewable_range và các đối số bổ sung |
| RangeAdaptorClosureObject | (C++20)   | Một FunctionObject hỗ trợ toán tử đường ống                                    |

## Multidimensional View Customization

| Tên                 | Phiên bản | Ý nghĩa                                                                 |
| :------------------ | :-------- | :---------------------------------------------------------------------- |
| LayoutMapping       | (C++23)   | Kiểm soát việc ánh xạ chỉ mục đa chiều trong `mdspan`                   |
| LayoutMappingPolicy | (C++23)   | Chính sách chứa các yêu cầu về Bản đồ bố cục                            |
| AccessorPolicy      | (C++23)   | Chính sách kiểm soát quyền truy cập vào bộ xử lý dữ liệu trong `mdspan` |

## Other

| Tên                 | Phiên bản | Ý nghĩa                                                                       |
| :------------------ | :-------- | :---------------------------------------------------------------------------- |
| UnaryTypeTrait      | (C++11)   | Mô tả một thuộc tính của một loại                                             |
| BinaryTypeTrait     | (C++11)   | Mô tả mối quan hệ giữa hai loại                                               |
| TransformationTrait | (C++11)   | Sửa đổi một thuộc tính của một loại                                           |
| Clock               | (C++11)   | Tổng hợp thời lượng, điểm thời gian và hàm để có được điểm thời gian hiện tại |
| TrivialClock        | (C++11)   | Đồng hồ không đưa ra ngoại lệ                                                 |
| CharTraits          |           | Xác định các loại và chức năng cho một loại ký tự                             |
| BitmaskType         |           | Bitset, số nguyên hoặc liệt kê                                                |
| NumericType         |           | Một loại mà việc khởi tạo có hiệu quả tương đương với sự phân công            |
| RegexTraits         | (C++11)   | Xác định các loại và hàm được sử dụng bởi thư viện biểu thức chính quy        |
| LiteralType         | (C++11)   | Một loại có hàm tạo constexpr                                                 |