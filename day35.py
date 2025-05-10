class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = []
        arr[:] = nums1 + nums2
        arr.sort()
        length = len(arr)
        if(length % 2 == 0):
            mid = length // 2
            sum = arr[mid] + arr[mid - 1]
            return sum/2.0
        else:
            mid = length // 2
            return arr[mid]


        
