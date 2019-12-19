class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = set()
        def addParenthesis(n1, n2, route):
            if n1 == 0 and n2 == 1:
                route += ')'
                result.add(route)
            if n2 >= n1:
                if n1 > 0:
                    addParenthesis(n1-1, n2, route + '(')
                if n2 > n1 and n1 < n:
                    addParenthesis(n1, n2-1, route + ')')
        
        if n == 0:
            result.add("")
            return result
        if n == 1:
            result.add("()")
            return result
    
        addParenthesis(n, n, '')
        return result
                    
                    