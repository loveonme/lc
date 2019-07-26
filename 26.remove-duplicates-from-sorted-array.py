class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        cur = length - 1 
        if length == 1:
            return 1
        for i in range(1,length):
            if nums[length - i -1] == nums[cur]:
                del nums[cur]
            cur -= 1
        return len(nums)


        
