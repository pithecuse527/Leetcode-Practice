#!/usr/bin/python3

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if image[sr][sc] == newColor: return image
        target_color = image[sr][sc]        # get target color first
        
        self.fill(image, sr, sc, target_color, newColor)
        return image
        
    def fill(self, image, based_row: int, based_col: int, target_color: int, new_color: int):
        # more easy base case
        # if the current based pixel is not target or current based pixel is outbound the given image
        if based_row < 0 or based_row >= len(image) or based_col < 0 or based_col >= len(image[based_row]) or image[based_row][based_col] != target_color:
            return
       
        # change to new color
        image[based_row][based_col] = new_color
        
        # 1. going up
        self.fill(image, based_row-1, based_col, target_color, new_color)
        
        # 2. going down
        self.fill(image, based_row+1, based_col, target_color, new_color)
        
        # 3. going left
        self.fill(image, based_row, based_col-1, target_color, new_color)
        
        # 4. going right
        self.fill(image, based_row, based_col+1, target_color, new_color)

if __name__ == "__main__":
    sol = Solution()
    print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
