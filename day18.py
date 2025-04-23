class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = []
        for i in range(len(nums)):
            if(nums[i] == target):
                idx.append(i)
        if(len(idx) == 0):
            return [-1,-1]
        else:
             return [idx[0], idx[-1]]
