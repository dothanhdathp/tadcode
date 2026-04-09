# 46. Permutations (Hoán vị)

> - Link: [https://leetcode.com/problems/permutations/description/](https://leetcode.com/problems/permutations/description/)
> - 🌟 Bài này cực hay!

### 46.1 Mô tả

Bài này đầu vào là chuỗi `vector<int>` có giá trị khác biệt hoàn toàn. Đầu ra yêu cầu đưa ra toàn bộ tổ hợp hoán vị của chuỗi đó. Ví dụ:

{% raw %}
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
{% endraw %}

Với cách làm hiện tại của mình là dùng đệ quy:

{% raw %}
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
{% endraw %}

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