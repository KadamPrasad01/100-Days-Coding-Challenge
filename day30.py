class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        count = Counter(nums)
        for num in count:
            if(count[num] == 1):
                sum+=num
        return sum
