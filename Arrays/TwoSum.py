
# url = "problem"
# for count in range(72,76):
#     print(url + str(count) + " -" + "\n")
import time
import timeit

def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def TwoSum(nums, target):
    PrevMap = {}
    for i, num in enumerate(nums):
        if target - num in PrevMap:
            return [PrevMap[target - num], i]
        PrevMap[num] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(twosum(nums, target))
    print(TwoSum(nums, target))

print(timeit.timeit("twosum([2,7,11,15], 9)", setup="from __main__ import twosum", number=1000000))
print(timeit.timeit("TwoSum([2,7,11,15], 9)", setup="from __main__ import TwoSum", number=1000000))