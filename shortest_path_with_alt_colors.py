class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        red = 0
        blue = 1
        adjlist = [[] for i in range(n)]
        for e in red_edges:
            adjlist[e[0]].append([e[1], red])
        for e in blue_edges:
            adjlist[e[0]].append([e[1], blue])
        visited = [[0 for i in range(n)], [0 for i in range(n)]]
        result = [-1 for i in range(n)]
        result[0] = 0
        dist = [[-1 for i in range(n)], [-1 for i in range(n)]]
        dist[red][0] = 0
        dist[blue][0] = 0
        queue = [[0, red], [0, blue]]
        while queue:
            node = queue.pop(0)
            curcol = node[1]
            curval = node[0]
            if not visited[curcol][curval]:
                visited[curcol][curval] = 1
                for neighbor in adjlist[curval]:   
                    nextcol = neighbor[1]
                    nextval = neighbor[0]
                    if curcol != nextcol and dist[nextcol][nextval] == -1 or dist[curcol][curval] + 1 < dist[nextcol][nextval]:
                        dist[nextcol][nextval] = dist[curcol][curval] + 1
                        if result[nextval] == -1 or dist[nextcol][nextval] < result[nextval]:
                            result[nextval] = dist[nextcol][nextval]
                            #print result
                        queue.append((nextval, nextcol))
            
        return result
        
        
        
        
            
            
        