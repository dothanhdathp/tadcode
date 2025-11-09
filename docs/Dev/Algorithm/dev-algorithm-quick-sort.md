# Quick Sort

=== "C++"
    ```c++
    int partition(std::vector<int>& arr, int low, int high)
    {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);  
        return i + 1;
    }

    void quickSort(std::vector<int>& arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    int main()
    {
        std::vector<int> v = {11,22,34,5,21,6,9,4,3,1,4,5,65,10};
        quickSort(v, 0, v.size()-1);
        for(auto x : v) {
            std::cout << x << ' ';
        }
        return 0;
    }
    ```