class Solution(object):
    def numOfBurgers(self, t, c):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        l, h = 0, c
        if t == c == 0:
            return [0, 0]
        while l <= h:
            s = (l + h) / 2
            j = c - s
            if 4*j + 2*s > t:
                l = s + 1
            if 4*j + 2*s < t:
                h = s - 1
            if 4*j + 2*s == t:
                return [j, s]
            
        return []