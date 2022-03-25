class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ''
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                s_new += c
        l, r = 0, len(s_new)-1
        while l <= r:
            if s_new[l] != s_new[r]:
                return False
            l += 1
            r -= 1
        
        return True
