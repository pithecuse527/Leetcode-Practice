from collections import deque

def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp in hash_map:
            return [i, hash_map[tmp]]
        hash_map[nums[i]] = i

print(twoSum([3,2,4], 6))
