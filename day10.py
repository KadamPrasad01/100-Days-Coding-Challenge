class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        half = len(arr) // 2
        lsum = 0
        rsum = 0
        for i in range(0,half):
            lsum+= arr[i]
        for i in range(half,len(arr)):
            rsum+= arr[i]
        if(lsum > rsum or rsum > lsum):
            diff = max(lsum,rsum) - min(lsum,rsum)
        return diff
--------------------------------------------------------------------
class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        # code here
        maxi = max(arr1)
        mini = min(arr2)
        
        result = maxi * mini
        return result
------------------------------------------------------------------
def maximumAdjacent(sizeOfArray, arr):
    
    # Your code here
    # Function should print max of all adjacents
    result = []
    for i in range(sizeOfArray -1):
        print(max(arr[i],arr[i+1]),end=" ")
-------------------------------------------------------------------
class Solution:
    def maxDays(self, arr):
        # code here
        return max(arr)
---------------------------------------------------------------
class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        left = 0
        right = len(arr) - 1
        arr2 = []
        
        while(left<=right):
            if(left!=right):
                arr2.append(arr[right])
                arr2.append(arr[left])
            else:
                arr2.append(arr[left])
            left+=1
            right-=1
        return arr2
