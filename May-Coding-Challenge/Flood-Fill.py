#!/usr/bin/python3

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        target_color = image[sr][sc]        # get target color first
        
        self.walker(image, sr, sc, target_color, newColor)
        return image
        
    def walker(self, image, based_row: int, based_col: int, target_color: int, new_color: int):
        # first base case (if the walker no needs to change the color, go back)
        if image[based_row][based_col] != target_color: return
    
        image[based_row][based_col] = new_color
        
        #========== more base cases ==========#
        
        # going up and down need more conditions as it may not holds enough cols
        # walker should not visit again to where walker comes from
        
        # 1. if walker can go up, then go ahead
        if based_row - 1 >= 0 and len(image[based_row-1]) > based_col:
            if image[based_row-1][based_col] != new_color:  # walker should not go up more than once
                self.walker(image, based_row-1, based_col, target_color, new_color)
            
        # 2. if walker can go down, then go ahead
        if based_row + 1 < len(image) and len(image[based_row+1]) > based_col:
            if image[based_row+1][based_col] != new_color:  # walker should not go down more than once
                self.walker(image, based_row+1, based_col, target_color, new_color)
            
        # 3. if walker can go left, then go ahead
        if based_col - 1 >= 0:
            if image[based_row][based_col-1] != new_color:  # walker should not go left more than once
                self.walker(image, based_row, based_col-1, target_color, new_color)
        
        # 4. if walker can go right, then go ahead
        if based_col + 1 < len(image[based_row]):
            if image[based_row][based_col+1] != new_color:  # walker should not go right more than once
                self.walker(image, based_row, based_col+1, target_color, new_color)
                
        #=================================#
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
