import copy


def heap_sort(array, compare=lambda x, y: x > y):
    """
    Best: O(n log n)
    Worst: O(n log n)
    Avg: O(n log n)
    @param array the array to be compare
    @param compare the comparing function
    @return the sorted array
    """
    def heapify(a, idx, max_len):
        left = idx * 2 + 1
        right = idx * 2 + 2

        if left < max_len and compare(a[left], a[idx]):
            largest = left
        else:
            largest = idx

        if right < max_len and compare(a[right], a[largest]):
            largest = right

        if largest != idx:
            temp = a[idx]
            a[idx] = a[largest]
            a[largest] = temp
            heapify(a, largest, max_len)

    def build_heap(a):
        n = len(a)
        for i in range(n / 2 - 1, -1, -1):
            heapify(a, i, n)

    array_copy = copy.deepcopy(array)

    build_heap(array_copy)

    n = len(array_copy)

    for i in range(n - 1, 0, -1):
        temp = array_copy[0]
        array_copy[0] = array_copy[i]
        array_copy[i] = temp
        heapify(array_copy, 0, i)

    return array_copy


def merge_sort(array, compare=lambda x, y: x > y):
    array_copy = copy.deepcopy(array)
    n = len(array_copy)

    if n <= 1:
        return array_copy
    if n == 2:
        if compare(array_copy[0], array_copy[1]):
            temp = array_copy[0]
            array_copy[0] = array_copy[1]
            array_copy[1] = temp
        return array_copy

    def merge(a, left, right):
        i = 0  # left index
        j = 0  # right index
        k = 0  # array index

        left_len = len(left)
        right_len = len(right)

        while i < left_len and j < right_len:
            if not compare(left[i], right[j]):
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1

            k += 1

        while i < left_len:
            a[k] = left[i]
            i += 1
            k += 1

        while j < right_len:
            a[k] = right[j]
            j += 1
            k += 1

    median = n / 2

    left = array_copy[0:median]
    right = array_copy[median:]

    left = merge_sort(left)
    right = merge_sort(right)
    merge(array_copy, left, right)
    return array_copy


def quick_sort(array, compare=lambda x, y: x > y):
    """
    Best: O(n log n)
    Avg: O(n log n)
    Worst: O(n^2)
    @param array: the array to be sorted
    @param compare: the comparing function
    @return: the sorted array
    """
    def partition(a, start, end):
        partition_idx = start
        pivot = a[end]

        for i in range(start, end):
            if compare(pivot, a[i]):
                temp = a[i]
                a[i] = a[partition_idx]
                a[partition_idx] = temp
                partition_idx += 1

        temp = a[partition_idx]
        a[partition_idx] = pivot
        a[end] = temp

        return partition_idx

    def sort(a, start, end):
        if start < end:
            pivot_idx = partition(a, start, end)
            sort(a, start, pivot_idx - 1)
            sort(a, pivot_idx + 1, end)

    n = len(array)
    array_copy = copy.deepcopy(array)
    sort(array_copy, 0, n - 1)
    return array_copy


def insertion_sort(array, compare=lambda x, y: x > y):
    """
    Best: O(n)
    Avg: O(n^2)
    Worst: O(n^2)
    @param array: the array to be sorted
    @param compare: the comparing function
    @return: the sorted array
    """
    array_copy = copy.deepcopy(array)

    def insert(a, pos, value):
        i = pos - 1
        while i >= 0 and compare(a[i], value):
            a[i+1] = a[i]
            i -= 1
        a[i+1] = value

    for i in range(1, len(array_copy)):
        insert(array_copy, i, array_copy[i])

    return array_copy

if __name__ == "__main__":
    array = [1, 2, 0, 4, 6, 10, 5]
    print array
    print merge_sort(array)
