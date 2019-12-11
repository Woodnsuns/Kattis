class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, grid, n):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return 0
            if grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                if n == 0:
                    return 1
                else:
                    return 0
            
            grid[i][j] = -1
            result = dfs(i-1, j, grid, n-1) + dfs(i, j+1, grid, n-1) + dfs(i+1, j, grid, n-1) + dfs(i, j-1, grid, n-1)
            grid[i][j] = 0
            return result
        
        
        si = -1
        sj = -1
        n = 1
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    si = i
                    sj = j
                elif grid[i][j] == 0:
                    n += 1
   
        return dfs(si, sj, grid, n)
                