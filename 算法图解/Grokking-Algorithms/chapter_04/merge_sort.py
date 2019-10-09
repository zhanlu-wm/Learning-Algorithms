"""
归并排序：二路原地归并算法
"""


def merge_sort(arr, tmp_arr, lo, hi):
    """
    执行分治递归排序以及归并逻辑的主体排序方法
    :param arr: 原始数组
    :param tmp_arr: 暂存中间归并结果的临时数组
    :param lo: 需要执行归并排序的子数组在原数组中的左边界
    :param hi: 需要执行归并排序的子数组在原数组中的右边界
    :return:
    """
    # 遇到长度小于等于1的数组时直接返回
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    merge_sort(arr, tmp_arr, lo, mid)
    merge_sort(arr, tmp_arr, mid + 1, hi)
    merge(arr, tmp_arr, lo, mid, hi)


def merge(arr, tmp_arr, lo, mid, hi):
    """
    执行归并的方法
    :param arr: 原始数组
    :param tmp_arr: 暂存中间归并结果的临时数组
    :param lo: 当前参与归并的第一个子数组在原数组中的左边界
    :param mid: 当前参与归并的第一个子数组在原数组中的右边界
    :param hi: 当前参与归并的第二个子数组在原数组中的右边界
    :return:
    """
    i = lo
    j = mid + 1
    num = lo
    while num <= hi:
        if i > mid:
            tmp_arr[num] = arr[j]
            j = j + 1
        elif j > hi:
            tmp_arr[num] = arr[i]
            i = i + 1
        elif arr[i] > arr[j]:
            tmp_arr[num] = arr[j]
            j = j + 1
        else:
            tmp_arr[num] = arr[i]
            i = i + 1
        num = num + 1
    for idx in range(lo, hi + 1):
        arr[idx] = tmp_arr[idx]


# 测试用例
arr_ = [1, 4, 2, 9, 5, 7, 3, 8, 6, 2, 9, 5, 7, 3, 0]
tmp_arr_ = [None for _ in range(len(arr_))]
merge_sort(arr_, tmp_arr_, 0, len(arr_) - 1)
print(arr_)
