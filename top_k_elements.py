class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        curmax = 0
        result = []
        
        return heapq.nlargest(k, counts.keys(), key=counts.get)
        
                