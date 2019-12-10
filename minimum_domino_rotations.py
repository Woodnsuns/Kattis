class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) != len(B):
            return -1
        
        
        targets = [A[0], B[0]]
        for target in targets:
            noway = False
            acount = 0
            bcount = 0
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    noway = True
                    break
                if A[i] == target: 
                    acount += 1
                if B[i] == target:
                    bcount += 1
            if not noway:
                return len(A) - max(acount, bcount)
        
                
            
        return -1
                
            
            
            
        