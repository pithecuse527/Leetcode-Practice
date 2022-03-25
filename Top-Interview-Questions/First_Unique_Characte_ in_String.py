class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], [])+[i]
        min_idx = 1e9
        for key, lst in hash_map.items():
            if len(hash_map[key]) == 1:
                min_idx = min(min_idx, lst[0])
        if min_idx == 1e9:
            return -1
        return min_idx
        