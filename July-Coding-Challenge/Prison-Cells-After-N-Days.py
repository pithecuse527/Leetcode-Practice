class Solution:
    def movePrisoners(self, cells: List[int]) -> List[int]:
        new_cells = [None] * len(cells)
        new_cells[0], new_cells[-1] = 0, 0  # first and last cells will be vacant anyway
        for i in range(1, len(cells) - 1):
            if cells[i-1] == 0 and cells[i+1] == 0 or cells[i-1] == 1 and cells[i+1] == 1:
                new_cells[i] = 1
            else:
                new_cells[i] = 0
        return new_cells
    
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14 if N % 14 else 14        # list will be repeated after 14 times movement
        
        for i in range(N):  # less than 14 times
            cells = self.movePrisoners(cells)
        return cells
