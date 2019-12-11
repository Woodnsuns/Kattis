from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dtoa = defaultdict(list)
        itin = []
        visited = dict()
        for ticket in tickets:
            dtoa[ticket[0]].append(ticket[1])
        
        for dep in dtoa.keys():
            dtoa[dep].sort()
            
        def dfs(dep, dtoa):
            # print dep
            # print dtoa[dep]
            while dtoa[dep]:
                dest = dtoa[dep].pop(0)
                dfs(dest, dtoa)
                itin.append(dest)
        
        dfs("JFK", dtoa)
        result = ["JFK"]
        while itin:
            result.append(itin.pop())
        return result
        
                    
                     
                    
            
        