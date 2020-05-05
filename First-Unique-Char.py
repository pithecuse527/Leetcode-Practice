#!/usr/bin/python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # character_bucket = [0] * 26    # bucket
        maps = {}
        
        for c in s:
            if c not in maps:
                maps[c] = 1
            else:
                maps[c] += 1
        
        for i in range(len(s)):
            if maps[s[i]] == 1:
                return i
        return -1
