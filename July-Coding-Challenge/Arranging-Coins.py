class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0: return 0
        
        row = 1
        s = 1
        
        while s <= n:
            row += 1
            s += row
        return row-1
