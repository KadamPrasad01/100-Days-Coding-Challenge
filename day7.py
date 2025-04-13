from typing import List


class Solution:
    def largest(self, arr):
        # code here
        arr.sort()
        largest = arr[len(arr)-1]
        return largest
-------------------------------------------------------------
class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i in range(len(arr)):
            if(arr[i] == x):
                return i
                break
        return -1
------------------------------------------------------------
class Solution:
    def get_min_max(self, arr):
        arr.sort()
        min = arr[0]
        max = arr[len(arr) - 1]
        return min,max
-----------------------------------------------------------
class Solution:
    def rotate(self, arr):
       
        last = arr.pop()
        arr.insert(0,last)
        return arr
----------------------------------------------------------
class Solution:
    def minAnd2ndMin(self, arr):
        #code here
        arr.sort()
        smallest = arr[0]
        
        for i in range(1,len(arr)):
            
            if(arr[i] > smallest):
                second_smallest = arr[i]
                return smallest,second_smallest
        return (-1,)
