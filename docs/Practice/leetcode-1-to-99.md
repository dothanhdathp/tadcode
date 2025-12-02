# \[Leetcode\] 1 To 99

## 1. Two Sum

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        for(int i{0};i<nums.size();++i)
        {
            auto it = umap.find(nums[i]);
            if(it!=umap.end())
            {
                return {i, it->second};
            } else {
                umap[target-nums[i]]=i;
            }
        }
        return {};
    }
};
```

## 2. Add Two Numbers

### 2.1 Mô Tả

Bài này không nhảm, bài này rất rất hay

### 2.2 My Solotion

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        ListNode* zero = new ListNode(0);
        ListNode* p = ans;
        int rem{0};
        for(;;)
        {
            int va  = l1->val;
            va += l2->val;
            va += rem;
            rem = va/10;
            p->val = va%10;
            if(l1->next!=nullptr || l2->next!=nullptr)
            {
                l1 = l1->next==nullptr ? zero : l1->next;
                l2 = l2->next==nullptr ? zero : l2->next;
                p->next = new ListNode();
                p = p->next;
            } else {
                if(rem!=0) p->next = new ListNode(rem);
                break;
            }
        }
        delete zero;
        return ans;
    }
};
```

### 2.3 Fastest Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy=new ListNode(0);
        ListNode* cur=dummy;
        int car=0;

        while(l1 || l2){
            int num=car;
            if(l1==NULL){
                num+=l2->val;
            }
            else if(l2==NULL){
                num+=l1->val;
            }
            else{
                num+=l1->val + l2->val;
            }
            ListNode* digit = new ListNode(num%10);
            car=num/10;
            cur->next=digit;
            cur=cur->next;
            if(l1!=NULL) l1=l1->next;
            if(l2!=NULL) l2=l2->next;
        }

        if(car!=0){
            cur->next= new ListNode(car);
        }

        return dummy->next;
    }
};
```

## 3. Longest Substring Without Repeating Characters

!!! warning "Warning"
    Tiết kiệm bộ nhớ chứ tốc độ thì như hạch

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length()<2) return s.length();
        unordered_map<char, bool> mmap;
        int temp = 1;
        int ans = 1;
        mmap[s[0]]=true;
        for(int i{1};i<s.length();++i) {
            if(s[i]==s[i-temp]) {
                continue;
            } else {
                if(mmap[s[i]]) {
                    temp=1;
                    mmap.clear();
                    mmap[s[i]]=true;
                    for(int j=1;j<ans;++j) {
                        if(s[i]==s[i-j]) break;
                        mmap[s[i-j]]=true;
                        ++temp;
                    }
                } else {
                    ++temp;
                    mmap[s[i]]=true;
                    ans = max(temp, ans);
                }
            }
        }
        return ans;
    }
};
```
## 11. Container With Most Water

### 11.1 Overview

Bài này có hai phương pháp, kết quả đem lại lại khác nhau rõ rệt. Mình muốn biết tại sao và làm thế nào mà tốc độ có thể khác biệt lớn đến như này.

|            | Language | Runtime | Memory |
| :--------- | :------: | :-----: | :----: |
| Solution 1 |   Cpp    |  5.69%  | 99.97% |
| Solution 2 |   Java   | 96.29%  | 99.97% |

### 11.2 Solution 1

```cpp
class Solution {
public:
    int maxArea(vector<int>& H) {
        int Ans = (H.size()-1)*min(H[0],H[H.size()-1]);
        for(int i{0}; i < H.size(); ++i) {
            if(H[i]==0) continue;
            int diff = Ans/H[i];
            while(i-diff>0) {
                Ans = max(Ans,diff*min(H[i-diff],H[i]));
                ++diff;
            }
            while(i+diff<H.size()) {
                Ans = max(Ans,diff*min(H[i+diff],H[i]));
                ++diff;
            }
        }
        return Ans;
    }
};
```

### 11.2 Solution 2

```java
class Solution {
    public int maxArea(int[] height) {
        int first = 0;
        int last = height.length-1;
        int ans = 0;
        while(last != first)
        {
            ans = Math.max((last-first)*Math.min(height[first], height[last]), ans);
            if(height[first] < height[last])
            {
                ++first;
            } else {
                --last;
            }
        }
        return ans;
    }
}
```

## 37. Sudoku Solver

### 37.1 Lịch sử

Bắt đầu từ một câu đố trên [https://leetcode.com/problems/sudoku-solver/](https://leetcode.com/problems/sudoku-solver/). Ngồi mày mò cách giải nhưng không thành công, ít nhất là mình cũng có thể giải được mấy bảng sudoku đơn giản.

### 37.2 Mã nguồn

```cpp title="main.cpp"
#include "stdio.h"
#include <algorithm>
#include <iostream>
#include <chrono>
#include <fstream>
#include <string>
#include <bitset>
#include <vector>

using namespace std;

#define _1_ (000000001b)
#define _2_ (000000010b)
#define _3_ (000000100b)
#define _4_ (000001000b)
#define _5_ (000010000b)
#define _6_ (000100000b)
#define _7_ (001000000b)
#define _8_ (010000000b)
#define _9_ (100000000b)

// Export function

const std::vector<std::vector<int>> id_row = {
    { 0, 1, 2, 3, 4, 5, 6, 7, 8},
    { 9,10,11,12,13,14,15,16,17},
    {18,19,20,21,22,23,24,25,26},
    {27,28,29,30,31,32,33,34,35},
    {36,37,38,39,40,41,42,43,44},
    {45,46,47,48,49,50,51,52,53},
    {54,55,56,57,58,59,60,61,62},
    {63,64,65,66,67,68,69,70,71},
    {72,73,74,75,76,77,78,79,80}
};
const std::vector<std::vector<int>> id_col {
    { 0, 9,18,27,36,45,54,63,72},
    { 1,10,19,28,37,46,55,64,73},
    { 2,11,20,29,38,47,56,65,74},
    { 3,12,21,30,39,48,57,66,75},
    { 4,13,22,31,40,49,58,67,76},
    { 5,14,23,32,41,50,59,68,77},
    { 6,15,24,33,42,51,60,69,78},
    { 7,16,25,34,43,52,61,70,79},
    { 8,17,26,35,44,53,62,71,80}
};
const std::vector<std::vector<int>> id_box {
    { 0, 1, 2, 9,10,11,18,19,20},
    { 3, 4, 5,12,13,14,21,22,23},
    { 6, 7, 8,15,16,17,24,25,26},
    {27,28,29,36,37,38,45,46,47},
    {30,31,32,39,40,41,48,49,50},
    {33,34,35,42,43,44,51,52,53},
    {54,55,56,63,64,65,72,73,74},
    {57,58,59,66,67,68,75,76,77},
    {60,61,62,69,70,71,78,79,80},
};

template<typename T>
void print_2d_vector(std::vector<std::vector<T>> &board, const char* prompt) {
    for(std::vector<T> V : board) {
        for(T v : V) {
            printf(prompt, v);
        }
        printf("\n");
    }
}

void solveSudoku(vector<vector<char>>& board) {
    std::vector<std::bitset<9>> data;
    std::vector<int> marker;

    // Fill data
    for(auto v : board) {
        for(auto c : v) {
            switch (c)
            {
                case '1': data.push_back(std::bitset<9>(0b000000001)); marker.push_back(1);  break;
                case '2': data.push_back(std::bitset<9>(0b000000010)); marker.push_back(1);  break;
                case '3': data.push_back(std::bitset<9>(0b000000100)); marker.push_back(1);  break;
                case '4': data.push_back(std::bitset<9>(0b000001000)); marker.push_back(1);  break;
                case '5': data.push_back(std::bitset<9>(0b000010000)); marker.push_back(1);  break;
                case '6': data.push_back(std::bitset<9>(0b000100000)); marker.push_back(1);  break;
                case '7': data.push_back(std::bitset<9>(0b001000000)); marker.push_back(1);  break;
                case '8': data.push_back(std::bitset<9>(0b010000000)); marker.push_back(1);  break;
                case '9': data.push_back(std::bitset<9>(0b100000000)); marker.push_back(1);  break;
                case '.': data.push_back(std::bitset<9>(0b111111111)); marker.push_back(10); break;
                default:
                    break;
            }
        }
    }

    bool repeat = true;
    int max_test = 1000000;
    while (repeat && --max_test)
    {
        // Fill data
        // Reach all in row
        for(int i=0; i<9; ++i) {
            std::bitset<9> rowbit(0b000000000);
            for(int j=0; j<9; ++j) {
                if(marker[id_row[i][j]] == 1) {
                    rowbit |= data[id_row[i][j]];
                }
            }
            for(int j=0; j<9; ++j) {
                if(marker[id_row[i][j]] != 1) {
                    data[id_row[i][j]] &= ~rowbit;
                }
            }
        }

        // Reach all in col
        for(int i=0; i<9; ++i) {
            std::bitset<9> colbit(0b000000000);
            for(int j=0; j<9; ++j) {
                if(marker[id_col[i][j]] == 1) {
                    colbit |= data[id_col[i][j]];
                }
            }
            for(int j=0; j<9; ++j) {
                if(marker[id_col[i][j]] != 1) {
                    data[id_col[i][j]] &= ~colbit;
                }
            }
        }

        // Reach all in box
        for(int i=0; i<9; ++i) {
            std::bitset<9> boxbit(0b000000000);;
            for(int j=0; j<9; ++j) {
                if(marker[id_box[i][j]] == 1) {
                    boxbit |= data[id_box[i][j]];
                }
            }
            for(int j=0; j<9; ++j) {
                if(marker[id_box[i][j]] != 1) {
                    data[id_box[i][j]] &= ~boxbit;
                }
            }
        }

        // Re-check map.
        repeat = false;
        for(int i=0; i<81; ++i) {
            if(1 != marker[i]) {
                if(data[i].count() == 0) {
                    printf("--- Wrong Table ---\n");
                    goto exit;
                }
                if(marker[i] != data[i].count()) {
                    marker[i] = data[i].count();
                    repeat = true;
                }
            }
        }
    }
exit:
    auto get_number_char = [](std::bitset<9> input) {
        if(std::bitset<9>(0b000000001) == input) return '1';
        if(std::bitset<9>(0b000000010) == input) return '2';
        if(std::bitset<9>(0b000000100) == input) return '3';
        if(std::bitset<9>(0b000001000) == input) return '4';
        if(std::bitset<9>(0b000010000) == input) return '5';
        if(std::bitset<9>(0b000100000) == input) return '6';
        if(std::bitset<9>(0b001000000) == input) return '7';
        if(std::bitset<9>(0b010000000) == input) return '8';
        if(std::bitset<9>(0b100000000) == input) return '9';
        return '.';
    };

    for(int i=0; i<9; ++i) {
        for(int j=0; j<9; ++j) {
            board[i][j] = get_number_char(data[i*9+j]);
        }
    }
}

int main(int argc, char const *argv[]) {
    std::vector<std::vector<char>> input;
    std::ifstream inputFile(argv[1]); // Replace with your file name

    if (!inputFile) {
        printf("Unable to open file %s", argv[1]);
        return 1; // Return with error code
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        vector<char> vc;
        for (char c : line)
        {
            if((('1'<=c)&&(c<='9'))||c=='.') 
                vc.push_back(c);
        }
        input.push_back(vc);
    }

    inputFile.close(); // Close the file
    printf("------ IN -------\n");
    print_2d_vector<char>(input, "%c ");
    printf("------ OUT ------\n");
    solveSudoku(input);
    print_2d_vector<char>(input, "%c ");

    return 0; // Return success
}
```

### 37.3 Build

```bash
g++ -std=c++11 -O2 -Wall main.cpp -o main
```

## 39. Combination Sum

> Link: https://leetcode.com/problems/combination-sum/

### 39.1 Mô tả

- Cho đầu vào là chuỗi số nguyên `candidates` và một số nguyên `target`
- Trả về tất cả tổ hợp có thể của các số trong `candidates` sao cho các số đó có tổng bằng với `target`

| candidates  | target | result                      |
| :---------- | :----: | :-------------------------- |
| `{2,3,6,7}` |  `7`   | `[[2,2,3],[7]]`             |
| `{2,3,5}`   |  `8`   | `{{2,2,2,2},{2,3,3},{3,5}}` |

- 1 <= `candidates.length` <= 30
- 2 <= `candidates[i]` <= 40
- <mark>Tẩt cả các số trong __candidates__ đều khác nhau</mark>
- 1 <= `target` <= 40

### 39.2 Giải thuật

___Backtracking___

Tư duy của mình khi giải bài này thế nào? Tưởng tượng mình <u>__là người thợ đào mỏ__</u>

- Gọi chuỗi đầu vào là tập $I={i_0, i_1, ..., i_k}$
- Trước hết, cần phải sắp xếp lại chuỗi $I$ sao cho  $i_0 < i_1 < ... < i_k$
- Đầu tiên cần tưởng tượng rằng mình __giống như người thợ đi đào mỏ__ qua từng tầng để đào vàng và cầm theo một cái túi chỉ vừa đủ ___target___:
  - Chủ nhân chỉ chấp nhận số đá có tổng là một mục tiêu (___target___ $T$) xác định.
  - Ở mỗi tầng chỉ được nhặt 1 viên đá.
  - ỗi tầng chỉ được nhặt 1 viên đá.
  - Có thể chọn nhặt đá có kích thước giống nhau ở các tầng khác nhau, nhưng cuối cùng các kết quả có tổ hợp giống nhau cần bị loại bỏ.
    - Giải thích: Nghĩa là giả sử đi qua ba tầng, đá nhặt có thứ tự lần lượt là `1,2,3` và `3,2,1` thì kết quả sẽ bị tính là giống nhau và loại bỏ. (Với mục tiêu giả định là `6`)
- Nếu mình là thợ mỏ sẽ thực hiện như sau:
  - Vì có thể nhặt lại viên đá có kích thước giống nhau nên hãy coi như mỗi tầng đá sẽ lại được phục hồi lại. Hay mỗi tầng đều có đá $I={i_0, i_1, ..., i_k}$ là như nhau.
  - Đi mỗi tầng nhặt đá, __chỉ 1 viên đá__, theo các luật sau:
    1. Đá nhặt ở mỗi tầng phải theo thứ tự từ nhỏ nhất đến lớn nhất.
    1. Nếu đá đó có thể nhặt, hãy bỏ vào giỏ và cập nhật dung lượng.
    1. __Đá có thể nhặt__ là đá mà túi có thể chứa được viên đá _(nghĩa là khi thêm viên đá đó vào túi vẫn chưa vượt quá dung tích)_.
    1. Nếu chưa đủ ___target___, hãy đi tiếp xuống tầng dưới và lặp lại, nhặt viên bé nhất.
    1. Nếu vừa đủ ___target___, hãy liệt kê và lưu lại danh sách cả số đá hiện có trong giỏ.
    1. Sử dụng `std::sort` để sắp xếp lại đá trong danh sách, việc này sẽ ___hỗ trợ loại bỏ các kết quả giống nhau___.
    1. Nếu viên đá nhặt lên ở tầng đó mà vượt quá dung tích, hãy bỏ viên đá đó và trở lại tầng trước đó.
    1. Khi quay lại tầng trước, hãy bỏ viên được nhặt ở tầng này và chọn viên đá lớn hơn tiếp theo.
    1. Lặp đi lặp lại cho đến khi bạn ở một tầng nào đó nhặt đến viên cuối cùng vẫn chưa đầy giỏ tức là đã hết trường hợp khả dĩ rồi.

### 39.3 Đáp án

```c++
struct DIGGER
{
    std::vector<int> backpack;
    int total;
    int target;
    std::vector<int> *mine;
    std::set<std::vector<int>> *report;
    std::set<int> avaible;
};


void dfs(DIGGER &digger) {
    for(size_t i=0; i < digger.mine->size(); ++i) {
        int gold = digger.mine->at(i);
        if ((digger.total + gold) == digger.target) {
            std::vector<int> package = digger.backpack;
            package.push_back(gold);
            std::sort(package.begin(), package.end());
            digger.report->insert(package);
            return;
        } else
        if ((digger.total + gold) < digger.target) {
            digger.backpack.push_back(gold);
            digger.total += gold;
            dfs(digger);
            digger.backpack.pop_back();
            digger.total -= gold;
        } else
        if ((digger.total + gold) > digger.target) {
            return;
        }
    }
}

std::vector<std::vector<int>> combinationSum(std::vector<int>& candidates, int target) {
    std::set<std::vector<int>> report;
    std::sort(candidates.begin(), candidates.end());
    DIGGER miner;
    miner.total = 0;
    miner.target = target;
    miner.mine = &candidates;
    miner.report = &report;
    dfs(miner);
    std::vector<std::vector<int>> ans(report.begin(), report.end());
    return ans;
}
```

## 46. Permutations (Hoán vị)

> - Link: [https://leetcode.com/problems/permutations/description/](https://leetcode.com/problems/permutations/description/)
> - 🌟 Bài này cực hay!

### 46.1 Mô tả

Bài này đầu vào là chuỗi `vector<int>` có giá trị khác biệt hoàn toàn. Đầu ra yêu cầu đưa ra toàn bộ tổ hợp hoán vị của chuỗi đó. Ví dụ:

```text
In:
{1,2}
Out:
{{1,2}, {2,1}}

In:
{1,2,3}
Out:
{{2,3,1}, {3,2,1},
 {1,3,2}, {3,1,2},
 {1,2,3}, {2,1,3}}
```

Với cách làm hiện tại của mình là dùng đệ quy:

```c++
vector<vector<int>> permute(vector<int> nums) {
	vector<vector<int>> ans;
	if(nums.size()==1) {
		ans.push_back(nums);
	} else if(nums.size()==2) {
		ans.push_back(nums);
		swap(nums[0],nums[1]);
		ans.push_back(nums);
	} else {
		for(int i=0; i<nums.size();++i) {
			swap(nums[0], nums[i]);
			int j = nums[0]; 
			vector<int> g(nums.begin()+1, nums.end());
			vector<vector<int>> tmp = permute(g);
			for(auto i : tmp) {
				i.push_back(j);
				ans.push_back(i);
			}
		}
	}
	return ans;
}
```

1. Trả về khi chuỗi dài 1, 2.
2. Nếu lớn hơn 1 và hai thì tách thành từng chuỗi con. Ví dụ {1,2,3} thì lần lượt đưa vào là:
	- {1} + __each_item_in__ `permute{2,3}`
	- {2} + __each_item_in__ `permute{1,3}`
	- {3} + __each_item_in__ `permute{1,2}`

Cách này siêu tệ, tốc độ và cả bộ nhớ đều tốn ở mức cao.

Hãy xem những người ở top hộ giải thế nào:

```c++
vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> ans;
    permute(nums, 0, ans);
    return ans;
}

void permute(vector<int>& nums, int k, vector<vector<int>>& ans) {
    if(k >= nums.size()) {
        ans.push_back(nums);
    }
    for(int i=k;i<nums.size(); i++) {
        swap(nums[i], nums[k]);
        permute(nums, k+1, ans);
        swap(nums[i], nums[k]);
    }
}
```

Kết quả hãy nhìn:

- `123`4
- `12`43
- `1`324
- `1`342
- `1`432
- `1`423
- ... continue ...

!!! note "Note"
	Có thấy không? Họ giữ nguyên số đầu, giữ số tiếp và ... xoay lần lượt như cái cách mình nghĩ đầu tiên nhưng không biết code thế nào.
	
	Giải thuật ở đây tên là `Backtracking`. Đây là một câu hỏi phỏng vấn thật sự. Cần nghiền ngẫm.

## 47. Permutations II

> link: [https://leetcode.com/problems/permutations-ii/description/](https://leetcode.com/problems/permutations-ii/description/)

### 47.1 Mô tả

Cho một tập hợp các số, nums, có thể chứa các số trùng lặp, trả về tất cả các hoán vị <mark>duy nhất</mark> có thể theo bất kỳ thứ tự nào.

_Khác biệt ở đây là các hoán vị không được trùng lặp._

### 47.2 Ví dụ

- __Input__: nums = [1,1,2]
- __Output__: [[1,1,2], [1,2,1], [2,1,1]]
    - Với phép hoán vị thông thường, kết quả trả về _[1, 1, 2], [1, 2, 1], __[1, 1, 2]__, __[1, 2, 1]__, [2, 1, 1], __[2, 1, 1]___ có ba giá trị trùng lặp bị loại bỏ.
    - Ở đây không được trùng lặp không được tính.

### 47.3 Bài giải

Thì ... giải thuật bài này khá là đơn giản, có kết quả loại bỏ các giá trị có giá trị giống nhau trong `ans`.

```c++
void permute(vector<int>& nums, int k, vector<vector<int>>& ans) {
    if(k >= nums.size()) {
        ans.push_back(nums);
    }
    for(int i=k;i<nums.size(); i++) {
        swap(nums[i], nums[k]);
        permute(nums, k+1, ans);
        swap(nums[i], nums[k]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> ans;
    permute(nums, 0, ans);
    std::sort(ans.begin(), ans.end());
    ans.erase(std::unique(ans.begin(), ans.end()), ans.end());
    return ans;
}
```

## 57. Insert Interval

> _Source: [https://leetcode.com/problems/insert-interval/](https://leetcode.com/problems/insert-interval/)_

### 57.1 Mô Tả

### 57.2 Giải Pháp

```cpp
#define MAXLEN 100002

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        std::bitset<MAXLEN> bits(0);
        std::stack<vector<vector<int>>::iterator> bin;

        for(int i = newInterval[0]; i <= newInterval[1]; ++i) {
            bits.set(i);
        }

        for(auto ir = intervals.begin(); ir != intervals.end(); ++ir) {
            for(int idx = (*ir)[0]; idx <= (*ir)[1]; ++idx) {
                if(bits.test(idx)) {
                    goto merged;
                }
            }
            continue;
            merged:
            bin.push(ir);
            for(int idx = (*ir)[0]; idx <= (*ir)[1]; ++idx) {
                bits.set(idx);
            }
        }
        
        // Remove each items in bin
        while (!bin.empty())
        {
            intervals.erase(bin.top());
            bin.pop();
        }
        
        // Prepare new item
        vector<int> new_item;
        for(int i = 0; i <= MAXLEN; ++i) {
            if(bits.test(i)) {
                new_item.push_back(i);
                for(int j = i+1; j <= MAXLEN; ++j) {
                    if(!bits.test(j)) {
                        new_item.push_back(j-1);
                        goto quit_double_for;
                    }
                }
            }
        }
        
        quit_double_for:
        intervals.push_back(new_item);
        std::sort(intervals.begin(), intervals.end());
        return intervals;
    }
};
```