"""
二分查找算法实现
"""


def binary_search(target_list, item):
    """有序数值列表的二分查找实现"""
    low = 0
    high = len(target_list) - 1
    while low <= high:
        # (low + high) / 2 的值为浮点数，需要转为整数
        # mid = int((low + high) / 2)
        # 通过 // 运算符获取除法的商的整数部分
        mid = (low + high) // 2
        print(mid)
        if target_list[mid] == item:
            return mid
        elif target_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None


my_list = [1, 3, 8, 10, 40, 90]

binary_search(my_list, 40)


