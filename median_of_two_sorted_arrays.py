class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        A, B = nums1, nums2
        if m > n:
            m = len(nums2)
            n = len(nums1)
            A, B = nums2, nums1
        
        
        l, r, half = 0, m, (m + n + 1) // 2
        while l <= r:
            i = (l + r) // 2
            j = half - i
            if i < m and B[j - 1] > A[i]:
                l = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                r = i - 1
            else:
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                
                if (m + n) % 2 != 0:
                    return max_of_left
                
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                    
                #print("max_of_left = {}, min_of_right = {}".format(max_of_left, min_of_right))
                
                return (max_of_left + min_of_right) / 2.0
                
        
        
        