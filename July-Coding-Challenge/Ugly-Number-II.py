class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num_lst = [1]
        two = three = five = 0        # track where to multiply
        
        while len(ugly_num_lst) < n:
            while ugly_num_lst[two]*2 <= ugly_num_lst[-1]: two += 1
            while ugly_num_lst[three]*3 <= ugly_num_lst[-1]: three += 1
            while ugly_num_lst[five]*5 <= ugly_num_lst[-1]: five +=1
            ugly_num_lst.append(min(ugly_num_lst[two]*2, ugly_num_lst[three]*3, ugly_num_lst[five]*5))  # use the minimun number to append
        return ugly_num_lst[-1]
    