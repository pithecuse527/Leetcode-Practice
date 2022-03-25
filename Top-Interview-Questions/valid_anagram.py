class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
        for i in range(len(t)):
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1
        for key, val in hash_s.items():
            if key not in hash_t or val != hash_t[key]:
                return False
        return True