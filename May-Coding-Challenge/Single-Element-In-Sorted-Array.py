#!/usr/bin/python3

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        
        # base case
        if len_of_nums % 2 == 0: return False
        if len_of_nums == 1: return nums[0]
        
        # if not a base case,
        for i in range(0, len_of_nums // 2 + 1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
            if nums[len_of_nums-i-1] != nums[len_of_nums-i-2]:
                return nums[len_of_nums-i-1]
