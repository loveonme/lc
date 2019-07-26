class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        a = 1
        while n > a:
            a  = a*3
        if n == a:
            return True
        return False
        '''
        left = 0
        while n >= 3 :
            left = n%3
            n /= 3
        if n 
        '''

        '''
        n <= 0 false
        n = 1 /3=0 %3=1 true
        n =2 /3=0 %3=2 false 
        n = 3 /3=1 %3=0 true
        n = 4 /3=1 %3=1 false
        n = 5 /3=2 %3=2 false
        n = 6 /3=2 %3=0 false
        n = 7 /3=2 %3=1 false
        n = 8 /3=2 %3=2 false
        n = 9 /3=3 %3=0 true
        '''