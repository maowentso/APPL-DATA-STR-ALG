##Input: nums = [4,9,10,13,17,17,19,21], target = 17
##Output: [4,5]

##Input: nums = [2,4,6,8,10,14,16], target = 12
##Output: [-1,-1]

##Input: nums = [], target = 0
##Output: [-1,-1]

import re
import ast

s = input("test case:")
nums = ast.literal_eval(re.search(r"nums\s*=\s*(\[.*?\])", s).group(1))
target = int(re.search(r"target\s*=\s*(-?\d+)", s).group(1))

print(nums)
print(target)


def findBound(flag: bool) -> int:
    left = 0
    right = len(nums) - 1
    find = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            find = mid
            if flag:
                right = mid - 1
            else:
                left = mid + 1 

        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return find
print([findBound(True), findBound(False)]) 


