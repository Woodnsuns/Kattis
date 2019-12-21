class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        def generate(input):
            if len(input) == 1:
                return [int(input)]
            
            result = []
            found = False
            for i, c in enumerate(input):
                
                if c == "+" or c == "-" or c == "*":
                    found = True
                    left = generate(input[:i])
                    right = generate(input[i+1:])
                    for l in left:
                        for r in right:
                            if c == "+":
                                result.append(l + r)
                            if c == "-":
                                result.append(l - r)
                            if c == "*":
                                result.append(l * r)
            if not found:
                return [int(input)]
            return result
        return generate(input)
        
                    
                    
                    
        