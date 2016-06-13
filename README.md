#pyalo

This project implements some of popular search and sort algorithms. This is on-going project; more algorithms and improvements will be added in the future.

##Documentation

###Substring search

There are 3 substring search algorithms are currently implemented which are Knuth-Morris-Patt, Boyer More and Rabin Karp.

####Knuth-Morris-Patt algorithm
**kmp_search(text, pattern)**
Return the index of the first occurrence of the pattern in the text. If the pattern does not exist, return -1.
#####Example
```python
>>> from pyalgo import search
>>> text = "ABBAACBCB"
>>> search.kmp_search(text, "ACDCB")
4
>>> search.kmp_search(text, "EDEF")
>>> -1
```

####Rabin-karp algorithm
**rabin_karp_search(text, pattern, q=37)**
Return the index of the first occurrence of the pattern in the text. If the pattern does not exist, return -1.
q is the modular constant. Setting q to a large prime to avoid collisions. Default value of q is 37
#####Example
```python
>>> from pyalgo import search
>>> text = "ABBAACBCB"
>>> search.rabin_karp_search(text, "ACDCB")
4
>>> search.rabin_karp_search(text, "EDEF")
>>> -1
```

####Boyer-Moore algorithm
**boyer_moore_search(text, pattern)**
Return the index of the first occurrence of the pattern in the text. If the pattern does not exist, return -1.
#####Example
```python
>>> from pyalgo import search
>>> text = "ABBAACBCB"
>>> search.boyer_moore_search(text, "ACDCB")
4
>>> search.boyer_moore_search(text, "EDEF")
>>> -1
```

###Sort
There are 4 sorting algorithms are implemented: merge sort, heap sort, quick sort and insertion sort

####Heap sort
**heap_sort(array, compare=lambda x, y: x > y)**
Return the sorted array. The order depends on the compare function.
Best: O(n log n)
Worst: O(n log n)
Avg: O(n log n)
#####Example
```python
>>> from pyalgo import serial_sort
>>> array = [1, 0, 2, 4, 5, 10, 8, 6, 3, 7, 9]
>>> serial_sort.heap_sort(array)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

####Quick sort
**quick_sort(array, compare=lambda x, y: x > y)**
Return the sorted array. The order depends on the compare function.
Best: O(n log n)
Avg: O(n log n)
Worst: O(n^2)
#####Example
```python
>>> from pyalgo import serial_sort
>>> array = [1, 0, 2, 4, 5, 10, 8, 6, 3, 7, 9]
>>> serial_sort.quick_sort(array)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

####Merge sort
**merge_sort(array, compare=lambda x, y: x > y)**
Return the sorted array. The order depends on the compare function.
Best: O(n log n)
Avg: O(n log n)
Worst: O(n log n)
#####Example
```python
>>> from pyalgo import serial_sort
>>> array = [1, 0, 2, 4, 5, 10, 8, 6, 3, 7, 9]
>>> serial_sort.merge_sort(array)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

####Insertion sort
**insertion_sort(array, compare=lambda x, y: x > y)**
Return the sorted array. The order depends on the compare function.
Best: O(n)
Avg: O(n^2)
Worst: O(n^2)
#####Example
```python
>>> from pyalgo import serial_sort
>>> array = [1, 0, 2, 4, 5, 10, 8, 6, 3, 7, 9]
>>> serial_sort.insertion_sort(array)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```



