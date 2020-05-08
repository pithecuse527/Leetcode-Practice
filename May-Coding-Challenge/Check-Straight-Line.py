#!/usr/bin/python3

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = None    # inclination for y=ax+b form
        b = None    # y intercept for y=ax+b form
        x_diff = None
        y_diff = None
        
        for i in range(len(coordinates) - 1):
            x_diff = coordinates[i][0] - coordinates[i+1][0]
            y_diff = coordinates[i][1] - coordinates[i+1][1]
            
            if not x_diff: continue
            a = y_diff / x_diff
            b = coordinates[i][1] - a*coordinates[i][0]
            break
        if not x_diff: return True     # which means vertical
        
        for i in range(len(coordinates)):
            if coordinates[i][1] != (a*coordinates[i][0] + b):
                return False
        return True
