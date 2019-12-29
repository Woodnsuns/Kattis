class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        if n == 1:
            return [0]
        if n % 2 == 0:
            sign = 1
            for k in range(1, n/2 + 1):
                result.append(k)
                result.append((-1) * k)
        else:
            sign = 1
            
            for k in range(2, n/2 + 1):
                result.append(k)
                result.append((-1) * k)
            result.append(-1)
            k = n/2 + 1
            result.append((-1) * k)
            result.append(abs(k + 1))
        return result