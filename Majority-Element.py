#!/usr/bin/python3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp_counter = 0         # checking the num is validate for the candidate of mojority element 
        candidate = nums[0]
        
        for num in nums:
            if num == candidate:
                tmp_counter += 1
            elif tmp_counter == 0:
                candidate = num
            else:
                tmp_counter -= 1
        
        return candidate
    