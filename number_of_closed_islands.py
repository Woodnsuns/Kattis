class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1 or grid[i][j] == 2:
                return True
            
            grid[i][j] = 2
            u, d, l, r = dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1)
            return u and d and l and r
        
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j]==0 and dfs(i,j):
                    count += 1
        return count
        