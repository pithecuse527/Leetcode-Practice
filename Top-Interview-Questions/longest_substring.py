class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        runner = 0
        while runner < len(s) and len(s) - ans > 0:
            visited = set()
            cnt = 0
            for i in range(runner, len(s)):
                if s[i] in visited:
                    break
                cnt += 1
                visited.add(s[i])
            runner += 1
            ans = max(ans, cnt)
        return ans