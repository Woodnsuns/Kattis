class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        goals = set()
        for i, num in enumerate(arr):
            if num == 0:
                goals.add(i)
                
        n = len(arr)
        memo = set()
        def dfs(cur):
            if cur in memo or cur >= n or cur < 0:
                return False
            memo.add(cur)
            #print memo
            if cur + arr[cur] in goals or cur - arr[cur] in goals:
                #print("found goal!")
                return True
            return dfs(cur + arr[cur]) or dfs(cur - arr[cur])
        
        return dfs(start)