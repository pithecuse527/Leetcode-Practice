#!/usr/bin/python3

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        
        for stone in S:
            if stone in J:
                cnt += 1
        
        return cnt
        
    def numJewelsInStones2(self, J: str, S: str) -> int:
        cnt = 0
        stone_map = self.returnMap(S)
        
        for key in J:
            if key in stone_map:
                cnt += stone_map[key]
        return cnt
            
    def returnMap(self, lst):
        maps = {}
        
        for e in lst:
            if not e in maps:
                maps[e] = 1
            else:
                maps[e] += 1
                
        return maps
