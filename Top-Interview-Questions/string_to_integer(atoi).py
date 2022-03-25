class Solution:
    def myAtoi(self, s: str) -> int:
        # step1
        s = list(s.strip())
        if not s:
            return 0
        
        # step2
        neg = False
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                neg = True
            s.pop(0)
        if not s or not ('0' <= s[0] <= '9'):
            return 0
            
        en = 0
        while True:
            if en >= len(s) or not('0' <= s[en] <= '9'):
                break
            en += 1
        
        s = "".join(s[:en])
        s_float = -float(s) if neg else float(s)
        if -pow(2.0, 31) <= s_float <= pow(2.0, 31)-1:
            return int(s_float)
        else:
            return -pow(2, 31) if neg else pow(2, 31)-1