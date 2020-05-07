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
        
        # st needs to be started from index 1, 
        # otherwise there will be a problem with (mid - 1)
        st = 1          
        fin = n
        
        # using binSearch algorithm
        while st <= fin:
            mid = (st + fin) // 2
            
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid) and not isBadVersion(mid - 1):
                st = mid + 1
            else:
                fin = mid - 1
