#!/usr/bin/python3

class Solution:
    def rob(self, nums) -> int:     # conquer
        nums_len = len(nums)
        res_max = 0
        
        # use i as the middle point for the dividing at the first time
        # calculate left, right and then pass those var to the divide() method
        # wait for the result and conquer
        for i in range(nums_len):
            left_max = 0
            right_max = 0
            if self.canGiveLeft(nums, i): left_max = self.divide(nums[:i-1])
            if self.canGiveRight(nums, i): right_max = self.divide(nums[i+2:])
            
            current_max = left_max + right_max + nums[i]
            
            if res_max < current_max: res_max = current_max
            
        return res_max
    
    def divide(self, nums):    # divide
        #until...
        if not len(nums): return 0
        if len(nums) == 1: return nums[0]
        
        max_idx = nums.index(max(nums))     # this will be the standard
        left_max = 0
        right_max = 0
        
        if self.canGiveLeft(nums, max_idx): left_max = self.divide(nums[:max_idx-1])
        if self.canGiveRight(nums, max_idx): right_max = self.divide(nums[max_idx+2:])
        return nums[max_idx] + left_max + right_max

    def canGiveLeft(self, nums, mid_idx):
        return True if not (mid_idx == 0 or mid_idx == 1) else False
    
    def canGiveRight(self, nums, mid_idx):
        return True if not (mid_idx == len(nums) - 1 or mid_idx == len(nums) - 2) else False
        
# if __name__ == "__main__":
test_lst1 = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
sol1 = Solution()
print(sol1.rob(test_lst1), tmp_lst)
