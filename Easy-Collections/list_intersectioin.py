from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        # define the short one and long one
        if len(nums1) < len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1
        
        # count the number of each given int
        counter_hash = Counter(long)
        
        # subtract the number from hash with given int from short list
        for n in short:
            if n in counter_hash and counter_hash[n] > 0:
                counter_hash[n] -= 1
                answer.append(n)
        return answer
