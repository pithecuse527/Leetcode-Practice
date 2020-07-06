class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num_lst = [1]
        two, three, five = 0
        
        while len(ugly_num_lst) < n:
            while ugly[two]*2 <= ugly[-1]: two += 1
            while ugly[three]*3 <= ugly[-1]: three += 1
            while ugly[five]*5 <= ugly[-1]: five +=1
            ugly_num_lst.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
        return ugly_num_lst[-1]
    