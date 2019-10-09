"""
创建空列表的两种方式
"""

# 方式1
arr = [None] * 5
print(arr)

# 方式2
arr = [None for _ in range(5)]
print(arr)
