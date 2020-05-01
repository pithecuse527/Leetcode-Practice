#!/usr/bin/python3

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        
        st = 0          
        fin = n - 1
        
        # using binSearch algorithm
        while st <= fin:
            mid = (st + fin) // 2
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid) and not isBadVersion(mid - 1):
                st = mid + 1
            else:
                fin = mid - 1
