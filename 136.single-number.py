class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if i % 2 == 0:
                a += nums[i]
            elif i%2 == 1:
                a -= nums[i]
                if a != 0:
                    return nums[i - 1]
        return nums[-1]
