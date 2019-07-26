'''
这里没有坑，没有最后的标点符号，要注意的只是最后可能有空格，要把空格先处理掉
不可以装太复杂的库，只能用python基本库来解决问题
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
