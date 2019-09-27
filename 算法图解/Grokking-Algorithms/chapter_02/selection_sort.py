"""
选择排序算法实现
"""


def selection_sort(arr):
    new_arr = []
    # while len(arr) > 0:
    for i in range(len(arr)):
        smallest_idx = find_smallest_idx(arr)
        new_arr.append(arr.pop(smallest_idx))
    return new_arr


def find_smallest_idx(arr):
    """查找数组中值最小的元素的索引"""
    idx = 0
    smallest = arr[0]
    i = 1
    length = len(arr)
    while i < length:
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i
        i = i + 1
    return idx


print(selection_sort([3, 5, 8, 2, 7, 9]))
print(selection_sort([]))
