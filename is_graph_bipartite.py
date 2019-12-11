class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        grps = {}
        visited = [0 for i in range(len(graph))]
        s = -1
        if len(graph) <= 2:
            return True
        
        for i in range(len(graph)):
            if i not in grps:
                grps[i] = -1
            stack = [i]
            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = 1
                while graph[node]:
                    neighbor = graph[node].pop(0)
                    if neighbor in grps and grps[neighbor] == grps[node]:
                        return False
                    if neighbor not in grps:
                        grps[neighbor] = grps[node] * (-1)
                    if not visited[neighbor]:
                        stack.append(neighbor)
              
        return True
    
            
                