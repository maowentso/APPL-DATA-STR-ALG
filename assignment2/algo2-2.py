import re
import ast

##Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
##Output: true

##Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
##Output: false


s = input("test case:")
matrix = ast.literal_eval(re.search(r"matrix\s*=\s*(\[.*\])", s).group(1))
target = int(re.search(r"target\s*=\s*(-?\d+)", s).group(1))

print(matrix)
print(target)

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(searchMatrix(matrix,target))