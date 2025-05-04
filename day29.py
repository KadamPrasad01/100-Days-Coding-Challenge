class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            count = len(str(i))
            if(count % 2 == 0):
                result +=1
        return result
        
