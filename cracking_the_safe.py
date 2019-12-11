class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = set()
        ans = []
        
        def dfs(node):
            for i in map(str, range(k)):
                nei = node + i
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei[1:])
                    ans.append(i)
        dfs("0"*(n-1))
        return  "".join(ans) + "0" * (n-1)
        