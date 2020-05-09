#!/usr/bin/python3

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # from math import ceil
        if num == 1: return True
        tmp = num // 2
        found = self.binSearch(num, 0, tmp)
        
        if found: return True
        return False
    
    def binSearch(self, num: int, left: int, right: int):
        if left > right: return False
        
        mid = (left + right) // 2
        mid_square = mid * mid
        
        if num == mid_square: return mid
        elif num > mid_square: return self.binSearch(num, mid + 1, right)
        else: return self.binSearch(num, left, mid - 1)

if __name__ == "__main__":
    sol1 = Solution()
    print(1 if sol1.isPerfectSquare(4) else 2)
    