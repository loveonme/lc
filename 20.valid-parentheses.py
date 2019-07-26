'''
原来list直接皆可以当做stack来使用的,append如，pop出
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {"(":")","{":"}","[":"]"}
        length = len(s)
        if length % 2 != 0:
            return False
        if length == 0:
            return True
        stack = []
        for i in range(length):
            if s[i] in pair.keys():
                stack.append(s[i])
            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if s[i] != pair[top]:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False 


