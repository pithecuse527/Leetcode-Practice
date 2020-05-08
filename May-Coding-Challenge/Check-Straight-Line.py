#!/usr/bin/python3

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:   
        x_diff = coordinates[0][0] - coordinates[1][0]
        y_diff = coordinates[0][1] - coordinates[1][1]
        a = 0 if not x_diff else y_diff / x_diff        # inclination for y=ax+b form
        b = coordinates[0][1] - a*coordinates[0][0]     # y intercept for y=ax+b form
        
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != (a*coordinates[i][0] + b):
                return False
        return True
