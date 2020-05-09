#!/usr/bin/python3

class Solution:
    def rob(self, nums) -> int:     # conquer
        nums_len = len(nums)
        if nums_len == 0: return 0
        if nums_len == 1: return nums[0]
        if nums_len == 2: return max(nums)
        
        robbed_money_until = []
        robbed_money_until.append(nums[0])
        robbed_money_until.append(max(nums[0], nums[1]))
        
        for i in range(2, nums_len):
            # if the i'th house money plus the amount of the money until i-2'th money is bigger, rob the i'th house,
            # but if the amount of the money robbed until i-1'th house is bigger, then not to choose to rob
            robbed_money_until.append(max(nums[i] + robbed_money_until[i-2], robbed_money_until[i-1]))
        return  robbed_money_until[len(robbed_money_until) - 1]
        
# if __name__ == "__main__":
test_lst1 = [200,234,182,111,87,194,221,217,71,162,140,51,81,80,232,193,223,103,139,103]
sol1 = Solution()
print(sol1.rob(test_lst1))
