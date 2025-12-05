# Insertion Sort

=== "C++"
    ```cpp
    std::vector<int> v = {11,22,34,5,21,6,9,4,3,1,4,5,65,10};
    bool done = false;
    for(int i{1}; i<v.size(); i++) {
        int j = i;
        while (j--)
        {
            if(v[j] > v[j+1]) {
                std::swap(v[j], v[j+1]);
            }
        }
    }
    ```