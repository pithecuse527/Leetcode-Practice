#!/usr/bin/python3

class Solution:
    def twoSum(self, nums, target):
        maps = {}
        for i in range(len(nums)):
            maps[nums[i]] = i
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in maps and maps[diff] != j:
                return [j, maps[diff]]
        return None

if __name__ == "__main__":
    Sol1 = Solution()
    print(Sol1.twoSum([2, 7, 11, 15], 9))

