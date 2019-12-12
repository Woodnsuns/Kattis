class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        min_sum = -1
        max_sum = 0
        for num in nums:
            if min_sum == -1:
                min_sum = num
            elif num > min_sum:
                min_sum = num
            max_sum += num
        mid = (min_sum + max_sum) / 2

        while (max_sum > min_sum):
            #print mid
            n = len(nums)
            mcount = 1
            cursum = 0
            max_cursum = 0
            for num in nums:
                if cursum + num > mid:
                    cursum = num
                    mcount += 1
                    if mcount > m:
                        break
                else:
                    cursum += num
                n -= 1
                if cursum > max_cursum: max_cursum = cursum
                #print("cursum = {}, num = {}".format(cursum, num))
            if n > 0:
                #print ("n = {}, mid = {}, max = {}".format(n, mid, max_sum))
                mid += 1
                min_sum = mid
                mid = (mid + max_sum) / 2
            if n <= 0:
                #print("mid = {}, min = {}, max_cursum = {}".format(mid, min_sum, max_cursum))
                if mid > max_cursum:
                    mid -= 1
                max_sum = mid
                mid = (min_sum + mid) / 2
                
        return mid
            
            
        