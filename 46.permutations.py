class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) == 1:
            return [nums]
        for num in nums:
            nums_new = copy.deepcopy(nums)
            nums_new.remove(num)
            ret_subs = self.permute(nums_new)      
            for sub in ret_subs:
                res = [num]
                res.extend(sub)
                ret.append(res)
        return ret

