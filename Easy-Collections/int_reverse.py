class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        y = abs(x)
        
        while y > 0:
            popped = y % 10  # pop the last int
            y //= 10
            rev = rev * 10 + popped

            if rev > 2**31:  # overflow
                return 0
        
        if x > 0:
            return rev
        else:
            return -rev
            