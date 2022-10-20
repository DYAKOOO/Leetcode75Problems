
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

import time
import timeit
from typing import List

# def twosum(self, nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

def TwoSum(nums,target):
    PrevMap = {}
    for i, num in enumerate(nums):
        if target - num in PrevMap:
            return [PrevMap[target - num], i]
        PrevMap[num] = i

# print(timeit.timeit("twosum([2,7,11,15], 9)", setup="from __main__ import twosum", number=1000000))
# print(timeit.timeit("TwoSum([2,7,11,15], 9)", setup="from __main__ import TwoSum", number=1000000))

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(TwoSum(nums, target))
