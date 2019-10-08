"""
快速排序
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_arr = [num for num in arr[1:] if num < pivot]
        more_arr = [num for num in arr[1:] if num >= pivot]

        return quick_sort(less_arr) + [pivot] + quick_sort(more_arr)


def quick_sort2(arr, lo, hi):
    if hi > lo:
        pivot_idx = lo
        pivot = arr[pivot_idx]
        m = lo + 1
        n = hi
        while True:
            if arr[m] < pivot and m < hi:
                m = m + 1
                continue
            if arr[n] > pivot and lo < n:
                n = n - 1
                continue
            if m < n:
                tmp = arr[m]
                arr[m] = arr[n]
                arr[n] = tmp
                m = m + 1
                n = n - 1
            else:
                break

        arr[pivot_idx] = arr[n]
        arr[n] = pivot
        pivot_idx = n
        quick_sort2(arr, lo, pivot_idx - 1)
        quick_sort2(arr, pivot_idx + 1, hi)


def quick_sort3(arr, lo, hi):
    if hi > lo:
        pivot_idx = (lo + hi + 1) // 2
        pivot = arr[pivot_idx]
        m = lo
        n = hi
        while True:
            if m < hi and arr[m] < pivot:
                if m == pivot_idx - 1:
                    m = m + 2
                else:
                    m = m + 1
                continue
            if lo < n and arr[n] > pivot:
                if n == pivot_idx + 1:
                    n = n - 2
                else:
                    n = n - 1
                continue
            if m < n:
                tmp = arr[m]
                arr[m] = arr[n]
                arr[n] = tmp
                if m == pivot_idx - 1:
                    m = m + 2
                else:
                    m = m + 1
                if n == pivot_idx + 1:
                    n = n - 2
                else:
                    n = n - 1
            else:
                break
        if pivot_idx < n:
            arr[pivot_idx] = arr[n]
            arr[n] = pivot
            pivot_idx = n
        if pivot_idx > m:
            arr[pivot_idx] = arr[m]
            arr[m] = pivot
            pivot_idx = m
        quick_sort3(arr, lo, pivot_idx - 1)
        quick_sort3(arr, pivot_idx + 1, hi)


arr0 = [2, 1, 4, 8, 3, 5, 6, 2, 1, 4, 8, 3, 5, 6, 9, 4, 8, 3, 5, 7]
print(quick_sort(arr0))

arr0 = [2, 1, 4, 8, 3, 5, 6, 2, 1, 4, 8, 3, 5, 6, 9, 4, 8, 3, 5, 7]
quick_sort2(arr0, 0, len(arr0) - 1)
print(arr0)

arr0 = [2, 1, 4, 8, 3, 5, 6, 2, 1, 4, 8, 3, 5, 6, 9, 4, 8, 3, 5, 7]
quick_sort3(arr0, 0, len(arr0) - 1)
print(arr0)

