#!/usr/bin/python3

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left = 0
        right = num // 2
        
        while not left > right:
            mid = (left + right) // 2
            mid_square = mid * mid
            if num == mid_square: return True
            elif num > mid_square:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # def binSearch(self, num: int, left: int, right: int):
    #     if left > right: return False
        
    #     mid = (left + right) // 2
    #     mid_square = mid * mid
        
    #     if num == mid_square: return mid
    #     elif num > mid_square: return self.binSearch(num, mid + 1, right)
    #     else: return self.binSearch(num, left, mid - 1)

if __name__ == "__main__":
    sol1 = Solution()
    print(1 if sol1.isPerfectSquare(16) else 2)
    