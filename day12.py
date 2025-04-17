class Solution:
    def maxNtype(self , arr):
        #code here.
        n = len(arr)
        a_breaks = 0
        d_breaks = 0
        
        for i in range(n-1):
            if arr[i] > arr[(i+1) % n]:
                a_breaks += 1
            if arr[i] < arr[(i+1) % n]:
                d_breaks += 1
        
        
        
        if(a_breaks == 0):
            return 1
        elif(d_breaks == 0):
            return 2
        elif(a_breaks == 1 and arr[0] > arr[-1]):
            return 4
        elif(d_breaks == 1 and arr[0] < arr[-1]):
            return 3
