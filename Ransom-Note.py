#!/usr/bin/python3

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = self.returnMap(magazine)
        ransomNote = list(ransomNote)
        
        while len(ransomNote):
            ransomNote_character = ransomNote.pop()
            
            if ransomNote_character in magazine_map and magazine_map[ransomNote_character] > 0:
                magazine_map[ransomNote_character] -= 1
            else:
                return False
        return True
        
    def returnMap(self, lst):
        maps = {}
        
        for e in lst:
            if not e in maps:
                maps[e] = 1
            else:
                maps[e] += 1
                
        return maps
