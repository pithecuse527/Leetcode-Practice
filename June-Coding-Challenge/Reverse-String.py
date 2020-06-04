class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s // 2):
            s[i], s[len_s -1 - i] = s[len_s -1 - i], s[i]

sol = Solution()
str_ = ["h","e","l","l","o"]
sol.reverseString(str_)
print(str_)
