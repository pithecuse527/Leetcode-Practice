#!/usr/bin/python3
import sys

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        len_of_S = len(S)
        if len_of_S <= K: return S
        
        new_key = ""
        r = len_of_S % K
        walker = 0
        
        while walker < len_of_S:
            if r:       # for first dough
                new_key += S[:r]
                new_key += '-'
                walker = r
                r = 0
                
            else:
                new_key += S[walker : walker + K]
                new_key += '-'
                walker = walker + K
                
        new_key = new_key[:-1]
        return new_key
    

if __name__ == '__main__':
    sol1 = Solution()
    print(sol1.licenseKeyFormatting("5F3ZA", 4))
