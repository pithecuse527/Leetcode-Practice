#!/usr/bin/python3

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        
        for stone in S:
            if stone in J:
                cnt += 1
        
        return cnt

