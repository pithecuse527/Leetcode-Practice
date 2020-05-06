#!/usr/bin/python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_maps = {}
        majority_num = len(nums) // 2
        
        for num in nums:
            if num not in num_maps:
                num_maps[num] = 1
            else:
                num_maps[num] += 1
                
        max_majority_num = 0
        for num in num_maps:
            if num_maps[num] > majority_num and num_maps[num] >= max_majority_num:
                max_majority_num = num
        
        return max_majority_num
    