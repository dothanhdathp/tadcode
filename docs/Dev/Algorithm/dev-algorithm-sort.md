# Sorting

## Overview

Tổng quan thì thuật toán này rất thú vị và có rất rất nhiều. Đi kèm với nó là thuật toán tìm kiếm và hai bộ này hợp với nhau xây dựng lên một thể chế tìm kiếm rộng khắp thế giới. Mọi mục đích chung quy lại đều là vì mục đích tìm kiếm. Trong thế giới thực, mọi loại thuật toán đều có lý do đề sắp xếp và tìm kiếm và là những tính năng cực kỳ cơ bản, nhiều loại phần mềm đều cần chúng như Excel, Google, ...

Bắt đầu với thuật toán sắp xếp là cách tốt nhất để học về thuật toán. Nếu nói ___Brute Force___ là thuật toán thì chưa hẳn, nó gần giống cách suy nghĩ hơn là thuật toán. Nói chính xác một câu đó là _cách suy nghĩ theo lối trực tiếp_ để xử lý bài toán, còn sắp xếp mới thể hiện rõ mục đích của thuật toán. Cách sắp xếp đơn giản nhất là `Selection Sort` hoặc `Bubble Sort` y hệt như cách suy nghĩ của chúng ta khi sắp xếp số. Nhưng trong thế giới phần mềm còn nhiều cách nghĩ khác có khả năng sắp xếp tốt hơn nhờ việc _tương thích tốt_ với hệ thống máy tính.

Hãy đi tìm hiểu về các loại thuật toán sắp xếp như dưới đây.

Có một sự thật rất thú vị, thay vì tìm kiếm các thuật toán sắp xếp sao cho nhanh nhất, họ lại cố gắng tìm cách để sắp xếp sao cho __chậm nhất__ hoặc __không bao giờ đạt được mục đích__.

## Các loại thuật toán sắp xếp

Phải nói là có rất rất nhiều loại thuật toán sắp xếp

| Type             | Type                 | Type                                       |
| :--------------- | :------------------- | :----------------------------------------- |
| Selection Sort   | Bingo Sort Algorithm | Pancake sorting                            |
| Bubble Sort      | ShellSort            | BogoSort or Permutation Sort               |
| Insertion Sort   | TimSort              | Gnome Sort                                 |
| Merge Sort       | Comb Sort            | Sleep Sort – The King of Laziness          |
| Quick Sort       | Pigeonhole Sort      | Structure Sorting in C++                   |
| Heap Sort        | Cycle Sort           | Stooge Sort                                |
| Counting Sort    | Cocktail Sort        | Tag Sort (To get both sorted and original) |
| Radix Sort       | Strand Sort          | Tree Sort                                  |
| Bucket Sort      | Bitonic Sort         | Odd-Even Sort / Brick Sort                 |
| 3-way Merge Sort |                      |                                            |

## So sánh các thể loại sắp xếp

| Sorting Algorithm | Average Case  |   Best Case   |  Worst Case   | Note |
| :---------------- | :-----------: | :-----------: | :-----------: | :--: |
| Bubble Sort       |   $O(n^2)$    |    $O(n)$     |   $O(n^2)$    |      |
| Insertion Sort    |   $O(n^2)$    |    $O(n)$     |   $O(n^2)$    |      |
| Selection Sort    |   $O(n^2)$    |   $O(n^2)$    |   $O(n^2)$    |      |
| Quick Sort        | $O(n.log(n))$ | $O(n.log(n))$ |   $O(n^2)$    |      |
| Merge Sort        | $O(n.log(n))$ | $O(n.log(n))$ | $O(n.log(n))$ |      |
| Heap Sort         | $O(n.log(n))$ | $O(n.log(n))$ | $O(n.log(n))$ |      |
| Counting Sort     |   $O(n+k)$    |   $O(n+k)$    |   $O(n+k)$    |      |
| Radix Sort        |   $O(n*k)$    |   $O(n*k)$    |   $O(n*k)$    |      |
| Bucket Sort       |   $O(n+k)$    |   $O(n+k)$    |   $O(n^2)$    |      |