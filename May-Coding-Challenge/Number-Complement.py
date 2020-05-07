#!/usr/bin/python3

class Solution:
    def findComplement(self, num: int) -> int:
        binary_num_str = bin(num)[2:]                   # i.e. '11001...'
        subtract_from_str = '1' * len(binary_num_str)   # i.e. '11111...'
        
        return int(subtract_from_str, 2) - num
    