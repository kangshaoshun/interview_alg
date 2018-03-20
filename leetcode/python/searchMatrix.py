#coding:utf-8
"""
搜索一个二维矩阵
"""
def searchMatrix(nums, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    T = O(M + N)
    """
    """
    row_num = len(nums)
    col_num = len(nums)
    i, j = 0, col_num - 1
    while j >= 0 and i <= row_num - 1:
        while j >= 0 and nums[i][j] > target:
            j -= 1
        if j >= 0 and  nums[i][j] == target:
            return True
        while i <= row_num - 1 and nums[i][j] < target:
            i += 1
        if i <= row_num - 1 and nums[i][j] == target:
            return True
    return False
    """
    """
    用二分法 T = log(n)
    """
    row = len(matrix)
    col = len(matrix[0])
    start, end = 0, row * col - 1
    while start <= end:
        mid = start + (end - start)/2
        tmp = matrix[mid/col][mid%col]
        print tmp
        if tmp == target:
            return True
        elif tmp > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

#matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
matrix = [[1], [3]]
print searchMatrix(matrix, 3)
