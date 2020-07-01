class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1: return n
        
        # R := row
        # S1 := the maximum sum of coins up to ith rows
        # S2 := the next maximum sum right after the S1
        # find S using difference series formula
        a1 = 1  # initiate
        
        # using pigeonhole princple
        for i in range(1,n):
            S1 = a1 + ((i-1)*(i+2)) // 2
            S2 = S1 + (i+1)
            
            if n == S1: return i        # case1: if n is S1
            elif n == S2: return i+1    # case2: if n is S2
            elif n > S1 and n < S2: return i  # case3: if n is between S1 and S2
            else: continue
