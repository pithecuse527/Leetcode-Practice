class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for i in range(9):
            hash_map = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in hash_map:
                        return False
                
                    hash_map.add(board[i][j])
        
        # col check
        for i in range(9):
            hash_map = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in hash_map:
                        return False
                    hash_map.add(board[j][i])
        
        # 3 x 3 check
        for i in range(0, 9, 3):        # i and j incides are the upper-left corner points
            for j in range(0, 9, 3):    # of each 3x3 square
                hash_map = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != ".":
                            if board[k][l] in hash_map:
                                return False
                            hash_map.add(board[k][l])
        return True
