class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_to_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def getCombinations(s, low, high):
            if high - low < 0:
                result.append(s)
            else:
                l = num_to_letter[digits[low]]
                for c in l:
                    getCombinations(s + c, low+1, high)
        if len(digits) <= 0:
            return []
        high = len(digits) - 1
        result = []
        getCombinations('', 0, high)
        return result