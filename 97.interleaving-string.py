class Solution(object):
    def isInterleave_v1(self, s1, s2, s3):
        '''
        aaa,bbb,ababab
        
        '''






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
