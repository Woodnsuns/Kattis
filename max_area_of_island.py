class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        def dfs(i, j, grid):
            area = 0
            stack = list()
            stack.append((i, j))
            while stack:
                cell = stack.pop()
                i = cell[0]
                j = cell[1]
                if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                    continue
                if not visited[i][j]:
                    visited[i][j] = 1
                else:
                    continue
                if grid[i][j] == 1:
                    area += 1
                    grid[i][j] = 0
                    for neighbor in {(i-1, j), (i, j+1), (i+1, j), (i, j-1)}:
                        stack.append(neighbor)
            return area
        
        maxarea = 0
        if len(grid) == 0:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print ("i = {}, j = {}".format(i, j))
                if visited[i][j]:
                    continue
                else:
                    maxarea = max(maxarea, dfs(i, j, grid))
        return maxarea
                        
                    
                    
                
                    

                
        