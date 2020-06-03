#!/usr/bin/python3

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        
        # 
        if len_of_nums % 2 == 0: return None
        if len_of_nums == 1: return nums[0]
        
        left = 0
        right = len_of_nums - 1
        mid = 0
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid-1] == nums[mid]:
                if (left + mid + 1) % 2 != 0: right = mid - 2
                else: left = mid + 1
            elif nums[mid] == nums[mid+1]:
                if (left + mid) % 2 != 0: right = mid - 1
                else: left = mid + 2
            else: return nums[mid]
            
        return nums[left]
        