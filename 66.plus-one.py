class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            i = length -1 
            while i  >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
                if i == 0:
                    digits = [1]+digits
                i -= 1
        return digits


