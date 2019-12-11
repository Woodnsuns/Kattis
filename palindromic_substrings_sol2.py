class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        def countsub(i, j, s):
            total = 0
            if s[i] == s[j]:
                head = i-1
                tail = j+1
                total += 1
                while head >= 0 and tail <= len(s)-1:
                    if s[head] == s[tail]:
                        total += 1
                        head -=1
                        tail += 1
                    else:break
            return total
        
        for i in range(len(s)):
            total += countsub(i, i, s)
            if i < len(s)-1:
                total += countsub(i, i+1, s)
        return total
        
            
                
                
        