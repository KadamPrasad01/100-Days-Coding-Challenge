class Solution:
    def getSecondLargest(self, arr):
        sec_largest = -1
        arr.sort()
        size = len(arr)
        largest = arr[size-1]
        
        for i in range(size-2,-1,-1):
            if(arr[i] != largest):
                sec_largest = arr[i]
                break
        return sec_largest
