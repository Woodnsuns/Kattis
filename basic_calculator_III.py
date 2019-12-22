class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def evaluate_stack(stack):
            res = 0
            num = 0
            while stack:
                c = stack.pop()
                if c == ")":
                    break
                elif c == "+":
                    res += num
                    num = stack.pop()
                elif c == "-":
                    res += num
                    num = (-1) * stack.pop()
                elif c == "*":
                    num *= stack.pop()
                elif c == "/":
                    #print num
                    if num < 0:
                        num = ((-1) * num / stack.pop()) * (-1)
                    else: num /= stack.pop()
                    #print num
                else:
                    num = c
            return res + num
                
        
        i = len(s) - 1
        stack = list()
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
                
            
            
                
                
            
        