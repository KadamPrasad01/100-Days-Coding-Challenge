class Solution:
    def getAlternates(self, arr):
        # Code Here
        arr2 = []
        for i in range(len(arr)):
            if(i%2 == 0):
                arr2.append(arr[i])
        return arr2
--------------------------------------------------
def isPalinArray(arr):
    # Code here
    for ele in arr:
        ele = str(ele)
        rev = ele[::-1]
        if(ele != rev):
            return False
            break
    return True
-------------------------------------------------

class Solution:
    def leftRotate(self, arr, d):
        # code here
        d = d % len(arr)
        rotated = arr[d:] + arr[:d]
        arr[:] = rotated
        return arr
        
-----------------------------------------------

class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        idx = -1
        for i in range(len(s)):
            if(s[i] == "1"):
                idx = i
        return idx
-----------------------------------------------
from collections import Counter
class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        count = Counter(arr)
        cx = count[x]
        cy = count[y]
        if(cx>cy):
            return x
        elif(cy>cx):
            return y
        else:
            return min(x,y)
---------------------------------------------------
class Solution:
    def convertFive(self, n):
        # Code here
        s = str(n)
        result = ""
        for i in range(len(s)):
            if(s[i] == "0"):
                result += "5"
            else:
                result += s[i]
        return int(result)
