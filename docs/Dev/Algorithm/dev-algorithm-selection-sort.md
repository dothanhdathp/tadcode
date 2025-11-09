# Selection Sort

__Selection Sort__ là một thuật toán sắp xếp đơn giản và trực quan hoạt động bằng cách chọn liên tục các phần tử nhỏ nhất (hoặc lớn nhất, tùy thuộc vào thứ tự) từ phần chưa được phân loại của mảng và chuyển nó sang đầu (hoặc kết thúc) của phần được sắp xếp. Nó có độ phức tạp về thời gian của $(O(n^2))$, làm cho nó không hiệu quả trong các danh sách lớn, nhưng nó dễ hiểu và thực hiện.

=== "C++"
    ```cpp
    std::vector<int> v = {11,22,34,5,21,6,9,4,3,1,4,5,65};
    for(int i{0}; i<v.size(); i++) {
        for(int j{0}; j<v.size(); j++) {
            if(v[i] < v[j]) {
                std::swap(v[i], v[j]);
            }
        }
    }
    for(auto x : v) {
        std::cout << x << ' ';
    }
    return 0;
    ```