class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left  = 0 
        right = n -1
        while(left<=right):
            mid = (left + right) // 2
            if(nums[mid] == target):
                return mid
            elif(target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return left
-------------------------------------------
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            if(nums[i] == target):
                return True
        return False
-------------------------------------------
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if(nums[i] == target):
                return i
        return -1
-------------------------------------------
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
-------------------------------------------
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n == 1):
            return 0
        for i in range(n):
            if(i == 0):
                if(nums[i] > nums[i+1]):
                    return i
            elif(i == n - 1):
                if(nums[i] > nums[i-1]):
                    return i
            else:
                if(nums[i] > nums[i-1] and nums[i] > nums[i+1]):
                    return i
-------------------------------------------
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n == 1):
            return nums[0]
        for i in range(len(nums)):
            if(i == 0):
                if(nums[i] != nums[i+1]):
                    return nums[i]
            elif(i == n - 1):
                if(nums[i] != nums[i-1]):
                    return nums[i]
            else:
                if(nums[i] != nums[i-1] and nums[i] != nums[i+1]):
                    return nums[i]
