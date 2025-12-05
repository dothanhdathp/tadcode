# \[Algorithm\] Radix Sort

```c++ title="My Implement"
void radix_sort(std::vector<int> &vec, int imax)
{
    std::vector<int> vh; vh.reserve(vec.size());
    std::vector<int> vl; vl.reserve(vec.size());
    int seed = 1u;

    // Load data to deque
    while (seed < imax)
    {
        /* code */
        for(int i : vec) {
            if(i & seed) {
                vh.push_back(i);
            } else {
                vl.push_back(i);
            }   
        }
        vl.insert(vl.end(), vh.begin(), vh.end());
        vec = vl;
        vl.clear();
        vh.clear();
        seed = seed << 1;
    }
}
```