class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        toflip = list()
        if len(board) == 0:
            return board
        
                
        def should_flip(i, j, board):
            if i < 0 or j < 0 or i > len(board) - 1 or j > (len(board[0])) - 1:
                #print("i = {}, j = {}, out of boundary".format(i, j))
                return False
            if board[i][j] == 'O':
                board[i][j] = '-'
                toflip.append((i, j))
                return should_flip(i-1, j, board) and should_flip(i, j+1, board) and should_flip(i+1, j, board) and should_flip(i, j-1, board)
            else:
                return True
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                #print board
                if should_flip(i, j, board):
                    for cell in toflip:
                        board[cell[0]][cell[1]] = 'X'
                else:
                    for cell in toflip:
                        board[cell[0]][cell[1]] = 'O'
                toflip = list()
                        
                