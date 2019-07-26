class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new_str = list(str)
        for i in range(len(new_str)):
            if new_str[i]>= 'A' and new_str[i] <= 'Z':
                new_str[i] = chr(ord(new_str[i])+32)
        new_str = ''.join(new_str)
        return new_str 

        
