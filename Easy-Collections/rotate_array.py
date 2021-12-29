class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # with O(1) space complexity
        for i in range(k):
            nums.insert(0, nums.pop())
