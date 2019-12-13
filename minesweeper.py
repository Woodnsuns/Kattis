class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        adjs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        def bfs(i, j, board):
            queue = [(i, j)]
            while queue:
                next = queue.pop(0)
                mc = 0
                if not visited[next[0]][next[1]]:
                    visited[next[0]][next[1]] = 1
                    if board[next[0]][next[1]] == 'E':
                        board[next[0]][next[1]] = 'B'
                    if board[next[0]][next[1]] == 'M':
                        continue
                    for adj in adjs:
                        adji = adj[0] + next[0]
                        adjj = adj[1] + next[1]
                        
                        if adji >= 0 and adjj >= 0 and adji <= len(board)-1 and adjj <= (len(board[0]))-1:
                            if board[adji][adjj] == 'M':
                                mc += 1
                    if mc == 0:
                        for adj in adjs:
                            adji = adj[0] + next[0]
                            adjj = adj[1] + next[1]

                            if adji >= 0 and adjj >= 0 and adji <= len(board)-1 and adjj <= (len(board[0]))-1:
                                if not visited[adji][adjj]:
                                    queue.append((adji, adjj))
                    else:
                        board[next[0]][next[1]] = str(mc)
            
                                
                            
                            
                    
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        bfs(click[0], click[1], board)
        return board
            
            
                    
                    