class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = dict()
        for i, val in enumerate(A):
            index[val] = i
        
        longest = collections.defaultdict(lambda: 2)
        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = -1
                if z - A[j] in index:
                    i = index[z - A[j]]
                if i != -1 and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0
                
        