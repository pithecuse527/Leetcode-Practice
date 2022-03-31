class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*M for _ in range(N)]
        
        flag = False
        for x in range(M):
            if not flag and obstacleGrid[0][x] == 1:
                flag = True
            dp[0][x] = 0 if flag  else 1
        flag = False
        for y in range(N):
            if not flag and obstacleGrid[y][0] == 1:
                flag = True
            dp[y][0] = 0 if flag  else 1
        
        for y in range(1, N):
            for x in range(1, M):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]
        