class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def can_place(row, col):
            return not(cols[col] + toleft[row + col] + toright[row - col])
        def place_queen(row, col):
            cols[col] = 1
            toleft[row + col] = 1
            toright[row - col] = 1
            queens.add((row, col))
        def remove_queen(row, col):
            cols[col] = 0
            toleft[row + col] = 0
            toright[row - col] = 0
            queens.remove((row, col))
        def add_solution():
            solution = []
            for row, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n - col - 1))
            output.append(solution)
            
        def backtrack(row):
            for col in range(n):
                if can_place(row, col):
                    place_queen(row, col)
                    if row == n - 1:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)
                      
                        
        cols = [0] * n
        toleft = [0] * (2*n - 1)
        toright = [0] * (2*n - 1)
        queens = set()
        output = []
        backtrack(0)
        return output

        