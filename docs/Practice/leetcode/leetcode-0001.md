# 1. Two Sum

<a href="javascript:void(0);" onclick="openSlide('http://localhost:65000/leetcode/leetcode1.html')">Xem Slide bài giảng</a>

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
            }json
        }
        return {};
    }
};
```