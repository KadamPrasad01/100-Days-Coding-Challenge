class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        my_set = set(nums)
        if(len(my_set) == n):
            return False
        else:
            return True
        
