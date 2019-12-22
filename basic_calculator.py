class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def evaluate_stack(stack):
            res = stack.pop()
            while stack:
                c = stack.pop()
                if c == ")":
                    break
                elif c == "+":
                    c = stack.pop()
                    res += c
                elif c == "-":
                    c = stack.pop()
                    res -= c
                else:
                    res += c
            return res
                
        
        i = len(s) - 1
        stack = list()
        sign = 1
        res = 0
        n = 0
        num = 0
        while i >= 0:
            
            if s[i].isdigit():
                num += (10 ** n * int(s[i]))
                n += 1
            elif  s[i] != " ":
                if n:
                    stack.append(num)
                    num, n = 0, 0
                if s[i] != "(":
                    stack.append(s[i])
                if s[i] == "(":
                    res = evaluate_stack(stack)
                    stack.append(res)
            i -= 1
        if n:
            stack.append(num)
    
        return evaluate_stack(stack)
                
            
            
                
                
            
        