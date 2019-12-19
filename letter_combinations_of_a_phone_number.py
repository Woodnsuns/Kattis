class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_letter = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        
        def expand(l1, l2):
            result = []
            if len(l1) <= 0:
                return l2
            if len(l2) <= 0:
                return l1
            for s1 in l1:
                for s2 in l2:
                    result.append(s1 + s2)
            return result
        
        product = []
        for i in range(len(digits)):
            product = expand(product, num_to_letter[int(digits[i])])
        return product