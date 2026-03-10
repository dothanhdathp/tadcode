# STD nhiều bộ

Là tập hợp các phần tử **có sắp xếp** nhưng mà không cần phải duy nhất như [std::set](cpp-std-set.md). Có thể nó coi như một `std::vector` nhưng luôn được sắp xếp. Thùng chứa này giúp giảm thời gian thêm mới phần tử vào chuỗi đã sắp xếp.

```cpp
#include <iostream> 
#include <set> 
#include <string_view>
 
template  < typename T > 
void println ( const  std:: string_view name, const  std:: multiset < T > & ms ) 
{ 
    std:: cout  << name <<  ": " ; 
    for  ( const  auto & element : ms ) 
        std:: cout  << element <<  ' ' ; 
    std:: cout  <<  ' \n ' ; 
}
 
int main ( ) 
{ 
    // (1) Hàm tạo mặc định 
    std:: multiset < int > a ; 
    a. insert ( 4 ) ; 
    a. insert ( 3 ) ; 
    a. insert ( 2 ) ; 
    a. insert ( 1 ) ; 
    println ( "a" , a ) ;
 
    // (4) Hàm tạo phạm vi 
    std:: multiset < int > b ( a. begin ( ) , a. find ( 3 ) ) ; 
    println ( "b" , b ) ;
 
    // (6) Hàm tạo sao chép 
    std:: multiset < int > c ( a ) ; 
    println ( "c" , c ) ;
 
    // (8) Hàm tạo di chuyển 
    std:: multiset < int > d ( std :: move ( a ) ) ; 
    println ( "d" , d ) ;
 
    // (10) Hàm tạo danh sách khởi tạo 
    std:: multiset < int > e { 3 , 2 , 1 , 2 , 4 , 7 , 3 } ; 
    println ( "e" , e ) ;
 
    // (12) Hàm tạo phạm vi 
    const  auto w =  { "α" , "β" , "γ" , "δ" , "δ" , "γ" , "β" , "α" } ; 
#if __cpp_lib_containers_ranges 
    std:: multiset < std:: string > f ( std:: from_range , w ) ;  // quá tải (12) 
#else 
    std:: multiset < std:: string > f ( w. begin ( ) , w. end ( ) ) ;  // dự phòng cho (4) 
#endif 
    println ( "f" , f ) ; 
}
```
```text title="Kết Quả"
a: 1 2 3 4
b: 1 2
c: 1 2 3 4
d: 1 2 3 4
e: 1 2 2 3 3 4 7
f: α α β β γ γ δ δ
```