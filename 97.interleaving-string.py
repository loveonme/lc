class Solution(object):
    def isInterleave(self, s1, s2, s3):
        '''
        a aa,b bb,a babab
        注意[[False]*3]*4，不可以这样初始化，会导致内存复用，改一个值会修改一大排，导致结果错误
        ''' 
        if len(s1) + len(s2) != len(s3):
            return False
        #dp = [[False]*(len(s1)+1)]*(len(s2)+1)
        dp = []
        for i in range(len(s2)+1):
            res = []
            for j in range(len(s1)+1):
                res.append(False)
            dp.append(res)

        dp[0][0] = True
        print dp
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                dp[i+1][0] = True
        for i in range(len(s2)):
            if s2[i] == s3[i]:
                dp[0][j+1] = True        
        print dp
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i - 1] == s3[i+j-2]) or (dp[i][j-1] and s2[j - 1] == s3[i+j-2])
                print dp[i-1][j],dp[i][j],dp[i][j-1]
        print dp
        return dp[len(s1)][len(s2)]





    def isInterleave_v1(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        这个递归法是对的，但有2个case过不了，只有中国版有这个要求，会超时
        """
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if s1[0] == s3[0]:
            if s2[0] != s3[0]:
                return self.isInterleave(s1[1:],s2,s3[1:])
            else:
                return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
        else:
            if s2[0] != s3[0]:
                return False
            else:
                return self.isInterleave(s1,s2[1:],s3[1:]) 
        return True
