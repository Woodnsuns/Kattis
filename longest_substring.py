class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strlen = len(s)        
        if len(s) <= 1:
            return s
        dp = [[0 for x in range(strlen)] for y in range(strlen)]

        for i in range(strlen):
            dp[i][i] = 1
            
        maxlen = 0
        maxsub = s[0]    

        
        for span in range(1, strlen):
            for head in range(0, strlen - span):
                #print(strlen - 1 - span)
                tail = head + span
                #print("span = {}, head = {}, tail = {}".format(span, head, tail))
            
                if span > 1 and dp[head + 1][tail - 1] == 0:
                    dp[head][tail] = 0
                else:
                    if s[head] == s[tail]:
                        dp[head][tail] = 1
                        if span > maxlen:
                            maxsub = s[head:tail+1]
        if len(maxsub) == 0:
            return s[0]
        return maxsub

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().longestPalindrome(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()